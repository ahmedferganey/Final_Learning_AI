# 56. Google Cloud Platform

> Phase 14 — Google Cloud Platform

This course moves from **Google Cloud Platform Fundamentals** into practical Google Cloud engineering, administration, operations, security, and troubleshooting.

Course 51 focused on:

```text
"What is this Google Cloud service?"
```

Course 56 focuses on:

```text
"How do I design it?"
"How do I deploy it?"
"How do I secure it?"
"How do I operate it?"
"How do I troubleshoot it?"
"How do I automate it?"
```

The course is intentionally **not short**. It is designed to be used as a self-contained learning reference rather than a glossary.

It is broadly aligned with the current:

```text
Google Cloud Associate Cloud Engineer
```

certification because that certification closely matches the practical administration/engineering level of this phase.

## Current Associate Cloud Engineer Baseline

Current standard exam information:

```text
Exam duration: 2 hours
Questions: 50–60
Question types:
  - Multiple choice
  - Multiple select
Registration fee: $125 + applicable tax
Validity: 3 years
Prerequisites: none
Recommended experience: 6+ months hands-on with Google Cloud
```

Current official exam domains:

```text
1. Setting up a cloud solution environment                 ~20%
2. Planning and implementing a cloud solution              ~30%
3. Ensuring successful operation of a cloud solution       ~30%
4. Configuring access and security                          ~20%
```

The current exam guide also reflects newer Google Cloud terminology and products, including:

```text
Cloud Run
Cloud Run functions
Google Cloud Hyperdisk
Cloud NGFW
Google Cloud Managed Service for Apache Kafka
Google Cloud NetApp Volumes
Google Cloud Managed Lustre
Database Center
Cloud Hub
Active Assist
Gemini Cloud Assist
Gemini CLI
Application Design Center
Agent Runtime on Gemini Enterprise Agent Platform
```

This course includes those current concepts while maintaining the broader infrastructure and cloud-engineering foundation you need beyond the exam.

---

# Google Cloud Engineer Mental Model

A Google Cloud engineer works through this hierarchy:

```text
Google Cloud Organization
        |
      Folders
        |
      Projects
        |
     Resources
```

Billing is attached separately:

```text
Cloud Billing Account
        |
        +-- Production Project
        +-- Development Project
        +-- Shared Services Project
```

The core operating model is:

```text
Identity
   ↓
Resource Hierarchy
   ↓
Billing / Quotas
   ↓
Networking
   ↓
Compute
   ↓
Containers / Serverless
   ↓
Storage
   ↓
Databases / Data
   ↓
Security
   ↓
Observability
   ↓
Backup / DR
   ↓
Automation
   ↓
Troubleshooting
```

A representative enterprise architecture:

```text
                              Users
                                |
                           Cloud DNS
                                |
                   Global External Load Balancer
                                |
                   Cloud Armor + Cloud CDN
                                |
                   +------------+------------+
                   |                         |
               Region A                  Region B
                   |                         |
              MIG / GKE /               Cloud Run /
              Cloud Run                   MIG / GKE
                   \                         /
                    \                       /
                      Managed Data Services
                  Cloud SQL / Spanner / Firestore
                               |
                         Cloud Storage
                               |
                    Backup / Replication
```

Enterprise resource hierarchy:

```text
Organization
├─ Platform
│  ├─ Networking
│  ├─ Security
│  └─ Observability
├─ Production
│  ├─ App-A
│  └─ App-B
├─ NonProduction
│  ├─ Dev
│  └─ Test
└─ Sandbox
```

---

## 1. Topic Title

**Google Cloud Platform**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Build and operate a Google Cloud resource hierarchy.
- Manage organizations, folders, projects, billing accounts, quotas, labels, and APIs.
- Configure Cloud Identity and Google Cloud IAM.
- Create IAM policies and understand inheritance.
- Use predefined and custom IAM roles.
- Manage service accounts safely.
- Use service account impersonation and short-lived credentials.
- Explain and configure Workforce Identity Federation and Workload Identity Federation.
- Apply organization policies.
- Use Cloud Asset Inventory.
- Use Gemini Cloud Assist conceptually for resource and operations analysis.
- Design and operate VPC networks and regional subnets.
- Configure custom mode VPC networks.
- Configure routes, firewall rules, Cloud NGFW policies, secure tags, and service-account targeting.
- Implement Shared VPC.
- Configure VPC Network Peering.
- Use Private Google Access.
- Explain and use Private Service Connect.
- Configure Cloud NAT and Cloud Router.
- Configure HA VPN and Cloud Interconnect concepts.
- Configure Cloud DNS.
- Select and configure Google Cloud load balancers.
- Understand Network Service Tiers.
- Deploy and manage Compute Engine VMs.
- Select machine families and custom machine types.
- Configure Persistent Disk and Hyperdisk.
- Use snapshots, images, image families, and instance templates.
- Deploy Managed Instance Groups.
- Configure autoscaling, autohealing, rolling updates, and health checks.
- Use Spot VMs and reservations appropriately.
- Configure OS Login and VM Manager.
- Deploy and operate Google Kubernetes Engine.
- Explain Standard and Autopilot clusters.
- Configure node pools, private clusters, regional clusters, autoscaling, and Artifact Registry access.
- Work with Pods, Deployments, Services, StatefulSets, HPA, and VPA.
- Deploy and operate Cloud Run.
- Configure Cloud Run scaling, revisions, traffic splitting, IAM, networking, and service-to-service authentication.
- Deploy Cloud Run functions and understand current terminology.
- Use Eventarc for event-driven serverless applications.
- Understand Agent Runtime on Gemini Enterprise Agent Platform at a current exam-recognition level.
- Operate Artifact Registry.
- Operate Cloud Storage and its storage classes.
- Configure lifecycle management, versioning, retention, replication, and CMEK.
- Use Filestore, NetApp Volumes, and Managed Lustre appropriately.
- Use Storage Transfer Service.
- Select and operate Cloud SQL, AlloyDB, Spanner, Firestore, Bigtable, and Memorystore.
- Explain Database Center and database fleet operations.
- Use BigQuery for analytics.
- Use Pub/Sub and Dataflow for event/data pipelines.
- Understand Google Cloud Managed Service for Apache Kafka.
- Configure Cloud Monitoring and Cloud Logging.
- Deploy the Ops Agent.
- Create dashboards, metrics, alerts, uptime checks, and SLOs.
- Configure log buckets, sinks, routers, analytics, and audit logs.
- Use Cloud Trace, Profiler, Query Insights, and diagnostic tools.
- Understand Managed Service for Prometheus.
- Use Personalized Service Health, Active Assist, and Cloud Hub conceptually.
- Configure Cloud KMS and Secret Manager.
- Use Security Command Center.
- Apply VPC Service Controls.
- Configure backup, snapshots, restore, and disaster-recovery patterns.
- Use `gcloud`, `gsutil`-replacement workflows through `gcloud storage`, `bq`, `kubectl`, and Terraform safely.
- Explain Config Connector, Helm, and current IaC tooling.
- Troubleshoot IAM, VPC, compute, GKE, Cloud Run, storage, database, and observability issues.
- Design and document a complete production Google Cloud platform.

---

## 3. Prerequisites

Required:

- 48. Cloud Computing Fundamentals
- 51. Google Cloud Platform Fundamentals
- Networking fundamentals
- Linux administration
- Storage fundamentals
- Database fundamentals
- Virtualization
- Git
- Bash
- Basic Python
- Container fundamentals

Recommended tools:

```text
Google Cloud account
Google Cloud console
Cloud Shell
Google Cloud CLI
kubectl
Docker
Terraform
VS Code
```

Before making changes:

```bash
gcloud auth list
gcloud config list
gcloud config get-value project
```

Verify:

```text
active account
active project
Region
zone
billing context
```

before creating or modifying resources.

---

## 4. Core Concepts Explanation

# Part 1 — Google Cloud Engineering Scope

Google Cloud engineering spans:

```text
resource hierarchy
identity
networking
compute
containers
serverless
storage
data
security
operations
cost
automation
```

A production issue often crosses several of these layers.

# Part 2 — Control Plane vs Data Plane

Control plane:

```text
create VM
create VPC
change IAM
configure bucket
```

Data plane:

```text
read object
query database
publish Pub/Sub message
serve application request
```

Permissions and logs can differ between the two.

# Part 3 — Google Cloud Resource Hierarchy

The primary hierarchy is:

```text
Organization
   ↓
Folder
   ↓
Project
   ↓
Resource
```

IAM and organization-policy controls can inherit downward.

# Part 4 — Organization Resource

The organization resource is the top-level administrative boundary for an enterprise.

It enables centralized:

```text
IAM
organization policies
folders
projects
billing governance
security
asset inventory
```

# Part 5 — Standalone Organization Concept

The current Associate Cloud Engineer guide includes standalone-organization setup concepts.

The important engineering principle is that an organization gives a governed root for projects rather than operating unrelated personal projects.

# Part 6 — Folders

Folders organize projects.

Example:

```text
Organization
├─ Platform
├─ Production
├─ NonProduction
└─ Sandbox
```

Folders can also represent business units, environments, regions, or compliance boundaries.

# Part 7 — Projects

A project is a major Google Cloud resource and IAM boundary.

It contains resources and is associated with:

```text
project name
project ID
project number
billing account
enabled APIs
IAM policy
quotas
```

# Part 8 — Project ID

Project ID is globally unique and appears in many resource names/API calls.

Example:

```text
factory-prod-1234
```

Choose naming standards before large-scale project creation.

# Part 9 — Project Number

Google assigns a numeric project number.

Some Google-managed service identities and APIs refer to project number instead of project ID.

# Part 10 — Resource Naming

Use consistent naming:

```text
<org>-<env>-<region>-<service>-<purpose>
```

Example:

```text
acme-prod-euw1-vpc-app
```

Avoid names that become misleading after organizational changes.

# Part 11 — Labels

Labels are key-value metadata.

```text
environment=prod
owner=platform
cost_center=1204
application=orders
```

Use for cost allocation, filtering, automation, and operations.

# Part 12 — Tags and Secure Tags

Google Cloud also has **Tags** as hierarchical policy-aware resources, distinct from ordinary labels.

Secure tags can participate in modern firewall policies and governance.

Do not confuse:

```text
labels
network tags
resource-manager Tags
```

# Part 13 — Cloud Billing Account

Billing account pays for linked projects.

```text
Billing Account
├─ Prod Project
├─ Dev Project
└─ Shared Project
```

Billing permissions are separate from project-resource permissions.

# Part 14 — Billing Account Roles

Separate responsibilities:

```text
Billing Account Administrator
Billing Account User
Billing Account Viewer
Project Billing Manager
```

Use least privilege.

# Part 15 — Linking Projects to Billing

A project that uses billable services must normally be linked to an active billing account.

A billing suspension can cause service impact.

# Part 16 — Budgets

Budgets track cost thresholds.

Example:

```text
50% actual
80% actual
100% forecast
```

Budgets alert; they do not automatically hard-stop spending.

# Part 17 — Billing Export

Export detailed billing data to BigQuery for:

```text
FinOps
chargeback
trend analysis
SKU analysis
custom dashboards
```

# Part 18 — Pricing Calculator Concept

Estimate architecture before deployment.

Model:

```text
compute
storage
database
egress
load balancing
logging
support
```

# Part 19 — Quotas

Quotas control:

```text
resource count
API rate
regional capacity allocation
```

Quota exhaustion is a common deployment failure.

# Part 20 — Quota Increase

Operational workflow:

```text
measure need
check current quota
request increase early
verify approved capacity
```

Do not wait for production launch day.

# Part 21 — Service APIs

Many Google Cloud products require an API enabled.

Example:

```bash
gcloud services list --enabled
```

Enable a service:

```bash
gcloud services enable compute.googleapis.com
```

# Part 22 — API Enablement Governance

API enablement can create new attack/cost surface.

Control who can enable services and use organization policy where appropriate.

# Part 23 — Regions

Region is a geographic deployment area.

Choose based on:

```text
latency
service availability
data residency
cost
DR
carbon considerations
```

# Part 24 — Zones

Zone is a failure domain inside a Region.

```text
Region
├─ zone-a
├─ zone-b
└─ zone-c
```

Use multi-zone architectures for high availability.

# Part 25 — Product Availability

Not every Google Cloud product, machine family, accelerator, or feature exists in every location.

Always verify location availability during planning.

# Part 26 — Cloud Asset Inventory

Cloud Asset Inventory provides inventory/history/search for Google Cloud resources and policies.

Use for:

```text
resource discovery
security review
change analysis
governance
```

# Part 27 — Asset Inventory Search

Conceptual:

```bash
gcloud asset search-all-resources   --scope=projects/PROJECT_ID
```

Use for controlled estate discovery.

# Part 28 — Gemini Cloud Assist

Current Google Cloud engineering guidance includes AI-assisted operations through Gemini Cloud Assist.

Use AI assistance for:

```text
resource understanding
troubleshooting suggestions
query assistance
configuration guidance
```

but validate recommendations against official product behavior and change controls.

# Part 29 — Cloud Setup / Enterprise Foundation

A mature foundation includes:

```text
Cloud Identity
Organization
administrative groups
billing
hierarchy
network
logging
monitoring
security
hybrid connectivity
```

# Part 30 — Landing Zone Mental Model

A landing zone is the governed environment where workloads can safely land.

```text
identity
hierarchy
shared VPC
logging
security
billing
policy
```

should exist before uncontrolled workload growth.

# Part 31 — Cloud Identity

Cloud Identity centrally manages workforce identities for Google Cloud environments.

Use groups rather than individual role assignment where practical.

# Part 32 — Administrative Groups

Example enterprise groups:

```text
gcp-org-admins
gcp-billing-admins
gcp-network-admins
gcp-security-admins
gcp-logging-admins
gcp-developers
```

Assign roles to groups, then manage user lifecycle inside groups.

# Part 33 — IAM Mental Model

IAM answers:

```text
Who
can do what
on which resource?
```

Core concepts:

```text
principal
permission
role
policy
resource
```

# Part 34 — Principals

Principals include:

```text
users
groups
service accounts
workforce identities
workload identities
domains
```

depending on supported policy context.

# Part 35 — Permissions

Permissions are granular API operations.

Example:

```text
compute.instances.get
storage.objects.get
```

Administrators normally grant roles rather than individual permissions.

# Part 36 — Basic Roles

Broad legacy roles:

```text
Owner
Editor
Viewer
```

Avoid Owner/Editor for routine production access.

# Part 37 — Predefined Roles

Google-managed service-specific roles.

Examples conceptually:

```text
Compute Instance Admin
Storage Object Viewer
Logging Viewer
```

Prefer predefined roles for least privilege.

# Part 38 — Custom Roles

Create custom roles when predefined roles do not fit.

Maintain:

```text
purpose
permissions
owner
review cycle
```

because APIs/permissions evolve.

# Part 39 — IAM Policy Binding

A binding associates:

```text
role
+
members
```

Conceptual:

```yaml
role: roles/viewer
members:
  - group:auditors@example.com
```

# Part 40 — IAM Inheritance

Policy inheritance flows:

```text
Organization
 ↓
Folder
 ↓
Project
 ↓
Resource
```

A project-level user can inherit access from higher scope.

# Part 41 — IAM Conditions

IAM Conditions restrict access based on attributes such as:

```text
resource
time
request context
```

Use when a permanent unconditional role is too broad.

# Part 42 — Least Privilege

Grant only what is needed.

Bad:

```text
roles/owner
```

for a CI system.

Better:

```text
specific deploy/runtime roles
```

# Part 43 — Service Accounts

Service accounts represent workloads.

```text
Compute Engine
Cloud Run
GKE
CI/CD
```

should use service identities instead of human credentials.

# Part 44 — Service Account Attachment

Attach a service account directly to a resource where supported.

```text
VM
 ↓ service account
short-lived token
 ↓
Cloud API
```

# Part 45 — Service Account Keys

Downloaded JSON keys are long-lived secrets.

Avoid unless unavoidable.

Prefer:

```text
attached service accounts
impersonation
Workload Identity Federation
```

# Part 46 — Service Account Impersonation

A human or workload with permission can impersonate a service account and receive short-lived credentials.

This is safer than distributing keys.

# Part 47 — Short-Lived Credentials

Short-lived credentials reduce exposure duration.

Use them for:

```text
automation
cross-system access
CI/CD
temporary admin
```

# Part 48 — Workload Identity Federation

Allows external workloads to exchange external identity for short-lived Google Cloud credentials.

Use for:

```text
GitHub Actions
AWS workloads
Azure workloads
on-prem applications
```

without Google service-account key files.

# Part 49 — Workforce Identity Federation

Federates workforce identities from an external identity provider into Google Cloud.

Use when the organization does not want to create/manage duplicate Google workforce accounts.

# Part 50 — OS Login

OS Login links Compute Engine SSH access to IAM identity.

Benefits:

```text
central identity
no unmanaged SSH key sprawl
auditability
role-based access
```

# Part 51 — Organization Policy

Organization Policy enforces configuration constraints.

Examples:

```text
restrict locations
disable service-account key creation
restrict external IPs
restrict sharing
```

# Part 52 — Organization Policy Inheritance

Constraints can be set at:

```text
organization
folder
project
```

and inherited downward.

# Part 53 — Organization Policy vs IAM

```text
IAM:
who can do something

Organization Policy:
what configurations/capabilities are allowed
```

# Part 54 — Policy Exception Strategy

Exceptions should include:

```text
business owner
reason
scope
expiry/review date
compensating control
```

Avoid permanent undocumented exemptions.

# Part 55 — Cloud KMS

Cloud KMS manages encryption keys.

Use for:

```text
CMEK
rotation
access control
audit
```

# Part 56 — CMEK

Customer-managed encryption keys give customers more control over encryption-key lifecycle.

Operational responsibility increases:

```text
key availability
permissions
rotation
deletion
```

# Part 57 — Cloud HSM

HSM-protected keys use hardware-backed protection levels for supported cryptographic requirements.

# Part 58 — Secret Manager

Store application secrets:

```text
DB password
API token
private credential
```

Use versioning and workload IAM access.

# Part 59 — Secret Rotation

Rotation process:

```text
create new secret
update dependency
validate
disable old
delete after safe window
```

Automate where supported.

# Part 60 — Security Command Center

Central security posture/findings platform.

Use for:

```text
misconfiguration
threat findings
vulnerability/exposure context
compliance posture
```

depending on tier.

# Part 61 — VPC Service Controls

Create service perimeters around supported Google-managed services to reduce data-exfiltration risk.

Use for sensitive analytics/data environments.

# Part 62 — Access Context Concept

Context-aware security can consider:

```text
identity
device
network
location
```

for access decisions in supported products.

# Part 63 — Cloud Audit Logs

Audit log types include concepts such as:

```text
Admin Activity
Data Access
System Event
Policy Denied
```

depending on service.

# Part 64 — Admin Activity Logs

Record administrative/control-plane operations.

Use to answer:

```text
who changed the resource?
```

# Part 65 — Data Access Logs

Capture access to data-plane resources for supported services.

High volume means you should deliberately plan collection and cost.

# Part 66 — Policy Denied Logs

Useful when a request is denied by policy controls.

Correlate with IAM and organization policy.

# Part 67 — Security by Default

Preferred patterns:

```text
no public IP where unnecessary
service identity
private connectivity
least privilege
central logs
CMEK where required
```

# Part 68 — Break-Glass Access

Emergency admin access should be:

```text
limited
strongly protected
monitored
documented
tested
```

and not used daily.

# Part 69 — Access Review

Regularly review:

```text
owners
service-account roles
unused accounts
external users
keys
high-risk roles
```

# Part 70 — Security Engineering Workflow

```text
prevent
 ↓
detect
 ↓
investigate
 ↓
contain
 ↓
remediate
 ↓
verify
```

Google Cloud security services support different stages.

# Part 71 — Google Cloud VPC

A VPC network is **global**.

Its subnets are **regional**.

This is a critical Google Cloud networking distinction.

# Part 72 — Custom Mode VPC

Custom mode lets administrators define subnets explicitly.

Preferred for controlled enterprise address planning.

# Part 73 — Auto Mode VPC

Auto mode creates predefined subnets automatically in Regions.

Useful for simple labs, but usually less appropriate for deliberate enterprise CIDR design.

# Part 74 — Regional Subnet

Example:

```text
VPC global
├─ subnet-eu  10.20.0.0/20   europe-west1
└─ subnet-us  10.20.16.0/20  us-central1
```

# Part 75 — CIDR Planning

Plan for:

```text
current workloads
growth
GKE secondary ranges
hybrid networking
other clouds
mergers
```

Avoid overlap.

# Part 76 — Secondary IP Ranges

GKE VPC-native clusters commonly use secondary ranges for:

```text
Pods
Services
```

Plan them before cluster growth.

# Part 77 — Subnet Expansion

Google Cloud can expand a subnet primary IPv4 range under supported constraints.

You generally cannot shrink it later.

Plan carefully.

# Part 78 — Routes

Routes determine next hop.

Sources include:

```text
system-generated routes
static routes
dynamic BGP routes
policy-based routing in supported designs
```

# Part 79 — Default Internet Route

A default route can direct:

```text
0.0.0.0/0
→ default Internet gateway
```

but Internet reachability also depends on external IP or Cloud NAT and firewall policy.

# Part 80 — Static Route

Create custom static route for:

```text
NVA
VPN
special next hop
```

Use priority deliberately.

# Part 81 — Dynamic Routing

Cloud Router exchanges routes with BGP.

Used with:

```text
HA VPN
Cloud Interconnect
```

# Part 82 — Dynamic Routing Mode

VPC dynamic routing can be configured to control whether learned routes are regional or global in scope.

Choose based on hybrid topology.

# Part 83 — VPC Firewall Rules

Traditional VPC firewall rules are stateful.

Rules include:

```text
direction
priority
action
source/destination
target
protocol/port
```

# Part 84 — Ingress Rules

Ingress controls traffic entering a target workload.

Example:

```text
allow tcp:443
from load-balancer health ranges / approved sources
```

# Part 85 — Egress Rules

Egress controls outbound traffic.

Restrict when security requirements justify it.

# Part 86 — Firewall Priority

Lower numerical priority is evaluated before higher priority.

Document priority ranges to prevent accidental shadowing.

# Part 87 — Network Tags

Network tags can target VM firewall rules.

Example:

```text
target tag = web
```

Do not confuse with Resource Manager Tags.

# Part 88 — Service Account Firewall Targeting

Firewall rules can target workload identity via service accounts in supported patterns.

This can be stronger than manually managed instance tags.

# Part 89 — Cloud NGFW

Current Google Cloud networking includes **Cloud Next Generation Firewall (Cloud NGFW)** policies.

It provides centralized modern firewall policy capabilities beyond classic per-network rules.

# Part 90 — Hierarchical Firewall Policies

Apply firewall controls at organization/folder scope.

Useful for enterprise baseline enforcement.

# Part 91 — Secure Tags in Firewall Policy

Modern Cloud NGFW policy can use secure Tags for policy targeting.

This separates security intent from IP addressing.

# Part 92 — Firewall Logging

Enable logs selectively to inspect:

```text
allowed traffic
denied traffic
rule behavior
```

and export for analysis.

# Part 93 — Shared VPC

Host project owns network.

Service projects consume shared subnets.

```text
Host Project
  Shared VPC
  ├─ App Project A
  └─ App Project B
```

# Part 94 — Shared VPC Administrative Separation

Network team manages:

```text
VPC
subnets
firewall
hybrid connectivity
```

Application teams manage resources in service projects.

# Part 95 — VPC Network Peering

Private connectivity between VPC networks.

```text
VPC A ↔ VPC B
```

Peering is non-transitive.

# Part 96 — Peering CIDR Requirements

Overlapping subnet routes cause conflicts and block useful peering.

Plan CIDRs centrally.

# Part 97 — Private Google Access

Allows internal-only VMs in enabled subnets to reach supported Google APIs/services without external IPs.

# Part 98 — Private Service Connect

Provides private endpoints/service attachments for consuming or publishing services privately.

Use for:

```text
managed services
service producer/consumer
cross-project private APIs
```

# Part 99 — Cloud NAT

Managed source NAT for private workloads.

```text
Private VM
 ↓
Cloud NAT
 ↓
Internet
```

The VM needs no external IP.

# Part 100 — Cloud NAT and Cloud Router

Public NAT configuration uses Cloud Router as a control/configuration component, but Cloud Router is not forwarding packets itself.

# Part 101 — NAT Port Exhaustion

High outbound connection volume can exhaust NAT ports.

Monitor:

```text
allocated ports
errors
VM connection behavior
NAT IP capacity
```

# Part 102 — Cloud Router

Managed BGP control plane.

Use with:

```text
HA VPN
Interconnect
NCC designs
```

depending on topology.

# Part 103 — HA VPN

High-availability IPsec VPN.

Use redundant interfaces/tunnels and dynamic routing.

# Part 104 — VPN Components

```text
HA VPN gateway
peer gateway
Cloud Router
BGP sessions
VPN tunnels
```

all must align.

# Part 105 — Cloud Interconnect

Private connectivity to Google network.

Models include:

```text
Dedicated Interconnect
Partner Interconnect
```

for enterprise hybrid networking.

# Part 106 — Interconnect vs VPN

```text
VPN:
encrypted over Internet

Interconnect:
private provider/dedicated connectivity
```

Use VPN as backup where appropriate.

# Part 107 — Network Connectivity Center Concept

Network Connectivity Center can provide hub-style connectivity for complex hybrid/multicloud networks.

Use when topology exceeds simple pairwise connections.

# Part 108 — Cloud DNS

Managed authoritative DNS.

Supports:

```text
public zones
private zones
routing policies
DNS forwarding/peering patterns
```

# Part 109 — Private DNS

Use private zones for internal names.

Hybrid environments need forwarding and split-horizon design where appropriate.

# Part 110 — Cloud DNS Troubleshooting

Check:

```text
zone visibility
record
TTL
VPC association
forwarding
resolver path
```

# Part 111 — Load Balancing Overview

Google Cloud provides multiple load-balancing products.

Select based on:

```text
global vs regional
external vs internal
HTTP(S) vs TCP/UDP
proxy vs passthrough
```

# Part 112 — Global External Application Load Balancer

Global HTTP/S entry:

```text
global anycast IP
 ↓
Google edge
 ↓
backend services
```

Use for global web applications.

# Part 113 — Regional External Application Load Balancer

Regional layer-7 load balancing for workloads that need regional control/data path.

# Part 114 — Internal Application Load Balancer

Private layer-7 load balancing for internal applications/services.

# Part 115 — Network Load Balancer Concepts

Layer-4 options support TCP/UDP workloads where HTTP-aware routing is unnecessary.

# Part 116 — Backend Service

Defines backend capacity and policy.

Backends can include:

```text
instance groups
network endpoint groups
serverless backends
```

depending on LB type.

# Part 117 — Health Checks

Load balancer health depends on probes.

Check:

```text
path
port
firewall
application readiness
```

A misconfigured health check can remove every healthy backend.

# Part 118 — Cloud CDN

Caches content at Google's edge.

Use with compatible load-balancing origins.

Monitor cache hit ratio.

# Part 119 — Cloud Armor

Protect supported external web applications.

Capabilities include:

```text
WAF rules
IP/rate rules
DDoS-related protections
adaptive security features
```

depending on configuration.

# Part 120 — Network Service Tiers

Google Cloud supports network service tiers that influence path/performance/cost for eligible traffic.

Know the trade-off between premium global network usage and standard Internet-oriented paths where supported.

# Part 121 — Static IP Addresses

Reserve static addresses when:

```text
DNS endpoint
allowlist
partner integration
```

requires stable IP.

# Part 122 — External vs Internal IP

External IP:

```text
Internet-routable
```

Internal IP:

```text
VPC/private routing
```

Prefer internal-only workloads where public access is unnecessary.

# Part 123 — VPC Flow Logs

Sample/record network-flow metadata.

Useful for:

```text
traffic analysis
security investigation
troubleshooting
```

No full packet payload.

# Part 124 — Network Intelligence / Connectivity Tests Concept

Google Cloud networking diagnostics can analyze reachability/configuration paths.

Use before packet capture where configuration analysis is sufficient.

# Part 125 — Network Troubleshooting Layer Order

Trace:

```text
DNS
route
firewall
NAT/VPN
load balancer
health check
guest firewall
application
```

Do not change all layers at once.

# Part 126 — Compute Engine

Compute Engine provides VMs.

You control:

```text
machine type
image
disk
network
service account
metadata
availability
```

# Part 127 — Machine Families

Broad categories include:

```text
general purpose
compute optimized
memory optimized
accelerator optimized
```

Exact families evolve.

# Part 128 — Custom Machine Types

Customize vCPU/memory for supported machine families.

Useful when predefined shapes waste one resource dimension.

# Part 129 — Spot VMs

Discounted interruptible capacity.

Use for:

```text
batch
CI
rendering
stateless workers
```

with interruption handling.

# Part 130 — Reservations

Reserve Compute Engine capacity for workloads requiring capacity assurance.

Distinct from pricing discounts.

# Part 131 — Sole-Tenant Nodes

Dedicated physical host capacity for one customer.

Use for:

```text
licensing
compliance
physical isolation
```

# Part 132 — Images

VM boot images can be:

```text
public
custom
family-based
```

Use versioned golden images.

# Part 133 — Image Families

An image family points to a current non-deprecated image in that family.

Useful for controlled image pipelines.

# Part 134 — Instance Template

Defines reusable VM configuration:

```text
machine
image
disk
network
service account
metadata
labels
```

Used by Managed Instance Groups.

# Part 135 — Persistent Disk

Durable block storage.

Can be zonal or regional depending on product/configuration.

# Part 136 — Regional Persistent Disk

Replicates data across two zones in a Region for supported high-availability designs.

# Part 137 — Google Cloud Hyperdisk

Current Google Cloud block-storage family offering configurable performance options for modern Compute Engine workloads.

Select based on:

```text
IOPS
throughput
latency
capacity
VM support
```

# Part 138 — Local SSD

High-performance ephemeral local storage.

Use for:

```text
cache
scratch
rebuildable data
```

not sole persistent state.

# Part 139 — Snapshots

Block-storage snapshots support:

```text
backup
restore
clone
cross-region policy patterns
```

according to service capability.

# Part 140 — Snapshot Schedules

Automate snapshots with resource policies.

Define:

```text
frequency
retention
location
labels
```

# Part 141 — VM Metadata

Metadata can configure instances and startup scripts.

Do not put secrets into plaintext metadata.

# Part 142 — Startup Scripts

Example:

```bash
#!/bin/bash
apt-get update
apt-get install -y nginx
systemctl enable --now nginx
```

Use for bootstrap; use stronger configuration management for complex long-term state.

# Part 143 — VM Manager

VM Manager supports fleet operations such as:

```text
OS inventory
patching
configuration
OS policies
```

depending on enabled capabilities.

# Part 144 — Patch Management

Use staged patching:

```text
dev
staging
production canary
production fleet
```

and monitor reboot/application health.

# Part 145 — Managed Instance Group

MIG manages identical VM fleets.

```text
Instance Template
      ↓
MIG
├─ VM
├─ VM
└─ VM
```

# Part 146 — Regional MIG

Spreads instances across zones in a Region.

Preferred for highly available stateless application tiers.

# Part 147 — Autohealing

Health check detects unhealthy VM and MIG replaces it.

Application health endpoint should represent readiness.

# Part 148 — Autoscaling

Scale by:

```text
CPU
load-balancer utilization
Cloud Monitoring metric
schedule
```

depending on configuration.

# Part 149 — Rolling Update

MIG can roll new instance-template versions.

Control:

```text
max unavailable
max surge
replacement method
```

# Part 150 — Canary MIG Update Concept

Introduce new template to small portion first.

Validate metrics before full rollout.

# Part 151 — SSH Access

Prefer controlled identity:

```text
OS Login
IAP TCP forwarding
private networking
```

rather than unmanaged static SSH keys.

# Part 152 — IAP TCP Forwarding Concept

Identity-Aware Proxy can provide authenticated tunnels to internal VMs without direct public SSH exposure.

# Part 153 — Compute Troubleshooting

Check:

```text
instance state
serial output
boot disk
startup script
service account
route
firewall
quota
zone capacity
guest OS
```

# Part 154 — Artifact Registry

Stores:

```text
container images
language packages
artifacts
```

Use IAM and repository-scoped access.

# Part 155 — Artifact Registry Authentication

Prefer short-lived `gcloud`/credential-helper flows rather than static registry passwords.

# Part 156 — Artifact Lifecycle

Use:

```text
version tags
cleanup policies
vulnerability scanning pipeline
promotion rules
```

# Part 157 — Google Kubernetes Engine

GKE is managed Kubernetes.

Important modes:

```text
Standard
Autopilot
```

# Part 158 — GKE Standard

You manage more cluster/node configuration.

Use when you need:

```text
node-level control
special machine types
custom daemon workloads
advanced tuning
```

# Part 159 — GKE Autopilot

Google manages more node infrastructure.

You focus on Pod resource requests and Kubernetes workloads.

Operational overhead is lower.

# Part 160 — Regional GKE Cluster

Control plane is replicated across zones for higher availability.

Worker/node design still matters.

# Part 161 — Private GKE Cluster

Nodes use private IPs and control-plane access is restricted according to configuration.

Plan:

```text
Cloud NAT
Private Google Access
authorized control-plane access
```

# Part 162 — GKE Node Pools

Node pool groups nodes with common configuration:

```text
machine type
disk
labels
taints
version
autoscaling
```

# Part 163 — Node Autoscaling

Cluster autoscaler adjusts nodes to satisfy unschedulable Pods.

Pod requests must be realistic.

# Part 164 — Horizontal Pod Autoscaler

HPA scales replicas based on metrics.

```text
CPU / custom metric high
→ more Pods
```

# Part 165 — Vertical Pod Autoscaler

VPA recommends/changes Pod resource requests based on observed utilization.

Understand interaction with HPA.

# Part 166 — Pods

Smallest Kubernetes scheduling unit.

A Pod can contain one or more tightly coupled containers.

# Part 167 — Deployments

Manage stateless replicated Pods.

Supports rolling updates and rollback.

# Part 168 — StatefulSets

For stateful Pods needing stable:

```text
identity
ordering
persistent storage
```

# Part 169 — Kubernetes Services

Expose Pods through stable virtual service endpoints.

Types include:

```text
ClusterIP
LoadBalancer
NodePort
```

depending on use case.

# Part 170 — GKE Artifact Registry Access

Nodes/workloads require correct identity/IAM to pull private images.

Troubleshoot:

```text
repository
region
image name
service account
permissions
```

# Part 171 — Workload Identity for GKE

Map Kubernetes workload identity to Google Cloud IAM without service-account keys.

Preferred for Pod-to-Google-API authentication.

# Part 172 — GKE Troubleshooting

Use:

```bash
kubectl get nodes
kubectl get pods -A
kubectl describe pod POD
kubectl logs POD
kubectl get events --sort-by=.metadata.creationTimestamp
```

Then correlate with Cloud Logging/Monitoring.

# Part 173 — Cloud Run

Cloud Run is a fully managed serverless application platform for containers invoked by requests or events.

No VM/node administration.

# Part 174 — Cloud Run Service

Deploy a stateless container:

```text
container image
 ↓
Cloud Run
 ↓
HTTPS / events
```

# Part 175 — Cloud Run Revision

Each deployment creates immutable revision configuration.

Use revisions for rollback and traffic management.

# Part 176 — Cloud Run Traffic Splitting

Example:

```text
revision-v1 90%
revision-v2 10%
```

Useful for canary releases.

# Part 177 — Cloud Run Autoscaling

Configure:

```text
minimum instances
maximum instances
concurrency
CPU behavior
```

according to workload.

# Part 178 — Cloud Run Authentication

Private services can require authenticated callers.

Use IAM/service identity for service-to-service calls.

# Part 179 — Cloud Run Networking

Options include:

```text
public/private ingress controls
VPC connectivity
direct VPC egress / connectors depending on configuration
private dependencies
```

Plan DNS and firewall carefully.

# Part 180 — Cloud Run Functions

Current Google Cloud terminology is **Cloud Run functions**.

They are lightweight event-driven functions integrated with the Cloud Run platform.

# Part 181 — Functions Framework

Functions use a language-specific Functions Framework.

Example Python HTTP function:

```python
def hello(request):
    return "hello"
```

# Part 182 — Eventarc

Routes events from Google Cloud/event sources to Cloud Run-based destinations.

Pattern:

```text
Cloud Storage event
 ↓
Eventarc
 ↓
Cloud Run / function
```

# Part 183 — Cloud Run Jobs

Use jobs for finite run-to-completion container workloads rather than HTTP services.

# Part 184 — Agent Runtime on Gemini Enterprise Agent Platform

The current Associate Cloud Engineer exam guide includes **Agent Runtime on Gemini Enterprise Agent Platform**, formerly Vertex AI Agent Engine.

At this stage, understand it as a managed runtime for deploying and operating AI agents, not as a replacement for general compute.

# Part 185 — Compute Selection Matrix

```text
VM control             → Compute Engine
Kubernetes             → GKE
serverless container   → Cloud Run
event function         → Cloud Run functions
batch container        → Cloud Run Jobs / Batch-style platform
AI agent runtime       → Gemini Enterprise Agent Platform runtime
```

Choose by execution model and operational needs.

# Part 186 — Cloud Storage

Object storage.

Use for:

```text
application objects
backups
logs
data lake
media
archives
```

# Part 187 — Buckets

Bucket has:

```text
name
location
storage configuration
IAM
retention
lifecycle
encryption
```

# Part 188 — Bucket Location

Location can be:

```text
region
dual-region
multi-region
```

depending on requirements and feature availability.

# Part 189 — Standard Storage

For frequently accessed data.

Lowest retrieval friction; higher storage rate than colder classes.

# Part 190 — Nearline

For infrequently accessed data.

Current classic model has a 30-day minimum storage duration.

# Part 191 — Coldline

For colder data.

Classic model has a 90-day minimum storage duration.

# Part 192 — Archive

For long-term rarely accessed data.

Classic model has a 365-day minimum storage duration.

Objects remain online-accessible; access/retrieval pricing applies.

# Part 193 — Autoclass

Automatically transitions objects between supported storage classes based on access.

Useful when access patterns are unpredictable.

# Part 194 — Lifecycle Management

Example:

```text
30d → Nearline
90d → Coldline
365d → Archive
7y → delete
```

Use with retention/compliance requirements.

# Part 195 — Object Versioning

Preserves prior object generations.

Useful for accidental overwrite/delete recovery.

# Part 196 — Soft Delete / Recovery Concepts

Cloud Storage includes protection features for recently deleted objects/buckets depending on current settings.

Plan them alongside versioning and retention.

# Part 197 — Retention Policy

Enforces minimum retention.

Use for:

```text
compliance
records
backup immutability
```

# Part 198 — Bucket Lock Concept

Locking retention policy makes retention enforcement difficult or impossible to reduce later.

Use only with approved compliance design.

# Part 199 — CMEK for Storage

Use Cloud KMS keys for supported customer-managed encryption.

Ensure service identities have key access.

# Part 200 — Storage IAM

Prefer uniform bucket-level access for simpler centralized IAM in many modern designs.

Avoid uncontrolled object ACL sprawl.

# Part 201 — Signed URLs

Temporarily grant object upload/download without proxying bytes through your application.

Use short expiry.

# Part 202 — gcloud storage

Modern CLI supports Cloud Storage operations.

Examples:

```bash
gcloud storage ls
gcloud storage cp ./file gs://BUCKET/
gcloud storage rsync ./data gs://BUCKET/data --recursive
```

# Part 203 — Storage Transfer Service

Managed data transfer from supported:

```text
on-prem
other clouds
other buckets
```

to/from Cloud Storage.

# Part 204 — Filestore

Managed NFS filesystem.

Use for shared filesystem semantics.

# Part 205 — Google Cloud NetApp Volumes

Managed enterprise file storage based on NetApp technology.

Use for enterprise NAS workloads requiring advanced file capabilities.

# Part 206 — Google Cloud Managed Lustre

Current Google Cloud high-performance parallel filesystem option for data-intensive/HPC/AI workloads.

Use when parallel high-throughput filesystem semantics are required.

# Part 207 — Storage Selection

```text
Object            → Cloud Storage
NFS file          → Filestore
Enterprise NAS    → NetApp Volumes
HPC parallel file → Managed Lustre
VM block          → Persistent Disk / Hyperdisk
```

# Part 208 — Cloud SQL

Managed relational databases for supported engines.

Use for traditional application SQL with reduced infrastructure administration.

# Part 209 — Cloud SQL HA

Regional HA configurations provide standby capacity across zones according to service behavior.

Use for production relational availability.

# Part 210 — Cloud SQL Backup

Configure:

```text
automated backups
PITR where supported
retention
on-demand backup
```

and test restore.

# Part 211 — Cloud SQL Read Replica

Use for:

```text
read scaling
reporting
DR/migration patterns
```

depending on engine.

# Part 212 — Cloud SQL Connectivity

Choices include:

```text
private IP
public IP with authorization
Cloud SQL connectors/auth proxy
```

Prefer private/identity-aware access where appropriate.

# Part 213 — AlloyDB

PostgreSQL-compatible managed relational platform optimized for high performance and cloud-native operation.

Use when PostgreSQL compatibility plus higher performance/scalability features are required.

# Part 214 — Spanner

Distributed relational database with horizontal scale and strong consistency.

Use for:

```text
large relational systems
regional/multi-region availability
high scale
```

# Part 215 — Firestore

Serverless document database.

Use for web/mobile/application document data and real-time-style application patterns.

# Part 216 — Bigtable

Wide-column NoSQL database.

Use for:

```text
time series
IoT
large key-based workloads
low-latency high throughput
```

# Part 217 — Memorystore

Managed in-memory caching/data store.

Use for:

```text
sessions
cache
low-latency hot data
```

# Part 218 — Database Center

Current Google Cloud guidance includes **Database Center** for central management/visibility across the Google Cloud database fleet.

Use for:

```text
inventory
health
security/posture
operational visibility
```

according to supported databases.

# Part 219 — Database Selection Matrix

```text
managed MySQL/Postgres/SQL Server → Cloud SQL
high-performance PostgreSQL       → AlloyDB
global scalable relational       → Spanner
document                          → Firestore
wide-column                       → Bigtable
cache                             → Memorystore
```

# Part 220 — BigQuery

Serverless analytics warehouse.

Use for:

```text
large SQL analytics
BI
data lake analytics
data science
```

# Part 221 — BigQuery Dataset Location

Dataset location matters.

Cross-location operations can fail or add architectural complexity.

Plan data geography intentionally.

# Part 222 — BigQuery Cost Control

Reduce scanned data:

```text
partition
cluster
select required columns
filter early
use appropriate materialization
```

# Part 223 — BigQuery Jobs

Monitor:

```text
running
completed
failed
bytes processed
slot behavior
```

through console/API.

# Part 224 — BigQuery ML

Supports building selected ML models with SQL.

Useful for analysts who already work in BigQuery.

# Part 225 — Pub/Sub

Managed asynchronous messaging.

```text
Publisher
 ↓ Topic
 ↓ Subscription
 ↓ Consumer
```

# Part 226 — Subscription Types Concept

Consumers can receive messages through:

```text
pull
push
export/BigQuery-style integrations where supported
```

depending on subscription configuration.

# Part 227 — Acknowledgement

Consumer acknowledges successfully processed messages.

Unacknowledged messages can be redelivered.

Consumers must be idempotent.

# Part 228 — Dead-Letter Topic

Repeatedly failed messages can be routed to a dead-letter path according to configuration.

Monitor and build replay/remediation process.

# Part 229 — Dataflow

Managed Apache Beam execution for:

```text
stream processing
batch pipelines
ETL
```

# Part 230 — Streaming Pipeline

Example:

```text
Factory Events
 ↓
Pub/Sub
 ↓
Dataflow
 ↓
BigQuery
```

# Part 231 — Managed Service for Apache Kafka

The current Associate Cloud Engineer guide includes **Google Cloud Managed Service for Apache Kafka**.

Use when the application requires Kafka APIs/ecosystem without self-managing Kafka infrastructure.

# Part 232 — Data Transfer / Loading

Loading methods include:

```text
CLI upload
Cloud Storage
Storage Transfer Service
streaming ingestion
database migration
```

Choose by size, latency, and source.

# Part 233 — Data Redundancy

For critical data decide:

```text
zonal
regional
dual-region
multi-region
backup copy
cross-region replica
```

by RPO/RTO and service capability.

# Part 234 — CMEK for Databases

For supported services, customer-managed keys add key-control requirements.

Check:

```text
service-agent permissions
key Region/location
rotation
restore
```

# Part 235 — Data Troubleshooting Model

Trace:

```text
service state
IAM
network
location
quota
capacity
schema/query
encryption key
backup
```

before changing data configuration.

# Part 236 — Google Cloud Observability

Core components:

```text
Cloud Monitoring
Cloud Logging
Cloud Trace
Cloud Profiler
Error Reporting
Managed Service for Prometheus
```

# Part 237 — Cloud Monitoring

Collects metrics and enables:

```text
dashboards
alerts
uptime checks
SLO monitoring
metrics scopes
```

# Part 238 — Metrics

Examples:

```text
VM CPU
load-balancer latency
Cloud Run request count
database connections
custom business metric
```

# Part 239 — Custom Metrics

Publish application-specific metrics:

```text
orders_failed
queue_depth
production_defects
```

when platform metrics do not express service health.

# Part 240 — Dashboards

A useful service dashboard includes:

```text
traffic
errors
latency
saturation
availability
dependencies
business KPI
```

# Part 241 — Alert Policies

Alert policy defines:

```text
resource
metric/query
condition
duration
notification
documentation
```

# Part 242 — Notification Channels

Route to:

```text
email
SMS
PagerDuty-style integrations
webhook
Pub/Sub
```

depending on current supported channels.

# Part 243 — Uptime Checks

External/internal synthetic checks can validate endpoint availability.

Use multiple failure signals, not uptime check alone.

# Part 244 — SLO Monitoring

Define:

```text
SLI
SLO
error budget
```

Example:

```text
99.9% successful requests
```

# Part 245 — Cloud Logging

Central log storage/query/routing.

Sources:

```text
Google Cloud services
VM agents
containers
applications
audit logs
```

# Part 246 — Log Buckets

Logs are stored in log buckets with configurable:

```text
retention
location
analytics
access
```

# Part 247 — Log Router

Routes log entries to:

```text
log bucket
BigQuery
Cloud Storage
Pub/Sub
external systems
```

via sinks.

# Part 248 — Log Sinks

Use for:

```text
central security logging
archive
SIEM
analytics
```

# Part 249 — Logs Explorer

Filter logs by resource and fields.

Example conceptual query:

```text
resource.type="gce_instance"
severity>=ERROR
```

# Part 250 — Log Analytics

Cloud Logging can provide SQL-style analytics capabilities over supported log buckets.

Useful for richer operational analysis.

# Part 251 — Ops Agent

Modern agent for Compute Engine guest telemetry.

Collects:

```text
logs
metrics
application telemetry integrations
```

according to config.

# Part 252 — Ops Agent Configuration

Define:

```text
receivers
processors
service pipelines
```

for logs/metrics.

Version-control agent configuration.

# Part 253 — Managed Service for Prometheus

Managed Prometheus-compatible metrics backend for Kubernetes/container monitoring.

Use for PromQL-based monitoring without managing Prometheus storage/control plane yourself.

# Part 254 — Cloud Trace

Distributed tracing helps locate request latency across services.

# Part 255 — Cloud Profiler

Continuous profiling identifies:

```text
CPU hotspots
memory behavior
performance bottlenecks
```

for supported runtimes.

# Part 256 — Error Reporting

Groups application errors/stack traces to identify new and recurring failures.

# Part 257 — Query Insights

Database diagnostic tool for supported Google Cloud databases.

Use to understand:

```text
slow queries
query load
database wait/bottleneck
```

# Part 258 — Personalized Service Health

Shows Google Cloud service incidents relevant to your resources/projects.

Check during platform-level incidents.

# Part 259 — Active Assist

Recommendation family for optimizing:

```text
cost
security
performance
sustainability
utilization
```

depending on recommender.

# Part 260 — Cloud Hub

Current Google Cloud operations guidance includes **Cloud Hub** for centralized visibility into active events and application/resource health data.

Treat it as an operations aggregation/visibility capability, not a replacement for detailed Monitoring/Logging.

# Part 261 — Cloud Monitoring with Gemini Cloud Assist

AI-assisted observability can help:

```text
write queries
interpret incidents
navigate telemetry
summarize resource context
```

Always verify proposed remediation.

# Part 262 — Backup Strategy

Backups must satisfy:

```text
RPO
RTO
retention
location
security
restore process
```

# Part 263 — Snapshots vs Backup

Snapshot:

```text
point-in-time storage copy
```

Backup strategy:

```text
retention + isolation + restore process + policy
```

A snapshot alone is not a complete DR strategy.

# Part 264 — Database Backups

Current ACE scope includes backup/restore for services such as:

```text
Cloud SQL
Firestore
Spanner
AlloyDB
Bigtable
```

according to service-specific capabilities.

# Part 265 — Restore Testing

Regularly test:

```text
restore
integrity
application connectivity
RTO
credentials
DNS
```

# Part 266 — DR Patterns

Use:

```text
backup/restore
regional standby
multi-region active/passive
multi-region active-active
```

based on requirements.

# Part 267 — RPO

Maximum tolerated data loss.

Example:

```text
RPO 15 minutes
```

# Part 268 — RTO

Maximum tolerated recovery duration.

Example:

```text
RTO 1 hour
```

# Part 269 — Cost Analysis

Investigate:

```text
billing account
project
service
SKU
Region
labels
time
```

to identify spikes.

# Part 270 — Idle Resource Detection

Common waste:

```text
idle VMs
unused disks
reserved external IPs
oversized databases
old snapshots
idle GKE nodes
excess logs
```

# Part 271 — Committed Use Discounts

Use commitments for stable predictable eligible usage.

Measure before committing.

# Part 272 — Spot Economics

Use Spot for interruptible workloads.

Design retry/requeue and diversification.

# Part 273 — Network Egress Cost

Model:

```text
Internet egress
inter-region
multicloud
CDN
hybrid
```

because networking can dominate application cost.

# Part 274 — Labels for FinOps

Require:

```text
owner
application
environment
cost_center
```

and monitor unlabeled spend.

# Part 275 — Operations Maturity

Mature operations includes:

```text
SLOs
alert quality
runbooks
postmortems
capacity planning
automation
cost ownership
security reviews
restore tests
```

# Part 276 — gcloud CLI

Primary administration CLI.

Examples:

```bash
gcloud auth list
gcloud config list
gcloud projects list
```

# Part 277 — Configurations

Create named gcloud configurations for environments:

```bash
gcloud config configurations create prod-admin
```

Avoid accidentally operating on the wrong project.

# Part 278 — Set Project

```bash
gcloud config set project PROJECT_ID
gcloud config get-value project
```

# Part 279 — Set Region and Zone

```bash
gcloud config set compute/region europe-west1
gcloud config set compute/zone europe-west1-b
```

Still specify explicitly in critical automation where ambiguity is risky.

# Part 280 — Compute Discovery

```bash
gcloud compute instances list
gcloud compute disks list
gcloud compute snapshots list
gcloud compute instance-groups managed list
```

# Part 281 — Network Discovery

```bash
gcloud compute networks list
gcloud compute networks subnets list
gcloud compute routes list
gcloud compute firewall-rules list
```

# Part 282 — IAM Discovery

```bash
gcloud projects get-iam-policy PROJECT_ID
```

Inspect inherited roles separately at folder/organization scope when needed.

# Part 283 — Storage Discovery

```bash
gcloud storage buckets list
gcloud storage ls gs://BUCKET
```

# Part 284 — GKE Discovery

```bash
gcloud container clusters list
gcloud container node-pools list --cluster CLUSTER --location REGION
```

# Part 285 — Cloud Run Discovery

```bash
gcloud run services list
gcloud run revisions list --service SERVICE --region REGION
```

# Part 286 — BigQuery CLI

`bq` provides BigQuery administration/query operations.

Examples:

```bash
bq ls
bq show PROJECT:DATASET
```

# Part 287 — kubectl

Kubernetes operational CLI:

```bash
kubectl get nodes
kubectl get pods -A
kubectl get svc -A
kubectl describe pod POD
kubectl logs POD
```

# Part 288 — Terraform

Declarative IaC:

```text
Git
 ↓
terraform plan
 ↓ review
terraform apply
 ↓
Google Cloud APIs
```

Secure remote state and separate environments.

# Part 289 — Config Connector

Allows managing Google Cloud resources through Kubernetes-style declarative resources.

Useful when Kubernetes is the control plane for infrastructure workflows.

# Part 290 — Helm

Package manager for Kubernetes applications.

Use for reusable parameterized GKE deployments.

# Part 291 — Fabric FAST

The current ACE exam guide includes **Fabric FAST** in the IaC/tooling category.

Treat it as a Google Cloud foundation/automation tooling concept; verify current documentation before production adoption because foundation tooling evolves rapidly.

# Part 292 — Gemini CLI

Current Google Cloud engineering materials include Gemini CLI as an AI-assisted development/operations tool.

Use for assistance, but retain:

```text
code review
change control
credential safety
verification
```

# Part 293 — Application Design Center

Current exam material includes Application Design Center for AI-assisted application/infrastructure planning.

At this phase, understand the use case:

```text
model application architecture
generate/assist deployment design
connect Google Cloud services
```

while verifying generated configuration.

# Part 294 — Google Antigravity Current-Exam Note

The current Associate Cloud Engineer guide includes **Google Antigravity** among AI-assisted planning/implementation tooling.

Because AI-assisted tooling changes rapidly, treat this as current-exam terminology and verify current product documentation before relying on it operationally.

# Part 295 — Infrastructure Change Safety

Before a change:

```text
identify project
review diff/plan
check blast radius
backup if necessary
schedule
apply
monitor
rollback if needed
```

# Part 296 — IAM Troubleshooting

For `PERMISSION_DENIED` check:

```text
active identity
project/resource
role binding
inheritance
service account
organization policy
IAM condition
VPC Service Controls
```

Do not grant Owner as first response.

# Part 297 — Network Troubleshooting

For unreachable service:

```text
DNS
route
firewall
NAT/VPN
load balancer
health
guest firewall
application
```

Use logs and connectivity tests.

# Part 298 — Compute / GKE / Run Troubleshooting

Compute Engine:

```text
boot
disk
network
IAM
startup
```

GKE:

```text
node
Pod
scheduler
image
service
network
IAM
```

Cloud Run:

```text
revision
container port
startup
IAM
ingress
VPC
dependency
```

# Part 299 — Data Troubleshooting

For data services check:

```text
location
IAM
network
service state
quota
capacity
encryption
query
backup
```

Differentiate permission, connectivity, and application errors.

# Part 300 — Google Cloud Platform Final Mental Model

Professional Google Cloud engineering means:

```text
build governed hierarchy
use identity instead of secrets
design global VPC deliberately
select managed services by workload
automate repeatable deployment
monitor real service health
protect and test recovery
understand cost
troubleshoot from evidence
```

The objective is not knowing the largest number of product names. It is operating cloud systems safely, predictably, and efficiently.

---

# Supplemental Deep-Study Layer — Google Cloud Platform

> **Source distinction:** The complete uploaded Course 56 remains preserved below. This layer adds deeper production engineering around hierarchy, short-lived identity, networking, GKE, Cloud Run, data services, messaging, observability, security, DR, IaC, FinOps, and troubleshooting. Certification logistics, product availability, quotas, pricing, preview/AI tooling, and exact service behavior can change; the certification baseline in the original source remains source-derived and should be checked against live Google Cloud documentation before production or exam decisions.

Study sequence:

```text
Concept
  ↓
Detailed explanation
  ↓
Diagram / mental model
  ↓
gcloud / kubectl / SQL / Terraform
  ↓
Expected evidence
  ↓
Production use
  ↓
Failure / troubleshooting
  ↓
Best practice
```


## Advanced Deep Dive 1 — gcloud Context Safety

### Concept

gcloud commands inherit account, project, region, and zone from the active configuration. Named configurations and explicit project checks reduce wrong-environment changes.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud auth list
gcloud config configurations list
gcloud config list
gcloud config get-value project
```

### Expected Evidence

The active identity and target project are unambiguous.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use named human configurations and explicit `--project` in critical automation.

---

## Advanced Deep Dive 2 — Organization and Folder Governance

### Concept

Folders define durable inheritance paths for IAM and organization policies. The hierarchy should reflect governance boundaries rather than temporary application naming.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud resource-manager folders list --organization=<ORG_ID>
```

### Expected Evidence

Projects sit under the intended governance branch.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Keep folder hierarchy stable, shallow, and control-oriented.

---

## Advanced Deep Dive 3 — Project as Blast-Radius Boundary

### Concept

Projects are major IAM, API, billing, quota, and operational boundaries. Project design influences how safely teams can delegate administration.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud projects list
gcloud projects describe <PROJECT_ID>
```

### Expected Evidence

Every project has a clear owner, purpose, billing relationship, and environment.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use projects deliberately for isolation and ownership.

---

## Advanced Deep Dive 4 — IAM Effective Access

### Concept

Google Cloud access can be inherited from organization/folder/project/resource policy, group membership, conditions, service-account impersonation, and deny controls.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud projects get-iam-policy <PROJECT_ID> --format=json
```

### Expected Evidence

The binding and scope responsible for access are identifiable.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Troubleshoot the hierarchy before granting broad roles.

---

## Advanced Deep Dive 5 — IAM Deny Guardrails

### Concept

Deny policies can prevent sensitive permissions even when an Allow role exists. They are powerful and should be applied only with clear exception and break-glass design.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Investigate:
allow bindings
deny policies
IAM conditions
organization policies
service perimeters
```

### Expected Evidence

Sensitive actions can be centrally blocked without removing every inherited allow.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use deny controls sparingly for high-impact permissions.

---

## Advanced Deep Dive 6 — Service Account Impersonation

### Concept

Humans and CI systems should prefer short-lived service-account impersonation over downloaded JSON keys.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud auth print-access-token   --impersonate-service-account=<SA_EMAIL> >/dev/null
```

### Expected Evidence

Temporary credentials are issued without distributing a private key.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Prefer impersonation for human and automation elevation.

---

## Advanced Deep Dive 7 — Workload Identity Federation

### Concept

External CI or workloads can exchange external identity for short-lived Google credentials. Trust should be restricted by issuer, audience, and workload attributes.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Validate:
issuer
audience
attribute mapping
attribute conditions
target service account
role scope
```

### Expected Evidence

External automation works without a long-lived Google service-account key.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Create separate federation trust for separate environments/repositories.

---

## Advanced Deep Dive 8 — Organization Policy

### Concept

Organization Policy constrains allowed resource configuration independently of IAM. A user may have permission to create a resource but still be blocked from an unsafe configuration.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud org-policies list --project=<PROJECT_ID> 2>/dev/null || true
```

### Expected Evidence

Production configuration restrictions are inherited and enforceable.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use organization policy for durable platform guardrails.

---

## Advanced Deep Dive 9 — Organization Policy Exceptions

### Concept

Policy exceptions should have a narrow scope, owner, business reason, compensating control, and expiry/review date.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Exception record:
constraint
scope
owner
reason
expiry
compensating control
review date
```

### Expected Evidence

Exceptions are visible and temporary rather than permanent hidden bypasses.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat exceptions as risk items with expiry.

---

## Advanced Deep Dive 10 — Cloud Asset Inventory

### Concept

Cloud Asset Inventory supports cross-resource search and policy/resource history, making it useful for inventory, security review, and incident investigation.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud asset search-all-resources   --scope=projects/<PROJECT_ID>   --format=table
```

### Expected Evidence

Authorized project resources are searchable centrally.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use Asset Inventory for fleet-level discovery and drift investigations.

---

## Advanced Deep Dive 11 — Billing Export to BigQuery

### Concept

Detailed billing export enables analysis by project, service, SKU, labels, credits, and time for FinOps and chargeback.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```sql
SELECT service.description, SUM(cost) AS cost
FROM `billing_export.gcp_billing_export_v1_*`
GROUP BY service.description
ORDER BY cost DESC;
```

### Expected Evidence

Cost can be tied to service and ownership dimensions.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Export billing data before you need historical FinOps analysis.

---

## Advanced Deep Dive 12 — Quota Headroom

### Concept

Autoscaling and disaster recovery can fail at project/region/service quotas. Quota headroom is a reliability concern.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute regions describe <REGION> --format=json
```

### Expected Evidence

Peak and DR capacity fit inside approved quotas.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Monitor quota headroom like any other capacity signal.

---

## Advanced Deep Dive 13 — API Enablement Governance

### Concept

Many Google Cloud services require APIs to be enabled. API enablement is also an attack and cost surface that should be controlled.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud services list --enabled
```

### Expected Evidence

Only required APIs are enabled for each project.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat service enablement as governed platform configuration.

---

## Advanced Deep Dive 14 — Shared VPC Administrative Separation

### Concept

Shared VPC lets a network host project own global network resources while service projects own application resources.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute shared-vpc get-host-project <SERVICE_PROJECT_ID> 2>/dev/null || true
```

### Expected Evidence

Application teams can consume assigned subnets without becoming network administrators.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Separate network ownership from application ownership.

---

## Advanced Deep Dive 15 — Global VPC / Regional Subnet Capacity

### Concept

Google Cloud VPC is global, but subnets are regional. Primary and GKE secondary ranges require centralized address planning.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute networks subnets list --format=table
```

### Expected Evidence

Primary/secondary ranges are non-overlapping and have growth headroom.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Plan VPC and GKE secondary ranges centrally.

---

## Advanced Deep Dive 16 — Hierarchical Firewall Policy

### Concept

Organization/folder-level firewall policies can enforce enterprise network controls above project-local rules.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Document:
policy scope
priority ranges
secure tags/service accounts
central baseline rules
delegated app rules
logging
```

### Expected Evidence

Central security controls cannot be silently bypassed by workload projects.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Reserve priority ranges and document central vs delegated ownership.

---

## Advanced Deep Dive 17 — Service-Account Targeted Firewall Rules

### Concept

Firewall rules can target workload service accounts, which can express application identity more reliably than changing VM IP addresses.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute firewall-rules list --format=json
```

### Expected Evidence

Firewall intent follows workload identity as VMs are replaced.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use stable workload identity for policy targeting where appropriate.

---

## Advanced Deep Dive 18 — Private Google Access

### Concept

Private VMs without external IPs can reach supported Google APIs through Private Google Access when subnet and DNS/routing are configured correctly.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute networks subnets describe <SUBNET>   --region=<REGION>   --format='value(privateIpGoogleAccess)'
```

### Expected Evidence

Private workloads reach required Google APIs without public VM addresses.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use Private Google Access for private-subnet API access where it fits.

---

## Advanced Deep Dive 19 — Private Service Connect

### Concept

Private Service Connect provides private endpoint/service attachment patterns for Google APIs, managed services, and producer services without broad VPC peering.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute forwarding-rules list --format=table
```

### Expected Evidence

Consumers reach the intended private service through an internal endpoint.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use PSC for private service consumption, not full network transit.

---

## Advanced Deep Dive 20 — Cloud NAT Capacity

### Concept

Cloud NAT removes the need for VM external IPs, but high outbound connection density can exhaust translation ports or NAT IP capacity.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute routers nats list   --router=<ROUTER> --region=<REGION> 2>/dev/null || true
```

### Expected Evidence

NAT has sufficient port/IP capacity for peak connections.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Monitor NAT connection pressure for large private fleets.

---

## Advanced Deep Dive 21 — Cloud Router Control Plane

### Concept

Cloud Router exchanges BGP routes but does not forward application packets. A healthy BGP session does not prove application connectivity.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute routers get-status <ROUTER>   --region=<REGION> --format=json
```

### Expected Evidence

BGP state and learned/advertised routes are visible.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Prove route exchange and packet forwarding separately.

---

## Advanced Deep Dive 22 — HA VPN Failure Domains

### Concept

HA VPN requires redundant tunnels/BGP sessions, but end-to-end availability also depends on independent customer routers, ISPs, and route design.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute vpn-tunnels list --format=table
gcloud compute routers get-status <ROUTER> --region=<REGION>
```

### Expected Evidence

Redundant paths are healthy and tested.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Test hybrid failover instead of trusting the diagram.

---

## Advanced Deep Dive 23 — Cloud Interconnect Resilience

### Concept

Interconnect is private high-capacity connectivity, but provider, edge, attachment, router, and route failures still need resilience and possibly VPN backup.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Validate:
attachment redundancy
BGP sessions
provider/edge diversity
bandwidth headroom
route preference
backup path
```

### Expected Evidence

Hybrid applications have a tested fallback aligned to RTO.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design end-to-end hybrid resilience, not just redundant cloud attachments.

---

## Advanced Deep Dive 24 — Cloud DNS Split-Horizon

### Concept

Public, private, and forwarding zones can return different answers to different clients. DNS authority must be documented by suffix and network.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud dns managed-zones list --format=table
```

### Expected Evidence

Internal and external clients resolve each namespace intentionally.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design DNS at the same time as network routing.

---

## Advanced Deep Dive 25 — Load Balancer Health Check Reachability

### Concept

Backends can be healthy at the application layer but marked unhealthy when health-check traffic is blocked by firewall or targets the wrong port/path.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute health-checks list --format=table
gcloud compute firewall-rules list --format=table
```

### Expected Evidence

Health checks reach the correct backend endpoint.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat health-check flows as explicit required network flows.

---

## Advanced Deep Dive 26 — Cloud Armor Policy Rollout

### Concept

WAF and rate rules can block legitimate users. New rules should be observed/tuned before broad enforcement where the service supports preview-style workflows.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute security-policies list --format=table
```

### Expected Evidence

Rule impact is understood before enforcement.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Roll complex WAF/rate policy progressively with log evidence.

---

## Advanced Deep Dive 27 — Cloud CDN Cache Key

### Concept

Cache reuse depends on which request attributes define the cache key. High-cardinality cookies, headers, or query strings can destroy cache efficiency.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Review:
path
query parameters
headers
cookies
TTL
Cache-Control
personalization
```

### Expected Evidence

Cacheable content gets high hit ratio without leaking personalized content.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Keep cache keys minimal and disable shared caching for sensitive responses.

---

## Advanced Deep Dive 28 — IAP TCP Forwarding

### Concept

IAP provides identity-aware administrative tunnels to private VMs, avoiding public SSH/RDP exposure.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute ssh <VM>   --zone=<ZONE>   --tunnel-through-iap
```

### Expected Evidence

Private VM administration works without an external IP.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Prefer identity-aware private administration over public management ports.

---

## Advanced Deep Dive 29 — OS Login

### Concept

OS Login links Linux SSH access to IAM identity and reduces unmanaged metadata SSH key sprawl.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute project-info describe   --format='yaml(commonInstanceMetadata)'
```

### Expected Evidence

SSH access follows centrally managed IAM eligibility.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use OS Login where supported for governed Compute Engine access.

---

## Advanced Deep Dive 30 — Golden Image Pipeline

### Concept

Compute Engine images should be immutable, versioned, tested, and traceable to source and hardening/patch state.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute images list --no-standard-images --format=table
```

### Expected Evidence

Production VMs map to an approved image build.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat VM images as versioned release artifacts.

---

## Advanced Deep Dive 31 — MIG Autohealing vs Autoscaling

### Concept

Autohealing replaces unhealthy instances; autoscaling changes fleet size because demand changed. They solve different problems.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute instance-groups managed list --format=table
```

### Expected Evidence

Health replacement and demand scaling are separately configured.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Do not use CPU autoscaling as a substitute for application health checks.

---

## Advanced Deep Dive 32 — MIG Rolling Update Capacity

### Concept

Rolling updates can require surge VMs, addresses, and quota. MaxSurge/MaxUnavailable should preserve service capacity within actual headroom.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute instance-groups managed describe <MIG>   --region=<REGION> --format=json
```

### Expected Evidence

The rollout strategy fits quota and preserves availability.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Capacity-plan the deployment overlap period.

---

## Advanced Deep Dive 33 — Spot VM Resilience

### Concept

Spot instances are interruptible. Work should be queued/checkpointed/idempotent so interruption loses only replaceable compute.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute instances list --format=table
```

### Expected Evidence

Spot loss reduces throughput temporarily but does not lose business state.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use Spot only for interruption-tolerant workload portions.

---

## Advanced Deep Dive 34 — Persistent Disk / Hyperdisk Performance

### Concept

Storage performance is limited by both disk configuration and VM I/O limits, plus filesystem and application access pattern.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud compute disks list --format=table
gcloud compute instances describe <VM> --zone=<ZONE> --format=json
```

### Expected Evidence

The bottleneck is identified as disk, machine, or application.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Evaluate disk and VM performance together.

---

## Advanced Deep Dive 35 — GKE Autopilot vs Standard

### Concept

Autopilot reduces node-management burden; Standard provides more host/node control. Choose from actual Kubernetes workload requirements.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud container clusters list --format=table
```

### Expected Evidence

Cluster mode is justified by concrete control requirements.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use the lowest operational complexity that satisfies Kubernetes needs.

---

## Advanced Deep Dive 36 — GKE Regional Availability

### Concept

A regional cluster control plane does not automatically spread application Pods. Replicas, topology spread, node pools, PDBs, and storage topology determine workload resilience.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl get nodes -L topology.kubernetes.io/zone
kubectl get pods -A -o wide
```

### Expected Evidence

Critical replicas are distributed across failure domains.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design workload topology explicitly.

---

## Advanced Deep Dive 37 — GKE Workload Identity Federation

### Concept

GKE workloads should access Google APIs through workload identity rather than service-account JSON keys mounted into Pods.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl get serviceaccount -A
gcloud iam service-accounts get-iam-policy <SA_EMAIL> 2>/dev/null || true
```

### Expected Evidence

Pods obtain short-lived credentials without embedded cloud private keys.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use a distinct workload identity per application capability.

---

## Advanced Deep Dive 38 — GKE Pod Pending Diagnosis

### Concept

Pending Pods often indicate scheduling constraints: resource requests, taints, selectors, PVC topology, IP exhaustion, quota, or autoscaler limits.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl describe pod <POD>
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get nodes
```

### Expected Evidence

Scheduler events reveal the unsatisfied constraint.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Read Kubernetes events before changing cluster-wide settings.

---

## Advanced Deep Dive 39 — GKE Image Pull Diagnosis

### Concept

ImagePullBackOff can be caused by wrong image name, Artifact Registry project/region, runtime identity, networking, or missing image digest.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl describe pod <POD>
gcloud artifacts docker images list <REGION>-docker.pkg.dev/<PROJECT>/<REPO>
```

### Expected Evidence

The image exists and the pulling identity is authorized.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Start with image reference and pulling identity evidence.

---

## Advanced Deep Dive 40 — GKE HPA + Cluster Autoscaler

### Concept

HPA adds Pods from workload metrics; cluster autoscaler adds nodes when Pods cannot schedule. Resource requests affect both systems.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl get hpa -A
kubectl top pods -A 2>/dev/null || true
kubectl top nodes 2>/dev/null || true
```

### Expected Evidence

Autoscaling converges without persistent Pending Pods or excess capacity.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Set realistic Pod requests because they are scheduling and scaling inputs.

---

## Advanced Deep Dive 41 — PodDisruptionBudget

### Concept

PDBs limit voluntary disruption but can block maintenance if configured more strictly than replica/capacity allows.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl get pdb -A
```

### Expected Evidence

Maintenance preserves required application replicas.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Derive PDB settings from real replica capacity and availability needs.

---

## Advanced Deep Dive 42 — GKE Network Policy

### Concept

Kubernetes network policy can restrict Pod-to-Pod flows inside a cluster, complementing VPC firewall controls.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl get networkpolicy -A
```

### Expected Evidence

Only intended east-west application paths are allowed.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use explicit workload flows and default-deny where operationally appropriate.

---

## Advanced Deep Dive 43 — GKE Ingress / Gateway Layers

### Concept

Kubernetes routing objects depend on Google load balancers, backend health, firewall, certificates, Services, and Pod readiness. Troubleshooting must cross both layers.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
kubectl get ingress -A
kubectl get gateway -A 2>/dev/null || true
kubectl get svc -A
```

### Expected Evidence

Kubernetes routing status and Google load-balancer health agree.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Troubleshoot Kubernetes and cloud load-balancer layers together.

---

## Advanced Deep Dive 44 — Cloud Run Revision Immutability

### Concept

Cloud Run revisions are immutable application/config snapshots. Traffic allocation should be controlled independently for fast rollback.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud run revisions list   --service=<SERVICE>   --region=<REGION>
```

### Expected Evidence

Every running revision maps to a known artifact/configuration.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Deploy immutable artifacts and shift traffic rather than rebuilding.

---

## Advanced Deep Dive 45 — Cloud Run Concurrency

### Concept

Concurrency trades instance count/cost against per-instance contention and downstream load. Maximum instances must protect databases and APIs.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud run services describe <SERVICE>   --region=<REGION> --format=json
```

### Expected Evidence

Concurrency and instance limits align with app and downstream capacity.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Benchmark concurrency and cap scale from dependency limits.

---

## Advanced Deep Dive 46 — Cloud Run VPC Egress

### Concept

Private dependency access changes routing, DNS, NAT, and API connectivity. VPC egress must be designed as a full network path.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud run services describe <SERVICE>   --region=<REGION>   --format='yaml(spec.template.metadata,spec.template.spec)'
```

### Expected Evidence

Cloud Run reaches private resources without unintentionally losing needed Internet/API connectivity.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design serverless egress paths before enabling private connectivity.

---

## Advanced Deep Dive 47 — Cloud Run Service-to-Service Auth

### Concept

Private Cloud Run services should require authenticated callers using workload identity and identity tokens with the correct audience.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud run services get-iam-policy <SERVICE> --region=<REGION>
```

### Expected Evidence

Only approved service identities can invoke the service.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use workload identity instead of shared application secrets.

---

## Advanced Deep Dive 48 — Cloud Run Minimum Instances

### Concept

Minimum instances reduce cold starts but add idle cost. Use them only where latency SLOs justify prewarming.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud run services describe <SERVICE> --region=<REGION> --format=json
```

### Expected Evidence

Prewarmed capacity is tied to a measured latency requirement.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Pay for warm capacity only when the SLO requires it.

---

## Advanced Deep Dive 49 — Cloud Run Jobs vs Services

### Concept

Cloud Run services are request-serving; Cloud Run Jobs are finite run-to-completion workloads. Use the execution model that matches the job.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud run jobs list --region=<REGION> 2>/dev/null || true
```

### Expected Evidence

Batch work does not depend on a long-lived HTTP request.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Choose Service vs Job from workload lifecycle.

---

## Advanced Deep Dive 50 — Eventarc Idempotency

### Concept

Event handlers should validate event source/schema and be safe under retry or duplicate delivery.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Log:
event ID
event type
source
resource/subject
schema version
processing result
```

### Expected Evidence

Repeated events do not create duplicate business effects.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design every event handler to be idempotent.

---

## Advanced Deep Dive 51 — Artifact Registry Provenance

### Concept

Production artifacts should map to source commit, build, scan/test, and immutable digest. Rebuilding for production destroys staging equivalence.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud artifacts docker images list   <REGION>-docker.pkg.dev/<PROJECT>/<REPO>   --include-tags
```

### Expected Evidence

Running workloads can be traced to one immutable digest.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Build once and promote the same digest.

---

## Advanced Deep Dive 52 — Artifact Cleanup and Rollback

### Concept

Registry cleanup should remove unneeded artifacts while retaining production and rollback releases.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Define:
protected release digests
minimum age
minimum versions
untagged build retention
rollback window
```

### Expected Evidence

Old artifacts expire without deleting the last known-good release.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Tie artifact retention to the rollback/support window.

---

## Advanced Deep Dive 53 — Cloud Storage Uniform Bucket-Level Access

### Concept

Uniform bucket-level access centralizes authorization in IAM and avoids object ACL sprawl.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud storage buckets describe gs://<BUCKET> --format=json
```

### Expected Evidence

Object access is governed by a clear bucket/project IAM model.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Prefer one consistent authorization model.

---

## Advanced Deep Dive 54 — Cloud Storage Protection Layers

### Concept

Versioning, soft-delete-style recovery, and retention policies protect against different loss/compliance scenarios.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud storage buckets describe gs://<BUCKET> --format=json
```

### Expected Evidence

Protection settings match accidental loss, ransomware, and retention requirements.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Choose protection layers from the data threat model.

---

## Advanced Deep Dive 55 — Signed URL Security

### Concept

Signed URLs delegate temporary object access. The app must authorize object key, method, expiry, and user before signing.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Guardrails:
specific object
specific HTTP method
short expiry
HTTPS
tenant prefix
post-upload validation
```

### Expected Evidence

Clients transfer data without broad bucket credentials.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat signed URLs as temporary credentials.

---

## Advanced Deep Dive 56 — Cloud Storage CMEK

### Concept

Customer-managed encryption keys add control and dependency on KMS key state, location, IAM, and service-agent permissions.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud kms keys list --keyring=<RING> --location=<LOCATION>
```

### Expected Evidence

Encrypted objects remain usable through normal operations and recovery.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat KMS as an availability dependency.

---

## Advanced Deep Dive 57 — Cloud SQL Private Connectivity

### Concept

Private Cloud SQL connectivity requires network path plus database/IAM authentication. Correct private IP does not prove the database credentials or connection limits are valid.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud sql instances describe <INSTANCE> --format=json
```

### Expected Evidence

The application reaches Cloud SQL privately and authenticates correctly.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Troubleshoot network and DB authorization separately.

---

## Advanced Deep Dive 58 — Cloud SQL Connection Pooling

### Concept

Autoscaling Cloud Run/GKE can create more database connections than Cloud SQL can handle. Pool size times maximum replicas is the relevant capacity.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```python
instances = 50
pool_per_instance = 10
print("Potential DB connections:", instances * pool_per_instance)
```

### Expected Evidence

Maximum application scale stays below safe DB connection capacity.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Capacity-plan total connections across maximum compute scale.

---

## Advanced Deep Dive 59 — Cloud SQL HA vs Read Replica

### Concept

High availability and read scaling are different requirements. Regional HA protects availability; replicas primarily serve reads and selected DR/migration use.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud sql instances list --format=table
```

### Expected Evidence

The topology maps separately to HA and read-scaling needs.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Write separate availability and read-scale requirements.

---

## Advanced Deep Dive 60 — Cloud SQL PITR

### Concept

HA replicates bad writes. Point-in-time recovery protects against logical corruption such as accidental DELETE or destructive application migration.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud sql instances describe <INSTANCE> --format=json
```

### Expected Evidence

The recovery plan can restore to a time before corruption.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design logical-corruption recovery separately from infrastructure HA.

---

## Advanced Deep Dive 61 — Spanner Global Placement

### Concept

Spanner offers distributed strongly consistent relational capabilities, but latency, replica/leader placement, residency, and cost must match business geography.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud spanner instances list --format=table 2>/dev/null || true
```

### Expected Evidence

Instance configuration is justified by write locality, latency, availability, and residency.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use multi-region relational design only when requirements justify its complexity.

---

## Advanced Deep Dive 62 — Firestore Hotspot Avoidance

### Concept

Concentrated document/key patterns can create hotspots. Document IDs, indexes, transaction contention, and write distribution are part of data modeling.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Review:
document ID strategy
write concentration
index count
transaction retries
query patterns
```

### Expected Evidence

High-volume writes are distributed rather than concentrated.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design document keys from traffic and query patterns.

---

## Advanced Deep Dive 63 — Bigtable Row-Key Design

### Concept

Bigtable rows are ordered lexicographically. Sequential timestamp-first keys can hotspot one range; row keys should balance distribution with scan locality.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Bad:
20260820T101500#device123

Better:
07#device123#20260820T101500
```

### Expected Evidence

Writes distribute across key ranges while important scans remain efficient.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design row keys from write distribution and read locality.

---

## Advanced Deep Dive 64 — Memorystore Cache Stampede

### Concept

When a popular key expires, many clients can miss simultaneously and overload the database. TTL jitter and coordinated refresh reduce stampedes.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Use:
TTL jitter
single-flight refresh
stale-while-revalidate
prewarming
backend rate limits
```

### Expected Evidence

Popular-key expiry does not create a synchronized backend spike.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design cache-miss behavior, not only cache-hit behavior.

---

## Advanced Deep Dive 65 — Pub/Sub Ack Deadline and Idempotency

### Concept

Messages can be redelivered when processing fails or exceeds acknowledgement behavior. Consumers must acknowledge only after durable success and remain duplicate-safe.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud pubsub subscriptions describe <SUBSCRIPTION>
```

### Expected Evidence

Retries do not create duplicate business effects.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Make consumers idempotent and acknowledge after durable completion.

---

## Advanced Deep Dive 66 — Pub/Sub Dead-Letter Operations

### Concept

A dead-letter topic needs monitoring, diagnosis, retention, fix, and controlled replay; it is not a permanent dumping ground.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud pubsub subscriptions describe <SUBSCRIPTION> --format=json
```

### Expected Evidence

Poison messages leave the main path and trigger actionable investigation.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Alert on dead-letter growth for critical workflows.

---

## Advanced Deep Dive 67 — Pub/Sub Ordering Keys

### Concept

Ordering should be scoped to the smallest entity requiring order. One global ordering key can serialize the entire stream.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Order by:
aggregate/entity ID
not one universal key
```

### Expected Evidence

Related events stay ordered while unrelated entities process in parallel.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use the narrowest ordering domain possible.

---

## Advanced Deep Dive 68 — Dataflow Backpressure

### Concept

Streaming health is determined by end-to-end lag and slowest stage/downstream dependency, not just worker CPU.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Monitor:
input throughput
system lag
stage latency
worker utilization
errors/retries
sink quota/latency
```

### Expected Evidence

Pipeline freshness remains inside the business target.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Alert on data lag/freshness rather than only worker utilization.

---

## Advanced Deep Dive 69 — BigQuery Partition / Cluster Cost Control

### Concept

BigQuery scans fewer bytes when queries use partition filters, clustering, and selected columns rather than `SELECT *`.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```sql
SELECT event_type, COUNT(*) AS n
FROM `project.dataset.events`
WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY event_type;
```

### Expected Evidence

Queries scan only relevant data.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design analytical storage around common predicates and lifecycle.

---

## Advanced Deep Dive 70 — BigQuery Location

### Concept

Datasets and jobs have location constraints. Cross-location analytics requires explicit architecture rather than assuming global transparency.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
bq show --format=prettyjson <PROJECT>:<DATASET> | grep -i location
```

### Expected Evidence

Related workloads and datasets are intentionally located.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Decide analytics data geography before ingestion.

---

## Advanced Deep Dive 71 — BigQuery Workload Isolation

### Concept

Interactive BI, ETL, ad hoc, and ML workloads can compete for analytical capacity. Workload isolation/reservation strategy may be needed at scale.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Classify:
interactive BI
ETL
ad hoc
ML
critical dashboards
```

### Expected Evidence

Critical analytical workloads stay responsive during heavy batch work.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use workload isolation when contention becomes a business problem.

---

## Advanced Deep Dive 72 — Cloud Logging Central Sinks

### Concept

Organization/folder/project sinks can route logs into a protected central logging/security project. Sink writer identity must have destination permission.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud logging sinks list
```

### Expected Evidence

Critical audit/security logs reach a central protected destination.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Separate security-log administration from workload administration.

---

## Advanced Deep Dive 73 — Log Exclusions and Cost

### Concept

High-volume low-value logs can dominate observability cost. Exclusions/retention should be intentional and must not remove security or incident evidence.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud logging sinks list
gcloud logging exclusions list 2>/dev/null || true
```

### Expected Evidence

Logging volume and retention align with operational value.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Reduce noise only after confirming the logs are not required for security or recovery.

---

## Advanced Deep Dive 74 — Metrics Scope and Central Operations

### Concept

Cross-project monitoring should centralize visibility without flattening project boundaries.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Design:
operations scoping project
monitored projects
dashboard ownership
alert ownership
least-privilege viewers
```

### Expected Evidence

SRE can view service health across projects without broad write permission.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Centralize observability views while preserving project isolation.

---

## Advanced Deep Dive 75 — SLI / SLO / Error Budget

### Concept

A service should define user-facing success and latency indicators, target SLO, and error budget so reliability becomes measurable.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
SLI = successful valid requests / valid requests
SLO = 99.9% over 30 days
Latency = p95 < 500 ms
```

### Expected Evidence

Monitoring can state whether the service meets its reliability target.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use SLOs to connect architecture, alerts, and release risk.

---

## Advanced Deep Dive 76 — Ops Agent as Code

### Concept

Guest telemetry collection should be versioned and standardized through Ops Agent configuration rather than one-off manual setup.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```yaml
logging:
  receivers:
    app:
      type: files
      include_paths:
        - /var/log/myapp/*.log
```

### Expected Evidence

VM telemetry is reproducible across replacements.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Version and test agent configuration.

---

## Advanced Deep Dive 77 — Audit Log Investigation

### Concept

Cloud Audit Logs provide structured principal, method, resource, request, and result evidence for administrative and selected data access events.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Logs Explorer filter:
logName:"cloudaudit.googleapis.com"
protoPayload.authenticationInfo.principalEmail="<PRINCIPAL>"
```

### Expected Evidence

Suspicious changes can be attributed to a principal/API method.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Centralize and protect audit logs before incidents.

---

## Advanced Deep Dive 78 — Security Command Center Triage

### Concept

Security findings should be prioritized using exposure, exploitability, business criticality, data sensitivity, and owner—not severity alone.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Triage:
asset/project
finding category
Internet exposure
privilege/data sensitivity
exploitability
owner
remediation SLA
```

### Expected Evidence

High-risk findings become owned remediation work.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Prioritize findings from contextual risk.

---

## Advanced Deep Dive 79 — VPC Service Controls

### Concept

VPC Service Controls add service-perimeter checks around supported Google APIs to reduce data exfiltration. They complement IAM rather than replacing it.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Troubleshoot:
source project
target project/service
perimeter membership
ingress/egress policy
access context
Policy Denied logs
```

### Expected Evidence

Sensitive data APIs reject requests from unauthorized contexts.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use VPC-SC for high-value data perimeters with tested workflows.

---

## Advanced Deep Dive 80 — Cloud KMS Lifecycle

### Concept

CMEK introduces dependence on key state, location, IAM, service-agent permissions, rotation, and deletion.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud kms keys list --keyring=<RING> --location=<LOCATION>
gcloud kms keys versions list <KEY> --keyring=<RING> --location=<LOCATION>
```

### Expected Evidence

Key users and administrators are separated and recovery is tested.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Inventory key dependencies before destructive key changes.

---

## Advanced Deep Dive 81 — Secret Manager Rotation

### Concept

Secret rotation is a distributed change. Create a new version, update the provider/consumer, verify refresh, then retire the old version safely.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud secrets versions list <SECRET>
```

### Expected Evidence

Long-running workloads adopt new secret versions without outage.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design consumer refresh behavior before automating rotation.

---

## Advanced Deep Dive 82 — Database Restore Testing

### Concept

Backup success is not recovery success. Restore drills must validate IAM, KMS, network, DNS, credentials, application schema, data integrity, and RTO.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Restore evidence:
recovery point
start/end time
target project/region
KMS
network
data validation
business transaction
```

### Expected Evidence

A test restore reaches a successful application transaction.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Make restore success and actual recovery time operational KPIs.

---

## Advanced Deep Dive 83 — RPO

### Concept

RPO is the maximum tolerated data-loss interval and depends on backup frequency, PITR, replication lag, and application consistency.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
For each data store:
RPO target
backup interval
PITR window
replication lag
last tested restore point
```

### Expected Evidence

The latest recoverable state is within the business target.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Measure recoverability against business RPO.

---

## Advanced Deep Dive 84 — RTO

### Concept

RTO includes detection, declaration, failover/restore, provisioning, routing/DNS, application startup, key/secret access, and validation.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```python
steps = {"detect":5,"declare":5,"restore":20,"network":5,"validate":10}
print("RTO minutes:", sum(steps.values()))
```

### Expected Evidence

Each recovery phase has a measured duration.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Measure RTO from outage start to successful business transaction.

---

## Advanced Deep Dive 85 — Multi-Region DR Dependency Inventory

### Concept

A recovery region is incomplete if it lacks artifacts, IAM, KMS, secrets, APIs, quotas, network, DNS, certificates, monitoring, or external integration configuration.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
DR bill of materials:
projects/APIs
network
artifacts
IAM/service accounts
KMS/secrets
database/object data
DNS/load balancing
quota
monitoring
runbooks
```

### Expected Evidence

A game day proves the full workload can run in DR.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Maintain and test a complete DR dependency inventory.

---

## Advanced Deep Dive 86 — Failback

### Concept

Failback requires resynchronizing data, preventing split-brain writes, validating original-region capacity and versions, then shifting traffic safely.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Failback:
current write owner
replication direction
data reconciliation
version parity
traffic shift
rollback
```

### Expected Evidence

Data created during the DR period is preserved.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design failback separately from failover.

---

## Advanced Deep Dive 87 — Cloud Build Least Privilege

### Concept

Build identities should have build/push/deploy permissions separate from runtime identities that access business data.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud builds list --limit=20 2>/dev/null || true
gcloud projects get-iam-policy <PROJECT_ID> --format=json
```

### Expected Evidence

CI/CD and runtime privileges are distinct.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Separate build/deploy identity from application runtime identity.

---

## Advanced Deep Dive 88 — Progressive Delivery

### Concept

Production releases should promote the same immutable artifact through environments with approval and verification gates.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Release:
artifact digest
source commit
target
approval
verification result
rollback release
```

### Expected Evidence

Production uses the artifact that passed staging.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Build once, promote immutably, and gate rollout by evidence.

---

## Advanced Deep Dive 89 — Binary Authorization / Supply Chain Policy

### Concept

Runtime admission can require trusted/attested container images, reducing deployment of artifacts that bypass approved build and security processes.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Policy:
trusted build identity
required attestation
environment scope
break-glass
audit
```

### Expected Evidence

Protected workloads deploy only approved artifacts.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use supply-chain admission controls for high-value environments with audited break-glass.

---

## Advanced Deep Dive 90 — Artifact Vulnerability Triage

### Concept

Image vulnerability scanning is most useful when findings feed build/release decisions using exploitability, exposure, runtime use, and fix availability.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Triage:
package/CVE
severity
known exploit
runtime reachable?
fixed version
running digest
```

### Expected Evidence

Critical exploitable image findings do not silently reach production.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Connect scanning results to immutable artifact provenance.

---

## Advanced Deep Dive 91 — Terraform State Security

### Concept

Terraform state is authoritative infrastructure metadata and can contain sensitive outputs. Remote state needs restricted IAM, environment separation, recovery/versioning, and concurrency control.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
State controls:
dedicated bucket/project
uniform IAM
versioning/retention
no public access
CI-only write
environment separation
```

### Expected Evidence

Only approved automation/operators can read or modify production state.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Protect Terraform state as production configuration.

---

## Advanced Deep Dive 92 — Terraform Plan / Drift

### Concept

A Terraform plan should be reviewed for replacement, deletion, IAM/network changes, and unexpected drift before apply.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
terraform plan
```

### Expected Evidence

High-risk changes and drift are visible before execution.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Treat plan review as a production change gate.

---

## Advanced Deep Dive 93 — Centralized Hybrid DNS

### Concept

Hybrid environments need a DNS architecture beside network routing: suffix authority, forwarding direction, split horizon, VPC visibility, TTL, and DR behavior.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
DNS table:
suffix
authority
forward-from
forward-to
VPC visibility
TTL
DR behavior
```

### Expected Evidence

Names resolve consistently from every intended environment.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design DNS at the same time as hybrid routing.

---

## Advanced Deep Dive 94 — Connectivity Tests

### Concept

Configuration-level connectivity analysis can identify route/firewall/load-balancer problems before broad changes or packet capture.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Use Connectivity Tests / Network Intelligence tooling for supported source-destination paths.
```

### Expected Evidence

The network configuration layer is identified as reachable or blocked.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Use configuration-path evidence before changing firewalls.

---

## Advanced Deep Dive 95 — VPC Flow Logs vs Packet Data

### Concept

Flow logs show network metadata, not HTTP/TLS payload. They help prove source/destination/port/volume, then investigation should move to protocol/application evidence when needed.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Flow logs answer:
who talks to whom
port/protocol
volume
flow pattern

They do not show application payload.
```

### Expected Evidence

Operators choose the correct evidence source for the layer.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Do not expect flow logs to explain application-layer errors.

---

## Advanced Deep Dive 96 — Prometheus Label Cardinality

### Concept

Unbounded labels such as request IDs, user IDs, and raw URLs create huge time-series cardinality, increasing cost and query complexity.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Good labels:
service
region
status
route template

Avoid:
request_id
user_id
UUID
full dynamic URL
```

### Expected Evidence

Metric series remain bounded and operationally meaningful.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Put high-cardinality identifiers in logs/traces, not metric labels.

---

## Advanced Deep Dive 97 — Trace Context Across Async Work

### Concept

Async Pub/Sub/Dataflow/worker boundaries need explicit correlation/event IDs so one business operation can be followed across independent services.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Propagate:
trace ID if supported
request/correlation ID
event ID
tenant/aggregate ID
deployment version
```

### Expected Evidence

One business transaction can be reconstructed through synchronous and async stages.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Create correlation context at ingress and propagate it everywhere.

---

## Advanced Deep Dive 98 — Cost per Business Transaction

### Concept

Cloud spend should be normalized by business output such as cost per order, user, report, or GB processed.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```python
monthly_cost = 38000
orders = 500000
print("Cost per order:", monthly_cost / orders)
```

### Expected Evidence

Teams can distinguish healthy business growth from inefficient spending.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Track business-aligned unit cost, not only total bill.

---

## Advanced Deep Dive 99 — Network Egress Economics

### Concept

Internet, inter-region, hybrid, and multicloud data transfer can dominate cost. Place compute near data and avoid unnecessary cross-boundary movement.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
For each high-volume flow:
source location
destination location
GB/day
reason
can processing/cache move closer?
```

### Expected Evidence

High-volume data movement is intentional and costed.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Design data locality and egress before scale makes it expensive.

---

## Advanced Deep Dive 100 — Cloud Run / GKE / Compute Selection

### Concept

The best platform is the least operationally complex option that still satisfies runtime, control, networking, scaling, storage, and portability requirements.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
VM/OS control → Compute Engine/MIG
Kubernetes API/operator → GKE
serverless HTTP container → Cloud Run
event function → Cloud Run functions
finite batch → Cloud Run Jobs
```

### Expected Evidence

Platform choice is traceable to hard requirements.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Do not choose Kubernetes merely because the workload uses containers.

---

## Advanced Deep Dive 101 — Retry Storm Prevention

### Concept

Immediate retries from thousands of workers can amplify a throttled service. Use bounded retries, exponential backoff, jitter, idempotency, and backpressure.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```python
import random
for attempt in range(5):
    delay = min(30, 2 ** attempt) + random.random()
    print(round(delay, 2))
```

### Expected Evidence

Transient faults recover without synchronized retry spikes.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Retry only transient failures and cap total retry time.

---

## Advanced Deep Dive 102 — Circuit Breaker and Graceful Degradation

### Concept

Optional dependency failure should not consume the entire application. Circuit breakers fail fast and allow fallback while testing recovery.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
CLOSED → normal calls
failures exceed threshold
OPEN → fail fast/fallback
after timeout
HALF-OPEN → test recovery
```

### Expected Evidence

Core application remains responsive during optional dependency outage.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Classify dependencies as critical versus optional and design fallbacks.

---

## Advanced Deep Dive 103 — Bulkhead Isolation

### Concept

Separate queues, services, concurrency limits, projects, or quotas keep one workload or tenant from consuming all shared capacity.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Isolate:
customer API
report workers
email workers
tenant quotas
database pools
projects
```

### Expected Evidence

Noncritical overload cannot starve critical business paths.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Partition scarce capacity by business criticality.

---

## Advanced Deep Dive 104 — SLO-Based Release Gate

### Concept

A canary should promote only when error, latency, business success, dependency health, and security signals remain within predefined thresholds.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
Rollback if:
5xx > 2x baseline
p95 latency > 20% baseline
business success < SLO
critical security finding
```

### Expected Evidence

Traffic expansion is evidence-driven and reversible.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Define canary success and rollback criteria before rollout.

---

## Advanced Deep Dive 105 — Architecture Decision Records

### Concept

High-impact cloud decisions should record context, alternatives, security/reliability/cost implications, operational burden, and revisit triggers.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
ADR:
Context
Decision
Alternatives
Security
Reliability
Cost
Operations
Migration/exit
Revisit trigger
```

### Expected Evidence

Future teams understand why the architecture exists.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Document difficult-to-reverse decisions and their exit criteria.

---

## Advanced Deep Dive 106 — Operational Readiness Review

### Concept

A critical service should have ownership, SLO, alerts, logs/traces, backup/restore, quota, IAM/secrets/KMS, rollback, cost controls, and runbooks before launch.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```text
[ ] owner/on-call
[ ] SLO + alerts
[ ] logs/traces
[ ] backup + restore test
[ ] quota/headroom
[ ] deployment rollback
[ ] IAM/secrets/KMS
[ ] DR inventory
[ ] budget/labels
```

### Expected Evidence

The team can operate and recover the service before customers depend on it.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Make operational readiness a launch gate.

---

## Advanced Deep Dive 107 — Evidence-First Troubleshooting

### Concept

Use a stable order: identity/context, IAM/policy/API enabled, DNS, routes/firewalls/NAT, platform health, application, data/KMS, quota, recent changes, provider health.

### Architecture / Mental Model

```text
Requirement
   ↓
Google Cloud control / service
   ↓
Identity + Resource Hierarchy
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Observability Evidence
```

### CLI / YAML / SQL / kubectl / Terraform

```bash
gcloud auth list
gcloud config list
gcloud services list --enabled
gcloud logging read 'severity>=ERROR' --limit=20 2>/dev/null || true
```

### Expected Evidence

The failing layer is found before broad remediation.

### Why It Works

Google Cloud separates resource hierarchy, IAM, control-plane APIs, global networking, regional/zonal execution, managed-service data planes, and observability. A resource existing in the control plane does not prove that the application data path, credentials, quota, or recovery behavior is correct.

### Production Example

Apply this topic by documenting the requirement, project/folder scope, principal/service account, network path, expected telemetry, failure mode, owner, rollback/recovery procedure, and cost/security implications.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify account + project
  ↓
Inspect IAM / Org Policy / API enablement
  ↓
Resolve DNS
  ↓
Inspect routes / firewall / NAT / VPN
  ↓
Inspect platform health
  ↓
Inspect application / Kubernetes / data service
  ↓
Inspect Audit Logs / Monitoring / Logging
  ↓
Check quota / KMS / recent changes
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Fixing `PERMISSION_DENIED` by granting Owner.
- Assigning public IPs to bypass private connectivity problems.
- Assuming a healthy managed control plane means the application is healthy.
- Ignoring project context, enabled APIs, quota, secondary IP ranges, or KMS.
- Changing multiple layers before preserving evidence.
- Treating snapshots or replication as a complete DR plan.

### Best Practice

Preserve evidence and change one layer at a time.

---

# Supplemental Hands-on Lab Series — Google Cloud Platform

## Enhanced Lab 1 — gcloud Context Safety

### Objective

Turn **gcloud Context Safety** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud auth list
gcloud config configurations list
gcloud config list
gcloud config get-value project
```

### Expected Result

The active identity and target project are unambiguous.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use named human configurations and explicit `--project` in critical automation.

---

## Enhanced Lab 2 — Organization and Folder Governance

### Objective

Turn **Organization and Folder Governance** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud resource-manager folders list --organization=<ORG_ID>
```

### Expected Result

Projects sit under the intended governance branch.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Keep folder hierarchy stable, shallow, and control-oriented.

---

## Enhanced Lab 3 — Project as Blast-Radius Boundary

### Objective

Turn **Project as Blast-Radius Boundary** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud projects list
gcloud projects describe <PROJECT_ID>
```

### Expected Result

Every project has a clear owner, purpose, billing relationship, and environment.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use projects deliberately for isolation and ownership.

---

## Enhanced Lab 4 — IAM Effective Access

### Objective

Turn **IAM Effective Access** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud projects get-iam-policy <PROJECT_ID> --format=json
```

### Expected Result

The binding and scope responsible for access are identifiable.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Troubleshoot the hierarchy before granting broad roles.

---

## Enhanced Lab 5 — IAM Deny Guardrails

### Objective

Turn **IAM Deny Guardrails** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Investigate:
allow bindings
deny policies
IAM conditions
organization policies
service perimeters
```

### Expected Result

Sensitive actions can be centrally blocked without removing every inherited allow.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use deny controls sparingly for high-impact permissions.

---

## Enhanced Lab 6 — Service Account Impersonation

### Objective

Turn **Service Account Impersonation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud auth print-access-token   --impersonate-service-account=<SA_EMAIL> >/dev/null
```

### Expected Result

Temporary credentials are issued without distributing a private key.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prefer impersonation for human and automation elevation.

---

## Enhanced Lab 7 — Workload Identity Federation

### Objective

Turn **Workload Identity Federation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Validate:
issuer
audience
attribute mapping
attribute conditions
target service account
role scope
```

### Expected Result

External automation works without a long-lived Google service-account key.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Create separate federation trust for separate environments/repositories.

---

## Enhanced Lab 8 — Organization Policy

### Objective

Turn **Organization Policy** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud org-policies list --project=<PROJECT_ID> 2>/dev/null || true
```

### Expected Result

Production configuration restrictions are inherited and enforceable.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use organization policy for durable platform guardrails.

---

## Enhanced Lab 9 — Organization Policy Exceptions

### Objective

Turn **Organization Policy Exceptions** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Exception record:
constraint
scope
owner
reason
expiry
compensating control
review date
```

### Expected Result

Exceptions are visible and temporary rather than permanent hidden bypasses.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat exceptions as risk items with expiry.

---

## Enhanced Lab 10 — Cloud Asset Inventory

### Objective

Turn **Cloud Asset Inventory** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud asset search-all-resources   --scope=projects/<PROJECT_ID>   --format=table
```

### Expected Result

Authorized project resources are searchable centrally.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use Asset Inventory for fleet-level discovery and drift investigations.

---

## Enhanced Lab 11 — Billing Export to BigQuery

### Objective

Turn **Billing Export to BigQuery** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```sql
SELECT service.description, SUM(cost) AS cost
FROM `billing_export.gcp_billing_export_v1_*`
GROUP BY service.description
ORDER BY cost DESC;
```

### Expected Result

Cost can be tied to service and ownership dimensions.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Export billing data before you need historical FinOps analysis.

---

## Enhanced Lab 12 — Quota Headroom

### Objective

Turn **Quota Headroom** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute regions describe <REGION> --format=json
```

### Expected Result

Peak and DR capacity fit inside approved quotas.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Monitor quota headroom like any other capacity signal.

---

## Enhanced Lab 13 — API Enablement Governance

### Objective

Turn **API Enablement Governance** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud services list --enabled
```

### Expected Result

Only required APIs are enabled for each project.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat service enablement as governed platform configuration.

---

## Enhanced Lab 14 — Shared VPC Administrative Separation

### Objective

Turn **Shared VPC Administrative Separation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute shared-vpc get-host-project <SERVICE_PROJECT_ID> 2>/dev/null || true
```

### Expected Result

Application teams can consume assigned subnets without becoming network administrators.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Separate network ownership from application ownership.

---

## Enhanced Lab 15 — Global VPC / Regional Subnet Capacity

### Objective

Turn **Global VPC / Regional Subnet Capacity** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute networks subnets list --format=table
```

### Expected Result

Primary/secondary ranges are non-overlapping and have growth headroom.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Plan VPC and GKE secondary ranges centrally.

---

## Enhanced Lab 16 — Hierarchical Firewall Policy

### Objective

Turn **Hierarchical Firewall Policy** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Document:
policy scope
priority ranges
secure tags/service accounts
central baseline rules
delegated app rules
logging
```

### Expected Result

Central security controls cannot be silently bypassed by workload projects.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Reserve priority ranges and document central vs delegated ownership.

---

## Enhanced Lab 17 — Service-Account Targeted Firewall Rules

### Objective

Turn **Service-Account Targeted Firewall Rules** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute firewall-rules list --format=json
```

### Expected Result

Firewall intent follows workload identity as VMs are replaced.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use stable workload identity for policy targeting where appropriate.

---

## Enhanced Lab 18 — Private Google Access

### Objective

Turn **Private Google Access** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute networks subnets describe <SUBNET>   --region=<REGION>   --format='value(privateIpGoogleAccess)'
```

### Expected Result

Private workloads reach required Google APIs without public VM addresses.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use Private Google Access for private-subnet API access where it fits.

---

## Enhanced Lab 19 — Private Service Connect

### Objective

Turn **Private Service Connect** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute forwarding-rules list --format=table
```

### Expected Result

Consumers reach the intended private service through an internal endpoint.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use PSC for private service consumption, not full network transit.

---

## Enhanced Lab 20 — Cloud NAT Capacity

### Objective

Turn **Cloud NAT Capacity** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute routers nats list   --router=<ROUTER> --region=<REGION> 2>/dev/null || true
```

### Expected Result

NAT has sufficient port/IP capacity for peak connections.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Monitor NAT connection pressure for large private fleets.

---

## Enhanced Lab 21 — Cloud Router Control Plane

### Objective

Turn **Cloud Router Control Plane** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute routers get-status <ROUTER>   --region=<REGION> --format=json
```

### Expected Result

BGP state and learned/advertised routes are visible.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prove route exchange and packet forwarding separately.

---

## Enhanced Lab 22 — HA VPN Failure Domains

### Objective

Turn **HA VPN Failure Domains** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute vpn-tunnels list --format=table
gcloud compute routers get-status <ROUTER> --region=<REGION>
```

### Expected Result

Redundant paths are healthy and tested.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Test hybrid failover instead of trusting the diagram.

---

## Enhanced Lab 23 — Cloud Interconnect Resilience

### Objective

Turn **Cloud Interconnect Resilience** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Validate:
attachment redundancy
BGP sessions
provider/edge diversity
bandwidth headroom
route preference
backup path
```

### Expected Result

Hybrid applications have a tested fallback aligned to RTO.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design end-to-end hybrid resilience, not just redundant cloud attachments.

---

## Enhanced Lab 24 — Cloud DNS Split-Horizon

### Objective

Turn **Cloud DNS Split-Horizon** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud dns managed-zones list --format=table
```

### Expected Result

Internal and external clients resolve each namespace intentionally.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design DNS at the same time as network routing.

---

## Enhanced Lab 25 — Load Balancer Health Check Reachability

### Objective

Turn **Load Balancer Health Check Reachability** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute health-checks list --format=table
gcloud compute firewall-rules list --format=table
```

### Expected Result

Health checks reach the correct backend endpoint.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat health-check flows as explicit required network flows.

---

## Enhanced Lab 26 — Cloud Armor Policy Rollout

### Objective

Turn **Cloud Armor Policy Rollout** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute security-policies list --format=table
```

### Expected Result

Rule impact is understood before enforcement.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Roll complex WAF/rate policy progressively with log evidence.

---

## Enhanced Lab 27 — Cloud CDN Cache Key

### Objective

Turn **Cloud CDN Cache Key** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Review:
path
query parameters
headers
cookies
TTL
Cache-Control
personalization
```

### Expected Result

Cacheable content gets high hit ratio without leaking personalized content.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Keep cache keys minimal and disable shared caching for sensitive responses.

---

## Enhanced Lab 28 — IAP TCP Forwarding

### Objective

Turn **IAP TCP Forwarding** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute ssh <VM>   --zone=<ZONE>   --tunnel-through-iap
```

### Expected Result

Private VM administration works without an external IP.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prefer identity-aware private administration over public management ports.

---

## Enhanced Lab 29 — OS Login

### Objective

Turn **OS Login** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute project-info describe   --format='yaml(commonInstanceMetadata)'
```

### Expected Result

SSH access follows centrally managed IAM eligibility.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use OS Login where supported for governed Compute Engine access.

---

## Enhanced Lab 30 — Golden Image Pipeline

### Objective

Turn **Golden Image Pipeline** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute images list --no-standard-images --format=table
```

### Expected Result

Production VMs map to an approved image build.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat VM images as versioned release artifacts.

---

## Enhanced Lab 31 — MIG Autohealing vs Autoscaling

### Objective

Turn **MIG Autohealing vs Autoscaling** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute instance-groups managed list --format=table
```

### Expected Result

Health replacement and demand scaling are separately configured.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Do not use CPU autoscaling as a substitute for application health checks.

---

## Enhanced Lab 32 — MIG Rolling Update Capacity

### Objective

Turn **MIG Rolling Update Capacity** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute instance-groups managed describe <MIG>   --region=<REGION> --format=json
```

### Expected Result

The rollout strategy fits quota and preserves availability.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Capacity-plan the deployment overlap period.

---

## Enhanced Lab 33 — Spot VM Resilience

### Objective

Turn **Spot VM Resilience** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute instances list --format=table
```

### Expected Result

Spot loss reduces throughput temporarily but does not lose business state.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use Spot only for interruption-tolerant workload portions.

---

## Enhanced Lab 34 — Persistent Disk / Hyperdisk Performance

### Objective

Turn **Persistent Disk / Hyperdisk Performance** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud compute disks list --format=table
gcloud compute instances describe <VM> --zone=<ZONE> --format=json
```

### Expected Result

The bottleneck is identified as disk, machine, or application.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Evaluate disk and VM performance together.

---

## Enhanced Lab 35 — GKE Autopilot vs Standard

### Objective

Turn **GKE Autopilot vs Standard** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud container clusters list --format=table
```

### Expected Result

Cluster mode is justified by concrete control requirements.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use the lowest operational complexity that satisfies Kubernetes needs.

---

## Enhanced Lab 36 — GKE Regional Availability

### Objective

Turn **GKE Regional Availability** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl get nodes -L topology.kubernetes.io/zone
kubectl get pods -A -o wide
```

### Expected Result

Critical replicas are distributed across failure domains.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design workload topology explicitly.

---

## Enhanced Lab 37 — GKE Workload Identity Federation

### Objective

Turn **GKE Workload Identity Federation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl get serviceaccount -A
gcloud iam service-accounts get-iam-policy <SA_EMAIL> 2>/dev/null || true
```

### Expected Result

Pods obtain short-lived credentials without embedded cloud private keys.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use a distinct workload identity per application capability.

---

## Enhanced Lab 38 — GKE Pod Pending Diagnosis

### Objective

Turn **GKE Pod Pending Diagnosis** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl describe pod <POD>
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get nodes
```

### Expected Result

Scheduler events reveal the unsatisfied constraint.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Read Kubernetes events before changing cluster-wide settings.

---

## Enhanced Lab 39 — GKE Image Pull Diagnosis

### Objective

Turn **GKE Image Pull Diagnosis** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl describe pod <POD>
gcloud artifacts docker images list <REGION>-docker.pkg.dev/<PROJECT>/<REPO>
```

### Expected Result

The image exists and the pulling identity is authorized.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Start with image reference and pulling identity evidence.

---

## Enhanced Lab 40 — GKE HPA + Cluster Autoscaler

### Objective

Turn **GKE HPA + Cluster Autoscaler** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl get hpa -A
kubectl top pods -A 2>/dev/null || true
kubectl top nodes 2>/dev/null || true
```

### Expected Result

Autoscaling converges without persistent Pending Pods or excess capacity.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Set realistic Pod requests because they are scheduling and scaling inputs.

---

## Enhanced Lab 41 — PodDisruptionBudget

### Objective

Turn **PodDisruptionBudget** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl get pdb -A
```

### Expected Result

Maintenance preserves required application replicas.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Derive PDB settings from real replica capacity and availability needs.

---

## Enhanced Lab 42 — GKE Network Policy

### Objective

Turn **GKE Network Policy** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl get networkpolicy -A
```

### Expected Result

Only intended east-west application paths are allowed.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use explicit workload flows and default-deny where operationally appropriate.

---

## Enhanced Lab 43 — GKE Ingress / Gateway Layers

### Objective

Turn **GKE Ingress / Gateway Layers** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
kubectl get ingress -A
kubectl get gateway -A 2>/dev/null || true
kubectl get svc -A
```

### Expected Result

Kubernetes routing status and Google load-balancer health agree.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Troubleshoot Kubernetes and cloud load-balancer layers together.

---

## Enhanced Lab 44 — Cloud Run Revision Immutability

### Objective

Turn **Cloud Run Revision Immutability** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud run revisions list   --service=<SERVICE>   --region=<REGION>
```

### Expected Result

Every running revision maps to a known artifact/configuration.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Deploy immutable artifacts and shift traffic rather than rebuilding.

---

## Enhanced Lab 45 — Cloud Run Concurrency

### Objective

Turn **Cloud Run Concurrency** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud run services describe <SERVICE>   --region=<REGION> --format=json
```

### Expected Result

Concurrency and instance limits align with app and downstream capacity.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Benchmark concurrency and cap scale from dependency limits.

---

## Enhanced Lab 46 — Cloud Run VPC Egress

### Objective

Turn **Cloud Run VPC Egress** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud run services describe <SERVICE>   --region=<REGION>   --format='yaml(spec.template.metadata,spec.template.spec)'
```

### Expected Result

Cloud Run reaches private resources without unintentionally losing needed Internet/API connectivity.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design serverless egress paths before enabling private connectivity.

---

## Enhanced Lab 47 — Cloud Run Service-to-Service Auth

### Objective

Turn **Cloud Run Service-to-Service Auth** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud run services get-iam-policy <SERVICE> --region=<REGION>
```

### Expected Result

Only approved service identities can invoke the service.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use workload identity instead of shared application secrets.

---

## Enhanced Lab 48 — Cloud Run Minimum Instances

### Objective

Turn **Cloud Run Minimum Instances** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud run services describe <SERVICE> --region=<REGION> --format=json
```

### Expected Result

Prewarmed capacity is tied to a measured latency requirement.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Pay for warm capacity only when the SLO requires it.

---

## Enhanced Lab 49 — Cloud Run Jobs vs Services

### Objective

Turn **Cloud Run Jobs vs Services** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud run jobs list --region=<REGION> 2>/dev/null || true
```

### Expected Result

Batch work does not depend on a long-lived HTTP request.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Choose Service vs Job from workload lifecycle.

---

## Enhanced Lab 50 — Eventarc Idempotency

### Objective

Turn **Eventarc Idempotency** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Log:
event ID
event type
source
resource/subject
schema version
processing result
```

### Expected Result

Repeated events do not create duplicate business effects.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design every event handler to be idempotent.

---

## Enhanced Lab 51 — Artifact Registry Provenance

### Objective

Turn **Artifact Registry Provenance** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud artifacts docker images list   <REGION>-docker.pkg.dev/<PROJECT>/<REPO>   --include-tags
```

### Expected Result

Running workloads can be traced to one immutable digest.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Build once and promote the same digest.

---

## Enhanced Lab 52 — Artifact Cleanup and Rollback

### Objective

Turn **Artifact Cleanup and Rollback** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Define:
protected release digests
minimum age
minimum versions
untagged build retention
rollback window
```

### Expected Result

Old artifacts expire without deleting the last known-good release.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Tie artifact retention to the rollback/support window.

---

## Enhanced Lab 53 — Cloud Storage Uniform Bucket-Level Access

### Objective

Turn **Cloud Storage Uniform Bucket-Level Access** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud storage buckets describe gs://<BUCKET> --format=json
```

### Expected Result

Object access is governed by a clear bucket/project IAM model.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prefer one consistent authorization model.

---

## Enhanced Lab 54 — Cloud Storage Protection Layers

### Objective

Turn **Cloud Storage Protection Layers** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud storage buckets describe gs://<BUCKET> --format=json
```

### Expected Result

Protection settings match accidental loss, ransomware, and retention requirements.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Choose protection layers from the data threat model.

---

## Enhanced Lab 55 — Signed URL Security

### Objective

Turn **Signed URL Security** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Guardrails:
specific object
specific HTTP method
short expiry
HTTPS
tenant prefix
post-upload validation
```

### Expected Result

Clients transfer data without broad bucket credentials.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat signed URLs as temporary credentials.

---

## Enhanced Lab 56 — Cloud Storage CMEK

### Objective

Turn **Cloud Storage CMEK** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud kms keys list --keyring=<RING> --location=<LOCATION>
```

### Expected Result

Encrypted objects remain usable through normal operations and recovery.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat KMS as an availability dependency.

---

## Enhanced Lab 57 — Cloud SQL Private Connectivity

### Objective

Turn **Cloud SQL Private Connectivity** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud sql instances describe <INSTANCE> --format=json
```

### Expected Result

The application reaches Cloud SQL privately and authenticates correctly.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Troubleshoot network and DB authorization separately.

---

## Enhanced Lab 58 — Cloud SQL Connection Pooling

### Objective

Turn **Cloud SQL Connection Pooling** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```python
instances = 50
pool_per_instance = 10
print("Potential DB connections:", instances * pool_per_instance)
```

### Expected Result

Maximum application scale stays below safe DB connection capacity.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Capacity-plan total connections across maximum compute scale.

---

## Enhanced Lab 59 — Cloud SQL HA vs Read Replica

### Objective

Turn **Cloud SQL HA vs Read Replica** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud sql instances list --format=table
```

### Expected Result

The topology maps separately to HA and read-scaling needs.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Write separate availability and read-scale requirements.

---

## Enhanced Lab 60 — Cloud SQL PITR

### Objective

Turn **Cloud SQL PITR** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud sql instances describe <INSTANCE> --format=json
```

### Expected Result

The recovery plan can restore to a time before corruption.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design logical-corruption recovery separately from infrastructure HA.

---

## Enhanced Lab 61 — Spanner Global Placement

### Objective

Turn **Spanner Global Placement** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud spanner instances list --format=table 2>/dev/null || true
```

### Expected Result

Instance configuration is justified by write locality, latency, availability, and residency.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use multi-region relational design only when requirements justify its complexity.

---

## Enhanced Lab 62 — Firestore Hotspot Avoidance

### Objective

Turn **Firestore Hotspot Avoidance** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Review:
document ID strategy
write concentration
index count
transaction retries
query patterns
```

### Expected Result

High-volume writes are distributed rather than concentrated.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design document keys from traffic and query patterns.

---

## Enhanced Lab 63 — Bigtable Row-Key Design

### Objective

Turn **Bigtable Row-Key Design** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Bad:
20260820T101500#device123

Better:
07#device123#20260820T101500
```

### Expected Result

Writes distribute across key ranges while important scans remain efficient.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design row keys from write distribution and read locality.

---

## Enhanced Lab 64 — Memorystore Cache Stampede

### Objective

Turn **Memorystore Cache Stampede** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Use:
TTL jitter
single-flight refresh
stale-while-revalidate
prewarming
backend rate limits
```

### Expected Result

Popular-key expiry does not create a synchronized backend spike.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design cache-miss behavior, not only cache-hit behavior.

---

## Enhanced Lab 65 — Pub/Sub Ack Deadline and Idempotency

### Objective

Turn **Pub/Sub Ack Deadline and Idempotency** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud pubsub subscriptions describe <SUBSCRIPTION>
```

### Expected Result

Retries do not create duplicate business effects.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Make consumers idempotent and acknowledge after durable completion.

---

## Enhanced Lab 66 — Pub/Sub Dead-Letter Operations

### Objective

Turn **Pub/Sub Dead-Letter Operations** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud pubsub subscriptions describe <SUBSCRIPTION> --format=json
```

### Expected Result

Poison messages leave the main path and trigger actionable investigation.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Alert on dead-letter growth for critical workflows.

---

## Enhanced Lab 67 — Pub/Sub Ordering Keys

### Objective

Turn **Pub/Sub Ordering Keys** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Order by:
aggregate/entity ID
not one universal key
```

### Expected Result

Related events stay ordered while unrelated entities process in parallel.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use the narrowest ordering domain possible.

---

## Enhanced Lab 68 — Dataflow Backpressure

### Objective

Turn **Dataflow Backpressure** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Monitor:
input throughput
system lag
stage latency
worker utilization
errors/retries
sink quota/latency
```

### Expected Result

Pipeline freshness remains inside the business target.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Alert on data lag/freshness rather than only worker utilization.

---

## Enhanced Lab 69 — BigQuery Partition / Cluster Cost Control

### Objective

Turn **BigQuery Partition / Cluster Cost Control** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```sql
SELECT event_type, COUNT(*) AS n
FROM `project.dataset.events`
WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY event_type;
```

### Expected Result

Queries scan only relevant data.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design analytical storage around common predicates and lifecycle.

---

## Enhanced Lab 70 — BigQuery Location

### Objective

Turn **BigQuery Location** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
bq show --format=prettyjson <PROJECT>:<DATASET> | grep -i location
```

### Expected Result

Related workloads and datasets are intentionally located.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Decide analytics data geography before ingestion.

---

## Enhanced Lab 71 — BigQuery Workload Isolation

### Objective

Turn **BigQuery Workload Isolation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Classify:
interactive BI
ETL
ad hoc
ML
critical dashboards
```

### Expected Result

Critical analytical workloads stay responsive during heavy batch work.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use workload isolation when contention becomes a business problem.

---

## Enhanced Lab 72 — Cloud Logging Central Sinks

### Objective

Turn **Cloud Logging Central Sinks** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud logging sinks list
```

### Expected Result

Critical audit/security logs reach a central protected destination.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Separate security-log administration from workload administration.

---

## Enhanced Lab 73 — Log Exclusions and Cost

### Objective

Turn **Log Exclusions and Cost** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud logging sinks list
gcloud logging exclusions list 2>/dev/null || true
```

### Expected Result

Logging volume and retention align with operational value.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Reduce noise only after confirming the logs are not required for security or recovery.

---

## Enhanced Lab 74 — Metrics Scope and Central Operations

### Objective

Turn **Metrics Scope and Central Operations** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Design:
operations scoping project
monitored projects
dashboard ownership
alert ownership
least-privilege viewers
```

### Expected Result

SRE can view service health across projects without broad write permission.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Centralize observability views while preserving project isolation.

---

## Enhanced Lab 75 — SLI / SLO / Error Budget

### Objective

Turn **SLI / SLO / Error Budget** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
SLI = successful valid requests / valid requests
SLO = 99.9% over 30 days
Latency = p95 < 500 ms
```

### Expected Result

Monitoring can state whether the service meets its reliability target.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use SLOs to connect architecture, alerts, and release risk.

---

## Enhanced Lab 76 — Ops Agent as Code

### Objective

Turn **Ops Agent as Code** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```yaml
logging:
  receivers:
    app:
      type: files
      include_paths:
        - /var/log/myapp/*.log
```

### Expected Result

VM telemetry is reproducible across replacements.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Version and test agent configuration.

---

## Enhanced Lab 77 — Audit Log Investigation

### Objective

Turn **Audit Log Investigation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Logs Explorer filter:
logName:"cloudaudit.googleapis.com"
protoPayload.authenticationInfo.principalEmail="<PRINCIPAL>"
```

### Expected Result

Suspicious changes can be attributed to a principal/API method.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Centralize and protect audit logs before incidents.

---

## Enhanced Lab 78 — Security Command Center Triage

### Objective

Turn **Security Command Center Triage** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Triage:
asset/project
finding category
Internet exposure
privilege/data sensitivity
exploitability
owner
remediation SLA
```

### Expected Result

High-risk findings become owned remediation work.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prioritize findings from contextual risk.

---

## Enhanced Lab 79 — VPC Service Controls

### Objective

Turn **VPC Service Controls** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Troubleshoot:
source project
target project/service
perimeter membership
ingress/egress policy
access context
Policy Denied logs
```

### Expected Result

Sensitive data APIs reject requests from unauthorized contexts.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use VPC-SC for high-value data perimeters with tested workflows.

---

## Enhanced Lab 80 — Cloud KMS Lifecycle

### Objective

Turn **Cloud KMS Lifecycle** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud kms keys list --keyring=<RING> --location=<LOCATION>
gcloud kms keys versions list <KEY> --keyring=<RING> --location=<LOCATION>
```

### Expected Result

Key users and administrators are separated and recovery is tested.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Inventory key dependencies before destructive key changes.

---

## Enhanced Lab 81 — Secret Manager Rotation

### Objective

Turn **Secret Manager Rotation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud secrets versions list <SECRET>
```

### Expected Result

Long-running workloads adopt new secret versions without outage.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design consumer refresh behavior before automating rotation.

---

## Enhanced Lab 82 — Database Restore Testing

### Objective

Turn **Database Restore Testing** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Restore evidence:
recovery point
start/end time
target project/region
KMS
network
data validation
business transaction
```

### Expected Result

A test restore reaches a successful application transaction.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Make restore success and actual recovery time operational KPIs.

---

## Enhanced Lab 83 — RPO

### Objective

Turn **RPO** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
For each data store:
RPO target
backup interval
PITR window
replication lag
last tested restore point
```

### Expected Result

The latest recoverable state is within the business target.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Measure recoverability against business RPO.

---

## Enhanced Lab 84 — RTO

### Objective

Turn **RTO** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```python
steps = {"detect":5,"declare":5,"restore":20,"network":5,"validate":10}
print("RTO minutes:", sum(steps.values()))
```

### Expected Result

Each recovery phase has a measured duration.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Measure RTO from outage start to successful business transaction.

---

## Enhanced Lab 85 — Multi-Region DR Dependency Inventory

### Objective

Turn **Multi-Region DR Dependency Inventory** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
DR bill of materials:
projects/APIs
network
artifacts
IAM/service accounts
KMS/secrets
database/object data
DNS/load balancing
quota
monitoring
runbooks
```

### Expected Result

A game day proves the full workload can run in DR.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Maintain and test a complete DR dependency inventory.

---

## Enhanced Lab 86 — Failback

### Objective

Turn **Failback** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Failback:
current write owner
replication direction
data reconciliation
version parity
traffic shift
rollback
```

### Expected Result

Data created during the DR period is preserved.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design failback separately from failover.

---

## Enhanced Lab 87 — Cloud Build Least Privilege

### Objective

Turn **Cloud Build Least Privilege** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud builds list --limit=20 2>/dev/null || true
gcloud projects get-iam-policy <PROJECT_ID> --format=json
```

### Expected Result

CI/CD and runtime privileges are distinct.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Separate build/deploy identity from application runtime identity.

---

## Enhanced Lab 88 — Progressive Delivery

### Objective

Turn **Progressive Delivery** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Release:
artifact digest
source commit
target
approval
verification result
rollback release
```

### Expected Result

Production uses the artifact that passed staging.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Build once, promote immutably, and gate rollout by evidence.

---

## Enhanced Lab 89 — Binary Authorization / Supply Chain Policy

### Objective

Turn **Binary Authorization / Supply Chain Policy** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Policy:
trusted build identity
required attestation
environment scope
break-glass
audit
```

### Expected Result

Protected workloads deploy only approved artifacts.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use supply-chain admission controls for high-value environments with audited break-glass.

---

## Enhanced Lab 90 — Artifact Vulnerability Triage

### Objective

Turn **Artifact Vulnerability Triage** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Triage:
package/CVE
severity
known exploit
runtime reachable?
fixed version
running digest
```

### Expected Result

Critical exploitable image findings do not silently reach production.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Connect scanning results to immutable artifact provenance.

---

## Enhanced Lab 91 — Terraform State Security

### Objective

Turn **Terraform State Security** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
State controls:
dedicated bucket/project
uniform IAM
versioning/retention
no public access
CI-only write
environment separation
```

### Expected Result

Only approved automation/operators can read or modify production state.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Protect Terraform state as production configuration.

---

## Enhanced Lab 92 — Terraform Plan / Drift

### Objective

Turn **Terraform Plan / Drift** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
terraform plan
```

### Expected Result

High-risk changes and drift are visible before execution.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat plan review as a production change gate.

---

## Enhanced Lab 93 — Centralized Hybrid DNS

### Objective

Turn **Centralized Hybrid DNS** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
DNS table:
suffix
authority
forward-from
forward-to
VPC visibility
TTL
DR behavior
```

### Expected Result

Names resolve consistently from every intended environment.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design DNS at the same time as hybrid routing.

---

## Enhanced Lab 94 — Connectivity Tests

### Objective

Turn **Connectivity Tests** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Use Connectivity Tests / Network Intelligence tooling for supported source-destination paths.
```

### Expected Result

The network configuration layer is identified as reachable or blocked.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use configuration-path evidence before changing firewalls.

---

## Enhanced Lab 95 — VPC Flow Logs vs Packet Data

### Objective

Turn **VPC Flow Logs vs Packet Data** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Flow logs answer:
who talks to whom
port/protocol
volume
flow pattern

They do not show application payload.
```

### Expected Result

Operators choose the correct evidence source for the layer.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Do not expect flow logs to explain application-layer errors.

---

## Enhanced Lab 96 — Prometheus Label Cardinality

### Objective

Turn **Prometheus Label Cardinality** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Good labels:
service
region
status
route template

Avoid:
request_id
user_id
UUID
full dynamic URL
```

### Expected Result

Metric series remain bounded and operationally meaningful.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Put high-cardinality identifiers in logs/traces, not metric labels.

---

## Enhanced Lab 97 — Trace Context Across Async Work

### Objective

Turn **Trace Context Across Async Work** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Propagate:
trace ID if supported
request/correlation ID
event ID
tenant/aggregate ID
deployment version
```

### Expected Result

One business transaction can be reconstructed through synchronous and async stages.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Create correlation context at ingress and propagate it everywhere.

---

## Enhanced Lab 98 — Cost per Business Transaction

### Objective

Turn **Cost per Business Transaction** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```python
monthly_cost = 38000
orders = 500000
print("Cost per order:", monthly_cost / orders)
```

### Expected Result

Teams can distinguish healthy business growth from inefficient spending.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Track business-aligned unit cost, not only total bill.

---

## Enhanced Lab 99 — Network Egress Economics

### Objective

Turn **Network Egress Economics** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
For each high-volume flow:
source location
destination location
GB/day
reason
can processing/cache move closer?
```

### Expected Result

High-volume data movement is intentional and costed.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design data locality and egress before scale makes it expensive.

---

## Enhanced Lab 100 — Cloud Run / GKE / Compute Selection

### Objective

Turn **Cloud Run / GKE / Compute Selection** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
VM/OS control → Compute Engine/MIG
Kubernetes API/operator → GKE
serverless HTTP container → Cloud Run
event function → Cloud Run functions
finite batch → Cloud Run Jobs
```

### Expected Result

Platform choice is traceable to hard requirements.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Do not choose Kubernetes merely because the workload uses containers.

---

## Enhanced Lab 101 — Retry Storm Prevention

### Objective

Turn **Retry Storm Prevention** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```python
import random
for attempt in range(5):
    delay = min(30, 2 ** attempt) + random.random()
    print(round(delay, 2))
```

### Expected Result

Transient faults recover without synchronized retry spikes.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Retry only transient failures and cap total retry time.

---

## Enhanced Lab 102 — Circuit Breaker and Graceful Degradation

### Objective

Turn **Circuit Breaker and Graceful Degradation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
CLOSED → normal calls
failures exceed threshold
OPEN → fail fast/fallback
after timeout
HALF-OPEN → test recovery
```

### Expected Result

Core application remains responsive during optional dependency outage.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Classify dependencies as critical versus optional and design fallbacks.

---

## Enhanced Lab 103 — Bulkhead Isolation

### Objective

Turn **Bulkhead Isolation** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Isolate:
customer API
report workers
email workers
tenant quotas
database pools
projects
```

### Expected Result

Noncritical overload cannot starve critical business paths.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Partition scarce capacity by business criticality.

---

## Enhanced Lab 104 — SLO-Based Release Gate

### Objective

Turn **SLO-Based Release Gate** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
Rollback if:
5xx > 2x baseline
p95 latency > 20% baseline
business success < SLO
critical security finding
```

### Expected Result

Traffic expansion is evidence-driven and reversible.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Define canary success and rollback criteria before rollout.

---

## Enhanced Lab 105 — Architecture Decision Records

### Objective

Turn **Architecture Decision Records** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
ADR:
Context
Decision
Alternatives
Security
Reliability
Cost
Operations
Migration/exit
Revisit trigger
```

### Expected Result

Future teams understand why the architecture exists.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Document difficult-to-reverse decisions and their exit criteria.

---

## Enhanced Lab 106 — Operational Readiness Review

### Objective

Turn **Operational Readiness Review** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```text
[ ] owner/on-call
[ ] SLO + alerts
[ ] logs/traces
[ ] backup + restore test
[ ] quota/headroom
[ ] deployment rollback
[ ] IAM/secrets/KMS
[ ] DR inventory
[ ] budget/labels
```

### Expected Result

The team can operate and recover the service before customers depend on it.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Make operational readiness a launch gate.

---

## Enhanced Lab 107 — Evidence-First Troubleshooting

### Objective

Turn **Evidence-First Troubleshooting** into a repeatable engineering and troubleshooting exercise.

### Procedure

1. Verify `gcloud auth list`, project, region, and zone.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In an authorized disposable environment, introduce one reversible failure where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Delete billable lab resources.

### Command / Query

```bash
gcloud auth list
gcloud config list
gcloud services list --enabled
gcloud logging read 'severity>=ERROR' --limit=20 2>/dev/null || true
```

### Expected Result

The failing layer is found before broad remediation.

### Evidence Record

```text
Symptom
Active account/project
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Preserve evidence and change one layer at a time.

---

## 5. Hands-on Lab / Practical Exercises

> Use an authorized Google Cloud sandbox. Configure budgets before experimentation and delete resources after labs.

### Lab 1 — Verify Account and Project Context

Run:

```bash
gcloud auth list
gcloud config list
gcloud config get-value project
```

Record:

```text
active account
project ID
Region
zone
```

Explain why wrong-project operations are dangerous.

### Lab 2 — Resource Hierarchy Design

Design:

```text
Organization
├─ Platform
│  ├─ Network
│  ├─ Security
│  └─ Observability
├─ Production
│  ├─ App-A
│  └─ Data
├─ NonProduction
└─ Sandbox
```

Document which controls belong at organization, folder, and project scopes.

### Lab 3 — Project and Billing Governance

Create a conceptual or sandbox project.

Check:

```bash
gcloud projects describe PROJECT_ID
gcloud services list --enabled
```

Document:

```text
billing account
labels
enabled APIs
quotas
```

### Lab 4 — Budget and Billing Export

Design:

```text
50% actual
80% actual
100% forecast
```

Then design BigQuery billing export for FinOps analysis.

### Lab 5 — Administrative Groups

Create a table for:

```text
org admins
billing admins
network admins
security admins
logging admins
developers
```

Map each to least-privilege roles.

### Lab 6 — IAM Policy Analysis

Run:

```bash
gcloud projects get-iam-policy PROJECT_ID
```

Identify:

```text
basic roles
service accounts
groups
unexpected users
```

Create a remediation proposal.

### Lab 7 — Service Account Without Keys

Create a lab service account.

Attach it to a VM or Cloud Run service.

Demonstrate that the workload can access one authorized service without a JSON key.

### Lab 8 — Service Account Impersonation

Design/perform authorized impersonation using short-lived credentials.

Document:

```text
caller
target service account
required permission
audit trail
```

### Lab 9 — Workload Identity Federation Tabletop

Design:

```text
GitHub Actions
 ↓ OIDC
Workload Identity Pool
 ↓
Service Account
 ↓
Google Cloud API
```

No JSON key.

### Lab 10 — Organization Policy

Design three constraints:

```text
restrict allowed locations
disable service-account key creation
restrict external IPs
```

Explain where to assign and when to create exception.

### Lab 11 — Cloud Asset Inventory

Search project resources.

```bash
gcloud asset search-all-resources \
  --scope=projects/PROJECT_ID
```

Create an inventory table.

### Lab 12 — Custom VPC

Create/design:

```text
VPC: prod-core

europe-west1:
  app 10.20.0.0/20

us-central1:
  app 10.20.16.0/20
```

Explain global VPC vs regional subnet.

### Lab 13 — Firewall Policy

Create rules for:

```text
Internet → public LB 443
LB → app
app → database
admin → IAP-managed SSH only
```

Compare network tags, service-account targets, and secure Tags.

### Lab 14 — Shared VPC

Design:

```text
Network Host Project
├─ Shared VPC
├─ Production Service Project
├─ Analytics Service Project
└─ Development Service Project
```

Define network-team vs application-team responsibilities.

### Lab 15 — Cloud NAT

Create/design:

```text
Private VM
 ↓
Cloud NAT
 ↓
Internet
```

Verify VM has no external IP.

Troubleshoot DNS and outbound connectivity.

### Lab 16 — HA VPN

Design:

```text
On-Prem Router
    ↕
two VPN tunnels
    ↕
HA VPN
    ↕
Cloud Router BGP
    ↕
VPC
```

Document ASNs and route exchange.

### Lab 17 — Load Balancer Selection

Choose the correct LB type for:

```text
global HTTPS website
regional internal HTTP API
regional TCP service
internal database proxy tier
```

Explain why.

### Lab 18 — Compute Engine VM

Create one Linux VM.

Configure:

```text
private IP
service account
OS Login
startup script
persistent disk
labels
```

Avoid public SSH if possible.

### Lab 19 — VM Manager

Design/perform:

```text
inventory
patch policy
maintenance ring
compliance check
```

for a small VM fleet.

### Lab 20 — MIG

Build/design:

```text
Instance Template
 ↓
Regional MIG
├─ Zone A
└─ Zone B
```

Configure:

```text
health check
autohealing
autoscaling
rolling update
```

### Lab 21 — MIG Failure Exercise

Break startup script or health endpoint intentionally in sandbox.

Trace:

```text
instance template
serial/startup logs
health check
MIG event
autohealing
```

### Lab 22 — Hyperdisk / Persistent Disk Selection

Choose storage for:

```text
general web VM
high-IOPS database
throughput analytics
regional HA VM
temporary scratch
```

Explain performance and durability trade-offs.

### Lab 23 — GKE Standard vs Autopilot

Create a decision matrix for:

```text
node control
operational overhead
daemon workloads
special hardware
cost model
security
```

### Lab 24 — GKE Deployment

Deploy a simple container:

```bash
kubectl create deployment web \
  --image=nginx

kubectl expose deployment web \
  --port=80 \
  --type=ClusterIP
```

Then inspect:

```bash
kubectl get pods
kubectl get svc
kubectl describe deployment web
```

Use only an authorized cluster.

### Lab 25 — GKE Autoscaling

Design:

```text
HPA
node autoscaling
Pod requests
limits
```

Explain how wrong resource requests can waste capacity or block scheduling.

### Lab 26 — GKE Workload Identity

Design:

```text
Kubernetes ServiceAccount
 ↓
Workload Identity
 ↓
Google IAM permissions
 ↓
Cloud Storage
```

No service-account key.

### Lab 27 — Cloud Run Deployment

Deploy a simple containerized service.

Verify:

```bash
gcloud run services list
gcloud run revisions list \
  --service SERVICE \
  --region REGION
```

Document public vs authenticated access.

### Lab 28 — Cloud Run Canary

Deploy revision v2.

Shift:

```text
90% → v1
10% → v2
```

Observe metrics then complete or rollback.

### Lab 29 — Cloud Run Function + Eventarc

Build/design:

```text
Cloud Storage upload
 ↓
Eventarc
 ↓
Cloud Run function
 ↓
write metadata / Pub/Sub
```

Explain event identity and retry behavior.

### Lab 30 — Cloud Storage Protection

Create/configure a lab bucket with:

```text
uniform bucket-level access
versioning
lifecycle
retention policy
CMEK if lab permits
```

Then simulate accidental overwrite.

### Lab 31 — Storage Selection

Choose:

```text
Cloud Storage
Filestore
NetApp Volumes
Managed Lustre
Persistent Disk
Hyperdisk
```

for six workloads.

### Lab 32 — Cloud SQL

Deploy/design private Cloud SQL.

Configure:

```text
private connectivity
backup
PITR
HA
read replica
```

Explain security and recovery.

### Lab 33 — Database Service Selection

Choose:

```text
Cloud SQL
AlloyDB
Spanner
Firestore
Bigtable
Memorystore
```

for six application scenarios.

### Lab 34 — Data Pipeline

Design:

```text
Factory Events
 ↓
Pub/Sub
 ↓
Dataflow
 ↓
BigQuery
 ↓
BI
```

Define schemas, retry, DLQ, and monitoring.

### Lab 35 — BigQuery Cost Optimization

Given a huge table, compare:

```sql
SELECT *
FROM dataset.events;
```

with partitioned/filter-selective query.

Explain bytes scanned.

### Lab 36 — Cloud Monitoring

Create/dashboard concept with:

```text
traffic
errors
latency
saturation
business KPI
```

Add at least three alerts.

### Lab 37 — Cloud Logging

Configure/query logs.

Example:

```text
resource.type="gce_instance"
severity>=ERROR
```

Design a log sink to BigQuery or Cloud Storage.

### Lab 38 — Ops Agent

Install/configure Ops Agent on a disposable VM.

Collect:

```text
system metrics
application log
```

Verify telemetry.

### Lab 39 — Security Operations

Create a security-response workflow:

```text
Security Command Center finding
 ↓
triage
 ↓
IAM/network evidence
 ↓
contain
 ↓
remediate
 ↓
verify
```

### Lab 40 — Backup and Restore

Select one supported service and perform/tabletop:

```text
backup
delete/test failure
restore
validate
measure RTO
```

### Lab 41 — Terraform Foundation

Design:

```text
Git
 ↓
Terraform
 ↓
project
VPC
subnets
firewall
service accounts
monitoring
```

Define state-security requirements.

### Lab 42 — Full Troubleshooting Game Day

Simulate:

1. `PERMISSION_DENIED`
2. service API disabled
3. wrong active project
4. VM unreachable
5. private VM has no Internet
6. Cloud NAT port issue
7. MIG unhealthy
8. GKE Pod pending
9. GKE image pull denied
10. Cloud Run revision fails
11. Cloud Run cannot access database
12. bucket access denied
13. Cloud SQL connection fails
14. Pub/Sub backlog
15. BigQuery query cost spike
16. log sink missing events
17. CMEK permission failure
18. quota exceeded
19. Region/product unavailable
20. billing spike

For each document:

```text
Layer
Evidence
Likely Cause
Fix
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — Production Google Cloud Enterprise Platform

Design a complete Google Cloud platform for a manufacturing and customer-facing digital system.

## Business Requirements

```text
20,000 daily users
2,000 peak concurrent users
production + staging + development
global web users
factory telemetry ingestion
customer/order relational data
document uploads
hybrid ERP connectivity
RPO = 15 minutes for orders
RTO = 1 hour for core portal
analytics RPO = 24 hours
central security and operations
controlled cloud cost
```

## Resource Hierarchy

```text
Organization
├─ Platform
│  ├─ Networking
│  │  └─ Shared VPC Host Project
│  ├─ Security
│  │  └─ Security Project
│  └─ Observability
│     └─ Logging/Monitoring Project
├─ Production
│  ├─ Portal Project
│  ├─ Data Project
│  └─ Integration Project
├─ NonProduction
│  ├─ Staging Project
│  └─ Development Project
└─ Sandbox
```

## Identity

Implement/design:

```text
Cloud Identity groups
IAM least privilege
service accounts
service account impersonation
Workload Identity Federation
GKE Workload Identity
OS Login
break-glass access
```

## Governance

Define:

```text
Organization Policy
mandatory labels
billing budgets
quota controls
Cloud Asset Inventory
security review
```

Required labels:

```text
environment
owner
application
cost_center
data_classification
criticality
```

## Networking

Design:

```text
Shared VPC
├─ europe-west1 application subnets
├─ europe-west1 GKE secondary ranges
├─ private-service ranges
└─ management ranges
```

Include:

```text
Cloud NGFW policies
Cloud NAT
Cloud Router
HA VPN
Cloud Interconnect future path
Private Google Access
Private Service Connect
Cloud DNS
```

## Public Application Edge

```text
Cloud DNS
 ↓
Global External Application Load Balancer
 ↓
Cloud Armor
 ↓
Cloud CDN
 ↓
Cloud Run / GKE / MIG
```

## Compute

Select between:

```text
Compute Engine MIG
GKE Autopilot/Standard
Cloud Run
Cloud Run functions
```

for different components.

Document trade-offs.

## Storage

Select:

```text
Cloud Storage
Persistent Disk / Hyperdisk
Filestore
NetApp Volumes
Managed Lustre
```

where appropriate.

For Cloud Storage configure:

```text
uniform bucket-level access
lifecycle
versioning
retention
CMEK if required
```

## Database

Select:

```text
Cloud SQL / AlloyDB
Spanner
Firestore
Bigtable
Memorystore
```

based on access patterns.

Define:

```text
HA
backup
PITR
read scaling
private connectivity
CMEK
```

## Data Platform

```text
Factory Telemetry
 ↓
Pub/Sub / Managed Kafka if justified
 ↓
Dataflow
 ↓
BigQuery
 ↓
BI / ML
```

## Security

Include:

```text
Security Command Center
Cloud KMS
Secret Manager
VPC Service Controls if justified
Audit Logs
Cloud Armor
Cloud NGFW
private service access
```

## Observability

Centralize:

```text
Cloud Monitoring
Cloud Logging
Ops Agent
Managed Service for Prometheus
Cloud Trace
Cloud Profiler
Personalized Service Health
Cloud Hub
```

Define:

```text
SLIs
SLOs
alerts
dashboards
runbooks
```

## Backup and DR

Document:

```text
RPO
RTO
snapshot schedules
database backup
object retention
cross-region strategy
restore tests
regional failure procedure
```

## Cost

Model:

```text
Compute Engine / GKE / Cloud Run
database
Cloud Storage
BigQuery
logging
NAT
load balancing
egress
backup
support
```

Propose at least 15 optimizations.

## Automation

Use:

```text
Git
 ↓
Terraform
 ↓
Google Cloud APIs
```

Optionally compare:

```text
Config Connector
Helm
Application Design Center
AI-assisted tooling
```

without sacrificing review/change control.

## Required Deliverables

```text
README.md
REQUIREMENTS.md
RESOURCE_HIERARCHY.md
BILLING.md
IAM.md
ORG_POLICY.md
NETWORK.md
COMPUTE.md
GKE.md
CLOUD_RUN.md
STORAGE.md
DATABASE.md
DATA_PLATFORM.md
SECURITY.md
OBSERVABILITY.md
BACKUP_DR.md
COST.md
AUTOMATION.md
DECISIONS/
RUNBOOKS/
```

## Required ADRs

```text
ADR-001-Shared-VPC.md
ADR-002-Compute-Platform.md
ADR-003-Database.md
ADR-004-Hybrid-Connectivity.md
ADR-005-Serverless-vs-GKE.md
ADR-006-Data-Pipeline.md
ADR-007-DR-Strategy.md
```

## Required Runbooks

```text
RUNBOOK_IAM_DENIED.md
RUNBOOK_VM_UNREACHABLE.md
RUNBOOK_NAT_FAILURE.md
RUNBOOK_LOAD_BALANCER_UNHEALTHY.md
RUNBOOK_MIG_FAILURE.md
RUNBOOK_GKE_POD_FAILURE.md
RUNBOOK_CLOUD_RUN_FAILURE.md
RUNBOOK_STORAGE_ACCESS.md
RUNBOOK_DATABASE_FAILURE.md
RUNBOOK_PUBSUB_BACKLOG.md
RUNBOOK_BIGQUERY_COST.md
RUNBOOK_CMEK_FAILURE.md
RUNBOOK_REGION_INCIDENT.md
RUNBOOK_COST_SPIKE.md
```

---

## 7. Recommended Resources

This Markdown is designed to be self-contained for the learning path.

For live production behavior, verify current official Google Cloud documentation:

```text
Associate Cloud Engineer exam guide
Google Cloud resource hierarchy
Cloud Identity
IAM
Organization Policy
Cloud Asset Inventory
VPC
Cloud NGFW
Shared VPC
Cloud NAT
Cloud Router
Cloud VPN
Cloud Interconnect
Cloud DNS
Cloud Load Balancing
Cloud Armor
Compute Engine
VM Manager
Google Kubernetes Engine
Cloud Run
Cloud Run functions
Artifact Registry
Cloud Storage
Filestore
NetApp Volumes
Managed Lustre
Cloud SQL
AlloyDB
Spanner
Firestore
Bigtable
Database Center
BigQuery
Pub/Sub
Dataflow
Managed Service for Apache Kafka
Cloud Monitoring
Cloud Logging
Managed Service for Prometheus
Security Command Center
Cloud KMS
Secret Manager
VPC Service Controls
Terraform on Google Cloud
```

Because Google Cloud changes rapidly, check current product documentation before using:

```text
AI-assisted tooling
preview products
specific machine families
specific API versions
regional product availability
deprecated terminology
```

---

## 8. Certification Relevance

Closest direct certification:

```text
Google Cloud Associate Cloud Engineer
```

Current standard exam:

```text
2 hours
50–60 multiple-choice/multiple-select questions
$125 + applicable tax
3-year validity
no prerequisite
6+ months hands-on Google Cloud recommended
```

Current exam domains:

```text
Setting up a cloud solution environment               ~20%
Planning and implementing a cloud solution            ~30%
Ensuring successful operation of a cloud solution     ~30%
Configuring access and security                       ~20%
```

This course goes beyond the exam by adding:

```text
enterprise foundation design
deeper networking
deeper GKE
DR
runbooks
FinOps
security operations
architecture decision records
troubleshooting game days
```

It prepares for later phases:

```text
Containers
Docker
Kubernetes
OpenShift
Infrastructure as Code
DevOps
Cloud Security
DevSecOps
```

and future Google Cloud certifications such as:

```text
Professional Cloud Architect
Professional Cloud Network Engineer
Professional Cloud Security Engineer
Professional Cloud DevOps Engineer
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Use personal projects for enterprise production.  
  **Best practice:** organization/folder/project hierarchy with governance.

- **Mistake:** Give Owner or Editor broadly.  
  **Best practice:** groups + predefined/custom least-privilege roles.

- **Mistake:** Download service-account keys by default.  
  **Best practice:** attached service accounts, impersonation, federation.

- **Mistake:** Confuse labels, network tags, and Resource Manager Tags.  
  **Best practice:** use each for its intended control plane.

- **Mistake:** Treat VPC as Regional.  
  **Best practice:** Google Cloud VPC is global; subnets are Regional.

- **Mistake:** Overlap CIDRs.  
  **Best practice:** centralized IP plan including GKE/hybrid growth.

- **Mistake:** Public IP on every VM.  
  **Best practice:** private VM + Cloud NAT/IAP as required.

- **Mistake:** GKE because "containers".  
  **Best practice:** choose Cloud Run when Kubernetes control is unnecessary.

- **Mistake:** Use GKE Standard when Autopilot meets requirements.  
  **Best practice:** choose lowest necessary operational complexity.

- **Mistake:** Use service-account JSON keys in Kubernetes.  
  **Best practice:** Workload Identity.

- **Mistake:** Put secrets in metadata or environment source files.  
  **Best practice:** Secret Manager + workload identity.

- **Mistake:** One VM rather than MIG for production stateless service.  
  **Best practice:** regional MIG + health + autoscaling.

- **Mistake:** Treat snapshot as full DR.  
  **Best practice:** backup, isolation, restore testing, RPO/RTO.

- **Mistake:** Query huge BigQuery tables with `SELECT *`.  
  **Best practice:** partition/filter/select required columns.

- **Mistake:** Keep every log forever.  
  **Best practice:** retention, routing, archive, and cost policy.

- **Mistake:** Budget means hard cost limit.  
  **Best practice:** budgets alert; automation/governance controls spending.

- **Mistake:** Follow AI-generated cloud changes blindly.  
  **Best practice:** verify, review, test, and retain change control.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Google Cloud resource hierarchy?

**Answer:** Organization → folder → project → resource.

### Q2. Is billing account the same as project?

**Answer:** No. Billing accounts pay for linked projects.

### Q3. Current closest operational certification?

**Answer:** Google Cloud Associate Cloud Engineer.

### Q4. Current ACE standard exam length?

**Answer:** 2 hours.

### Q5. Current ACE question count?

**Answer:** 50–60.

### Q6. Largest current ACE domains?

**Answer:** Planning/implementation and successful operations, each about 30%.

### Q7. Is Google Cloud VPC Regional?

**Answer:** No. VPC is global.

### Q8. Are subnets global?

**Answer:** No. Subnets are Regional.

### Q9. IAM?

**Answer:** Controls which principals get which roles/permissions on which resources.

### Q10. Service account?

**Answer:** Workload identity.

### Q11. Workload Identity Federation?

**Answer:** Exchanges external workload identity for short-lived Google Cloud credentials without service-account keys.

### Q12. Organization Policy?

**Answer:** Hierarchical constraints controlling allowed resource configuration.

### Q13. Cloud Asset Inventory?

**Answer:** Resource/policy inventory and search/history service.

### Q14. Shared VPC?

**Answer:** Host project centrally provides VPC subnets/networking to service projects.

### Q15. Cloud NAT?

**Answer:** Managed outbound NAT for private workloads without external IPs.

### Q16. Cloud Router?

**Answer:** Managed BGP control plane for dynamic route exchange.

### Q17. HA VPN?

**Answer:** Highly available IPsec VPN connectivity.

### Q18. Cloud Interconnect?

**Answer:** Private enterprise connectivity to Google's network.

### Q19. Cloud NGFW?

**Answer:** Google's modern managed next-generation firewall/policy platform.

### Q20. Compute Engine?

**Answer:** Google Cloud VM service.

### Q21. MIG?

**Answer:** Managed Instance Group for VM fleet scaling, healing, and updates.

### Q22. Hyperdisk?

**Answer:** Modern Google Cloud high-performance/configurable block-storage family.

### Q23. GKE?

**Answer:** Google Kubernetes Engine.

### Q24. Autopilot?

**Answer:** More-managed GKE operating mode where Google manages more node infrastructure.

### Q25. Cloud Run?

**Answer:** Fully managed serverless container application platform.

### Q26. Current function terminology?

**Answer:** Cloud Run functions.

### Q27. Eventarc?

**Answer:** Event routing to Cloud Run-based and other supported event destinations.

### Q28. Cloud Storage?

**Answer:** Object storage.

### Q29. Filestore?

**Answer:** Managed NFS filesystem.

### Q30. Managed Lustre?

**Answer:** High-performance parallel filesystem service.

### Q31. Cloud SQL?

**Answer:** Managed traditional relational database service.

### Q32. Spanner?

**Answer:** Distributed horizontally scalable strongly consistent relational database.

### Q33. Bigtable?

**Answer:** Wide-column NoSQL database.

### Q34. Firestore?

**Answer:** Serverless document database.

### Q35. BigQuery?

**Answer:** Serverless analytical data warehouse/query platform.

### Q36. Pub/Sub?

**Answer:** Managed asynchronous messaging/event ingestion.

### Q37. Dataflow?

**Answer:** Managed Apache Beam batch/stream processing.

### Q38. Database Center?

**Answer:** Central Google Cloud database-fleet visibility/management capability.

### Q39. Cloud Monitoring?

**Answer:** Metrics, dashboards, alerts, SLO and operational monitoring.

### Q40. Cloud Logging?

**Answer:** Central logs, routing, retention, querying, and analytics.

### Q41. Ops Agent?

**Answer:** Agent for guest OS/application logs and metrics on supported compute environments.

### Q42. Managed Service for Prometheus?

**Answer:** Managed Prometheus-compatible monitoring backend.

### Q43. Security Command Center?

**Answer:** Central security posture, risk, and findings platform.

### Q44. VPC Service Controls?

**Answer:** Service perimeters reducing data-exfiltration risk for supported Google-managed services.

### Q45. Core Google Cloud engineer mindset?

**Answer:** Govern hierarchy, use strong workload identity, design networking deliberately, automate infrastructure, observe services, test recovery, control cost, and troubleshoot from evidence.

---

# Expanded Self-Assessment Bank — Google Cloud Platform

### Q1. What is the main engineering lesson from **gcloud Context Safety**?

**Answer:** Use named human configurations and explicit `--project` in critical automation.

### Q2. What is the main engineering lesson from **Organization and Folder Governance**?

**Answer:** Keep folder hierarchy stable, shallow, and control-oriented.

### Q3. What is the main engineering lesson from **Project as Blast-Radius Boundary**?

**Answer:** Use projects deliberately for isolation and ownership.

### Q4. What is the main engineering lesson from **IAM Effective Access**?

**Answer:** Troubleshoot the hierarchy before granting broad roles.

### Q5. What is the main engineering lesson from **IAM Deny Guardrails**?

**Answer:** Use deny controls sparingly for high-impact permissions.

### Q6. What is the main engineering lesson from **Service Account Impersonation**?

**Answer:** Prefer impersonation for human and automation elevation.

### Q7. What is the main engineering lesson from **Workload Identity Federation**?

**Answer:** Create separate federation trust for separate environments/repositories.

### Q8. What is the main engineering lesson from **Organization Policy**?

**Answer:** Use organization policy for durable platform guardrails.

### Q9. What is the main engineering lesson from **Organization Policy Exceptions**?

**Answer:** Treat exceptions as risk items with expiry.

### Q10. What is the main engineering lesson from **Cloud Asset Inventory**?

**Answer:** Use Asset Inventory for fleet-level discovery and drift investigations.

### Q11. What is the main engineering lesson from **Billing Export to BigQuery**?

**Answer:** Export billing data before you need historical FinOps analysis.

### Q12. What is the main engineering lesson from **Quota Headroom**?

**Answer:** Monitor quota headroom like any other capacity signal.

### Q13. What is the main engineering lesson from **API Enablement Governance**?

**Answer:** Treat service enablement as governed platform configuration.

### Q14. What is the main engineering lesson from **Shared VPC Administrative Separation**?

**Answer:** Separate network ownership from application ownership.

### Q15. What is the main engineering lesson from **Global VPC / Regional Subnet Capacity**?

**Answer:** Plan VPC and GKE secondary ranges centrally.

### Q16. What is the main engineering lesson from **Hierarchical Firewall Policy**?

**Answer:** Reserve priority ranges and document central vs delegated ownership.

### Q17. What is the main engineering lesson from **Service-Account Targeted Firewall Rules**?

**Answer:** Use stable workload identity for policy targeting where appropriate.

### Q18. What is the main engineering lesson from **Private Google Access**?

**Answer:** Use Private Google Access for private-subnet API access where it fits.

### Q19. What is the main engineering lesson from **Private Service Connect**?

**Answer:** Use PSC for private service consumption, not full network transit.

### Q20. What is the main engineering lesson from **Cloud NAT Capacity**?

**Answer:** Monitor NAT connection pressure for large private fleets.

### Q21. What is the main engineering lesson from **Cloud Router Control Plane**?

**Answer:** Prove route exchange and packet forwarding separately.

### Q22. What is the main engineering lesson from **HA VPN Failure Domains**?

**Answer:** Test hybrid failover instead of trusting the diagram.

### Q23. What is the main engineering lesson from **Cloud Interconnect Resilience**?

**Answer:** Design end-to-end hybrid resilience, not just redundant cloud attachments.

### Q24. What is the main engineering lesson from **Cloud DNS Split-Horizon**?

**Answer:** Design DNS at the same time as network routing.

### Q25. What is the main engineering lesson from **Load Balancer Health Check Reachability**?

**Answer:** Treat health-check flows as explicit required network flows.

### Q26. What is the main engineering lesson from **Cloud Armor Policy Rollout**?

**Answer:** Roll complex WAF/rate policy progressively with log evidence.

### Q27. What is the main engineering lesson from **Cloud CDN Cache Key**?

**Answer:** Keep cache keys minimal and disable shared caching for sensitive responses.

### Q28. What is the main engineering lesson from **IAP TCP Forwarding**?

**Answer:** Prefer identity-aware private administration over public management ports.

### Q29. What is the main engineering lesson from **OS Login**?

**Answer:** Use OS Login where supported for governed Compute Engine access.

### Q30. What is the main engineering lesson from **Golden Image Pipeline**?

**Answer:** Treat VM images as versioned release artifacts.

### Q31. What is the main engineering lesson from **MIG Autohealing vs Autoscaling**?

**Answer:** Do not use CPU autoscaling as a substitute for application health checks.

### Q32. What is the main engineering lesson from **MIG Rolling Update Capacity**?

**Answer:** Capacity-plan the deployment overlap period.

### Q33. What is the main engineering lesson from **Spot VM Resilience**?

**Answer:** Use Spot only for interruption-tolerant workload portions.

### Q34. What is the main engineering lesson from **Persistent Disk / Hyperdisk Performance**?

**Answer:** Evaluate disk and VM performance together.

### Q35. What is the main engineering lesson from **GKE Autopilot vs Standard**?

**Answer:** Use the lowest operational complexity that satisfies Kubernetes needs.

### Q36. What is the main engineering lesson from **GKE Regional Availability**?

**Answer:** Design workload topology explicitly.

### Q37. What is the main engineering lesson from **GKE Workload Identity Federation**?

**Answer:** Use a distinct workload identity per application capability.

### Q38. What is the main engineering lesson from **GKE Pod Pending Diagnosis**?

**Answer:** Read Kubernetes events before changing cluster-wide settings.

### Q39. What is the main engineering lesson from **GKE Image Pull Diagnosis**?

**Answer:** Start with image reference and pulling identity evidence.

### Q40. What is the main engineering lesson from **GKE HPA + Cluster Autoscaler**?

**Answer:** Set realistic Pod requests because they are scheduling and scaling inputs.

### Q41. What is the main engineering lesson from **PodDisruptionBudget**?

**Answer:** Derive PDB settings from real replica capacity and availability needs.

### Q42. What is the main engineering lesson from **GKE Network Policy**?

**Answer:** Use explicit workload flows and default-deny where operationally appropriate.

### Q43. What is the main engineering lesson from **GKE Ingress / Gateway Layers**?

**Answer:** Troubleshoot Kubernetes and cloud load-balancer layers together.

### Q44. What is the main engineering lesson from **Cloud Run Revision Immutability**?

**Answer:** Deploy immutable artifacts and shift traffic rather than rebuilding.

### Q45. What is the main engineering lesson from **Cloud Run Concurrency**?

**Answer:** Benchmark concurrency and cap scale from dependency limits.

### Q46. What is the main engineering lesson from **Cloud Run VPC Egress**?

**Answer:** Design serverless egress paths before enabling private connectivity.

### Q47. What is the main engineering lesson from **Cloud Run Service-to-Service Auth**?

**Answer:** Use workload identity instead of shared application secrets.

### Q48. What is the main engineering lesson from **Cloud Run Minimum Instances**?

**Answer:** Pay for warm capacity only when the SLO requires it.

### Q49. What is the main engineering lesson from **Cloud Run Jobs vs Services**?

**Answer:** Choose Service vs Job from workload lifecycle.

### Q50. What is the main engineering lesson from **Eventarc Idempotency**?

**Answer:** Design every event handler to be idempotent.

### Q51. What is the main engineering lesson from **Artifact Registry Provenance**?

**Answer:** Build once and promote the same digest.

### Q52. What is the main engineering lesson from **Artifact Cleanup and Rollback**?

**Answer:** Tie artifact retention to the rollback/support window.

### Q53. What is the main engineering lesson from **Cloud Storage Uniform Bucket-Level Access**?

**Answer:** Prefer one consistent authorization model.

### Q54. What is the main engineering lesson from **Cloud Storage Protection Layers**?

**Answer:** Choose protection layers from the data threat model.

### Q55. What is the main engineering lesson from **Signed URL Security**?

**Answer:** Treat signed URLs as temporary credentials.

### Q56. What is the main engineering lesson from **Cloud Storage CMEK**?

**Answer:** Treat KMS as an availability dependency.

### Q57. What is the main engineering lesson from **Cloud SQL Private Connectivity**?

**Answer:** Troubleshoot network and DB authorization separately.

### Q58. What is the main engineering lesson from **Cloud SQL Connection Pooling**?

**Answer:** Capacity-plan total connections across maximum compute scale.

### Q59. What is the main engineering lesson from **Cloud SQL HA vs Read Replica**?

**Answer:** Write separate availability and read-scale requirements.

### Q60. What is the main engineering lesson from **Cloud SQL PITR**?

**Answer:** Design logical-corruption recovery separately from infrastructure HA.

### Q61. What is the main engineering lesson from **Spanner Global Placement**?

**Answer:** Use multi-region relational design only when requirements justify its complexity.

### Q62. What is the main engineering lesson from **Firestore Hotspot Avoidance**?

**Answer:** Design document keys from traffic and query patterns.

### Q63. What is the main engineering lesson from **Bigtable Row-Key Design**?

**Answer:** Design row keys from write distribution and read locality.

### Q64. What is the main engineering lesson from **Memorystore Cache Stampede**?

**Answer:** Design cache-miss behavior, not only cache-hit behavior.

### Q65. What is the main engineering lesson from **Pub/Sub Ack Deadline and Idempotency**?

**Answer:** Make consumers idempotent and acknowledge after durable completion.

### Q66. What is the main engineering lesson from **Pub/Sub Dead-Letter Operations**?

**Answer:** Alert on dead-letter growth for critical workflows.

### Q67. What is the main engineering lesson from **Pub/Sub Ordering Keys**?

**Answer:** Use the narrowest ordering domain possible.

### Q68. What is the main engineering lesson from **Dataflow Backpressure**?

**Answer:** Alert on data lag/freshness rather than only worker utilization.

### Q69. What is the main engineering lesson from **BigQuery Partition / Cluster Cost Control**?

**Answer:** Design analytical storage around common predicates and lifecycle.

### Q70. What is the main engineering lesson from **BigQuery Location**?

**Answer:** Decide analytics data geography before ingestion.

### Q71. What is the main engineering lesson from **BigQuery Workload Isolation**?

**Answer:** Use workload isolation when contention becomes a business problem.

### Q72. What is the main engineering lesson from **Cloud Logging Central Sinks**?

**Answer:** Separate security-log administration from workload administration.

### Q73. What is the main engineering lesson from **Log Exclusions and Cost**?

**Answer:** Reduce noise only after confirming the logs are not required for security or recovery.

### Q74. What is the main engineering lesson from **Metrics Scope and Central Operations**?

**Answer:** Centralize observability views while preserving project isolation.

### Q75. What is the main engineering lesson from **SLI / SLO / Error Budget**?

**Answer:** Use SLOs to connect architecture, alerts, and release risk.

### Q76. What is the main engineering lesson from **Ops Agent as Code**?

**Answer:** Version and test agent configuration.

### Q77. What is the main engineering lesson from **Audit Log Investigation**?

**Answer:** Centralize and protect audit logs before incidents.

### Q78. What is the main engineering lesson from **Security Command Center Triage**?

**Answer:** Prioritize findings from contextual risk.

### Q79. What is the main engineering lesson from **VPC Service Controls**?

**Answer:** Use VPC-SC for high-value data perimeters with tested workflows.

### Q80. What is the main engineering lesson from **Cloud KMS Lifecycle**?

**Answer:** Inventory key dependencies before destructive key changes.

### Q81. What is the main engineering lesson from **Secret Manager Rotation**?

**Answer:** Design consumer refresh behavior before automating rotation.

### Q82. What is the main engineering lesson from **Database Restore Testing**?

**Answer:** Make restore success and actual recovery time operational KPIs.

### Q83. What is the main engineering lesson from **RPO**?

**Answer:** Measure recoverability against business RPO.

### Q84. What is the main engineering lesson from **RTO**?

**Answer:** Measure RTO from outage start to successful business transaction.

### Q85. What is the main engineering lesson from **Multi-Region DR Dependency Inventory**?

**Answer:** Maintain and test a complete DR dependency inventory.

### Q86. What is the main engineering lesson from **Failback**?

**Answer:** Design failback separately from failover.

### Q87. What is the main engineering lesson from **Cloud Build Least Privilege**?

**Answer:** Separate build/deploy identity from application runtime identity.

### Q88. What is the main engineering lesson from **Progressive Delivery**?

**Answer:** Build once, promote immutably, and gate rollout by evidence.

### Q89. What is the main engineering lesson from **Binary Authorization / Supply Chain Policy**?

**Answer:** Use supply-chain admission controls for high-value environments with audited break-glass.

### Q90. What is the main engineering lesson from **Artifact Vulnerability Triage**?

**Answer:** Connect scanning results to immutable artifact provenance.

### Q91. What is the main engineering lesson from **Terraform State Security**?

**Answer:** Protect Terraform state as production configuration.

### Q92. What is the main engineering lesson from **Terraform Plan / Drift**?

**Answer:** Treat plan review as a production change gate.

### Q93. What is the main engineering lesson from **Centralized Hybrid DNS**?

**Answer:** Design DNS at the same time as hybrid routing.

### Q94. What is the main engineering lesson from **Connectivity Tests**?

**Answer:** Use configuration-path evidence before changing firewalls.

### Q95. What is the main engineering lesson from **VPC Flow Logs vs Packet Data**?

**Answer:** Do not expect flow logs to explain application-layer errors.

### Q96. What is the main engineering lesson from **Prometheus Label Cardinality**?

**Answer:** Put high-cardinality identifiers in logs/traces, not metric labels.

### Q97. What is the main engineering lesson from **Trace Context Across Async Work**?

**Answer:** Create correlation context at ingress and propagate it everywhere.

### Q98. What is the main engineering lesson from **Cost per Business Transaction**?

**Answer:** Track business-aligned unit cost, not only total bill.

### Q99. What is the main engineering lesson from **Network Egress Economics**?

**Answer:** Design data locality and egress before scale makes it expensive.

### Q100. What is the main engineering lesson from **Cloud Run / GKE / Compute Selection**?

**Answer:** Do not choose Kubernetes merely because the workload uses containers.

### Q101. What is the main engineering lesson from **Retry Storm Prevention**?

**Answer:** Retry only transient failures and cap total retry time.

### Q102. What is the main engineering lesson from **Circuit Breaker and Graceful Degradation**?

**Answer:** Classify dependencies as critical versus optional and design fallbacks.

### Q103. What is the main engineering lesson from **Bulkhead Isolation**?

**Answer:** Partition scarce capacity by business criticality.

### Q104. What is the main engineering lesson from **SLO-Based Release Gate**?

**Answer:** Define canary success and rollback criteria before rollout.

### Q105. What is the main engineering lesson from **Architecture Decision Records**?

**Answer:** Document difficult-to-reverse decisions and their exit criteria.

### Q106. What is the main engineering lesson from **Operational Readiness Review**?

**Answer:** Make operational readiness a launch gate.

### Q107. What is the main engineering lesson from **Evidence-First Troubleshooting**?

**Answer:** Preserve evidence and change one layer at a time.

## Completion Checklist

- [ ] I understand Google Cloud organization/folder/project hierarchy.
- [ ] I can manage billing, budgets, quotas, labels, and APIs.
- [ ] I understand Cloud Identity and IAM.
- [ ] I can manage service accounts securely.
- [ ] I understand impersonation and federation.
- [ ] I can use Organization Policy.
- [ ] I understand Cloud Asset Inventory.
- [ ] I understand global VPC and regional subnets.
- [ ] I can design routes and firewall policies.
- [ ] I understand Cloud NGFW and secure Tags.
- [ ] I understand Shared VPC.
- [ ] I understand Cloud NAT and Cloud Router.
- [ ] I understand VPN and Interconnect.
- [ ] I understand Cloud DNS and load balancing.
- [ ] I understand Cloud CDN and Cloud Armor.
- [ ] I can deploy and operate Compute Engine.
- [ ] I understand Persistent Disk and Hyperdisk.
- [ ] I can design MIGs and autoscaling.
- [ ] I understand OS Login and VM Manager.
- [ ] I understand GKE Standard and Autopilot.
- [ ] I can operate Pods, Services, node pools, HPA and VPA.
- [ ] I understand GKE Workload Identity.
- [ ] I understand Cloud Run and revisions.
- [ ] I understand Cloud Run functions and Eventarc.
- [ ] I understand Artifact Registry.
- [ ] I understand Cloud Storage and its storage classes.
- [ ] I understand Filestore, NetApp Volumes, and Managed Lustre.
- [ ] I can select Cloud SQL, AlloyDB, Spanner, Firestore, Bigtable, and Memorystore.
- [ ] I understand Database Center.
- [ ] I understand BigQuery, Pub/Sub, Dataflow, and Managed Kafka.
- [ ] I can configure Monitoring and Logging.
- [ ] I understand Ops Agent and Managed Prometheus.
- [ ] I understand Trace, Profiler, Query Insights, Service Health, Active Assist, and Cloud Hub.
- [ ] I understand KMS, Secret Manager, SCC, and VPC Service Controls.
- [ ] I understand backup, restore, RPO, and RTO.
- [ ] I can safely use gcloud, bq, kubectl, and Terraform concepts.
- [ ] I understand current AI-assisted tooling without relying on it blindly.
- [ ] I can troubleshoot IAM, network, compute, GKE, Cloud Run, storage, and data problems.
- [ ] I completed all 42 labs.
- [ ] I completed the Production Google Cloud Enterprise Platform capstone.
