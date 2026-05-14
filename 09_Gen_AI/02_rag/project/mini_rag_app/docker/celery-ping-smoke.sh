#!/usr/bin/env bash
# Phase 1.7: run a synchronous Celery task inside the worker container (broker + result backend).
set -euo pipefail
cd "$(dirname "$0")"
docker compose exec -T celery-worker celery -A celery_app call tasks.maintenance.ping
