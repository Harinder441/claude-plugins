# Shopify Documentation Domain Rules

## Authoritative Domains

Only these domains are considered primary, authoritative sources for Shopify information:

| Domain | Content Type | Use When |
|--------|-------------|----------|
| `shopify.dev` | Developer documentation | APIs, Liquid, themes, apps, functions, Hydrogen, webhooks, metafields |
| `help.shopify.com` | Merchant help documentation | Store setup, products, orders, payments, shipping, markets |

## WebSearch Configuration

Always use domain filtering when searching for Shopify documentation:

```
WebSearch with allowed_domains: ["shopify.dev", "help.shopify.com"]
```

This ensures results come exclusively from official Shopify sources. Never omit the `allowed_domains` parameter when performing searches for this skill.

## User-Provided URLs

When the user provides a URL to read:

1. **Official domain URL** (`shopify.dev` or `help.shopify.com`) — Treat as a primary source. Read via WebFetch and use its content as the basis for the explanation.
2. **External URL** (any other domain) — Read via WebFetch as supplemental context. Still search official docs for the canonical answer on the same topic.
3. **Conflict resolution** — If an external source contradicts official Shopify documentation, always defer to the official docs. Note the discrepancy to the user.

## Out-of-Scope Sources

Do NOT use these as primary sources. They may contain outdated, inaccurate, or opinion-based information:

- Medium, Dev.to, and personal blogs
- Stack Overflow and other Q&A sites
- YouTube videos and tutorials
- Shopify Community forums
- Third-party course platforms
- AI-generated content aggregators

These sources may be referenced only if the user explicitly provides a URL from one of them, and even then, always cross-reference with official docs.

## When Official Documentation Is Insufficient

If the official docs do not adequately cover a topic:

1. State clearly that official documentation on this specific topic is limited
2. Share what IS documented, even if partial
3. Do NOT fabricate or speculate about undocumented behavior
4. Suggest the user check:
   - Shopify Changelog (`shopify.dev/changelog`) for recent changes
   - Shopify Community forums for community-reported behavior
   - Shopify Partner Slack or Discord for real-time help
5. If the topic involves an API, suggest the user test in a development store
