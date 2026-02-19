# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### use-proxy

Remind the assistant to use Next.js 16 Proxy (`proxy.ts`) instead of Middleware (`middleware.ts`), with migration guidance.

**Use when:**

- Working on Next.js 16 apps
- Creating or updating `middleware.ts`
- Migrating existing middleware to proxy

**Includes:**

- Proxy-first guidance
- Codemod command: `npx @next/codemod@canary middleware-to-proxy .`
- Reference links to the official Next.js docs

### nextjs-rendering-strategy

Analyze a React/Next.js project route-by-route and decide where to use SSG, ISR, SSR, or CSR.

**Use when:**

- Planning rendering strategy for routes
- Improving performance and SEO
- Reducing compute cost
- Fixing stale or personalized content issues

**Covers:**

- Decision framework (SSG/ISR/SSR/CSR definitions, quick checklist)
- Strategy matrix (cacheability vs. freshness SLA)
- Implementation patterns for App Router and Pages Router
- Common archetypes (marketing, blog, e-commerce, SaaS)

## Installation

```bash
npx skills add natemcgrady/skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**

```
We're on Next.js 16 - should I add middleware.ts?
```

```
Should my landing page be statically generated?
```

## Skill Structure

Each skill contains:

- `SKILL.md` - Instructions for the agent
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)

## License

MIT
