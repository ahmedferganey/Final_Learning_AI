# ADR 001: Use a Modular Monolith Architecture

**Status**: proposed

**Date**: 2026-04-09

## Context

GymOS has eight backend modules (auth, users, training, coaching, analytics, nutrition,
notifications, sync) that share a single data model and must call each other frequently. The
team is pre-product-market fit with a small codebase. Distributed systems add network
partitions, independent deployments, distributed tracing complexity, and eventual consistency
concerns that are not warranted at this stage.

## Decision

GymOS will be developed as a modular monolith through Phase 8. All backend modules share a
single FastAPI process and a single PostgreSQL database. Each module has its own SQLAlchemy
models, Pydantic schemas, service layer, router, and test suite. Cross-module calls go through
the owning module's service interface — never via direct model imports from another module's
internal layer.

This decision should be revisited if: (a) a specific module requires per-module horizontal
scaling that cannot be achieved by vertical scaling the monolith, or (b) team growth creates
deployment coordination friction that module isolation would solve.

## Consequences

**Positive:**
Simpler deployment (single process), simpler debugging (no network hops between components),
straightforward testing (no distributed test infrastructure), clear module boundaries that
preserve a future extraction path to microservices if needed.

**Negative / Tradeoffs:**
Horizontal scaling applies to the entire application, not individual modules. A bug in one
module can bring down all modules. Future extraction to microservices will require interface
cleanup if boundaries drift.

## Alternatives Considered

| Alternative | Reason rejected |
|---|---|
| Microservices from day one | Adds network partitions, distributed tracing, independent deployment pipelines, and eventual consistency concerns not warranted before product-market fit |
| Serverless functions | Stateless model poorly suited to long-running coaching calculations; cold starts unacceptable for in-gym use; harder to test locally |

## Superseded By
