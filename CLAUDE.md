# CLAUDE.md

This repository's conventions, structure, versioning rules, and security
requirements live in **[AGENTS.md](./AGENTS.md)**. Read and follow that file —
it is the single source of truth for working in this repo.

Quick reminders (see AGENTS.md for the full detail):

- This is a **public personal plugin marketplace** for Harinder441 — never
  commit tokens, secrets, or personal/work details.
- After any change, **bump the version in both** the plugin's `plugin.json`
  **and** its entry in `.claude-plugin/marketplace.json`, or installs won't pull
  the update.
- New plugins must be registered in `.claude-plugin/marketplace.json`.
