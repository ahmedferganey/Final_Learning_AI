# 50. Microsoft Azure Fundamentals

> Phase 11 — Cloud Fundamentals

This course maps the provider-neutral concepts from Course 48 into Microsoft Azure.

It is aligned to the current **Microsoft Certified: Azure Fundamentals** certification and **Exam AZ-900** skills measured **as of July 20, 2026**.

Current exam domains:

```text
Describe cloud concepts                         25–30%
Describe Azure architecture and services        35–40%
Describe Azure management and governance        30–35%
```

The current Microsoft certification page states that the assessment duration is **45 minutes**.

This course goes beyond the minimum certification boundary because the long-term goal is practical Azure administration and cloud engineering.

---

# Azure Mental Model

```text
Microsoft Entra Tenant
        |
Management Groups
        |
Subscriptions
        |
Resource Groups
        |
Azure Resources
```

Example:

```text
Tenant
└─ Management Group: Corp
   ├─ Subscription: Production
   │  ├─ RG-Network
   │  │  └─ VNet / VPN / DNS
   │  └─ RG-App
   │     ├─ VM / App Service
   │     ├─ Storage
   │     └─ Database
   └─ Subscription: NonProduction
```

A typical Azure web architecture:

```text
                            Users
                              |
                         Azure DNS
                              |
                      Azure Front Door/CDN
                              |
                    Web Application Firewall
                              |
                 Application Gateway / Load Balancer
                       /                 \
                  Zone 1                Zone 2
                    |                     |
                App/VM1                App/VM2
                    \                     /
                     Azure SQL / Managed DB
                              |
                        Azure Storage
                              |
                         Azure Backup
```

Core operating layers:

```text
Azure Global Infrastructure
        ↓
Tenant / Subscription Hierarchy
        ↓
Microsoft Entra ID
        ↓
Virtual Networking
        ↓
Compute / Containers / Serverless
        ↓
Storage / Databases
        ↓
Security
        ↓
Management / Monitoring
        ↓
Governance / Cost
```

The learning pattern is:

```text
Azure Concept
   ↓
Architecture Diagram
   ↓
Portal / CLI / PowerShell / ARM-Bicep Example
   ↓
Expected Behavior
   ↓
Security / Governance Implication
   ↓
Cost / Reliability Implication
   ↓
Troubleshooting
```

---

## 1. Topic Title

**Microsoft Azure Fundamentals**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain Azure cloud value and consumption-based economics.
- Explain IaaS, PaaS, SaaS, and serverless in Azure.
- Explain public, private, and hybrid cloud.
- Explain Azure regions, availability zones, region pairs, sovereign regions, and datacenters.
- Explain Azure resources, resource groups, subscriptions, management groups, and hierarchy.
- Explain Microsoft Entra ID and Microsoft Entra Domain Services.
- Explain authentication, SSO, MFA, passwordless, external identities, Conditional Access, Azure RBAC, Zero Trust, and defense in depth.
- Explain Azure Virtual Machines, VM Scale Sets, availability sets, and Azure Virtual Desktop.
- Explain App Service, containers, Azure Container Apps, AKS, Azure Functions, and serverless fundamentals.
- Explain VNet, subnet, NSG, route tables, peering, Azure DNS, VPN Gateway, ExpressRoute, public/private endpoints, Private Link, NAT Gateway, Load Balancer, Application Gateway, Front Door, and Traffic Manager conceptually.
- Explain Azure Storage accounts, Blob, Files, Queues, Tables, managed disks, storage tiers, and redundancy.
- Explain LRS, ZRS, GRS, RA-GRS, GZRS, and RA-GZRS.
- Explain AzCopy, Storage Explorer, Azure File Sync, Azure Migrate, and Azure Data Box.
- Explain Azure SQL Database, SQL Managed Instance, Cosmos DB, Azure Database for PostgreSQL, Redis-style cache concepts, and Synapse at a fundamentals level.
- Explain Microsoft Defender for Cloud.
- Explain Key Vault, encryption, secrets, certificates, and managed identities conceptually.
- Explain Azure Policy, resource locks, tags, Purview, and governance.
- Explain Azure portal, Cloud Shell, CLI, PowerShell, Resource Manager, ARM templates, and Bicep fundamentals.
- Explain Azure Arc.
- Explain Azure Monitor, Log Analytics, Application Insights, alerts, Advisor, and Service Health.
- Explain Cost Management + Billing and Pricing Calculator.
- Explain budgets, reservations/savings concepts, spot VMs, Hybrid Benefit, and cost factors conceptually.
- Explain Azure Well-Architected Framework and Cloud Adoption Framework conceptually.
- Recognize AZ-900 scenario patterns.
- Perform safe basic Azure CLI and PowerShell discovery.
- Design a production-style Azure foundation.
- Troubleshoot foundational Azure identity, network, compute, storage, and cost issues.

---

## 3. Prerequisites

Required:

- 48. Cloud Computing Fundamentals
- networking
- Linux/Windows administration basics
- storage
- databases
- Git/configuration-management fundamentals

Optional tools:

```text
Azure subscription
Azure portal
Azure CLI
Azure PowerShell
Cloud Shell
```

Safe identity verification:

```bash
az account show
```

PowerShell:

```powershell
Get-AzContext
```

Before creating resources, always verify the active tenant and subscription.

---

## 4. Core Concepts Explanation

# Part 1 — What Microsoft Azure Is

Azure is Microsoft's public cloud platform for:

```text
compute
networking
storage
databases
identity
analytics
AI
integration
security
management
```

Its value is not just hosted servers; it is a large API-driven managed-service platform.

# Part 2 — Azure and the Microsoft Cloud Ecosystem

Azure integrates closely with:

```text
Microsoft Entra
Microsoft 365
GitHub
Windows Server
SQL Server
Power Platform
Defender
Purview
```

This integration can be a major reason enterprises choose Azure.

# Part 3 — AZ-900 Cloud Concepts Domain

The current exam expects:

```text
cloud computing
shared responsibility
public/private/hybrid
consumption-based model
pricing models
serverless
HA/scalability
reliability/predictability
security/governance
manageability
IaaS/PaaS/SaaS
```

These were introduced in Course 48 and are now mapped to Azure.

# Part 4 — Consumption-Based Model

Azure services are often billed according to measurable consumption.

Examples:

```text
VM time
storage capacity
transactions
database capacity
network egress
```

Cloud flexibility requires cost governance because consumption can grow automatically.

# Part 5 — Azure IaaS

Examples:

```text
Azure Virtual Machines
Virtual Network
Managed Disks
```

Customer still manages significant OS/application responsibility.

# Part 6 — Azure PaaS

Examples:

```text
Azure App Service
Azure SQL Database
Azure Functions platform
```

Azure operates more of the OS/runtime/infrastructure layer.

# Part 7 — Azure SaaS Concept

Microsoft SaaS examples exist outside Azure itself, such as Microsoft 365.

The service-model principle remains:

```text
more abstraction
→ less infrastructure administration
```

# Part 8 — Azure Serverless

Azure Functions is a core serverless compute example.

```text
Event
 ↓
Azure Function
 ↓
Business Logic
```

You manage function code/configuration; Azure manages server infrastructure and scaling mechanisms.

# Part 9 — Shared Responsibility in Azure

Responsibility changes by service model.

```text
On-prem:
customer manages nearly everything

IaaS:
Azure manages physical/hypervisor
customer manages guest OS/app/data

PaaS:
Azure manages more OS/runtime

SaaS:
provider manages application platform too
```

Identity/data responsibilities remain important for the customer.

# Part 10 — High Availability in Azure

Use redundant service instances/failure domains.

Examples:

```text
Availability Zones
zone-redundant services
load balancing
replication
```

A single VM is not a highly available application.

# Part 11 — Scalability

Azure supports:

```text
vertical scale
horizontal scale
autoscale
```

Examples:

```text
resize VM
scale VMSS instances
autoscale App Service
```

# Part 12 — Reliability

Reliability includes:

```text
redundancy
recovery
monitoring
backup
multi-zone architecture
tested failover
```

Azure service-specific reliability behavior differs, so production design requires service documentation.

# Part 13 — Predictability

Cloud predictability includes:

```text
performance planning
cost estimation
autoscaling rules
SLAs
monitoring
```

Managed services reduce some operational uncertainty but do not eliminate workload variability.

# Part 14 — Azure Global Infrastructure

Azure infrastructure is organized through:

```text
geographies
regions
availability zones
datacenters
edge/network infrastructure
```

Exact region counts evolve.

# Part 15 — Azure Region

A Region is a set of datacenters deployed within a geographic area and connected through low-latency networking.

Region selection depends on:

```text
service availability
latency
residency
reliability options
cost
```

# Part 16 — Azure Availability Zone

Availability zones are separated groups of datacenters within a Region with independent infrastructure.

```text
Region
├─ Zone 1
├─ Zone 2
└─ Zone 3
```

Use zones to reduce the impact of datacenter-level failures.

# Part 17 — Zonal Resource

A zonal resource is pinned to one zone.

Example concept:

```text
VM in Zone 1
```

You create additional replicas/resources in another zone for higher availability.

# Part 18 — Zone-Redundant Resource

A zone-redundant service distributes/replicates across zones according to service design.

The service may hide the physical replicas while providing regional resilience.

# Part 19 — Region Pairs

Many Azure regions have pairing relationships for specific platform/resiliency behaviors, but not every Region follows the same pairing model.

Do not assume every Region has a traditional pair; check current regional reliability guidance.

# Part 20 — Sovereign Regions / Clouds

Azure supports sovereign or specialized cloud environments designed for specific regulatory/government requirements.

They can differ in:

```text
service availability
endpoints
operations
compliance
```

# Part 21 — Azure Datacenter

A datacenter contains physical:

```text
compute
storage
network
power
cooling
security
```

Customers consume logical services rather than rack-level infrastructure.

# Part 22 — Azure Resource

A resource is an individual manageable Azure object.

Examples:

```text
VM
VNet
Storage Account
SQL Database
Key Vault
```

# Part 23 — Resource Group

A resource group is a logical management container for Azure resources.

```text
RG-App-Prod
├─ App Service
├─ Storage
└─ Key Vault
```

A resource belongs to one resource group at a time.

# Part 24 — Resource Group Lifecycle

Deleting a resource group deletes the contained resources.

Therefore resource grouping should consider:

```text
lifecycle
ownership
permissions
deployment
```

not only technology type.

# Part 25 — Subscription

Subscription is a major Azure boundary for:

```text
billing
quotas
management
access
policy
```

Large organizations commonly separate workloads/environments into multiple subscriptions.

# Part 26 — Management Group

Management groups organize subscriptions.

```text
Tenant Root Group
├─ Platform
│  ├─ Connectivity Subscription
│  └─ Identity Subscription
└─ Landing Zones
   ├─ Production
   └─ NonProduction
```

Policy/RBAC can be inherited down the hierarchy.

# Part 27 — Azure Resource Hierarchy

Simplified:

```text
Management Group
   ↓
Subscription
   ↓
Resource Group
   ↓
Resource
```

Microsoft Entra tenant sits above/alongside this resource-governance hierarchy as the identity directory.

# Part 28 — Microsoft Entra ID

Microsoft Entra ID is Azure's cloud identity and access directory service.

It supports:

```text
users
groups
applications
service principals
authentication
SSO
Conditional Access
identity governance
```

# Part 29 — Entra Tenant

A tenant is a dedicated Entra directory instance.

Azure subscriptions have a trust relationship with a tenant for authentication/authorization.

# Part 30 — Entra ID vs Active Directory Domain Services

Entra ID:

```text
cloud identity directory
OAuth/OIDC/SAML-style modern auth
cloud application identity
```

AD DS:

```text
traditional domain
Kerberos/NTLM
LDAP
domain join
Group Policy
```

They are related but not the same technology.

# Part 31 — Microsoft Entra Domain Services

Managed domain services provide capabilities such as:

```text
domain join
LDAP
Kerberos
NTLM
Group Policy compatibility
```

without customers managing traditional domain controllers for the managed domain.

# Part 32 — Azure RBAC

Azure Role-Based Access Control determines:

```text
who
can do what
at which scope
```

Scope can include:

```text
management group
subscription
resource group
resource
```

# Part 33 — RBAC Role Assignment

Concept:

```text
Principal
+
Role Definition
+
Scope
=
Role Assignment
```

Example:

```text
Alice
+
Reader
+
RG-App
```

# Part 34 — Built-In Roles

Examples:

```text
Owner
Contributor
Reader
User Access Administrator
```

Use narrower service-specific roles where possible.

# Part 35 — Owner vs Contributor

Broadly:

```text
Owner:
resource management + access delegation

Contributor:
resource management
but cannot grant all access like Owner
```

Use least privilege.

# Part 36 — Authentication vs Authorization

Authentication:

```text
Who are you?
```

Authorization:

```text
What can you do?
```

Entra handles authentication; Azure RBAC commonly handles Azure-resource authorization.

# Part 37 — Single Sign-On

SSO allows one corporate identity/session to access multiple applications.

```text
User
 ↓
Entra ID
 ↓
Azure + SaaS applications
```

# Part 38 — Multifactor Authentication

MFA adds a second/different verification factor.

Critical for privileged Azure accounts.

# Part 39 — Passwordless Authentication

Passwordless methods can use supported mechanisms such as:

```text
FIDO2/security keys
Windows Hello for Business
Microsoft Authenticator passwordless methods
```

Reducing passwords can reduce phishing risk.

# Part 40 — External Identities

Entra External ID/B2B-style collaboration allows external partners/users to access resources/applications without creating unmanaged local identities for every organization.

# Part 41 — Conditional Access

Conditional Access evaluates signals:

```text
user/group
location
device
risk
application
authentication strength
```

then applies controls:

```text
require MFA
block
require compliant device
```

# Part 42 — Zero Trust

Core principle:

```text
verify explicitly
use least privilege
assume breach
```

Network location alone does not grant trust.

# Part 43 — Defense in Depth

Layers:

```text
physical
identity
perimeter
network
compute
application
data
```

A failure in one layer should not expose the entire workload.

# Part 44 — Microsoft Defender for Cloud

Cloud security posture and workload-protection platform for Azure and connected environments.

Conceptual uses:

```text
security recommendations
secure score/posture
regulatory compliance views
workload protection plans
```

# Part 45 — Managed Identity

Azure resources can obtain Entra identities without storing application secrets.

```text
App Service / VM
   ↓ Managed Identity
Entra token
   ↓
Key Vault / Storage / SQL
```

This is a preferred workload-authentication pattern.

# Part 46 — System-Assigned Managed Identity

Lifecycle tied to one Azure resource.

Delete the resource:

```text
identity removed
```

Good for one-resource-specific workload identity.

# Part 47 — User-Assigned Managed Identity

Independent identity resource that can be assigned to multiple supported Azure resources.

Useful when identity lifecycle should not be tied to one compute resource.

# Part 48 — Azure Virtual Machines

IaaS compute.

Choose:

```text
image
VM size
disk
VNet/subnet
identity
availability option
```

Customer administers guest OS.

# Part 49 — VM Size

VM families optimize:

```text
general compute
CPU
memory
storage
GPU
HPC
```

Right-size based on metrics and workload requirements.

# Part 50 — Azure VM Images

Images can come from:

```text
Azure Marketplace
custom image
Azure Compute Gallery
```

Use controlled, patched, versioned images for repeatability.

# Part 51 — Managed Disks

Azure managed disks provide block storage for VMs.

Types can target:

```text
cost
performance
latency
IOPS
```

depending on disk class.

# Part 52 — OS Disk vs Data Disk

```text
OS disk:
boot operating system

data disk:
application/database data
```

Separate data can simplify lifecycle and performance design.

# Part 53 — Temporary Disk Concept

Some VM sizes offer temporary/local storage.

Do not place unique persistent data on storage that may be lost during lifecycle/host events.

# Part 54 — VM Availability Set

Availability sets provide logical grouping across fault/update domains for supported non-zonal VM designs.

Modern zone-capable designs often use Availability Zones where appropriate.

# Part 55 — Fault Domain

Fault domain represents shared physical failure characteristics such as:

```text
power
rack/network
```

Spreading VMs reduces correlated failures.

# Part 56 — Update Domain

Update domains group instances so planned platform maintenance does not update every instance simultaneously.

# Part 57 — Virtual Machine Scale Sets

VMSS manages a fleet of VM instances.

```text
Model
 ↓
VM Scale Set
 ├─ VM1
 ├─ VM2
 └─ VM3
```

Supports scaling and resilient fleet patterns.

# Part 58 — VMSS Autoscaling

Scale using metrics/schedules:

```text
CPU high
→ add instances

quiet night
→ reduce instances
```

Application should be stateless or externalize state.

# Part 59 — Azure Virtual Desktop

Managed desktop/application virtualization platform.

Use for:

```text
remote desktops
published apps
Windows user environments
```

# Part 60 — Azure App Service

PaaS for hosting web applications/APIs.

Supports managed platform capabilities such as:

```text
runtime
deployment
scaling
TLS integration
slots
monitoring
```

without customer-managed VM OS.

# Part 61 — App Service Plan

App Service Plan defines underlying compute capacity/pricing for App Service workloads.

Multiple apps can share a plan depending on architecture.

# Part 62 — Deployment Slots

Slots allow staged application deployments.

```text
production
staging
```

You can validate before swapping traffic.

# Part 63 — Azure Functions

Serverless event-driven compute.

Triggers can include:

```text
HTTP
timer
queue
event
storage
```

# Part 64 — Azure Container Instances

Run containers without managing a full orchestrator/VM cluster.

Useful for simple isolated container workloads.

# Part 65 — Azure Container Apps

Managed container application platform for microservices/serverless-container patterns.

Provides capabilities around:

```text
scaling
revisions
ingress
events
```

without directly managing Kubernetes control plane.

# Part 66 — Azure Kubernetes Service

AKS is managed Kubernetes.

Microsoft manages significant control-plane infrastructure while customer remains responsible for:

```text
workloads
RBAC
networking choices
images
secrets
cluster configuration
```

# Part 67 — Azure Container Registry

Private container image registry.

```text
Build
 ↓
ACR
 ↓
AKS / Container Apps / App Service
```

# Part 68 — Azure Virtual Network

VNet is Azure's software-defined private network.

```text
VNet 10.20.0.0/16
├─ Web subnet
├─ App subnet
└─ DB subnet
```

# Part 69 — Subnet

Subnets divide a VNet IP space.

Azure subnets are regional constructs inside the VNet; zonal resources in different AZs can use the same regional VNet/subnet depending on service design.

# Part 70 — Network Security Group

NSG filters inbound/outbound traffic for supported:

```text
subnets
network interfaces
```

Rules use:

```text
priority
source
destination
port
protocol
allow/deny
```

# Part 71 — NSG Stateful Behavior

NSGs are stateful.

Allowed connection return traffic is handled as part of the established flow.

# Part 72 — Application Security Group

ASGs let you group VM NICs logically and use those groups in NSG rules.

Example:

```text
ASG-Web → ASG-App TCP/8443
```

This reduces IP-specific rules.

# Part 73 — User-Defined Routes

Azure route tables can override/add routes.

Example:

```text
0.0.0.0/0
→ Azure Firewall/NVA
```

Useful for forced tunneling/security inspection.

# Part 74 — VNet Peering

Connect VNets privately through Azure backbone.

```text
VNet A ↔ VNet B
```

Peering is not inherently transitive.

# Part 75 — Azure VPN Gateway

Managed VPN connectivity.

Use for:

```text
site-to-site
point-to-site
VNet-to-VNet
```

depending on gateway/configuration.

# Part 76 — Azure ExpressRoute

Private dedicated connectivity from on-premises/network provider into Microsoft cloud connectivity.

Use for enterprise hybrid connectivity requiring more predictable/private routing than Internet VPN.

# Part 77 — Azure DNS

Authoritative DNS hosting service.

Azure also provides private DNS capabilities for internal names.

# Part 78 — Private DNS Zone

Private DNS zones resolve names inside linked VNets without exposing them publicly.

Common with Private Endpoint architectures.

# Part 79 — Public Endpoint

Service reachable through a public IP/address.

Public does not necessarily mean anonymously open; authentication/firewall policy can still restrict access.

# Part 80 — Private Endpoint

Private Endpoint creates a private IP NIC in your VNet for a supported Azure PaaS service.

```text
VM
 ↓ private IP
Private Endpoint
 ↓
Storage / SQL / Key Vault
```

# Part 81 — Azure Private Link

Private Link is the underlying private connectivity model for private endpoints and private services.

Goal:

```text
access PaaS privately
without traversing public Internet
```

# Part 82 — Service Endpoints Concept

VNet service endpoints provide a different private-access model by extending VNet identity/routing to supported services over the Azure backbone.

Private Endpoint usually provides a private IP and stronger private-service isolation model.

# Part 83 — Azure NAT Gateway

Managed outbound NAT for subnets.

```text
Private VM
 ↓
NAT Gateway
 ↓
Internet
```

Provides controlled scalable outbound public connectivity.

# Part 84 — Azure Load Balancer

Layer 4 load balancing.

Use for:

```text
TCP/UDP
internal/public load balancing
VM/VMSS traffic
```

# Part 85 — Application Gateway

Layer 7 regional web traffic load balancer.

Capabilities include:

```text
HTTP/S routing
TLS
path/host routing
WAF option
```

# Part 86 — Azure Front Door

Global application-delivery and routing service at Microsoft's edge.

Use for:

```text
global HTTP/S acceleration
load balancing
WAF
multi-region origin routing
```

# Part 87 — Traffic Manager

DNS-based global traffic distribution.

It directs DNS responses according to policies such as:

```text
priority
weighted
performance
geographic
```

Unlike Front Door, it is DNS-based rather than a full HTTP reverse-proxy service.

# Part 88 — Load Balancer vs Application Gateway

```text
Load Balancer:
Layer 4 TCP/UDP

Application Gateway:
Layer 7 HTTP/S regional

Front Door:
global HTTP/S edge

Traffic Manager:
DNS routing
```

This is a useful exam/service-recognition matrix.

# Part 89 — Azure Storage Account

Storage account is the namespace/control resource for Azure Storage services.

Can provide:

```text
Blob
Files
Queues
Tables
```

depending on account type/configuration.

# Part 90 — Blob Storage

Object storage for:

```text
files
images
backups
logs
data lake
static content
```

Containers organize blobs inside a storage account.

# Part 91 — Blob Access Tiers

Common access tiers:

```text
Hot
Cool
Cold
Archive
```

designed around access frequency and retrieval requirements.

Exact pricing/minimum retention differs by tier.

# Part 92 — Hot Tier

For frequently accessed data.

Higher storage cost than colder tiers but lower access/retrieval friction.

# Part 93 — Cool Tier

For infrequently accessed data that still needs online retrieval.

Use when access frequency is lower but latency still matters.

# Part 94 — Cold Tier

For even less frequently accessed online data than Cool, with pricing/retention tradeoffs.

# Part 95 — Archive Tier

Offline/archive-oriented storage.

Lowest storage cost profile but data must be rehydrated before normal access, so retrieval time is longer.

# Part 96 — Azure Files

Managed file shares using supported protocols such as SMB and NFS depending on service tier/config.

Use for shared filesystem workloads.

# Part 97 — Azure Queue Storage

Simple message queue in Azure Storage.

Use for basic asynchronous decoupling.

Azure Service Bus provides more advanced enterprise messaging capabilities.

# Part 98 — Azure Table Storage

NoSQL key/attribute storage model within Azure Storage.

For globally distributed richer NoSQL, Azure Cosmos DB is the more prominent service.

# Part 99 — Storage Redundancy — LRS

Locally Redundant Storage keeps multiple copies within a single physical location/datacenter region boundary according to service design.

Lowest geographic redundancy.

# Part 100 — Storage Redundancy — ZRS

Zone-Redundant Storage replicates across availability zones in the primary Region.

Useful for zone-failure resilience.

# Part 101 — Storage Redundancy — GRS

Geo-Redundant Storage replicates locally in primary Region and asynchronously to a secondary Region.

Read access to secondary depends on whether read-access variant is selected.

# Part 102 — RA-GRS

Read-Access GRS provides read access to the secondary Region in addition to geo-replication.

# Part 103 — GZRS

Geo-Zone-Redundant Storage combines:

```text
zone redundancy in primary Region
+
geo replication to secondary Region
```

# Part 104 — RA-GZRS

Read-access variant of GZRS provides read access to secondary Region.

# Part 105 — Storage Redundancy Selection

Choose based on:

```text
required durability
zone failure tolerance
regional DR
read access
cost
```

Do not choose the strongest option automatically without business requirements.

# Part 106 — AzCopy

CLI utility for copying data to/from Azure Storage.

Example concept:

```bash
azcopy copy ./data "https://storage.../container?<SAS>"
```

Protect SAS tokens as credentials.

# Part 107 — Azure Storage Explorer

GUI tool for interacting with Azure Storage.

Useful for:

```text
Blob
Files
Queues
Tables
local/emulated/storage accounts
```

# Part 108 — Azure File Sync

Synchronizes on-premises Windows Server file shares with Azure Files.

Use for hybrid file-service/cache architectures.

# Part 109 — Azure Data Box

Physical data-transfer appliance/service for large data movement where network transfer is impractical.

```text
on-prem data
 ↓ Data Box
ship
 ↓
Azure
```

# Part 110 — Azure Migrate

Central migration/discovery/assessment service family for moving servers/databases/apps to Azure.

Use for:

```text
discovery
assessment
migration planning
migration orchestration
```

# Part 111 — Azure SQL Database

Fully managed relational PaaS SQL database.

Customer focuses on:

```text
schema
queries
users
data
performance design
```

Microsoft manages OS/database platform infrastructure.

# Part 112 — Azure SQL Managed Instance

Managed SQL Server-compatible instance model with greater instance-level compatibility than Azure SQL Database for many migration scenarios.

# Part 113 — SQL Server on Azure VM

IaaS SQL:

```text
full OS/SQL control
more operational responsibility
```

Useful when application needs unsupported instance/OS-level behavior.

# Part 114 — Azure Database for PostgreSQL

Managed PostgreSQL service.

Use when:

```text
relational PostgreSQL workload
managed HA/backup/platform operations desired
```

# Part 115 — Azure Cosmos DB

Globally distributed NoSQL database platform supporting multiple APIs/data models.

Recognition:

```text
low-latency globally distributed NoSQL
```

# Part 116 — Cosmos DB Distribution Concept

Designed for replication and application access across Azure Regions.

Architects choose consistency/distribution according to application needs.

# Part 117 — Azure Cache Concept

Managed in-memory caching services improve application latency and reduce database load.

Use for:

```text
sessions
hot data
query results
```

# Part 118 — Azure Synapse Analytics

Analytics platform combining data warehousing/big-data integration capabilities.

Recognition:

```text
enterprise analytics / data warehouse / integrated analytics
```

# Part 119 — Azure Service Bus

Enterprise message broker.

Supports:

```text
queues
topics/subscriptions
reliable enterprise messaging
```

More advanced messaging semantics than simple Storage Queue.

# Part 120 — Azure Event Grid

Event routing service.

```text
event source
 ↓
Event Grid
 ↓
handler
```

Used for reactive/event-driven integration.

# Part 121 — Azure Event Hubs

High-throughput event/stream ingestion.

Use for:

```text
telemetry
logs
IoT/event streams
```

# Part 122 — Key Vault

Stores/manages:

```text
secrets
keys
certificates
```

Applications should retrieve secrets using managed identities rather than embedding them.

# Part 123 — Azure Encryption

Azure supports encryption:

```text
at rest
in transit
```

through service-specific encryption plus customer-managed key options where supported.

# Part 124 — Microsoft Purview

Data governance/compliance family.

AZ-900 recognition centers on governance, data discovery/classification, catalog/compliance-related capabilities.

# Part 125 — Azure Policy

Policy evaluates/enforces resource rules.

Examples:

```text
allowed locations
required tags
deny public IP
audit encryption
deploy configuration
```

Policy works at resource-governance level.

# Part 126 — Policy Definition

Policy definition contains a condition and effect.

Concept:

```text
IF resource location not approved
THEN deny
```

# Part 127 — Policy Assignment

Apply policy to a scope:

```text
management group
subscription
resource group
resource
```

Inheritance helps govern at scale.

# Part 128 — Azure Initiative

An initiative groups multiple policy definitions.

Example:

```text
Security Baseline Initiative
├─ require encryption
├─ deny public exposure
└─ require logs
```

# Part 129 — Resource Lock

Locks help prevent accidental changes.

Types:

```text
ReadOnly
CanNotDelete
```

Locks are governance controls, not IAM permissions.

# Part 130 — Lock vs RBAC

RBAC:

```text
who can perform actions
```

Lock:

```text
additional protection from change/delete
```

An Owner can still encounter a resource lock until the lock is removed by an authorized identity.

# Part 131 — Azure Tags

Metadata:

```text
Environment=Prod
Owner=Finance
CostCenter=1204
```

Use for:

```text
cost
operations
governance
automation
```

# Part 132 — Tags Do Not Automatically Inherit Everywhere

Do not assume child resources inherit parent tags automatically in every scenario.

Azure Policy/automation can enforce/inherit tagging patterns.

# Part 133 — Azure Portal

Web-based management interface.

Useful for:

```text
learning
visual administration
monitoring
manual investigation
```

# Part 134 — Azure Cloud Shell

Browser shell with Azure tooling and authenticated context.

Supports:

```text
Bash
PowerShell
Azure CLI
Azure PowerShell
```

depending on shell environment.

# Part 135 — Azure CLI

Cross-platform command line.

Examples:

```bash
az login
az account show
az group list
az vm list
```

# Part 136 — Azure PowerShell

PowerShell module family:

```powershell
Connect-AzAccount
Get-AzContext
Get-AzResourceGroup
Get-AzVM
```

Useful for Windows/PowerShell-centric administration and automation.

# Part 137 — Azure Resource Manager

ARM is the Azure control-plane deployment/management layer.

Requests from:

```text
portal
CLI
PowerShell
SDK
templates
```

flow through Azure Resource Manager APIs.

# Part 138 — ARM Template

JSON Infrastructure-as-Code definition.

Concept:

```json
{
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts"
    }
  ]
}
```

ARM templates support declarative repeatable deployment.

# Part 139 — Bicep

Bicep is a domain-specific declarative language for Azure Resource Manager resources.

Example:

```bicep
resource rgStorage 'Microsoft.Storage/storageAccounts@...' = {
  name: 'example'
  location: resourceGroup().location
  ...
}
```

It compiles to ARM template semantics.

# Part 140 — IaC Benefit

```text
Git
 ↓
review
 ↓
ARM/Bicep
 ↓
Azure Resource Manager
 ↓
repeatable resources
```

This reduces manual drift.

# Part 141 — Azure Arc

Azure Arc extends Azure management/governance capabilities to resources outside native Azure.

Examples:

```text
on-prem servers
other-cloud servers
Kubernetes
data services in supported models
```

Think:

```text
Azure management plane beyond Azure datacenters
```

# Part 142 — Azure Advisor

Recommendations across areas such as:

```text
reliability
security
performance
cost
operational excellence
```

depending on current Advisor categorization/service.

# Part 143 — Azure Service Health

Shows Azure service issues relevant to your resources/subscriptions.

Concepts:

```text
service issues
planned maintenance
health advisories
```

# Part 144 — Azure Status vs Service Health

Azure Status:

```text
broad public platform status
```

Service Health:

```text
personalized/subscription-relevant service health
```

# Part 145 — Azure Resource Health

Helps assess health of individual Azure resources.

Use when:

```text
Is this VM/resource experiencing an Azure platform issue?
```

# Part 146 — Azure Monitor

Azure's core monitoring platform.

Works with:

```text
metrics
logs
alerts
dashboards/workbooks
application telemetry
```

# Part 147 — Azure Monitor Metrics

Numeric time series:

```text
CPU
requests
latency
disk
network
```

Used for charts/alerts/autoscale.

# Part 148 — Log Analytics

Azure Monitor Logs workspace/query platform.

Uses Kusto Query Language (KQL).

Concept:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
```

# Part 149 — Application Insights

Application performance monitoring capability within Azure Monitor.

Provides:

```text
requests
dependencies
exceptions
traces
distributed application telemetry
```

# Part 150 — Azure Monitor Alerts

Alerts evaluate conditions and notify/action.

Sources can include:

```text
metrics
logs
activity
service health
```

depending on alert type.

# Part 151 — Action Group

Alert actions can target:

```text
email/SMS/push
webhook
automation
functions
ITSM integrations
```

according to supported action types.

# Part 152 — Activity Log

Subscription-level control-plane events.

Answers:

```text
who changed/deleted resource?
what operation?
when?
```

Comparable conceptually to cloud audit/control-plane logs.

# Part 153 — Azure Cost Factors

Cost can depend on:

```text
resource type
size
Region
usage duration
storage
transactions
network egress
licenses
support
```

# Part 154 — Azure Pricing Calculator

Estimate costs before deployment.

Use:

```text
service
Region
size
hours
storage
transfer
```

to model architecture.

# Part 155 — Cost Management + Billing

Provides:

```text
cost analysis
budgets
alerts
allocation
billing scopes
exports
```

for Azure spending governance.

# Part 156 — Azure Budgets

Set thresholds against cost/usage scopes.

Budget alerts do not automatically stop resources unless automation/policy is explicitly built around them.

# Part 157 — Azure Reservations

Commitment model for eligible resources to reduce cost for predictable usage.

Use after measuring stable baseline demand.

# Part 158 — Azure Savings Plan for Compute Concept

Commit to eligible compute spend for a term in exchange for discounted rates with flexibility across supported compute usage.

# Part 159 — Azure Spot Virtual Machines

Use unused Azure capacity at lower price but subject to eviction.

Good:

```text
batch
CI
fault-tolerant workers
```

Poor:

```text
single critical database
```

# Part 160 — Azure Hybrid Benefit

Allows eligible existing Windows Server/SQL Server licenses with Software Assurance/subscriptions to reduce Azure costs in supported scenarios.

# Part 161 — Bandwidth / Egress Cost

Data leaving Azure or crossing certain boundaries can incur charges.

Model:

```text
Internet egress
inter-region transfer
cross-zone/service transfer
```

according to current pricing.

# Part 162 — Azure Marketplace

Catalog for Microsoft/third-party cloud software/services/solutions.

Can simplify procurement and deployment.

# Part 163 — Service-Level Agreement Concept

Azure services publish service-specific SLAs.

Your application SLA depends on:

```text
architecture
dependencies
deployment mode
service SLAs
```

not merely one Azure component.

# Part 164 — Composite Availability

If two serially required independent services each have availability A and B:

```text
overall ≈ A × B
```

Example:

```text
0.999 × 0.999 = 0.998001
```

Architecture redundancy can change this model.

# Part 165 — Azure Well-Architected Framework

Azure WAF uses five pillars:

```text
Reliability
Security
Cost Optimization
Operational Excellence
Performance Efficiency
```

Use as architecture review lenses.

# Part 166 — Reliability Pillar

Design:

```text
failure handling
redundancy
recovery
testing
```

Use availability zones and service-specific resilient modes where justified.

# Part 167 — Security Pillar

Focus:

```text
identity
network
data protection
governance
security operations
```

# Part 168 — Cost Optimization Pillar

Focus:

```text
right-size
budgets
reservations
remove waste
architecture value
```

# Part 169 — Operational Excellence Pillar

Focus:

```text
automation
monitoring
deployment practice
incident management
continuous improvement
```

# Part 170 — Performance Efficiency Pillar

Focus:

```text
resource selection
scaling
data design
caching
monitoring
```

# Part 171 — Microsoft Cloud Adoption Framework

CAF provides guidance for cloud adoption:

```text
strategy
plan
ready
adopt
govern
secure
manage
```

and organizational/platform practices.

# Part 172 — Azure Landing Zone

A landing zone provides governed foundation for enterprise workloads.

Common elements:

```text
management groups
subscriptions
identity
network
policy
logging
security
platform services
```

# Part 173 — Platform Landing Zone

Shared foundation areas:

```text
identity
connectivity
management
security
```

commonly live in platform subscriptions.

# Part 174 — Application Landing Zone

Subscription/resource environment where an application workload is deployed under inherited platform governance.

# Part 175 — Azure Policy vs Defender for Cloud

```text
Azure Policy:
govern/configure/audit resource compliance rules

Defender for Cloud:
security posture + workload protection capabilities
```

They integrate but have different primary purposes.

# Part 176 — Azure Policy vs RBAC

```text
RBAC:
who can do what

Policy:
what configurations are allowed/required
```

# Part 177 — Service Health vs Monitor

```text
Service Health:
Azure service incidents/maintenance relevant to you

Azure Monitor:
your workload/resource telemetry
```

# Part 178 — Advisor vs Cost Management

```text
Advisor:
recommendations

Cost Management:
actual cost analysis/budgets/allocation
```

# Part 179 — App Service vs VM

```text
VM:
more OS control
more administration

App Service:
PaaS
less OS management
application-focused
```

# Part 180 — VMSS vs Availability Set

```text
VMSS:
fleet/scaling model

Availability Set:
fault/update-domain grouping for VMs
```

VMSS can also use zonal/resilient architectures.

# Part 181 — Front Door vs Application Gateway

```text
Front Door:
global edge HTTP/S routing

Application Gateway:
regional HTTP/S load balancing
```

# Part 182 — ExpressRoute vs VPN Gateway

```text
VPN Gateway:
encrypted IPsec over Internet

ExpressRoute:
private dedicated connectivity through provider circuits
```

# Part 183 — Private Endpoint vs Public Endpoint

```text
Public endpoint:
public network address

Private endpoint:
private IP inside VNet for supported PaaS
```

# Part 184 — Storage Service Recognition

```text
object → Blob
shared file → Azure Files
simple queue → Queue Storage
NoSQL key table → Table Storage
VM block disk → Managed Disk
```

# Part 185 — Migration Recognition

```text
assess/migrate servers → Azure Migrate
large offline data → Data Box
copy storage data → AzCopy
hybrid file sync → Azure File Sync
GUI storage admin → Storage Explorer
```

# Part 186 — Identity Recognition

```text
cloud directory → Entra ID
managed AD-compatible domain → Entra Domain Services
resource authorization → Azure RBAC
risk/condition auth rules → Conditional Access
workload identity → Managed Identity
```

# Part 187 — Governance Recognition

```text
enforce resource rules → Azure Policy
prevent delete/change → Resource Lock
metadata/cost ownership → Tags
resource organization → RG/subscription/MG
data governance → Purview
```

# Part 188 — Management Recognition

```text
browser → portal
browser terminal → Cloud Shell
cross-platform CLI → Azure CLI
PowerShell → Azure PowerShell
resource control plane → ARM
IaC → ARM/Bicep
hybrid management → Azure Arc
```

# Part 189 — Monitoring Recognition

```text
metrics/logs → Azure Monitor
query logs → Log Analytics
app telemetry → Application Insights
platform incident → Service Health
recommendations → Advisor
```

# Part 190 — Azure CLI Login

Interactive:

```bash
az login
```

In enterprise automation prefer managed identity/service principal/workload federation rather than personal interactive login.

# Part 191 — Show Current Subscription

```bash
az account show \
  --query '{Name:name,Subscription:id,Tenant:tenantId}' \
  --output table
```

Check before modifying resources.

# Part 192 — List Subscriptions

```bash
az account list \
  --query '[].{Name:name,Id:id,State:state}' \
  --output table
```

# Part 193 — Set Subscription

```bash
az account set --subscription "<subscription-id-or-name>"
```

Verify again with:

```bash
az account show
```

# Part 194 — List Resource Groups

```bash
az group list \
  --query '[].{Name:name,Location:location}' \
  --output table
```

# Part 195 — List VMs

```bash
az vm list \
  --show-details \
  --query '[].{Name:name,RG:resourceGroup,Location:location,State:powerState}' \
  --output table
```

# Part 196 — List VNets

```bash
az network vnet list \
  --query '[].{Name:name,RG:resourceGroup,Location:location}' \
  --output table
```

# Part 197 — PowerShell Context

```powershell
Get-AzContext
Get-AzSubscription
```

Set:

```powershell
Set-AzContext -Subscription "<id>"
```

# Part 198 — PowerShell Resource Discovery

```powershell
Get-AzResourceGroup
Get-AzVM
Get-AzVirtualNetwork
```

Use `Get-*` first for read-oriented exploration.

# Part 199 — Bicep Example

Conceptual resource group deployment file:

```bicep
param location string = resourceGroup().location

resource stg 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'uniquestorageexample'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
```

API versions should be checked against current resource-provider documentation for real deployment.

# Part 200 — Azure Architecture Pattern

```text
Azure DNS
   ↓
Front Door + WAF
   ↓
Application Gateway
   ↓
App Service / VMSS across zones
   ↓
Azure SQL zone-redundant/HA design
   ↓
Blob Storage
```

Add:

```text
Entra
Key Vault
Monitor
Defender
Policy
Backup
```

# Part 201 — Azure Serverless Pattern

```text
Client
 ↓
API Management
 ↓
Azure Functions
 ↓
Cosmos DB
 ↓
Event Grid / Service Bus
```

# Part 202 — Azure Hybrid Pattern

```text
On-Prem
   |
ExpressRoute
 + backup VPN
   |
Hub VNet
   |
Spoke VNets
```

Centralize:

```text
firewall
DNS
shared services
```

# Part 203 — Hub-and-Spoke Networking

```text
            Spoke App1
                |
On-Prem -- Hub -- Spoke App2
                |
            Spoke Data
```

Hub contains shared connectivity/security services.

# Part 204 — Azure Firewall Concept

Managed stateful network firewall service.

Use for centralized:

```text
network/application rules
threat-intelligence-related filtering
logging
```

in hub architectures.

# Part 205 — DDoS Protection Concept

Azure provides platform DDoS protections and enhanced DDoS Protection offerings.

Use alongside WAF and application security.

# Part 206 — API Management

Managed API gateway/lifecycle service.

Use for:

```text
publish APIs
authentication/policies
rate limiting
analytics
developer portal
```

# Part 207 — Azure Logic Apps

Low-code/workflow integration service.

Use for:

```text
business workflows
connectors
event/process automation
```

# Part 208 — Azure Backup

Managed backup service for supported Azure/on-prem workloads.

Use:

```text
vaults
policies
retention
recovery
```

# Part 209 — Azure Site Recovery

Disaster-recovery replication/orchestration for supported VMs/workloads.

Concept:

```text
source
 ↓ replication
recovery location
 ↓ failover
```

# Part 210 — Azure Cost Troubleshooting

If bill spikes:

```text
Cost Management
 ↓
scope
 ↓
service
 ↓
resource group/resource
 ↓
meter
 ↓
tag/owner
```

Then identify:

```text
scale event
egress
idle VM
storage growth
database tier
```

# Part 211 — Azure AccessDenied Troubleshooting

Check:

```text
correct tenant?
correct subscription?
principal?
role assignment?
scope?
deny assignment/policy?
token refreshed?
```

Do not immediately grant Owner.

# Part 212 — VM Unreachable Troubleshooting

Check:

```text
VM power
NIC
private/public IP
NSG
route
Azure Firewall/NVA
guest firewall
service listening
```

# Part 213 — Private Endpoint Troubleshooting

Check:

```text
private endpoint approved?
private DNS?
VNet link?
NSG/routes?
public access disabled?
application resolving private IP?
```

# Part 214 — Storage Access Troubleshooting

Check:

```text
account/network firewall
Entra/RBAC
SAS/key
container/share permissions
private endpoint/DNS
encryption/key access
```

# Part 215 — Azure SQL Connectivity Troubleshooting

Check:

```text
server/database state
private/public endpoint
DNS
firewall
credentials/Entra
connection string
TLS
application pool
```

# Part 216 — Service Health Incident Workflow

```text
alert detected
 ↓
check Service Health
 ↓
identify affected Region/service
 ↓
apply workload failover/runbook
 ↓
communicate
 ↓
recover/validate
```

# Part 217 — AZ-900 Question Strategy

First identify category:

```text
cloud concept
architecture/service
management/governance
```

Then select the service whose primary purpose matches.

# Part 218 — Exam Distractor Strategy

Example:

```text
Need prevent resource deletion:
Resource Lock
```

Distractors might be:

```text
RBAC
Policy
Tag
```

All are real Azure features, but only lock directly matches accidental deletion protection.

# Part 219 — Azure Engineer Mental Model

Do not think only:

```text
Create VM
```

Think:

```text
Tenant?
Subscription?
Resource Group?
Region/Zones?
VNet?
Identity?
RBAC?
Policy?
Monitoring?
Backup?
Cost?
DR?
IaC?
```

# Part 220 — Course Transition

AZ-900 gives provider fundamentals.

Later Azure Administration must go deeper into:

```text
identity administration
networking
compute
storage
governance
monitoring
backup
automation
```

This course builds the vocabulary and architecture map needed for that next level.

---

# Enhanced Deep-Study Layer — Microsoft Azure Fundamentals

This enhanced layer preserves the complete uploaded Course 50 as the source baseline and adds deeper engineering material beyond the AZ-900 minimum: identity-plane vs resource-plane authorization, PIM, workload federation, landing zones, effective routes and NSGs, hybrid DNS, private endpoints, hub-spoke routing, VM/VMSS/image lifecycle, App Service and Functions scaling, AKS/ACR responsibility, data-protection semantics, Cosmos DB design, messaging, Key Vault, observability/KQL, backup/DR, FinOps, and safe Bicep/ARM operations.

Certification dates, percentages, product names, and live commercial details in the original course remain source-derived. The enhancement below focuses on durable engineering concepts and does not silently replace those source claims.

The additional learning sequence is:

```text
Concept
  ↓
Detailed Explanation
  ↓
Architecture / Failure Model
  ↓
CLI / PowerShell / Config / Code
  ↓
Expected Behavior
  ↓
Why It Works
  ↓
Production Example
  ↓
Troubleshooting
  ↓
Best Practice
```

## Advanced Deep Dive 1 — Azure Scope Hierarchy and Inheritance

### Concept and Detailed Explanation
Azure governance is evaluated through nested scopes: management group, subscription, resource group, and resource. RBAC and Policy assignments can inherit downward, so a permission or deny at a parent can affect thousands of descendant resources.

### Architecture / Failure Model
```text
Management Group
  ↓
Subscription
  ↓
Resource Group
  ↓
Resource
```

### Command / Config / Calculation
```text
az account management-group list -o table
az account show -o table
az group list -o table
```

### Expected Behavior
The engineer can state which parent scopes influence a resource before changing its local configuration.

### Why It Works
Azure evaluates governance against the effective hierarchy, not only the object currently visible in the portal.

### Production Example
A corporate policy denying unapproved regions is assigned at a management group so every production subscription inherits it.

### Troubleshooting Workflow
```text
Unexpected denial
  ↓
identify resource ID
  ↓
walk parent scopes
  ↓
inspect RBAC + Policy inheritance
  ↓
check exemption/deny assignment
```

### Best Practice
Always troubleshoot Azure permissions and policy from the resource upward through every parent scope.

---

## Advanced Deep Dive 2 — Microsoft Entra Tenant vs Azure Subscription

### Concept and Detailed Explanation
A Microsoft Entra tenant is the identity directory; an Azure subscription is a resource, quota, billing, and governance boundary that trusts one Entra tenant for authentication. Moving or associating subscriptions changes identity context and must be planned carefully.

### Architecture / Failure Model
```text
Entra Tenant
  ↓ trust
Azure Subscription
  ↓
Resources
```

### Command / Config / Calculation
```text
az account show --query '{subscription:id,tenant:tenantId,user:user}' -o json
```

### Expected Behavior
The active tenant and subscription are unambiguous before administration begins.

### Why It Works
Azure separates identity-directory lifecycle from resource-subscription lifecycle.

### Production Example
A consultant can authenticate to multiple tenants but must intentionally select the correct tenant/subscription before changing production.

### Troubleshooting Workflow
```text
Wrong identity context
  ↓
az account show
  ↓
active tenant?
  ↓
active subscription?
  ↓
re-authenticate/select
```

### Best Practice
Make tenant and subscription verification the first line of every privileged runbook.

---

## Advanced Deep Dive 3 — Azure RBAC Effective Access

### Concept and Detailed Explanation
Azure RBAC authorization combines principal, role definition, scope, inheritance, and deny assignments. A broad role at subscription scope can dominate many narrower resource-group assumptions, while deny assignments can block actions even when an allow role exists.

### Architecture / Failure Model
```text
Principal
 + Role Definition
 + Scope/Inheritance
 + Deny Assignments
 = Effective Access
```

### Command / Config / Calculation
```text
az role assignment list --assignee <OBJECT_ID> --all -o table
az role definition list --name Reader -o json
```

### Expected Behavior
Access decisions can be explained by exact role assignments and scope rather than guessed from group names.

### Why It Works
RBAC is hierarchical and additive for allows, while explicit deny mechanisms can constrain otherwise allowed operations.

### Production Example
An engineer has Contributor on a resource group but cannot delete a protected resource because a deny assignment created by a managed service applies.

### Troubleshooting Workflow
```text
AuthorizationFailed
  ↓
principal object ID
  ↓
role assignments
  ↓
parent scopes
  ↓
deny assignments
  ↓
token freshness
```

### Best Practice
Never grant Owner as a diagnostic shortcut; identify the missing action and effective scope.

---

## Advanced Deep Dive 4 — Entra Directory Roles vs Azure RBAC

### Concept and Detailed Explanation
Entra directory roles govern identity-directory operations such as managing users or Conditional Access. Azure RBAC governs Azure resource operations such as creating VMs or reading storage. Being Global Administrator does not automatically mean full resource access, and being Subscription Owner does not automatically mean full Entra administration.

### Architecture / Failure Model
```text
Identity Plane: Entra directory roles
Resource Plane: Azure RBAC
```

### Command / Config / Calculation
```text
az ad signed-in-user show -o json
az role assignment list --all -o table
```

### Expected Behavior
The team can distinguish identity-plane administration from Azure resource-plane administration.

### Why It Works
Microsoft intentionally separates directory governance from resource authorization.

### Production Example
A security administrator can manage authentication policy without permission to deploy production VMs.

### Troubleshooting Workflow
```text
Cannot perform action
  ↓
is it Entra or Azure resource operation?
  ↓
check corresponding role system
```

### Best Practice
Classify every privilege request as identity-plane or resource-plane before assigning a role.

---

## Advanced Deep Dive 5 — Privileged Identity Management and Just-in-Time Administration

### Concept and Detailed Explanation
Microsoft Entra Privileged Identity Management (PIM) supports eligible rather than permanently active privileged assignments, activation workflows, MFA/approval requirements, time limits, and audit. It reduces standing privilege while keeping emergency administration available.

### Architecture / Failure Model
```text
Eligible admin
  ↓ activate
MFA/approval
  ↓
Time-bounded privileged role
  ↓ expires
```

### Command / Config / Calculation
```text
Operational design:
Eligible role: Contributor
Activation: 1 hour
MFA: required
Approval: production admin
Justification: ticket ID
```

### Expected Behavior
Privileged rights exist only during authorized activation windows.

### Why It Works
Reducing standing privilege reduces the time window in which compromised credentials carry powerful permissions.

### Production Example
Production subscription administrators activate Owner only for an approved break-fix task and return automatically to nonprivileged state afterward.

### Troubleshooting Workflow
```text
Admin cannot activate
  ↓
eligibility
  ↓
MFA/approval
  ↓
activation policy
  ↓
role assignment propagation
```

### Best Practice
Use permanent active privilege only when a documented operational requirement justifies it.

---

## Advanced Deep Dive 6 — Managed Identity Token Flow

### Concept and Detailed Explanation
Managed identities let an Azure resource request short-lived Entra tokens without storing client secrets. The workload asks the Azure identity endpoint for a token for a specific resource/audience, then presents that token to Key Vault, Storage, SQL, or another supported service.

### Architecture / Failure Model
```text
VM/App Service
  ↓ managed identity token
Entra ID
  ↓ short-lived token
Key Vault / Storage / SQL
```

### Command / Config / Calculation
```text
az vm identity show -g <RG> -n <VM> 2>/dev/null || true
az webapp identity show -g <RG> -n <APP> 2>/dev/null || true
```

### Expected Behavior
The workload authenticates without an embedded password or certificate file.

### Why It Works
Azure binds an identity to the resource and issues temporary tokens based on that identity.

### Production Example
An App Service reads a Key Vault secret with its managed identity, so deployment packages contain no secret.

### Troubleshooting Workflow
```text
Managed identity 403
  ↓
identity enabled?
  ↓
correct principal ID?
  ↓
RBAC/access policy?
  ↓
resource audience/token?
  ↓
network/private endpoint
```

### Best Practice
Prefer managed identity for Azure-hosted workloads whenever the target service supports Entra authentication.

---

## Advanced Deep Dive 7 — System-Assigned vs User-Assigned Managed Identity

### Concept and Detailed Explanation
A system-assigned managed identity is created and deleted with one resource. A user-assigned managed identity has an independent lifecycle and can be attached to multiple supported resources. The choice affects reuse, lifecycle coupling, and permission management.

### Architecture / Failure Model
```text
System-assigned:
Resource ↔ Identity same lifecycle

User-assigned:
Identity
 ├─ App A
 ├─ App B
 └─ VMSS
```

### Command / Config / Calculation
```text
az identity list -o table
az vm identity show -g <RG> -n <VM> 2>/dev/null || true
```

### Expected Behavior
The selected identity type matches whether permissions should follow one resource or a reusable workload role.

### Why It Works
Identity lifecycle is either coupled to the compute resource or deliberately separated.

### Production Example
A blue/green application reuses one user-assigned identity across both deployment environments so downstream permissions do not change during cutover.

### Troubleshooting Workflow
```text
Identity missing after rebuild
  ↓
was it system-assigned?
  ↓
new principal ID?
  ↓
recreate role assignments or use user-assigned identity
```

### Best Practice
Use user-assigned identities when identity continuity must survive compute replacement.

---

## Advanced Deep Dive 8 — Service Principals and Workload Identity Federation

### Concept and Detailed Explanation
External automation may need an Entra application/service principal. Instead of creating a long-lived client secret, workload identity federation can trust an external OIDC identity such as a CI platform and exchange it for short-lived Azure tokens.

### Architecture / Failure Model
```text
CI OIDC token
  ↓ federation trust
Entra application/service principal
  ↓
short-lived Azure token
```

### Command / Config / Calculation
```text
az ad app federated-credential list --id <APP_ID> 2>/dev/null || true
az ad sp show --id <CLIENT_ID> 2>/dev/null || true
```

### Expected Behavior
CI authenticates to Azure without storing a reusable cloud secret.

### Why It Works
Federation converts externally proven identity into temporary Azure credentials.

### Production Example
A GitHub Actions deployment receives a token only for the production deploy role and only from the approved repository/environment.

### Troubleshooting Workflow
```text
Federated login fails
  ↓
issuer
  ↓
subject
  ↓
audience
  ↓
app/service principal
  ↓
RBAC assignment
```

### Best Practice
Prefer federated workload identity to stored service-principal secrets for modern CI/CD.

---

## Advanced Deep Dive 9 — Conditional Access and Emergency Access

### Concept and Detailed Explanation
Conditional Access can require MFA, compliant devices, trusted locations, authentication strength, or risk controls. Because policy mistakes can lock out administrators, organizations need carefully protected emergency-access identities excluded from normal policy but tightly monitored.

### Architecture / Failure Model
```text
Sign-in
  ↓
Conditional Access evaluation
  ↓
allow / MFA / device / block

Emergency account → controlled exception
```

### Command / Config / Calculation
```text
Policy design:
- admins require phishing-resistant MFA
- legacy auth blocked
- emergency accounts excluded
- emergency sign-in alert enabled
```

### Expected Behavior
Normal privileged access is strongly controlled while a tested recovery path remains available.

### Why It Works
Conditional Access is enforced during authentication, so a bad policy can affect the administrators who would otherwise fix it.

### Production Example
A device-compliance outage blocks normal admins; a monitored break-glass account restores access long enough to correct the policy.

### Troubleshooting Workflow
```text
Tenant-wide login failure
  ↓
CA change?
  ↓
emergency account
  ↓
sign-in logs
  ↓
policy condition/control
  ↓
rollback
```

### Best Practice
Test emergency accounts periodically and alert on every use.

---

## Advanced Deep Dive 10 — Resource Locks vs Authorization

### Concept and Detailed Explanation
Resource locks are an additional protection layer against deletion or modification. They are not a substitute for RBAC. An authorized administrator may still need permission to remove the lock before performing the protected operation.

### Architecture / Failure Model
```text
RBAC allow
  +
Resource Lock
  ↓
operation may still be blocked
```

### Command / Config / Calculation
```text
az lock list -o table
az lock create -g <RG> -n protect-prod --lock-type CanNotDelete
```

### Expected Behavior
The team understands why an authorized Contributor/Owner operation can still fail against a locked scope.

### Why It Works
Locks are evaluated as resource-management safeguards independent of ordinary role assignment.

### Production Example
A production Key Vault resource group carries CanNotDelete to protect against accidental teardown.

### Troubleshooting Workflow
```text
Delete blocked
  ↓
RBAC allows?
  ↓
lock at resource/RG/subscription?
  ↓
change approval
  ↓
remove lock temporarily if authorized
```

### Best Practice
Use locks for high-impact accidental actions, but still design least-privilege RBAC.

---

## Advanced Deep Dive 11 — Azure Policy Effects and Compliance

### Concept and Detailed Explanation
Azure Policy can audit, deny, modify, append, or deploy related configuration depending on effect and definition. Policy therefore supports preventive and detective governance, not only reporting.

### Architecture / Failure Model
```text
Resource request/state
  ↓
Policy rule
  ↓
Deny / Audit / Modify / DeployIfNotExists
```

### Command / Config / Calculation
```text
az policy assignment list -o table
az policy state summarize 2>/dev/null || true
```

### Expected Behavior
Engineers can tell whether a policy prevents creation, reports drift, or remediates configuration.

### Why It Works
Policy evaluation compares resource properties against centrally defined rules at assigned scopes.

### Production Example
A policy denies public IP creation in production while a separate initiative audits diagnostic settings.

### Troubleshooting Workflow
```text
Request denied
  ↓
policy assignment
  ↓
definition/effect
  ↓
scope + parameters
  ↓
exemption?
```

### Best Practice
Use deny only for clear invariants and stage new policies in audit mode before broad enforcement.

---

## Advanced Deep Dive 12 — Policy Initiatives, Exemptions, and Remediation

### Concept and Detailed Explanation
An initiative groups related policy definitions into a governance baseline. Exemptions document approved deviations; remediation tasks can bring existing noncompliant resources toward desired state when the policy supports it.

### Architecture / Failure Model
```text
Initiative
 ├─ encryption policy
 ├─ tag policy
 ├─ diagnostic policy
 └─ network policy
       ↓
assignment + exemptions + remediation
```

### Command / Config / Calculation
```text
az policy set-definition list -o table
az policy exemption list 2>/dev/null || true
```

### Expected Behavior
Compliance reports distinguish genuine violations from approved exceptions.

### Why It Works
Governance at scale requires policy bundles plus an explicit lifecycle for exceptions and correction.

### Production Example
A legacy appliance receives a time-limited policy exemption while the platform team migrates it to a compliant architecture.

### Troubleshooting Workflow
```text
Noncompliance remains
  ↓
policy effect supports remediation?
  ↓
managed identity permissions?
  ↓
remediation task status
  ↓
exception expiry
```

### Best Practice
Every exemption should have an owner, justification, and review/expiry date.

---

## Advanced Deep Dive 13 — Tags, Inheritance, and Cost Metadata

### Concept and Detailed Explanation
Azure tags support ownership, environment, application, cost-center, data-classification, and automation metadata. Tags do not universally inherit from parent scopes by default; Azure Policy or deployment automation is commonly used to enforce or copy required metadata.

### Architecture / Failure Model
```text
Management Group / Subscription / RG
  ↓ policy
Resource tags:
Owner, App, Env, CostCenter
```

### Command / Config / Calculation
```text
az tag list 2>/dev/null || true
az resource list --query '[].{name:name,tags:tags}' -o json
```

### Expected Behavior
Critical resources carry consistent, machine-readable ownership and cost metadata.

### Why It Works
Tags become useful only when values are standardized and enforced where resources are created.

### Production Example
A Cost Management report groups production spend by CostCenter because deployment policy ensures every resource receives the tag.

### Troubleshooting Workflow
```text
Missing cost owner
  ↓
resource tags
  ↓
policy assignment
  ↓
deployment template
  ↓
remediate missing metadata
```

### Best Practice
Define a controlled tag dictionary and enforce required tags at creation.

---

## Advanced Deep Dive 14 — Azure Landing Zones as a Platform Product

### Concept and Detailed Explanation
Azure landing zones combine management-group hierarchy, subscriptions, identity, networking, policy, logging, security, cost governance, and platform automation into a reusable enterprise foundation. They should be versioned and operated as a platform product, not a one-time architecture diagram.

### Architecture / Failure Model
```text
Entra Tenant
  ↓
Management Groups
  ↓
Platform subscriptions + App landing zones
  ↓
Policy / RBAC / Network / Logging / Cost
```

### Command / Config / Calculation
```text
Landing-zone release checklist:
identity
connectivity
management
security
policy
billing
logging
onboarding
```

### Expected Behavior
New workloads inherit a known governance and connectivity baseline.

### Why It Works
Centralized platform capabilities remove repeated one-off foundations from application teams.

### Production Example
A product team receives a pre-governed subscription with hub connectivity, diagnostics, budgets, and policy already enabled.

### Troubleshooting Workflow
```text
Workload onboarding inconsistent
  ↓
which foundation capability is missing?
  ↓
move into landing-zone standard
  ↓
version/test/redeploy
```

### Best Practice
Manage the landing zone through code, releases, ownership, and documented onboarding contracts.

---

## Advanced Deep Dive 15 — VNet System Routes and Longest Prefix Match

### Concept and Detailed Explanation
Azure creates system routes for connected address spaces and default platform behavior. User-defined routes can override many paths. Route selection follows longest-prefix-match logic, so a more specific route can unexpectedly bypass a broad default route.

### Architecture / Failure Model
```text
Packet
  ↓
10.20.8.5 matches:
10.20.0.0/16
10.20.8.0/24 ← more specific
0.0.0.0/0
```

### Command / Config / Calculation
```text
az network nic show-effective-route-table -g <RG> -n <NIC> -o table 2>/dev/null || true
```

### Expected Behavior
The effective route table explains the next hop chosen for a destination.

### Why It Works
Routing decisions are based on the most specific matching prefix among effective routes.

### Production Example
A /24 UDR toward an NVA overrides a /16 route toward peering, sending one application subnet through inspection.

### Troubleshooting Workflow
```text
Packet path wrong
  ↓
effective routes
  ↓
longest matching prefix
  ↓
next hop health
  ↓
return path
```

### Best Practice
Use effective route tables during troubleshooting instead of reasoning only from configured route-table objects.

---

## Advanced Deep Dive 16 — User-Defined Routes and Forced Tunneling

### Concept and Detailed Explanation
UDRs let administrators direct traffic to virtual appliances, VPN/ExpressRoute gateways, or other supported next hops. Forced tunneling commonly sends Internet-bound traffic through a central firewall or on-premises security path.

### Architecture / Failure Model
```text
Spoke subnet
  ↓ 0.0.0.0/0 UDR
Azure Firewall/NVA
  ↓
Internet or On-Prem
```

### Command / Config / Calculation
```text
az network route-table route list -g <RG> --route-table-name <RT> -o table 2>/dev/null || true
```

### Expected Behavior
Outbound flows traverse the intended security path without breaking required Azure service connectivity.

### Why It Works
UDRs alter the default next-hop decision for matching prefixes.

### Production Example
Production spokes route all egress through Azure Firewall so DNS, threat filtering, and logging are centralized.

### Troubleshooting Workflow
```text
Internet unavailable after UDR
  ↓
effective route
  ↓
NVA/firewall forwarding
  ↓
SNAT
  ↓
return route
  ↓
service tags/private endpoints
```

### Best Practice
Change UDRs with a rollback path because a single default route can disconnect entire subnets.

---

## Advanced Deep Dive 17 — NSG Priority, Direction, and Stateful Behavior

### Concept and Detailed Explanation
Network Security Group rules are evaluated by priority within inbound or outbound direction. Lower priority numbers are processed first. NSGs are stateful, so return traffic for an allowed connection is automatically permitted by connection tracking.

### Architecture / Failure Model
```text
Packet
  ↓
Inbound rules priority 100,200,...
  ↓ first match
Allow/Deny
  ↓
state tracked for return
```

### Command / Config / Calculation
```text
az network nic list-effective-nsg -g <RG> -n <NIC> -o json 2>/dev/null || true
```

### Expected Behavior
The engineer can identify the exact effective NSG rule that allows or blocks a flow.

### Why It Works
Azure combines NSGs applied at subnet and NIC levels into effective security rules.

### Production Example
A subnet NSG permits web traffic but a more restrictive NIC NSG blocks the application port; effective-rule inspection reveals the result.

### Troubleshooting Workflow
```text
Flow denied
  ↓
source/destination/port
  ↓
effective NSG
  ↓
priority + direction
  ↓
subnet/NIC combination
```

### Best Practice
Use narrow service-to-service rules and document every broad Internet rule.

---

## Advanced Deep Dive 18 — Application Security Groups as Logical Targets

### Concept and Detailed Explanation
Application Security Groups let NSG rules target sets of NICs by workload role rather than by changing IP addresses. This is especially useful for scale sets and tiered applications.

### Architecture / Failure Model
```text
ASG-Web
  ↓ TCP/8443
ASG-App
  ↓ TCP/1433
ASG-DB
```

### Command / Config / Calculation
```text
az network asg list -o table 2>/dev/null || true
```

### Expected Behavior
Security policy follows application role as instances are replaced or scaled.

### Why It Works
ASGs decouple security intent from ephemeral addresses.

### Production Example
A VMSS instance joins ASG-Web automatically, so app-tier rules do not need to be updated with each new private IP.

### Troubleshooting Workflow
```text
Rule looks right but flow denied
  ↓
NIC ASG membership
  ↓
NSG source/destination ASG
  ↓
port/protocol
  ↓
effective rules
```

### Best Practice
Prefer identity-like workload grouping over static IP lists inside a VNet.

---

## Advanced Deep Dive 19 — VNet Peering and Non-Transitive Connectivity

### Concept and Detailed Explanation
VNet peering provides private connectivity between VNets but does not automatically make peering transitive. If A peers with Hub and Hub peers with B, A does not simply route to B unless a supported transit architecture is deliberately configured.

### Architecture / Failure Model
```text
Spoke A ↔ Hub ↔ Spoke B

Peering alone does not imply A ↔ B transit
```

### Command / Config / Calculation
```text
az network vnet peering list -g <RG> --vnet-name <VNET> -o table 2>/dev/null || true
```

### Expected Behavior
Connectivity expectations match actual peering and gateway/transit configuration.

### Why It Works
Azure prevents peering from becoming an uncontrolled router between all networks.

### Production Example
A hub-spoke architecture enables gateway transit and firewall routing instead of assuming spoke-to-spoke transitivity.

### Troubleshooting Workflow
```text
Spoke-to-spoke fails
  ↓
peerings connected?
  ↓
transit/gateway settings?
  ↓
UDRs/firewall?
  ↓
return route
```

### Best Practice
Document which component provides transit; do not infer it from peering diagrams.

---

## Advanced Deep Dive 20 — Hub-and-Spoke Network Architecture

### Concept and Detailed Explanation
Hub-and-spoke centralizes shared services such as Azure Firewall, DNS, Bastion, VPN/ExpressRoute gateways, and inspection while isolating application networks into spokes. It improves governance but creates shared-hub dependencies that must be scaled and made resilient.

### Architecture / Failure Model
```text
On-Prem
  ↓
Hub VNet
├─ Firewall
├─ DNS
├─ Gateways
└─ Shared Services
   ↙      ↘
Spoke A   Spoke B
```

### Command / Config / Calculation
```text
Architecture inventory:
hub CIDR
spoke CIDRs
peerings
UDRs
shared DNS
gateway transit
inspection paths
```

### Expected Behavior
Application spokes receive governed connectivity without hosting duplicate network appliances.

### Why It Works
Centralized transit and security simplify policy but concentrate critical dependencies.

### Production Example
A network team owns the hub subscription while application teams deploy resources only in delegated spoke subscriptions.

### Troubleshooting Workflow
```text
Many spokes fail together
  ↓
hub service health
  ↓
firewall/gateway capacity
  ↓
DNS
  ↓
route propagation
```

### Best Practice
Treat the hub as production platform infrastructure with its own SLO and capacity model.

---

## Advanced Deep Dive 21 — Azure Firewall, NVAs, and Asymmetric Routing

### Concept and Detailed Explanation
Stateful firewalls require forward and return traffic to traverse a compatible path. UDRs, peering, and gateway routes can accidentally create asymmetry, causing legitimate sessions to fail even when individual rules are correct.

### Architecture / Failure Model
```text
Client → Firewall → App
Client ← other path ← App  X

Stateful firewall loses return flow
```

### Command / Config / Calculation
```text
az network watcher show-next-hop -g <RG> --vm <VM> --source-ip <SRC> --dest-ip <DST> 2>/dev/null || true
```

### Expected Behavior
Forward and return paths are symmetric through required stateful inspection.

### Why It Works
Stateful security devices maintain flow state and expect both directions of a session.

### Production Example
Traffic from on-prem enters Azure Firewall, but a more-specific route sends replies directly to ExpressRoute, breaking the state table.

### Troubleshooting Workflow
```text
Intermittent connection
  ↓
forward next hop
  ↓
return next hop
  ↓
UDRs/BGP routes
  ↓
firewall SNAT/state
```

### Best Practice
Validate both directions of every inspected flow.

---

## Advanced Deep Dive 22 — Azure NAT Gateway and Outbound Architecture

### Concept and Detailed Explanation
Azure NAT Gateway provides scalable outbound SNAT for supported subnets. It separates outbound Internet connectivity from inbound exposure and can reduce SNAT-port exhaustion compared with ad-hoc public-IP patterns.

### Architecture / Failure Model
```text
Private Subnet
  ↓
NAT Gateway
  ↓ public IP/prefix
Internet
```

### Command / Config / Calculation
```text
az network nat gateway list -o table 2>/dev/null || true
az network public-ip list -o table 2>/dev/null || true
```

### Expected Behavior
Private workloads initiate Internet sessions without individual public IP addresses.

### Why It Works
NAT Gateway centralizes source translation and port allocation for attached subnets.

### Production Example
A private VMSS accesses package repositories through NAT Gateway while accepting no direct inbound Internet traffic.

### Troubleshooting Workflow
```text
Outbound failures
  ↓
subnet NAT association
  ↓
route
  ↓
SNAT port capacity
  ↓
NSG/Firewall
  ↓
DNS/external service
```

### Best Practice
Prefer explicit outbound architecture instead of relying on implicit/default outbound behavior.

---

## Advanced Deep Dive 23 — Private Endpoint and Private DNS Coupling

### Concept and Detailed Explanation
A Private Endpoint creates a private NIC/IP in a VNet for a supported PaaS service. The service hostname must resolve to that private IP for clients to use the private path, so DNS is part of the architecture rather than an optional detail.

### Architecture / Failure Model
```text
VM
  ↓ DNS: storage.example → 10.20.5.4
Private Endpoint
  ↓
Storage / SQL / Key Vault
```

### Command / Config / Calculation
```text
az network private-endpoint list -o table 2>/dev/null || true
az network private-dns zone list -o table 2>/dev/null || true
nslookup <service-fqdn>
```

### Expected Behavior
Private clients resolve and connect through the private endpoint while public exposure can be disabled where required.

### Why It Works
Private Link changes the network interface/path but applications normally continue using the service FQDN.

### Production Example
A storage account becomes unreachable after public access is disabled because the private DNS zone was not linked to the application VNet.

### Troubleshooting Workflow
```text
Private endpoint failure
  ↓
endpoint approved?
  ↓
DNS A/CNAME chain
  ↓
VNet zone link
  ↓
NSG/UDR
  ↓
service firewall/RBAC
```

### Best Practice
Treat private DNS configuration as part of every Private Endpoint deployment.

---

## Advanced Deep Dive 24 — Service Endpoints vs Private Endpoints

### Concept and Detailed Explanation
Service Endpoints extend VNet identity to selected PaaS services while the service still uses its public service endpoint. Private Endpoints give the service a private IP in your VNet. The two models differ in DNS, routing, exfiltration control, and network isolation.

### Architecture / Failure Model
```text
Service Endpoint:
Subnet → Azure backbone → public service endpoint

Private Endpoint:
Subnet → private IP NIC → service
```

### Command / Config / Calculation
```text
Decision matrix:
need private IP?
public access disabled?
consumer VNet count?
DNS complexity?
exfiltration requirement?
```

### Expected Behavior
The chosen access model matches security and operational requirements.

### Why It Works
Azure offers both network-trust extension and Private Link-based endpoint models for different service scenarios.

### Production Example
A regulated database uses Private Endpoint and disables public network access; a lower-risk storage workload uses Service Endpoints.

### Troubleshooting Workflow
```text
Access unexpectedly public/private
  ↓
which model configured?
  ↓
DNS target
  ↓
service firewall
  ↓
route
```

### Best Practice
Choose one access model deliberately and document why it satisfies the threat model.

---

## Advanced Deep Dive 25 — VPN Gateway, ExpressRoute, and BGP

### Concept and Detailed Explanation
VPN Gateway provides encrypted IPsec connectivity over the Internet. ExpressRoute provides private connectivity through a connectivity provider. Dynamic routing through BGP is commonly used to exchange prefixes and support resilient hybrid paths.

### Architecture / Failure Model
```text
On-Prem Router
  ├─ IPsec → VPN Gateway
  └─ Private circuit → ExpressRoute Gateway
            ↓
          Azure
```

### Command / Config / Calculation
```text
az network vpn-gateway list 2>/dev/null || true
az network express-route list -o table 2>/dev/null || true
```

### Expected Behavior
Hybrid paths advertise the intended prefixes and fail over according to business design.

### Why It Works
Routing protocol and gateway architecture determine which path is used when links change.

### Production Example
ExpressRoute carries primary enterprise traffic while HA VPN provides an encrypted backup path.

### Troubleshooting Workflow
```text
Hybrid network outage
  ↓
BGP session
  ↓
learned routes
  ↓
gateway health
  ↓
provider circuit/VPN
  ↓
return path
```

### Best Practice
Test hybrid failover periodically; having two circuits is not proof that routing will fail over correctly.

---

## Advanced Deep Dive 26 — Azure DNS Private Resolver and Hybrid Name Resolution

### Concept and Detailed Explanation
Hybrid environments often require on-premises DNS clients to resolve Azure private zones and Azure workloads to resolve on-premises zones. Azure DNS Private Resolver can provide inbound and outbound resolver endpoints and forwarding rules without maintaining custom DNS VMs.

### Architecture / Failure Model
```text
On-Prem DNS
  ↕ conditional forwarding
Private Resolver
  ↕ forwarding rules
Azure Private DNS / On-Prem zones
```

### Command / Config / Calculation
```text
az dns-resolver list -o table 2>/dev/null || true
az network private-dns zone list -o table 2>/dev/null || true
```

### Expected Behavior
Clients resolve private names through the intended authoritative and forwarding paths.

### Why It Works
DNS Private Resolver provides managed forwarding endpoints between Azure VNets and external DNS domains.

### Production Example
A hub VNet hosts resolver endpoints so every spoke can resolve on-prem ERP names and private endpoint zones consistently.

### Troubleshooting Workflow
```text
Hybrid DNS failure
  ↓
client resolver
  ↓
forwarding rule
  ↓
inbound/outbound endpoint
  ↓
zone link
  ↓
network path
```

### Best Practice
Document DNS authority and forwarding exactly like route tables.

---

## Advanced Deep Dive 27 — Azure Load Balancer Health Probes

### Concept and Detailed Explanation
Azure Load Balancer routes Layer-4 traffic only to backends considered healthy by its probe. Probe design therefore becomes part of service availability. A TCP probe proves a port is open; an HTTP probe can validate a more meaningful readiness endpoint.

### Architecture / Failure Model
```text
Client
  ↓
Azure Load Balancer
  ↓ health probe
Backend pool
  ├─ VM1 healthy
  └─ VM2 unhealthy
```

### Command / Config / Calculation
```text
az network lb probe list -g <RG> --lb-name <LB> -o table 2>/dev/null || true
```

### Expected Behavior
Unhealthy backends stop receiving new connections while healthy capacity remains.

### Why It Works
The load balancer uses health-probe state as a routing signal.

### Production Example
A web VM process remains running but its dependency is unavailable; `/ready` returns failure and the VM is removed from the backend pool.

### Troubleshooting Workflow
```text
Backend marked down
  ↓
probe protocol/port/path
  ↓
NSG
  ↓
service listening
  ↓
app dependency
  ↓
threshold
```

### Best Practice
Make health probes representative enough to protect users but simple enough to remain reliable.

---

## Advanced Deep Dive 28 — Application Gateway Routing and WAF

### Concept and Detailed Explanation
Application Gateway is a regional Layer-7 reverse proxy that can terminate TLS, route by host/path, use backend pools, and optionally apply Web Application Firewall rules. Listener, rule, HTTP setting, probe, and backend configuration all participate in request flow.

### Architecture / Failure Model
```text
Client
  ↓ HTTPS
Listener
  ↓ rule
WAF
  ↓ backend setting/probe
App backend
```

### Command / Config / Calculation
```text
az network application-gateway show-backend-health -g <RG> -n <APPGW> 2>/dev/null || true
```

### Expected Behavior
The gateway routes requests to healthy backends and security rules are applied at the intended layer.

### Why It Works
Layer-7 proxying lets Azure make decisions from HTTP host, path, headers, TLS, and health state.

### Production Example
A single gateway routes `/api/*` to API servers and `/` to web servers while WAF blocks known attack patterns.

### Troubleshooting Workflow
```text
502/403 from App Gateway
  ↓
listener/rule
  ↓
backend health
  ↓
probe
  ↓
TLS/backend setting
  ↓
WAF logs
```

### Best Practice
Use backend-health diagnostics before changing DNS or application code.

---

## Advanced Deep Dive 29 — Azure Front Door Global Edge Routing

### Concept and Detailed Explanation
Azure Front Door provides global HTTP/S entry, anycast edge routing, TLS termination, health-based origin selection, acceleration, and WAF integration. It is appropriate when users and origins span regions and the application benefits from a global edge reverse proxy.

### Architecture / Failure Model
```text
Global users
  ↓ anycast edge
Front Door + WAF
  ├─ Region A origin
  └─ Region B origin
```

### Command / Config / Calculation
```text
az afd profile list -o table 2>/dev/null || true
az afd endpoint list --profile-name <PROFILE> -g <RG> 2>/dev/null || true
```

### Expected Behavior
Users enter through the nearest/appropriate edge and are routed to healthy configured origins.

### Why It Works
Front Door separates global client entry from regional application infrastructure.

### Production Example
A customer portal serves Egypt and Europe through one global endpoint while failing over between Azure regions.

### Troubleshooting Workflow
```text
Front Door error
  ↓
endpoint/domain
  ↓
route
  ↓
origin group health
  ↓
WAF
  ↓
TLS/DNS
```

### Best Practice
Use Front Door for global HTTP/S delivery; do not confuse it with regional Application Gateway.

---

## Advanced Deep Dive 30 — Traffic Manager DNS-Based Routing

### Concept and Detailed Explanation
Traffic Manager changes DNS answers according to endpoint health and routing policy. It does not proxy the application connection. Client DNS caching and TTL therefore influence failover speed.

### Architecture / Failure Model
```text
Client DNS query
  ↓
Traffic Manager profile
  ↓ returns endpoint A/B
Client connects directly
```

### Command / Config / Calculation
```text
az network traffic-manager profile list -o table 2>/dev/null || true
nslookup <traffic-manager-name>
```

### Expected Behavior
DNS answers reflect the selected policy and healthy endpoints.

### Why It Works
Traffic Manager controls name resolution rather than carrying request traffic.

### Production Example
A multi-region non-HTTP service uses priority routing so DNS moves clients to Region B after Region A fails.

### Troubleshooting Workflow
```text
Failover appears slow
  ↓
endpoint health
  ↓
profile policy
  ↓
TTL/cache
  ↓
client resolver
```

### Best Practice
Use Traffic Manager when DNS-level routing is enough; use Front Door when you need global HTTP reverse proxy behavior.

---

## Advanced Deep Dive 31 — Azure VM Boot Path and Platform Diagnostics

### Concept and Detailed Explanation
A VM can be `running` in Azure while the guest OS or application is unhealthy. The boot path includes platform host health, disk attachment, bootloader/kernel, guest networking, cloud-init/Windows provisioning, extensions, firewall, and service startup.

### Architecture / Failure Model
```text
Azure platform
  ↓
VM power state
  ↓
OS boot
  ↓
agent/extensions
  ↓
network
  ↓
application
```

### Command / Config / Calculation
```text
az vm get-instance-view -g <RG> -n <VM> -o json 2>/dev/null || true
az vm boot-diagnostics get-boot-log -g <RG> -n <VM> 2>/dev/null || true
```

### Expected Behavior
The engineer can distinguish Azure platform state from guest-OS and application state.

### Why It Works
Azure control-plane status represents VM lifecycle, not necessarily guest service readiness.

### Production Example
A VM reports running but boot diagnostics show an fstab error dropping Linux into emergency mode.

### Troubleshooting Workflow
```text
VM unreachable
  ↓
resource health
  ↓
power/provisioning state
  ↓
boot diagnostics
  ↓
NIC/NSG/route
  ↓
guest service
```

### Best Practice
Check platform and boot evidence before resetting or redeploying a VM.

---

## Advanced Deep Dive 32 — Availability Zones vs Availability Sets

### Concept and Detailed Explanation
Availability Zones separate resources across datacenter groups within a region. Availability Sets distribute VMs across fault and update domains inside non-zonal designs. Zones generally provide stronger datacenter-failure isolation where supported.

### Architecture / Failure Model
```text
Zone design:
VM1 → Zone 1
VM2 → Zone 2

Availability Set:
FD/UD distribution within region
```

### Command / Config / Calculation
```text
az vm list-skus --location <REGION> --query '[?capabilities]' 2>/dev/null | head
```

### Expected Behavior
Architecture uses the failure-domain mechanism appropriate to the service and region.

### Why It Works
Zones isolate datacenter infrastructure; availability sets reduce correlated host/rack/update events without explicit zone placement.

### Production Example
A legacy workload uses an availability set while a new production VMSS spreads instances across zones.

### Troubleshooting Workflow
```text
HA design unclear
  ↓
service supports zones?
  ↓
current VM placement
  ↓
SLA/reliability requirement
  ↓
redesign if single domain
```

### Best Practice
Choose based on the failure you need to survive, not just on a certification definition.

---

## Advanced Deep Dive 33 — VM Scale Sets and Autoscale Safety

### Concept and Detailed Explanation
VM Scale Sets maintain a fleet based on a common model and can scale using metrics or schedules. Safe autoscaling requires a minimum instance count, load-balancer health, externalized state, and graceful scale-in behavior.

### Architecture / Failure Model
```text
Image/model
  ↓
VMSS
  ├─ VM1
  ├─ VM2
  └─ VM3
  ↕ autoscale metric
```

### Command / Config / Calculation
```text
az vmss list -o table 2>/dev/null || true
az monitor autoscale list -o table 2>/dev/null || true
```

### Expected Behavior
Capacity changes without violating the application's minimum healthy instance requirement.

### Why It Works
VMSS reconciles desired fleet capacity while autoscale changes that desired capacity from observed signals.

### Production Example
A web tier keeps minimum two instances across zones and scales to ten during peak traffic.

### Troubleshooting Workflow
```text
VMSS not scaling
  ↓
metric rule
  ↓
min/max/default
  ↓
quota/capacity
  ↓
instance provisioning
  ↓
health
```

### Best Practice
Set minimum capacity from reliability needs and scale-in only after the application is designed for termination.

---

## Advanced Deep Dive 34 — Azure Compute Gallery and Image Versioning

### Concept and Detailed Explanation
Azure Compute Gallery distributes and versions VM images across regions. A controlled image pipeline can patch, harden, test, and publish an immutable version that VMSS or deployments consume.

### Architecture / Failure Model
```text
Trusted base image
  ↓
patch/harden/test
  ↓
Compute Gallery image version
  ↓
VM / VMSS rollout
```

### Command / Config / Calculation
```text
az sig list -o table 2>/dev/null || true
az sig image-version list -g <RG> --gallery-name <GALLERY> --gallery-image-definition <IMAGE> -o table 2>/dev/null || true
```

### Expected Behavior
Running instances can be traced to an approved image version.

### Why It Works
Versioned gallery artifacts decouple image build from instance creation and support reproducible regional deployment.

### Production Example
A security patch produces image `2026.08.20`, which a VMSS rolling upgrade deploys after validation.

### Troubleshooting Workflow
```text
Unknown image in prod
  ↓
VM image reference
  ↓
gallery version
  ↓
build provenance
  ↓
replace if unapproved
```

### Best Practice
Treat images as signed/versioned build artifacts, not manually maintained servers.

---

## Advanced Deep Dive 35 — Managed Disk Performance and Host Limits

### Concept and Detailed Explanation
Managed disks have capacity, IOPS, throughput, latency, caching, and tier characteristics. VM size can also cap storage throughput. A high-performance disk attached to a small VM may therefore be throttled by the host path.

### Architecture / Failure Model
```text
Application
  ↓
filesystem
  ↓
VM storage bandwidth limit
  ↓
Managed Disk limits
```

### Command / Config / Calculation
```text
az disk show -g <RG> -n <DISK> -o json 2>/dev/null || true
# Linux guest
iostat -xz 1 5 2>/dev/null || true
```

### Expected Behavior
Performance analysis identifies whether the bottleneck is guest queueing, VM limits, or disk limits.

### Why It Works
Storage performance is constrained by the narrowest layer in the I/O path.

### Production Example
A database disk supports high IOPS but the selected VM size cannot drive them, so upgrading only the disk does not help.

### Troubleshooting Workflow
```text
Disk latency high
  ↓
guest iostat
  ↓
VM storage limits
  ↓
disk tier/IOPS/throughput
  ↓
caching/workload pattern
```

### Best Practice
Size VM and disks together from measured workload I/O.

---

## Advanced Deep Dive 36 — App Service Plan and Scaling Model

### Concept and Detailed Explanation
App Service separates the application from the App Service Plan that provides compute capacity. Multiple apps can share a plan, which improves utilization but also couples them to the same CPU, memory, scale, and maintenance capacity.

### Architecture / Failure Model
```text
App Service Plan
  ├─ Web App A
  ├─ API B
  └─ Worker C

Plan size/instances = shared capacity
```

### Command / Config / Calculation
```text
az appservice plan show -g <RG> -n <PLAN> -o json 2>/dev/null || true
az webapp list -o table 2>/dev/null || true
```

### Expected Behavior
The team understands whether performance problems come from one application or contention in the shared plan.

### Why It Works
Apps in the same plan consume the same underlying worker pool.

### Production Example
Three low-traffic apps share one plan, but a CPU-heavy batch endpoint causes latency for the others.

### Troubleshooting Workflow
```text
App Service slow
  ↓
plan CPU/memory
  ↓
which apps share plan
  ↓
autoscale
  ↓
app telemetry
```

### Best Practice
Group apps on a plan only when shared capacity and scaling behavior are acceptable.

---

## Advanced Deep Dive 37 — Deployment Slots and Configuration Stickiness

### Concept and Detailed Explanation
App Service deployment slots support staged releases and traffic swaps. Some configuration values are slot-specific ('sticky'), while others move during swap. Misunderstanding this can make a staging app suddenly use production or vice versa.

### Architecture / Failure Model
```text
Build
  ↓
Staging Slot
  ↓ validate
Swap
  ↓
Production Slot

Sticky settings remain with slot
```

### Command / Config / Calculation
```text
az webapp deployment slot list -g <RG> -n <APP> -o table 2>/dev/null || true
az webapp config appsettings list -g <RG> -n <APP> --slot staging 2>/dev/null || true
```

### Expected Behavior
A swap promotes code safely while environment-specific secrets/endpoints remain on the intended slot.

### Why It Works
Slot swap exchanges selected application/content configuration while marked deployment-slot settings remain fixed.

### Production Example
A staging slot points to a staging database even after code is swapped into production because the DB connection setting is slot-sticky.

### Troubleshooting Workflow
```text
Bad state after swap
  ↓
which settings are sticky?
  ↓
slot config
  ↓
connection strings
  ↓
rollback swap
```

### Best Practice
Explicitly classify every environment-specific setting before using slot swaps.

---

## Advanced Deep Dive 38 — Azure Functions Concurrency and Downstream Pressure

### Concept and Detailed Explanation
Azure Functions can scale execution quickly, but databases, APIs, and third-party systems have finite capacity. Trigger concurrency, host settings, plan limits, and queue buffering should protect downstream dependencies.

### Architecture / Failure Model
```text
Event burst
  ↓
Functions scale
  ↓
DB/API finite capacity
  ↓
possible throttling/connection exhaustion
```

### Command / Config / Calculation
```text
Design values:
max concurrent executions
queue depth
DB max connections
retry/backoff
poison queue
```

### Expected Behavior
Function scale stays within the safe capacity of downstream systems.

### Why It Works
Serverless compute and downstream services scale independently, so unbounded concurrency can move the bottleneck rather than remove it.

### Production Example
A Service Bus-triggered function limits concurrency so Azure SQL never exceeds its safe connection pool.

### Troubleshooting Workflow
```text
Functions fail during burst
  ↓
instance/concurrency count
  ↓
trigger backlog
  ↓
downstream limits
  ↓
retry/throttle
```

### Best Practice
Scale the dependency chain, not only the function runtime.

---

## Advanced Deep Dive 39 — Azure Container Apps Revisions and Event-Driven Scaling

### Concept and Detailed Explanation
Azure Container Apps provides managed container revisions, ingress, and event-driven scaling based on KEDA-style signals. Revisions can support blue/green or weighted traffic while scale rules react to HTTP or event demand.

### Architecture / Failure Model
```text
Container image
  ↓
Revision A / Revision B
  ↓ traffic weights
Container Apps
  ↕ event/HTTP scale
```

### Command / Config / Calculation
```text
az containerapp revision list -g <RG> -n <APP> -o table 2>/dev/null || true
```

### Expected Behavior
New revisions are validated with controlled traffic and scale to demand without direct node management.

### Why It Works
Container Apps separates application revision lifecycle from the underlying Kubernetes infrastructure.

### Production Example
A new API revision receives 10% traffic, then 100% after error-rate validation.

### Troubleshooting Workflow
```text
Revision unhealthy
  ↓
image start
  ↓
env/secrets
  ↓
ingress port
  ↓
scale rule
  ↓
logs
```

### Best Practice
Use revision traffic splitting for risky application changes rather than replacing all traffic at once.

---

## Advanced Deep Dive 40 — AKS Shared Responsibility and Control Loops

### Concept and Detailed Explanation
AKS is managed Kubernetes, not fully managed applications. Microsoft operates significant control-plane infrastructure, while customers still own workloads, identities/RBAC, pod security, network policy, images, secrets, node-pool choices, upgrades under the service model, and application reliability.

### Architecture / Failure Model
```text
Azure-managed control plane
  ↓
AKS cluster
  ├─ node pools
  ├─ workloads
  ├─ network policy
  └─ identities
```

### Command / Config / Calculation
```text
az aks show -g <RG> -n <AKS> -o json 2>/dev/null || true
kubectl get nodes,pods -A 2>/dev/null || true
```

### Expected Behavior
The team can state which failures belong to Azure platform, cluster configuration, node pools, or workload code.

### Why It Works
Kubernetes continuously reconciles desired state but still depends on capacity, images, network, storage, and correct policies.

### Production Example
Azure keeps the API control plane available, but a bad network policy still blocks application-to-database traffic.

### Troubleshooting Workflow
```text
AKS app down
  ↓
cluster/API health
  ↓
nodes
  ↓
pods/events
  ↓
network/storage
  ↓
app logs
```

### Best Practice
Do not interpret 'managed Kubernetes' as 'managed workload security and reliability'.

---

## Advanced Deep Dive 41 — Azure Container Registry and Image Supply Chain

### Concept and Detailed Explanation
ACR stores container images and artifacts. Production security requires immutable versioning/digests, vulnerability scanning in the pipeline, restricted push permissions, and workload pull through managed identity where possible.

### Architecture / Failure Model
```text
Source
  ↓ build
Image scan/test
  ↓
ACR digest
  ↓
AKS/Container Apps/App Service
```

### Command / Config / Calculation
```text
az acr list -o table 2>/dev/null || true
az acr repository list -n <ACR> -o table 2>/dev/null || true
```

### Expected Behavior
Every deployed container can be traced to a tested image digest and build commit.

### Why It Works
Registries provide a controlled distribution point between CI and runtime.

### Production Example
A pipeline publishes `sha256:...`; AKS deploys that digest rather than a mutable `latest` tag.

### Troubleshooting Workflow
```text
Image pull/unknown image
  ↓
registry/digest
  ↓
identity role AcrPull
  ↓
network/private endpoint
  ↓
build provenance
```

### Best Practice
Deploy immutable digests and minimize who can push to production registries.

---

## Advanced Deep Dive 42 — Blob Versioning, Soft Delete, and Immutability

### Concept and Detailed Explanation
Azure Blob data protection can combine versioning, soft delete, snapshots, and immutable/WORM policies. These controls solve different problems: versioning preserves generations, soft delete creates a recovery window, and immutability prevents modification/deletion for a defined retention model.

### Architecture / Failure Model
```text
Blob
 ├─ current version
 ├─ old versions
 ├─ soft-deleted state
 └─ immutable retention if configured
```

### Command / Config / Calculation
```text
az storage account blob-service-properties show --account-name <ACCOUNT> 2>/dev/null || true
```

### Expected Behavior
Operators know which mechanism can recover an overwritten, deleted, or maliciously modified object.

### Why It Works
Data protection is strongest when historical copies and administrative deletion controls are independent.

### Production Example
A compliance archive uses immutable retention while everyday application blobs use versioning and soft delete.

### Troubleshooting Workflow
```text
Blob lost
  ↓
versioning?
  ↓
soft delete window?
  ↓
immutable copy?
  ↓
backup/replication
```

### Best Practice
Design recovery from accidental deletion and malicious deletion as separate scenarios.

---

## Advanced Deep Dive 43 — Storage Redundancy and Failure Domains

### Concept and Detailed Explanation
LRS, ZRS, GRS, GZRS, and read-access variants differ in which failure domains receive copies. Geo-redundancy generally uses asynchronous replication, so the secondary copy may have a nonzero RPO during a primary-region failure.

### Architecture / Failure Model
```text
Primary region:
LRS or ZRS copies
  ↓ async geo replication
Secondary region:
additional copies
```

### Command / Config / Calculation
```text
Decision inputs:
zone failure tolerance
regional DR
secondary read need
RPO
cost
service support
```

### Expected Behavior
The storage redundancy option directly maps to the business failure scenario and recovery requirement.

### Why It Works
Replication topology determines which physical failures can be survived without restore.

### Production Example
A customer portal uses GZRS because it requires primary-region zone resilience plus a secondary-region copy.

### Troubleshooting Workflow
```text
Storage incident
  ↓
which redundancy SKU?
  ↓
primary/secondary availability
  ↓
last sync / RPO
  ↓
failover procedure
```

### Best Practice
Do not select redundancy by acronym strength; select it from failure-domain and RPO requirements.

---

## Advanced Deep Dive 44 — Blob Lifecycle Management

### Concept and Detailed Explanation
Lifecycle rules can transition blobs to cooler tiers and delete current or previous versions based on age and conditions. Because lifecycle is automated and potentially destructive, it should be version-controlled and reviewed like code.

### Architecture / Failure Model
```text
Hot
  ↓ age
Cool
  ↓
Cold/Archive
  ↓
Expire
```

### Command / Config / Calculation
```text
az storage account management-policy show -g <RG> --account-name <ACCOUNT> 2>/dev/null || true
```

### Expected Behavior
Data moves to cost-appropriate tiers without violating retention or recovery requirements.

### Why It Works
Lifecycle policies evaluate blob age/state and execute automatically at scale.

### Production Example
Operational logs move to cool storage after 30 days and archive after 180 days while legal records remain protected longer.

### Troubleshooting Workflow
```text
Unexpected deletion/tier
  ↓
management policy
  ↓
matching prefix/tags
  ↓
version state
  ↓
retention requirement
```

### Best Practice
Test lifecycle rules on narrow prefixes before applying them to large production datasets.

---

## Advanced Deep Dive 45 — Azure Files and Azure File Sync

### Concept and Detailed Explanation
Azure Files provides managed SMB/NFS-style shared storage. Azure File Sync extends Windows Server file shares with cloud tiering and synchronization to Azure Files. It is useful for hybrid file-service modernization, but identity, namespace, cache, and conflict behavior must be planned.

### Architecture / Failure Model
```text
Branch File Server
  ↕ File Sync
Azure Files
  ↕
Other synced servers/clients
```

### Command / Config / Calculation
```text
az storage share list --account-name <ACCOUNT> --auth-mode login 2>/dev/null || true
```

### Expected Behavior
Users retain shared-file semantics while Azure provides central durable storage and optional local caching.

### Why It Works
File Sync separates authoritative cloud file storage from local frequently accessed cached copies.

### Production Example
Factory file servers keep hot engineering files locally while cold content tiers to Azure Files.

### Troubleshooting Workflow
```text
File missing/stale
  ↓
sync group
  ↓
server endpoint health
  ↓
cloud endpoint
  ↓
conflict/tiering
  ↓
identity/network
```

### Best Practice
Use file services only when applications require filesystem semantics; use Blob for object-native workloads.

---

## Advanced Deep Dive 46 — Azure SQL High Availability and Connection Resilience

### Concept and Detailed Explanation
Azure SQL Database abstracts the database host and supports service-tier-specific high availability. Applications should use the logical server/database endpoint, connection retries, and transient-fault handling rather than assuming one fixed backend.

### Architecture / Failure Model
```text
App
  ↓ logical SQL endpoint
Azure SQL HA platform
  ↓
current healthy replica
```

### Command / Config / Calculation
```text
Application design:
connect timeout
retry with backoff
pool recycle
idempotent transaction retry where safe
```

### Expected Behavior
Brief platform failovers cause recoverable connection errors instead of prolonged application outage.

### Why It Works
Managed database endpoints decouple client connection strings from underlying replica placement.

### Production Example
Planned maintenance changes the active replica; resilient connection logic reconnects automatically.

### Troubleshooting Workflow
```text
Azure SQL outage
  ↓
Service Health/resource health
  ↓
DNS/private endpoint
  ↓
firewall/RBAC
  ↓
connections
  ↓
query/DB health
```

### Best Practice
Design every managed-database client for transient disconnects.

---

## Advanced Deep Dive 47 — Cosmos DB Partition Keys

### Concept and Detailed Explanation
Cosmos DB distributes data and throughput using logical partitions derived from the partition key. A poor key can create hot partitions, limited scale, or expensive cross-partition queries. Good keys have high cardinality and align with dominant access patterns.

### Architecture / Failure Model
```text
Requests
  ↓ partition key
Logical partitions
  ↓ distributed physical partitions
```

### Command / Config / Calculation
```text
Design worksheet:
query pattern
partition key
cardinality
expected RU/s
hot-key risk
cross-partition queries
```

### Expected Behavior
Traffic and storage distribute evenly enough for the workload and key-based queries remain efficient.

### Why It Works
Cosmos DB routes requests based on partition-key values and allocates distributed capacity behind them.

### Production Example
Telemetry data uses deviceId rather than country as the partition key to avoid concentrating most writes into a few hot values.

### Troubleshooting Workflow
```text
Cosmos throttling/high RU
  ↓
hot partition?
  ↓
query fan-out?
  ↓
item size/indexing
  ↓
throughput mode
```

### Best Practice
Choose the partition key before production data volume makes redesign expensive.

---

## Advanced Deep Dive 48 — Cosmos DB Consistency Models

### Concept and Detailed Explanation
Cosmos DB offers multiple consistency levels that trade freshness, latency, and availability. Strong consistency simplifies reads but can constrain distribution/latency; weaker models improve availability/performance while allowing controlled staleness.

### Architecture / Failure Model
```text
Write
  ↓ replicas
Readers see data according to selected consistency model
```

### Command / Config / Calculation
```text
Decision inputs:
read-after-write requirement
acceptable staleness
multi-region writes
latency
availability
business semantics
```

### Expected Behavior
The consistency choice is justified by the application's correctness requirements.

### Why It Works
Distributed replicas cannot maximize all consistency, latency, and availability properties simultaneously.

### Production Example
A product catalog accepts session-style consistency, while a financial workflow uses stronger guarantees where required.

### Troubleshooting Workflow
```text
Unexpected stale read
  ↓
consistency level
  ↓
session token/client behavior
  ↓
region routing
  ↓
replication state
```

### Best Practice
Choose the weakest consistency that still satisfies business correctness.

---

## Advanced Deep Dive 49 — Azure Service Bus Delivery Semantics

### Concept and Detailed Explanation
Service Bus supports enterprise queues and topics with delivery retries, locks, sessions, dead-lettering, duplicate detection, and transactions in supported scenarios. Consumers must understand peek-lock vs receive-and-delete and should remain idempotent.

### Architecture / Failure Model
```text
Producer
  ↓
Service Bus Queue/Topic
  ↓ lock
Consumer
  ↓ complete
or timeout → redelivery
```

### Command / Config / Calculation
```text
az servicebus queue show -g <RG> --namespace-name <NS> -n <QUEUE> 2>/dev/null || true
```

### Expected Behavior
Failed processing returns messages for retry and poison messages move to the dead-letter queue.

### Why It Works
Message locks separate receipt from successful acknowledgement.

### Production Example
A billing worker crashes after receiving an order event; the lock expires and another worker processes it.

### Troubleshooting Workflow
```text
Duplicate/backlog
  ↓
lock duration
  ↓
max delivery count
  ↓
DLQ
  ↓
consumer idempotency
```

### Best Practice
Treat message delivery as at-least-once unless the end-to-end business operation proves otherwise.

---

## Advanced Deep Dive 50 — Event Grid vs Event Hubs

### Concept and Detailed Explanation
Event Grid routes discrete events to handlers, while Event Hubs ingests high-volume ordered event streams/telemetry. They can appear together but solve different messaging shapes.

### Architecture / Failure Model
```text
Event Grid:
resource event → route → handler

Event Hubs:
continuous stream → partitions → consumers
```

### Command / Config / Calculation
```text
Scenario mapping:
Blob created notification → Event Grid
1M telemetry events/min → Event Hubs
```

### Expected Behavior
The selected service matches whether the workload is reactive event notification or sustained streaming ingestion.

### Why It Works
Routing individual events and ingesting a high-throughput stream require different retention, partitioning, and consumer models.

### Production Example
A factory sends machine telemetry through Event Hubs while storage-object-created events trigger workflows through Event Grid.

### Troubleshooting Workflow
```text
Wrong messaging service
  ↓
event rate
  ↓
retention/replay need
  ↓
ordering/partitions
  ↓
subscriber model
```

### Best Practice
Choose messaging from delivery semantics and volume, not from similar names.

---

## Advanced Deep Dive 51 — API Management as a Policy Gateway

### Concept and Detailed Explanation
Azure API Management provides a managed API façade for authentication, authorization, quotas, transformations, versioning, analytics, and developer onboarding. Policies can protect backends but can also become critical application logic if overused.

### Architecture / Failure Model
```text
Clients
  ↓
API Management
  ├─ auth
  ├─ rate limit
  ├─ transform
  └─ logging
  ↓
Backend APIs
```

### Command / Config / Calculation
```text
Policy examples:
validate-jwt
rate-limit
set-header
rewrite-uri
cache-lookup
```

### Expected Behavior
Backend services receive controlled, authenticated, and observable API traffic.

### Why It Works
APIM centralizes cross-cutting API concerns before requests reach backend implementations.

### Production Example
A partner API uses Entra tokens, a per-client rate limit, and versioned routes without exposing backend hosts directly.

### Troubleshooting Workflow
```text
API 401/429/5xx
  ↓
APIM trace
  ↓
policy execution
  ↓
backend health
  ↓
DNS/private endpoint
```

### Best Practice
Keep business domain logic in services; use APIM mainly for gateway concerns.

---

## Advanced Deep Dive 52 — Key Vault Control Plane vs Data Plane

### Concept and Detailed Explanation
Key Vault has management operations on the vault resource and data operations on secrets, keys, and certificates. Azure RBAC or legacy access-policy models govern data access depending on vault configuration. Having Contributor on the vault resource does not automatically mean reading secrets.

### Architecture / Failure Model
```text
Azure Resource Manager control plane
  ↓ manage vault
Key Vault data plane
  ↓ read/use secret/key/cert
```

### Command / Config / Calculation
```text
az keyvault show -n <VAULT> -o json 2>/dev/null || true
az keyvault secret list --vault-name <VAULT> 2>/dev/null || true
```

### Expected Behavior
Administration of the vault resource is separated from sensitive secret/key use.

### Why It Works
Azure intentionally separates resource configuration permissions from protected data operations.

### Production Example
A platform engineer can configure diagnostics on the vault but cannot read application secrets.

### Troubleshooting Workflow
```text
Key Vault 403
  ↓
network/private endpoint
  ↓
data-plane RBAC/access policy
  ↓
principal/token
  ↓
secret/key state
```

### Best Practice
Grant secret/key operations only to workloads and operators that actually need them.

---

## Advanced Deep Dive 53 — Secret and Certificate Rotation

### Concept and Detailed Explanation
Credential rotation is a multi-party workflow: create a new value, update the provider/issuer, make consumers use it, verify, then retire the old value. Key Vault can store versions and integrate with certificates, but consumers must refresh correctly.

### Architecture / Failure Model
```text
Old secret CURRENT
  ↓ create new version
Consumers update
  ↓ verify
Old version disabled/retired
```

### Command / Config / Calculation
```text
Rotation record:
secret name
old version
new version
consumer list
verification
retirement time
```

### Expected Behavior
All consumers authenticate with the new credential before the old one is disabled.

### Why It Works
Distributed applications rarely update every instance atomically, so overlap prevents downtime.

### Production Example
An app pool keeps the old database password cached; rotation succeeds only after connection refresh behavior is fixed.

### Troubleshooting Workflow
```text
Post-rotation auth failure
  ↓
current Key Vault version
  ↓
provider credential
  ↓
consumer cache
  ↓
managed identity/secret reference
```

### Best Practice
Test rotation in staging and design consumers to reload secrets without full outages.

---

## Advanced Deep Dive 54 — Defender for Cloud and Security Operations

### Concept and Detailed Explanation
Microsoft Defender for Cloud provides posture management and workload-protection capabilities across Azure and connected resources. Its value is strongest when recommendations/findings map to owners, remediation SLAs, and central security workflows rather than remaining dashboard noise.

### Architecture / Failure Model
```text
Resources
  ↓
Defender posture/findings
  ↓
Security workflow / SIEM
  ↓
owner remediation
```

### Command / Config / Calculation
```text
Security workflow fields:
subscription
resource
finding
severity
exposure
owner
due date
exception
```

### Expected Behavior
Security recommendations become actionable engineering work with traceable closure.

### Why It Works
Cloud posture tools continuously compare resources and telemetry with security expectations.

### Production Example
Defender identifies an Internet-exposed management port and creates a tracked remediation task for the owning team.

### Troubleshooting Workflow
```text
Finding volume high
  ↓
prioritize exposure/business criticality
  ↓
validate false positive
  ↓
remediate/exception
  ↓
verify
```

### Best Practice
Measure security posture by resolved risk, not by dashboard score alone.

---

## Advanced Deep Dive 55 — Azure Monitor Telemetry Model

### Concept and Detailed Explanation
Azure Monitor brings metrics, logs, traces/application telemetry, alerts, and workbooks together. Metrics are efficient time series; logs provide detailed records; Application Insights adds request/dependency traces. A production service needs all of them correlated.

### Architecture / Failure Model
```text
Resource/App
  ├─ Metrics
  ├─ Logs
  ├─ Traces
  └─ Activity events
      ↓
Azure Monitor
      ↓ alerts/workbooks
```

### Command / Config / Calculation
```text
az monitor metrics list --resource <RESOURCE_ID> --metric <METRIC> 2>/dev/null || true
```

### Expected Behavior
An alert can be correlated with detailed logs and application dependencies on one timeline.

### Why It Works
Different telemetry types answer different diagnostic questions.

### Production Example
High request latency leads to an Application Insights dependency trace showing slow Azure SQL calls.

### Troubleshooting Workflow
```text
Incident
  ↓
metric/SLO symptom
  ↓
logs
  ↓
trace/dependency
  ↓
Activity Log/recent deployment
```

### Best Practice
Standardize correlation IDs and resource dimensions across telemetry.

---

## Advanced Deep Dive 56 — KQL for Evidence-Driven Troubleshooting

### Concept and Detailed Explanation
Kusto Query Language lets engineers query Log Analytics and Azure Monitor data. Good KQL narrows time, resource, operation, and correlation fields before aggregating. Queries should answer an operational question rather than dump raw logs.

### Architecture / Failure Model
```text
Question
  ↓
time filter
  ↓
resource/user filter
  ↓
project fields
  ↓
summarize/correlate
```

### Command / Config / Calculation
```text
AzureActivity
| where TimeGenerated > ago(1h)
| where ActivityStatusValue == 'Failure'
| project TimeGenerated, OperationNameValue, Caller, ResourceGroup
```

### Expected Behavior
The query produces a small evidence set tied to the incident window.

### Why It Works
KQL executes structured filtering and aggregation over centralized telemetry.

### Production Example
After a deployment failure, the operator queries failed control-plane operations for the affected resource group in the last hour.

### Troubleshooting Workflow
```text
Query returns too much/nothing
  ↓
workspace/table
  ↓
time range
  ↓
field names
  ↓
resource ID
  ↓
ingestion delay
```

### Best Practice
Start every KQL investigation with time and scope boundaries.

---

## Advanced Deep Dive 57 — Activity Log, Resource Health, and Service Health

### Concept and Detailed Explanation
These three evidence sources answer different questions. Activity Log records subscription control-plane operations. Resource Health evaluates one resource's health from Azure's perspective. Service Health reports subscription-relevant platform incidents and maintenance.

### Architecture / Failure Model
```text
Activity Log → who changed what
Resource Health → is this resource platform-healthy?
Service Health → is Azure service/region affected?
```

### Command / Config / Calculation
```text
az monitor activity-log list --offset 1h -o table 2>/dev/null || true
az rest --method get --url 'https://management.azure.com/subscriptions/<SUB>/providers/Microsoft.ResourceHealth/events?api-version=2022-10-01' 2>/dev/null || true
```

### Expected Behavior
The incident investigation uses the source matching change history, resource health, or platform event.

### Why It Works
Azure separates customer actions from resource-specific platform state and wider service incidents.

### Production Example
A VM outage coincides with a regional service event, while Activity Log shows no customer configuration change.

### Troubleshooting Workflow
```text
Outage
  ↓
recent Activity Log?
  ↓
Resource Health?
  ↓
Service Health?
  ↓
workload telemetry
```

### Best Practice
Check all three before concluding whether Azure or your configuration caused the problem.

---

## Advanced Deep Dive 58 — Azure Backup Vault Isolation and Restore Testing

### Concept and Detailed Explanation
Backup policy success is not the same as recoverability. Critical backups should use protected vault design, separation of duties, soft-delete/immutability capabilities where supported, and regular restore exercises.

### Architecture / Failure Model
```text
Production workload
  ↓
Azure Backup
  ↓
Vault
  ↓
protected recovery points
  ↓
restore test
```

### Command / Config / Calculation
```text
az backup vault list -o table 2>/dev/null || true
az backup job list --vault-name <VAULT> -g <RG> -o table 2>/dev/null || true
```

### Expected Behavior
Recovery points exist, are protected from ordinary operational mistakes, and have proven restore procedures.

### Why It Works
Backup systems require both stored copies and an independently tested path to rebuild usable service.

### Production Example
A quarterly restore test discovers that an application certificate was never included in the recovery runbook.

### Troubleshooting Workflow
```text
Restore fails
  ↓
recovery point
  ↓
vault/KMS access
  ↓
network/identity
  ↓
application consistency
  ↓
runbook gap
```

### Best Practice
Track restore success and measured RTO, not only backup job success.

---

## Advanced Deep Dive 59 — Azure Site Recovery and DR Orchestration

### Concept and Detailed Explanation
Azure Site Recovery replicates supported workloads and coordinates failover/failback. DR still depends on DNS, identity, network, data dependencies, quotas, and application validation; ASR cannot make an incomplete secondary environment production-ready by itself.

### Architecture / Failure Model
```text
Primary workload
  ↓ replication
Recovery region/site
  ↓
Test failover / planned failover / disaster failover
```

### Command / Config / Calculation
```text
az site-recovery vault list 2>/dev/null || true
DR checklist:
network mapping
recovery plan
DNS
secrets
capacity
validation
```

### Expected Behavior
Test failover proves the workload can recover without disrupting production.

### Why It Works
Replication and orchestration reduce rebuild time but do not eliminate external dependencies.

### Production Example
A VM recovery succeeds but users still fail because the DR VNet lacks the private DNS zone link.

### Troubleshooting Workflow
```text
DR test failure
  ↓
replication health
  ↓
recovery plan
  ↓
network/DNS
  ↓
identity/secrets
  ↓
application validation
```

### Best Practice
Run non-disruptive DR tests and measure end-to-end RTO.

---

## Advanced Deep Dive 60 — Cost Management, Budgets, and Unit Economics

### Concept and Detailed Explanation
Azure Cost Management analyzes actual spend and allocation. Budgets provide thresholds/alerts but are not hard caps. Useful FinOps extends beyond total spend to unit cost such as cost per order, user, or transaction.

### Architecture / Failure Model
```text
Azure usage
  ↓
Cost Management
  ↓
subscription/RG/tag/service analysis
  ↓
Budget alerts + unit economics
```

### Command / Config / Calculation
```text
monthly_cost = 25000
orders = 125000
print('cost/order =', monthly_cost/orders)
```

### Expected Behavior
Teams can identify both absolute spend drivers and whether business unit cost is improving.

### Why It Works
Cloud resources are metered at many dimensions, so ownership and usage context are necessary for meaningful optimization.

### Production Example
Spend rises 20% while order volume rises 50%, making cost per order lower despite a larger bill.

### Troubleshooting Workflow
```text
Cost spike
  ↓
scope
  ↓
service/meter
  ↓
resource/tag
  ↓
usage change
  ↓
architecture cause
```

### Best Practice
Track at least one business-relevant unit-cost metric for each major workload.

---

## Advanced Deep Dive 61 — Reservations, Savings Plans, Spot, and Baseline Capacity

### Concept and Detailed Explanation
Azure Reservations and Savings Plan for Compute exchange commitment for lower eligible compute cost, while Spot VMs exchange reliability for lower price. Stable baseline demand and interruptible burst demand should be analyzed separately.

### Architecture / Failure Model
```text
Demand
  ├─ stable baseline → commitment candidate
  └─ variable/fault-tolerant burst → flexible/Spot
```

### Command / Config / Calculation
```text
Decision inputs:
baseline utilization
term
instance flexibility
eviction tolerance
capacity requirement
```

### Expected Behavior
Discount mechanisms match the predictability and interruption tolerance of the workload.

### Why It Works
Pricing products optimize different economic characteristics and do not replace capacity/reliability design.

### Production Example
A batch analytics pool uses Spot while the 24/7 application baseline is evaluated for Savings Plan coverage.

### Troubleshooting Workflow
```text
Discount waste/eviction issue
  ↓
actual usage
  ↓
commit coverage
  ↓
workload elasticity
  ↓
Spot interruption handling
```

### Best Practice
Commit only measured baseline usage and design Spot workloads to survive eviction.

---

## Advanced Deep Dive 62 — Bicep, ARM What-If, and Safe IaC Changes

### Concept and Detailed Explanation
Bicep provides a higher-level declarative syntax for Azure Resource Manager. Production deployment should include lint/validation, review, `what-if`, policy evaluation, deployment, and post-change verification. What-if predicts resource changes but cannot prove application health.

### Architecture / Failure Model
```text
Git
  ↓
Bicep
  ↓ validate/what-if
ARM
  ↓
Azure resources
  ↓
health verification
```

### Command / Config / Calculation
```text
az bicep build --file main.bicep 2>/dev/null || true
az deployment group what-if -g <RG> -f main.bicep 2>/dev/null || true
```

### Expected Behavior
Reviewers see intended create/modify/delete operations before deployment.

### Why It Works
Declarative IaC lets ARM compare desired resource definitions with current state.

### Production Example
A network change reveals an unexpected subnet replacement in what-if, so the pull request is corrected before production.

### Troubleshooting Workflow
```text
Deployment unexpected
  ↓
Git diff
  ↓
Bicep build
  ↓
what-if
  ↓
Policy
  ↓
ARM deployment operations
```

### Best Practice
Never treat `what-if` as a substitute for staging and runtime validation.

---


# Enhanced Practical Lab Series — Microsoft Azure Fundamentals

These labs extend the uploaded course. Each lab should produce evidence, not only a screenshot. Use read-only discovery first, define the expected state, make the smallest safe change if a sandbox is available, and record rollback/cleanup.

## Enhanced Lab 1 — Azure Scope Hierarchy and Inheritance

### Objective
Turn **Azure Scope Hierarchy and Inheritance** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az account management-group list -o table
az account show -o table
az group list -o table
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The engineer can state which parent scopes influence a resource before changing its local configuration.

### Troubleshooting Path
```text
Unexpected denial
  ↓
identify resource ID
  ↓
walk parent scopes
  ↓
inspect RBAC + Policy inheritance
  ↓
check exemption/deny assignment
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 2 — Microsoft Entra Tenant vs Azure Subscription

### Objective
Turn **Microsoft Entra Tenant vs Azure Subscription** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az account show --query '{subscription:id,tenant:tenantId,user:user}' -o json
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The active tenant and subscription are unambiguous before administration begins.

### Troubleshooting Path
```text
Wrong identity context
  ↓
az account show
  ↓
active tenant?
  ↓
active subscription?
  ↓
re-authenticate/select
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 3 — Azure RBAC Effective Access

### Objective
Turn **Azure RBAC Effective Access** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az role assignment list --assignee <OBJECT_ID> --all -o table
az role definition list --name Reader -o json
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Access decisions can be explained by exact role assignments and scope rather than guessed from group names.

### Troubleshooting Path
```text
AuthorizationFailed
  ↓
principal object ID
  ↓
role assignments
  ↓
parent scopes
  ↓
deny assignments
  ↓
token freshness
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 4 — Entra Directory Roles vs Azure RBAC

### Objective
Turn **Entra Directory Roles vs Azure RBAC** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az ad signed-in-user show -o json
az role assignment list --all -o table
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The team can distinguish identity-plane administration from Azure resource-plane administration.

### Troubleshooting Path
```text
Cannot perform action
  ↓
is it Entra or Azure resource operation?
  ↓
check corresponding role system
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 5 — Privileged Identity Management and Just-in-Time Administration

### Objective
Turn **Privileged Identity Management and Just-in-Time Administration** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Operational design:
Eligible role: Contributor
Activation: 1 hour
MFA: required
Approval: production admin
Justification: ticket ID
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Privileged rights exist only during authorized activation windows.

### Troubleshooting Path
```text
Admin cannot activate
  ↓
eligibility
  ↓
MFA/approval
  ↓
activation policy
  ↓
role assignment propagation
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 6 — Managed Identity Token Flow

### Objective
Turn **Managed Identity Token Flow** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az vm identity show -g <RG> -n <VM> 2>/dev/null || true
az webapp identity show -g <RG> -n <APP> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The workload authenticates without an embedded password or certificate file.

### Troubleshooting Path
```text
Managed identity 403
  ↓
identity enabled?
  ↓
correct principal ID?
  ↓
RBAC/access policy?
  ↓
resource audience/token?
  ↓
network/private endpoint
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 7 — System-Assigned vs User-Assigned Managed Identity

### Objective
Turn **System-Assigned vs User-Assigned Managed Identity** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az identity list -o table
az vm identity show -g <RG> -n <VM> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The selected identity type matches whether permissions should follow one resource or a reusable workload role.

### Troubleshooting Path
```text
Identity missing after rebuild
  ↓
was it system-assigned?
  ↓
new principal ID?
  ↓
recreate role assignments or use user-assigned identity
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 8 — Service Principals and Workload Identity Federation

### Objective
Turn **Service Principals and Workload Identity Federation** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az ad app federated-credential list --id <APP_ID> 2>/dev/null || true
az ad sp show --id <CLIENT_ID> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
CI authenticates to Azure without storing a reusable cloud secret.

### Troubleshooting Path
```text
Federated login fails
  ↓
issuer
  ↓
subject
  ↓
audience
  ↓
app/service principal
  ↓
RBAC assignment
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 9 — Conditional Access and Emergency Access

### Objective
Turn **Conditional Access and Emergency Access** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Policy design:
- admins require phishing-resistant MFA
- legacy auth blocked
- emergency accounts excluded
- emergency sign-in alert enabled
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Normal privileged access is strongly controlled while a tested recovery path remains available.

### Troubleshooting Path
```text
Tenant-wide login failure
  ↓
CA change?
  ↓
emergency account
  ↓
sign-in logs
  ↓
policy condition/control
  ↓
rollback
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 10 — Resource Locks vs Authorization

### Objective
Turn **Resource Locks vs Authorization** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az lock list -o table
az lock create -g <RG> -n protect-prod --lock-type CanNotDelete
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The team understands why an authorized Contributor/Owner operation can still fail against a locked scope.

### Troubleshooting Path
```text
Delete blocked
  ↓
RBAC allows?
  ↓
lock at resource/RG/subscription?
  ↓
change approval
  ↓
remove lock temporarily if authorized
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 11 — Azure Policy Effects and Compliance

### Objective
Turn **Azure Policy Effects and Compliance** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az policy assignment list -o table
az policy state summarize 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Engineers can tell whether a policy prevents creation, reports drift, or remediates configuration.

### Troubleshooting Path
```text
Request denied
  ↓
policy assignment
  ↓
definition/effect
  ↓
scope + parameters
  ↓
exemption?
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 12 — Policy Initiatives, Exemptions, and Remediation

### Objective
Turn **Policy Initiatives, Exemptions, and Remediation** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az policy set-definition list -o table
az policy exemption list 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Compliance reports distinguish genuine violations from approved exceptions.

### Troubleshooting Path
```text
Noncompliance remains
  ↓
policy effect supports remediation?
  ↓
managed identity permissions?
  ↓
remediation task status
  ↓
exception expiry
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 13 — Tags, Inheritance, and Cost Metadata

### Objective
Turn **Tags, Inheritance, and Cost Metadata** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az tag list 2>/dev/null || true
az resource list --query '[].{name:name,tags:tags}' -o json
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Critical resources carry consistent, machine-readable ownership and cost metadata.

### Troubleshooting Path
```text
Missing cost owner
  ↓
resource tags
  ↓
policy assignment
  ↓
deployment template
  ↓
remediate missing metadata
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 14 — Azure Landing Zones as a Platform Product

### Objective
Turn **Azure Landing Zones as a Platform Product** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Landing-zone release checklist:
identity
connectivity
management
security
policy
billing
logging
onboarding
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
New workloads inherit a known governance and connectivity baseline.

### Troubleshooting Path
```text
Workload onboarding inconsistent
  ↓
which foundation capability is missing?
  ↓
move into landing-zone standard
  ↓
version/test/redeploy
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 15 — VNet System Routes and Longest Prefix Match

### Objective
Turn **VNet System Routes and Longest Prefix Match** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network nic show-effective-route-table -g <RG> -n <NIC> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The effective route table explains the next hop chosen for a destination.

### Troubleshooting Path
```text
Packet path wrong
  ↓
effective routes
  ↓
longest matching prefix
  ↓
next hop health
  ↓
return path
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 16 — User-Defined Routes and Forced Tunneling

### Objective
Turn **User-Defined Routes and Forced Tunneling** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network route-table route list -g <RG> --route-table-name <RT> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Outbound flows traverse the intended security path without breaking required Azure service connectivity.

### Troubleshooting Path
```text
Internet unavailable after UDR
  ↓
effective route
  ↓
NVA/firewall forwarding
  ↓
SNAT
  ↓
return route
  ↓
service tags/private endpoints
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 17 — NSG Priority, Direction, and Stateful Behavior

### Objective
Turn **NSG Priority, Direction, and Stateful Behavior** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network nic list-effective-nsg -g <RG> -n <NIC> -o json 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The engineer can identify the exact effective NSG rule that allows or blocks a flow.

### Troubleshooting Path
```text
Flow denied
  ↓
source/destination/port
  ↓
effective NSG
  ↓
priority + direction
  ↓
subnet/NIC combination
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 18 — Application Security Groups as Logical Targets

### Objective
Turn **Application Security Groups as Logical Targets** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network asg list -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Security policy follows application role as instances are replaced or scaled.

### Troubleshooting Path
```text
Rule looks right but flow denied
  ↓
NIC ASG membership
  ↓
NSG source/destination ASG
  ↓
port/protocol
  ↓
effective rules
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 19 — VNet Peering and Non-Transitive Connectivity

### Objective
Turn **VNet Peering and Non-Transitive Connectivity** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network vnet peering list -g <RG> --vnet-name <VNET> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Connectivity expectations match actual peering and gateway/transit configuration.

### Troubleshooting Path
```text
Spoke-to-spoke fails
  ↓
peerings connected?
  ↓
transit/gateway settings?
  ↓
UDRs/firewall?
  ↓
return route
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 20 — Hub-and-Spoke Network Architecture

### Objective
Turn **Hub-and-Spoke Network Architecture** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Architecture inventory:
hub CIDR
spoke CIDRs
peerings
UDRs
shared DNS
gateway transit
inspection paths
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Application spokes receive governed connectivity without hosting duplicate network appliances.

### Troubleshooting Path
```text
Many spokes fail together
  ↓
hub service health
  ↓
firewall/gateway capacity
  ↓
DNS
  ↓
route propagation
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 21 — Azure Firewall, NVAs, and Asymmetric Routing

### Objective
Turn **Azure Firewall, NVAs, and Asymmetric Routing** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network watcher show-next-hop -g <RG> --vm <VM> --source-ip <SRC> --dest-ip <DST> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Forward and return paths are symmetric through required stateful inspection.

### Troubleshooting Path
```text
Intermittent connection
  ↓
forward next hop
  ↓
return next hop
  ↓
UDRs/BGP routes
  ↓
firewall SNAT/state
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 22 — Azure NAT Gateway and Outbound Architecture

### Objective
Turn **Azure NAT Gateway and Outbound Architecture** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network nat gateway list -o table 2>/dev/null || true
az network public-ip list -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Private workloads initiate Internet sessions without individual public IP addresses.

### Troubleshooting Path
```text
Outbound failures
  ↓
subnet NAT association
  ↓
route
  ↓
SNAT port capacity
  ↓
NSG/Firewall
  ↓
DNS/external service
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 23 — Private Endpoint and Private DNS Coupling

### Objective
Turn **Private Endpoint and Private DNS Coupling** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network private-endpoint list -o table 2>/dev/null || true
az network private-dns zone list -o table 2>/dev/null || true
nslookup <service-fqdn>
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Private clients resolve and connect through the private endpoint while public exposure can be disabled where required.

### Troubleshooting Path
```text
Private endpoint failure
  ↓
endpoint approved?
  ↓
DNS A/CNAME chain
  ↓
VNet zone link
  ↓
NSG/UDR
  ↓
service firewall/RBAC
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 24 — Service Endpoints vs Private Endpoints

### Objective
Turn **Service Endpoints vs Private Endpoints** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Decision matrix:
need private IP?
public access disabled?
consumer VNet count?
DNS complexity?
exfiltration requirement?
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The chosen access model matches security and operational requirements.

### Troubleshooting Path
```text
Access unexpectedly public/private
  ↓
which model configured?
  ↓
DNS target
  ↓
service firewall
  ↓
route
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 25 — VPN Gateway, ExpressRoute, and BGP

### Objective
Turn **VPN Gateway, ExpressRoute, and BGP** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network vpn-gateway list 2>/dev/null || true
az network express-route list -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Hybrid paths advertise the intended prefixes and fail over according to business design.

### Troubleshooting Path
```text
Hybrid network outage
  ↓
BGP session
  ↓
learned routes
  ↓
gateway health
  ↓
provider circuit/VPN
  ↓
return path
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 26 — Azure DNS Private Resolver and Hybrid Name Resolution

### Objective
Turn **Azure DNS Private Resolver and Hybrid Name Resolution** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az dns-resolver list -o table 2>/dev/null || true
az network private-dns zone list -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Clients resolve private names through the intended authoritative and forwarding paths.

### Troubleshooting Path
```text
Hybrid DNS failure
  ↓
client resolver
  ↓
forwarding rule
  ↓
inbound/outbound endpoint
  ↓
zone link
  ↓
network path
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 27 — Azure Load Balancer Health Probes

### Objective
Turn **Azure Load Balancer Health Probes** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network lb probe list -g <RG> --lb-name <LB> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Unhealthy backends stop receiving new connections while healthy capacity remains.

### Troubleshooting Path
```text
Backend marked down
  ↓
probe protocol/port/path
  ↓
NSG
  ↓
service listening
  ↓
app dependency
  ↓
threshold
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 28 — Application Gateway Routing and WAF

### Objective
Turn **Application Gateway Routing and WAF** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network application-gateway show-backend-health -g <RG> -n <APPGW> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The gateway routes requests to healthy backends and security rules are applied at the intended layer.

### Troubleshooting Path
```text
502/403 from App Gateway
  ↓
listener/rule
  ↓
backend health
  ↓
probe
  ↓
TLS/backend setting
  ↓
WAF logs
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 29 — Azure Front Door Global Edge Routing

### Objective
Turn **Azure Front Door Global Edge Routing** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az afd profile list -o table 2>/dev/null || true
az afd endpoint list --profile-name <PROFILE> -g <RG> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Users enter through the nearest/appropriate edge and are routed to healthy configured origins.

### Troubleshooting Path
```text
Front Door error
  ↓
endpoint/domain
  ↓
route
  ↓
origin group health
  ↓
WAF
  ↓
TLS/DNS
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 30 — Traffic Manager DNS-Based Routing

### Objective
Turn **Traffic Manager DNS-Based Routing** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az network traffic-manager profile list -o table 2>/dev/null || true
nslookup <traffic-manager-name>
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
DNS answers reflect the selected policy and healthy endpoints.

### Troubleshooting Path
```text
Failover appears slow
  ↓
endpoint health
  ↓
profile policy
  ↓
TTL/cache
  ↓
client resolver
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 31 — Azure VM Boot Path and Platform Diagnostics

### Objective
Turn **Azure VM Boot Path and Platform Diagnostics** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az vm get-instance-view -g <RG> -n <VM> -o json 2>/dev/null || true
az vm boot-diagnostics get-boot-log -g <RG> -n <VM> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The engineer can distinguish Azure platform state from guest-OS and application state.

### Troubleshooting Path
```text
VM unreachable
  ↓
resource health
  ↓
power/provisioning state
  ↓
boot diagnostics
  ↓
NIC/NSG/route
  ↓
guest service
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 32 — Availability Zones vs Availability Sets

### Objective
Turn **Availability Zones vs Availability Sets** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az vm list-skus --location <REGION> --query '[?capabilities]' 2>/dev/null | head
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Architecture uses the failure-domain mechanism appropriate to the service and region.

### Troubleshooting Path
```text
HA design unclear
  ↓
service supports zones?
  ↓
current VM placement
  ↓
SLA/reliability requirement
  ↓
redesign if single domain
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 33 — VM Scale Sets and Autoscale Safety

### Objective
Turn **VM Scale Sets and Autoscale Safety** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az vmss list -o table 2>/dev/null || true
az monitor autoscale list -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Capacity changes without violating the application's minimum healthy instance requirement.

### Troubleshooting Path
```text
VMSS not scaling
  ↓
metric rule
  ↓
min/max/default
  ↓
quota/capacity
  ↓
instance provisioning
  ↓
health
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 34 — Azure Compute Gallery and Image Versioning

### Objective
Turn **Azure Compute Gallery and Image Versioning** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az sig list -o table 2>/dev/null || true
az sig image-version list -g <RG> --gallery-name <GALLERY> --gallery-image-definition <IMAGE> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Running instances can be traced to an approved image version.

### Troubleshooting Path
```text
Unknown image in prod
  ↓
VM image reference
  ↓
gallery version
  ↓
build provenance
  ↓
replace if unapproved
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 35 — Managed Disk Performance and Host Limits

### Objective
Turn **Managed Disk Performance and Host Limits** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az disk show -g <RG> -n <DISK> -o json 2>/dev/null || true
# Linux guest
iostat -xz 1 5 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Performance analysis identifies whether the bottleneck is guest queueing, VM limits, or disk limits.

### Troubleshooting Path
```text
Disk latency high
  ↓
guest iostat
  ↓
VM storage limits
  ↓
disk tier/IOPS/throughput
  ↓
caching/workload pattern
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 36 — App Service Plan and Scaling Model

### Objective
Turn **App Service Plan and Scaling Model** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az appservice plan show -g <RG> -n <PLAN> -o json 2>/dev/null || true
az webapp list -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The team understands whether performance problems come from one application or contention in the shared plan.

### Troubleshooting Path
```text
App Service slow
  ↓
plan CPU/memory
  ↓
which apps share plan
  ↓
autoscale
  ↓
app telemetry
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 37 — Deployment Slots and Configuration Stickiness

### Objective
Turn **Deployment Slots and Configuration Stickiness** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az webapp deployment slot list -g <RG> -n <APP> -o table 2>/dev/null || true
az webapp config appsettings list -g <RG> -n <APP> --slot staging 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
A swap promotes code safely while environment-specific secrets/endpoints remain on the intended slot.

### Troubleshooting Path
```text
Bad state after swap
  ↓
which settings are sticky?
  ↓
slot config
  ↓
connection strings
  ↓
rollback swap
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 38 — Azure Functions Concurrency and Downstream Pressure

### Objective
Turn **Azure Functions Concurrency and Downstream Pressure** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Design values:
max concurrent executions
queue depth
DB max connections
retry/backoff
poison queue
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Function scale stays within the safe capacity of downstream systems.

### Troubleshooting Path
```text
Functions fail during burst
  ↓
instance/concurrency count
  ↓
trigger backlog
  ↓
downstream limits
  ↓
retry/throttle
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 39 — Azure Container Apps Revisions and Event-Driven Scaling

### Objective
Turn **Azure Container Apps Revisions and Event-Driven Scaling** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az containerapp revision list -g <RG> -n <APP> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
New revisions are validated with controlled traffic and scale to demand without direct node management.

### Troubleshooting Path
```text
Revision unhealthy
  ↓
image start
  ↓
env/secrets
  ↓
ingress port
  ↓
scale rule
  ↓
logs
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 40 — AKS Shared Responsibility and Control Loops

### Objective
Turn **AKS Shared Responsibility and Control Loops** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az aks show -g <RG> -n <AKS> -o json 2>/dev/null || true
kubectl get nodes,pods -A 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The team can state which failures belong to Azure platform, cluster configuration, node pools, or workload code.

### Troubleshooting Path
```text
AKS app down
  ↓
cluster/API health
  ↓
nodes
  ↓
pods/events
  ↓
network/storage
  ↓
app logs
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 41 — Azure Container Registry and Image Supply Chain

### Objective
Turn **Azure Container Registry and Image Supply Chain** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az acr list -o table 2>/dev/null || true
az acr repository list -n <ACR> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Every deployed container can be traced to a tested image digest and build commit.

### Troubleshooting Path
```text
Image pull/unknown image
  ↓
registry/digest
  ↓
identity role AcrPull
  ↓
network/private endpoint
  ↓
build provenance
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 42 — Blob Versioning, Soft Delete, and Immutability

### Objective
Turn **Blob Versioning, Soft Delete, and Immutability** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az storage account blob-service-properties show --account-name <ACCOUNT> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Operators know which mechanism can recover an overwritten, deleted, or maliciously modified object.

### Troubleshooting Path
```text
Blob lost
  ↓
versioning?
  ↓
soft delete window?
  ↓
immutable copy?
  ↓
backup/replication
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 43 — Storage Redundancy and Failure Domains

### Objective
Turn **Storage Redundancy and Failure Domains** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Decision inputs:
zone failure tolerance
regional DR
secondary read need
RPO
cost
service support
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The storage redundancy option directly maps to the business failure scenario and recovery requirement.

### Troubleshooting Path
```text
Storage incident
  ↓
which redundancy SKU?
  ↓
primary/secondary availability
  ↓
last sync / RPO
  ↓
failover procedure
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 44 — Blob Lifecycle Management

### Objective
Turn **Blob Lifecycle Management** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az storage account management-policy show -g <RG> --account-name <ACCOUNT> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Data moves to cost-appropriate tiers without violating retention or recovery requirements.

### Troubleshooting Path
```text
Unexpected deletion/tier
  ↓
management policy
  ↓
matching prefix/tags
  ↓
version state
  ↓
retention requirement
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 45 — Azure Files and Azure File Sync

### Objective
Turn **Azure Files and Azure File Sync** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az storage share list --account-name <ACCOUNT> --auth-mode login 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Users retain shared-file semantics while Azure provides central durable storage and optional local caching.

### Troubleshooting Path
```text
File missing/stale
  ↓
sync group
  ↓
server endpoint health
  ↓
cloud endpoint
  ↓
conflict/tiering
  ↓
identity/network
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 46 — Azure SQL High Availability and Connection Resilience

### Objective
Turn **Azure SQL High Availability and Connection Resilience** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Application design:
connect timeout
retry with backoff
pool recycle
idempotent transaction retry where safe
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Brief platform failovers cause recoverable connection errors instead of prolonged application outage.

### Troubleshooting Path
```text
Azure SQL outage
  ↓
Service Health/resource health
  ↓
DNS/private endpoint
  ↓
firewall/RBAC
  ↓
connections
  ↓
query/DB health
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 47 — Cosmos DB Partition Keys

### Objective
Turn **Cosmos DB Partition Keys** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Design worksheet:
query pattern
partition key
cardinality
expected RU/s
hot-key risk
cross-partition queries
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Traffic and storage distribute evenly enough for the workload and key-based queries remain efficient.

### Troubleshooting Path
```text
Cosmos throttling/high RU
  ↓
hot partition?
  ↓
query fan-out?
  ↓
item size/indexing
  ↓
throughput mode
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 48 — Cosmos DB Consistency Models

### Objective
Turn **Cosmos DB Consistency Models** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Decision inputs:
read-after-write requirement
acceptable staleness
multi-region writes
latency
availability
business semantics
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The consistency choice is justified by the application's correctness requirements.

### Troubleshooting Path
```text
Unexpected stale read
  ↓
consistency level
  ↓
session token/client behavior
  ↓
region routing
  ↓
replication state
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 49 — Azure Service Bus Delivery Semantics

### Objective
Turn **Azure Service Bus Delivery Semantics** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az servicebus queue show -g <RG> --namespace-name <NS> -n <QUEUE> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Failed processing returns messages for retry and poison messages move to the dead-letter queue.

### Troubleshooting Path
```text
Duplicate/backlog
  ↓
lock duration
  ↓
max delivery count
  ↓
DLQ
  ↓
consumer idempotency
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 50 — Event Grid vs Event Hubs

### Objective
Turn **Event Grid vs Event Hubs** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Scenario mapping:
Blob created notification → Event Grid
1M telemetry events/min → Event Hubs
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The selected service matches whether the workload is reactive event notification or sustained streaming ingestion.

### Troubleshooting Path
```text
Wrong messaging service
  ↓
event rate
  ↓
retention/replay need
  ↓
ordering/partitions
  ↓
subscriber model
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 51 — API Management as a Policy Gateway

### Objective
Turn **API Management as a Policy Gateway** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Policy examples:
validate-jwt
rate-limit
set-header
rewrite-uri
cache-lookup
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Backend services receive controlled, authenticated, and observable API traffic.

### Troubleshooting Path
```text
API 401/429/5xx
  ↓
APIM trace
  ↓
policy execution
  ↓
backend health
  ↓
DNS/private endpoint
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 52 — Key Vault Control Plane vs Data Plane

### Objective
Turn **Key Vault Control Plane vs Data Plane** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az keyvault show -n <VAULT> -o json 2>/dev/null || true
az keyvault secret list --vault-name <VAULT> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Administration of the vault resource is separated from sensitive secret/key use.

### Troubleshooting Path
```text
Key Vault 403
  ↓
network/private endpoint
  ↓
data-plane RBAC/access policy
  ↓
principal/token
  ↓
secret/key state
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 53 — Secret and Certificate Rotation

### Objective
Turn **Secret and Certificate Rotation** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Rotation record:
secret name
old version
new version
consumer list
verification
retirement time
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
All consumers authenticate with the new credential before the old one is disabled.

### Troubleshooting Path
```text
Post-rotation auth failure
  ↓
current Key Vault version
  ↓
provider credential
  ↓
consumer cache
  ↓
managed identity/secret reference
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 54 — Defender for Cloud and Security Operations

### Objective
Turn **Defender for Cloud and Security Operations** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Security workflow fields:
subscription
resource
finding
severity
exposure
owner
due date
exception
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Security recommendations become actionable engineering work with traceable closure.

### Troubleshooting Path
```text
Finding volume high
  ↓
prioritize exposure/business criticality
  ↓
validate false positive
  ↓
remediate/exception
  ↓
verify
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 55 — Azure Monitor Telemetry Model

### Objective
Turn **Azure Monitor Telemetry Model** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az monitor metrics list --resource <RESOURCE_ID> --metric <METRIC> 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
An alert can be correlated with detailed logs and application dependencies on one timeline.

### Troubleshooting Path
```text
Incident
  ↓
metric/SLO symptom
  ↓
logs
  ↓
trace/dependency
  ↓
Activity Log/recent deployment
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 56 — KQL for Evidence-Driven Troubleshooting

### Objective
Turn **KQL for Evidence-Driven Troubleshooting** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
AzureActivity
| where TimeGenerated > ago(1h)
| where ActivityStatusValue == 'Failure'
| project TimeGenerated, OperationNameValue, Caller, ResourceGroup
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The query produces a small evidence set tied to the incident window.

### Troubleshooting Path
```text
Query returns too much/nothing
  ↓
workspace/table
  ↓
time range
  ↓
field names
  ↓
resource ID
  ↓
ingestion delay
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 57 — Activity Log, Resource Health, and Service Health

### Objective
Turn **Activity Log, Resource Health, and Service Health** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az monitor activity-log list --offset 1h -o table 2>/dev/null || true
az rest --method get --url 'https://management.azure.com/subscriptions/<SUB>/providers/Microsoft.ResourceHealth/events?api-version=2022-10-01' 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
The incident investigation uses the source matching change history, resource health, or platform event.

### Troubleshooting Path
```text
Outage
  ↓
recent Activity Log?
  ↓
Resource Health?
  ↓
Service Health?
  ↓
workload telemetry
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 58 — Azure Backup Vault Isolation and Restore Testing

### Objective
Turn **Azure Backup Vault Isolation and Restore Testing** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az backup vault list -o table 2>/dev/null || true
az backup job list --vault-name <VAULT> -g <RG> -o table 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Recovery points exist, are protected from ordinary operational mistakes, and have proven restore procedures.

### Troubleshooting Path
```text
Restore fails
  ↓
recovery point
  ↓
vault/KMS access
  ↓
network/identity
  ↓
application consistency
  ↓
runbook gap
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 59 — Azure Site Recovery and DR Orchestration

### Objective
Turn **Azure Site Recovery and DR Orchestration** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az site-recovery vault list 2>/dev/null || true
DR checklist:
network mapping
recovery plan
DNS
secrets
capacity
validation
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Test failover proves the workload can recover without disrupting production.

### Troubleshooting Path
```text
DR test failure
  ↓
replication health
  ↓
recovery plan
  ↓
network/DNS
  ↓
identity/secrets
  ↓
application validation
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 60 — Cost Management, Budgets, and Unit Economics

### Objective
Turn **Cost Management, Budgets, and Unit Economics** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
monthly_cost = 25000
orders = 125000
print('cost/order =', monthly_cost/orders)
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Teams can identify both absolute spend drivers and whether business unit cost is improving.

### Troubleshooting Path
```text
Cost spike
  ↓
scope
  ↓
service/meter
  ↓
resource/tag
  ↓
usage change
  ↓
architecture cause
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 61 — Reservations, Savings Plans, Spot, and Baseline Capacity

### Objective
Turn **Reservations, Savings Plans, Spot, and Baseline Capacity** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
Decision inputs:
baseline utilization
term
instance flexibility
eviction tolerance
capacity requirement
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Discount mechanisms match the predictability and interruption tolerance of the workload.

### Troubleshooting Path
```text
Discount waste/eviction issue
  ↓
actual usage
  ↓
commit coverage
  ↓
workload elasticity
  ↓
Spot interruption handling
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---

## Enhanced Lab 62 — Bicep, ARM What-If, and Safe IaC Changes

### Objective
Turn **Bicep, ARM What-If, and Safe IaC Changes** into an observable engineering exercise.

### Preparation
1. Verify the active identity and administrative scope.
2. Record region/location, network, resource/project/subscription, and cost context.
3. Capture the before-state with read-only discovery.
4. Write the expected result before changing anything.

### Mental Model
```text
Requirement
  ↓
Control-plane object / policy
  ↓
Runtime or data-plane behavior
  ↓
Logs / metrics / state evidence
  ↓
Correction / prevention
```

### Commands / Data
```text
az bicep build --file main.bicep 2>/dev/null || true
az deployment group what-if -g <RG> -f main.bicep 2>/dev/null || true
```

### Procedure
1. Draw the dependency path.
2. Identify the resource or policy that owns the behavior.
3. Run the read-only evidence commands.
4. If you have a disposable lab, create or modify the smallest test case.
5. Verify runtime behavior independently from control-plane success.
6. Introduce one reversible misconfiguration only in the lab when safe.
7. Diagnose using the troubleshooting path.
8. Restore the intended state.
9. Record `Symptom → Layer → Evidence → Root Cause → Correction → Prevention`.

### Expected Result
Reviewers see intended create/modify/delete operations before deployment.

### Troubleshooting Path
```text
Deployment unexpected
  ↓
Git diff
  ↓
Bicep build
  ↓
what-if
  ↓
Policy
  ↓
ARM deployment operations
```

### Safety / Cost Control
Use an authorized Azure sandbox or read-only tenant. Verify `az account show` / `Get-AzContext` before writes. Check pricing before creating VMs, NAT Gateway, Firewall, Application Gateway, Front Door, SQL, AKS, or backup/DR resources. Delete disposable resources after the lab. Never expose real secrets or production endpoints for practice.

---


## 5. Hands-on Lab / Practical Exercises

> Use a free/authorized lab where possible. Verify current pricing before creating resources.

### Lab 1 — Verify Azure Context

CLI:

```bash
az account show
```

PowerShell:

```powershell
Get-AzContext
```

Record:

```text
tenant
subscription
identity
```

### Lab 2 — Resource Hierarchy

Design:

```text
Tenant Root
├─ Platform
│  ├─ Connectivity
│  └─ Management
└─ LandingZones
   ├─ Production
   └─ NonProduction
```

Place subscriptions and resource groups.

### Lab 3 — Shared Responsibility

Create matrix for:

```text
VM
App Service
Azure SQL Database
Microsoft 365-like SaaS
```

Rows:

```text
physical
hypervisor
OS
runtime
application
identity
data
```

### Lab 4 — Entra + RBAC

Design:

```text
CloudAdmin
NetworkOperator
SecurityReader
AppDeveloper
BillingReader
```

Assign roles at correct scopes.

### Lab 5 — Conditional Access Tabletop

Policy:

```text
Admins
→ require MFA
→ require compliant device
→ block high-risk sign-in
```

Explain risks of misconfiguration and emergency access.

### Lab 6 — Managed Identity

Draw:

```text
App Service
 ↓ Managed Identity
Key Vault
```

No password in application config.

### Lab 7 — VNet CIDR

Use:

```text
10.20.0.0/16
```

Create:

```text
GatewaySubnet
AzureFirewallSubnet
Web
App
DB
PrivateEndpoints
```

### Lab 8 — NSG Design

Rules:

```text
Internet → AppGateway 443
AppGateway → Web 443
Web → App 8443
App → DB 1433
```

No Internet-to-DB.

### Lab 9 — Private Endpoint

Design private access to:

```text
Storage Account
Key Vault
Azure SQL
```

Include private DNS.

### Lab 10 — Hybrid Connectivity

Compare:

```text
VPN Gateway
ExpressRoute
```

for:

```text
branch office
datacenter primary circuit
temporary migration
backup path
```

### Lab 11 — Compute Selection

Choose:

```text
VM
VMSS
App Service
Functions
Container Apps
AKS
ACI
```

for seven scenarios.

### Lab 12 — VM Availability

Compare:

```text
single VM
availability set
availability zones
VMSS across zones
```

for reliability.

### Lab 13 — Storage Selection

Map:

```text
object files
shared SMB
VM disk
simple queue
NoSQL key table
```

to:

```text
Blob
Files
Managed Disk
Queue
Table
```

### Lab 14 — Storage Redundancy

Choose:

```text
LRS
ZRS
GRS
RA-GRS
GZRS
RA-GZRS
```

for six durability/DR scenarios.

### Lab 15 — Blob Lifecycle

Design:

```text
Hot → Cool → Cold → Archive → Delete
```

according to fictional access patterns.

### Lab 16 — Migration Tools

Select:

```text
Azure Migrate
Data Box
AzCopy
File Sync
Storage Explorer
```

for five migration tasks.

### Lab 17 — Database Selection

Choose:

```text
Azure SQL Database
SQL Managed Instance
SQL on VM
PostgreSQL
Cosmos DB
```

for five scenarios.

### Lab 18 — Governance Matrix

Select:

```text
Azure Policy
RBAC
Resource Lock
Tags
Purview
```

for:

```text
deny unapproved Region
grant Reader
prevent delete
track cost owner
data governance
```

### Lab 19 — ARM/Bicep

Create a simple Bicep design for:

```text
resource group deployment
storage account
tag
```

Explain declarative deployment.

### Lab 20 — Azure CLI Read-Only Discovery

```bash
az group list -o table
az vm list --show-details -o table
az network vnet list -o table
```

### Lab 21 — Azure PowerShell Discovery

```powershell
Get-AzResourceGroup
Get-AzVM
Get-AzVirtualNetwork
```

### Lab 22 — Monitoring Selection

Choose:

```text
Azure Monitor
Log Analytics
Application Insights
Advisor
Service Health
```

for five scenarios.

### Lab 23 — KQL Starter

Conceptual query:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| project TimeGenerated, OperationNameValue, Caller, ActivityStatusValue
```

Explain what question it answers.

### Lab 24 — Cost Review

Fictional spend:

```text
VMs $800
SQL $700
Storage $250
Egress $300
```

Use:

```text
Cost Management
Budgets
Pricing Calculator
Reservations
Savings Plan
Spot
Hybrid Benefit
```

to optimize.

### Lab 25 — Well-Architected Review

Review one workload against:

```text
Reliability
Security
Cost Optimization
Operational Excellence
Performance Efficiency
```

### Lab 26 — Landing Zone Design

Include:

```text
management groups
subscriptions
policy
RBAC
hub networking
logging
security
budgets
```

### Lab 27 — Architecture Diagram

Design:

```text
Azure DNS
 ↓
Front Door + WAF
 ↓
App Gateway
 ↓
App Service/VMSS across zones
 ↓
Azure SQL
 ↓
Blob
```

Add Key Vault, Monitor, Defender, Backup.

### Lab 28 — Exam Scenario Drill

Create 30 prompts such as:

```text
Need private dedicated circuit?
Need prevent delete?
Need global HTTP routing?
Need serverless?
Need data governance?
Need app telemetry?
```

For each:

```text
answer
why
two distractors
```

### Lab 29 — Access and Network Troubleshooting

Analyze:

```text
RBAC denied
VM unreachable
Private Endpoint DNS fails
SQL inaccessible
Storage returns 403
```

### Lab 30 — Cost / Reliability / Governance Challenge

For a production portal, identify:

```text
single points of failure
governance gaps
identity risks
cost waste
missing monitoring
missing backup
```

and redesign.

---

## 6. Mini Project

# Mini Project — Azure Enterprise Portal Foundation

Requirements:

```text
production + nonproduction
5,000 daily users
sensitive customer data
RPO 1 hour
RTO 4 hours
hybrid corporate connectivity
```

Architecture:

```text
                       Azure DNS
                           |
                    Azure Front Door
                           |
                          WAF
                           |
                  Application Gateway
                    /             \
                 Zone 1           Zone 2
                    |               |
             App Service/VMSS  App Service/VMSS
                    \               /
                     Azure SQL / Managed DB
                            |
                       Blob Storage
                            |
                        Azure Backup
```

Governance:

```text
Management Groups
Subscriptions
Resource Groups
RBAC
Policy
Locks
Tags
Budgets
```

Identity:

```text
Entra ID
MFA
Conditional Access
Managed Identity
Emergency account
```

Networking:

```text
Hub-Spoke
ExpressRoute
VPN backup
Azure Firewall
Private Endpoints
Private DNS
```

Operations:

```text
Monitor
Log Analytics
Application Insights
Service Health
Advisor
Defender for Cloud
```

Deliverables:

```text
README.md
ARCHITECTURE.md
HIERARCHY.md
IDENTITY.md
NETWORK.md
COMPUTE.md
STORAGE.md
DATA.md
SECURITY.md
GOVERNANCE.md
MONITORING.md
BACKUP_DR.md
COST.md
AUTOMATION.md
RUNBOOKS/
```

Required runbooks:

```text
RUNBOOK_RBAC_DENIED.md
RUNBOOK_VM_UNREACHABLE.md
RUNBOOK_PRIVATE_ENDPOINT.md
RUNBOOK_SQL_FAILURE.md
RUNBOOK_SERVICE_HEALTH.md
RUNBOOK_COST_SPIKE.md
RUNBOOK_SECRET_COMPROMISE.md
```

---


# Expanded Capstone — Azure Enterprise Landing Zone + Customer Platform

Build an Azure design that can later be implemented in the Azure Administration, Terraform, DevOps, and Cloud Security phases.

## 1. Business Scenario

Design for:

```text
customer portal
supplier portal
manufacturing API integration
ERP integration
production + staging + development
5,000 daily users
peak 500 concurrent users
RPO = 1 hour
RTO = 4 hours
hybrid connectivity to two factories
sensitive customer and order data
```

Convert the business targets into engineering requirements:

```text
availability SLO
failure domains
minimum instance count
backup frequency
restore test frequency
database HA
network path
identity controls
cost allocation
```

## 2. Tenant and Management-Group Design

```text
Microsoft Entra Tenant
└─ Tenant Root Group
   ├─ Platform
   │  ├─ Identity
   │  ├─ Connectivity
   │  └─ Management
   ├─ LandingZones
   │  ├─ Production
   │  └─ NonProduction
   └─ Sandbox
```

Document:

```text
RBAC inheritance
Policy inheritance
subscription ownership
billing ownership
PIM roles
break-glass access
```

## 3. Subscription Model

Use separate subscriptions for:

```text
Connectivity
Management / Logging
Security
Production Application
Production Data
NonProduction
Sandbox
```

Explain why a subscription boundary is stronger than only separating resource groups.

## 4. Identity

Use:

```text
Entra federation/SSO
MFA
Conditional Access
PIM
managed identities
workload identity federation for CI
break-glass identities
```

No production application may use:

```text
developer password
hard-coded secret
shared personal account
```

## 5. RBAC Matrix

Create:

```text
Role / Group
Scope
Required Actions
Why
Activation model
```

Include:

```text
PlatformAdmin
NetworkAdmin
SecurityReader
ApplicationDeployer
DatabaseOperator
BillingReader
CI/CD identity
Application managed identity
Backup operator
```

## 6. Policy and Guardrails

Create an initiative containing policies such as:

```text
allowed regions
required Owner/CostCenter/Environment tags
deny public database access
audit missing diagnostic settings
require approved storage redundancy
restrict public IPs
audit Key Vault network exposure
```

Define:

```text
effect
scope
parameters
exemption process
remediation process
```

## 7. Network

Use hub-and-spoke:

```text
Factories / On-Prem
      |
ExpressRoute
 + HA VPN backup
      |
Hub VNet
├─ Azure Firewall
├─ DNS Private Resolver
├─ Bastion/management if justified
├─ Private DNS
└─ Shared services
      |
+-----+------+
|            |
Prod Spoke   NonProd Spoke
```

Document for each important flow:

```text
source
destination
port/protocol
DNS name
route
security rule
inspection path
return path
```

## 8. Private PaaS Access

Use Private Endpoint where justified for:

```text
Azure SQL
Storage
Key Vault
Container Registry
```

For each, document:

```text
private endpoint subnet
private DNS zone
VNet links
public network setting
RBAC/data-plane permission
```

## 9. Compute

Compare:

```text
VMSS
App Service
Container Apps
AKS
Functions
```

Choose one primary runtime for the customer portal and justify:

```text
operational overhead
autoscaling
network requirements
deployment model
identity
cost
team skills
```

## 10. VM / Image Pipeline

If VMs/VMSS are used:

```text
trusted source image
   ↓
patch/harden
   ↓
test
   ↓
Azure Compute Gallery
   ↓
versioned image
   ↓
VMSS rolling upgrade
```

Record:

```text
image version
build commit
scan result
rollback version
```

## 11. Edge and Traffic

Design:

```text
Azure DNS
  ↓
Azure Front Door + WAF
  ↓
Application Gateway where regional L7 need exists
  ↓
Application runtime
```

Explain whether both Front Door and Application Gateway are justified.

## 12. Data

Use:

```text
Azure SQL Database / Managed Instance
Cosmos DB only if access pattern justifies it
Blob Storage
Azure Files only if filesystem semantics are required
Service Bus for asynchronous business workflows
Event Hubs for high-volume telemetry
```

## 13. Messaging

Example:

```text
Order Created
  ↓
Service Bus Topic
  ├─ Billing Subscription
  ├─ Notification Subscription
  └─ Analytics Subscription
```

Define:

```text
message ID
idempotency key
lock duration
retry
dead-letter behavior
schema version
```

## 14. Key Vault

Design:

```text
application managed identity
    ↓
Key Vault
    ↓
secret / certificate / key
```

Define:

```text
RBAC
private endpoint
rotation
versioning
emergency access
logging
```

## 15. Observability

Use:

```text
Azure Monitor
Log Analytics
Application Insights
Activity Log
Service Health
Resource Health
```

Required signals:

```text
availability
request rate
p95/p99 latency
5xx rate
database connections
queue depth
VM/app saturation
backup status
policy compliance
cost anomaly
```

## 16. KQL Evidence

Write queries for:

```text
failed control-plane operations
authentication failures
application exceptions
slow dependencies
firewall denies
deployment correlation
```

## 17. Backup and DR

Design:

```text
Azure Backup vault
soft-delete/immutability controls where applicable
separation of duties
quarterly restore test
ASR or application-native regional DR where justified
```

Measure:

```text
actual RPO
actual RTO
```

Do not count a successful backup job as a successful DR test.

## 18. FinOps

Use:

```text
Cost Management
Budgets
mandatory tags
Pricing Calculator
Reservations/Savings Plan analysis
Spot candidates
Hybrid Benefit where licensed
```

Track:

```text
cost per user
cost per order
cost by application
cost by environment
```

## 19. IaC

Use:

```text
Git
  ↓
Bicep
  ↓
lint/build
  ↓
what-if
  ↓
Policy evaluation
  ↓
ARM deployment
  ↓
runtime verification
```

Separate ownership between:

```text
Bicep/Terraform → cloud resources
configuration management → guest OS where used
application CI/CD → application artifacts
```

## 20. Failure Scenarios

Tabletop:

```text
wrong subscription deployment
Conditional Access lockout
Private Endpoint DNS failure
hub firewall outage
zone failure
App Service bad slot swap
VMSS bad image rollout
Azure SQL transient failover
Service Bus backlog
Key Vault access denied
region service incident
backup restore failure
cost spike
```

For each write:

```text
Symptom
Blast Radius
Evidence
Root Cause
Containment
Recovery
Prevention
```

## Required Deliverables

```text
README.md
HIERARCHY.md
SUBSCRIPTIONS.md
IDENTITY.md
RBAC.md
POLICY.md
NETWORK.md
PRIVATE_ENDPOINTS.md
COMPUTE.md
IMAGE_PIPELINE.md
EDGE.md
DATA.md
MESSAGING.md
KEY_VAULT.md
OBSERVABILITY.md
BACKUP_DR.md
FINOPS.md
IAC.md
RUNBOOKS/
```


## 7. Recommended Resources

This Markdown is intended to be self-contained.

For current production behavior, use official Microsoft sources:

```text
AZ-900 Study Guide
Microsoft Certified: Azure Fundamentals
Azure Architecture Center
Azure Well-Architected Framework
Cloud Adoption Framework
Azure Reliability documentation
Microsoft Entra documentation
Azure networking/storage/compute documentation
Azure Monitor
Cost Management
```

Current exam baseline:

```text
Skills measured as of July 20, 2026
```

---

## 8. Certification Relevance

Direct certification:

```text
Microsoft Certified: Azure Fundamentals
Exam AZ-900
```

Current skill domains:

```text
Cloud concepts                    25–30%
Architecture and services         35–40%
Management and governance         30–35%
```

The Microsoft certification page currently states:

```text
Assessment duration: 45 minutes
```

This course prepares for later:

```text
55. Microsoft Azure Administration
Cloud Security
Terraform
DevOps
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Entra ID = AD DS.  
  **Best practice:** understand cloud identity vs traditional domain services.

- **Mistake:** RBAC = Policy.  
  **Best practice:** RBAC controls who; Policy controls allowed/required resource configuration.

- **Mistake:** Resource Lock = permission system.  
  **Best practice:** use locks as additional change/delete protection.

- **Mistake:** One subscription for everything.  
  **Best practice:** use hierarchy/account boundaries based on management, billing, policy, and blast radius.

- **Mistake:** Public PaaS endpoints by default.  
  **Best practice:** use private endpoints when workload requirements justify it.

- **Mistake:** NSG alone equals complete security.  
  **Best practice:** identity + network + app + data + governance defense in depth.

- **Mistake:** App Service and VM are equivalent.  
  **Best practice:** understand PaaS vs IaaS responsibility.

- **Mistake:** Front Door = Application Gateway.  
  **Best practice:** global edge vs regional application load balancing.

- **Mistake:** ZRS and GRS are the same.  
  **Best practice:** zone resilience vs geo replication.

- **Mistake:** Service Health = Azure Monitor.  
  **Best practice:** platform incidents vs workload telemetry.

- **Mistake:** Tags automatically enforce governance.  
  **Best practice:** use Policy and processes to enforce metadata.

- **Mistake:** Budget automatically stops spending.  
  **Best practice:** budget alerts require deliberate automated controls for shutdown actions.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Current Azure Fundamentals exam code?

**Short answer:** AZ-900.

### Q2. Current largest exam domain?

**Short answer:** Azure architecture and services, 35–40%.

### Q3. Azure resource hierarchy?

**Short answer:** Management groups → subscriptions → resource groups → resources.

### Q4. Entra ID?

**Short answer:** Microsoft cloud identity and access directory service.

### Q5. Entra ID vs Entra Domain Services?

**Short answer:** Entra ID is cloud identity; Domain Services provides managed traditional domain capabilities.

### Q6. Azure RBAC?

**Short answer:** Authorization system assigning roles to principals at Azure scopes.

### Q7. Conditional Access?

**Short answer:** Identity policy engine that evaluates signals and applies access controls such as MFA/block/device requirements.

### Q8. Managed Identity?

**Short answer:** Azure workload identity that avoids storing application credentials.

### Q9. Azure VM?

**Short answer:** IaaS virtual machine.

### Q10. VMSS?

**Short answer:** Managed fleet/scaling model for Azure VMs.

### Q11. Availability Zone?

**Short answer:** Independent datacenter group/failure domain within an Azure Region.

### Q12. VNet?

**Short answer:** Azure software-defined private network.

### Q13. NSG?

**Short answer:** Stateful network-security rule set for subnets/NICs.

### Q14. ExpressRoute?

**Short answer:** Private dedicated connectivity from customer/provider network to Microsoft cloud.

### Q15. Private Endpoint?

**Short answer:** Private IP network interface in your VNet providing private access to a supported Azure service.

### Q16. Load Balancer vs Application Gateway?

**Short answer:** Layer 4 TCP/UDP vs Layer 7 HTTP/S regional routing.

### Q17. Front Door?

**Short answer:** Global edge HTTP/S routing/application-delivery service.

### Q18. Blob Storage?

**Short answer:** Azure object storage.

### Q19. Azure Files?

**Short answer:** Managed shared file storage.

### Q20. LRS vs ZRS?

**Short answer:** Local redundancy in one primary location vs replication across availability zones.

### Q21. GRS?

**Short answer:** Geo-redundant storage with asynchronous copy to secondary Region.

### Q22. Azure Migrate?

**Short answer:** Discovery/assessment/migration service family for moving workloads to Azure.

### Q23. Azure Policy?

**Short answer:** Governance service that audits/enforces resource configuration rules.

### Q24. Resource Lock?

**Short answer:** Prevents deletion or modification according to lock type.

### Q25. Azure Monitor?

**Short answer:** Azure monitoring platform for metrics, logs, alerts, and telemetry.

### Q26. Log Analytics?

**Short answer:** Azure Monitor Logs workspace/query platform using KQL.

### Q27. Application Insights?

**Short answer:** Application-performance/telemetry monitoring within Azure Monitor.

### Q28. Service Health?

**Short answer:** Personalized Azure service incident/maintenance/advisory information.

### Q29. Azure Advisor?

**Short answer:** Azure recommendations for architecture/operations optimization.

### Q30. ARM?

**Short answer:** Azure Resource Manager control-plane/deployment management layer.

---

# Expanded Self-Assessment Bank — Microsoft Azure Fundamentals

### Q1. What is the most important operational lesson from **Azure Scope Hierarchy and Inheritance**?
**Answer:** Always troubleshoot Azure permissions and policy from the resource upward through every parent scope.

### Q2. What is the most important operational lesson from **Microsoft Entra Tenant vs Azure Subscription**?
**Answer:** Make tenant and subscription verification the first line of every privileged runbook.

### Q3. What is the most important operational lesson from **Azure RBAC Effective Access**?
**Answer:** Never grant Owner as a diagnostic shortcut; identify the missing action and effective scope.

### Q4. What is the most important operational lesson from **Entra Directory Roles vs Azure RBAC**?
**Answer:** Classify every privilege request as identity-plane or resource-plane before assigning a role.

### Q5. What is the most important operational lesson from **Privileged Identity Management and Just-in-Time Administration**?
**Answer:** Use permanent active privilege only when a documented operational requirement justifies it.

### Q6. What is the most important operational lesson from **Managed Identity Token Flow**?
**Answer:** Prefer managed identity for Azure-hosted workloads whenever the target service supports Entra authentication.

### Q7. What is the most important operational lesson from **System-Assigned vs User-Assigned Managed Identity**?
**Answer:** Use user-assigned identities when identity continuity must survive compute replacement.

### Q8. What is the most important operational lesson from **Service Principals and Workload Identity Federation**?
**Answer:** Prefer federated workload identity to stored service-principal secrets for modern CI/CD.

### Q9. What is the most important operational lesson from **Conditional Access and Emergency Access**?
**Answer:** Test emergency accounts periodically and alert on every use.

### Q10. What is the most important operational lesson from **Resource Locks vs Authorization**?
**Answer:** Use locks for high-impact accidental actions, but still design least-privilege RBAC.

### Q11. What is the most important operational lesson from **Azure Policy Effects and Compliance**?
**Answer:** Use deny only for clear invariants and stage new policies in audit mode before broad enforcement.

### Q12. What is the most important operational lesson from **Policy Initiatives, Exemptions, and Remediation**?
**Answer:** Every exemption should have an owner, justification, and review/expiry date.

### Q13. What is the most important operational lesson from **Tags, Inheritance, and Cost Metadata**?
**Answer:** Define a controlled tag dictionary and enforce required tags at creation.

### Q14. What is the most important operational lesson from **Azure Landing Zones as a Platform Product**?
**Answer:** Manage the landing zone through code, releases, ownership, and documented onboarding contracts.

### Q15. What is the most important operational lesson from **VNet System Routes and Longest Prefix Match**?
**Answer:** Use effective route tables during troubleshooting instead of reasoning only from configured route-table objects.

### Q16. What is the most important operational lesson from **User-Defined Routes and Forced Tunneling**?
**Answer:** Change UDRs with a rollback path because a single default route can disconnect entire subnets.

### Q17. What is the most important operational lesson from **NSG Priority, Direction, and Stateful Behavior**?
**Answer:** Use narrow service-to-service rules and document every broad Internet rule.

### Q18. What is the most important operational lesson from **Application Security Groups as Logical Targets**?
**Answer:** Prefer identity-like workload grouping over static IP lists inside a VNet.

### Q19. What is the most important operational lesson from **VNet Peering and Non-Transitive Connectivity**?
**Answer:** Document which component provides transit; do not infer it from peering diagrams.

### Q20. What is the most important operational lesson from **Hub-and-Spoke Network Architecture**?
**Answer:** Treat the hub as production platform infrastructure with its own SLO and capacity model.

### Q21. What is the most important operational lesson from **Azure Firewall, NVAs, and Asymmetric Routing**?
**Answer:** Validate both directions of every inspected flow.

### Q22. What is the most important operational lesson from **Azure NAT Gateway and Outbound Architecture**?
**Answer:** Prefer explicit outbound architecture instead of relying on implicit/default outbound behavior.

### Q23. What is the most important operational lesson from **Private Endpoint and Private DNS Coupling**?
**Answer:** Treat private DNS configuration as part of every Private Endpoint deployment.

### Q24. What is the most important operational lesson from **Service Endpoints vs Private Endpoints**?
**Answer:** Choose one access model deliberately and document why it satisfies the threat model.

### Q25. What is the most important operational lesson from **VPN Gateway, ExpressRoute, and BGP**?
**Answer:** Test hybrid failover periodically; having two circuits is not proof that routing will fail over correctly.

### Q26. What is the most important operational lesson from **Azure DNS Private Resolver and Hybrid Name Resolution**?
**Answer:** Document DNS authority and forwarding exactly like route tables.

### Q27. What is the most important operational lesson from **Azure Load Balancer Health Probes**?
**Answer:** Make health probes representative enough to protect users but simple enough to remain reliable.

### Q28. What is the most important operational lesson from **Application Gateway Routing and WAF**?
**Answer:** Use backend-health diagnostics before changing DNS or application code.

### Q29. What is the most important operational lesson from **Azure Front Door Global Edge Routing**?
**Answer:** Use Front Door for global HTTP/S delivery; do not confuse it with regional Application Gateway.

### Q30. What is the most important operational lesson from **Traffic Manager DNS-Based Routing**?
**Answer:** Use Traffic Manager when DNS-level routing is enough; use Front Door when you need global HTTP reverse proxy behavior.

### Q31. What is the most important operational lesson from **Azure VM Boot Path and Platform Diagnostics**?
**Answer:** Check platform and boot evidence before resetting or redeploying a VM.

### Q32. What is the most important operational lesson from **Availability Zones vs Availability Sets**?
**Answer:** Choose based on the failure you need to survive, not just on a certification definition.

### Q33. What is the most important operational lesson from **VM Scale Sets and Autoscale Safety**?
**Answer:** Set minimum capacity from reliability needs and scale-in only after the application is designed for termination.

### Q34. What is the most important operational lesson from **Azure Compute Gallery and Image Versioning**?
**Answer:** Treat images as signed/versioned build artifacts, not manually maintained servers.

### Q35. What is the most important operational lesson from **Managed Disk Performance and Host Limits**?
**Answer:** Size VM and disks together from measured workload I/O.

### Q36. What is the most important operational lesson from **App Service Plan and Scaling Model**?
**Answer:** Group apps on a plan only when shared capacity and scaling behavior are acceptable.

### Q37. What is the most important operational lesson from **Deployment Slots and Configuration Stickiness**?
**Answer:** Explicitly classify every environment-specific setting before using slot swaps.

### Q38. What is the most important operational lesson from **Azure Functions Concurrency and Downstream Pressure**?
**Answer:** Scale the dependency chain, not only the function runtime.

### Q39. What is the most important operational lesson from **Azure Container Apps Revisions and Event-Driven Scaling**?
**Answer:** Use revision traffic splitting for risky application changes rather than replacing all traffic at once.

### Q40. What is the most important operational lesson from **AKS Shared Responsibility and Control Loops**?
**Answer:** Do not interpret 'managed Kubernetes' as 'managed workload security and reliability'.

### Q41. What is the most important operational lesson from **Azure Container Registry and Image Supply Chain**?
**Answer:** Deploy immutable digests and minimize who can push to production registries.

### Q42. What is the most important operational lesson from **Blob Versioning, Soft Delete, and Immutability**?
**Answer:** Design recovery from accidental deletion and malicious deletion as separate scenarios.

### Q43. What is the most important operational lesson from **Storage Redundancy and Failure Domains**?
**Answer:** Do not select redundancy by acronym strength; select it from failure-domain and RPO requirements.

### Q44. What is the most important operational lesson from **Blob Lifecycle Management**?
**Answer:** Test lifecycle rules on narrow prefixes before applying them to large production datasets.

### Q45. What is the most important operational lesson from **Azure Files and Azure File Sync**?
**Answer:** Use file services only when applications require filesystem semantics; use Blob for object-native workloads.

### Q46. What is the most important operational lesson from **Azure SQL High Availability and Connection Resilience**?
**Answer:** Design every managed-database client for transient disconnects.

### Q47. What is the most important operational lesson from **Cosmos DB Partition Keys**?
**Answer:** Choose the partition key before production data volume makes redesign expensive.

### Q48. What is the most important operational lesson from **Cosmos DB Consistency Models**?
**Answer:** Choose the weakest consistency that still satisfies business correctness.

### Q49. What is the most important operational lesson from **Azure Service Bus Delivery Semantics**?
**Answer:** Treat message delivery as at-least-once unless the end-to-end business operation proves otherwise.

### Q50. What is the most important operational lesson from **Event Grid vs Event Hubs**?
**Answer:** Choose messaging from delivery semantics and volume, not from similar names.

### Q51. What is the most important operational lesson from **API Management as a Policy Gateway**?
**Answer:** Keep business domain logic in services; use APIM mainly for gateway concerns.

### Q52. What is the most important operational lesson from **Key Vault Control Plane vs Data Plane**?
**Answer:** Grant secret/key operations only to workloads and operators that actually need them.

### Q53. What is the most important operational lesson from **Secret and Certificate Rotation**?
**Answer:** Test rotation in staging and design consumers to reload secrets without full outages.

### Q54. What is the most important operational lesson from **Defender for Cloud and Security Operations**?
**Answer:** Measure security posture by resolved risk, not by dashboard score alone.

### Q55. What is the most important operational lesson from **Azure Monitor Telemetry Model**?
**Answer:** Standardize correlation IDs and resource dimensions across telemetry.

### Q56. What is the most important operational lesson from **KQL for Evidence-Driven Troubleshooting**?
**Answer:** Start every KQL investigation with time and scope boundaries.

### Q57. What is the most important operational lesson from **Activity Log, Resource Health, and Service Health**?
**Answer:** Check all three before concluding whether Azure or your configuration caused the problem.

### Q58. What is the most important operational lesson from **Azure Backup Vault Isolation and Restore Testing**?
**Answer:** Track restore success and measured RTO, not only backup job success.

### Q59. What is the most important operational lesson from **Azure Site Recovery and DR Orchestration**?
**Answer:** Run non-disruptive DR tests and measure end-to-end RTO.

### Q60. What is the most important operational lesson from **Cost Management, Budgets, and Unit Economics**?
**Answer:** Track at least one business-relevant unit-cost metric for each major workload.

### Q61. What is the most important operational lesson from **Reservations, Savings Plans, Spot, and Baseline Capacity**?
**Answer:** Commit only measured baseline usage and design Spot workloads to survive eviction.

### Q62. What is the most important operational lesson from **Bicep, ARM What-If, and Safe IaC Changes**?
**Answer:** Never treat `what-if` as a substitute for staging and runtime validation.


## Completion Checklist

- [ ] I understand the current AZ-900 domains.
- [ ] I understand Azure global infrastructure.
- [ ] I understand resources/RGs/subscriptions/management groups.
- [ ] I understand Entra ID.
- [ ] I understand RBAC/Conditional Access/MFA.
- [ ] I understand managed identities.
- [ ] I understand VMs/VMSS/App Service/Functions/containers.
- [ ] I understand VNet/subnet/NSG/routing.
- [ ] I understand VPN/ExpressRoute/Private Link.
- [ ] I understand Azure DNS/LB/App Gateway/Front Door.
- [ ] I understand Azure Storage services.
- [ ] I understand storage redundancy.
- [ ] I understand migration/data-transfer tools.
- [ ] I understand Azure SQL/Cosmos fundamentals.
- [ ] I understand Key Vault/Defender for Cloud.
- [ ] I understand Policy/locks/tags/Purview.
- [ ] I understand portal/Cloud Shell/CLI/PowerShell.
- [ ] I understand ARM/Bicep/Azure Arc.
- [ ] I understand Monitor/Log Analytics/App Insights.
- [ ] I understand Advisor/Service Health.
- [ ] I understand Cost Management/Pricing Calculator.
- [ ] I understand Azure WAF/CAF concepts.
- [ ] I completed all 30 labs.
- [ ] I completed the Azure Enterprise Portal Foundation project.
