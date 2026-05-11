# RAG Application - Next Phase Plan

This plan captures the suggested next steps after adding RAG prompting templates (en/ar), retrieved-document schemas, and `answer_rag_question()`.

## Goals

- Provide a clean runtime API for asking RAG questions with language selection.
- Make RAG behavior observable and debuggable via persistent traces.
- Normalize vector DB payload structure to reduce edge cases.
- Add basic testing + evaluation so changes are safe and measurable.
- Prepare for multi-turn chat / session-based RAG.

## Proposed Tasks (Dependency-Ordered)

### 1) API: RAG Answer Endpoint

- Add a new request/response schema for RAG answering (question, language, top_k, limit, temperature, max_tokens, optional debug flag).
- Add a new route endpoint (e.g. `POST /api/v1/nlp/rag/answer/{project_id}`) that:
  - loads the project
  - calls `NLPController.answer_rag_question(language=...)`
  - returns `answer` + `hits` + (optional) `last_llm_payload` when debug is enabled
- Ensure consistent HTTP error handling when:
  - project not found
  - no collection exists
  - no docs retrieved
  - LLM call fails

### 2) Persistence: Store Prompt/Trace Data

- Define a DB schema/collection for LLM traces (prompt + docs + model params + response).
- Save per-request trace records including:
  - system/user messages sent
  - rendered user prompt (or hash + rendered)
  - last two lines of prompt
  - retrieved docs (text/metadata/score)
  - generation params (model, temperature, max_tokens)
  - final answer and timestamps
- Add a retrieval endpoint to fetch traces for a project (optional, admin/debug).

### 3) Data Consistency: Normalize Vector Payload Shape

- Standardize the payload written to the vector DB so it is always:
  - `{"text": <string>, "metadata": <dict>}`
- Update `insert_one()` to match `insert_many()` payload structure.
- Add a small migration strategy (optional) for existing collections if needed.

### 4) Quality Controls: Context + Retrieval Hygiene

- Add retrieval post-processing:
  - minimum score threshold (configurable)
  - deduplicate near-identical chunks
  - limit context size (truncate or summarize)
- Define explicit behavior when:
  - no relevant docs meet threshold
  - conflicting docs exist
  - context is too large

### 5) Tests: Unit + Integration

- Unit tests:
  - `TemplateParser` loads en/ar templates and falls back correctly
  - prompt rendering produces expected strings
  - metadata normalization works for both payload formats
- Integration tests (mocked):
  - vector search returns docs -> prompt -> LLM -> response
  - route returns correct response body with/without debug payload

### 6) Multi-Turn Chat Support (Optional Next)

- Add session concept:
  - store chat history per session/project
  - feed history into `generate_text(chat_history=...)`
- Add endpoints for session start/continue/reset.

## Deliverables

- New RAG answer endpoint with runtime language support (en/ar).
- Persisted trace logs for each RAG call.
- Normalized vector DB payloads.
- A minimal automated test suite for prompts + retrieval.
- (Optional) session-based multi-turn RAG.

