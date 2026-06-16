# Shopify Documentation Map

## Developer Documentation (shopify.dev)

Use these topic areas to construct targeted search queries against `shopify.dev`.

| Topic Area | URL Path Prefix | Key Concepts |
|-----------|----------------|--------------|
| Apps | `shopify.dev/docs/apps` | App architecture, OAuth, app extensions, embedded apps, app bridge |
| Storefront API | `shopify.dev/docs/api/storefront` | Headless commerce, custom storefronts, cart API, customer API |
| Admin API (GraphQL) | `shopify.dev/docs/api/admin-graphql` | Product, order, customer, inventory management via GraphQL |
| Admin API (REST) | `shopify.dev/docs/api/admin-rest` | Legacy REST endpoints (GraphQL preferred for new development) |
| Liquid | `shopify.dev/docs/api/liquid` | Template language, objects, filters, tags, theme rendering |
| Themes | `shopify.dev/docs/themes` | Theme architecture, sections, blocks, JSON templates, settings |
| Functions | `shopify.dev/docs/api/functions` | Discount functions, delivery customization, payment customization, cart transform |
| Checkout | `shopify.dev/docs/api/checkout-extensions` | Checkout UI extensions, post-purchase extensions, checkout branding |
| Hydrogen | `shopify.dev/docs/custom-storefronts/hydrogen` | React-based headless framework, Remix, Oxygen hosting |
| Webhooks | `shopify.dev/docs/apps/webhooks` | Event subscriptions, mandatory webhooks, webhook delivery |
| Metafields | `shopify.dev/docs/apps/custom-data/metafields` | Custom data storage, metafield definitions, types, namespaces |
| POS | `shopify.dev/docs/apps/pos` | Point of sale extensions, POS UI extensions |
| Payments | `shopify.dev/docs/apps/payments` | Payment apps, payment extensions |
| Markets | `shopify.dev/docs/apps/markets` | International commerce, multi-currency, localization |

## Merchant Help Documentation (help.shopify.com)

| Topic Area | URL Path Prefix | Key Concepts |
|-----------|----------------|--------------|
| Getting Started | `help.shopify.com/en/manual/intro-to-shopify` | Store setup, plans, Shopify admin overview |
| Products | `help.shopify.com/en/manual/products` | Product creation, variants, collections, inventory |
| Orders | `help.shopify.com/en/manual/orders` | Order management, fulfillment, refunds, drafts |
| Payments | `help.shopify.com/en/manual/payments` | Payment providers, Shopify Payments, manual payments |
| Shipping | `help.shopify.com/en/manual/shipping` | Shipping rates, zones, labels, fulfillment services |
| Markets | `help.shopify.com/en/manual/markets` | International selling, market-specific settings |
| Online Store | `help.shopify.com/en/manual/online-store` | Themes, navigation, domains, pages, blogs |
| Customers | `help.shopify.com/en/manual/customers` | Customer management, segments, accounts |
| Discounts | `help.shopify.com/en/manual/discounts` | Discount codes, automatic discounts, discount combinations |
| Apps | `help.shopify.com/en/manual/apps` | Installing apps, app permissions, app management |

## API Versioning

Shopify uses calendar-based API versioning:

- Format: `YYYY-MM` (e.g., `2025-01`, `2025-04`)
- Releases: January, April, July, October each year
- Support window: Each version supported for ~12 months
- Always prefer the latest stable version in explanations
- Check `shopify.dev/docs/api/usage/versioning` for current version details

## Terminology Mappings

Users often use informal or generic terms. Map them to Shopify's canonical terminology:

| User Might Say | Shopify Canonical Term | Documentation Area |
|---------------|----------------------|-------------------|
| custom fields | Metafields | Apps > Custom Data |
| plugins | Apps | Apps |
| extensions | App extensions or Theme extensions | Apps or Themes |
| headless | Hydrogen / Storefront API | Custom Storefronts |
| templates | Liquid templates / JSON templates | Themes |
| serverless functions | Shopify Functions | Functions |
| discount rules | Discount Functions or Automatic Discounts | Functions or Discounts |
| custom checkout | Checkout UI Extensions | Checkout |
| API keys | API credentials / Access tokens | Apps > Auth |
| hooks / webhooks | Webhooks | Apps > Webhooks |
| custom data | Metafields or Metaobjects | Apps > Custom Data |
| sections | Theme sections | Themes |
| blocks | Theme blocks or Checkout blocks | Themes or Checkout |
| storefront | Online Store or Storefront API | Depends on context |
| backend | Admin API or App backend | Apps |
| theme code | Liquid / Theme files | Themes |
