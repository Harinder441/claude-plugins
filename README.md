# claude-plugins

Harinder441's personal [Claude Code](https://claude.com/claude-code) plugin
marketplace. A growing collection of plugins for personal use — each plugin
bundles one or more skills.

> Maintainers / agents: see **[AGENTS.md](./AGENTS.md)** for structure,
> versioning, and security rules before making changes.

## Install

```
/plugin marketplace add Harinder441/claude-plugins
/plugin install google-workspace@claude-plugins
```

## Plugins

| Plugin | Description |
|---|---|
| [`google-workspace`](./plugins/google-workspace) | Google-ecosystem skills. Currently: fetch a YouTube video transcript from a URL or ID. |

## Layout

```
.claude-plugin/marketplace.json   # marketplace manifest (lists plugins)
plugins/<name>/                    # one directory per plugin
```

## License

MIT
