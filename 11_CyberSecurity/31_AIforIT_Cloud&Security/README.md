# Phase 31 — AI for IT, Cloud & Security

Phase 31 intentionally comes **after** the technical domains that AI is assisting.

> **Domain knowledge first. AI assistance second.**

A model can generate commands, architectures, Terraform, scripts, incident summaries, and security recommendations very quickly. The engineer still needs enough domain knowledge to detect when those outputs are incorrect, stale, incomplete, unsafe, or over-privileged.

---

# Study Order

```text
121 Introduction to Generative AI and Prompt Engineering
        ↓
122 AI for System Administrators
        ↓
123 AI for Cloud Engineers
        ↓
124 Generative AI for DevOps Engineers
        ↓
125 AI Security
```

The broader dependency is:

```text
Programming
Networking
Linux / Windows
Cloud
Containers / Kubernetes
IaC
DevOps
Cybersecurity
Application Security
SOC / IR
Cloud Security
DevSecOps
        ↓
AI-assisted engineering
        ↓
AI Security
```

---

# Phase Mental Model

```text
DOMAIN EXPERTISE
      ↓
AI ASSISTANCE
      ↓
AUTHORITATIVE CONTEXT / RAG
      ↓
DETERMINISTIC VALIDATION
      ↓
LEAST-PRIVILEGE TOOLING
      ↓
HUMAN / POLICY APPROVAL
      ↓
CONTROLLED EXECUTION
      ↓
AUDIT
      ↓
EVALUATION / IMPROVEMENT
```

Do not invert this into:

```text
AI generated it
      ↓
therefore execute it
```

---

# Course 121 — Introduction to Generative AI and Prompt Engineering

This course builds the AI foundation needed by every later course.

Core concepts include:

```text
LLMs
tokens
tokenization
context windows
embeddings
transformers
attention
inference
sampling
prompt hierarchy
prompt engineering
structured outputs
tool calling
agents
memory
RAG
vector search
reranking
groundedness
hallucination
evaluation
prompt injection
data governance
fine-tuning awareness
multimodal models
```

## Core LLM Mental Model

```text
Prompt
  +
Context
  +
Model
      ↓
Token-by-token generation
      ↓
Model output
      ↓
Validation
```

The model output is probabilistic.

Therefore:

```text
fluent
≠
correct
```

## RAG

```text
Documents
   ↓
parse
   ↓
chunk
   ↓
embed
   ↓
index
   ↓
query
   ↓
authorization / metadata filter
   ↓
retrieve
   ↓
rerank
   ↓
LLM context
   ↓
grounded answer
```

RAG does not automatically solve hallucination. It creates additional systems that also need to work correctly:

```text
document quality
chunking
embedding quality
retrieval
authorization
reranking
context assembly
citation
model synthesis
```

## Prompt Template Pattern

```text
TASK
What exactly should the model do?

AUTHORITATIVE CONTEXT
What information is it allowed to rely on?

UNTRUSTED DATA
What content must remain data rather than authority?

CONSTRAINTS
What is prohibited or required?

OUTPUT
What exact format/schema?

VALIDATION
How will correctness be checked?
```

---

# Course 122 — AI for System Administrators

The objective is not to create an AI with unrestricted root or Domain Admin access.

The objective is:

```text
System evidence
     ↓
AI analysis
     ↓
administrator verification
     ↓
safe proposed action
     ↓
approval
     ↓
execution
     ↓
post-change verification
```

## Recommended Permission Model

```text
Read system inventory        → allowed
Read logs                    → allowed
Explain configuration        → allowed
Draft command                → allowed
Execute low-risk lab change  → controlled approval
Privileged change            → explicit approval
Delete/reboot/disable        → deny by default
```

## AI-Assisted Troubleshooting

```text
symptom
  ↓
collect raw evidence
  ↓
AI generates hypotheses
  ↓
test hypotheses
  ↓
identify root cause
  ↓
draft fix
  ↓
rollback plan
  ↓
change
  ↓
validation
```

Use AI to increase reasoning speed, not to replace operational discipline.

---

# Course 123 — AI for Cloud Engineers

Cloud AI must be grounded in:

```text
actual provider
actual account/subscription/project
actual region
actual service/API version
actual resource inventory
actual IAM
actual routes/network policy
actual provider documentation
```

## Safe IaC Workflow

```text
Architecture requirement
        ↓
AI drafts Terraform / Bicep / CloudFormation
        ↓
format / validate
        ↓
plan / what-if
        ↓
security / policy checks
        ↓
engineer review
        ↓
approval
        ↓
scoped deployment identity
        ↓
apply
        ↓
audit / verify / rollback
```

High-risk AI errors include:

```text
invented cloud services
wrong region support
deprecated APIs
wrong SKU assumptions
over-permissive IAM
accidental destroy/replace
incorrect network reachability
secret leakage
incorrect pricing assumptions
```

---

# Course 124 — Generative AI for DevOps Engineers

AI coding agents become much more reliable when the repository itself is engineered for them.

## Agent-Friendly Repository

```text
Repository
├─ clear specifications
├─ architecture documentation
├─ repository instructions
├─ deterministic environment
├─ one-command lint
├─ one-command test
├─ one-command build
├─ strong typing / static analysis
├─ security checks
└─ machine-readable errors
```

## Agent Workflow

```text
Specification
   ↓
Plan
   ↓
Task
   ↓
Isolated workspace
   ↓
Code change
   ↓
Tests
   ↓
Static / security checks
   ↓
Diff review
   ↓
Pull Request
   ↓
Approval
   ↓
Merge
```

Repository content itself can be untrusted:

```text
README
Issue
PR comment
dependency documentation
test output
CI log
generated file
```

A coding agent must not let repository text override the agent's tool policy or expose secrets.

---

# Course 125 — AI Security

This is the most security-intensive course in the phase.

The system to secure is not only:

```text
LLM
```

It is:

```text
User
 ↓
AI Gateway
 ↓
Model Endpoint
 ├─ Prompt / context
 ├─ RAG
 │   ├─ document ingestion
 │   ├─ embeddings
 │   ├─ vector DB
 │   └─ retrieval
 ├─ Memory
 └─ Tool Router
     ├─ shell
     ├─ cloud
     ├─ database
     ├─ source code
     └─ SaaS APIs
```

Every arrow creates a trust boundary.

## Prompt Injection Security Model

```text
Trusted instructions
       ↓
User request
       ↓
Retrieved document / webpage / ticket / email
       ↓
Model
       ↓
Tool request
```

The critical principle is:

> **Untrusted content cannot grant itself authority.**

Tool permissions must therefore live outside prompt text.

```text
Model asks for action
        ↓
Policy layer
  ├─ tool allowlist
  ├─ resource scope
  ├─ argument constraints
  ├─ spend/rate limits
  ├─ user authorization
  └─ approval requirements
        ↓
short-lived credential
        ↓
external system
```

## Secure RAG

```text
User identity
    ↓
tenant / document authorization
    ↓
retrieval metadata filter
    ↓
vector / hybrid search
    ↓
approved chunks only
    ↓
LLM
```

Do **not** retrieve everything and ask the model to enforce access control afterward.

Authorization belongs before retrieval reaches the context.

## AI Incident Evidence

For an AI-agent incident preserve:

```text
user identity
prompt
system/developer instructions
model deployment/version
retrieved document IDs/chunks
memory entries
tool request
tool arguments
tool result
credential identity
approval decision
timestamps
policy result
model output
```

This evidence can be as important as traditional endpoint/network logs.

---

# Framework Awareness

The phase uses these as supporting frameworks:

```text
NIST AI Risk Management Framework
NIST Generative AI Profile
OWASP GenAI / LLM security guidance
MITRE ATLAS

plus existing:
NIST CSF
Zero Trust
Application Security
Cloud Security
DevSecOps
GRC
Incident Response
```

Frameworks should organize thinking and control coverage; they do not replace architecture-specific threat modeling.

---

# Recommended Lab Architecture

```text
                         Engineer
                            │
                            ↓
                    AI Application
                            │
                ┌───────────┼───────────┐
                │           │           │
              Model        RAG        Tools
                │           │           │
                │       Vector DB       ├─ Linux lab
                │       Documents       ├─ Windows lab
                │                       ├─ Cloud sandbox
                │                       └─ Git test repo
                │
                ↓
            Audit Store
                │
                ↓
         Evaluation Harness
```

Tool targets should be:

```text
synthetic
lab
read-only
or explicitly authorized
```

---

# Recommended Repository Structure

```text
Phase_31_AI/
├── 121_GenAI/
│   ├── prompts/
│   ├── rag/
│   ├── evaluation/
│   └── injection_tests/
├── 122_SysAdmin/
│   ├── linux/
│   ├── windows/
│   ├── runbooks/
│   └── safe_tools/
├── 123_Cloud/
│   ├── architecture/
│   ├── terraform/
│   ├── inventory/
│   └── plan_reviews/
├── 124_DevOps/
│   ├── specs/
│   ├── repo_instructions/
│   ├── agent_tasks/
│   ├── ci/
│   ├── tests/
│   └── agent_evals/
├── 125_AI_Security/
│   ├── threat_models/
│   ├── rag_auth/
│   ├── tool_policy/
│   ├── memory/
│   ├── prompt_injection/
│   ├── incident_response/
│   └── security_metrics/
└── README.md
```

---

# Combined Phase 31 Capstone

Build a controlled **AI Operations and Security Assistant** capable of helping with:

```text
Linux diagnostics
Windows diagnostics
cloud inventory
Terraform review
repository analysis
CI failure analysis
security-log summarization
```

Architecture:

```text
User identity
     ↓
AI gateway
     ↓
policy enforcement
     ↓
model
 ┌───┴─────────────────────┐
 │                         │
RAG                     Tool Router
 │                    ┌────┼─────────────┐
authorized docs        │    │             │
                     OS RO Cloud RO     Git
                                      Test env change
                                           ↓
                                      approval required
```

## Required Deliverables

1. AI architecture
2. AI data-flow diagram
3. threat model
4. instruction hierarchy
5. RAG authorization
6. two-tenant isolation test
7. tool allowlist
8. tool argument policy
9. short-lived tool identity
10. read-only default
11. state-changing approval flow
12. structured output schemas
13. direct prompt-injection tests
14. indirect prompt-injection tests
15. hallucination evaluation
16. cloud/provider freshness validation
17. coding-agent repository guardrails
18. AI audit-log schema
19. AI incident-response runbook
20. kill/disable procedure
21. AI risk register
22. security metrics
23. retest report
24. executive summary

---

# Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 121 — GenAI & Prompt Engineering | 149 | 80 | 149 | 16,420 |
| 122 — AI for System Administrators | 139 | 80 | 139 | 15,734 |
| 123 — AI for Cloud Engineers | 126 | 80 | 126 | 14,441 |
| 124 — GenAI for DevOps Engineers | 140 | 80 | 140 | 15,639 |
| 125 — AI Security | 204 | 80 | 204 | 21,241 |
| **TOTAL** | **758** | **400** | **758** | **83,475** |

---

# Completion Criteria

Do not leave Phase 31 until you can:

- explain why LLM output is probabilistic;
- build prompt templates and evaluation sets;
- create a RAG architecture with authorization;
- explain direct and indirect prompt injection;
- safely use AI for Linux/Windows troubleshooting;
- verify AI-generated Bash and PowerShell;
- use AI to review cloud IaC through plan/what-if;
- design least-privilege cloud agents;
- build agent-friendly repositories;
- require tests/security checks for AI-generated code;
- treat repository/log/document content as untrusted;
- threat-model RAG, memory, tools, agents, models, and data;
- enforce tenant isolation before retrieval;
- constrain tools outside the model;
- use short-lived agent credentials;
- preserve AI incident evidence;
- build prompt-injection and output-validation tests;
- create AI-security metrics and risk governance.

---

# Next Phase

```text
Phase 32 — Professional Skills
126 Communication Essentials for Professionals
127 High Impact Presentations
128 Progressive Teamwork
129 Professional Demeanor
130 Job Seeking Skills
131 Freelancing Basics
```
