# GymOS

An adaptive training intelligence platform — not a workout tracker.
GymOS dynamically adjusts load, volume, and structure based on real performance data,
models fatigue across sessions, and applies structured progression algorithms
(linear, double progression, wave, RPE-based).

## Client Surfaces

| Surface | Technology | Best for |
|---|---|---|
| Backend | FastAPI (Python 3.11+) | All business logic, coaching engine, data authority |
| Web | Next.js 14 (TypeScript) | Plan design, analytics, history, deep editing, settings |
| Mobile | Flutter | In-gym execution, set logging, rest timer, offline capture |

## Technology Stack

- Backend: FastAPI · Python 3.11+ · SQLAlchemy (async) · Alembic · Pydantic v2
- Database: PostgreSQL (primary) · Redis (cache + job queue)
- Web: Next.js 14 (App Router) · TypeScript (strict mode)
- Mobile: Flutter · Riverpod · Dio · Hive/Drift
- Infrastructure: Docker

## Directory Layout

```text
gymos/
├── backend/    FastAPI application code
├── web/        Next.js application code
├── mobile/     Flutter application code
├── infra/      Docker, CI, infrastructure config
├── docs/       Architecture docs, ADRs, API contracts
└── specs/      Spec Kit feature specifications
```

## Getting Started

- See `CONTRIBUTING.md` for branch strategy, commit conventions, and PR process.
- See `specs/` for all feature specifications organized by phase.
