# 23. Red Hat System Administration III

> Phase 5 — Linux System Administration

In this curriculum, **Red Hat System Administration III** is the Linux automation stage.

The historical Red Hat naming "System Administration III: Linux Automation" maps to the modern **Red Hat Enterprise Linux Automation with Ansible** training path (AU294/RH294 naming appears across Red Hat materials).

The current Red Hat automation course is based on:

- **Red Hat Enterprise Linux 10**
- **Ansible Core 2.16**
- development tooling aligned with **Red Hat Ansible Automation Platform 2.5 and 2.6**

The goal is to stop administering servers one command at a time and begin expressing desired state as repeatable automation.
## 1. Topic Title

**Red Hat System Administration III — Linux Automation with Ansible**

## 2. Learning Objectives

- Explain Ansible control-node, managed-node, inventory, module, play, task, role, collection, and idempotency concepts.
- Configure inventories, SSH connectivity, privilege escalation, and Ansible configuration.
- Write valid YAML playbooks using fully qualified collection names where appropriate.
- Use modules to manage packages, users, files, services, networking-related configuration, and other Linux state.
- Use variables, facts, host/group variables, registered results, and magic variables.
- Protect sensitive variables with Ansible Vault.
- Control task execution with loops, conditions, handlers, blocks, tags, and error handling.
- Deploy static and templated files with `copy`, `template`, `file`, and related modules.
- Scale automation with imports, includes, host patterns, roles, and collections.
- Troubleshoot inventory, SSH, privilege escalation, YAML, module, idempotency, and host failures.
- Automate common RHEL administration workflows across multiple hosts safely.

## 3. Prerequisites

Required:

- 20. Linux Essentials
- 21. Red Hat System Administration I
- 22. Red Hat System Administration II
- RHCSA-level equivalent practical ability
- SSH key authentication
- Bash/YAML familiarity helps

Recommended lab:

```text
Control node:
ansible-control.lab.example

Managed nodes:
node1.lab.example
node2.lab.example
node3.lab.example

Private network
SSH name resolution
non-root automation user
sudo policy for approved administration
```

Use disposable VMs and a dedicated lab account.
## 4. Core Concepts Explanation

# Part 1 — Introduction to Ansible

Ansible is an agentless automation system.

Typical architecture:

```text
Control Node
    |
    | SSH
    +------------------+
    |                  |
    v                  v
Managed Node 1     Managed Node 2
    |                  |
 Python/modules      Python/modules
```

Core concepts:

**Control node**
Machine from which automation runs.

**Managed node**
Target host.

**Inventory**
Defines managed hosts and groups.

**Module**
An automation unit that performs a specific operation.

**Task**
One module invocation with parameters.

**Play**
Maps tasks to selected hosts.

**Playbook**
YAML file containing one or more plays.

**Role**
Reusable automation structure.

**Collection**
Packaged namespace containing modules, roles, plugins, and other content.
### Why Ansible Instead of Shell Loops?

```bash
for host in node1 node2 node3; do
    ssh "$host" 'sudo dnf install -y httpd'
done
```
The shell loop can work, but it has weak state modeling and error/reporting.

Ansible:
```yaml
---
- name: Install Apache on web servers
  hosts: web
  become: true

  tasks:
    - name: Ensure Apache is installed
      ansible.builtin.dnf:
        name: httpd
        state: present
```
The playbook expresses desired state:

```text
httpd should be present
```

If it is already installed, a well-behaved module should report no change. This is **idempotency**.
# Part 2 — Installing and Configuring Ansible Development Tools

Current Red Hat automation training includes development tooling and VS Code integration.

At a conceptual level, you need:

- supported Ansible/Automation Platform environment,
- editor with YAML/Ansible support,
- SSH client,
- inventory,
- configuration file,
- linting/validation tools where available.
### Verify Tools

```bash
ansible --version
ansible-playbook --version

command -v ansible-navigator || true
command -v ansible-lint || true
```
Exact installation method depends on your Red Hat training environment, subscription, and Ansible Automation Platform version.

Do not mix arbitrary pip-installed Ansible packages into a managed enterprise automation environment without understanding dependency/support implications.
# Part 3 — Inventories and Managed-host Connections

### INI Inventory

```ini
[web]
node1.lab.example
node2.lab.example

[db]
node3.lab.example

[production:children]
web
db
```
### YAML Inventory

```yaml
all:
  children:
    web:
      hosts:
        node1.lab.example:
        node2.lab.example:
    db:
      hosts:
        node3.lab.example:
```
### Verify Inventory

```bash
ansible-inventory -i inventory.ini --graph
ansible-inventory -i inventory.ini --list
```
### Ansible Configuration

```ini
# ansible.cfg
[defaults]
inventory = ./inventory.ini
remote_user = automation
host_key_checking = True
forks = 10

[privilege_escalation]
become = True
become_method = sudo
```
Do not disable SSH host-key checking simply to remove errors. Host keys are part of server identity verification.

Fix DNS/known-hosts/key provisioning properly.
### Connectivity Test

```bash
ansible all -m ansible.builtin.ping

ansible all -m ansible.builtin.command -a 'hostname'
```
`ansible.builtin.ping` is not ICMP ping. It validates Ansible's ability to connect and execute a small module payload.
# Part 4 — Developing Automation Content

### First Playbook

```yaml
---
- name: Configure web hosts
  hosts: web
  become: true

  tasks:
    - name: Ensure Apache package is installed
      ansible.builtin.dnf:
        name: httpd
        state: present

    - name: Ensure Apache is enabled and running
      ansible.builtin.service:
        name: httpd
        state: started
        enabled: true
```
```bash
ansible-playbook site.yml --syntax-check
ansible-playbook site.yml --check
ansible-playbook site.yml
```
`--check` provides dry-run-style prediction where modules support check mode. It is valuable but not perfect; some operations cannot fully predict changes.
### Idempotency Test

Run the same playbook twice.

Expected:

```text
First run:
changed > 0

Second run:
changed = 0
```

If the second run always changes the same task, investigate whether:
- module is non-idempotent,
- template output changes every run,
- command/shell is used unnecessarily,
- state is not expressed correctly.
# Part 5 — Core Linux Administration Modules

### Packages

```yaml
- name: Ensure required packages are installed
  ansible.builtin.dnf:
    name:
      - httpd
      - chrony
      - rsync
    state: present
```
### Users

```yaml
- name: Ensure operations group exists
  ansible.builtin.group:
    name: operations
    state: present

- name: Ensure operations user exists
  ansible.builtin.user:
    name: appops
    groups: operations
    append: true
    shell: /bin/bash
    state: present
```
### Files and Directories

```yaml
- name: Ensure application directory exists
  ansible.builtin.file:
    path: /srv/app
    state: directory
    owner: root
    group: operations
    mode: '2770'
```
### Services

```yaml
- name: Ensure chronyd is running
  ansible.builtin.service:
    name: chronyd
    state: started
    enabled: true
```
### Why Prefer Modules to command/shell

Bad default:
```yaml
- name: Install Apache
  ansible.builtin.shell: dnf install -y httpd
```
Better:
```yaml
- name: Ensure Apache is installed
  ansible.builtin.dnf:
    name: httpd
    state: present
```
The module understands package state and can report changed/unchanged meaningfully.
# Part 6 — Variables, Facts, and Magic Variables

### Play Variables

```yaml
---
- name: Configure service
  hosts: web
  become: true

  vars:
    web_package: httpd
    web_service: httpd

  tasks:
    - name: Install web package
      ansible.builtin.dnf:
        name: "{{ web_package }}"
        state: present
```
### group_vars and host_vars

```text
project/
├── ansible.cfg
├── inventory.ini
├── group_vars/
│   └── web.yml
├── host_vars/
│   └── node1.lab.example.yml
└── site.yml
```
```yaml
# group_vars/web.yml
web_port: 8080
document_root: /srv/web
```
### Facts

```bash
ansible node1.lab.example -m ansible.builtin.setup
```
```yaml
- name: Show default IPv4
  ansible.builtin.debug:
    var: ansible_default_ipv4
```
Facts describe managed-host state.

Examples:
- distribution,
- interfaces,
- memory,
- CPU,
- addresses,
- mounts.

Do not assume every fact exists in every environment.
### Registered Results

```yaml
- name: Query service
  ansible.builtin.command: systemctl is-active httpd
  register: httpd_state
  changed_when: false
  failed_when: false

- name: Show result
  ansible.builtin.debug:
    var: httpd_state.stdout
```
### Magic Variables

```yaml
- name: Show current inventory host
  ansible.builtin.debug:
    msg: "Managing {{ inventory_hostname }}"
```
Other important concepts include:
- `groups`
- `hostvars`
- `inventory_hostname`
- `ansible_play_hosts`

Use them carefully; excessive cross-host variable coupling can make automation hard to understand.
# Part 7 — Ansible Vault

```bash
ansible-vault create group_vars/production/vault.yml
ansible-vault edit group_vars/production/vault.yml
ansible-vault view group_vars/production/vault.yml
```
Vault encrypts sensitive Ansible variable files or values.

Do not commit:

```text
plaintext passwords
API tokens
private SSH keys
vault password files
```

Use approved secret-management workflow.
### Variable Separation Pattern

```yaml
# group_vars/production/vars.yml
db_user: appuser
db_password: "{{ vault_db_password }}"
```
```yaml
# encrypted vault.yml conceptually contains:
vault_db_password: very-secret-value
```
# Part 8 — Task Control

### Loops

```yaml
- name: Install common tools
  ansible.builtin.dnf:
    name: "{{ item }}"
    state: present
  loop:
    - curl
    - rsync
    - vim
```
Better package-list form when supported by the module:

```yaml
- name: Install common tools in one transaction
  ansible.builtin.dnf:
    name:
      - curl
      - rsync
      - vim
    state: present
```
### Conditions

```yaml
- name: Install package only on Red Hat family
  ansible.builtin.dnf:
    name: httpd
    state: present
  when: ansible_facts['os_family'] == 'RedHat'
```
### Handlers

```yaml
tasks:
  - name: Deploy Apache configuration
    ansible.builtin.template:
      src: httpd.conf.j2
      dest: /etc/httpd/conf/httpd.conf
      owner: root
      group: root
      mode: '0644'
    notify: Restart Apache

handlers:
  - name: Restart Apache
    ansible.builtin.service:
      name: httpd
      state: restarted
```
Handlers run only when notified by a task that reports a change, normally at the end of the relevant play section.

This avoids unnecessary service restarts.
### Blocks and Rescue

```yaml
- name: Deploy application safely
  block:
    - name: Copy configuration
      ansible.builtin.copy:
        src: app.conf
        dest: /etc/app.conf

    - name: Validate application
      ansible.builtin.command: /usr/local/bin/app --check-config
      changed_when: false

  rescue:
    - name: Report failure
      ansible.builtin.debug:
        msg: "Deployment validation failed"
```
### Tags

```yaml
- name: Install package
  ansible.builtin.dnf:
    name: httpd
    state: present
  tags:
    - packages
    - web
```
```bash
ansible-playbook site.yml --tags web
ansible-playbook site.yml --skip-tags packages
```
# Part 9 — Deploying Files

### copy

```yaml
- name: Deploy static MOTD
  ansible.builtin.copy:
    src: motd
    dest: /etc/motd
    owner: root
    group: root
    mode: '0644'
```
### Jinja2 Template

```jinja2
# templates/app.conf.j2
server_name={{ inventory_hostname }}
listen_port={{ app_port }}
environment={{ deployment_environment }}
```
```yaml
- name: Deploy application template
  ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app.conf
    owner: root
    group: root
    mode: '0640'
```
### lineinfile — Use Carefully

```yaml
- name: Ensure one configuration line exists
  ansible.builtin.lineinfile:
    path: /etc/example.conf
    regexp: '^MaxClients='
    line: 'MaxClients=200'
```
For complex configuration files, a complete managed template can be easier to reason about than many unrelated `lineinfile` mutations.
# Part 10 — Developing Automation Content at Scale

### Host Patterns

```bash
ansible 'web' --list-hosts
ansible 'web:&production' --list-hosts
ansible 'all:!db' --list-hosts
```
### Import Playbooks

```yaml
---
- import_playbook: baseline.yml
- import_playbook: web.yml
- import_playbook: monitoring.yml
```
### Include Tasks

```yaml
- name: Include web tasks
  ansible.builtin.include_tasks: web_tasks.yml
  when: web_enabled | bool
```
General mental distinction:

- imports are more static/preprocessed,
- includes are more dynamic/runtime-oriented.

Use the simplest structure that remains readable.
# Part 11 — Reusing Code with Roles and Collections

### Role Structure

```text
roles/
└── webserver/
    ├── defaults/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml
    ├── tasks/
    │   └── main.yml
    ├── templates/
    │   └── index.html.j2
    ├── files/
    └── vars/
        └── main.yml
```
### Use a Role

```yaml
---
- name: Configure web tier
  hosts: web
  become: true

  roles:
    - role: webserver
```
### Collections

Collections package:

- modules,
- plugins,
- roles,
- documentation.

FQCN example:

```text
ansible.builtin.dnf
ansible.builtin.service
ansible.builtin.template
```

A third-party/vendor collection might use another namespace.

Install only trusted/approved collections in enterprise automation.
```bash
ansible-galaxy collection list
ansible-galaxy role list
```
# Part 12 — Troubleshooting Automation

### Syntax and YAML

```bash
ansible-playbook site.yml --syntax-check
```
Typical failures:

- tabs/indentation,
- missing colon,
- wrong YAML type,
- misspelled module argument,
- undefined variable.
### Inventory/Connection

```bash
ansible-inventory --graph
ansible all -m ansible.builtin.ping -vv
ssh automation@node1.lab.example
sudo -l
```
Separate:

```text
DNS/route
SSH
host key
user authentication
sudo/become
Python/module execution
playbook logic
```
### Verbosity

```bash
ansible-playbook site.yml -v
ansible-playbook site.yml -vv
ansible-playbook site.yml -vvv
```
Increase verbosity only as needed because logs can expose sensitive data.

Use `no_log: true` for tasks that handle secrets where appropriate.
### Debug Module

```yaml
- name: Inspect variable during troubleshooting
  ansible.builtin.debug:
    var: app_port
```
### Idempotency Failure Example

```yaml
# Bad: changes timestamp every run
- name: Write generated timestamp
  ansible.builtin.copy:
    content: "generated={{ ansible_date_time.iso8601 }}
"
    dest: /etc/generated.conf
```
If the timestamp is not actually required, remove it. Otherwise, accept/document that this task intentionally changes every run.
# Part 13 — Automating Common RHEL Administration Tasks

### Baseline Playbook

```yaml
---
- name: Apply RHEL baseline
  hosts: all
  become: true

  vars:
    baseline_packages:
      - chrony
      - rsync
      - vim

  tasks:
    - name: Ensure baseline packages are installed
      ansible.builtin.dnf:
        name: "{{ baseline_packages }}"
        state: present

    - name: Ensure chronyd is enabled and running
      ansible.builtin.service:
        name: chronyd
        state: started
        enabled: true

    - name: Ensure operations group exists
      ansible.builtin.group:
        name: operations
        state: present

    - name: Deploy managed MOTD
      ansible.builtin.template:
        src: motd.j2
        dest: /etc/motd
        owner: root
        group: root
        mode: '0644'
```
### User Deployment

```yaml
- name: Ensure automation admin exists
  ansible.builtin.user:
    name: opsadmin
    groups: wheel
    append: true
    state: present

- name: Install authorized SSH key
  ansible.posix.authorized_key:
    user: opsadmin
    state: present
    key: "{{ lookup('file', 'files/opsadmin.pub') }}"
```
`ansible.posix.authorized_key` belongs to the `ansible.posix` collection, so collection availability must be managed explicitly.
### Firewall Automation Example

```yaml
- name: Ensure firewalld is running
  ansible.builtin.service:
    name: firewalld
    state: started
    enabled: true

# Requires a collection/module available in the environment.
- name: Allow HTTPS
  ansible.posix.firewalld:
    service: https
    permanent: true
    immediate: true
    state: enabled
```
Automation does not remove the need to understand firewalld. It multiplies the speed and scale of your configuration, including mistakes.
# Part 14 — Safe Automation Workflow

```text
Edit
 ↓
YAML/editor validation
 ↓
ansible-playbook --syntax-check
 ↓
inventory verification
 ↓
--check on limited hosts
 ↓
run on one canary host
 ↓
verify service/state
 ↓
expand batch
 ↓
monitor
 ↓
commit version-controlled change
```
### Limit Scope

```bash
ansible-playbook site.yml --limit node1.lab.example
ansible-playbook site.yml --limit web
```
### Check and Diff

```bash
ansible-playbook site.yml --check --diff --limit node1.lab.example
```
`--diff` may expose sensitive file content. Use it carefully.

# Enhanced Deep-Study Layer — Ansible Automation Engineering

The uploaded RHSA III / Ansible course is preserved. This layer expands it into a deeper automation-engineering module focused on correctness, idempotency, variable design, reusable roles, secure secrets, validation, testing, controlled rollout, troubleshooting, and enterprise automation architecture.

The central model is:

```text
Git / human intent
       ↓
Inventory + variables
       ↓
Playbooks / roles / collections
       ↓
Module arguments
       ↓
SSH / connection
       ↓
Privilege escalation if required
       ↓
Managed-host resource
       ↓
ok / changed / failed / skipped
       ↓
Verification
       ↓
Second run / idempotency
```

A safe rollout should look like:

```text
edit
 ↓
YAML/editor validation
 ↓
ansible syntax-check
 ↓
inventory inspection
 ↓
lint/static checks
 ↓
check + diff
 ↓
canary
 ↓
health verification
 ↓
small batch / serial
 ↓
full rollout
 ↓
second run
 ↓
monitor/audit
```

---

## Enhanced Deep Dive 1 — What Ansible Actually Does

Ansible is agentless in the ordinary Linux-management model.

The control node:

```text
reads inventory
resolves variables
parses YAML
renders Jinja2
selects modules
connects using SSH/connection plugin
executes remote work
receives structured result
```

Managed node:

```text
packages
files
users
groups
services
firewall
SELinux
storage
network state
```

Architecture:

```text
Control node
├── ansible.cfg
├── inventory
├── playbooks
├── variables
├── roles
├── collections
└── secrets
       |
       | SSH
       v
Managed node
├── OS state
├── Python/runtime
└── services/resources
```

Ansible does not replace Linux knowledge.

It automates Linux state changes.

---

## Enhanced Deep Dive 2 — Idempotency as Convergence

Idempotency:

```text
Run 1:
incorrect/current state
      ↓
playbook
      ↓
desired state
changed > 0
```

Run 2:

```text
desired state
      ↓
same playbook
      ↓
desired state
changed = 0
```

Example:

```yaml
- name: Ensure Apache is installed
  ansible.builtin.dnf:
    name: httpd
    state: present
```

This does not mean:

```text
run dnf install every time
```

It means:

```text
desired state:
httpd package exists
```

Idempotency reduces:

```text
unnecessary service restarts
configuration churn
deployment risk
audit noise
```

---

## Enhanced Deep Dive 3 — Controller State vs Managed-Host State

Ansible project files describe intent.

The managed node remains the runtime source of truth.

Example:

```text
playbook says:
sshd should be enabled

but target has:
sshd disabled
```

Run:

```text
Ansible observes state
      ↓
module changes target
      ↓
new target state
```

If a manual administrator later disables it:

```text
configuration drift
```

The next automation run can reconverge it.

This creates:

```text
desired state
vs
actual state
```

---

## Enhanced Deep Dive 4 — `ansible.cfg` Discovery and Configuration

Never assume the configuration file.

Inspect:

```bash
ansible --version
```

It shows the config file in use.

Also:

```bash
ansible-config dump --only-changed
ansible-config view
```

Configuration can affect:

```text
inventory path
remote user
forks
callbacks
host-key behavior
timeout
collections path
```

Operational problem:

```text
engineer runs from different directory
       ↓
different ansible.cfg discovered
       ↓
different inventory/user/settings
```

Always know the effective configuration.

---

## Enhanced Deep Dive 5 — Recommended Project Layout

Example:

```text
rhel-automation/
├── ansible.cfg
├── inventories/
│   ├── lab/
│   │   ├── hosts.yml
│   │   ├── group_vars/
│   │   └── host_vars/
│   ├── staging/
│   └── production/
├── roles/
│   ├── baseline/
│   └── webserver/
├── playbooks/
│   ├── baseline.yml
│   └── site.yml
├── collections/
│   └── requirements.yml
├── files/
├── templates/
├── tests/
└── README.md
```

Why structure matters:

```text
scope visible
variables predictable
review easier
environment separation
dependencies reproducible
```

---

## Enhanced Deep Dive 6 — Inventory Hostname vs `ansible_host`

Inventory logical name:

```text
web01
```

Connection endpoint:

```text
192.0.2.21
```

Example:

```ini
[web]
web01 ansible_host=192.0.2.21
web02 ansible_host=192.0.2.22

[web:vars]
ansible_user=automation
```

Inside a play:

```yaml
inventory_hostname
```

returns:

```text
web01
```

even if connection occurs to:

```text
192.0.2.21
```

This allows stable logical host identity independent of addressing.

---

## Enhanced Deep Dive 7 — Inventory Groups and Children

Example:

```text
all
└── production
    ├── web
    │   ├── web01
    │   └── web02
    └── db
        └── db01
```

Inspect:

```bash
ansible-inventory \
  -i inventories/lab \
  --graph
```

Inspect one host:

```bash
ansible-inventory \
  -i inventories/lab \
  --host web01
```

A host can belong to several groups.

Therefore it can inherit variables from several scopes.

---

## Enhanced Deep Dive 8 — Dynamic Inventory Awareness

Large cloud environments often do not maintain every instance manually in a text file.

Dynamic inventory can query:

```text
cloud API
CMDB
virtualization platform
asset inventory
```

and create groups based on:

```text
tags
region
environment
application
role
```

Model:

```text
Cloud API
   ↓ inventory plugin
hosts + metadata
   ↓
Ansible groups
```

Before running automation:

```bash
ansible-inventory --graph
ansible-inventory --list
```

still applies.

Automation should never change hosts you have not inspected/scoped.

---

## Enhanced Deep Dive 9 — SSH Layer Before Ansible Layer

If:

```bash
ansible all -m ansible.builtin.ping
```

fails, classify the layer.

```text
DNS?
route?
TCP/22?
host key?
SSH authentication?
remote shell?
Python/module execution?
sudo/become?
playbook?
```

Direct test:

```bash
ssh -vv \
automation@node1.lab.example
```

Then Ansible:

```bash
ansible node1.lab.example \
  -m ansible.builtin.ping \
  -vvv
```

`ansible.builtin.ping` is not ICMP ping.

It verifies Ansible connectivity/module execution.

---

## Enhanced Deep Dive 10 — `become`: Authentication vs Privilege Escalation

Connection:

```text
SSH as automation user
```

Privilege operation:

```text
sudo/become to root
```

These are different layers.

```text
Control node
    ↓ SSH
automation user
    ↓ sudo
root privilege for selected task
```

Example:

```yaml
- name: Install package
  hosts: web
  become: true

  tasks:
    - name: Ensure httpd is installed
      ansible.builtin.dnf:
        name: httpd
        state: present
```

Security principle:

```text
automation account
→ only required privilege
```

Unrestricted passwordless sudo increases the impact of a stolen automation credential.

---

## Enhanced Deep Dive 11 — Ad-Hoc Commands vs Playbooks

Ad-hoc:

```bash
ansible all \
  -m ansible.builtin.command \
  -a 'uptime'
```

Useful for:

```text
inspection
one-off read-only query
small safe operational task
```

Playbook:

```text
version controlled
repeatable
reviewable
variables
handlers
roles
tests
```

Do not build a critical environment from an undocumented history of ad-hoc commands.

---

## Enhanced Deep Dive 12 — YAML Types

YAML represents:

```text
mapping
list
string
integer
boolean
null
```

Example:

```yaml
web:
  port: 8080
  enabled: true

packages:
  - curl
  - rsync
```

File modes should normally be quoted:

```yaml
mode: '0640'
```

Why?

Because a mode should be treated as the expected mode representation, not accidentally interpreted as an ordinary integer.

---

## Enhanced Deep Dive 13 — FQCN

FQCN:

```text
Fully Qualified Collection Name
```

Examples:

```text
ansible.builtin.dnf
ansible.builtin.copy
ansible.builtin.template
ansible.posix.firewalld
```

Benefits:

```text
clear collection
clear module identity
fewer naming collisions
easier documentation lookup
```

---

## Enhanced Deep Dive 14 — `ansible-doc`

Use installed documentation:

```bash
ansible-doc ansible.builtin.dnf
ansible-doc ansible.builtin.template
ansible-doc ansible.builtin.user
```

Short form:

```bash
ansible-doc -s \
ansible.builtin.user
```

Read:

```text
arguments
types
defaults
examples
return values
check-mode support
```

This is more reliable than remembering syntax from another Ansible version.

---

## Enhanced Deep Dive 15 — State Modules vs `command` and `shell`

Bad default:

```yaml
- name: Install web server
  ansible.builtin.shell:
    cmd: dnf install -y httpd
```

Better:

```yaml
- name: Ensure web package is present
  ansible.builtin.dnf:
    name: httpd
    state: present
```

State module:

```text
observes state
compares desired state
changes only if necessary
returns structured result
```

Shell:

```text
executes text
```

Use shell only when shell features are genuinely required.

Avoid shell with untrusted variables.

---

## Enhanced Deep Dive 16 — Making `command` More Idempotent

Sometimes no state module exists.

Example:

```yaml
- name: Initialize application once
  ansible.builtin.command:
    cmd: /usr/local/bin/app-init --output /var/lib/app/db
    creates: /var/lib/app/db
```

Mental model:

```text
Does /var/lib/app/db exist?
 ├── yes → skip
 └── no  → run command
```

Another pattern:

```yaml
removes:
```

can run a command only when a path exists.

---

## Enhanced Deep Dive 17 — Playbook Structure

Example:

```yaml
---
- name: Configure web tier
  hosts: web
  become: true

  vars:
    web_port: 8080

  pre_tasks:
    - name: Validate variables
      ansible.builtin.assert:
        that:
          - web_port | int > 0

  roles:
    - webserver

  tasks:
    - name: Verify service
      ansible.builtin.uri:
        url: "http://127.0.0.1:{{ web_port }}/"

  post_tasks:
    - name: Report completion
      ansible.builtin.debug:
        msg: "Configured {{ inventory_hostname }}"
```

Think:

```text
preconditions
    ↓
roles/tasks
    ↓
handlers
    ↓
verification
```

---

## Enhanced Deep Dive 18 — Handlers

Configuration task:

```yaml
- name: Deploy config
  ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app.conf
  notify: Restart app
```

Handler:

```yaml
- name: Restart app
  ansible.builtin.service:
    name: app
    state: restarted
```

Handler is queued only when notifying task reports:

```text
changed
```

This prevents unnecessary restarts.

---

## Enhanced Deep Dive 19 — `meta: flush_handlers`

Sometimes a later health check needs the restart first.

```yaml
- name: Deploy configuration
  ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app.conf
  notify: Restart app

- name: Run pending handlers now
  ansible.builtin.meta:
    flush_handlers

- name: Validate application
  ansible.builtin.uri:
    url: http://127.0.0.1:8080/health
```

Do not overuse this.

Frequent handler flushes can create repeated restarts.

---

## Enhanced Deep Dive 20 — Handler `listen`

Several handlers can listen to one notification topic.

```yaml
tasks:
  - name: Deploy web config
    ansible.builtin.template:
      src: web.conf.j2
      dest: /etc/web.conf
    notify: web configuration changed

handlers:
  - name: Validate web config
    ansible.builtin.command:
      cmd: webd --check
    changed_when: false
    listen: web configuration changed

  - name: Restart web
    ansible.builtin.service:
      name: webd
      state: restarted
    listen: web configuration changed
```

This decouples task notification from exact handler names.

---

## Enhanced Deep Dive 21 — Variables: Data vs Logic

Hard-coded:

```yaml
dest: /srv/prod-web
port: 8443
```

Reusable:

```yaml
dest: "{{ web_document_root }}"
port: "{{ web_port }}"
```

Then:

```text
lab
web_port=8080

production
web_port=8443
```

Same role.

Different data.

This is the core idea:

```text
automation logic
+
environment data
```

---

## Enhanced Deep Dive 22 — Variable Precedence

Ansible has many variable sources.

Do not design a project where the same variable is overridden everywhere.

Practical rule:

```text
role defaults
      ↓
group data
      ↓
host exceptions
      ↓
very deliberate higher-precedence overrides
```

When confused:

```bash
ansible-inventory \
  --host web01
```

and add temporary debug:

```yaml
- ansible.builtin.debug:
    var: web_port
```

Do not add:

```yaml
| default(...)
```

to hide a truly required missing variable.

---

## Enhanced Deep Dive 23 — Facts and Fact Gathering Cost

Facts can include:

```text
distribution
kernel
CPU
memory
interfaces
addresses
mounts
```

Gather:

```bash
ansible node1 \
  -m ansible.builtin.setup
```

But fact gathering costs:

```text
connection
remote execution
data transfer
processing
```

If a play does not use facts:

```yaml
gather_facts: false
```

can reduce overhead.

---

## Enhanced Deep Dive 24 — Registered Results Are Structured

Example:

```yaml
- name: Query kernel
  ansible.builtin.command:
    cmd: uname -r
  register: kernel_result
  changed_when: false

- name: Show kernel
  ansible.builtin.debug:
    msg: "{{ kernel_result.stdout }}"
```

Typical result fields can include:

```text
stdout
stderr
rc
changed
failed
```

Do not parse formatted terminal output if the module already returns structured fields.

---

## Enhanced Deep Dive 25 — `changed_when`

Diagnostic commands should not claim that they changed the host.

```yaml
- name: Read service state
  ansible.builtin.command:
    cmd: systemctl is-active httpd
  register: httpd_state
  changed_when: false
  failed_when: false
```

Now Ansible reports:

```text
ok
```

rather than:

```text
changed
```

for an inspection command.

---

## Enhanced Deep Dive 26 — `failed_when`

Suppose a tool uses:

```text
0 healthy
3 stopped but expected/acceptable for query
other error
```

Example:

```yaml
- name: Query application
  ansible.builtin.command:
    cmd: /usr/local/bin/app status
  register: result
  changed_when: false
  failed_when: result.rc not in [0, 3]
```

Only do this when you understand the command's exit-code contract.

Bad:

```yaml
failed_when: false
```

everywhere.

That hides failures.

---

## Enhanced Deep Dive 27 — Preconditions with `assert`

Fail before changing the host.

```yaml
- name: Validate web settings
  ansible.builtin.assert:
    that:
      - web_port | int >= 1024
      - web_port | int <= 65535
      - web_document_root is string
    fail_msg: "Invalid web configuration"
```

Useful assertions:

```text
required variable defined
valid port range
supported distribution
correct environment
minimum free capacity
allowed target disk
```

---

## Enhanced Deep Dive 28 — Jinja2 Filters and Types

Examples:

```jinja2
{{ web_port | int }}

{{ web_enabled | bool }}

{{ admin_users | join(',') }}

{{ optional_value | default('fallback') }}
```

For stable generated files:

```jinja2
{% for admin in admin_users | sort %}
admin={{ admin }}
{% endfor %}
```

Sorting makes deterministic output.

---

## Enhanced Deep Dive 29 — `omit`

Sometimes:

```text
argument should not be sent
```

instead of:

```text
argument = empty
```

Example:

```yaml
- name: Manage users
  ansible.builtin.user:
    name: "{{ item.name }}"
    shell: "{{ item.shell | default(omit) }}"
  loop: "{{ users }}"
```

This allows module/default/current behavior when shell is not defined.

---

## Enhanced Deep Dive 30 — Lookups Run on the Control Side

Example:

```yaml
key: "{{ lookup('file', 'files/opsadmin.pub') }}"
```

The file is read from the control-side project.

Model:

```text
control node file
     ↓ lookup
Jinja value
     ↓ module argument
managed host
```

Be careful with:

```text
control-node private data
credentials
environment variables
secret files
```

Do not expose them to hosts unnecessarily.

---

## Enhanced Deep Dive 31 — Ansible Vault and Secret Separation

Normal variable:

```yaml
db_password: "{{ vault_db_password }}"
```

Encrypted file contains:

```text
vault_db_password
```

Good structure:

```text
group_vars/production/vars.yml
group_vars/production/vault.yml
```

Principles:

```text
logic outside encrypted file
secret values encrypted
vault password outside Git
limited production decrypt access
```

Vault protects data at rest.

It does not automatically hide runtime output.

---

## Enhanced Deep Dive 32 — `no_log` Is Not Complete Secret Management

Example:

```yaml
- name: Configure secret
  no_log: true
  ...
```

This can suppress Ansible task output.

But a secret can still leak through:

```text
template content
application log
shell command line
debug task elsewhere
callback/plugin
external system
```

Do not put secrets in:

```text
task name
filename
error message
command argument when avoidable
```

---

## Enhanced Deep Dive 33 — Loops and Data Modeling

List of dicts:

```yaml
users:
  - name: alice
    groups:
      - operations
  - name: bob
    groups:
      - developers
```

Task:

```yaml
- name: Create users
  ansible.builtin.user:
    name: "{{ item.name }}"
    groups: "{{ item.groups }}"
  loop: "{{ users }}"
  loop_control:
    label: "{{ item.name }}"
```

Readable output:

```text
item=alice
item=bob
```

instead of printing the entire structure.

---

## Enhanced Deep Dive 34 — Dictionary Loop with `dict2items`

Data:

```yaml
users:
  alice:
    groups:
      - operations
  bob:
    groups:
      - developers
```

Task:

```yaml
- name: Create users
  ansible.builtin.user:
    name: "{{ item.key }}"
    groups: "{{ item.value.groups }}"
  loop: "{{ users | dict2items }}"
```

Choose the data structure that makes intent easiest to review.

---

## Enhanced Deep Dive 35 — Blocks, Rescue, Always

Structure:

```yaml
- name: Controlled deployment
  block:
    - name: Deploy config
      ...

    - name: Validate app
      ...

  rescue:
    - name: Report deployment failure
      ...

  always:
    - name: Collect final status
      ...
```

Important:

```text
block/rescue
≠
database transaction
```

If task 1 already changed the host before task 2 fails, rescue must explicitly undo it if rollback is required.

---

## Enhanced Deep Dive 36 — Tags

Tags select execution subsets:

```bash
ansible-playbook site.yml \
  --tags web

ansible-playbook site.yml \
  --skip-tags packages
```

Inspect:

```bash
ansible-playbook site.yml \
  --list-tags
```

Risk:

```text
configuration tag runs
but package prerequisite tag skipped
```

Document which tags are safe independently.

Tags are not security boundaries.

---

## Enhanced Deep Dive 37 — Imports vs Includes

Concept:

```text
import
→ more static
→ expanded earlier

include
→ more dynamic
→ evaluated at runtime
```

Examples:

```yaml
- import_playbook: baseline.yml
```

and:

```yaml
- name: Include optional web tasks
  ansible.builtin.include_tasks:
    file: web.yml
  when: web_enabled | bool
```

Static structure is easier to inspect.

Use dynamic includes when runtime behavior genuinely requires them.

---

## Enhanced Deep Dive 38 — Role Structure

```text
roles/
└── webserver/
    ├── defaults/
    │   └── main.yml
    ├── vars/
    │   └── main.yml
    ├── tasks/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml
    ├── templates/
    ├── files/
    └── meta/
```

Use:

```text
defaults
→ values users of role can override

vars
→ stronger internal values
```

Do not put every configurable value into `vars/main.yml`, or the role becomes hard to reuse.

---

## Enhanced Deep Dive 39 — Role README as an Operational Contract

A reusable role should document:

```text
purpose
supported OS/release
required collections
variables
defaults
examples
security impact
ports/services
files changed
handlers/restarts
verification
rollback
```

Automation is not truly reusable if only the original author understands it.

---

## Enhanced Deep Dive 40 — Collections and `requirements.yml`

Example:

```yaml
---
collections:
  - name: ansible.posix
  - name: community.general
```

Install:

```bash
ansible-galaxy collection install \
  -r collections/requirements.yml
```

Inspect:

```bash
ansible-galaxy collection list
```

A collection is a software dependency.

Manage:

```text
source
version
trust
compatibility
```

rather than installing random content manually.

---

## Enhanced Deep Dive 41 — Execution Environments

An execution environment can package:

```text
ansible-core
collections
Python libraries
system utilities
```

into a reproducible container image.

Model:

```text
playbook
  +
execution environment
  ↓
same automation dependencies
  ↓
developer
CI
Automation Controller
```

This reduces:

```text
works on my laptop
```

caused by hidden dependency differences.

---

## Enhanced Deep Dive 42 — `ansible-navigator` Awareness

Where available, `ansible-navigator` supports workflows around:

```text
execution environments
inventory inspection
module documentation
playbook execution
run artifacts
```

The exact available features depend on the installed Red Hat automation environment.

The important concept is reproducible execution tooling, not memorizing one UI.

---

## Enhanced Deep Dive 43 — Validation Pipeline

Different tools answer different questions.

```text
YAML parser
→ is the document valid YAML?

syntax-check
→ is Ansible structure/module syntax acceptable?

ansible-lint
→ style/risk patterns?

check mode
→ predicted state change?

diff
→ content differences?

canary
→ does the real system actually work?
```

Commands:

```bash
ansible-playbook \
  site.yml \
  --syntax-check

ansible-lint 2>/dev/null || true

ansible-playbook \
  site.yml \
  --check \
  --diff \
  --limit node1
```

No single step proves production safety.

---

## Enhanced Deep Dive 44 — Check Mode Limitations

Check mode can be incomplete.

Examples:

```text
module does not support check
command cannot predict
later task depends on file that check did not create
external API has no dry-run
registered output differs
```

Therefore:

```text
check mode
≠
real execution
```

Use:

```text
check
+
canary
+
verification
```

---

## Enhanced Deep Dive 45 — Diff Mode and Secret Leakage

`--diff` can print:

```text
old file
new file
```

This is excellent for configuration review.

It is dangerous for:

```text
password files
private keys
tokens
database credentials
secret config
```

CI logs can retain the output.

Use:

```text
no_log
secret separation
controlled log access
```

and avoid diffing secret files.

---

## Enhanced Deep Dive 46 — Canary and `serial`

Rolling update:

```yaml
- name: Update web tier
  hosts: web
  serial: 1
```

Model:

```text
web01
  ↓ change
  ↓ health check
web02
  ↓ change
  ↓ health check
web03
```

If the canary fails:

```text
stop
investigate
```

instead of changing every host.

---

## Enhanced Deep Dive 47 — `max_fail_percentage`

A play can control tolerated failure level.

Concept:

```text
batch
  ↓
failures exceed threshold?
  ├── yes → stop
  └── no  → continue
```

Use carefully.

A nonzero tolerance is not automatically appropriate for a security or critical configuration rollout.

---

## Enhanced Deep Dive 48 — `run_once`

Some tasks should execute once.

Example:

```yaml
- name: Query deployment metadata once
  ansible.builtin.command:
    cmd: /usr/local/bin/get-release-id
  register: release_id
  run_once: true
  changed_when: false
```

Typical use:

```text
create one shared value
query central API once
generate one report
```

Understand variable behavior across hosts/batches.

---

## Enhanced Deep Dive 49 — `delegate_to`

A task can execute on another host.

Example architecture:

```text
web01
  ↓ delegate
load balancer: drain web01
  ↓
update web01
  ↓
health check
  ↓ delegate
load balancer: enable web01
```

Example:

```yaml
- name: Drain host from load balancer
  ansible.builtin.command:
    cmd: /usr/local/bin/lb-drain {{ inventory_hostname }}
  delegate_to: lb01
```

Delegation changes the trust/execution context.

Know where credentials and files are used.

---

## Enhanced Deep Dive 50 — Async Tasks

Some legitimate tasks take longer than normal task timeout.

Ansible supports asynchronous execution/polling patterns.

Use cases:

```text
long software operation
long maintenance operation
background workflow
```

Still require:

```text
completion check
failure check
post-validation
```

Async does not remove the need for safe rollout.

---

## Enhanced Deep Dive 51 — Forks and Concurrency

Higher parallelism is not automatically better.

Too many simultaneous hosts can overload:

```text
package repository
storage
database
API
network
control node
target CPU
```

Automation performance is a systems problem.

Controls include:

```text
forks
serial
strategy
task design
```

---

## Enhanced Deep Dive 52 — Deterministic Jinja Templates

Bad:

```jinja2
generated={{ ansible_date_time.iso8601 }}
```

if the timestamp is not functionally required.

Every run changes the file.

Better:

```jinja2
# Managed by Ansible

server={{ inventory_hostname }}

{% for admin in admin_users | sort %}
admin={{ admin }}
{% endfor %}
```

Same input:

```text
same output
```

which supports idempotency.

---

## Enhanced Deep Dive 53 — Template Validation

For critical config, validate the temporary rendered file before replacement.

Example sudoers:

```yaml
- name: Deploy sudoers policy safely
  ansible.builtin.template:
    src: ops.sudoers.j2
    dest: /etc/sudoers.d/ops
    owner: root
    group: root
    mode: '0440'
    validate: '/usr/sbin/visudo -cf %s'
```

Mental model:

```text
render temporary file
       ↓
validator
  ├── fail → destination unchanged
  └── success → replace destination
```

Use service-specific validators wherever possible.

---

## Enhanced Deep Dive 54 — `copy` vs `template` vs `lineinfile` vs `blockinfile`

Choose based on ownership.

```text
copy
→ entire static file owned by automation

template
→ entire dynamic file owned by automation

lineinfile
→ one managed line in otherwise unmanaged file

blockinfile
→ one managed block
```

Many independent `lineinfile` tasks can become hard to understand and can interact badly.

If automation owns the whole file, template is often cleaner.

---

## Enhanced Deep Dive 55 — Backup of Managed Configuration

Example:

```yaml
- name: Deploy app config
  ansible.builtin.template:
    src: app.conf.j2
    dest: /etc/app.conf
    owner: root
    group: root
    mode: '0640'
    backup: true
```

Backups can help rollback.

But old backups can contain:

```text
old passwords
tokens
internal IPs
deprecated security settings
```

Define retention and permissions.

---

## Enhanced Deep Dive 56 — Correct Service Role Pattern

Use this dependency chain:

```text
package
   ↓
directory
   ↓
configuration/template
   ↓ notify
config validator / handler
   ↓
service enabled/running
   ↓
firewall/SELinux
   ↓
health check
```

Example health check:

```yaml
- name: Verify HTTP
  ansible.builtin.uri:
    url: http://127.0.0.1:8080/
    status_code: 200
```

"systemd active" does not guarantee the application is healthy.

---

## Enhanced Deep Dive 57 — Firewall and SELinux Automation

Some modules live outside:

```text
ansible.builtin
```

Example namespaces can include:

```text
ansible.posix
```

Therefore:

```text
playbook dependency
→ collection dependency
```

Declare it in `requirements.yml`.

After developing automation, verify manually:

```bash
firewall-cmd --list-all
semanage port -l
ls -Z
```

Automation does not eliminate the need to understand the resulting Linux state.

---

## Enhanced Deep Dive 58 — Storage Automation Guardrails

Storage automation can destroy data rapidly.

Never design:

```text
find first unused disk
format it
```

without strong controls.

Better:

```text
inventory defines exact device ID
        ↓
assert expected size/model/path
        ↓
assert not mounted
        ↓
assert not already in LVM unless expected
        ↓
only then modify
```

Example guard concept:

```yaml
- name: Confirm approved lab disk
  ansible.builtin.assert:
    that:
      - storage_device == '/dev/sdb'
      - environment == 'lab'
```

In real environments use stronger stable device identity and inventory data.

---

## Enhanced Deep Dive 59 — Network Automation Guardrails

Changing the interface carrying SSH can disconnect Ansible.

Safe considerations:

```text
console/OOB
second interface
checkpoint/rollback feature if supported
canary
serial
post-change reachability
```

Model:

```text
Ansible changes IP
    ↓
SSH session disappears
    ↓
Can controller reconnect?
```

If the answer is unknown, the change design is incomplete.

---

## Enhanced Deep Dive 60 — Environment Separation

Repository:

```text
inventories/
├── lab/
├── staging/
└── production/
```

Benefits:

```text
separate hosts
separate variables
separate secret scope
clear operator intent
```

Do not depend only on host names like:

```text
prod-web01
```

to prevent accidental targeting.

Run commands with explicit inventory when safety matters:

```bash
ansible-playbook \
  -i inventories/lab \
  site.yml
```

---

## Enhanced Deep Dive 61 — Version Control Workflow

Treat automation as code.

```text
feature branch
    ↓
change
    ↓
lint/syntax
    ↓
lab test
    ↓
pull request
    ↓
review
    ↓
merge
    ↓
controlled deployment
```

Commit:

```text
playbooks
roles
inventories without secrets
requirements
docs
tests
```

Do not commit:

```text
vault password
private SSH keys
API tokens
generated production output
```

---

## Enhanced Deep Dive 62 — CI for Ansible

A CI pipeline can run:

```text
YAML validation
ansible-lint
syntax-check
role tests
static policy checks
execution environment build/test
```

Example conceptual pipeline:

```text
Git push
   ↓
lint
   ↓
syntax
   ↓
test role
   ↓
idempotency
   ↓
review approval
```

Production credentials should not be required for basic static validation.

---

## Enhanced Deep Dive 63 — Molecule Awareness

Molecule is commonly used for testing roles in disposable environments.

Conceptual lifecycle:

```text
create
  ↓
prepare
  ↓
converge
  ↓
verify
  ↓
idempotence
  ↓
destroy
```

A role test might prove:

```text
package installed
service active
config correct
port listening
second converge changed=0
```

Use tooling supported by your environment and test against an OS environment close enough to the real target.

---

## Enhanced Deep Dive 64 — Execution Environment Reproducibility

Without a reproducible controller:

```text
Engineer A:
ansible-core X
collection A version 1

Engineer B:
ansible-core Y
collection A version 3
```

Same playbook can behave differently.

Execution environment model:

```text
ansible-core
+
collections
+
Python packages
+
system dependencies
=
versioned execution image
```

This is a critical enterprise automation concept.

---

## Enhanced Deep Dive 65 — Automation Controller / AAP Architecture Awareness

Central automation platforms can add:

```text
Projects
Inventories
Credentials
RBAC
Job Templates
Schedules
Execution Environments
Workflow Jobs
Audit/Job Output
```

Model:

```text
Git repository
     ↓
Automation Controller
├── project
├── inventory
├── credentials
├── RBAC
├── job template
└── execution environment
       ↓
managed nodes
```

Benefits:

```text
central credential control
repeatable execution environment
auditing
RBAC
scheduled/approved jobs
```

---

## Enhanced Deep Dive 66 — Troubleshooting Undefined Variables

Error:

```text
VARIABLE IS NOT DEFINED
```

Do not immediately add a default.

Workflow:

```text
check spelling
  ↓
ansible-inventory --host
  ↓
group_vars/host_vars path
  ↓
role defaults/vars
  ↓
include/import scope
  ↓
nested dictionary structure
```

Commands:

```bash
ansible-inventory \
  --host web01

ansible-playbook \
  site.yml \
  -vv
```

A required variable should fail clearly if it is truly missing.

---

## Enhanced Deep Dive 67 — UNREACHABLE vs FAILED

Ansible result types matter.

```text
UNREACHABLE
→ connection layer
  DNS
  route
  SSH
  host key
  authentication

FAILED
→ connection succeeded
  but task/module failed
```

Example debugging:

```bash
ssh automation@node1
sudo -l

ansible node1 \
  -m ansible.builtin.ping \
  -vvv

ansible node1 \
  -b \
  -m ansible.builtin.command \
  -a 'id'
```

Classify before changing playbook logic.

---

## Enhanced Deep Dive 68 — Non-Idempotent Task Investigation

Second run reports:

```text
changed=1
```

for the same task.

Investigation:

```text
Which task?
    ↓
What diff/result changed?
    ↓
timestamp/random/order?
    ↓
shell instead of state module?
    ↓
missing creates/removes?
    ↓
incorrect changed_when?
    ↓
external system always changes?
```

Treat repeated changes as a signal.

---

## Enhanced Deep Dive 69 — Automation Run Auditing

For a production change, preserve:

```text
operator
timestamp
Git revision
inventory
limit
execution environment
changed hosts
failed hosts
task recap
approval/change reference
```

This lets you answer:

```text
Who changed web01?
Which code revision?
Which variables/inventory scope?
Which hosts actually changed?
```

Job output itself may contain sensitive infrastructure information, so protect it.

---

## Enhanced Deep Dive 70 — Final Automation Design Checklist

Before merge/deployment:

```text
Does the role express desired state?
Is it idempotent?
Are required inputs asserted?
Are secrets protected?
Is inventory scope explicit?
Are collections versioned?
Can it run in a reproducible environment?
Does it validate config before replacing?
Are handlers used for restarts?
Can it run on one canary?
Is serial/batch available?
Are storage/network destructive paths guarded?
Does check/diff help?
Is rollback defined?
Is second-run changed=0?
Can another engineer understand the README?
```

Automation quality is operational risk management written as code.

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Control Environment Baseline

Record:

```text
ansible-core version
Python
active ansible.cfg
collections
ansible-navigator availability
ansible-lint availability
SSH client
```

## Enhanced Lab 2 — Project Skeleton

Create:

```text
inventories/lab
inventories/staging
roles
playbooks
templates
files
collections
tests
README
```

## Enhanced Lab 3 — Inventory Aliases

Use logical:

```text
web01
```

with:

```text
ansible_host=IP
```

Verify.

## Enhanced Lab 4 — Group Hierarchy

Create:

```text
web
db
production
monitoring
```

and children.

Inspect using `--graph`.

## Enhanced Lab 5 — Effective Host Variables

Use:

```bash
ansible-inventory --host web01
```

and explain every inherited variable.

## Enhanced Lab 6 — Dynamic Inventory Design

Without real cloud credentials, design a mock mapping:

```text
tag:Role=web
→ web group

tag:Environment=prod
→ production group
```

## Enhanced Lab 7 — SSH Failure Layers

Break separately:

```text
DNS
host key
wrong private key
wrong user
```

Classify Ansible output.

## Enhanced Lab 8 — become

Configure a lab automation account.

Prove:

```text
normal command
privileged command
sudo denial
```

## Enhanced Lab 9 — Ad-Hoc vs Playbook

Inspect uptime ad hoc.

Then turn package/service desired state into a playbook.

## Enhanced Lab 10 — YAML Types

Create examples of:

```text
list
mapping
string
boolean
integer
```

and explain why modes are quoted.

## Enhanced Lab 11 — `ansible-doc`

Research 15 modules.

Record:

```text
important arguments
returns
check mode
examples
```

## Enhanced Lab 12 — First Idempotent Baseline

Manage:

```text
three packages
chronyd
operations group
MOTD
```

Run twice.

Require:

```text
second run changed=0
```

## Enhanced Lab 13 — `command` with `creates`

Build a safe generated artifact and prove it does not run twice.

## Enhanced Lab 14 — Play Execution Order

Use:

```text
pre_tasks
role
tasks
handler
post_tasks
```

Log actual execution order.

## Enhanced Lab 15 — Handler Notification

Change template once.

Observe handler runs.

Run again.

Observe no restart.

## Enhanced Lab 16 — Flush Handlers

Create a health check requiring the restart to happen before validation.

## Enhanced Lab 17 — Handler `listen`

Create one notification topic with two handlers.

## Enhanced Lab 18 — Variable Separation

Move:

```text
port
document root
environment
package list
```

out of tasks into variables.

## Enhanced Lab 19 — Variable Conflict

Deliberately define one value in several scopes.

Determine which value wins.

Then simplify the design.

## Enhanced Lab 20 — Facts Cost

Compare play with:

```text
gather_facts true
false
```

across several VMs.

## Enhanced Lab 21 — Registered Results

Register:

```text
rc
stdout
stderr
```

and use them conditionally.

## Enhanced Lab 22 — `changed_when`

Make a diagnostic command return `ok`, not `changed`.

## Enhanced Lab 23 — `failed_when`

Model a command where return code 3 is expected.

## Enhanced Lab 24 — Assertions

Reject:

```text
port outside range
missing required var
wrong environment
```

before any change.

## Enhanced Lab 25 — Filters

Use:

```text
default
bool
int
join
sort
```

in a real template.

## Enhanced Lab 26 — `omit`

Build user data with optional shell and use `omit`.

## Enhanced Lab 27 — Lookups

Read a public SSH key from a control-side file.

Explain where lookup executes.

## Enhanced Lab 28 — Vault

Create encrypted lab secret.

Ensure:

```text
secret not in Git
vault password not in Git
```

## Enhanced Lab 29 — `no_log`

Use a synthetic secret and inspect output with/without `no_log`.

Document remaining leak paths.

## Enhanced Lab 30 — Complex Loops

Manage users from:

```text
list of dictionaries
dictionary + dict2items
```

Use loop labels.

## Enhanced Lab 31 — Blocks

Create:

```text
block
rescue
always
```

and show that changed state before failure is not magically rolled back.

## Enhanced Lab 32 — Tags

Create safe tags.

Then demonstrate one unsafe partial-execution dependency and document it.

## Enhanced Lab 33 — Import vs Include

Implement static import and conditional dynamic include.

Compare:

```bash
--list-tasks
```

behavior.

## Enhanced Lab 34 — Role Defaults

Create a reusable role with tunable defaults and minimal internal vars.

## Enhanced Lab 35 — Role README

Document:

```text
purpose
variables
files changed
ports
services
security impact
verification
rollback
```

## Enhanced Lab 36 — Collection Requirements

Create `requirements.yml`.

Rebuild collection dependencies on a clean lab control node.

## Enhanced Lab 37 — Execution Environment Design

List:

```text
ansible-core
collections
Python dependencies
system packages
```

required for a reproducible environment.

## Enhanced Lab 38 — ansible-navigator

If available, inspect inventory/docs/run artifacts.

If unavailable, document its place in Red Hat automation tooling.

## Enhanced Lab 39 — Validation Pipeline

Run:

```text
syntax
lint
check
diff
canary
real run
second run
```

## Enhanced Lab 40 — Check Mode Limitation

Find a task whose later state cannot be fully predicted in check mode.

Explain why.

## Enhanced Lab 41 — Diff Secret Risk

Create a synthetic secret config.

Observe why diff output is sensitive.

Redesign.

## Enhanced Lab 42 — `serial: 1`

Update three web nodes one at a time with a health check.

## Enhanced Lab 43 — Canary Failure

Make canary health validation fail.

Ensure rollout stops.

## Enhanced Lab 44 — `run_once`

Generate one shared deployment value once.

## Enhanced Lab 45 — `delegate_to`

Delegate a local or load-balancer-simulator task.

## Enhanced Lab 46 — Async

Run a safe long-running task asynchronously and verify completion.

## Enhanced Lab 47 — Concurrency

Compare:

```text
forks
serial
```

and document infrastructure load implications.

## Enhanced Lab 48 — Deterministic Template

Render a sorted user/admin list.

Run twice.

No change on second run.

## Enhanced Lab 49 — Template Validation

Deploy a sudoers or service config using a validator.

Deliberately make the template invalid and prove destination stays safe.

## Enhanced Lab 50 — Module Choice

For 15 scenarios choose:

```text
copy
template
lineinfile
blockinfile
command
state module
```

and justify.

## Enhanced Lab 51 — Config Backup

Enable backup for a synthetic config.

Define retention/security policy.

## Enhanced Lab 52 — Web Role

Implement:

```text
package
document root
template
handler
service
firewall
health check
```

## Enhanced Lab 53 — SELinux Automation

Automate one safe content context or port rule with supported module/collection where available.

Verify manually.

## Enhanced Lab 54 — Storage Guardrails

Before any lab storage change, assert:

```text
environment=lab
exact device
expected capacity
not mounted
```

## Enhanced Lab 55 — Network Guardrails

Design a second-interface change with:

```text
console recovery
canary
post-change ping/SSH
rollback
```

## Enhanced Lab 56 — Environment Separation

Create lab/staging/production inventory trees.

Use explicit `-i` in run commands.

## Enhanced Lab 57 — Git Workflow

Use:

```text
feature branch
commit
diff
validation
review
merge
```

## Enhanced Lab 58 — CI Design

Create pipeline pseudocode/YAML for:

```text
YAML check
ansible-lint
syntax
role tests
```

without production credentials.

## Enhanced Lab 59 — Molecule Test Plan

Design:

```text
create
converge
verify
idempotence
destroy
```

for the web role.

## Enhanced Lab 60 — AAP Mapping

Map:

```text
Git project
inventory
credentials
job template
execution environment
RBAC
```

to the local project.

## Enhanced Lab 61 — Undefined Variable

Create three variable-scope failures.

Debug from inventory/project structure.

## Enhanced Lab 62 — UNREACHABLE vs FAILED

Create examples of:

```text
SSH unreachable
sudo task failure
module argument error
```

and classify.

## Enhanced Lab 63 — Non-Idempotent Timestamp

Create a timestamped template.

Observe repeated changes.

Remove nondeterministic field.

## Enhanced Lab 64 — Automation Audit

For one lab run record:

```text
operator
Git commit
inventory
limit
changed hosts
failed hosts
recap
```

## Enhanced Lab 65 — Baseline Role

Automate:

```text
packages
group
admin public key
chronyd
MOTD
firewall baseline
```

## Enhanced Lab 66 — Three-Tier Project

Deploy:

```text
web01
web02
db01
```

using:

```text
roles
group_vars
host_vars
Vault
handlers
templates
```

## Enhanced Lab 67 — Failure Injection

Create at least 15 failures across:

```text
inventory
SSH
become
YAML
variables
template
handler
collection
check mode
idempotency
```

## Enhanced Lab 68 — Full Safe Rollout

Use:

```text
syntax
check
diff
canary
serial
health
second run
```

and produce an idempotency report.



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Build the Automation Lab

1. Create one control node and three managed nodes.
2. Configure DNS or `/etc/hosts` lab resolution.
3. Create automation user.
4. Configure SSH key authentication.
5. Configure controlled sudo privilege.
6. Verify host-key checking.

### Lab 2 — Inventory

1. Build groups `web`, `db`, and `production`.
2. Verify using `ansible-inventory --graph`.
3. Add one host variable.
4. Add one group variable.
5. Explain variable scope.

### Lab 3 — First Playbook

1. Install three baseline packages.
2. Enable chronyd.
3. Run twice.
4. Verify second run is idempotent.

### Lab 4 — Variables and Facts

1. Gather facts.
2. Create OS-specific message.
3. Use group_vars.
4. Register a command result.
5. Print selected structured data.

### Lab 5 — Vault

1. Create encrypted variable file.
2. Reference a secret from a normal variable.
3. Run playbook with approved vault-password workflow.
4. Verify no plaintext secret appears in Git or logs.

### Lab 6 — Task Control

1. Use a loop.
2. Use condition based on fact.
3. Deploy config that notifies handler.
4. Use one block/rescue structure.
5. Run using tags.

### Lab 7 — Templates

1. Create Jinja2 service banner.
2. Render hostname, environment, IP, and managed warning.
3. Deploy to three hosts.
4. Change one variable and observe only affected output.

### Lab 8 — Roles

1. Create a `webserver` role.
2. Move package/service/template/handler tasks into role.
3. Apply to web group.
4. Reuse role in a second playbook.

### Lab 9 — Linux Baseline

1. Automate users/groups.
2. Automate packages.
3. Automate time service.
4. Automate MOTD.
5. Automate one firewall rule using available collection/module.
6. Verify state manually on managed nodes.

### Lab 10 — Failure Troubleshooting

1. Create wrong inventory hostname.
2. Break SSH key.
3. Create sudo failure.
4. Introduce YAML indentation error.
5. Reference undefined variable.
6. Use wrong package name.
7. Troubleshoot each with the appropriate layer/tool.

### Lab 11 — Safe Rollout

1. Create change affecting all three hosts.
2. Run syntax check.
3. Run check mode.
4. Apply to one canary host.
5. Verify.
6. Expand to remaining hosts.

### Lab 12 — Automation Review Challenge

1. Build a playbook from a written desired-state requirement without copying a solution.
2. Use at least one role, template, variable, handler, loop/condition, and Vault secret.
3. Run twice and verify idempotency.

## 6. Mini Project

# Mini Project — Automate a Three-Tier RHEL Environment

Inventory:

```text
[web]
web01
web02

[db]
db01

[all:vars]
ansible_user=automation
```

## Baseline Role
Apply to all hosts:

- baseline packages,
- operations group,
- NTP/chronyd,
- MOTD,
- admin SSH key,
- selected firewall baseline,
- service health verification.

## Web Role
Apply to web hosts:

- install web server,
- create document root,
- deploy Jinja2 site page,
- enable/start service,
- open required firewall service,
- handler on configuration change.

## Database Host
Do not deploy a full production database unless needed.

Instead:
- create database service account,
- create data directory,
- deploy lab config,
- demonstrate service-specific variable separation.

## Variables
Use:
```text
group_vars/all/
group_vars/web/
host_vars/db01/
```

## Secrets
Protect one lab secret with Vault.

## Scale
Structure:

```text
automation-project/
├── ansible.cfg
├── inventory.ini
├── group_vars/
├── host_vars/
├── roles/
│   ├── baseline/
│   └── webserver/
├── site.yml
└── README.md
```

## Validation Pipeline
Required workflow:

```text
syntax check
→ inventory graph
→ check mode
→ one canary host
→ manual verification
→ all web hosts
→ all environment
→ rerun to prove idempotency
```

## Failure Tests
1. host unreachable,
2. sudo failure,
3. invalid YAML,
4. undefined variable,
5. template syntax error,
6. service config failure,
7. firewall rule missing,
8. handler not triggered,
9. Vault password unavailable,
10. non-idempotent task.

Document:
```text
Failure
Layer
Evidence
Fix
Verification
Prevention
```

# Expanded Capstone — Automate a Managed RHEL Fleet

Topology:

```text
ansible-control.lab.example
       |
       +---- web01.lab.example
       +---- web02.lab.example
       +---- db01.lab.example
       +---- util01.lab.example
```

## Repository

```text
rhel-fleet-automation/
├── ansible.cfg
├── inventories/
│   ├── lab/
│   │   ├── hosts.yml
│   │   ├── group_vars/
│   │   └── host_vars/
│   └── production-example/
├── collections/
│   └── requirements.yml
├── roles/
│   ├── baseline/
│   ├── webserver/
│   ├── service_account/
│   └── monitoring_stub/
├── playbooks/
│   ├── baseline.yml
│   ├── web.yml
│   └── site.yml
├── tests/
├── docs/
└── README.md
```

## Baseline Role

Manage:

```text
approved packages
operations group
admin public key
chronyd
MOTD
selected service state
firewalld baseline
one SELinux-aware path
```

## Web Role

Required dependency flow:

```text
package
   ↓
document root
   ↓
template
   ↓
configuration validation
   ↓
handler restart only on change
   ↓
service enabled/running
   ↓
firewall
   ↓
health check
```

## Variable Model

Use:

```text
role defaults
group_vars
host_vars only for real exception
one Vault secret
assert for required values
```

## Security Rules

Do not:

```text
disable SSH host-key checking
commit Vault password
commit private key
put plaintext secret in Git
use unrestricted shell where module exists
use ignore_errors everywhere
automatically format discovered disk
run against every production host first
```

## Validation Pipeline

```text
ansible --version/config
      ↓
inventory graph
      ↓
syntax
      ↓
lint
      ↓
check + diff canary
      ↓
real canary
      ↓
health
      ↓
serial rollout
      ↓
second run changed=0
```

## Required Guardrails

### Storage

If automation contains storage examples:

```text
environment must equal lab
exact allowed device defined
assert target is expected
```

### Networking

Use:

```text
second interface
console/OOB plan
canary
post-change connectivity
```

### Secrets

Use:

```text
Vault or approved secret system
no_log where required
restricted job output
```

## Failure Matrix

At least 20:

```text
inventory hostname wrong
DNS failure
host-key mismatch
wrong SSH key
sudo denied
missing remote Python/module dependency
YAML indentation
undefined variable
wrong variable precedence assumption
missing collection
template syntax
template validator failure
handler not notified
wrong service handler
check-mode false confidence
Vault password unavailable
diff leaks synthetic secret
non-idempotent command
canary health failure
serial rollout halted
```

Document:

```text
Failure layer
Observed output
Verbose evidence
Root cause
Fix
Idempotency result
Rollback
Prevention
```

## Documentation

```text
ARCHITECTURE.md
INVENTORY_DESIGN.md
VARIABLE_MODEL.md
SECRET_MODEL.md
ROLE_DESIGN.md
VALIDATION_PIPELINE.md
ROLLOUT_POLICY.md
SECURITY_GUARDRAILS.md
TROUBLESHOOTING.md
IDEMPOTENCY_REPORT.md
CHANGE_LOG.md
```


## 7. Recommended Resources

Primary references:

- Red Hat Enterprise Linux Automation with Ansible (AU294/RH294 path) official course outline.
- Red Hat Ansible Automation Platform documentation.
- Ansible Core documentation for version 2.16-compatible behavior.
- Red Hat Enterprise Linux 10 documentation for the Linux tasks being automated.
- `ansible-doc` for installed modules.

Examples:

```bash
ansible-doc ansible.builtin.dnf
ansible-doc ansible.builtin.template
ansible-doc ansible.builtin.service
```
## 8. Certification Relevance

The current Red Hat automation course is the recommended next step after RHCSA-level knowledge and prepares for RHCE automation skills.

Red Hat currently describes the automation course as based on:
- RHEL 10,
- Ansible Core 2.16,
- development tools aligned with Ansible Automation Platform 2.5/2.6.

The key transition from RHCSA to RHCE-style work is:

```text
administer one system manually
        ↓
express repeatable state
        ↓
administer many systems safely with Ansible
```
## 9. Common Mistakes & Best Practices

- **Mistake:** Using shell/command for everything.
  - **Best practice:** Prefer state-aware modules when available.
- **Mistake:** Disabling SSH host-key checking.
  - **Best practice:** Provision and trust host keys properly.
- **Mistake:** Putting secrets in plain YAML.
  - **Best practice:** Use Vault or approved secret-management integration.
- **Mistake:** Running against all hosts first.
  - **Best practice:** Use syntax check, check mode, canary, and limited batches.
- **Mistake:** Writing one 1000-line playbook.
  - **Best practice:** Use roles, imports/includes, variables, and collections.
- **Mistake:** Creating templates that change every run.
  - **Best practice:** Keep generated content deterministic unless change is intentional.
- **Mistake:** Using `ignore_errors: true` to hide problems.
  - **Best practice:** Handle only expected failure modes and preserve real failures.
- **Mistake:** Automating a task you do not understand manually.
  - **Best practice:** Understand the underlying RHEL state first.
- **Mistake:** Treating check mode as perfect.
  - **Best practice:** Verify module check-mode support and test actual runtime state.
- **Mistake:** Not testing idempotency.
  - **Best practice:** Run automation twice and investigate repeated changes.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the current Red Hat automation base platform?

**Short answer:** RHEL 10 with Ansible Core 2.16, aligned with AAP 2.5/2.6 development tooling.

### Q2. What is an inventory?

**Short answer:** A definition of managed hosts and groups.

### Q3. What is a play?

**Short answer:** A mapping of tasks to selected hosts.

### Q4. What is a module?

**Short answer:** A reusable unit that performs a specific automation operation.

### Q5. What is idempotency?

**Short answer:** Repeated runs converge to the same desired state without unnecessary changes.

### Q6. Why prefer `dnf` module over shelling out to dnf?

**Short answer:** It is state-aware and provides clearer idempotent behavior.

### Q7. What are facts?

**Short answer:** Information gathered about managed hosts.

### Q8. What is `register` used for?

**Short answer:** Store a task result in a variable.

### Q9. What is Ansible Vault?

**Short answer:** Encryption for sensitive Ansible variable/content data.

### Q10. What is a handler?

**Short answer:** A task normally run only when notified by a changed task.

### Q11. What is a role?

**Short answer:** A reusable standardized directory structure for automation content.

### Q12. What is a collection?

**Short answer:** A namespaced package of modules/plugins/roles/content.

### Q13. What does `--limit` do?

**Short answer:** Restricts a playbook run to selected inventory hosts/groups.

### Q14. What does `--check` do?

**Short answer:** Requests check/dry-run behavior where supported.

### Q15. Why run a playbook twice?

**Short answer:** To test idempotency.

### Q16. What does `ansible-doc` do?

**Short answer:** Displays documentation for installed Ansible modules/plugins.

### Q17. What is the safest rollout pattern?

**Short answer:** Validate → check → canary → verify → expand.


# Enhanced Self-Assessment Bank

### Q1. What does agentless mean here?
**Answer:** Ansible normally connects to managed Linux hosts without a permanent Ansible agent service.

### Q2. What is idempotency?
**Answer:** Repeated automation converges to the same desired state without unnecessary changes.

### Q3. What does `ansible --version` help identify?
**Answer:** Version/environment information including the active config file.

### Q4. Why does project structure matter?
**Answer:** It makes inventory, variables, roles, dependencies, and review predictable.

### Q5. `inventory_hostname` vs `ansible_host`?
**Answer:** Logical Ansible host identity vs actual connection endpoint.

### Q6. What does `ansible-inventory --graph` show?
**Answer:** Resolved inventory group/host relationships.

### Q7. Dynamic inventory purpose?
**Answer:** Generate inventory from APIs/cloud/CMDB metadata.

### Q8. What should be tested before Ansible logic?
**Answer:** Network and direct SSH connectivity.

### Q9. What does `become` do?
**Answer:** Privilege escalation after connection.

### Q10. Why prefer playbooks over many ad-hoc changes?
**Answer:** Repeatability, review, variables, version control, handlers, and testing.

### Q11. Why quote mode `'0640'`?
**Answer:** Express file mode predictably and avoid YAML numeric interpretation issues.

### Q12. What is FQCN?
**Answer:** Fully Qualified Collection Name.

### Q13. What does `ansible-doc` provide?
**Answer:** Documentation for installed modules/plugins.

### Q14. Why prefer state module to shell?
**Answer:** It understands desired/current state and supports clearer idempotent behavior.

### Q15. How can command be conditionally idempotent?
**Answer:** `creates`, `removes`, or correct `changed_when` patterns where appropriate.

### Q16. What is a play?
**Answer:** A mapping of hosts to tasks/roles and play-level settings.

### Q17. When does a handler run?
**Answer:** Normally after it is notified by a changed task.

### Q18. Why use `flush_handlers`?
**Answer:** Run queued handlers before later tasks that need their effect.

### Q19. What is handler `listen`?
**Answer:** A shared notification topic for handlers.

### Q20. Why separate variables from task logic?
**Answer:** Reuse the same automation across environments.

### Q21. Best response to variable precedence confusion?
**Answer:** Simplify competing definitions and inspect effective host variables.

### Q22. Why disable fact gathering sometimes?
**Answer:** Reduce unnecessary remote work when facts are not needed.

### Q23. What does `register` store?
**Answer:** Structured task result.

### Q24. What does `changed_when` do?
**Answer:** Defines whether a task result counts as changed.

### Q25. What does `failed_when` do?
**Answer:** Defines which result conditions count as failure.

### Q26. Why use `assert`?
**Answer:** Fail early before unsafe changes when preconditions are invalid.

### Q27. What does `default` filter do?
**Answer:** Supplies a fallback value when appropriate.

### Q28. What does `omit` do?
**Answer:** Causes a module argument to be left out.

### Q29. Where do lookups normally execute?
**Answer:** On the control side.

### Q30. What does Vault protect?
**Answer:** Selected Ansible data at rest.

### Q31. Does Vault suppress runtime secret output?
**Answer:** No.

### Q32. What does `no_log` do?
**Answer:** Suppresses most Ansible task-result output.

### Q33. Why `loop_control.label`?
**Answer:** Keep loop output concise/readable and reduce unnecessary data exposure.

### Q34. Is block/rescue a transaction?
**Answer:** No. Earlier changes remain unless explicitly reverted.

### Q35. Are tags a security boundary?
**Answer:** No.

### Q36. Import vs include?
**Answer:** Imports are more static; includes are evaluated more dynamically at runtime.

### Q37. Role defaults vs role vars?
**Answer:** Defaults are easily overridden; role vars have stronger precedence.

### Q38. Why role README?
**Answer:** Make behavior, variables, security impact, verification, and rollback understandable.

### Q39. What is a collection?
**Answer:** Namespaced package of modules/plugins/roles/content.

### Q40. Why requirements.yml?
**Answer:** Declare collection dependencies reproducibly.

### Q41. What is an execution environment?
**Answer:** Reproducible image containing Ansible and its automation dependencies.

### Q42. What does ansible-navigator help with?
**Answer:** Execution-environment-oriented inspection/execution where available.

### Q43. Does syntax-check prove production safety?
**Answer:** No.

### Q44. Is check mode perfect?
**Answer:** No; support and prediction vary by module/task.

### Q45. Why is diff mode sensitive?
**Answer:** It can print confidential file contents.

### Q46. What does `serial` do?
**Answer:** Limits how many hosts are updated in a batch.

### Q47. Why can canary rollout help?
**Answer:** It limits blast radius before wider deployment.

### Q48. What does `run_once` do?
**Answer:** Executes the task once in the relevant play/batch context.

### Q49. What does `delegate_to` do?
**Answer:** Runs a task on another host/control context.

### Q50. Why use async?
**Answer:** Support legitimate long-running tasks with later completion checking.

### Q51. Are more forks always better?
**Answer:** No; high concurrency can overload infrastructure.

### Q52. Why deterministic templates?
**Answer:** Same input produces same output and avoids unnecessary changes.

### Q53. What does template validation do?
**Answer:** Tests temporary rendered content before replacing destination.

### Q54. copy vs template?
**Answer:** Static full file vs dynamically rendered full file.

### Q55. lineinfile vs template?
**Answer:** One line in partly unmanaged file vs ownership of the whole file.

### Q56. Why protect config backups?
**Answer:** Old configs can contain sensitive values.

### Q57. Correct service automation sequence?
**Answer:** Package → config → handler → service → security policy → health check.

### Q58. Why declare external collections?
**Answer:** Modules such as some firewalld/SELinux tools are collection dependencies.

### Q59. Main storage automation risk?
**Answer:** Modifying the wrong device can destroy data.

### Q60. Main network automation risk?
**Answer:** Changing the active management path can disconnect the controller.

### Q61. Why separate lab/staging/production inventory?
**Answer:** Reduce accidental targeting and isolate environment data/secrets.

### Q62. Why version control Ansible?
**Answer:** Review, history, collaboration, rollback, CI.

### Q63. What can CI validate?
**Answer:** YAML, lint, syntax, role/static tests before deployment.

### Q64. Molecule purpose?
**Answer:** Test Ansible roles in disposable environments including idempotence.

### Q65. What does AAP Controller add?
**Answer:** Central projects, inventories, credentials, RBAC, jobs, schedules, execution environments, audit.

### Q66. Best response to undefined required variable?
**Answer:** Find the missing/mis-scoped definition rather than silently defaulting it.

### Q67. UNREACHABLE vs FAILED?
**Answer:** Connection-layer failure vs task/module execution failure.

### Q68. How troubleshoot non-idempotent task?
**Answer:** Identify repeated changed task, inspect diff/result, remove nondeterminism or use a state-aware model.

### Q69. Why audit automation runs?
**Answer:** Know who ran what revision against which scope and what actually changed.

### Q70. Safest rollout?
**Answer:** Validate → check/diff → canary → verify → serial/batch → full rollout → second-run idempotency.


## Completion Checklist

- [ ] I can configure an inventory and Ansible project.
- [ ] I can verify SSH/become connectivity.
- [ ] I can write idempotent YAML playbooks.
- [ ] I can use variables, facts, registered results, and Vault.
- [ ] I can use conditions, loops, handlers, blocks, and tags.
- [ ] I can deploy templates safely.
- [ ] I can build and reuse roles.
- [ ] I can troubleshoot inventory, SSH, YAML, variable, and module failures.
- [ ] I can automate common RHEL baseline tasks.
- [ ] I completed all labs and the three-tier automation mini project.
