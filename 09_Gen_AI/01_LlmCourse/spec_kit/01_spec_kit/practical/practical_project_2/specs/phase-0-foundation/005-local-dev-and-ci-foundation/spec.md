# Feature Specification: Local Dev and CI Foundation

**Feature Branch**: `005-local-dev-and-ci-foundation`
**Created**: 2026-04-09
**Status**: Draft
**Phase**: 0 — Foundation
**Plan Reference**: Plan.md → Spec 0.5

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Developer Brings Up the Full Local Stack in One Command (Priority: P1)

A developer clones the repository on a machine with Docker installed. They run `make up`
from the repository root. Within two minutes, all services are running: the FastAPI backend,
the Next.js web app, PostgreSQL, and Redis. The backend health check returns `200 OK`.
They did not need to install Python, Node.js, or any runtime locally.

**Why this priority**: A one-command local stack is the single most important developer
experience investment in Phase 0. It eliminates setup friction for every contributor, ensures
all developers work against identical infrastructure, and is the prerequisite for all
integration testing across all future specs.

**Independent Test**: Can be fully tested by running `make up` on a clean Docker environment
and verifying `curl http://localhost:8000/api/v1/health` returns `200`. Delivers complete
value independently — a working local stack is immediately usable.

**Acceptance Scenarios**:

1. **Given** Docker and Docker Compose are installed and no services are running, **When**
   `make up` is executed from the repository root, **Then** all four services start
   (`backend`, `web`, `postgres`, `redis`) and the command exits with code 0 within
   120 seconds.

2. **Given** `make up` has completed, **When**
   `curl http://localhost:8000/api/v1/health` is called, **Then** the response is
   `200 OK` with `{ "status": "ok" }`.

3. **Given** all services are running, **When** `make down` is executed, **Then** all
   containers stop and are removed cleanly, and `make up` can be re-run immediately
   without port conflicts or leftover state.

4. **Given** a `.env` file is not present in a service directory, **When** `make up`
   is executed, **Then** Docker Compose reports a clear error naming the missing variable —
   it does not start services with silent `undefined` values.

---

### User Story 2 — CI Validates Backend and Web on Every Pull Request (Priority: P2)

A developer opens a pull request to `main`. GitHub Actions automatically runs the CI
pipeline: backend lint → backend type check → backend tests; web lint → web type check →
web tests. If any step fails, the PR is blocked from merging and the developer sees the
specific failure in the Actions log. If all steps pass, the PR is unblocked.

**Why this priority**: CI is the quality gate that enforces the constitution's standards at
the repository level. Without it, constitution compliance depends entirely on reviewers
catching violations manually. CI enforcement is non-negotiable from the first commit.

**Independent Test**: Can be fully tested by pushing a PR and observing the Actions run.
A passing CI on an empty test suite and a failing CI on a deliberately introduced lint error
validates both the pass and fail paths.

**Acceptance Scenarios**:

1. **Given** a PR is opened targeting `main`, **When** the PR is created or updated with
   a new commit, **Then** the GitHub Actions workflow `ci.yml` is triggered automatically
   within 60 seconds.

2. **Given** the CI workflow is triggered, **When** the backend code has zero lint violations
   and zero type errors, **Then** the `backend-lint` and `backend-test` jobs pass and report
   green status on the PR.

3. **Given** the CI workflow is triggered and a `ruff` violation is present in backend code,
   **When** the `backend-lint` job runs, **Then** it fails, the PR is marked as failing,
   and the violation is visible in the job log.

4. **Given** the CI workflow is triggered, **When** backend tests run, **Then** a real
   PostgreSQL service container is available to the test runner (not a mock), and the
   test suite exits with code 0 on the empty scaffold.

5. **Given** the CI workflow is triggered on a push to `main` (not a PR), **When** all jobs
   pass, **Then** the workflow completes with a green status — no deployment or staging steps
   are triggered at this phase.

---

### User Story 3 — Developer Runs All Tests and Linters With a Single Root Command (Priority: P3)

A developer working on any layer of the stack runs `make test` and `make lint` from the
repository root. Both commands execute the corresponding checks for backend and web in
sequence. The developer does not need to navigate into subdirectories or remember
layer-specific commands.

**Why this priority**: As the codebase grows across three layers (backend, web, mobile),
root-level `make` commands prevent developers from accidentally skipping checks on layers
they are not primarily working on. This supports the constitution's requirement that quality
checks are not optional.

**Independent Test**: Can be tested by running `make test` and `make lint` from the root
and verifying both backend and web checks execute, even with zero tests present.

**Acceptance Scenarios**:

1. **Given** Docker services are up, **When** `make test` is run from the repository root,
   **Then** it sequentially runs `pytest` in `backend/` and `npm run test` in `web/`,
   and exits with code 0 when both pass.

2. **Given** `make lint` is run from the repository root, **When** all code is clean,
   **Then** it runs `ruff check .` in `backend/`, `mypy app/` in `backend/`,
   and `npm run lint` in `web/`, all exiting with code 0.

3. **Given** `make test` is run and backend tests fail, **When** the backend test step
   exits non-zero, **Then** `make test` stops and reports the failure — it does not
   continue to run web tests after a backend failure.

---

### Edge Cases

- **Port conflicts:** If port 8000 (backend), 3000 (web), 5432 (PostgreSQL), or 6379 (Redis)
  is already in use, Docker Compose fails with an OS-level port binding error. This is
  not handled by the compose file — developers override ports via environment variables
  (`BACKEND_PORT`, `WEB_PORT`, etc.) documented in `.env.example`.
- **Volume persistence between restarts:** PostgreSQL data MUST persist between `make down`
  / `make up` cycles because a named volume is used. `make clean` (documented separately)
  removes volumes for a full reset. Developers MUST NOT use `docker-compose down -v`
  without understanding data loss implications — this is documented in `CONTRIBUTING.md`.
- **CI PostgreSQL service container vs. local Docker:** The CI workflow uses GitHub Actions'
  `services:` key to spin up a PostgreSQL container — NOT Docker-in-Docker. The backend
  test runner connects to the service container via `localhost` on the standard port.
  This must be tested before the CI is considered complete.
- **Secrets in CI:** `DATABASE_URL`, `REDIS_URL`, and any other secrets used in CI MUST be
  stored as GitHub Actions Secrets, not hardcoded in `ci.yml`. The `ci.yml` file MUST
  reference `${{ secrets.* }}` for all sensitive values.
- **`detect-secrets` pre-commit hook:** The `ci.yml` MUST include a `detect-secrets` scan
  step that fails the pipeline if any secret patterns are found in committed files.
  This enforces the constitution's security requirement at the CI level.
- **Hot reload in Docker:** The backend container MUST mount the `backend/app/` directory
  as a volume so `uvicorn --reload` picks up code changes without rebuilding the image.
  The web container MUST mount `web/src/` for Next.js hot reload. Failure to configure
  volumes correctly makes local development unusable.
- **CI cache invalidation:** Cache keys MUST use `hashFiles('backend/pyproject.toml')` for
  Python and `hashFiles('web/package-lock.json')` for Node. Using a static cache key
  causes stale dependencies to persist across dependency updates.
- **Mobile CI:** Mobile (Flutter) CI is explicitly out of scope for this spec. It is added
  in Spec 4.x (mobile MVP phase) when the Flutter toolchain is stable and the build process
  is understood. Adding it prematurely in Phase 0 introduces build infrastructure complexity
  before it is needed.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A `docker-compose.yml` MUST exist at `infra/compose/docker-compose.yml` (or
  root) defining four services: `backend`, `web`, `postgres`, `redis`.
- **FR-002**: Each service MUST define a `healthcheck` so Docker Compose can report service
  readiness. The `backend` healthcheck MUST call `GET /api/v1/health`. `postgres` MUST use
  `pg_isready`. `redis` MUST use `redis-cli ping`.
- **FR-003**: PostgreSQL data MUST persist in a named Docker volume across container restarts.
  The volume name MUST be `gymos_postgres_data`.
- **FR-004**: Backend and web containers MUST mount their source directories as volumes to
  enable hot reload during local development.
- **FR-005**: `.env.example` files MUST exist for each service directory (`backend/.env.example`,
  `web/.env.example`) and at the root (`.env.example`). Every required environment variable
  MUST appear with a placeholder value and an inline comment explaining its purpose.
- **FR-006**: A `Makefile` MUST exist at the repository root with targets: `up`, `down`,
  `test`, `lint`, `clean`. Each target MUST have a comment explaining what it does.
- **FR-007**: A GitHub Actions workflow `ci.yml` MUST exist at `.github/workflows/ci.yml`.
  It MUST be triggered on: `pull_request` targeting `main`, and `push` to `main`.
- **FR-008**: The CI workflow MUST contain four jobs: `backend-lint`, `backend-test`,
  `web-lint`, `web-test`. Jobs MUST run in parallel where independent.
- **FR-009**: The `backend-test` job MUST use a GitHub Actions `services:` PostgreSQL
  container. Tests MUST connect to this container via the service hostname.
- **FR-010**: CI MUST cache Python dependencies using `hashFiles('backend/pyproject.toml')`
  as the cache key. CI MUST cache Node dependencies using
  `hashFiles('web/package-lock.json')` as the cache key.
- **FR-011**: A `detect-secrets` scan step MUST run in the CI workflow and fail the pipeline
  if any secrets patterns are detected.
- **FR-012**: No real secrets, API keys, or passwords MUST be committed to any file,
  including `ci.yml`. All sensitive values MUST be referenced as `${{ secrets.* }}`.
- **FR-013**: Mobile CI (Flutter build and test) is explicitly out of scope for this spec.

### Key Entities

- **Docker Compose Stack**: The local development infrastructure. Four services: `backend`
  (FastAPI on port 8000), `web` (Next.js on port 3000), `postgres` (on port 5432),
  `redis` (on port 6379). Managed via `make up` / `make down`.
- **`.env.example`**: A committed template file listing every required environment variable
  for a service, with placeholder values. Developers copy it to `.env` and fill in actual
  values. `.env` is gitignored.
- **CI Workflow**: The GitHub Actions pipeline that enforces quality gates on every PR.
  Four jobs, real PostgreSQL for backend tests, caching for fast execution.
- **Makefile**: The developer's command interface to the repository. Abstracts Docker Compose
  commands, test runners, and linters behind simple named targets.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `make up` brings all four services to a healthy state in under 120 seconds
  on a machine with Docker installed but no local language runtimes.
- **SC-002**: After `make up`, `curl http://localhost:8000/api/v1/health` returns `200 OK`.
- **SC-003**: `make down` followed immediately by `make up` succeeds with no port conflicts
  or leftover container state.
- **SC-004**: A GitHub Actions CI run completes in under 5 minutes for a clean scaffold
  (zero tests, zero violations).
- **SC-005**: A deliberately introduced `ruff` violation causes the `backend-lint` CI job
  to fail and the PR to be blocked from merging.
- **SC-006**: `make test` from the repository root runs both backend and web test suites
  and exits with code 0 on the empty scaffold.
- **SC-007**: `detect-secrets scan` run against the repository returns zero findings.
- **SC-008**: All `.env.example` files are present with comments — a new developer can
  identify every required variable without reading source code.

---

## Assumptions

- Docker and Docker Compose v2 (`docker compose`) are the only prerequisites for local
  development. No local Python, Node.js, or Flutter installation is required to run
  the backend and web via Docker.
- GitHub Actions is the CI platform. No other CI platform (Jenkins, CircleCI, GitLab CI)
  is configured in this spec.
- The PostgreSQL version in Docker Compose MUST match the version used in production
  (PostgreSQL 15). Using different versions between local and CI/prod creates compatibility
  risks.
- Redis does not require authentication in local development. In production (Phase 9),
  Redis authentication is added.
- The `Makefile` uses GNU Make syntax. It is the only build orchestration tool — no
  `Taskfile`, `justfile`, or `npm scripts` at the root level.
- Hot reload for the backend (`uvicorn --reload`) and web (`next dev`) is enabled by
  default in the Docker Compose local configuration.
- The production Docker images (used in staging and production in Phase 9) are separate
  `Dockerfile` files optimised for size, distinct from the development images which
  prioritise hot reload convenience.
- `act` (local GitHub Actions runner) is documented in `CONTRIBUTING.md` as an optional
  tool for testing CI locally, but is not required.
