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

### skill-creator

Guide for creating or updating agent skills with proper structure, frontmatter, and packaging.

**Use when:**
- Creating a new skill
- Updating an existing skill
- Packaging or validating skills

**Covers:**
- Skill anatomy (`SKILL.md`, `scripts/`, `references/`, `assets/`)
- Writing guidelines (concise, imperative)
- Packaging workflow (`scripts/package_skill.py`)

## Installation

```bash
npx skills add natemcgrady/skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
```
Create a new skill for PDF editing
```
```
We're on Next.js 16 - should I add middleware.ts?
```

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)

## License

MIT