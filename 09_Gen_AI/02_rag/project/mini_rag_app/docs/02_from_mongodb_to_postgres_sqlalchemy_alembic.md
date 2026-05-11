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

Use the repository pattern for PostgreSQL instead of rewriting the old Mongo model classes in place.

The old classes can remain temporarily for reference during the transition, but routes/controllers should move to new SQLAlchemy repositories backed by `AsyncSession`.

Recommended repository location:

- `src/repositories/minirag/project_repository.py`
- `src/repositories/minirag/asset_repository.py`
- `src/repositories/minirag/chunk_repository.py`
- `src/repositories/minirag/__init__.py`

Recommended class names:

- `ProjectRepository`
- `AssetRepository`
- `ChunkRepository`

Task list:

- [x] P4-T001 Create `src/repositories/` package and `src/repositories/minirag/` package.
- [x] P4-T002 Implement `ProjectRepository` using `AsyncSession` and `ProjectORM`.
- [x] P4-T003 Implement `AssetRepository` using `AsyncSession` and `AssetORM`.
- [x] P4-T004 Implement `ChunkRepository` using `AsyncSession` and `DataChunkORM`.
- [x] P4-T005 Add repository exports in `src/repositories/minirag/__init__.py`.
- [x] P4-T006 Keep transaction control outside repositories unless a method needs an atomic local operation.
- [x] P4-T007 Return Pydantic app schemas or plain DTOs from repositories, not raw ORM objects, where route/controller code expects serializable objects.
- [x] P4-T008 Update `src/routes/data.py` to use repositories instead of `ProjectModel`, `AssetModel`, and `ChunkModel`.
- [x] P4-T009 Update `src/routes/nlp.py` to use repositories instead of `ProjectModel` and `ChunkModel`.
- [x] P4-T010 Remove route usage of `request.app.db_client`.
- [x] P4-T011 Verify no active route imports `src/models/ProjectModel.py`, `src/models/AssetModel.py`, or `src/models/ChunkModel.py`.

Required `ProjectRepository` methods:

- [x] P4-T012 `create_project(project_id: str)` inserts a `ProjectORM`.
- [x] P4-T013 `get_project_or_create(project_id: str)` selects by public `project_id`, inserts if missing, and returns the project.
- [x] P4-T014 `get_project_by_project_id(project_id: str)` selects by public `project_id`.
- [x] P4-T015 `get_all_projects(page: int, page_size: int)` uses `COUNT`, `OFFSET`, and `LIMIT`.
- [x] P4-T016 `get_project_uuid(project_id: str)` returns internal `projects.id` UUID.

Required `AssetRepository` methods:

- [x] P4-T017 `create_asset(...)` inserts an `AssetORM`.
- [x] P4-T018 `get_all_project_assets(project_uuid, asset_type=None)` returns `{asset_uuid: asset_name}`.
- [x] P4-T019 `get_project_asset_by_name(project_uuid, asset_name, asset_type=None)` returns `{asset_uuid: asset_name}`.

Required `ChunkRepository` methods:

- [x] P4-T020 `create_chunk(...)` inserts a single `DataChunkORM`.
- [x] P4-T021 `insert_many_chunks(chunks, batch_size=100)` inserts chunks in batches.
- [x] P4-T022 `delete_chunks_by_project_uuid(project_uuid)` deletes chunks for a project UUID.
- [x] P4-T023 `get_chunk(chunk_uuid)` selects one chunk by UUID.
- [x] P4-T024 `get_project_chunks(project_uuid, page_no=1, page_size=50)` selects project chunks with pagination.

Compatibility rules for this phase:

- [x] P4-T025 Keep public API payloads stable where possible.
- [x] P4-T026 Keep vector DB payload shape stable unless Phase 8 proves Mongo IDs are embedded there.
- [x] P4-T027 Do not delete old Mongo model files until routes no longer use them and tests/manual flows pass.

## Phase 5: Remove Mongo `ObjectId` from App Data Flow

The current app passes Mongo `ObjectId` values between projects, assets, and chunks. PostgreSQL should use UUIDs.

Task list:

- [x] P5-T001 Update `src/models/db_schemes/project.py` to use `uuid.UUID` instead of `bson.ObjectId`.
- [x] P5-T002 Update `src/models/db_schemes/asset.py` to use `uuid.UUID` instead of `bson.ObjectId`.
- [x] P5-T003 Update `src/models/db_schemes/data_chunk.py` to use `uuid.UUID` instead of `bson.ObjectId`.
- [x] P5-T004 Keep `RetrievedDocument` unchanged because it is a vector-search response schema, not a PostgreSQL table schema.
- [x] P5-T005 Replace Mongo `_id` alias assumptions with explicit `id` fields.
- [x] P5-T006 Rename app data fields where route/controller changes allow it:
  - `asset_project_id` -> `project_uuid`
  - `chunk_project_id` -> `project_uuid`
  - `chunk_asset_id` -> `asset_uuid`
- [x] P5-T007 Remove all imports of `bson`, `bson.objectid`, and `pymongo` from active app code.
- [x] P5-T008 Update logging text that says "MongoDB object id" to "project UUID" or "database UUID".
- [x] P5-T009 Run `rg -n "ObjectId|bson|pymongo|_id|MongoDB object id" src` and resolve active references.
- [x] P5-T010 Keep compatibility conversion only inside repositories if a route still passes an old field name during transition.

## Phase 6: Update FastAPI Wiring

Current code creates model instances from `request.app.db_client`. Replace this with database sessions.

Task list:

- [x] P6-T001 Add a FastAPI DB dependency, recommended location `src/database/dependencies.py`.
- [x] P6-T002 Implement `get_db_session(request: Request) -> AsyncIterator[AsyncSession]`.
- [x] P6-T003 Ensure the dependency opens one `AsyncSession` per request.
- [x] P6-T004 Add rollback handling for exceptions inside the dependency.
- [x] P6-T005 Update data routes to inject `AsyncSession` with `Depends(get_db_session)`.
- [x] P6-T006 Update NLP routes to inject `AsyncSession` with `Depends(get_db_session)`.
- [x] P6-T007 Instantiate repositories with the injected session.
- [x] P6-T008 Commit only after successful business operations.
- [x] P6-T009 Roll back on failed upload/process/index operations that changed PostgreSQL state.
- [x] P6-T010 Keep FastAPI startup free of `Base.metadata.create_all()` or any direct table creation.

Recommended dependency shape:

```python
async def get_db_session(request: Request) -> AsyncIterator[AsyncSession]:
    async with request.app.db_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
```

## Phase 7: Update Local Development Environment

PostgreSQL is now the local metadata database.

Task list:

- [x] P7-T001 Verify `docker/docker-compose.yml` runs PostgreSQL and does not require MongoDB for app metadata.
- [x] P7-T002 Verify `docker/.env.example` contains PostgreSQL variables only for metadata DB setup.
- [x] P7-T003 Verify `src/.env.example` contains `DATABASE_URL` or `POSTGRES_*` variables.
- [x] P7-T004 Remove active MongoDB environment examples from app docs.
- [x] P7-T005 Keep Qdrant/vector DB settings separate from PostgreSQL settings.
- [x] P7-T006 Add a local setup command sequence:
  - start PostgreSQL
  - install dependencies
  - run Alembic migrations
  - start FastAPI
- [x] P7-T007 Document how to reset local metadata DB safely using Alembic downgrade/upgrade or container volume reset.

Example app environment:

```env
DATABASE_URL=postgresql+asyncpg://mini_rag:mini_rag@localhost:5432/mini_rag
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mini_rag
POSTGRES_USER=mini_rag
POSTGRES_PASSWORD=mini_rag
```

## Phase 8: Data Migration "Optional"

If existing MongoDB data must be preserved, write a one-time migration script.

Task list:

- [ ] P8-T001 Decide whether existing MongoDB data must be preserved.
- [ ] P8-T002 If no data preservation is needed, document that this phase is skipped.
- [ ] P8-T003 If data preservation is needed, create `scripts/migrate_mongodb_to_postgres.py`.
- [ ] P8-T004 Connect to MongoDB read-only.
- [ ] P8-T005 Connect to PostgreSQL through SQLAlchemy async session or a controlled sync migration session.
- [ ] P8-T006 Read all Mongo `projects`.
- [ ] P8-T007 Insert PostgreSQL `projects` and store old Mongo `_id` -> new PostgreSQL UUID mapping.
- [ ] P8-T008 Read all Mongo `assets`.
- [ ] P8-T009 Convert `asset_project_id` using the project mapping.
- [ ] P8-T010 Insert PostgreSQL `assets` and store old Mongo `_id` -> new PostgreSQL UUID mapping.
- [ ] P8-T011 Read all Mongo `chunks`.
- [ ] P8-T012 Convert `chunk_project_id` and `chunk_asset_id` using mappings.
- [ ] P8-T013 Insert PostgreSQL `chunks` in batches.
- [ ] P8-T014 Validate Mongo and PostgreSQL counts for projects, assets, and chunks.
- [ ] P8-T015 Inspect Qdrant payloads to see whether Mongo `_id` values are stored.
- [ ] P8-T016 If Qdrant stores Mongo IDs, update vector payloads or keep an ID mapping strategy.
- [ ] P8-T017 Run one sample upload/process/index/query flow after migration.
- [ ] P8-T018 Do not regenerate embeddings unless vector payload migration proves impossible.

## Phase 9: Tests and Verification "Optional"

Task list:

- [ ] P9-T001 Add repository tests for `ProjectRepository`.
- [ ] P9-T002 Add repository tests for `AssetRepository`.
- [ ] P9-T003 Add repository tests for `ChunkRepository`.
- [ ] P9-T004 Test project creation and fetching an existing project.
- [ ] P9-T005 Test asset creation and unique asset name enforcement per project UUID.
- [ ] P9-T006 Test chunk batch insertion.
- [ ] P9-T007 Test chunk deletion by `project_uuid`.
- [ ] P9-T008 Test paginated chunk fetching.
- [x] P9-T009 Test upload endpoint creates project and asset rows in PostgreSQL.
- [x] P9-T010 Test process endpoint creates chunk rows in PostgreSQL.
- [x] P9-T011 Test index endpoint reads chunks from PostgreSQL and writes to vector DB.
- [x] P9-T012 Test RAG/search endpoint still returns `RetrievedDocument` payloads.
- [x] P9-T013 Run Alembic verification:
  - `alembic upgrade head`
  - `alembic downgrade -1`
  - `alembic upgrade head`
- [x] P9-T014 Run manual API flow:
  - start PostgreSQL
  - run migrations
  - start FastAPI
  - upload file
  - process file
  - verify rows
  - index vectors
  - query project

## Phase 10: Documentation Cleanup

Task list:

- [x] P10-T001 Update root `README.md` app overview from MongoDB metadata to PostgreSQL metadata.
- [x] P10-T002 Replace "MongoDB Collections" with "PostgreSQL Tables".
- [x] P10-T003 Document `projects`, `assets`, and `chunks` columns.
- [x] P10-T004 Document that `project_id` is the public string identifier and `id`/`*_uuid` fields are internal UUIDs.
- [x] P10-T005 Add Alembic command examples from `src/models/db_schemes/minirag/README.md`.
- [x] P10-T006 Remove MongoDB setup instructions from active local development docs.
- [x] P10-T007 Remove MongoDB environment variable examples.
- [x] P10-T008 Add PostgreSQL setup and reset instructions.
- [x] P10-T009 Document that PostgreSQL stores metadata and Qdrant stores vectors.
- [x] P10-T010 Update architecture docs/notebooks if they mention MongoDB as the app metadata store.
- [x] P10-T011 Update troubleshooting notes for common PostgreSQL/Alembic failures.
- [x] P10-T012 Run `rg -n "MongoDB|Mongo|MONGODB|ObjectId|pymongo|motor" README.md docs src docker` and revise stale docs or active code references.

## Cutover Strategy

Recommended cutover for this app:

1. Keep Phase 1-3 foundation in place: PostgreSQL connection, ORM schemas, and Alembic migrations.
2. Add new PostgreSQL repository classes under `src/repositories/minirag/`.
3. Update routes/controllers to use repositories and injected `AsyncSession`.
4. Remove active Mongo `ObjectId` usage from app data flow.
5. Run all API flows locally against PostgreSQL.
6. If needed, run one-time Mongo-to-Postgres data migration.
7. Remove old Mongo imports, dependencies, env vars, and inactive model classes after verification.
8. Update docs and examples.

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
