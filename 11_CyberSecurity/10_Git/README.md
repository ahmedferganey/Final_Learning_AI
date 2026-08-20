# Phase 10 — Git & Configuration Automation

This phase changes your operating model from:

```text
Engineer
   ↓
SSH
   ↓
Manual Command
   ↓
Server Changes
```

to:

```text
Requirement
   ↓
Git
   ↓
Reviewed Desired State
   ↓
Configuration Management
   ↓
Ansible
   ↓
Repeatable Infrastructure
```

The exact study order is:

```text
45. Git and Version Control Systems
        ↓
46. Configuration Management
        ↓
47. Ansible
```

Dependency from the earlier phases:

```text
Linux + Bash
     ↓
Git
     ↓
Configuration Management Concepts
     ↓
Ansible
```

The reason for this order is important.

If you study Ansible without understanding Linux administration, you may know how to write:

```yaml
ansible.builtin.service:
  name: nginx
  state: started
```

but not understand:

```text
systemd
service dependencies
logs
permissions
ports
configuration syntax
failure modes
```

If you study Ansible without configuration-management concepts, you may write large collections of remote shell commands but miss:

```text
desired state
idempotency
drift
convergence
source of truth
safe rollout
verification
```

If you study automation without Git, you lose:

```text
history
review
rollback
audit
release control
collaboration
```

Therefore Phase 10 deliberately builds the reasoning before the tool.

---

# Phase Goal

By the end of this phase you should be able to transform a manual change such as:

```bash
sudo apt install nginx

sudo cp nginx.conf /etc/nginx/nginx.conf

sudo nginx -t

sudo systemctl restart nginx
```

into a controlled process:

```text
Business Change
      ↓
Git Feature Branch
      ↓
Desired State
      ↓
Peer Review
      ↓
CI Validation
      ↓
Ansible Role
      ↓
Development
      ↓
Staging
      ↓
Production Canary
      ↓
Rolling Deployment
      ↓
Health Check
      ↓
Audit / Monitoring
```

A mature infrastructure repository should become:

```text
Git
├── inventory
├── variables
├── templates
├── roles
├── playbooks
├── tests
├── documentation
└── runbooks
```

with secrets stored through an appropriate protected mechanism rather than normal plaintext Git history.

---

# 45. Git and Version Control Systems

**File:** `45_Git_and_Version_Control_Systems.md`

Git provides the history and collaboration model required before serious infrastructure automation.

The first mental model is:

```text
Working Tree
      |
      | git add
      v
Staging Area / Index
      |
      | git commit
      v
Local Repository
      |
      | git push
      v
Remote Repository
```

The deeper object model is:

```text
File Content
   ↓
Blob

Directory
   ↓
Tree

Snapshot + Parent + Metadata
   ↓
Commit

Movable Human Name
   ↓
Branch

Current Checkout
   ↓
HEAD
```

Major topics include:

```text
Version Control
Distributed VCS
Repositories
Working Tree
Index / Staging Area
Commits
Blobs
Trees
Object IDs
References
HEAD

git init
git status
git add
git add -p
git diff
git commit
git log
git show

Branches
git switch
Detached HEAD
Merges
Fast-Forward
Three-Way Merge
Conflicts
Rebase
Interactive Rebase
Amend

Remotes
origin
Remote-Tracking Branches
fetch
pull
push
upstreams
non-fast-forward
force-with-lease

.gitignore
.gitattributes
line endings
permissions
binary files

stash
restore
reset
revert
reflog

tags
signed tags
blame
bisect
worktree
submodules
hooks

SSH / HTTPS Git authentication
credential helpers

branching strategies
trunk-based development
release branches
cherry-pick
squash merge

Git for Infrastructure as Code
GitOps concepts
secret handling
code review
audit
recovery
```

Useful commands:

```bash
git status

git diff
git diff --staged

git log --oneline --graph --decorate --all

git switch -c feature/change

git fetch origin

git reflog

git bisect

git worktree list
```

### Course Project

**Version-Controlled Infrastructure Repository**

The project becomes the repository used for the rest of Phase 10.

---

# 46. Configuration Management

**File:** `46_Configuration_Management.md`

This is intentionally tool-neutral before Ansible.

The key loop is:

```text
Desired State
      |
      v
Compare
      |
      v
Actual State
      |
      +-- matches → no change
      |
      +-- differs
             ↓
          correct
             ↓
          verify
```

Important vocabulary:

```text
Desired State
Actual State
Drift
Convergence
Reconciliation
Idempotency
```

Main topics:

```text
Why Configuration Management Exists

Imperative vs Declarative
Idempotency
Convergence
Reconciliation

Configuration Management
vs
Provisioning
Orchestration
Deployment
Infrastructure as Code

Push vs Pull
Agent vs Agentless

Mutable vs Immutable Infrastructure

Day 0
Day 1
Day 2 Operations

Source of Truth
Inventory
Dynamic Inventory
CMDB
IPAM

Variables
Hierarchy
Defaults
Templates

Files
Packages
Users
Groups
Services
Handlers
Firewalls
Sysctl
Mounts
Scheduled Tasks

Dependency Graphs
Ordering
Serial Rollout
Canary
Blast Radius
Maintenance Windows

Environment Separation
Promotion

Validation
Dry Run
Diff
Testing
Idempotency Testing
Health Verification

Rollback
Forward Fix
Partial Failure
Compensating Actions
Retries
Timeouts

Linux
Windows
Network Devices
Cloud
Containers
Kubernetes

Configuration Baselines
Golden Configuration
Drift Detection
Compliance as Code
Policy as Code

Secrets
Secret Rotation
Certificates

Observability
Change Correlation
Git Integration
Separation of Duties
Least Privilege

Rebuildability
Backup / DR
Automation Maturity
Configuration Ownership
Troubleshooting
```

A configuration should describe:

```text
WHAT should exist
```

rather than only:

```text
WHICH command should run
```

Example:

```text
Desired:
nginx package present
service enabled
service running
configuration validated
port 443 permitted
```

rather than simply:

```bash
apt install nginx
systemctl start nginx
```

### Course Project

**Configuration Management Operating Model**

This project creates the operational design that Course 47 implements.

---

# 47. Ansible

**File:** `47_Ansible.md`

Ansible maps configuration-management concepts into practical automation.

Architecture:

```text
                 Ansible Control Node
                         |
                Inventory / Playbooks
                         |
          +--------------+--------------+
          |              |              |
         SSH          WinRM/PSRP      API/SSH
          |              |              |
        Linux          Windows         Network/
        Hosts           Hosts           Cloud
```

Ansible works best when the automation looks like state:

```yaml
- name: Configure web servers
  hosts: webservers
  become: true

  tasks:
    - name: Ensure NGINX is installed
      ansible.builtin.package:
        name: nginx
        state: present

    - name: Ensure NGINX is running
      ansible.builtin.service:
        name: nginx
        enabled: true
        state: started
```

Desired idempotency:

```text
First run:
changed

Second run:
ok
changed=0
```

Main topics:

```text
Control Nodes
Managed Nodes
Agentless Model

Ansible Community Package
ansible-core
Collections
FQCN

Installation
ansible --version
ansible.cfg

Inventory
INI Inventory
YAML Inventory
Groups
Children
group_vars
host_vars
Patterns
--limit
--list-hosts

Dynamic Inventory
Inventory Plugins
Inventory Caching

SSH
Host-Key Checking
Connection Variables

Ad Hoc Commands

Modules:
ping
command
shell
raw
package
apt
dnf
service
systemd_service
file
copy
template
lineinfile
blockinfile
user
group
get_url
unarchive
uri
mount
sysctl
firewall collections

Playbooks
Plays
Tasks
YAML
become

Check Mode
Diff Mode

Handlers
notify
flush_handlers

Variables
Role Defaults
Facts
Local Facts
Fact Caching
register
set_fact
changed_when
failed_when

Conditions
Loops
Jinja2
Filters
Lookups
Queries
Magic Variables

Tags

Blocks
rescue
always

Retries
until
async
poll

serial
delegation
run_once
strategies
forks

Roles
Role Structure
Role Defaults
Role Handlers
Role Templates
Role Metadata

import_tasks
include_tasks
import_role
include_role

Collections
ansible-galaxy
requirements.yml

Ansible Vault
no_log
External Secret Managers

Separate Environments

Linux Automation
Windows Automation
Network Automation
Cloud Automation
REST APIs

Ansible vs Terraform

CI
ansible-lint
Molecule Concept
Execution Environments
Automation Platform Concepts

Security
Supply Chain
Troubleshooting
```

Core commands:

```bash
ansible --version

ansible-inventory --graph

ansible all \
  -m ansible.builtin.ping

ansible-playbook \
  playbooks/site.yml

ansible-playbook \
  playbooks/site.yml \
  --check \
  --diff

ansible-playbook \
  playbooks/site.yml \
  --limit web01

ansible-galaxy collection install \
  -r requirements.yml

ansible-vault create \
  group_vars/prod/vault.yml
```

### Course Project

**Enterprise Ansible Configuration Platform**

---

# Recommended Study Sequence

Do not jump directly into playbooks.

## Step 1 — Git

Study Course 45 until you can answer:

```text
What is the index?
What is a commit?
What is a branch?
What is HEAD?
fetch vs pull?
merge vs rebase?
reset vs revert?
How does reflog recover work?
Why should secrets never enter Git?
```

You should be able to recover from common Git mistakes before using Git for production infrastructure.

## Step 2 — Configuration Management

Study Course 46 until you can explain:

```text
desired state
actual state
drift
idempotency
convergence
reconciliation
source of truth
inventory
template
canary
blast radius
rollback
```

without mentioning Ansible.

## Step 3 — Ansible

Now map concepts:

```text
Configuration Concept      Ansible Feature
--------------------------------------------------
Inventory                  inventory
Desired State              modules/tasks
Reusable Component         role
Parameter                  variable
Template                   Jinja2 template
Change Trigger             handler
Secret                     Vault / lookup
Canary                     --limit
Rolling Deployment         serial
Orchestration              delegation / run_once
Validation                 assert / uri / commands
Drift Correction           repeated playbook run
```

This mapping is more important than memorizing module names.

---

# Integrated Phase Architecture

```text
                         Engineer
                            |
                         Git Repo
                            |
             +--------------+--------------+
             |                             |
         Desired State                  Review
             |                             |
             +--------------+--------------+
                            |
                        CI Validation
                            |
                      Ansible Control
                            |
       +--------------------+--------------------+
       |                    |                    |
    Linux                Windows              Network
       |                    |                    |
      App                 IIS/AD             Switches/
     Servers                                  Routers
```

External systems can supply data:

```text
CMDB
  |
IPAM
  |
Secret Manager
  |
Dynamic Inventory
  |
Ansible
```

The critical rule is:

```text
one authoritative owner
for each configuration domain
```

---

# Phase 10 Integrated Capstone

Build an enterprise infrastructure automation repository.

Target:

```text
10 Linux web/app servers
3 Linux database servers
2 monitoring servers
2 Windows servers
4 network devices
dev / staging / production
```

Repository:

```text
infrastructure/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CHANGE_POLICY.md
│   ├── SOURCE_OF_TRUTH.md
│   └── RUNBOOKS/
├── ansible/
│   ├── ansible.cfg
│   ├── requirements.yml
│   ├── inventories/
│   │   ├── dev/
│   │   ├── staging/
│   │   └── prod/
│   ├── group_vars/
│   ├── host_vars/
│   ├── playbooks/
│   ├── roles/
│   └── tests/
├── scripts/
│   └── validate.sh
├── .gitignore
└── .gitattributes
```

Required change workflow:

```text
Requirement
   ↓
Git Feature Branch
   ↓
Ansible Change
   ↓
Syntax / Lint / Secret Scan
   ↓
Code Review
   ↓
Development
   ↓
Staging
   ↓
Production --limit Canary
   ↓
serial Rolling Deployment
   ↓
Health Verification
   ↓
Full Fleet
   ↓
Audit
```

Required security rules:

```text
No plaintext passwords
No private SSH keys
No API tokens in Git
No disabled TLS verification for production APIs
No universal shared root credential
No uncontrolled ANY-host production runs
```

Required recovery scenarios:

```text
Git bad commit
Git bad merge
Git bad reset
server unreachable
sudo failure
template failure
service failure
partial rollout
Vault/secret failure
rollback/forward fix
```

---

# Troubleshooting Framework

For Ansible, trace:

```text
Git / Code
    ↓
Inventory
    ↓
Variables
    ↓
Control Node
    ↓
Connection
    ↓
Authentication
    ↓
Privilege Escalation
    ↓
Module
    ↓
Target OS
    ↓
Application
    ↓
Health Verification
```

Examples:

```text
UNREACHABLE
→ transport/authentication/inventory

FAILED
→ module/target/application

unexpected CHANGED
→ idempotency/desired-state issue

SKIPPED
→ condition/tag/targeting issue
```

Do not debug an application configuration failure by immediately changing SSH settings.

---

# Phase 10 Completion Checklist

## Git

- [ ] I understand Git's object model.
- [ ] I understand working tree/index/repository.
- [ ] I understand branches/HEAD.
- [ ] I can merge and rebase.
- [ ] I can resolve conflicts.
- [ ] I understand remotes/fetch/pull/push.
- [ ] I understand reset/restore/revert.
- [ ] I can recover using reflog.
- [ ] I understand tags/bisect/worktree/submodules.
- [ ] I understand secure Git practices.
- [ ] I can build an infrastructure Git workflow.

## Configuration Management

- [ ] I understand desired/actual state.
- [ ] I understand drift/convergence.
- [ ] I understand idempotency.
- [ ] I understand imperative/declarative.
- [ ] I understand push/pull and agentless models.
- [ ] I understand inventory and source of truth.
- [ ] I understand variables/templates.
- [ ] I understand safe rollout/blast radius.
- [ ] I understand verification and rollback.
- [ ] I understand secrets/compliance.
- [ ] I understand configuration ownership.

## Ansible

- [ ] I understand control/managed nodes.
- [ ] I understand ansible-core/package/Collections.
- [ ] I can create inventory.
- [ ] I can use ad hoc commands.
- [ ] I can write idempotent playbooks.
- [ ] I can use common modules.
- [ ] I understand facts/variables/register.
- [ ] I understand Jinja/loops/conditions.
- [ ] I understand handlers.
- [ ] I understand check/diff.
- [ ] I understand blocks/retries.
- [ ] I understand serial/delegation.
- [ ] I can create roles.
- [ ] I can manage Collections.
- [ ] I can use Vault securely.
- [ ] I understand environment separation.
- [ ] I understand CI/testing.
- [ ] I understand Ansible security.
- [ ] I can troubleshoot major failures.

---

# Folder Structure

```text
Phase_10_Git_Configuration_Automation/
│
├── README.md
├── 45_Git_and_Version_Control_Systems.md
├── 46_Configuration_Management.md
└── 47_Ansible.md
```

---

# Next Phase

After Phase 10:

```text
Phase 11 — Cloud Fundamentals

48. Cloud Computing Fundamentals
49. AWS Cloud Practitioner
50. Microsoft Azure Fundamentals
51. Google Cloud Platform Fundamentals
```

Dependency:

```text
Infrastructure Administration
        ↓
Version Control
        ↓
Configuration Automation
        ↓
Cloud Platforms
```

At that point, cloud resources will not feel like isolated web-console objects. You will already understand how infrastructure should be versioned, configured, secured, tested, and automated.
