# clear-text

Clean up dictated text and prompts on command — without changing your tone or intent.

Built for voice dictation: the transcript comes out with filler words, duplicated
sentences, stray punctuation, grammar slips, and the occasional mishear (the wrong word
transcribed). These skills tidy that up so the result reads like *you* wrote it carefully,
not like it was rewritten by someone else.

## Skills

| Trigger | What it does |
|---|---|
| **clear my words** | Cleans dictated prose: fixes grammar/punctuation, removes filler and buzzwords, drops duplicated words/sentences, repairs obvious mishears. Keeps your tone, structure, and roughly the same length. No summarizing. |
| **clear my prompt** | Treats the text as a *prompt/instruction*. Does everything above, then drops tangents irrelevant to the request's core intent — leaving a tightened prompt with the same intent and tone. |
| **clear my prompt and concise** | Same as *clear my prompt*, then condenses further: rewrites and merges sentences/paragraphs to the minimum that conveys the same intent, still in your voice. |

## How to use

Dictate the text in the **same message** as the trigger, e.g.:

```
clear my words so basically um I think we should like maybe ship the thing the thing on friday
```

→ returns just the cleaned text, ready to copy.

If you type a trigger on its own, it falls back to cleaning your previous message.

## How it works

The three triggers are thin entry skills. Each forwards your text to an isolated
**`text-cleaner` subagent** running on **Haiku 4.5**, which loads the `text-cleaning-rules`
worker skill and returns only the cleaned text.

Running the cleanup in a subagent means it never inherits the surrounding conversation —
it only ever sees the text you hand it, so it can't get confused by unrelated context, and
the main session stays clean. The subagent treats your text strictly as **data to clean**,
never as instructions to follow (important for prompt cleanup, where the text itself
contains commands).
