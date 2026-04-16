# LLM / Generative AI Engineer Production Roadmap Monorepo

This repository is a **study + implementation monorepo** for becoming a production-grade **LLM Engineer / Generative AI Engineer**.

It is intentionally structured as both:
1. a **learning roadmap**, and
2. a **build system** for progressively shipping working AI services.

## Repository Goals

By finishing this repo, you should be able to:

- build LLM apps with API providers and local models
- design prompt pipelines and structured-output systems
- implement RAG with evaluation and observability
- build tool-calling and agentic systems
- package services with Docker and deploy them
- benchmark models, prompts, and retrieval quality
- ship a final integrated AI platform

---

## Phases

| Phase | Name | Main Outcome | Main Project |
|---|---|---|---|
| 01 | Foundation | Reliable LLM API usage | Structured Chat Assistant |
| 02 | RAG | External knowledge grounding | Document Intelligence Service |
| 03 | Agents | Tool-calling workflows | Multi-tool AI Operator |
| 04 | Production | Scalable services & infra | Production AI Gateway |
| 05 | Evaluation | Measurement and optimization | Evaluation & Benchmark Suite |
| 06 | Capstone | Full platform integration | AI Productivity Platform |

---

## Monorepo Layout

```text
.
├── README.md
├── ROADMAP.md
├── pyproject.toml
├── Makefile
├── .env.example
├── docker-compose.yml
├── docs/
├── infra/
├── scripts/
├── shared/
│   ├── core/
│   ├── observability/
│   ├── llm/
│   └── rag/
├── services/
│   ├── gateway_api/
│   ├── chat_service/
│   ├── rag_service/
│   ├── agent_service/
│   ├── eval_service/
│   └── ingestion_worker/
├── phases/
│   ├── 01_foundation/
│   ├── 02_rag/
│   ├── 03_agents/
│   ├── 04_production/
│   ├── 05_evaluation/
│   └── 06_capstone/
└── tests/
```

---

## How to Use This Repo

### Learning mode
Read in this order:

1. `ROADMAP.md`
2. `phases/01_foundation/README.md`
3. `phases/02_rag/README.md`
4. `phases/03_agents/README.md`
5. `phases/04_production/README.md`
6. `phases/05_evaluation/README.md`
7. `phases/06_capstone/README.md`

### Build mode
Implement in this order:

1. `services/chat_service`
2. `services/rag_service`
3. `services/agent_service`
4. `services/gateway_api`
5. `services/eval_service`
6. `infra/`

---

## Engineering Principles

- Prefer understanding before abstraction.
- Use frameworks selectively, not blindly.
- Every phase ends with a working project.
- Every project must have tests, docs, and a clear API contract.
- Every system should be observable, measurable, and reproducible.

---

## Recommended Core Stack

### Backend
- Python 3.12
- FastAPI
- Pydantic
- SQLAlchemy
- Redis
- PostgreSQL

### LLM / GenAI
- OpenAI SDK
- Anthropic SDK
- Ollama
- Hugging Face Transformers
- SentenceTransformers

### RAG
- FAISS / Chroma
- LlamaIndex
- LangChain (selectively)

### Infra
- Docker
- Docker Compose
- Nginx
- Prometheus / Grafana

### Testing / Quality
- pytest
- httpx
- Ruff
- MyPy

---

## Definition of Done for Any Phase

A phase is complete only when all of the following exist:

- concept notes are documented
- code skeleton is present
- project is runnable
- tests exist
- task checklist is complete
- README explains how to run it
- design tradeoffs are written down

---

## Suggested Weekly Rhythm

- Day 1-2: concepts + notes
- Day 3-4: implement minimal working version
- Day 5: refactor
- Day 6: tests + documentation
- Day 7: review + retrospective

---

## Next Deliverable After This Repo

Once this scaffold exists, your next step is to progressively implement:
- chat
- retrieval
- tools
- observability
- benchmarking
- full integration

Use GitHub issues from the phase task lists to drive execution.
