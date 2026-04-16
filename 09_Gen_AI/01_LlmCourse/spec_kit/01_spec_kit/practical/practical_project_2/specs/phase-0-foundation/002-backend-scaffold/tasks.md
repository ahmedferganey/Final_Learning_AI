# Tasks: Backend Scaffold

**Input**: `specs/phase-0-foundation/002-backend-scaffold/`
**Spec**: [spec.md](spec.md)

> **For LLM agents**: All tasks produce Python source files under `backend/`. No business
> logic, authentication, or domain models are created. All module routers are empty
> placeholders. Required file content and exact configuration values are specified inline.
> Python 3.11+ syntax only (`X | Y` unions, no `Optional[X]`). Commit after each phase.

---

## Phase 1: Setup — Project Skeleton & Dependency Declaration

- [X] T001 Create the full `backend/` directory tree. Run from repo root:
  ```
  mkdir -p backend/app/core backend/app/db backend/app/shared
  mkdir -p backend/app/modules/auth backend/app/modules/users
  mkdir -p backend/app/modules/training backend/app/modules/coaching
  mkdir -p backend/app/modules/analytics backend/app/modules/nutrition
  mkdir -p backend/app/modules/notifications backend/app/modules/sync
  mkdir -p backend/tests/unit backend/tests/integration
  mkdir -p backend/alembic/versions
  touch backend/app/__init__.py backend/app/core/__init__.py
  touch backend/app/db/__init__.py backend/app/shared/__init__.py
  touch backend/app/modules/__init__.py
  touch backend/app/modules/auth/__init__.py backend/app/modules/users/__init__.py
  touch backend/app/modules/training/__init__.py backend/app/modules/coaching/__init__.py
  touch backend/app/modules/analytics/__init__.py backend/app/modules/nutrition/__init__.py
  touch backend/app/modules/notifications/__init__.py backend/app/modules/sync/__init__.py
  touch backend/tests/__init__.py backend/tests/unit/__init__.py
  touch backend/tests/integration/__init__.py
  ```

- [X] T002 Create `backend/pyproject.toml` with this exact content (FR-008):

  ```toml
  [build-system]
  requires = ["hatchling"]
  build-backend = "hatchling.build"

  [project]
  name = "gymos-backend"
  version = "0.1.0"
  requires-python = ">=3.11"
  dependencies = [
      "fastapi>=0.111.0",
      "uvicorn[standard]>=0.29.0",
      "pydantic>=2.7.0",
      "pydantic-settings>=2.2.0",
      "sqlalchemy[asyncio]>=2.0.30",
      "alembic>=1.13.0",
      "asyncpg>=0.29.0",
      "redis>=5.0.0",
  ]

  [project.optional-dependencies]
  dev = [
      "pytest==8.2.0",
      "pytest-asyncio==0.23.6",
      "pytest-cov==5.0.0",
      "httpx==0.27.0",
      "ruff==0.4.4",
      "mypy==1.10.0",
      "sqlalchemy[mypy]==2.0.30",
  ]

  [tool.ruff]
  target-version = "py311"
  line-length = 100
  select = ["E", "F", "I", "N", "UP", "S"]
  ignore = ["S101"]

  [tool.ruff.per-file-ignores]
  "tests/**" = ["S101"]

  [tool.mypy]
  python_version = "3.11"
  strict = true
  plugins = ["sqlalchemy.ext.mypy.plugin"]

  [tool.pytest.ini_options]
  asyncio_mode = "auto"
  testpaths = ["tests"]
  ```

- [X] T003 Create `backend/.env.example` (FR-002, SC-006). This file lists every required env variable with a placeholder and comment — never real values:

  ```
  # Application
  APP_ENV=development
  APP_VERSION=0.1.0
  PORT=8000

  # PostgreSQL — required, no default
  DATABASE_URL=postgresql+asyncpg://gymos:gymos@localhost:5432/gymos

  # Redis — required, no default
  REDIS_URL=redis://localhost:6379/0
  ```

**Checkpoint — Phase 1**: Verify `backend/pyproject.toml` exists and `pip install -e ".[dev]"` installs without error in a fresh venv.

---

## Phase 2: Foundational — Config, Database, Migrations

**Purpose**: These components are required by both the health endpoint (US1) and all module routers (US3). Complete before starting user story phases.

- [X] T004 Create `backend/app/core/config.py` (FR-002). This module uses `pydantic-settings` to load all config from environment variables. Missing required variables cause an immediate startup error:

  ```python
  from pydantic_settings import BaseSettings, SettingsConfigDict


  class Settings(BaseSettings):
      model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

      app_env: str
      app_version: str = "0.1.0"
      port: int = 8000

      database_url: str
      redis_url: str


  def get_settings() -> Settings:
      return Settings()
  ```

- [X] T005 Create `backend/app/db/base.py` with the SQLAlchemy declarative base, and `backend/app/db/session.py` with the async engine and session factory (FR-006):

  **`backend/app/db/base.py`**:
  ```python
  from sqlalchemy.orm import DeclarativeBase


  class Base(DeclarativeBase):
      pass
  ```

  **`backend/app/db/session.py`**:
  ```python
  from collections.abc import AsyncGenerator

  from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

  from app.core.config import get_settings

  _settings = get_settings()

  engine = create_async_engine(
      _settings.database_url,
      echo=_settings.app_env == "development",
      pool_pre_ping=True,
  )

  AsyncSessionFactory: async_sessionmaker[AsyncSession] = async_sessionmaker(
      engine,
      expire_on_commit=False,
  )


  async def get_db() -> AsyncGenerator[AsyncSession, None]:
      async with AsyncSessionFactory() as session:
          yield session
  ```

- [X] T006 Create `backend/alembic.ini` and `backend/alembic/env.py`. `alembic.ini` MUST NOT hardcode a database URL — it reads from the environment (FR-007, Edge Case):

  **`backend/alembic.ini`**:
  ```ini
  [alembic]
  script_location = alembic
  prepend_sys_path = .
  version_path_separator = os

  [loggers]
  keys = root,sqlalchemy,alembic

  [handlers]
  keys = console

  [formatters]
  keys = generic

  [logger_root]
  level = WARN
  handlers = console
  qualname =

  [logger_sqlalchemy]
  level = WARN
  handlers =
  qualname = sqlalchemy.engine

  [logger_alembic]
  level = INFO
  handlers =
  qualname = alembic

  [handler_console]
  class = StreamHandler
  args = (sys.stderr,)
  level = NOTSET
  formatter = generic

  [formatter_generic]
  format = %(levelname)-5.5s [%(name)s] %(message)s
  datefmt = %H:%M:%S
  ```

  **`backend/alembic/env.py`**:
  ```python
  import asyncio
  import os
  from logging.config import fileConfig

  from alembic import context
  from sqlalchemy.ext.asyncio import create_async_engine

  from app.db.base import Base

  config = context.config
  if config.config_file_name is not None:
      fileConfig(config.config_file_name)

  target_metadata = Base.metadata


  def get_url() -> str:
      url = os.environ.get("DATABASE_URL")
      if not url:
          raise RuntimeError("DATABASE_URL environment variable is not set")
      return url


  def run_migrations_offline() -> None:
      context.configure(
          url=get_url(),
          target_metadata=target_metadata,
          literal_binds=True,
          dialect_opts={"paramstyle": "named"},
      )
      with context.begin_transaction():
          context.run_migrations()


  async def run_async_migrations() -> None:
      connectable = create_async_engine(get_url())
      async with connectable.connect() as connection:
          await connection.run_sync(
              lambda conn: context.configure(
                  connection=conn, target_metadata=target_metadata
              )
          )
          async with connection.begin():
              await connection.run_sync(lambda _: context.run_migrations())
      await connectable.dispose()


  def run_migrations_online() -> None:
      asyncio.run(run_async_migrations())


  if context.is_offline_mode():
      run_migrations_offline()
  else:
      run_migrations_online()
  ```

- [X] T007 Create `backend/alembic/versions/0001_baseline.py` — a no-op baseline migration that establishes the migration history without creating any tables (FR-007):

  ```python
  """baseline

  Revision ID: 0001
  Revises:
  Create Date: 2026-04-09
  """

  revision: str = "0001"
  down_revision: str | None = None
  branch_labels: str | None = None
  depends_on: str | None = None


  def upgrade() -> None:
      pass  # Baseline migration — no tables defined yet


  def downgrade() -> None:
      pass
  ```

**Checkpoint — Phase 2**: Run `mypy app/` from `backend/` — must exit 0. Run `alembic upgrade head` with `DATABASE_URL` set — must exit 0.

---

## Phase 3: User Story 1 — Backend Starts and Reports Health (Priority: P1) 🎯 MVP

**Goal**: `uvicorn app.main:app` starts without errors, `GET /api/v1/health` returns 200 when DB is reachable, 503 when not.

**Independent test** (SC-001, SC-002): Start server, call health endpoint:
- Healthy: `curl http://localhost:8000/api/v1/health` → `{"status":"ok","version":"0.1.0"}`
- DB down: same call → `{"status":"degraded","checks":{"database":"unreachable","redis":"unreachable"}}`

- [X] T008 [P] [US1] Create `backend/app/core/dependencies.py` — FastAPI dependency providers (FR-006):

  ```python
  from collections.abc import AsyncGenerator
  from typing import Annotated

  from fastapi import Depends
  from sqlalchemy.ext.asyncio import AsyncSession

  from app.core.config import Settings, get_settings
  from app.db.session import get_db

  SettingsDep = Annotated[Settings, Depends(get_settings)]
  DbDep = Annotated[AsyncSession, Depends(get_db)]
  ```

- [X] T009 [US1] Create `backend/app/main.py` implementing the `create_app()` factory with health endpoint (FR-001, FR-003, FR-004):

  ```python
  from contextlib import asynccontextmanager
  from typing import Any

  from fastapi import FastAPI
  from fastapi.responses import JSONResponse
  from sqlalchemy import text

  from app.core.config import get_settings
  from app.db.session import engine


  @asynccontextmanager  # type: ignore[arg-type]
  async def lifespan(app: FastAPI) -> Any:
      yield
      await engine.dispose()


  def create_app() -> FastAPI:
      settings = get_settings()
      app = FastAPI(
          title="GymOS API",
          version=settings.app_version,
          lifespan=lifespan,
      )

      @app.get("/api/v1/health")
      async def health() -> JSONResponse:
          checks: dict[str, str] = {}

          # Check database
          try:
              async with engine.connect() as conn:
                  await conn.execute(text("SELECT 1"))
              checks["database"] = "ok"
          except Exception:
              checks["database"] = "unreachable"

          # Check Redis
          try:
              import redis.asyncio as aioredis
              r = aioredis.from_url(settings.redis_url, socket_connect_timeout=2)
              await r.ping()
              await r.aclose()
              checks["redis"] = "ok"
          except Exception:
              checks["redis"] = "unreachable"

          all_ok = all(v == "ok" for v in checks.values())
          status_code = 200 if all_ok else 503
          if all_ok:
              return JSONResponse(
                  status_code=200,
                  content={"status": "ok", "version": settings.app_version},
              )
          return JSONResponse(
              status_code=503,
              content={"status": "degraded", "checks": checks},
          )

      _register_routers(app)
      return app


  def _register_routers(app: FastAPI) -> None:
      pass  # Routers registered in Phase 5 (US3)


  app = create_app()
  ```

- [X] T010 [US1] Create `backend/tests/conftest.py` for the test suite baseline (FR-011):

  ```python
  import pytest
  from httpx import ASGITransport, AsyncClient

  from app.main import create_app


  @pytest.fixture
  async def client() -> AsyncClient:
      async with AsyncClient(
          transport=ASGITransport(app=create_app()),
          base_url="http://test",
      ) as ac:
          yield ac
  ```

**Checkpoint — US1**: `uvicorn app.main:app --reload` starts on port 8000. Health endpoint responds correctly.

---

## Phase 4: User Story 2 — Quality Checks With a Single Command (Priority: P2)

**Goal**: `make lint` and `make test` run from `backend/` and all exit 0 against the scaffold.

**Independent test** (SC-003): `ruff check .` exits 0; `mypy app/` exits 0; `pytest` exits 0 with 0 collected.

- [X] T011 [US2] Create `backend/Makefile` with lint and test targets (FR-009, FR-010, FR-011):

  ```makefile
  .PHONY: install lint test run

  # Install all dependencies including dev extras
  install:
  	pip install -e ".[dev]"

  # Run all linters and type checkers
  lint:
  	ruff check .
  	mypy app/

  # Run the test suite (exits 0 even with 0 tests collected)
  test:
  	pytest --tb=short -q

  # Start the development server
  run:
  	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```

**Checkpoint — US2**: From `backend/`, run `make lint` (exit 0) and `make test` (exit 0, "no tests ran" or "0 passed").

---

## Phase 5: User Story 3 — All Module Routers Registered (Priority: P3)

**Goal**: `GET /openapi.json` lists path prefixes for all 8 modules under `/api/v1/`.

**Independent test** (US3, FR-005): Start server, call `curl http://localhost:8000/openapi.json | python3 -m json.tool` and confirm `/api/v1/auth`, `/api/v1/users`, `/api/v1/training`, `/api/v1/coaching`, `/api/v1/analytics`, `/api/v1/nutrition`, `/api/v1/notifications`, `/api/v1/sync` all appear.

- [X] T012 [P] [US3] Create empty router stubs for all 8 modules. Create one file per module with this exact pattern (substitute module name and tag):

  **`backend/app/modules/auth/router.py`** (repeat for all 8 modules):
  ```python
  from fastapi import APIRouter

  router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

  # Endpoints for the auth module are implemented in Phase 1 (Spec 1.x)
  ```

  Create the same file for: `users` (prefix `/api/v1/users`, tag `users`), `training` (prefix `/api/v1/training`, tag `training`), `coaching` (prefix `/api/v1/coaching`, tag `coaching`), `analytics` (prefix `/api/v1/analytics`, tag `analytics`), `nutrition` (prefix `/api/v1/nutrition`, tag `nutrition`), `notifications` (prefix `/api/v1/notifications`, tag `notifications`), `sync` (prefix `/api/v1/sync`, tag `sync`).

- [X] T013 [US3] Update `backend/app/main.py` — replace the `_register_routers` stub with actual router imports and `app.include_router()` calls (FR-005):

  ```python
  def _register_routers(app: FastAPI) -> None:
      from app.modules.auth.router import router as auth_router
      from app.modules.users.router import router as users_router
      from app.modules.training.router import router as training_router
      from app.modules.coaching.router import router as coaching_router
      from app.modules.analytics.router import router as analytics_router
      from app.modules.nutrition.router import router as nutrition_router
      from app.modules.notifications.router import router as notifications_router
      from app.modules.sync.router import router as sync_router

      app.include_router(auth_router)
      app.include_router(users_router)
      app.include_router(training_router)
      app.include_router(coaching_router)
      app.include_router(analytics_router)
      app.include_router(nutrition_router)
      app.include_router(notifications_router)
      app.include_router(sync_router)
  ```

**Checkpoint — US3**: Start server, verify `/openapi.json` contains all 8 module prefixes.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T014 [P] Create `backend/README.md` with these sections: (1) **Prerequisites** — Python 3.11, PostgreSQL, Redis; (2) **Install** — `pip install -e ".[dev]"`; (3) **Environment** — copy `.env.example` to `.env` and fill values; (4) **Run** — `make run` or `uvicorn app.main:app --reload`; (5) **Quality checks** — `make lint` and `make test`; (6) **Migrations** — `alembic upgrade head`; (7) **Port conflict** — set `PORT` env variable to override 8000.

- [X] T015 Run `ruff check .` and `mypy app/` from `backend/` — fix any violations before marking done (SC-003).

- [X] T016 Run `pytest` from `backend/` — must exit 0 with "no tests ran" or "0 passed, 0 failed" (SC-003, FR-011).

---

## Dependencies & Execution Order

```
Phase 1 (T001–T003) — sequential, no dependencies
  └─► Phase 2 (T004–T007) — T004 before T005; T006 before T007; T005 parallel with T006
        └─► Phase 3 (T008–T010) — T008 parallel with T009; T010 after T009
        └─► Phase 4 (T011) — independent of Phase 3
        └─► Phase 5 (T012, T013) — T012 before T013
              └─► Phase 6 (T014–T016) — all after all stories complete
```

| Tasks | Order |
|---|---|
| T001, T002, T003 | T001 first, then T002 and T003 in parallel |
| T004, T005, T006, T007 | T004 → T005; T006 → T007; T005 and T006 in parallel |
| T008, T009 | Parallel (different files) |
| T010 | After T009 (needs create_app) |
| T011 | Parallel with Phase 3 (independent file) |
| T012 | Parallel for each of 8 files |
| T013 | After T012 |

---

## Parallel Execution Examples

### Phase 2 — Config and DB setup:
```
T004 → Write app/core/config.py
T006 → Write alembic.ini + alembic/env.py   (parallel with T004)
After both: T005 → Write app/db/session.py (needs T004)
After T006: T007 → Write baseline migration
```

### Phase 5 — 8 router files are fully independent:
```
Launch simultaneously:
  app/modules/auth/router.py
  app/modules/users/router.py
  app/modules/training/router.py
  app/modules/coaching/router.py
  app/modules/analytics/router.py
  app/modules/nutrition/router.py
  app/modules/notifications/router.py
  app/modules/sync/router.py
Then: update app/main.py to register them
```

---

## Implementation Strategy

### MVP (US1 only — health check working)
1. Phase 1: pyproject.toml, .env.example
2. Phase 2: config.py, db/session.py, alembic setup
3. Phase 3: main.py with health endpoint
4. Validate: server starts, health check responds

### Incremental Delivery
1. Phase 1–3 (US1) → Working backend, health check green
2. Phase 4 (US2) → Quality toolchain confirmed
3. Phase 5 (US3) → All 8 module routers registered
4. Phase 6 → Zero lint/type violations

---

## Notes for LLM Agents

- **Python 3.11+ syntax only** — use `X | Y` not `Optional[X]`, use `list[str]` not `List[str]`
- **No business logic** — all module routers are `# placeholder` stubs only (FR-012)
- **No hardcoded values** — all config comes from `Settings` class (FR-002)
- **Alembic must read DATABASE_URL from env** — not from `alembic.ini` sqlalchemy.url
- **Commit message**: `feat(infra): add backend FastAPI scaffold with health check and module routers`
