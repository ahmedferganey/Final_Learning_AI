# Migration Plan: MongoDB to PostgreSQL with SQLAlchemy and Alembic

## Goal

Move the application metadata store from MongoDB to PostgreSQL while keeping the existing FastAPI, file upload, chunk processing, and vector database behavior intact.

This migration targets only the application metadata currently stored in MongoDB:

- `projects`
- `assets`
- `chunks`

The vector database remains separate and should not be migrated as part of this plan.

## Current State

The app currently uses MongoDB through Motor and PyMongo:

- `src/main.py` creates `AsyncIOMotorClient`, stores `app.mongo_conn`, and exposes `app.db_client`.
- `src/helpers/config.py` defines `MONGODB_*` settings and builds a MongoDB URL.
- `src/models/ProjectModel.py` manages the `projects` collection.
- `src/models/AssetModel.py` manages the `assets` collection.
- `src/models/ChunkModel.py` manages the `chunks` collection.
- `src/models/db_schemes/` contains Pydantic schemas using Mongo `ObjectId`.
- `docker/docker-compose.yml` runs MongoDB locally.
- `README.md` documents MongoDB setup and MongoDB collections.

The project already includes:

- `SQLAlchemy==2.0.36`
- `alembic==1.14.0`

Required additions will likely include:

- `asyncpg` for async PostgreSQL access.
- `psycopg` or `psycopg2-binary` only if synchronous tooling/scripts need it.

## Target Architecture

Use PostgreSQL as the source of truth for app metadata:

- FastAPI creates one async SQLAlchemy engine on startup.
- Request handlers use async SQLAlchemy sessions through a shared session factory.
- Alembic owns schema creation and schema evolution.
- SQLAlchemy ORM models represent database tables.
- Existing Pydantic schemas remain API/data-transfer schemas, but should stop depending on `bson.ObjectId`.

Recommended runtime components:

- `sqlalchemy.ext.asyncio.create_async_engine`
- `sqlalchemy.ext.asyncio.async_sessionmaker`
- `sqlalchemy.ext.asyncio.AsyncSession`
- PostgreSQL driver: `asyncpg`
- Alembic migrations under `src/migrations/` or repo-level `migrations/`

## Proposed Relational Schema

### `projects`

| Column | Type | Constraints |
| --- | --- | --- |
| `id` | `UUID` | Primary key |
| `project_id` | `VARCHAR` | Not null, unique |
| `created_at` | `TIMESTAMPTZ` | Not null, default now |
| `updated_at` | `TIMESTAMPTZ` | Not null, default now |

Notes:

- Keep public `project_id` as the stable user-facing identifier.
- Use internal UUID primary keys instead of Mongo `ObjectId`.

### `assets`

| Column | Type | Constraints |
| --- | --- | --- |
| `id` | `UUID` | Primary key |
| `project_id` | `UUID` | Foreign key to `projects.id`, not null |
| `asset_name` | `VARCHAR` | Not null |
| `asset_type` | `VARCHAR` | Not null |
| `asset_size` | `INTEGER` | Nullable |
| `asset_pushed_at` | `TIMESTAMPTZ` | Not null |
| `asset_config` | `JSONB` | Not null, default `{}` |
| `created_at` | `TIMESTAMPTZ` | Not null, default now |
| `updated_at` | `TIMESTAMPTZ` | Not null, default now |

Indexes and constraints:

- Unique constraint on `(project_id, asset_name)`.
- Index on `project_id`.
- Optional index on `(project_id, asset_type)` if filtering by type becomes frequent.

### `chunks`

| Column | Type | Constraints |
| --- | --- | --- |
| `id` | `UUID` | Primary key |
| `chunk_text` | `TEXT` | Not null |
| `chunk_metadata` | `JSONB` | Not null, default `{}` |
| `chunk_order` | `INTEGER` | Not null |
| `project_id` | `UUID` | Foreign key to `projects.id`, not null |
| `asset_id` | `UUID` | Foreign key to `assets.id`, not null |
| `created_at` | `TIMESTAMPTZ` | Not null, default now |
| `updated_at` | `TIMESTAMPTZ` | Not null, default now |

Indexes and constraints:

- Index on `project_id`.
- Index on `asset_id`.
- Optional unique constraint on `(asset_id, chunk_order)` to prevent duplicated chunk positions per asset.

## Migration Phases

## Phase 1: Add PostgreSQL Runtime Foundation

1. Add PostgreSQL dependencies:
   - `asyncpg`
   - keep `SQLAlchemy` and `alembic`
2. Replace Mongo settings with PostgreSQL settings:
   - `POSTGRES_HOST`
   - `POSTGRES_PORT`
   - `POSTGRES_DB`
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `DATABASE_URL`
3. Add a helper method such as `get_database_url()` in `src/helpers/config.py`.
4. Add SQLAlchemy database module, for example:
   - `src/database/session.py`
   - `src/database/base.py`
5. Update app startup in `src/main.py`:
   - create async engine
   - create async session factory
   - expose session factory on `app`
   - verify connection with `SELECT 1`
6. Update app shutdown:
   - dispose SQLAlchemy engine
   - remove `app.mongo_conn.close()`

Implementation target:

```python
app.db_engine = create_async_engine(settings.get_database_url())
app.db_session_factory = async_sessionmaker(app.db_engine, expire_on_commit=False)
```

## Phase 2: Add SQLAlchemy ORM Models

Create ORM models for:

- `Project`
- `Asset`
- `DataChunk`

Recommended location:

- `src/models/orm/project.py`
- `src/models/orm/asset.py`
- `src/models/orm/chunk.py`
- `src/models/orm/__init__.py`

Keep names distinct from the current Pydantic schema names to avoid import confusion.

Recommended names:

- `ProjectORM`
- `AssetORM`
- `DataChunkORM`

Use:

- UUID primary keys.
- `JSONB` for `asset_config` and `chunk_metadata`.
- `relationship()` only where it improves clarity.
- Database-level unique constraints and indexes instead of Mongo collection indexes.

## Phase 3: Configure Alembic

1. Initialize Alembic if not already initialized:
   - `alembic init src/migrations`
2. Configure `alembic.ini` and `env.py`.
3. Import SQLAlchemy metadata in Alembic `env.py`.
4. Support async database URLs.
5. Create the initial migration:
   - `projects`
   - `assets`
   - `chunks`
   - indexes
   - constraints
6. Verify migration:
   - `alembic upgrade head`
   - `alembic downgrade -1`
   - `alembic upgrade head`

Alembic must be the only mechanism used to create or alter PostgreSQL tables. Do not create tables during FastAPI startup.

## Phase 4: Replace Mongo Data Access Layer

Replace the current Mongo implementation behind these files:

- `src/models/ProjectModel.py`
- `src/models/AssetModel.py`
- `src/models/ChunkModel.py`

Two acceptable approaches:

1. Keep the same class names and method names, but rewrite internals to use `AsyncSession`.
2. Create new repository classes and update routes/controllers to use them.

Recommended for lower risk:

- Keep the existing class names and public method names first.
- Change only their constructor dependencies and internals.
- Refactor names later after behavior is stable.

Required method mappings:

### `ProjectModel`

- `create_project()` becomes SQLAlchemy `session.add()` plus `flush()`/`commit()`.
- `get_project_or_create_one()` becomes a `SELECT` by `project_id`, then insert if missing.
- `get_project_by_project_id()` becomes a `SELECT` by `project_id`.
- `get_all_projects()` becomes `SELECT`, `COUNT`, `OFFSET`, and `LIMIT`.
- `get_project_object_id()` should become `get_project_db_id()` and return UUID.

### `AssetModel`

- `create_asset()` inserts an `AssetORM`.
- `get_all_project_assets()` selects `id` and `asset_name` by `project_id`.
- `get_project_asset_by_name()` selects `id` and `asset_name` by `project_id`, `asset_name`, and optional `asset_type`.

### `ChunkModel`

- `create_chunk()` inserts a single chunk row.
- `insert_many_chunks()` uses `session.add_all()` or bulk insert.
- `delete_chunks_by_project_id()` uses SQLAlchemy `delete()`.
- `get_chunk()` selects by UUID.
- `get_project_chunks()` selects by project UUID with pagination.

## Phase 5: Remove Mongo `ObjectId` from App Data Flow

The current app passes Mongo `ObjectId` values between projects, assets, and chunks. PostgreSQL should use UUIDs.

Update:

- `src/models/db_schemes/project.py`
- `src/models/db_schemes/asset.py`
- `src/models/db_schemes/data_chunk.py`
- route/controller code that imports or creates `bson.ObjectId`

Replace:

- `ObjectId` with `uuid.UUID`
- Mongo `_id` alias assumptions with explicit `id`
- `asset_project_id` with `project_id` or a clear compatibility alias
- `chunk_project_id` with `project_id`
- `chunk_asset_id` with `asset_id`

Compatibility option:

- During the first migration, keep old Pydantic field names if that avoids a large route rewrite.
- Internally convert them to ORM column names.
- Once tests pass, rename the app fields to match SQL terminology.

## Phase 6: Update FastAPI Wiring

Current code creates model instances from `request.app.db_client`. Replace this with database sessions.

Recommended dependency:

```python
async def get_db_session(request: Request) -> AsyncIterator[AsyncSession]:
    async with request.app.db_session_factory() as session:
        yield session
```

Then route code can either:

- inject the session with `Depends(get_db_session)`, or
- keep using `request.app.db_session_factory()` directly for a smaller first change.

Recommended long-term approach:

- Use FastAPI dependencies.
- Keep transaction boundaries explicit.
- Commit only after successful business operations.
- Roll back on exceptions.

## Phase 7: Update Local Development Environment

Replace MongoDB service with PostgreSQL in Docker:

- Update `docker/docker-compose.yml`.
- Update `docker/.env.example`.
- Update `src/.env.example`.

Example environment:

```env
DATABASE_URL=postgresql+asyncpg://mini_rag:mini_rag@localhost:5432/mini_rag
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mini_rag
POSTGRES_USER=mini_rag
POSTGRES_PASSWORD=mini_rag
```

Remove or deprecate:

- `MONGODB_URL`
- `MONGODB_DATABASE`
- `MONGODB_USERNAME`
- `MONGODB_PASSWORD`
- `MONGODB_HOST`
- `MONGODB_PORT`
- `MONGODB_AUTH_SOURCE`

## Phase 8: Data Migration

If existing MongoDB data must be preserved, write a one-time migration script.

Recommended location:

- `scripts/migrate_mongodb_to_postgres.py`

Migration flow:

1. Connect to MongoDB.
2. Connect to PostgreSQL through SQLAlchemy.
3. Read all `projects`.
4. Insert projects into PostgreSQL and store mapping:
   - old Mongo `_id` to new PostgreSQL UUID
5. Read all `assets`.
6. Convert `asset_project_id` using the project ID mapping.
7. Insert assets and store mapping:
   - old Mongo `_id` to new PostgreSQL UUID
8. Read all `chunks`.
9. Convert `chunk_project_id` and `chunk_asset_id` using mappings.
10. Insert chunks in batches.
11. Validate counts:
   - Mongo project count equals PostgreSQL project count.
   - Mongo asset count equals PostgreSQL asset count.
   - Mongo chunk count equals PostgreSQL chunk count.
12. Run a sample API flow against migrated data.

Important:

- Do not regenerate embeddings during this migration.
- If vector DB payloads store Mongo chunk IDs, update the vector payloads or maintain an ID mapping table.
- Confirm whether Qdrant payloads currently reference Mongo `_id` values before deleting MongoDB.

## Phase 9: Tests and Verification

Add or update tests for:

- Creating a project.
- Fetching an existing project.
- Uploading an asset.
- Enforcing unique asset names per project.
- Processing files into chunks.
- Deleting old chunks before reprocessing.
- Fetching paginated chunks.
- Running the RAG query flow after metadata is stored in PostgreSQL.

Manual verification flow:

1. Start PostgreSQL.
2. Run `alembic upgrade head`.
3. Start FastAPI.
4. Create or access a project.
5. Upload a file.
6. Process the file into chunks.
7. Verify rows exist in PostgreSQL.
8. Build/update the vector index.
9. Run a query against the project.

## Phase 10: Documentation Cleanup

Update:

- `README.md`
- `docker/.env.example`
- `src/.env.example`
- any architecture docs that mention MongoDB

Remove or revise:

- "MongoDB Collections" section.
- MongoDB setup instructions.
- MongoDB environment variable examples.
- MongoDB Docker service documentation.

Add:

- PostgreSQL setup instructions.
- Alembic migration commands.
- Database reset instructions for local development.
- Notes explaining that PostgreSQL stores metadata and Qdrant stores vectors.

## Cutover Strategy

Recommended cutover for this app:

1. Add PostgreSQL support behind the existing data-access method names.
2. Add Alembic schema.
3. Update local Docker and env files.
4. Run all API flows locally against PostgreSQL.
5. If needed, run one-time Mongo-to-Postgres data migration.
6. Remove Mongo imports and dependencies.
7. Update docs.

Avoid running MongoDB and PostgreSQL writes in parallel unless there is a production need for zero downtime. Dual-write logic adds complexity and is not necessary for a local learning app unless existing data must remain available during a staged rollout.

## Main Risks

- Mongo `ObjectId` values are currently part of the app's internal data flow.
- Vector DB payloads may contain Mongo IDs that need migration or compatibility handling.
- JSON fields need explicit PostgreSQL `JSONB` handling.
- Transaction boundaries must be clear so partial file processing does not leave inconsistent metadata.
- Existing route code may assume dictionaries returned by Mongo instead of ORM objects.

## Definition of Done

The migration is complete when:

- FastAPI starts without Motor, PyMongo, or MongoDB settings.
- PostgreSQL connection is created and disposed cleanly.
- Alembic can create the full schema from an empty database.
- Projects, assets, and chunks are persisted in PostgreSQL.
- Upload, process, index, and query flows work end to end.
- MongoDB Docker service and env vars are removed from active documentation.
- Tests or manual verification cover the full metadata flow.
