# Rendering Strategy Decision Framework

## Contents
1. [Core Definitions](#core-definitions)
2. [Quick Decision Checklist](#quick-decision-checklist)
3. [Strategy Matrix](#strategy-matrix)
4. [Heuristics Per Strategy](#heuristics-per-strategy)
5. [Edge Cases & Pitfalls](#edge-cases--pitfalls)

---

## Core Definitions

| Strategy | When HTML is produced | Best for |
|----------|----------------------|----------|
| **SSG** | Build time | Public, cacheable, mostly-stable content. Served from CDN. |
| **ISR** | Build time + re-generated after deploy (time-based or on-demand) | Public content that changes sometimes; CDN speed with bounded staleness. |
| **SSR** | Each request | Request-specific data: auth/session, personalization, truly real-time. |
| **CSR** | Browser (shell from server) | Highly interactive app areas, especially behind auth where SEO doesn't matter. |

---

## Quick Decision Checklist

Pick the **first** that applies:

1. **Does HTML vary per user/request?** (user dashboards, auth-gated content, A/B tests at HTML level)
   → **SSR** (or **CSR behind auth** if SEO isn't needed)

2. **Is the page public and cacheable for everyone?**
   - Rarely changes → **SSG**
   - Changes occasionally (prices, CMS edits, ratings) → **ISR**

3. **Near real-time correctness required at request time?** (checkout inventory, live auctions, personalized search)
   → **SSR** (or **CSR** for live widgets if SEO not needed)

4. **SEO/share-preview critical?**
   → **SSG / ISR / SSR** (pre-rendered HTML). Avoid pure CSR.

5. **Interactive app screen behind login?**
   → **CSR** (optionally with SSR/SSG shell for fast nav)

---

## Strategy Matrix

| Cacheability \ Freshness | Static OK | Bounded staleness OK | Real-time required |
|---|---|---|---|
| Public cacheable | **SSG** | **ISR** | **SSR** (or CSR widget) |
| Public query-dependent | SSG shell + CSR results, or SSR with caching | ISR for common queries (rare) | **SSR** |
| User-specific | **CSR** (behind auth) or SSR | **SSR** | **SSR** |
| Mixed | SSG/ISR shell + CSR widgets | ISR shell + CSR widgets | SSR shell + CSR widgets |

---

## Heuristics Per Strategy

### SSG — choose when
- Content is **public** and **not user-specific**
- Updates are **rare** (hours/days/weeks)
- Build-time page count is manageable
- Examples: `/`, `/pricing`, `/about`, `/docs/*`, `/blog/*`

### ISR — choose when
- Content is **public** but changes **periodically**
- CDN speed most of the time, bounded staleness acceptable
- **Rule:** If content changes more frequently than you want to rebuild/deploy, use ISR
- Examples: product pages (stock/ratings), CMS-driven pages, listings

### SSR — choose when
- Output depends on request context: cookies/session/auth, geo/locale (can't safely cache), personalization in HTML
- Data must be **correct at request time**
- Responses cannot safely be shared across users
- Examples: auth pages, search results, checkout/billing/inventory

### CSR — choose when
- Page is mostly a **data-heavy interactive UI**
- **SEO is not a requirement**
- Need browser-only APIs (WebUSB, local device state)
- Examples: dashboards, settings, admin panels, complex charts
- **Guardrail:** CSR-only for public marketing pages is a mistake

### "Don't Mix Unless You Must"
Prefer a **clear primary strategy per route**. Use client components to add interactivity, but avoid confusing hybrids without concrete benefit.

---

## Edge Cases & Pitfalls

| Pitfall | Problem | Fix |
|---------|---------|-----|
| Accidentally static when personalized | Cookies/auth affect content but page is SSG | Ensure SSR or client-only personalization |
| Over-SSR | Public, stable route wastes compute | Switch to SSG or ISR |
| Over-CSR | Public pages slower + worse SEO/share previews | Switch to SSG/ISR for public routes |
| Build-time explosion | Too many dynamic pages → build never finishes | Use ISR on-demand/long revalidate, or SSR for long-tail |
| Cache safety | User-specific HTML cached and served to other users | Never cache user-specific HTML across users |
