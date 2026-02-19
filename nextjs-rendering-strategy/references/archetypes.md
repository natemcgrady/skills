# Common Route Archetypes

Use this as a fast-mapping reference. Validate against the project's actual data freshness and auth requirements.

## Marketing Site

| Route | Strategy | Notes |
|-------|----------|-------|
| `/`, `/pricing`, `/about` | **SSG** | Public, stable |
| CMS-driven pages | **ISR** (minutes/hours) or on-demand | Trigger revalidation on CMS publish |

## Blog / Docs

| Route | Strategy | Notes |
|-------|----------|-------|
| Posts / docs pages | **SSG** | Or ISR if frequently edited |
| Search results | **SSR** or **SSG shell + CSR search** | Depends on query personalization |

## E-commerce

| Route | Strategy | Notes |
|-------|----------|-------|
| Category templates | **SSG** | Stable structure |
| Product pages | **ISR** | Descriptions/specs static; regenerate for price/stock/reviews |
| Search results | **SSR** | Query/personalization changes frequently |
| Cart / checkout | **CSR** or **SSR** | SSR for correctness (inventory); CSR for interactive UI |

## SaaS App

| Route | Strategy | Notes |
|-------|----------|-------|
| Public marketing | **SSG / ISR** | Same as marketing site |
| Dashboard / settings / admin | **CSR** | Or SSR for faster first meaningful paint if needed |
| Onboarding flows (auth-gated) | **SSR** or **CSR** | SSR if personalized HTML matters; CSR otherwise |
