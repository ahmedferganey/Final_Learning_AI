# Tasks: Local Dev and CI Foundation

**Input**: `specs/phase-0-foundation/005-local-dev-and-ci-foundation/`
**Spec**: [spec.md](spec.md)

> **For LLM agents**: This spec delivers Docker Compose local stack, a root Makefile, and
> GitHub Actions CI. No application code changes. All secrets are references to environment
> variables or GitHub Secrets — never hardcoded values. Exact file content is specified inline.
> Commit after each phase. This spec REQUIRES Specs 0.2 (backend) and 0.3 (web) to be complete
> because their Dockerfiles are created here.

---

## Phase 1: Setup — Environment Files and Dockerfiles

- [ ] T001 [P] Create `backend/.env.example` (if not already created by Spec 0.2 — update if it exists) (FR-005). Every required variable must appear with a placeholder and inline comment:

  ```
  # Application
  APP_ENV=development
  APP_VERSION=0.1.0
  PORT=8000

  # PostgreSQL — required, no default
  DATABASE_URL=postgresql+asyncpg://gymos:gymos_password@postgres:5432/gymos

  # Redis — required, no default
  REDIS_URL=redis://redis:6379/0
  ```

  > Note: In Docker Compose context the DB host is `postgres` (service name), not `localhost`.

- [ ] T002 [P] Create `web/.env.example` (if not already created by Spec 0.3 — update if it exists) (FR-005):

  ```
  # Backend API URL — accessible from the browser (client-side)
  NEXT_PUBLIC_API_URL=http://localhost:8000
  ```

- [ ] T003 [P] Create root `.env.example` — the top-level template for Docker Compose (FR-005):

  ```
  # PostgreSQL
  POSTGRES_DB=gymos
  POSTGRES_USER=gymos
  POSTGRES_PASSWORD=gymos_password

  # Redis (no auth in local dev — see Spec 0.9 for production auth)
  REDIS_URL=redis://redis:6379/0

  # Service ports — override if defaults conflict with local services
  BACKEND_PORT=8000
  WEB_PORT=3000
  POSTGRES_PORT=5432
  REDIS_PORT=6379
  ```

  Also create a root `.env` file (gitignored) for actual local dev by copying `.env.example` — do NOT commit `.env`.

- [ ] T004 [P] Create `backend/Dockerfile` — development image with hot reload support (FR-004):

  ```dockerfile
  FROM python:3.11-slim

  WORKDIR /app

  # Install system dependencies
  RUN apt-get update && apt-get install -y --no-install-recommends \
      gcc \
      libpq-dev \
      && rm -rf /var/lib/apt/lists/*

  # Install Python dependencies
  COPY pyproject.toml .
  RUN pip install --no-cache-dir -e ".[dev]"

  # Source code is mounted as a volume — no COPY needed for hot reload
  EXPOSE 8000

  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
  ```

- [ ] T005 [P] Create `web/Dockerfile` — development image with hot reload support (FR-004):

  ```dockerfile
  FROM node:20-alpine

  WORKDIR /app

  # Install dependencies
  COPY package.json package-lock.json ./
  RUN npm ci

  # Source code is mounted as a volume — no COPY needed for hot reload
  EXPOSE 3000

  ENV NEXT_TELEMETRY_DISABLED=1
  ENV NODE_ENV=development

  CMD ["npm", "run", "dev"]
  ```

**Checkpoint — Phase 1**: `docker build -f backend/Dockerfile backend/` exits 0. `docker build -f web/Dockerfile web/` exits 0.

---

## Phase 2: Foundational — Docker Compose Stack

**Purpose**: The compose file must be complete before the Makefile can reference it.

- [ ] T006 Create `infra/compose/docker-compose.yml` defining all four services with healthchecks and volumes (FR-001, FR-002, FR-003, FR-004):

  ```yaml
  version: "3.9"

  services:
    postgres:
      image: postgres:15-alpine
      environment:
        POSTGRES_DB: ${POSTGRES_DB:-gymos}
        POSTGRES_USER: ${POSTGRES_USER:-gymos}
        POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-gymos_password}
      ports:
        - "${POSTGRES_PORT:-5432}:5432"
      volumes:
        - gymos_postgres_data:/var/lib/postgresql/data
      healthcheck:
        test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-gymos}"]
        interval: 5s
        timeout: 5s
        retries: 10
      networks:
        - gymos

    redis:
      image: redis:7-alpine
      ports:
        - "${REDIS_PORT:-6379}:6379"
      healthcheck:
        test: ["CMD", "redis-cli", "ping"]
        interval: 5s
        timeout: 3s
        retries: 10
      networks:
        - gymos

    backend:
      build:
        context: ../../backend
        dockerfile: Dockerfile
      ports:
        - "${BACKEND_PORT:-8000}:8000"
      environment:
        DATABASE_URL: postgresql+asyncpg://${POSTGRES_USER:-gymos}:${POSTGRES_PASSWORD:-gymos_password}@postgres:5432/${POSTGRES_DB:-gymos}
        REDIS_URL: redis://redis:6379/0
        APP_ENV: development
        APP_VERSION: 0.1.0
      volumes:
        # Hot reload — mount source directory (FR-004)
        - ../../backend/app:/app/app
      depends_on:
        postgres:
          condition: service_healthy
        redis:
          condition: service_healthy
      healthcheck:
        test: ["CMD-SHELL", "curl -f http://localhost:8000/api/v1/health || exit 1"]
        interval: 10s
        timeout: 5s
        retries: 10
        start_period: 30s
      networks:
        - gymos

    web:
      build:
        context: ../../web
        dockerfile: Dockerfile
      ports:
        - "${WEB_PORT:-3000}:3000"
      environment:
        NEXT_PUBLIC_API_URL: http://localhost:${BACKEND_PORT:-8000}
      volumes:
        # Hot reload — mount source directory (FR-004)
        - ../../web/src:/app/src
      depends_on:
        - backend
      networks:
        - gymos

  volumes:
    gymos_postgres_data:
      name: gymos_postgres_data  # FR-003: named volume for persistence

  networks:
    gymos:
      driver: bridge
  ```

**Checkpoint — Phase 2**: `docker compose -f infra/compose/docker-compose.yml config` exits 0 (config validation).

---

## Phase 3: User Story 1 — Full Local Stack in One Command (Priority: P1) 🎯 MVP

**Goal**: `make up` from repo root brings up all four services. `curl http://localhost:8000/api/v1/health` returns 200.

**Independent test** (SC-001, SC-002, SC-003): `make up` completes in ≤120s; health check returns 200; `make down` then `make up` works cleanly.

- [ ] T007 [US1] Create root `Makefile` with all required targets and inline comments (FR-006). Note: indentation MUST use tabs, not spaces:

  ```makefile
  .PHONY: up down test lint clean help

  COMPOSE := docker compose -f infra/compose/docker-compose.yml

  ## up: Start all services (backend, web, postgres, redis) via Docker Compose
  up:
  	$(COMPOSE) up --build -d
  	@echo "Services starting... checking backend health"
  	@$(COMPOSE) ps

  ## down: Stop and remove all containers (data volume is preserved)
  down:
  	$(COMPOSE) down

  ## test: Run backend and web test suites (backend first, then web)
  test:
  	@echo "=== Running backend tests ==="
  	cd backend && pytest --tb=short -q
  	@echo "=== Running web tests ==="
  	cd web && npm run test

  ## lint: Run all linters and type checkers for backend and web
  lint:
  	@echo "=== Backend: ruff ==="
  	cd backend && ruff check .
  	@echo "=== Backend: mypy ==="
  	cd backend && mypy app/
  	@echo "=== Web: eslint ==="
  	cd web && npm run lint
  	@echo "=== Web: tsc ==="
  	cd web && npx tsc --noEmit

  ## clean: Stop all containers AND remove the postgres data volume (destructive!)
  clean:
  	$(COMPOSE) down -v
  	@echo "Warning: gymos_postgres_data volume has been removed."

  ## help: Show this help message
  help:
  	@grep -E '^## ' Makefile | sed 's/^## //'
  ```

**Checkpoint — US1**: From repo root, run `make up`. Wait up to 120s. Run `curl http://localhost:8000/api/v1/health` → `{"status":"ok","version":"0.1.0"}`. Run `make down && make up` — must work cleanly.

---

## Phase 4: User Story 2 — CI Validates Backend and Web on Every PR (Priority: P2)

**Goal**: `.github/workflows/ci.yml` runs 4 jobs on every PR to `main`. Backend lint/test and web lint/test run in parallel. Real PostgreSQL used for backend tests.

**Independent test** (SC-005): Push a PR with a deliberate `ruff` violation → `backend-lint` job fails and blocks merge. Remove violation → all jobs green.

- [ ] T008 [US2] Create `.github/workflows/ci.yml` with 4 jobs (FR-007, FR-008, FR-009, FR-010, FR-011, FR-012, Edge Cases):

  ```yaml
  name: CI

  on:
    pull_request:
      branches: [main]
    push:
      branches: [main]

  jobs:
    # ─── Secret Scanning ─────────────────────────────────────────────────────
    secret-scan:
      name: Secret Scan
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Install detect-secrets
          run: pip install detect-secrets
        - name: Scan for secrets
          run: detect-secrets scan --baseline .secrets.baseline

    # ─── Backend Lint ─────────────────────────────────────────────────────────
    backend-lint:
      name: Backend Lint & Type Check
      runs-on: ubuntu-latest
      defaults:
        run:
          working-directory: backend
      steps:
        - uses: actions/checkout@v4

        - name: Set up Python 3.11
          uses: actions/setup-python@v5
          with:
            python-version: "3.11"

        - name: Cache pip dependencies
          uses: actions/cache@v4
          with:
            path: ~/.cache/pip
            key: ${{ runner.os }}-pip-${{ hashFiles('backend/pyproject.toml') }}
            restore-keys: |
              ${{ runner.os }}-pip-

        - name: Install dependencies
          run: pip install -e ".[dev]"

        - name: Ruff lint
          run: ruff check .

        - name: Mypy type check
          run: mypy app/

    # ─── Backend Tests ────────────────────────────────────────────────────────
    backend-test:
      name: Backend Tests
      runs-on: ubuntu-latest
      defaults:
        run:
          working-directory: backend
      services:
        postgres:
          image: postgres:15-alpine
          env:
            POSTGRES_DB: gymos_test
            POSTGRES_USER: gymos
            POSTGRES_PASSWORD: gymos_test_password
          ports:
            - 5432:5432
          options: >-
            --health-cmd pg_isready
            --health-interval 5s
            --health-timeout 5s
            --health-retries 10
      env:
        DATABASE_URL: postgresql+asyncpg://gymos:gymos_test_password@localhost:5432/gymos_test
        REDIS_URL: redis://localhost:6379/0
        APP_ENV: test
      steps:
        - uses: actions/checkout@v4

        - name: Set up Python 3.11
          uses: actions/setup-python@v5
          with:
            python-version: "3.11"

        - name: Cache pip dependencies
          uses: actions/cache@v4
          with:
            path: ~/.cache/pip
            key: ${{ runner.os }}-pip-${{ hashFiles('backend/pyproject.toml') }}
            restore-keys: |
              ${{ runner.os }}-pip-

        - name: Install dependencies
          run: pip install -e ".[dev]"

        - name: Run migrations
          run: alembic upgrade head

        - name: Run tests
          run: pytest --tb=short -q

    # ─── Web Lint ─────────────────────────────────────────────────────────────
    web-lint:
      name: Web Lint & Type Check
      runs-on: ubuntu-latest
      defaults:
        run:
          working-directory: web
      steps:
        - uses: actions/checkout@v4

        - name: Set up Node.js 20
          uses: actions/setup-node@v4
          with:
            node-version: "20"
            cache: "npm"
            cache-dependency-path: web/package-lock.json

        - name: Install dependencies
          run: npm ci

        - name: ESLint
          run: npm run lint

        - name: TypeScript
          run: npx tsc --noEmit
          env:
            NEXT_PUBLIC_API_URL: http://localhost:8000

    # ─── Web Tests ────────────────────────────────────────────────────────────
    web-test:
      name: Web Tests
      runs-on: ubuntu-latest
      defaults:
        run:
          working-directory: web
      steps:
        - uses: actions/checkout@v4

        - name: Set up Node.js 20
          uses: actions/setup-node@v4
          with:
            node-version: "20"
            cache: "npm"
            cache-dependency-path: web/package-lock.json

        - name: Install dependencies
          run: npm ci

        - name: Run tests
          run: npm run test
          env:
            NEXT_PUBLIC_API_URL: http://localhost:8000
  ```

**Checkpoint — US2**: Push a branch with a deliberate `ruff` violation to a PR → `backend-lint` job fails. Fix it → all jobs green. Verify the `backend-test` job connects to the real PostgreSQL service container (check logs for "running migrations").

---

## Phase 5: User Story 3 — Root Commands Run All Checks (Priority: P3)

**Goal**: `make test` and `make lint` from repo root execute both backend and web checks in sequence.

**Independent test** (SC-006): `make test` from root runs both `pytest` and `npm run test`. `make lint` runs both `ruff`+`mypy` and `npm run lint`+`tsc`.

- [ ] T009 [US3] Verify the root `Makefile` created in T007 satisfies US3 acceptance scenarios:
  - `make test` runs `cd backend && pytest ...` then `cd web && npm run test` — sequential, stops on failure
  - `make lint` runs all four checks: `ruff`, `mypy`, `eslint`, `tsc`
  - `make test` with backend failure exits non-zero without running web tests (Makefile default behavior with `&&` or sequential commands without `-` prefix)
  
  If any of these are not satisfied, update the `Makefile` accordingly. No new file is created — this is an audit-and-patch task.

**Checkpoint — US3**: `make test` from repo root runs both suites and exits 0 on the empty scaffold. Break `make test` intentionally (introduce `exit 1` in backend) — confirms it stops without running web tests.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T010 Run `detect-secrets scan --baseline .secrets.baseline` from repo root — exit 0, no findings (SC-007). If new files added by this spec introduced false positives, run `detect-secrets audit .secrets.baseline` to acknowledge them.

- [ ] T011 [P] Verify all `.env.example` files are present and complete (SC-008). Run `ls backend/.env.example web/.env.example .env.example` — all must exist. Open each and confirm every variable has a placeholder value and an inline comment. Add any missing variables.

- [ ] T012 [P] Verify `infra/compose/docker-compose.yml` does not contain any hardcoded secrets (FR-012). Open the file and check: no hardcoded passwords (use `${POSTGRES_PASSWORD}` not `hardcoded123`), no API keys, no tokens. All sensitive values must come from env variables.

- [ ] T013 [P] Verify `.github/workflows/ci.yml` does not contain any hardcoded secrets (FR-012). Check: no hardcoded `DATABASE_URL` with real credentials (test credentials in the `env:` block for the test job are acceptable as they're throwaway values). Any production secrets MUST use `${{ secrets.* }}`.

- [ ] T014 Run `make up` one final time and confirm all SC-001 through SC-003 pass: (1) all services healthy in ≤120s; (2) health check returns 200; (3) `make down && make up` works cleanly.

---

## Dependencies & Execution Order

```
Phase 1 (T001–T005) — all parallel after each other
  └─► Phase 2 (T006) — needs Dockerfiles from Phase 1
        └─► Phase 3 (T007) — needs docker-compose.yml from Phase 2
        └─► Phase 4 (T008) — independent of Phase 3 (CI file only)
        └─► Phase 5 (T009) — after Phase 3 (Makefile already exists)
              └─► Phase 6 (T010–T014) — after all phases
```

| Tasks | Order |
|---|---|
| T001, T002, T003, T004, T005 | All parallel |
| T006 | After T004 and T005 (needs Dockerfiles) |
| T007 | After T006 (Makefile references compose file) |
| T008 | Parallel with T007 (CI file is independent) |
| T009 | After T007 (audit of existing Makefile) |

---

## Notes for LLM Agents

- **Makefile indentation MUST be tabs** — spaces in Makefiles cause "missing separator" errors
- **No mobile CI** — Flutter CI is explicitly out of scope (FR-013); do NOT add a flutter job
- **PostgreSQL 15** — compose and CI both use `postgres:15-alpine` for consistency (Assumption)
- **No Redis auth in local/CI** — production Redis auth added in Phase 9 (Assumption)
- **`detect-secrets` in CI** — required by the spec; it references the committed `.secrets.baseline` file from Spec 0.1
- **Hot reload volumes** — `backend/app` mounted into the backend container; `web/src` into the web container (FR-004)
- **`gymos_postgres_data`** — named volume for persistence; `make clean` removes it (`down -v`); document the difference in README
- **Commit message**: `feat(infra): add Docker Compose local stack, Makefile, and GitHub Actions CI`
