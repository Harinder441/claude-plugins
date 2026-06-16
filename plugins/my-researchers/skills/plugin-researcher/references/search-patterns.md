# Search Patterns for Claude Code Plugin Discovery

## GitHub Search Queries

### Primary Queries (use with WebSearch)

Use these search queries to discover Claude Code plugins on GitHub. Run multiple queries to maximize coverage.

**Repository discovery:**
- `claude-code-plugin site:github.com`
- `claude-code plugin site:github.com`
- `".claude-plugin" "plugin.json" site:github.com`
- `claude-code extension site:github.com`
- `claude code marketplace plugin site:github.com`

**Topic-based discovery:**
- `site:github.com topic:claude-code-plugin`
- `site:github.com topic:claude-plugin`
- `site:github.com topic:claude-code`

**File-based discovery (search for plugin structure indicators):**
- `".claude-plugin/plugin.json" site:github.com`
- `"SKILL.md" claude-code site:github.com`
- `hooks.json "PreToolUse" claude site:github.com`

**Marketplace and collection repos:**
- `claude-code plugins marketplace site:github.com`
- `awesome-claude-code site:github.com`
- `claude-code-plugins collection site:github.com`

### Domain-Specific Queries

When the user wants plugins for a specific domain, combine the base query with the domain keyword:

- `claude-code plugin {domain} site:github.com`
- `claude plugin {domain} site:github.com`

Examples:
- `claude-code plugin testing site:github.com`
- `claude-code plugin database site:github.com`
- `claude-code plugin docker site:github.com`
- `claude-code plugin code-review site:github.com`

### GitHub API Exploration

When WebSearch results are insufficient, use WebFetch on these GitHub search URLs:
- `https://github.com/search?q=claude-code-plugin&type=repositories&sort=stars`
- `https://github.com/search?q=.claude-plugin+plugin.json&type=code`
- `https://github.com/topics/claude-code-plugin`

## Twitter/X Search Queries

### Primary Queries (use with WebSearch)

**Plugin announcements:**
- `"Claude Code plugin" site:twitter.com OR site:x.com`
- `"Claude Code" plugin announcement site:twitter.com OR site:x.com`
- `#ClaudeCode plugin site:twitter.com OR site:x.com`

**Plugin recommendations and discussions:**
- `"Claude Code" best plugins site:twitter.com OR site:x.com`
- `"Claude Code" plugin recommendation site:twitter.com OR site:x.com`
- `"Claude Code" extension site:twitter.com OR site:x.com`

**Plugin author shares:**
- `"built a Claude Code plugin" site:twitter.com OR site:x.com`
- `"made a plugin for Claude Code" site:twitter.com OR site:x.com`
- `"Claude Code" "my plugin" site:twitter.com OR site:x.com`
- `"Claude Code" plugin github.com site:twitter.com OR site:x.com`

### Domain-Specific Queries

- `"Claude Code" plugin {domain} site:twitter.com OR site:x.com`

## Tips for Better Results

1. **Recency**: Append the current year to queries to find recent plugins
2. **Combine sources**: Cross-reference GitHub repos found via Twitter with direct GitHub search
3. **Follow authors**: When a prolific plugin author is found, check their other repos
4. **Check forks**: Popular plugin repos may have forks with improvements
5. **README inspection**: Use WebFetch on promising repos to read their README for quality assessment
6. **Star count**: Sort GitHub results by stars to find popular, community-validated plugins
