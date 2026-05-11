# Mini RAG App

Minimal FastAPI service for:

- uploading `.txt` and `.pdf` files into project-scoped storage
- registering uploaded files as PostgreSQL assets
- processing one file or all project files into text chunks
- storing project, asset, and chunk metadata in PostgreSQL
- indexing chunks into a local Qdrant vector store
- searching the vector index and answering questions via RAG (en/ar prompt templates)

## Current Architecture

The application is organized as a small layered backend:

- `routes/`: HTTP layer, request/response handling, orchestration of controllers and models
- `controllers/`: file-system and content-processing logic
- `models/`: SQLAlchemy ORM models, Alembic migrations, and Pydantic schemas
- `helpers/`: configuration and environment loading
- `stores/`: pluggable backends (LLM providers, vector DB providers, prompt templates)
- `assets/files/`: uploaded file storage on disk
- `docker/`: local PostgreSQL runtime

The runtime flow is:

1. FastAPI starts and builds a PostgreSQL async engine and session factory.
2. `POST /api/v1/data/upload/{project_id}` saves the file to disk and registers it in the `assets` table.
3. `POST /api/v1/data/process/{project_id}` resolves the target files from PostgreSQL assets.
4. Each file is loaded from disk, split into chunks with LangChain, and inserted into the `chunks` table.
5. Processing is best-effort: one bad file does not stop the others.
6. `POST /api/v1/nlp/index/push/{project_id}` indexes project chunks into Qdrant.
7. `POST /api/v1/nlp/rag/answer/{project_id}` retrieves top-k chunks and generates a grounded answer.

## Project Structure

Current tree:

```text
.
├── LICENSE
├── README.md
├── docker
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   └── docker-compose.yml
├── docs
│   ├── Arch.ipynb
│   └── Pdfs
└── src
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── assets
    │   ├── .gitignore
    │   ├── .gitkeep
    │   ├── database
    │   │   └── qdrant_db/
    │   ├── files
    │   │   └── <project_id>/
    │   └── mini-rag-app.postman_collection.json
    ├── controllers
    │   ├── BaseController.py
    │   ├── DataController.py
    │   ├── NLPController.py
    │   ├── ProcessController.py
    │   ├── ProjectController.py
    │   └── __init__.py
    ├── helpers
    │   ├── __init__.py
    │   └── config.py
    ├── database
    │   ├── __init__.py
    │   ├── base.py
    │   ├── dependencies.py
    │   └── session.py
    ├── main.py
    ├── models
    │   ├── __init__.py
    │   ├── db_schemes
    │   │   ├── __init__.py
    │   │   ├── asset.py
    │   │   ├── data_chunk.py
    │   │   ├── minirag
    │   │   │   ├── README.md
    │   │   │   ├── alembic.ini.example
    │   │   │   ├── migrations/
    │   │   │   └── schemes/
    │   │   └── project.py
    │   └── enums
    │       ├── AssetTypeEnum.py
    │       ├── DataBaseEnum.py
    │       ├── ProcessingEnum.py
    │       ├── ResponseEnums.py
    │       └── __init__.py
    ├── requirements.txt
    ├── repositories
    │   ├── __init__.py
    │   └── minirag
    │       ├── __init__.py
    │       ├── asset_repository.py
    │       ├── chunk_repository.py
    │       └── project_repository.py
    └── routes
        ├── __init__.py
        ├── base.py
        ├── data.py
        ├── nlp.py
        └── schemes
            ├── __init__.py
            ├── data.py
            └── nlp.py
    └── stores
        ├── llm
        │   ├── __init__.py
        │   ├── LlmEnums.py
        │   ├── LlmInterface.py
        │   ├── LLMProviderFactory.py
        │   ├── providers
        │   │   ├── __init__.py
        │   │   ├── CoHereProvider.py
        │   │   └── OpenAIProvider.py
        │   └── templates
        │       ├── __init__.py
        │       ├── template_parser.py
        │       └── locales
        │           ├── __init__.py
        │           ├── en
        │           │   ├── __init__.py
        │           │   └── rag.py
        │           └── ar
        │               ├── __init__.py
        │               └── rag.py
        └── vectordb
            ├── __init__.py
            ├── VectorDBEnums.py
            ├── VectorDBInterface.py
            ├── VectorDBProviderFactory.py
            └── providers
                ├── __init__.py
                └── QdrantDBProvider.py
```

Note: `__pycache__/` folders are omitted for brevity.

## File Responsibilities

### Runtime Entry

- `src/main.py`
  - FastAPI app creation
  - PostgreSQL connection startup and shutdown
  - router registration

### Configuration

- `src/helpers/config.py`
  - loads settings from `.env`
  - supports either a full `DATABASE_URL` or `POSTGRES_*` credential parts
  - builds PostgreSQL connection URL when needed
  - includes template localization default via `DEFAULT_LANGUAGE` (e.g. `en`, `ar`)

### Database Runtime

- `src/database/base.py`
  - SQLAlchemy declarative `Base`

- `src/database/session.py`
  - async engine/session-factory creation
  - lightweight DB connectivity check helper

- `src/database/dependencies.py`
  - FastAPI dependency that yields per-request `AsyncSession`

### API Layer

- `src/routes/base.py`
  - base health/info route under `/api/v1/`

- `src/routes/data.py`
  - upload endpoint
  - process endpoint
  - project lookup, asset lookup, best-effort processing orchestration

- `src/routes/nlp.py`
  - vector index endpoints (index push/info/search)
  - RAG answer endpoint (`/api/v1/nlp/rag/answer/{project_id}`)

- `src/routes/schemes/data.py`
  - request schema for processing payload

- `src/routes/schemes/nlp.py`
  - request schemas for NLP endpoints (`SearchRequest`, `RagAnswerRequest`, etc.)

### Controllers

- `src/controllers/BaseController.py`
  - common path setup and helper utilities

- `src/controllers/ProjectController.py`
  - resolves and creates project directory paths on disk

- `src/controllers/DataController.py`
  - file validation
  - filename sanitization
  - unique file path generation

- `src/controllers/ProcessController.py`
  - file loader selection by extension
  - disk existence checks
  - LangChain chunk generation

- `src/controllers/NLPController.py`
  - vector DB collection naming and indexing
  - vector search and RAG prompt construction
  - stores last LLM payload for debug (`last_llm_payload`)

### Persistence Layer

- `src/repositories/minirag/project_repository.py`
  - repository for project metadata operations
  - public `project_id` lookup and internal UUID resolution

- `src/repositories/minirag/asset_repository.py`
  - repository for asset persistence and project asset lookup

- `src/repositories/minirag/chunk_repository.py`
  - repository for chunk insert, query, and project chunk cleanup

### Database Schemas

- `src/models/db_schemes/project.py`
  - public API/data-transfer schema for `projects`

- `src/models/db_schemes/asset.py`
  - public API/data-transfer schema for `assets`

- `src/models/db_schemes/data_chunk.py`
  - public API/data-transfer schema for `chunks`
  - RAG schema: `RetrievedDocument` (vector search hit normalized to `id`, `score`, `text`, `metadata`)

- `src/models/db_schemes/minirag/schemes/project.py`
  - SQLAlchemy ORM table mapping for `projects`

- `src/models/db_schemes/minirag/schemes/asset.py`
  - SQLAlchemy ORM table mapping for `assets`

- `src/models/db_schemes/minirag/schemes/chunk.py`
  - SQLAlchemy ORM table mapping for `chunks`

- `src/models/db_schemes/minirag/migrations/`
  - Alembic migration scripts for PostgreSQL schema changes

### Stores (Backends)

- `src/stores/llm/`
  - LLM provider abstraction and implementations

- `src/stores/llm/providers/OpenAIProvider.py`
  - OpenAI chat + embeddings client
  - validates `OPENAI_API_URL` (must include `http(s)://` if set)

- `src/stores/llm/providers/CoHereProvider.py`
  - Cohere embeddings client

- `src/stores/llm/templates/template_parser.py`
  - loads locale templates from `src/stores/llm/templates/locales/<lang>/`

- `src/stores/llm/templates/locales/en/rag.py`
  - English RAG system/user/document/footer templates

- `src/stores/llm/templates/locales/ar/rag.py`
  - Arabic RAG system/user/document/footer templates

- `src/stores/vectordb/`
  - vector DB provider abstraction and implementations

- `src/stores/vectordb/providers/QdrantDBProvider.py`
  - Qdrant local vector store implementation (insert/search)
  - returns normalized `RetrievedDocument` objects on search

### Enums

- `src/models/enums/DataBaseEnum.py`
  - logical database entity names used by the app

- `src/models/enums/ProcessingEnum.py`
  - supported file extensions for processing

- `src/models/enums/ResponseEnums.py`
  - API response signals

- `src/models/enums/AssetTypeEnum.py`
  - asset type values stored in PostgreSQL

### Data and Tooling

- `src/assets/files/`
  - physical uploaded file storage

- `src/assets/database/`
  - local on-disk databases used by the app (currently Qdrant `VECTOR_DB_PATH`)

- `src/assets/mini-rag-app.postman_collection.json`
  - starter Postman collection

- `docker/docker-compose.yml`
  - local PostgreSQL (pgvector) service definition

- `docker/.env.example`
  - example Docker PostgreSQL credentials

## Requirements

- Python `3.10+`
- Docker and Docker Compose
- Linux packages for Python builds:

```bash
sudo apt update
sudo apt install -y gcc python3-dev libpq-dev
```

## Setup

### 1. Start PostgreSQL (pgvector image)

Create the Docker env file:

```bash
cp docker/.env.example docker/.env
```

Then update credentials in `docker/.env` if needed.

Start PostgreSQL from the repo root:

```bash
docker compose --env-file docker/.env -f docker/docker-compose.yml up -d
```

PostgreSQL is exposed on `localhost:5432`.

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r src/requirements.txt
```

### 4. Configure the FastAPI app

Create the app env file:

```bash
cp src/.env.example src/.env
```

Recommended PostgreSQL metadata configuration:

```env
APP_NAME="mini-RAG"
APP_VERSION="0.1"
OPENAI_API_KEY=""
OPENAI_API_URL=

FILE_ALLOWED_TYPES=["text/plain", "application/pdf"]
FILE_MAX_SIZE=10
FILE_DEFAULT_CHUNK_SIZE=512000

DATABASE_URL="postgresql+asyncpg://mini_rag:mini_rag@localhost:5432/mini_rag"
POSTGRES_HOST="localhost"
POSTGRES_PORT=5432
POSTGRES_DB="mini_rag"
POSTGRES_USER="mini_rag"
POSTGRES_PASSWORD="mini_rag"

# ============ LLM / Vector DB / Templates ===========
GENERATION_BACKEND="OPENAI"
EMBEDDING_BACKEND="COHERE"

GENERATION_MODEL_ID="gpt-4o-mini"
EMBEDDING_MODEL_ID="embed-multilingual-light-v3.0"
EMBEDDING_MODEL_SIZE=384

VECTOR_DB_BACKEND="QDRANT"
VECTOR_DB_PATH="qdrant_db"
VECTOR_DB_DISTANCE_METHOD="cosine"

DEFAULT_LANGUAGE="en"
```

Notes:

- `FILE_MAX_SIZE` is in MB.
- `FILE_DEFAULT_CHUNK_SIZE` is the streamed upload write size in bytes.
- The server reads `.env` from `src/`, so run commands from inside `src/`.
- Leave `OPENAI_API_URL` empty unless you are using a custom gateway/proxy. If set, it must include `http://` or `https://`.

### 5. Run Alembic migrations (metadata schema)

From repo root:

```bash
cd src/models/db_schemes/minirag
../../../../../.venv/bin/python -m alembic -c alembic.ini upgrade head
```

### 6. Start FastAPI

From `src/`:

```bash
cd src
source ../.venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

### Local DB reset (development)

Reset metadata schema with Alembic:

```bash
cd src/models/db_schemes/minirag
../../../../../.venv/bin/python -m alembic -c alembic.ini downgrade base
../../../../../.venv/bin/python -m alembic -c alembic.ini upgrade head
```

Or reset full PostgreSQL container volume:

```bash
docker compose --env-file docker/.env -f docker/docker-compose.yml down -v
docker compose --env-file docker/.env -f docker/docker-compose.yml up -d
```

## Run the API

From `src/`:

```bash
cd src
source ../.venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

Base URL:

```text
http://127.0.0.1:5000/api/v1
```

## API Endpoints

### `GET /api/v1/`

Returns application metadata.

Example response:

```json
{
  "app_name": "mini-RAG",
  "app_version": "0.1"
}
```

### `POST /api/v1/data/upload/{project_id}`

Uploads a file to disk and creates an asset record in PostgreSQL.

Request:

- path param: `project_id`
- body type: `form-data`
- file field name: `file`

Example:

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/data/upload/demo123" \
  -F "file=@/absolute/path/minirag.txt"
```

Success response:

```json
{
  "signal": "file_upload_success",
  "file_id": "abc123_minirag.txt",
  "project_id": "demo123"
}
```

`file_id` is the stored disk filename and is also the asset name in PostgreSQL.

### `POST /api/v1/data/process/{project_id}`

Processes uploaded project files into chunks.

Request body:

```json
{
  "file_id": "abc123_minirag.txt",
  "chunk_size": 100,
  "overlap_size": 20,
  "do_reset": 0
}
```

Fields:

- `file_id`
  - optional
  - if provided, the API first looks up that file in PostgreSQL assets for the project
  - if omitted, the API loads all file assets for the project
- `chunk_size`
  - chunk length used by `RecursiveCharacterTextSplitter`
- `overlap_size`
  - overlap between chunks
- `do_reset`
  - if `1`, all existing chunks for the project are deleted before inserting new ones

Best-effort behavior:

- if one file fails, the API continues with the remaining files
- the final response includes both `processed_files` and `failed_files`
- if all files fail, the endpoint returns `processing_failed`

Example with a single file:

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/data/process/demo123" \
  -H "Content-Type: application/json" \
  -d '{
    "file_id": "abc123_minirag.txt",
    "chunk_size": 100,
    "overlap_size": 20,
    "do_reset": 1
  }'
```

Example without `file_id`:

```bash
curl -X POST "http://127.0.0.1:5000/api/v1/data/process/demo123" \
  -H "Content-Type: application/json" \
  -d '{
    "chunk_size": 100,
    "overlap_size": 20,
    "do_reset": 1
  }'
```

Success response:

```json
{
  "signal": "processing_success",
  "inserted_chunks": 42,
  "processed_files": [
    "abc123_minirag.txt"
  ],
  "failed_files": [],
  "no_files": 1
}
```

All-failed response shape:

```json
{
  "signal": "processing_failed",
  "project_id": "demo123",
  "inserted_chunks": 0,
  "processed_files": [],
  "failed_files": [
    {
      "file_id": "missing.txt",
      "signal": "file_not_found"
    }
  ],
  "no_files": 0
}
```

### `POST /api/v1/nlp/index/push/{project_id}`

Indexes all project chunks from PostgreSQL into the vector DB collection for this project.

Request body:

```json
{ "do_reset": 1 }
```

Success response:

```json
{
  "signal": "insert_into_vectordb_sucess",
  "inserted_items_count": 123
}
```

### `GET /api/v1/nlp/index/info/{project_id}`

Returns vector DB collection info for the project (if exists).

### `POST /api/v1/nlp/index/search/{project_id}`

Searches the project vector DB index by a query string.

Request body:

```json
{ "query_text": "your query", "top_k": 5, "limit": 5 }
```

Success response includes `hits` (retrieved documents with `text` + `metadata` + `score`).

### `POST /api/v1/nlp/rag/answer/{project_id}`

Retrieves relevant chunks from the vector DB and generates an answer grounded in the retrieved context.

Request body:

```json
{
  "question": "What is this project about?",
  "language": "en",
  "top_k": 5,
  "limit": 5,
  "temperature": 0.1,
  "max_output_tokens": 300,
  "system_message": null,
  "debug": false
}
```

Response:

- `answer`: generated text
- `hits`: retrieved documents (`id`, `score`, `text`, `metadata`)
- if `debug=true`, returns a `debug` object that includes the exact messages/prompts sent to the LLM.

## PostgreSQL Tables

### `projects`

- `id` (UUID, primary key)
- `project_id`
- `created_at`
- `updated_at`

### `assets`

- `id` (UUID, primary key)
- `project_id` (UUID, FK -> `projects.id`)
- `asset_name`
- `asset_type`
- `asset_size`
- `asset_pushed_at`
- `asset_config`
- `created_at`
- `updated_at`

### `chunks`

- `id` (UUID, primary key)
- `chunk_text`
- `chunk_metadata`
- `chunk_order`
- `project_id` (UUID, FK -> `projects.id`)
- `asset_id` (UUID, FK -> `assets.id`)
- `created_at`
- `updated_at`

## Supported File Types

Current processing support:

- `.txt` via `TextLoader`
- `.pdf` via `PyMuPDFLoader`

## Important Notes

- `project_id` must be alphanumeric.
- `project_id` is the public string identifier used in API routes; internal table relationships use UUID primary keys.
- Uploaded files are stored under `src/assets/files/<project_id>/`.
- Asset/chunk/project metadata is stored in PostgreSQL; Qdrant stores only vector index data for retrieval.
- The provided Postman collection is still minimal and may need manual extension for the current upload/process flow.
- RAG prompt templates live under `src/stores/llm/templates/locales/<lang>/rag.py` (currently `en` and `ar`).

## Troubleshooting

- `alembic upgrade head` fails with connection/auth errors:
  - verify `DATABASE_URL` or `POSTGRES_*` values in `src/.env`.
  - ensure PostgreSQL is running: `docker compose --env-file docker/.env -f docker/docker-compose.yml ps`.
- `alembic` command not found:
  - run through project venv Python: `.venv/bin/python -m alembic -c src/models/db_schemes/minirag/alembic.ini current`.
- app fails on startup with DB connection errors:
  - run migrations before starting app, then restart `uvicorn`.
