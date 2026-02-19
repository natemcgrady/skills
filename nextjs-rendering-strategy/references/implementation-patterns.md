# Implementation Patterns

## App Router (Next.js 13+)

### SSG — cached fetch (default)
```ts
// Server Component
const data = await fetch("https://example.com/api/public", {
  cache: "force-cache",
}).then((r) => r.json());
```

### ISR — time-based revalidation
```ts
// Server Component: revalidate every 300s
const data = await fetch("https://example.com/api/public", {
  next: { revalidate: 300 },
}).then((r) => r.json());
```

### ISR — on-demand revalidation
```ts
// In a route handler or server action
import { revalidatePath, revalidateTag } from "next/cache";

revalidatePath("/products/[slug]");
// or tag-based:
revalidateTag("products");
```

```ts
// Fetch with tag
const data = await fetch("https://example.com/api/products", {
  next: { tags: ["products"] },
}).then((r) => r.json());
```

### SSR — always fresh
```ts
export const dynamic = "force-dynamic";

const data = await fetch("https://example.com/api/fresh", {
  cache: "no-store",
}).then((r) => r.json());
```

### CSR widget inside an SSG/ISR page
```tsx
"use client";

import { useEffect, useState } from "react";

export function LiveWidget() {
  const [state, setState] = useState(null);

  useEffect(() => {
    fetch("/api/live").then((r) => r.json()).then(setState);
  }, []);

  return <pre>{JSON.stringify(state, null, 2)}</pre>;
}
```

---

## Pages Router

### SSG
```ts
export async function getStaticProps() {
  const data = await fetch("https://example.com/api/public").then((r) => r.json());
  return { props: { data } };
}
```

### SSG with dynamic paths
```ts
export async function getStaticPaths() {
  const slugs = await fetchAllSlugs();
  return {
    paths: slugs.map((slug) => ({ params: { slug } })),
    fallback: "blocking", // or true / false
  };
}
```

### ISR
```ts
export async function getStaticProps() {
  const data = await fetch("https://example.com/api/public").then((r) => r.json());
  return { props: { data }, revalidate: 300 };
}
```

### SSR
```ts
export async function getServerSideProps(ctx) {
  const data = await fetch("https://example.com/api/fresh").then((r) => r.json());
  return { props: { data } };
}
```

### CSR (no data fetching at server)
```ts
// Simply export a page with no getStaticProps / getServerSideProps
// Fetch data in the component with useEffect or SWR/React Query
```
