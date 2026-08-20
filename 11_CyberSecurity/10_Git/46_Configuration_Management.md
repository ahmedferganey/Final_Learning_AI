# 46. Configuration Management

> Phase 10 — Git & Configuration Automation

Configuration management is the discipline of **defining, applying, verifying, and maintaining the desired state of systems over time**.

Before using Ansible, you need to understand the problem Ansible solves.

A manually managed server looks like:

```text
Engineer SSHs to Server
        ↓
Runs commands
        ↓
Edits files
        ↓
Restarts services
        ↓
Leaves
```

Months later:

```text
What changed?
Who changed it?
Was every server changed?
Can we rebuild it?
Can we prove compliance?
```

Configuration management replaces this with a controlled model:

```text
Business Requirement
        ↓
Desired State
        ↓
Version-Controlled Configuration
        ↓
Review / Test
        ↓
Automation Engine
        ↓
Managed Systems
        ↓
Verification
        ↓
Drift Detection / Reconciliation
```

This course is tool-agnostic first. Ansible appears later as one implementation.

---

## 1. Topic Title

**Configuration Management**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain configuration management and its business purpose.
- Explain desired state, actual state, drift, convergence, and reconciliation.
- Differentiate imperative and declarative automation.
- Explain idempotency and why it matters.
- Differentiate configuration management, provisioning, orchestration, deployment, and IaC.
- Explain push versus pull configuration models.
- Explain agent-based versus agentless architectures.
- Explain mutable versus immutable infrastructure.
- Explain Day 0, Day 1, and Day 2 operations.
- Design a source-of-truth model.
- Explain inventory and asset identity.
- Design configuration data and variable hierarchies.
- Explain templates and parameterization.
- Explain secrets separation.
- Explain configuration baselines.
- Explain standardization and golden configuration.
- Explain drift detection.
- Explain continuous enforcement versus scheduled enforcement.
- Explain compliance as code and policy as code.
- Explain auditability and change history.
- Explain safe rollout, canary, phased change, maintenance windows, and rollback.
- Explain blast radius.
- Explain test environments and promotion.
- Explain configuration dependencies.
- Explain service handlers/restarts.
- Explain ordering and orchestration.
- Explain package, user, service, file, firewall, sysctl, mount, scheduled-task, and application configuration domains.
- Explain configuration management for Linux, Windows, network devices, cloud resources, and containers.
- Explain inventory from static files, CMDBs, cloud APIs, and dynamic discovery.
- Explain configuration ownership and separation of concerns.
- Explain role/module/component design.
- Explain reusable configuration abstractions.
- Explain variable precedence as a general design problem.
- Explain state validation and post-change verification.
- Explain dry-run/check/diff concepts.
- Explain transactional limitations and compensating rollback.
- Explain error handling and partial failure.
- Explain concurrency, serial rollout, and dependency-aware execution.
- Explain observability for automation.
- Explain configuration-management security.
- Explain secret rotation.
- Explain disaster recovery and rebuildability.
- Explain why Git belongs in the workflow.
- Design a configuration-management operating model that can later be implemented with Ansible.

---

## 3. Prerequisites

Required:

- Linux System Administration
- Windows administration fundamentals
- Networking
- Bash
- 45. Git and Version Control Systems

You should be comfortable manually performing tasks such as:

```bash
apt install nginx
systemctl enable --now nginx
useradd
chmod
chown
sysctl
mount
firewall configuration
```

Configuration automation only makes sense when you understand the manual operation it replaces.

---

## 4. Core Concepts Explanation

# Part 1 — What Configuration Management Solves

The core problem is inconsistency over time.

```text
Server A → correct
Server B → missing patch
Server C → wrong config
Server D → unknown manual change
```

Configuration management aims to make many systems converge on an intentional state rather than depending on administrator memory.

# Part 2 — Desired State

Desired state is the configuration that **should** exist.

Example:

```text
Package: nginx installed
Service: nginx enabled and running
File: /etc/nginx/nginx.conf owned by root
Port: 443 permitted
TLS certificate: present
```

The desired state should be reviewable and reproducible.

# Part 3 — Actual State

Actual state is what currently exists on the target.

```text
Desired: nginx running
Actual:  nginx stopped
```

Configuration management compares or acts on actual state to move it toward desired state.

# Part 4 — Configuration Drift

Drift is the difference between approved desired state and current actual state.

Sources:

```text
manual SSH changes
package updates
emergency fixes
application installers
malware
failed automation
hardware replacement
```

Drift is inevitable unless systems are immutable or continuously reconciled.

# Part 5 — Convergence

Convergence means repeated application moves a system toward the same desired result.

```text
Run 1 → 15 changes
Run 2 → 2 changes
Run 3 → 0 changes
```

A convergent system becomes stable when desired state is satisfied.

# Part 6 — Reconciliation

Reconciliation is the loop:

```text
Observe Actual State
        ↓
Compare with Desired State
        ↓
Apply Required Change
        ↓
Verify
        ↓
Repeat
```

This concept appears in Ansible, Kubernetes, GitOps, cloud controllers, and policy systems.

# Part 7 — Idempotency

An idempotent operation can be repeated without producing unwanted additional effects.

Good:

```text
Ensure user `appsvc` exists
```

Bad:

```bash
echo "server 10.0.0.10" >> /etc/hosts
```

every run, because it adds duplicate lines.

# Part 8 — Idempotent Shell Example

Imperative but safer:

```bash
grep -qxF 'server 10.0.0.10' /etc/hosts ||
  echo 'server 10.0.0.10' >> /etc/hosts
```

A configuration-management module should ideally model this as state rather than requiring custom shell guards.

# Part 9 — Imperative Automation

Imperative means specifying **how** to perform change.

```text
1. install package
2. copy file
3. chmod file
4. start service
```

It can be precise, but the author must manage current state and repeatability.

# Part 10 — Declarative Automation

Declarative means specifying **what state should exist**.

```yaml
package: nginx
state: installed

service: nginx
state: running
enabled: true
```

The engine determines whether change is required.

# Part 11 — Declarative Does Not Mean Order Is Irrelevant

Even declarative systems have dependencies:

```text
package installed
   ↓
configuration file
   ↓
service start
```

The difference is that each operation models desired state rather than blindly executing a mutation.

# Part 12 — Configuration Management vs Provisioning

Provisioning creates infrastructure:

```text
VM
network
disk
cloud instance
```

Configuration management configures the operating system/application after resources exist:

```text
packages
users
files
services
```

Tools can overlap, but the mental distinction is useful.

# Part 13 — Configuration Management vs Orchestration

Configuration management:

```text
make each system correct
```

Orchestration:

```text
coordinate multiple systems in sequence
```

Example:

```text
remove web01 from load balancer
patch web01
restart
health check
return to load balancer
```

# Part 14 — Configuration Management vs Deployment

Application deployment delivers a new application release. Configuration management establishes the environment it requires.

They often work together but should have clear ownership boundaries.

# Part 15 — Infrastructure as Code

IaC is a broader idea:

```text
infrastructure/configuration expressed as version-controlled machine-readable definitions
```

Configuration management is one part of IaC.

Terraform and Ansible solve overlapping but different problems.

# Part 16 — Push Model

Control node initiates change:

```text
Control Node
   |
   +-- Server A
   +-- Server B
   +-- Server C
```

Ansible commonly uses this model.

# Part 17 — Pull Model

Managed node periodically pulls configuration:

```text
Config Server
   ↑
Agent A
Agent B
Agent C
```

Benefits include continuous convergence. Costs include agents, certificates, and distributed scheduling.

# Part 18 — Agent-Based Model

An agent runs on the managed system.

Potential benefits:

```text
continuous enforcement
local reporting
offline queueing
```

Costs:

```text
agent lifecycle
ports/certs
resource overhead
version compatibility
```

# Part 19 — Agentless Model

Agentless systems use existing management protocols.

Examples:

```text
SSH for Linux
WinRM/PSRP for Windows
network APIs/SSH
cloud APIs
```

Ansible is designed primarily around this model.

# Part 20 — Mutable Infrastructure

A mutable server is changed in place.

```text
server v1
  ↓ patch/config
same server v2
```

This is common in enterprise infrastructure and configuration management.

# Part 21 — Immutable Infrastructure

Immutable model:

```text
old image/server
   ↓
build new image/server
   ↓
replace
```

Rather than repeatedly modifying a long-lived machine.

Containers and image-based cloud deployments often use this model.

# Part 22 — Mutable vs Immutable

Neither model universally wins.

Mutable is useful for:

```text
long-lived servers
network appliances
existing estates
```

Immutable is powerful for:

```text
cloud-native apps
containers
autoscaling fleets
```

Many enterprises use both.

# Part 23 — Day 0

Day 0:

```text
design
architecture
initial provisioning
network/storage
baseline planning
```

# Part 24 — Day 1

Day 1:

```text
initial OS/application configuration
users
packages
services
security baseline
```

# Part 25 — Day 2

Day 2 is ongoing operations:

```text
patch
rotate secrets
change config
scale
repair drift
upgrade
audit
recover
```

Most operational effort exists here.

# Part 26 — Source of Truth

A source of truth answers:

```text
What should this system be?
```

Possible sources:

```text
Git repository
CMDB
inventory service
secret manager
IPAM
cloud API
```

One system rarely owns every data type.

# Part 27 — Authority by Data Domain

Example:

```text
Git → desired application configuration
CMDB → asset owner
IPAM → IP addresses
Vault → secrets
Cloud API → discovered instance IDs
```

Define which system is authoritative for each value.

# Part 28 — Inventory

Inventory identifies managed targets.

```text
web01
web02
db01
router01
```

It can also group them:

```text
web
database
production
dc1
```

# Part 29 — Static Inventory

Static inventory is manually maintained.

Good for:

```text
small stable lab
```

Risk:

```text
cloud/server changes
inventory becomes stale
```

# Part 30 — Dynamic Inventory

Dynamic inventory queries a live source:

```text
AWS/Azure/GCP
VMware
OpenStack
CMDB
Nutanix
```

The target set changes as infrastructure changes.

# Part 31 — Inventory Identity

Use stable machine identity where possible.

Names should answer:

```text
which host?
which environment?
which role?
```

But avoid encoding every changing attribute into a hostname.

# Part 32 — Groups

Groups apply configuration by responsibility:

```text
all
├─ webservers
├─ dbservers
└─ monitoring
```

A server can belong to multiple groups.

This enables composition.

# Part 33 — Variables

Variables parameterize desired state.

```text
http_port = 8080
timezone = UTC
package_version = ...
```

Avoid copying entire configuration trees merely to change one value.

# Part 34 — Variable Hierarchy

A practical hierarchy:

```text
global defaults
  ↓
environment
  ↓
role
  ↓
group
  ↓
host
```

More-specific data should exist only when genuinely required.

# Part 35 — Variable Precedence as a Design Problem

If the same variable is defined in ten places, operators cannot predict the result.

Good configuration design minimizes override layers and documents precedence.

# Part 36 — Defaults

Reusable automation should provide safe defaults.

Example:

```text
nginx_worker_processes = auto
```

Environment-specific values override only when needed.

# Part 37 — Templates

A template turns structured variables into configuration.

Template:

```text
listen {{ web_port }};
server_name {{ hostname }};
```

Variables:

```text
web_port=443
hostname=app.example.com
```

# Part 38 — Template Benefits

Templates centralize structure while allowing controlled differences.

Avoid making one giant template with hundreds of conditional branches. That becomes harder to test than separate well-designed components.

# Part 39 — Configuration Files

A configuration-management system should control:

```text
content
owner
group
mode
location
validation
notification
```

not merely copy bytes.

# Part 40 — File Ownership

Correct content with wrong permissions can be a security incident.

Example desired state:

```text
/etc/myapp/secret.conf
owner=root
group=myapp
mode=0640
```

# Part 41 — Services

Configuration often follows:

```text
package
 ↓
file
 ↓
service
```

If the file changes:

```text
restart/reload service
```

Only when required.

# Part 42 — Handlers Concept

A handler runs only when a task reports change.

```text
configuration unchanged
→ no restart

configuration changed
→ reload service
```

This reduces unnecessary downtime.

# Part 43 — Reload vs Restart

Reload:

```text
process remains running
reads new config
```

Restart:

```text
process stops/starts
```

Prefer reload when application supports it and the change does not require restart.

# Part 44 — Packages

Desired state can be:

```text
present
absent
specific version
latest
```

Production caution:

```text
latest
```

can introduce uncontrolled change unless updates are intentionally governed.

# Part 45 — Package Repository Configuration

Automation should manage repository trust and configuration before packages depend on it.

```text
repo key
repo URL
priority
package install
```

Supply-chain controls matter.

# Part 46 — Users

User desired state includes:

```text
username
UID
group membership
shell
home
SSH key
locked/unlocked state
```

Offboarding is as important as onboarding.

# Part 47 — Groups

OS group management enables role-based access.

Example:

```text
appadmins
backupops
monitoring
```

Avoid placing every operator in `sudo`/Administrator.

# Part 48 — SSH Keys

Automation can ensure approved public keys are present and obsolete keys are absent.

Do not distribute private keys through configuration management unless a specific secure design requires it.

# Part 49 — Sudo Policy

Configuration management should treat privilege policy as code.

Example:

```text
backupops can run backup command
not arbitrary root shell
```

Validate syntax before replacing sudoers files.

# Part 50 — Firewall Configuration

Desired state should express:

```text
allowed source
destination/service
protocol
port
zone/interface
```

Avoid "disable firewall because automation failed."

# Part 51 — Sysctl

Kernel settings are configuration state.

Example:

```text
net.ipv4.ip_forward=1
```

Good automation manages both:

```text
runtime value
persistent configuration
```

# Part 52 — Mounts

Mount state includes:

```text
device/source
mount point
filesystem
options
persistent boot entry
mounted/unmounted
```

A correct `/etc/fstab` entry with failed mount still requires verification.

# Part 53 — Scheduled Tasks

Manage cron/systemd timers/Windows scheduled tasks as desired state.

Avoid duplicate cron lines on every run.

# Part 54 — Application Configuration

Infrastructure automation should know where its responsibility ends.

Possible separation:

```text
platform team → OS/web server
application team → app config
security team → policy baseline
```

Ownership boundaries reduce conflicting automation.

# Part 55 — Configuration Dependency Graph

Example:

```text
DNS
 ↓
package repository
 ↓
package install
 ↓
configuration
 ↓
database
 ↓
application service
```

Automation must account for dependencies, not just host order.

# Part 56 — Ordering

Some changes must occur sequentially:

```text
create directory
copy config
validate config
reload service
```

Other changes can run in parallel.

Good orchestration knows the difference.

# Part 57 — Serial Rollout

For ten web servers:

```text
change 2
health check
change next 2
```

instead of:

```text
change all 10 simultaneously
```

This limits blast radius.

# Part 58 — Canary

A canary receives the change first.

```text
1 server
 ↓
observe
 ↓
fleet
```

Use for high-risk or poorly understood changes.

# Part 59 — Maintenance Window

A maintenance window defines:

```text
when
who
what
expected impact
rollback deadline
```

Automation does not eliminate change-management requirements.

# Part 60 — Blast Radius

Blast radius is the number/importance of systems a failed change can affect.

Controls:

```text
limits
serial
environment separation
approvals
target patterns
```

# Part 61 — Environment Separation

Separate:

```text
development
test
staging
production
```

through inventory, credentials, permissions, and deployment workflows.

A typo should not turn a staging operation into a production change.

# Part 62 — Promotion

Preferred model:

```text
same code
 ↓
dev data/vars
 ↓
test
 ↓
staging
 ↓
production
```

Avoid manually rewriting the automation for each environment.

# Part 63 — Configuration Validation

Before applying a config, validate syntax when the application offers a checker.

Examples:

```bash
nginx -t
sshd -t
visudo -c
named-checkconf
```

A template can render valid YAML but invalid application semantics.

# Part 64 — Post-Change Verification

After change, verify outcomes:

```text
service running
port listening
health endpoint returns 200
process has expected config
```

"Automation returned success" is not the same as "business service works."

# Part 65 — Dry Run

Dry-run/check mode estimates changes without applying them where supported.

It is useful but imperfect because some operations cannot predict state safely without execution.

# Part 66 — Diff Mode

Diff mode shows content/state differences before or during a change.

Protect secrets: a diff can leak passwords, keys, or confidential configuration into CI logs.

# Part 67 — Testing Pyramid for Configuration

```text
static checks
  ↓
unit/template tests
  ↓
integration on disposable machine
  ↓
staging
  ↓
production canary
```

Do not use production as the first syntax test.

# Part 68 — Linting

Linting catches:

```text
syntax
style
unsafe patterns
deprecated constructs
```

It improves consistency but does not prove runtime correctness.

# Part 69 — Integration Testing

Create a disposable target:

```text
VM/container
 ↓
apply configuration
 ↓
verify service
 ↓
apply again
 ↓
expect zero changes
```

The second run is an idempotency test.

# Part 70 — State Verification

Verification should be explicit.

Example Python probe:

```python
import requests

r = requests.get("https://app.example/health", timeout=5)
assert r.status_code == 200
```

Test the user-visible result, not only process state.

# Part 71 — Rollback

Rollback approaches:

```text
reapply previous desired state
restore config backup
deploy previous package/image
fail back traffic
restore VM/volume if necessary
```

A rollback plan should exist before execution.

# Part 72 — Forward Fix vs Rollback

Sometimes rollback is unsafe because:

```text
database schema changed
data migrated
certificate rotated
```

Then the correct recovery is a forward fix.

Change plans must identify whether reversal is actually possible.

# Part 73 — Partial Failure

Example:

```text
10 servers targeted
7 succeed
3 fail
```

Now the fleet is inconsistent.

Automation must report exact affected systems and provide a safe convergence strategy.

# Part 74 — Compensating Action

Distributed configuration does not usually have one transaction.

If step 3 fails after steps 1 and 2:

```text
reverse steps
or
continue forward safely
```

according to the change design.

# Part 75 — Retries

Retries help with transient failures:

```text
service startup delay
temporary network timeout
API rate limit
```

They do not fix deterministic bad configuration.

# Part 76 — Timeouts

Every remote operation should have bounded time.

Without timeout:

```text
one hung host
→ entire automation waits indefinitely
```

# Part 77 — Unreachable vs Failed

Differentiate:

```text
unreachable
  transport/connection failure

failed
  reached target but operation failed
```

The remediation is different.

# Part 78 — Concurrency

Parallel execution reduces deployment time but increases load and blast radius.

Choose based on:

```text
service dependencies
backend capacity
risk
```

# Part 79 — Rolling Change

For clustered service:

```text
Node A drain/change/health
Node B drain/change/health
Node C drain/change/health
```

Never update all quorum members simultaneously unless the architecture explicitly supports it.

# Part 80 — Load Balancer Coordination

Safe web patch:

```text
remove server from LB
 ↓
wait for connections
 ↓
patch/restart
 ↓
health check
 ↓
return to LB
```

This is orchestration around configuration management.

# Part 81 — Database Configuration

Database automation may manage:

```text
config parameters
users/roles
backup jobs
monitoring
TLS
```

Schema/data migration often belongs to a separate application/database migration workflow.

# Part 82 — Network Device Configuration

Network configuration management deals with:

```text
interfaces
VLANs
routing
ACLs
BGP
NTP
SNMP
AAA
```

Network devices may support SSH CLI, NETCONF, RESTCONF, or vendor APIs.

# Part 83 — Network Source of Truth

For network automation, IPAM/NetBox-like systems can own:

```text
prefix
VLAN
device
interface
rack
```

Git can own templates/policies.

Do not duplicate authoritative IP data manually in five repositories.

# Part 84 — Windows Configuration

Windows management can automate:

```text
features
services
registry
local users/groups
files
IIS
updates
firewall
scheduled tasks
```

Transport and privilege models differ from Linux.

# Part 85 — Cloud Configuration

Cloud APIs can configure:

```text
security groups
instances
load balancers
DNS
IAM
```

Some of this belongs to provisioning IaC; some to configuration automation. Define ownership to avoid two tools fighting over the same resource.

# Part 86 — Container Configuration

Container images favor immutable configuration:

```text
Dockerfile/image build
```

Runtime environment supplies:

```text
environment variables
mounted config
secrets
```

Avoid SSH-driven mutation inside disposable containers.

# Part 87 — Kubernetes Configuration

Kubernetes uses a reconciliation model:

```text
YAML desired state
 ↓
API server
 ↓
controllers
 ↓
actual state
```

This is configuration management implemented as continuous control loops.

# Part 88 — CMDB

A Configuration Management Database records configuration items and relationships.

Possible data:

```text
server
owner
service
environment
location
dependency
```

A CMDB is not automatically accurate; it must be integrated with discovery and change workflows.

# Part 89 — Configuration Item

A CI can be:

```text
server
network device
application
database
service
certificate
```

Define granularity appropriate to operational decisions.

# Part 90 — Configuration Baseline

A baseline is an approved starting state.

Example Linux baseline:

```text
NTP configured
SSH hardened
logging enabled
firewall active
monitoring installed
standard users/groups
```

Servers can then receive role-specific configuration.

# Part 91 — Golden Configuration

A golden configuration is the approved reference.

Avoid a golden server configured manually and copied by memory.

Prefer a golden **definition** in Git that can rebuild the server.

# Part 92 — Drift Detection

Detection can be:

```text
scheduled audit
continuous agent
periodic Ansible run
file-integrity monitoring
cloud-policy service
```

Decide whether drift should merely alert or be automatically corrected.

# Part 93 — Automatic Drift Correction Risk

If an operator makes an emergency change:

```text
automation may immediately revert it
```

This can be good security—or dangerous during incidents.

Define emergency override/change procedures.

# Part 94 — Compliance as Code

Express compliance requirements programmatically.

Example:

```text
SSH root login disabled
password authentication disabled
audit service running
```

Then continuously test targets.

# Part 95 — Policy as Code

Policy as code evaluates proposed/runtime configuration against rules.

Example:

```text
"No public SSH from 0.0.0.0/0"
```

It complements configuration automation by preventing unsafe desired states.

# Part 96 — Security Baselines

Security configuration should be:

```text
versioned
reviewed
tested
measured
```

Avoid one-time hardening checklists that drift immediately after deployment.

# Part 97 — Secrets Separation

Repository:

```yaml
db_password: "{{ secret_lookup }}"
```

Secret store:

```text
real password
```

The automation definition and secret value should have different access controls.

# Part 98 — Secret Rotation

Rotation workflow:

```text
create new secret
 ↓
update consuming systems
 ↓
verify
 ↓
revoke old secret
```

Order matters to avoid outages.

# Part 99 — Certificates

Certificate automation includes:

```text
issue
deploy
permissions
chain
reload
expiration monitoring
renewal
revocation
```

Treat private keys as secrets.

# Part 100 — Configuration Data Classification

Not every variable is equally sensitive.

Examples:

```text
public:
package name

internal:
server topology

secret:
password/token/private key
```

Access/logging controls should reflect classification.

# Part 101 — Logging Automation

Record:

```text
who ran
what version/commit
which targets
what changed
what failed
duration
```

Avoid logging secret content.

# Part 102 — Observability

Useful metrics:

```text
run success rate
changed hosts
failed hosts
duration
drift count
rollback count
configuration age
```

This shows whether automation is actually improving operations.

# Part 103 — Change Correlation

A production incident at 14:03 should be traceable to:

```text
automation run
Git commit
operator
change ticket
targets
```

This is why version control and automation logs belong together.

# Part 104 — Git as Change Control

Workflow:

```text
branch
 ↓
change desired state
 ↓
review
 ↓
tests
 ↓
merge
 ↓
automation
```

Git makes infrastructure changes reviewable before execution.

# Part 105 — Avoid Manual Production Drift

If an emergency SSH fix is necessary:

```text
1. restore service.
2. record exact change.
3. update desired-state repository.
4. review/merge.
5. re-run automation.
```

Otherwise the fix becomes undocumented drift.

# Part 106 — Separation of Duties

Example:

```text
author writes change
reviewer approves
automation service executes
security/audit reviews logs
```

This is stronger than one admin directly editing every production server.

# Part 107 — Least Privilege for Automation

Automation credentials are powerful.

Restrict by:

```text
targets
commands/modules
API roles
vault access
environment
```

Do not make one universal root key for every system if you can avoid it.

# Part 108 — Credential Rotation for Automation

Automation access must have lifecycle:

```text
issue
store
use
audit
rotate
revoke
```

Service accounts should not become immortal credentials.

# Part 109 — Control Node Security

The control node can reach many systems.

Protect it with:

```text
patching
MFA/admin access
disk encryption
secret controls
logging
network segmentation
backups
```

Compromise can have fleet-wide impact.

# Part 110 — Supply Chain

Configuration code depends on:

```text
packages
roles/modules
container images
repositories
collections
```

Pin, verify, review, and update dependencies deliberately.

# Part 111 — Rebuildability

A strong configuration-management goal:

```text
If server is lost,
can we create a replacement
without copying undocumented state from the old one?
```

If not, important configuration is still trapped outside code.

# Part 112 — Backup Still Matters

Configuration management can rebuild configuration, but not necessarily data.

You still need:

```text
database backups
file backups
secrets recovery
certificate/key recovery
```

Automation is not backup.

# Part 113 — Disaster Recovery Automation

DR runbook can be partially automated:

```text
provision/recover infrastructure
configure OS
restore data
configure application
update DNS/LB
validate
```

This reduces RTO only if tested.

# Part 114 — Documentation as Code

Store close to automation:

```text
architecture
variables
runbooks
ownership
failure modes
```

Documentation should evolve with the code that implements it.

# Part 115 — When Not to Automate Immediately

Do not automate a process you do not understand.

First:

```text
perform manually
document
identify inputs/outputs
identify failure modes
make it repeatable
then automate
```

This is especially important for destructive storage/network/security changes.

# Part 116 — Automation Maturity Model

A useful progression:

```text
manual documented
  ↓
scripted
  ↓
idempotent configuration
  ↓
versioned/tested
  ↓
reviewed CI/CD
  ↓
continuous reconciliation/policy
```

# Part 117 — Reusable Components

Break large configuration into units:

```text
base OS
SSH
monitoring
web server
database client
backup agent
```

Composition is easier to test than one 5,000-line automation file.

# Part 118 — Interface Contract for a Component

A reusable component should define:

```text
inputs
defaults
dependencies
outputs
supported OS
side effects
restart behavior
```

This prepares you for Ansible roles.

# Part 119 — Configuration Ownership

Every managed setting should ideally have one owner.

If:

```text
Ansible
startup script
cloud-init
application installer
human admin
```

all edit the same file, drift and race conditions result.

# Part 120 — Avoid Tool Conflict

Example:

```text
Terraform manages security group
Ansible also manages same security group
```

Two sources of truth can continuously undo each other.

Define resource ownership.

# Part 121 — Configuration Review Checklist

Before merge:

```text
Is desired state clear?
Is it idempotent?
What is blast radius?
Are secrets protected?
Does it require restart?
Is validation present?
Can it roll back?
Is there a canary?
```

# Part 122 — Production Run Checklist

Before execution:

```text
correct commit/version?
correct inventory?
correct environment?
credentials valid?
maintenance approved?
backup/rollback ready?
monitoring available?
```

# Part 123 — Post-Run Checklist

After:

```text
failed hosts?
unexpected changes?
service health?
alerts?
configuration drift?
Git/change record updated?
```

# Part 124 — Troubleshooting Configuration Automation

Use the layers:

```text
control node
 ↓
transport
 ↓
authentication/privilege
 ↓
module/action
 ↓
OS/application
 ↓
verification
```

Identify the failed layer rather than changing random automation options.

# Part 125 — Configuration Management Mental Model

The professional goal is not:

```text
"run commands on many servers"
```

It is:

```text
define an approved desired state,
apply it safely,
prove the actual state,
detect drift,
and recover predictably.
```

That is the foundation you need before Ansible.

---

# Enhanced Deep-Study Layer — Configuration Management

This enhancement preserves the complete uploaded Course 46 and adds a deeper layer on desired-state modeling, convergence, ownership, safe rollout, distributed failure handling, secrets, compliance, testing, control-plane security, observability, and disaster recovery.

The goal is to make configuration management a **systems-engineering discipline**, not merely 'running commands on many servers.' Every automated change should have a defined desired state, authoritative data source, ownership boundary, validation method, blast-radius control, failure model, and recovery path.

The additional learning sequence used throughout is:

```text
Concept
  ↓
Detailed Explanation
  ↓
Internal / Architecture Model
  ↓
Commands / Code / Configuration
  ↓
Expected State / Output
  ↓
Why It Works
  ↓
Production Example
  ↓
Failure / Troubleshooting
  ↓
Best Practice
```

## Advanced Deep Dive 1 — Desired State as a Formal Contract

### Concept and Detailed Explanation
Configuration management starts by expressing the state a system should have independently of the commands used to reach it. A good desired-state definition is testable: package version/state, service state, file content/permissions, firewall rule, user/group membership, kernel setting, mount, or application endpoint.

When desired state is vague, automation becomes a shell-script launcher rather than a configuration system.

### Internal / Architecture Model
```text
Business requirement
   |
Desired-state contract
   |
Automation implementation
   |
Actual system
   |
Verification
```

### Commands / Code / Configuration
```text
desired:
  nginx:
    package: present
    service: running
    enabled: true
  config:
    path: /etc/nginx/nginx.conf
    owner: root
    mode: "0644"
```

### Expected State / Output
Two engineers reading the definition agree on what the compliant end state must be.

### Why It Works
Configuration engines can compare or enforce state only when the target condition is explicit.

### Production Example
Instead of 'run these five commands to harden SSH,' the platform standard states exact settings, permissions, service behavior, and validation tests.

### Failure / Troubleshooting Workflow
```text
automation behaves strangely
  ↓
is desired state explicit?
  ↓
which attributes are authoritative?
  ↓
what evidence proves compliance?
  ↓
clarify contract before changing implementation
```

### Best Practice
Write the end-state contract before writing tasks.

---

## Advanced Deep Dive 2 — Actual State, Observation, and Facts

### Concept and Detailed Explanation
Actual state is not just what a previous automation run reported. It is what the target currently exposes through package managers, service managers, files, APIs, runtime probes, and discovered facts. Reliable reconciliation depends on trustworthy observation.

### Internal / Architecture Model
```text
Target system
  |
observe:
packages
files
services
users
network
runtime API
  |
actual-state model
```

### Commands / Code / Configuration
```text
rpm -q nginx 2>/dev/null || dpkg-query -W nginx 2>/dev/null || true
systemctl is-enabled nginx
systemctl is-active nginx
stat /etc/nginx/nginx.conf
ss -lntp
```

### Expected State / Output
The evidence reflects current target state independently of what automation expected to happen.

### Why It Works
Configuration drift can occur after deployment through manual changes, package scripts, emergency work, or external controllers.

### Production Example
An automation run says nginx started successfully, but a later process crash leaves the service inactive; runtime observation detects the difference.

### Failure / Troubleshooting Workflow
```text
desired says correct but service broken
  ↓
observe actual system
  ↓
compare files/packages/service/runtime
  ↓
identify drift or runtime failure
```

### Best Practice
Treat automation output as evidence of an attempt; verify actual state separately.

---

## Advanced Deep Dive 3 — Convergence as a Control Loop

### Concept and Detailed Explanation
Convergence means repeated configuration runs reduce the difference between desired and actual state until no change is required. This control-loop mindset is more powerful than thinking in one-time scripts.

### Internal / Architecture Model
```text
Observe actual
   |
Compare to desired
   |
difference?
 /      yes      no
 |        |
change   stable
 |
verify
 |
repeat
```

### Commands / Code / Configuration
```text
for i in 1 2 3; do
  ./apply-configuration.sh
  ./verify-state.sh
done
```

### Expected State / Output
Later runs make fewer changes and a stable target produces a no-change result.

### Why It Works
State-aware operations avoid repeating mutations that are already satisfied.

### Production Example
A hardened Linux baseline corrects manually changed SSH permissions on the next approved reconciliation run.

### Failure / Troubleshooting Workflow
```text
never converges
  ↓
identify resource changing every run
  ↓
compare rendered desired vs actual
  ↓
timestamp/random value?
  ↓
external tool modifying same resource?
  ↓
fix ownership/idempotency
```

### Best Practice
Investigate any resource that reports changed on every run.

---

## Advanced Deep Dive 4 — Idempotency Beyond 'Run Twice'

### Concept and Detailed Explanation
Idempotency means that applying the same desired state repeatedly does not create additional unintended effects. A second-run zero-change test is useful, but true idempotency also requires stable inputs and no hidden side effects such as timestamp regeneration, duplicate users, repeated API object creation, or unconditional service restart.

### Internal / Architecture Model
```text
Same desired input
   |
run 1 → change to desired
   |
run 2 → no semantic change
   |
run N → remains desired
```

### Commands / Code / Configuration
```text
# Bad
echo "10.0.0.10 api" >> /etc/hosts

# Better shell guard
grep -qxF "10.0.0.10 api" /etc/hosts ||
  echo "10.0.0.10 api" >> /etc/hosts
```

### Expected State / Output
Repeated runs leave one correct entry and do not restart/rewrite resources unnecessarily.

### Why It Works
Idempotent resources model state instead of replaying mutations.

### Production Example
A certificate-deployment task rewrites a file with a new timestamp every run, causing an unnecessary web-server reload each time.

### Failure / Troubleshooting Workflow
```text
changed every run
  ↓
compare before/after content
  ↓
hidden timestamp/order?
  ↓
module reports change incorrectly?
  ↓
side-effect command unconditional?
```

### Best Practice
Test both state idempotency and side-effect idempotency.

---

## Advanced Deep Dive 5 — Imperative vs Declarative as Design Choices

### Concept and Detailed Explanation
Imperative automation describes steps; declarative automation describes the end state. Declarative style improves convergence, but imperative actions remain necessary for migrations, one-time commands, and workflows that do not map cleanly to a resource state.

The goal is not to ban commands; it is to use state-aware modules where a stable state exists and reserve imperative execution for real operations.

### Internal / Architecture Model
```text
Declarative:
"service nginx should be running"

Imperative:
"run schema migration 42"

Different problem types
need different semantics
```

### Commands / Code / Configuration
```text
# Declarative-like pseudo state
service:
  name: nginx
  state: started

# Imperative one-time operation
./migrate-db --to 42
```

### Expected State / Output
Stable resources converge declaratively, while one-time operations have explicit guards and completion markers.

### Why It Works
Some operations represent persistent state; others represent events or transitions.

### Production Example
A package should be 'present'; a one-time database data migration should not execute every reconciliation run.

### Failure / Troubleshooting Workflow
```text
automation repeats destructive command
  ↓
is this resource state or event?
  ↓
add guard/version marker
  ↓
separate migration workflow if needed
```

### Best Practice
Model persistent state declaratively and isolate irreversible transitions.

---

## Advanced Deep Dive 6 — Configuration Management vs Provisioning Ownership

### Concept and Detailed Explanation
Provisioning creates infrastructure resources such as VMs, networks, disks, load balancers, and cloud identities. Configuration management typically configures the OS and applications after those resources exist. Overlap is possible, but each resource should have one authoritative owner.

### Internal / Architecture Model
```text
Terraform / cloud API
   |
creates VM/network/disk
   |
Configuration Management
   |
packages/users/files/services
```

### Commands / Code / Configuration
```text
Ownership matrix:
Resource                  Owner
VM                        Terraform
Security group            Terraform
OS packages               Config Mgmt
/etc/sshd_config          Config Mgmt
Application artifact      Deployment pipeline
```

### Expected State / Output
No two tools continuously fight over the same resource.

### Why It Works
Independent control loops managing the same field can oscillate or overwrite each other.

### Production Example
Terraform sets a security-group rule one way while configuration automation changes the same cloud object differently on every run.

### Failure / Troubleshooting Workflow
```text
resource keeps reverting
  ↓
list every tool touching it
  ↓
identify authoritative owner
  ↓
remove duplicate management
```

### Best Practice
Maintain a resource-ownership matrix for the automation stack.

---

## Advanced Deep Dive 7 — Configuration Management vs Orchestration

### Concept and Detailed Explanation
Configuration management makes individual systems correct. Orchestration coordinates systems and dependencies over time. A safe clustered change often combines both: orchestrate traffic/drain/order while configuration management changes each node.

### Internal / Architecture Model
```text
Load Balancer
   |
drain node A
   |
configure node A
   |
health check
   |
return node A
   |
repeat node B
```

### Commands / Code / Configuration
```text
workflow:
  - disable_backend: web01
  - wait_connections_drained
  - apply_baseline: web01
  - verify_health: web01
  - enable_backend: web01
```

### Expected State / Output
Each node reaches desired configuration without removing all service capacity at once.

### Why It Works
Correct per-node state does not imply safe fleet-wide sequencing.

### Production Example
A patch is safe on one web server but causes outage when all ten servers restart simultaneously.

### Failure / Troubleshooting Workflow
```text
fleet outage risk
  ↓
identify service dependency
  ↓
define drain/order/quorum rules
  ↓
configure serially
```

### Best Practice
Use orchestration around configuration changes whenever system order matters.

---

## Advanced Deep Dive 8 — Mutable vs Immutable Infrastructure

### Concept and Detailed Explanation
Mutable infrastructure changes long-lived systems in place; immutable infrastructure builds a replacement image/version and swaps it into service. Both need desired-state definitions, but the enforcement mechanism differs.

Mutable configuration is common for enterprise servers and devices. Immutable delivery is common for containers and autoscaling fleets.

### Internal / Architecture Model
```text
Mutable:
server v1 → patch/config → same server v2

Immutable:
image v1 → build image v2 → replace instances
```

### Commands / Code / Configuration
```text
# Mutable
systemctl reload nginx

# Immutable conceptual pipeline
build image
test image
deploy new instances
health check
shift traffic
remove old instances
```

### Expected State / Output
Operations use the model appropriate to the platform rather than mixing ad-hoc mutation into disposable systems.

### Why It Works
Immutable replacement reduces accumulated drift, while mutable management supports long-lived stateful or appliance-like systems.

### Production Example
An autoscaling web tier is rebuilt from a patched image instead of SSH-patching hundreds of ephemeral nodes.

### Failure / Troubleshooting Workflow
```text
drift appears in immutable fleet
  ↓
was instance mutated manually?
  ↓
rebuild from approved image
  ↓
remove manual mutation path
```

### Best Practice
Use immutable replacement where the platform naturally supports it; do not force it onto every stateful system.

---

## Advanced Deep Dive 9 — Day 0, Day 1, and Day 2 Responsibility

### Concept and Detailed Explanation
Configuration management spans more than initial setup. Day 0 defines architecture and prerequisites, Day 1 establishes the baseline, and Day 2 handles patching, rotation, drift, scaling, certificate renewal, upgrades, incident fixes, and retirement.

Most operational risk accumulates in Day 2.

### Internal / Architecture Model
```text
Day 0 → design/provisioning
Day 1 → initial baseline
Day 2 → patch/rotate/change/audit/recover
```

### Commands / Code / Configuration
```text
Lifecycle checklist:
Day0: network, identity, image, storage
Day1: users, packages, services, baseline
Day2: patch, drift, certs, secrets, upgrades, decommission
```

### Expected State / Output
The same configuration model supports ongoing maintenance and recovery, not only first deployment.

### Why It Works
Servers live much longer than the initial install event.

### Production Example
An environment is perfectly automated at build time but certificate renewal remains manual and causes an outage a year later.

### Failure / Troubleshooting Workflow
```text
operational gap
  ↓
which lifecycle stage owns it?
  ↓
add Day2 automation/runbook
  ↓
test periodic operation
```

### Best Practice
Design recurring maintenance automation at the same time as initial configuration.

---

## Advanced Deep Dive 10 — Source of Truth by Data Domain

### Concept and Detailed Explanation
One repository should not blindly own every piece of information. Git may own desired configuration, IPAM may own addresses, a CMDB may own business ownership, a secret manager may own credentials, and a cloud API may be authoritative for discovered instance IDs.

The key is explicit authority and reliable integration.

### Internal / Architecture Model
```text
Git → desired config
IPAM → IP/VLAN
CMDB → owner/service
Vault → secrets
Cloud API → runtime IDs
     |
configuration pipeline
```

### Commands / Code / Configuration
```text
Data Domain        Authority       Consumer
NTP servers        Git/CMDB        Config Mgmt
IP addresses       IPAM            Inventory
DB password        Secret Manager  App config
Instance ID        Cloud API       Dynamic inventory
```

### Expected State / Output
Every variable has one documented authoritative source.

### Why It Works
Duplicating authoritative data across files creates drift between the copies.

### Production Example
An IP address is manually copied into inventory, firewall YAML, DNS YAML, and documentation; one change updates only three of them.

### Failure / Troubleshooting Workflow
```text
data mismatch
  ↓
which system owns value?
  ↓
remove duplicated authority
  ↓
integrate consumers with source
```

### Best Practice
Define authority per data domain before designing variable files.

---

## Advanced Deep Dive 11 — Inventory Identity and Stable Targeting

### Concept and Detailed Explanation
Inventory identifies targets and their grouping. Good identity is stable enough that automation can recognize a machine through normal lifecycle changes without encoding every transient attribute into the hostname.

Inventory should separate identity from connection details where possible.

### Internal / Architecture Model
```text
Inventory identity:
web01

Connection data:
10.0.1.15
SSH user
port

Groups:
prod
web
dc1
```

### Commands / Code / Configuration
```text
hosts:
  web01:
    address: 10.0.1.15
    groups: [prod, web, dc1]
```

### Expected State / Output
Changing an IP or connection method does not require changing the conceptual host identity.

### Why It Works
Automation needs a stable key to correlate state, history, and ownership while infrastructure details can change.

### Production Example
A VM is re-IPed after migration; inventory updates connection data without renaming every variable and policy path.

### Failure / Troubleshooting Workflow
```text
wrong target
  ↓
inventory identity
  ↓
connection address
  ↓
group membership
  ↓
environment scope
```

### Best Practice
Keep host identity stable and store mutable attributes separately.

---

## Advanced Deep Dive 12 — Static vs Dynamic Inventory

### Concept and Detailed Explanation
Static inventory is predictable and easy to review but can become stale. Dynamic inventory queries authoritative systems such as cloud APIs, VMware, OpenStack, Nutanix, or CMDBs. Dynamic discovery improves freshness but creates runtime dependencies and requires filtering to avoid targeting unintended systems.

### Internal / Architecture Model
```text
Static file
  or
Cloud/CMDB API
   |
inventory plugin/query
   |
target set
```

### Commands / Code / Configuration
```text
# Conceptual dynamic filter:
environment == "prod"
AND managed_by == "platform"
AND lifecycle_state == "active"
```

### Expected State / Output
The target set matches the authoritative source and excludes unmanaged or retired systems.

### Why It Works
Dynamic infrastructure changes too quickly for manual host lists to remain accurate.

### Production Example
A cloud autoscaling group creates new nodes; dynamic inventory includes them automatically based on tags.

### Failure / Troubleshooting Workflow
```text
dynamic inventory unexpected
  ↓
query filters
  ↓
API credentials/scope
  ↓
tags/metadata
  ↓
cache freshness
```

### Best Practice
Use narrow, testable filters and preview the resolved target list before production runs.

---

## Advanced Deep Dive 13 — Group Composition and Cross-Cutting Roles

### Concept and Detailed Explanation
A host can belong to multiple groups representing environment, application role, location, or compliance class. This lets desired state be composed instead of copied.

Group design should reflect real concerns and avoid contradictory configurations.

### Internal / Architecture Model
```text
web01 belongs to:
prod
web
dc1
pci

Effective desired state =
base + prod + web + dc1 + pci
```

### Commands / Code / Configuration
```text
groups:
  prod: [web01, db01]
  web: [web01, web02]
  pci: [web01, db01]
```

### Expected State / Output
Common baselines and role-specific configuration combine predictably for a host.

### Why It Works
Composition avoids duplicated per-host definitions while supporting cross-cutting policy.

### Production Example
A PCI security baseline applies to selected web and database hosts regardless of their application role.

### Failure / Troubleshooting Workflow
```text
unexpected effective config
  ↓
list all host groups
  ↓
identify overlapping variables/policies
  ↓
remove contradictory group ownership
```

### Best Practice
Use groups for orthogonal concerns, not as a substitute for arbitrary override layers.

---

## Advanced Deep Dive 14 — Variable Hierarchy and Override Discipline

### Concept and Detailed Explanation
Variables make configuration reusable, but excessive precedence layers make the effective value hard to predict. A practical model uses safe defaults, environment/role data, and rare host exceptions.

The more override points a system has, the harder it becomes to answer 'why is this value 8443 on this host?'

### Internal / Architecture Model
```text
defaults
  ↓
environment
  ↓
role
  ↓
group
  ↓
host exception
```

### Commands / Code / Configuration
```text
http_port:
  default: 8080
  prod: 8443

# Document exceptions:
web07:
  http_port: 9443
  reason: legacy integration
  expires: 2026-12-01
```

### Expected State / Output
Most hosts inherit common values; exceptions are few, documented, and time-bounded.

### Why It Works
Precedence resolves conflicts but also hides intent when definitions are scattered.

### Production Example
A host-level variable silently overrides the production standard for years because nobody remembers why it exists.

### Failure / Troubleshooting Workflow
```text
wrong effective value
  ↓
search all definitions
  ↓
show precedence/source
  ↓
remove stale exception
  ↓
test effective config
```

### Best Practice
Prefer fewer override layers and record the reason/expiry for exceptions.

---

## Advanced Deep Dive 15 — Templates as Controlled Compilation

### Concept and Detailed Explanation
A configuration template transforms structured data into an application-specific file. Treat rendering like compilation: inputs must be typed/validated, output must be deterministic, and the rendered file should pass the application's syntax checker before replacement.

### Internal / Architecture Model
```text
Variables
   |
Template
   |
render
   |
candidate config
   |
syntax validation
   |
atomic install
   |
reload
```

### Commands / Code / Configuration
```text
# Jinja-like
server {
    listen {{ http_port }};
    server_name {{ server_name }};
}

# Validation
nginx -t -c /path/to/candidate.conf
```

### Expected State / Output
Identical inputs produce identical output and invalid output is rejected before service reload.

### Why It Works
Templates centralize structure while preserving controlled parameter differences.

### Production Example
A bad variable renders an invalid nginx directive; pre-install validation catches it before the live configuration is replaced.

### Failure / Troubleshooting Workflow
```text
template deployment fails
  ↓
input data
  ↓
rendered candidate
  ↓
syntax checker
  ↓
permissions/ownership
  ↓
install/reload
```

### Best Practice
Validate rendered configuration before replacing the live file.

---

## Advanced Deep Dive 16 — Configuration File Ownership, Mode, and Atomic Replacement

### Concept and Detailed Explanation
Correct file content is only one part of desired state. Owner, group, permissions, SELinux context where relevant, parent directory, and atomic replacement behavior can all affect security and availability.

A configuration workflow should avoid exposing partially written files to a running service.

### Internal / Architecture Model
```text
candidate file
  |
validate
  |
write temporary file
  |
set owner/mode/context
  |
atomic rename/install
  |
reload service
```

### Commands / Code / Configuration
```text
install -o root -g root -m 0644 new.conf /etc/myapp/myapp.conf
stat /etc/myapp/myapp.conf
ls -Z /etc/myapp/myapp.conf 2>/dev/null || true
```

### Expected State / Output
The file has correct content, ownership, mode, and security context, and the service reads a complete file.

### Why It Works
Unix permissions and security labels are part of the effective configuration; atomic replacement prevents partial reads.

### Production Example
A secret configuration is rendered correctly but world-readable, creating a data exposure despite successful service startup.

### Failure / Troubleshooting Workflow
```text
config correct but service/security wrong
  ↓
content
  ↓
owner/group/mode
  ↓
SELinux/AppArmor context
  ↓
parent directory
  ↓
service read access
```

### Best Practice
Model metadata and security context together with file content.

---

## Advanced Deep Dive 17 — Handlers, Notifications, and Change-Driven Side Effects

### Concept and Detailed Explanation
Dependent actions such as service reloads should occur only when the resource they depend on actually changes. This decouples state management from side effects and reduces unnecessary downtime.

### Internal / Architecture Model
```text
Template unchanged
    |
no notification
    |
no reload

Template changed
    |
notify
    |
handler reloads service once
```

### Commands / Code / Configuration
```text
# Pseudo declarative flow
template config
  notify: reload nginx

handler reload nginx
  when: notified
```

### Expected State / Output
Repeated no-change runs do not reload services; several related file changes can trigger one handler at the end.

### Why It Works
Change events provide a clean signal that a dependent action is required.

### Production Example
Five template tasks all update during one run, but nginx reloads once instead of five times.

### Failure / Troubleshooting Workflow
```text
service reloading every run
  ↓
why task reports changed?
  ↓
template nondeterministic?
  ↓
handler triggered unconditionally?
  ↓
fix change detection
```

### Best Practice
Use change-driven handlers instead of unconditional restarts.

---

## Advanced Deep Dive 18 — Reload vs Restart Decision

### Concept and Detailed Explanation
Reload asks a running process to re-read configuration while preserving process continuity; restart stops and starts the process. The correct action depends on the application's capabilities and the changed setting.

Some changes cannot take effect on reload, while unnecessary restart increases service disruption.

### Internal / Architecture Model
```text
config changed
   |
does app support safe reload?
  / yes  no
 |    |
reload restart
   |
health verification
```

### Commands / Code / Configuration
```text
nginx -t && systemctl reload nginx
sshd -t && systemctl reload sshd 2>/dev/null || true
systemctl restart <service>
```

### Expected State / Output
The chosen action applies the configuration and service health remains acceptable.

### Why It Works
Applications define which runtime state can be refreshed without process recreation.

### Production Example
A TLS certificate renewal needs only reload, but a low-level process startup option requires restart.

### Failure / Troubleshooting Workflow
```text
change not taking effect
  ↓
is setting reloadable?
  ↓
service documentation
  ↓
runtime status
  ↓
restart only if required
```

### Best Practice
Encode restart semantics in the reusable component interface.

---

## Advanced Deep Dive 19 — Package State and Version Governance

### Concept and Detailed Explanation
Package configuration should distinguish 'present', 'absent', and intentionally pinned versions. Using `latest` in production can create uncontrolled change every run or whenever repositories publish a new build.

Package state also depends on repository configuration and trust.

### Internal / Architecture Model
```text
Repository trust/config
   ↓
package metadata
   ↓
desired package/version
   ↓
install/update/remove
   ↓
service compatibility
```

### Commands / Code / Configuration
```text
apt-cache policy nginx 2>/dev/null || true
dnf info nginx 2>/dev/null || true
rpm -q nginx 2>/dev/null || true
dpkg-query -W nginx 2>/dev/null || true
```

### Expected State / Output
Production hosts run the approved package version/channel and upgrades occur through an explicit change process.

### Why It Works
Repositories are moving sources; `latest` turns repository publication into an implicit production deployment trigger.

### Production Example
A minor package update changes default TLS behavior and restarts a critical service unexpectedly.

### Failure / Troubleshooting Workflow
```text
package drift
  ↓
installed version
  ↓
configured repository
  ↓
pin/lock policy
  ↓
approved target version
```

### Best Practice
Use explicit version policy for production-critical software.

---

## Advanced Deep Dive 20 — Repository Trust and Software Supply Chain

### Concept and Detailed Explanation
Package repositories, automation modules, roles, collections, images, and scripts are software supply-chain dependencies. Configuration management should control where they come from, how versions are pinned, and how trust/signature verification is performed.

### Internal / Architecture Model
```text
Trusted upstream
   |
signature/hash
   |
approved internal mirror
   |
pinned dependency
   |
automation target
```

### Commands / Code / Configuration
```text
# Inventory dependencies:
component
source URL
version
hash/signature
owner
update cadence

# Example package repo inspection:
apt-cache policy 2>/dev/null | head
dnf repolist 2>/dev/null || true
```

### Expected State / Output
Automation consumes only approved dependency sources and versions with documented update ownership.

### Why It Works
Highly privileged automation magnifies the impact of a compromised dependency.

### Production Example
A community role is updated automatically and introduces a malicious shell task across the entire server fleet.

### Failure / Troubleshooting Workflow
```text
supply-chain concern
  ↓
identify artifact/source
  ↓
version/hash/signature
  ↓
who approved?
  ↓
isolate dependency
  ↓
restore known-good version
```

### Best Practice
Pin and review privileged automation dependencies.

---

## Advanced Deep Dive 21 — User Lifecycle as Desired State

### Concept and Detailed Explanation
User management must model onboarding, role changes, and offboarding. Desired state includes UID, groups, shell, home, SSH public keys, password/lock state, and account expiration where applicable.

The most dangerous failure is often not missing creation but incomplete removal.

### Internal / Architecture Model
```text
HR / Identity event
   |
desired user state
   |
create/change/disable/remove
   |
verify access
```

### Commands / Code / Configuration
```text
id appsvc 2>/dev/null || true
getent passwd appsvc
getent group appadmins
passwd -S appsvc 2>/dev/null || true
```

### Expected State / Output
The account has exactly the intended access and obsolete memberships/keys are absent.

### Why It Works
Accounts accumulate privilege unless lifecycle changes are modeled as strongly as creation.

### Production Example
An engineer changes teams but retains membership in a production-admin group because automation only adds groups and never removes obsolete ones.

### Failure / Troubleshooting Workflow
```text
access drift
  ↓
account identity
  ↓
group memberships
  ↓
SSH keys
  ↓
sudo policy
  ↓
desired role
  ↓
remove stale access
```

### Best Practice
Design offboarding and privilege removal before onboarding automation.

---

## Advanced Deep Dive 22 — SSH Key Management and Private-Key Boundaries

### Concept and Detailed Explanation
Configuration management is well suited to distributing approved public keys. Private keys require much stronger handling and usually should not be pushed broadly through ordinary configuration code.

Key rotation should support overlap so new access is verified before old keys are removed.

### Internal / Architecture Model
```text
Public key source
   |
authorized_keys desired state
   |
target hosts

Private key
   |
protected secret/identity system
not ordinary Git
```

### Commands / Code / Configuration
```text
ssh-keygen -lf ~/.ssh/authorized_keys 2>/dev/null || true
grep -n 'ssh-' ~/.ssh/authorized_keys 2>/dev/null || true
```

### Expected State / Output
Only approved public keys exist; revoked keys disappear after the controlled rotation window.

### Why It Works
Public keys are safe to distribute broadly; private keys grant identity and require restricted storage.

### Production Example
A universal private deployment key is copied to hundreds of servers and later leaks from one backup.

### Failure / Troubleshooting Workflow
```text
SSH access problem
  ↓
expected public key?
  ↓
file ownership/mode
  ↓
sshd policy
  ↓
account/group
  ↓
key rotation state
```

### Best Practice
Prefer per-service or federated identities over one fleet-wide private key.

---

## Advanced Deep Dive 23 — Sudo / Privilege Policy as Code

### Concept and Detailed Explanation
Privilege escalation policy should be explicit, least-privilege, syntactically validated, and reviewed like application code. Automation should avoid granting full root shells when a narrower command set or role is sufficient.

### Internal / Architecture Model
```text
Identity
  |
group/role
  |
sudo policy
  |
specific privileged action
```

### Commands / Code / Configuration
```text
visudo -cf /etc/sudoers
sudo -l -U backupops 2>/dev/null || true
```

### Expected State / Output
Sudoers syntax is valid and each operational role can execute only required privileged actions.

### Why It Works
Configuration management can preserve consistent privilege policy and prevent manual exceptions from accumulating.

### Production Example
A backup service account receives unrestricted NOPASSWD ALL instead of access only to the backup command.

### Failure / Troubleshooting Workflow
```text
sudo policy failure
  ↓
syntax validation
  ↓
effective rules
  ↓
group membership
  ↓
command path/arguments
  ↓
least-privilege correction
```

### Best Practice
Always validate sudoers before replacing live policy.

---

## Advanced Deep Dive 24 — Firewall State as a Dependency-Aware Resource

### Concept and Detailed Explanation
Firewall automation should model direction, source, destination, service/port, interface/zone, and business purpose. Broad 'allow all' changes are not acceptable troubleshooting shortcuts.

Remote automation must also protect its own management path.

### Internal / Architecture Model
```text
Automation controller
   |
management SSH/WinRM/API
   |
host firewall
   |
application ports
```

### Commands / Code / Configuration
```text
# Linux examples
firewall-cmd --list-all 2>/dev/null || true
nft list ruleset 2>/dev/null || true
ss -lntp
```

### Expected State / Output
Required management and application flows work; unauthorized flows remain blocked.

### Why It Works
Firewall rules define network reachability and can disconnect the very control channel applying them.

### Production Example
A firewall baseline removes SSH before the new bastion rule is installed, locking automation out mid-run.

### Failure / Troubleshooting Workflow
```text
firewall change
  ↓
preserve control path
  ↓
apply new rule
  ↓
verify from external probe
  ↓
remove old rule
```

### Best Practice
Sequence remote-firewall changes so a verified management path always remains.

---

## Advanced Deep Dive 25 — Sysctl Runtime vs Persistent State

### Concept and Detailed Explanation
Kernel parameters can exist in runtime memory and persistent configuration files. Managing only one layer creates drift after reboot or leaves the current system inconsistent with the stored policy.

### Internal / Architecture Model
```text
persistent config
   |
boot/sysctl load
   |
runtime kernel value

Configuration management should align both.
```

### Commands / Code / Configuration
```text
sysctl net.ipv4.ip_forward
grep -R "net.ipv4.ip_forward" /etc/sysctl.conf /etc/sysctl.d 2>/dev/null || true
```

### Expected State / Output
The current runtime value and persistent configuration agree.

### Why It Works
Kernel runtime state resets or reloads independently of configuration files.

### Production Example
A forwarding setting is changed with `sysctl -w` during an incident but disappears after reboot because persistent config was never updated.

### Failure / Troubleshooting Workflow
```text
sysctl mismatch
  ↓
current runtime
  ↓
which config file defines value?
  ↓
precedence/duplicate definitions
  ↓
apply persistent + runtime desired state
```

### Best Practice
Manage runtime and persistence together and eliminate duplicate conflicting definitions.

---

## Advanced Deep Dive 26 — Mounts as Multi-Layer State

### Concept and Detailed Explanation
A mount is not just an `/etc/fstab` line. Desired state includes source, filesystem type, options, mountpoint, persistent boot configuration, current mounted state, credentials where needed, and actual reachability of the storage backend.

### Internal / Architecture Model
```text
storage source
   |
mount config
   |
mountpoint
   |
runtime mount
   |
application
```

### Commands / Code / Configuration
```text
findmnt /data
grep -n '/data' /etc/fstab
mount -a -f 2>/dev/null || true
stat /data
```

### Expected State / Output
The mount is present with correct options and survives reboot while the application can read/write as intended.

### Why It Works
A syntactically correct fstab entry does not prove the backend is reachable or the mount succeeded.

### Production Example
Automation writes an NFS fstab entry but the firewall blocks NFS, leaving the directory unmounted and the app writing to the local root filesystem.

### Failure / Troubleshooting Workflow
```text
mount problem
  ↓
source reachability
  ↓
mount config/options
  ↓
credentials
  ↓
runtime mount
  ↓
application path
```

### Best Practice
Verify the mounted filesystem itself, not only the configuration file.

---

## Advanced Deep Dive 27 — Scheduled Tasks Without Duplication

### Concept and Detailed Explanation
Cron entries, systemd timers, and Windows scheduled tasks are persistent configuration resources. Repeated automation must converge on one correct schedule rather than append duplicate lines.

### Internal / Architecture Model
```text
desired schedule
   |
resource identity
   |
create/update exact task
   |
one active schedule
```

### Commands / Code / Configuration
```text
crontab -l 2>/dev/null || true
systemctl list-timers --all | head -30
```

### Expected State / Output
Exactly one intended job exists with the correct schedule and command.

### Why It Works
State-aware management identifies a task by name/resource rather than blindly appending text.

### Production Example
A backup script is appended to crontab on every run and executes ten times nightly.

### Failure / Troubleshooting Workflow
```text
duplicate scheduled job
  ↓
identify owning automation
  ↓
normalize to one resource
  ↓
remove duplicates
  ↓
verify next run
```

### Best Practice
Manage scheduled tasks as named resources, not text append operations.

---

## Advanced Deep Dive 28 — Application Configuration Ownership Boundary

### Concept and Detailed Explanation
Platform, application, database, security, and deployment teams often touch the same hosts. Configuration management needs a clear boundary describing which team/tool owns which files and settings.

Without ownership, two automation systems may continuously overwrite each other.

### Internal / Architecture Model
```text
Platform:
OS / SSH / monitoring / web server

Application:
app config / artifact

Security:
baseline/policy

Database:
DB parameters/schema workflow
```

### Commands / Code / Configuration
```text
Ownership record:
Path/Resource | Owner Tool | Team | Change Process
/etc/nginx/*  | Config Mgmt | Platform | infra PR
/opt/app/*    | Deploy CI   | App      | app release
```

### Expected State / Output
Every managed resource has one authoritative writer.

### Why It Works
Control loops cannot converge if multiple independent systems express different desired values.

### Production Example
An app installer rewrites nginx.conf after Ansible hardens it, so every configuration run reports drift.

### Failure / Troubleshooting Workflow
```text
resource oscillates
  ↓
who writes it?
  ↓
list tools/scripts/packages
  ↓
select authoritative owner
  ↓
remove competing writer
```

### Best Practice
Document one owner per configuration resource.

---

## Advanced Deep Dive 29 — Dependency Graphs and Topological Ordering

### Concept and Detailed Explanation
Configuration resources form a graph. Package repositories must exist before packages; directories before files; certificates before TLS listeners; database readiness before application startup. The correct execution order is a topological ordering of dependencies, not simply the file order of tasks.

### Internal / Architecture Model
```text
DNS
 ↓
package repository
 ↓
package
 ↓
directory
 ↓
config/cert
 ↓
service
 ↓
health check
```

### Commands / Code / Configuration
```text
# Pseudo dependency declaration
repo -> package
package -> config
certificate -> tls_config
config -> service_reload
service_reload -> health_check
```

### Expected State / Output
Each resource is applied only after its prerequisites are valid.

### Why It Works
Dependent resources cannot reach desired state before the states they consume exist.

### Production Example
An application starts before its database schema and credentials exist, fails, and is misdiagnosed as a service problem.

### Failure / Troubleshooting Workflow
```text
resource failure
  ↓
what prerequisites does it consume?
  ↓
verify upstream dependency
  ↓
correct ordering/readiness
```

### Best Practice
Model dependencies explicitly instead of relying on accidental task order.

---

## Advanced Deep Dive 30 — Readiness vs Mere Process State

### Concept and Detailed Explanation
A process being `running` does not mean the service is ready. Post-change verification should use the strongest practical signal: local socket, health endpoint, dependency check, or business transaction.

### Internal / Architecture Model
```text
systemd active
   |
port listening
   |
health endpoint
   |
business transaction

Each level gives stronger evidence.
```

### Commands / Code / Configuration
```text
systemctl is-active nginx
ss -lntp | grep ':443'
curl --fail --max-time 5 https://localhost/health
```

### Expected State / Output
The verification proves the level of service actually required by the rollout decision.

### Why It Works
Services can run while misconfigured, disconnected from dependencies, or returning errors.

### Production Example
A Java process is active but returns HTTP 503 because its database connection pool failed.

### Failure / Troubleshooting Workflow
```text
automation says success
  ↓
process?
  ↓
port?
  ↓
health endpoint?
  ↓
business dependency?
```

### Best Practice
Use application-level readiness to decide whether the next rollout wave may proceed.

---

## Advanced Deep Dive 31 — Canary Rollout as Risk Measurement

### Concept and Detailed Explanation
A canary is a small representative subset that receives a change before the wider fleet. The purpose is not merely 'change one server first'; it is to collect evidence about compatibility, performance, error rate, and business behavior under real conditions.

A canary should be representative enough to reveal likely failure modes but small enough to limit impact.

### Internal / Architecture Model
```text
Change candidate
   |
Canary 1–5%
   |
health / errors / latency / logs
   |
pass? ---- no → stop/recover
   |
  yes
   |
next wave
```

### Commands / Code / Configuration
```text
Canary gate:
- config syntax valid
- service healthy
- application error rate normal
- latency within SLO
- no new critical alert
- rollback still possible
```

### Expected State / Output
The rollout automatically or procedurally stops when canary acceptance criteria fail.

### Why It Works
Testing on a real but limited target captures environment-specific behavior while constraining blast radius.

### Production Example
A new TLS policy works in staging but breaks one legacy production client; the canary catches the issue before all web servers change.

### Failure / Troubleshooting Workflow
```text
canary fails
  ↓
stop further waves
  ↓
collect evidence
  ↓
rollback or forward-fix canary
  ↓
update change
  ↓
retest
```

### Best Practice
Define numeric/observable canary success criteria before the change starts.

---

## Advanced Deep Dive 32 — Serial Rollout and Batch Sizing

### Concept and Detailed Explanation
Serial execution limits how many systems change at once. Batch size should reflect service redundancy, backend capacity, failure tolerance, and recovery speed.

`20% at a time` is not automatically safer than `2 at a time`; the correct size depends on architecture.

### Internal / Architecture Model
```text
Fleet of 20
  |
Batch 1: 1 canary
  |
Batch 2: 2
  |
Batch 3: 5
  |
Batch 4: remaining
```

### Commands / Code / Configuration
```text
Batch design:
minimum healthy instances
load balancer capacity
quorum rules
database connection surge
restart time
rollback time
```

### Expected State / Output
The service remains above required capacity during every wave and each batch passes health checks before the next begins.

### Why It Works
Rolling change trades speed for bounded simultaneous risk.

### Production Example
Restarting four of six web servers at once overloads the remaining two and causes a user-visible outage.

### Failure / Troubleshooting Workflow
```text
rollout overload
  ↓
batch size
  ↓
remaining service capacity
  ↓
backend/load impact
  ↓
reduce concurrency
```

### Best Practice
Calculate batch size from minimum surviving service capacity.

---

## Advanced Deep Dive 33 — Quorum-Aware Changes

### Concept and Detailed Explanation
Clusters such as databases, message queues, consensus systems, and control planes require quorum. Configuration management must not update or restart too many quorum members simultaneously.

The orchestration logic should understand membership and voting behavior, not just host count.

### Internal / Architecture Model
```text
5-member cluster
majority = 3

safe rolling update:
1 node out
4 remain
then return healthy
next node
```

### Commands / Code / Configuration
```text
Quorum worksheet:
members
voters
majority required
current unhealthy members
maintenance members
remaining votes
```

### Expected State / Output
Quorum remains available during each maintenance step and every node rejoins healthy before the next step.

### Why It Works
Consensus systems require enough communicating voters to make safe progress.

### Production Example
Automation restarts two members of a three-node control-plane cluster simultaneously and loses quorum.

### Failure / Troubleshooting Workflow
```text
quorum risk
  ↓
current members healthy?
  ↓
votes required
  ↓
planned concurrent changes
  ↓
reduce batch/stop
```

### Best Practice
Encode quorum math into change prerequisites.

---

## Advanced Deep Dive 34 — Load Balancer Drain and Connection Grace

### Concept and Detailed Explanation
Removing a server from a load balancer is not the same as immediately terminating existing sessions. Safe orchestration often disables new traffic, waits for active connections to drain or reach a deadline, then changes the node.

### Internal / Architecture Model
```text
LB
 |
disable new connections to web01
 |
wait for active sessions
 |
patch/restart
 |
health check
 |
enable web01
```

### Commands / Code / Configuration
```text
Drain steps:
disable backend
query active connections
wait with timeout
apply configuration
verify health
enable backend
```

### Expected State / Output
New traffic avoids the node during maintenance and existing sessions end cleanly within the defined drain window.

### Why It Works
Graceful draining reduces user impact from forced connection termination.

### Production Example
A long-running file upload is cut off because automation restarts the server immediately after marking it disabled.

### Failure / Troubleshooting Workflow
```text
drain hangs
  ↓
active connection count
  ↓
maximum drain deadline
  ↓
business policy for forced close
  ↓
continue or abort
```

### Best Practice
Define both graceful-drain criteria and a maximum wait time.

---

## Advanced Deep Dive 35 — Maintenance Windows and Change Deadlines

### Concept and Detailed Explanation
Automation speed does not remove maintenance governance. A change window should define start, stop, rollback deadline, responsible roles, expected user impact, monitoring, and escalation.

The most important boundary is often the latest time at which rollback remains safe.

### Internal / Architecture Model
```text
Approved window
start
  |
change waves
  |
decision point
  |
rollback deadline
  |
window end
```

### Commands / Code / Configuration
```text
Change record:
start_time
stop_time
rollback_deadline
owner
approver
monitor
escalation_contact
expected_impact
```

### Expected State / Output
Operators know when to stop attempting fixes and execute the planned recovery path.

### Why It Works
Complex changes can consume the entire window if no decision deadline exists.

### Production Example
A patch fails halfway through; engineers troubleshoot for three hours and miss the point where restoring the previous version was still easy.

### Failure / Troubleshooting Workflow
```text
change running long
  ↓
current time vs rollback deadline
  ↓
business impact
  ↓
continue / rollback / escalate
```

### Best Practice
Put a time-based decision point in every high-risk production change.

---

## Advanced Deep Dive 36 — Dry Run and Check-Mode Limitations

### Concept and Detailed Explanation
Dry-run or check mode estimates changes but cannot perfectly predict operations that depend on runtime side effects, generated values, command output, API behavior, or later tasks. It is useful evidence, not a transactional guarantee.

### Internal / Architecture Model
```text
check mode
  |
predict state change
  |
some operations known
some skipped/uncertain
  |
real run still required
```

### Commands / Code / Configuration
```text
Dry-run review:
predicted changed hosts
predicted files/packages
tasks skipped in check mode
unknown commands/APIs
secret-sensitive diffs
```

### Expected State / Output
Operators know which parts of the change were actually predicted and which require staging/canary evidence.

### Why It Works
A configuration engine cannot know the final result of an arbitrary shell command without executing it.

### Production Example
A database migration task is skipped in check mode, so the dry run looks safe even though the real migration can fail.

### Failure / Troubleshooting Workflow
```text
dry run says no problem, real run fails
  ↓
which task lacked predictive support?
  ↓
add integration test/canary
  ↓
improve validation
```

### Best Practice
Use dry-run together with real tests on disposable/staging targets.

---

## Advanced Deep Dive 37 — Diff Mode and Secret Leakage

### Concept and Detailed Explanation
Diff output is extremely useful for review but may reveal passwords, private keys, tokens, certificates, or confidential topology. Automation systems and CI logs must suppress or redact sensitive diffs.

### Internal / Architecture Model
```text
Desired file
   |
diff engine
   |
log / CI / terminal
   |
potential secret exposure
```

### Commands / Code / Configuration
```text
Classification:
public config → diff allowed
internal topology → restricted logs
secret material → diff suppressed/redacted
```

### Expected State / Output
Reviewers can see safe configuration changes without sensitive values appearing in logs.

### Why It Works
Diff systems print before/after content by design, which conflicts with secret confidentiality.

### Production Example
A secret rotation succeeds but the old and new passwords are both written into CI logs through diff mode.

### Failure / Troubleshooting Workflow
```text
secret shown in log
  ↓
rotate affected secret
  ↓
restrict/delete log copy
  ↓
mark resource no-log/redacted
  ↓
audit exposure
```

### Best Practice
Classify configuration data before enabling verbose diff logging.

---

## Advanced Deep Dive 38 — Static Validation vs Runtime Validation

### Concept and Detailed Explanation
Static validators confirm syntax or schema before a configuration is applied. Runtime validation confirms the actual service behavior afterward. Both are needed because a syntactically valid file can still be operationally wrong.

### Internal / Architecture Model
```text
template render
   |
static validator
   |
apply
   |
reload/restart
   |
runtime probe
   |
business test
```

### Commands / Code / Configuration
```text
nginx -t
sshd -t
visudo -c
named-checkconf

# Runtime
curl --fail https://service/health
```

### Expected State / Output
Invalid syntax is blocked before deployment and semantic/runtime failures are detected before rollout continues.

### Why It Works
Static tools understand configuration grammar; runtime probes test real dependencies and behavior.

### Production Example
nginx configuration is syntactically valid but points upstream to the wrong application port.

### Failure / Troubleshooting Workflow
```text
validation failure
  ↓
syntax?
  ↓
service startup?
  ↓
dependency?
  ↓
business response?
```

### Best Practice
Use the strongest validator available at each stage.

---

## Advanced Deep Dive 39 — Configuration Testing Pyramid

### Concept and Detailed Explanation
Configuration code should be tested at several levels: formatting/schema checks, template/unit tests, integration on disposable systems, staging, canary, and production verification. Each level catches different failure classes.

### Internal / Architecture Model
```text
static / lint
    ↓
unit/template
    ↓
integration VM/container
    ↓
staging
    ↓
canary
    ↓
production rollout
```

### Commands / Code / Configuration
```text
Pipeline:
lint
render test
idempotency test
service syntax test
integration health
security policy check
```

### Expected State / Output
Simple failures are caught early and expensive real-environment tests focus on integration behavior.

### Why It Works
No single test environment perfectly represents syntax, OS behavior, dependency availability, and production traffic.

### Production Example
A missing package dependency passes template lint but fails on a clean integration VM, before production.

### Failure / Troubleshooting Workflow
```text
production bug escaped
  ↓
which test layer could have detected it?
  ↓
add regression test at cheapest appropriate layer
```

### Best Practice
Move each discovered failure into a repeatable earlier test where possible.

---

## Advanced Deep Dive 40 — Idempotency Testing in Disposable Systems

### Concept and Detailed Explanation
A useful integration test applies configuration to a clean target, verifies it, applies the same configuration again, and expects zero unintended changes. It can then introduce drift and prove convergence.

### Internal / Architecture Model
```text
clean target
  ↓
apply → changes expected
  ↓
verify
  ↓
apply again → 0 changes
  ↓
introduce drift
  ↓
apply → targeted correction
```

### Commands / Code / Configuration
```text
Test steps:
1. build VM/container
2. run automation
3. capture changed resources
4. run again
5. assert no change
6. modify one managed file
7. rerun
8. assert only drift corrected
```

### Expected State / Output
The second run is stable and deliberate drift is repaired without unrelated changes.

### Why It Works
This directly tests the convergence contract rather than only task syntax.

### Production Example
A reusable web-server role is rejected because it rewrites a template timestamp and reloads nginx every run.

### Failure / Troubleshooting Workflow
```text
idempotency test fails
  ↓
find always-changed resource
  ↓
compare desired/actual
  ↓
remove nondeterminism
  ↓
repeat test
```

### Best Practice
Make idempotency a regression test for reusable components.

---

## Advanced Deep Dive 41 — Rollback vs Forward Fix

### Concept and Detailed Explanation
Not every change is reversible. Configuration files and package versions may roll back cleanly, but database schema changes, key rotations, or data transformations may require forward correction.

A change plan must classify its recovery path before execution.

### Internal / Architecture Model
```text
Change
  |
reversible?
 /       yes       no
 |         |
rollback  forward fix / restore
```

### Commands / Code / Configuration
```text
Recovery classification:
config file        → previous version
package            → previous package if compatible
database schema    → migration-specific
secret rotation    → dual-secret/forward transition
data transformation→ restore or corrective migration
```

### Expected State / Output
Operators know whether rollback is valid and have artifacts/runbooks for the chosen recovery path.

### Why It Works
State changes can affect persistent data or external systems in ways that cannot be undone by restoring a file.

### Production Example
A new application schema writes data in a format the previous version cannot read; package rollback alone makes the outage worse.

### Failure / Troubleshooting Workflow
```text
change failed
  ↓
is old state still compatible?
  ↓
data/schema changed?
  ↓
rollback or forward-fix plan
  ↓
verify consistency
```

### Best Practice
Never label a procedure 'rollback' until compatibility has been proven.

---

## Advanced Deep Dive 42 — Partial Failure and Fleet Inconsistency

### Concept and Detailed Explanation
Distributed configuration runs can succeed on some targets and fail on others, leaving the fleet split between versions or policies. Recovery must be based on application compatibility and business risk rather than blindly making all hosts match the majority.

### Internal / Architecture Model
```text
10 targets
  |
7 changed
3 failed
  |
mixed fleet
  |
decision:
finish forward?
rollback 7?
isolate failed nodes?
```

### Commands / Code / Configuration
```text
Partial-failure report:
host
before version
after version
failure reason
service health
traffic status
next action
```

### Expected State / Output
Every target's state is known and the recovery decision is explicit.

### Why It Works
There is no global transaction across independent hosts; each target can commit changes separately.

### Production Example
Seven web servers receive a new config while three fail package download, leaving incompatible behavior behind one load balancer.

### Failure / Troubleshooting Workflow
```text
partial failure
  ↓
stop next wave
  ↓
classify compatibility
  ↓
traffic isolate if needed
  ↓
repair failed or rollback changed
  ↓
restore uniform supported state
```

### Best Practice
Design the partial-failure decision tree before large fleet changes.

---

## Advanced Deep Dive 43 — Compensating Actions and Saga-Like Recovery

### Concept and Detailed Explanation
Multi-step configuration workflows often cannot roll back atomically. A compensating action undoes or neutralizes a completed step when a later step fails, similar to a Saga pattern in distributed applications.

### Internal / Architecture Model
```text
Step A succeeds
  ↓
Step B succeeds
  ↓
Step C fails
  ↓
compensate B
  ↓
compensate A
or continue forward safely
```

### Commands / Code / Configuration
```text
Example:
remove node from LB
install package
write config
restart fails

Compensation:
restore previous config
restore package if safe
verify old service
return to LB
```

### Expected State / Output
The workflow leaves the environment in a known serviceable state after failure rather than an undocumented half-state.

### Why It Works
Independent systems do not participate in one atomic transaction.

### Production Example
A node is removed from the load balancer, patched, then fails health check; the recovery workflow restores the prior package/config before rejoining.

### Failure / Troubleshooting Workflow
```text
step fails
  ↓
what earlier steps committed?
  ↓
which are reversible?
  ↓
run compensations in safe reverse dependency order
  ↓
verify
```

### Best Practice
Document compensation for every irreversible boundary in an orchestrated change.

---

## Advanced Deep Dive 44 — Retries, Backoff, and Error Classification

### Concept and Detailed Explanation
Retries should address transient conditions such as temporary network failures, service startup delay, API throttling, or package mirror hiccups. Deterministic errors such as invalid syntax or permission denial should fail quickly.

Unbounded immediate retry can amplify an outage.

### Internal / Architecture Model
```text
error
  |
transient?
 /      yes      no
 |        |
retry     fail
backoff   actionable evidence
jitter
```

### Commands / Code / Configuration
```text
Retry policy:
max_attempts: 5
initial_delay: 2s
backoff: exponential
jitter: enabled
retry_on:
  - timeout
  - selected 5xx
  - temporary lock
```

### Expected State / Output
Transient faults recover without endless loops while deterministic configuration errors surface immediately.

### Why It Works
Different errors have different expected future behavior.

### Production Example
One thousand agents retry a failed package repository every second and overload it further.

### Failure / Troubleshooting Workflow
```text
repeated failure
  ↓
classify error
  ↓
transient or deterministic?
  ↓
bounded retry/backoff
  ↓
final fail with evidence
```

### Best Practice
Retry by error semantics, not because 'something failed'.

---

## Advanced Deep Dive 45 — Timeouts and Hung Targets

### Concept and Detailed Explanation
Every remote operation needs a bounded timeout. One hung SSH session, package manager, API call, or service stop should not block an entire fleet indefinitely.

### Internal / Architecture Model
```text
automation
  |
target operation
  |
timeout deadline
 / complete  expire
 |        |
next      fail/handle
```

### Commands / Code / Configuration
```text
timeout 30s ssh host command
curl --max-time 10 https://service/health
systemctl stop myapp  # pair orchestration with an external deadline if needed
```

### Expected State / Output
The run reports a bounded failure and can continue or stop according to rollout policy.

### Why It Works
Distributed operations must assume some nodes can become unresponsive.

### Production Example
A service stop hangs on one server and prevents a 500-host patch run from ever reaching completion.

### Failure / Troubleshooting Workflow
```text
run hanging
  ↓
which operation/host?
  ↓
timeout configured?
  ↓
collect target process/network state
  ↓
fail host cleanly
```

### Best Practice
Set timeouts based on expected operation duration plus realistic margin.

---

## Advanced Deep Dive 46 — Unreachable vs Failed Targets

### Concept and Detailed Explanation
An unreachable target means the automation could not establish the required transport or management session. A failed target means the tool reached the target but the requested operation failed. These are different failure classes and need different runbooks.

### Internal / Architecture Model
```text
Control Node
  |
  +-- no SSH/WinRM/API → UNREACHABLE
  |
  +-- session works
        |
        +-- command/module error → FAILED
```

### Commands / Code / Configuration
```text
# Transport checks
ping <host>             # only if ICMP is relevant
ssh -vvv user@host
nc -vz <host> 22 2>/dev/null || true

# On target after connection:
id
sudo -n true
systemctl status <service>
```

### Expected State / Output
The operator can classify the incident before changing application configuration.

### Why It Works
Transport, authentication, privilege, and module/application execution are separate layers.

### Production Example
A host shows unreachable because DNS resolves to an old IP; changing package tasks would not help.

### Failure / Troubleshooting Workflow
```text
target problem
  ↓
name resolution
  ↓
network/port
  ↓
authentication
  ↓
privilege
  ↓
module/action
  ↓
application
```

### Best Practice
Branch troubleshooting at the first failed layer.

---

## Advanced Deep Dive 47 — Concurrency, Forks, and Backend Pressure

### Concept and Detailed Explanation
Parallel execution shortens run time but increases simultaneous load on package mirrors, databases, APIs, storage, authentication systems, and the application itself. Concurrency should be sized to infrastructure capacity, not only controller CPU.

### Internal / Architecture Model
```text
Control node
  |
many parallel workers
  |
+-- 100 SSH sessions
+-- package downloads
+-- service restarts
+-- health checks
  |
shared backends
```

### Commands / Code / Configuration
```text
Concurrency worksheet:
target_count
max_parallel
package_repo_capacity
API rate limits
database connection limit
LB spare capacity
network bandwidth
```

### Expected State / Output
Parallelism improves duration without exceeding shared backend limits or service SLOs.

### Why It Works
Automation fan-out can create a workload spike much larger than normal user traffic.

### Production Example
A patch job starts 500 package downloads simultaneously and saturates the internal repository.

### Failure / Troubleshooting Workflow
```text
run slows/fails under scale
  ↓
parallelism
  ↓
shared backend metrics
  ↓
rate limits
  ↓
reduce batch/forks
```

### Best Practice
Load-test automation fan-out before using maximum concurrency in production.

---

## Advanced Deep Dive 48 — Distributed Locks and Change Collisions

### Concept and Detailed Explanation
Two automation runs targeting the same resource at the same time can race. Depending on the resource, this may create harmless last-writer-wins behavior, a package-manager lock failure, duplicate API objects, or corrupted orchestration state.

High-risk workflows need run serialization or distributed locking.

### Internal / Architecture Model
```text
Pipeline A ----               > same target/resource
Pipeline B ----/
         |
race / conflict
```

### Commands / Code / Configuration
```text
Lock identity:
environment
resource/group
change type
owner
expiry/lease

# Local illustration
flock /var/lock/platform-change.lock ./apply.sh
```

### Expected State / Output
Overlapping incompatible production changes are prevented or detected before mutation.

### Why It Works
Configuration tools generally do not provide a global transaction across separate pipeline executions.

### Production Example
Two scheduled jobs both modify the same firewall and reload the service within seconds, producing unpredictable intermediate state.

### Failure / Troubleshooting Workflow
```text
concurrent run suspected
  ↓
automation execution history
  ↓
lock/change ticket
  ↓
target timestamps
  ↓
stop/serialize
  ↓
reconcile desired state
```

### Best Practice
Prevent concurrent writers for resources that cannot tolerate overlap.

---

## Advanced Deep Dive 49 — Dynamic Inventory Cache and Freshness

### Concept and Detailed Explanation
Dynamic inventory systems often cache API/CMDB data for performance. Caching introduces a freshness tradeoff: too short creates API pressure, too long targets deleted systems or misses newly created ones.

### Internal / Architecture Model
```text
Authoritative API
   |
inventory query
   |
cache
   |
automation target list

Freshness window matters
```

### Commands / Code / Configuration
```text
Inventory controls:
cache TTL
manual refresh
filter
source timestamp
target preview
```

### Expected State / Output
The automation can show when inventory was last refreshed and refresh it before high-risk production runs.

### Why It Works
Dynamic discovery is only as accurate as the source plus cache age.

### Production Example
A server is decommissioned in cloud inventory but remains in a 24-hour cache and still receives an attempted change.

### Failure / Troubleshooting Workflow
```text
inventory stale
  ↓
source current?
  ↓
cache timestamp/TTL
  ↓
refresh
  ↓
preview target set
```

### Best Practice
Refresh and preview dynamic inventory before destructive or security-sensitive changes.

---

## Advanced Deep Dive 50 — CMDB Accuracy and Reconciliation

### Concept and Detailed Explanation
A CMDB is useful only when records are connected to discovery and change processes. Manual-only CMDBs tend to drift. Configuration management can consume CMDB metadata and also help detect mismatches.

### Internal / Architecture Model
```text
Discovery / Cloud / Inventory
        |
        v
      CMDB
        |
 owner/service/location
        |
Configuration decisions
```

### Commands / Code / Configuration
```text
CMDB audit:
recorded hostname
actual identity
owner
environment
service
IP
last discovered
last config run
```

### Expected State / Output
CMDB records used for automation reflect current assets and relationships within a known freshness target.

### Why It Works
An authoritative record without reconciliation gradually becomes historical fiction.

### Production Example
A host changes owner/team after an acquisition but CMDB metadata is not updated, causing wrong maintenance notifications.

### Failure / Troubleshooting Workflow
```text
CMDB mismatch
  ↓
which field authoritative?
  ↓
discovery evidence
  ↓
change record
  ↓
update source
  ↓
rerun reconciliation
```

### Best Practice
Assign ownership and freshness SLOs to CMDB data domains.

---

## Advanced Deep Dive 51 — Compliance as Code and Evidence

### Concept and Detailed Explanation
Compliance as code expresses requirements as executable tests. The result should include both the rule and evidence showing which systems passed or failed. A control is stronger when it is continuously measurable rather than documented once.

### Internal / Architecture Model
```text
Policy requirement
   |
machine-readable test
   |
fleet evaluation
   |
pass/fail evidence
   |
remediation / exception
```

### Commands / Code / Configuration
```text
# Example checks
sshd -T | grep -i '^permitrootlogin no'
systemctl is-active auditd
timedatectl show -p NTPSynchronized
```

### Expected State / Output
The organization can report current compliance state and identify exact failing systems.

### Why It Works
Executable tests reduce ambiguity in manual checklist interpretation.

### Production Example
A security standard says root SSH must be disabled; an automated test finds three servers where an emergency change re-enabled it.

### Failure / Troubleshooting Workflow
```text
compliance fail
  ↓
confirm test correctness
  ↓
is there approved exception?
  ↓
identify drift/cause
  ↓
remediate
  ↓
retain evidence
```

### Best Practice
Store the rule, rationale, remediation, and exception process together.

---

## Advanced Deep Dive 52 — Policy as Code Before Change

### Concept and Detailed Explanation
Policy as code evaluates proposed desired state before deployment. It complements configuration management by preventing unsafe configurations from being approved in the first place.

### Internal / Architecture Model
```text
Git change
  |
policy evaluation
  |
allowed?
 /     yes     no
 |       |
merge   block with reason
```

### Commands / Code / Configuration
```text
Pseudo policies:
deny SSH 0.0.0.0/0
require encryption=true
require owner tag
forbid plaintext_secret fields
require approved package repository
```

### Expected State / Output
Unsafe proposed configuration fails CI before any target is changed.

### Why It Works
Preventive controls are cheaper than detecting and repairing the same unsafe state after deployment.

### Production Example
A firewall pull request opening administrative access to the Internet is blocked by CI policy before review completes.

### Failure / Troubleshooting Workflow
```text
policy failure
  ↓
read violated rule
  ↓
is desired state actually unsafe?
  ↓
correct config or obtain documented exception
```

### Best Practice
Use policy as code for high-impact invariants, not for every subjective style preference.

---

## Advanced Deep Dive 53 — Secrets Separation and Runtime Retrieval

### Concept and Detailed Explanation
Automation code should reference secrets without containing the real values. The secret store should enforce independent access control, rotation, audit, and possibly short-lived credential issuance.

### Internal / Architecture Model
```text
Git:
db_password_ref = "secret/db/prod"

Secret Manager:
actual secret

Automation runtime:
authenticated lookup
   |
inject only where needed
```

### Commands / Code / Configuration
```text
# Conceptual
secret_ref: secret/data/prod/database
# no plaintext secret committed

Controls:
least privilege
short TTL if possible
redacted logs
rotation
audit
```

### Expected State / Output
Repository access does not automatically grant access to production secrets.

### Why It Works
Desired-state logic and secret-value confidentiality have different access requirements.

### Production Example
A developer can review nginx templates but cannot retrieve the production database password.

### Failure / Troubleshooting Workflow
```text
secret lookup fails
  ↓
automation identity
  ↓
secret path
  ↓
policy/scope
  ↓
secret version
  ↓
network/TLS
```

### Best Practice
Separate code review permissions from secret-read permissions.

---

## Advanced Deep Dive 54 — Secret Rotation with Overlap

### Concept and Detailed Explanation
Safe rotation often requires a period where both old and new credentials are valid. Consumers are moved to the new secret, verified, and only then is the old secret revoked.

Immediate replacement can create outages when all consumers do not update atomically.

### Internal / Architecture Model
```text
Create new secret
   |
provider accepts old + new
   |
update consumers
   |
verify all using new
   |
revoke old
```

### Commands / Code / Configuration
```text
Rotation record:
old version
new version
consumers
update status
verification
revocation time
rollback window
```

### Expected State / Output
Every consumer authenticates successfully with the new credential before the old credential becomes invalid.

### Why It Works
Distributed consumers change at different times; overlap prevents a gap in valid authentication.

### Production Example
Five application servers rotate a database password. Three update successfully; if the old password is revoked immediately, two remain offline.

### Failure / Troubleshooting Workflow
```text
rotation problem
  ↓
which consumers updated?
  ↓
is old credential still valid?
  ↓
restore overlap
  ↓
update failed consumers
  ↓
verify
  ↓
revoke old
```

### Best Practice
Design secret rotation as an orchestrated multi-party change.

---

## Advanced Deep Dive 55 — Certificate Lifecycle Automation

### Concept and Detailed Explanation
Certificates have a complete lifecycle: issuance, validation, deployment, private-key permissions, chain installation, service reload, expiry monitoring, renewal, and revocation. Automating only the initial copy leaves future outages waiting to happen.

### Internal / Architecture Model
```text
CA / Issuer
   |
certificate + key
   |
secure deployment
   |
service reload
   |
expiry monitoring
   |
renewal
```

### Commands / Code / Configuration
```text
openssl x509 -in cert.pem -noout -subject -issuer -dates
openssl verify -CAfile ca-chain.pem cert.pem
stat private.key
```

### Expected State / Output
The service presents the intended certificate, clients trust the chain, and renewal occurs before expiry.

### Why It Works
TLS service correctness depends on both cryptographic material and runtime reload.

### Production Example
A renewed certificate exists on disk but nginx still serves the old one because reload was never triggered.

### Failure / Troubleshooting Workflow
```text
TLS incident
  ↓
certificate dates/SAN
  ↓
chain
  ↓
private key match/permissions
  ↓
service loaded version
  ↓
reload
```

### Best Practice
Monitor actual served certificate expiry, not only files on disk.

---

## Advanced Deep Dive 56 — Control Node Security and Blast Radius

### Concept and Detailed Explanation
A configuration-management controller can authenticate to many systems and read secrets. Compromise can therefore become fleet-wide compromise. Treat the controller, automation runners, and CI executors as privileged infrastructure.

### Internal / Architecture Model
```text
Admin / CI
   |
Control Node
   |
credentials + inventory + code
   |
many managed systems
```

### Commands / Code / Configuration
```text
Security baseline:
MFA/admin access
patching
disk encryption
restricted network
secret manager
audit logs
ephemeral runners where possible
backups
EDR/monitoring
```

### Expected State / Output
The control plane is reachable only through approved administrative paths and credentials are scoped/audited.

### Why It Works
Automation centralizes powerful access that previously existed across many manual admin sessions.

### Production Example
A compromised CI runner has a universal root SSH key and can change every production server.

### Failure / Troubleshooting Workflow
```text
controller compromise
  ↓
isolate runner
  ↓
revoke automation credentials
  ↓
audit recent runs
  ↓
validate target drift
  ↓
rebuild controller from trusted state
```

### Best Practice
Minimize credential scope and prefer short-lived/ephemeral automation identities.

---

## Advanced Deep Dive 57 — Least Privilege for Automation

### Concept and Detailed Explanation
Automation often defaults to broad root/Administrator rights because it is convenient. A mature design separates read-only inventory, OS administration, network administration, secret retrieval, and production deployment permissions.

### Internal / Architecture Model
```text
Automation identity
  |
role/scope
  |
only required:
targets
commands/modules
secret paths
API actions
environment
```

### Commands / Code / Configuration
```text
Privilege matrix:
Job              Targets      Privilege
Inventory        all          read-only
Web baseline     web          sudo limited/root as needed
Network audit    routers      read-only
Prod deploy      prod app     approved deploy role
```

### Expected State / Output
A stolen or misused automation credential cannot automatically control unrelated environments and systems.

### Why It Works
Least privilege reduces the blast radius of automation bugs and credential compromise.

### Production Example
A staging automation token is mistakenly used by a script but cannot modify production because environment scope is enforced.

### Failure / Troubleshooting Workflow
```text
permission denied
  ↓
is operation legitimately required?
  ↓
adjust narrow role
  ↓
avoid granting global admin as quick fix
```

### Best Practice
Grant privilege to the automation use case, not to the tool as a whole.

---

## Advanced Deep Dive 58 — Observability for Configuration Automation

### Concept and Detailed Explanation
Automation should emit structured data about who ran it, which Git commit/version, target set, changed resources, failures, duration, retries, drift count, and verification result. This turns automation from a black box into an operational system.

### Internal / Architecture Model
```text
Git commit
   |
automation run ID
   |
targets / tasks
   |
changes / failures
   |
post-checks
   |
metrics + logs + audit
```

### Commands / Code / Configuration
```text
Run event fields:
run_id
git_commit
actor
environment
target_count
changed_count
failed_count
duration
rollback
verification_status
```

### Expected State / Output
An incident can be correlated to an exact automation run and desired-state revision.

### Why It Works
Reliable operations require evidence linking intent to execution and outcome.

### Production Example
At 14:03 application errors start. The monitoring system links the time to run 8842, commit abc123, and the three hosts changed in the current wave.

### Failure / Troubleshooting Workflow
```text
incident correlation
  ↓
time
  ↓
automation run
  ↓
commit
  ↓
targets
  ↓
changed resources
  ↓
verification
```

### Best Practice
Make run IDs and Git commit IDs first-class audit fields.

---

## Advanced Deep Dive 59 — Automation SLOs and Reliability Metrics

### Concept and Detailed Explanation
Configuration management itself is a production service. Useful measures include run success rate, median/p95 duration, unreachable targets, drift backlog, idempotency violations, rollback rate, stale baseline age, and post-change health failures.

### Internal / Architecture Model
```text
Automation metrics
  |
success
duration
drift
rollback
verification
  |
platform SLO
```

### Commands / Code / Configuration
```text
Example:
95% scheduled compliance runs succeed
99% targets checked within 24h
p95 production rollout < 30 min
0 secrets printed to logs
<1% hosts in unresolved drift > 24h
```

### Expected State / Output
Operators can tell whether automation is improving fleet consistency rather than merely existing.

### Why It Works
A tool can run every day yet leave 15% of hosts perpetually unreachable and unmanaged.

### Production Example
Dashboards show a rising unreachable-host rate after a network ACL change, revealing automation coverage degradation.

### Failure / Troubleshooting Workflow
```text
automation SLO breach
  ↓
which metric?
  ↓
common targets/failure layer
  ↓
capacity/transport/tool issue
  ↓
remediate
```

### Best Practice
Measure configuration coverage and verification outcomes, not only pipeline success.

---

## Advanced Deep Dive 60 — Rebuildability as a Disaster-Recovery Test

### Concept and Detailed Explanation
A mature configuration system should be able to recreate a lost server's intended configuration from authoritative sources without copying undocumented state from the failed machine.

Rebuildability reveals hidden dependencies, manual changes, missing secrets, and untracked data.

### Internal / Architecture Model
```text
Lost server
   |
image/provisioning
   |
inventory/IPAM/CMDB
   |
Git desired state
   |
secret manager
   |
application artifact
   |
data restore
   |
verified replacement
```

### Commands / Code / Configuration
```text
Rebuild checklist:
image
network
DNS
inventory
Git commit
secrets
certificates
application artifact
business data
monitoring
backup registration
```

### Expected State / Output
A replacement server can be built and validated from controlled sources inside the target RTO.

### Why It Works
Configuration management protects reproducible configuration, while backups protect data and secret recovery systems protect credentials.

### Production Example
A web server is destroyed and rebuilt successfully, but the team discovers one application license file had existed only on the old host.

### Failure / Troubleshooting Workflow
```text
rebuild fails
  ↓
what state is missing?
  ↓
which source should own it?
  ↓
capture into code/secret/data backup
  ↓
repeat rebuild test
```

### Best Practice
Perform periodic rebuild tests to expose undocumented state before a disaster.

---


# Enhanced Practical Lab Series — Configuration Management

These labs extend the original labs and are intended to turn the concepts into repeatable operational skills.

## Enhanced Lab 1 — Desired State as a Formal Contract

### Objective
Demonstrate **Desired State as a Formal Contract** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
desired:
  nginx:
    package: present
    service: running
    enabled: true
  config:
    path: /etc/nginx/nginx.conf
    owner: root
    mode: "0644"
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Two engineers reading the definition agree on what the compliant end state must be.

### Troubleshooting Path
```text
automation behaves strangely
  ↓
is desired state explicit?
  ↓
which attributes are authoritative?
  ↓
what evidence proves compliance?
  ↓
clarify contract before changing implementation
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 2 — Actual State, Observation, and Facts

### Objective
Demonstrate **Actual State, Observation, and Facts** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
rpm -q nginx 2>/dev/null || dpkg-query -W nginx 2>/dev/null || true
systemctl is-enabled nginx
systemctl is-active nginx
stat /etc/nginx/nginx.conf
ss -lntp
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The evidence reflects current target state independently of what automation expected to happen.

### Troubleshooting Path
```text
desired says correct but service broken
  ↓
observe actual system
  ↓
compare files/packages/service/runtime
  ↓
identify drift or runtime failure
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 3 — Convergence as a Control Loop

### Objective
Demonstrate **Convergence as a Control Loop** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
for i in 1 2 3; do
  ./apply-configuration.sh
  ./verify-state.sh
done
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Later runs make fewer changes and a stable target produces a no-change result.

### Troubleshooting Path
```text
never converges
  ↓
identify resource changing every run
  ↓
compare rendered desired vs actual
  ↓
timestamp/random value?
  ↓
external tool modifying same resource?
  ↓
fix ownership/idempotency
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 4 — Idempotency Beyond 'Run Twice'

### Objective
Demonstrate **Idempotency Beyond 'Run Twice'** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Bad
echo "10.0.0.10 api" >> /etc/hosts

# Better shell guard
grep -qxF "10.0.0.10 api" /etc/hosts ||
  echo "10.0.0.10 api" >> /etc/hosts
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Repeated runs leave one correct entry and do not restart/rewrite resources unnecessarily.

### Troubleshooting Path
```text
changed every run
  ↓
compare before/after content
  ↓
hidden timestamp/order?
  ↓
module reports change incorrectly?
  ↓
side-effect command unconditional?
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 5 — Imperative vs Declarative as Design Choices

### Objective
Demonstrate **Imperative vs Declarative as Design Choices** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Declarative-like pseudo state
service:
  name: nginx
  state: started

# Imperative one-time operation
./migrate-db --to 42
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Stable resources converge declaratively, while one-time operations have explicit guards and completion markers.

### Troubleshooting Path
```text
automation repeats destructive command
  ↓
is this resource state or event?
  ↓
add guard/version marker
  ↓
separate migration workflow if needed
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 6 — Configuration Management vs Provisioning Ownership

### Objective
Demonstrate **Configuration Management vs Provisioning Ownership** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Ownership matrix:
Resource                  Owner
VM                        Terraform
Security group            Terraform
OS packages               Config Mgmt
/etc/sshd_config          Config Mgmt
Application artifact      Deployment pipeline
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
No two tools continuously fight over the same resource.

### Troubleshooting Path
```text
resource keeps reverting
  ↓
list every tool touching it
  ↓
identify authoritative owner
  ↓
remove duplicate management
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 7 — Configuration Management vs Orchestration

### Objective
Demonstrate **Configuration Management vs Orchestration** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
workflow:
  - disable_backend: web01
  - wait_connections_drained
  - apply_baseline: web01
  - verify_health: web01
  - enable_backend: web01
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Each node reaches desired configuration without removing all service capacity at once.

### Troubleshooting Path
```text
fleet outage risk
  ↓
identify service dependency
  ↓
define drain/order/quorum rules
  ↓
configure serially
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 8 — Mutable vs Immutable Infrastructure

### Objective
Demonstrate **Mutable vs Immutable Infrastructure** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Mutable
systemctl reload nginx

# Immutable conceptual pipeline
build image
test image
deploy new instances
health check
shift traffic
remove old instances
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Operations use the model appropriate to the platform rather than mixing ad-hoc mutation into disposable systems.

### Troubleshooting Path
```text
drift appears in immutable fleet
  ↓
was instance mutated manually?
  ↓
rebuild from approved image
  ↓
remove manual mutation path
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 9 — Day 0, Day 1, and Day 2 Responsibility

### Objective
Demonstrate **Day 0, Day 1, and Day 2 Responsibility** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Lifecycle checklist:
Day0: network, identity, image, storage
Day1: users, packages, services, baseline
Day2: patch, drift, certs, secrets, upgrades, decommission
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The same configuration model supports ongoing maintenance and recovery, not only first deployment.

### Troubleshooting Path
```text
operational gap
  ↓
which lifecycle stage owns it?
  ↓
add Day2 automation/runbook
  ↓
test periodic operation
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 10 — Source of Truth by Data Domain

### Objective
Demonstrate **Source of Truth by Data Domain** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Data Domain        Authority       Consumer
NTP servers        Git/CMDB        Config Mgmt
IP addresses       IPAM            Inventory
DB password        Secret Manager  App config
Instance ID        Cloud API       Dynamic inventory
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Every variable has one documented authoritative source.

### Troubleshooting Path
```text
data mismatch
  ↓
which system owns value?
  ↓
remove duplicated authority
  ↓
integrate consumers with source
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 11 — Inventory Identity and Stable Targeting

### Objective
Demonstrate **Inventory Identity and Stable Targeting** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
hosts:
  web01:
    address: 10.0.1.15
    groups: [prod, web, dc1]
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Changing an IP or connection method does not require changing the conceptual host identity.

### Troubleshooting Path
```text
wrong target
  ↓
inventory identity
  ↓
connection address
  ↓
group membership
  ↓
environment scope
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 12 — Static vs Dynamic Inventory

### Objective
Demonstrate **Static vs Dynamic Inventory** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Conceptual dynamic filter:
environment == "prod"
AND managed_by == "platform"
AND lifecycle_state == "active"
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The target set matches the authoritative source and excludes unmanaged or retired systems.

### Troubleshooting Path
```text
dynamic inventory unexpected
  ↓
query filters
  ↓
API credentials/scope
  ↓
tags/metadata
  ↓
cache freshness
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 13 — Group Composition and Cross-Cutting Roles

### Objective
Demonstrate **Group Composition and Cross-Cutting Roles** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
groups:
  prod: [web01, db01]
  web: [web01, web02]
  pci: [web01, db01]
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Common baselines and role-specific configuration combine predictably for a host.

### Troubleshooting Path
```text
unexpected effective config
  ↓
list all host groups
  ↓
identify overlapping variables/policies
  ↓
remove contradictory group ownership
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 14 — Variable Hierarchy and Override Discipline

### Objective
Demonstrate **Variable Hierarchy and Override Discipline** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
http_port:
  default: 8080
  prod: 8443

# Document exceptions:
web07:
  http_port: 9443
  reason: legacy integration
  expires: 2026-12-01
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Most hosts inherit common values; exceptions are few, documented, and time-bounded.

### Troubleshooting Path
```text
wrong effective value
  ↓
search all definitions
  ↓
show precedence/source
  ↓
remove stale exception
  ↓
test effective config
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 15 — Templates as Controlled Compilation

### Objective
Demonstrate **Templates as Controlled Compilation** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Jinja-like
server {
    listen {{ http_port }};
    server_name {{ server_name }};
}

# Validation
nginx -t -c /path/to/candidate.conf
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Identical inputs produce identical output and invalid output is rejected before service reload.

### Troubleshooting Path
```text
template deployment fails
  ↓
input data
  ↓
rendered candidate
  ↓
syntax checker
  ↓
permissions/ownership
  ↓
install/reload
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 16 — Configuration File Ownership, Mode, and Atomic Replacement

### Objective
Demonstrate **Configuration File Ownership, Mode, and Atomic Replacement** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
install -o root -g root -m 0644 new.conf /etc/myapp/myapp.conf
stat /etc/myapp/myapp.conf
ls -Z /etc/myapp/myapp.conf 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The file has correct content, ownership, mode, and security context, and the service reads a complete file.

### Troubleshooting Path
```text
config correct but service/security wrong
  ↓
content
  ↓
owner/group/mode
  ↓
SELinux/AppArmor context
  ↓
parent directory
  ↓
service read access
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 17 — Handlers, Notifications, and Change-Driven Side Effects

### Objective
Demonstrate **Handlers, Notifications, and Change-Driven Side Effects** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Pseudo declarative flow
template config
  notify: reload nginx

handler reload nginx
  when: notified
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Repeated no-change runs do not reload services; several related file changes can trigger one handler at the end.

### Troubleshooting Path
```text
service reloading every run
  ↓
why task reports changed?
  ↓
template nondeterministic?
  ↓
handler triggered unconditionally?
  ↓
fix change detection
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 18 — Reload vs Restart Decision

### Objective
Demonstrate **Reload vs Restart Decision** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
nginx -t && systemctl reload nginx
sshd -t && systemctl reload sshd 2>/dev/null || true
systemctl restart <service>
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The chosen action applies the configuration and service health remains acceptable.

### Troubleshooting Path
```text
change not taking effect
  ↓
is setting reloadable?
  ↓
service documentation
  ↓
runtime status
  ↓
restart only if required
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 19 — Package State and Version Governance

### Objective
Demonstrate **Package State and Version Governance** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
apt-cache policy nginx 2>/dev/null || true
dnf info nginx 2>/dev/null || true
rpm -q nginx 2>/dev/null || true
dpkg-query -W nginx 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Production hosts run the approved package version/channel and upgrades occur through an explicit change process.

### Troubleshooting Path
```text
package drift
  ↓
installed version
  ↓
configured repository
  ↓
pin/lock policy
  ↓
approved target version
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 20 — Repository Trust and Software Supply Chain

### Objective
Demonstrate **Repository Trust and Software Supply Chain** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Inventory dependencies:
component
source URL
version
hash/signature
owner
update cadence

# Example package repo inspection:
apt-cache policy 2>/dev/null | head
dnf repolist 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Automation consumes only approved dependency sources and versions with documented update ownership.

### Troubleshooting Path
```text
supply-chain concern
  ↓
identify artifact/source
  ↓
version/hash/signature
  ↓
who approved?
  ↓
isolate dependency
  ↓
restore known-good version
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 21 — User Lifecycle as Desired State

### Objective
Demonstrate **User Lifecycle as Desired State** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
id appsvc 2>/dev/null || true
getent passwd appsvc
getent group appadmins
passwd -S appsvc 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The account has exactly the intended access and obsolete memberships/keys are absent.

### Troubleshooting Path
```text
access drift
  ↓
account identity
  ↓
group memberships
  ↓
SSH keys
  ↓
sudo policy
  ↓
desired role
  ↓
remove stale access
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 22 — SSH Key Management and Private-Key Boundaries

### Objective
Demonstrate **SSH Key Management and Private-Key Boundaries** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
ssh-keygen -lf ~/.ssh/authorized_keys 2>/dev/null || true
grep -n 'ssh-' ~/.ssh/authorized_keys 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Only approved public keys exist; revoked keys disappear after the controlled rotation window.

### Troubleshooting Path
```text
SSH access problem
  ↓
expected public key?
  ↓
file ownership/mode
  ↓
sshd policy
  ↓
account/group
  ↓
key rotation state
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 23 — Sudo / Privilege Policy as Code

### Objective
Demonstrate **Sudo / Privilege Policy as Code** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
visudo -cf /etc/sudoers
sudo -l -U backupops 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Sudoers syntax is valid and each operational role can execute only required privileged actions.

### Troubleshooting Path
```text
sudo policy failure
  ↓
syntax validation
  ↓
effective rules
  ↓
group membership
  ↓
command path/arguments
  ↓
least-privilege correction
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 24 — Firewall State as a Dependency-Aware Resource

### Objective
Demonstrate **Firewall State as a Dependency-Aware Resource** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Linux examples
firewall-cmd --list-all 2>/dev/null || true
nft list ruleset 2>/dev/null || true
ss -lntp
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Required management and application flows work; unauthorized flows remain blocked.

### Troubleshooting Path
```text
firewall change
  ↓
preserve control path
  ↓
apply new rule
  ↓
verify from external probe
  ↓
remove old rule
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 25 — Sysctl Runtime vs Persistent State

### Objective
Demonstrate **Sysctl Runtime vs Persistent State** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
sysctl net.ipv4.ip_forward
grep -R "net.ipv4.ip_forward" /etc/sysctl.conf /etc/sysctl.d 2>/dev/null || true
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The current runtime value and persistent configuration agree.

### Troubleshooting Path
```text
sysctl mismatch
  ↓
current runtime
  ↓
which config file defines value?
  ↓
precedence/duplicate definitions
  ↓
apply persistent + runtime desired state
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 26 — Mounts as Multi-Layer State

### Objective
Demonstrate **Mounts as Multi-Layer State** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
findmnt /data
grep -n '/data' /etc/fstab
mount -a -f 2>/dev/null || true
stat /data
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The mount is present with correct options and survives reboot while the application can read/write as intended.

### Troubleshooting Path
```text
mount problem
  ↓
source reachability
  ↓
mount config/options
  ↓
credentials
  ↓
runtime mount
  ↓
application path
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 27 — Scheduled Tasks Without Duplication

### Objective
Demonstrate **Scheduled Tasks Without Duplication** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
crontab -l 2>/dev/null || true
systemctl list-timers --all | head -30
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Exactly one intended job exists with the correct schedule and command.

### Troubleshooting Path
```text
duplicate scheduled job
  ↓
identify owning automation
  ↓
normalize to one resource
  ↓
remove duplicates
  ↓
verify next run
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 28 — Application Configuration Ownership Boundary

### Objective
Demonstrate **Application Configuration Ownership Boundary** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Ownership record:
Path/Resource | Owner Tool | Team | Change Process
/etc/nginx/*  | Config Mgmt | Platform | infra PR
/opt/app/*    | Deploy CI   | App      | app release
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Every managed resource has one authoritative writer.

### Troubleshooting Path
```text
resource oscillates
  ↓
who writes it?
  ↓
list tools/scripts/packages
  ↓
select authoritative owner
  ↓
remove competing writer
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 29 — Dependency Graphs and Topological Ordering

### Objective
Demonstrate **Dependency Graphs and Topological Ordering** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Pseudo dependency declaration
repo -> package
package -> config
certificate -> tls_config
config -> service_reload
service_reload -> health_check
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Each resource is applied only after its prerequisites are valid.

### Troubleshooting Path
```text
resource failure
  ↓
what prerequisites does it consume?
  ↓
verify upstream dependency
  ↓
correct ordering/readiness
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 30 — Readiness vs Mere Process State

### Objective
Demonstrate **Readiness vs Mere Process State** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
systemctl is-active nginx
ss -lntp | grep ':443'
curl --fail --max-time 5 https://localhost/health
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The verification proves the level of service actually required by the rollout decision.

### Troubleshooting Path
```text
automation says success
  ↓
process?
  ↓
port?
  ↓
health endpoint?
  ↓
business dependency?
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 31 — Canary Rollout as Risk Measurement

### Objective
Demonstrate **Canary Rollout as Risk Measurement** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Canary gate:
- config syntax valid
- service healthy
- application error rate normal
- latency within SLO
- no new critical alert
- rollback still possible
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The rollout automatically or procedurally stops when canary acceptance criteria fail.

### Troubleshooting Path
```text
canary fails
  ↓
stop further waves
  ↓
collect evidence
  ↓
rollback or forward-fix canary
  ↓
update change
  ↓
retest
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 32 — Serial Rollout and Batch Sizing

### Objective
Demonstrate **Serial Rollout and Batch Sizing** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Batch design:
minimum healthy instances
load balancer capacity
quorum rules
database connection surge
restart time
rollback time
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The service remains above required capacity during every wave and each batch passes health checks before the next begins.

### Troubleshooting Path
```text
rollout overload
  ↓
batch size
  ↓
remaining service capacity
  ↓
backend/load impact
  ↓
reduce concurrency
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 33 — Quorum-Aware Changes

### Objective
Demonstrate **Quorum-Aware Changes** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Quorum worksheet:
members
voters
majority required
current unhealthy members
maintenance members
remaining votes
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Quorum remains available during each maintenance step and every node rejoins healthy before the next step.

### Troubleshooting Path
```text
quorum risk
  ↓
current members healthy?
  ↓
votes required
  ↓
planned concurrent changes
  ↓
reduce batch/stop
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 34 — Load Balancer Drain and Connection Grace

### Objective
Demonstrate **Load Balancer Drain and Connection Grace** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Drain steps:
disable backend
query active connections
wait with timeout
apply configuration
verify health
enable backend
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
New traffic avoids the node during maintenance and existing sessions end cleanly within the defined drain window.

### Troubleshooting Path
```text
drain hangs
  ↓
active connection count
  ↓
maximum drain deadline
  ↓
business policy for forced close
  ↓
continue or abort
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 35 — Maintenance Windows and Change Deadlines

### Objective
Demonstrate **Maintenance Windows and Change Deadlines** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Change record:
start_time
stop_time
rollback_deadline
owner
approver
monitor
escalation_contact
expected_impact
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Operators know when to stop attempting fixes and execute the planned recovery path.

### Troubleshooting Path
```text
change running long
  ↓
current time vs rollback deadline
  ↓
business impact
  ↓
continue / rollback / escalate
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 36 — Dry Run and Check-Mode Limitations

### Objective
Demonstrate **Dry Run and Check-Mode Limitations** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Dry-run review:
predicted changed hosts
predicted files/packages
tasks skipped in check mode
unknown commands/APIs
secret-sensitive diffs
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Operators know which parts of the change were actually predicted and which require staging/canary evidence.

### Troubleshooting Path
```text
dry run says no problem, real run fails
  ↓
which task lacked predictive support?
  ↓
add integration test/canary
  ↓
improve validation
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 37 — Diff Mode and Secret Leakage

### Objective
Demonstrate **Diff Mode and Secret Leakage** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Classification:
public config → diff allowed
internal topology → restricted logs
secret material → diff suppressed/redacted
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Reviewers can see safe configuration changes without sensitive values appearing in logs.

### Troubleshooting Path
```text
secret shown in log
  ↓
rotate affected secret
  ↓
restrict/delete log copy
  ↓
mark resource no-log/redacted
  ↓
audit exposure
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 38 — Static Validation vs Runtime Validation

### Objective
Demonstrate **Static Validation vs Runtime Validation** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
nginx -t
sshd -t
visudo -c
named-checkconf

# Runtime
curl --fail https://service/health
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Invalid syntax is blocked before deployment and semantic/runtime failures are detected before rollout continues.

### Troubleshooting Path
```text
validation failure
  ↓
syntax?
  ↓
service startup?
  ↓
dependency?
  ↓
business response?
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 39 — Configuration Testing Pyramid

### Objective
Demonstrate **Configuration Testing Pyramid** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Pipeline:
lint
render test
idempotency test
service syntax test
integration health
security policy check
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Simple failures are caught early and expensive real-environment tests focus on integration behavior.

### Troubleshooting Path
```text
production bug escaped
  ↓
which test layer could have detected it?
  ↓
add regression test at cheapest appropriate layer
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 40 — Idempotency Testing in Disposable Systems

### Objective
Demonstrate **Idempotency Testing in Disposable Systems** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Test steps:
1. build VM/container
2. run automation
3. capture changed resources
4. run again
5. assert no change
6. modify one managed file
7. rerun
8. assert only drift corrected
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The second run is stable and deliberate drift is repaired without unrelated changes.

### Troubleshooting Path
```text
idempotency test fails
  ↓
find always-changed resource
  ↓
compare desired/actual
  ↓
remove nondeterminism
  ↓
repeat test
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 41 — Rollback vs Forward Fix

### Objective
Demonstrate **Rollback vs Forward Fix** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Recovery classification:
config file        → previous version
package            → previous package if compatible
database schema    → migration-specific
secret rotation    → dual-secret/forward transition
data transformation→ restore or corrective migration
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Operators know whether rollback is valid and have artifacts/runbooks for the chosen recovery path.

### Troubleshooting Path
```text
change failed
  ↓
is old state still compatible?
  ↓
data/schema changed?
  ↓
rollback or forward-fix plan
  ↓
verify consistency
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 42 — Partial Failure and Fleet Inconsistency

### Objective
Demonstrate **Partial Failure and Fleet Inconsistency** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Partial-failure report:
host
before version
after version
failure reason
service health
traffic status
next action
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Every target's state is known and the recovery decision is explicit.

### Troubleshooting Path
```text
partial failure
  ↓
stop next wave
  ↓
classify compatibility
  ↓
traffic isolate if needed
  ↓
repair failed or rollback changed
  ↓
restore uniform supported state
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 43 — Compensating Actions and Saga-Like Recovery

### Objective
Demonstrate **Compensating Actions and Saga-Like Recovery** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Example:
remove node from LB
install package
write config
restart fails

Compensation:
restore previous config
restore package if safe
verify old service
return to LB
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The workflow leaves the environment in a known serviceable state after failure rather than an undocumented half-state.

### Troubleshooting Path
```text
step fails
  ↓
what earlier steps committed?
  ↓
which are reversible?
  ↓
run compensations in safe reverse dependency order
  ↓
verify
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 44 — Retries, Backoff, and Error Classification

### Objective
Demonstrate **Retries, Backoff, and Error Classification** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Retry policy:
max_attempts: 5
initial_delay: 2s
backoff: exponential
jitter: enabled
retry_on:
  - timeout
  - selected 5xx
  - temporary lock
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Transient faults recover without endless loops while deterministic configuration errors surface immediately.

### Troubleshooting Path
```text
repeated failure
  ↓
classify error
  ↓
transient or deterministic?
  ↓
bounded retry/backoff
  ↓
final fail with evidence
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 45 — Timeouts and Hung Targets

### Objective
Demonstrate **Timeouts and Hung Targets** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
timeout 30s ssh host command
curl --max-time 10 https://service/health
systemctl stop myapp  # pair orchestration with an external deadline if needed
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The run reports a bounded failure and can continue or stop according to rollout policy.

### Troubleshooting Path
```text
run hanging
  ↓
which operation/host?
  ↓
timeout configured?
  ↓
collect target process/network state
  ↓
fail host cleanly
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 46 — Unreachable vs Failed Targets

### Objective
Demonstrate **Unreachable vs Failed Targets** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Transport checks
ping <host>             # only if ICMP is relevant
ssh -vvv user@host
nc -vz <host> 22 2>/dev/null || true

# On target after connection:
id
sudo -n true
systemctl status <service>
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The operator can classify the incident before changing application configuration.

### Troubleshooting Path
```text
target problem
  ↓
name resolution
  ↓
network/port
  ↓
authentication
  ↓
privilege
  ↓
module/action
  ↓
application
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 47 — Concurrency, Forks, and Backend Pressure

### Objective
Demonstrate **Concurrency, Forks, and Backend Pressure** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Concurrency worksheet:
target_count
max_parallel
package_repo_capacity
API rate limits
database connection limit
LB spare capacity
network bandwidth
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Parallelism improves duration without exceeding shared backend limits or service SLOs.

### Troubleshooting Path
```text
run slows/fails under scale
  ↓
parallelism
  ↓
shared backend metrics
  ↓
rate limits
  ↓
reduce batch/forks
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 48 — Distributed Locks and Change Collisions

### Objective
Demonstrate **Distributed Locks and Change Collisions** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Lock identity:
environment
resource/group
change type
owner
expiry/lease

# Local illustration
flock /var/lock/platform-change.lock ./apply.sh
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Overlapping incompatible production changes are prevented or detected before mutation.

### Troubleshooting Path
```text
concurrent run suspected
  ↓
automation execution history
  ↓
lock/change ticket
  ↓
target timestamps
  ↓
stop/serialize
  ↓
reconcile desired state
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 49 — Dynamic Inventory Cache and Freshness

### Objective
Demonstrate **Dynamic Inventory Cache and Freshness** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Inventory controls:
cache TTL
manual refresh
filter
source timestamp
target preview
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The automation can show when inventory was last refreshed and refresh it before high-risk production runs.

### Troubleshooting Path
```text
inventory stale
  ↓
source current?
  ↓
cache timestamp/TTL
  ↓
refresh
  ↓
preview target set
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 50 — CMDB Accuracy and Reconciliation

### Objective
Demonstrate **CMDB Accuracy and Reconciliation** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
CMDB audit:
recorded hostname
actual identity
owner
environment
service
IP
last discovered
last config run
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
CMDB records used for automation reflect current assets and relationships within a known freshness target.

### Troubleshooting Path
```text
CMDB mismatch
  ↓
which field authoritative?
  ↓
discovery evidence
  ↓
change record
  ↓
update source
  ↓
rerun reconciliation
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 51 — Compliance as Code and Evidence

### Objective
Demonstrate **Compliance as Code and Evidence** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Example checks
sshd -T | grep -i '^permitrootlogin no'
systemctl is-active auditd
timedatectl show -p NTPSynchronized
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The organization can report current compliance state and identify exact failing systems.

### Troubleshooting Path
```text
compliance fail
  ↓
confirm test correctness
  ↓
is there approved exception?
  ↓
identify drift/cause
  ↓
remediate
  ↓
retain evidence
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 52 — Policy as Code Before Change

### Objective
Demonstrate **Policy as Code Before Change** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Pseudo policies:
deny SSH 0.0.0.0/0
require encryption=true
require owner tag
forbid plaintext_secret fields
require approved package repository
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Unsafe proposed configuration fails CI before any target is changed.

### Troubleshooting Path
```text
policy failure
  ↓
read violated rule
  ↓
is desired state actually unsafe?
  ↓
correct config or obtain documented exception
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 53 — Secrets Separation and Runtime Retrieval

### Objective
Demonstrate **Secrets Separation and Runtime Retrieval** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
# Conceptual
secret_ref: secret/data/prod/database
# no plaintext secret committed

Controls:
least privilege
short TTL if possible
redacted logs
rotation
audit
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Repository access does not automatically grant access to production secrets.

### Troubleshooting Path
```text
secret lookup fails
  ↓
automation identity
  ↓
secret path
  ↓
policy/scope
  ↓
secret version
  ↓
network/TLS
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 54 — Secret Rotation with Overlap

### Objective
Demonstrate **Secret Rotation with Overlap** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Rotation record:
old version
new version
consumers
update status
verification
revocation time
rollback window
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Every consumer authenticates successfully with the new credential before the old credential becomes invalid.

### Troubleshooting Path
```text
rotation problem
  ↓
which consumers updated?
  ↓
is old credential still valid?
  ↓
restore overlap
  ↓
update failed consumers
  ↓
verify
  ↓
revoke old
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 55 — Certificate Lifecycle Automation

### Objective
Demonstrate **Certificate Lifecycle Automation** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
openssl x509 -in cert.pem -noout -subject -issuer -dates
openssl verify -CAfile ca-chain.pem cert.pem
stat private.key
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The service presents the intended certificate, clients trust the chain, and renewal occurs before expiry.

### Troubleshooting Path
```text
TLS incident
  ↓
certificate dates/SAN
  ↓
chain
  ↓
private key match/permissions
  ↓
service loaded version
  ↓
reload
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 56 — Control Node Security and Blast Radius

### Objective
Demonstrate **Control Node Security and Blast Radius** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Security baseline:
MFA/admin access
patching
disk encryption
restricted network
secret manager
audit logs
ephemeral runners where possible
backups
EDR/monitoring
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
The control plane is reachable only through approved administrative paths and credentials are scoped/audited.

### Troubleshooting Path
```text
controller compromise
  ↓
isolate runner
  ↓
revoke automation credentials
  ↓
audit recent runs
  ↓
validate target drift
  ↓
rebuild controller from trusted state
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 57 — Least Privilege for Automation

### Objective
Demonstrate **Least Privilege for Automation** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Privilege matrix:
Job              Targets      Privilege
Inventory        all          read-only
Web baseline     web          sudo limited/root as needed
Network audit    routers      read-only
Prod deploy      prod app     approved deploy role
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
A stolen or misused automation credential cannot automatically control unrelated environments and systems.

### Troubleshooting Path
```text
permission denied
  ↓
is operation legitimately required?
  ↓
adjust narrow role
  ↓
avoid granting global admin as quick fix
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 58 — Observability for Configuration Automation

### Objective
Demonstrate **Observability for Configuration Automation** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Run event fields:
run_id
git_commit
actor
environment
target_count
changed_count
failed_count
duration
rollback
verification_status
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
An incident can be correlated to an exact automation run and desired-state revision.

### Troubleshooting Path
```text
incident correlation
  ↓
time
  ↓
automation run
  ↓
commit
  ↓
targets
  ↓
changed resources
  ↓
verification
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 59 — Automation SLOs and Reliability Metrics

### Objective
Demonstrate **Automation SLOs and Reliability Metrics** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Example:
95% scheduled compliance runs succeed
99% targets checked within 24h
p95 production rollout < 30 min
0 secrets printed to logs
<1% hosts in unresolved drift > 24h
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
Operators can tell whether automation is improving fleet consistency rather than merely existing.

### Troubleshooting Path
```text
automation SLO breach
  ↓
which metric?
  ↓
common targets/failure layer
  ↓
capacity/transport/tool issue
  ↓
remediate
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---

## Enhanced Lab 60 — Rebuildability as a Disaster-Recovery Test

### Objective
Demonstrate **Rebuildability as a Disaster-Recovery Test** and prove the resulting state using evidence rather than assumption.

### Preparation
1. Use a disposable repository, VM, container, or explicitly authorized lab target.
2. Record the before-state.
3. Identify what should change and what must remain unchanged.
4. Define the verification step before executing the change.

### Mental Model
```text
Desired action/state
      |
Tool / command / automation
      |
Observed actual state
      |
Verification
      |
Recovery if wrong
```

### Commands / Data
```text
Rebuild checklist:
image
network
DNS
inventory
Git commit
secrets
certificates
application artifact
business data
monitoring
backup registration
```

### Procedure
1. Draw the expected state transition.
2. Capture the current state using read-only inspection commands.
3. Perform the smallest change required by the lab.
4. Capture the resulting state and compare it with the prediction.
5. Repeat the operation where idempotency or repeatability is relevant.
6. Introduce one reversible failure in the disposable lab where safe.
7. Diagnose using the troubleshooting path below.
8. Recover using the least destructive method.
9. Record `Symptom → Evidence → Cause → Correction → Verification`.

### Expected Result
A replacement server can be built and validated from controlled sources inside the target RTO.

### Troubleshooting Path
```text
rebuild fails
  ↓
what state is missing?
  ↓
which source should own it?
  ↓
capture into code/secret/data backup
  ↓
repeat rebuild test
```

### Safety
Use disposable or explicitly authorized lab targets. Do not test firewall lockout, account removal, package downgrade, quorum loss, certificate rotation, or destructive rollback against production systems.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Manual Baseline

Build a disposable Linux VM manually.

Install:

```bash
sudo apt install nginx
sudo systemctl enable --now nginx
```

Document every command needed. This becomes the process you will later automate.

### Lab 2 — Define Desired State

Write `DESIRED_STATE.md` for the VM:

```text
hostname
users
packages
services
files
firewall
NTP
monitoring
```

Do not write commands—write state.

### Lab 3 — Identify Drift

Manually change:

```text
service state
file permissions
config line
package
```

Compare actual vs desired state and create a drift report.

### Lab 4 — Idempotent Shell

Write a Bash script that ensures:

```text
directory exists
user exists
package installed
one exact config line exists
service running
```

Run twice and prove the second run makes no duplicate changes.

### Lab 5 — Imperative vs Declarative

For five tasks, write both:

```text
imperative commands
declarative state statement
```

Compare complexity.

### Lab 6 — Source-of-Truth Matrix

Create:

```text
Data                   Authority
IP address             IPAM
server owner           CMDB
desired config         Git
password               Vault
runtime instance ID    cloud API
```

### Lab 7 — Inventory Design

Create groups:

```text
production
staging
web
database
dc1
dc2
```

Place at least eight lab hosts conceptually into overlapping groups.

### Lab 8 — Variable Hierarchy

Define:

```text
global default
environment value
role value
host exception
```

for:

```text
timezone
NTP server
HTTP port
backup retention
```

Explain why each override belongs at that level.

### Lab 9 — Template Exercise

Create Jinja-like template:

```text
server {
    listen {{ http_port }};
    server_name {{ server_name }};
}
```

Render it manually with Python or shell substitution for two environments.

### Lab 10 — Configuration Validation

Create a deliberately invalid NGINX config.

Run:

```bash
nginx -t
```

Fix it.

Document how an automation workflow should validate before reload.

### Lab 11 — Handler Design

Design:

```text
config file changed
  → nginx reload

config unchanged
  → no reload
```

Explain why this reduces service impact.

### Lab 12 — Canary Rollout

For ten web servers, design:

```text
1 canary
2 second wave
7 final wave
```

Define health checks and stop conditions.

### Lab 13 — Rolling Maintenance

Create a runbook:

```text
remove from LB
patch
restart
health check
return to LB
```

for three application servers.

### Lab 14 — Partial Failure

Scenario:

```text
10 hosts targeted
7 succeeded
3 failed
```

Decide whether to:

```text
roll back 7
fix 3 and continue
stop
```

based on three different application scenarios.

### Lab 15 — Secrets Model

Create:

```text
config.example.yml
```

that references a secret variable but contains no real secret.

Design the secret-store retrieval flow.

### Lab 16 — Secret Rotation

Design a zero/minimal-downtime rotation:

```text
database password old
database password new
```

Include overlap, verification, and old-secret revocation.

### Lab 17 — Linux Security Baseline

Define desired state:

```text
SSH root login disabled
firewall enabled
NTP configured
audit/logging enabled
monitoring installed
admin groups controlled
```

### Lab 18 — Drift Correction Policy

Classify drift:

```text
automatic correction
alert only
emergency exception
```

for:

```text
SSH config
application feature flag
kernel parameter
temporary incident firewall rule
```

### Lab 19 — Configuration as Git

Create:

```text
configuration-management/
├── README.md
├── inventory/
├── vars/
├── templates/
├── baselines/
├── runbooks/
└── tests/
```

Commit each logical component.

### Lab 20 — Review Workflow

Create a change branch for:

```text
increase app worker count from 4 to 8
```

Write a pull-request style description covering:

```text
reason
risk
validation
rollback
blast radius
```

### Lab 21 — Compliance as Code

Write five pseudo-tests:

```text
SSH root login == no
password auth == no
firewall == active
NTP == synchronized
audit == running
```

Implement at least two with shell/Python checks.

### Lab 22 — Rebuildability Test

Assume `web01` is destroyed.

List every source needed to rebuild:

```text
image
network
DNS
Git configuration
secrets
application artifact
data/backup
```

Identify undocumented state.

### Lab 23 — Tool Ownership Matrix

For a future stack containing:

```text
Terraform
Ansible
cloud-init
Kubernetes
application deployment
```

assign one owner to each resource/configuration domain.

### Lab 24 — Failure Simulation

Analyze:

```text
SSH unreachable
sudo denied
package repo unavailable
template syntax invalid
service fails after config
secret store unavailable
half fleet changed
```

Write evidence and recovery for each.

### Lab 25 — Configuration Management Capstone Tabletop

Design a complete change:

```text
Enable TLS on 20 production web servers
```

Include:

```text
Git change
certificate secret
template
validation
canary
rolling waves
health checks
rollback
audit
drift detection
```

---

## 6. Mini Project

# Mini Project — Configuration Management Operating Model

Design a configuration-management framework for:

```text
20 Linux servers
5 Windows servers
4 network devices
2 database servers
development/staging/production
```

Required architecture:

```text
Git
  |
  +-- desired configuration
  +-- templates
  +-- tests
  +-- runbooks
  |
  v
Automation Control Plane
  |
  +-- Linux
  +-- Windows
  +-- Network
```

External systems:

```text
CMDB → ownership/assets
IPAM → IP/VLAN
Secret Manager → credentials
Monitoring → post-change verification
```

Deliverables:

```text
README.md
SOURCE_OF_TRUTH.md
INVENTORY_MODEL.md
VARIABLE_MODEL.md
BASELINES.md
SECRETS.md
CHANGE_PROCESS.md
ROLLBACK.md
DRIFT_POLICY.md
TEST_STRATEGY.md
SECURITY.md
RUNBOOKS/
```

The project should be designed so Course 47 can implement it using Ansible.

---


# Expanded Capstone — Enterprise Configuration Management Operating Model

Design an operating model that Course 47 can later implement with Ansible.

## Managed Estate

```text
40 Linux servers
10 Windows servers
8 network devices
4 database servers
2 load balancers
development
test
staging
production
two data centers
```

## Control Architecture

```text
                    Git
                     |
        desired state / templates / tests
                     |
                     v
             Automation Control Plane
                     |
       +-------------+--------------+
       |             |              |
     Linux         Windows        Network
       |             |              |
       +-------------+--------------+
                     |
                  Verify
                     |
             Monitoring / Audit
```

External authoritative systems:

```text
CMDB          → owner / service / lifecycle
IPAM          → IP / VLAN / subnet
Secret Store  → passwords / API keys / private keys
Cloud APIs    → runtime instance identity
PKI           → certificates
Monitoring    → post-change health
Ticketing     → approved change context
```

## Required Documents

```text
README.md
SOURCE_OF_TRUTH.md
RESOURCE_OWNERSHIP.md
INVENTORY_MODEL.md
VARIABLE_MODEL.md
BASELINES.md
SECRETS.md
CERTIFICATES.md
CHANGE_PROCESS.md
CANARY_AND_ROLLOUT.md
ROLLBACK_AND_FORWARD_FIX.md
DRIFT_POLICY.md
COMPLIANCE.md
TEST_STRATEGY.md
SECURITY.md
OBSERVABILITY.md
DISASTER_RECOVERY.md
RUNBOOKS/
```

## Source-of-Truth Contract

Build a table:

```text
Data Domain
Authoritative System
Read/Write Owner
Consumers
Freshness Requirement
Failure Behavior
```

Cover:

```text
host identity
IP addresses
VLANs
application owner
environment
package versions
configuration
secrets
certificates
runtime cloud IDs
maintenance state
```

## Resource Ownership Matrix

Assign exactly one primary writer for:

```text
VM
network
security group
OS package
user/group
SSH policy
firewall
application artifact
application configuration
database schema
certificate
DNS
backup policy
Kubernetes object
```

Candidate tools:

```text
Terraform
Ansible
cloud-init
application CI/CD
Kubernetes controller
PKI automation
human emergency process
```

## Baseline Model

Create:

```text
Base Linux
Base Windows
Web Server
Database Client
Monitoring
Backup Agent
Security Baseline
PCI / High-Security Overlay
```

Each reusable component must define:

```text
inputs
defaults
dependencies
outputs
side effects
restart/reload behavior
supported OS
validation
rollback/forward-fix
```

## Inventory Model

Include overlapping groups:

```text
environment
application role
data center
security class
maintenance ring
```

Design both:

```text
static lab inventory
dynamic production inventory
```

Include freshness/cache behavior.

## Variable Model

Use:

```text
safe defaults
environment values
role values
rare host exceptions
```

Every host exception requires:

```text
reason
owner
expiry/review date
```

## Change Pipeline

```text
feature branch
   |
lint/static validation
   |
template rendering tests
   |
policy-as-code
   |
integration target
   |
idempotency test
   |
staging
   |
production canary
   |
serial waves
   |
business verification
```

## Production Rollout

Design a change:

```text
Enable a new TLS baseline on 20 production web servers.
```

Required sequence:

```text
verify certificate/key
validate config
canary one server
remove from LB
drain connections
apply config
reload
health check
TLS probe
return to LB
observe
next batch
```

Define:

```text
success metrics
stop conditions
batch size
rollback deadline
forward-fix path
```

## Partial Failure Scenarios

Model:

```text
20 targets
15 success
5 unreachable

20 targets
10 new config
10 old config

quorum cluster has one pre-existing failed node

secret store unavailable halfway through rollout

package repository rate-limits automation

firewall change threatens control connection
```

For each decide:

```text
stop?
continue?
rollback changed hosts?
fix failed hosts forward?
isolate hosts from traffic?
```

## Security Model

Require:

```text
least-privilege automation identities
separate production/staging credentials
secret manager
MFA/admin access
control-node hardening
audit logs
short-lived credentials where possible
dependency pinning
signed/trusted package repositories
no secret diff logging
```

## Compliance / Drift

Create executable checks for:

```text
SSH root login disabled
password authentication policy
firewall enabled
NTP synchronized
logging/audit enabled
monitoring agent present
approved admin groups
approved package repository
certificate expiry
```

Classify drift as:

```text
auto-correct
alert-only
emergency exception
```

## Observability

Record:

```text
run_id
Git commit
actor
environment
resolved target set
changed hosts
failed hosts
unreachable hosts
duration
retry count
verification result
rollback/forward-fix
```

Metrics:

```text
run success rate
drift backlog
idempotency failures
unreachable target rate
rollback rate
configuration age
post-change failure rate
```

## Rebuildability Test

Destroy a disposable `web01` and rebuild using only:

```text
provisioning definition
inventory/IPAM/CMDB
Git desired state
secret store
PKI
application artifact
backup/data
```

Any state copied manually from the old server is a gap that must be assigned to an authoritative source.


## 7. Recommended Resources

This Markdown is intended to contain the concepts required before learning Ansible.

When you study a specific automation engine later, map each tool feature back to these concepts:

```text
inventory
desired state
idempotency
templates
variables
handlers
secrets
rollout
verification
drift
```

---

## 8. Certification Relevance

Configuration-management concepts are foundational to:

```text
Ansible
Puppet
Chef
Salt
Terraform
Kubernetes
GitOps
DevOps
SRE
Cloud Engineering
Cybersecurity hardening
```

They directly prepare you for **47. Ansible**.

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Automate commands without defining desired state.  
  **Best practice:** model the end state first.

- **Mistake:** Non-idempotent scripts.  
  **Best practice:** ensure repeat runs converge.

- **Mistake:** Store all configuration data in one flat file.  
  **Best practice:** create clear variable/data hierarchy.

- **Mistake:** Put secrets in Git.  
  **Best practice:** use dedicated secret handling.

- **Mistake:** Apply to whole fleet first.  
  **Best practice:** canary and phased rollout.

- **Mistake:** Automation success equals application success.  
  **Best practice:** perform post-change functional verification.

- **Mistake:** Two tools manage the same resource.  
  **Best practice:** define ownership.

- **Mistake:** Continuous drift correction without emergency override policy.  
  **Best practice:** design controlled exceptions.

- **Mistake:** No rollback/forward-fix plan.  
  **Best practice:** decide recovery before change.

- **Mistake:** Automate a process nobody understands manually.  
  **Best practice:** understand and document first.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is desired state?

**Short answer:** The approved configuration that should exist.

### Q2. What is drift?

**Short answer:** Difference between actual state and desired state.

### Q3. What is convergence?

**Short answer:** Repeated automation moves systems toward the same desired state.

### Q4. What is idempotency?

**Short answer:** Repeating an operation does not create unintended additional changes once desired state is reached.

### Q5. Imperative vs declarative?

**Short answer:** Imperative specifies steps; declarative specifies the state that should exist.

### Q6. Push vs pull?

**Short answer:** Push control node initiates changes; pull agents periodically retrieve/apply configuration.

### Q7. Agentless?

**Short answer:** Uses existing management protocols rather than installing a permanent management agent.

### Q8. Configuration management vs provisioning?

**Short answer:** Provisioning creates resources; configuration management establishes/maintains their OS/application state.

### Q9. What is source of truth?

**Short answer:** Authoritative system for a specific configuration/data domain.

### Q10. Why use templates?

**Short answer:** Reuse one configuration structure with controlled variable differences.

### Q11. Why use handlers?

**Short answer:** Trigger dependent actions such as service reload only when configuration changed.

### Q12. What is blast radius?

**Short answer:** Scope/importance of systems affected by a failed change.

### Q13. What is a canary?

**Short answer:** Small initial target used to validate a change before broad rollout.

### Q14. Why is dry-run imperfect?

**Short answer:** Some operations cannot predict real runtime behavior without execution.

### Q15. Why isn't automation backup?

**Short answer:** It can rebuild configuration but not necessarily recover business data/secrets.

### Q16. What is immutable infrastructure?

**Short answer:** Replace systems with newly built versions rather than repeatedly modifying them in place.

### Q17. What is a CMDB?

**Short answer:** Database of configuration items and their attributes/relationships.

### Q18. What is compliance as code?

**Short answer:** Programmatically express and test required compliance states.

### Q19. Why define resource ownership between tools?

**Short answer:** Prevent two automation systems from continually overwriting each other.

### Q20. What is the core configuration-management objective?

**Short answer:** Define, apply, verify, and maintain approved desired state safely and reproducibly.

---

# Expanded Self-Assessment Bank — Configuration Management

### Q1. What is the most important operational lesson from **Desired State as a Formal Contract**?
**Answer:** Write the end-state contract before writing tasks.

### Q2. What is the most important operational lesson from **Actual State, Observation, and Facts**?
**Answer:** Treat automation output as evidence of an attempt; verify actual state separately.

### Q3. What is the most important operational lesson from **Convergence as a Control Loop**?
**Answer:** Investigate any resource that reports changed on every run.

### Q4. What is the most important operational lesson from **Idempotency Beyond 'Run Twice'**?
**Answer:** Test both state idempotency and side-effect idempotency.

### Q5. What is the most important operational lesson from **Imperative vs Declarative as Design Choices**?
**Answer:** Model persistent state declaratively and isolate irreversible transitions.

### Q6. What is the most important operational lesson from **Configuration Management vs Provisioning Ownership**?
**Answer:** Maintain a resource-ownership matrix for the automation stack.

### Q7. What is the most important operational lesson from **Configuration Management vs Orchestration**?
**Answer:** Use orchestration around configuration changes whenever system order matters.

### Q8. What is the most important operational lesson from **Mutable vs Immutable Infrastructure**?
**Answer:** Use immutable replacement where the platform naturally supports it; do not force it onto every stateful system.

### Q9. What is the most important operational lesson from **Day 0, Day 1, and Day 2 Responsibility**?
**Answer:** Design recurring maintenance automation at the same time as initial configuration.

### Q10. What is the most important operational lesson from **Source of Truth by Data Domain**?
**Answer:** Define authority per data domain before designing variable files.

### Q11. What is the most important operational lesson from **Inventory Identity and Stable Targeting**?
**Answer:** Keep host identity stable and store mutable attributes separately.

### Q12. What is the most important operational lesson from **Static vs Dynamic Inventory**?
**Answer:** Use narrow, testable filters and preview the resolved target list before production runs.

### Q13. What is the most important operational lesson from **Group Composition and Cross-Cutting Roles**?
**Answer:** Use groups for orthogonal concerns, not as a substitute for arbitrary override layers.

### Q14. What is the most important operational lesson from **Variable Hierarchy and Override Discipline**?
**Answer:** Prefer fewer override layers and record the reason/expiry for exceptions.

### Q15. What is the most important operational lesson from **Templates as Controlled Compilation**?
**Answer:** Validate rendered configuration before replacing the live file.

### Q16. What is the most important operational lesson from **Configuration File Ownership, Mode, and Atomic Replacement**?
**Answer:** Model metadata and security context together with file content.

### Q17. What is the most important operational lesson from **Handlers, Notifications, and Change-Driven Side Effects**?
**Answer:** Use change-driven handlers instead of unconditional restarts.

### Q18. What is the most important operational lesson from **Reload vs Restart Decision**?
**Answer:** Encode restart semantics in the reusable component interface.

### Q19. What is the most important operational lesson from **Package State and Version Governance**?
**Answer:** Use explicit version policy for production-critical software.

### Q20. What is the most important operational lesson from **Repository Trust and Software Supply Chain**?
**Answer:** Pin and review privileged automation dependencies.

### Q21. What is the most important operational lesson from **User Lifecycle as Desired State**?
**Answer:** Design offboarding and privilege removal before onboarding automation.

### Q22. What is the most important operational lesson from **SSH Key Management and Private-Key Boundaries**?
**Answer:** Prefer per-service or federated identities over one fleet-wide private key.

### Q23. What is the most important operational lesson from **Sudo / Privilege Policy as Code**?
**Answer:** Always validate sudoers before replacing live policy.

### Q24. What is the most important operational lesson from **Firewall State as a Dependency-Aware Resource**?
**Answer:** Sequence remote-firewall changes so a verified management path always remains.

### Q25. What is the most important operational lesson from **Sysctl Runtime vs Persistent State**?
**Answer:** Manage runtime and persistence together and eliminate duplicate conflicting definitions.

### Q26. What is the most important operational lesson from **Mounts as Multi-Layer State**?
**Answer:** Verify the mounted filesystem itself, not only the configuration file.

### Q27. What is the most important operational lesson from **Scheduled Tasks Without Duplication**?
**Answer:** Manage scheduled tasks as named resources, not text append operations.

### Q28. What is the most important operational lesson from **Application Configuration Ownership Boundary**?
**Answer:** Document one owner per configuration resource.

### Q29. What is the most important operational lesson from **Dependency Graphs and Topological Ordering**?
**Answer:** Model dependencies explicitly instead of relying on accidental task order.

### Q30. What is the most important operational lesson from **Readiness vs Mere Process State**?
**Answer:** Use application-level readiness to decide whether the next rollout wave may proceed.

### Q31. What is the most important operational lesson from **Canary Rollout as Risk Measurement**?
**Answer:** Define numeric/observable canary success criteria before the change starts.

### Q32. What is the most important operational lesson from **Serial Rollout and Batch Sizing**?
**Answer:** Calculate batch size from minimum surviving service capacity.

### Q33. What is the most important operational lesson from **Quorum-Aware Changes**?
**Answer:** Encode quorum math into change prerequisites.

### Q34. What is the most important operational lesson from **Load Balancer Drain and Connection Grace**?
**Answer:** Define both graceful-drain criteria and a maximum wait time.

### Q35. What is the most important operational lesson from **Maintenance Windows and Change Deadlines**?
**Answer:** Put a time-based decision point in every high-risk production change.

### Q36. What is the most important operational lesson from **Dry Run and Check-Mode Limitations**?
**Answer:** Use dry-run together with real tests on disposable/staging targets.

### Q37. What is the most important operational lesson from **Diff Mode and Secret Leakage**?
**Answer:** Classify configuration data before enabling verbose diff logging.

### Q38. What is the most important operational lesson from **Static Validation vs Runtime Validation**?
**Answer:** Use the strongest validator available at each stage.

### Q39. What is the most important operational lesson from **Configuration Testing Pyramid**?
**Answer:** Move each discovered failure into a repeatable earlier test where possible.

### Q40. What is the most important operational lesson from **Idempotency Testing in Disposable Systems**?
**Answer:** Make idempotency a regression test for reusable components.

### Q41. What is the most important operational lesson from **Rollback vs Forward Fix**?
**Answer:** Never label a procedure 'rollback' until compatibility has been proven.

### Q42. What is the most important operational lesson from **Partial Failure and Fleet Inconsistency**?
**Answer:** Design the partial-failure decision tree before large fleet changes.

### Q43. What is the most important operational lesson from **Compensating Actions and Saga-Like Recovery**?
**Answer:** Document compensation for every irreversible boundary in an orchestrated change.

### Q44. What is the most important operational lesson from **Retries, Backoff, and Error Classification**?
**Answer:** Retry by error semantics, not because 'something failed'.

### Q45. What is the most important operational lesson from **Timeouts and Hung Targets**?
**Answer:** Set timeouts based on expected operation duration plus realistic margin.

### Q46. What is the most important operational lesson from **Unreachable vs Failed Targets**?
**Answer:** Branch troubleshooting at the first failed layer.

### Q47. What is the most important operational lesson from **Concurrency, Forks, and Backend Pressure**?
**Answer:** Load-test automation fan-out before using maximum concurrency in production.

### Q48. What is the most important operational lesson from **Distributed Locks and Change Collisions**?
**Answer:** Prevent concurrent writers for resources that cannot tolerate overlap.

### Q49. What is the most important operational lesson from **Dynamic Inventory Cache and Freshness**?
**Answer:** Refresh and preview dynamic inventory before destructive or security-sensitive changes.

### Q50. What is the most important operational lesson from **CMDB Accuracy and Reconciliation**?
**Answer:** Assign ownership and freshness SLOs to CMDB data domains.

### Q51. What is the most important operational lesson from **Compliance as Code and Evidence**?
**Answer:** Store the rule, rationale, remediation, and exception process together.

### Q52. What is the most important operational lesson from **Policy as Code Before Change**?
**Answer:** Use policy as code for high-impact invariants, not for every subjective style preference.

### Q53. What is the most important operational lesson from **Secrets Separation and Runtime Retrieval**?
**Answer:** Separate code review permissions from secret-read permissions.

### Q54. What is the most important operational lesson from **Secret Rotation with Overlap**?
**Answer:** Design secret rotation as an orchestrated multi-party change.

### Q55. What is the most important operational lesson from **Certificate Lifecycle Automation**?
**Answer:** Monitor actual served certificate expiry, not only files on disk.

### Q56. What is the most important operational lesson from **Control Node Security and Blast Radius**?
**Answer:** Minimize credential scope and prefer short-lived/ephemeral automation identities.

### Q57. What is the most important operational lesson from **Least Privilege for Automation**?
**Answer:** Grant privilege to the automation use case, not to the tool as a whole.

### Q58. What is the most important operational lesson from **Observability for Configuration Automation**?
**Answer:** Make run IDs and Git commit IDs first-class audit fields.

### Q59. What is the most important operational lesson from **Automation SLOs and Reliability Metrics**?
**Answer:** Measure configuration coverage and verification outcomes, not only pipeline success.

### Q60. What is the most important operational lesson from **Rebuildability as a Disaster-Recovery Test**?
**Answer:** Perform periodic rebuild tests to expose undocumented state before a disaster.


## Completion Checklist

- [ ] I understand desired/actual state.
- [ ] I understand drift/reconciliation/convergence.
- [ ] I understand idempotency.
- [ ] I understand imperative/declarative.
- [ ] I understand push/pull and agent/agentless.
- [ ] I understand mutable/immutable.
- [ ] I understand inventory/source of truth.
- [ ] I understand variables/templates.
- [ ] I understand secrets.
- [ ] I understand handlers and ordering.
- [ ] I understand canary/serial rollout/blast radius.
- [ ] I understand validation/testing.
- [ ] I understand rollback/partial failure.
- [ ] I understand compliance/policy as code.
- [ ] I understand automation security.
- [ ] I understand rebuildability/DR.
- [ ] I completed all 25 labs.
- [ ] I completed the Configuration Management Operating Model project.
