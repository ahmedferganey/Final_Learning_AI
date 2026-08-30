# 64. Terraform Remote State Management

> Phase 16 — Infrastructure as Code

Terraform state is one of the most important operational assets in an Infrastructure as Code platform. This course moves beyond the basic definition of `terraform.tfstate` and builds a production operating model for remote state, locking, collaboration, security, migration, state partitioning, cross-state data sharing, backups, disaster recovery, HCP Terraform, and state incident response.

The core mental model is:

```text
Terraform Configuration
        |
        v
Logical Resource Address
        |
        v
Terraform State
        |
        v
Provider Resource Identity
        |
        v
Actual Infrastructure
```

A production state platform must solve:

```text
durability
encryption
locking
concurrency
identity
authorization
versioning
audit
backup
recovery
migration
team collaboration
```

---

# Current Terraform Baseline

```text
Terraform stable baseline: 1.15.x
Latest stable patch verified: 1.15.8
```

Important current backend facts used in this course:

```text
S3 backend:
  native S3 lockfile supported through use_lockfile
  DynamoDB-based locking is deprecated

AzureRM backend:
  supports state locking and consistency checking using Azure Blob native capabilities

GCS backend:
  supports state locking
  HashiCorp strongly recommends enabling Object Versioning for recovery

HCP Terraform:
  each workspace has separate state
  stores historical state versions
  serializes state-changing remote runs
```

HashiCorp currently recommends HCP Terraform's built-in `cloud` integration instead of the older `remote` backend for modern HCP Terraform workflows.

---

## 1. Topic Title

**Terraform Remote State Management**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain Terraform state internals and resource identity.
- Explain why remote state is required for team environments.
- Explain state locking and write concurrency.
- Safely diagnose and recover failed locks.
- Explain state lineage, serial/version progression, and state snapshots conceptually.
- Configure backends without embedding credentials.
- Explain partial backend configuration.
- Bootstrap state infrastructure.
- Migrate state between local and remote backends safely.
- Migrate between remote backends.
- Configure production AWS S3 state with native S3 locking.
- Explain why DynamoDB state locking is now deprecated for the S3 backend.
- Configure Azure Blob remote state conceptually.
- Configure GCS remote state conceptually.
- Understand HCP Terraform state and run locking.
- Compare object-storage backends with HCP Terraform.
- Design state sharding and ownership boundaries.
- Separate development, staging, and production state.
- Explain Terraform CLI workspace state behavior.
- Explain HCP Terraform workspace state behavior.
- Use state commands safely.
- Use `terraform state list`, `show`, `mv`, and `rm`.
- Use `terraform state pull` and understand the risk of `push`.
- Use configuration-driven `moved`, `removed`, and `import` blocks as safer normal workflows.
- Understand `terraform force-unlock`.
- Recover from state corruption and accidental deletion.
- Use backend object versioning for recovery.
- Secure state with IAM and encryption.
- Design state access roles for humans and CI.
- Explain state-sensitive-data risks.
- Safely share outputs between Terraform configurations.
- Explain why `terraform_remote_state` grants access to the full state snapshot.
- Use safer output-sharing alternatives.
- Understand `tfe_outputs` for HCP Terraform.
- Handle cross-stack dependencies without excessive coupling.
- Design remote-state CI/CD workflows.
- Diagnose concurrent apply problems.
- Diagnose stale state and unexpected drift.
- Diagnose failed state migrations.
- Design multi-account/multi-cloud state platforms.
- Define state RPO/RTO.
- Perform state disaster-recovery drills.
- Build a production-grade Terraform state platform.

---

## 3. Prerequisites

Required:

```text
62. Infrastructure as Code Fundamentals
63. Terraform
Git
Cloud IAM
Object storage concepts
Encryption/KMS basics
CI/CD fundamentals
```

Recommended:

```text
AWS S3 and IAM
Azure Blob Storage and Entra identity
Google Cloud Storage and IAM
HCP Terraform fundamentals
```

All destructive state labs must use disposable infrastructure or an isolated copy of state.

Never practice `state push`, force unlock, or backend migration against production without a tested recovery procedure.

---

## 4. Core Concepts Explanation

# Part 1 — State as Resource Mapping

### Concept

Terraform state maps logical configuration addresses to provider-managed physical resource identities. That mapping lets Terraform know that `module.network.aws_vpc.main` corresponds to one specific remote VPC rather than needing to create a new one.

### Example / Operational Reference

```hcl
terraform state list
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State as Resource Mapping** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 2 — State Is Not the Real Infrastructure

### Concept

Deleting a state file does not normally delete the cloud resources. It deletes Terraform's management knowledge. The resources remain, while the next plan may try to create duplicates or lose track of ownership.

### Example / Operational Reference

```hcl
terraform state pull > state-backup.json
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Is Not the Real Infrastructure** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 3 — State Snapshot

### Concept

A state snapshot records managed resource instances, provider associations, dependency-related metadata, outputs, and known attributes at a point in time.

### Example / Operational Reference

```hcl
terraform show
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Snapshot** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 4 — State Serial Concept

### Concept

Terraform state snapshots advance as state-changing operations occur. Backend/version systems use version information to prevent stale writers and support history.

### Example / Operational Reference

```hcl
Treat newer state as authoritative unless performing a controlled recovery
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Serial Concept** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 5 — State Lineage Concept

### Concept

Terraform tracks state lineage so unrelated state histories are not casually combined. Replacing a state file with an unrelated one can create severe ownership errors.

### Example / Operational Reference

```hcl
Never overwrite state merely because filenames match
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Lineage Concept** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 6 — Local State

### Concept

The default local backend stores state on the local filesystem. It is appropriate for labs but weak for shared production because collaboration, locking, audit, and recovery depend on one machine.

### Example / Operational Reference

```hcl
terraform.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Local State** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 7 — Local Backup File

### Concept

Local Terraform operations may create backup state files during state-changing operations. They help with local recovery but are not a production backup architecture.

### Example / Operational Reference

```hcl
terraform.tfstate.backup
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Local Backup File** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 8 — Remote State

### Concept

Remote state stores the state snapshot in a shared backend such as object storage, HCP Terraform, or another supported backend.

### Example / Operational Reference

```hcl
terraform { backend "..." { ... } }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Remote State** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 9 — Why Teams Need Remote State

### Concept

Remote state creates one shared authoritative location so CI and authorized engineers do not each carry a different copy of production ownership metadata.

### Example / Operational Reference

```hcl
Central state + locking + IAM
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Why Teams Need Remote State** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 10 — Backend

### Concept

A Terraform backend determines where state is stored and can provide additional capabilities such as locking. Backend initialization occurs before normal resource evaluation.

### Example / Operational Reference

```hcl
terraform { backend "s3" { ... } }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 11 — Backend Is Not a Provider

### Concept

A backend stores Terraform state; a provider manages external infrastructure resources. You can use the AWS provider while storing state in HCP Terraform, Azure Blob, or another backend.

### Example / Operational Reference

```hcl
Backend lifecycle and provider lifecycle are separate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Is Not a Provider** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 12 — Backend Initialization

### Concept

Terraform initializes the configured backend during `terraform init`, before planning normal resources.

### Example / Operational Reference

```hcl
terraform init
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Initialization** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 13 — Backend Configuration Is Early

### Concept

Backend configuration cannot depend on ordinary resource values that only exist after provider evaluation. Backend infrastructure must already exist or be bootstrapped separately.

### Example / Operational Reference

```hcl
Do not try to create the state bucket in the same state that needs that bucket before init
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Configuration Is Early** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 14 — Partial Backend Configuration

### Concept

Keep non-sensitive stable backend information in code and supply sensitive/environment-specific settings during initialization through supported mechanisms.

### Example / Operational Reference

```hcl
terraform init -backend-config=backend.hcl
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Partial Backend Configuration** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 15 — Backend Credentials Warning

### Concept

HashiCorp warns against hardcoding backend credentials or supplying sensitive values in ways that are copied into `.terraform` metadata or plan artifacts. Prefer environment/workload identity.

### Example / Operational Reference

```hcl
Use OIDC / managed identity / ADC / role assumption
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Credentials Warning** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 16 — Backend Bootstrap

### Concept

A common architecture uses a small bootstrap stack or one-time controlled process to create state storage, locking, encryption keys, and CI identity before normal Terraform stacks use them.

### Example / Operational Reference

```hcl
bootstrap/ → state backend → live stacks
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Bootstrap** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 17 — Bootstrap State

### Concept

The bootstrap configuration itself needs a lifecycle strategy. Some organizations keep its state local and encrypted under strict custody; others use a separate foundation backend.

### Example / Operational Reference

```hcl
Document who owns the backend of the backend
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Bootstrap State** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 18 — Backend Migration

### Concept

Changing the backend requires reinitialization and potentially copying state. Treat migration as a state database migration with backups and a change window.

### Example / Operational Reference

```hcl
terraform init -migrate-state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Migration** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 19 — Migration Precheck

### Concept

Before moving state: stop all applies, create a backup, verify source state, verify destination permissions/locking/versioning, and record current resource count/lineage.

### Example / Operational Reference

```hcl
freeze → backup → validate destination → migrate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Migration Precheck** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 20 — Migration Verification

### Concept

After migration, run a fresh plan and confirm the old backend is no longer receiving writes. A no-op plan is the desired result.

### Example / Operational Reference

```hcl
terraform plan
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Migration Verification** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 21 — State Locking

### Concept

If the backend supports locking, Terraform automatically locks state for operations that can write it. The lock prevents simultaneous writers from corrupting or racing state changes.

### Example / Operational Reference

```hcl
terraform plan/apply uses backend locking where supported
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Locking** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 22 — Lock Failure

### Concept

If Terraform cannot acquire a required lock, it stops rather than continuing with unsafe concurrent writes.

### Example / Operational Reference

```hcl
Do not solve by immediately adding -lock=false
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Lock Failure** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 23 — -lock=false Risk

### Concept

Disabling locking can allow concurrent state mutation. It should be reserved for exceptional read/recovery scenarios where the concurrency risk is explicitly understood.

### Example / Operational Reference

```hcl
terraform plan -lock=false  # generally avoid
```

### Why it matters

State is Terraform's ownership database. A mistake involving **-lock=false Risk** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 24 — Lock Timeout

### Concept

Automation can wait for a busy lock rather than failing instantly. Tune waiting according to deployment duration and CI concurrency design.

### Example / Operational Reference

```hcl
terraform plan -lock-timeout=5m
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Lock Timeout** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 25 — force-unlock

### Concept

Terraform provides `force-unlock` for a lock left behind after automatic unlocking fails. It requires the unique lock ID.

### Example / Operational Reference

```hcl
terraform force-unlock LOCK_ID
```

### Why it matters

State is Terraform's ownership database. A mistake involving **force-unlock** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 26 — Force Unlock Safety

### Concept

Force-unlock only after proving the original writer is gone. Unlocking a state actively being modified creates multiple writers and can corrupt the state workflow.

### Example / Operational Reference

```hcl
verify CI/user/process → force-unlock → fresh plan
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Force Unlock Safety** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 27 — CI Concurrency

### Concept

Backend locking is necessary but CI should also ensure one state-changing pipeline per state. This reduces queued conflicts and stale plan problems.

### Example / Operational Reference

```hcl
CI concurrency group keyed by state/workspace
```

### Why it matters

State is Terraform's ownership database. A mistake involving **CI Concurrency** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 28 — Stale Plan

### Concept

Even with locking, a plan produced before another apply can become outdated. Saved-plan apply must ensure state has not changed incompatibly.

### Example / Operational Reference

```hcl
plan → approval → apply without unrelated writes
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Stale Plan** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 29 — State Versioning

### Concept

Object storage or HCP Terraform should retain historical state versions so accidental deletion/corruption can be recovered.

### Example / Operational Reference

```hcl
Enable bucket/blob/object versioning where supported
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Versioning** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 30 — State RPO

### Concept

RPO asks how much state history can be lost. With durable versioned remote state, the target is commonly near-zero state-write loss.

### Example / Operational Reference

```hcl
RPO example: latest committed state write
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State RPO** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 31 — State RTO

### Concept

RTO asks how long until Terraform can safely manage infrastructure again after state/backend failure.

### Example / Operational Reference

```hcl
RTO example: restore state platform within 30 minutes
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State RTO** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 32 — State Security

### Concept

State should be classified as sensitive infrastructure data because it can contain resource IDs, topology, addresses, and provider-returned sensitive attributes.

### Example / Operational Reference

```hcl
Restrict read as well as write access
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Security** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 33 — Encryption at Rest

### Concept

Use backend/platform encryption. Customer-managed KMS can add key-control requirements, but losing/deleting the key can make state unrecoverable.

### Example / Operational Reference

```hcl
KMS key lifecycle must outlive encrypted state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Encryption at Rest** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 34 — Encryption in Transit

### Concept

Backend traffic should use TLS and authenticated endpoints. Never expose state service over untrusted plaintext transport.

### Example / Operational Reference

```hcl
HTTPS/TLS
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Encryption in Transit** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 35 — State IAM

### Concept

Separate state permissions: read, write, delete/version restore, lock operations, and backend administration. Most users do not need every permission.

### Example / Operational Reference

```hcl
Developer ≠ CI Apply ≠ State Admin
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State IAM** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 36 — State Read Is Privileged

### Concept

A user who can read state may be able to see sensitive values even if normal Terraform CLI output labels them sensitive.

### Example / Operational Reference

```hcl
Sensitive output hiding is not a state-access boundary
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Read Is Privileged** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 37 — State Write Is Highly Privileged

### Concept

State write access can change Terraform's understanding of ownership and therefore influence future destructive operations.

### Example / Operational Reference

```hcl
Protect state write like infrastructure-admin capability
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Write Is Highly Privileged** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 38 — State Delete Protection

### Concept

Use backend versioning/retention and IAM to make accidental permanent deletion difficult.

### Example / Operational Reference

```hcl
Deny permanent delete except break-glass
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Delete Protection** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 39 — State Audit Logging

### Concept

Enable backend access logs/cloud audit logs so reads, writes, deletes, KMS usage, and policy changes can be investigated.

### Example / Operational Reference

```hcl
Audit state access independently from Terraform run logs
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Audit Logging** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 40 — S3 Backend

### Concept

The S3 backend stores state as an S3 object identified by bucket and key. The bucket must exist before the backend can use it.

### Example / Operational Reference

```hcl
backend "s3" { bucket = "tf-state-prod" key = "network/prod.tfstate" region = "us-east-1" }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 41 — S3 Native Locking

### Concept

Current Terraform supports native S3 lockfile-based state locking using `use_lockfile = true`. This avoids needing DynamoDB solely for new S3 state locking designs.

### Example / Operational Reference

```hcl
use_lockfile = true
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Native Locking** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 42 — DynamoDB Locking Deprecation

### Concept

HashiCorp currently marks DynamoDB-based S3 locking as deprecated and states it will be removed in a future minor version. Existing environments should plan migration toward native S3 locking.

### Example / Operational Reference

```hcl
Use S3 lockfile; DynamoDB only for compatibility during migration where required
```

### Why it matters

State is Terraform's ownership database. A mistake involving **DynamoDB Locking Deprecation** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 43 — S3 Versioning

### Concept

Enable S3 bucket versioning so previous state objects and lock-related recovery information can be recovered after accidental state overwrite/deletion.

### Example / Operational Reference

```hcl
S3 bucket versioning = Enabled
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Versioning** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 44 — S3 Encryption

### Concept

Use S3 server-side encryption and appropriate KMS controls according to organization requirements. State confidentiality depends on both storage and KMS IAM.

### Example / Operational Reference

```hcl
SSE / KMS
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Encryption** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 45 — S3 IAM Separation

### Concept

State users need only the object/key operations required by Terraform. Backend administrators who change bucket/KMS policy should be a smaller group.

### Example / Operational Reference

```hcl
Prefix-scoped IAM
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 IAM Separation** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 46 — S3 State Key Design

### Concept

Organize keys by environment and stack so unrelated state files have distinct ownership and blast radius.

### Example / Operational Reference

```hcl
network/prod/terraform.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 State Key Design** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 47 — S3 Bucket Centralization

### Concept

A centralized state bucket can simplify governance, but permissions must isolate prefixes and a bucket outage has wide blast radius.

### Example / Operational Reference

```hcl
Central bucket + per-state prefix IAM
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Bucket Centralization** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 48 — S3 Per-Account Backend

### Concept

Separate state buckets per environment/account improve blast-radius isolation but require more bootstrap/governance.

### Example / Operational Reference

```hcl
prod account state separate from dev
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Per-Account Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 49 — S3 Cross-Account

### Concept

Cross-account state access should use role assumption and narrowly scoped bucket/KMS policies rather than copying permanent credentials.

### Example / Operational Reference

```hcl
CI role → state role → S3/KMS
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Cross-Account** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 50 — S3 Lock Incident

### Concept

For a stuck native S3 lock, prove no Terraform writer remains before any manual recovery. Preserve the lock/state objects and logs for incident evidence.

### Example / Operational Reference

```hcl
stop writers → inspect → supported unlock/recovery
```

### Why it matters

State is Terraform's ownership database. A mistake involving **S3 Lock Incident** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 51 — AzureRM Backend

### Concept

The `azurerm` backend stores state as a blob in a Storage Account container and supports native state locking and consistency checking.

### Example / Operational Reference

```hcl
backend "azurerm" { resource_group_name = "rg-state" storage_account_name = "tfstate..." container_name = "tfstate" key = "prod.tfstate" }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **AzureRM Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 52 — Azure Blob Locking

### Concept

AzureRM uses Azure Blob native capabilities for locking/consistency, so no separate external locking database is normally required.

### Example / Operational Reference

```hcl
One blob lease/locking mechanism per state operation
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Azure Blob Locking** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 53 — Azure Authentication

### Concept

Prefer Microsoft Entra workload identity, managed identity, or other short-lived supported identity instead of embedding storage keys.

### Example / Operational Reference

```hcl
OIDC / Managed Identity
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Azure Authentication** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 54 — Azure Storage Security

### Concept

Restrict network access, require TLS, enable appropriate encryption, logging, soft-delete/versioning features according to platform design.

### Example / Operational Reference

```hcl
Private endpoint where architecture requires
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Azure Storage Security** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 55 — Azure State RBAC

### Concept

Grant data-plane Blob permissions required for state to the Terraform execution identity rather than broad subscription owner.

### Example / Operational Reference

```hcl
Least privilege at storage/container scope
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Azure State RBAC** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 56 — Azure State Key

### Concept

The backend `key` identifies the state blob. Use predictable environment/stack naming without collisions.

### Example / Operational Reference

```hcl
platform/prod.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Azure State Key** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 57 — Azure Recovery

### Concept

Use Azure Blob versioning/soft delete/backup controls as appropriate, then validate restored state against live infrastructure before resuming writes.

### Example / Operational Reference

```hcl
restore → plan → verify
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Azure Recovery** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 58 — GCS Backend

### Concept

The GCS backend stores state as objects under a configurable prefix in a pre-existing Cloud Storage bucket.

### Example / Operational Reference

```hcl
backend "gcs" { bucket = "tf-state-prod" prefix = "network/prod" }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 59 — GCS State Locking

### Concept

The current GCS backend supports state locking.

### Example / Operational Reference

```hcl
Terraform uses backend-supported locking automatically for writes
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS State Locking** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 60 — GCS Object Versioning

### Concept

HashiCorp strongly recommends enabling GCS Object Versioning so state can be recovered from accidental deletion or human error.

### Example / Operational Reference

```hcl
Object Versioning = enabled
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS Object Versioning** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 61 — GCS Authentication

### Concept

Use Application Default Credentials, service-account impersonation, or workload identity federation according to execution environment. Avoid long-lived service-account key files.

### Example / Operational Reference

```hcl
ADC / impersonation / WIF
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS Authentication** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 62 — GCS IAM

### Concept

Limit the execution identity to the specific state bucket/prefix and required object permissions. Backend administrators remain separate.

### Example / Operational Reference

```hcl
Least privilege Cloud Storage access
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS IAM** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 63 — GCS KMS

### Concept

Customer-managed encryption keys add governance but key deletion can make state unavailable. Key rotation/migration must be planned before removing old keys.

### Example / Operational Reference

```hcl
KMS lifecycle must account for old state versions
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS KMS** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 64 — GCS Customer-Supplied Keys

### Concept

Customer-supplied encryption-key workflows require special care during backend/key migration because the storage service does not retain the supplied key for later automatic access.

### Example / Operational Reference

```hcl
Follow current GCS backend migration procedure
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS Customer-Supplied Keys** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 65 — GCS IAM Eventual Consistency

### Concept

Changes to bucket IAM can take time to propagate, producing temporary 403 errors. Distinguish propagation from permanent authorization failure.

### Example / Operational Reference

```hcl
wait/retry after IAM change rather than expanding privileges blindly
```

### Why it matters

State is Terraform's ownership database. A mistake involving **GCS IAM Eventual Consistency** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 66 — Consul Backend

### Concept

Terraform can store state in Consul KV and the backend supports state locking when configured with required session and KV permissions.

### Example / Operational Reference

```hcl
backend "consul" { address = "consul.example.com" path = "terraform/prod" }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Consul Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 67 — Kubernetes Backend Concept

### Concept

Terraform includes a Kubernetes backend option for selected use cases. The backend lifecycle then depends on Kubernetes API availability, credentials, namespace, and the cluster itself.

### Example / Operational Reference

```hcl
Avoid circular dependency where Terraform must create the cluster that hosts its own state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Kubernetes Backend Concept** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 68 — HTTP Backend Concept

### Concept

The HTTP backend can integrate a custom state service when it implements required state and optional lock endpoints. Security and correctness become the service owner's responsibility.

### Example / Operational Reference

```hcl
HTTPS + auth + lock/unlock semantics
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HTTP Backend Concept** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 69 — Backend Selection Criteria

### Concept

Choose based on durability, locking, IAM, encryption, versioning, audit, operational maturity, execution platform, and disaster-recovery requirements.

### Example / Operational Reference

```hcl
Do not choose only because it is easiest to configure
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Selection Criteria** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 70 — Object Storage vs HCP Terraform

### Concept

Object storage gives backend primitives; HCP Terraform adds run execution, state version history, workspace RBAC, VCS integration, policies, variables, run queue, and collaboration.

### Example / Operational Reference

```hcl
Backend service vs infrastructure lifecycle platform
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Object Storage vs HCP Terraform** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 71 — HCP Terraform cloud Integration

### Concept

HashiCorp recommends the built-in `cloud` integration for modern HCP Terraform workflows instead of configuring the legacy-style `remote` backend.

### Example / Operational Reference

```hcl
terraform { cloud { organization = "example" workspaces { name = "network-prod" } } }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Terraform cloud Integration** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 72 — Legacy Remote Backend Context

### Concept

The `remote` backend still exists and can store state/execute HCP runs, but modern documentation recommends the `cloud` integration for the improved experience.

### Example / Operational Reference

```hcl
backend "remote" { ... }  # legacy-compatible pattern
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Legacy Remote Backend Context** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 73 — HCP Workspace State

### Concept

Each HCP Terraform workspace owns separate state and lifecycle for its managed resources.

### Example / Operational Reference

```hcl
workspace network-prod → one state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Workspace State** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 74 — HCP Historical State Versions

### Concept

HCP Terraform retains historical state versions and associates them with runs/VCS commits, aiding auditing and recovery.

### Example / Operational Reference

```hcl
Workspace → States
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Historical State Versions** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 75 — HCP Run Serialization

### Concept

State-changing remote runs are queued because planning a later run before the previous state change completes could produce an invalid plan.

### Example / Operational Reference

```hcl
pending → plan → policy → apply
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Run Serialization** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 76 — HCP Workspace Lock

### Concept

Workspace locking prevents normal run/state modification workflows while administrative/recovery actions occur.

### Example / Operational Reference

```hcl
Lock workspace during sensitive state maintenance
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Workspace Lock** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 77 — HCP Per-Run Tokens

### Concept

Remote runs use scoped temporary execution tokens for Terraform platform operations; cloud provider credentials should also be dynamic where possible.

### Example / Operational Reference

```hcl
Per-run identity reduces long-lived secrets
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Per-Run Tokens** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 78 — HCP Dynamic Provider Credentials

### Concept

Use HCP workload identity/dynamic credentials to obtain short-lived AWS/Azure/GCP credentials for each run.

### Example / Operational Reference

```hcl
HCP run → OIDC → cloud role
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Dynamic Provider Credentials** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 79 — HCP State Access

### Concept

Workspace/team permissions determine who can inspect or modify state and runs. State admin permissions should be rare.

### Example / Operational Reference

```hcl
Read ≠ Write ≠ Admin
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP State Access** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 80 — HCP Projects

### Concept

Projects group related workspaces and support access boundaries. They do not merge workspace states.

### Example / Operational Reference

```hcl
Organization → Project → Workspaces
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Projects** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 81 — HCP Stacks Context

### Concept

HCP Terraform Stacks can coordinate multiple component deployments while each deployment maintains isolated remote state. This is different from one giant workspace state.

### Example / Operational Reference

```hcl
Stack → components/deployments → isolated state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Stacks Context** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 82 — CLI Workspaces and Remote Backends

### Concept

Many backends store each CLI workspace under a separate key/prefix. Understand the backend's naming behavior before deleting or migrating workspaces.

### Example / Operational Reference

```hcl
terraform workspace list
```

### Why it matters

State is Terraform's ownership database. A mistake involving **CLI Workspaces and Remote Backends** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 83 — CLI Workspace Default

### Concept

Every root starts with the `default` CLI workspace. Workspace names change state selection, not configuration source.

### Example / Operational Reference

```hcl
terraform workspace show
```

### Why it matters

State is Terraform's ownership database. A mistake involving **CLI Workspace Default** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 84 — CLI Workspace Production Risk

### Concept

CLI workspaces provide state separation but not necessarily separate accounts, credentials, policy, or repositories. They are weak as the only production environment boundary.

### Example / Operational Reference

```hcl
Separate accounts + roots often clearer
```

### Why it matters

State is Terraform's ownership database. A mistake involving **CLI Workspace Production Risk** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 85 — HCP Workspace vs CLI Workspace

### Concept

An HCP workspace is a managed lifecycle/state/RBAC/run unit. A CLI workspace is a state namespace selected by the CLI. The concepts share a name but are not equivalent.

### Example / Operational Reference

```hcl
Do not design enterprise access assuming they are interchangeable
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP Workspace vs CLI Workspace** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 86 — State Sharding by Lifecycle

### Concept

Separate resources that change at different rates: network foundation, shared identity, Kubernetes platform, database, application infrastructure.

### Example / Operational Reference

```hcl
network.tfstate ≠ app.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Sharding by Lifecycle** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 87 — State Sharding by Team

### Concept

A state should generally have one clear team/automation owner. Cross-team writes increase conflict and approval complexity.

### Example / Operational Reference

```hcl
network team owns network state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Sharding by Team** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 88 — State Sharding by Blast Radius

### Concept

A state-changing operation can affect any managed object in that state. Keep high-risk foundations separate from frequently changed application resources.

### Example / Operational Reference

```hcl
IAM organization state separate from app VM state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Sharding by Blast Radius** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 89 — State Sharding by Environment

### Concept

Development and production should never share one Terraform state. They should have separate state and preferably separate cloud boundaries/identities.

### Example / Operational Reference

```hcl
dev state ≠ prod state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Sharding by Environment** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 90 — State Sharding by Region

### Concept

Multi-region systems may use one state or multiple region states. Separate states improve failure/blast isolation but require clearer cross-region contracts.

### Example / Operational Reference

```hcl
primary-region state + dr-region state
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Sharding by Region** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 91 — Over-Sharding

### Concept

Hundreds of tiny states create excessive output wiring, run ordering, repositories, and operational overhead. Shard only along meaningful ownership/lifecycle boundaries.

### Example / Operational Reference

```hcl
Balance autonomy with dependency complexity
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Over-Sharding** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 92 — Giant State Anti-Pattern

### Concept

One state controlling network, organization IAM, databases, clusters, and every application increases plan time and blast radius.

### Example / Operational Reference

```hcl
Split foundations from product stacks
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Giant State Anti-Pattern** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 93 — Cross-State Dependency

### Concept

One stack may need a stable output such as `vpc_id` or `private_subnet_ids` from another state.

### Example / Operational Reference

```hcl
Producer output → consumer input
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Cross-State Dependency** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 94 — terraform_remote_state

### Concept

The built-in `terraform_remote_state` data source reads root outputs from another backend's latest state snapshot.

### Example / Operational Reference

```hcl
data "terraform_remote_state" "network" { backend = "..." config = { ... } }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **terraform_remote_state** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 95 — Remote State Security Caveat

### Concept

Although `terraform_remote_state` exposes only root outputs to configuration, the caller must have permission to read the entire state snapshot, which may contain sensitive information.

### Example / Operational Reference

```hcl
Do not grant full state read merely to share one subnet ID
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Remote State Security Caveat** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 96 — Root Outputs Only

### Concept

`terraform_remote_state` exposes only root-module outputs, not arbitrary child-module internal outputs unless the root explicitly re-exports them.

### Example / Operational Reference

```hcl
output "vpc_id" { value = module.network.vpc_id }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Root Outputs Only** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 97 — Explicit Data Publishing

### Concept

A safer loose-coupling pattern is to publish shared data into DNS, parameter stores, object stores, Consul, cloud configuration services, or another purpose-built store with narrower access.

### Example / Operational Reference

```hcl
Network stack publishes VPC ID to parameter store
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Explicit Data Publishing** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 98 — HCP tfe_outputs

### Concept

HashiCorp recommends the `tfe_outputs` data source for HCP Terraform/Enterprise output access because it can fetch outputs without requiring full workspace-state access.

### Example / Operational Reference

```hcl
Use HCP output-access permissions instead of raw state where possible
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP tfe_outputs** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 99 — Remote State Consumer Policy

### Concept

HCP Terraform can limit which workspaces are authorized consumers of another workspace's outputs.

### Example / Operational Reference

```hcl
network-prod → approved app-prod consumers
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Remote State Consumer Policy** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 100 — Cross-State Contract Design

### Concept

Publish a small stable interface rather than dozens of internal attributes. This reduces consumer coupling to producer implementation.

### Example / Operational Reference

```hcl
vpc_id + private_subnet_ids, not every route table resource
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Cross-State Contract Design** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 101 — Cross-State Cycle

### Concept

If network state needs app output and app state needs network output, the architecture has a lifecycle cycle. Redesign ownership or introduce an external contract.

### Example / Operational Reference

```hcl
A → B → A is not independently deployable
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Cross-State Cycle** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 102 — Output Versioning

### Concept

Changing output names/types can break consumers like an API breaking change. Version module/stack interfaces and coordinate migration.

### Example / Operational Reference

```hcl
private_subnet_ids remains stable
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Output Versioning** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 103 — Sensitive Output Sharing

### Concept

Marking an output sensitive affects display but does not solve consumer authorization. Use a secret manager for secret material.

### Example / Operational Reference

```hcl
Passwords should not travel through generic remote-state outputs
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Sensitive Output Sharing** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 104 — State Commands

### Concept

Terraform CLI provides state inspection/manipulation commands for exceptional administration and refactoring. Prefer configuration-driven workflows for normal changes.

### Example / Operational Reference

```hcl
terraform state -help
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Commands** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 105 — state list

### Concept

Lists resource instance addresses in current selected state.

### Example / Operational Reference

```hcl
terraform state list
```

### Why it matters

State is Terraform's ownership database. A mistake involving **state list** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 106 — state show

### Concept

Shows one resource instance as recorded in state.

### Example / Operational Reference

```hcl
terraform state show module.network.aws_vpc.main
```

### Why it matters

State is Terraform's ownership database. A mistake involving **state show** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 107 — state mv

### Concept

Moves an address inside state. Use for controlled refactors when `moved` blocks are not suitable.

### Example / Operational Reference

```hcl
terraform state mv OLD NEW
```

### Why it matters

State is Terraform's ownership database. A mistake involving **state mv** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 108 — state rm

### Concept

Stops managing an address without deleting the real object. Configuration-driven `removed` blocks are more reviewable for many normal workflows.

### Example / Operational Reference

```hcl
terraform state rm ADDRESS
```

### Why it matters

State is Terraform's ownership database. A mistake involving **state rm** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 109 — state pull

### Concept

Downloads the latest state snapshot to stdout. This exposes sensitive state data and should be stored/protected carefully.

### Example / Operational Reference

```hcl
terraform state pull > protected-backup.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **state pull** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 110 — state push

### Concept

`state push` replaces remote state with a local state snapshot. It is a high-risk recovery tool and should not be part of normal workflows.

### Example / Operational Reference

```hcl
terraform state push recovered.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **state push** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 111 — State Push Safety

### Concept

Before pushing state: lock/freeze all writers, verify lineage/serial implications, back up current remote state, compare live resources, and have a rollback path.

### Example / Operational Reference

```hcl
Never push an arbitrary old state over active production
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Push Safety** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 112 — replace-provider

### Concept

Terraform supports state provider-source replacement workflows when migrating provider source addresses. Treat as state surgery and validate the plan afterward.

### Example / Operational Reference

```hcl
terraform state replace-provider ...
```

### Why it matters

State is Terraform's ownership database. A mistake involving **replace-provider** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 113 — Configuration-Driven moved

### Concept

Use `moved` blocks for address refactoring so the migration is version controlled and visible in plan.

### Example / Operational Reference

```hcl
moved { from = OLD to = NEW }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Configuration-Driven moved** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 114 — Configuration-Driven removed

### Concept

Use `removed` blocks to stop managing infrastructure through a reviewable plan, optionally retaining the real object.

### Example / Operational Reference

```hcl
removed { from = RESOURCE lifecycle { destroy = false } }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Configuration-Driven removed** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 115 — Configuration-Driven import

### Concept

Use import blocks for brownfield adoption so the import operation is reviewable and repeatable through normal Terraform configuration.

### Example / Operational Reference

```hcl
import { to = RESOURCE id = "remote-id" }
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Configuration-Driven import** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 116 — State Surgery Principle

### Concept

Imperative state commands are for exceptional operations. Prefer code-based lifecycle/refactoring whenever Terraform provides a declarative equivalent.

### Example / Operational Reference

```hcl
Code history beats undocumented shell history
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Surgery Principle** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 117 — State Backup Before Surgery

### Concept

Always pull/export or use backend versioning before `mv`, `rm`, `push`, provider replacement, or migration operations.

### Example / Operational Reference

```hcl
backup → change → plan → verify
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Backup Before Surgery** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 118 — No Manual JSON Editing

### Concept

Direct state JSON editing bypasses Terraform validation and can corrupt internal metadata. Use supported commands whenever possible.

### Example / Operational Reference

```hcl
Do not hand-edit terraform.tfstate
```

### Why it matters

State is Terraform's ownership database. A mistake involving **No Manual JSON Editing** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 119 — State Corruption Signals

### Concept

Symptoms include decode errors, missing instances, lineage/version conflict, impossible plan changes, or backend object damage.

### Example / Operational Reference

```hcl
Stop writes before attempting repair
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Corruption Signals** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 120 — State Corruption Recovery

### Concept

Recover from backend version history or known-good snapshot, then refresh/plan against live infrastructure and reconcile any post-snapshot changes.

### Example / Operational Reference

```hcl
restore → refresh/plan → reconcile
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Corruption Recovery** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 121 — Accidental State Deletion

### Concept

Restore the latest backend object version or HCP state version. If no backup exists, carefully import/reconstruct management mapping rather than blindly applying empty state.

### Example / Operational Reference

```hcl
Never initialize empty prod state and apply immediately
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Accidental State Deletion** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 122 — Accidental Resource Deletion

### Concept

If state still contains an object that was deleted externally, the next plan usually proposes recreation when configuration still requires it. Stateful-data recovery may require backups.

### Example / Operational Reference

```hcl
plan reveals missing remote object
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Accidental Resource Deletion** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 123 — Wrong Backend Incident

### Concept

A developer initialized against the wrong backend/environment can produce an alarming plan. Verify backend identity and state before applying.

### Example / Operational Reference

```hcl
terraform init -reconfigure only after confirming destination
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Wrong Backend Incident** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 124 — Wrong Workspace Incident

### Concept

Using the correct backend but wrong CLI/HCP workspace can target a different state. Always print context before state-changing runs.

### Example / Operational Reference

```hcl
terraform workspace show / HCP workspace name
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Wrong Workspace Incident** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 125 — Backend Credential Rotation

### Concept

Rotate backend credentials without changing state location. With workload identity, credentials are short-lived and rotation burden is reduced.

### Example / Operational Reference

```hcl
OIDC/managed identity preferred
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Credential Rotation** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 126 — KMS Key Rotation

### Concept

Key rotation must preserve the ability to decrypt all retained historical state versions or perform a documented re-encryption migration.

### Example / Operational Reference

```hcl
Do not delete old key until state versions no longer depend on it
```

### Why it matters

State is Terraform's ownership database. A mistake involving **KMS Key Rotation** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 127 — Backend Network Outage

### Concept

If state storage is unavailable, do not perform local production applies that create a divergent replacement state. Restore backend access first.

### Example / Operational Reference

```hcl
Backend availability is part of IaC control plane
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Network Outage** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 128 — Object Version Recovery

### Concept

Select the correct prior state version based on timestamps/run history and compare it with live infrastructure before marking it current.

### Example / Operational Reference

```hcl
version N-1 may miss a valid later resource creation
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Object Version Recovery** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 129 — HCP State Recovery

### Concept

Historical workspace state versions help analyze and recover from state problems. State administration should be performed with workspace locking and strict permissions.

### Example / Operational Reference

```hcl
Lock → inspect state versions → recover → plan
```

### Why it matters

State is Terraform's ownership database. A mistake involving **HCP State Recovery** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 130 — State Drift vs State Corruption

### Concept

Drift means live infrastructure changed; corruption means state data itself is invalid/inaccurate. The recovery method is different.

### Example / Operational Reference

```hcl
drift: reconcile live; corruption: recover state metadata
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Drift vs State Corruption** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 131 — State Drift vs Stale State

### Concept

A state can be stale because remote objects changed after the last refresh. A fresh plan/provider read often updates observations.

### Example / Operational Reference

```hcl
plan/refresh before state surgery
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Drift vs Stale State** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 132 — Provider Schema Migration

### Concept

Provider upgrades can change state schema internally. Downgrading or manually replacing old state can become unsafe.

### Example / Operational Reference

```hcl
Keep provider/version history with incident records
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Provider Schema Migration** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 133 — Terraform Version Compatibility

### Concept

State written by a newer Terraform can contain data older tools do not understand. Use supported Terraform version constraints and avoid forcing remote-version checks.

### Example / Operational Reference

```hcl
Pin supported Terraform in CI
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Terraform Version Compatibility** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 134 — Remote Backend Version Mismatch

### Concept

HCP Terraform protects remote operations against incompatible local/remote Terraform versions. Overriding version checks can produce unusable state and is strongly discouraged.

### Example / Operational Reference

```hcl
Align local and workspace Terraform versions
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Remote Backend Version Mismatch** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 135 — State File Size

### Concept

Very large states slow refresh/plan and increase blast radius. State sharding and avoiding unnecessary giant generated objects can improve operability.

### Example / Operational Reference

```hcl
Measure managed resource count and plan duration
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State File Size** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 136 — Managed Resource Count

### Concept

HCP Terraform tracks resources based on state. State size and managed-resource count affect both operations and platform usage/cost considerations.

### Example / Operational Reference

```hcl
One count/for_each instance is a managed instance
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Managed Resource Count** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 137 — State and Secrets Architecture

### Concept

Prefer provider features such as write-only/ephemeral values or runtime secret retrieval so secret material is not persisted unnecessarily.

### Example / Operational Reference

```hcl
Secret manager + workload identity
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State and Secrets Architecture** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 138 — State Redaction Myth

### Concept

Marking a Terraform value sensitive does not redact it from the state file if Terraform needs to persist it.

### Example / Operational Reference

```hcl
Protect the backend
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Redaction Myth** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 139 — Plan and State Access

### Concept

Users who can download plans/state may learn internal architecture even without cloud-console access. Apply information classification to IaC artifacts.

### Example / Operational Reference

```hcl
State/plan logs should not be public CI artifacts
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Plan and State Access** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 140 — Backup Retention

### Concept

Define how many state versions and how long they are retained. Retention should cover discovery time for accidental changes while meeting security/compliance requirements.

### Example / Operational Reference

```hcl
Example: 90-day state version retention
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backup Retention** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 141 — Immutable/WORM Retention

### Concept

Highly regulated environments may use retention/immutability controls for state backups. Ensure Terraform can still write the active object while backups remain protected.

### Example / Operational Reference

```hcl
Separate active state from immutable backup archive if needed
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Immutable/WORM Retention** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 142 — Cross-Region Backend DR

### Concept

State backend failure should not become permanent loss. Object replication or HCP service design can support recovery, but test how failover changes endpoint/consistency.

### Example / Operational Reference

```hcl
Do not run two active writers in two regions
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Cross-Region Backend DR** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 143 — Active-Passive State Backend

### Concept

For custom state platforms, active-passive is simpler than active-active because a single authoritative writer location avoids split-brain state.

### Example / Operational Reference

```hcl
One active state authority
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Active-Passive State Backend** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 144 — Backend Monitoring

### Concept

Monitor availability, failed auth, object writes, KMS errors, lock contention, version deletion, and unusual reads.

### Example / Operational Reference

```hcl
State backend is part of production control plane
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Monitoring** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 145 — Lock Contention Metric

### Concept

Frequent lock contention can signal too-large state, slow applies, or too many teams sharing one ownership boundary.

### Example / Operational Reference

```hcl
Shard by lifecycle/owner instead of disabling locks
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Lock Contention Metric** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 146 — Plan Queue Time

### Concept

Long HCP run queues can indicate one workspace/state is managing too much frequently changed infrastructure.

### Example / Operational Reference

```hcl
Review workspace boundary
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Plan Queue Time** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 147 — State Access Review

### Concept

Periodically review human/team/CI permissions to production state and remove stale users/tokens.

### Example / Operational Reference

```hcl
Quarterly or policy-defined access review
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Access Review** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 148 — State Incident Evidence

### Concept

Preserve backend audit logs, CI run IDs, lock IDs, state-version IDs, Terraform/provider versions, and the exact plan before changing anything.

### Example / Operational Reference

```hcl
Evidence first, surgery second
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Incident Evidence** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 149 — State Incident Freeze

### Concept

During state incidents, suspend automation and human applies to create a stable recovery point.

### Example / Operational Reference

```hcl
CI environment lock + HCP workspace lock
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Incident Freeze** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 150 — State Recovery Verification

### Concept

After recovery run a fresh plan and inspect every create/update/replace/destroy. Then test service health before reopening normal changes.

### Example / Operational Reference

```hcl
Recovered state + no-op/expected plan
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Recovery Verification** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 151 — Backend Migration Local to Remote

### Concept

Typical first migration: initialize local configuration, create remote backend separately, back up local state, configure backend, migrate state, verify remote object and no-op plan.

### Example / Operational Reference

```hcl
local → remote
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Migration Local to Remote** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 152 — Backend Migration Remote to Remote

### Concept

Move one authoritative state from backend A to backend B while writers are frozen. Never leave both backends active for different teams.

### Example / Operational Reference

```hcl
freeze → backup A → migrate to B → disable A writes
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Migration Remote to Remote** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 153 — Backend Key Rename

### Concept

Changing an S3 key/GCS prefix/Azure blob key changes where Terraform finds state. Treat it as migration rather than simply editing a string.

### Example / Operational Reference

```hcl
Old key and new key must not become two active states
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Key Rename** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 154 — Workspace Rename

### Concept

Renaming HCP/remote workspace can affect automation, VCS, state consumers, variables, run triggers, and API references. Review dependencies before rename.

### Example / Operational Reference

```hcl
Workspace name is part of platform contract
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Workspace Rename** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 155 — State Split

### Concept

Splitting one state requires moving selected resources to a new state without destroying them and then rewiring outputs/dependencies.

### Example / Operational Reference

```hcl
backup → new backend → move/import → plan both states
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Split** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 156 — State Merge

### Concept

Merging states increases blast radius and requires careful address/provider collision checks. It is less common than splitting and should be planned like a database migration.

### Example / Operational Reference

```hcl
No duplicate addresses or dual ownership
```

### Why it matters

State is Terraform's ownership database. A mistake involving **State Merge** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 157 — Move Resource Between States

### Concept

Configuration-driven removed/import workflows can move ownership between state files while preserving the physical resource. Use staged plans and freeze both states.

### Example / Operational Reference

```hcl
source removes management → destination imports
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Move Resource Between States** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 158 — Cross-State Migration Window

### Concept

During transfer, no other stack should modify the resource. Document the exact handoff point so ownership is never simultaneous or absent unintentionally.

### Example / Operational Reference

```hcl
State A owner → change freeze → State B owner
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Cross-State Migration Window** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 159 — Backend Bootstrap Repository

### Concept

Keep bootstrap code small and heavily protected because a backend outage can block every downstream stack.

### Example / Operational Reference

```hcl
bootstrap/state-backend
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend Bootstrap Repository** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 160 — Backend as Tier-0 Infrastructure

### Concept

State storage, KMS, CI identity, and Git are control-plane dependencies. Classify them as critical infrastructure rather than ordinary app storage.

### Example / Operational Reference

```hcl
Tier-0 IaC control plane
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Backend as Tier-0 Infrastructure** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


# Part 161 — Production State Architecture

### Concept

A strong design combines durable remote storage, locking, versioning, encryption, least privilege, audit, separate environment states, CI serialization, and recovery drills.

### Example / Operational Reference

```hcl
Durability + Concurrency + Security + DR
```

### Why it matters

State is Terraform's ownership database. A mistake involving **Production State Architecture** can cause duplicate infrastructure, unexpected replacement, destructive plans, cross-team conflicts, loss of management ownership, or exposure of sensitive information.

### Production rule

Treat every state-changing operation as a database change: identify the correct backend/workspace, stop conflicting writers, preserve a recovery copy or state version, perform the smallest supported operation, then run a fresh plan against live infrastructure and verify the result before reopening normal applies.


---

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Inspect Local State
Create disposable local Terraform resources. Inspect `terraform.tfstate`, `state list`, `state show`, and `terraform show`. Do not edit the JSON.

### Lab 2 — State Pull
Use `terraform state pull` and store the output in a protected file. Compare it with human-readable `terraform show`.

### Lab 3 — State Sensitivity
Create a sensitive variable/output in a disposable configuration and observe the difference between CLI redaction and raw state representation.

### Lab 4 — Simulated State Loss
Copy local state away, remove it from the working directory, run a plan, and observe why Terraform loses ownership. Restore the copy before applying.

### Lab 5 — State Locking Tabletop
Draw two concurrent applies and explain the race that locking prevents.

### Lab 6 — Lock Timeout
In a disposable backend that supports locking, experiment with a second Terraform operation and a safe `-lock-timeout`.

### Lab 7 — Force-Unlock Runbook
Do not force-unlock an active writer. Write the exact evidence you would require before running `terraform force-unlock`.

### Lab 8 — Backend Bootstrap Design
Design a bootstrap stack for:
```text
state storage
encryption key
locking
CI role
audit logs
```

### Lab 9 — Partial Backend Configuration
Create a backend config that keeps bucket/container/key in code while credentials come from environment/workload identity.

### Lab 10 — Local-to-Remote Migration Tabletop
Write precheck, backup, `init -migrate-state`, verification, and rollback steps.

### Lab 11 — S3 Backend Architecture
Design:
```text
versioned S3 bucket
native use_lockfile
KMS
TLS
prefix IAM
audit
```

### Lab 12 — S3 Native Locking
In an authorized AWS sandbox, configure `use_lockfile = true` and verify normal plan/apply locking behavior.

### Lab 13 — DynamoDB Migration Plan
For a hypothetical old S3 + DynamoDB lock environment, design migration to native S3 locking without creating two active writers.

### Lab 14 — S3 Version Recovery
Using a disposable bucket, create multiple state object versions and practice selecting a previous version without touching production.

### Lab 15 — S3 IAM
Design three IAM roles:
```text
plan reader
apply writer
state administrator
```
Minimize permissions.

### Lab 16 — AzureRM Backend Design
Design Storage Account/container/key, Blob locking, Entra workload identity, private access, versioning/soft-delete, and audit.

### Lab 17 — Azure Identity
Create a permission matrix for a CI managed identity versus state administrators.

### Lab 18 — Azure Recovery Tabletop
Design recovery from accidental state blob deletion using native storage recovery features.

### Lab 19 — GCS Backend
Design bucket/prefix, Object Versioning, IAM, WIF/service-account impersonation, encryption, and audit.

### Lab 20 — GCS Object Versioning
In an authorized GCP sandbox, inspect object generations/versions for disposable state.

### Lab 21 — GCS KMS Tabletop
Design KMS rotation while preserving access to historical encrypted state.

### Lab 22 — Backend Comparison
Create a table comparing:
```text
S3
AzureRM
GCS
HCP Terraform
Consul
```
for locking, version history, identity, audit, execution features, and operational complexity.

### Lab 23 — HCP Workspace Architecture
Create a conceptual organization:
```text
Project: Foundation
  network-prod
  identity-prod

Project: Applications
  orders-prod
  analytics-prod
```
Each workspace owns one state.

### Lab 24 — HCP Run Queue
Diagram two concurrent VCS changes to one workspace and explain why state-changing runs serialize.

### Lab 25 — HCP State Versions
In an HCP lab if available, inspect state history and associate a state version with a run/commit.

### Lab 26 — HCP Workspace Lock Tabletop
Define when an administrator should lock a workspace for recovery and who may unlock it.

### Lab 27 — CLI Workspaces
Create `dev` and `test` CLI workspaces on a disposable remote backend and inspect how separate state objects/keys are stored.

### Lab 28 — CLI vs HCP Workspace
Write a comparison explaining identity, state, RBAC, run execution, and naming differences.

### Lab 29 — State Sharding
Split an architecture into:
```text
network
security
platform
database
application
```
states. Explain each boundary.

### Lab 30 — Over-Sharding Review
Given 70 tiny states for one application, consolidate them into meaningful lifecycle boundaries.

### Lab 31 — Giant State Review
Given one state managing 2,000 unrelated resources across 10 teams, propose a staged split.

### Lab 32 — terraform_remote_state
Create two disposable local/remote configurations where one reads a root output from another. Document the full-state-read security implication.

### Lab 33 — Safer Output Publishing
Replace a hypothetical remote-state dependency with:
```text
DNS
parameter store
object/config store
```
and compare permissions.

### Lab 34 — HCP Output Sharing
Design use of `tfe_outputs`/workspace output access instead of granting full raw state access.

### Lab 35 — Cross-State Cycle
Given:
```text
network needs app IP
app needs subnet ID
```
redesign the ownership to eliminate the cycle.

### Lab 36 — state mv
In disposable local state, rename a resource using `state mv`. Then repeat the lesson using a `moved` block and compare auditability.

### Lab 37 — removed Block
Stop managing a disposable resource without destroying it. Verify the resource remains and the new state no longer owns it.

### Lab 38 — Import to New State
Move ownership of a disposable object from one state to another using a controlled remove/import sequence.

### Lab 39 — State Split Game
Take one disposable state with six resources and split three into another backend/state without physical recreation.

### Lab 40 — Corrupt State Recovery Tabletop
Given a malformed/latest state object and previous good object version, design freeze, restore, refresh/plan, and verification.

### Lab 41 — Wrong Backend Incident
Model a developer initializing prod code against dev state. Identify the warning signs before any apply.

### Lab 42 — Wrong Workspace Incident
Create an operational preflight command checklist that always prints:
```text
Git commit
Terraform version
backend/workspace
cloud identity
environment
```

### Lab 43 — State Access Audit
Create a quarterly review checklist for:
```text
state readers
state writers
KMS users
CI identities
break-glass admins
```

### Lab 44 — State Monitoring
Define alerts for:
```text
state delete
versioning disabled
KMS deny
unusual state download
lock contention
backend outage
```

### Lab 45 — Full State Disaster-Recovery Drill
Simulate:
```text
backend state unavailable
latest snapshot damaged
live infrastructure still running
```
Restore from a known-good state version, reconcile later live changes, and prove a safe plan before resuming automation.

---

## 6. Mini Project

# Mini Project — Enterprise Terraform State Platform

Design and document remote-state architecture for an organization using:

```text
AWS
Azure
GCP
HCP Terraform
```

## Required State Boundaries

At minimum:

```text
bootstrap
organization / identity
network
security
Kubernetes / OpenShift platform
database
application infrastructure
```

For every state specify:

```text
owner
environment
backend
lock mechanism
encryption
KMS ownership
reader roles
writer identity
versioning
audit
RPO
RTO
recovery runbook
```

## AWS State Design

Use current architecture:

```text
S3
+
Object Versioning
+
Encryption/KMS
+
use_lockfile = true
+
prefix-scoped IAM
```

Do not design a new solution around DynamoDB locking because current Terraform marks DynamoDB-based S3 locking deprecated.

## Azure State Design

Use:

```text
Azure Blob Storage
native state locking/consistency
Entra workload identity
encryption
version/soft-delete recovery
restricted network access
```

## GCP State Design

Use:

```text
GCS
state locking
Object Versioning
workload identity / impersonation
KMS where required
audit logging
```

## HCP Terraform Design

Use:

```text
Organization
Projects
Workspaces
remote runs
state history
workspace RBAC
dynamic provider credentials
remote-state consumer controls
```

## Cross-State Data

Define which outputs are shared through:

```text
HCP outputs / tfe_outputs
DNS
parameter/config store
data sources
```

Avoid giving application teams full raw network/security state unless necessary.

## CI/CD

Pipeline requirements:

```text
one writer per state
fresh plan
lock timeout
saved plan
approval
apply
post-apply validation
state/run artifact audit
```

## Disaster Recovery

Document:

```text
state corruption
state deletion
backend outage
KMS failure
stuck lock
wrong workspace
wrong backend
state migration failure
state split
accidental state push
```

## Required Documentation

```text
STATE_ARCHITECTURE.md
BACKEND_BOOTSTRAP.md
AWS_STATE.md
AZURE_STATE.md
GCP_STATE.md
HCP_TERRAFORM_STATE.md
ACCESS_CONTROL.md
CROSS_STATE_DATA.md
STATE_MIGRATION.md
STATE_DR.md
STATE_MONITORING.md
```

## Required Runbooks

```text
RUNBOOK_FORCE_UNLOCK.md
RUNBOOK_STATE_RECOVERY.md
RUNBOOK_BACKEND_OUTAGE.md
RUNBOOK_STATE_MIGRATION.md
RUNBOOK_STATE_SPLIT.md
RUNBOOK_WRONG_WORKSPACE.md
RUNBOOK_WRONG_BACKEND.md
RUNBOOK_KMS_FAILURE.md
RUNBOOK_ACCIDENTAL_DELETE.md
RUNBOOK_STATE_ACCESS_INCIDENT.md
```

---

## 7. Recommended Resources

This material is self-contained for the learning path. For production implementation, verify exact backend behavior in the current official HashiCorp Terraform documentation for:

```text
Backend configuration
S3 backend
AzureRM backend
GCS backend
State locking
Remote state storage
terraform_remote_state
State commands
HCP Terraform workspace state
HCP Terraform remote operations
```

Current course baseline:

```text
Terraform 1.15.8
```

---

## 8. Certification Relevance

The current Terraform Associate (004) explicitly covers:

```text
local backend
state locking
remote state through backend configuration
resource drift
state inspection
import
HCP Terraform collaboration
```

This course goes substantially deeper into production architecture and prepares for the state/collaboration portions of the advanced Terraform Authoring and Operations Professional path.

---

## 9. Common Mistakes & Best Practices

- Do not store production state only on a laptop.
- Do not disable locking to "fix" concurrency.
- Do not force-unlock without proving the writer is gone.
- Do not hardcode backend credentials.
- Do not store secrets in backend config files.
- Enable state versioning/recovery features.
- Treat state read access as sensitive.
- Treat state write access as privileged.
- Separate dev and production state.
- Do not let two states manage one object.
- Keep state boundaries aligned with lifecycle and ownership.
- Do not create one giant enterprise state.
- Do not over-shard into hundreds of tiny mutually dependent states.
- Prefer explicit output contracts.
- Avoid raw `terraform_remote_state` when it grants excessive access.
- Prefer `tfe_outputs` in HCP Terraform where appropriate.
- Back up before state surgery.
- Prefer moved/removed/import blocks for normal refactoring.
- Treat `state push` as high-risk recovery tooling.
- Test backend migration in non-production first.
- Never delete encryption keys before retained state no longer requires them.
- Monitor backend/KMS/access changes.
- Test state recovery, not only backup creation.

---

## 10. Self-Assessment Questions (with short answers)

1. **Why does Terraform need state?** To map logical addresses to real resources and retain known attributes/lifecycle information.
2. **Does deleting state delete infrastructure?** Normally no.
3. **Why remote state?** Shared durable authoritative state for teams/CI.
4. **What is a backend?** The state-storage/locking integration used by Terraform.
5. **Backend vs provider?** Backend stores state; provider manages external resources.
6. **When is backend initialized?** During `terraform init`.
7. **Can the same configuration create the backend before init?** Not in the normal direct lifecycle; bootstrap separately.
8. **State locking purpose?** Prevent concurrent writers.
9. **What happens if locking fails?** Terraform stops the write-capable operation.
10. **Should `-lock=false` be normal?** No.
11. **When use force-unlock?** Only after proving the original lock holder is gone.
12. **State RPO?** Maximum acceptable state-write loss.
13. **State RTO?** Time to restore safe Terraform management.
14. **Why encrypt state?** It can contain sensitive infrastructure information.
15. **Why is state read privileged?** Sensitive values may exist in the snapshot.
16. **Current S3 locking recommendation?** Native S3 lockfile using `use_lockfile`.
17. **DynamoDB S3 locking status?** Deprecated in current Terraform.
18. **Why enable S3 versioning?** Recover prior state object versions.
19. **AzureRM locking?** Uses Azure Blob native locking/consistency capabilities.
20. **GCS locking?** Supported by the backend.
21. **GCS recovery recommendation?** Enable Object Versioning.
22. **Best backend credential pattern?** Workload/federated/managed identity.
23. **HCP Terraform state unit?** Workspace.
24. **Does HCP store state history?** Yes, historical state versions.
25. **Why HCP run queue?** Serialize state-changing runs.
26. **Current preferred HCP integration?** Built-in `cloud` integration rather than legacy remote backend.
27. **CLI workspace vs HCP workspace?** CLI workspace selects state namespace; HCP workspace is a managed state/run/RBAC unit.
28. **State sharding goal?** Reduce blast radius and align lifecycle/ownership.
29. **Can dev and prod share one state?** They should not.
30. **Risk of giant state?** High blast radius, contention, slow runs, team coupling.
31. **Risk of too many states?** Excessive cross-state dependencies/operations.
32. **terraform_remote_state purpose?** Read root outputs from another state.
33. **Security issue with terraform_remote_state?** Reader requires access to the full snapshot.
34. **Safer HCP output option?** `tfe_outputs`.
35. **Alternative to remote state output sharing?** DNS, parameter store, object/config store, provider data sources.
36. **`state list`?** Lists managed addresses.
37. **`state show`?** Shows one state instance.
38. **`state mv`?** Moves a logical state address.
39. **`state rm`?** Stops managing without destroying the remote object.
40. **`state pull`?** Downloads current state snapshot.
41. **`state push`?** High-risk operation replacing backend state from local snapshot.
42. **Preferred normal refactor?** `moved` block.
43. **Preferred normal unmanage workflow?** `removed` block.
44. **Preferred brownfield adoption?** Configuration-driven import.
45. **Before state surgery?** Freeze writers and make/rely on a known recovery version.
46. **State corruption vs drift?** Corruption is bad state metadata; drift is live infrastructure difference.
47. **Wrong backend symptom?** Huge unexpected create/destroy plan or missing expected resources.
48. **KMS key deletion risk?** Historical/current state can become unrecoverable.
49. **Production state monitoring?** Backend availability, deletes, IAM/KMS changes, lock contention, unusual access.
50. **Safe recovery finish condition?** Fresh reviewed plan matches expected live infrastructure and normal writers can resume.

---

## Completion Checklist

- [ ] I understand Terraform state identity and snapshots.
- [ ] I understand backend initialization.
- [ ] I understand remote-state requirements.
- [ ] I understand locking and force-unlock safety.
- [ ] I understand S3 native lockfiles and DynamoDB deprecation.
- [ ] I understand AzureRM backend locking.
- [ ] I understand GCS locking and Object Versioning.
- [ ] I understand HCP Terraform state/run behavior.
- [ ] I understand CLI vs HCP workspaces.
- [ ] I can design state sharding.
- [ ] I can design state access roles.
- [ ] I understand state encryption/KMS.
- [ ] I understand state commands and state-surgery risk.
- [ ] I understand moved/removed/import workflows.
- [ ] I understand remote-state output security.
- [ ] I understand safer cross-state data sharing.
- [ ] I can migrate backends safely.
- [ ] I can split/move state ownership safely.
- [ ] I understand state RPO/RTO.
- [ ] I can design monitoring/audit for the state backend.
- [ ] I can recover from state loss/corruption conceptually.
- [ ] I completed all 45 labs.
- [ ] I completed the Enterprise Terraform State Platform capstone.
