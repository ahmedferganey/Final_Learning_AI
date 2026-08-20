# Phase 16 — Infrastructure as Code

Phase 16 moves from infrastructure concepts into production-grade declarative infrastructure engineering with Terraform.

## Courses

```text
62. Infrastructure as Code Fundamentals
63. Terraform
64. Terraform Remote State Management
```

## Recommended Order

```text
62. Infrastructure as Code Fundamentals
              ↓
63. Terraform
              ↓
64. Terraform Remote State Management
```

## Phase Goal

By the end of Phase 16, you should be able to:

- Explain declarative infrastructure, desired state, idempotency, convergence, drift, and dependency graphs.
- Design a version-controlled Infrastructure as Code operating model.
- Use Terraform safely from initialization through planning, applying, refactoring, importing, testing, and troubleshooting.
- Write strongly typed HCL using resources, data sources, variables, locals, outputs, expressions, functions, meta-arguments, and custom conditions.
- Build secure reusable Terraform modules.
- Manage provider versions and dependency lock files.
- Use multiple providers, aliases, accounts, subscriptions, projects, regions, and clusters.
- Refactor Terraform code without unnecessary resource recreation.
- Adopt existing brownfield infrastructure with import workflows.
- Use native Terraform testing and provider mocking.
- Integrate Terraform into secure CI/CD pipelines.
- Understand HCP Terraform workspaces, remote runs, state history, collaboration, and governance.
- Design production remote-state backends with locking, encryption, versioning, least privilege, audit, and disaster recovery.
- Configure state architecture for AWS S3, Azure Blob Storage, Google Cloud Storage, and HCP Terraform.
- Split state according to lifecycle, ownership, environment, and blast radius.
- Share infrastructure outputs safely without unnecessarily exposing whole state snapshots.
- Recover from state lock, state corruption, accidental deletion, backend outage, wrong workspace, and migration failures.

## Current Technical Baseline

```text
Terraform:
  Stable line used by the phase: 1.15.x
  Latest stable patch verified: 1.15.8
  Terraform 1.16 was beta when these materials were prepared

Current Terraform certification:
  HashiCorp Certified: Terraform Associate (004)
  Exam product baseline: Terraform 1.12
```

## Important Current Remote-State Notes

```text
AWS S3 backend:
  Native S3 lockfile supported using use_lockfile
  DynamoDB-based state locking is deprecated

AzureRM backend:
  Uses Azure Blob native state locking and consistency capabilities

GCS backend:
  Supports state locking
  Object Versioning is strongly recommended for state recovery

HCP Terraform:
  Workspace state is remote and versioned
  State-changing remote runs are serialized
  Modern built-in cloud integration is preferred over the older remote backend
```

## Folder Structure

```text
Phase_16_Infrastructure_as_Code/
│
├── README.md
├── 62_Infrastructure_as_Code_Fundamentals.md
├── 63_Terraform.md
└── 64_Terraform_Remote_State_Management.md
```

## Learning Progression

```text
Manual Infrastructure
        ↓
Infrastructure as Code
        ↓
Desired State / Idempotency
        ↓
Git / Review / Policy
        ↓
Terraform Core
        ↓
HCL
        ↓
Providers
        ↓
Resources / Data
        ↓
Expressions / Functions
        ↓
Modules
        ↓
Plan / Apply
        ↓
Testing
        ↓
Import / Refactoring
        ↓
Terraform State
        ↓
Remote State
        ↓
Locking / Versioning
        ↓
State Security
        ↓
CI/CD Collaboration
        ↓
Disaster Recovery
```

## Capstone Outcome

By completing all three courses, you should be able to design a production IaC platform that includes:

```text
Git
Modules
Terraform
Provider Version Management
Remote State
Locking
Short-Lived CI Identity
Policy as Code
Security Scanning
Testing
Drift Detection
Cost Governance
Multi-Environment Promotion
State Recovery
Operational Runbooks
```

## Next Phase

```text
Phase 17 — DevOps Fundamentals

65. DevOps Concepts and Toolchain
66. Continuous Integration
67. Continuous Delivery
68. CI/CD Automation, Integration and Testing
69. Unit and Automated Testing
```
