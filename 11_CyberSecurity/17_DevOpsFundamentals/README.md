# Phase 17 — DevOps Fundamentals

Phase 17 develops the complete software-delivery operating model from DevOps culture through Continuous Integration, Continuous Delivery, end-to-end CI/CD automation, and automated testing.

## Courses

```text
65. DevOps Concepts and Toolchain
66. Continuous Integration
67. Continuous Delivery
68. CI/CD Automation, Integration and Testing
69. Unit and Automated Testing
```

## Recommended Order

```text
65. DevOps Concepts and Toolchain
            ↓
66. Continuous Integration
            ↓
67. Continuous Delivery
            ↓
68. CI/CD Automation, Integration and Testing
            ↓
69. Unit and Automated Testing
```

## Phase Goal

By the end of Phase 17, you should be able to:

- Explain DevOps as a socio-technical operating model rather than a collection of tools.
- Analyze software delivery using systems thinking, value-stream mapping, flow, feedback, queues, WIP, and batch size.
- Explain CALMS, Lean, Agile, SRE, Platform Engineering, DevSecOps, and GitOps relationships.
- Design Git and pull-request workflows for frequent safe integration.
- Design production-quality Continuous Integration pipelines.
- Design runners/agents, trust zones, caches, artifacts, matrices, DAGs, merge queues, and reusable workflows.
- Integrate unit, integration, contract, API, UI, performance, and security testing into CI.
- Build trusted immutable artifacts using SBOM, provenance, scanning, and signing.
- Design Continuous Delivery with build-once-deploy-many promotion.
- Use rolling, blue/green, canary, feature flags, and progressive-delivery strategies.
- Design backward-compatible database and API release workflows.
- Integrate Terraform, Kubernetes, OpenShift, Helm, Kustomize, and GitOps into delivery automation.
- Use OIDC, workload identity, secret managers, least privilege, protected environments, and policy as code.
- Design ephemeral integration/preview environments.
- Build a complete CI/CD automation graph from commit to runtime verification.
- Design maintainable unit and automated testing strategies.
- Use fixtures, parameterization, dependency injection, test doubles, property testing, mutation testing, and coverage appropriately.
- Diagnose and eliminate flaky tests.
- Design API, contract, integration, UI, load, security, and production-safe synthetic tests.
- Measure CI/CD using queue time, execution time, lead time, deployment success, change failure, recovery time, and internal SLOs.
- Design CI/CD platform observability, incident response, runbooks, and disaster recovery.

## Learning Progression

```text
DevOps Culture
      ↓
Systems Thinking
Flow / Feedback
      ↓
Git
Pull Requests
      ↓
Continuous Integration
      ↓
Build
Test
Security
      ↓
Trusted Artifact
      ↓
Continuous Delivery
      ↓
Environment Promotion
      ↓
Deployment Strategies
      ↓
Terraform / Kubernetes / OpenShift / GitOps
      ↓
Automated Verification
      ↓
Unit + Integration + Contract + API + E2E Testing
      ↓
Observability
      ↓
Incident Learning
      ↓
Continuous Improvement
```

## Core Delivery Model

```text
Requirement
   ↓
Git
   ↓
Pull Request
   ↓
CI
├─ Format
├─ Lint
├─ Build
├─ Unit Tests
├─ Security Checks
└─ Package
   ↓
Artifact
├─ Version
├─ Digest
├─ SBOM
├─ Provenance
└─ Signature
   ↓
Integration Environment
   ↓
Automated Tests
   ↓
Stage
   ↓
Canary / Blue-Green / Rolling
   ↓
Production
   ↓
Metrics / Logs / Traces / Synthetics
   ↓
Feedback
```

## Folder Structure

```text
Phase_17_DevOps_Fundamentals/
│
├── README.md
├── 65_DevOps_Concepts_and_Toolchain.md
├── 66_Continuous_Integration.md
├── 67_Continuous_Delivery.md
├── 68_CI_CD_Automation_Integration_and_Testing.md
└── 69_Unit_and_Automated_Testing.md
```

## Capstone Outcome

After all five courses, you should be able to design a production delivery platform containing:

```text
Git Platform
CI/CD Platform
Ephemeral Runners
Reusable Pipeline Templates
Artifact Repository
Container Registry
SBOM / Provenance / Signing
Automated Test Platform
Terraform
Kubernetes / OpenShift
GitOps
Secrets / OIDC
Policy as Code
Progressive Delivery
Observability
Incident Management
Platform SLOs
Disaster Recovery
```

## Next Phase

```text
Phase 18 — Backend & Cloud Application Development

70. Backend Development Fundamentals
71. Node.js
72. Web Services and APIs
73. REST API Development
74. Message Queuing
75. Microservices Architecture
76. Enterprise Application Architecture and Integration
```
