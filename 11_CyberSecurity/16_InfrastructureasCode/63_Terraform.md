# 63. Terraform

> Phase 16 — Infrastructure as Code

This course turns the Infrastructure as Code concepts from Course 62 into practical Terraform engineering. It covers Terraform CLI, HCL, providers, resources, data sources, expressions, meta-arguments, modules, state, import/refactoring, testing, cloud and Kubernetes patterns, HCP Terraform, CI/CD, security, and troubleshooting.

## Current Baseline

```text
Terraform stable line: 1.15.x
Latest stable patch verified for this course: 1.15.8
Terraform 1.16: beta at the time this course was prepared
```

HashiCorp currently identifies Terraform 1.15.8 as the latest stable release. The course therefore uses Terraform 1.15 behavior as the primary production baseline.

Current certification mapping:

```text
HashiCorp Certified: Terraform Associate (004)
Exam product baseline: Terraform 1.12
Current course baseline: Terraform 1.15
```

The course deliberately teaches newer production capabilities while retaining all concepts required by the Associate exam.

## Terraform Execution Model

```text
.tf configuration
      ↓
terraform init
      ↓
providers + modules + backend
      ↓
terraform validate
      ↓
terraform plan
      ↓
configuration + state + provider reads
      ↓
dependency graph
      ↓
execution plan
      ↓
terraform apply
      ↓
provider API calls
      ↓
real infrastructure
      ↓
updated state
```

---

## 1. Topic Title

**Terraform**

---

## 2. Learning Objectives

By the end of the course, you should be able to:

- Install and version Terraform safely.
- Explain Terraform Core, providers, modules, state, and backends.
- Write idiomatic HCL.
- Configure required Terraform and provider versions.
- Use `terraform init`, `fmt`, `validate`, `plan`, `apply`, `destroy`, `show`, `console`, `graph`, `test`, and state commands.
- Configure default and aliased providers.
- Authenticate with short-lived cloud identities.
- Create resources and query data sources.
- Use references to build dependency graphs.
- Use `count`, `for_each`, `depends_on`, and provider meta-arguments.
- Use lifecycle rules correctly.
- Write typed variables, locals, outputs, and validation.
- Use conditionals, `for` expressions, splats, dynamic blocks, and built-in functions.
- Handle `null`, unknown, sensitive, ephemeral, and write-only value concepts.
- Design reusable Terraform modules.
- Version and test modules.
- Refactor code with `moved` and `removed` blocks.
- Import brownfield infrastructure with configuration-driven imports.
- Understand current bulk search/import concepts.
- Inspect and troubleshoot Terraform state.
- Detect and reconcile drift.
- Write Terraform tests and mock providers.
- Use Terraform in CI/CD safely.
- Design AWS, Azure, GCP, Kubernetes, and OpenShift Terraform boundaries.
- Understand CLI workspaces versus HCP Terraform workspaces.
- Understand HCP Terraform remote runs, state, policies, and dynamic provider credentials.
- Troubleshoot production Terraform failures systematically.
- Build a production-grade multi-environment Terraform platform.

---

## 3. Prerequisites

Required:

```text
62. Infrastructure as Code Fundamentals
Git
Linux CLI
YAML / JSON
Cloud fundamentals
Networking
IAM basics
```

Recommended:

```text
AWS / Azure / GCP fundamentals
Kubernetes / OpenShift fundamentals
Bash
Python
```

Use only your own cloud accounts, local resources, or authorized training environments.

---

## 4. Core Concepts Explanation

# Part 1 — Terraform Core

### Concept

Terraform Core parses HCL, loads module trees, asks providers for schemas and remote object information, constructs the dependency graph, compares configuration with state, and produces an execution plan.

### Syntax / Example

```hcl
terraform version
terraform -help
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Terraform Core**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 2 — Providers

### Concept

Providers are plugins that translate Terraform resource and data-source operations into calls against external APIs. Terraform and each provider have independent release cycles.

### Syntax / Example

```hcl
terraform providers
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Providers**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 3 — Root Module

### Concept

All `.tf` files in the current working directory form one root module. File names are organizational; Terraform evaluates the configuration as one module rather than executing files in filename order.

### Syntax / Example

```hcl
terraform -chdir=live/dev validate
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Root Module**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 4 — Child Modules

### Concept

A child module is called from another module to package reusable infrastructure behavior. Child modules expose explicit variable inputs and output values.

### Syntax / Example

```hcl
module "network" {\n  source = "./modules/network"\n}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Child Modules**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 5 — terraform Block

### Concept

The `terraform` block configures Terraform behavior such as required Terraform version, required providers, backend, or HCP Terraform integration.

### Syntax / Example

```hcl
terraform {\n  required_version = "~> 1.15.0"\n}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform Block**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 6 — required_version

### Concept

Use a Terraform version constraint to prevent untested CLI versions from running the configuration. Production teams should deliberately define an upgrade window.

### Syntax / Example

```hcl
required_version = ">= 1.15.0, < 1.16.0"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **required_version**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 7 — required_providers

### Concept

Provider requirements declare source addresses and version constraints. Provider version configuration belongs here rather than in the runtime provider block.

### Syntax / Example

```hcl
required_providers {\n  aws = { source = "hashicorp/aws" }\n}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **required_providers**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 8 — Terraform Installation Verification

### Concept

Always verify the binary before using a production repository. Different Terraform versions can support different language features and workflows.

### Syntax / Example

```hcl
terraform version
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Terraform Installation Verification**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 9 — Working Directory

### Concept

Terraform stores local working metadata under `.terraform/`. The directory is recreated by `terraform init` and normally must not be committed.

### Syntax / Example

```hcl
ls -la .terraform
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Working Directory**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 10 — terraform init

### Concept

Initialization configures the backend and downloads the provider and module dependencies needed by the current root module.

### Syntax / Example

```hcl
terraform init
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform init**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 11 — init -upgrade

### Concept

Use `terraform init -upgrade` when intentionally allowing provider/module dependency selection to move to newer versions permitted by constraints.

### Syntax / Example

```hcl
terraform init -upgrade
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **init -upgrade**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 12 — init -reconfigure

### Concept

Use reconfigure when backend settings intentionally changed and Terraform must forget the previously initialized backend configuration.

### Syntax / Example

```hcl
terraform init -reconfigure
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **init -reconfigure**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 13 — .terraform.lock.hcl

### Concept

The dependency lock file records provider selections and cryptographic checksums. Commit it so developers and CI use consistent provider artifacts.

### Syntax / Example

```hcl
git add .terraform.lock.hcl
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **.terraform.lock.hcl**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 14 — Provider Locking for Multiple Platforms

### Concept

Teams with Linux CI and Windows/macOS developers can pre-populate provider checksums for multiple platforms using Terraform provider-lock workflows.

### Syntax / Example

```hcl
terraform providers lock -platform=linux_amd64 -platform=windows_amd64
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Locking for Multiple Platforms**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 15 — terraform fmt

### Concept

The formatter makes HCL style deterministic. CI should fail unformatted Terraform rather than debating whitespace in reviews.

### Syntax / Example

```hcl
terraform fmt -recursive
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform fmt**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 16 — terraform validate

### Concept

Validation checks configuration structure and internal consistency. It does not prove cloud credentials, quotas, or all runtime API operations will succeed.

### Syntax / Example

```hcl
terraform validate
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform validate**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 17 — terraform plan

### Concept

Plan refreshes/reads relevant state and provider information, constructs the graph, and calculates proposed create, update, replacement, and destroy operations.

### Syntax / Example

```hcl
terraform plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform plan**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 18 — Saved Plans

### Concept

A saved plan creates a reviewable artifact that can later be applied without recalculating a different plan.

### Syntax / Example

```hcl
terraform plan -out=tfplan\nterraform show tfplan\nterraform apply tfplan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Saved Plans**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 19 — terraform apply

### Concept

Apply executes a plan through providers and updates state as operations complete. Production pipelines should use controlled identities and post-apply verification.

### Syntax / Example

```hcl
terraform apply
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform apply**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 20 — terraform destroy

### Concept

Destroy plans removal of managed infrastructure. Production access should be protected by approvals, deletion protection, backups, and least privilege.

### Syntax / Example

```hcl
terraform destroy
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform destroy**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 21 — Auto Approval

### Concept

`-auto-approve` is appropriate only when the review and approval controls have moved elsewhere into trusted automation. It should never be used merely to bypass thinking.

### Syntax / Example

```hcl
terraform apply -auto-approve
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Auto Approval**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 22 — -chdir

### Concept

`-chdir` lets automation execute Terraform against another root-module directory without changing the shell directory.

### Syntax / Example

```hcl
terraform -chdir=live/prod plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **-chdir**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 23 — TF_DATA_DIR

### Concept

`TF_DATA_DIR` relocates Terraform working data. It is not a substitute for a remote state backend.

### Syntax / Example

```hcl
export TF_DATA_DIR=/tmp/tfdata
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **TF_DATA_DIR**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 24 — TF_LOG

### Concept

Terraform debug logging is useful for provider and protocol diagnosis, but debug logs can expose sensitive API details and should be protected.

### Syntax / Example

```hcl
TF_LOG=DEBUG terraform plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **TF_LOG**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 25 — CLI Configuration

### Concept

Terraform CLI configuration controls settings such as credentials, plugin cache, and provider installation mirrors. It is different from infrastructure `.tf` files.

### Syntax / Example

```hcl
~/.terraformrc or terraform.rc
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **CLI Configuration**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 26 — Plugin Cache

### Concept

A provider plugin cache reduces repeated downloads. Integrity must still be governed by provider source and lock-file checksums.

### Syntax / Example

```hcl
plugin_cache_dir = "$HOME/.terraform.d/plugin-cache"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Plugin Cache**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 27 — HCL Blocks

### Concept

HCL blocks have a type, optional labels, and a body. Terraform and provider schemas determine which arguments and nested blocks are valid.

### Syntax / Example

```hcl
resource "random_pet" "name" {\n  length = 2\n}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCL Blocks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 28 — HCL Arguments

### Concept

An argument assigns an expression to a schema field. Arguments are not the same as nested blocks.

### Syntax / Example

```hcl
instance_type = "t3.micro"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCL Arguments**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 29 — Nested Blocks

### Concept

Many provider resources use nested blocks for repeated or structured configuration. Follow the provider schema instead of guessing whether an object should be a map.

### Syntax / Example

```hcl
ingress {\n  from_port = 443\n  to_port = 443\n}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Nested Blocks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 30 — HCL Comments

### Concept

Comments should explain architectural intent and unusual constraints, not repeat obvious syntax.

### Syntax / Example

```hcl
# Production requires three AZs for fault tolerance
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCL Comments**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 31 — Strings

### Concept

Terraform strings can contain interpolation expressions, but direct expressions should be used when the whole value is not truly a string template.

### Syntax / Example

```hcl
name = "${var.app}-${var.environment}"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Strings**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 32 — Heredocs

### Concept

Heredocs make small multi-line configuration readable. For large scripts use external templates or machine-image/configuration-management mechanisms.

### Syntax / Example

```hcl
user_data = <<-EOT\n#!/bin/bash\necho hello\nEOT
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Heredocs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 33 — templatefile

### Concept

`templatefile` renders a separate template using explicit values. This is better than embedding a very large configuration in HCL.

### Syntax / Example

```hcl
templatefile("${path.module}/cloud-init.tftpl", { app = var.app })
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **templatefile**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 34 — Numbers and Booleans

### Concept

HCL uses native numeric and boolean types. Quoting a number changes its type and can cause provider/type errors.

### Syntax / Example

```hcl
replicas = 3\nenabled = true
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Numbers and Booleans**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 35 — Lists

### Concept

Lists are ordered collections and support positional indexing. They are useful when order is meaningful.

### Syntax / Example

```hcl
subnets = ["10.0.1.0/24", "10.0.2.0/24"]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Lists**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 36 — Sets

### Concept

Sets contain unique unordered values. They are frequently used with `for_each` where the value itself is a stable identity.

### Syntax / Example

```hcl
for_each = toset(var.names)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Sets**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 37 — Maps

### Concept

Maps are key-value collections. Stable meaningful keys are powerful for infrastructure identity.

### Syntax / Example

```hcl
tags = { Environment = "prod", Owner = "platform" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Maps**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 38 — Objects

### Concept

Objects create structured typed module interfaces and are usually clearer than unrelated parallel variables.

### Syntax / Example

```hcl
type = object({ engine = string, size = string, backup = bool })
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Objects**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 39 — Tuples

### Concept

Tuples represent fixed-position values with potentially different element types. Objects are usually clearer for business-facing module inputs.

### Syntax / Example

```hcl
type = tuple([string, number, bool])
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Tuples**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 40 — null

### Concept

`null` means absence rather than empty string, zero, or empty collection. Providers often treat null as 'do not set this argument'.

### Syntax / Example

```hcl
description = var.description != "" ? var.description : null
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **null**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 41 — Unknown Values

### Concept

Values displayed as known after apply are not errors. Terraform intentionally propagates unknown values through the graph until the provider creates or reads them.

### Syntax / Example

```hcl
(known after apply)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Unknown Values**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 42 — Sensitive Values

### Concept

The `sensitive` flag suppresses values in normal UI output, but it does not guarantee that those values are absent from state.

### Syntax / Example

```hcl
variable "password" { sensitive = true }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Sensitive Values**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 43 — Ephemeral Value Concept

### Concept

Current Terraform supports ephemeral value patterns for short-lived values that should not persist through normal state/plan flows where language/provider schemas support them.

### Syntax / Example

```hcl
Use only with current Terraform/provider support
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Ephemeral Value Concept**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 44 — Write-Only Argument Concept

### Concept

Current provider schemas may expose write-only arguments so secret material can be sent without being read back into normal state. Support is provider-specific.

### Syntax / Example

```hcl
Consult the installed provider schema
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Write-Only Argument Concept**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 45 — Provider Block

### Concept

Provider blocks configure runtime provider instances such as region or endpoint. Credentials should usually come from the provider's standard external identity chain.

### Syntax / Example

```hcl
provider "aws" { region = var.region }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Block**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 46 — Default Provider

### Concept

Resources automatically use the default unaliased provider configuration unless an alias is explicitly selected.

### Syntax / Example

```hcl
provider "aws" { region = "eu-west-1" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Default Provider**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 47 — Provider Alias

### Concept

Aliases let one configuration manage multiple accounts, subscriptions, projects, clusters, or regions without confusing identities.

### Syntax / Example

```hcl
provider "aws" { alias = "dr" region = "eu-central-1" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Alias**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 48 — Resource Provider Selection

### Concept

The `provider` meta-argument selects an aliased provider instance for a resource.

### Syntax / Example

```hcl
provider = aws.dr
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Resource Provider Selection**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 49 — Provider Authentication

### Concept

Prefer OIDC federation, managed identity, workload identity, or role assumption over static secrets in Terraform configuration.

### Syntax / Example

```hcl
AWS_PROFILE / OIDC / managed identity / workload identity
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Authentication**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 50 — Provider Version Upgrade

### Concept

Upgrade providers deliberately: change constraints, run `init -upgrade`, inspect the lock change, test, plan, and promote through environments.

### Syntax / Example

```hcl
terraform init -upgrade
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Version Upgrade**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 51 — Provider Schema Inspection

### Concept

Provider schema JSON is useful for IDEs, policy systems, code generation, and troubleshooting unfamiliar arguments.

### Syntax / Example

```hcl
terraform providers schema -json > schema.json
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Schema Inspection**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 52 — Provider Authentication Failure

### Concept

A successful `terraform validate` can still be followed by API 401/403 errors. Diagnose identity, role, account, alias, and token expiry before changing HCL.

### Syntax / Example

```hcl
terraform plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Authentication Failure**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 53 — Resource Block

### Concept

A resource block declares an object whose lifecycle this Terraform state owns.

### Syntax / Example

```hcl
resource "random_pet" "app" { length = 2 }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Resource Block**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 54 — Resource Reference

### Concept

Referencing another managed resource both passes data and usually creates an implicit dependency edge.

### Syntax / Example

```hcl
network_id = aws_vpc.main.id
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Resource Reference**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 55 — Resource Address

### Concept

Addresses identify objects in configuration and state, including indexes, keys, and module paths.

### Syntax / Example

```hcl
module.network.aws_subnet.private["az-a"]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Resource Address**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 56 — Data Source

### Concept

A data source reads existing information without taking create/destroy ownership of the remote object.

### Syntax / Example

```hcl
data "aws_caller_identity" "current" {}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Data Source**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 57 — Data Source Timing

### Concept

Terraform tries to read data during planning but can defer reads until apply when inputs are unknown.

### Syntax / Example

```hcl
data.<type>.<name>.<attribute>
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Data Source Timing**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 58 — Resource vs Data

### Concept

Use a resource for lifecycle ownership and a data source for read-only dependency on infrastructure owned elsewhere.

### Syntax / Example

```hcl
One real object should have one lifecycle owner
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Resource vs Data**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 59 — count

### Concept

`count` creates indexed instances and is best for interchangeable positional resources.

### Syntax / Example

```hcl
count = 3
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **count**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 60 — count.index

### Concept

The index can derive names, but removing an item from a list can shift indexes and cause unnecessary changes.

### Syntax / Example

```hcl
name = "node-${count.index}"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **count.index**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 61 — for_each

### Concept

`for_each` creates instances using stable map/set keys and is usually safer for named infrastructure.

### Syntax / Example

```hcl
for_each = toset(["api", "worker"])
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **for_each**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 62 — each.key and each.value

### Concept

Map-based `for_each` provides a stable key and structured value for each instance.

### Syntax / Example

```hcl
each.key\neach.value.size
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **each.key and each.value**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 63 — count vs for_each

### Concept

Choose count for truly positional homogeneous instances and for_each for stable named identity.

### Syntax / Example

```hcl
Prefer stable keys for production objects
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **count vs for_each**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 64 — depends_on

### Concept

Use explicit dependency only when a real ordering relationship cannot be represented by a normal reference. Overuse makes plans unnecessarily conservative.

### Syntax / Example

```hcl
depends_on = [aws_iam_role_policy.app]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **depends_on**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 65 — create_before_destroy

### Concept

Terraform can create a replacement before deleting the old object when provider/platform naming and quota constraints permit coexistence.

### Syntax / Example

```hcl
lifecycle { create_before_destroy = true }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **create_before_destroy**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 66 — prevent_destroy

### Concept

This lifecycle rule causes Terraform to reject planned destruction while the protected resource remains configured. It is a guardrail, not a backup.

### Syntax / Example

```hcl
lifecycle { prevent_destroy = true }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **prevent_destroy**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 67 — ignore_changes

### Concept

Ignore only attributes deliberately owned by another system. Broad ignores can conceal real drift and security changes.

### Syntax / Example

```hcl
lifecycle { ignore_changes = [tags["external"]] }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **ignore_changes**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 68 — replace_triggered_by

### Concept

A lifecycle rule can force replacement when another managed resource or attribute changes and replacement is required by architecture.

### Syntax / Example

```hcl
replace_triggered_by = [aws_launch_template.app]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **replace_triggered_by**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 69 — Preconditions

### Concept

Preconditions reject a plan/resource operation when a module assumption is false.

### Syntax / Example

```hcl
precondition { condition = var.environment != "prod" || var.backup_enabled error_message = "Production requires backup." }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Preconditions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 70 — Postconditions

### Concept

Postconditions validate guarantees after Terraform evaluates a resource or data source.

### Syntax / Example

```hcl
postcondition { condition = self.encrypted error_message = "Encryption is required." }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Postconditions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 71 — check Blocks

### Concept

`check` blocks validate infrastructure outside the normal resource lifecycle. Failed assertions report warnings and are useful for health assertions that should not behave like lifecycle preconditions.

### Syntax / Example

```hcl
check "health" { assert { condition = ... error_message = "..." } }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **check Blocks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 72 — Provisioners

### Concept

Provisioners execute arbitrary side effects that Terraform cannot model well. Prefer cloud-init, images, native APIs, or configuration-management systems.

### Syntax / Example

```hcl
Avoid local-exec/remote-exec unless there is no better integration
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provisioners**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 73 — Input Variables

### Concept

Variables form the root or module input API. Use explicit types and descriptions.

### Syntax / Example

```hcl
variable "environment" { type = string }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Input Variables**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 74 — Variable Defaults

### Concept

A default makes an input optional. Defaults should be safe and unsurprising.

### Syntax / Example

```hcl
default = false
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Variable Defaults**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 75 — Variable Validation

### Concept

Validation fails early with a domain-specific error rather than waiting for a provider API rejection.

### Syntax / Example

```hcl
condition = contains(["dev","stage","prod"], var.environment)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Variable Validation**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 76 — Optional Object Attributes

### Concept

Optional object attributes let a module accept structured configuration while providing safe defaults.

### Syntax / Example

```hcl
backup = optional(bool, true)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Optional Object Attributes**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 77 — Variable Precedence

### Concept

Terraform can receive values from defaults, tfvars, auto tfvars, environment variables, CLI flags, and HCP Terraform. Production pipelines should make the source explicit.

### Syntax / Example

```hcl
TF_VAR_environment=prod
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Variable Precedence**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 78 — tfvars

### Concept

Variable definition files are convenient but must not become a place to commit secrets.

### Syntax / Example

```hcl
terraform plan -var-file=prod.tfvars
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **tfvars**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 79 — Locals

### Concept

Locals calculate reusable values inside a module. Use them to normalize naming/tags and reduce repetition.

### Syntax / Example

```hcl
locals { prefix = "${var.app}-${var.environment}" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Locals**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 80 — Outputs

### Concept

Outputs are the public interface of a module/root configuration and can be consumed by humans, automation, or other stacks.

### Syntax / Example

```hcl
output "endpoint" { value = aws_lb.app.dns_name }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Outputs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 81 — Sensitive Outputs

### Concept

Mark sensitive outputs to reduce accidental display. Avoid exporting secrets unless a consumer genuinely requires them.

### Syntax / Example

```hcl
sensitive = true
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Sensitive Outputs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 82 — Conditional Expressions

### Concept

Ternary expressions select between two compatible values. Deeply nested ternaries are a signal to simplify module design.

### Syntax / Example

```hcl
var.environment == "prod" ? "large" : "small"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Conditional Expressions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 83 — for Expressions

### Concept

For-expressions transform collections and can produce lists, sets, or maps.

### Syntax / Example

```hcl
[for n in var.names : upper(n)]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **for Expressions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 84 — for Filtering

### Concept

A trailing `if` filters values while transforming.

### Syntax / Example

```hcl
[for s in var.subnets : s if !s.public]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **for Filtering**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 85 — Splat Expressions

### Concept

Splats provide concise attribute extraction from list-like resource collections.

### Syntax / Example

```hcl
aws_instance.app[*].id
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Splat Expressions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 86 — Dynamic Blocks

### Concept

Dynamic blocks generate repeated nested blocks. They should not replace normal `for_each` resource instances.

### Syntax / Example

```hcl
dynamic "ingress" { for_each = var.rules content { ... } }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Dynamic Blocks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 87 — merge

### Concept

Merge combines maps; later arguments win on duplicate keys. This is useful for standard plus caller tags.

### Syntax / Example

```hcl
merge(local.common_tags, var.extra_tags)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **merge**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 88 — try

### Concept

`try` evaluates expressions in order until one succeeds. Use it to normalize optional complex input, not to hide schema mistakes.

### Syntax / Example

```hcl
try(var.config.database.port, 5432)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **try**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 89 — can

### Concept

`can` returns whether an expression can be evaluated and is particularly useful in variable validation.

### Syntax / Example

```hcl
can(cidrhost(var.cidr, 1))
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **can**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 90 — coalesce

### Concept

Coalesce selects the first usable non-null/non-empty value. Prefer clear defaults when the fallback chain becomes complicated.

### Syntax / Example

```hcl
coalesce(var.name, local.default_name)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **coalesce**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 91 — concat

### Concept

Concatenate lists to build derived collections.

### Syntax / Example

```hcl
concat(var.base_subnets, var.extra_subnets)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **concat**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 92 — flatten

### Concept

Flatten is powerful when deriving a resource map from nested network/application input structures.

### Syntax / Example

```hcl
flatten(local.nested_subnets)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **flatten**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 93 — toset

### Concept

Convert a list to an unordered unique set, often before `for_each`.

### Syntax / Example

```hcl
toset(var.names)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **toset**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 94 — zipmap

### Concept

Create a map by pairing keys and values. Ensure the input lists have matching semantics.

### Syntax / Example

```hcl
zipmap(var.names, var.ids)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **zipmap**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 95 — keys and values

### Concept

Extract map keys or values. Use stable explicit keys rather than relying on incidental ordering.

### Syntax / Example

```hcl
keys(var.tags)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **keys and values**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 96 — length

### Concept

Return collection/string size. Be careful using list length with `count` if element identity should remain stable.

### Syntax / Example

```hcl
length(var.subnets)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **length**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 97 — contains

### Concept

Useful for allow-list validation such as regions and environments.

### Syntax / Example

```hcl
contains(var.allowed_regions, var.region)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **contains**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 98 — distinct

### Concept

Removes duplicate list elements when duplicate semantics are not wanted.

### Syntax / Example

```hcl
distinct(var.regions)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **distinct**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 99 — sort

### Concept

Sort normalizes ordering for deterministic outputs or comparisons.

### Syntax / Example

```hcl
sort(var.names)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **sort**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 100 — setproduct

### Concept

Produces a Cartesian product such as regions × environments. Review cardinality carefully to avoid accidental resource explosion.

### Syntax / Example

```hcl
setproduct(var.regions, var.environments)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **setproduct**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 101 — cidrsubnet

### Concept

Derive predictable subnet CIDRs from a parent range. Keep the design documented so numeric indexes have architectural meaning.

### Syntax / Example

```hcl
cidrsubnet("10.0.0.0/16", 8, 1)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **cidrsubnet**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 102 — cidrhost

### Concept

Derive an address within a CIDR. Cloud providers may reserve addresses, so arithmetic alone does not guarantee usability.

### Syntax / Example

```hcl
cidrhost("10.0.1.0/24", 10)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **cidrhost**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 103 — file

### Concept

Reads a file that already exists when Terraform evaluates configuration. Do not use it as an uncontrolled dependency on files created during apply.

### Syntax / Example

```hcl
file("${path.module}/policy.json")
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **file**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 104 — jsonencode

### Concept

Build JSON from typed HCL data rather than hand-escaping JSON strings.

### Syntax / Example

```hcl
jsonencode({ Version = "2012-10-17", Statement = [] })
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **jsonencode**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 105 — jsondecode

### Concept

Decode JSON into Terraform values. Normalize and validate external structures before using them broadly.

### Syntax / Example

```hcl
jsondecode(file("${path.module}/config.json"))
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **jsondecode**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 106 — yamlencode/yamldecode

### Concept

Useful when integrating YAML systems, but dedicated providers often give stronger type validation than constructing giant YAML documents.

### Syntax / Example

```hcl
yamlencode(local.config)
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **yamlencode/yamldecode**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 107 — path.module

### Concept

The directory of the module containing the expression. Use it for files shipped with a reusable module.

### Syntax / Example

```hcl
file("${path.module}/template.tftpl")
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **path.module**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 108 — path.root

### Concept

The root module directory. Child modules should usually not couple themselves to arbitrary root file layout.

### Syntax / Example

```hcl
path.root
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **path.root**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 109 — terraform.workspace

### Concept

The current CLI workspace name. CLI workspaces are state namespaces and are different from HCP Terraform workspaces.

### Syntax / Example

```hcl
terraform.workspace
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform.workspace**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 110 — Root Module Design

### Concept

Root modules should compose reusable modules, configure providers/backends, and express environment-specific values rather than contain every low-level implementation.

### Syntax / Example

```hcl
live/prod/main.tf
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Root Module Design**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 111 — Local Module Source

### Concept

Local sources are ideal inside a monorepo while developing modules.

### Syntax / Example

```hcl
source = "../../modules/network"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Local Module Source**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 112 — Registry Module Source

### Concept

Registry modules support explicit semantic version constraints and discoverability.

### Syntax / Example

```hcl
source = "org/network/aws"\nversion = "2.4.1"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Registry Module Source**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 113 — Git Module Source

### Concept

Git module sources can reference tags or commits. Production should avoid a mutable branch when reproducibility matters.

### Syntax / Example

```hcl
source = "git::https://example/repo.git?ref=v2.1.0"
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Git Module Source**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 114 — Module Inputs

### Concept

A module call supplies values to child variables. The input contract should be small, typed, and documented.

### Syntax / Example

```hcl
module "db" { source = "./modules/db" environment = var.environment }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module Inputs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 115 — Module Outputs

### Concept

Child outputs become references such as `module.network.private_subnet_ids`.

### Syntax / Example

```hcl
module.network.private_subnet_ids
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module Outputs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 116 — Provider Inheritance in Modules

### Concept

Default provider configurations are generally inherited by child modules. Keep environment credentials in the root.

### Syntax / Example

```hcl
Child uses caller default provider
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Inheritance in Modules**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 117 — Passing Aliased Providers to Modules

### Concept

When a child module needs a specific provider alias, pass the provider mapping explicitly.

### Syntax / Example

```hcl
providers = { aws = aws.dr }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Passing Aliased Providers to Modules**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 118 — configuration_aliases

### Concept

Reusable modules that intentionally require provider aliases declare those aliases in required provider configuration.

### Syntax / Example

```hcl
configuration_aliases = [aws.source, aws.destination]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **configuration_aliases**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 119 — Module count

### Concept

Module calls can be repeated using count, producing indexed module instances.

### Syntax / Example

```hcl
module "site" { count = 3 source = "./modules/site" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module count**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 120 — Module for_each

### Concept

Repeated modules with stable names are often better modeled with for_each.

### Syntax / Example

```hcl
for_each = var.regions
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module for_each**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 121 — Module Scope

### Concept

A child module cannot implicitly access parent variables/resources; data must cross the boundary through inputs, providers, or outputs.

### Syntax / Example

```hcl
Explicit interfaces reduce hidden coupling
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module Scope**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 122 — Module Design

### Concept

Good modules are opinionated, typed, documented, secure by default, and narrow enough to test.

### Syntax / Example

```hcl
secure_database / private_cluster / network
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module Design**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 123 — Module README

### Concept

Document requirements, providers, inputs, outputs, examples, security assumptions, and upgrade notes.

### Syntax / Example

```hcl
README.md
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module README**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 124 — Module Tests

### Concept

Reusable modules should have fast validation tests plus selected real-provider integration tests.

### Syntax / Example

```hcl
terraform test
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Module Tests**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 125 — Refactor Into a Module

### Concept

Use moved blocks when addresses change during module extraction so Terraform understands identity rather than recreating resources.

### Syntax / Example

```hcl
moved { from = aws_vpc.main to = module.network.aws_vpc.main }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Refactor Into a Module**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 126 — Terraform State

### Concept

State maps Terraform addresses to real objects and stores known attributes. Course 64 covers production remote-state architecture in depth.

### Syntax / Example

```hcl
terraform state list
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Terraform State**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 127 — state list

### Concept

Lists all managed addresses in current state.

### Syntax / Example

```hcl
terraform state list
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **state list**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 128 — state show

### Concept

Shows one state object and its known attributes.

### Syntax / Example

```hcl
terraform state show aws_instance.app
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **state show**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 129 — terraform show

### Concept

Shows current state or a saved plan in human-readable form.

### Syntax / Example

```hcl
terraform show tfplan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform show**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 130 — show -json

### Concept

Machine-readable plan/state output enables policy, security, cost, and custom CI processing. Treat it as potentially sensitive.

### Syntax / Example

```hcl
terraform show -json tfplan > plan.json
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **show -json**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 131 — state mv

### Concept

Imperatively changes an address in state. Useful in controlled refactors, though moved blocks document the change in configuration.

### Syntax / Example

```hcl
terraform state mv OLD NEW
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **state mv**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 132 — moved Block

### Concept

A moved block records previous and new addresses so Terraform plans a refactor without destroying the real resource.

### Syntax / Example

```hcl
moved { from = aws_instance.old to = aws_instance.app }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **moved Block**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 133 — Keeping moved Blocks

### Concept

Published modules often retain move history long enough for consumers that skip intermediate versions.

### Syntax / Example

```hcl
Do not delete migration history too early
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Keeping moved Blocks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 134 — removed Block

### Concept

A configuration-driven removed block can tell Terraform to stop managing a resource, optionally without destroying the physical object.

### Syntax / Example

```hcl
removed { from = aws_instance.legacy lifecycle { destroy = false } }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **removed Block**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 135 — state rm vs removed

### Concept

`state rm` is imperative; a removed block is reviewable and versioned with configuration.

### Syntax / Example

```hcl
Prefer configuration-driven removal when practical
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **state rm vs removed**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 136 — Import Block

### Concept

Configuration-driven imports place brownfield resources under Terraform ownership using a destination address and provider identity/ID.

### Syntax / Example

```hcl
import { to = aws_s3_bucket.logs id = "existing-bucket" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Import Block**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 137 — Import for_each

### Concept

Import blocks can repeat over known collections using stable keys, which is useful for controlled small-batch adoption.

### Syntax / Example

```hcl
for_each = var.existing_buckets
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Import for_each**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 138 — Import Identity

### Concept

Current import workflows can use provider-defined structured resource identities where supported rather than only one opaque ID.

### Syntax / Example

```hcl
Consult provider resource identity documentation
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Import Identity**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 139 — Generated Import Configuration

### Concept

Terraform can generate starting resource configuration for supported import workflows. Generated code still requires human review.

### Syntax / Example

```hcl
terraform plan -generate-config-out=generated.tf
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Generated Import Configuration**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 140 — Bulk Search and Import

### Concept

Current Terraform supports provider-assisted resource discovery/import workflows through query/list configuration for providers and resources that implement them.

### Syntax / Example

```hcl
.tfquery.hcl + terraform query
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Bulk Search and Import**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 141 — tfquery Files

### Concept

Bulk resource discovery uses dedicated query configuration files and should be treated as an inventory/adoption workflow, not ordinary deployment configuration.

### Syntax / Example

```hcl
*.tfquery.hcl
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **tfquery Files**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 142 — One Resource One State

### Concept

Never import a resource already managed by another state. Dual ownership creates competing writes and destructive drift.

### Syntax / Example

```hcl
Establish state ownership before import
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **One Resource One State**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 143 — Drift

### Concept

A plan after refresh can reveal cloud changes that were made outside Terraform. Investigate before blindly applying.

### Syntax / Example

```hcl
terraform plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Drift**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 144 — Refresh-Only Plan

### Concept

Refresh-only workflows can update recorded state/output information from remote objects without proposing ordinary configuration changes.

### Syntax / Example

```hcl
terraform plan -refresh-only
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Refresh-Only Plan**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 145 — Targeting Warning

### Concept

`-target` is a recovery/special-purpose tool, not a normal dependency-management strategy. Routine targeting can leave infrastructure only partially reconciled.

### Syntax / Example

```hcl
terraform plan -target=...
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Targeting Warning**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 146 — replace Option

### Concept

Explicit replacement is useful when a resource must be recreated even though configuration itself does not require replacement.

### Syntax / Example

```hcl
terraform apply -replace=RESOURCE_ADDRESS
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **replace Option**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 147 — CLI Workspaces

### Concept

CLI workspaces provide multiple state instances for the same root configuration. They are not a substitute for strong account/project separation.

### Syntax / Example

```hcl
terraform workspace list
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **CLI Workspaces**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 148 — workspace new/select

### Concept

Use CLI workspaces for compatible scenarios such as similar disposable environments. Be cautious using them for major production isolation.

### Syntax / Example

```hcl
terraform workspace new dev\nterraform workspace select dev
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **workspace new/select**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 149 — terraform console

### Concept

Interactive expression evaluator is one of the best ways to learn and debug HCL types/functions without applying infrastructure.

### Syntax / Example

```hcl
terraform console
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform console**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 150 — terraform graph

### Concept

Outputs a dependency graph in DOT format. Useful when explicit/implicit dependencies are confusing.

### Syntax / Example

```hcl
terraform graph > graph.dot
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform graph**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 151 — Output JSON

### Concept

Terraform commands often provide JSON modes for robust automation. Prefer structured JSON over parsing human CLI text.

### Syntax / Example

```hcl
terraform output -json
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Output JSON**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 152 — terraform test

### Concept

Terraform has a native test framework using `.tftest.hcl` or `.tftest.json` files with run blocks and assertions.

### Syntax / Example

```hcl
terraform test
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **terraform test**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 153 — Test Run Blocks

### Concept

A Terraform test file contains one or more run blocks that execute plan/apply-style test steps against the module under test.

### Syntax / Example

```hcl
run "valid" { command = plan }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Test Run Blocks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 154 — Test Assertions

### Concept

Assertions evaluate conditions and emit clear errors when module behavior is incorrect.

### Syntax / Example

```hcl
assert { condition = output.enabled error_message = "expected enabled" }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Test Assertions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 155 — Test Expected Failures

### Concept

Negative tests can assert that specific validation failures are expected rather than treating every failure as a broken test.

### Syntax / Example

```hcl
expect_failures = [var.region]
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Test Expected Failures**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 156 — Provider Mocking

### Concept

Terraform supports mock providers/resources/data sources in the test framework so many module behaviors can be tested without real infrastructure or credentials.

### Syntax / Example

```hcl
mock_provider "aws" {}
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider Mocking**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 157 — Real Integration Tests

### Concept

Mocks validate logic but cannot prove provider/API behavior. Critical modules also need selected real-provider tests in isolated accounts/projects.

### Syntax / Example

```hcl
create → assert → destroy
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Real Integration Tests**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 158 — Parallel Terraform Tests

### Concept

Current Terraform tests can execute eligible run blocks in parallel. Only parallelize tests with isolated state/resources.

### Syntax / Example

```hcl
test { parallel = true }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Parallel Terraform Tests**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 159 — Test Cleanup

### Concept

Terraform attempts to destroy infrastructure created by tests. CI needs cleanup monitoring because API failures can still leave resources behind.

### Syntax / Example

```hcl
Tag test resources with owner/TTL
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Test Cleanup**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 160 — Format/Validate/Test Pipeline

### Concept

A baseline CI pipeline should run formatting, initialization, validation, tests, security checks, then plan.

### Syntax / Example

```hcl
terraform fmt -check\nterraform init -backend=false\nterraform validate\nterraform test
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Format/Validate/Test Pipeline**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 161 — Provider-Free Validation

### Concept

Some CI stages can initialize without a production backend and run syntax/module checks before any production credentials are introduced.

### Syntax / Example

```hcl
terraform init -backend=false
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Provider-Free Validation**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 162 — Security Scanning

### Concept

IaC scanners evaluate configuration/plan for problems such as public databases, weak network rules, or missing encryption. Scanner results must be validated against actual provider semantics.

### Syntax / Example

```hcl
scan configuration and/or plan JSON
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Security Scanning**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 163 — Policy as Code

### Concept

HCP Terraform or external systems can enforce organization policy against runs/plans. Policies are particularly valuable for high-blast-radius guardrails.

### Syntax / Example

```hcl
deny public DB / require tags / approved regions
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Policy as Code**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 164 — Plan JSON in CI

### Concept

Plan JSON allows deterministic tooling to examine resource changes and attributes. Never publish it publicly because sensitive values may be present.

### Syntax / Example

```hcl
terraform show -json tfplan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Plan JSON in CI**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 165 — AWS Provider Pattern

### Concept

Use separate root provider configurations for accounts/regions and reusable modules for networking, IAM, compute, and databases.

### Syntax / Example

```hcl
provider "aws" { region = var.region }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **AWS Provider Pattern**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 166 — AWS Multi-Account Pattern

### Concept

Prefer role assumption or workload federation per account rather than long-lived access keys. State boundaries should align with ownership/blast radius.

### Syntax / Example

```hcl
provider aliases + assume role/workload identity
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **AWS Multi-Account Pattern**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 167 — Azure Provider Pattern

### Concept

Use `azurerm` provider with subscription/tenant identity supplied externally. Separate subscriptions are strong environment boundaries.

### Syntax / Example

```hcl
provider "azurerm" { features {} }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Azure Provider Pattern**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 168 — Azure Managed Identity Pattern

### Concept

CI in Azure can use managed identity/workload federation rather than embedded client secrets.

### Syntax / Example

```hcl
External identity chain
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Azure Managed Identity Pattern**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 169 — GCP Provider Pattern

### Concept

Configure project/region and authenticate through Application Default Credentials or workload identity federation.

### Syntax / Example

```hcl
provider "google" { project = var.project_id region = var.region }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **GCP Provider Pattern**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 170 — GCP Project Separation

### Concept

GCP projects form a useful Terraform state/ownership/billing boundary. Avoid one giant state spanning unrelated projects.

### Syntax / Example

```hcl
project-per-environment where appropriate
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **GCP Project Separation**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 171 — Kubernetes Provider

### Concept

Terraform can manage Kubernetes objects after a cluster exists. Be careful coupling cluster creation and every application resource into one state.

### Syntax / Example

```hcl
provider "kubernetes" { ... }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Kubernetes Provider**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 172 — Helm Provider

### Concept

Terraform can install Helm releases, but large application fleets are often better owned by GitOps or dedicated deployment pipelines.

### Syntax / Example

```hcl
helm_release resource
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Helm Provider**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 173 — OpenShift Boundary

### Concept

Terraform can manage cloud prerequisites, cluster resources, projects, quotas, and selected Operators, but should respect OpenShift Operator-owned sources of truth.

### Syntax / Example

```hcl
Terraform → OCP APIs, GitOps → apps
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **OpenShift Boundary**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 174 — Multi-Provider Graph

### Concept

Terraform can build one graph across multiple providers. This is powerful but increases blast radius and credential complexity.

### Syntax / Example

```hcl
AWS network → Kubernetes cluster → DNS
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Multi-Provider Graph**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 175 — HCP Terraform

### Concept

HCP Terraform provides remote state, remote runs, VCS integration, workspace/project access control, policy, variable management, run history, and other collaboration features.

### Syntax / Example

```hcl
HCP Terraform workspace
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP Terraform**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 176 — HCP Terraform Workspace

### Concept

An HCP Terraform workspace manages the lifecycle and state of one Terraform root configuration. It is different from a Terraform CLI workspace.

### Syntax / Example

```hcl
One workspace → one state
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP Terraform Workspace**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 177 — HCP Projects

### Concept

Projects group HCP Terraform workspaces and support organization/access structure. They are not cloud provider projects.

### Syntax / Example

```hcl
Organization → Project → Workspace
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP Projects**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 178 — Remote Runs

### Concept

With remote execution, HCP Terraform queues and runs Terraform in managed disposable execution environments using workspace configuration, variables, state, and policy.

### Syntax / Example

```hcl
terraform plan can trigger remote run when configured
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Remote Runs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 179 — Run Queue

### Concept

State-changing runs for a workspace are serialized because later plans could become invalid if an earlier run changes state.

### Syntax / Example

```hcl
pending → plan → policy → apply
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Run Queue**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 180 — Plan-Only Runs

### Concept

Plan-only operations can provide analysis without applying infrastructure, but a saved plan still must respect state-changing run serialization when applied.

### Syntax / Example

```hcl
Speculative/plan-only workflow
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Plan-Only Runs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 181 — HCP State Versions

### Concept

HCP Terraform stores current and historical workspace state versions, linking state changes to runs and VCS commits.

### Syntax / Example

```hcl
Workspace → States
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP State Versions**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 182 — HCP Workspace Access

### Concept

Workspace permissions should separate read, plan, write, variable, and administration capabilities according to team responsibilities.

### Syntax / Example

```hcl
Team access
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP Workspace Access**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 183 — Remote State Consumers

### Concept

HCP Terraform can restrict which workspaces may consume outputs from another workspace rather than exposing all workspace state globally.

### Syntax / Example

```hcl
Explicit remote-state consumers
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Remote State Consumers**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 184 — Dynamic Provider Credentials

### Concept

HCP Terraform can use dynamic provider credential workflows so each run obtains temporary cloud credentials rather than storing long-lived keys.

### Syntax / Example

```hcl
OIDC/dynamic credentials
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Dynamic Provider Credentials**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 185 — HCP Run Tasks

### Concept

Run tasks integrate third-party security, cost, compliance, or operational checks into the Terraform run lifecycle.

### Syntax / Example

```hcl
plan → run task → policy/approval
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP Run Tasks**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 186 — Sentinel / OPA Policy Context

### Concept

HCP Terraform supports governance policy capabilities. Policies should be versioned, tested, and rolled out carefully.

### Syntax / Example

```hcl
Policy sets
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Sentinel / OPA Policy Context**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 187 — HCP vs Local Execution

### Concept

Remote execution centralizes state, run history, variables, policy, and execution environment. Local execution shifts those responsibilities to the operator/CI system.

### Syntax / Example

```hcl
Choose intentionally
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP vs Local Execution**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 188 — HCP Stacks Concept

### Concept

HCP Terraform Stacks are intended for orchestrating multiple modules/deployments at scale, while workspaces remain well suited to one self-contained root-module lifecycle.

### Syntax / Example

```hcl
Stacks ≠ ordinary CLI workspaces
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **HCP Stacks Concept**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 189 — Terraform Associate 004

### Concept

The current Associate exam tests Terraform 1.12 and includes IaC, providers, core workflow, configuration, modules, state, maintenance, and HCP Terraform concepts.

### Syntax / Example

```hcl
Current course is newer: Terraform 1.15
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Terraform Associate 004**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 190 — Associate State Objectives

### Concept

Expect understanding of local/remote state, locking, backend configuration, drift, state inspection, and import.

### Syntax / Example

```hcl
terraform state list / backend block
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Associate State Objectives**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 191 — Associate HCP Objectives

### Concept

Expect HCP Terraform collaboration/governance, workspace/project organization, and integration concepts.

### Syntax / Example

```hcl
Workspace / Project / remote runs
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Associate HCP Objectives**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 192 — Professional Certification Context

### Concept

The Authoring and Operations Professional certification goes deeper into hands-on lifecycle, modules, providers, remote state, automation, and HCP workflows.

### Syntax / Example

```hcl
Advanced production path
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Professional Certification Context**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 193 — Troubleshoot Invalid HCL

### Concept

Syntax/type errors should be caught by format/validate/editor tooling before a real provider plan.

### Syntax / Example

```hcl
terraform fmt\nterraform validate
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Invalid HCL**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 194 — Troubleshoot Missing Provider

### Concept

If initialization/provider selection fails, inspect required provider source/version, registry access, lock file, and network/proxy.

### Syntax / Example

```hcl
terraform providers\nterraform init
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Missing Provider**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 195 — Troubleshoot Provider Alias

### Concept

Errors about missing provider configuration commonly arise when a child module expects an alias that the root did not pass.

### Syntax / Example

```hcl
providers = { aws = aws.dr }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Provider Alias**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 196 — Troubleshoot Authentication

### Concept

A valid Terraform configuration can still fail because provider credentials are absent, expired, or pointed at the wrong account.

### Syntax / Example

```hcl
Check identity before changing resources
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Authentication**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 197 — Troubleshoot Authorization

### Concept

Fix the minimum missing permission rather than granting administrator. Cloud audit/error messages identify the denied action/resource.

### Syntax / Example

```hcl
401/403/AccessDenied analysis
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Authorization**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 198 — Troubleshoot Dependency Cycle

### Concept

Read the cycle path, identify mutual references, and split rules/resources or redesign interfaces to remove circular dependencies.

### Syntax / Example

```hcl
terraform graph
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Dependency Cycle**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 199 — Troubleshoot Unknown Values

### Concept

Known-after-apply values are normal unless an expression requires them for a key/count that must be known during planning.

### Syntax / Example

```hcl
for_each keys must generally be known during plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Unknown Values**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 200 — for_each Unknown-Key Problem

### Concept

Resource instance keys become state addresses, so Terraform needs stable known keys. Use known configuration keys and place unknown values in the map values.

### Syntax / Example

```hcl
{ for name in var.names : name => computed_value }
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **for_each Unknown-Key Problem**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 201 — Troubleshoot count Churn

### Concept

If removing an item from a list causes many indexed replacements, migrate to stable `for_each` keys where appropriate.

### Syntax / Example

```hcl
moved blocks can preserve identity during migration
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot count Churn**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 202 — Troubleshoot Module Upgrade

### Concept

Unexpected replacement after module upgrade often comes from address changes, default changes, or provider changes. Compare module release notes and moved blocks.

### Syntax / Example

```hcl
Pin version and inspect plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Module Upgrade**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 203 — Troubleshoot Lock File Conflict

### Concept

When different environments update provider locks differently, regenerate deliberately with agreed constraints/platform checksums rather than deleting the lock file.

### Syntax / Example

```hcl
terraform providers lock
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Lock File Conflict**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 204 — Troubleshoot State Lock

### Concept

Confirm no active apply before force-unlocking. A forced unlock during another write can corrupt workflow/state consistency.

### Syntax / Example

```hcl
terraform force-unlock LOCK_ID
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot State Lock**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 205 — Troubleshoot Partial Apply

### Concept

After an interrupted or failed apply, preserve state, fix the cause, and run a fresh plan. Terraform should reconcile successful partial operations.

### Syntax / Example

```hcl
terraform plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Partial Apply**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 206 — Troubleshoot Drift

### Concept

Determine whether live drift is unauthorized, emergency, another controller's ownership, or desired. Then revert, codify, or ignore only the intentionally external attribute.

### Syntax / Example

```hcl
plan → investigate → reconcile
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Drift**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 207 — Troubleshoot Import

### Concept

If imported resource plans huge changes, the configuration does not yet match the real object/provider defaults. Do not apply until the diff is understood.

### Syntax / Example

```hcl
import → plan → normalize → no-op
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Import**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 208 — Troubleshoot Destroy

### Concept

A resource blocked from deletion may have prevent_destroy, provider deletion protection, dependencies, or remote API constraints. Do not bypass protection without impact analysis.

### Syntax / Example

```hcl
Inspect plan + provider resource settings
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Destroy**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 209 — Troubleshoot Debug Logs

### Concept

Use `TF_LOG` only long enough to capture evidence, then remove/archive securely because logs can contain credentials or sensitive payloads.

### Syntax / Example

```hcl
TF_LOG=TRACE TF_LOG_PATH=terraform.log terraform plan
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Troubleshoot Debug Logs**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


# Part 210 — Production Terraform Definition of Done

### Concept

A mature root module has remote state, locking, version constraints, committed lock file, typed inputs, module versions, CI plan/apply, policy, tests, drift monitoring, and a recovery runbook.

### Syntax / Example

```hcl
Git + State + Providers + Modules + CI + Policy + DR
```

### Why it matters

Terraform configuration is not only syntax. This concept affects at least one of the following: resource identity, dependency ordering, repeatability, state safety, provider behavior, security, or team collaboration. In production, treat the configuration and the generated plan as change-control artifacts.

### Practical operating rule

Before applying a change involving **Production Terraform Definition of Done**, run the relevant formatting/validation steps, inspect the plan, confirm the target account/project/workspace and state, and verify the result after apply. If the plan proposes unexpected replacement or destruction, stop and identify the cause instead of forcing the change.


---

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Install and Verify Terraform
Install Terraform 1.15.x from an official package/release source. Run `terraform version` and record the exact version.

### Lab 2 — First Local Configuration
Create a root module using the `random` provider. Run `init`, `fmt`, `validate`, `plan`, and `apply`.

### Lab 3 — Dependency Lock File
Inspect `.terraform.lock.hcl`. Explain provider source, selected version, and checksums. Commit it to a test Git repository.

### Lab 4 — HCL Types
Use `terraform console` to create and inspect a string, number, bool, list, set, map, object, tuple, and null.

### Lab 5 — Expressions
Practice conditional, `for`, filtering, splat, and collection conversion expressions in `terraform console`.

### Lab 6 — Functions
Test `merge`, `try`, `can`, `flatten`, `toset`, `zipmap`, `sort`, `distinct`, `cidrsubnet`, `jsonencode`, and `templatefile`.

### Lab 7 — Typed Variables
Create typed variables for environment, replicas, tags, and a database object. Add validation.

### Lab 8 — Locals and Naming
Create a naming standard using locals and merge standard tags with caller tags.

### Lab 9 — Outputs
Create normal and sensitive outputs. Observe display behavior.

### Lab 10 — Data Sources
Use an authorized/local provider data source. Explain why the object is read rather than owned.

### Lab 11 — count
Create three local/random resources with `count`. Remove the middle logical input and observe index behavior.

### Lab 12 — for_each
Rebuild the same design using stable keys. Compare the plan.

### Lab 13 — Explicit Dependency
Create a justified hidden dependency and use `depends_on`. Then explain why it should not be used when a normal reference exists.

### Lab 14 — create_before_destroy
Use a disposable resource that supports replacement. Observe replacement ordering.

### Lab 15 — prevent_destroy
Protect a lab resource and intentionally plan a removal. Record the error, then restore configuration.

### Lab 16 — ignore_changes
Simulate an attribute owned by an external system. Ignore only that one attribute and explain the drift trade-off.

### Lab 17 — Preconditions
Reject a "production" configuration when backups are disabled.

### Lab 18 — Postconditions
Add a postcondition or supported equivalent assertion checking a created/read resource property.

### Lab 19 — check Block
Create a non-blocking check and compare its failure behavior with a precondition.

### Lab 20 — Provider Alias
Configure two harmless provider instances or two regions in an authorized cloud account. Route one resource to the alias.

### Lab 21 — Provider Schema
Run `terraform providers schema -json` and inspect selected resource schema fields with `jq`.

### Lab 22 — Local Module
Create `modules/network_like/` using local/random resources to model inputs/outputs without cloud cost.

### Lab 23 — Module Inputs/Outputs
Pass structured variables into the module and consume its outputs from the root module.

### Lab 24 — Module for_each
Create module instances keyed by `dev`, `stage`, and `prod`.

### Lab 25 — Module Versioning Tabletop
Design releases 1.0.0, 1.1.0, 1.1.1, and 2.0.0 and classify changes.

### Lab 26 — Refactor with moved
Move a root resource into a child module using a `moved` block and confirm the plan avoids destroy/create.

### Lab 27 — Rename with moved
Rename a resource address safely and verify identity remains.

### Lab 28 — removed Block
In a disposable local configuration, stop managing an object without destroying it using a configuration-driven removal workflow.

### Lab 29 — Configuration-Driven Import
Create a resource outside the target state, write a matching resource/import block, import it, then reach a safe plan.

### Lab 30 — Import Generated Configuration
Where the chosen provider supports it, experiment with generated import configuration and manually review every generated argument.

### Lab 31 — Bulk Import Tabletop
Create a `.tfquery.hcl` example and document the provider support needed for `terraform query`/bulk import.

### Lab 32 — State Inspection
Practice `state list`, `state show`, `show`, and JSON output against disposable state.

### Lab 33 — Refresh-Only
Create controlled drift and inspect a refresh-only plan. Explain what changes state knowledge versus infrastructure.

### Lab 34 — Explicit Replace
Use `-replace` on a disposable resource and observe the plan.

### Lab 35 — CLI Workspaces
Create `dev` and `test` CLI workspaces. Show that they have separate state while using the same code.

### Lab 36 — terraform console Debugging
Debug a complex nested `for` expression interactively before putting it into configuration.

### Lab 37 — Graph
Generate `terraform graph`, render or inspect DOT, and identify three dependency edges.

### Lab 38 — Saved Plan
Create a saved plan, inspect it, apply it, and record why this is better for controlled approvals.

### Lab 39 — Plan JSON
Generate `terraform show -json` for a saved plan and use `jq` to list resource change actions.

### Lab 40 — Native Terraform Test
Create a `.tftest.hcl` file with at least three assertions and run `terraform test`.

### Lab 41 — Negative Test
Use validation plus expected-failure testing to prove invalid input is rejected.

### Lab 42 — Mock Provider
Use provider mocking where supported to test module logic without real credentials.

### Lab 43 — Integration Test
Create and destroy a harmless real/local resource in a test run and verify output.

### Lab 44 — Formatting CI
Build a shell CI script that runs `fmt -check`, `init`, `validate`, and `test`.

### Lab 45 — Security Plan Review
Create or mock a plan containing public SSH, a public database, and missing encryption. Define policy decisions.

### Lab 46 — AWS Module Design
Design a VPC module with public/private subnets, NAT strategy, tags, and outputs. Use real AWS only in an authorized sandbox.

### Lab 47 — Azure Module Design
Design VNet/subnet/NSG/private-endpoint module interfaces and subscription/provider boundaries.

### Lab 48 — GCP Module Design
Design project/VPC/subnet/firewall/GKE or Cloud SQL boundaries.

### Lab 49 — Kubernetes Boundary
Decide which objects Terraform owns and which GitOps owns. Write an ADR.

### Lab 50 — OpenShift Boundary
Design Terraform ownership for projects/quotas and GitOps ownership for application workloads while respecting OpenShift Operators.

### Lab 51 — Multi-Region Providers
Design primary and DR provider aliases and pass them to a reusable module.

### Lab 52 — Failed Authentication
Intentionally use a harmless invalid/expired lab credential and distinguish authentication error from HCL validation.

### Lab 53 — Least-Privilege Failure
Use a constrained lab identity and identify the precise denied API action rather than granting admin.

### Lab 54 — Partial Apply Tabletop
Model a run where network succeeds but database creation fails. Write recovery steps.

### Lab 55 — Drift Incident
Introduce controlled external drift, run plan, classify it as unauthorized or legitimate, then reconcile.

### Lab 56 — Module Upgrade Incident
Model a module upgrade that changes resource addresses. Use moved blocks and versioning to avoid replacement.

### Lab 57 — Provider Upgrade
Upgrade one provider within an allowed version range, inspect lock-file and plan differences, and document promotion steps.

### Lab 58 — HCP Terraform Architecture
Design Organization → Project → Workspace organization for network, platform, database, and application states.

### Lab 59 — HCP Remote Run Tabletop
Diagram VCS-triggered remote run: queue → plan → policy → approval → apply → state version.

### Lab 60 — Full Terraform Game Day
Troubleshoot ten scenarios: invalid HCL, provider download failure, auth failure, RBAC failure, unknown `for_each` key, dependency cycle, state lock, import mismatch, drift, and unexpected replacement.

---

## 6. Mini Project

# Mini Project — Multi-Cloud Terraform Platform

Build a production-style Terraform repository with reusable modules and environment roots.

```text
terraform-platform/
├── modules/
│   ├── network/
│   ├── database/
│   ├── compute/
│   ├── kubernetes/
│   └── monitoring/
├── live/
│   ├── aws/
│   │   ├── dev/
│   │   └── prod/
│   ├── azure/
│   │   ├── dev/
│   │   └── prod/
│   └── gcp/
│       ├── dev/
│       └── prod/
├── tests/
├── policies/
├── docs/
└── README.md
```

Requirements:

```text
Terraform 1.15 version constraint
provider version constraints
committed dependency lock file
typed module inputs
safe defaults
standard tags
module outputs
provider aliases for DR/multi-region
moved blocks for at least one refactor
configuration-driven import example
native terraform tests
CI format/validate/test/plan
plan JSON inspection
security policy checks
short-lived CI identity design
remote state design (implemented deeply in Course 64)
```

Architecture must include at least one complete environment flow:

```text
network
  ↓
private compute / Kubernetes
  ↓
load balancing
  ↓
database
  ↓
monitoring
```

Required documents:

```text
ARCHITECTURE.md
MODULE_STANDARD.md
PROVIDER_STRATEGY.md
IMPORT_RUNBOOK.md
UPGRADE_RUNBOOK.md
DRIFT_RUNBOOK.md
TESTING.md
SECURITY.md
```

---

## 7. Recommended Resources

The course is self-contained for the learning path. For implementation against current behavior, use official HashiCorp documentation for:

```text
Terraform installation
Terraform language
Provider configuration
Resource/data/module blocks
Meta-arguments
Functions and expressions
State
Import/search
Testing
HCP Terraform
Terraform Registry
```

Current baseline:

```text
Terraform 1.15.8 stable
```

---

## 8. Certification Relevance

Current foundational certification:

```text
HashiCorp Certified: Terraform Associate (004)
Product version tested: Terraform 1.12
```

The current exam covers:

```text
IaC concepts
Terraform fundamentals
providers
core workflow
configuration
modules
state management
import/maintenance
HCP Terraform
```

This course uses Terraform 1.15, so it is intentionally broader than the exam.

Advanced path:

```text
Terraform Authoring and Operations Professional
```

which emphasizes production authoring, lifecycle, remote state, modules, providers, automation, and HCP Terraform.

---

## 9. Common Mistakes & Best Practices

- Commit `.terraform.lock.hcl`; do not commit `.terraform/`.
- Pin Terraform/provider/module versions through an explicit upgrade process.
- Keep credentials outside HCL.
- Prefer short-lived workload identity.
- Use `for_each` when stable keys matter.
- Prefer implicit references to excessive `depends_on`.
- Review replacements and destroys carefully.
- Treat `ignore_changes` as an ownership decision, not a way to silence plans.
- Prefer modules with narrow, typed interfaces.
- Keep provider configuration in roots and pass aliases deliberately.
- Test reusable modules.
- Use `moved` blocks for refactors rather than accidental recreation.
- Import then plan until configuration matches reality.
- Never let two states own one real resource.
- Avoid routine `-target`.
- Treat plan JSON/debug logs as potentially sensitive.
- Separate cluster infrastructure ownership from application GitOps where appropriate.
- Do not confuse CLI workspaces with HCP Terraform workspaces.
- Protect HCP/state write permissions as production infrastructure admin access.
- Verify service health after apply; a successful apply is not an application SLO.

---

## 10. Self-Assessment Questions (with short answers)

1. **Terraform Core vs provider?** Core manages HCL/graph/state/plan; provider integrates external APIs.
2. **What does `init` do?** Initializes backend and downloads providers/modules.
3. **Commit `.terraform.lock.hcl`?** Normally yes.
4. **Commit `.terraform/`?** Normally no.
5. **What does `validate` prove?** Configuration consistency, not full provider/API success.
6. **Why save a plan?** To review and later apply the same planned change.
7. **Provider version defined where?** `required_providers`.
8. **Provider credentials in HCL?** Avoid; use external identity chains.
9. **Provider alias purpose?** Multiple regions/accounts/projects/provider configurations.
10. **Resource vs data source?** Own lifecycle vs read existing data.
11. **count vs for_each?** Positional instances vs stable keyed instances.
12. **What creates implicit dependency?** References between resources/values.
13. **When use `depends_on`?** Hidden real dependency not represented by references.
14. **create_before_destroy?** Create replacement before removing old when possible.
15. **prevent_destroy?** Guardrail against Terraform destruction.
16. **ignore_changes danger?** Can hide real drift.
17. **Precondition?** Blocks an invalid operation before lifecycle work.
18. **Postcondition?** Validates a guarantee after evaluation.
19. **check block failure behavior?** Reports a warning rather than behaving like a lifecycle-blocking precondition.
20. **What is null?** Absence of a value, not empty string/zero.
21. **Known after apply?** A normal unknown value resolved later.
22. **Sensitive means encrypted?** No.
23. **Why use objects?** Strong structured module interfaces.
24. **Why `for_each` stable keys?** Keys become resource identities.
25. **Dynamic block use?** Repeated nested blocks.
26. **Why `jsonencode`?** Build valid JSON from typed HCL.
27. **What is a module?** Reusable collection of Terraform resources with inputs/outputs.
28. **Why version modules?** Module changes can affect many consumers.
29. **Root-module responsibility?** Environment composition, providers, backend/cloud integration.
30. **State purpose?** Map Terraform addresses to real objects and known attributes.
31. **`state list`?** Lists managed addresses.
32. **`state show`?** Shows one state resource instance.
33. **`moved` block?** Records address refactor without physical recreation.
34. **`removed` block?** Configuration-driven removal from management, optionally without destroy.
35. **Import block?** Brings existing infrastructure under Terraform state ownership.
36. **Why plan after import?** Ensure code matches reality before modifying it.
37. **Bulk search/import?** Current provider-assisted discovery/import workflow for supported resources.
38. **Why avoid two states owning one object?** Competing writes and destructive conflict.
39. **`-target` normal workflow?** No; special recovery/surgical tool.
40. **`terraform console` use?** Evaluate/debug HCL expressions.
41. **`terraform graph` use?** Inspect dependency graph.
42. **Native test file extension?** `.tftest.hcl` or `.tftest.json`.
43. **Provider mocking benefit?** Test module logic without real infrastructure/credentials.
44. **Mock tests replace integration tests?** No.
45. **CLI workspace?** Multiple state instances for same configuration.
46. **HCP workspace?** Managed lifecycle/state/run unit for one root configuration.
47. **HCP run queue purpose?** Serialize state-changing workspace runs.
48. **Dynamic provider credentials?** Temporary per-run cloud identity instead of long-lived keys.
49. **Current stable Terraform baseline in this course?** 1.15.8.
50. **Current Terraform Associate exam?** Associate (004), testing Terraform 1.12.
51. **Best response to partial apply?** Fix cause and run a fresh plan.
52. **Best response to huge unexpected plan?** Stop and investigate state/provider/module/drift.
53. **Best response to state lock?** Confirm no active writer before supported unlock.
54. **Best response to dependency cycle?** Redesign references/resource boundaries.
55. **What should CI run before plan?** Format, initialize, validate, tests, security/policy checks.
56. **Why plan JSON sensitive?** It can expose internal topology and sensitive values.
57. **Why provider lock file matters?** Deterministic/integrity-checked provider selection.
58. **Terraform for every Kubernetes app?** Often no; GitOps/Helm may better own app lifecycle.
59. **What does apply success not prove?** That the application/service is healthy.
60. **Production Terraform operating model?** Versioned code + providers + modules + remote state + plan + testing + policy + controlled identity + recovery.
