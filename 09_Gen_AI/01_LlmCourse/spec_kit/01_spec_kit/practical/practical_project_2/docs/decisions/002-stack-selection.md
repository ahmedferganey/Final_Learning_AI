# ADR 002: Technology Stack Selection

**Status**: proposed

**Date**: 2026-04-09

## Context

GymOS requires three surfaces: a backend API with complex domain logic (coaching engine,
progression algorithms, fatigue modeling), a web dashboard for plan editing and analytics, and
a mobile app for in-gym use with offline capability. All surfaces must share data through a
single authoritative backend. The stack must support strong typing, async I/O for the backend,
offline-first mobile, and containerized deployment.

## Decision

- Backend language/framework: Python 3.11+ with FastAPI (async, type-annotated, Pydantic v2 request validation)
- ORM: SQLAlchemy async with Alembic for migrations
- Primary database: PostgreSQL (ACID guarantees, complex analytics queries, row-level security)
- Cache and job queue: Redis (session cache, rate limit counters, offline sync queue, background jobs)
- Background jobs: Celery or RQ (Redis-backed)
- Web framework: Next.js 14 (App Router), TypeScript strict mode
- Mobile framework: Flutter (Dart), Riverpod for state management, Dio for HTTP, Hive or Drift for local storage
- Containers: Docker for all services

## Consequences

**Positive:**
Well-established ecosystems with strong community support. Strong typing across all layers
(Python mypy + TypeScript + Dart). FastAPI's Pydantic validation enforces contracts at the API
boundary. Flutter's offline/local-storage capabilities are well-suited to in-gym use.

**Negative / Tradeoffs:**
Three separate codebases (Python, TypeScript, Dart) require expertise across all three
languages. Flutter/Dart ecosystem is smaller than React Native. PostgreSQL requires a running
database for all integration tests.

## Alternatives Considered

| Alternative | Reason rejected |
|---|---|
| Node.js/Express for backend | Less ergonomic for complex domain logic; Pydantic-style runtime validation not native |
| React Native for mobile | Flutter performance and offline storage (Hive/Drift) better suited for in-gym use |
| MongoDB for primary DB | Lacks ACID transactions needed for coaching decision auditability; weaker analytics query support |
| SQLite for primary DB | Insufficient for multi-user concurrent writes and complex analytics |

## Superseded By
