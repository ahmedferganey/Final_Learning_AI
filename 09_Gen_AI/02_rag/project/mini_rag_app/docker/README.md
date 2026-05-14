# Docker setup (Mini RAG App)

This directory defines a **multi-service** stack for running the Mini RAG API together with databases and observability. Compose file: **`docker-compose.yml`** (run commands from **`docker/`** so relative paths resolve).

## Services

| Service | Role |
|--------|------|
| **fastapi** | App image (`minirag/Dockerfile`): Alembic migrations on start, then **Uvicorn** on port **8000** (4 workers; no bind-mount of source, so **no hot reload** in this stack) |
| **nginx** | Reverse proxy on host **80** → `fastapi:8000` |
| **pgvector** | PostgreSQL **17** with **pgvector** (`pgvector/pgvector:0.8.0-pg17`), port **5432** |
| **qdrant** | Optional vector DB when the app is configured with `VECTOR_DB_BACKEND=QDRANT` (host **6333** / **6334**) |
| **prometheus** | Scrapes FastAPI metrics, Qdrant, node-exporter, self, Postgres exporter |
| **grafana** | Dashboards on host **3000** |
| **node-exporter** | Host metrics on **9100** |
| **postgres_exporter** | Postgres metrics on **9187** (Compose service name uses an **underscore**) |
| **rabbitmq** | Celery **AMQP broker**; **5672** (AMQP), **15672** (management UI when enabled). Env: **`docker/env/.env.rabbitmq`**. |
| **redis** | Celery **result backend** (and optional broker in other setups); **6379**. Password from **`docker/env/.env.redis`** (`REDIS_PASSWORD`; compose default **`minirag_redis_2222`**). |
| **celery-worker** | Same **`minirag`** image as **fastapi**; runs **`celery -A celery_app worker`**. Needs **`CELERY_*`** (see **`docker/env/.env.example.celery`**, merged via Compose **`env_file`**). |

Application data written under `/app/assets` in the container is stored in the **`fastapi_data`** volume.

## Environment files

Compose reads per-service files under **`docker/env/`**:

- **`.env.app`** — application settings (mirrors `src/.env.example` style: DB host `pgvector`, LLM keys, `VECTOR_DB_BACKEND`, etc.). For Celery inside Compose, append or merge variables from **`.env.example.celery`** (broker/backend URLs must use service hostnames **`rabbitmq`** and **`redis`**).
- **`.env.postgres`** — `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` for the database container
- **`.env.grafana`** — Grafana admin credentials
- **`.env.postgres-exporter`** — `DATA_SOURCE_NAME` for postgres_exporter
- **`.env.rabbitmq`** — `RABBITMQ_DEFAULT_USER`, `RABBITMQ_DEFAULT_PASS`, `RABBITMQ_DEFAULT_VHOST` for the broker container
- **`.env.redis`** — `REDIS_PASSWORD` and tuning keys for the Redis container
- **`.env.example.celery`** — template **`CELERY_*`** URLs and tuning (copy values into **`.env.app`** or a dedicated worker env file)

Templates:

```bash
cd docker/env
# If your repo ships these templates, copy them; otherwise create .env.* from docs or from the examples above.
cp .env.example.app .env.app 2>/dev/null || true
cp .env.example.grafana .env.grafana 2>/dev/null || true
cp .env.example.postgres-exporter .env.postgres-exporter 2>/dev/null || true
# Celery: merge CELERY_* lines from .env.example.celery into .env.app (or maintain a separate env file for workers).
```

Create **`.env.postgres`** with valid credentials and the same database name/user expectations as **`.env.app`** (the app must be able to connect to the DB the stack starts).

> **Note:** If you only see a misnamed template like `.env .example.postgres` (space in the filename), create **`docker/env/.env.postgres`** manually using the same variables as a standard Postgres image (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`).

## Alembic inside the image

The runtime image copies **`docker/minirag/alembic.ini`** into `/app/models/db_schemes/minirag/alembic.ini`. To customize locally before build:

```bash
cd docker/minirag
cp alembic.ini.example alembic.ini
# edit if needed, then rebuild
```

## Start the stack

From **`docker/`**:

```bash
docker compose up --build -d
```

Start a subset (example: databases + app + edge):

```bash
docker compose up -d pgvector qdrant fastapi nginx
```

Start **broker + Redis** only (Phase 0 smoke / Celery prep):

```bash
docker compose up -d rabbitmq redis
docker compose ps rabbitmq redis
```

If the API starts before Postgres is ready, rely on **`depends_on`** with **`condition: service_healthy`** on `pgvector`, or restart FastAPI after databases are up:

```bash
docker compose restart fastapi
```

Tear down including volumes:

```bash
docker compose down -v --remove-orphans
```

## URLs (default ports)

| Service | URL |
|--------|-----|
| API (direct) | http://localhost:8000 |
| API docs | http://localhost:8000/docs |
| Through Nginx | http://localhost/ |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Qdrant dashboard | http://localhost:6333/dashboard |
| RabbitMQ management | http://localhost:15672 (management UI; login matches **`RABBITMQ_DEFAULT_*`** in **`docker/env/.env.rabbitmq`**) |

## RabbitMQ, Redis, and Celery

### Ports

| Service | Host port | Notes |
|--------|-----------|--------|
| **rabbitmq** | **5672** | AMQP for Celery broker |
| **rabbitmq** | **15672** | Management plugin UI |
| **redis** | **6379** | Result backend; requires **`AUTH`** (see **`REDIS_PASSWORD`** in **`docker/env/.env.redis`**) |

### Smoke check (recorded)

From **`docker/`**, with **`.env.rabbitmq`** and **`.env.redis`** present (as in this repo):

```bash
docker compose up -d rabbitmq redis
docker compose ps rabbitmq redis
```

Expect **State** `running` (or healthy) for both. Then:

```bash
# RabbitMQ (inside container; matches compose healthcheck)
docker compose exec rabbitmq rabbitmq-diagnostics ping

# Redis (password must match REDIS_PASSWORD in docker/env/.env.redis; default in compose is minirag_redis_2222)
docker compose exec redis redis-cli -a "${REDIS_PASSWORD:-minirag_redis_2222}" ping
```

Expect **`Ping succeeded`** (RabbitMQ diagnostics) and **`PONG`** (Redis).

### Celery URLs

- **Inside Docker network** (worker or app container): use **`CELERY_BROKER_URL`** / **`CELERY_RESULT_BACKEND`** from **`docker/env/.env.example.celery`** (hosts **`rabbitmq`**, **`redis`**).
- **On the host** (e.g. `celery -A celery_app worker` from `src/` with published ports): use **`localhost`** in those URLs and the same user/password/vhost and Redis password as in **`docker/env/.env.rabbitmq`** and **`docker/env/.env.redis`**.

### Celery worker (`celery-worker` service)

From **`docker/`** (after **`pgvector`**, **`rabbitmq`**, and **`redis`** are healthy):

```bash
docker compose up -d celery-worker
docker compose logs -f --tail=50 celery-worker
```

**Phase 1.7 — broker + result smoke** (synchronous `call`, no Redis polling required):

```bash
chmod +x ./celery-ping-smoke.sh   # once
./celery-ping-smoke.sh
```

Expect JSON like `{"ok": true, "task": "tasks.maintenance.ping"}`.

### Phase 2 manual check (async index + job status)

With **fastapi** and **celery-worker** up, enqueue index push (replace `PROJECT_ID`):

```bash
curl -sS -X POST "http://localhost:8000/api/v1/nlp/index/push/PROJECT_ID/async" \
  -H "Content-Type: application/json" \
  -d '{"do_reset":0}'
```

Copy **`task_id`** from the response, then poll:

```bash
curl -sS "http://localhost:8000/api/v1/jobs/TASK_ID"
```

When **`state`** is **`SUCCESS`**, **`result`** should include **`signal`** and **`inserted_items_count`** (same shape as the synchronous index push body). Compare counts with **`POST /api/v1/nlp/index/push/{project_id}`** on a small fixture project if you need parity proof.

## Metrics

FastAPI exposes Prometheus text on a **fixed, non-documented path** (see `src/utils/metrics.py`):

```text
http://localhost:8000/TrhBVe_m5gg2002_E5VVqS
```

Nginx proxies **`/TrhBVe_m5gg2002_E5VVqS`** to the same backend path (`nginx/default.conf`). **`prometheus/prometheus.yml`** sets `metrics_path` for the `fastapi` job to that path.

If the **postgres** scrape job fails, confirm the scrape **hostname** matches the Compose **service** name. This project names the service **`postgres_exporter`**; Prometheus must target a resolvable DNS name on the Compose network (adjust `prometheus.yml` if your target name differs).

## Volume tips

Common maintenance commands:

```bash
docker volume ls
docker volume inspect <volume_name>
docker compose logs --tail=100 fastapi
docker compose logs --tail=100 pgvector
```

For production backups, prefer **`pg_dump`** / **`pg_restore`** over only archiving Docker volumes.

## Grafana

1. Sign in (credentials from **`docker/env/.env.grafana`**; example template uses `admin` / `admin_password`).
2. Add Prometheus data source URL **`http://prometheus:9090`** (from inside the Grafana container network).
3. Optionally import community dashboards, for example:
   - [FastAPI observability](https://grafana.com/grafana/dashboards/18739-fastapi-observability/)
   - [Node exporter full](https://grafana.com/grafana/dashboards/1860-node-exporter-full/)
   - [Qdrant](https://grafana.com/grafana/dashboards/23033-qdrant/)
   - [PostgreSQL exporter](https://grafana.com/grafana/dashboards/12485-postgresql-exporter/)

## systemd (server)

**`minirag.service`** is an example unit that runs **`docker compose up --build -d`** from a fixed **`WorkingDirectory`** on the server. Edit **`WorkingDirectory`**, **`User`**, and **`Group`** for your host. GitHub Actions in the repo reference restarting this service after deploy.
