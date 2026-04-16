# Full Roadmap

## Phase 01 — Foundation: LLM APIs and Prompt Engineering

### Goal
Learn to build reliable, typed, and controllable LLM applications.

### Skills
- prompt engineering
- chat completion patterns
- structured outputs
- role separation
- memory basics
- token accounting
- error handling and retries

### Frameworks
#### Core
- FastAPI
- Pydantic
- OpenAI SDK / Anthropic SDK

#### Secondary
- Typer
- Rich

#### Avoid overusing
- agent frameworks too early

### Project
Build a **Structured Chat Assistant**:
- chat API
- CLI client
- JSON output mode
- short-term memory
- prompt templates

---

## Phase 02 — RAG

### Goal
Ground LLM answers in external context.

### Skills
- embeddings
- chunking
- retrieval
- re-ranking basics
- ingestion pipelines
- source attribution

### Frameworks
#### Core
- FAISS or Chroma
- SentenceTransformers
- FastAPI

#### Secondary
- LlamaIndex
- LangChain for retrieval only

### Project
Build a **Document Intelligence Service**:
- ingest documents
- create embeddings
- retrieve relevant chunks
- answer with citations

---

## Phase 03 — Agents and Tool Calling

### Goal
Build systems that can reason across steps and invoke tools.

### Skills
- function/tool schemas
- state and execution loops
- tool routing
- action/observation cycles
- long vs short term memory separation

### Frameworks
#### Core
- FastAPI
- OpenAI tool calling / Anthropic tools
- Redis

#### Secondary
- LangGraph / LangChain agents
- LlamaIndex agents

### Project
Build a **Multi-tool AI Operator**:
- weather tool
- search tool stub
- calculator tool
- database lookup tool
- audit trail

---

## Phase 04 — Production Systems

### Goal
Package AI services as production-grade systems.

### Skills
- service boundaries
- async APIs
- queues and workers
- rate limiting
- caching
- observability
- config management

### Frameworks
#### Core
- FastAPI
- Redis
- Docker
- PostgreSQL

#### Secondary
- Celery / RQ
- Prometheus / Grafana
- Nginx

### Project
Build a **Production AI Gateway**:
- central API
- routing to services
- auth stub
- caching
- metrics
- health checks

---

## Phase 05 — Evaluation and Optimization

### Goal
Measure quality, latency, and cost instead of guessing.

### Skills
- LLM eval methodology
- golden datasets
- benchmark design
- latency profiling
- prompt versioning
- hallucination analysis
- retrieval metrics

### Frameworks
#### Core
- Hugging Face Transformers
- Ollama
- pytest
- pandas

#### Secondary
- Weights & Biases
- LangSmith

### Project
Build an **Evaluation & Benchmark Suite**:
- prompt benchmark runner
- model comparison
- RAG retrieval benchmark
- cost and latency summary

---

## Phase 06 — Capstone

### Goal
Integrate all phases into one portfolio-grade AI platform.

### Project
Build an **AI Productivity Platform**:
- gateway API
- chat service
- RAG service
- agent service
- evaluation pipeline
- ingestion worker
- Redis / PostgreSQL
- observability dashboard
