# Mini RAG App

A small **FastAPI** backend for learning and demos: upload project-scoped documents, chunk them with **LangChain**, persist metadata in **PostgreSQL**, index embeddings in **Qdrant** or **PGVector**, and answer questions with **RAG** using **OpenAI** or **Cohere** (with **English / Arabic** prompt templates). The app also exposes **Prometheus-friendly HTTP metrics** (custom path) and can be run locally or via the **Docker Compose** stack under `docker/`.

## What it does

- Accept **`.txt`** and **`.pdf`** uploads per `project_id`
- Register files as **assets** and split them into **chunks** in PostgreSQL (best-effort per file)
- **Push** chunks into a vector backend (`VECTOR_DB_BACKEND`: `QDRANT` or `PGVECTOR`)
- **Search** the index and call **RAG** (`/api/v1/nlp/rag/answer/{project_id}`) with optional debug payload and optional normalized `chat_history`

## Architecture (code)

Layers and responsibilities:

- **`routes/`** — HTTP routers (`base`, `data`, `nlp`) and Pydantic request bodies under `routes/schemes/`
- **`controllers/`** — validation, paths, LangChain loading/splitting, NLP orchestration (`NLPController`)
- **`repositories/minirag/`** — async SQLAlchemy access for projects, assets, chunks
- **`database/`** — async engine, sessions, FastAPI `get_db_session`
- **`models/`** — ORM tables under `models/db_schemes/minirag/schemes/`, shared enums, Alembic under `models/db_schemes/minirag/migrations/`
- **`stores/llm/`** — `LLMProviderFactory` (OpenAI / Cohere), locale templates
- **`stores/vectordb/`** — `VectorStoreFactory`, Qdrant and PGVector adapters
- **`helpers/config.py`** — `pydantic-settings` from `src/.env`
- **`utils/metrics.py`** — Prometheus counters/histograms and a non-schema metrics route

Runtime startup (`main.py`): load settings, connect PostgreSQL, build generation and embedding clients from config, create the configured vector store and `TemplateParser`, and register routers.

## Project layout (source)

```text
mini_rag_app/
├── README.md
├── .github/workflows/deploy-main.yml
├── docker/                    # full stack: app, nginx, pgvector, qdrant, monitoring
│   ├── README.md
│   ├── docker-compose.yml
│   ├── env/                   # per-service env files (see docker/README.md)
│   ├── minirag/Dockerfile
│   ├── minirag/entrypoint.sh  # runs Alembic then uvicorn
│   ├── nginx/default.conf
│   └── prometheus/prometheus.yml
└── src/
    ├── main.py
    ├── requirements.txt
    ├── .env.example
    ├── utils/metrics.py
    ├── helpers/config.py
    ├── database/
    ├── routes/  (+ routes/schemes/)
    ├── controllers/
    ├── repositories/minirag/
    ├── models/
    └── stores/
        ├── llm/
        └── vectordb/
```

More detail on Alembic for the `minirag` schema lives in `src/models/db_schemes/minirag/README.md`.

## Requirements

- **Python 3.10+** (Docker image uses 3.10)
- **Docker** and **Docker Compose** (for the bundled stack or for PostgreSQL only)
- On Debian/Ubuntu-style hosts, typical build deps for `asyncpg` / `psycopg2`:

```bash
sudo apt update
sudo apt install -y gcc python3-dev libpq-dev
```

## Configuration (`src/.env`)

Copy the example and adjust:

```bash
cp src/.env.example src/.env
```

`helpers.config.Settings` loads **`src/.env`** (run the app with working directory `src/` so relative paths resolve). You can set either:

- **`DATABASE_URL`** (async SQLAlchemy URL, e.g. `postgresql+asyncpg://...`), or  
- **`POSTGRES_*`** pieces: `POSTGRES_USERNAME` or `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`, and `POSTGRES_MAIN_DATABASE` or `POSTGRES_DB`

Important keys (non-exhaustive; see `src/.env.example`):

| Area | Variables |
|------|-----------|
| App | `APP_NAME`, `APP_VERSION` |
| Uploads | `FILE_ALLOWED_TYPES`, `FILE_MAX_SIZE` (MB), `FILE_DEFAULT_CHUNK_SIZE` (stream write size, bytes) |
| LLM | `GENERATION_BACKEND` / `EMBEDDING_BACKEND` (`OPENAI` or `COHERE`), API keys, `GENERATION_MODEL_ID`, `EMBEDDING_MODEL_ID`, `EMBEDDING_MODEL_SIZE`, defaults such as `INPUT_DAFAULT_MAX_CHARACTERS`, `GENERATION_DAFAULT_MAX_TOKENS`, `GENERATION_DAFAULT_TEMPERATURE` |
| Vector DB | `VECTOR_DB_BACKEND` (`QDRANT` or `PGVECTOR`), `VECTOR_DB_PATH`, `VECTOR_DB_DISTANCE_METHOD`, optional `PGVECTOR_*` |
| Templates | `DEFAULT_LANGUAGE` (e.g. `en`, `ar`) |

Leave **`OPENAI_API_URL`** empty unless you use a custom base URL; if set, it must include `http://` or `https://` (validated in the OpenAI provider).

## Database migrations (Alembic)

From the repo root (venv recommended):

```bash
.venv/bin/python -m alembic -c src/models/db_schemes/minirag/alembic.ini upgrade head
```

This creates/updates metadata tables (`projects`, `assets`, `chunks`) and, when migrations require it, **PGVector** support including `vector_documents`. Run migrations **before** starting the app if the database is empty.

**Docker:** the image entrypoint runs `alembic upgrade head` automatically before Uvicorn.

## Run the API locally

```bash
cd src
source ../.venv/bin/activate   # if using a venv
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

Base URL for versioned routes:

```text
http://127.0.0.1:5000/api/v1
```

Interactive docs: `http://127.0.0.1:5000/docs`

### Prometheus metrics (local)

The app registers a **hidden** metrics route (not listed in OpenAPI) used by the bundled Prometheus scrape config:

```text
GET http://127.0.0.1:5000/TrhBVe_m5gg2002_E5VVqS
```

Nginx in `docker/` proxies the same path to the app.

## Run with Docker (full stack)

See **`docker/README.md`** for services (FastAPI, Nginx, PostgreSQL/pgvector, Qdrant, Prometheus, Grafana, exporters), env files under **`docker/env/`**, and compose commands.

**PostgreSQL only** for local dev (from the `docker/` directory, after `docker/env/.env.postgres` exists):

```bash
docker compose up -d pgvector
```

Point `src/.env` at `localhost:5432` with matching DB name and credentials.

## CI / deploy

On push to **`main`**, `.github/workflows/deploy-main.yml` SSHs to the configured host, runs `git pull` under the server app path, and **`sudo systemctl restart minirag.service`**. The sample `docker/minirag.service` unit runs `docker compose up --build -d` from a server working directory that contains the compose file (adjust paths and secrets for your environment).

## API overview

### `GET /api/v1/`

Returns app name, version, and server UTC timestamp:

```json
{
  "app_name": "mini-RAG",
  "app_version": "0.1",
  "date": "2026-05-13T12:00:00.000000"
}
```

### `POST /api/v1/data/upload/{project_id}`

Multipart upload (`file` field). Persists the file under `src/assets/files/<project_id>/` and creates an **asset** row. Response includes `signal`, `file_id`, `project_id`.

### `POST /api/v1/data/process/{project_id}`

JSON body (`ProcessRequest`): optional `file_id`, `chunk_size`, `overlap_size`, `do_reset` (`1` clears existing chunks for the project first). Best-effort: failures per file appear in `failed_files`. Possible HTTP statuses include **404** when the file id is unknown or no file assets exist.

### `POST /api/v1/nlp/index/push/{project_id}`

Body: `{ "do_reset": 0|1 }`. Pages project chunks from the DB and indexes them into the active vector backend; `do_reset` applies to the first batch only.

### `GET /api/v1/nlp/index/info/{project_id}`

Returns collection metadata when the index exists.

### `POST /api/v1/nlp/index/search/{project_id}`

Body: `query_text`, optional `top_k` / `limit`. Returns `hits` as serialized retrieved documents.

### `POST /api/v1/nlp/rag/answer/{project_id}`

Body (`RagAnswerRequest`): `question`; optional `language`, `top_k`, `limit`, `temperature`, `max_output_tokens`, `system_message`, `debug`, `include_chat_history`.

Successful JSON shape:

- **`signal`**, **`answer`**
- **`fullpayload`**: object with (at least) `project_id`, `collection_name`, `hits`; plus **`chat_history`** when `include_chat_history` is true, and **`debug`** when `debug` is true (LLM payload from the controller).

Errors return appropriate status codes with `signal` and partial fields (see route handlers in `src/routes/nlp.py`).

## PostgreSQL tables (summary)

- **`projects`** — public `project_id` and UUID primary key  
- **`assets`** — files linked to a project  
- **`chunks`** — text and metadata per asset  
- **`vector_documents`** — used when **`VECTOR_DB_BACKEND=PGVECTOR`**

## Supported file types

- **`.txt`** — text loader  
- **`.pdf`** — PyMuPDF loader  

## Conventions and notes

- **`project_id`** in URLs is the public string identifier; foreign keys use UUIDs internally.
- **Vector backend:** Qdrant can use on-disk storage under `src/assets/database/` (path from config); PGVector stores vectors in PostgreSQL.
- **Postman:** `src/assets/mini-rag-app.postman_collection.json` is a starter; extend it as APIs evolve.

## Troubleshooting

- **Alembic / DB URL:** ensure `DATABASE_URL` or all required `POSTGRES_*` variables are set for both the app and Alembic (`migrations/env.py` loads `src/.env` then project root `.env`).
- **PGVector errors at startup:** run migrations so `vector_documents` (and extensions) exist when using `PGVECTOR`.
- **Docker:** credential mismatches between `docker/env/.env.app` and `docker/env/.env.postgres` cause connection failures; see `docker/README.md`.
