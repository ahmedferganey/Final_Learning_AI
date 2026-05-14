# Plan: Celery Task Queue with Redis and RabbitMQ

This plan is aligned with the **current** Mini RAG codebase under `src/`: FastAPI routers, async SQLAlchemy (`asyncpg`), `ProcessController` / `NLPController`, `VectorStoreFactory`, and `LLMProviderFactory` as wired in `main.py`.

## 1. Problem definition

### Current limitation

- **Chunk processing** is fully inline in `routes/data.py` → `POST /api/v1/data/process/{project_id}`: resolves the project with `ProjectRepository`, loads file assets with `AssetRepository`, optionally deletes chunks (`ChunkRepository.delete_chunks_by_project_uuid` when `do_reset == 1`), then for each asset uses **`ProcessController`** (`get_file_content`, `process_file_content` with LangChain loaders + `RecursiveCharacterTextSplitter`) and **`ChunkRepository.insert_many_chunks`**. All of this holds a **request-scoped `AsyncSession`** until commit.
- **Vector index push** is inline in `routes/nlp.py` → `POST /api/v1/nlp/index/push/{project_id}`: paginated reads via **`ChunkRepository.get_project_chunks`** (`page_size` default **50**, `page_no` loop), each page passed to **`NLPController.index_into_vector_db`** (embeddings via `embedding_client`, writes via `vector_store`). Uses **`get_vector_store`** → `request.app.vector_store` (singleton from startup).
- **RAG** (`POST /api/v1/nlp/rag/{project_id}`) combines retrieval + **`generation_client`** + templates; reasonable to keep **synchronous** initially for interactive clients.
- Heavy work therefore shares **Uvicorn workers**, HTTP timeouts, and no built-in **task id / retry / progress** semantics.
- `src/requirements.txt` already contains **commented** Celery-related pins (`celery`, `redis`, `kombu`, `billiard`, `vine`, `flower`) intended for a later phase.

### Target state

- **Celery** workers run offloaded jobs using the same business rules as today’s routes.
- **RabbitMQ** as the primary **AMQP broker** for task messages.
- **Redis** as **`CELERY_RESULT_BACKEND`** (and optionally as broker in dev).
- FastAPI returns quickly with **`202 Accepted`** + **`task_id`** (and a small status API), while existing endpoints can remain for backward compatibility until deprecated.

---

## 2. Current implementation snapshot (`src`)

Use this as the **refactor boundary** when extracting “enqueue-only” routes.

| Area | Files / behavior relevant to Celery |
|------|-------------------------------------|
| Entry | `main.py`: `create_engine_and_session_factory`, `LLMProviderFactory`, `VectorStoreFactory(settings, db_session_factory).create()`, `await vector_store.connect()`, `TemplateParser` |
| Data API | `routes/data.py`, body schema `routes/schemes/data.py` → **`ProcessRequest`** (`file_id`, `chunk_size`, `overlap_size`, `do_reset`) |
| NLP API | `routes/nlp.py`, `routes/schemes/nlp.py` → **`PushRequest`** (`do_reset`); index push loop + **`NLPController`** |
| Sync CPU | `controllers/ProcessController.py` — disk paths via `ProjectController`, **sync** LangChain loaders / splitter (no `async` here) |
| NLP logic | `controllers/NLPController.py` — **`index_into_vector_db`**, `reset_vector_db_collection`, embedding batching, `VectorStoreInterface` |
| DB | `database/session.py` — **`AsyncEngine`** + **`async_sessionmaker[AsyncSession]`** only; `database/dependencies.py` — `get_db_session` yields `request.app.db_session_factory()` |
| Repositories | `repositories/minirag/project_repository.py`, `asset_repository.py`, **`chunk_repository.py`** (`get_project_chunks` **page_size=50**, `insert_many_chunks` batch **100**) |
| Vector DI | `stores/vectordb/dependencies.py` — returns **`request.app.vector_store`** (not per-request factory) |
| Vector creation | `stores/vectordb/VectorStoreFactory.py` — **`QDRANT`** vs **`PGVECTOR`** from settings |
| Settings | `helpers/config.py` — `Settings`, `get_database_url()`, LLM + vector keys |

**Important:** There is **no separate service layer** today; the **route handlers own orchestration**. Celery integration should introduce **`services/` or `tasks/` modules** that either call **extracted async functions** (preferred) or carefully duplicate the same sequence (avoid long-term drift).

---

## 3. Broker and Redis roles

| Component | Role in this plan |
|-----------|-------------------|
| **RabbitMQ** | Primary **broker** (`amqp://…`) for durable task delivery. |
| **Redis** | **`CELERY_RESULT_BACKEND`** for `AsyncResult` state; optional **broker** in dev (`redis://…`). |

**Modes:** (1) RabbitMQ + Redis results — default for “full” stack; (2) Redis broker + Redis results — minimal local dev.

---

## 4. Task inventory (mapped to current code)

| Celery task (suggested name) | Mirrors | Payload (conceptual) | Notes |
|------------------------------|---------|----------------------|--------|
| **`process_project_chunks`** | `routes/data.py` `process_endpoint` | `project_id` + `ProcessRequest` fields | After extraction: same repo calls + `ProcessController` loop; **`do_reset`** and multi-file **best-effort** semantics must match existing JSON responses / signals (`ResponseSignal`). |
| **`push_project_index`** | `routes/nlp.py` `index_project` | `project_id` + `PushRequest.do_reset` | Recreate **`NLPController`** inside worker with **`embedding_client`** + **`vector_store`** only (no need for `template_parser` on this path). Preserve **paged** `get_project_chunks` and **first-page-only** `do_reset` behavior (`do_reset` cleared after first successful batch in current loop). |
| **`delete_project_index`** (optional) | `NLPController.reset_vector_db_collection` | `project_id` | Expose later if you add a dedicated HTTP route; method already exists on controller. |
| **`rag_answer_async`** (optional, later) | `routes/nlp.py` `rag_answer` | `RagAnswerRequest` + `project_id` | Needs **`generation_client`**, **`embedding_client`**, **`vector_store`**, **`TemplateParser`**; large payloads in Redis results are a bad fit—return summary ids or store outcome in DB if added. |

**Recommended order:** **`push_project_index`** first (single dominant slow path: embeddings + vector I/O), then **`process_project_chunks`**.

---

## 5. Worker runtime: rebuilding what `main.py` provides

Celery workers **do not** have `Request` or `app.state`. Each task (or worker process init) should reconstruct:

1. **`Settings`** — same as FastAPI: `get_settings()` / `Settings()` from `src/.env` (Docker: `/app/.env` or env vars).
2. **`db_engine`, `db_session_factory`** — `create_engine_and_session_factory(settings.get_database_url())` from `database/session.py`.
3. **`embedding_client`** — `LLMProviderFactory(settings.model_dump()).create(settings.EMBEDDING_BACKEND)` + `set_embedding_model(...)`.
4. **`vector_store`** — `VectorStoreFactory(settings, db_session_factory).create()` then **`await vector_store.connect()`** (use **`asyncio.run()`** for worker lifecycle once per process if using async vector store, or a small async helper; see section 7).
5. **Index push only:** **`generation_client`** is not required for **`index_into_vector_db`** (only **`embedding_client`** + **`vector_store`**).

Avoid importing **`main:app`** inside task modules to prevent circular imports; factor shared “bootstrap” into e.g. `src/worker_bootstrap.py`.

---

## 6. Async SQLAlchemy + sync LangChain (Celery-specific)

- **Repositories** and **`NLPController.index_into_vector_db`** are **`async`**. **`ProcessController`** methods used today are **synchronous** (file I/O + LangChain).
- **Options:**
  1. **`asyncio.run()`** per task: open **`async_sessionmaker()`** session(s), run the same async repository/controller calls as routes. Simplest alignment with **one** codebase path; pay attention to **pool size** and **not** nesting `asyncio.run` inside running loops.
  2. **Dedicated sync SQLAlchemy + `psycopg2`** in workers: duplicate data access or maintain dual paths — higher cost, but traditional Celery style.

**Recommendation for this repo:** start with **(1)** and a **single session per task** (or per batch) with explicit `commit`/`rollback` mirroring `routes/data.py` and `routes/nlp.py`.

---

## 7. Refactor prerequisites (before or with Celery)

1. **`run_process_job(db_session, project_id, process_request)`** — async function containing the body of `process_endpoint` (or move to `services/data_processing.py`).
2. **`run_index_push_job(db_session, vector_store, embedding_client, project_id, do_reset)`** — async function containing the `while has_records` loop + `NLPController(...)` construction as in `index_project`.
3. Optional: **`run_index_push_job`** accepts pre-built **`NLPController`** to simplify testing.

Routes then either call these functions **or** `task.delay(...)` after validation.

---

## 8. Configuration design

### New / extended environment variables

```env
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
CELERY_RESULT_BACKEND=redis://redis:6379/0
CELERY_TASK_DEFAULT_QUEUE=minirag.default
CELERY_TASK_TIME_LIMIT=3600
CELERY_TASK_SOFT_TIME_LIMIT=3300
```

- Add fields to **`helpers/config.py`** `Settings` (or a dedicated module imported by both FastAPI and Celery).
- **Uncomment** and pin in `src/requirements.txt` when implementing: the existing commented lines (`celery`, `redis`, `kombu`, …). Add **`amqp`** / **`librabbitmq`** only if you choose non-default drivers (document when chosen).

### Docker

- Extend **`docker/docker-compose.yml`** with **`rabbitmq`**, **`redis`**, **`celery-worker`** (same image as `fastapi` / `docker/minirag/Dockerfile` with **overridden `CMD`** to `celery -A … worker`, or a second stage/target).
- Add **`docker/env/.env.example.celery`** (or extend **`.env.example.app`**) with `CELERY_*` URLs pointing at service hostnames (`rabbitmq`, `redis`).

---

## 9. Proposed `src` layout (implementation phase)

```text
src/
  celery_app.py              # Celery() instance; broker + result backend from Settings
  worker_bootstrap.py        # rebuild settings, session factory, embedding_client, vector_store
  tasks/
    __init__.py
    data_tasks.py            # process_project_chunks → run_process_job
    nlp_tasks.py             # push_project_index → run_index_push_job
```

- **`celery_app.py`:** `autodiscover_tasks(["tasks"])`, JSON serialization, sane `task_time_limit`, optional `task_acks_late` once idempotency is proven.
- **`tasks/*`:** call **`asyncio.run(worker_bootstrap.with_session(run_…))`** pattern (exact helper TBD in implementation).

---

## 10. API contract changes (conceptual)

- **`POST /api/v1/data/process/{project_id}/async`** (or query flag `?async=1`) — validate **`ProcessRequest`**, enqueue **`process_project_chunks`**, return **`202`** + **`task_id`** + **`signal`** placeholder if desired.
- **`POST /api/v1/nlp/index/push/{project_id}/async`** — same for **`PushRequest`**.
- **`GET /api/v1/jobs/{task_id}`** — new small router (e.g. `routes/jobs.py`) using **`celery.result.AsyncResult`**; map Celery states to JSON. **Do not** store full chunk lists in Redis; return **`SUCCESS`** + summary (`inserted_items_count`, `processed_files`, etc.) populated from task return value or from DB reads.

Keep existing **`POST …/process/{project_id}`** and **`POST …/index/push/{project_id}`** until clients migrate.

---

## 11. Reliability and operations

- **Retries:** wrap transient **`openai`** / **`cohere`** / vector / DB connection errors; watch **embedding rate limits**.
- **Idempotency:** today’s index loop sets **`do_reset = 0`** after the first page; a **retried** task mid-run could duplicate vectors unless **`do_reset`** semantics or **upsert** strategy are documented. Prefer **task_id → job row** in PostgreSQL for strict idempotency later.
- **Observability:** existing Prometheus path in **`utils/metrics.py`** applies to FastAPI only; workers need **structured logging** (and optionally a Celery metrics exporter).

---

## 12. Phases and tasks

Each phase ends when its tasks are done and manually verified (compose up, worker consumes, or API returns expected status). Task IDs are for tracking only.

**Implementation status (repo scan, 2026-05-14):** `Status` is **Done** when the deliverable exists in tree in an equivalent form; **Pending** when missing or not verified. Celery tasks live under **`src/tasks/`** (`worker_context.py`, `file_processing.py`, `process_workflow.py`, `data_indexing.py`, `maintenance.py`) with **`celery_app.conf.imports`** (not `autodiscover_tasks`); there is still **no** `celery-worker` Compose service, **no** `GET /api/v1/jobs/{task_id}`, and **no** shared **`services/run_*`** extraction from routes yet.

### Phase 0 — Infrastructure (broker, result backend, docs)

**Goal:** RabbitMQ and Redis run in Docker (or documented equivalents), reachable from the host and from future containers, without changing application behavior yet.

| Status | ID | Task |
|--------|-----|------|
| Done | **0.1** | Add **`rabbitmq`** service to `docker/docker-compose.yml` (image, volumes, `5672`, optional `15672` for management UI, healthcheck). |
| Done | **0.2** | Add **`redis`** service (persistence volume optional, port `6379`, healthcheck `redis-cli ping` or equivalent). |
| Done | **0.3** | Wire **`backend`** network so future `fastapi` / `celery-worker` resolve hostnames `rabbitmq` and `redis`. |
| Pending | **0.4** | Add **`docker/env/.env.example.celery`** (or extend `.env.example.app`) with `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`, and placeholders for RabbitMQ credentials if not embedded in URL. *(Runtime `docker/env/.env.rabbitmq` / `.env.redis` exist; no committed `CELERY_*` example template or `src/.env.example` Celery block yet.)* |
| Pending | **0.5** | Update **`docker/README.md`**: new services, ports, how to verify (`docker compose ps`, `curl` to Redis, RabbitMQ management URL if enabled). *(Compose includes RabbitMQ/Redis; README service table still omits them.)* |
| Done | **0.6** | Smoke test: `docker compose up -d rabbitmq redis` from `docker/`; confirm healthchecks green. *(Manual verification — not recorded in repo.)* |

---

### Phase 1 — Celery skeleton (no business tasks yet)

**Goal:** Workers start, consume from the broker, write results to Redis; FastAPI unchanged.

| Status | ID | Task |
|--------|-----|------|
| Done | **1.1** | Uncomment Celery-related packages in **`src/requirements.txt`** (`celery`, `redis`, `kombu`, `billiard`, `vine`; add `amqp` if required by chosen broker URL). |
| Pending | **1.2** | Extend **`helpers/config.py`** `Settings` with `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`, optional `CELERY_TASK_*` limits; document in **`src/.env.example`**. *(Settings fields exist; **`src/.env.example`** has no Celery section yet.)* |
| Done | **1.3** | Add **`src/celery_app.py`**: instantiate `Celery`, set broker and result backend from settings, `task_serializer`/`result_serializer` `json`, register task packages. *(Uses `conf.imports` for `tasks.*` modules.)* |
| Done | **1.4** | Add **`src/tasks/__init__.py`** and **`src/tasks/health.py`** (or `tasks/ping.py`) with a minimal **`ping`** task returning a small dict (e.g. `{"ok": true}`). *(Implemented as **`tasks/maintenance.py`** → `tasks.maintenance.ping`.)* |
| Done | **1.5** | Add **`src/worker_bootstrap.py`** stub (optional in this phase) or document CLI: run worker from **`src/`** so `.env` resolves: `celery -A celery_app worker --loglevel=INFO`. *(Bootstrap implemented as **`tasks/worker_context.py`** `worker_bundle()` per task; no top-level `worker_bootstrap.py` file.)* |
| Pending | **1.6** | Add **`celery-worker`** service to **`docker/docker-compose.yml`**: same build context/image as `fastapi`, **override `CMD`** to Celery worker; `env_file` includes `CELERY_*`; `depends_on` RabbitMQ + Redis healthy. |
| Pending | **1.7** | Verify: start stack, exec into worker host or use a one-off container to **`delay(ping)`** (or small script in `docs/` / dev tool); `AsyncResult` state reaches **`SUCCESS`** in Redis. |

---

### Phase 2 — Index push async path (first real domain task)

**Goal:** `POST /api/v1/nlp/index/push/{project_id}/async` (or equivalent) enqueues work; job status readable by id; sync `index/push` still works via shared runner.

| Status | ID | Task |
|--------|-----|------|
| Pending | **2.1** | Extract **`run_index_push_job`** from **`routes/nlp.py`** into **`services/index_push.py`** (or `jobs/index_push.py`): same logic as `index_project` (repositories, `while` loop, `NLPController`, `commit`/`rollback`). |
| Pending | **2.2** | Refactor **`routes/nlp.py`** `index_project` to call **`await run_index_push_job(...)`** only (no duplicated loop). |
| Done | **2.3** | Implement **`worker_bootstrap.py`**: build `Settings`, `db_session_factory`, `embedding_client`, `vector_store` (+ `connect` / lifecycle as decided in section 6). *(Delivered as **`tasks/worker_context.worker_bundle`** including `generation_client` + `TemplateParser` for shared NLP tasks.)* |
| Done | **2.4** | Add **`tasks/nlp_tasks.py`**: Celery task **`push_project_index`** that runs `asyncio.run(run_index_push_job_with_bootstrap(...))` (or worker-level async runner); task args: `project_id`, `do_reset` (JSON-serializable). *(Implemented as **`tasks/data_indexing.push_project_index_task`** / `tasks.data_indexing.push_project_index`.)* |
| Done | **2.5** | Define a **small task result schema** (e.g. `signal`, `inserted_items_count`, `project_id`) for Redis; avoid large payloads. |
| Pending | **2.6** | Add **`POST /api/v1/nlp/index/push/{project_id}/async`** in **`routes/nlp.py`** (or dedicated router): validate **`PushRequest`**, `apply_async`, return **`202`** + `task_id` + optional `status_path`. |
| Pending | **2.7** | Add **`routes/jobs.py`** + register in **`main.py`**: **`GET /api/v1/jobs/{task_id}`** mapping Celery states to JSON (`PENDING`, `STARTED`, `SUCCESS`, `FAILURE`) and surfacing task result meta on success. |
| Pending | **2.8** | Manual test: enqueue index push for a project with chunks; poll job until `SUCCESS`; compare **`inserted_items_count`** with sync path for a small fixture project. |

---

### Phase 3 — Data process async path (second domain task)

**Goal:** Long-running chunking + DB inserts can be queued; behavior matches current **`process_endpoint`** signals and edge cases.

| Status | ID | Task |
|--------|-----|------|
| Pending | **3.1** | Extract **`run_process_job`** from **`routes/data.py`** into **`services/data_processing.py`** (or equivalent): `ProjectRepository`, `AssetRepository`, `ChunkRepository`, `ProcessController`, same HTTP-equivalent outcomes. |
| Pending | **3.2** | Refactor **`routes/data.py`** `process_endpoint` to **`await run_process_job(...)`** only. |
| Done | **3.3** | Add **`tasks/data_tasks.py`**: Celery task **`process_project_chunks`** with args derived from **`ProcessRequest`** + `project_id`. *(Implemented as **`tasks/process_workflow.process_project_task`** / `tasks.process_workflow.process_project`.)* |
| Done | **3.4** | Reuse **`worker_bootstrap`** for DB session; processing needs **no** `vector_store` / `embedding_client` unless you add side effects—keep bootstrap minimal or split “data worker” vs “nlp worker” queues later. *(**`worker_bundle`** is reused; it currently builds full NLP stack per task—not minimal.)* |
| Pending | **3.5** | Add **`POST /api/v1/data/process/{project_id}/async`**: validate body, enqueue, return **`202`** + `task_id`. |
| Pending | **3.6** | Extend **`GET /api/v1/jobs/{task_id}`** (or task result serializer) to return **process-specific** summary: `inserted_chunks`, `processed_files`, `failed_files` lists **bounded** in size or truncated in result. |
| Pending | **3.7** | Manual test: upload → process async → job `SUCCESS`; verify chunks in DB; verify `do_reset`, missing `file_id`, and all-failed paths match existing **`ResponseSignal`** behavior (document any intentional differences). |

---

### Phase 4 — Hardening, observability, optional ops tooling

**Goal:** Production-minded defaults without changing core contracts.

| Status | ID | Task |
|--------|-----|------|
| Pending | **4.1** | Configure **`task_time_limit`** / **`task_soft_time_limit`** per task type (index vs process) in `celery_app` or `@task` decorators. *(Global `CELERY_TASK_TIME_LIMIT` only; no `task_soft_time_limit`.)* |
| Pending | **4.2** | Add **`autoretry_for`** / backoff for transient embedding / HTTP / broker errors; cap max retries; log final failure with `task_id` and `project_id`. |
| Pending | **4.3** | Document **idempotency** limits (section 11): mid-task retry and `do_reset` behavior; optional follow-up task **4.x** for a **`celery_jobs`** DB table keyed by `task_id`. |
| Pending | **4.4** | Worker logging: structured logs (task name, `project_id`, duration); ensure no secrets in log lines. |
| Pending | **4.5** | Optional: uncomment **`flower`** in requirements and add **`flower`** compose service bound to localhost only in dev. |
| Pending | **4.6** | Optional: **`celery beat`** + periodic task (e.g. nightly noop or future “reindex stale projects”)—only if product requires it. |
| Pending | **4.7** | CI smoke job (optional): compose up minimal set + `celery call tasks.health.ping` (or equivalent) in pipeline. |

---

### Phase dependency overview

```text
Phase 0 (infra)
    → Phase 1 (Celery skeleton)
          → Phase 2 (index push async) — depends on 2.1 refactor
                → Phase 3 (process async) — can start after 2.3 bootstrap exists
                      → Phase 4 (hardening) — after at least one domain task is stable
```

**Parallelism:** After **1.7**, **2.1** (extract index job) can proceed in parallel with further Phase 0 doc polish; **3.1** should wait until **2.3** worker bootstrap pattern is proven to avoid two bootstrap designs.

---

## 13. Risks and mitigations

| Risk | Mitigation |
|------|------------|
| **Vector store connection** per worker process | Initialize once in **`worker_ready`** / process bootstrap; **`disconnect()`** on worker shutdown. |
| **`PGVECTOR`** path uses **`db_session_factory`** inside provider | Same factory as API; avoid creating multiple unbounded engines per task. |
| **Large Celery results** | Return **counts and signals** only; client loads final state from existing GET endpoints if needed. |
| **Drift** between route and task | Single **`run_*`** function per workflow. |

---

## 14. Out of scope (this plan document)

- Changing **`VectorDBEnums`** or LLM providers.  
- Replacing **`ResponseSignal`** JSON contracts.  
- Flower / Beat details beyond mentioning existing commented deps.

---

This document is the **Celery integration plan**; **Section 12** tracks what is implemented in the repo versus what remains.
