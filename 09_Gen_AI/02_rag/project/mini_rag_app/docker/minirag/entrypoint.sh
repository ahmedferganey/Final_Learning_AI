#!/bin/bash
set -ex  # 👈 important (prints commands)

echo "ENTRYPOINT STARTED"

echo "PWD: $(pwd)"
echo "Listing /app:"
ls -la /app

echo "CMD received: $@"

echo "Running database migrations..."
cd /app/models/db_schemes/minirag/
alembic upgrade head

cd /app

echo "Checking uvicorn..."
which uvicorn || echo "uvicorn NOT FOUND"

echo "Checking python uvicorn..."
python -m uvicorn --help || echo "python -m uvicorn FAILED"

echo "Starting FastAPI..."
exec "$@"