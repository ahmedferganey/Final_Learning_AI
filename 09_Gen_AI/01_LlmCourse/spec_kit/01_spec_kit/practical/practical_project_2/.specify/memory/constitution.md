# GymOS Constitution

## Core Principles

### I. Backend Intelligence Supremacy (NON-NEGOTIABLE)

All training intelligence MUST live exclusively in the FastAPI backend. This is the single most
critical architectural rule in GymOS and overrides all convenience arguments.

**What MUST live in the backend:**
- Progression engine decisions (linear, double progression, wave load, RPE-based)
- Fatigue accumulation model and scoring
- Week type modifiers (deload, refeed, custom load/volume adjustments)
- Expected load and next-load calculations
- Coaching recommendations and rationale
- Personal record detection logic
- Volume and analytics aggregation
- Readiness score computation (composite formula)
- Sync conflict resolution logic

**What MUST NOT live in the frontend (web or mobile):**
- Any calculation that determines what a user should lift
- Any formula that scores fatigue, readiness, or progression status
- Any rule that modifies training based on performance history
- Any PR detection or 1RM estimation

**Rationale:** A divergent frontend implementation — however small — creates two sources of truth.
Users receive different coaching outcomes depending on their client, which is a fundamental product
failure. The backend must be the sole authority so that every client always produces identical
outcomes from identical inputs.

**Compliance check:** Any PR touching a frontend file that contains training logic (load
calculations, fatigue scores, progression decisions) MUST be rejected and reworked.

---

### II. Coaching Engine Versioning (NON-NEGOTIABLE)

Every coaching engine MUST be versioned using semantic versioning. All outputs MUST be traceable
to an exact engine version. Engine behavior MUST NOT be changed in-place — changes require a new
version entry.

**Rules:**
- Each engine module (`progression_engine`, `fatigue_model`, `week_adjustment_engine`,
  `load_calculator`) maintains an active version in the `rule_versions` table.
- Exactly one version per engine is active (`is_active=true`) at any time.
- Activation is atomic: deactivate old → activate new in a single transaction.
- All coaching API responses MUST include `engine_version` and `rule_version_id`.
- `config_snapshot_json` MUST be stored at activation time to allow exact reproduction of
  past decisions.
- MAJOR bump: decision algorithm changes (different output for same input).
- MINOR bump: new progression rule type or configurable parameter added.
- PATCH bump: wording, rationale text, or logging improvements with no behavioral change.

**Rationale:** Athlete training data spans months or years. A user must be able to understand
why a recommendation was made six months ago using the exact logic active at that time.
Versioning also enables safe A/B testing and rollback of bad engine updates.

**Compliance check:** Any coaching engine function that does not carry a `rule_version_id` in
its output MUST be rejected. Any in-place modification of an active engine version (without
creating a new version record) MUST be rejected.

---

### III. Modular Monolith — No Premature Service Extraction

GymOS MUST be developed as a modular monolith through Phase 8. Service extraction into
independent deployables is prohibited until evidence of a specific scaling or team-isolation
need justifies it in Phase 9 or beyond.

**Rules:**
- All backend modules share a single FastAPI process and a single PostgreSQL database.
- Modules are: `auth`, `users`, `training`, `coaching`, `analytics`, `nutrition`,
  `notifications`, `sync`.
- Each module MUST have its own: SQLAlchemy models, Pydantic schemas, service layer, router,
  and test suite.
- Cross-module calls MUST go through service interfaces, never through direct model imports
  from another module's internal layer.
- No message broker (Kafka, RabbitMQ) until Phase 9+ and a documented justification ADR.
- Background jobs use Redis + Celery or RQ — no separate worker service until justified.

**Rationale:** Distributed systems introduce operational complexity (network partitions, eventual
consistency, distributed tracing, independent deployments) that is not warranted before
product-market fit. Module boundaries preserve the future extraction path without paying the
cost now.

**Compliance check:** Any PR that introduces inter-process communication between backend
components (HTTP calls from one "service" to another, message broker setup, separate databases
per module) MUST be rejected unless an ADR approving the extraction has been ratified.

---

### IV. Spec-First Delivery (NON-NEGOTIABLE)

Every meaningful feature, module, or behavioral change MUST begin as a Spec Kit spec. Code MUST
NOT precede specification.

**Rules:**
- The mandatory spec phases are: `specify → plan → tasks → implement`.
- Optional phases that SHOULD be used for ambiguous or high-risk specs: `clarify` (before plan),
  `analyze` (after tasks, before implement), `checklist` (after plan).
- A spec MUST include: Objective, Scope (in/out), Domain Logic, API Endpoints (if applicable),
  Data Models (if applicable), Edge Cases, Dependencies, and Acceptance Criteria.
- A spec is NOT complete without testable Acceptance Criteria.
- Implementation MUST NOT begin until the spec is reviewed, domain logic is documented, and
  acceptance criteria are agreed upon.
- Hot fixes for production-breaking bugs are the only exception; a retroactive spec MUST be
  created within 24 hours.

**Rationale:** GymOS is an intelligence platform with complex, interdependent rules. Undocumented
logic creates divergence between what the product intends and what the code implements.
Spec-first enforces alignment before investment in code.

**Compliance check:** PRs without a linked spec MUST be rejected (except documented hot fixes).
Every spec MUST have at least 3 testable acceptance criteria before planning begins.

---

### V. Test-First Discipline

Testing for GymOS follows a strict pyramid and discipline model. Untested business logic does
not ship.

**Rules:**
- **Coaching engine:** 100% unit test coverage of all decision branches is MANDATORY.
  Every progression rule path, every fatigue level boundary, every week-type modifier MUST have
  a named fixture scenario with defined inputs and expected outputs.
- **Backend integration tests:** MUST use a real PostgreSQL database. No database mocking in
  integration tests. CI provides a real PostgreSQL service container.
- **API contract tests:** Every endpoint MUST have at least one integration test covering the
  happy path and one covering the primary error condition.
- **Frontend (web):** Component tests with React Testing Library. Critical flows (auth, plan
  creation, session logging) MUST have Playwright E2E coverage.
- **Mobile:** Widget tests for the workout logging flow. Offline sync behavior MUST have
  integration test coverage.
- **No domain logic testing on mobile:** Mobile does not contain business logic; therefore,
  mobile tests cover UI behavior and sync correctness only — not training calculations.
- **Test naming convention:** Tests for the coaching engine MUST use descriptive fixture names
  that encode the scenario (e.g., `test_linear_progression_all_sets_completed_increases_load`).

**Rationale:** GymOS makes decisions that directly affect athlete training outcomes. A bug in
the progression engine does not cause a UI glitch — it causes an athlete to train incorrectly.
The cost of a coaching engine error is high; therefore the test coverage standard is higher.

**Compliance check:** PRs touching any file in `backend/app/modules/coaching/engine/` MUST
maintain 100% branch coverage. PRs that reduce test coverage on coaching engine code MUST be
rejected.

---

### VI. API-First Design

The backend API is the product contract between the backend and all clients. API design MUST
precede implementation and MUST be stable across minor releases.

**Rules:**
- All endpoints MUST be versioned under `/api/v1/`.
- All responses MUST use the standard envelopes:
  - Success: `{ "data": {}, "meta": {} }`
  - Error: `{ "error": { "code": str, "message": str, "details": {} } }`
- Pagination MUST use cursor-based pagination. Offset-based pagination is prohibited.
- All mutations MUST return the full updated resource in the response body.
- Breaking API changes (removing fields, changing types, renaming endpoints) require a new API
  version (`/api/v2/`) and a deprecation notice maintained for at least one release cycle.
- API contracts MUST be documented in `docs/api/` before the endpoint is implemented.
- Coaching API responses MUST include `engine_version` and `rule_version_id` in every response.

**Rationale:** Web and mobile clients are developed in parallel. An undocumented or unstable
API creates integration failures across teams. Cursor-based pagination is required because
offset pagination produces incorrect results on live data with concurrent writes.

**Compliance check:** PRs introducing an endpoint without documentation in `docs/api/` MUST be
rejected. PRs that remove or rename response fields in an existing `/v1/` endpoint without a
migration plan MUST be rejected.

---

### VII. Row-Level Security Enforcement

Every data access operation MUST be scoped to the authenticated user. Cross-user data access is
a security violation.

**Rules:**
- Every service method that reads or writes user data MUST accept `user_id` as a required
  parameter and filter ALL queries by it.
- Row-level security is enforced at the **service layer**, not only at the database or route
  level. ORM queries MUST include `.where(Model.user_id == user_id)` explicitly.
- Admin users MAY access other users' data, but every such access MUST be audit-logged with
  `actor_user_id`, `target_user_id`, `action`, and `timestamp`.
- Automated tests MUST verify cross-user isolation: a request authenticated as User A that
  targets User B's resource MUST return 403 or 404, never the actual data.

**Rationale:** GymOS handles personal health, performance, and nutrition data. A row-level
security failure is a privacy breach, not just a bug. Defense in depth at the service layer
ensures that a routing error cannot accidentally expose another user's data.

**Compliance check:** Integration tests MUST include a cross-user isolation test for every
resource type. PRs that introduce a query without `user_id` filtering MUST be rejected
unless the resource is explicitly public (e.g., global exercise library).

---

### VIII. Offline Continuity — Scoped and Reliable

Mobile offline support is scoped precisely. It MUST be reliable within its defined scope and
MUST NOT creep beyond it without a spec.

**Offline scope (v1 — Phase 4):**
- Supported offline: active workout session execution (logging sets while connectivity is lost).
- Not supported offline: plan editing, analytics browsing, nutrition logging, history viewing
  (beyond the most recently cached session).

**Rules:**
- Every offline write operation MUST be assigned a client-generated UUID (`operation_id`) before
  being stored locally.
- The sync queue MUST be processed in `local_timestamp` order on reconnect.
- The server MUST deduplicate by `(user_id, device_id, operation_id)` — replaying a sync queue
  MUST be idempotent.
- Conflict resolution: server is authoritative. Client local data MUST NOT override server state.
- The mobile app MUST display a sync status indicator: `offline`, `syncing`, `synced`, `error`.
- A sync queue cap of 500 operations per device is enforced. If exceeded, the oldest unsynced
  operations are discarded and the user is notified.

**Rationale:** Gyms frequently have poor connectivity. An app that silently loses workout data
during a sync failure destroys user trust. The scoped offline model is deliberately limited in
v1 to ensure the in-gym execution path is rock-solid before expanding offline coverage.

**Compliance check:** Any spec proposing to expand offline scope beyond active session execution
MUST explicitly document the conflict resolution strategy and idempotency model before approval.

---

### IX. Security by Default

Security controls are not optional additions to be addressed at launch. They MUST be built
into every feature from the start.

**Non-negotiable controls:**
- **Authentication:** JWT (RS256) with 15-minute access token TTL. Refresh tokens rotate on
  every use. Reuse detection triggers full session revocation.
- **Password storage:** bcrypt with cost factor ≥ 12. Plaintext passwords MUST never appear
  in logs, error messages, or database fields.
- **Rate limiting:** Auth endpoints: 10 failed attempts per IP per 15 minutes → 429 + temporary
  IP block. All API endpoints: 1,000 req/min per authenticated user.
- **Input validation:** All request bodies MUST use Pydantic strict mode. Maximum request body
  size: 1MB.
- **CORS:** Production MUST enforce an allowlist of known origins only. Wildcard `*` CORS
  is prohibited in any deployed environment.
- **Secrets:** Secrets MUST be provided via environment variables. No secrets in code, config
  files committed to version control, or log output. `detect-secrets` pre-commit hook is
  mandatory.
- **HTTPS:** All external traffic terminates TLS at Nginx. The backend process MUST NOT be
  exposed directly to public traffic.
- **Dependency auditing:** `pip-audit` (backend) and `npm audit` (web) MUST pass with 0
  high/critical findings before any production release.

**Rationale:** GymOS stores personal health data, training performance history, and nutrition
logs. A security failure is a privacy incident affecting real users. Security controls built
in from Phase 1 cost a fraction of what a retrofit costs.

**Compliance check:** PRs that introduce hardcoded secrets, disabled CORS restrictions,
unbounded input, or plaintext password handling MUST be rejected immediately.

---

### X. Observability is Operational Debt Prevention

Every feature MUST include the logging and error reporting necessary to operate it in production.
Observability is not a Phase 9 concern — it is a Phase 2 concern.

**Rules:**
- **Error tracking:** Sentry MUST be integrated in backend, web, and mobile from Phase 2.
  All unhandled exceptions MUST be captured with user context (user_id, NOT PII like email).
- **Structured logging:** All backend logs MUST be structured JSON. Log fields MUST include:
  `timestamp`, `level`, `module`, `event`, `user_id` (when applicable), `trace_id`.
- **Audit trail:** All mutations to training plans, session logs, and coaching decisions MUST
  be written to the `audit_log` table.
- **Health check:** `GET /api/v1/health` MUST return 200 with DB and Redis connectivity status.
  A degraded status (DB down) MUST return 503.
- **Background jobs:** All job executions MUST log: start time, end time, records processed,
  errors encountered.
- **No PII in logs:** Email addresses, names, and phone numbers MUST NOT appear in log output.
  Use `user_id` (UUID) as the user identifier in all log entries.

**Rationale:** GymOS will be used by athletes during workouts — uptime matters. An unobservable
system means production failures are discovered by users before engineers. Structured logs
enable automated alerting and fast incident response.

**Compliance check:** PRs introducing a new service, endpoint, or background job that does not
include Sentry integration and structured logging MUST be rejected.

---

## Architecture Constraints

### Technology Stack (Locked — ADR Required to Change)

Changes to the core technology stack require a written ADR in `docs/decisions/` that is
approved before implementation begins.

| Layer | Technology | Locked |
|---|---|---|
| Backend language | Python 3.11+ | Yes |
| Backend framework | FastAPI | Yes |
| ORM | SQLAlchemy (async) | Yes |
| Migrations | Alembic | Yes |
| Validation | Pydantic v2 | Yes |
| Primary database | PostgreSQL | Yes |
| Cache / queue | Redis | Yes |
| Background jobs | Celery or RQ (Redis-backed) | Yes |
| Web framework | Next.js 14 (App Router) | Yes |
| Web language | TypeScript (strict mode) | Yes |
| Mobile framework | Flutter | Yes |
| Mobile state | Riverpod | Yes |
| Mobile HTTP | Dio | Yes |
| Mobile local storage | Hive or Drift | Yes |
| Container | Docker | Yes |

### Data Model Rules

- All schema changes MUST be implemented via Alembic migrations. Direct DDL against the
  database is prohibited in all environments except local throwaway setups.
- All migrations MUST be backwards-compatible (additive only) until the column/table is
  confirmed safe to drop in a subsequent release.
- Dropping a column or table requires two releases: first release marks it as deprecated
  (stop writing to it); second release drops it.
- `user_id` foreign keys MUST use UUID type. Auto-increment integer IDs are prohibited for
  user-facing resource identifiers.
- All tables MUST have `created_at` (timestamp with timezone). Mutable tables MUST also have
  `updated_at`.

### Module Boundary Rules

- A module's internal models MUST NOT be imported by another module's service or router.
- Cross-module data access goes through the service interface of the owning module.
- Shared enums, types, and utilities live in `backend/app/shared/` and are the only cross-module
  imports permitted outside of the module's public service interface.

---

## Quality Gates

### Definition of Done

A spec is NOT done until ALL of the following are true:

- [ ] All API endpoints return correct responses — verified by integration tests against a real
      PostgreSQL database.
- [ ] All coaching engine decision branches have unit test coverage — 100% branch coverage
      verified by CI.
- [ ] Database migrations created, backwards-compatible, and reviewed.
- [ ] API contract documented in `docs/api/` before the first integration test runs.
- [ ] Sentry integration active and error capture verified for all new service code.
- [ ] Structured logging added to all new service methods and background jobs.
- [ ] Edge cases documented in the spec are covered by tests.
- [ ] All acceptance criteria in the spec are passing.
- [ ] PR reviewed and approved by at least one engineer.
- [ ] `ruff`, `mypy`, `eslint`, and `flutter analyze` pass with zero violations.

### Performance Targets (Non-Negotiable for Production Release)

| Endpoint category | p95 latency target |
|---|---|
| Training CRUD endpoints | < 200ms |
| Coaching decision endpoints | < 500ms |
| Analytics endpoints | < 1,000ms |
| Auth endpoints | < 300ms |

Any production release that cannot demonstrate these targets under a 500-concurrent-user load
test MUST NOT be promoted until the regression is resolved.

### Code Quality Standards

- **Python:** `ruff` for linting, `mypy` in strict mode for type checking. Zero violations
  permitted in CI.
- **TypeScript:** `eslint` with `@typescript-eslint/strict` ruleset, `tsc --noEmit` in strict
  mode. Zero violations permitted in CI.
- **Flutter:** `flutter analyze` with zero violations permitted in CI.
- **No `any` types** in TypeScript without an explicit `// eslint-disable` comment with
  justification.
- **No untyped function signatures** in Python — all public service functions MUST carry full
  type annotations.

---

## Security Requirements

### Authentication & Authorization

- JWT MUST use RS256 (asymmetric signing). HS256 is prohibited for user-facing tokens.
- Access token TTL: 15 minutes. Refresh token TTL: 30 days, rotating.
- Refresh token reuse detection MUST be implemented: if a revoked token is presented, ALL tokens
  for that user MUST be revoked immediately.
- Every protected endpoint MUST verify token validity, user `is_active` status, and role
  permissions before executing any business logic.
- Admin endpoints MUST be tested with a non-admin token to verify 403 rejection.

### Data Protection

- Passwords: bcrypt, cost factor ≥ 12. No alternatives.
- No PII (email, name, DOB) in log output.
- Health data (readiness scores, body weight, nutrition) is user-private data. Row-level
  security applies. No analytics aggregation that could identify an individual.
- Device tokens for push notifications MUST be stored hashed or encrypted at rest.

### Secrets Management

- All secrets via environment variables. `.env` files MUST be in `.gitignore`.
- `.env.example` MUST exist with placeholder values and comments for every required variable.
- Production secrets rotation procedure MUST be documented before Phase 9 release.
- JWT private key rotation: issue new tokens with new key; retain old key for validation
  until the access token TTL (15 min) expires, then decommission.

---

## Development Workflow

### Branch Strategy

- `main`: production-ready code only. Direct commits prohibited.
- `feature/<spec-id>-<short-name>`: all feature work. Created by Spec Kit `create-new-feature`
  script.
- `fix/<short-name>`: hot fixes to production-breaking bugs only.
- `release/<version>`: release preparation branches.

### PR Requirements

- Every PR MUST reference a Spec Kit spec (spec ID in the PR title or description).
- PRs MUST be small and reviewable (< 500 lines of diff excluding generated code and migrations).
  Large PRs MUST be split by spec boundary.
- PRs MUST include: what changed, why it changed, how to test it, and the spec link.
- CI MUST pass before a PR can be merged. Green CI is a floor, not a gate that overrides review.
- At least one approval is required. Self-merge is prohibited.

### Commit Convention

All commits MUST follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

Types: feat, fix, docs, refactor, test, chore, perf
Scope: auth, training, coaching, analytics, nutrition, notifications, sync, web, mobile, infra
```

### ADR (Architecture Decision Record) Policy

Any decision that changes the technology stack, module boundaries, API versioning strategy,
coaching engine versioning model, or offline sync model MUST be documented as an ADR in
`docs/decisions/` before implementation begins. ADRs are never deleted — superseded ADRs are
marked `status: superseded` and linked to the superseding ADR.

---

## Governance

### Constitution Authority

This constitution is the highest-level governance document for GymOS engineering. It supersedes
all other practices, conventions, and individual preferences where there is a conflict.

In case of conflict between this constitution and a spec, the constitution wins and the spec
MUST be updated before implementation proceeds.

### Compliance Review

Every PR review MUST include a constitution compliance check. Reviewers MUST explicitly verify:
- No business logic in frontend
- Coaching outputs include `rule_version_id` (if coaching is involved)
- Row-level security enforced in all new queries
- Migrations are backwards-compatible
- Tests meet the required coverage standards for the affected module

### Amendment Procedure

1. Propose the amendment in writing — include the principle being changed, the reason, and
   the migration plan for any existing code that violates the new rule.
2. Require approval from at least two engineers (or the project lead on a solo project, with
   a documented self-review).
3. Update this file with a MINOR or MAJOR version bump:
   - PATCH: clarifications, wording, examples — no behavioral change.
   - MINOR: new principle or section added.
   - MAJOR: existing non-negotiable principle removed or fundamentally redefined.
4. Update `LAST_AMENDED_DATE`.
5. Propagate the change to affected spec templates, plan templates, and task templates.
6. Commit with message: `docs: amend constitution to vX.Y.Z (<summary of change>)`

### Deferred Items

The following items are intentionally out of scope for the current constitution version and will
be addressed in a future amendment when the corresponding phases are reached:

- Coach-athlete relationship model and permissions (post-Phase 4)
- Multi-region deployment constraints (post-Phase 9)
- AI/ML model governance (when AI integration is specced)
- GDPR / data deletion compliance specifics (Phase 9+)
- Real-time collaboration constraints (post-Phase 9)

---

**Version**: 1.0.0 | **Ratified**: 2026-04-09 | **Last Amended**: 2026-04-09
