# Plan: Pluggable Vector DB Support with Qdrant and PGVector

## 1. Problem Definition

### Current Limitation

- The RAG pipeline currently depends directly on the existing Qdrant vector DB implementation.
- Provider-specific logic leaks into application flow through concrete Qdrant client usage.
- Adding PGVector directly beside Qdrant without an abstraction would duplicate indexing, search, delete, and collection/table management logic.
- Runtime switching is not clean if route/controller/service code knows which vector database is active.

### Target State

- The application supports both Qdrant and PGVector integrations.
- Only one vector DB provider is selected at runtime through configuration.
- RAG services depend on a unified vector store interface, not provider-specific classes.
- Qdrant remains the default provider during rollout.
- PGVector is added without removing or weakening the existing Qdrant flow.

## 2. High-Level Architecture

### Core Components

- `VectorStore` interface:
  - Defines the contract used by indexing, search, delete, and RAG retrieval.
  - Hides provider-specific details from routes and controllers.

- `QdrantVectorStore`:
  - Wraps the existing Qdrant implementation.
  - Keeps Qdrant collection management and search behavior behind the interface.

- `PGVectorStore`:
  - Uses PostgreSQL + PGVector for vector storage and similarity search.
  - Uses SQLAlchemy async sessions or an async connection strategy compatible with the app.

- `VectorStoreFactory` or DI provider:
  - Reads configuration.
  - Builds the selected vector store implementation.
  - Exposes one runtime-selected instance to application services.

### Dependency Direction

- Routes call services/controllers.
- Services/controllers depend on `VectorStore`.
- Concrete vector DB providers depend on external clients/drivers.
- Application flow does not import Qdrant or PGVector implementations directly.

## 3. Configuration Design

### Environment Variables

```env
VECTOR_DB_PROVIDER=qdrant

# Qdrant
QDRANT_PATH=qdrant_db
QDRANT_DISTANCE_METHOD=cosine

# PGVector
PGVECTOR_TABLE=rag_embeddings
PGVECTOR_DISTANCE_METHOD=cosine
PGVECTOR_EMBEDDING_DIM=384
```

Allowed values:

- `qdrant`
- `pgvector`

### Settings Module

- Keep vector DB configuration in `src/helpers/config.py`.
- Validate `VECTOR_DB_PROVIDER` during settings load.
- Keep Qdrant-specific and PGVector-specific settings separate.
- Reuse the existing PostgreSQL `DATABASE_URL` for PGVector unless a separate vector DB connection is required.

### Runtime Resolution

- On app startup:
  - load settings
  - create required shared resources
  - resolve `VECTOR_DB_PROVIDER`
  - initialize the selected `VectorStore`
  - attach it to `app.vector_store`

- Invalid provider values should fail fast during startup.

## 4. Interface Design

Define one unified async interface for vector storage:

- `add_documents(project_id, documents, embeddings, metadata)`
  - Inserts documents and vectors for one project.
  - Must preserve enough metadata to reconstruct RAG citations and source text.

- `similarity_search(project_id, query_embedding, top_k, filters=None)`
  - Returns normalized retrieved documents.
  - Response shape should match the existing `RetrievedDocument` schema.

- `delete(project_id, ids=None, filters=None)`
  - Deletes all project vectors or selected vectors.
  - Used for project reset and re-indexing.

- `upsert(project_id, documents, embeddings, metadata)`
  - Optional provider capability.
  - Can be implemented as delete + add if provider-native upsert is unavailable.

- `hybrid_search(project_id, query_text, query_embedding, top_k, filters=None)`
  - Optional future capability.
  - Do not expose in core flow until both providers have a clear behavior.

Interface rules:

- Methods should be async even if one provider wraps a sync client internally.
- Inputs should use app-level DTOs or simple typed objects.
- Outputs should be provider-neutral.
- Provider-specific IDs must not leak into route responses unless normalized.

## 5. Implementation Plan

### Step 1: Define Provider-Neutral Contract

- Add a vector store interface module.
- Define required async methods.
- Define normalized return models if current schemas are insufficient.
- Keep `RetrievedDocument` as the public retrieval result unless it blocks provider neutrality.

### Step 2: Refactor Existing Qdrant Logic

- Move current Qdrant operations behind `QdrantVectorStore`.
- Preserve current Qdrant behavior:
  - collection naming
  - vector insertion
  - search response shape
  - reset behavior
- Keep route and RAG behavior unchanged after refactor.

### Step 3: Add PGVector Schema and Migration

- Add a dedicated PGVector table for embeddings.
- Use Alembic as the only mechanism for table creation.
- Recommended columns:
  - `id` UUID primary key
  - `project_id` public string or `project_uuid` UUID
  - `chunk_id` UUID nullable or required depending on current chunk flow
  - `document_text` text
  - `metadata` JSONB
  - `embedding` vector dimension configured by `PGVECTOR_EMBEDDING_DIM`
  - `created_at`
  - `updated_at`
- Add indexes appropriate for PGVector distance strategy.

### Step 4: Implement `PGVectorStore`

- Use async SQLAlchemy where possible.
- Insert vectors with metadata in batches.
- Implement similarity search using the configured distance metric.
- Return the same normalized result shape as Qdrant.
- Keep embedding generation outside the vector store.

### Step 5: Create Factory Selector

- Add `VectorStoreFactory`.
- Read `settings.VECTOR_DB_PROVIDER`.
- Return `QdrantVectorStore` or `PGVectorStore`.
- Fail startup for unknown providers.

### Step 6: Inject into RAG Pipeline

- Replace hardcoded Qdrant references in routes/controllers/services with `app.vector_store` or a FastAPI dependency.
- Keep service logic provider-neutral.
- Keep provider-specific setup inside startup/factory code.

### Step 7: Preserve Existing Behavior

- Keep Qdrant as default.
- Existing endpoints should keep the same request/response shape.
- Search and RAG response payloads should remain stable.

## 6. Dependency Injection Strategy

### Startup Injection

- Build the selected vector store once during app startup.
- Store it on the FastAPI app state:
  - `app.vector_store`

### Request-Time Access

- Add a dependency such as `get_vector_store(request)`.
- Routes receive `VectorStore` through dependency injection.
- Controllers/services receive the interface instance as a constructor argument.

### Rules

- Do not instantiate vector DB providers inside route handlers.
- Do not branch on provider name inside business logic.
- Provider switching should only happen in factory/startup code.
- Tests should be able to inject a fake vector store.

## 7. Migration Strategy

### Phase 1: Non-Breaking Refactor

- Introduce the interface.
- Wrap existing Qdrant logic without changing behavior.
- Keep `VECTOR_DB_PROVIDER=qdrant` as the default.

### Phase 2: PGVector Infrastructure

- Add PGVector dependency and Alembic migration.
- Add PGVector ORM/table mapping if SQLAlchemy is used.
- Verify migration with upgrade/downgrade/upgrade.

### Phase 3: PGVector Runtime Support

- Implement `PGVectorStore`.
- Add configuration.
- Add provider selection tests.

### Phase 4: Controlled Rollout

- Test Qdrant and PGVector independently.
- Run local smoke tests for upload, process, index, search, and RAG answer.
- Switch provider only through env configuration.

### Compatibility Rules

- No breaking endpoint changes.
- No forced migration from Qdrant vectors to PGVector.
- Re-indexing from PostgreSQL chunks should be the standard way to populate the selected provider.

## 8. Testing Strategy

### Unit Tests

- Test vector store interface consumers with a fake vector store.
- Test factory provider selection.
- Test invalid provider config fails clearly.
- Test normalized retrieval result shape.

### Qdrant Integration Tests

- Verify collection creation/reset.
- Verify document indexing.
- Verify similarity search returns expected normalized payloads.
- Verify delete/reset behavior.

### PGVector Integration Tests

- Verify Alembic creates vector table and indexes.
- Verify batch insert.
- Verify similarity search ordering.
- Verify delete by project.
- Verify metadata round-trip through JSONB.

### Config Switching Tests

- Run the same RAG flow with:
  - `VECTOR_DB_PROVIDER=qdrant`
  - `VECTOR_DB_PROVIDER=pgvector`
- Assert routes do not change response shape.
- Assert only the selected provider is initialized.

## 9. Risks & Edge Cases

- Embedding dimension mismatch:
  - PGVector table dimension must match the active embedding model.
  - Fail fast if configured dimension differs from embedding output size.

- Distance metric differences:
  - Qdrant and PGVector may score cosine/euclidean/dot product differently.
  - Normalize only the response shape, not necessarily exact score values.

- Schema ownership:
  - PGVector tables must be managed by Alembic.
  - Do not create vector tables during FastAPI startup.

- Metadata differences:
  - Qdrant payloads and PostgreSQL JSONB metadata must preserve the same retrieval fields.
  - Keep metadata keys stable for RAG prompts and citations.

- Performance differences:
  - PGVector requires correct indexes for production-sized data.
  - Batch insert and query plans should be tested with realistic chunk counts.

- Transaction boundaries:
  - PostgreSQL metadata and PGVector writes may share a database but should have explicit transaction behavior.
  - Avoid committing vector writes in hidden helper methods unless the service owns the full operation.

- Re-indexing behavior:
  - Switching providers does not automatically migrate existing vector data.
  - The app should support re-indexing from stored chunks into the selected provider.

## 10. Future Extensions

- Add more providers:
  - Weaviate
  - Pinecone
  - Milvus
  - Elasticsearch/OpenSearch vector search

- Add feature flags:
  - provider-specific rollout
  - per-environment provider selection
  - gradual PGVector enablement

- Add multi-provider fallback:
  - primary provider for writes
  - fallback provider for reads
  - background consistency checks

- Add dual-write mode only if production migration requires it:
  - write to both Qdrant and PGVector
  - read from configured primary
  - compare retrieval quality and latency

- Add observability:
  - provider name in logs
  - indexing latency
  - search latency
  - returned score ranges
  - vector insert counts
