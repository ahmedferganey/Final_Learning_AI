# Mini RAG App

Minimal FastAPI service for:

- uploading `.txt` and `.pdf` files into project-scoped storage
- registering uploaded files as MongoDB assets
- processing one file or all project files into text chunks
- storing project, asset, and chunk metadata in MongoDB
- indexing chunks into a local Qdrant vector store
- searching the vector index and answering questions via RAG (en/ar prompt templates)

## Current Architecture

The application is organized as a small layered backend:

- `routes/`: HTTP layer, request/response handling, orchestration of controllers and models
- `controllers/`: file-system and content-processing logic
- `models/`: MongoDB access layer plus Pydantic database schemas and enums
- `helpers/`: configuration and environment loading
- `stores/`: pluggable backends (LLM providers, vector DB providers, prompt templates)
- `assets/files/`: uploaded file storage on disk
- `docker/`: local MongoDB runtime

The runtime flow is:

1. FastAPI starts and builds a MongoDB client.
2. `POST /api/v1/data/upload/{project_id}` saves the file to disk and registers it in the `assets` collection.
3. `POST /api/v1/data/process/{project_id}` resolves the target files from MongoDB assets.
4. Each file is loaded from disk, split into chunks with LangChain, and inserted into the `chunks` collection.
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
    ├── main.py
    ├── models
    │   ├── AssetModel.py
    │   ├── BaseDataModel.py
    │   ├── ChunkModel.py
    │   ├── ProjectModel.py
    │   ├── __init__.py
    │   ├── db_schemes
    │   │   ├── __init__.py
    │   │   ├── asset.py
    │   │   ├── data_chunk.py
    │   │   └── project.py
    │   └── enums
    │       ├── AssetTypeEnum.py
    │       ├── DataBaseEnum.py
    │       ├── ProcessingEnum.py
    │       ├── ResponseEnums.py
    │       └── __init__.py
    ├── requirements.txt
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

- `src/models/BaseDataModel.py`
  - common DB model base and shared settings access

- `src/models/ProjectModel.py`
  - CRUD-like access for project records
  - project collection index setup
  - project ObjectId resolution

- `src/models/AssetModel.py`
  - asset collection index setup
  - uploaded asset persistence
  - project asset lookup by id/name mapping

- `src/models/ChunkModel.py`
  - chunk collection index setup
  - bulk chunk insertion
  - project chunk cleanup

### Database Schemas

- `src/models/db_schemes/project.py`
  - schema for `projects`

- `src/models/db_schemes/asset.py`
  - schema for `assets`

- `src/models/db_schemes/data_chunk.py`
  - schema for `chunks`
  - RAG schema: `RetrievedDocument` (vector search hit normalized to `id`, `score`, `text`, `metadata`)

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
  - Mongo collection names

- `src/models/enums/ProcessingEnum.py`
  - supported file extensions for processing

- `src/models/enums/ResponseEnums.py`
  - API response signals

- `src/models/enums/AssetTypeEnum.py`
  - asset type values stored in MongoDB

### Data and Tooling

- `src/assets/files/`
  - physical uploaded file storage

- `src/assets/database/`
  - local on-disk databases used by the app (currently Qdrant `VECTOR_DB_PATH`)

- `src/assets/mini-rag-app.postman_collection.json`
  - starter Postman collection

- `docker/docker-compose.yml`
  - local MongoDB service definition with authentication

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

Uploads a file to disk and creates an asset record in MongoDB.

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

`file_id` is the stored disk filename and is also the asset name in MongoDB.

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
  - if provided, the API first looks up that file in MongoDB assets for the project
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

Indexes all project chunks from MongoDB into the vector DB collection for this project.

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

## MongoDB Collections

### `projects`

- `_id`
- `project_id`

### `assets`

- `_id`
- `asset_project_id`
- `asset_name`
- `asset_type`
- `asset_size`
- `asset_pushed_at`
- `asset_config`

### `chunks`

- `_id`
- `chunk_text`
- `chunk_metadata`
- `chunk_order`
- `chunk_project_id`
- `chunk_asset_id`

## Supported File Types

Current processing support:

- `.txt` via `TextLoader`
- `.pdf` via `PyMuPDFLoader`

## Important Notes

- `project_id` must be alphanumeric.
- Uploaded files are stored under `src/assets/files/<project_id>/`.
- Asset metadata is stored in MongoDB and is used by the process endpoint.
- The provided Postman collection is still minimal and may need manual extension for the current upload/process flow.
- RAG prompt templates live under `src/stores/llm/templates/locales/<lang>/rag.py` (currently `en` and `ar`).
