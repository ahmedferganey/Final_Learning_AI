# Feature Specification: Web Scaffold

**Feature Branch**: `003-web-scaffold`
**Created**: 2026-04-09
**Status**: Draft
**Phase**: 0 — Foundation
**Plan Reference**: Plan.md → Spec 0.3

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Developer Starts the Web App and Sees Placeholder Pages (Priority: P1)

A developer runs `npm run dev` in the `web/` directory. The Next.js development server starts
on port 3000. They open `/login` and `/dashboard` in a browser and see placeholder pages that
render without JavaScript console errors and without any `404` or build failures.

**Why this priority**: All web feature specs (Phase 3) depend on a functioning Next.js
application with route structure and toolchain in place. Discovering toolchain incompatibilities
after Phase 1 auth exists is far more expensive than discovering them now.

**Independent Test**: Can be fully tested by running `npm run dev` and navigating to `/login`
and `/dashboard`. Delivers value by confirming the full Next.js + TypeScript + Tailwind
dependency chain is wired correctly.

**Acceptance Scenarios**:

1. **Given** Node.js dependencies are installed via `npm install`, **When** `npm run dev`
   is executed in `web/`, **Then** the development server starts on port 3000 and prints a
   ready message within 30 seconds.

2. **Given** the development server is running, **When** a browser navigates to
   `http://localhost:3000/login`, **Then** a page renders with HTTP 200 and the browser
   console shows zero JavaScript errors.

3. **Given** the development server is running, **When** a browser navigates to
   `http://localhost:3000/dashboard`, **Then** a page renders with HTTP 200 and the browser
   console shows zero JavaScript errors.

4. **Given** `NEXT_PUBLIC_API_URL` is not set in the environment, **When** `npm run build`
   is executed, **Then** the build fails with an error message that names the missing
   variable — it does not produce a build silently configured with `undefined` as the API URL.

---

### User Story 2 — Developer Produces a Production Build With No Errors (Priority: P2)

A developer runs `npm run build`. The Next.js production build completes successfully with
no TypeScript errors, no ESLint violations, and no build warnings that indicate broken
configuration. The output is a valid production artefact.

**Why this priority**: A scaffold that cannot produce a production build is not a scaffold —
it is a development-only prototype. Ensuring the build works from day one prevents build
configuration drift that grows harder to fix as the codebase grows.

**Independent Test**: Can be fully tested by running `npm run build` with `NEXT_PUBLIC_API_URL`
set. A successful exit code with no errors delivers the value of confirming production
build integrity.

**Acceptance Scenarios**:

1. **Given** `NEXT_PUBLIC_API_URL` is set and `npm install` has run, **When** `npm run build`
   is executed, **Then** the build exits with code 0 and produces a `.next/` output directory.

2. **Given** a TypeScript error is introduced into any file (e.g., a wrong type assignment),
   **When** `npm run build` is executed, **Then** the build fails and the error is reported
   with the file name and line number.

3. **Given** an ESLint violation is introduced into any file, **When** `npm run lint` is
   executed, **Then** the violation is reported with the rule name, file, and line number.

---

### User Story 3 — API Client Is Configured and Usable Across the App (Priority: P3)

A developer working on a Phase 3 feature imports the API client from `lib/api/` and makes a
typed request without needing to configure base URLs, headers, or error handling from scratch.
The client reads `NEXT_PUBLIC_API_URL` from the environment and applies it automatically.

**Why this priority**: Without a shared API client, each feature in Phase 3 would implement
its own fetch logic, resulting in inconsistent error handling, duplicated auth header code,
and untestable network layers. Establishing the client in Phase 0 makes Phase 3 work
immediately consistent.

**Independent Test**: Can be tested by importing the API client in a placeholder page and
calling a method — verifying the base URL is applied and the request is typed without
TypeScript errors.

**Acceptance Scenarios**:

1. **Given** the API client exists at `web/src/lib/api/client.ts`, **When** it is imported
   in any page or component, **Then** TypeScript does not report any type errors related to
   the import or its usage.

2. **Given** `NEXT_PUBLIC_API_URL=http://localhost:8000`, **When** the API client is used
   to call an endpoint, **Then** the request is sent to `http://localhost:8000/<endpoint>`
   without any manual URL construction in the calling code.

3. **Given** TanStack Query is configured via a provider in the root layout, **When** a
   component uses `useQuery` from TanStack Query, **Then** the query executes without
   provider-missing errors and the TypeScript types are correctly inferred.

---

### Edge Cases

- **Missing `NEXT_PUBLIC_API_URL`:** The API client initialization MUST throw a descriptive
  error at build time (not a silent `undefined` base URL) if this variable is absent.
  Implemented via an explicit env validation step at the top of `client.ts`.
- **Route group conflicts:** Next.js App Router route groups (`(auth)`, `(dashboard)`) MUST
  NOT create conflicting URL paths. `/login` under `(auth)` and `/dashboard` under
  `(dashboard)` must both resolve to their correct paths with no 404s.
- **TanStack Query provider placement:** The `QueryClientProvider` MUST be placed in the
  root layout (`app/layout.tsx`) and not in individual page files. A provider placed per-page
  creates a new query cache per page and breaks cache sharing.
- **Tailwind CSS purging:** The Tailwind `content` configuration MUST include
  `./src/**/*.{ts,tsx}`. Missing this causes all Tailwind classes to be purged in production
  builds, resulting in unstyled pages.
- **TypeScript strict mode:** `tsconfig.json` MUST enable `"strict": true`. Any use of
  `// @ts-ignore` or `// @ts-expect-error` in scaffold code is a blocker for review.
- **`npm run test` with no tests:** Jest is the canonical test runner (ships with `create-next-app@14`).
  The test script MUST pass `--passWithNoTests` so `npm run test` exits 0 on a fresh scaffold with
  no test files. Do NOT install Vitest alongside Jest.
- **Node version:** `package.json` MUST include an `engines` field specifying the minimum
  Node.js version (`>=20`). This prevents developers from running the app on an incompatible
  version silently.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The Next.js application MUST use the App Router (`app/` directory), NOT the
  Pages Router (`pages/` directory).
- **FR-002**: TypeScript MUST be configured with `"strict": true` in `tsconfig.json`. No
  exceptions or suppressions in scaffold code.
- **FR-003**: Route groups MUST be created: `app/(auth)/` containing `login/page.tsx` and
  `app/(dashboard)/` containing `dashboard/page.tsx`. Both pages render valid placeholder
  content (not blank or erroring).
- **FR-004**: Tailwind CSS MUST be configured with the correct `content` paths covering all
  `src/**/*.{ts,tsx}` files. A utility class applied to a placeholder element must appear
  in the production CSS output.
- **FR-005**: TanStack Query MUST be initialized with a `QueryClient` in a client component
  (`'use client'`) and wrapped around the application in the root layout.
- **FR-006**: An API client module MUST exist at `web/src/lib/api/client.ts`. It MUST read
  `NEXT_PUBLIC_API_URL` from `process.env`, validate it is defined, and export a configured
  HTTP client instance.
- **FR-007**: ESLint MUST be configured with `@typescript-eslint/strict` ruleset. `npm run
  lint` MUST run ESLint against all `src/**/*.{ts,tsx}` files.
- **FR-008**: Prettier MUST be configured with a `.prettierrc` file. `npm run format:check`
  MUST verify formatting without modifying files (for use in CI).
- **FR-009**: `npm run build` MUST succeed with `NEXT_PUBLIC_API_URL` set and MUST fail
  with a descriptive error when it is absent.
- **FR-010**: `npm run test` MUST execute Jest (the `create-next-app@14` default runner) with
  `--passWithNoTests` and exit with code 0 when zero test files are present. Vitest MUST NOT
  be installed alongside Jest in this spec.
- **FR-011**: `package.json` MUST pin all dependencies to exact versions (`"next": "14.x.x"`,
  not `"^14"`). Dev dependencies MUST also be pinned.
- **FR-012**: This spec MUST NOT implement any authentication logic, real API calls, or
  state management beyond the TanStack Query provider. All pages are static placeholders only.

### Key Entities

- **API Client**: A configured HTTP client instance (Axios or native `fetch` wrapper) that
  applies the base URL, default headers, and request/response interceptors. Exported as a
  singleton from `lib/api/client.ts`. Future auth header injection is added in Phase 3.
- **Root Layout**: `app/layout.tsx` — the top-level layout wrapping all routes. Contains
  the `QueryClientProvider` and any global CSS imports. Does NOT contain any auth logic.
- **Route Group**: Next.js App Router convention. `(auth)` and `(dashboard)` groups share
  layouts within their group without those group names appearing in the URL.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `npm run dev` starts and both `/login` and `/dashboard` render with zero
  console errors within 30 seconds of the command running.
- **SC-002**: `npm run build` succeeds in under 60 seconds with `NEXT_PUBLIC_API_URL` set,
  producing a valid `.next/` output.
- **SC-003**: `npm run lint` reports zero ESLint violations against the scaffold codebase.
- **SC-004**: TypeScript strict mode is active: introducing a type error into any file and
  running `npx tsc --noEmit` produces a type error within 10 seconds.
- **SC-005**: `npm run test` exits with code 0 when no test files exist.
- **SC-006**: The API client correctly uses `NEXT_PUBLIC_API_URL` as its base — verified by
  inspecting the outbound request URL in a test environment.

---

## Assumptions

- Next.js 14 with the App Router is the mandated framework (locked in constitution tech stack).
- TypeScript is used throughout — no JavaScript files in `src/`. `allowJs: false` in
  `tsconfig.json`. The `@/*` path alias MUST be explicitly set in `tsconfig.json` `paths`
  (`"@/*": ["./src/*"]`) and not assumed to be present from `create-next-app` defaults.
- Tailwind CSS v3 is the styling solution. CSS Modules and styled-components are not used.
- TanStack Query v5 is the data fetching and caching solution. SWR is not used.
- The HTTP client library choice (Axios vs. native `fetch` wrapper) is an implementation
  decision made during planning — both are acceptable. The spec requires the abstraction,
  not a specific library.
- No authentication middleware (`middleware.ts`) is implemented in this spec — route
  protection is added in Spec 3.1 (web auth and shell).
- Dark mode, i18n, and analytics are out of scope for this spec.
- `output: "standalone"` MUST NOT be set in `next.config.ts`. Production Docker image optimization
  (standalone output, multi-stage builds) is deferred to Phase 9 hardening to avoid Dockerfile
  mismatches with Spec 0.5.
- The `web/` directory has its own `README.md` explaining how to run the web app locally,
  separate from the root README.

---

## Clarifications

### Session 2026-04-09

- Q: Which test runner should be canonical for the web layer? → A: Jest — use the `create-next-app@14` default Jest config with `--passWithNoTests` added to the test script. Vitest must not be installed in this spec.
- Q: Should `output: "standalone"` be set in `next.config.ts`? → A: No — use default Next.js output. Standalone output requires a different Dockerfile structure; production image optimization is deferred to Phase 9 hardening.
- Q: Should `@/` path alias be explicitly configured or replaced with relative imports? → A: Explicitly configure — add `"@/*": ["./src/*"]` to `tsconfig.json` `paths` in T002 to guarantee the alias regardless of `create-next-app` flag behavior.
