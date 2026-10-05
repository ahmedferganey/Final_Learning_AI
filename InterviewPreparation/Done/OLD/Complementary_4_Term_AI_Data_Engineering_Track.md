# Complementary 4-Term AI & Data Engineering Track

> **Purpose:** Complement the Nile University Big Data & Data Science Professional Diploma rather than duplicate it.  
> **Target roles:** Data Scientist, ML Engineer, AI Engineer, GenAI / LLM Engineer.  
> **Recommended extra workload:** Approximately **6–10 hours per week** alongside Nile University and full-time work.

---

# Curriculum Strategy

The Nile University Big Data & Data Science diploma already provides the academic core in:

- Probability and statistics
- Regression and statistical analysis
- Classical machine learning
- Clustering
- PCA / ICA
- Neural networks
- Hadoop
- Spark
- Big Data analytics
- Applied Data Science project work

The complementary track therefore focuses on the major areas that should be added on top of Nile:

- Professional Python development
- Software engineering
- SQL and PostgreSQL
- Data engineering
- Backend development
- APIs
- Docker
- CI/CD
- Cloud
- MLOps
- PyTorch
- Transformers
- LLM engineering
- Vector databases
- RAG
- AI agents
- Kubernetes
- Production AI system design

The objective is to avoid studying Machine Learning twice and instead build the engineering layers required to move from:

```text
Data Science
    ↓
Machine Learning
    ↓
ML Engineering
    ↓
AI Engineering
    ↓
Production Generative AI
```

---

# First Term — Software Engineering & Data Foundations

## SWE601: Python Software Engineering for AI

- **Advanced Python:** Functions, modules, packages, comprehensions, iterators, generators, decorators, and context managers.
- **Object-oriented programming:** Classes, inheritance, composition, abstraction, interfaces, and SOLID fundamentals.
- **Python typing:** Type hints, generics, protocols, and static type checking.
- **Data structures and algorithms:** Arrays, hash maps, stacks, queues, trees, searching, sorting, and algorithmic complexity.
- **Error handling:** Exceptions, custom exceptions, and robust failure handling.
- **Testing:** Unit testing with `pytest`, fixtures, mocking, and test-driven development fundamentals.
- **Logging and debugging:** Structured logging, debugging strategies, and profiling.
- **Code quality:** Formatting, linting, modularity, clean code, and refactoring.
- **Environment management:** `venv`, `pip`, `uv`, dependency management, and reproducible environments.
- **Project organization:** Building maintainable Python applications using professional directory structures.
- **Version control:** Git, GitHub, branches, pull requests, merge strategies, and code reviews.
- **AI-assisted development:** Effective use of coding assistants without replacing software-engineering fundamentals.

---

## DAT601: SQL, PostgreSQL & Data Modeling

- **SQL fundamentals:** `SELECT`, filtering, sorting, aggregation, and grouping.
- **Joins:** `INNER`, `LEFT`, `RIGHT`, `FULL`, and self joins.
- **Advanced SQL:** CTEs, subqueries, and recursive queries.
- **Window functions:** Ranking, partitions, running totals, and analytical functions.
- **Database design:** Tables, relationships, normalization, and denormalization.
- **Relational modeling:** Primary keys, foreign keys, and constraints.
- **PostgreSQL:** Installation, configuration, and practical database development.
- **Indexes:** B-tree indexes, composite indexes, and query-performance fundamentals.
- **Query optimization:** `EXPLAIN`, `EXPLAIN ANALYZE`, and execution plans.
- **Transactions:** ACID properties, isolation levels, and concurrency.
- **Data warehousing concepts:** Facts, dimensions, and star schemas.
- **Data quality:** Validation, constraints, missing values, and duplicate management.

---

## DAT602: Applied Data Engineering with Python

- **NumPy:** Vectorized numerical computing.
- **Pandas:** DataFrame manipulation, joins, grouping, reshaping, and time-series operations.
- **Polars:** High-performance dataframe processing.
- **Data ingestion:** CSV, JSON, APIs, relational databases, and object storage.
- **Data cleaning:** Missing values, duplicates, invalid records, and outliers.
- **ETL and ELT:** Extract, transform, and load workflows.
- **Data validation:** Schema validation and automated checks.
- **Pipeline design:** Reusable data-processing pipelines.
- **File formats:** CSV, JSON, Parquet, and Avro fundamentals.
- **Batch versus streaming processing:** Architectural differences and use cases.
- **Spark integration:** Connect local Python data workflows with the Spark knowledge learned at Nile.

### Term 1 Outcome

```text
Nile:
Statistics + ML + Spark

Complement:
Python Engineering + SQL + Data Engineering

Result:
Strong Data / ML Development Foundation
```

---

# Second Term — Backend, Cloud & MLOps

## SWE602: Backend Engineering for AI Systems

- **HTTP fundamentals:** Requests, responses, headers, status codes, and REST principles.
- **FastAPI:** Building production-oriented Python APIs.
- **Pydantic:** Schema validation and typed request / response models.
- **REST APIs:** CRUD operations and resource-oriented API design.
- **Asynchronous programming:** `async` / `await` and asynchronous I/O.
- **Database integration:** PostgreSQL with SQLAlchemy.
- **Database migrations:** Alembic.
- **Authentication:** Password hashing, JWT, and OAuth concepts.
- **Authorization:** Roles and permissions.
- **Caching:** Redis.
- **Background jobs:** Asynchronous task-processing concepts.
- **Streaming responses:** Important for LLM applications.
- **WebSockets:** Fundamentals for interactive AI applications.
- **API security:** Input validation, rate limiting, secrets, and secure API design.
- **Testing:** API and integration testing.
- **API documentation:** OpenAPI / Swagger.

---

## DEV601: Docker, Linux & CI/CD

- **Linux fundamentals:** File systems, processes, networking, permissions, and environment variables.
- **Shell basics:** Bash commands and scripting.
- **Docker concepts:** Images, containers, registries, volumes, and networks.
- **Dockerfile:** Building reproducible application containers.
- **Multi-stage builds:** Reducing production image size.
- **Docker Compose:** Running APIs, PostgreSQL, Redis, and AI services together.
- **Git workflows:** Feature branches and pull requests.
- **Continuous integration:** GitHub Actions.
- **Automated testing:** Running test suites in CI.
- **Container registries:** Image tagging and publishing.
- **Continuous deployment:** Basic automated deployment workflows.
- **Secrets management:** Safe configuration practices.
- **Deployment environments:** Development, staging, and production.

---

## MLO601: MLOps Foundations

- **ML experiment management:** Experiments, parameters, metrics, and artifacts.
- **MLflow:** Experiment tracking.
- **Model registry:** Versioning and lifecycle management.
- **Data versioning:** DVC fundamentals.
- **Model reproducibility:** Environment, code, and data versioning.
- **Training pipelines:** Automating model-training workflows.
- **Model packaging:** Saving and serving trained models.
- **Model deployment:** Batch versus online inference.
- **Model APIs:** Exposing ML predictions through FastAPI.
- **Monitoring:** Latency, failures, and prediction monitoring.
- **Data drift:** Detecting changes in input distributions.
- **Model drift:** Identifying model-performance degradation.
- **Retraining strategies:** Scheduled and event-triggered retraining.
- **CI/CD for ML:** Validation before model promotion.

### Term 2 Outcome

```text
Nile ML Model
      ↓
MLflow
      ↓
FastAPI
      ↓
Docker
      ↓
CI/CD
      ↓
Cloud Deployment
      ↓
Monitoring
```

At this stage, the goal is to move beyond notebook-only Machine Learning and start building deployable ML systems.

---

# Third Term — Deep Learning, Transformers & Generative AI

## AI601: Advanced Deep Learning with PyTorch

- **PyTorch fundamentals:** Tensors, datasets, dataloaders, and modules.
- **Automatic differentiation:** Autograd.
- **Neural-network training:** Forward propagation and backpropagation.
- **Loss functions:** Regression, classification, and representation-learning losses.
- **Optimization:** SGD, Momentum, and Adam.
- **Learning-rate scheduling.**
- **Regularization:** Dropout, weight decay, and normalization.
- **CNN architectures:** Fundamental convolutional architectures.
- **Sequence modeling:** RNN and LSTM concepts.
- **Attention:** Query, key, and value mechanism.
- **Transfer learning:** Using pretrained models.
- **Fine-tuning:** Adapting models to downstream tasks.
- **GPU acceleration:** CUDA concepts and GPU-based training.
- **Training diagnostics:** Overfitting, underfitting, and learning curves.
- **Experiment tracking:** Connecting PyTorch training to MLflow.

---

## AI602: Transformers, NLP & Foundation Models

- **Traditional NLP recap:** Tokenization, TF-IDF, and embeddings.
- **Word embeddings:** Word2Vec and semantic representations.
- **Attention mechanism:** Self-attention and multi-head attention.
- **Transformer architecture:** Encoder and decoder blocks.
- **Positional encoding.**
- **BERT:** Encoder-based language models.
- **GPT:** Decoder-based generative models.
- **Tokenization:** BPE, WordPiece, and modern tokenizer concepts.
- **Hugging Face Transformers.**
- **Hugging Face Datasets.**
- **Pretrained models:** Loading and using foundation models.
- **Fine-tuning:** Domain-specific adaptation.
- **PEFT:** Parameter-efficient fine-tuning.
- **LoRA and QLoRA:** Concepts and practical applications.
- **Inference:** Running transformer models efficiently.
- **Model evaluation:** Evaluating NLP and generative tasks.

---

## AI603: LLM Application Engineering

- **LLM APIs:** Working with hosted language-model APIs.
- **Prompt construction:** System, developer, and user instructions.
- **Prompt templates:** Reusable structured prompts.
- **Structured outputs:** JSON schemas and validated responses.
- **Function / tool calling:** Connecting models with application functions.
- **Context windows:** Managing limited model context.
- **Tokenization:** Token budgets and cost awareness.
- **Streaming:** Real-time token responses.
- **Model selection:** Cost, latency, and quality trade-offs.
- **Retries and fallbacks:** Resilient LLM applications.
- **Guardrails:** Input / output validation.
- **Caching:** Reducing repeated inference.
- **Observability:** Logging requests, latency, and failures.
- **Evaluation:** Moving beyond subjective prompt testing.
- **Security:** Prompt injection and data-leakage fundamentals.

### Term 3 Outcome

```text
Classical ML
     +
Deep Learning
     +
Transformers
     +
LLMs
     ↓
Modern AI Engineering Foundation
```

---

# Fourth Term — RAG, Agents, Cloud AI & Production Capstone

## AI604: Retrieval-Augmented Generation & Vector Search

- **RAG architecture:** Retriever + context + generator.
- **Document ingestion:** PDFs, HTML, structured documents, and text.
- **Document parsing:** Extracting useful content.
- **Chunking strategies:** Fixed, semantic, and structure-aware chunking.
- **Embeddings:** Dense vector representations.
- **Vector similarity:** Cosine similarity, dot product, and distance metrics.
- **Vector databases:** Architecture and indexing concepts.
- **pgvector:** PostgreSQL-based vector storage.
- **FAISS:** Local similarity search.
- **Qdrant / Weaviate / Pinecone concepts.**
- **Metadata filtering.**
- **Semantic search.**
- **BM25:** Lexical retrieval.
- **Hybrid search:** Combining keyword and semantic search.
- **Reranking:** Cross-encoder and other reranking techniques.
- **Query transformation.**
- **Context construction.**
- **Citations and source grounding.**
- **RAG evaluation:** Retrieval and generation metrics.
- **Hallucination analysis.**
- **Caching and performance optimization.**

---

## AI605: AI Agents & Agentic Systems

- **Agent architecture:** Model + state + tools + control logic.
- **Function calling:** Connecting agents to APIs and business logic.
- **Tool design:** Safe interfaces for databases, APIs, and services.
- **Structured outputs:** Reliable agent communication.
- **State management:** Managing workflow state.
- **Conversation memory:** Short-term and persistent memory concepts.
- **Planning:** Breaking complex goals into executable steps.
- **Agent workflows:** Deterministic versus autonomous approaches.
- **Human-in-the-loop systems:** Approval gates.
- **Multi-agent architectures:** When they help and when they do not.
- **Error recovery:** Retry, fallback, and timeout strategies.
- **Agent evaluation:** Task success, reliability, and cost.
- **Tracing:** Observing agent execution.
- **Security:** Permissions, tool restrictions, and prompt injection.
- **Production considerations:** Latency, scalability, and reliability.

---

## CLD601: Cloud AI Infrastructure & Kubernetes

Choose **one primary cloud** rather than trying to master AWS, Azure, and GCP simultaneously.

### Cloud Foundations

- Compute.
- Object storage.
- Managed PostgreSQL.
- Redis.
- Container registries.
- Identity and access management.
- Secrets management.
- Logging and monitoring.
- Serverless computing.
- Managed AI services.
- Networking fundamentals.

### Kubernetes Fundamentals

- Pods.
- Deployments.
- Services.
- ConfigMaps.
- Secrets.
- Ingress.
- Persistent volumes.
- Horizontal scaling.
- Health probes.
- Resource limits.
- Helm fundamentals.

### Infrastructure as Code

- Terraform fundamentals.
- Reusable infrastructure definitions.
- Environment separation.
- Automated deployment.

---

## CAP601: Production AI Engineering Capstone

The final project should be a complete production-oriented AI system rather than another notebook-only ML project.

### Recommended Capstone

**Industrial AI Knowledge & Analytics Platform**

```text
                         Users
                           │
                           ▼
                      Web / UI
                           │
                           ▼
                       FastAPI
                           │
             ┌─────────────┼──────────────┐
             │             │              │
             ▼             ▼              ▼
          AI Agent       RAG         ML Prediction
             │             │              │
             │       Hybrid Search        │
             │             │              │
             ▼             ▼              ▼
          Tools        pgvector        ML Model
             │             │              │
             └─────────────┼──────────────┘
                           │
                      PostgreSQL
                           │
                         Redis
                           │
                           ▼
                         MLflow
                           │
                           ▼
                         Docker
                           │
                           ▼
                         CI/CD
                           │
                           ▼
                      Cloud / K8s
                           │
                           ▼
                       Monitoring
```

### Capstone Requirements

- Clean Python architecture.
- Git / GitHub.
- SQL / PostgreSQL.
- ML model.
- MLflow tracking.
- REST API.
- Authentication.
- Docker.
- Redis.
- LLM integration.
- RAG.
- Vector database.
- Tool calling.
- Automated tests.
- CI/CD.
- Cloud deployment.
- Logging.
- Monitoring.
- Technical documentation.
- Architecture diagram.
- Professional README.
- Working demo.

---

# Integration with Nile University

| Nile University Provides | Complementary Track Provides |
|---|---|
| Probability | Production Python |
| Statistics | Software engineering |
| Regression | Data structures & algorithms |
| Classical Machine Learning | SQL / PostgreSQL |
| Clustering | Data engineering |
| PCA / ICA | Backend engineering |
| Neural networks | FastAPI |
| Spark | Redis |
| Hadoop | Docker |
| Big Data analytics | CI/CD |
| Data Science methodology | MLflow / MLOps |
| Applied Data Science project | Cloud engineering |
| Deep Learning introduction | PyTorch depth |
| Text analytics | Transformers |
| — | LLM engineering |
| — | Vector databases |
| — | RAG |
| — | AI Agents |
| — | Kubernetes |
| — | Production AI capstone |

---

# Recommended Progression

```text
                         TERM 4
               Production AI Engineering
         RAG • Agents • Cloud • Kubernetes
                         ▲
                         │
                         TERM 3
                Modern Artificial Intelligence
          PyTorch • Transformers • LLMs
                         ▲
                         │
                         TERM 2
                   ML Engineering
       Backend • Docker • CI/CD • MLOps
                         ▲
                         │
                         TERM 1
             Software / Data Engineering
        Python • SQL • PostgreSQL • Git
                         ▲
                         │
        ┌────────────────┴────────────────┐
        │                                 │
                  NILE UNIVERSITY
        Statistics • ML • Spark • Hadoop
             Big Data • Data Science
```

---

# Topics Deliberately Deprioritized

A full frontend-development specialization is not necessary for the primary target roles.

Do **not** spend a full term mastering:

- React
- Angular
- Vue
- Redux
- Advanced UI / UX
- SEO
- Complex frontend optimization

Instead, learn enough frontend capability to expose AI projects through:

- Streamlit
- Gradio
- Basic HTML / CSS / JavaScript
- Basic React if required later

The priority should remain:

```text
FastAPI
+
PostgreSQL
+
Docker
+
MLflow
+
PyTorch
+
Transformers
+
RAG
+
Cloud
```

---

# Final 4-Term Structure

```text
TERM 1
Software & Data Engineering
├── SWE601 Python Software Engineering for AI
├── DAT601 SQL, PostgreSQL & Data Modeling
└── DAT602 Applied Data Engineering with Python

TERM 2
ML Engineering & Production
├── SWE602 Backend Engineering for AI Systems
├── DEV601 Docker, Linux & CI/CD
└── MLO601 MLOps Foundations

TERM 3
Modern AI
├── AI601 Advanced Deep Learning with PyTorch
├── AI602 Transformers, NLP & Foundation Models
└── AI603 LLM Application Engineering

TERM 4
Production Generative AI
├── AI604 Retrieval-Augmented Generation & Vector Search
├── AI605 AI Agents & Agentic Systems
├── CLD601 Cloud AI Infrastructure & Kubernetes
└── CAP601 Production AI Engineering Capstone
```

---

# Target Profile After Completion

After combining the Nile University diploma with this complementary curriculum, the intended profile is:

```text
Data Science Foundation
        +
Machine Learning
        +
Big Data / Spark
        +
Software Engineering
        +
Backend Development
        +
MLOps
        +
Deep Learning
        +
Transformers
        +
LLM Engineering
        +
RAG
        +
Agents
        +
Cloud / Kubernetes
        ↓
Data Scientist / ML Engineer / AI Engineer / GenAI Engineer
```

The curriculum is designed so that Nile University remains the academic Data Science and Big Data foundation, while the four complementary terms build the software, deployment, MLOps, and modern AI engineering capabilities needed for production-oriented roles.
