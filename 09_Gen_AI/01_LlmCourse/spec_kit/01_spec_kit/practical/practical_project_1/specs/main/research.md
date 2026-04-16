# Research: AI-Powered Backend System

## Decision 1: FastAPI as the application framework

- **Decision**: Use FastAPI for all HTTP APIs and OpenAPI generation.
- **Rationale**: FastAPI provides strong type-driven request validation, first-class OpenAPI support, and a clear fit for auth and AI-serving endpoints.
- **Alternatives considered**:
  - Django REST Framework: heavier than needed for a focused service stack.
  - Flask: requires more manual validation and schema plumbing.

## Decision 2: JWT access tokens with server-side refresh session records

- **Decision**: Use short-lived JWT access tokens and store refresh sessions in PostgreSQL with rotation metadata.
- **Rationale**: This preserves stateless request authentication while allowing revocation, replay detection, logout, and device-scoped session management.
- **Alternatives considered**:
  - Fully stateless JWT refresh tokens: poor revocation and replay control.
  - Opaque access tokens only: adds lookup cost to every authenticated request.

## Decision 3: RBAC with explicit role claims plus policy checks

- **Decision**: Use role claims in access tokens and re-check critical authorization rules in service-layer permission guards.
- **Rationale**: Tokens enable fast request filtering while service-layer checks protect against drift and support auditability.
- **Alternatives considered**:
  - Route-only authorization decorators: too shallow for domain-level checks.
  - Attribute-based access control for v1: more flexible but unnecessary complexity for initial scope.

## Decision 4: PostgreSQL as both operational store and retrieval metadata store

- **Decision**: Store users, refresh sessions, audit events, collections, chunks, and vector metadata in PostgreSQL.
- **Rationale**: Reduces system sprawl for v1 and keeps auth and retrieval consistency inside one durable datastore.
- **Alternatives considered**:
  - Separate vector database: higher operational complexity for initial delivery.
  - SQLite: insufficient concurrency and operational guarantees for the stated scale.

## Decision 5: RAG pipeline orchestration behind a dedicated service layer

- **Decision**: Split retrieval, generation, and orchestration into separate services behind a single RAG API route.
- **Rationale**: Keeps provider-specific logic isolated and makes testing easier across retrieval-only, generation-only, and end-to-end flows.
- **Alternatives considered**:
  - Single monolithic endpoint function: harder to test and evolve.
  - Agentic multi-step orchestration from day one: too much complexity for baseline delivery.
