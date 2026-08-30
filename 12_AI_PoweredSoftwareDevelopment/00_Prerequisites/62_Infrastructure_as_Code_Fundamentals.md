# 62. Infrastructure as Code Fundamentals

> Phase 16 — Infrastructure as Code

This course establishes the engineering foundation required before Terraform, OpenTofu, AWS CloudFormation, Azure Bicep, Pulumi, Ansible-driven provisioning, or GitOps-based infrastructure workflows.

The purpose is not to memorize one tool. The purpose is to understand the **operating model behind Infrastructure as Code (IaC)** so that later tools make sense rather than becoming command memorization.

A useful end-to-end model is:

```text
Business / Technical Requirement
            ↓
Architecture Decision
            ↓
Version-Controlled Infrastructure Definition
            ↓
Formatting / Validation / Testing
            ↓
Security & Policy Checks
            ↓
Plan / Preview
            ↓
Human or Automated Approval
            ↓
Provisioning Engine
            ↓
Cloud / Virtualization / Kubernetes APIs
            ↓
Real Infrastructure
            ↓
Observed State
            ↓
Drift Detection / Monitoring
            ↓
Change / Replace / Destroy / Recover
```

Infrastructure becomes a **software engineering artifact**. That means it should be:

```text
repeatable
reviewable
versioned
auditable
testable
reproducible
recoverable
secure
maintainable
```

---

## 1. Topic Title

**Infrastructure as Code Fundamentals**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain Infrastructure as Code and why organizations adopt it.
- Distinguish IaC from shell scripting, configuration management, CI/CD, deployment automation, and GitOps.
- Explain declarative versus imperative automation.
- Explain desired state, actual state, reconciliation, convergence, and idempotency.
- Explain infrastructure drift and drift remediation.
- Explain immutable versus mutable infrastructure.
- Explain how an IaC engine models resources, providers, dependencies, and lifecycle.
- Explain why state exists and why state is sensitive.
- Explain local state, remote state, state locking, state versioning, and state recovery.
- Explain plan/preview workflows and why they are a major safety control.
- Explain create, update, replace, destroy, import, move, and adoption workflows.
- Explain variables, local values, outputs, data lookups, expressions, and resource addressing.
- Explain reusable modules and module interfaces.
- Explain environment separation and account/subscription/project boundaries.
- Explain naming, tagging, ownership, and cost-allocation standards.
- Explain monorepo versus multi-repository IaC architectures.
- Explain self-service infrastructure and platform engineering patterns.
- Explain pull-request-based infrastructure delivery.
- Explain CI/CD pipelines for IaC.
- Explain short-lived identity and least-privilege permissions for automation.
- Explain IaC testing, linting, static analysis, security scanning, and policy as code.
- Explain preventive versus detective controls.
- Explain secret-management requirements for infrastructure code.
- Explain supply-chain risks involving providers, modules, build systems, and CI.
- Explain drift detection and reconciliation workflows.
- Explain infrastructure rollback limitations.
- Explain disaster recovery for IaC repositories, state, and infrastructure.
- Explain how IaC applies to AWS, Azure, Google Cloud, VMware, OpenStack, Kubernetes, and OpenShift.
- Compare Terraform/OpenTofu, CloudFormation, Bicep, Pulumi, Ansible, Helm, Kustomize, and GitOps.
- Design a production-ready IaC repository, governance model, and deployment pipeline.
- Troubleshoot common IaC failures systematically.

---

## 3. Prerequisites

Required knowledge:

```text
Linux fundamentals
Networking fundamentals
Git
YAML / JSON
Basic cloud computing
At least one cloud provider
Bash or Python basics
Basic security/IAM concepts
```

Recommended prior courses:

```text
45. Git and Version Control Systems
46. Configuration Management
47. Ansible
48. Cloud Computing Fundamentals
52–56. Cloud Platform Courses
57–61. Containers / Kubernetes / OpenShift
```

Recommended commands:

```bash
git status
git diff
git log
git branch
git commit
git push
curl
jq
grep
sed
bash
```

---

## 4. Core Concepts Explanation

# Part 1 — What Infrastructure as Code Actually Means

Infrastructure as Code means that infrastructure is defined through **machine-readable code or declarative configuration** rather than depending on undocumented clicks or manual commands.

Infrastructure can include:

```text
VPCs / VNets
subnets
routes
firewalls
load balancers
virtual machines
managed databases
object storage
IAM roles
DNS
Kubernetes clusters
Kubernetes resources
monitoring resources
backup policies
```

Traditional infrastructure:

```text
Ticket
  ↓
Engineer logs into console
  ↓
Clicks through UI
  ↓
Creates resources
  ↓
Changes settings later
  ↓
Documentation becomes outdated
```

IaC:

```text
Requirement
  ↓
Git
  ↓
Infrastructure code
  ↓
Review
  ↓
Plan
  ↓
Apply
  ↓
Infrastructure
```

The key principle is not merely automation. It is that **the intended infrastructure is represented in code**.

---

# Part 2 — Why Manual Infrastructure Fails at Scale

Manual infrastructure works when there are only a few servers. It becomes unreliable at scale.

Common problems:

```text
configuration differences
forgotten settings
inconsistent naming
missing logs
open firewall rules
unknown owners
slow recovery
poor auditability
```

Example:

```text
Environment A:
HTTPS only
encrypted disk
flow logs enabled

Environment B:
HTTPS + SSH from Internet
unencrypted disk
flow logs forgotten
```

Both environments were supposedly built from the same architecture document, but manual implementation created drift.

IaC reduces this risk by making one implementation repeatable.

---

# Part 3 — Infrastructure as a Software Engineering Discipline

Once infrastructure becomes code, software practices can be applied:

```text
Git
branches
pull requests
code review
tests
CI/CD
release versions
static analysis
security scanning
documentation
```

An infrastructure change should therefore resemble a software change:

```text
Feature:
Add private application subnet

Implementation:
IaC code change

Validation:
syntax + policy + plan

Review:
network/platform team

Deployment:
controlled apply

Evidence:
Git commit + CI logs + plan
```

This is one of the most important changes IaC introduces.

---

# Part 4 — Repeatability

Repeatability means the same infrastructure definition can be executed repeatedly and produce the intended result.

Example:

```text
module "application_environment"
```

can create:

```text
dev
test
stage
prod
```

with different values:

```text
dev:
replicas = 1

prod:
replicas = 6
```

The architecture is consistent while scale differs intentionally.

---

# Part 5 — Reproducibility

Repeatability is not enough if external dependencies constantly change.

For reproducibility, record or pin important inputs:

```text
IaC version
provider version
module version
machine image
Kubernetes version
region
variables
policy version
```

Bad:

```text
use latest module
use latest VM image
use latest provider
```

Better:

```text
module version 2.4.1
provider version constraint
approved machine-image ID
```

Reproducibility is essential for disaster recovery.

---

# Part 6 — Auditability

A properly designed IaC workflow can answer:

```text
Who requested the change?
Who wrote it?
Who reviewed it?
What changed?
Which plan was approved?
When was it applied?
Which commit produced production?
```

Infrastructure provider audit logs tell you what happened at the API level. Git and CI/CD tell you **why** it happened.

Both are required for strong governance.

---

# Part 7 — IaC Is Not Just a Shell Script

A shell script can automate provisioning:

```bash
cloud-cli network create ...
cloud-cli vm create ...
cloud-cli firewall create ...
```

But a simple script usually lacks:

```text
state tracking
resource identity
dependency graph
plan/preview
drift awareness
replacement lifecycle
safe import
parallel dependency execution
```

A real IaC engine generally understands the infrastructure as a graph of managed objects rather than only a list of commands.

---

# Part 8 — Provisioning vs Configuration Management

Provisioning answers:

```text
What infrastructure should exist?
```

Examples:

```text
VPC
VM
load balancer
database
Kubernetes cluster
```

Configuration management answers:

```text
How should the operating system/application be configured?
```

Examples:

```text
install nginx
create users
configure SSH
edit /etc/app.conf
start services
```

Typical combination:

```text
Terraform
   ↓
VMs / network / database
   ↓
Ansible
   ↓
OS / middleware configuration
```

The boundary is not absolute, but separating responsibilities usually reduces complexity.

---

# Part 9 — IaC vs Application Deployment

Infrastructure provisioning and application delivery are related but not identical.

Example:

```text
IaC:
create Kubernetes cluster

Application deployment:
deploy application into Kubernetes
```

Possible toolchain:

```text
Terraform
  ↓
AKS / EKS / GKE
  ↓
Helm / Kustomize / GitOps
  ↓
Application
```

Do not make one tool manage every lifecycle unless there is a strong reason.

---

# Part 10 — IaC vs GitOps

Both use desired state, but execution differs.

Typical IaC:

```text
Git change
 ↓
CI job
 ↓
plan/apply
 ↓
infrastructure
```

GitOps:

```text
Git desired state
        ↓
Controller continuously watches
        ↓
Live cluster
        ↓
Controller reconciles drift
```

GitOps is especially common for Kubernetes/OpenShift resources.

IaC often uses **run-driven reconciliation** instead of continuous reconciliation.

---

# Part 11 — Declarative Automation

Declarative configuration says:

```text
I want this state.
```

Example concept:

```text
VPC CIDR = 10.20.0.0/16
private subnets = 3
application replicas = 4
```

The engine determines:

```text
creation order
updates
dependencies
replacement
```

This is the main model used by Terraform, CloudFormation, Bicep, and Kubernetes YAML.

---

# Part 12 — Imperative Automation

Imperative automation says:

```text
Do these steps.
```

Example:

```text
1. Create VPC.
2. Wait.
3. Create subnet.
4. Create NIC.
5. Create VM.
6. Add route.
```

Shell scripts and SDK programs are commonly imperative.

Imperative automation is useful when the workflow itself is the main concern, but it puts more lifecycle responsibility on the author.

---

# Part 13 — Desired State

Desired state is what infrastructure code says should exist.

```text
Desired:
VPC = 1
Private subnets = 3
Public subnets = 3
NAT gateways = 3
Application nodes = 6
```

The IaC engine compares desired state with managed/observed infrastructure.

This comparison creates a plan.

---

# Part 14 — Actual State

Actual state is what currently exists.

Example:

```text
Desired application nodes: 6
Actual managed nodes:       5
```

The plan may propose:

```text
+ create 1 node
```

If the tool cannot accurately observe actual state, automation becomes dangerous.

---

# Part 15 — Convergence

Convergence is the process of moving actual state toward desired state.

```text
Desired State
     ↓
Compare
     ↓
Actual State
     ↓
Calculate Difference
     ↓
Change
     ↓
New Actual State
```

Configuration management systems and GitOps controllers use the same general principle.

---

# Part 16 — Idempotency

An operation is idempotent when running it multiple times keeps the same intended result.

Bad:

```bash
create-server
```

Run three times:

```text
server1
server2
server3
```

Desired-state model:

```text
server_count = 1
```

Run repeatedly:

```text
one server remains
```

Idempotency makes automation safe to rerun after failures.

---

# Part 17 — Resource

An IaC resource represents one manageable infrastructure object.

Conceptual examples:

```text
network.main
subnet.private_a
database.orders
load_balancer.public
```

A resource normally has:

```text
type
logical name
arguments
provider
state identity
outputs/computed attributes
```

---

# Part 18 — Provider / Plugin

The provisioning engine usually does not directly know every cloud API.

A provider translates resources into API operations.

```text
IaC Engine
   ↓
AWS Provider
   ↓
AWS APIs
```

or:

```text
IaC Engine
   ↓
Kubernetes Provider
   ↓
Kubernetes API
```

Provider versions therefore influence behavior and schemas.

---

# Part 19 — Resource Schema

A provider defines which fields are:

```text
required
optional
computed
sensitive
force replacement
deprecated
validated
```

Example:

```text
database.name             required
database.endpoint         computed
database.storage_size     updateable
database.engine           may require replacement
```

Understanding the schema helps explain plans.

---

# Part 20 — Computed Values

Some values are not known until infrastructure exists.

Examples:

```text
public IP
load balancer DNS
generated resource ID
database endpoint
```

The IaC engine can pass those outputs into dependent resources after creation.

---

# Part 21 — Unknown Values During Planning

At plan time:

```text
load_balancer_dns = known after apply
```

A good engine still understands dependency:

```text
DNS record
depends on
load balancer
```

even if the exact hostname is not yet known.

---

# Part 22 — Resource Address

IaC needs a stable logical address.

Concept:

```text
module.network.subnet.private[0]
```

This is different from the cloud-provider ID:

```text
subnet-01abc...
```

State maps the logical address to the physical resource.

---

# Part 23 — Logical Identity vs Physical Identity

Example:

```text
IaC logical address:
module.database.db.main

Cloud resource ID:
projects/x/locations/y/databases/db-91a...
```

Renaming the IaC object without telling the state engine can make it appear that:

```text
old resource must be destroyed
new resource must be created
```

State migration avoids this.

---

# Part 24 — Create, Update, Replace, Destroy

Every plan action fits into a lifecycle category:

```text
Create
Update in place
Replace
Destroy
No change
```

Example:

```text
change tag:
update

change immutable network property:
replace

remove resource from code:
destroy
```

Review replacement carefully.

---

# Part 25 — Replacement Is a Risk Event

Replacing a stateless worker may be easy.

Replacing:

```text
database
KMS key
DNS zone
public endpoint
stateful disk
```

can be dangerous.

Production workflows should identify replacements explicitly before approval.

---

# Part 26 — Destruction Protection

IaC makes destruction easy, which means production needs guardrails.

Controls:

```text
deletion protection
prevent-destroy lifecycle
cloud resource locks
separate production identity
manual approval
backup checks
policy as code
```

Do not rely on "the engineer will notice."

---

# Part 27 — Infrastructure Drift

Drift is a difference between code/state and live infrastructure.

Example:

```text
IaC:
SSH allowed only from admin VPN

Manual console change:
SSH allowed from 0.0.0.0/0
```

Now the environment is insecure and the code no longer represents reality.

---

# Part 28 — Causes of Drift

Common causes:

```text
console changes
manual CLI changes
emergency incident actions
another automation tool
cloud default changes
operator/controller mutations
provider behavior changes
```

Drift is inevitable unless detected.

---

# Part 29 — Drift Detection

Methods:

```text
scheduled plan
refresh
cloud configuration monitoring
policy tools
GitOps reconciliation
asset inventory
```

A scheduled plan that produces unexpected changes is a strong signal.

---

# Part 30 — Drift Remediation

Possible responses:

```text
1. Revert live state back to code.
2. Update code to represent legitimate manual change.
3. Import/adopt the external resource.
4. Move ownership to another stack.
```

Do not automatically overwrite an emergency change before understanding why it exists.

---

# Part 31 — Mutable Infrastructure

Some resources are naturally updated:

```text
firewall rules
DNS records
IAM policies
database parameters
autoscaling thresholds
```

IaC can manage these in place.

---

# Part 32 — Immutable Infrastructure

Immutable pattern:

```text
old server image
     ↓
build new image
     ↓
create replacement servers
     ↓
move traffic
     ↓
remove old servers
```

Benefits:

```text
lower drift
repeatable deployment
simpler rollback
known image provenance
```

---

# Part 33 — Persistent vs Ephemeral Infrastructure

Ephemeral:

```text
feature environment
test cluster
temporary runner
```

Persistent:

```text
database
DNS
KMS key
identity
shared network
```

Do not put long-lived foundational infrastructure in the same lifecycle as temporary environments without careful boundaries.

---

# Part 34 — Shared Infrastructure

Shared resources:

```text
central VPC/VNet
DNS
transit network
logging
identity
registry
security services
```

should often have separate state and ownership from application infrastructure.

This reduces blast radius.

---

# Part 35 — Dependency Graph

Infrastructure has dependencies.

```text
VPC
 ↓
Subnet
 ↓
Network Interface
 ↓
VM
```

IaC engines model these as a directed dependency graph.

---

# Part 36 — Directed Acyclic Graph

A typical dependency graph is a DAG:

```text
Directed
Acyclic
Graph
```

A cycle is impossible to order.

Bad:

```text
Resource A depends on B
Resource B depends on A
```

The design must be restructured.

---

# Part 37 — Implicit Dependency

If one resource references another:

```text
subnet_id = private_subnet.id
```

the engine automatically understands:

```text
private_subnet
must exist before
dependent resource
```

Prefer implicit dependencies when real data relationships exist.

---

# Part 38 — Explicit Dependency

Sometimes a dependency exists operationally without direct data reference.

Example:

```text
application deployment
must wait for
policy attachment
```

A tool may support an explicit dependency.

Use it only when the dependency cannot be expressed through normal references.

---

# Part 39 — Parallelism

Independent resources can be created simultaneously.

```text
VPC ready
├─ subnet A
├─ subnet B
└─ subnet C
```

Parallelism speeds deployments.

Too much parallelism can hit API limits.

---

# Part 40 — API Rate Limits

Infrastructure APIs protect themselves with quotas/throttling.

Errors:

```text
429 Too Many Requests
ThrottlingException
quota exceeded
```

Providers usually retry automatically, but very large deployments may require:

```text
lower parallelism
quota increase
better stack separation
```

---

# Part 41 — Eventual Consistency

Cloud APIs are distributed.

Example:

```text
Create IAM role
API returns success
Immediately use role
another API says "role not found"
```

The object exists but has not propagated everywhere.

Good providers implement retries.

Avoid arbitrary sleeps when a proper wait/retry mechanism exists.

---

# Part 42 — Partial Failure

An apply can partially succeed.

```text
network       ✓
subnet        ✓
load balancer ✓
database      ✗
```

The correct recovery is usually:

```text
fix root cause
run plan again
continue from current managed state
```

not manually destroy everything.

---

# Part 43 — Why State Exists

IaC needs a mapping between code and real resources.

```text
module.web.server.main
        ↓
cloud resource ID
```

State records this relationship.

Without state, the engine may not know which existing resource belongs to which code object.

---

# Part 44 — State Is Metadata, Not Infrastructure

Deleting state does not necessarily delete the real resources.

```text
state file deleted
↓
cloud VPC still exists
```

But the tool may lose management knowledge and propose new resources.

State loss is therefore an operational incident.

---

# Part 45 — State Can Contain Sensitive Information

Depending on tool/provider, state may contain:

```text
IP addresses
resource IDs
database endpoints
IAM metadata
connection strings
secret values
```

Therefore state should be protected like a sensitive operational database.

---

# Part 46 — Local State

Local state:

```text
engineer laptop
```

Advantages:

```text
simple
good for labs
```

Problems:

```text
easy to lose
not shared
weak collaboration
no central access policy
no reliable locking
```

Production teams should normally use remote state.

---

# Part 47 — Remote State

Remote state is centralized.

Possible locations conceptually:

```text
object storage
IaC SaaS/platform
cloud-native backend
enterprise state service
```

Benefits:

```text
team sharing
locking
backups
versioning
central access control
CI integration
```

---

# Part 48 — State Locking

Without locking:

```text
Engineer A reads state version 5
Engineer B reads state version 5

A applies changes → version 6
B applies based on version 5
```

This can create conflicts or state corruption.

A lock ensures only one writer modifies one state at a time.

---

# Part 49 — State Versioning

Remote state should retain history.

```text
v31
v32
v33 current
```

If state is damaged, a previous version may help recovery.

Do not restore blindly; compare with live infrastructure first.

---

# Part 50 — State Backup

A production state backend needs:

```text
encryption
versioning
backup/replication
access control
logging
restore procedure
```

The backend is critical infrastructure.

---

# Part 51 — State Disaster Recovery

Safe workflow:

```text
1. Stop all applies.
2. Identify last known-good state.
3. Inspect live infrastructure.
4. Restore state backup if needed.
5. Refresh/plan.
6. Verify no unexpected destroy/replace.
7. Resume controlled writes.
```

---

# Part 52 — State Ownership Boundary

One resource should have one clear IaC owner.

Bad:

```text
Stack A manages firewall rule
Stack B also manages same firewall rule
```

Each will try to overwrite the other.

Ownership must be explicit.

---

# Part 53 — State Sharding

Large environments split infrastructure into states.

Example:

```text
network
identity
security
platform
database
application
```

Benefits:

```text
smaller blast radius
faster plans
clear ownership
team parallelism
```

---

# Part 54 — Too Much State Fragmentation

If every resource has a separate state:

```text
200 states
300 cross-state dependencies
```

operations become difficult.

Balance:

```text
blast radius
ownership
coupling
operational simplicity
```

---

# Part 55 — Cross-State Contracts

One stack can publish outputs:

```text
network_id
private_subnet_ids
dns_zone_id
kms_key_id
```

Consumers should depend on these stable outputs rather than internal implementation details.

Think of outputs as an API contract.

---

# Part 56 — Plan / Preview

The most important safety question:

```text
What will happen if I apply this code?
```

A plan answers:

```text
create
update
replace
destroy
unknown values
```

Plan review is a core production control.

---

# Part 57 — No-Op Plan

Healthy unchanged environment:

```text
0 to create
0 to update
0 to destroy
```

A no-op means desired state and managed observed state match.

---

# Part 58 — Destructive Plan

If plan includes:

```text
database destroy
KMS replacement
network recreation
```

stop and understand why.

Production policy can automatically block destructive changes.

---

# Part 59 — Plan Can Become Stale

Timeline:

```text
09:00 plan
09:05 another change occurs
09:10 old plan applied
```

The reviewed plan no longer represents current state.

High-assurance workflows generate a fresh plan and apply the exact approved artifact.

---

# Part 60 — Saved Plan Concept

A pipeline can:

```text
generate plan
sign/store plan artifact
human approves
apply same plan
```

This prevents plan/apply differences.

---

# Part 61 — Import Existing Infrastructure

Brownfield environment:

```text
existing VPC created manually
```

Adoption workflow:

```text
write matching IaC code
import real resource
run plan
fix differences
reach no-op
```

Only then should the resource be considered safely managed.

---

# Part 62 — Import Risk

If configuration does not represent all important current settings, the next apply may remove them.

Therefore:

```text
import
↓
plan
↓
compare every important attribute
↓
adjust code
↓
no-op
```

---

# Part 63 — Move / Rename Resources

Refactoring:

```text
network.main
→
module.network.network.main
```

should not recreate the actual network.

State-aware move functionality tells the engine that the logical address changed while physical object remains the same.

---

# Part 64 — Remove From Management

Sometimes ownership moves elsewhere.

```text
resource remains live
but
current state stops managing it
```

Use supported state-removal workflows.

Do not delete code and accidentally destroy the resource.

---

# Part 65 — Variables

Variables separate reusable logic from environment inputs.

```text
environment = "prod"
region = "region-a"
instance_count = 4
```

Avoid hardcoding production-specific values inside reusable modules.

---

# Part 66 — Variable Types

Strong types improve safety.

```text
string
number
boolean
list
set
map
object
```

Example:

```text
allowed_ports = [443, 8443]
```

Type errors should fail before infrastructure changes.

---

# Part 67 — Variable Validation

Reject invalid values early.

Examples:

```text
environment must be dev|stage|prod
replicas must be >= 1
CIDR must be valid
production database must enable backup
```

Input validation is one form of policy.

---

# Part 68 — Safe Defaults

Default values should be safe.

Bad:

```text
public_access = true
```

Better:

```text
public_access = false
```

and require deliberate opt-in.

---

# Part 69 — Local / Derived Values

Local values reduce repetition.

Example:

```text
name_prefix =
company + "-" + app + "-" + environment
```

Useful for:

```text
naming
tags
derived CIDRs
common expressions
```

Do not hide major environment decisions inside complex local logic.

---

# Part 70 — Outputs

Outputs expose useful results.

```text
load_balancer_dns
database_endpoint
private_subnet_ids
cluster_name
```

Outputs are infrastructure interfaces.

---

# Part 71 — Sensitive Outputs

A pipeline should not print:

```text
database password
private key
token
```

Mark outputs sensitive where supported and deliver secrets through dedicated secret-management channels.

---

# Part 72 — Data Lookups

A data lookup reads infrastructure managed elsewhere.

Examples:

```text
existing DNS zone
approved machine image
central VPC
shared KMS key
secret metadata
```

This avoids taking ownership of the resource.

---

# Part 73 — Dynamic Lookup Risk

Bad reproducibility:

```text
find latest image
```

Today:

```text
image-100
```

Tomorrow:

```text
image-105
```

Same code now creates different infrastructure.

Production pipelines should promote approved artifact IDs deliberately.

---

# Part 74 — Modules

A module is a reusable infrastructure component.

Example:

```text
network module
database module
Kubernetes module
logging module
```

A module should represent an architecture capability, not just reduce line count.

---

# Part 75 — Module Interface

A module has:

```text
inputs
outputs
behavior
version
documentation
```

Example:

```text
secure_database(
  engine,
  size,
  backup_retention,
  subnet_ids
)
```

Internally it may create many resources.

---

# Part 76 — Module Encapsulation

Application team should not need to know every low-level control.

Example secure database module may automatically create:

```text
encrypted storage
backup policy
monitoring
private networking
security group
parameter group
```

The module encodes organizational standards.

---

# Part 77 — Module Versioning

Modules are software libraries.

Use controlled versions:

```text
v1.4.2
v1.5.0
v2.0.0
```

Do not point production to a mutable `main` branch unless there is a deliberate release model.

---

# Part 78 — Breaking Module Changes

Changing:

```text
input name
output name
resource address
default behavior
```

can break consumers.

Treat module interfaces like APIs.

---

# Part 79 — Module Composition

Root architecture:

```text
environment root
├── network module
├── compute module
├── database module
├── monitoring module
└── IAM module
```

Composition should create clear ownership and dependency boundaries.

---

# Part 80 — Over-Abstraction

Bad module:

```text
160 variables
70 flags
supports every possible cloud architecture
```

This becomes a programming language inside IaC.

Prefer smaller opinionated modules.

---

# Part 81 — Under-Abstraction

Copying the same 500 lines into 25 repositories creates:

```text
security drift
inconsistent fixes
slow upgrades
duplicate bugs
```

Extract shared stable patterns.

---

# Part 82 — Environment Separation

Typical environments:

```text
development
test
staging
production
```

Each should have explicit:

```text
state
variables
credentials
permissions
account/subscription/project
```

---

# Part 83 — Strong Account Separation

Best enterprise boundary often uses:

```text
separate AWS accounts
separate Azure subscriptions
separate GCP projects
```

Benefits:

```text
RBAC
billing
quota
blast radius
policy
network
```

---

# Part 84 — Same Account Multi-Environment

Possible in small environments, but creates risks:

```text
name collision
shared quota
accidental access
shared failure domain
weak cost separation
```

Use only deliberately.

---

# Part 85 — Workspace Concept

Some tools provide multiple states from same configuration.

Useful for:

```text
developer sandboxes
temporary environments
similar test stacks
```

A workspace is not automatically a strong security or account boundary.

---

# Part 86 — Directory-Based Environments

Example:

```text
live/
├── dev/
├── stage/
└── prod/
```

Each environment can have:

```text
own backend
variables
provider identity
```

This makes differences explicit.

---

# Part 87 — Avoid Long-Lived Environment Branches

Anti-pattern:

```text
dev branch
stage branch
prod branch
```

Over time:

```text
branches diverge
fixes do not merge cleanly
production becomes unique
```

Better:

```text
same code version
+
different environment inputs
```

---

# Part 88 — Promotion

Promotion model:

```text
module/app infra version 2.1.0
        ↓
dev
        ↓
stage
        ↓
production
```

Promote the same tested version.

---

# Part 89 — Naming Standards

Example:

```text
company-application-environment-region-purpose
```

Names should be:

```text
predictable
unique
within provider limits
human-readable
```

---

# Part 90 — Tagging / Labeling

Standard metadata:

```text
Environment
Owner
Application
CostCenter
DataClassification
ManagedBy
Repository
BusinessUnit
```

IaC should enforce tags automatically.

---

# Part 91 — ManagedBy Metadata

Example:

```text
ManagedBy = IaC
Repository = platform/network
```

This helps engineers find the source of truth.

It does not technically stop console changes.

---

# Part 92 — FinOps Integration

IaC can require cost-allocation labels before provisioning.

```text
No CostCenter
→ policy fails
→ resource not created
```

This improves cost visibility from day one.

---

# Part 93 — Landing Zones

A landing zone is a prebuilt governed cloud foundation.

Typical:

```text
identity
network
logging
security
billing
policy
account/project hierarchy
```

IaC is usually the implementation mechanism.

---

# Part 94 — Account Factory

Large enterprises automate:

```text
new cloud account
baseline IAM
network
logging
security controls
budgets
tags
```

instead of building each account manually.

---

# Part 95 — Golden Paths

Platform engineering principle:

```text
secure standard path
should be easier than
custom insecure path
```

IaC modules can expose:

```text
secure-web-app
secure-database
private-kubernetes-cluster
```

as approved building blocks.

---

# Part 96 — Self-Service Infrastructure

Developer request:

```text
Need PostgreSQL:
size = medium
environment = test
```

Platform module automatically handles:

```text
private networking
encryption
backup
monitoring
tags
policy
```

This gives speed without giving everyone cloud-admin rights.

---

# Part 97 — Service Catalog

Approved infrastructure modules can be exposed through:

```text
Git templates
developer portal
internal registry
cloud service catalog
Backstage-like platform
```

The developer consumes a product rather than low-level cloud APIs.

---

# Part 98 — Monorepo

One repository contains many stacks/modules.

Advantages:

```text
visibility
shared tooling
atomic changes
easy search
```

Disadvantages:

```text
permissions
large CI
ownership complexity
larger blast radius
```

---

# Part 99 — Multi-Repository

Separate repositories by:

```text
team
platform
service
state
```

Advantages:

```text
autonomy
smaller scope
simpler permissions
```

Disadvantages:

```text
cross-repo dependency coordination
version discovery
shared standards
```

---

# Part 100 — Repository Ownership

Use review ownership:

```text
network/    → network team
security/   → security team
production/ → platform + application owner
```

The repository itself is a governance boundary.

---

# Part 101 — Pull-Request Infrastructure Workflow

Recommended:

```text
branch
 ↓
change IaC
 ↓
format
 ↓
validate
 ↓
lint
 ↓
security scan
 ↓
plan
 ↓
review
 ↓
merge
 ↓
apply
 ↓
verify
```

This is the heart of enterprise IaC delivery.

---

# Part 102 — Plan in Pull Request

A PR should show infrastructure impact.

Example:

```text
+ create 2 private subnets
~ update firewall tags
- destroy 0
```

Reviewers should see plan, not only code diff.

---

# Part 103 — Apply After Merge

A strong workflow separates:

```text
proposal
approval
execution
```

`main` represents approved desired state.

A protected pipeline performs apply.

---

# Part 104 — Manual Approval

For production, approval can validate:

```text
change window
destructive operations
cost impact
security impact
backup readiness
business approval
```

Not every environment needs manual approval.

---

# Part 105 — Automated Apply

Good for:

```text
development
preview environments
low-risk ephemeral stacks
```

Production can also be fully automated if controls are mature.

Automation is not inherently unsafe; uncontrolled automation is.

---

# Part 106 — CI Identity

CI should authenticate using a machine identity.

Preferred:

```text
OIDC federation
managed identity
short-lived role
workload identity
```

Avoid permanent cloud keys stored as CI secrets.

---

# Part 107 — Short-Lived Credentials

Flow:

```text
CI system
 ↓ OIDC
cloud identity provider
 ↓
temporary role credentials
 ↓
IaC apply
```

Benefits:

```text
no permanent key
automatic expiration
better audit trail
```

---

# Part 108 — Least Privilege for Automation

Bad:

```text
all IaC pipelines use organization-admin
```

Better:

```text
network pipeline → network permissions
database pipeline → DB permissions
application pipeline → app resource permissions
```

Limit blast radius.

---

# Part 109 — Separation of Duties

Example:

```text
Developer writes change
Platform engineer reviews
Security policy validates
CI identity applies
Auditor reviews logs
```

No single human requires unrestricted end-to-end privilege.

---

# Part 110 — Formatting

Automated formatter ensures:

```text
consistent style
smaller diffs
less review noise
```

Formatting should be a CI requirement.

---

# Part 111 — Linting

Linting detects:

```text
syntax issues
deprecated constructs
unused values
bad conventions
provider-specific problems
```

before planning.

---

# Part 112 — Validation

Validation checks configuration structure and schemas.

It should run before any API-changing step.

Typical pipeline:

```text
format
↓
validate
↓
lint
↓
plan
```

---

# Part 113 — Static Security Analysis

Tools can inspect code for patterns:

```text
public storage
unencrypted database
0.0.0.0/0 SSH
missing audit logs
weak TLS
public Kubernetes API
```

This catches problems before deployment.

---

# Part 114 — Policy as Code

Policy expresses organization rules in machine-readable form.

Examples:

```text
Only approved regions
No public database
Encryption required
Required tags
Production deletion protection required
No Internet SSH
```

Policy can evaluate configuration or plan.

---

# Part 115 — Preventive Policy

Preventive control:

```text
violation
↓
pipeline fails
↓
apply blocked
```

Appropriate for high-risk requirements.

---

# Part 116 — Detective Policy

Detective control:

```text
violation deployed
↓
monitor detects
↓
alert/ticket
```

Useful where automatic blocking would disrupt necessary operations.

---

# Part 117 — Cloud Guardrails + IaC Policy

Combine:

```text
IaC policy
+
cloud organization policy
+
IAM
+
runtime security monitoring
```

Examples:

```text
AWS SCP
Azure Policy
GCP Organization Policy
Kubernetes admission
```

Defense in depth.

---

# Part 118 — Unit Testing

Test module logic without necessarily creating real infrastructure.

Examples:

```text
name output correct
validation rejects public CIDR
production enables backups
required tags always included
```

---

# Part 119 — Integration Testing

Create real temporary resources:

```text
deploy module
↓
query cloud API
↓
verify expected properties
↓
destroy
```

Example checks:

```text
disk encrypted
database private
port 22 closed
logging enabled
```

---

# Part 120 — End-to-End Testing

Provision a realistic environment and test application-level behavior.

Example:

```text
create VPC
create cluster
deploy test service
test ingress
test database path
destroy
```

More expensive but catches integration failures.

---

# Part 121 — Contract Testing

Reusable modules expose interfaces.

Test:

```text
input compatibility
output names
output types
default behaviors
```

Breaking a module output can break many repositories.

---

# Part 122 — Security Tests

Examples:

```text
no open management ports
encryption enabled
private endpoints
MFA/identity policies
flow logs enabled
backup configured
```

Security should be tested like functionality.

---

# Part 123 — Cost Tests

A plan can be checked for cost.

Example accidental change:

```text
instance_count = 10
→
instance_count = 100
```

A cost policy can block unexpected monthly increase.

---

# Part 124 — Drift Pipeline

Scheduled workflow:

```text
checkout approved main
↓
initialize
↓
refresh/plan
↓
unexpected change?
↓
notify owner
```

This detects console edits and external changes.

---

# Part 125 — Preview Environments

A PR can create temporary infrastructure.

```text
PR #152
 ↓
network
application
database
test URL
```

When PR closes:

```text
destroy preview stack
```

This improves realistic testing.

---

# Part 126 — TTL / Expiration

Temporary infrastructure should include:

```text
ExpiresAt
Owner
PullRequest
Environment=Temporary
```

Cleanup automation can delete expired resources.

Without this, cloud costs grow silently.

---

# Part 127 — Pipeline Concurrency

Only one apply should modify one state at a time.

Use:

```text
state lock
CI concurrency group
environment lock
```

Locking at both IaC and pipeline levels is strong defense.

---

# Part 128 — Cancelled Apply

If a pipeline is cancelled mid-apply:

```text
some resources may already exist
state may have partial updates
```

Recovery:

```text
do not manually guess
run fresh plan
inspect state/live resources
continue safely
```

---

# Part 129 — Pipeline Evidence

Retain:

```text
commit SHA
plan
policy results
security scans
cost estimate
approval
apply logs
```

This creates change evidence.

---

# Part 130 — Protected Branches

Production IaC repository should commonly use:

```text
no direct push to main
mandatory reviews
required CI
CODEOWNERS
restricted admin bypass
```

---

# Part 131 — Emergency Change Process

Sometimes manual cloud changes are necessary during an incident.

Correct follow-up:

```text
contain incident
↓
record manual change
↓
update IaC immediately
↓
plan
↓
restore code/live alignment
```

Otherwise drift becomes permanent.

---

# Part 132 — Break-Glass Access

Emergency infrastructure credentials should be:

```text
strongly protected
MFA enforced
time-limited
audited
rarely used
post-reviewed
```

Break-glass is not daily administration.

---

# Part 133 — Secrets in IaC

Never commit:

```text
password
API key
private key
cloud credential
database secret
```

to IaC repositories.

Git history retains deleted secrets.

---

# Part 134 — Secret References

Better:

```text
IaC references secret ID
runtime/application reads secret
```

Example:

```text
secret manager object
↓
application workload identity
↓
secret retrieved at runtime
```

---

# Part 135 — Secret Creation vs Secret Value

IaC can safely manage:

```text
secret container/resource
permissions
rotation policy
```

while the secret value may be supplied separately.

Separate lifecycle where possible.

---

# Part 136 — Sensitive Variables Are Not Encryption

A tool may hide sensitive output.

But the value may still exist in:

```text
state
provider request
logs
memory
backend
```

Use real secret-management controls.

---

# Part 137 — State and Secret Exposure

Because state may store sensitive values:

```text
encrypt backend
restrict access
enable audit
avoid broad read permissions
```

Do not store production state in a public repository.

---

# Part 138 — Environment Variable Secrets

CI often passes secrets through environment variables.

Risks:

```text
debug output
process environment
crash dump
misconfigured logging
```

Prefer workload identity and secret files/API where available.

---

# Part 139 — Provider Credentials

Best:

```text
federated short-lived credentials
```

Acceptable depending on platform:

```text
managed identity
service account
temporary token
```

Avoid hardcoded static access keys.

---

# Part 140 — Provider Supply Chain

IaC downloads executable provider/plugin code.

Risks:

```text
compromised release
typosquatted provider
untrusted source
unexpected upgrade
```

Use trusted registries, lock files, version pinning, integrity verification.

---

# Part 141 — Module Supply Chain

Third-party modules are code.

Review:

```text
source
maintainer
permissions/resources
version
license
security history
```

Do not install unknown module directly into production.

---

# Part 142 — Dependency Locking

Record exact provider/module versions where possible.

Purpose:

```text
developer
CI
production
```

should use the same dependency version unless intentionally upgraded.

---

# Part 143 — Provider Upgrade

Workflow:

```text
review changelog
update version
initialize lock
run tests
plan dev
apply dev
promote
```

Never casually upgrade all providers during unrelated production change.

---

# Part 144 — Module Upgrade

A new module version may change:

```text
resource names
defaults
outputs
lifecycle
```

Always plan in representative environment.

---

# Part 145 — Infrastructure Rollback Is Different From Application Rollback

Application rollback:

```text
deploy old container version
```

Infrastructure rollback can be dangerous.

Example:

```text
database engine upgraded
```

Changing code to old version may not support downgrade.

Therefore rollback may mean:

```text
restore backup
replace infrastructure
fail over
forward fix
```

not simply `git revert`.

---

# Part 146 — Git Revert Does Not Guarantee Infrastructure Revert

`git revert` only changes desired code.

The provider may not support reversing the change.

Always plan the reverted code before applying.

---

# Part 147 — Backup Before Destructive Change

Before:

```text
database replacement
storage change
cluster rebuild
network migration
```

verify:

```text
backup exists
restore tested
RPO/RTO acceptable
```

---

# Part 148 — Blue/Green Infrastructure

Create replacement environment:

```text
Blue current
Green new
```

Test Green.

Then move:

```text
DNS/load balancer
Blue → Green
```

Rollback can move traffic back while Blue remains.

---

# Part 149 — Canary Infrastructure Change

Change a small subset first:

```text
1 node pool
1 region
1 account
```

observe before broad rollout.

Useful for:

```text
new VM image
security agent
network config
Kubernetes node configuration
```

---

# Part 150 — Blast Radius

Every state/module/pipeline has a blast radius.

Examples:

```text
application stack → one service
network core → entire environment
identity stack → organization-wide
```

Apply stronger controls as blast radius increases.

---

# Part 151 — Change Windows

High-impact infrastructure should be scheduled when:

```text
owners available
monitoring active
rollback/recovery possible
business impact acceptable
```

IaC automation does not eliminate operational change management.

---

# Part 152 — Infrastructure Observability

After apply, verify infrastructure.

Monitor:

```text
resource health
API errors
network reachability
logs
metrics
cost
security findings
```

`apply succeeded` is not the same as `service is healthy`.

---

# Part 153 — Post-Apply Verification

Pipeline should verify:

```text
resources reachable
health checks pass
DNS works
policy remains compliant
monitoring receives data
```

Example:

```bash
curl -f https://service.example/health
```

---

# Part 154 — Infrastructure Smoke Tests

Examples:

```text
private subnet has no direct Internet route
load balancer returns 200
database not publicly reachable
DNS resolves
Kubernetes node Ready
backup policy attached
```

---

# Part 155 — Infrastructure SLO

Platform can define SLOs:

```text
provisioning success rate
average environment creation time
drift remediation time
change failure rate
state-backend availability
```

IaC itself becomes an internal platform service.

---

# Part 156 — AWS IaC Example

Architecture:

```text
VPC
├── public subnets
├── private subnets
├── route tables
├── NAT
├── load balancer
├── compute
└── database
```

IaC should encode:

```text
CIDRs
AZ distribution
security groups
encryption
logging
backup
tags
```

---

# Part 157 — Azure IaC Example

Architecture:

```text
Resource Group
  ↓
VNet
├── ApplicationSubnet
├── DatabaseSubnet
└── PrivateEndpoints
```

IaC can also manage:

```text
Managed Identity
NSGs
Key Vault
Azure Monitor
Private DNS
AKS
```

---

# Part 158 — Google Cloud IaC Example

Architecture:

```text
Project
 ↓
VPC
 ↓
regional subnets
 ↓
firewall policy
 ↓
GKE / Compute / Cloud SQL
```

IaC must consider:

```text
project APIs
IAM
service accounts
organization policies
billing
```

---

# Part 159 — Kubernetes IaC

Kubernetes manifests are themselves declarative infrastructure definitions.

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
```

Kubernetes continuously reconciles desired state.

This is conceptually IaC/GitOps.

---

# Part 160 — Terraform Managing Kubernetes

Possible architecture:

```text
Terraform
 ↓
create Kubernetes cluster
 ↓
Kubernetes provider
 ↓
create namespaces/basic platform objects
```

But large application deployments may be better delegated to Helm/GitOps.

Avoid one giant state managing cloud + every application object.

---

# Part 161 — OpenShift IaC

IaC can create/manage:

```text
cloud infrastructure
DNS
load balancers
OpenShift cluster prerequisites
projects
quotas
RBAC
Operators
platform configuration
```

But respect OpenShift Operator-owned resources.

Configure the correct source-of-truth API.

---

# Part 162 — VMware IaC

IaC can manage:

```text
VMs
templates
networks
datastores
resource pools
tags
```

through vSphere provider/API.

Golden templates improve reproducibility.

---

# Part 163 — OpenStack IaC

IaC can manage:

```text
networks
subnets
routers
security groups
instances
volumes
load balancers
```

through OpenStack APIs.

---

# Part 164 — Terraform / OpenTofu Concept

General-purpose declarative provisioning engines using HCL-style configuration and provider ecosystem.

Core model:

```text
configuration
provider
state
plan
apply
modules
```

Course 63 will go deep into Terraform.

---

# Part 165 — CloudFormation

AWS-native declarative provisioning.

Strengths:

```text
deep AWS integration
AWS-managed service
change sets
stack lifecycle
```

Scope:

```text
primarily AWS
```

---

# Part 166 — Azure Bicep

Azure-native declarative language over ARM.

Model:

```text
Bicep
↓ compile
ARM template
↓
Azure Resource Manager
```

Strong choice for Azure-native teams.

---

# Part 167 — Pulumi

Uses general-purpose languages such as:

```text
Python
TypeScript
Go
C#
```

to define infrastructure while maintaining desired-state/state concepts.

Benefit:

```text
real programming language
```

Trade-off:

```text
more programming complexity
```

---

# Part 168 — Ansible

Primarily configuration management/orchestration.

Can provision infrastructure using cloud modules, but model is generally task-driven rather than Terraform-style resource graph/state lifecycle.

Good combination:

```text
Terraform → provision
Ansible → configure
```

---

# Part 169 — Helm

Helm manages Kubernetes application packages.

It is not a general cloud-provisioning tool.

Use for:

```text
Kubernetes application/platform releases
```

not VPC creation.

---

# Part 170 — Kustomize

Transforms Kubernetes YAML through overlays.

```text
base
+
dev overlay
+
prod overlay
```

Good for Kubernetes configuration reuse.

---

# Part 171 — GitOps

GitOps controllers such as Argo CD continuously reconcile Kubernetes/OpenShift desired state.

Possible combination:

```text
Terraform → cluster/infrastructure
Argo CD → cluster applications/platform configuration
```

---

# Part 172 — Tool Selection Principle

Choose based on lifecycle ownership.

Questions:

```text
What API?
Who owns lifecycle?
Does resource need state?
Does it need continuous reconciliation?
Does team know the language?
How large is ecosystem?
How is secret/state managed?
```

Do not choose a tool because it is fashionable.

---

# Part 173 — One Tool for Everything Anti-Pattern

A single state managing:

```text
organization IAM
network
database
Kubernetes
500 application Deployments
DNS
CI
```

creates huge blast radius and slow plans.

Split by lifecycle and ownership.

---

# Part 174 — Multi-Tool Architecture

Example:

```text
Terraform
  ↓
cloud foundation
  ↓
Ansible
  ↓
special VM configuration

Terraform
  ↓
Kubernetes cluster
  ↓
Argo CD
  ↓
Helm / Kubernetes manifests
```

Each tool owns a clear layer.

---

# Part 175 — Brownfield Adoption

Existing organization often has:

```text
manual infrastructure
scripts
old templates
unmanaged resources
```

Migration process:

```text
inventory
classify ownership
write IaC
import
plan
fix differences
lock manual changes
```

Do not rewrite everything at once.

---

# Part 176 — Infrastructure Inventory

Before migration collect:

```text
resource type
ID
owner
environment
criticality
dependencies
data
backup
current config
```

Unknown ownership is a migration risk.

---

# Part 177 — Prioritize Brownfield Migration

Start with:

```text
low-risk repeatable resources
new environments
shared modules
noncritical services
```

Delay high-risk legacy databases until tooling/process is proven.

---

# Part 178 — Greenfield Advantage

New environment can be IaC-first.

Rule:

```text
No production resource without code ownership.
```

This prevents drift from day one.

---

# Part 179 — Manual Console Access Policy

Options:

```text
read-only console for developers
write access limited to break-glass/admin
changes through PR
```

The stricter the console access, the easier drift control becomes.

---

# Part 180 — Infrastructure Coding Standards

Standardize:

```text
file layout
naming
variables
outputs
tags
module versioning
provider pinning
state layout
documentation
```

Consistency improves review and onboarding.

---

# Part 181 — Documentation Standards

Every stack should document:

```text
purpose
owner
architecture
dependencies
state backend
apply workflow
destroy policy
recovery
contacts
```

---

# Part 182 — Architecture Decision Records

ADR example:

```text
ADR-004:
Use separate production account and state

Reason:
blast radius + compliance

Alternatives:
workspace in shared account

Consequences:
more account management
```

IaC code says what; ADR says why.

---

# Part 183 — Runbooks

IaC does not replace operations.

Runbooks should cover:

```text
state lock stuck
state recovery
provider outage
failed apply
import
drift
destroy mistake
credential failure
```

---

# Part 184 — Provider API Outage

If cloud API is unavailable:

```text
plan may fail
apply may partially fail
reads may timeout
```

Do not repeatedly rerun destructive operations blindly.

Wait for provider recovery, then refresh/plan.

---

# Part 185 — Authentication Failure

Symptoms:

```text
401
403
AccessDenied
Unauthorized
```

Investigate:

```text
identity
token expiry
role assumption
scope
policy
subscription/account
```

not code syntax first.

---

# Part 186 — Authorization Failure

The CI identity may authenticate but lack one action.

Example:

```text
can create VM
cannot create IAM role
```

Fix least-privilege policy deliberately.

Do not grant administrator as a quick solution.

---

# Part 187 — Quota Failure

Examples:

```text
vCPU quota reached
public IP limit
VPC limit
database quota
```

Plan may be valid while provider rejects apply.

Monitor quotas before large changes.

---

# Part 188 — Naming Collision

Resource with required globally unique name already exists.

Solutions:

```text
naming strategy
random/suffix design
import existing object
different scope
```

Do not endlessly retry same invalid name.

---

# Part 189 — Dependency Cycle Failure

Engine reports cycle.

Fix architecture:

```text
separate resource rules
break mutual references
use data/output boundary
```

Avoid explicit dependencies that create more cycles.

---

# Part 190 — State Lock Failure

If job crashes and lock remains:

```text
1. Confirm no active apply.
2. Identify lock owner.
3. Use supported unlock command.
4. Run plan.
```

Never force-unlock active state.

---

# Part 191 — State Drift Failure

Unexpected large plan:

```text
50 updates
10 replacements
```

Before applying:

```text
check provider version
check state/backend
check manual changes
check imported resources
check defaults
```

---

# Part 192 — Provider Upgrade Surprise

A provider update can change default/schema behavior and produce unexpected plan.

This is why provider version pinning and lock files matter.

---

# Part 193 — Module Upgrade Surprise

A module update can internally rename resources.

Result:

```text
destroy old
create new
```

even when architecture appears unchanged.

Review module changelog and plan.

---

# Part 194 — Secret Leak Incident

If secret is committed:

```text
1. Revoke/rotate immediately.
2. Remove from code.
3. Clean Git history if policy requires.
4. Scan forks/artifacts/logs.
5. Replace with secret manager.
```

Deleting the latest commit alone is insufficient.

---

# Part 195 — Accidental Destroy

Response:

```text
stop further applies
identify affected resources/data
restore from backup
recreate infrastructure
recover state
validate DNS/network/data
perform incident review
```

Prevent with deletion protection and approval policy.

---

# Part 196 — Production State Lost

Recovery:

```text
state backend version history
backup
live inventory
import
refresh
plan
```

Do not initialize a blank production state and immediately apply.

---

# Part 197 — Repository Lost

Git should be backed by remote enterprise repository.

Recovery needs:

```text
Git history
module artifacts
state
provider locks
variables
documentation
```

IaC repository is critical operational data.

---

# Part 198 — State vs Code Disaster Recovery

Both are needed:

```text
Code:
what should exist

State:
what code owns

Cloud:
what actually exists
```

DR requires reconciling all three.

---

# Part 199 — Infrastructure DR Strategy

A resilient platform should be able to rebuild:

```text
network
compute
Kubernetes
load balancers
IAM configuration
monitoring
```

from code.

Application data restoration is a separate requirement.

---

# Part 200 — RPO and RTO for IaC

Examples:

```text
State RPO:
near-zero via versioned remote backend

IaC repository RPO:
near-zero via hosted Git

Environment rebuild RTO:
2 hours

Database RTO:
30 minutes from backup/failover
```

Measure recovery rather than assuming automation makes it fast.

---

# Part 201 — Testing Disaster Recovery

Run exercises:

```text
restore state copy
rebuild test environment
recreate networking
recover secrets/config
validate application
```

A DR plan not tested is only documentation.

---

# Part 202 — Enterprise IaC Layers

A mature organization may structure:

```text
Layer 0: Organization / accounts
Layer 1: Network / identity / security
Layer 2: Shared platform
Layer 3: Kubernetes / compute / databases
Layer 4: Application infrastructure
Layer 5: Application deployment
```

Each layer has distinct ownership and state.

---

# Part 203 — Platform Team Responsibilities

Platform team can own:

```text
module standards
CI templates
state backend
security policy
provider versions
landing zones
shared networking
documentation
```

Application teams consume approved interfaces.

---

# Part 204 — Security Team Responsibilities

Security team can define machine-enforced policies:

```text
encryption
public exposure
IAM boundaries
logging
approved regions
data residency
required tags
```

without manually reviewing every resource.

---

# Part 205 — Application Team Responsibilities

Application teams should control what they understand:

```text
service sizing
application load balancer rules
queue/database capacity
environment variables
application-specific resources
```

within platform guardrails.

---

# Part 206 — Centralized IaC Model

One central team applies all infrastructure.

Advantages:

```text
consistency
strong control
```

Disadvantages:

```text
bottleneck
slow delivery
weak product ownership
```

---

# Part 207 — Federated IaC Model

Platform defines standards/modules/pipelines.

Product teams own their stacks.

Advantages:

```text
speed
ownership
scalability
```

Requires strong automated policy and documentation.

---

# Part 208 — Multi-Cloud IaC

A common language can manage:

```text
AWS
Azure
GCP
Kubernetes
```

but multi-cloud does not automatically create portability.

Each provider still has unique:

```text
networking
IAM
database
load balancer
services
```

Avoid lowest-common-denominator architecture unless necessary.

---

# Part 209 — Abstraction Leakage

A "generic cloud database" module eventually encounters provider differences:

```text
backup
HA
replicas
networking
engine support
maintenance
```

Good modules expose meaningful platform differences instead of pretending they do not exist.

---

# Part 210 — Policy for Multi-Cloud

Central rules can still be common:

```text
encryption required
owner tag required
public database forbidden
logging required
approved regions
```

Implementation may differ by provider.

---

# Part 211 — IaC and Compliance

IaC supports compliance by providing:

```text
repeatable controls
review evidence
version history
policy results
change logs
configuration baselines
```

It does not automatically make an environment compliant.

---

# Part 212 — Evidence Generation

A pipeline can archive:

```text
plan
policy pass
security scan
approver
commit
apply result
```

for audit evidence.

---

# Part 213 — Data Classification

Infrastructure modules can require:

```text
DataClassification = Public|Internal|Confidential|Restricted
```

and select:

```text
encryption
backup
network isolation
logging
region
```

accordingly.

---

# Part 214 — Policy Exceptions

Sometimes a rule needs exception.

Good process:

```text
document reason
owner
expiration
approval
scope
compensating control
```

Never create permanent hidden bypass.

---

# Part 215 — Policy Versioning

Policy as code is software.

Version it.

```text
policy v3
↓
tested
↓
warn mode
↓
enforce
```

Avoid sudden organization-wide breakage.

---

# Part 216 — IaC Metrics

Useful engineering metrics:

```text
deployment frequency
change failure rate
mean apply duration
plan failure rate
drift incidents
recovery time
policy violations
module adoption
```

---

# Part 217 — Change Failure Rate

Infrastructure change failure:

```text
rollback
incident
manual repair
failed apply
availability impact
```

Track causes and improve modules/tests.

---

# Part 218 — Lead Time

Measure:

```text
PR opened
→
production infrastructure available
```

IaC should reduce lead time without weakening controls.

---

# Part 219 — Standard Module Adoption

If teams bypass standard modules, ask why.

Possible issues:

```text
module too rigid
poor documentation
slow release
missing feature
bad developer experience
```

A platform must be useful, not only restrictive.

---

# Part 220 — When IaC Is the Wrong Tool

Do not force IaC for every temporary investigative action.

Examples:

```text
read-only troubleshooting
one-time packet capture
temporary diagnostics
interactive performance test
```

But persistent changes should return to code.

---

# Part 221 — Configuration Data vs Infrastructure Code

Do not mix enormous application configuration into infrastructure modules.

Separate:

```text
infrastructure
platform config
application config
secrets
```

according to lifecycle.

---

# Part 222 — Generated Code

Generated IaC can improve consistency but creates risk if humans cannot understand output.

Rule:

```text
generated
must still be reviewable
testable
versioned
```

Do not deploy opaque AI-generated infrastructure directly.

---

# Part 223 — AI-Assisted IaC

AI can help:

```text
generate skeleton
explain plan
write tests
review policy
document modules
```

But AI can also invent:

```text
unsupported attributes
insecure defaults
wrong APIs
destructive lifecycle
```

Always validate against provider schemas and plans.

---

# Part 224 — IaC Code Review Checklist

Reviewer should ask:

```text
What resources change?
Any destroy/replace?
Any public exposure?
Any IAM expansion?
Any secret?
Any provider/module upgrade?
Any cost increase?
Any backup impact?
Any state move/import?
```

---

# Part 225 — Network Change Review

For network changes verify:

```text
CIDR overlap
routes
NAT
firewall
DNS
VPN/transit
MTU
availability zones
```

A small route change can have huge blast radius.

---

# Part 226 — IAM Change Review

IAM review:

```text
principal
resource
actions
conditions
scope
cross-account trust
expiration
```

Look especially for:

```text
*
admin
wildcard resource
```

---

# Part 227 — Database Change Review

Check:

```text
replacement?
backup?
replication?
maintenance window?
encryption?
storage shrink?
engine version?
```

Database changes deserve stronger approval.

---

# Part 228 — Kubernetes Cluster Change Review

Check:

```text
version
node pools
CNI
CSI
API endpoint
CIDRs
control plane
upgrade path
PDB/capacity
```

IaC apply must respect Kubernetes lifecycle.

---

# Part 229 — Cost Review

Infrastructure code can create expensive mistakes instantly.

Review:

```text
instance size
replica count
NAT gateways
cross-region traffic
premium disks
managed databases
log retention
```

---

# Part 230 — Destruction Review

Before destroy:

```text
Is resource stateful?
Is backup valid?
Who depends on output?
Is DNS referencing it?
Is another stack consuming it?
```

---

# Part 231 — Environment Destroy Strategy

For ephemeral environment:

```text
automatic destroy
```

For production:

```text
destroy disabled or heavily approved
```

Different environments deserve different controls.

---

# Part 232 — State Backend Architecture

Production backend should provide:

```text
high durability
encryption
locking
versioning
access control
audit
backup
```

Course 64 will explore remote state deeply.

---

# Part 233 — Backend Bootstrap Problem

Question:

```text
What creates the backend that stores the state used to create infrastructure?
```

Usually solve with:

```text
small bootstrap stack
manual one-time guarded setup
separate foundation repository
IaC service platform
```

Document it explicitly.

---

# Part 234 — Backend Chicken-and-Egg Pattern

Example:

```text
bootstrap/
  creates state bucket
  creates lock mechanism
  creates KMS
  creates CI role
```

Then normal stacks use that backend.

Keep bootstrap changes rare.

---

# Part 235 — Locking and CI

Even if state backend has lock, configure CI:

```text
one production apply at a time
```

This improves user feedback and reduces contention.

---

# Part 236 — State Access Roles

Example:

```text
developer:
read code
run local validation
no prod state read

CI plan:
read state

CI apply:
read/write state + cloud changes

platform admin:
emergency state operations
```

---

# Part 237 — Sensitive State Segmentation

Highly sensitive stacks:

```text
identity
secrets
KMS
organization
```

may use separate backend/account and stricter access than ordinary application stacks.

---

# Part 238 — Remote State Coupling Risk

Directly reading another stack's entire state exposes implementation details and possibly secrets.

Prefer:

```text
published outputs
parameter store
service catalog
provider data lookup
```

for stable interfaces.

---

# Part 239 — Environment Configuration Repository

Some organizations separate:

```text
module source
from
environment composition
```

Example:

```text
modules repo
+
live environments repo
```

This allows module releases and controlled environment promotion.

---

# Part 240 — Lock File

Dependency lock file records selected provider versions/checksums.

Commit it when recommended by tool.

This improves deterministic CI and supply-chain integrity.

---

# Part 241 — Version Constraint

Examples conceptually:

```text
>= 5.0, < 6.0
exact 5.4.2
~> compatible minor
```

Choose constraints based on upgrade process.

---

# Part 242 — Pinning Everything Forever Is Also Bad

Never upgrading means:

```text
security vulnerabilities
unsupported APIs
old cloud features
technical debt
```

Use controlled regular dependency upgrades.

---

# Part 243 — Upgrade Cadence

Example:

```text
monthly provider review
quarterly module major review
immediate critical security patch
```

Automation keeps upgrades predictable.

---

# Part 244 — Sandbox Before Production

Test changes in:

```text
unit
ephemeral test
dev
stage
production
```

especially provider/module upgrades.

---

# Part 245 — Failure Injection

Test IaC operational resilience:

```text
kill CI apply
remove permission
simulate API throttle
restore state version
create drift
```

Learn recovery before production incident.

---

# Part 246 — IaC Threat Model

Assets:

```text
cloud credentials
state
repository
CI runner
provider plugins
modules
plan
backend
```

Attack paths:

```text
malicious PR
stolen CI token
compromised provider/module
state theft
secret leak
pipeline bypass
```

---

# Part 247 — Malicious Pull Request

A PR can look harmless while adding:

```text
new IAM admin role
public storage
external network egress
credential output
```

Require code review + policy as code.

---

# Part 248 — Compromised CI Runner

If CI runner controls production credentials, runner compromise can become cloud compromise.

Use:

```text
ephemeral runners
short-lived identity
network restrictions
least privilege
runner hardening
```

---

# Part 249 — Provider Integrity

Use:

```text
official registry
checksums/signatures where supported
lock file
restricted plugin sources
```

Do not download arbitrary providers from random URLs.

---

# Part 250 — Module Integrity

Production module should come from:

```text
trusted repository
versioned release
reviewed code
CI-tested artifact
```

Not an unreviewed copy from a blog.

---

# Part 251 — Plan Security

Plans can contain:

```text
resource names
IP addresses
secret values
internal topology
```

Treat plan artifacts as potentially sensitive.

---

# Part 252 — Pipeline Logs

Logs can accidentally expose:

```text
environment variables
tokens
provider debug output
state snippets
```

Protect and redact logs.

---

# Part 253 — Debug Logging

Provider debug logging can be extremely verbose and may include sensitive request/response data.

Enable only temporarily in protected environment.

---

# Part 254 — Drift as Security Signal

Unexpected drift can indicate:

```text
manual error
unauthorized change
compromised credential
another automation
```

Security monitoring should treat critical drift seriously.

---

# Part 255 — Destroy as Security Capability

An attacker with IaC apply permissions may destroy infrastructure even if they cannot directly log into servers.

Protect IaC automation as privileged infrastructure control.

---

# Part 256 — IaC Maturity Model

Level 0:

```text
manual
```

Level 1:

```text
scripts
```

Level 2:

```text
IaC files + local state
```

Level 3:

```text
remote state + PR + CI
```

Level 4:

```text
modules + policy + testing + drift
```

Level 5:

```text
self-service platform + governance + observability + DR
```

---

# Part 257 — Production IaC Definition of Done

A production stack is not finished until it has:

```text
Git ownership
remote state
locking
provider lock
documentation
plan pipeline
security checks
approval model
backup/DR
drift detection
runbook
```

---

# Part 258 — Fundamental Troubleshooting Framework

Always determine which layer failed:

```text
Code syntax
↓
Validation
↓
Provider/plugin
↓
Authentication
↓
Authorization
↓
State
↓
Dependency graph
↓
Cloud API
↓
Resource operation
↓
Post-apply health
```

Do not debug the wrong layer.

---

# Part 259 — Evidence-Driven Troubleshooting

Collect:

```text
exact error
plan
state/backend status
provider version
module version
identity
cloud audit logs
resource events
recent changes
```

Then form a hypothesis.

---

# Part 260 — Final IaC Mental Model

A production IaC system is not a collection of `.tf`, YAML, or code files.

It is an operating system for infrastructure change:

```text
Git
+
Modules
+
State
+
Providers
+
Plan
+
Policy
+
Identity
+
CI/CD
+
Testing
+
Drift Detection
+
Backup / Recovery
+
Governance
```

The next courses will implement these fundamentals concretely with Terraform and remote state management.

---

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Manual vs IaC Workflow

Create a comparison document:

```text
Manual VPC creation
vs
IaC VPC creation
```

Compare:

```text
repeatability
audit
speed
drift
rollback
review
```

---

### Lab 2 — Desired vs Actual State

Given:

```text
Desired:
3 servers
HTTPS only

Actual:
2 servers
HTTPS + SSH public
```

Write the expected remediation plan.

---

### Lab 3 — Declarative vs Imperative

Write imperative pseudocode:

```text
create network
create subnet
create server
```

Then rewrite as desired-state configuration.

Explain which dependencies the engine can infer.

---

### Lab 4 — Idempotency

Design two scripts:

```text
non-idempotent user creation
idempotent user creation
```

Explain why the second is safer for automation.

---

### Lab 5 — Dependency Graph

Draw:

```text
VPC
├─ public subnet
│   └─ load balancer
└─ private subnet
    ├─ app server
    └─ database
```

Mark implicit dependencies.

---

### Lab 6 — Dependency Cycle

Given:

```text
SecurityGroupA → SecurityGroupB
SecurityGroupB → SecurityGroupA
```

redesign the rules to remove the cycle.

---

### Lab 7 — State Mapping

Create a table:

```text
Logical Address | Physical ID | Owner | Environment
```

for ten imaginary resources.

Explain why state is needed.

---

### Lab 8 — State Loss Tabletop

Scenario:

```text
state file deleted
cloud resources still exist
```

Write a safe recovery sequence.

---

### Lab 9 — State Lock Incident

Scenario:

```text
CI job crashed while holding lock
```

Write:

```text
verification
unlock criteria
post-unlock plan
```

---

### Lab 10 — Plan Review

Review hypothetical plan:

```text
+ 4 resources
~ 3 resources
-/+ database
- 1 KMS key
```

Identify which changes require immediate investigation.

---

### Lab 11 — Import Existing Resource

Design the full process to adopt an existing manually created network.

Do not skip the post-import no-op plan.

---

### Lab 12 — Resource Rename

Explain why:

```text
network.main
→
module.network.network.main
```

can cause recreation without state migration.

Design the safe move.

---

### Lab 13 — Variable Design

Design variables for a reusable web environment:

```text
environment
region
CIDR
replicas
instance size
public access
```

Add validation.

---

### Lab 14 — Safe Defaults

Review:

```text
allow_public_ssh = true
database_public = true
backup_enabled = false
```

replace with safer defaults.

---

### Lab 15 — Module Interface

Design:

```text
secure_database module
```

Inputs:

```text
engine
size
environment
subnet IDs
```

Outputs:

```text
endpoint
port
resource ID
```

List controls that should remain internal.

---

### Lab 16 — Module Versioning

Create release sequence:

```text
1.0.0
1.1.0
1.1.1
2.0.0
```

Classify:

```text
bug fix
new optional input
breaking output rename
```

---

### Lab 17 — Environment Separation

Design:

```text
dev
stage
prod
```

with:

```text
separate account
state
CI identity
variables
approval
```

---

### Lab 18 — Repository Architecture

Compare:

```text
monorepo
multi-repo
```

for an organization with:

```text
network team
security team
5 application teams
```

Choose one and justify.

---

### Lab 19 — Tagging Standard

Design mandatory metadata:

```text
Owner
Application
Environment
CostCenter
DataClassification
ManagedBy
Repository
```

Create a policy rule for missing tags.

---

### Lab 20 — Pull Request Pipeline

Design:

```text
format
validate
lint
security
test
plan
cost
policy
review
merge
apply
verify
```

Specify which steps may access production credentials.

---

### Lab 21 — OIDC CI Identity

Draw:

```text
GitHub/GitLab/Azure DevOps
 ↓ OIDC
Cloud IAM
 ↓
Temporary Role
 ↓
IaC Apply
```

Explain why this is safer than static access keys.

---

### Lab 22 — Least Privilege

Create permission matrix:

```text
Network pipeline
Database pipeline
Application pipeline
```

Determine what each must not be able to modify.

---

### Lab 23 — Policy as Code

Write pseudocode rules:

```text
deny if database.public == true
deny if ssh.cidr == 0.0.0.0/0
deny if encryption == false
deny if Owner tag missing
```

---

### Lab 24 — Security Static Analysis

Review an intentionally insecure pseudo-architecture:

```text
public DB
unencrypted disk
Internet SSH
no logs
admin IAM
```

Identify all findings.

---

### Lab 25 — Integration Test

Design a test that provisions a temporary network/module and verifies:

```text
encryption
private subnet
HTTPS
logging
```

then destroys it.

---

### Lab 26 — Cost Guardrail

Scenario:

```text
worker_count changes 5 → 100
database tier changes standard → premium
```

Design cost-policy response.

---

### Lab 27 — Drift Detection

Scenario:

```text
engineer manually opens SSH
```

Show how scheduled plan detects it and define remediation workflow.

---

### Lab 28 — Emergency Change

Scenario:

```text
production incident requires temporary firewall rule
```

Design:

```text
break-glass
manual containment
expiration
Git reconciliation
review
removal
```

---

### Lab 29 — Secret Leak

Scenario:

```text
cloud API key committed to Git
```

Write incident response.

Include:

```text
rotation
history
CI artifacts
logs
repository access
replacement design
```

---

### Lab 30 — Provider Upgrade

Design a safe provider upgrade:

```text
review notes
lock update
test
dev plan
dev apply
stage
prod
```

---

### Lab 31 — Module Upgrade

Given module 2.0 changes resource addresses, design migration without recreation.

---

### Lab 32 — Blue/Green Infrastructure

Design:

```text
Blue production
Green new version
```

including:

```text
data strategy
traffic switch
health checks
rollback
```

---

### Lab 33 — Brownfield Migration

Inventory:

```text
20 VMs
3 networks
2 DBs
1 Kubernetes cluster
manual IAM
```

Create migration waves from lowest to highest risk.

---

### Lab 34 — Landing Zone

Design a landing zone with:

```text
identity
network
logging
security
billing
budgets
policy
```

Mark which teams own each layer.

---

### Lab 35 — Self-Service Platform

Create a developer request:

```text
new web service
environment=dev
database=yes
```

Map to internal modules and policies.

---

### Lab 36 — AWS Architecture Mapping

Map an AWS web architecture into logical IaC modules:

```text
network
security
compute
database
DNS
monitoring
```

Define outputs between modules.

---

### Lab 37 — Azure Architecture Mapping

Map:

```text
Resource Group
VNet
Subnets
NSGs
Key Vault
AKS
Private DNS
```

into state boundaries.

---

### Lab 38 — Google Cloud Architecture Mapping

Map:

```text
Project
VPC
Subnets
Firewall
GKE
Cloud SQL
IAM
```

into modules and environment boundaries.

---

### Lab 39 — Kubernetes IaC Boundary

Decide which of the following should be managed by Terraform versus GitOps:

```text
cluster
node pools
namespaces
Ingress controller
application Deployment
application ConfigMap
```

Justify.

---

### Lab 40 — OpenShift IaC Boundary

Design ownership for:

```text
cloud infrastructure
OpenShift installation
projects
quotas
Operators
application workloads
Routes
```

respecting Operator-managed resources.

---

### Lab 41 — State Backend Design

Design backend requirements:

```text
encryption
versioning
locking
audit
backup
least privilege
```

Do not implement tool-specific syntax yet.

---

### Lab 42 — Backend Bootstrap

Design a bootstrap stack that creates:

```text
state storage
lock
KMS key
CI role
audit logging
```

Explain how bootstrap itself is protected.

---

### Lab 43 — Disaster Recovery

Scenario:

```text
Git available
state corrupted
cloud infrastructure partially available
```

Create recovery decision tree.

---

### Lab 44 — Failed Apply Game Day

Simulate/tabletop:

```text
authentication failure
authorization failure
quota exceeded
provider timeout
partial resource creation
state lock
naming collision
```

For each write:

```text
Evidence
Root Cause
Recovery
Prevention
```

---

### Lab 45 — Full IaC Architecture Review

Review your final mini project using:

```text
state
dependencies
modules
security
identity
policy
CI/CD
testing
drift
cost
DR
ownership
```

---

## 6. Mini Project

# Mini Project — Enterprise Infrastructure as Code Operating Model

Design the IaC operating model for a company with:

```text
AWS
Azure
Google Cloud
Kubernetes
OpenShift
```

The goal is not to implement Terraform yet. The goal is to design **how infrastructure code will be organized, secured, reviewed, applied, and recovered**.

## Required Architecture

```text
                           Developers
                               |
                               v
                           Git Platform
                               |
                     Pull Request / Review
                               |
              +----------------+----------------+
              |                |                |
           Validate         Security          Tests
              |                |                |
              +----------------+----------------+
                               |
                              Plan
                               |
                          Policy / Cost
                               |
                            Approval
                               |
                               v
                         CI Apply Identity
                               |
       +-----------------------+-----------------------+
       |                       |                       |
      AWS                    Azure                    GCP
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                         Kubernetes / OCP
                               |
                          Application Teams
```

## Repository Design

Create:

```text
iac-platform/
├── bootstrap/
├── modules/
│   ├── network/
│   ├── database/
│   ├── kubernetes/
│   ├── identity/
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
├── policies/
├── tests/
├── docs/
└── runbooks/
```

## State Architecture

Design states:

```text
bootstrap
organization
network
identity
security
platform
database
application-infrastructure
```

For every state define:

```text
owner
backend
lock
read access
write identity
blast radius
backup
restore procedure
```

## Module Architecture

Required modules:

```text
secure-network
secure-database
private-kubernetes
standard-monitoring
application-load-balancer
```

Each module must document:

```text
inputs
outputs
security defaults
dependencies
versioning
upgrade policy
```

## Identity Model

No static personal production keys.

Design:

```text
Human:
SSO/MFA
read/plan permissions

CI:
OIDC federation
short-lived role

Break Glass:
strongly protected
audited
time-limited
```

## CI/CD Pipeline

Required:

```text
format
validate
lint
unit tests
security scan
plan
cost estimate
policy evaluation
human approval for prod
apply
post-apply verification
artifact retention
```

## Policy as Code

At minimum enforce:

```text
No public databases
No Internet SSH
Encryption required
Approved regions
Required tags
Production backup required
Production deletion protection
No wildcard admin IAM
```

## Drift

Design:

```text
scheduled daily/weekly plan
critical drift alert
owner routing
manual-change investigation
code reconciliation
```

## Security

Threat-model:

```text
Git compromise
CI compromise
provider/module compromise
state theft
secret leakage
malicious PR
unauthorized console change
```

Define controls for each.

## Disaster Recovery

Define:

```text
Git recovery
state recovery
backend recovery
cloud resource import
environment rebuild
application-data restore boundary
```

Set example:

```text
IaC repository RPO
state RPO
platform rebuild RTO
application RTO
```

## Required Documentation

```text
README.md
ARCHITECTURE.md
REPOSITORY_STRATEGY.md
STATE_STRATEGY.md
MODULE_STANDARD.md
IDENTITY.md
CI_CD.md
POLICY.md
SECURITY.md
DRIFT.md
COST_GOVERNANCE.md
DISASTER_RECOVERY.md
```

## Required ADRs

```text
ADR-001-State-Partitioning.md
ADR-002-Repository-Model.md
ADR-003-Environment-Separation.md
ADR-004-Module-Versioning.md
ADR-005-CI-Identity.md
ADR-006-Policy-Enforcement.md
ADR-007-Kubernetes-IaC-Boundary.md
ADR-008-Remote-State-Backend.md
```

## Required Runbooks

```text
RUNBOOK_STATE_LOCK.md
RUNBOOK_STATE_LOSS.md
RUNBOOK_FAILED_APPLY.md
RUNBOOK_PROVIDER_OUTAGE.md
RUNBOOK_AUTH_FAILURE.md
RUNBOOK_DRIFT.md
RUNBOOK_SECRET_LEAK.md
RUNBOOK_ACCIDENTAL_DESTROY.md
RUNBOOK_IMPORT.md
RUNBOOK_BREAK_GLASS.md
```

---

## 7. Recommended Resources

This course is designed to be self-contained for the fundamentals.

Optional official resources for deeper implementation later:

```text
HashiCorp Terraform documentation
OpenTofu documentation
AWS CloudFormation documentation
Microsoft Bicep documentation
Pulumi documentation
Ansible documentation
Kubernetes declarative configuration documentation
OpenShift GitOps / platform documentation
Cloud provider IAM and policy documentation
```

Course 63 will implement these principles in Terraform.

Course 64 will go deeply into remote state architecture, locking, collaboration, state migration, and recovery.

---

## 8. Certification Relevance

This course supports concepts used in:

```text
HashiCorp Terraform Associate-style knowledge
AWS cloud engineering
Azure administration / architecture
Google Cloud engineering
DevOps
Platform Engineering
SRE
Kubernetes administration
OpenShift administration
DevSecOps
Cloud Security
```

Certification exams may ask tool-specific syntax later, but this course gives the conceptual foundation behind:

```text
state
providers
resources
modules
variables
outputs
plan/apply
remote backends
drift
policy
CI/CD
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** IaC means "a script that creates servers."  
  **Best practice:** think desired state + lifecycle + state + dependency graph + controlled change.

- **Mistake:** Manually edit production after IaC adoption.  
  **Best practice:** return persistent changes to code immediately.

- **Mistake:** Store production state on one laptop.  
  **Best practice:** remote encrypted versioned state with locking.

- **Mistake:** Run two applies against one state.  
  **Best practice:** backend locking + CI concurrency controls.

- **Mistake:** Apply without reviewing plan.  
  **Best practice:** plan is a production change artifact.

- **Mistake:** Trust a no-error apply as proof of health.  
  **Best practice:** post-apply smoke tests and monitoring.

- **Mistake:** Put secrets in variables committed to Git.  
  **Best practice:** external secret systems and short-lived identity.

- **Mistake:** Give CI organization-admin.  
  **Best practice:** least-privilege stack-specific roles.

- **Mistake:** Use `latest` provider/module/image everywhere.  
  **Best practice:** controlled versions and lock files.

- **Mistake:** Upgrade provider during unrelated change.  
  **Best practice:** separate dependency upgrades.

- **Mistake:** Treat `git revert` as guaranteed infrastructure rollback.  
  **Best practice:** plan first and understand resource reversibility.

- **Mistake:** Import resource then immediately apply.  
  **Best practice:** adjust code until post-import plan is safe/no-op.

- **Mistake:** Put every resource into one giant state.  
  **Best practice:** split by ownership, lifecycle, and blast radius.

- **Mistake:** Create hundreds of tiny states.  
  **Best practice:** balance isolation with manageable dependencies.

- **Mistake:** Let multiple stacks own the same object.  
  **Best practice:** one clear owner.

- **Mistake:** Use a module with 150 flags.  
  **Best practice:** focused opinionated modules.

- **Mistake:** Assume module abstraction removes cloud differences.  
  **Best practice:** expose meaningful provider-specific behavior.

- **Mistake:** Treat policy as documentation only.  
  **Best practice:** enforce critical rules automatically.

- **Mistake:** Ignore drift because code is correct.  
  **Best practice:** scheduled drift detection.

- **Mistake:** Assume automation means DR is solved.  
  **Best practice:** test state recovery and environment rebuild.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is Infrastructure as Code?

**Answer:** Managing infrastructure through versioned machine-readable definitions and automated lifecycle tooling rather than undocumented manual changes.

### Q2. Declarative vs imperative?

**Answer:** Declarative states the desired result; imperative defines the sequence of actions.

### Q3. Desired state?

**Answer:** The infrastructure configuration that code says should exist.

### Q4. Actual state?

**Answer:** What currently exists in the real platform/provider.

### Q5. Idempotency?

**Answer:** Repeated execution produces the same intended result rather than duplicate changes.

### Q6. Convergence?

**Answer:** Moving actual state toward desired state.

### Q7. Drift?

**Answer:** Difference between IaC-managed desired state and live infrastructure.

### Q8. Provider?

**Answer:** Plugin/integration translating IaC resources into platform API operations.

### Q9. Resource?

**Answer:** One managed infrastructure object with lifecycle and identity.

### Q10. Dependency graph?

**Answer:** Directed relationships determining resource ordering.

### Q11. Implicit dependency?

**Answer:** Dependency inferred from one resource referencing another.

### Q12. Explicit dependency?

**Answer:** Manually declared ordering when no direct data reference expresses the real dependency.

### Q13. Why does state exist?

**Answer:** To map logical IaC objects to physical resources and track known attributes/lifecycle.

### Q14. Is state the actual infrastructure?

**Answer:** No; it is management metadata describing/mapping infrastructure.

### Q15. Why is state sensitive?

**Answer:** It can contain internal infrastructure details and sometimes secrets.

### Q16. Local state problem?

**Answer:** Weak collaboration, backup, locking, and centralized access control.

### Q17. Remote state benefit?

**Answer:** Shared durable state with locking, versioning, access control, and CI integration.

### Q18. State locking?

**Answer:** Prevents simultaneous writers from changing one state.

### Q19. Plan?

**Answer:** Preview of create/update/replace/destroy operations before apply.

### Q20. No-op plan?

**Answer:** Desired and managed actual state match with no changes required.

### Q21. Import?

**Answer:** Adopt an existing external resource into IaC state management.

### Q22. Why plan after import?

**Answer:** To ensure code accurately represents existing resource and will not unintentionally change it.

### Q23. Module?

**Answer:** Reusable infrastructure component exposing inputs/outputs and hiding implementation details.

### Q24. Module versioning importance?

**Answer:** Modules are shared software; uncontrolled changes can affect many environments.

### Q25. Variable?

**Answer:** Input used to customize reusable configuration.

### Q26. Output?

**Answer:** Published result used by users, pipelines, or other infrastructure stacks.

### Q27. Data lookup?

**Answer:** Reads existing infrastructure without taking creation ownership.

### Q28. Why avoid dynamic "latest" in production?

**Answer:** Same code can produce different infrastructure later, reducing reproducibility.

### Q29. Golden path?

**Answer:** Approved secure self-service infrastructure pattern exposed by platform team.

### Q30. Landing zone?

**Answer:** Governed cloud foundation for identity, network, logging, security, billing, and policies.

### Q31. CI identity best practice?

**Answer:** Short-lived federated workload identity rather than permanent cloud keys.

### Q32. Policy as code?

**Answer:** Machine-readable rules that evaluate infrastructure configuration or plans.

### Q33. Preventive policy?

**Answer:** Blocks a noncompliant infrastructure change before apply.

### Q34. Detective policy?

**Answer:** Detects and alerts on violations after or outside provisioning.

### Q35. IaC unit testing?

**Answer:** Testing logic, validation, outputs, and policies without necessarily provisioning full infrastructure.

### Q36. Integration testing?

**Answer:** Provisioning temporary real infrastructure and verifying behavior.

### Q37. Why can Git revert be unsafe?

**Answer:** Provider/resource changes may not be reversible in place.

### Q38. Blue/green infrastructure?

**Answer:** Build replacement environment, test it, switch traffic, keep old environment for fallback.

### Q39. Blast radius?

**Answer:** Scope of infrastructure potentially affected by one change/state/pipeline.

### Q40. Brownfield?

**Answer:** Existing infrastructure that predates current IaC management.

### Q41. Brownfield adoption process?

**Answer:** Inventory, write code, import, plan, reconcile differences, establish ownership.

### Q42. Monorepo advantage?

**Answer:** Central visibility/shared tooling and easier coordinated changes.

### Q43. Multi-repo advantage?

**Answer:** Smaller ownership boundaries and stronger team-level permissions.

### Q44. Why not one state for everything?

**Answer:** Large blast radius, slow plans, cross-team coupling, and operational risk.

### Q45. Why not hundreds of tiny states?

**Answer:** Excessive cross-state dependencies and operational complexity.

### Q46. Secret best practice?

**Answer:** External secret management plus short-lived identities; never commit secrets to IaC code.

### Q47. Provider supply-chain control?

**Answer:** Trusted source, version pinning, lock/checksum verification, controlled upgrades.

### Q48. Drift security significance?

**Answer:** Unexpected drift may indicate manual error, unauthorized change, or compromised automation.

### Q49. IaC disaster recovery requires what three views?

**Answer:** Code, state, and live infrastructure.

### Q50. Core production IaC model?

**Answer:** Git + modules + state + providers + plan + policy + CI identity + testing + drift detection + recovery.

---

## Completion Checklist

- [ ] I understand IaC vs scripting.
- [ ] I understand declarative and imperative automation.
- [ ] I understand desired state, actual state, convergence, and idempotency.
- [ ] I understand resource lifecycle.
- [ ] I understand dependency graphs.
- [ ] I understand provider/plugin concepts.
- [ ] I understand state and resource identity.
- [ ] I understand local and remote state.
- [ ] I understand locking/versioning/recovery.
- [ ] I understand plan/preview.
- [ ] I understand import/move/remove.
- [ ] I understand modules, variables, outputs, and data lookups.
- [ ] I understand environment separation.
- [ ] I understand naming/tagging.
- [ ] I understand monorepo vs multi-repo.
- [ ] I understand PR-based IaC workflows.
- [ ] I understand short-lived CI identity.
- [ ] I understand policy as code.
- [ ] I understand IaC testing and security scanning.
- [ ] I understand drift detection.
- [ ] I understand secret-management requirements.
- [ ] I understand provider/module supply-chain risks.
- [ ] I understand rollback limitations.
- [ ] I understand brownfield adoption.
- [ ] I understand blue/green infrastructure.
- [ ] I understand IaC DR.
- [ ] I understand AWS/Azure/GCP/Kubernetes/OpenShift IaC boundaries.
- [ ] I can compare Terraform, Bicep, CloudFormation, Pulumi, Ansible, Helm, Kustomize, and GitOps.
- [ ] I completed all 45 labs.
- [ ] I completed the Enterprise Infrastructure as Code Operating Model project.
