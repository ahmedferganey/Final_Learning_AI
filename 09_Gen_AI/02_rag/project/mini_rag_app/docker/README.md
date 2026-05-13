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

Application data written under `/app/assets` in the container is stored in the **`fastapi_data`** volume.

## Environment files

Compose reads per-service files under **`docker/env/`**:

- **`.env.app`** — application settings (mirrors `src/.env.example` style: DB host `pgvector`, LLM keys, `VECTOR_DB_BACKEND`, etc.)
- **`.env.postgres`** — `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` for the database container
- **`.env.grafana`** — Grafana admin credentials
- **`.env.postgres-exporter`** — `DATA_SOURCE_NAME` for postgres_exporter

Templates:

```bash
cd docker/env
cp .env.example.app .env.app
cp .env.example.grafana .env.grafana
cp .env.example.postgres-exporter .env.postgres-exporter
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
