#!/usr/bin/env python3
"""Fetch a YouTube transcript from a URL or video ID.

Usage:
    python3 fetch_transcript.py <URL_OR_VIDEO_ID> [LANG_CODE]

Behaviour:
    - Extracts the 11-character video ID from any common YouTube URL form
      (watch, youtu.be, embed, live, shorts) or accepts a bare video ID.
    - Fetches the transcript via `youtube-transcript-api`, preferring a native
      (non-translated) track and honouring an optional language preference.
    - Prints a small metadata header (TITLE / LANG / VIDEO_ID / CHARS / LINES).
    - SHORT transcripts are printed inline to stdout after the header.
    - LONG transcripts (over INLINE_LIMIT chars) are written to a file and the
      script prints `TRANSCRIPT_FILE: <absolute path>` instead of the body, so
      the caller can read the file in batches.

All errors are emitted as a single `ERROR:<CODE> <message>` line and exit 1.
No third-party network code is fetched at runtime — the only outbound calls are
to YouTube (transcript fetch + a lightweight title scrape).
"""
import argparse
import os
import re
import sys
import tempfile
import urllib.request
from urllib.parse import parse_qs, urlparse

# Transcripts longer than this many characters are written to a file instead of
# printed inline. Override with the TRANSCRIPT_INLINE_LIMIT environment variable.
INLINE_LIMIT = int(os.environ.get("TRANSCRIPT_INLINE_LIMIT", "15000"))

VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com"}
YOUTUBE_SHORT_HOSTS = {"youtu.be", "www.youtu.be"}

# Friendly language names → ISO codes. Unknown values pass through unchanged;
# youtube-transcript-api emits its own warning if the code is unavailable.
LANGUAGE_MAP = {
    "english": "en", "spanish": "es", "french": "fr", "german": "de",
    "japanese": "ja", "portuguese": "pt", "italian": "it",
    "chinese": "zh", "korean": "ko", "russian": "ru", "hindi": "hi",
    "arabic": "ar", "dutch": "nl",
}


def extract_video_id(raw):
    """Return the 11-char video ID, or None if it cannot be parsed."""
    raw = raw.strip()
    if VIDEO_ID_RE.fullmatch(raw):
        return raw

    if not raw.startswith(("http://", "https://")):
        raw = "https://" + raw.lstrip("/")

    parsed = urlparse(raw)
    host = parsed.netloc.lower()

    if host in YOUTUBE_SHORT_HOSTS:
        candidate = parsed.path.strip("/").split("/", 1)[0]
    elif host in YOUTUBE_HOSTS:
        if parsed.path == "/watch":
            candidate = (parse_qs(parsed.query).get("v") or [""])[0]
        elif parsed.path.startswith(("/embed/", "/live/", "/shorts/")):
            parts = parsed.path.strip("/").split("/", 2)
            candidate = parts[1] if len(parts) >= 2 else ""
        else:
            return None
    else:
        return None

    return candidate if VIDEO_ID_RE.fullmatch(candidate) else None


def map_language(raw):
    raw = (raw or "").strip().lower()
    return LANGUAGE_MAP.get(raw, raw)


def fetch_title(video_id):
    """Best-effort title scrape. Returns "" on any failure."""
    try:
        req = urllib.request.Request(
            f"https://www.youtube.com/watch?v={video_id}",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        m = re.search(r"<title>([^<]+)</title>", html)
        if m:
            return m.group(1).replace(" - YouTube", "").strip()
    except Exception:
        pass
    return ""


def select_transcript(tlist, lang_pref):
    """Pick a transcript object, preferring native tracks and lang_pref."""
    warn = None
    if lang_pref:
        for t in tlist:  # 1. native exact match
            if t.language_code == lang_pref and not getattr(t, "is_translation", False):
                return t, warn
        for t in tlist:  # 2. any exact match (incl. translated)
            if t.language_code == lang_pref:
                return t, warn
        for t in tlist:  # 3. native fallback
            if not getattr(t, "is_translation", False):
                warn = f'LANG_WARN: requested "{lang_pref}" unavailable; using {t.language_code}'
                return t, warn
        chosen = next(iter(tlist))
        warn = f'LANG_WARN: requested "{lang_pref}" unavailable; using {chosen.language_code}'
        return chosen, warn

    for t in tlist:  # prefer native (non-translated)
        if not getattr(t, "is_translation", False):
            return t, warn
    return next(iter(tlist)), warn


def format_timestamp(start):
    total_s = int(start)
    h, rem = divmod(total_s, 3600)
    m, s = divmod(rem, 60)
    return f"[{h}:{m:02d}:{s:02d}]" if h > 0 else f"[{m}:{s:02d}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url_or_id")
    parser.add_argument("lang", nargs="?", default="")
    args = parser.parse_args()

    raw = args.url_or_id.strip()
    lang_pref = args.lang
    # Allow "<id> <lang>" passed as a single argument.
    if " " in raw and not lang_pref:
        raw, _, rest = raw.partition(" ")
        lang_pref = rest.strip()

    video_id = extract_video_id(raw)
    if not video_id:
        print(f"ERROR:INVALID_INPUT could not extract a YouTube video id from {raw!r}")
        sys.exit(1)
    lang_pref = map_language(lang_pref)

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("ERROR:LIBRARY_MISSING install with: pip install 'youtube-transcript-api>=0.6.3'")
        sys.exit(1)

    # Defensive imports — class names vary across library versions.
    def _opt(*names):
        try:
            mod = __import__("youtube_transcript_api", fromlist=list(names))
            return tuple(getattr(mod, n, None) for n in names)
        except Exception:
            return tuple(None for _ in names)

    (TranscriptsDisabled, VideoUnavailable, NoTranscriptFound, InvalidVideoId) = _opt(
        "TranscriptsDisabled", "VideoUnavailable", "NoTranscriptFound", "InvalidVideoId")
    (AgeRestricted, IpBlocked, RequestBlocked, YouTubeRequestFailed) = _opt(
        "AgeRestricted", "IpBlocked", "RequestBlocked", "YouTubeRequestFailed")

    try:
        try:
            tlist = YouTubeTranscriptApi().list(video_id)
        except (AttributeError, TypeError):
            tlist = YouTubeTranscriptApi.list_transcripts(video_id)
    except Exception as e:
        error_map = [
            (TranscriptsDisabled,  "CAPTIONS_DISABLED"),
            (AgeRestricted,        "AGE_RESTRICTED"),
            (VideoUnavailable,     "VIDEO_UNAVAILABLE"),
            (InvalidVideoId,       "INVALID_VIDEO_ID"),
            (IpBlocked,            "IP_BLOCKED"),
            (RequestBlocked,       "REQUEST_BLOCKED"),
            (NoTranscriptFound,    "NO_TRANSCRIPT"),
            (YouTubeRequestFailed, "NETWORK_ERROR"),
        ]
        code = "TRANSCRIPT_FETCH_FAILED"
        for cls, mapped in error_map:
            if cls is not None and isinstance(e, cls):
                code = mapped
                break
        print(f"ERROR:{code} {e}")
        sys.exit(1)

    transcript_obj, warn = select_transcript(tlist, lang_pref)

    try:
        segments = transcript_obj.fetch()
    except Exception as e:
        print(f"ERROR:TRANSCRIPT_FETCH_FAILED {type(e).__name__}: {e}")
        sys.exit(1)

    lang = transcript_obj.language_code
    use_dict = bool(segments) and isinstance(segments[0], dict)

    body_lines = []
    for s in segments:
        text = (s["text"] if use_dict else s.text).strip()
        start = s["start"] if use_dict else s.start
        if text:
            body_lines.append(f"{format_timestamp(start)} {text}")
    body = "\n".join(body_lines)

    title = fetch_title(video_id) or f"YouTube video {video_id}"
    url = f"https://www.youtube.com/watch?v={video_id}"

    header = [
        f"TITLE: {title}",
        f"VIDEO_ID: {video_id}",
        f"URL: {url}",
        f"LANG: {lang}",
        f"LINES: {len(body_lines)}",
        f"CHARS: {len(body)}",
    ]
    if warn:
        header.append(warn)

    if len(body) <= INLINE_LIMIT:
        print("\n".join(header))
        print("---TRANSCRIPT---")
        print(body)
    else:
        out_dir = os.path.join(tempfile.gettempdir(), "claude-youtube-transcripts")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"transcript_{video_id}_{lang}.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(header) + "\n---TRANSCRIPT---\n" + body + "\n")
        header.append(f"TRANSCRIPT_FILE: {out_path}")
        print("\n".join(header))


if __name__ == "__main__":
    main()
