---
name: lean-code
description: Review and rewrite code changes in the current branch to be lean, simple, and beautiful. Use this skill when the user asks to "clean up my branch", "make my code beautiful", "simplify my changes", "review my PR code", "polish my diff", or "make this code simpler". Also trigger when the user says things like "is my code clean?", "review my changes for quality", "make this more readable", "tighten up the code", or "apply code style to my branch". This skill enforces a specific opinionated philosophy: minimal state, no defensive code, discriminated unions, asserts over try/catch, fewer lines. Trigger even if the user doesn't say "lean" explicitly — any request to improve, clean, or beautify code changes belongs here.
---

You are reviewing code changes in the current branch and rewriting them to be lean, simple, and beautiful.

## The philosophy

Simple code is skimmable. Someone should be able to read it quickly and understand it without slowing down. Every line is a line someone has to read. Every argument is a state to track. Every optional field is a branch in the reader's head.

The goal isn't "correct and complete" — it's "correct and minimal."

## Read the diff first

```bash
git diff main
```

Work through each changed file. For each one, identify every violation of the rules below and fix it.

Only touch files in the diff. Don't refactor surrounding code that wasn't changed.

---

## The rules

### 1. Keep argument counts low

If a function takes 4+ arguments, ask whether fewer would work. Often, some arguments are always passed together — group them into an object. Sometimes an argument is always the same — make it a constant inside the function.

**Before:**

```ts
function render(label: string, value: number, isLoading?: boolean, error?: string) {
```

**After:**

```ts
function render(label: string, value: number) {
```

### 2. Required means required

Don't make arguments optional if they're always provided. `?` in a type signature is a claim: "this might not exist." If it always does, the `?` is a lie that forces every caller to handle a case that never happens.

**Before:**

```ts
function fetchUser(id?: string) {
  if (!id) return null
```

**After:**

```ts
function fetchUser(id: string) {
```

### 3. Use asserts at data boundaries, not guards inside logic

When loading data from external sources (API responses, DB results, user input), assert that it has the shape you expect. Inside your own logic, don't guard against things that "shouldn't happen" — just let the code crash if your assumptions are wrong.

```ts
// Loading data — assert the shape
const user = await db.users.findFirst({ where: { id } });
assert(user, `user ${id} not found`);

// Inside logic — no need to guard
return user.email.toLowerCase(); // not: user?.email?.toLowerCase() ?? ""
```

### 4. No silent fallbacks

`?? defaultValue` is often a cover-up. If the value should always be there, and it's not, you want to know. Use an assert instead.

**Before:**

```ts
const name = user.name ?? "Anonymous";
```

**After:**

```ts
assert(user.name, "user must have a name");
const name = user.name;
```

...unless `"Anonymous"` is genuinely a valid business-logic fallback (new user who hasn't set a name yet, etc.). Use judgment.

### 5. No try/catch around code you expect to succeed

Try/catch hides crashes and makes failure silent. If something should work, let it throw. The only exception: explicitly handling known failure modes (e.g., a network request that might time out, where you want to show a specific error message).

**Before:**

```ts
try {
  const data = JSON.parse(raw);
  return data.value;
} catch {
  return null;
}
```

**After:**

```ts
return JSON.parse(raw).value;
```

### 6. Discriminated unions over multiple optional fields

When an object can be in a few distinct states, model it as a union, not as a record with lots of optional fields. This eliminates whole classes of invalid states.

**Before:**

```ts
type Result = {
  data?: User;
  error?: string;
  loading?: boolean;
};
```

**After:**

```ts
type Result =
  | { kind: "loading" }
  | { kind: "error"; message: string }
  | { kind: "data"; user: User };
```

### 7. Exhaustive handling — throw on unknown types

When switching on a union or discriminated type, handle every case and throw on the default. This makes unknown states loud instead of silent.

```ts
switch (result.kind) {
  case "loading": return <Spinner />
  case "error": return <ErrorView message={result.message} />
  case "data": return <UserView user={result.user} />
  default: throw new Error(`unknown result kind: ${(result as any).kind}`)
}
```

### 8. Fewer lines, always

When two forms are equivalent, prefer the shorter one. Don't introduce variables just to give things names if the expression is already clear inline. Don't split a 3-line function into two 2-line functions.

**Before:**

```ts
const isActive = user.status === "active"
const shouldShow = isActive && user.verified
if (shouldShow) {
```

**After:**

```ts
if (user.status === "active" && user.verified) {
```

### 9. Early returns

Don't nest happy-path code inside an `if`. Return early for the guard case and let the happy path flow at the top level.

**Before:**

```ts
function process(item: Item | null) {
  if (item) {
    doSomething(item);
    doMore(item);
  }
}
```

**After:**

```ts
function process(item: Item | null) {
  if (!item) return;
  doSomething(item);
  doMore(item);
}
```

### 10. Don't over-extract functions

A short sequence of steps is often more readable inline than broken into named helper functions. Only extract a function if it's called from more than one place, or if the extracted function has a name that genuinely communicates something the inline code doesn't.

### 11. Remove unnecessary changes

If a change doesn't affect behavior, remove it. Whitespace reformatting, comment rewording, renames of internal variables — these add noise to the diff without value.

---

## How to present changes

For each file with violations, show:

1. What was wrong
2. The rewritten version

Be direct. Don't pad with explanations of rules the user already gave you. Show the improved code and say why in one line if it's not obvious.

If the diff is already clean, say so.
