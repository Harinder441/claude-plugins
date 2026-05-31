# google-workspace

Personal Google-ecosystem skills for Claude Code.

## Skills

### `youtube-transcript`

Fetches the transcript (captions) of a YouTube video from a URL or bare video
ID. Activates automatically when you share a YouTube link and ask for its
transcript, captions, or spoken text; supports an optional language preference.

Short transcripts are returned inline; long ones are written to a temp file and
the path is reported so Claude can read it in batches.

**Requirement:** the Python package `youtube-transcript-api` (>=0.6.3):

```
pip install 'youtube-transcript-api>=0.6.3'
```

See [`requirements.txt`](./requirements.txt).
