# GymOS — Production Engineering Plan

---

## 1. Executive Summary

GymOS is a production-grade, adaptive training intelligence platform designed to replace static workout tracking with a dynamic coaching system that responds to user performance, fatigue, and progression trends in real time.

This document defines the complete engineering plan for GymOS: architecture, domain model, API strategy, offline sync, security, observability, testing, deployment, and a fully decomposed Spec Kit implementation plan broken into 10 phases and 45+ specs.

**Stack:** FastAPI (Python) · Next.js (TypeScript) · Flutter · PostgreSQL · Redis  
**Methodology:** Spec-driven development via Spec Kit  
**Architecture:** Modular monolith backend, multi-platform frontends  
**Delivery model:** Phase-gated, spec-per-slice, test-first

---

## 2. Product Vision

GymOS is not a workout tracker. It is an **adaptive training intelligence platform** that:

- Dynamically adjusts load, volume, and structure based on real performance data
- Models fatigue across sessions and weeks to prevent overtraining
- Applies structured progression algorithms (linear, double progression, wave, RPE-based)
- Translates a training philosophy into deterministic, versioned, auditable coaching rules
- Serves athletes across two surfaces: deep editing and analytics on web, in-gym execution on mobile

### User personas

**The self-coached athlete** — needs structured plans, auto-progression, and performance visibility without a human coach.

**The coached athlete** — coach uses web to program, athlete executes on mobile. Sync and accuracy are critical.

**The performance analyst** — reviews volume trends, muscle distribution, PR progression, and adherence over time.

### Primary product surfaces

| Surface | Best for |
|---|---|
| Web (Next.js) | Plan design, analytics, history, deep editing, settings |
| Mobile (Flutter) | In-gym execution, set logging, timers, offline capture, readiness |
| Backend (FastAPI) | All business logic, coaching engine, data authority, API |

---

## 3. System Architecture

### 3.1 Architecture Decision: Modular Monolith

GymOS starts as a **modular monolith** — not microservices. Modules have clean internal boundaries but share a single deployment unit.

**Rationale:**
- Simpler deployment, debugging, and testing at early stage
- Avoids distributed systems complexity before product-market fit
- Module boundaries preserve future extraction path to services if needed
- FastAPI's router system maps cleanly to module boundaries

### 3.2 Full Architecture Diagram

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT LAYER                                    │
│                                                                              │
│   ┌─────────────────────────┐          ┌─────────────────────────┐          │
│   │       Web App           │          │       Mobile App         │          │
│   │  Next.js + TypeScript   │          │        Flutter           │          │
│   │  - Plan editor          │          │  - Active workout flow   │          │
│   │  - Analytics dashboard  │          │  - Set/rep/load logging  │          │
│   │  - History viewer       │          │  - Rest timer            │          │
│   │  - Settings             │          │  - Offline session cache │          │
│   │  - Deep plan editing    │          │  - Readiness input       │          │
│   └────────────┬────────────┘          └────────────┬────────────┘          │
└────────────────┼────────────────────────────────────┼──────────────────────┘
                 │ HTTPS/REST                          │ HTTPS/REST + Sync Queue
                 │                                     │
┌────────────────▼─────────────────────────────────────▼──────────────────────┐
│                           API GATEWAY / NGINX                                │
│                    (TLS termination, rate limiting, routing)                 │
└────────────────────────────────┬─────────────────────────────────────────────┘
                                 │
┌────────────────────────────────▼─────────────────────────────────────────────┐
│                        FASTAPI APPLICATION SERVER                            │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │     auth     │  │    users     │  │   training   │  │   coaching   │    │
│  │  JWT/refresh │  │ profile/prefs│  │ plans/logs   │  │ progression  │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  analytics   │  │  nutrition   │  │notifications │  │    sync      │    │
│  │ PRs/trends   │  │macros/recov. │  │ push/remind  │  │ offline ops  │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    COACHING ENGINE (versioned)                       │    │
│  │  progression_engine_v1 │ fatigue_model_v1 │ week_adjustment_v1      │    │
│  │  load_calculator_v1    │ rule_engine_v1   │ recommendation_v1        │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└────────────────────────────────┬─────────────────────────────────────────────┘
                                 │
              ┌──────────────────┴──────────────────┐
              │                                     │
┌─────────────▼───────────────┐      ┌──────────────▼──────────────┐
│         PostgreSQL           │      │            Redis             │
│  - users, profiles, prefs   │      │  - session cache             │
│  - training plans/weeks/days │      │  - rate limit counters       │
│  - session logs, set logs   │      │  - async job queue           │
│  - coaching rules/versions  │      │  - offline sync queue        │
│  - PRs, analytics snapshots │      │  - push notification jobs    │
│  - nutrition/recovery logs  │      │  - TTL-based feature flags   │
└─────────────────────────────┘      └─────────────────────────────┘
```

### 3.3 Critical Architecture Rules

1. **Backend owns ALL business logic.** No training intelligence lives in clients.
   - Progression decisions → backend
   - Fatigue calculations → backend
   - Load predictions → backend
   - Week type modifications → backend
   - Recommendation generation → backend

2. **Clients are dumb renderers.** Web and mobile:
   - Render UI from backend responses
   - Capture user input
   - Manage local UI state and offline cache
   - Never diverge from backend rule definitions

3. **Coaching engine is versioned.** Every rule set carries a semantic version. Outputs are traceable to the exact engine version that produced them.

4. **Modular monolith boundaries.** Each module has its own:
   - SQLAlchemy models
   - Pydantic schemas
   - Service layer
   - Router
   - Tests

---

## 4. Repository Structure

```text
gymos/
├── Plan.md                          # This document
├── specs/                           # All Spec Kit specs
│   ├── phase-0-foundation/
│   ├── phase-1-auth-users/
│   ├── phase-2-training-domain/
│   ├── phase-3-web-app/
│   ├── phase-4-mobile-app/
│   ├── phase-5-coaching-engine/
│   ├── phase-6-analytics/
│   ├── phase-7-nutrition-recovery/
│   ├── phase-8-notifications/
│   └── phase-9-hardening/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── config.py            # Settings via pydantic-settings
│   │   │   ├── security.py          # JWT, hashing
│   │   │   ├── dependencies.py      # FastAPI deps
│   │   │   └── exceptions.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── migrations/          # Alembic
│   │   ├── modules/
│   │   │   ├── auth/
│   │   │   │   ├── router.py
│   │   │   │   ├── service.py
│   │   │   │   ├── models.py
│   │   │   │   └── schemas.py
│   │   │   ├── users/
│   │   │   ├── training/
│   │   │   ├── coaching/
│   │   │   │   ├── engine/
│   │   │   │   │   ├── base.py
│   │   │   │   │   ├── v1/
│   │   │   │   │   │   ├── progression.py
│   │   │   │   │   │   ├── fatigue.py
│   │   │   │   │   │   ├── week_adjustment.py
│   │   │   │   │   │   └── load_calculator.py
│   │   │   │   │   └── registry.py
│   │   │   ├── analytics/
│   │   │   ├── nutrition/
│   │   │   ├── notifications/
│   │   │   └── sync/
│   │   └── shared/
│   │       ├── enums.py
│   │       ├── types.py
│   │       └── utils.py
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   ├── alembic/
│   ├── pyproject.toml
│   └── Dockerfile
│
├── web/
│   ├── src/
│   │   ├── app/                     # Next.js App Router
│   │   │   ├── (auth)/
│   │   │   ├── (dashboard)/
│   │   │   ├── plans/
│   │   │   ├── history/
│   │   │   └── analytics/
│   │   ├── features/                # Feature slices
│   │   │   ├── auth/
│   │   │   ├── plans/
│   │   │   ├── workout/
│   │   │   └── analytics/
│   │   ├── components/              # Shared UI
│   │   ├── lib/
│   │   │   ├── api/                 # API client
│   │   │   └── utils/
│   │   └── hooks/
│   ├── package.json
│   └── Dockerfile
│
├── mobile/
│   ├── lib/
│   │   ├── core/
│   │   │   ├── api/
│   │   │   ├── storage/             # Hive / Drift
│   │   │   └── sync/
│   │   ├── features/
│   │   │   ├── auth/
│   │   │   ├── workout/
│   │   │   ├── history/
│   │   │   └── readiness/
│   │   └── shared/
│   ├── pubspec.yaml
│   └── Dockerfile
│
├── infra/
│   ├── docker/
│   │   ├── backend.Dockerfile
│   │   ├── web.Dockerfile
│   │   └── mobile.Dockerfile
│   ├── compose/
│   │   ├── docker-compose.yml
│   │   └── docker-compose.prod.yml
│   └── ci/
│       └── .github/workflows/
│
└── docs/
    ├── architecture/
    ├── api/
    ├── domain/
    └── decisions/                   # ADRs
```

---

## 5. Domain Modules (Deep Breakdown)

### 5.1 Auth Module

**Responsibilities:**
- User registration with email verification
- Password hashing (bcrypt)
- JWT access token (15min TTL) + refresh token (30 days, rotating)
- Token revocation via Redis denylist
- Rate limiting on auth endpoints

**Key domain rules:**
- Refresh tokens are single-use (rotation on every refresh)
- Revoked tokens are stored in Redis with TTL matching their remaining lifetime
- Failed login attempts are counted per IP per email; lock after 10 failures in 15 minutes

### 5.2 Users Module

**Responsibilities:**
- User profile (name, dob, gender, unit preference)
- Training preferences (training age, experience level, goal type)
- App settings (notification preferences, dark mode, offline mode toggle)

### 5.3 Training Module

**Responsibilities:**
- Training plan CRUD (name, goal, weeks, days, exercises)
- Week structure (type: normal / deload / refeed / custom, order, label)
- Day structure (label, day-of-week, exercises list)
- Exercise instances (sets, reps target, load target, method type, notes)
- Session logs (planned day → actual execution record)
- Set logs (actual reps, actual load, RPE if captured, completed flag)
- Exercise library (name, muscle group, movement pattern, equipment)
- Substitution rules (per exercise, per muscle group)

**Key domain rules:**
- A session log is linked to exactly one training day
- Set logs are immutable once a session is completed and locked
- Exercise substitutions must preserve the primary muscle group
- A plan must have at least 1 week and 1 day to be activatable

### 5.4 Coaching Module

**Responsibilities:**
- Progression engine (next load calculation)
- Fatigue model (session-to-session and week-to-week)
- Week type adjustments (set/rep/load modifiers)
- Expected load calculation (pre-session target)
- Method-aware rule application (superset, drop set, rest-pause, cluster)
- Recommendation generation
- Rule versioning and traceability

**Key domain rules:**
- All coaching outputs carry the engine version that produced them
- Progression decisions are deterministic given the same inputs
- Fatigue accumulation is calculated per muscle group, not globally
- Deload weeks reduce volume by a configured percentage (default 40–60%)

### 5.5 Analytics Module

**Responsibilities:**
- Personal records per exercise (1RM estimates, actual PRs)
- Volume tracking per muscle group per week
- Adherence rate (sessions completed / sessions planned)
- Progression trend visualization data
- Weekly summary generation

### 5.6 Nutrition & Recovery Module

**Responsibilities:**
- Daily readiness log (sleep quality, energy, soreness, stress — scored 1–10)
- Recovery activities (cardio, sauna, stretching — type, duration)
- Nutrition log (calories, protein, carbs, fat, water intake)
- Body weight log
- Weekly nutrition average calculation

### 5.7 Notifications Module

**Responsibilities:**
- Workout reminders (scheduled push)
- Streak nudges (missed session detection)
- Coaching summary digests (weekly push)
- Sync status events (offline → online transitions)
- Push delivery via FCM (Android) / APNs (iOS)

### 5.8 Sync Module

**Responsibilities:**
- Offline operation queue (mobile writes while offline → server sync on reconnect)
- Conflict resolution strategy (last-write-wins with server authority)
- Sync status tracking per user device
- Idempotency enforcement on sync endpoints

---

## 6. Data Model Direction

### Core Entities

```sql
-- Identity
users (id, email, password_hash, is_active, is_verified, created_at)
profiles (id, user_id, first_name, last_name, dob, gender, unit_preference)
preferences (id, user_id, goal_type, experience_level, training_age_years,
             notification_enabled, offline_mode_enabled)

-- Auth
refresh_tokens (id, user_id, token_hash, expires_at, revoked, device_id)

-- Exercise library
exercises (id, name, slug, primary_muscle, secondary_muscles[], movement_pattern,
           equipment_type, is_bodyweight, created_by, is_global)
exercise_substitutions (id, exercise_id, substitute_exercise_id, reason)

-- Training plans
training_plans (id, user_id, name, goal_type, is_active, created_at)
training_weeks (id, plan_id, week_number, week_type, label, notes)
training_days (id, week_id, day_number, day_of_week, label)
exercise_instances (id, day_id, exercise_id, position, sets_target,
                    reps_target, load_target_kg, method_type, rest_seconds,
                    progression_rule, notes)

-- Execution logs
session_logs (id, user_id, plan_id, week_id, day_id, started_at, completed_at,
              is_locked, readiness_score, session_notes, sync_id)
set_logs (id, session_id, exercise_instance_id, set_number, reps_actual,
          load_actual_kg, rpe_actual, is_completed, notes, logged_at)

-- Coaching
coaching_recommendations (id, user_id, session_id, engine_version,
                           recommendation_type, payload_json, generated_at)
rule_versions (id, engine_name, version, is_active, activated_at,
               deactivated_at, config_snapshot_json, notes)

-- Analytics
personal_records (id, user_id, exercise_id, record_type, value, achieved_at,
                  session_id, set_log_id)
volume_snapshots (id, user_id, week_start_date, muscle_group,
                  total_sets, total_reps, total_load_kg, created_at)

-- Nutrition & Recovery
readiness_logs (id, user_id, logged_date, sleep_hours, sleep_quality,
                energy_level, soreness_level, stress_level, notes)
nutrition_logs (id, user_id, logged_date, calories, protein_g, carbs_g,
                fat_g, water_ml, notes)
body_weight_logs (id, user_id, logged_date, weight_kg)
recovery_activities (id, user_id, logged_date, activity_type, duration_minutes, notes)

-- Notifications
notification_records (id, user_id, type, title, body, sent_at, read_at,
                      delivery_status, platform)

-- Sync
sync_operations (id, user_id, device_id, operation_type, resource_type,
                 resource_id, payload_json, local_timestamp, server_timestamp,
                 status, conflict_resolution)
```

### Key table: `rule_versions`

Every coaching engine output must be traceable to a specific `rule_versions` record. This enables:
- Reproducing past decisions given historical inputs
- Safely rolling back to a prior engine version
- Comparing outputs between engine generations
- Auditing progression recommendations in user disputes

---

## 7. API Strategy

### 7.1 Design Principles

- REST with resource-based URLs
- JSON request/response bodies
- Versioned via URL prefix: `/api/v1/`
- Consistent error envelope: `{ "error": { "code": str, "message": str, "details": {} } }`
- Consistent success envelope: `{ "data": {}, "meta": {} }`
- Pagination via cursor (not offset) for all list endpoints
- All mutations return the updated resource

### 7.2 Authentication

All protected endpoints require `Authorization: Bearer <access_token>`.  
Refresh flow: `POST /api/v1/auth/refresh` with refresh token in HttpOnly cookie.

### 7.3 Core Endpoint Groups

```
/api/v1/auth/          register, login, logout, refresh, verify-email
/api/v1/users/         profile, preferences, settings
/api/v1/exercises/     library CRUD, substitutions
/api/v1/plans/         CRUD, activate, archive
/api/v1/plans/{id}/weeks/        week CRUD
/api/v1/plans/{id}/weeks/{id}/days/     day CRUD
/api/v1/plans/{id}/weeks/{id}/days/{id}/exercises/   exercise instance CRUD
/api/v1/sessions/      list, create, complete, lock
/api/v1/sessions/{id}/sets/      set log CRUD
/api/v1/coaching/      next-load, recommendations, progression-preview
/api/v1/analytics/     PRs, volume, trends, adherence, weekly-summary
/api/v1/readiness/     CRUD
/api/v1/nutrition/     CRUD
/api/v1/notifications/ list, mark-read, preferences
/api/v1/sync/          push (offline ops), pull (server state diff)
```

### 7.4 Coaching API contract

```
POST /api/v1/coaching/next-load
Request:
{
  "exercise_instance_id": "uuid",
  "last_session_id": "uuid",
  "week_type": "normal" | "deload" | "refeed" | "custom",
  "readiness_score": 1-10
}
Response:
{
  "data": {
    "suggested_load_kg": float,
    "suggested_reps": int,
    "engine_version": "v1.2.0",
    "rule_version_id": "uuid",
    "rationale": str,
    "adjustment_type": "increase" | "maintain" | "decrease" | "deload",
    "confidence": "high" | "medium" | "low"
  }
}
```

---

## 8. Offline & Sync Strategy

### 8.1 Scope

Mobile offline support is scoped to **active workout execution**. The user must be able to:
- Load the current day's workout while online
- Execute sets and log data while offline
- Have data sync automatically when connectivity returns

Planning, editing, analytics, and nutrition are **online-only** in v1.

### 8.2 Architecture

```text
Mobile App (Flutter)
  ├── Local DB (Hive / Drift)          ← Stores active session data
  ├── Sync Queue                        ← Ordered list of pending operations
  └── Connectivity Monitor              ← Triggers sync on reconnect

Backend (FastAPI)
  ├── /api/v1/sync/push                 ← Accepts batch of offline operations
  └── /api/v1/sync/pull                 ← Returns server state diff since last sync
```

### 8.3 Operation Model

Each offline operation is a JSON record:
```json
{
  "operation_id": "uuid",
  "operation_type": "create" | "update" | "delete",
  "resource_type": "set_log" | "session_log",
  "resource_id": "uuid",
  "payload": {},
  "local_timestamp": "ISO8601",
  "device_id": "uuid"
}
```

Operations are applied in `local_timestamp` order. Server is authoritative on conflicts.

### 8.4 Conflict Resolution

| Conflict type | Resolution |
|---|---|
| Two devices log the same set | Last write wins (server timestamp) |
| Session completed on device A while device B is logging | Device B sync rejected with 409; user notified |
| Network drops mid-sync | Idempotent replay: operations with duplicate `operation_id` are ignored |

### 8.5 Idempotency

All sync endpoints are idempotent. Operations include a client-generated `operation_id` (UUID). Server deduplicates by `(user_id, device_id, operation_id)`.

---

## 9. Security & Observability

### 9.1 Security

| Control | Implementation |
|---|---|
| Auth | JWT (RS256), rotating refresh tokens, HttpOnly cookie |
| Password storage | bcrypt with cost factor 12 |
| Rate limiting | Nginx + Redis counter per IP per route |
| Input validation | Pydantic strict mode on all request bodies |
| SQL injection | SQLAlchemy ORM (parameterized queries only) |
| CORS | Allowlist of known origins only |
| Secrets | Environment variables via `.env` + Docker secrets in prod |
| HTTPS | TLS at Nginx; backend not exposed directly |
| Row-level security | All queries filter by `user_id`; enforced at service layer |

### 9.2 Observability

| Signal | Tool |
|---|---|
| Error tracking | Sentry (backend + web + mobile) |
| Structured logs | `structlog` on backend, JSON format |
| Metrics | Prometheus (later) — expose `/metrics` endpoint |
| Dashboards | Grafana (later) |
| Tracing | OpenTelemetry (later, Phase 9) |
| Uptime | Health check endpoint `/api/v1/health` |
| DB slow queries | PostgreSQL `pg_stat_statements` |

### 9.3 Audit Trail

All mutations to training plans, session logs, and coaching decisions are appended to an `audit_log` table with: `user_id`, `action`, `resource_type`, `resource_id`, `payload_before`, `payload_after`, `timestamp`.

---

## 10. Testing Strategy

### 10.1 Test pyramid

```
E2E tests (few)          ← Critical user journeys only
Integration tests        ← API endpoint + DB (real PostgreSQL in CI)
Unit tests (many)        ← Domain logic, coaching engine, calculators
```

### 10.2 Backend testing rules

- **No mocking the database.** Integration tests use a real PostgreSQL instance (Docker in CI).
- Unit tests target pure functions: progression calculations, fatigue models, load calculations.
- Every coaching engine decision must have a corresponding unit test with explicit inputs and expected outputs.
- API contract tests validate response shape against Pydantic schemas.

### 10.3 Web testing

- Component tests with React Testing Library
- API integration tests with MSW (mock service worker)
- Critical flows (login, plan creation, history view) covered by Playwright E2E

### 10.4 Mobile testing

- Widget tests for workout logging flow
- Integration tests for offline queue and sync behavior
- No unit tests for business logic — logic lives in backend

### 10.5 Coaching engine testing

The coaching engine must have a **test fixture library**: a set of named scenarios (e.g., `linear_progression_week3_normal`, `deload_after_4_weeks_fatigue`) with defined inputs and expected outputs. These serve as regression tests across engine versions.

---

## 11. Deployment Strategy

### 11.1 Environments

| Environment | Purpose |
|---|---|
| Local | Developer machines via Docker Compose |
| CI | GitHub Actions — test + build only |
| Staging | Full stack deployment; used for QA and acceptance testing |
| Production | Live traffic |

### 11.2 Local stack (Docker Compose)

Services: `backend`, `web`, `postgres`, `redis`, `worker`  
Volumes: persistent postgres data, hot-reload for backend and web  
Ports: backend:8000, web:3000, postgres:5432, redis:6379

### 11.3 CI/CD (GitHub Actions)

```
On PR:
  - backend: lint (ruff) → typecheck (mypy) → unit tests → integration tests
  - web: lint (eslint) → typecheck (tsc) → component tests
  - mobile: lint → widget tests

On merge to main:
  - build Docker images
  - push to container registry
  - deploy to staging (auto)
  - run E2E smoke tests on staging

On release tag:
  - promote staging image to production (manual approval)
```

### 11.4 Future: Kubernetes

Staging and production will move to Kubernetes (k8s) in Phase 9. Each module exposes its own health check. Horizontal pod autoscaling on backend. Separate deployment for background worker.

---

## 12. Risks & Assumptions

| Risk | Severity | Mitigation |
|---|---|---|
| Prototype logic undocumented → lost in rewrite | High | Phase 1 domain extraction before any implementation |
| Business logic duplicated across web/mobile/backend | High | Backend is sole authority; clients never compute coaching decisions |
| Coaching engine complexity grows without control | High | Strict versioning; engine changes require new version, not in-place edits |
| Mobile offline sync conflict handling underestimated | Medium | Start with minimal offline scope (active session only); expand in Phase 8 |
| Analytics queries become slow at scale | Medium | Volume snapshot materialization from Phase 6; query optimization in Phase 9 |
| Specs too broad → implementation drift | Medium | Spec granularity rule enforced; each spec represents one coherent delivery slice |
| Over-engineering early (premature microservices) | Medium | Modular monolith only until Phase 9; no service extraction without evidence |
| PostgreSQL schema drift from rapid iteration | Low | Alembic migrations required for all schema changes from Phase 2 onwards |

**Assumptions:**
- Single deployment region initially
- Single currency / unit system (metric primary, imperial optional per user)
- No real-time collaboration between users in v1
- Coach-athlete relationship is out of scope until post-MVP

---

## 13. Success Metrics

| Metric | Target | Phase |
|---|---|---|
| API p95 latency | < 200ms for training endpoints | Phase 9 |
| API p95 latency | < 500ms for coaching decisions | Phase 9 |
| Coaching engine unit test coverage | 100% of decision paths | Phase 5 |
| Backend integration test coverage | > 80% of endpoints | Phase 2+ |
| Offline session completion rate | > 95% without data loss | Phase 4 |
| Sync success rate on reconnect | > 99% | Phase 8 |
| Time to create and activate a training plan | < 3 minutes | Phase 3 |
| Mobile cold start time | < 2 seconds | Phase 4 |
| Error rate in production | < 0.1% of requests | Phase 9 |

---

## 14. SPEC KIT IMPLEMENTATION PLAN

This is the implementation authority. Every spec below maps to a concrete Spec Kit execution unit: spec → plan → tasks → implementation.

---

### PHASE 0: Foundation

**Objective:** Create the engineering skeleton required by all future work. No business logic. No domain model. Infrastructure and standards only.

---

#### Spec 0.1: `repository-foundation`

**Objective:** Establish the mono-repo structure, directory conventions, documentation layout, branch strategy, and commit standards.

**Scope (in):**
- Directory creation: `backend/`, `web/`, `mobile/`, `infra/`, `docs/`, `specs/`
- README with project overview and setup instructions
- `.gitignore` for all three stacks
- Branch strategy documentation (main, feature/*, release/*)
- Commit message convention (Conventional Commits)
- PR template
- ADR (Architecture Decision Record) template under `docs/decisions/`
- Initial ADRs: monolith over microservices, stack choices

**Scope (out):** No application code, no Docker, no CI.

**Inputs:** This Plan.md document.

**Outputs:**
- Repository with full directory structure
- README.md
- CONTRIBUTING.md
- `docs/decisions/001-modular-monolith.md`
- `docs/decisions/002-stack-selection.md`
- `.github/pull_request_template.md`

**Domain Logic:** None. This spec is infrastructure only.

**Edge Cases:**
- Mono-repo tooling (Turborepo, Nx) explicitly NOT added — too early, adds complexity without benefit.

**Dependencies:** None.

**Acceptance Criteria:**
- All directories exist and are committed
- README accurately describes the project and stack
- At least 2 ADRs are written and follow the standard template
- `git clone` + reading README is sufficient to understand what GymOS is

---

#### Spec 0.2: `backend-scaffold`

**Objective:** Create a runnable FastAPI application with module structure, dependency injection, settings management, and health check.

**Scope (in):**
- FastAPI app factory pattern (`create_app()`)
- Module router registration (`auth`, `users`, `training`, `coaching`, `analytics`, `nutrition`, `notifications`, `sync`)
- `pydantic-settings` config with environment variable loading
- Database session factory (SQLAlchemy async)
- Alembic setup with initial migration
- Health check endpoint: `GET /api/v1/health`
- `pyproject.toml` with all dependencies pinned
- `ruff` for linting, `mypy` for type checking
- `pytest` with async support

**Scope (out):** No business logic. No domain models beyond a placeholder.

**Inputs:** Stack decision (FastAPI, PostgreSQL, Redis, SQLAlchemy).

**Outputs:**
- Runnable FastAPI app returning 200 on health check
- Empty module routers registered
- Alembic baseline migration
- `make dev`, `make test`, `make lint` commands working

**API Endpoints:**
```
GET /api/v1/health → { "status": "ok", "version": "0.1.0" }
```

**Data Models:** SQLAlchemy `Base` only. No tables yet.

**Edge Cases:**
- DB connection failure → health check returns 503 with degraded status
- Missing env variable → app fails fast on startup with clear error

**Dependencies:** Spec 0.1

**Acceptance Criteria:**
- `uvicorn app.main:app` starts without error
- `GET /api/v1/health` returns 200
- `pytest` runs (0 tests, no failures)
- `ruff check .` passes
- `mypy app/` passes

---

#### Spec 0.3: `web-scaffold`

**Objective:** Create a runnable Next.js application with route structure, API client setup, and authentication middleware placeholder.

**Scope (in):**
- Next.js 14 App Router setup with TypeScript
- Route groups: `(auth)`, `(dashboard)`
- Tailwind CSS configured
- TanStack Query provider
- API client base (axios or fetch wrapper with base URL from env)
- ESLint + Prettier configured
- `npm run dev`, `npm run build`, `npm run lint`, `npm run test` working
- Placeholder pages: `/login`, `/dashboard`

**Scope (out):** No real API calls. No auth logic. No state management beyond provider setup.

**Inputs:** Next.js 14, TypeScript, Tailwind, TanStack Query.

**Outputs:**
- Runnable Next.js app with placeholder pages
- Configured toolchain

**Edge Cases:**
- `NEXT_PUBLIC_API_URL` missing → build fails with clear error

**Dependencies:** Spec 0.1

**Acceptance Criteria:**
- `npm run dev` starts on port 3000
- `/login` and `/dashboard` routes render without console errors
- `npm run build` produces a successful production build
- `npm run lint` passes

---

#### Spec 0.4: `mobile-scaffold`

**Objective:** Create a runnable Flutter application with feature structure, state management setup, and API client placeholder.

**Scope (in):**
- Flutter project with null safety
- Riverpod for state management
- Dio for HTTP client with base URL configuration
- Feature directory structure: `auth/`, `workout/`, `history/`, `readiness/`
- Local storage setup: Hive initialized
- Placeholder screens: Login, Home
- `flutter analyze` passing
- `flutter test` running

**Scope (out):** No real API integration. No offline logic. No platform-specific config (FCM, APNs).

**Inputs:** Flutter, Riverpod, Dio, Hive.

**Outputs:**
- Runnable Flutter app on Android emulator / iOS simulator
- Clean feature directory structure

**Edge Cases:**
- API base URL not configured → app shows configuration error screen, does not crash

**Dependencies:** Spec 0.1

**Acceptance Criteria:**
- `flutter run` succeeds on both Android and iOS targets
- `flutter analyze` reports 0 issues
- `flutter test` runs (0 tests, no failures)

---

#### Spec 0.5: `local-dev-and-ci-foundation`

**Objective:** Create the local development stack (Docker Compose) and the baseline CI pipeline (GitHub Actions).

**Scope (in):**
- `docker-compose.yml`: services for `backend`, `web`, `postgres`, `redis`
- Health checks for postgres and redis containers
- Environment variable files: `.env.example` for each service
- GitHub Actions workflow: `ci.yml`
  - Triggered on: PR to main, push to main
  - Jobs: `backend-lint`, `backend-test`, `web-lint`, `web-test`
  - Backend tests use a real PostgreSQL service container
- `Makefile` at repo root with: `make up`, `make down`, `make test`, `make lint`

**Scope (out):** No deployment. No staging environment. No mobile CI (added in Phase 4).

**Inputs:** Specs 0.2, 0.3, 0.4 scaffolds.

**Outputs:**
- `docker-compose.yml` with all services
- `.env.example` files committed (no real secrets)
- GitHub Actions CI passing on an empty test suite
- `make up` brings the full stack up locally

**Edge Cases:**
- Port conflicts → documented port override via env variables
- CI cache invalidation → use `hashFiles` on lock files for cache keys

**Dependencies:** Specs 0.2, 0.3, 0.4

**Acceptance Criteria:**
- `make up` starts all services; backend health check passes
- `make test` runs backend and web test suites
- GitHub Actions CI passes on a clean checkout
- No secrets committed (checked by `detect-secrets` pre-commit hook)

---

### PHASE 1: Auth & Users

**Objective:** Build the authentication foundation and user profile system. First real business logic.

---

#### Spec 1.1: `auth-core`

**Objective:** Implement user registration, login, logout, and token management.

**Scope (in):**
- `POST /api/v1/auth/register` — create user, send verification email (stubbed in v1)
- `POST /api/v1/auth/login` — authenticate, return access token + set refresh token cookie
- `POST /api/v1/auth/logout` — revoke current refresh token
- `POST /api/v1/auth/refresh` — rotate refresh token, return new access token
- `GET /api/v1/auth/me` — return current user identity
- JWT (RS256): access token TTL 15 min, signed with private key
- Refresh token: 30-day TTL, stored hashed in `refresh_tokens` table
- Token rotation: each refresh invalidates the old refresh token
- Rate limiting: 10 failed logins per IP per 15 minutes → 429 response

**Scope (out):** Email verification (stubbed), OAuth (Phase 9), 2FA.

**Inputs:** User email, password.

**Outputs:**
- `users` table with hashed passwords
- `refresh_tokens` table
- JWT access token in response body
- Refresh token in HttpOnly Secure cookie

**Domain Logic:**
- `bcrypt` with cost factor 12 for password hashing
- Failed login counter stored in Redis: key `auth:fail:{ip}:{email}`, TTL 15 minutes, increment on fail, reset on success
- On 10th failure: return 429, add IP to temporary denylist (Redis, TTL 15 min)
- Refresh token rotation: `POST /auth/refresh` marks old token as revoked before issuing new one — if old token is already revoked, revoke all tokens for that user (compromise detected)

**API Endpoints:**
```
POST /api/v1/auth/register
  Body: { email, password, first_name, last_name }
  Response 201: { data: { user_id, email } }
  Response 409: email already exists

POST /api/v1/auth/login
  Body: { email, password }
  Response 200: { data: { access_token, token_type: "bearer", expires_in: 900 } }
  Sets-Cookie: refresh_token=...; HttpOnly; Secure; SameSite=Strict; Path=/api/v1/auth/refresh
  Response 401: invalid credentials
  Response 429: too many failed attempts

POST /api/v1/auth/logout
  Header: Authorization: Bearer <token>
  Response 204: no body

POST /api/v1/auth/refresh
  Cookie: refresh_token
  Response 200: { data: { access_token, expires_in: 900 } }
  Response 401: token expired or revoked

GET /api/v1/auth/me
  Header: Authorization: Bearer <token>
  Response 200: { data: { user_id, email, is_verified } }
```

**Data Models:**
```python
# users: id, email, password_hash, is_active, is_verified, created_at, updated_at
# refresh_tokens: id, user_id, token_hash, expires_at, revoked_at, device_id
```

**Edge Cases:**
- Simultaneous refresh from two devices using the same refresh token → first succeeds, second triggers full session revocation (reuse detection)
- Access token presented after logout → remains valid until TTL (stateless; mitigation: short TTL)
- User account deactivated mid-session → access token validation checks `is_active` on every request

**Dependencies:** Spec 0.2

**Acceptance Criteria:**
- Register → Login → Refresh → Logout flow passes integration tests
- Failed login rate limiting triggers at threshold
- Refresh token reuse detection revokes all user sessions
- Passwords never stored in plaintext (verified by inspection + test)
- All endpoints return correct HTTP status codes per spec

---

#### Spec 1.2: `user-profile-and-preferences`

**Objective:** Allow users to manage their profile, training preferences, and app settings.

**Scope (in):**
- `GET /api/v1/users/profile` — return profile
- `PATCH /api/v1/users/profile` — update profile fields
- `GET /api/v1/users/preferences` — return training preferences
- `PATCH /api/v1/users/preferences` — update preferences
- `GET /api/v1/users/settings` — return app settings
- `PATCH /api/v1/users/settings` — update settings
- Profile created automatically on registration with defaults

**Domain Logic:**
- `unit_preference` defaults to `"metric"`. If changed to `"imperial"`, all load values returned by the API are converted client-side (API always stores and returns metric internally).
- `experience_level` options: `"beginner"` (< 1 year), `"intermediate"` (1–3 years), `"advanced"` (3+ years). This field influences coaching defaults.
- `goal_type` options: `"strength"`, `"hypertrophy"`, `"endurance"`, `"weight_loss"`, `"maintenance"`.

**API Endpoints:**
```
GET  /api/v1/users/profile
PATCH /api/v1/users/profile
  Body: { first_name?, last_name?, dob?, gender?, unit_preference? }

GET  /api/v1/users/preferences
PATCH /api/v1/users/preferences
  Body: { goal_type?, experience_level?, training_age_years? }

GET  /api/v1/users/settings
PATCH /api/v1/users/settings
  Body: { notification_enabled?, offline_mode_enabled?, dark_mode? }
```

**Edge Cases:**
- `dob` in the future → validation error
- `training_age_years` > 50 → validation error
- PATCH with no body → 400 bad request
- Profile or preferences records must exist for every user (created on registration)

**Dependencies:** Spec 1.1

**Acceptance Criteria:**
- Profile, preferences, and settings are returned correctly after registration
- PATCH updates only provided fields (partial update)
- Invalid field values return 422 with field-level error details
- All endpoints require authentication (401 without valid token)

---

#### Spec 1.3: `role-and-permissions-model`

**Objective:** Establish the authorization model to support future coach-athlete relationships and admin capabilities.

**Scope (in):**
- `role` field on `users`: `"athlete"` (default), `"coach"` (future), `"admin"`
- Middleware that enforces role-based access on protected routes
- Admin-only endpoints for user management (list users, deactivate user)
- Row-level security: every data query must filter by `user_id` unless the requester is an admin
- `get_current_user` dependency returns user + role for use in all route handlers

**Scope (out):** Coach-athlete relationships (future phase). Organization-level roles.

**Domain Logic:**
- Row-level security is enforced at the **service layer**, not only at the DB level. Every service method that queries user data takes `user_id` as a required parameter.
- Admin users can query any user's data by passing `?user_id=` override.
- Unauthenticated requests to protected routes return 401.
- Authenticated requests to role-restricted routes return 403.

**Edge Cases:**
- User with `role=athlete` attempts to access admin endpoint → 403, logged to audit trail
- Admin accessing another user's data → permitted + audit logged

**Dependencies:** Spec 1.1

**Acceptance Criteria:**
- `role` field present on all user records
- Protected endpoints return 401 without auth, 403 for wrong role
- Row-level isolation: user A cannot read user B's data
- Admin bypass works and is audit logged

---

### PHASE 2: Training Domain

**Objective:** Build the core training data model — the foundation all coaching, analytics, and execution depends on.

---

#### Spec 2.1: `training-domain-language`

**Objective:** Document and formalize the GymOS training domain before any implementation. Convert prototype concepts into canonical, testable definitions.

**Scope (in):**
- Formal definition of all training entities: plan, week, day, exercise instance, session log, set log
- Week type taxonomy: `normal`, `deload`, `refeed`, `custom`
- Method type taxonomy: `standard`, `superset`, `drop_set`, `rest_pause`, `cluster`, `amrap`
- Progression rule taxonomy: `linear`, `double_progression`, `wave_load`, `rpe_based`, `percentage_based`
- Muscle group taxonomy (canonical list, used across exercise library and analytics)
- Movement pattern taxonomy: `squat`, `hinge`, `push_horizontal`, `push_vertical`, `pull_horizontal`, `pull_vertical`, `carry`, `isolation`
- State machine for session: `planned` → `in_progress` → `completed` → `locked`
- State machine for set log: `pending` → `logged` → `skipped`
- Decision tables for week type modifiers (load%, volume%, rest%)
- Glossary of all domain terms

**Scope (out):** No code. This is documentation + domain model only.

**Outputs:**
- `docs/domain/training-domain-language.md`
- `docs/domain/week-type-decision-table.md`
- `docs/domain/method-type-definitions.md`
- `docs/domain/progression-rules.md`
- `docs/domain/muscle-group-taxonomy.md`

**Domain Logic:**
- **Deload week defaults:** volume −50%, load −10%, rest +30 seconds
- **Refeed week defaults:** volume −20%, load maintained, carbohydrates increased (nutrition domain, not training)
- **Custom week:** all modifiers explicitly defined in the week record
- **AMRAP sets:** reps_target represents minimum; actual reps are logged without upper bound
- **Drop sets:** each drop is a separate set_log entry with a flag `is_drop=true`
- **Supersets:** two or more exercise instances share a `superset_group_id`; rest is applied after the group, not between exercises

**Edge Cases:**
- Exercise with no muscle group assignment (must be required on insert)
- Plan with 0 days in a week (valid — represents a rest week)
- Session log for a day that has no exercise instances (valid — rest day execution)

**Dependencies:** Spec 0.2 (running backend to validate models against)

**Acceptance Criteria:**
- All domain entities are formally documented with field-level definitions
- All week types have explicit decision tables
- All method types have example set sequences
- Domain document is reviewed and signed off before Phase 2 implementation begins

---

#### Spec 2.2: `exercise-library`

**Objective:** Build the canonical exercise database with search, filtering, and substitution support.

**Scope (in):**
- `exercises` table with all fields from data model
- Seed data: 100+ canonical exercises across all muscle groups and movement patterns
- CRUD endpoints (admin creates global exercises; users can create custom exercises)
- Search: by name (fuzzy), by muscle group, by movement pattern, by equipment
- Substitution: link exercises as substitutes with a reason

**Scope (out):** Video/image attachments (Phase 9). AI exercise recognition.

**API Endpoints:**
```
GET  /api/v1/exercises?search=&muscle=&pattern=&equipment=&page_cursor=
POST /api/v1/exercises                    (user: custom; admin: global)
GET  /api/v1/exercises/{id}
PATCH /api/v1/exercises/{id}             (own custom exercises only)
GET  /api/v1/exercises/{id}/substitutions
POST /api/v1/exercises/{id}/substitutions
DELETE /api/v1/exercises/{id}/substitutions/{sub_id}
```

**Data Models:**
```
exercises: id, name, slug, primary_muscle, secondary_muscles[],
           movement_pattern, equipment_type, is_bodyweight, is_global, created_by
exercise_substitutions: id, exercise_id, substitute_exercise_id, reason
```

**Domain Logic:**
- Global exercises (`is_global=true`) are visible to all users; only admins can create/edit them
- Custom exercises (`is_global=false, created_by=user_id`) are visible only to their creator
- A substitution must preserve `primary_muscle` — cannot substitute bench press with a squat
- Substitution is bidirectional in the UI but stored as two directed records

**Edge Cases:**
- Fuzzy search on exercise name with accented characters → normalize to ASCII before search
- Creating a substitution where both IDs are the same exercise → 400 validation error
- Deleting an exercise that is referenced in a training plan → soft delete only (`is_archived=true`); cascade does not destroy plan integrity

**Dependencies:** Spec 2.1, Spec 1.3

**Acceptance Criteria:**
- 100+ seed exercises present after `make seed`
- Search returns relevant results for common terms (bench, squat, deadlift)
- Substitution validation rejects cross-muscle-group pairs
- Custom exercises not visible to other users

---

#### Spec 2.3: `training-plan-core-model`

**Objective:** Build full CRUD for training plans including week, day, and exercise instance management.

**Scope (in):**
- Plan CRUD: create, read, update, delete, list (own plans)
- Plan activation: only one plan can be active per user at a time
- Week CRUD within a plan
- Day CRUD within a week
- Exercise instance CRUD within a day (reorder, copy, delete)
- Plan archival (soft delete)
- Plan duplication (copy plan structure, not logs)

**Scope (out):** Session execution, progression rules, coaching, week type logic beyond storage.

**API Endpoints:**
```
GET  /api/v1/plans
POST /api/v1/plans
GET  /api/v1/plans/{id}
PATCH /api/v1/plans/{id}
DELETE /api/v1/plans/{id}              (soft delete / archive)
POST /api/v1/plans/{id}/activate
POST /api/v1/plans/{id}/duplicate

GET  /api/v1/plans/{id}/weeks
POST /api/v1/plans/{id}/weeks
GET  /api/v1/plans/{id}/weeks/{wid}
PATCH /api/v1/plans/{id}/weeks/{wid}
DELETE /api/v1/plans/{id}/weeks/{wid}

GET  /api/v1/plans/{id}/weeks/{wid}/days
POST /api/v1/plans/{id}/weeks/{wid}/days
PATCH /api/v1/plans/{id}/weeks/{wid}/days/{did}
DELETE /api/v1/plans/{id}/weeks/{wid}/days/{did}

GET  /api/v1/plans/{id}/weeks/{wid}/days/{did}/exercises
POST /api/v1/plans/{id}/weeks/{wid}/days/{did}/exercises
PATCH /api/v1/plans/{id}/weeks/{wid}/days/{did}/exercises/{eid}
DELETE /api/v1/plans/{id}/weeks/{wid}/days/{did}/exercises/{eid}
POST /api/v1/plans/{id}/weeks/{wid}/days/{did}/exercises/reorder
```

**Data Models:**
```
training_plans: id, user_id, name, goal_type, is_active, is_archived, created_at
training_weeks: id, plan_id, week_number, week_type, label, notes
training_days: id, week_id, day_number, day_of_week, label
exercise_instances: id, day_id, exercise_id, position, sets_target, reps_target,
                    load_target_kg, method_type, rest_seconds, superset_group_id,
                    progression_rule, notes
```

**Domain Logic:**
- Activating a plan deactivates the current active plan automatically
- Archived plans cannot be activated
- Deleting a week deletes all its days and exercise instances (cascade)
- `position` field on `exercise_instances` is a float (1.0, 2.0, 3.0) to allow insertion without renumbering (new exercise between 1 and 2 gets 1.5)
- Plan duplication creates deep copies of all weeks, days, and exercise instances with new IDs; logs are NOT copied

**Edge Cases:**
- Activating a plan with 0 weeks → allowed (user may build progressively)
- Deleting the active plan → deactivates first, then archives
- Reordering exercise instances → recalculate positions to avoid float drift
- Plan duplication for a plan with 50+ weeks → must complete atomically (transaction)

**Dependencies:** Spec 2.2, Spec 1.3

**Acceptance Criteria:**
- Full CRUD for plans/weeks/days/exercises passes integration tests
- Only one active plan per user enforced
- Plan duplication produces identical structure with new IDs
- Cascade delete verified: deleting a week removes all child records
- Position-based reordering works correctly

---

#### Spec 2.4: `workout-session-logging-core`

**Objective:** Build the session logging system — the core execution record for every workout.

**Scope (in):**
- Create session from a training day (start workout)
- Log individual sets (reps, load, RPE optional)
- Mark sets as skipped
- Complete a session
- Lock a completed session (immutable after lock)
- View session history (paginated, filterable by date range)
- View a single session with all set logs

**Scope (out):** Coaching decisions triggered by session data (Phase 5). Real-time sync (Phase 4 mobile). Analytics aggregation (Phase 6).

**API Endpoints:**
```
POST /api/v1/sessions                     start session from day_id
GET  /api/v1/sessions                     list sessions (cursor paginated)
GET  /api/v1/sessions/{id}                full session with set logs
PATCH /api/v1/sessions/{id}               update session notes, readiness_score
POST /api/v1/sessions/{id}/complete       mark session as completed
POST /api/v1/sessions/{id}/lock           lock session (immutable)

GET  /api/v1/sessions/{id}/sets
POST /api/v1/sessions/{id}/sets           log a set
PATCH /api/v1/sessions/{id}/sets/{set_id} update a set (only if session not locked)
POST /api/v1/sessions/{id}/sets/{set_id}/skip
```

**Data Models:**
```
session_logs: id, user_id, plan_id, week_id, day_id, started_at, completed_at,
              is_locked, readiness_score, session_notes, sync_id
set_logs: id, session_id, exercise_instance_id, set_number, reps_actual,
          load_actual_kg, rpe_actual, is_completed, is_skipped, notes, logged_at
```

**Domain Logic:**
- A session starts in state `in_progress`. It can be `completed` then `locked`.
- `complete` requires at least 1 set logged (cannot complete an empty session).
- `lock` sets `is_locked=true`. After locking, no set can be added, modified, or deleted.
- A session that is `in_progress` for more than 24 hours is auto-completed by a background job (stale session cleanup).
- Set logs reference `exercise_instance_id` from the plan. If an exercise is substituted during a session, the set log references the substitute exercise instance.
- `readiness_score` (1–10) is captured at session start. It is passed to the coaching engine for load adjustments.

**Edge Cases:**
- Attempting to log a set after session is locked → 409 Conflict
- Logging a set with `reps_actual=0` → valid (failed attempt, weight too heavy)
- Session started for a day that has no exercise instances → allowed (rest day tracking)
- Two sessions started for the same day on the same day → allowed (split sessions)
- `load_actual_kg` = 0 → valid for bodyweight exercises

**Dependencies:** Spec 2.3, Spec 1.3

**Acceptance Criteria:**
- Start → log sets → complete → lock flow passes integration tests
- Locked session rejects all modification attempts with 409
- Stale session job auto-completes sessions older than 24 hours
- Session history is paginated correctly with cursor

---

### PHASE 3: Web App

**Objective:** Build the first production web interface. The web app is a client only — it calls the backend API for all data and logic.

---

#### Spec 3.1: `web-auth-and-shell`

**Objective:** Implement authentication flows and the authenticated application shell.

**Scope (in):**
- Login page (`/login`)
- Register page (`/register`)
- Token storage: access token in memory (not localStorage), refresh via cookie
- Auth middleware in Next.js (route protection using middleware.ts)
- Authenticated shell layout: sidebar navigation, header, user menu
- Logout flow
- Token refresh on 401 response (transparent refresh via Axios interceptor)

**Scope (out):** Password reset, email verification UI.

**Domain Logic:**
- Access token stored in React context (in-memory). On page refresh, the app immediately calls `/auth/refresh` using the HttpOnly cookie to rehydrate the access token.
- If refresh fails (cookie expired or revoked), user is redirected to `/login`.
- Navigation state (active plan name, user name) loaded once after auth and cached in React context.

**Edge Cases:**
- Multiple browser tabs: each tab independently refreshes tokens. Simultaneous refresh from two tabs → one succeeds, one fails → the failing tab retries once, then redirects to login if it fails again.
- User navigates directly to `/dashboard` without being logged in → middleware redirects to `/login` with `?redirect=/dashboard`

**Dependencies:** Spec 1.1, Spec 0.3

**Acceptance Criteria:**
- Login and logout work end-to-end with the real backend
- Page refresh restores auth session via cookie-based refresh
- Unauthenticated routes redirect to login
- Authenticated routes redirect to dashboard if already logged in
- Playwright E2E test covers login → dashboard → logout

---

#### Spec 3.2: `web-dashboard-v1`

**Objective:** Build the main dashboard showing the user's current plan, recent sessions, and quick stats.

**Scope (in):**
- Active plan summary card (name, current week, current week type)
- "Start Today's Workout" CTA (links to active day)
- Recent sessions list (last 5, with date, duration, exercise count)
- Quick stats: current week session count, total sessions this month, current streak
- Empty state when no active plan

**Scope (out):** Charts, detailed analytics, nutrition summary (added in Phase 6).

**Domain Logic (rendering only):**
- "Today's Workout" is derived from the active plan's current week and the current day of the week. If no workout is scheduled for today, show the next scheduled day.
- Streak is calculated client-side from the recent sessions list (consecutive days with a completed session).

**Edge Cases:**
- No active plan → show "Create your first plan" CTA
- Active plan has no sessions yet → show "Start your first workout" CTA
- Session in progress (started but not completed) → show "Continue Workout" CTA instead

**Dependencies:** Spec 3.1, Spec 2.4

**Acceptance Criteria:**
- Dashboard renders correctly with real data from backend
- Empty states are handled for all combinations (no plan, no sessions, no today's workout)
- Loading states shown during API calls
- Error state shown on API failure

---

#### Spec 3.3: `training-plan-editor-web`

**Objective:** Build the full plan editor — the primary tool for constructing and editing training plans.

**Scope (in):**
- Plan list page with create, archive, activate actions
- Plan editor: add/edit/delete weeks
- Week editor: set week type, add/edit/delete days
- Day editor: add/edit/reorder/delete exercise instances
- Exercise search with inline add from library
- Exercise instance form: sets, reps, load, method type, rest, notes
- Superset grouping UI (drag two exercises to the same group)
- Plan duplication action

**Scope (out):** Mobile drag-and-drop (mobile is execution-only). Progression rule configuration (Phase 5 web integration).

**Domain Logic (rendering only):**
- Week type badge rendered with color coding (normal=blue, deload=yellow, refeed=green, custom=purple)
- Exercise position managed via optimistic updates (UI reorders immediately, API called async)

**Edge Cases:**
- Reordering exercise while another reorder request is in flight → queue requests, do not allow concurrent reorders
- Editing a plan that has logged sessions against it → warn the user that changes may affect historical data; do not block
- Adding an exercise that conflicts with a superset group → validate superset group consistency before saving

**Dependencies:** Spec 3.1, Spec 2.3, Spec 2.2

**Acceptance Criteria:**
- Full plan CRUD works end-to-end
- Exercise search returns results in under 300ms (with debounce)
- Superset grouping works visually and is saved correctly
- Plan duplication creates a copy visible in the plan list

---

#### Spec 3.4: `workout-history-web`

**Objective:** Build the session history browser — allowing users to review past workouts.

**Scope (in):**
- Session history list (paginated, filterable by date range, plan)
- Session detail view: all sets logged, readiness score, notes, duration
- Exercise-level history: previous N sessions for a given exercise (for context)

**Scope (out):** Analytics charts (Phase 6). PR highlighting (Phase 6).

**Edge Cases:**
- Viewing a session from a now-deleted plan → session still visible; plan name shown as "[Archived Plan]"
- Very long sessions (3+ hours) → duration formatted as hours:minutes
- Sessions with 0 exercises logged → shown with "Rest day" label

**Dependencies:** Spec 3.1, Spec 2.4

**Acceptance Criteria:**
- History list paginates correctly
- Session detail shows all set logs accurately
- Date range filter works correctly

---

#### Spec 3.5: `analytics-dashboard-web-v1`

**Objective:** Build the first analytics surface — PR tracking and volume trends.

**Scope (in):**
- Personal records table: exercise name, record type (actual, estimated 1RM), value, date
- Volume chart: sets per muscle group per week (bar chart, last 8 weeks)
- Adherence tracker: sessions completed vs planned per week

**Scope (out):** Fatigue trends, nutrition overlay, coaching decision history (Phase 6+).

**Domain Logic (rendering only):**
- Volume data fetched from `/api/v1/analytics/volume?weeks=8`
- Charts rendered with Recharts or Chart.js
- Estimated 1RM from backend: `1RM = load * (1 + reps / 30)` (Epley formula, computed backend-side)

**Edge Cases:**
- Less than 8 weeks of data → chart shows available weeks only, no empty placeholders
- No PRs recorded → empty state with "Complete workouts to track PRs"
- Volume data for a muscle group with 0 sets → not rendered (omit from chart)

**Dependencies:** Spec 3.1, Spec 2.4 (session data must exist)

**Acceptance Criteria:**
- PR table renders correctly with real data
- Volume chart shows correct data for last 8 weeks
- Adherence metric is accurate against logged sessions

---

### PHASE 4: Mobile App (Flutter)

**Objective:** Build the in-gym mobile experience. Mobile is execution-only — not a plan editor.

---

#### Spec 4.1: `mobile-auth-foundation`

**Objective:** Implement authentication on mobile with secure token storage.

**Scope (in):**
- Login screen
- Registration screen
- Secure token storage: access token in memory, refresh token in Flutter Secure Storage
- Auto-refresh on 401 (Dio interceptor)
- Splash screen with auth check (redirect based on token validity)
- Logout

**Domain Logic:**
- On app launch: check if refresh token exists in secure storage → call `/auth/refresh` → if valid, enter app; if not, show login.
- Refresh token stored in Flutter Secure Storage (Keychain on iOS, Keystore on Android).

**Edge Cases:**
- App killed mid-session → on relaunch, refresh token is still valid → user enters app directly
- Device clock skew causes premature token expiry → if server returns 401 on a seemingly valid token, force refresh before showing login

**Dependencies:** Spec 1.1, Spec 0.4

**Acceptance Criteria:**
- Login and logout work end-to-end on both platforms
- App re-authenticates silently from refresh token after kill/relaunch
- Credentials are not stored in plaintext (verified on device)

---

#### Spec 4.2: `mobile-active-workout-flow`

**Objective:** Build the primary mobile workflow: viewing today's workout and navigating through exercises.

**Scope (in):**
- Home screen: today's workout card (exercise list preview)
- Start workout → creates session via API
- Workout screen: exercise list, current exercise highlight
- Navigation: previous/next exercise
- Session notes input
- Complete session action

**Scope (out):** Set logging (Spec 4.3). Offline mode (Spec 4.5).

**Domain Logic:**
- "Today's workout" resolved by backend (`GET /api/v1/sessions/today` → returns the active plan's day for today or the next scheduled day).
- If a session is already in progress (started but not completed), the home screen shows "Continue" instead of "Start".

**Edge Cases:**
- No active plan → home shows "Set up a plan on the web app" guidance
- Today is a rest day in the plan → home shows rest day card
- Network error when starting session → show retry prompt, do not create a local placeholder

**Dependencies:** Spec 4.1, Spec 2.4

**Acceptance Criteria:**
- Start workout creates a session and navigation enters the workout screen
- Exercise list matches the plan's day structure
- Complete session calls the correct endpoint and shows confirmation
- In-progress session is correctly surfaced on home screen re-entry

---

#### Spec 4.3: `mobile-set-logging-and-timer`

**Objective:** Build the core set logging interface and rest timer.

**Scope (in):**
- Set logging form: reps input, load input, RPE selector (optional, 1–10)
- Log set action (calls `POST /api/v1/sessions/{id}/sets`)
- Skip set action
- Rest timer: auto-starts after each logged set (duration from `rest_seconds` on exercise instance)
- Timer: countdown with vibration at 0, skip timer option
- Previous performance display: last N sets for this exercise (from history)
- Set status indicators (logged / skipped / pending)

**Domain Logic:**
- Previous performance is fetched at workout start and cached locally for the session (not re-fetched per set).
- Rest timer is purely client-side. Timer state is not sent to backend.
- If load input is left blank and exercise is not bodyweight → validation error (required field).
- If exercise is bodyweight → load field is hidden; reps only.

**Edge Cases:**
- User closes app during rest timer → timer state is lost; this is acceptable in v1
- Network error on set log → retry once automatically; if still fails, queue for offline sync (Spec 4.5)
- Negative load entered → validation error
- Very high reps (>100) → allowed, but show warning "That's a lot of reps — did you mean to log this?"

**Dependencies:** Spec 4.2

**Acceptance Criteria:**
- Set logging calls API and updates set status immediately
- Rest timer starts automatically after logging a set
- Previous performance is displayed correctly
- Bodyweight exercises hide the load field

---

#### Spec 4.4: `mobile-history-and-recent-performance`

**Objective:** Build the mobile history view for quick reference during workouts.

**Scope (in):**
- Recent sessions list (last 10)
- Session detail: exercise list + set logs
- Exercise history: last 3 sessions for a given exercise (accessed from within the workout flow)

**Scope (out):** Charts, analytics (web-only in v1).

**Edge Cases:**
- No session history → empty state
- History loaded while offline → show cached data from last successful load

**Dependencies:** Spec 4.1, Spec 2.4

**Acceptance Criteria:**
- History list loads and displays correctly
- Exercise history accessible from within workout flow
- Offline cached history shows stale data notice

---

#### Spec 4.5: `mobile-offline-cache-v1`

**Objective:** Enable workout execution without network connectivity.

**Scope (in):**
- Offline detection via `connectivity_plus` package
- Active session data cached locally on session start (exercise instances, previous performance)
- Set logs queued locally when offline (stored in Hive)
- Sync queue processed when connectivity returns
- Sync status indicator in UI (syncing, synced, pending)
- Idempotent sync: each operation has a UUID; server deduplicates

**Scope (out):**
- Plan editing offline
- History browsing offline (only most recent cached session)
- Conflict resolution UI (server is authoritative; no UI for conflict resolution in v1)

**Domain Logic:**
- Offline operations are stored in a local queue: `[ { operation_id, type, resource, payload, local_timestamp } ]`
- On reconnect: queue is sent to `POST /api/v1/sync/push` in order
- Server processes operations and returns: `{ succeeded: [], failed: [], conflicts: [] }`
- Failed operations are shown to the user with a retry option
- Conflicts (e.g., session already locked on server): user is notified; conflicting local data is discarded

**Edge Cases:**
- Device runs out of Hive storage while offline → queue is capped at 500 operations; oldest operations are dropped with a warning
- User completes a session offline → session `complete` operation is queued; server applies it in order during sync
- Sync interrupted mid-way → completed operations are marked; remaining operations re-sent on next sync (idempotency prevents duplicates)

**Dependencies:** Spec 4.3, Spec 2.4, Backend Sync module

**Acceptance Criteria:**
- Set logging works with airplane mode enabled
- All queued operations sync successfully on reconnect
- Sync status indicator reflects actual state
- Server deduplication confirmed: replaying a sync queue twice produces no duplicates

---

### PHASE 5: Coaching Engine

**Objective:** Transform GymOS from a logging tool into an adaptive training intelligence platform.

---

#### Spec 5.1: `progression-engine-v1`

**Objective:** Implement the core progression algorithm — the engine that decides whether to increase, maintain, or decrease load.

**Scope (in):**
- Progression decision logic for all supported progression rules
- Input: exercise instance config, last session performance, week type, readiness score
- Output: `{ suggested_load_kg, suggested_reps, adjustment_type, rationale, confidence, rule_version_id }`
- Progression rules implemented:
  - `linear`: increase load by fixed increment if all sets completed at target reps
  - `double_progression`: increase reps first (within a rep range), then increase load when top of range achieved
  - `wave_load`: 3-week wave pattern (heavy/medium/light relative to a base load)
  - `percentage_based`: calculate load as % of 1RM (1RM estimated from best recent performance)

**Domain Logic:**

**Linear Progression:**
```
if reps_actual >= reps_target for ALL sets:
    suggested_load = load_actual + increment_kg
    adjustment_type = "increase"
elif reps_actual >= reps_target for >= 50% of sets:
    suggested_load = load_actual  (maintain)
    adjustment_type = "maintain"
else:
    suggested_load = load_actual - increment_kg
    adjustment_type = "decrease"

increment_kg defaults:
  upper_body: 2.5 kg
  lower_body: 5.0 kg
  isolation: 1.25 kg
```

**Double Progression:**
```
if reps_actual == reps_range_high for ALL sets (for N consecutive sessions):
    increase load by increment; reset reps_target to reps_range_low
elif reps_actual >= reps_range_low for all sets:
    reps_target = reps_actual + 1 (progress reps)
else:
    maintain current reps_target
```

**Readiness modifier:**
```
readiness_score 1–3: apply -10% load modifier (hard floor: not below -20% from target)
readiness_score 4–6: no modifier (normal)
readiness_score 7–10: no modifier (do not auto-increase beyond rule logic)
```

**API Endpoints:**
```
POST /api/v1/coaching/next-load
POST /api/v1/coaching/progression-preview   (preview without committing)
GET  /api/v1/coaching/recommendations/{session_id}
```

**Edge Cases:**
- First ever session for an exercise (no history) → suggest `load_target_kg` from plan, no adjustment
- Last session had all sets skipped → treat as a missed session; maintain current load
- Readiness score not provided → treat as 7 (neutral, no modifier)
- Exercise with `method_type=drop_set` → progression is calculated on the first (heaviest) set only; drop percentages are maintained

**Dependencies:** Spec 2.4, Spec 5.6 (rule versioning must exist before first engine write)

**Acceptance Criteria:**
- Unit tests cover all progression rules with named fixture scenarios
- Linear progression correctly increases, maintains, and decreases load
- Double progression correctly transitions from rep increase to load increase
- Readiness modifier correctly adjusts suggestions
- All outputs include `rule_version_id`

---

#### Spec 5.2: `fatigue-model-v1`

**Objective:** Implement a fatigue accumulation model that modulates coaching decisions based on training stress.

**Scope (in):**
- Fatigue score calculated per user per muscle group per week
- Inputs: session logs over the past 2–4 weeks (volume, intensity, frequency)
- Output: `{ muscle_group: str, fatigue_level: "low" | "moderate" | "high" | "excessive", fatigue_score: float }`
- Fatigue level influences coaching recommendations (not overrides)
- Background job recalculates fatigue weekly

**Domain Logic:**

```
Weekly Stress Score (WSS) per muscle group:
  WSS = Σ (sets * reps * relative_intensity)
  relative_intensity = load_actual / estimated_1RM

Fatigue accumulation (simple exponential decay model):
  fatigue_t = WSS_current + (fatigue_t-1 * decay_factor)
  decay_factor = 0.85 (configurable per rule version)

Fatigue levels:
  fatigue_score < 0.5 * baseline_WSS  → "low"
  fatigue_score 0.5–1.0 * baseline_WSS → "moderate"
  fatigue_score 1.0–1.5 * baseline_WSS → "high"
  fatigue_score > 1.5 * baseline_WSS   → "excessive"

Coaching modifiers:
  "excessive" fatigue for a muscle group:
    → flag for deload consideration in recommendation
    → do not auto-recommend load increases for that muscle group
  "high" fatigue:
    → include note in recommendation: "volume accumulation is high for [muscle]"
```

**Edge Cases:**
- New user with no session history → fatigue_score = 0 for all muscle groups (no history = no fatigue)
- User takes 2+ weeks off → decay model naturally reduces fatigue to near zero; detraining is NOT modeled in v1
- Exercise with multiple secondary muscles → WSS is distributed: 100% to primary, 50% to each secondary

**Dependencies:** Spec 5.1, Spec 2.4

**Acceptance Criteria:**
- Fatigue calculation produces correct scores for documented fixture scenarios
- Background job runs weekly and updates fatigue snapshots
- Fatigue level "excessive" correctly suppresses load increase recommendations
- Unit test coverage: 100% of fatigue calculation branches

---

#### Spec 5.3: `week-type-adjustment-engine-v1`

**Objective:** Implement week type modifiers that alter coaching outputs based on the current training week type.

**Scope (in):**
- Week type modifier tables (configurable per rule version)
- Applied on top of base progression engine output
- Week types: `normal`, `deload`, `refeed`, `custom`
- Modifiers: `load_modifier_%`, `sets_modifier_%`, `reps_modifier_%`, `rest_modifier_seconds`

**Domain Logic:**

```
Default modifier tables (v1):

normal:
  load_modifier: 0%      (no change)
  sets_modifier: 0%
  reps_modifier: 0%
  rest_modifier: 0

deload:
  load_modifier: -10%
  sets_modifier: -50%    (e.g., 4 sets → 2 sets)
  reps_modifier: 0%
  rest_modifier: +30s

refeed:
  load_modifier: 0%
  sets_modifier: -20%
  reps_modifier: 0%
  rest_modifier: 0

custom:
  All modifiers explicitly set on the training_week record (no defaults)

Application order:
  1. Get base suggestion from progression engine
  2. Apply week type modifier to load and reps
  3. Apply readiness modifier
  4. Round load to nearest 0.25 kg (equipment constraint)
  5. Enforce minimum load floor (bodyweight = 0; weighted = 2.5 kg minimum)
```

**Edge Cases:**
- Custom week with no modifiers set → treat as `normal` (no modifiers)
- Deload modifier results in 0 sets → floor at 1 set minimum
- Refeed week for an exercise with no previous load → use `load_target_kg` from plan

**Dependencies:** Spec 5.1

**Acceptance Criteria:**
- Deload modifier correctly reduces sets and load from base suggestion
- Custom week applies only explicitly configured modifiers
- Modifier rounding is consistent (0.25 kg increments)
- All modifier combinations have unit test coverage

---

#### Spec 5.4: `expected-load-and-next-load-calculator`

**Objective:** Expose the pre-session expected load calculation as a dedicated API — the "what should I do today" endpoint.

**Scope (in):**
- `GET /api/v1/coaching/today` — returns expected loads for all exercises in today's session
- `POST /api/v1/coaching/next-load` — calculate next load for a single exercise instance
- Calculation pipeline: history lookup → progression engine → week type adjustment → fatigue modifier → rounding
- Response includes full rationale chain

**API Endpoints:**
```
GET /api/v1/coaching/today
Response:
{
  "data": {
    "session_day_id": "uuid",
    "week_type": "normal",
    "exercises": [
      {
        "exercise_instance_id": "uuid",
        "exercise_name": "Bench Press",
        "suggested_sets": 4,
        "suggested_reps": 8,
        "suggested_load_kg": 90.0,
        "adjustment_type": "increase",
        "fatigue_level": "moderate",
        "rationale": "Completed all 4x8 @ 87.5kg last session. Linear progression: +2.5kg.",
        "engine_version": "v1.0.0",
        "rule_version_id": "uuid"
      }
    ]
  }
}
```

**Edge Cases:**
- No active plan → 404 with `{ "error": { "code": "NO_ACTIVE_PLAN" } }`
- Today is a rest day → 200 with `{ "data": { "is_rest_day": true, "exercises": [] } }`
- Exercise has no session history → suggestion uses `load_target_kg` from plan with `adjustment_type: "baseline"`

**Dependencies:** Spec 5.1, 5.2, 5.3

**Acceptance Criteria:**
- `GET /coaching/today` returns correct suggestions matching the active plan's day
- Full rationale chain is included in response
- Response time < 500ms for a plan with up to 10 exercises

---

#### Spec 5.5: `method-aware-training-rules`

**Objective:** Extend the coaching engine to correctly handle special training methods.

**Scope (in):**
- Superset: no rest between grouped exercises; rest after the group; progression calculated independently per exercise
- Drop set: progression calculated on the first (heaviest) set; drop percentages are maintained relative to first set
- Rest-pause: reps logged as multiple mini-sets; total reps compared to target for progression decision
- Cluster: similar to rest-pause; logged as cluster groups
- AMRAP: no reps_target upper bound; progression triggers when average reps exceed threshold by N sessions

**Domain Logic:**

```
Superset handling:
  - exercise_instances with same superset_group_id form a group
  - rest_seconds applied once after all exercises in group are completed
  - progression calculated independently per exercise

Drop set handling:
  - set_logs with is_drop=true are excluded from progression calculation
  - only the first (non-drop) set determines progression decision
  - drop percentages: [100%, 80%, 60%] of first set load — configurable

AMRAP handling:
  - progression_trigger_reps: if reps_actual > reps_target + progression_threshold for N sessions
    then increase load
  - progression_threshold default: 3 reps above target
  - N default: 2 consecutive sessions
```

**Edge Cases:**
- Superset group with exercises targeting the same muscle → allowed; fatigue model accounts for combined volume
- Drop set with first set failed → all drops inherit "failed first set" status; no progression
- AMRAP with only 1 session of history → no progression decision possible yet (insufficient data)

**Dependencies:** Spec 5.1, 5.3

**Acceptance Criteria:**
- Superset progression is independent per exercise in the group
- Drop set progression ignores drop set logs correctly
- AMRAP progression triggers only after N qualifying sessions
- Unit tests cover each method type with example fixture data

---

#### Spec 5.6: `coaching-rule-versioning`

**Objective:** Implement the versioning system for the coaching engine — ensuring all outputs are traceable and the engine can evolve safely.

**Scope (in):**
- `rule_versions` table with: engine_name, semantic_version, is_active, activated_at, config_snapshot_json
- Engine registry: maps `engine_name` + `version` to the correct Python class
- Active version lookup: for each engine, exactly one version is `is_active=true` at a time
- All coaching outputs include `rule_version_id` (FK to `rule_versions`)
- Admin API to activate/deactivate a rule version
- Version activation is atomic: deactivate old → activate new in a single transaction

**Domain Logic:**

```
Engine names (v1):
  - progression_engine
  - fatigue_model
  - week_adjustment_engine
  - load_calculator

Version format: semver (e.g., "1.0.0", "1.1.0", "2.0.0")

config_snapshot_json: stores all configurable parameters at the time of activation
  (e.g., decay_factor, progression thresholds, week type modifier tables)
  This allows reproducing past decisions exactly, even if the default config changes.

Version activation:
  POST /api/v1/admin/coaching/rule-versions/{id}/activate
  → within a transaction:
    1. set current active version for engine_name to is_active=false
    2. set requested version to is_active=true
    3. record activated_at timestamp
```

**Edge Cases:**
- Activating a version for an engine that has no currently active version → allowed (first activation)
- Attempting to activate a version that is already active → 409 Conflict
- Requesting coaching decision when no active version exists for an engine → 503 with `{ "error": { "code": "ENGINE_UNAVAILABLE" } }`

**Dependencies:** Spec 2.4

**Acceptance Criteria:**
- Every coaching output includes a valid `rule_version_id`
- Version activation is atomic (verified by concurrent activation test)
- Config snapshot is stored correctly at activation time
- Past coaching decisions remain readable even after engine is upgraded

---

### PHASE 6: Analytics

**Objective:** Surface meaningful performance data to users and enable data-driven coaching decisions.

---

#### Spec 6.1: `personal-records-and-performance-metrics`

**Objective:** Track, detect, and surface personal records automatically.

**Scope (in):**
- PR types: actual PR (heaviest weight for exact reps), estimated 1RM (Epley: `load * (1 + reps/30)`)
- Automatic PR detection: after each session lock, background job checks if any set log beats previous records
- PR history per exercise (all-time, last 90 days)
- `personal_records` table
- API: list PRs per exercise, global PR feed (recent PRs across all exercises)

**Domain Logic:**
```
Epley 1RM = load_kg * (1 + reps / 30)
PR detection (runs after session lock):
  for each set_log in session:
    if set_log.load_kg > max(load_kg for same exercise, same reps) → actual PR
    if epley(set_log) > max(estimated_1RM for exercise) → 1RM PR
```

**Edge Cases:**
- Set with reps = 1 → estimated 1RM = actual load (1 + 1/30 ≈ 1.03 ≈ actual)
- Set marked as skipped → excluded from PR calculation
- Exercise deleted → PRs retained with exercise_id preserved; exercise shown as [Archived]

**Dependencies:** Spec 2.4

**Acceptance Criteria:**
- PR detection runs correctly after each session lock
- Epley formula produces correct values (verified with fixture data)
- PRs are not detected for skipped sets
- PR feed is paginated and sorted by achieved_at descending

---

#### Spec 6.2: `muscle-volume-analytics-v1`

**Objective:** Calculate and expose training volume per muscle group per week.

**Scope (in):**
- Volume calculation: `sets * reps * load_kg` per muscle group per week
- Weekly snapshot materialization (background job, runs after each session lock)
- API: `GET /api/v1/analytics/volume?muscle=&weeks=8`
- Breakdown by: total volume, total sets, total reps

**Domain Logic:**
- Volume is attributed to `primary_muscle` at 100% and each `secondary_muscle` at 50%
- Only completed sets (not skipped) count toward volume
- Snapshots are updated incrementally (only the current week is recalculated on each session lock)

**Edge Cases:**
- Session locked mid-week → snapshot for that week is updated, prior weeks unchanged
- Exercise with no secondary muscles → 100% attributed to primary only
- User changes `unit_preference` → volume stored in kg; API converts to lbs on response if preference = imperial

**Dependencies:** Spec 6.1, Spec 2.4

**Acceptance Criteria:**
- Volume snapshots match manual calculation for documented fixture sessions
- Incremental update only recalculates the current week
- API response time < 200ms for 8 weeks of data

---

#### Spec 6.3: `progression-trend-engine-v1`

**Objective:** Calculate and expose load progression trends per exercise over time.

**Scope (in):**
- Trend data: session-by-session load and estimated 1RM per exercise
- Linear regression slope over last N sessions (indicates direction of progression)
- Trend classification: `improving`, `plateaued`, `declining`
- API: `GET /api/v1/analytics/trends/{exercise_id}?sessions=12`

**Domain Logic:**
```
Trend classification:
  slope > 0.5 kg/session → "improving"
  slope between -0.5 and 0.5 → "plateaued"
  slope < -0.5 → "declining"

Minimum sessions for trend: 3 (fewer → return { trend: "insufficient_data" })
```

**Edge Cases:**
- Exercise with high variance (weight fluctuates) → regression smooths this; a single poor session does not flip trend to "declining"
- Bodyweight exercise (load=0) → trend based on reps, not load

**Dependencies:** Spec 6.1, Spec 2.4

**Acceptance Criteria:**
- Trend classification is correct for documented fixture datasets
- Insufficient data case handled gracefully
- Bodyweight trend calculated from reps correctly

---

#### Spec 6.4: `adherence-and-consistency-metrics`

**Objective:** Track and expose user adherence to their training plan.

**Scope (in):**
- Weekly adherence: sessions_completed / sessions_planned per week
- Rolling 30-day adherence %
- Current streak (consecutive days with a completed session)
- Longest streak (all-time)
- API: `GET /api/v1/analytics/adherence`

**Domain Logic:**
- `sessions_planned` derived from the active plan's week structure (days with at least 1 exercise)
- Missed session: a planned day passes without a completed session
- Rest days (days with 0 exercise instances) do not count as planned or missed

**Edge Cases:**
- User switches active plan mid-week → planned sessions for that week split between two plans; both count
- No active plan → adherence is not calculable; return `{ "error": "NO_ACTIVE_PLAN" }`
- Plan activated mid-week → planned sessions start from activation date, not week start

**Dependencies:** Spec 2.4, Spec 2.3

**Acceptance Criteria:**
- Adherence % matches manual calculation for fixture data
- Streak calculation is correct across week boundaries
- Plan switch mid-week handled correctly

---

### PHASE 7: Nutrition & Recovery

**Objective:** Capture recovery and nutrition context to enrich coaching decisions.

---

#### Spec 7.1: `readiness-and-recovery-logging`

**Objective:** Allow users to log daily readiness and recovery activities.

**Scope (in):**
- Daily readiness log: sleep_hours, sleep_quality (1–10), energy_level (1–10), soreness_level (1–10), stress_level (1–10), notes
- Recovery activities: type (cardio, sauna, stretching, massage, ice bath), duration_minutes, notes
- Composite readiness score: `(sleep_quality * 0.4) + (energy_level * 0.3) + (10 - soreness_level) * 0.2 + (10 - stress_level) * 0.1`
- API: CRUD for readiness logs and recovery activities
- Readiness score made available to coaching engine for load modifier decisions

**Domain Logic:**
- One readiness log per user per day (upsert on date)
- Composite readiness score is computed by backend and returned in API response
- If readiness log is missing for today: coaching engine uses neutral score (7)

**Edge Cases:**
- Logging readiness for a future date → 400 validation error
- Readiness score below 4 for 3 consecutive days → trigger "recovery alert" notification (Phase 8)

**Dependencies:** Spec 1.2, Spec 5.1

**Acceptance Criteria:**
- Readiness CRUD works correctly
- Composite score calculation is correct for documented fixture inputs
- Missing readiness log defaults coaching engine to neutral score

---

#### Spec 7.2: `nutrition-tracking-v1`

**Objective:** Allow users to log daily nutrition and body weight.

**Scope (in):**
- Daily nutrition log: calories, protein_g, carbs_g, fat_g, water_ml, notes
- Body weight log: weight_kg, logged_date
- Weekly nutrition averages (calculated by backend)
- API: CRUD for nutrition logs and body weight logs

**Domain Logic:**
- One nutrition log per user per date (upsert)
- Macros validation: protein_g + carbs_g + fat_g ≤ calories / 4 * 4 (approximate; not strictly enforced, but flagged in response)
- Body weight trend (7-day moving average) computed and returned in analytics

**Edge Cases:**
- Zero calories logged with non-zero macros → allowed (partial logging)
- Body weight log in the future → 400 validation error
- Weekly average with fewer than 3 days logged → return available days with a `partial: true` flag

**Dependencies:** Spec 1.2

**Acceptance Criteria:**
- Nutrition CRUD and body weight CRUD work correctly
- Weekly averages are correct for fixture data
- Moving average body weight calculation is correct

---

#### Spec 7.3: `weekly-summary-engine-v1`

**Objective:** Generate and deliver a weekly training and nutrition summary.

**Scope (in):**
- Weekly summary: sessions completed, total volume by muscle, PRs achieved, adherence %, average readiness, average nutrition (if logged)
- Summary generated every Monday for the prior week (background job)
- API: `GET /api/v1/analytics/weekly-summary?week_start=YYYY-MM-DD`
- Stored in DB for history retrieval

**Domain Logic:**
- Week starts Monday (ISO 8601 week)
- Summary generation is idempotent: re-running for the same week overwrites the stored summary
- If no sessions in the week → summary still generated (shows 0s and adherence %)

**Edge Cases:**
- Summary requested for a future week → 400 error
- Summary not yet generated for the most recent week → trigger synchronous generation on demand

**Dependencies:** Spec 6.1, 6.2, 6.4, 7.1, 7.2

**Acceptance Criteria:**
- Weekly summary generated correctly matches individual metric values
- Monday job runs reliably
- Summary retrieval for past weeks returns stored (not recalculated) data

---

### PHASE 8: Notifications

**Objective:** Drive engagement and surface coaching insights via push notifications.

---

#### Spec 8.1: `notification-service-v1`

**Objective:** Build the notification infrastructure and delivery system.

**Scope (in):**
- Push notification delivery via FCM (Android) and APNs (iOS)
- Device token registration API: `POST /api/v1/notifications/devices`
- Notification types: `workout_reminder`, `streak_nudge`, `coaching_summary`, `recovery_alert`, `sync_status`
- Notification record stored in DB for history
- User notification preferences (per type, on/off) from Spec 1.2

**Domain Logic:**
- FCM and APNs integrations use the same internal notification service interface
- Failed delivery: retry up to 3 times with exponential backoff (1s, 4s, 16s)
- Token expiry: if delivery returns a token-invalid response, mark device token as inactive
- Do Not Disturb: if user has set quiet hours (Phase 9), schedule notifications for delivery after quiet hours end

**Edge Cases:**
- User has multiple devices → notification sent to all active device tokens for that user
- Device token changes (app reinstall) → old token deactivated on first failed delivery; new token registered by app
- User disables a notification type → skip delivery for that type; do not remove from DB

**Dependencies:** Spec 1.2, Spec 0.5 (Redis for job queue)

**Acceptance Criteria:**
- Device token registration works for both Android and iOS
- Notification delivery recorded in DB
- Retry logic verified: up to 3 retries with correct backoff
- Notifications respect per-type user preferences

---

#### Spec 8.2: `workout-reminder-scheduler`

**Objective:** Schedule and deliver workout reminders based on the user's training plan.

**Scope (in):**
- Daily job: identifies users with a workout scheduled today who have not yet started a session
- Sends `workout_reminder` notification at the user's preferred reminder time (default: 08:00 local time)
- Nudge: if no session started by 18:00, send a second nudge notification
- Streak nudge: if user has a streak ≥ 3 days and today's workout is not yet started by 14:00, send a streak-preservation nudge

**Domain Logic:**
- Job runs every hour; checks for reminders due in the next hour
- User's timezone is stored in `profiles` (added to this spec)
- If user has already completed today's session → no reminder sent
- If user's notification preference for `workout_reminder` is off → skip

**Edge Cases:**
- User has no active plan → no reminder sent
- Today is a rest day in the plan → no reminder sent
- User completes session after reminder is sent → no nudge sent at 18:00

**Dependencies:** Spec 8.1, Spec 2.4, Spec 1.2

**Acceptance Criteria:**
- Reminders are sent at the correct time in the user's timezone
- No reminder sent for rest days or users without active plans
- No nudge sent if session was completed after initial reminder
- Streak nudge triggers correctly at ≥ 3 day streak

---

### PHASE 9: Production Hardening

**Objective:** Prepare GymOS for real production traffic — security, performance, reliability, and release process.

---

#### Spec 9.1: `security-hardening`

**Objective:** Systematic security review and hardening before production launch.

**Scope (in):**
- Rate limiting: all auth endpoints (10 req/min/IP), all API endpoints (1000 req/min/user)
- CORS: strict allowlist of production origins only
- Secrets rotation: documented process for rotating JWT private key, DB passwords, FCM keys
- Dependency audit: `pip-audit` for backend, `npm audit` for web, `flutter pub audit` for mobile
- OWASP Top 10 review: SQL injection (already mitigated by ORM), XSS (CSP headers on web), CSRF (SameSite cookies)
- Input size limits: request body max 1MB for all endpoints
- Access log review: verify row-level security is enforced for all modules

**Edge Cases:**
- JWT private key rotation: new key issues new tokens; old key kept for token validation until all old tokens expire (TTL 15 min)
- Rate limit on load balancer vs. application layer: Nginx handles IP-based rate limits; application handles user-based rate limits

**Acceptance Criteria:**
- `pip-audit` and `npm audit` report 0 high/critical vulnerabilities
- CORS is restricted to production origins
- Rate limiting verified under load test
- Row-level security verified: penetration test script confirms user A cannot access user B's data

---

#### Spec 9.2: `performance-and-query-optimization`

**Objective:** Ensure the backend meets performance targets under realistic load.

**Scope (in):**
- Identify and add missing DB indexes (all FK columns, all filter columns used in queries)
- Query analysis: `EXPLAIN ANALYZE` on the 10 most frequent query patterns
- Caching: add Redis cache for `GET /coaching/today` (TTL 5 min, invalidated on session lock)
- Pagination: verify all list endpoints use cursor-based pagination (no OFFSET)
- Load test: 500 concurrent users, all training endpoints, measure p95 latency

**Target:**
- Training endpoints: p95 < 200ms
- Coaching decisions: p95 < 500ms
- Analytics: p95 < 1000ms (acceptable for less frequent access)

**Edge Cases:**
- Cache invalidation on session lock: `GET /coaching/today` cache must be invalidated when a session is locked (invalidate by user_id key)
- Long-running analytics queries: add `statement_timeout` = 5s on DB connection for API requests; analytics queries use a separate connection pool with 30s timeout

**Acceptance Criteria:**
- Load test achieves p95 targets with 500 concurrent users
- All 10 analyzed queries show index usage in `EXPLAIN ANALYZE`
- No N+1 queries in any training or coaching endpoint (verified by query count assertion in integration tests)

---

#### Spec 9.3: `release-pipeline-and-staging`

**Objective:** Establish the full CI/CD pipeline and staging environment.

**Scope (in):**
- Staging environment: full stack deployment (backend, web, mobile API-compatible)
- GitHub Actions release pipeline:
  - On merge to `main`: build images, push to registry, deploy to staging
  - E2E smoke tests on staging post-deploy
  - Manual promotion gate: staging → production
- Mobile release pipeline: Flutter build → TestFlight (iOS) / Firebase App Distribution (Android)
- Rollback procedure: documented process for reverting a bad release
- Database migration safety: all migrations must be backwards-compatible (additive only, no dropping columns before two releases)

**Edge Cases:**
- Migration failure during deploy → pipeline aborts; previous version stays running; migration rolled back
- E2E smoke tests fail on staging → deploy to staging is blocked; alert is sent; production is not affected

**Acceptance Criteria:**
- Full deploy pipeline runs end-to-end on a test release
- Staging environment accessible and functional
- Rollback procedure is documented and tested (simulate a bad deploy and roll back)
- Migration backwards compatibility rule is enforced in CI (migration linter)

---

#### Spec 9.4: `end-to-end-quality-gates`

**Objective:** Establish final quality gates that must pass before every production release.

**Scope (in):**
- E2E test suite (Playwright for web): covers 5 critical user journeys
  1. Register → create plan → activate plan
  2. Start workout → log sets → complete session
  3. View coaching suggestion → execute → verify PR detection
  4. Review analytics dashboard with volume and PRs
  5. Notification preference update → verify no notifications sent for disabled types
- Mobile integration tests: active workout flow offline → sync → verify server state
- Performance regression gate: if p95 latency for any training endpoint exceeds 300ms in CI load test → build fails
- Security gate: `pip-audit` and `npm audit` must pass

**Acceptance Criteria:**
- All 5 Playwright E2E journeys pass in CI
- Mobile offline → sync test passes
- Performance gate blocks a release that introduces a regression
- Security audit passes before every production release

---

## 15. Definition of Done (Per Spec)

A spec is considered done when:

- [ ] All API endpoints return correct responses (verified by integration tests)
- [ ] All domain logic has unit test coverage (100% of decision branches for coaching engine)
- [ ] Database migrations are created, reviewed, and backwards-compatible
- [ ] API contracts are documented in `docs/api/`
- [ ] Monitoring and logging are in place (errors tracked by Sentry, key events logged)
- [ ] Edge cases from the spec are covered by tests
- [ ] Acceptance criteria are all passing
- [ ] PR reviewed and approved

---

## 16. Spec Execution Order

```
Wave 1 (Foundation):
  0.1 repository-foundation
  0.2 backend-scaffold
  0.3 web-scaffold
  0.4 mobile-scaffold
  0.5 local-dev-and-ci-foundation

Wave 2 (Auth & Users):
  1.1 auth-core
  1.2 user-profile-and-preferences
  1.3 role-and-permissions-model

Wave 3 (Training Domain — backend):
  2.1 training-domain-language
  2.2 exercise-library
  2.3 training-plan-core-model
  2.4 workout-session-logging-core

Wave 4 (Web + Mobile — parallel after Wave 3):
  3.1 web-auth-and-shell          ─┐
  3.2 web-dashboard-v1             │  Web team
  3.3 training-plan-editor-web     │
  3.4 workout-history-web          │
  3.5 analytics-dashboard-web-v1  ─┘

  4.1 mobile-auth-foundation      ─┐
  4.2 mobile-active-workout-flow   │  Mobile team
  4.3 mobile-set-logging-timer     │
  4.4 mobile-history               │
  4.5 mobile-offline-cache-v1     ─┘

Wave 5 (Coaching Engine):
  5.6 coaching-rule-versioning    (must come before other coaching specs)
  5.1 progression-engine-v1
  5.2 fatigue-model-v1
  5.3 week-type-adjustment-engine-v1
  5.4 expected-load-calculator
  5.5 method-aware-training-rules

Wave 6 (Analytics + Nutrition):
  6.1 personal-records
  6.2 muscle-volume-analytics-v1
  6.3 progression-trend-engine-v1
  6.4 adherence-and-consistency-metrics
  7.1 readiness-and-recovery-logging
  7.2 nutrition-tracking-v1
  7.3 weekly-summary-engine-v1

Wave 7 (Notifications):
  8.1 notification-service-v1
  8.2 workout-reminder-scheduler

Wave 8 (Hardening):
  9.1 security-hardening
  9.2 performance-and-query-optimization
  9.3 release-pipeline-and-staging
  9.4 end-to-end-quality-gates
```

---

## 17. Phase Dependencies

```
Phase 0 (Foundation)
  └─▶ Phase 1 (Auth & Users)
        └─▶ Phase 2 (Training Domain)
              ├─▶ Phase 3 (Web App) ─┐
              └─▶ Phase 4 (Mobile)  ─┤
                                     ▼
                              Phase 5 (Coaching Engine)
                                     │
                              Phase 6 (Analytics)
                                     │
                              Phase 7 (Nutrition & Recovery)
                                     │
                              Phase 8 (Notifications)
                                     │
                              Phase 9 (Production Hardening)
```

**Notes:**
- Phase 3 and Phase 4 can run in parallel once Phase 2 is stable (API contracts agreed)
- Phase 5 requires Phase 2 (session data) and Spec 5.6 (rule versioning) before any engine spec begins
- Phase 6 analytics become significantly more valuable after Phase 5 (coaching data enriches analytics)
- Phase 9 hardening is not a final phase — security and performance work starts in Phase 2 and is systematically completed in Phase 9

---

## 18. Key Risks and Mitigations

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | Domain logic duplicated across web/mobile/backend | High | Backend is sole authority; enforced by code review and architecture testing |
| 2 | Coaching engine complexity grows uncontrolled | High | Versioning mandatory; all engine changes require a new version entry |
| 3 | Prototype rules lost during rewrite | High | Spec 2.1 domain extraction must be completed and signed off before implementation |
| 4 | Mobile offline sync underestimated | Medium | Offline scope limited to active session only in v1; expand after validation |
| 5 | Analytics queries slow at scale | Medium | Volume snapshot materialization from Phase 6; query optimization in Phase 9 |
| 6 | Spec granularity too broad | Medium | Each spec must have testable acceptance criteria; broad specs are split |
| 7 | JWT private key compromise | Medium | Key rotation procedure documented in Phase 9; short access token TTL (15 min) limits blast radius |
| 8 | DB schema drift from rapid iteration | Low | Alembic required for all schema changes; CI rejects PRs without migrations |

---

## 19. Success Metrics

| Metric | Target | Measured In |
|---|---|---|
| API p95 latency — training endpoints | < 200ms | Phase 9 load test |
| API p95 latency — coaching decisions | < 500ms | Phase 9 load test |
| Coaching engine unit test coverage | 100% of decision branches | Phase 5 CI |
| Backend integration test coverage | > 80% of all endpoints | Phase 2+ CI |
| Offline session data loss rate | < 1% of sessions | Phase 4 integration test |
| Sync success rate on reconnect | > 99% | Phase 4/8 integration test |
| Time to create and activate a training plan (web) | < 3 minutes | Phase 3 UX test |
| Mobile cold start time | < 2 seconds | Phase 4 device benchmark |
| Production error rate | < 0.1% of requests | Phase 9 Sentry monitoring |
| Weekly adherence calculation accuracy | 100% vs manual | Phase 6 unit test |
