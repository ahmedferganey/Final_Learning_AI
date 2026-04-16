# Data Model: AI-Powered Backend System

## User

- **Purpose**: Represents an authenticated principal.
- **Key fields**:
  - `id: UUID`
  - `email: string`
  - `password_hash: string`
  - `full_name: string`
  - `is_active: bool`
  - `created_at: datetime`
  - `updated_at: datetime`
- **Relationships**:
  - many-to-many with `Role`
  - one-to-many with `RefreshSession`
  - one-to-many with `AuditEvent`

## Role

- **Purpose**: Encodes authorization levels for protected operations.
- **Key fields**:
  - `id: UUID`
  - `name: enum(user, manager, admin)`
  - `description: string`

## RefreshSession

- **Purpose**: Tracks refresh token lifecycle and revocation state.
- **Key fields**:
  - `id: UUID`
  - `user_id: UUID`
  - `token_id: UUID`
  - `token_hash: string`
  - `expires_at: datetime`
  - `revoked_at: datetime | null`
  - `replaced_by_token_id: UUID | null`
  - `created_at: datetime`
  - `last_used_at: datetime | null`
  - `client_fingerprint: string | null`

## AuditEvent

- **Purpose**: Captures traceable security and operational actions.
- **Key fields**:
  - `id: UUID`
  - `actor_user_id: UUID | null`
  - `event_type: string`
  - `resource_type: string`
  - `resource_id: string | null`
  - `status: enum(success, failure)`
  - `metadata: jsonb`
  - `created_at: datetime`

## KnowledgeCollection

- **Purpose**: Defines a searchable corpus boundary for RAG.
- **Key fields**:
  - `id: UUID`
  - `slug: string`
  - `name: string`
  - `description: string`
  - `visibility: enum(private, team, global)`
  - `created_by_user_id: UUID`
  - `created_at: datetime`

## DocumentChunk

- **Purpose**: Stores retrieval-ready chunks and source metadata.
- **Key fields**:
  - `id: UUID`
  - `collection_id: UUID`
  - `document_id: UUID`
  - `chunk_index: integer`
  - `content: text`
  - `embedding: vector`
  - `source_uri: string`
  - `source_title: string`
  - `token_count: integer`
  - `created_at: datetime`

## RagQueryRequest

- **Purpose**: API-level request model for retrieval and generation.
- **Key fields**:
  - `query: string`
  - `collection_ids: UUID[]`
  - `top_k: integer`
  - `conversation_context: string[]`
  - `include_citations: bool`

## RagAnswer

- **Purpose**: API-level response model for generated answers.
- **Key fields**:
  - `answer: string`
  - `citations: Citation[]`
  - `model_name: string`
  - `retrieved_chunk_count: integer`
  - `latency_ms: integer`

## Citation

- **Purpose**: References the evidence used to support an answer.
- **Key fields**:
  - `chunk_id: UUID`
  - `source_title: string`
  - `source_uri: string`
  - `snippet: string`
  - `score: number`
