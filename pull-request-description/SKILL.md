---
name: pull-request-description
description: Generate a pull request description that matches the repo's existing conventions. Use this whenever the user asks to write, generate, or fill in a PR description — even if they just say "write the PR body" or "summarize this branch for review."
---

# Pull Request Description

## Learn the repo's style first

PR description conventions vary a lot between repos, so before writing anything, read the descriptions of the 10 most recent merged pull requests:

```bash
gh pr list --state merged --limit 10
gh pr view <number> --json body
```

Use these to understand the formatting, tone, and level of detail this repo expects, and match them. The template below is a starting point, not a replacement for the repo's own conventions — if the existing PRs do something different, follow them.

## Title

Write the title as a conventional commit: `type(scope): <short description of the changes>`, e.g. `feat(api): add retry logic to webhook deliveries`.

In a monorepo, the scope is the app or package name, e.g. `fix(web): stop duplicate form submissions`.

## Body template

```text
## Summary

<summary of the changes>

## Changes

- <change 1>
- <change 2>
- <change 3>
```

## What to include

The reader is a reviewer who wants to understand the PR in under a minute. Every sentence should earn its place:

- Be extremely concise and to the point — easy to skim, easy to understand.
- Only include changes that are high impact or important. Skip refactors, cleanups, and mechanical changes (renames, formatting, version bumps) unless they're the point of the PR.

## Full output example

The output should look exactly like this — same structure, same headings, nothing added:

```text
fix(web): stop duplicate form submissions

## Summary

Prevent users from accidentally submitting a form twice by disabling the submit button while the request is in flight.

## Changes

- Disable submit button during submission
- Add debounce to form submit handler
```
