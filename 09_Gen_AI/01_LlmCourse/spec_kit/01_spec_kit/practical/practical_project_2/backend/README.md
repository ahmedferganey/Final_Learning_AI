# Backend

## Prerequisites

- Python 3.11
- PostgreSQL
- Redis

## Install

`pip install -e ".[dev]"`

## Environment

Copy `.env.example` to `.env` and fill in the required values.

## Run

Use `make run` or `uvicorn app.main:app --reload`.

## Quality checks

Run `make lint` and `make test`.

## Migrations

Run `alembic upgrade head`.

## Port conflict

Set the `PORT` environment variable to override port 8000.
