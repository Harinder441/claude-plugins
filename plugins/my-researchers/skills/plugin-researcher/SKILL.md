---
name: plugin-researcher
description: >
  This skill should be used when the user asks to "find Claude Code plugins",
  "search for Claude Code plugins on GitHub", "find plugins on Twitter",
  "what Claude Code plugins exist", "find community plugins for Claude Code",
  "are there any Claude Code plugins for testing" (or other domains),
  "research Claude Code extensions", or wants to discover third-party
  Claude Code plugins and extensions available publicly.
version: 0.1.0
---

# Claude Code Plugin Researcher

## Purpose

Research and discover Claude Code plugins across GitHub and Twitter/X. Focus exclusively on these two sources where the Claude Code plugin community is most active.

## Research Strategy

When the user requests a plugin search, launch **parallel research agents** to search both sources simultaneously. Use the `Task` tool with `subagent_type: "general-purpose"` to spawn independent agents for each source.

### Parallel Agent Dispatch

Fire two agents concurrently in a single message using two Task tool calls:

**Agent 1 — GitHub Researcher:**
Prompt the agent to use `WebSearch` and `WebFetch` to find Claude Code plugins on GitHub. Include these instructions in the agent prompt:
- Search for repositories with topics/keywords: `claude-code-plugin`, `claude-plugin`, `.claude-plugin`, `claude-code-extension`
- Search for repos containing `.claude-plugin/plugin.json` files
- Look for marketplace repositories that aggregate plugins
- Check GitHub trending and recently created repos
- For each plugin found, extract: repo name, author, description, stars, last updated, and what components it provides (skills, commands, agents, hooks)
- Return structured results as a markdown table

**Agent 2 — Twitter/X Researcher:**
Prompt the agent to use `WebSearch` to find Claude Code plugin discussions on Twitter/X. Include these instructions in the agent prompt:
- Search for tweets mentioning "Claude Code plugin", "Claude Code extension", "#ClaudeCode plugin"
- Look for plugin announcements, demos, and recommendations
- Find plugin authors sharing their work
- Search for threads discussing best Claude Code plugins
- For each relevant finding, extract: author handle, tweet summary, any linked repos, and date
- Return structured results as a markdown list

### Handling User-Specific Queries

If the user is looking for a specific type of plugin (e.g., "find Claude Code plugins for testing"), refine the search queries accordingly:
- Append the domain keyword to all search queries (e.g., "Claude Code plugin testing")
- Instruct both agents to filter results relevant to that domain
- Prioritize results that match the user's specific need

### Presenting Results

After both agents return, compile and present a unified report:

1. **Summary** — Total plugins found, sources searched, search terms used
2. **GitHub Findings** — Table of discovered plugins with repo links, descriptions, and star counts
3. **Twitter/X Findings** — Notable discussions, announcements, and recommendations
4. **Recommendations** — Highlight the most relevant or popular plugins based on the user's query
5. **Installation** — Include instructions on how to install discovered plugins (e.g., cloning the repo and using `claude --plugin-dir /path/to/plugin`)

### Search Query Patterns

Consult `references/search-patterns.md` for detailed search query patterns optimized for each platform.

## Important Notes

- Only search GitHub and Twitter/X — do not expand to other sources unless the user explicitly requests it
- Always launch both agents in parallel (single message, two Task tool calls) for speed
- If a search returns no results, suggest alternative search terms to the user — consult `references/search-patterns.md` for fallback queries
- Note that results may include outdated or archived plugins — always surface the last-updated date when available
