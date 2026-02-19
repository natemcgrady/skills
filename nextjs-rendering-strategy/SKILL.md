---
name: nextjs-rendering-strategy
description: Analyze a React/Next.js project route-by-route and decide where to use SSG, ISR, SSR, or CSR. Use when planning rendering strategy, improving performance or SEO, reducing compute cost, or fixing stale/personalized content issues. Supports both App Router (Next.js 13+) and Pages Router.
---

# Next.js Rendering Strategy

## Goal

Produce a **per-route rendering plan** optimizing for: SEO/share previews, data freshness, personalization/auth, latency (TTFB/LCP), compute cost, and build-time scale.

## References

Load these as needed:

- **[decision-framework.md](references/decision-framework.md)** — Strategy definitions, quick decision checklist, heuristics matrix, edge cases/pitfalls. Load when deciding strategy for any route.
- **[implementation-patterns.md](references/implementation-patterns.md)** — Code snippets for App Router and Pages Router. Load when producing implementation output.
- **[archetypes.md](references/archetypes.md)** — Common site archetypes (marketing, blog, e-commerce, SaaS) with pre-mapped strategies. Load to quickly map familiar route types.

## Analysis Process

### Step 0 — Inventory routes

- App Router: `app/**/page.tsx`, `app/**/layout.tsx`
- Pages Router: `pages/**/*.tsx`

For each route, note: path, auth requirement, data sources, update frequency, SEO requirement, personalization, and scale (number of dynamic pages).

### Step 1 — Classify by cacheability

- **Public cacheable** — same HTML for all users
- **Public query-dependent** — search/filters vary output
- **User-specific** — cannot share cache across users
- **Mixed** — public shell + personalized widgets

### Step 2 — Classify by freshness SLA

- **Static OK** — days/weeks
- **Bounded staleness OK** — minutes/hours
- **Real-time required** — seconds/always current

### Step 3 — Apply the strategy matrix

See [decision-framework.md](references/decision-framework.md) for the full matrix and heuristics.

### Step 4 — Validate against build/compute constraints

- Huge cardinality (millions of pages) → avoid prebuilding all; use ISR on-demand or SSR for long-tail
- SSR compute too high → prefer ISR where possible, or edge caching (only if safe)

### Step 5 — Produce the final plan

For each route output:
- Chosen strategy
- Why (1–3 bullets)
- Data freshness SLA
- Caching notes
- Implementation snippets (see [implementation-patterns.md](references/implementation-patterns.md))

## Required Output

**1. Route Plan Table**

| Route | Audience | Freshness SLA | SEO | Strategy | Notes |
|-------|----------|--------------|-----|----------|-------|

**2. Top 5 Highest Impact Changes**

For each: what to change, expected benefit (latency/cost/SEO/freshness), risks.

**3. Implementation Checklist**

Files to edit, strategy-specific config/snippets, how to validate (TTFB, LCP, cache hit rate, correctness).

## Validation Signals (after changes)

Measure per route: TTFB, LCP, cache hit rate, serverless compute time/invocations, staleness incidents, SEO crawl/index correctness.
