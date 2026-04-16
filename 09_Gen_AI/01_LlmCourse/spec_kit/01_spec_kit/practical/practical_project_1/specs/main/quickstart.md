# Quickstart: AI-Powered Backend System

## Prerequisites

- Python 3.12
- PostgreSQL 15+
- A configured JWT signing secret or private key
- An LLM provider API key for generation

## Environment

Create a `.env` file for local development:

```env
APP_ENV=development
DATABASE_URL=postgresql+psycopg://app:app@localhost:5432/aibackend
JWT_ACCESS_TTL_SECONDS=900
JWT_REFRESH_TTL_SECONDS=1209600
JWT_SIGNING_KEY=replace-me
LLM_PROVIDER_API_KEY=replace-me
```

## Start the backend

```bash
uvicorn backend.app.main:app --reload
```

## Validate authentication flow

1. Register a user via `POST /v1/auth/register`
2. Capture `access_token` and `refresh_token`
3. Call `GET /v1/users/me` with `Authorization: Bearer <access_token>`
4. Call `POST /v1/auth/refresh` with the refresh token
5. Call `POST /v1/auth/logout` to revoke the active session

## Validate admin flow

1. Seed or promote one user to the `admin` role
2. Call `PUT /v1/users/{user_id}/roles`
3. Confirm the target user's profile reflects the new roles
4. Confirm a non-admin caller receives HTTP 403 for the same action

## Validate RAG flow

1. Seed one or more `KnowledgeCollection` records and indexed chunks
2. Call `POST /v1/rag/query` with a valid authenticated user
3. Confirm the response includes `answer`, `citations`, and latency metadata
4. Confirm invalid payloads and unauthorized collection access return structured errors
