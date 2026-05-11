# Minirag Schema Migrations (Alembic)

This directory owns PostgreSQL schema migrations for the Minirag ORM models:

- `schemes/project.py`
- `schemes/asset.py`
- `schemes/chunk.py`

Alembic is the only supported mechanism to create or alter these tables.

## Directory Layout

- `alembic.ini`: Alembic config for this module
- `migrations/env.py`: async Alembic environment wired to `Base.metadata`
- `migrations/versions/`: revision scripts

## Database URL Resolution

`migrations/env.py` resolves DB URL in this order:

1. `DATABASE_URL` (if set)
2. Build from `POSTGRES_*` vars:
   - `POSTGRES_USERNAME` or `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_HOST`
   - `POSTGRES_PORT` (default `5432`)
   - `POSTGRES_MAIN_DATABASE` or `POSTGRES_DB`

It loads env files from:

- `src/.env` (preferred for this app)
- project root `.env` (fallback)

## Run Commands

Run from:

```bash
cd src/models/db_schemes/minirag
```

Use the project venv Python (recommended):

```bash
../../../../../.venv/bin/python -m alembic -c alembic.ini current
```

Alternative from repo root:

```bash
.venv/bin/python -m alembic -c src/models/db_schemes/minirag/alembic.ini current
```

## Common Operations

Create a new migration from model changes:

```bash
../../../../../.venv/bin/python -m alembic -c alembic.ini revision --autogenerate -m "your message"
```

Apply latest migrations:

```bash
../../../../../.venv/bin/python -m alembic -c alembic.ini upgrade head
```

Rollback one migration:

```bash
../../../../../.venv/bin/python -m alembic -c alembic.ini downgrade -1
```

Show migration history:

```bash
../../../../../.venv/bin/python -m alembic -c alembic.ini history
```

## Verification Flow

For a migration sanity check:

1. `upgrade head`
2. `downgrade -1`
3. `upgrade head`

## Current Baseline Revision

- `abc25a35ca49_create_initial_minirag_schema.py`
- Creates `projects`, `assets`, `chunks` with indexes and constraints.
