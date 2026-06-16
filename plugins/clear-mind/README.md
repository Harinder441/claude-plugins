# Clear Mind

A Claude Code plugin with three reflection skills that help you clear your head, decide what matters, and preserve useful context in Obsidian. Conversation-first — markdown notes are optional and lightweight.

The design follows one rule: **conversation first, clarity second, markdown third.**

## Skills

| Skill | Use when you want to… |
|-------|------------------------|
| [mind-sweep-next-action](skills/mind-sweep-next-action) | Clear your head, reduce mental noise, unload stress, and turn scattered thoughts into a few concrete next actions. |
| [priority-blocker-coach](skills/priority-blocker-coach) | Decide what matters, face avoidance, examine blockers, work through a meaningful decision, or set a weekly focus. |
| [obsidian-context-keeper](skills/obsidian-context-keeper) | Save, update, or summarize useful context into simple Obsidian markdown notes without over-engineering the vault. |

## How they fit together

1. **Empty the mind** — `mind-sweep-next-action` (used most often).
2. **Choose what matters** — `priority-blocker-coach` (when there's a real choice, avoidance, or confusion).
3. **Preserve useful context** — `obsidian-context-keeper` (only when something is worth saving).

## Obsidian vault

The skills assume an Obsidian vault at:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Personal
```

They never write unless saving is clearly useful and you ask. If file access is unavailable, they hand back copyable markdown instead. They prefer a small folder set (`Inbox/`, `Journal/Daily/`, `Projects/`, `Areas/`, `Resources/`, `Decisions/`, `System/`) over plugins or databases.

## Safety boundaries

These skills are reflective assistants and coaches — **not** therapy. They will not diagnose, treat mental illness, interpret your past as trauma, or encourage dependency. If you describe immediate danger or self-harm intent, they stop the coaching workflow and point you toward immediate human support.

## Installation

Add the marketplace, then install the plugin:

```
/plugin marketplace add Harinder441/claude-plugins
/plugin install clear-mind@harinder-plugins
```
