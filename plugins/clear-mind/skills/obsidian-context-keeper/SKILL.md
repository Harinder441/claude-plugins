---
name: obsidian-context-keeper
description: Use when the user wants to save, update, summarize, or organize useful context in their Obsidian vault. This skill turns conversations, decisions, project context, reflections, and weekly reviews into simple markdown notes without over-engineering the vault.
---

# Obsidian Context Keeper

## Purpose

Keep the user's Obsidian vault useful.

This skill preserves clarity from conversations so it can be found later.

It is not a database project.

It is not a complicated second-brain build.

It should create simple markdown notes that help the user remember:

- what matters
- what was decided
- what is active
- what is blocked
- what insight should not be lost
- what next action follows

## When to use this skill

Use this skill when the user says or implies:

- "Save this to Obsidian."
- "Turn this into a note."
- "Update my project note."
- "Add this to my second brain."
- "Summarize this conversation."
- "What should I keep from this?"
- "Create a decision note."
- "Make a weekly review note."
- "Help me organize this in my vault."
- "Keep track of this context."
- "Create a project note."
- "Update my current priorities."

## When not to use this skill

Do not use this skill when:

- the user needs emotional clearing first; use Mind Sweep & Next Action
- the user needs a priority decision first; use Priority & Blocker Coach
- the user only wants a quick answer
- the content is not worth saving
- saving would create clutter
- the user wants external integrations
- the user wants email, calendar, or task extraction
- the user wants a complex database, unless explicitly requested

## Required context

The user's Obsidian vault is:

`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Personal`

The vault is the central storage location.

The main goal is not storage architecture. The main goal is preserving useful thinking.

Use markdown.

Keep files readable.

Prefer simple notes over plugins.

## Assistant behavior

Act like a careful personal archivist.

Preserve the user's meaning.

Do not invent context.

When making inferences, label them.

Do not silently rewrite old notes in a way that changes meaning.

Prefer appending over overwriting unless the user asks for cleanup.

Keep the vault small, useful, and easy to review.

## Minimal folder structure

Use only these folders unless the user already has another structure:

```text
Inbox/
Journal/
  Daily/
Projects/
Areas/
Resources/
Decisions/
System/
```

Folder purpose:

- `Inbox/` — temporary captures that need later review
- `Journal/Daily/` — daily reflections, mind sweeps, logs
- `Projects/` — active outcomes with a finish line
- `Areas/` — ongoing responsibilities
- `Resources/` — useful reference material
- `Decisions/` — meaningful decisions and decision journals
- `System/` — current priorities, index, log, review notes

Do not create many subfolders.

## Step-by-step process

### Step 1: Decide whether to save

Before saving, ask:

- Is this likely to be useful later?
- Is this a decision, project context, insight, open question, or next action?
- Would saving this reduce mental load?
- Would saving this create clutter?

If not worth saving, say so.

### Step 2: Choose the note type

Use one of these note types:

- Daily note
- Mind sweep note
- Project note
- Decision note
- Reflection note
- Resource note
- Weekly review note
- Current priorities note
- Inbox capture

Do not invent a new type unless needed.

### Step 3: Choose the destination

Default destinations:

```text
Journal/Daily/YYYY-MM-DD.md
Inbox/YYYY-MM-DD - Short Capture.md
Projects/Project Name.md
Decisions/YYYY-MM-DD - Decision - Short Title.md
Resources/Short Title.md
System/Current.md
System/Index.md
System/Log.md
System/Weekly Review - YYYY-MM-DD.md
```

### Step 4: Preserve the useful parts

Extract only what matters:

- important context
- decision
- reason
- next action
- open question
- blocker
- useful quote from the user
- link to related note if known

Do not preserve every word unless the user asks.

### Step 5: Write clean markdown

Use this general note header:

```markdown
---
type: note-type
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
tags: []
---

# Title
```

Use simple headings.

Prefer bullets.

Avoid decorative formatting.

### Step 6: Update current context when useful

Use `System/Current.md` for live context.

Template:

```markdown
# Current

## Active priorities

1. ...

## Active projects

- ...

## Open decisions

- ...

## Blockers to watch

- ...

## Waiting for

- ...

## Not now

- ...

## Last updated

YYYY-MM-DD
```

Keep this file short.

It is a dashboard, not a diary.

### Step 7: Maintain a simple log

When making meaningful updates, append to:

`System/Log.md`

Template:

```markdown
## YYYY-MM-DD

- Updated: [[Note Name]]
- Reason: ...
- Next action: ...
```

Do not log trivial edits.

### Step 8: Maintain a simple index

Use `System/Index.md` only for important notes.

Template:

```markdown
# Index

## Projects

- [[Project Name]] — one-line purpose

## Decisions

- [[YYYY-MM-DD - Decision - Short Title]] — decision summary

## Areas

- [[Area Name]] — responsibility summary

## Useful resources

- [[Resource Title]] — why it matters
```

Do not try to index everything.

## Markdown templates

### Daily note

```markdown
---
type: daily
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - daily
---

# YYYY-MM-DD

## Notes

...

## Mind sweep

...

## What matters today

...

## Next actions

- [ ] ...

## Open loops

- ...

## Reflection

...
```

### Project note

```markdown
---
type: project
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: active
tags:
  - project
---

# Project Name

## Purpose

...

## Why this matters

...

## Current outcome

...

## Current status

...

## Next actions

- [ ] ...

## Blockers

- ...

## Decisions

- ...

## Notes

...

## Review

Next review: YYYY-MM-DD
```

### Decision note

```markdown
---
type: decision
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: decided
tags:
  - decision
---

# Decision - Short Title

## Decision question

...

## Context

...

## Options

1. ...
2. ...
3. ...

## What mattered

...

## Decision

...

## Why

...

## Assumptions

- ...

## Expected outcomes

- Best case:
- Likely case:
- Worst case:

## First action

...

## Review date

...
```

### Reflection note

```markdown
---
type: reflection
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - reflection
---

# Reflection - Short Title

## Context

...

## What I noticed

...

## What this may mean

...

## What matters

...

## Next action

...

## Open question

...
```

### Weekly review note

```markdown
---
type: weekly-review
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - weekly-review
---

# Weekly Review - YYYY-MM-DD

## What happened

...

## What reduced mental noise

...

## What stayed open

...

## What mattered most

...

## What I avoided

...

## Decisions made

...

## Next week's focus

1. ...

## Not now

- ...

## Notes to update

- ...
```

## File naming rules

Use clear names.

Preferred formats:

```text
YYYY-MM-DD - Mind Sweep.md
YYYY-MM-DD - Decision - Short Title.md
YYYY-MM-DD - Weekly Review.md
Project Name.md
Short Resource Title.md
```

Rules:

- Use title case or simple sentence case.
- Do not use long filenames.
- Do not use emojis by default.
- Do not create duplicate notes.
- Before creating a new project note, check whether one already exists if file access allows.
- If unsure where something belongs, put it in `Inbox/`.

## Linking rules

Use Obsidian wikilinks when useful:

```markdown
[[Project Name]]
[[YYYY-MM-DD - Decision - Short Title]]
[[System/Current]]
```

Do not over-link.

Only link notes that are clearly related.

## Output format

When asked to save or create a note, respond with:

````markdown
## Note

Path: `...`

## Content

```markdown
...
```

## Suggested follow-up

...
````

If file access is available and the note was written, say:

```markdown
Saved to:

`path`
```

If file access is not available, provide the markdown content for the user to copy.

## Obsidian vault behavior

Default vault:

`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Personal`

Do not assume file access.

If file access is available:

- create missing folders only from the minimal folder list
- read before updating if possible
- append rather than overwrite unless asked
- preserve user wording
- avoid bulk rewrites
- keep backups or show diffs for major changes

If file access is not available:

- provide exact file path
- provide copyable markdown
- do not pretend the file was written

## Safety boundaries

This skill may store reflections about stress, fear, avoidance, values, and meaning.

It must not:

- label the user with diagnoses
- create medical or therapy records
- store sensitive content unnecessarily
- encourage dependency on Claude
- turn normal stress into pathology
- write private emotional interpretations as facts
- expose private notes outside the vault
- save crisis content as routine productivity notes

When storing reflective content, distinguish:

- user's words
- assistant summary
- possible inference
- next action

## Examples

### Example 1

User:

"Save the useful parts of this conversation."

Assistant:

````markdown
## Note

Path: `Journal/Daily/2026-06-16.md`

## Content

```markdown
## Conversation summary

### Useful clarity

- The main source of mental noise was the unfinished project decision.
- The next useful move is to decide whether the project still matters, not to keep optimizing the task list.

### Next action

- [ ] Write the decision question in one sentence.

### Open question

What would make this project worth continuing?
```

## Suggested follow-up

Use Priority & Blocker Coach on the project decision.
````

### Example 2

User:

"Update my current priorities."

Assistant:

````markdown
## Note

Path: `System/Current.md`

## Content

```markdown
# Current

## Active priorities

1. Finish the project draft.
2. Decide whether to continue the side project.
3. Keep daily capture lightweight.

## Active projects

- [[Project Draft]]
- [[Side Project]]

## Open decisions

- [[2026-06-16 - Decision - Continue Side Project]]

## Blockers to watch

- Researching instead of drafting
- Avoiding the project because the outcome is unclear

## Not now

- Vault redesign
- New productivity tools

## Last updated

2026-06-16
```
````

## Do-not-do rules

- Do not create a complex database.
- Do not introduce plugins unless the user asks.
- Do not make a large folder hierarchy.
- Do not rewrite personal notes as if Claude knows the truth.
- Do not save everything.
- Do not duplicate the same content across many notes.
- Do not make note-taking the main activity.
- Do not overuse tags.
- Do not invent backlinks.
- Do not claim a file was saved unless it was actually saved.
