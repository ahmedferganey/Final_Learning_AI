# Minirag schema migrations (Alembic)

This package owns **PostgreSQL** schema migrations for the Minirag ORM models under `schemes/`:

- `schemes/project.py` — `projects`
- `schemes/asset.py` — `assets`
- `schemes/chunk.py` — `chunks`
- `schemes/vector_document.py` — `vector_documents` (PGVector-backed embeddings)

**Alembic** is the supported way to create or alter these tables. `migrations/env.py` imports `Base` and the ORM models so autogenerate and upgrades stay aligned with SQLAlchemy metadata.

## Layout

- **`alembic.ini`** — Alembic config for this module (also copied into the Docker image from `docker/minirag/alembic.ini`)
- **`migrations/env.py`** — async Alembic environment; resolves DB URL and loads env files
- **`migrations/versions/`** — revision scripts

## Database URL resolution (`migrations/env.py`)

1. **`DATABASE_URL`** if set (non-empty)  
2. Otherwise built from **`POSTGRES_USERNAME`** or **`POSTGRES_USER`**, **`POSTGRES_PASSWORD`**, **`POSTGRES_HOST`**, **`POSTGRES_PORT`** (default `5432`), and **`POSTGRES_MAIN_DATABASE`** or **`POSTGRES_DB`**

Environment files loaded (in order, without overriding already-set values from the first load):

- **`src/.env`**
- **Project root `.env`**

## Revision history (this repo)

| Revision | Purpose |
|----------|---------|
| `abc25a35ca49` | Initial schema: `projects`, `assets`, `chunks` |
| `7b7f0b2e9c2f` | Enable `vector` extension; create `vector_documents` for PGVector |
| `9c2f2a52d8a1` | Add `project_uuid` to `vector_documents` with FK to `projects` |

## Commands

Working directory for relative `-c alembic.ini`:

```bash
cd src/models/db_schemes/minirag
```

With a venv at repo root:

```bash
../../../../../.venv/bin/python -m alembic -c alembic.ini current
```

From repo root:

```bash
.venv/bin/python -m alembic -c src/models/db_schemes/minirag/alembic.ini upgrade head
```

### Common operations

```bash
# New migration after model edits
../../../../../.venv/bin/python -m alembic -c alembic.ini revision --autogenerate -m "describe change"

# Apply all pending
../../../../../.venv/bin/python -m alembic -c alembic.ini upgrade head

# Roll back one revision
../../../../../.venv/bin/python -m alembic -c alembic.ini downgrade -1

# History
../../../../../.venv/bin/python -m alembic -c alembic.ini history
```

## Quick verification

1. `upgrade head`  
2. `downgrade -1`  
3. `upgrade head`  

## Docker

The container **entrypoint** runs **`alembic upgrade head`** automatically before starting Uvicorn, using the same `alembic.ini` path under `/app`.
