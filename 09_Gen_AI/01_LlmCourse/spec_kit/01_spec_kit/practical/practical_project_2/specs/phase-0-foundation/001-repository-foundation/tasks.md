# Tasks: Repository Foundation

**Input**: `specs/phase-0-foundation/001-repository-foundation/`
**Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md) | **Research**: [research.md](research.md)
**Data model**: [data-model.md](data-model.md) | **Quickstart**: [quickstart.md](quickstart.md)

> **For LLM agents**: Every task description is self-contained. The required file content,
> required sections, and key text are specified inline — do not invent content that is not
> listed. No application code is created anywhere in this task list. All outputs are Markdown
> or plain-text config files. ADR `status` must be set to `proposed` (not `accepted`) —
> advancement to `accepted` requires a human GitHub PR approval and is outside LLM scope.

---

## Phase 1: Setup — Directory Skeleton & Tooling Config

**Purpose**: Create the bare repository structure and the two tooling files that all subsequent
tasks depend on. Complete this phase fully before starting any user story phase.

- [X] T001 Create six top-level directories with `.gitkeep` placeholder files so Git tracks them after a fresh clone (FR-001). Run: `mkdir -p backend web mobile infra docs/decisions specs && touch backend/.gitkeep web/.gitkeep mobile/.gitkeep infra/.gitkeep docs/decisions/.gitkeep specs/.gitkeep`. Verify with `ls` that all six directories exist at repo root.

- [X] T002 Create `.gitignore` at repo root (FR-008). The file MUST contain exactly three labeled sections. Write the following content verbatim:

  ```
  # Python
  __pycache__/
  *.py[cod]
  *.pyo
  *.pyd
  .Python
  env/
  venv/
  .venv/
  *.egg-info/
  dist/
  build/
  .pytest_cache/
  .mypy_cache/
  .ruff_cache/
  .coverage
  htmlcov/

  # Node.js / Next.js
  node_modules/
  .next/
  out/
  *.tsbuildinfo
  .npm
  .eslintcache

  # Flutter / Dart
  .dart_tool/
  .flutter-plugins
  .flutter-plugins-dependencies
  build/

  # Secrets — never commit these
  .env
  .env.local
  .env.*.local
  .secrets.baseline.bak
  ```

- [X] T003 Initialize `.secrets.baseline` at repo root (FR-010, SC-005). Run: `pip install detect-secrets && detect-secrets scan > .secrets.baseline`. This file MUST be committed to the repository. It stores the empty baseline that CI will compare against on every PR. If `pip` is unavailable, create the file manually with content `{"version": "1.4.0", "plugins_used": [], "filters_used": [], "results": {}, "generated_at": "2026-04-09T00:00:00Z"}` as a fallback.

**Checkpoint — Phase 1**: Run `ls` at repo root and confirm: `backend/`, `web/`, `mobile/`, `infra/`, `docs/`, `specs/`, `.gitignore`, `.secrets.baseline` all exist.

---

## Phase 2: Foundational

No blocking foundational phase for this spec — Phase 1 produces all prerequisites.
Proceed to user story phases immediately after Phase 1 checkpoint passes.

---

## Phase 3: User Story 1 — New Engineer Onboards Without Help (Priority: P1) 🎯 MVP

**Goal**: A new engineer clones the repo, reads only `README.md` and `CONTRIBUTING.md`, and can
answer four questions without asking anyone: (1) What is GymOS? (2) Where does backend code live?
(3) Where do mobile workout screens go? (4) What is the branch naming convention?

**Independent test** (SC-001): Clone to a fresh directory → read only `README.md` and
`CONTRIBUTING.md` → answer the four questions above → all must be answerable from those two files.

- [X] T004 [P] [US1] Create `README.md` at repo root (FR-002). The file MUST contain all five sections below with this exact content structure:

  **Section 1 — Project title and tagline**
  ```
  # GymOS

  An adaptive training intelligence platform — not a workout tracker.
  GymOS dynamically adjusts load, volume, and structure based on real performance data,
  models fatigue across sessions, and applies structured progression algorithms
  (linear, double progression, wave, RPE-based).
  ```

  **Section 2 — Client Surfaces** (Markdown table, 3 rows)
  | Surface | Technology | Best for |
  |---|---|---|
  | Backend | FastAPI (Python 3.11+) | All business logic, coaching engine, data authority |
  | Web | Next.js 14 (TypeScript) | Plan design, analytics, history, deep editing, settings |
  | Mobile | Flutter | In-gym execution, set logging, rest timer, offline capture |

  **Section 3 — Technology Stack** (bulleted list)
  - Backend: FastAPI · Python 3.11+ · SQLAlchemy (async) · Alembic · Pydantic v2
  - Database: PostgreSQL (primary) · Redis (cache + job queue)
  - Web: Next.js 14 (App Router) · TypeScript (strict mode)
  - Mobile: Flutter · Riverpod · Dio · Hive/Drift
  - Infrastructure: Docker

  **Section 4 — Directory Layout** (code block tree)
  ```
  gymos/
  ├── backend/    FastAPI application code
  ├── web/        Next.js application code
  ├── mobile/     Flutter application code
  ├── infra/      Docker, CI, infrastructure config
  ├── docs/       Architecture docs, ADRs, API contracts
  └── specs/      Spec Kit feature specifications
  ```

  **Section 5 — Getting Started** (two bullet points)
  - See `CONTRIBUTING.md` for branch strategy, commit conventions, and PR process.
  - See `specs/` for all feature specifications organized by phase.

- [X] T005 [P] [US1] Create `CONTRIBUTING.md` at repo root (FR-003, FR-010; also satisfies US3 SC-001). The file MUST contain all six sections below:

  **Section 1 — Branch Naming** (FR-003)
  ```
  ## Branch Naming

  Format: `feature/<spec-id>-<short-name>`

  Examples:
  - `feature/001-repository-foundation`
  - `feature/002-backend-scaffold`
  - `fix/short-description`
  - `release/1.0.0`

  Branches are created per spec. One spec = one branch = one PR.
  ```

  **Section 2 — Commit Convention** (FR-003; satisfies US3 in full)
  ```
  ## Commit Convention

  All commits MUST follow [Conventional Commits](https://www.conventionalcommits.org/):

  Format: `<type>(<scope>): <description>`

  Permitted types: feat, fix, docs, refactor, test, chore, perf

  Permitted scopes: auth, training, coaching, analytics, nutrition,
  notifications, sync, web, mobile, infra

  Valid examples:
  - `feat(auth): add JWT login endpoint`
  - `docs(specs): add spec 0.2 backend scaffold`
  - `chore(infra): update Docker base image to python 3.11`

  Invalid examples (DO NOT USE):
  - `updated stuff` — missing type, scope, and description format
  - `fixed bug` — missing type and scope
  ```

  **Section 3 — PR Process** (FR-003)
  ```
  ## PR Process

  - PRs MUST reference a spec ID in the title or description.
  - Keep PRs small and reviewable (< 500 lines of diff, excluding generated code and migrations).
  - CI must pass before a PR can be merged.
  - At least 1 approving review is required. Self-merge is prohibited.
  - Use the PR template — fill all four sections (what changed, why, how to test, spec link).
  ```

  **Section 4 — ADR Creation Process** (FR-003)
  ```
  ## Creating an Architecture Decision Record (ADR)

  1. Copy `docs/decisions/adr-template.md` to `docs/decisions/NNN-short-name.md`
     where NNN is the next available zero-padded number (e.g., `003-...`).
  2. Fill in all sections of the template.
  3. Set `status: proposed`.
  4. Open a PR with the new ADR file.
  5. Obtain at least 1 approving review from a team member other than the author.
  6. On merge, update `status: accepted`.
  7. ADRs are immutable once accepted. Only `status` may change post-acceptance
     (to `superseded` if a replacement ADR is ratified).

  Numbering collision: if two engineers create an ADR simultaneously, the second
  must be renumbered before merging.
  ```

  **Section 5 — Secret Scanning** (FR-010)
  ```
  ## Secret Scanning

  `detect-secrets` is mandatory. Install it: `pip install detect-secrets`

  Before committing: `detect-secrets scan --baseline .secrets.baseline`

  The CI pipeline runs this scan automatically on every PR and will block merge
  if unacknowledged secrets are found.

  To acknowledge a false positive:
  `detect-secrets audit .secrets.baseline`
  Then commit the updated `.secrets.baseline`.
  ```

  **Section 6 — Reviewing the Spec** (brief pointer)
  ```
  ## Spec-Driven Development

  Every feature begins as a spec in `specs/`. Implementation MUST NOT begin
  before the spec is reviewed and acceptance criteria are agreed upon.
  See `Plan.md` at the repository root for the full phase and spec breakdown.
  ```

- [X] T006 [P] [US1] Create `.github/pull_request_template.md` (FR-004). The file MUST contain exactly this content — do not add or remove sections:

  ```markdown
  <!-- Fill all four sections. PRs missing a spec link will not be reviewed. -->

  ## What changed

  <!-- Describe the change clearly. What did you add, remove, or modify? -->

  ## Why

  <!-- What problem does this solve? What requirement or spec drives this change? -->

  ## How to test

  <!-- Numbered steps to verify the change works as intended. -->
  1.
  2.
  3.

  ## Spec link

  <!-- Paste the path to the spec file, e.g.: specs/phase-0-foundation/001-repository-foundation/spec.md -->
  ```

**Checkpoint — US1 complete**: Read only `README.md` and `CONTRIBUTING.md`. Confirm all four
onboarding questions are answered: purpose ✓, backend directory ✓, mobile directory ✓,
branch naming convention ✓. Confirm PR template has all four required sections.

---

## Phase 4: User Story 2 — Architecture Decisions Are Traceable (Priority: P2)

**Goal**: Any team member can read the two ADR files and understand why GymOS chose a modular
monolith and the current technology stack, including what alternatives were considered and what
conditions would trigger revisiting each decision.

**Independent test** (SC-002, US2 acceptance scenarios):
- Read `docs/decisions/001-modular-monolith.md` → find: decision, microservices rejected with rationale, conditions for revisiting.
- Read `docs/decisions/002-stack-selection.md` → find: each technology choice with rationale, alternatives considered.
- Read both in sequence → confirm no contradictions.

- [X] T007 [P] [US2] Create `docs/decisions/adr-template.md` (FR-005). The file MUST contain placeholder instructions in each section so a future engineer knows exactly what to write:

  ```markdown
  # ADR NNN: [Title — describe the decision, not the outcome]

  **Status**: proposed
  <!-- Change to `accepted` after PR approval; `superseded` if replaced by a later ADR -->

  **Date**: YYYY-MM-DD

  ## Context

  <!-- Describe the forces, constraints, and background that make this decision necessary.
       What is the problem being solved? What are the relevant tradeoffs? -->

  ## Decision

  <!-- State the decision clearly and decisively. Start with "We will..." or "GymOS will..."
       Be specific: name the technology, pattern, or rule being adopted. -->

  ## Consequences

  **Positive:**
  <!-- List the benefits of this decision. -->

  **Negative / Tradeoffs:**
  <!-- List the costs or limitations accepted by making this decision. -->

  ## Alternatives Considered

  <!-- List at least one alternative that was evaluated and rejected.
       For each: name it, and explain why it was rejected in 1–2 sentences. -->

  | Alternative | Reason rejected |
  |---|---|
  | [Alternative A] | [Why rejected] |

  ## Superseded By

  <!-- Leave blank unless this ADR is superseded. If superseded, add:
       Superseded by [ADR NNN: Title](NNN-short-name.md) -->
  ```

- [X] T008 [US2] Create `docs/decisions/001-modular-monolith.md` (FR-006). Use `docs/decisions/adr-template.md` as the structural template. Set `status: proposed`. Write the following content in each section:

  **Title**: `ADR 001: Use a Modular Monolith Architecture`

  **Context section**: GymOS has eight backend modules (auth, users, training, coaching,
  analytics, nutrition, notifications, sync) that share a single data model and must call
  each other frequently. The team is pre-product-market fit with a small codebase. Distributed
  systems add network partitions, independent deployments, distributed tracing complexity, and
  eventual consistency concerns that are not warranted at this stage.

  **Decision section**: GymOS will be developed as a modular monolith through Phase 8. All
  backend modules share a single FastAPI process and a single PostgreSQL database. Each module
  has its own SQLAlchemy models, Pydantic schemas, service layer, router, and test suite.
  Cross-module calls go through the owning module's service interface — never via direct
  model imports from another module's internal layer.

  **Consequences — Positive**: Simpler deployment (single process), simpler debugging (no
  network hops between components), straightforward testing (no distributed test infrastructure),
  clear module boundaries that preserve a future extraction path to microservices if needed.

  **Consequences — Negative/Tradeoffs**: Horizontal scaling applies to the entire application,
  not individual modules. A bug in one module can bring down all modules. Future extraction to
  microservices will require interface cleanup if boundaries drift.

  **Alternatives Considered table** (at minimum these two rows):
  | Alternative | Reason rejected |
  |---|---|
  | Microservices from day one | Adds network partitions, distributed tracing, independent deployment pipelines, and eventual consistency concerns not warranted before product-market fit |
  | Serverless functions | Stateless model poorly suited to long-running coaching calculations; cold starts unacceptable for in-gym use; harder to test locally |

  **Conditions for revisiting** (add as a final paragraph under Decision or Consequences):
  This decision should be revisited if: (a) a specific module requires per-module horizontal
  scaling that cannot be achieved by vertical scaling the monolith, or (b) team growth creates
  deployment coordination friction that module isolation would solve.

- [X] T009 [US2] Create `docs/decisions/002-stack-selection.md` (FR-007). Use `docs/decisions/adr-template.md` as the structural template. Set `status: proposed`. Write the following content:

  **Title**: `ADR 002: Technology Stack Selection`

  **Context section**: GymOS requires three surfaces: a backend API with complex domain logic
  (coaching engine, progression algorithms, fatigue modeling), a web dashboard for plan editing
  and analytics, and a mobile app for in-gym use with offline capability. All surfaces must
  share data through a single authoritative backend. The stack must support strong typing,
  async I/O for the backend, offline-first mobile, and containerized deployment.

  **Decision section** (list each layer):
  - Backend language/framework: Python 3.11+ with FastAPI (async, type-annotated, Pydantic v2 request validation)
  - ORM: SQLAlchemy async with Alembic for migrations
  - Primary database: PostgreSQL (ACID guarantees, complex analytics queries, row-level security)
  - Cache and job queue: Redis (session cache, rate limit counters, offline sync queue, background jobs)
  - Background jobs: Celery or RQ (Redis-backed)
  - Web framework: Next.js 14 (App Router), TypeScript strict mode
  - Mobile framework: Flutter (Dart), Riverpod for state management, Dio for HTTP, Hive or Drift for local storage
  - Containers: Docker for all services

  **Consequences — Positive**: Well-established ecosystems with strong community support.
  Strong typing across all layers (Python mypy + TypeScript + Dart). FastAPI's Pydantic
  validation enforces contracts at the API boundary. Flutter's offline/local-storage
  capabilities are well-suited to in-gym use.

  **Consequences — Negative/Tradeoffs**: Three separate codebases (Python, TypeScript, Dart)
  require expertise across all three languages. Flutter/Dart ecosystem is smaller than React Native.
  PostgreSQL requires a running database for all integration tests.

  **Alternatives Considered table** (at minimum these rows):
  | Alternative | Reason rejected |
  |---|---|
  | Node.js/Express for backend | Less ergonomic for complex domain logic; Pydantic-style runtime validation not native |
  | React Native for mobile | Flutter performance and offline storage (Hive/Drift) better suited for in-gym use |
  | MongoDB for primary DB | Lacks ACID transactions needed for coaching decision auditability; weaker analytics query support |
  | SQLite for primary DB | Insufficient for multi-user concurrent writes and complex analytics |

  **No Superseded By entry** — leave blank.

**Checkpoint — US2 complete**: Open both ADR files. Verify each follows the template, contains
no placeholder text (`NNN`, `YYYY-MM-DD`, `[Title]`), and that the two ADRs do not contradict
each other (e.g., ADR 001 says modular monolith; ADR 002 confirms single PostgreSQL database —
these are consistent).

---

## Phase 5: User Story 3 — Commit History Is Consistent From Day One (Priority: P3)

**Goal**: The Conventional Commits standard is documented in `CONTRIBUTING.md` with the exact
format, all permitted types, all permitted scopes, and at least two valid examples, so any
engineer can identify valid vs. invalid commit messages without asking for help.

**Independent test** (US3 acceptance scenarios):
- Read `CONTRIBUTING.md` commit section → find: format string, types list, scopes list, 2+ examples.
- Confirm `feat(auth): add JWT login endpoint` matches the documented format.
- Confirm `updated stuff` is identifiably invalid (missing type, scope, and format).

- [X] T010 [US3] Audit the `CONTRIBUTING.md` commit convention section created in T005. Verify it contains all five required elements: (1) the format string `<type>(<scope>): <description>`, (2) a list of permitted types including at minimum `feat fix docs refactor test chore perf`, (3) a list of permitted scopes including at minimum `auth training coaching analytics nutrition notifications sync web mobile infra`, (4) at least two valid commit message examples including `feat(auth): add JWT login endpoint`, (5) at least one invalid example such as `updated stuff` to make the standard unambiguous. If any element is missing, update `CONTRIBUTING.md` to add it. No new file is created — this is an audit-and-patch task only.

**Checkpoint — US3 complete**: Re-read `CONTRIBUTING.md` commit section. Confirm all five
elements are present. `feat(auth): add JWT login endpoint` is valid; `updated stuff` is
clearly invalid against the documented rules.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T011 Run `detect-secrets scan --baseline .secrets.baseline` from repo root and confirm exit 0 with no unacknowledged findings (SC-005). If any findings appear, run `detect-secrets audit .secrets.baseline` to review — mark as false positive if appropriate, then commit the updated `.secrets.baseline`.

- [X] T012 Verify full directory structure by running `ls` at repo root and confirming these all exist: `backend/`, `web/`, `mobile/`, `infra/`, `docs/`, `specs/`, `README.md`, `CONTRIBUTING.md`, `.gitignore`, `.secrets.baseline`, `.github/pull_request_template.md` (SC-003, FR-001).

- [X] T013 [P] Spot-check `.gitignore` covers all three stacks (FR-008): confirm `node_modules/` is listed (Node), `__pycache__/` is listed (Python), `.dart_tool/` is listed (Flutter/Dart). Open `.gitignore` and scan — if any are missing, add them.

- [X] T014 [P] Cross-check ADR consistency (Edge Case from spec): read `docs/decisions/001-modular-monolith.md` and `docs/decisions/002-stack-selection.md` in sequence and confirm no contradictions. Specifically: ADR 001 states single deployment unit → ADR 002 must not propose separate databases per module. If a contradiction is found, update the offending section and add a note in the spec Edge Cases section.

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
  └─► Phase 3 (US1)   — needs directory structure from T001
  └─► Phase 4 (US2)   — needs docs/decisions/ directory from T001
      └─► T008, T009 depend on T007 (ADR template must exist first)
  └─► Phase 5 (US3)   — depends on T005 (CONTRIBUTING.md must exist)
        └─► Phase 6 (Polish) — needs all phases complete
```

### User Story Dependencies

- **US1 (P1)**: Start after Phase 1 — no dependency on US2 or US3
- **US2 (P2)**: Start after Phase 1 — fully parallel with US1 (different files)
- **US3 (P3)**: Depends on T005 from US1 — audit-and-patch only, no new file
- **Polish**: Start after US1, US2, US3 all complete

### Within Each Phase

| Tasks | Order |
|---|---|
| T001, T002, T003 | Sequential — T003 needs clean state from T001/T002 |
| T004, T005, T006 | Parallel — independent files |
| T007 | Must complete before T008 and T009 |
| T008, T009 | Parallel after T007 |
| T010 | Sequential after T005 |
| T011, T012 | Sequential verifications |
| T013, T014 | Parallel with each other |

---

## Parallel Execution Examples

### Phase 3 (US1) — three independent files:

```
Launch simultaneously:
  T004 → Write README.md
  T005 → Write CONTRIBUTING.md
  T006 → Write .github/pull_request_template.md
```

### Phase 4 (US2) — template first, then both ADRs in parallel:

```
Sequential then parallel:
  T007 → Write docs/decisions/adr-template.md  ← complete first
  Then launch simultaneously:
    T008 → Write docs/decisions/001-modular-monolith.md
    T009 → Write docs/decisions/002-stack-selection.md
```

---

## Implementation Strategy

### MVP (US1 only — minimum for engineer onboarding)

1. Complete Phase 1 (T001, T002, T003)
2. Complete Phase 3 (T004, T005, T006)
3. Run SC-001 independent test — all four questions answered from docs alone
4. **Stop and validate** before adding US2/US3

### Incremental Delivery

1. Phase 1 + Phase 3 (US1) → Onboarding ready
2. Phase 4 (US2) → ADRs documented, architectural decisions traceable
3. Phase 5 (US3) → Commit standard enforced from day one
4. Phase 6 (Polish) → All acceptance criteria verified, SC-001 through SC-005 pass

### Parallel Team (two engineers)

After Phase 1 completes:
- Engineer A: T004, T005, T006 (US1 — onboarding docs)
- Engineer B: T007, T008, T009 (US2 — ADRs)
Both finish before Phase 5 and Phase 6 begin.

---

## Notes for LLM Agents

- **No application code** — every task produces only Markdown or plain-text config files
- **Content is fully specified** — use the inline task descriptions as the authoritative source for what to write; do not invent sections that are not listed
- **ADR status** — write `status: proposed` in both ADR files; advancing to `accepted` requires a human GitHub PR approval and is outside LLM scope
- **Commit message** to use after completing each phase:
  - After Phase 1: `chore(infra): initialize repository skeleton and tooling config`
  - After Phase 3: `docs(infra): add README, CONTRIBUTING, and PR template`
  - After Phase 4: `docs(infra): add ADR template and founding architecture decisions`
  - After Phase 5+6: `docs(infra): verify commit convention and repository acceptance criteria`
- **Do not add** Turborepo, Nx, Docker Compose, GitHub Actions, or any application scaffold — those are Specs 0.2–0.5
- **Reference** `specs/phase-0-foundation/001-repository-foundation/spec.md` FR-XXX entries if any task requirement is ambiguous
