# Architecture

## Services

- `gateway_api`: front door for clients
- `chat_service`: prompt orchestration and structured chat
- `rag_service`: ingestion, retrieval, grounded answering
- `agent_service`: tools, planning, execution traces
- `eval_service`: benchmarks, regression tests, scoring
- `ingestion_worker`: offline document processing

## Shared packages

- `shared/core`: settings, base schemas, utils
- `shared/observability`: logging, metrics, tracing helpers
- `shared/llm`: provider clients and prompt abstractions
- `shared/rag`: chunking, embedding, retrieval interfaces

## Data stores

- PostgreSQL: app metadata, runs, configs
- Redis: cache, short-term state, throttling
- FAISS / local store: embeddings index in dev
