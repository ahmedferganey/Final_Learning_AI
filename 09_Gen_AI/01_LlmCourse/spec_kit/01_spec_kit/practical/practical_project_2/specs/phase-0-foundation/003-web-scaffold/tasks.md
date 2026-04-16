# Tasks: Web Scaffold

**Input**: `specs/phase-0-foundation/003-web-scaffold/`
**Spec**: [spec.md](spec.md)

> **For LLM agents**: All files live under `web/`. No authentication logic, real API calls,
> or state beyond the TanStack Query provider. All pages are static placeholders. TypeScript
> strict mode is active throughout — no `any`, no `@ts-ignore`. File content and configuration
> values are specified inline. Commit after each phase.

---

## Phase 1: Setup — Next.js Project Initialization

- [X] T001 Initialize the Next.js 14 project in the `web/` directory using the App Router (FR-001). Run from repo root:
  ```
  cd web && npx create-next-app@14 . \
    --typescript \
    --tailwind \
    --eslint \
    --app \
    --src-dir \
    --no-import-alias
  ```
  Accept all defaults. After creation, verify `web/src/app/` exists (App Router confirmed).

- [X] T002 Update `web/tsconfig.json` to enforce strict mode and guarantee the `@/` path alias (FR-002). Merge these keys into the existing `compilerOptions` — do not replace the whole file:
  ```json
  {
    "compilerOptions": {
      "strict": true,
      "allowJs": false,
      "noImplicitAny": true,
      "strictNullChecks": true,
      "noUncheckedIndexedAccess": true,
      "baseUrl": ".",
      "paths": {
        "@/*": ["./src/*"]
      }
    }
  }
  ```
  The `@/*` alias maps `@/providers/...` → `src/providers/...`, `@/lib/...` → `src/lib/...`, etc.
  This MUST be set explicitly — do not rely on `create-next-app` to configure it.
  Run `npx tsc --noEmit` from `web/` — must exit 0.

- [X] T003 Update `web/.eslintrc.json` to add `@typescript-eslint/strict` ruleset (FR-007). Replace the file content with:
  ```json
  {
    "extends": [
      "next/core-web-vitals",
      "plugin:@typescript-eslint/strict"
    ],
    "parser": "@typescript-eslint/parser",
    "plugins": ["@typescript-eslint"],
    "rules": {
      "@typescript-eslint/no-explicit-any": "error"
    }
  }
  ```
  Install the plugin if not present: `npm install --save-dev @typescript-eslint/eslint-plugin @typescript-eslint/parser`.

- [X] T004 Create `web/.prettierrc` (FR-008):
  ```json
  {
    "semi": true,
    "singleQuote": false,
    "tabWidth": 2,
    "trailingComma": "all",
    "printWidth": 100
  }
  ```
  Add `"format:check": "prettier --check \"src/**/*.{ts,tsx}\""` to `web/package.json` `scripts` section.

- [X] T005 Verify `web/tailwind.config.ts` has the correct `content` paths (FR-004). The `content` array MUST include `"./src/**/*.{ts,tsx}"`. Open the file and confirm this line is present. If the file uses `.js` extension, rename to `.ts` and update content accordingly.

- [X] T006 Update `web/package.json` to pin all dependencies to exact versions and add the `engines` field (FR-011, Edge Case). Set:
  - `"engines": { "node": ">=20" }` at the top level
  - Change all `"^x.y.z"` version strings to `"x.y.z"` (remove carets) for all `dependencies` and `devDependencies`
  - Add TanStack Query: `npm install @tanstack/react-query@5`

**Checkpoint — Phase 1**: Run `npm run lint` — exit 0. Run `npx tsc --noEmit` — exit 0.

---

## Phase 2: Foundational — Root Layout and Query Provider

**Purpose**: The root layout and QueryClientProvider must exist before any page renders.

- [X] T007 Create `web/src/providers/query-provider.tsx` — a `'use client'` component wrapping children with `QueryClientProvider` (FR-005). This MUST be a separate client component so the root layout can remain a server component:

  ```tsx
  "use client";

  import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
  import { useState } from "react";

  export function ReactQueryProvider({ children }: { children: React.ReactNode }) {
    const [queryClient] = useState(
      () =>
        new QueryClient({
          defaultOptions: {
            queries: {
              staleTime: 60 * 1000,
            },
          },
        })
    );

    return (
      <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
    );
  }
  ```

- [X] T008 Update `web/src/app/layout.tsx` to wrap children with `ReactQueryProvider` (FR-005). Replace the default content with:

  ```tsx
  import type { Metadata } from "next";
  import "./globals.css";
  import { ReactQueryProvider } from "@/providers/query-provider";

  export const metadata: Metadata = {
    title: "GymOS",
    description: "Adaptive training intelligence platform",
  };

  export default function RootLayout({
    children,
  }: {
    children: React.ReactNode;
  }) {
    return (
      <html lang="en">
        <body>
          <ReactQueryProvider>{children}</ReactQueryProvider>
        </body>
      </html>
    );
  }
  ```

**Checkpoint — Phase 2**: Run `npm run dev` — server starts on port 3000 with no errors.

---

## Phase 3: User Story 1 — Placeholder Pages Render Without Errors (Priority: P1) 🎯 MVP

**Goal**: `npm run dev` starts, `/login` and `/dashboard` both return HTTP 200 with no JS console errors.

**Independent test** (SC-001): Run `npm run dev`, open browser to `http://localhost:3000/login` and `http://localhost:3000/dashboard` — both render, browser console shows zero errors.

- [X] T009 [P] [US1] Create `web/src/app/(auth)/login/page.tsx` (FR-003). This is a placeholder — no form, no auth logic:

  ```tsx
  export default function LoginPage() {
    return (
      <main className="flex min-h-screen items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold">GymOS</h1>
          <p className="mt-2 text-gray-500">Login — coming in Phase 1</p>
        </div>
      </main>
    );
  }
  ```

- [X] T010 [P] [US1] Create `web/src/app/(dashboard)/dashboard/page.tsx` (FR-003). Placeholder only:

  ```tsx
  export default function DashboardPage() {
    return (
      <main className="flex min-h-screen items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold">GymOS Dashboard</h1>
          <p className="mt-2 text-gray-500">Dashboard — coming in Phase 3</p>
        </div>
      </main>
    );
  }
  ```

**Checkpoint — US1**: `npm run dev` → navigate to both `/login` and `/dashboard` → both render, zero console errors.

---

## Phase 4: User Story 2 — Production Build With No Errors (Priority: P2)

**Goal**: `npm run build` succeeds with `NEXT_PUBLIC_API_URL` set; fails with a descriptive error when absent.

**Independent test** (SC-002): `NEXT_PUBLIC_API_URL=http://localhost:8000 npm run build` → exit 0, `.next/` directory created.

- [X] T011 [US2] Create `web/next.config.ts` with environment variable validation (FR-009). Replace the existing `next.config.js` or `next.config.ts`:

  ```ts
  import type { NextConfig } from "next";

  // Validate required environment variables at build time
  const requiredEnvVars = ["NEXT_PUBLIC_API_URL"] as const;
  for (const envVar of requiredEnvVars) {
    if (!process.env[envVar]) {
      throw new Error(
        `Missing required environment variable: ${envVar}\n` +
          `Set it in your .env.local file or CI environment.`
      );
    }
  }

  const nextConfig: NextConfig = {
    // output: "standalone" is deferred to Phase 9 production hardening
  };

  export default nextConfig;
  ```

- [X] T012 [P] [US2] Create `web/.env.example` listing all required env variables (FR-009):

  ```
  # Backend API URL — required for all API requests
  NEXT_PUBLIC_API_URL=http://localhost:8000
  ```

  Also create `web/.env.local` (gitignored) for local development with the same content using real values. Add `web/.env.local` to `web/.gitignore` if not already there.

**Checkpoint — US2**: `NEXT_PUBLIC_API_URL=http://localhost:8000 npm run build` exits 0. `npm run build` without the variable fails with the descriptive error.

---

## Phase 5: User Story 3 — API Client Configured (Priority: P3)

**Goal**: `web/src/lib/api/client.ts` exists, reads `NEXT_PUBLIC_API_URL` from env, and is importable without TypeScript errors.

**Independent test** (SC-006, US3): Import client in a page component and call a method — TypeScript reports no errors.

- [X] T013 [US3] Create `web/src/lib/api/client.ts` — an API client that reads the base URL from the environment and fails loudly if absent (FR-006, Edge Case):

  ```ts
  const apiBaseUrl = process.env.NEXT_PUBLIC_API_URL;

  if (!apiBaseUrl) {
    throw new Error(
      "NEXT_PUBLIC_API_URL is not defined. " +
        "Add it to your .env.local file: NEXT_PUBLIC_API_URL=http://localhost:8000"
    );
  }

  export interface ApiResponse<T> {
    data: T;
    meta?: Record<string, unknown>;
  }

  export interface ApiError {
    error: {
      code: string;
      message: string;
      details?: Record<string, unknown>;
    };
  }

  async function request<T>(
    path: string,
    options?: RequestInit
  ): Promise<ApiResponse<T>> {
    const url = `${apiBaseUrl}${path}`;
    const response = await fetch(url, {
      headers: {
        "Content-Type": "application/json",
        ...options?.headers,
      },
      ...options,
    });

    if (!response.ok) {
      const errorBody = (await response.json()) as ApiError;
      throw new Error(errorBody.error?.message ?? `HTTP ${response.status}`);
    }

    return response.json() as Promise<ApiResponse<T>>;
  }

  export const apiClient = {
    get: <T>(path: string, options?: RequestInit) =>
      request<T>(path, { ...options, method: "GET" }),
    post: <T>(path: string, body: unknown, options?: RequestInit) =>
      request<T>(path, {
        ...options,
        method: "POST",
        body: JSON.stringify(body),
      }),
    put: <T>(path: string, body: unknown, options?: RequestInit) =>
      request<T>(path, {
        ...options,
        method: "PUT",
        body: JSON.stringify(body),
      }),
    delete: <T>(path: string, options?: RequestInit) =>
      request<T>(path, { ...options, method: "DELETE" }),
  };
  ```

**Checkpoint — US3**: `npx tsc --noEmit` from `web/` exits 0. Import `apiClient` in any page file — no TypeScript errors.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T014 Update the `"test"` script in `web/package.json` to use Jest with `--passWithNoTests` (FR-010). `create-next-app@14` generates a Jest script by default. Find the existing test script (likely `"jest"` or `"jest --watch"`) and replace it with:
  ```json
  "test": "jest --passWithNoTests"
  ```
  Do NOT install Vitest. Verify `npm run test` exits 0 with the message "No test suites were run" or "Tests: 0 passed".

- [X] T015 [P] Create `web/README.md` with these sections: (1) **Prerequisites** — Node.js ≥20; (2) **Install** — `npm install`; (3) **Environment** — copy `.env.example` to `.env.local`; (4) **Dev server** — `npm run dev` → http://localhost:3000; (5) **Build** — `NEXT_PUBLIC_API_URL=... npm run build`; (6) **Quality checks** — `npm run lint`, `npx tsc --noEmit`, `npm run format:check`.

- [X] T016 Run `npm run lint` → exit 0 (SC-003). Run `npx tsc --noEmit` → exit 0 (SC-004). Fix any violations before marking done.

---

## Dependencies & Execution Order

```
Phase 1 (T001–T006) — T001 first; T002–T006 after T001 (in parallel with each other)
  └─► Phase 2 (T007, T008) — T007 before T008
        └─► Phase 3 (T009, T010) — parallel with each other, after T008
        └─► Phase 4 (T011, T012) — T011 parallel with Phase 3; T012 parallel with T011
        └─► Phase 5 (T013) — after Phase 2
              └─► Phase 6 (T014–T016) — all after all stories complete
```

---

## Notes for LLM Agents

- **App Router only** — no `pages/` directory (FR-001); do not create `pages/index.tsx`
- **No auth logic** — placeholder pages only, no middleware.ts (FR-012)
- **`QueryClientProvider` must be in a `'use client'` component** — the root layout is a server component (Edge Case)
- **Tailwind `content` path** — must include `./src/**/*.{ts,tsx}` or classes are purged (Edge Case)
- **Commit message**: `feat(web): add Next.js 14 scaffold with placeholder routes and API client`
