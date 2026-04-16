#!/usr/bin/env bash
set -e

# 1) Kick off the default entrypoint *in the background*
#    this will run initialization scripts and start postgres
/docker-entrypoint.sh postgres &

# 2) Wait until Postgres is accepting connections
until pg_isready -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB"; do
  echo "Waiting for Postgres to be ready…"
  sleep 2
done

# 3) Always re-apply your init.sql (optional, dev only)
/usr/bin/psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /docker-entrypoint-initdb.d/init.sql

# 4) Bring Postgres back to foreground so the container PID 1 is the server
wait

