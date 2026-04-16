# Feature Specification: Backend Scaffold

**Feature Branch**: `002-backend-scaffold`
**Created**: 2026-04-09
**Status**: Draft
**Phase**: 0 — Foundation
**Plan Reference**: Plan.md → Spec 0.2

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Backend Starts and Reports Health (Priority: P1)

A developer clones the repository, installs dependencies, sets required environment variables,
and starts the FastAPI application. The server starts without errors. They call the health
check endpoint and receive a valid response confirming the backend is running and can reach
the database.

**Why this priority**: Every subsequent backend spec depends on a runnable server with a
confirmed database connection. Without a working health check, integration test reliability is
undefined and developer onboarding time increases.

**Independent Test**: Can be fully tested by running `uvicorn app.main:app --reload` and
calling `GET /api/v1/health`. Delivers value by confirming the entire dependency chain
(Python, FastAPI, SQLAlchemy, PostgreSQL) is correctly wired.

**Acceptance Scenarios**:

1. **Given** environment variables are set (`DATABASE_URL`, `REDIS_URL`, `APP_ENV`), **When**
   `uvicorn app.main:app` is executed, **Then** the server starts on port 8000 with no
   startup errors in the console.

2. **Given** the server is running and PostgreSQL is reachable, **When** `GET /api/v1/health`
   is called, **Then** the response is `200 OK` with body
   `{ "status": "ok", "version": "0.1.0" }`.

3. **Given** the server is running but PostgreSQL is NOT reachable, **When**
   `GET /api/v1/health` is called, **Then** the response is `503 Service Unavailable` with
   body `{ "status": "degraded", "checks": { "database": "unreachable" } }`.

4. **Given** a required environment variable is missing at startup, **When** the server
   attempts to start, **Then** startup fails immediately with a clear error message naming
   the missing variable — the server does not start in a partially configured state.

---

### User Story 2 — Developer Runs Quality Checks With a Single Command (Priority: P2)

A developer working on the backend runs `make lint` and `make test` from the `backend/`
directory. All lint and type checks execute against the full codebase and report results.
The test suite runs (even with zero tests at this stage) and exits with code 0.

**Why this priority**: Establishing lint, type checking, and test commands before any
application code exists means every future contribution is validated from the start. Retrofitting
these tools after business logic exists is significantly more costly.

**Independent Test**: Can be tested independently by running `make lint` and `make test` in
the `backend/` directory. Delivers value by confirming the quality toolchain (ruff, mypy,
pytest) is correctly configured with project-appropriate rules.

**Acceptance Scenarios**:

1. **Given** Python dependencies are installed, **When** `ruff check .` is run from `backend/`,
   **Then** it exits with code 0 with no violations reported.

2. **Given** Python dependencies are installed, **When** `mypy app/` is run from `backend/`,
   **Then** it exits with code 0 with no type errors reported — strict mode enabled.

3. **Given** Python dependencies are installed, **When** `pytest` is run from `backend/`,
   **Then** it exits with code 0, reports 0 tests collected, and 0 failures (empty suite is
   valid at this stage).

4. **Given** `pyproject.toml` defines all dependencies, **When** `pip install -e ".[dev]"`
   is run in a fresh virtual environment, **Then** all tools (`ruff`, `mypy`, `pytest`,
   `uvicorn`, `sqlalchemy`, `alembic`, `pydantic`) install without version conflicts.

---

### User Story 3 — All Module Routers Are Registered and Reachable (Priority: P3)

A developer inspects the running FastAPI application. Every domain module (`auth`, `users`,
`training`, `coaching`, `analytics`, `nutrition`, `notifications`, `sync`) has a registered
router with a defined prefix. The auto-generated OpenAPI docs at `/docs` show each module's
prefix, confirming the router registration is correct even before any endpoints are implemented.

**Why this priority**: Router registration defines the URL namespace that all future specs
build upon. Establishing this structure now means no future spec needs to debate route
prefixes and no router collisions can occur.

**Independent Test**: Can be tested independently by starting the server and inspecting
`GET /openapi.json` — it must list the prefix for each of the 8 modules.

**Acceptance Scenarios**:

1. **Given** the server is running, **When** `GET /openapi.json` is called, **Then** the
   response includes path entries under `/api/v1/auth/`, `/api/v1/users/`,
   `/api/v1/training/`, `/api/v1/coaching/`, `/api/v1/analytics/`, `/api/v1/nutrition/`,
   `/api/v1/notifications/`, `/api/v1/sync/`.

2. **Given** all module routers are registered, **When** a developer adds a new endpoint
   to the `training` module router, **Then** it is automatically available at
   `/api/v1/training/<new-endpoint>` with no changes needed to `main.py`.

3. **Given** the Alembic baseline migration exists, **When** `alembic upgrade head` is run
   against a fresh database, **Then** it completes successfully with no errors (even though
   no tables are defined yet — baseline migration is valid).

---

### Edge Cases

- **Missing env variable at startup:** The application MUST fail fast with a clear, named
  error on startup — not silently default to `None` or an unsafe value. `pydantic-settings`
  is used specifically to enforce this; every required variable has no default.
- **DB connection failure at health check time:** The health check MUST distinguish between
  "database unreachable" and "application error" in its response body. A `503` with a
  structured body is required — a `500` with an unhandled exception is not acceptable.
- **Port conflict on 8000:** If port 8000 is in use, `uvicorn` fails with a clear OS-level
  error. This is not handled by the application — the developer resolves via an env variable
  (`PORT`). Documented in `README.md`.
- **SQLAlchemy async session on sync code path:** The async session factory must not be called
  from a synchronous context. Any accidental sync usage raises an immediate runtime error.
  `mypy` with `sqlalchemy[mypy]` plugin enforces this at type-check time.
- **Alembic running against wrong database:** `alembic.ini` MUST read `DATABASE_URL` from
  the environment, not hardcode a connection string. A hardcoded connection string in
  `alembic.ini` is a blocker for review.
- **`pyproject.toml` dependency pins:** All production dependencies MUST specify a minimum
  version constraint (`>=`). All dev dependencies MUST be pinned exactly (`==`) to ensure
  reproducible CI runs.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The FastAPI application MUST be created via an `app factory` pattern
  (`create_app()` function in `app/main.py`) to support test-time configuration overrides.
- **FR-002**: The application MUST load all configuration from environment variables using
  `pydantic-settings`. There MUST be no hardcoded configuration values in application code.
- **FR-003**: The application MUST expose `GET /api/v1/health` returning `200` with
  `{ "status": "ok", "version": str }` when all dependencies are reachable.
- **FR-004**: The health endpoint MUST return `503` with `{ "status": "degraded",
  "checks": { "database": "unreachable" | "ok", "redis": "unreachable" | "ok" } }` when
  any dependency is unavailable.
- **FR-005**: All 8 domain module routers (`auth`, `users`, `training`, `coaching`,
  `analytics`, `nutrition`, `notifications`, `sync`) MUST be registered in `main.py`
  under `/api/v1/<module>/`.
- **FR-006**: The SQLAlchemy async session factory MUST be configured and injectable via
  FastAPI's dependency injection system.
- **FR-007**: Alembic MUST be initialized with a baseline migration. `alembic upgrade head`
  MUST succeed against a fresh PostgreSQL database.
- **FR-008**: `pyproject.toml` MUST declare all production and dev dependencies with version
  constraints. The project MUST be installable in one command.
- **FR-009**: `ruff` MUST be configured with the `app/` directory as its target and project-
  appropriate rules (E, F, I, N, UP enabled; S enabled for security linting).
- **FR-010**: `mypy` MUST be configured in strict mode (`strict = true`) targeting `app/`.
  The `sqlalchemy-stubs` or `sqlalchemy[mypy]` plugin MUST be enabled.
- **FR-011**: `pytest` MUST be configured with `asyncio_mode = "auto"` to support async test
  functions. The test discovery path MUST be `tests/`.
- **FR-012**: The application MUST NOT contain any domain model, business logic, or
  authentication code in this spec — routers are empty placeholders only.

### Key Entities

- **App Factory**: `create_app() -> FastAPI` — the single entry point for creating the
  FastAPI application instance. Accepts optional config overrides for test environments.
- **Settings**: A `pydantic-settings` `BaseSettings` subclass that defines all required
  environment variables. Instantiated once at startup; injected as a FastAPI dependency.
- **Module Router**: An `APIRouter` instance per domain module, registered in `main.py`.
  Each router has a prefix (`/api/v1/<module>`) and a tag for OpenAPI grouping.
- **Database Session**: An async SQLAlchemy `AsyncSession`, provided via FastAPI dependency
  injection. One session per request; committed or rolled back at request end.
- **Alembic Environment**: Configured to read `DATABASE_URL` from the environment.
  `env.py` uses the async engine for migrations.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `uvicorn app.main:app` starts in under 5 seconds on a developer machine with
  PostgreSQL and Redis running via Docker Compose.
- **SC-002**: `GET /api/v1/health` returns `200` within 200ms when all dependencies are
  healthy. Returns `503` within 200ms when the database is unreachable.
- **SC-003**: `ruff check .`, `mypy app/`, and `pytest` all exit with code 0 against the
  scaffold codebase (zero application code, zero violations, zero test failures).
- **SC-004**: `alembic upgrade head` completes successfully against a fresh PostgreSQL
  database in under 10 seconds.
- **SC-005**: A new developer can install all dependencies and start the backend in under
  10 minutes by following only the `README.md` and `backend/README.md` instructions.
- **SC-006**: Zero hardcoded secrets, connection strings, or configuration values appear in
  any committed file (verified by `detect-secrets scan`).

---

## Assumptions

- PostgreSQL and Redis are available locally via Docker Compose (Spec 0.5 delivers the
  Compose file; this spec assumes they can be started independently for development).
- Python 3.11 is the target runtime. Type annotations use 3.11+ syntax (`X | Y` union
  syntax; no `Optional[X]`).
- `pyproject.toml` is the single source of project metadata and dependency declaration.
  No `setup.py` or `requirements.txt` files are created.
- The Alembic baseline migration creates zero tables — it establishes the migration history
  only. Table definitions come from Phase 1+ specs.
- `ruff` replaces `flake8`, `isort`, and `pep8` — no separate configurations for those
  tools are created.
- All module routers at this stage return `404 Not Found` for any request to their prefix,
  as no endpoints are implemented. This is expected and acceptable for Phase 0.
- This spec does not configure Sentry error tracking — that is introduced in Phase 2 when
  the first real endpoints exist (per the constitution's observability requirement starting
  from Phase 2).
