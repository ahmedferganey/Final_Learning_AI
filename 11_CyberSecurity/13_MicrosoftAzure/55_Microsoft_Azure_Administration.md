# 55. Microsoft Azure Administration

> Phase 13 — Microsoft Azure

This course moves from **Azure Fundamentals** into actual day-to-day Azure administration.

Course 50 asked:

```text
"What is this Azure service?"
```

Course 55 asks:

```text
"How do I configure it?"
"How do I secure it?"
"How do I monitor it?"
"How do I troubleshoot it?"
"How do I automate it?"
```

The course is aligned to the current:

```text
Microsoft Certified: Azure Administrator Associate
Exam: AZ-104 — Microsoft Azure Administrator
```

Current Microsoft exam baseline:

```text
Skills measured as of April 17, 2026

Manage Azure identities and governance                 20–25%
Implement and manage storage                           15–20%
Deploy and manage Azure compute resources              20–25%
Implement and manage virtual networking                15–20%
Monitor and maintain Azure resources                   10–15%
```

The current Microsoft certification page states:

```text
Exam time: 100 minutes
Passing score: 700 or greater
Certification renewal frequency: 12 months
```

Microsoft describes the Azure Administrator role as implementing, managing, and monitoring Azure environments across:

```text
virtual networking
storage
compute
identity
security
governance
```

and expects familiarity with:

```text
operating systems
networking
servers
virtualization
PowerShell
Azure CLI
Azure portal
ARM templates / Bicep
Microsoft Entra ID
```

This course is intentionally broader than exam memorization. It teaches Azure as an operational platform.

---

# Azure Administrator Mental Model

An Azure administrator operates this hierarchy:

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

The operating loop is:

```text
Identity
   ↓
Governance
   ↓
Network
   ↓
Compute
   ↓
Storage
   ↓
Monitoring
   ↓
Backup / Recovery
   ↓
Automation
   ↓
Troubleshooting
```

Typical production layout:

```text
                         Internet
                            |
                       Azure DNS
                            |
                      Azure Front Door
                            |
                           WAF
                            |
                  Application Gateway
                      /           \
                   Zone 1        Zone 2
                     |             |
                  VMSS/App      VMSS/App
                      \           /
                        Database
                           |
                      Storage
                           |
                       Backup
```

Enterprise administrative hierarchy:

```text
Tenant Root
├─ Platform
│  ├─ Identity
│  ├─ Connectivity
│  └─ Management
└─ Landing Zones
   ├─ Production
   ├─ NonProduction
   └─ Sandbox
```

---

## 1. Topic Title

**Microsoft Azure Administration**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Manage Microsoft Entra users and groups.
- Manage licenses in Microsoft Entra ID.
- Manage external users.
- Configure self-service password reset.
- Manage built-in Azure roles and role assignments.
- Interpret effective access.
- Manage subscriptions and management groups.
- Implement Azure Policy.
- Configure resource locks and tags.
- Manage resource groups.
- Configure budgets, alerts, and Azure Advisor recommendations.
- Create and configure Azure Storage accounts.
- Configure storage network access and firewalls.
- Create and use SAS tokens.
- Configure stored access policies.
- Manage storage account access keys.
- Configure identity-based access for Azure Files.
- Configure Blob Storage and Azure Files.
- Configure storage redundancy, lifecycle, object replication, versioning, snapshots, soft delete, and encryption.
- Use Storage Explorer and AzCopy.
- Interpret and modify ARM templates and Bicep.
- Deploy resources using ARM/Bicep.
- Create and configure Azure virtual machines.
- Configure encryption at host.
- Move VMs between scopes where supported.
- Manage VM sizes and disks.
- Deploy VMs to availability zones and availability sets.
- Deploy and manage Virtual Machine Scale Sets.
- Create and manage Azure Container Registry.
- Provision Azure Container Instances.
- Provision Azure Container Apps.
- Configure container sizing and scaling.
- Create and configure Azure App Service.
- Configure App Service plans, scaling, TLS, DNS, backups, networking, and deployment slots.
- Create VNets and subnets.
- Configure VNet peering.
- Configure public IP addresses and user-defined routes.
- Troubleshoot network connectivity.
- Create NSGs and ASGs.
- Evaluate effective NSG security rules.
- Implement Azure Bastion.
- Configure service endpoints.
- Configure private endpoints.
- Configure Azure DNS.
- Configure internal and public Azure Load Balancer.
- Troubleshoot load balancing.
- Interpret Azure Monitor metrics.
- Configure diagnostic/log settings.
- Query logs with KQL.
- Configure alerts, action groups, and alert processing rules.
- Configure Azure Monitor Insights.
- Use Network Watcher and Connection Monitor.
- Create Recovery Services and Backup vaults.
- Configure backup policies.
- Perform backup and restore operations.
- Configure Azure Site Recovery.
- Perform regional failover with Site Recovery.
- Interpret backup reports and alerts.
- Use Azure CLI and Azure PowerShell safely.
- Operate Azure using repeatable automation.
- Troubleshoot identity, network, compute, storage, and monitoring issues systematically.

---

## 3. Prerequisites

Required:

- 48. Cloud Computing Fundamentals
- 50. Microsoft Azure Fundamentals
- Windows and Linux administration basics
- Networking fundamentals
- Storage fundamentals
- Virtualization
- PowerShell basics
- Bash/CLI basics
- Git

Recommended lab tools:

```text
Azure subscription
Azure portal
Azure Cloud Shell
Azure CLI
Azure PowerShell
VS Code
Bicep extension
AzCopy
Azure Storage Explorer
```

Before any administrative action:

```bash
az account show
```

PowerShell:

```powershell
Get-AzContext
```

Always verify:

```text
Tenant
Subscription
Identity
Resource scope
Region
```

before modifying resources.

---

## 4. Core Concepts Explanation

# Part 1 — Azure Administrator Role

Azure administration is not only VM administration.

The administrator operates:

```text
identity
governance
storage
compute
network
monitoring
backup
automation
```

Most production incidents cross more than one of these layers.

# Part 2 — Control Plane vs Data Plane

Control plane manages Azure resources:

```text
create VM
modify VNet
assign role
configure policy
```

Data plane manages service data:

```text
read blob
write file
query database
```

Permissions for control plane and data plane can differ.

# Part 3 — Azure Resource Manager

ARM is Azure's control-plane layer.

Requests from:

```text
portal
Azure CLI
PowerShell
SDK
ARM template
Bicep
```

are processed through Azure Resource Manager.

# Part 4 — Azure Resource ID

A resource has a hierarchical resource ID:

```text
/subscriptions/<sub>
/resourceGroups/<rg>
/providers/<provider>/<type>/<name>
```

Resource IDs matter in automation, RBAC, Policy, diagnostics, and troubleshooting.

# Part 5 — Azure Scope Hierarchy

```text
Management Group
  ↓
Subscription
  ↓
Resource Group
  ↓
Resource
```

RBAC and Policy can inherit downward.

# Part 6 — Microsoft Entra Tenant

A tenant is a Microsoft Entra directory.

It contains:

```text
users
groups
applications
service principals
managed identities
authentication settings
```

Azure subscriptions trust a tenant for identity.

# Part 7 — User Object

A user has properties such as:

```text
display name
user principal name
object ID
account status
usage location
licenses
```

Use object IDs in automation when names may change.

# Part 8 — Create User

Portal workflow:

```text
Microsoft Entra ID
→ Users
→ New user
```

CLI concept:

```bash
az ad user create   --display-name "Lab User"   --user-principal-name labuser@tenant.example   --password 'TemporaryPassword'
```

Use secure password workflows in real environments.

# Part 9 — User Properties

Administrators manage:

```text
job information
department
usage location
authentication
group membership
licenses
```

Some identity attributes may be synchronized from on-premises and should not be edited directly in cloud.

# Part 10 — Groups

Common group types include:

```text
Security groups
Microsoft 365 groups
```

Azure administration commonly uses security groups for RBAC and access assignment.

# Part 11 — Assigned Membership

Assigned group:

```text
administrator explicitly adds/removes members
```

Simple and predictable.

# Part 12 — Dynamic Membership

Dynamic groups evaluate rules.

Example concept:

```text
department = Finance
→ automatically become Finance group member
```

Licensing and feature availability must be checked in current Entra plans.

# Part 13 — Group-Based Access

Better:

```text
User
 ↓
Group
 ↓
RBAC Role
```

than assigning many permissions directly to users.

This simplifies lifecycle management.

# Part 14 — External Users

B2B/external identities allow partner access.

Pattern:

```text
Partner Identity
 ↓ invitation/federation
Entra External User
 ↓
Azure/App Access
```

Review external access regularly.

# Part 15 — Guest Lifecycle

Guest governance should cover:

```text
sponsor
business reason
expiration/review
group membership
role assignments
offboarding
```

# Part 16 — Licenses

Microsoft Entra/Microsoft services can require license assignment.

Automation should consider:

```text
usage location
license availability
group-based licensing if used
```

# Part 17 — Self-Service Password Reset

SSPR allows eligible users to reset passwords.

Configure:

```text
scope
authentication methods
registration
notifications
```

according to identity policy.

# Part 18 — Authentication Methods

Depending on tenant policy, users may use supported:

```text
Authenticator
FIDO2/security key
SMS/voice in selected scenarios
Temporary Access Pass
Windows Hello
```

Prefer phishing-resistant methods for privileged users where possible.

# Part 19 — MFA

MFA reduces risk from stolen passwords.

Privileged identities should have strong MFA and emergency-access planning.

# Part 20 — Conditional Access Concept

Although deeper Conditional Access design is outside core AZ-104 scope, administrators must understand that access can be conditioned on:

```text
user
device
risk
location
application
authentication strength
```

# Part 21 — Azure RBAC

RBAC answers:

```text
Who
can do what
at what scope?
```

Components:

```text
security principal
role definition
scope
role assignment
```

# Part 22 — Security Principal

Can be:

```text
user
group
service principal
managed identity
```

# Part 23 — Role Definition

A role is a set of permissions.

Examples:

```text
Reader
Contributor
Owner
Virtual Machine Contributor
Storage Blob Data Reader
```

# Part 24 — Role Assignment

```text
Principal
+
Role
+
Scope
=
Role Assignment
```

Example:

```text
Ops-Team
+
Virtual Machine Contributor
+
RG-Compute
```

# Part 25 — Reader

Reader can view Azure resource configuration but cannot modify resources.

Data-plane access to service contents may require separate data roles.

# Part 26 — Contributor

Contributor can manage resources but generally cannot assign Azure RBAC permissions.

Avoid using it where narrower roles suffice.

# Part 27 — Owner

Owner includes resource management and access delegation.

Use sparingly.

# Part 28 — User Access Administrator

Focused on managing user access to Azure resources.

Useful when separating access administration from resource administration.

# Part 29 — Scope Inheritance

Role assignment at subscription:

```text
Subscription
 ↓
all child RGs/resources
```

unless constrained by other controls.

Assign at lowest practical scope.

# Part 30 — Effective Access

Effective permission is the result of:

```text
direct assignments
group assignments
inherited assignments
deny assignments
conditions
```

Troubleshoot full path.

# Part 31 — Management Groups

Management groups organize subscriptions.

Example:

```text
Tenant Root
├─ Platform
├─ Production
└─ NonProduction
```

Policy/RBAC can be inherited.

# Part 32 — Subscriptions

Subscription is boundary for:

```text
billing
quotas
RBAC scope
Policy scope
resource organization
```

Use separate subscriptions for strong environment/business boundaries where justified.

# Part 33 — Resource Groups

Resource group should group resources with related:

```text
lifecycle
ownership
deployment
permissions
```

Deleting the RG deletes contained resources.

# Part 34 — Move Resources

Some resources can move:

```text
between resource groups
between subscriptions
sometimes Regions using service-specific migration
```

Always validate dependencies/support before move.

# Part 35 — Tags

Metadata examples:

```text
Owner=Platform
Environment=Prod
CostCenter=1204
Criticality=Tier1
```

Use for cost, automation, and governance.

# Part 36 — Tag Governance

Tags do not automatically solve governance.

Use:

```text
Azure Policy
deployment standards
automation
```

to enforce tag requirements.

# Part 37 — Resource Locks

Types:

```text
CanNotDelete
ReadOnly
```

Use to protect critical resources from accidental changes.

# Part 38 — Lock Inheritance

Locks applied at parent scope can affect child resources.

A lock is not RBAC; even highly privileged users may need to remove the lock before the protected action.

# Part 39 — Azure Policy

Policy evaluates/enforces resource configuration.

Example:

```text
Allowed Regions
Required Tags
Audit Encryption
Deny Public IP
```

# Part 40 — Policy Definition

Contains:

```text
condition
effect
parameters
```

Concept:

```text
IF resource location not allowed
THEN deny
```

# Part 41 — Policy Assignment

Apply at:

```text
management group
subscription
resource group
resource
```

Use exclusions only with documented business reason.

# Part 42 — Policy Effects

Common conceptual effects:

```text
Audit
Deny
Modify
DeployIfNotExists
Append
Disabled
```

Exact supported effects depend on resource/policy.

# Part 43 — Initiative

An initiative groups multiple policies.

Example:

```text
Platform Baseline
├─ require tags
├─ audit encryption
├─ deny unapproved locations
└─ deploy diagnostics
```

# Part 44 — Policy Compliance

Administrators monitor:

```text
compliant
non-compliant
exempt
not started
```

Then remediate or document exception.

# Part 45 — Policy Remediation

Modify/DeployIfNotExists policies can require remediation tasks for existing resources.

New deployments and existing estate may behave differently.

# Part 46 — Cost Management

Administrator should manage:

```text
budgets
alerts
cost analysis
resource ownership
idle resources
Advisor recommendations
```

# Part 47 — Budget

Budget:

```text
planned spending threshold
```

It does not automatically stop resources unless you build automation around alerts.

# Part 48 — Cost Alert

Example:

```text
50% actual
80% actual
100% forecast
```

Notify accountable owners early.

# Part 49 — Azure Advisor

Advisor provides recommendations across areas such as:

```text
cost
reliability
security
performance
operational excellence
```

Validate recommendation against workload constraints.

# Part 50 — Subscription Quotas

Examples:

```text
vCPU family limits
public IPs
network resources
storage limits
```

Quota exhaustion can look like deployment failure.

# Part 51 — Storage Account

Azure Storage account provides namespace/configuration for:

```text
Blob
Files
Queues
Tables
```

depending on account type.

# Part 52 — StorageV2

General-purpose v2 is the standard account type for many Blob/File/Queue/Table use cases.

Always verify feature compatibility before production choice.

# Part 53 — Storage Account Region

Storage account has:

```text
Region
performance tier
redundancy
network access
encryption
```

These choices affect durability, latency, and cost.

# Part 54 — Storage Redundancy

Common:

```text
LRS
ZRS
GRS
RA-GRS
GZRS
RA-GZRS
```

Select based on failure/DR needs.

# Part 55 — LRS

Locally redundant copies within primary region location.

Lowest geographic resilience.

# Part 56 — ZRS

Replicates across availability zones in primary Region.

Use for zone-failure resilience.

# Part 57 — GRS

Replicates primary data to paired/secondary Region according to service design.

Secondary replication is asynchronous.

# Part 58 — RA-GRS

Adds read access to secondary endpoint.

# Part 59 — GZRS

Combines:

```text
zone redundancy in primary
+
geo replication
```

# Part 60 — RA-GZRS

Adds read access to secondary region for GZRS.

# Part 61 — Storage Firewall

Restrict access by:

```text
public network settings
selected networks
IP rules
private endpoints
```

Avoid broad public access for sensitive storage.

# Part 62 — Storage Network Rules

If application access suddenly fails check:

```text
public network access
VNet/subnet
service endpoint
private endpoint
firewall IP
DNS
```

# Part 63 — Storage Access Keys

Storage account keys provide broad access.

Treat as highly privileged secrets.

Prefer:

```text
Entra ID
managed identity
SAS
```

where appropriate.

# Part 64 — Shared Access Signature

SAS delegates limited access:

```text
resource
permissions
start/expiry
IP
protocol
```

Use short expiry and least privilege.

# Part 65 — Service SAS

Delegates access to one Storage service/resource scope using account credentials.

# Part 66 — Account SAS

Can span multiple storage services/resource types.

Broader capability means greater risk.

# Part 67 — User Delegation SAS

Blob SAS signed using Entra user delegation key rather than account key.

Often preferable when using identity-based authorization.

# Part 68 — Stored Access Policy

Central policy can control selected service SAS behavior for supported resources.

Useful for changing/revoking SAS policy centrally.

# Part 69 — Identity-Based Storage Access

Use Azure RBAC data roles.

Examples:

```text
Storage Blob Data Reader
Storage Blob Data Contributor
```

Control plane Contributor alone does not necessarily grant blob data access.

# Part 70 — Azure Files Identity Access

Azure Files can integrate with identity-based SMB access using supported directory/identity configurations.

Share-level and NTFS permissions may both matter.

# Part 71 — Blob Container

Blob storage hierarchy:

```text
Storage Account
 ↓
Container
 ↓
Blob
```

# Part 72 — Blob Types

Common concepts:

```text
block blob
append blob
page blob
```

Block blobs are common for files/objects.

# Part 73 — Blob Tiers

Common:

```text
Hot
Cool
Cold
Archive
```

Choose from access frequency and retrieval requirements.

# Part 74 — Lifecycle Management

Example:

```text
30d → Cool
90d → Cold
365d → Archive
7y → delete
```

Policy runs automatically.

# Part 75 — Blob Versioning

Keeps previous versions after overwrite.

Useful for recovery but increases storage usage.

# Part 76 — Blob Soft Delete

Protects deleted blobs for a retention window.

Useful against accidental deletion.

# Part 77 — Container Soft Delete

Protects deleted containers for supported retention period.

# Part 78 — Object Replication

Asynchronously copies block blobs between storage accounts.

Use for:

```text
geo distribution
data copies
DR-related scenarios
```

according to feature constraints.

# Part 79 — Storage Encryption

Azure Storage encrypts data at rest.

Customer-managed keys can be used where supported for greater key control.

# Part 80 — Infrastructure Encryption Concept

Some scenarios require an additional infrastructure encryption layer.

Use only when security/compliance requirements justify it.

# Part 81 — Azure Files

Managed file shares.

Protocols can include:

```text
SMB
NFS
```

depending on account/share configuration.

# Part 82 — File Share Quota

Set share capacity/quota appropriate to workload.

Monitor usage before exhaustion.

# Part 83 — Azure Files Snapshot

Point-in-time share snapshot.

Useful for:

```text
file recovery
rollback
```

# Part 84 — File Soft Delete

Protects deleted file shares within configured retention window.

# Part 85 — Azure File Sync

Hybrid pattern:

```text
Windows Server
 ↕
Azure File Sync
 ↕
Azure Files
```

Can provide local caching/cloud tiering.

# Part 86 — Azure Storage Explorer

GUI administration for:

```text
Blob
Files
Queues
Tables
```

Useful for troubleshooting and controlled data operations.

# Part 87 — AzCopy

Command-line transfer utility.

Example:

```bash
azcopy copy "./data/*"   "https://ACCOUNT.blob.core.windows.net/container?<SAS>"   --recursive
```

Protect SAS values from shell history/logging.

# Part 88 — Storage Troubleshooting

For 403/access failure inspect:

```text
identity/RBAC
SAS expiry
access key
firewall
private endpoint
DNS
storage scope
```

# Part 89 — ARM Template

Declarative JSON IaC.

Defines desired resource state.

```text
template
 ↓
ARM
 ↓
resource deployment
```

# Part 90 — Bicep

Azure-native declarative IaC language.

Example:

```bicep
resource stg 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageName
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
```

Check current API versions for production.

# Part 91 — Parameters

Parameters make templates reusable.

```bicep
param environment string
param location string
```

# Part 92 — Variables

Variables derive reusable values.

```bicep
var prefix = '${environment}-web'
```

# Part 93 — Outputs

Expose deployed values.

```bicep
output storageId string = stg.id
```

# Part 94 — Modules

Bicep modules split infrastructure into reusable files.

```text
main.bicep
├─ network.bicep
├─ compute.bicep
└─ monitoring.bicep
```

# Part 95 — Bicep Deployment

Resource-group scope:

```bash
az deployment group create   --resource-group RG   --template-file main.bicep
```

# Part 96 — What-If

Preview changes:

```bash
az deployment group what-if   --resource-group RG   --template-file main.bicep
```

Use before production deployments.

# Part 97 — Template Export

Azure can export an existing resource/resource-group representation to ARM template.

Treat exports as starting points, not automatically clean production IaC.

# Part 98 — ARM to Bicep Conversion

Bicep tooling can decompile ARM JSON.

Review the result for:

```text
hardcoded names
dependencies
API versions
secrets
```

# Part 99 — Azure Virtual Machine

VM configuration:

```text
size
image
OS disk
data disks
NIC
VNet
identity
availability
extensions
```

# Part 100 — VM Size

Select based on:

```text
vCPU
RAM
storage bandwidth
network bandwidth
GPU
cost
```

Resize when workload requirements change.

# Part 101 — VM Image

Sources:

```text
Marketplace
custom managed image
Azure Compute Gallery
```

Use standardized images for repeatability.

# Part 102 — Azure Compute Gallery

Manages:

```text
image definitions
versions
replication
sharing
```

across Regions/subscriptions where supported.

# Part 103 — OS Disk

Boot volume.

Use managed disks and appropriate performance tier.

# Part 104 — Data Disk

Attach separate managed disks for:

```text
application data
database files
logs
```

according to workload.

# Part 105 — Disk Caching

Options can include:

```text
None
ReadOnly
ReadWrite
```

depending on disk/workload.

Database disk caching choices should follow vendor/application guidance.

# Part 106 — Managed Disk Types

Common categories:

```text
Standard HDD
Standard SSD
Premium SSD
Premium SSD v2
Ultra Disk
```

availability/features vary.

# Part 107 — Disk Encryption

Azure disks support platform-managed encryption and customer-managed key scenarios.

Encryption at host adds protection for supported VM temporary/cache data paths.

# Part 108 — Encryption at Host

Encrypts supported data on VM host before reaching storage service.

Must be supported/enabled for the VM configuration.

# Part 109 — Availability Set

Provides fault/update domain distribution for non-zonal VM architecture.

Use where Availability Zones are unavailable or requirements fit set-based design.

# Part 110 — Availability Zone

Pin VMs to different zones:

```text
VM1 Zone 1
VM2 Zone 2
VM3 Zone 3
```

behind a load balancer for zone resilience.

# Part 111 — VM Scale Sets

VMSS manages a fleet.

```text
model
 ↓
instances
 ↓
load balancer
```

Supports scaling and resilient placement.

# Part 112 — Uniform vs Flexible Orchestration Concept

VMSS supports orchestration modes with different instance-management models.

Know the architecture trade-off and check current feature support before deployment.

# Part 113 — VMSS Autoscale

Metrics/rules:

```text
CPU > 75% → scale out
CPU < 30% → scale in
```

Use cooldown and safe minimum capacity.

# Part 114 — VM Extensions

Extensions perform post-deployment operations.

Examples:

```text
Custom Script
monitoring agents
configuration
security tools
```

Avoid excessive boot-time complexity.

# Part 115 — Custom Script Extension

Can run a script on VM.

Use idempotent scripts and avoid secrets in command arguments.

# Part 116 — Managed Identity for VM

VM can access Azure services:

```text
VM
 ↓ managed identity
Entra token
 ↓
Key Vault/Storage
```

without stored credentials.

# Part 117 — Move VM

Resource move may involve dependencies:

```text
NIC
disk
public IP
availability resources
```

Validate Azure Resource Mover/service-specific support for Region moves.

# Part 118 — VM Troubleshooting

Check:

```text
power state
boot diagnostics
activity log
serial console
network
NSG
disk
extension
guest OS
```

# Part 119 — Azure Container Registry

Private registry for container images/artifacts.

```text
build
 ↓
ACR
 ↓
ACI / Container Apps / AKS / App Service
```

# Part 120 — ACR Authentication

Prefer:

```text
managed identity
service principal/workload identity
RBAC
```

instead of long-lived admin credentials.

# Part 121 — ACR Repositories

Use:

```text
versioned tags
immutable release process
image cleanup
scan/security pipeline
```

# Part 122 — Azure Container Instances

Run containers without managing VMs/orchestrator.

Use for:

```text
simple task
temporary workload
batch
isolated container
```

# Part 123 — ACI Resource Configuration

Specify:

```text
image
CPU
memory
ports
environment
network
restart policy
```

# Part 124 — Azure Container Apps

Managed application platform for containerized microservices/serverless-style apps.

Capabilities include:

```text
ingress
revisions
autoscaling
secrets
managed identity
```

# Part 125 — Container Apps Revision

A revision is an immutable snapshot of app configuration/image.

Use for:

```text
canary
blue/green
rollback
```

depending on traffic settings.

# Part 126 — Container Apps Scaling

Scale based on:

```text
HTTP traffic
events
custom KEDA-supported signals
```

depending on configuration.

# Part 127 — Container Troubleshooting

Check:

```text
image pull
registry auth
port
CPU/memory
environment
secret
logs
health
network
```

# Part 128 — Azure App Service

PaaS web application hosting.

Supports:

```text
web apps
APIs
multiple runtimes
containers
TLS
scaling
deployment slots
```

# Part 129 — App Service Plan

Defines compute capacity and pricing tier for App Service.

Multiple apps can share a plan.

# Part 130 — Scale Up vs Scale Out

Scale up:

```text
larger plan SKU
```

Scale out:

```text
more instances
```

# Part 131 — Autoscale App Service

Use metric/schedule rules where supported.

Application should be stateless or use shared external state.

# Part 132 — Custom Domain

Map:

```text
www.example.com
→ App Service
```

using required DNS records.

# Part 133 — TLS Certificate

App Service supports managed/imported certificates depending on configuration.

Use HTTPS-only where required.

# Part 134 — App Service Networking

Concepts include:

```text
inbound access
private endpoint
VNet integration
service endpoints/private access to dependencies
```

Do not confuse inbound private access with outbound VNet integration.

# Part 135 — VNet Integration

Allows app outbound connectivity into a VNet.

Use to access:

```text
private database
private service
internal API
```

# Part 136 — App Service Private Endpoint

Provides private inbound IP access to App Service.

Requires private DNS planning.

# Part 137 — Deployment Slots

Use:

```text
staging
production
```

Deploy/test staging then swap.

# Part 138 — Slot Settings

Mark environment-specific configuration as slot settings so it does not move during swap.

# Part 139 — App Service Backup

Configure backup for supported app content/config and data integration scenarios.

Database backup often requires database-native backup strategy too.

# Part 140 — App Service Troubleshooting

Check:

```text
deployment logs
application logs
health
configuration
runtime
DNS
TLS
network
dependencies
```

# Part 141 — Virtual Network

VNet is regional Azure network.

```text
VNet
├─ Web subnet
├─ App subnet
└─ DB subnet
```

# Part 142 — VNet Address Space

Plan non-overlapping CIDRs.

Example:

```text
10.20.0.0/16
```

Avoid overlap with on-prem and peer VNets.

# Part 143 — Subnet

Subdivide address space.

Example:

```text
10.20.1.0/24 web
10.20.2.0/24 app
10.20.3.0/24 db
```

# Part 144 — Subnet Delegation

Some PaaS services require subnet delegation.

Delegation grants the service permission to manage specific network behavior in the subnet.

# Part 145 — Public IP

Azure public IP can be associated with supported resources.

Use only where needed; private administration is preferable for internal systems.

# Part 146 — Private IP

Allocated inside VNet.

Can be dynamic/static depending on resource configuration.

# Part 147 — VNet Peering

Private connectivity:

```text
VNet A ↔ VNet B
```

Peering is not automatically transitive.

# Part 148 — Peering Options

Common settings include:

```text
allow VNet access
forwarded traffic
gateway transit
use remote gateway
```

Misconfiguration can break hub-spoke routing.

# Part 149 — User-Defined Route

Custom route example:

```text
0.0.0.0/0
→ Azure Firewall/NVA
```

Use for forced routing/security inspection.

# Part 150 — Effective Routes

Troubleshoot actual route set applied to NIC/subnet.

Sources include:

```text
system routes
UDR
BGP
```

# Part 151 — Network Security Group

Stateful security rules.

Fields:

```text
priority
source
destination
port
protocol
allow/deny
```

# Part 152 — NSG Priority

Lower numeric priority is processed first.

Example:

```text
100 allow app
200 deny broader traffic
```

# Part 153 — NSG Scope

Can be associated with:

```text
subnet
NIC
```

Effective rules combine applicable rules.

# Part 154 — Application Security Group

Logical grouping of NICs.

Example:

```text
ASG-Web
ASG-App
ASG-DB
```

Use in NSG rules instead of IP lists.

# Part 155 — Effective Security Rules

Azure calculates effective NSG rules at NIC.

Use portal/Network Watcher to identify why traffic is allowed/denied.

# Part 156 — Azure Bastion

Managed browser-based SSH/RDP access.

Pattern:

```text
Admin
 ↓ TLS
Azure Bastion
 ↓ private IP
VM
```

No VM public IP required.

# Part 157 — Service Endpoint

Extends VNet identity to supported PaaS service.

The service still has public endpoint semantics but can restrict access to selected VNets/subnets.

# Part 158 — Private Endpoint

Creates private IP NIC for a supported PaaS service.

```text
VM
 ↓ private IP
Private Endpoint
 ↓
Storage/SQL/Key Vault
```

# Part 159 — Private Link

Underlying private-connectivity platform for private endpoints/services.

Useful to eliminate public-path dependency.

# Part 160 — Private DNS

Private endpoints require DNS resolution to the private IP.

Common failure:

```text
endpoint correct
but DNS returns public endpoint
```

# Part 161 — Azure DNS

Managed authoritative DNS.

Supports:

```text
public DNS zones
private DNS zones
```

# Part 162 — DNS Record Sets

Common:

```text
A
AAAA
CNAME
MX
TXT
NS
SRV
```

depending on zone.

# Part 163 — Private DNS Zone Link

Link private zone to VNet so resources can resolve private names.

Auto-registration is available in selected private-DNS scenarios.

# Part 164 — Azure Load Balancer

Layer 4:

```text
TCP
UDP
```

Can be:

```text
public
internal
```

# Part 165 — Frontend IP

The address clients connect to.

Can be:

```text
public IP
private IP
```

# Part 166 — Backend Pool

Contains target NICs/VMs/VMSS instances.

Load-balancing rules send traffic to healthy members.

# Part 167 — Health Probe

Checks target health.

Example:

```text
TCP/80
HTTP /health
```

A bad probe makes healthy servers unavailable.

# Part 168 — Load-Balancing Rule

Defines:

```text
frontend
frontend port
backend pool
backend port
probe
protocol
```

# Part 169 — Inbound NAT Rule

Maps a frontend port to a specific backend VM port.

Useful for specific administrative scenarios, but Bastion is often preferred for management.

# Part 170 — Load Balancer Troubleshooting

Check:

```text
frontend
backend pool
probe
NSG
guest firewall
service listening
route
```

# Part 171 — Network Watcher

Network troubleshooting platform.

Tools include concepts such as:

```text
Connection Monitor
IP flow verify
next hop
packet capture
NSG diagnostics
```

depending on feature.

# Part 172 — IP Flow Verify

Tests whether NSG rules allow/deny a packet tuple.

Useful for:

```text
source/destination/port/protocol
```

# Part 173 — Next Hop

Shows route decision for traffic from VM NIC.

Useful for UDR/VPN/NVA troubleshooting.

# Part 174 — Connection Troubleshoot / Monitor

Tests connectivity and continuously monitors supported endpoint paths.

Helps isolate:

```text
DNS
route
NSG
endpoint
latency
```

# Part 175 — Packet Capture

Network Watcher can initiate packet capture on supported Azure VMs.

Use only in authorized troubleshooting and protect captured sensitive traffic.

# Part 176 — Azure Monitor

Central observability platform.

Works with:

```text
metrics
logs
alerts
insights
workbooks
diagnostic settings
```

# Part 177 — Metrics

Time-series telemetry.

Examples:

```text
VM CPU
disk operations
storage transactions
load-balancer health
```

# Part 178 — Platform Metrics

Azure services emit native metrics automatically to different degrees.

Metric retention/granularity depends on service and platform behavior.

# Part 179 — Diagnostic Settings

Route supported platform logs/metrics to destinations such as:

```text
Log Analytics
Storage Account
Event Hub
partner destinations
```

depending on resource.

# Part 180 — Log Analytics Workspace

Central workspace for Azure Monitor Logs.

Use for:

```text
query
correlation
alerts
workbooks
```

# Part 181 — Kusto Query Language

KQL example:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue
| order by TimeGenerated desc
```

# Part 182 — KQL Filter

```kusto
Heartbeat
| where TimeGenerated > ago(15m)
| summarize LastSeen=max(TimeGenerated) by Computer
```

Find systems not reporting.

# Part 183 — Activity Log

Subscription control-plane events.

Use to answer:

```text
who changed the resource?
what operation?
when?
status?
```

# Part 184 — Resource Logs

Service-specific data/operation logs enabled through diagnostic settings where supported.

# Part 185 — Azure Monitor Agent

Modern agent for collecting guest OS monitoring data using Data Collection Rules.

Use instead of legacy agents for supported modern deployments.

# Part 186 — Data Collection Rule

Defines:

```text
what data
from which sources
to which destination
with which transformation
```

for Azure Monitor Agent scenarios.

# Part 187 — VM Insights

Provides VM performance/dependency monitoring views.

Use for:

```text
CPU
memory
disk
network
process/dependency
```

depending on enabled features.

# Part 188 — Storage Insights

Monitor storage:

```text
transactions
latency
availability
capacity
errors
```

# Part 189 — Network Insights

Azure Monitor network views can summarize health/metrics for selected networking resources.

# Part 190 — Azure Monitor Alert

Alert rules combine:

```text
signal
condition
scope
evaluation
action
```

# Part 191 — Metric Alert

Example:

```text
VM CPU > 85%
for 10 minutes
```

# Part 192 — Log Search Alert

Run KQL periodically and alert based on result.

Good for events not represented as native metrics.

# Part 193 — Action Group

Notification/action endpoints:

```text
email
SMS
push
webhook
Logic App
Function
automation
ITSM
```

depending on support.

# Part 194 — Alert Processing Rule

Modify/suppress actions under conditions.

Example:

```text
maintenance window
→ suppress notification
```

without deleting alert rules.

# Part 195 — Alert Noise

Avoid:

```text
one alarm per transient spike
```

Design:

```text
threshold
duration
severity
owner
runbook
```

# Part 196 — Recovery Services Vault

Used for supported backup and Site Recovery workloads.

Stores:

```text
backup configuration/recovery points
ASR configuration
```

depending on service.

# Part 197 — Backup Vault

Azure Backup also uses Backup vault for supported newer workload types/scenarios.

Know both vault concepts in current AZ-104 scope.

# Part 198 — Backup Policy

Defines:

```text
schedule
retention
frequency
```

according to workload.

# Part 199 — VM Backup

Typical:

```text
VM
 ↓ snapshot/backup process
Recovery Services Vault
```

Restore should be tested.

# Part 200 — Restore Options

Depending on workload:

```text
restore VM
restore disks
file-level recovery
alternate location
```

may be supported.

# Part 201 — Soft Delete for Backup

Backup service can retain deleted backup data for protection against accidental/malicious deletion according to current feature configuration.

# Part 202 — Backup Reports

Monitor:

```text
job success
failures
protected instances
storage
policy compliance
```

# Part 203 — Backup Alerts

Alert on:

```text
failed backup
restore failure
protection stopped
replication issue
```

according to monitoring integration.

# Part 204 — Azure Site Recovery

ASR replicates supported workloads for disaster recovery.

Pattern:

```text
Primary
 ↓ replication
Secondary Region
 ↓
Failover
```

# Part 205 — Recovery Plan

Coordinates failover sequence for groups of protected workloads.

Useful for multi-tier applications.

# Part 206 — Test Failover

Test DR without impacting production where supported.

A DR plan not tested is only theoretical.

# Part 207 — Planned Failover

Used when primary site remains available and controlled migration/failover is desired.

# Part 208 — Unplanned Failover

Used during primary-site disaster.

Data loss depends on replication state/RPO.

# Part 209 — Failback

After primary recovery:

```text
resynchronize
validate
reverse replication
planned failback
```

# Part 210 — Azure CLI Context

Verify:

```bash
az account show   --query '{Name:name,Subscription:id,Tenant:tenantId,User:user.name}'   -o table
```

# Part 211 — Azure PowerShell Context

```powershell
Get-AzContext
Get-AzSubscription
```

Set:

```powershell
Set-AzContext -Subscription "<id>"
```

# Part 212 — List Resources

CLI:

```bash
az resource list -o table
```

PowerShell:

```powershell
Get-AzResource
```

# Part 213 — List Role Assignments

```bash
az role assignment list   --scope /subscriptions/SUBSCRIPTION_ID   -o table
```

Use narrower scope where possible.

# Part 214 — List VNets

```bash
az network vnet list -o table
```

# Part 215 — List NSGs

```bash
az network nsg list -o table
```

# Part 216 — List VMs

```bash
az vm list --show-details -o table
```

# Part 217 — List Storage Accounts

```bash
az storage account list -o table
```

# Part 218 — List Alerts

```bash
az monitor metrics alert list   --resource-group RG   -o table
```

# Part 219 — Azure Admin Troubleshooting Model

Always trace:

```text
Identity
 ↓
Scope / RBAC / Policy
 ↓
DNS
 ↓
Routing
 ↓
NSG / Firewall
 ↓
Compute
 ↓
Application
 ↓
Storage / Dependency
 ↓
Monitoring Evidence
```

# Part 220 — Azure Administrator Final Mental Model

Professional Azure administration means:

```text
least privilege
repeatable deployment
controlled change
private-by-design networking
central monitoring
tested recovery
cost visibility
automation
documented troubleshooting
```

The goal is not simply to keep resources running. It is to operate Azure predictably and safely.

---

# Supplemental Deep-Study Layer — Microsoft Azure Administration

> **Source distinction:** The complete uploaded Course 55 remains preserved below. This supplemental layer adds production administration, architecture reasoning, CLI/PowerShell/KQL evidence, troubleshooting, security, recovery, and operational engineering. Certification logistics, pricing, service availability, quotas, and product behavior can change; the certification baseline in the original section remains source-derived and should be checked against live Microsoft documentation before exam or production decisions.

Study sequence:

```text
Concept
  ↓
Detailed explanation
  ↓
Diagram / mental model
  ↓
CLI / PowerShell / KQL
  ↓
Expected evidence
  ↓
Production use
  ↓
Failure / troubleshooting
  ↓
Best practice
```


## Advanced Deep Dive 1 — Context Safety and Subscription Selection

### Concept

Azure CLI and PowerShell inherit tenant/subscription context. A correct command executed in the wrong subscription is still a dangerous command.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az account show --query '{subscription:name,id:id,tenant:tenantId,user:user.name}' -o table
az account list -o table
```

```powershell
Get-AzContext
Get-AzSubscription
```

### Expected Evidence

The active tenant, subscription, and identity match the intended environment.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Fail closed when the expected tenant/subscription does not match.

---

## Advanced Deep Dive 2 — Management Group Governance

### Concept

Management groups define inheritance paths for Azure Policy and RBAC. The hierarchy should reflect durable governance boundaries, not temporary application teams.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az account management-group list -o table
```

### Expected Evidence

Subscriptions are attached to the intended governance branch.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Keep the management-group hierarchy shallow, stable, and policy-oriented.

---

## Advanced Deep Dive 3 — RBAC Effective Access

### Concept

Azure RBAC access can be direct, group-based, inherited from parent scopes, or influenced by deny assignments and conditions. Troubleshoot from the target resource upward.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az role assignment list --assignee <OBJECT_ID> --all -o table
```

### Expected Evidence

All relevant assignments and scopes are visible.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use groups and the lowest practical scope; do not grant Owner to troubleshoot.

---

## Advanced Deep Dive 4 — Control Plane vs Data Plane Authorization

### Concept

Resource-management permission does not automatically grant access to service data. Storage, Key Vault, and other services can require separate data-plane roles.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az role assignment list --scope <RESOURCE_ID> -o table
```

### Expected Evidence

Control-plane roles and data roles are distinguishable.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Troubleshoot management authorization and data authorization separately.

---

## Advanced Deep Dive 5 — Privileged Access / Just-in-Time Administration

### Concept

Standing high privilege increases risk. Privileged access should be eligible, time-bound, strongly authenticated, and approved where the business risk justifies it.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Review:
eligible assignment
active assignment
activation duration
MFA/authentication strength
approval requirement
scope
```

### Expected Evidence

Highly privileged roles are not permanently active for ordinary administration.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use time-bound privileged elevation and a separate break-glass path.

---

## Advanced Deep Dive 6 — Managed Identity Lifecycle

### Concept

Managed identities remove stored credentials, but the identity still needs correct RBAC, network reachability, and lifecycle ownership. System-assigned and user-assigned identities have different lifecycle behavior.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az vm identity show -g <RG> -n <VM>
az identity list -g <RG> -o table
```

### Expected Evidence

The workload has a known principal ID with narrowly scoped permissions.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Prefer managed identities and avoid sharing one identity across unrelated applications.

---

## Advanced Deep Dive 7 — Federated Credentials for CI/CD

### Concept

External CI systems can obtain short-lived Azure credentials through federation instead of storing client secrets. Trust should be restricted by issuer, subject, audience, repository, and environment.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Validate:
issuer
subject
audience
target identity
role assignment scope
token lifetime
```

### Expected Evidence

CI can deploy without a long-lived Azure client secret.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use separate federation trust per environment/repository boundary.

---

## Advanced Deep Dive 8 — Azure Policy Effect Selection

### Concept

Audit, Deny, Modify, and DeployIfNotExists have different operational consequences. Governance should mature from visibility to enforcement instead of jumping directly to disruptive Deny rules.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az policy assignment list -o table
az policy state summarize -o table
```

### Expected Evidence

Each assignment has an intentional effect and remediation owner.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Roll policy out progressively: observe, test remediation, then enforce.

---

## Advanced Deep Dive 9 — Policy Remediation Identity

### Concept

Modify and DeployIfNotExists can require an assignment identity with permission to change existing resources. Policy evaluation can succeed while remediation fails.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az policy assignment list -o json
az policy remediation list -o table 2>/dev/null || true
```

### Expected Evidence

Remediation tasks complete using a narrowly scoped policy identity.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Grant the policy identity only the permissions required for remediation.

---

## Advanced Deep Dive 10 — Policy Exemptions

### Concept

Exceptions are sometimes necessary, but every exemption should have an owner, reason, exact scope, compensating control, and expiry/review date.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az policy exemption list -o table 2>/dev/null || true
```

### Expected Evidence

All exemptions are documented and time-bounded.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Treat exemptions as tracked risk, not permanent convenience.

---

## Advanced Deep Dive 11 — Resource Locks vs RBAC

### Concept

Locks are evaluated separately from RBAC and protect against accidental write/delete operations. An authorized user can still be blocked by an inherited lock.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az lock list --resource-group <RG> -o table
```

### Expected Evidence

Direct and inherited locks are known before maintenance.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use locks as an extra safety barrier, not as a substitute for least privilege.

---

## Advanced Deep Dive 12 — Azure Resource Graph

### Concept

Large estates need fleet-level discovery. Azure Resource Graph lets administrators query resource metadata across subscriptions quickly.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az graph query -q "Resources | project name, type, resourceGroup, subscriptionId, location | limit 25"
```

### Expected Evidence

Cross-subscription inventory is returned in a queryable form.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use Resource Graph for inventory, drift, exposure, and ownership investigations.

---

## Advanced Deep Dive 13 — Activity Log Investigation

### Concept

The Activity Log answers who changed an Azure resource, what operation occurred, when, and whether it succeeded.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az monitor activity-log list --offset 2h -o table
```

### Expected Evidence

Recent control-plane events show caller, operation, scope, and result.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Check Activity Log early when configuration changed unexpectedly.

---

## Advanced Deep Dive 14 — Bicep What-If

### Concept

Declarative deployment is safer when the proposed change is reviewed before execution. What-If exposes planned creates, deletes, and modifications.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az deployment group what-if   --resource-group <RG>   --template-file main.bicep
```

### Expected Evidence

High-risk changes are visible before deployment.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Require What-If review for production Bicep changes.

---

## Advanced Deep Dive 15 — Infrastructure Ownership and Drift

### Concept

A production resource should have one authoritative configuration owner. Manual portal changes plus multiple IaC tools create drift and unpredictable reconciliation.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
For each resource record:
authoritative tool
Git repository/module
owner
environment
deletion behavior
```

### Expected Evidence

No resource is simultaneously managed by conflicting systems.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Give every production resource one authoritative writer.

---

## Advanced Deep Dive 16 — Storage Network Access

### Concept

Storage 403 errors can come from correct identity but blocked network access. Public network settings, firewall rules, service endpoints, private endpoints, and DNS all matter.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az storage account show -g <RG> -n <ACCOUNT>   --query '{public:publicNetworkAccess,networkRuleSet:networkRuleSet}' -o json
```

### Expected Evidence

The intended client network path is allowed.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Troubleshoot Storage identity and network restrictions independently.

---

## Advanced Deep Dive 17 — User Delegation SAS

### Concept

A user delegation SAS provides short-lived blob access based on Entra authorization instead of exposing a storage account key.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Design:
resource path
permissions
start/expiry
HTTPS only
optional IP restriction
```

### Expected Evidence

Temporary access is narrow and expires automatically.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use the shortest practical SAS lifetime and narrowest resource scope.

---

## Advanced Deep Dive 18 — Storage Redundancy vs RPO

### Concept

ZRS/GRS/GZRS describe replication topology, not a guaranteed application RPO. Geo replication can be asynchronous and recovery behavior must be tested.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az storage account show -g <RG> -n <ACCOUNT>   --query '{sku:sku.name,primary:primaryLocation,secondary:secondaryLocation}' -o json
```

### Expected Evidence

The selected redundancy mode maps explicitly to zone/region failure requirements.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Do not derive business RPO from the redundancy acronym alone.

---

## Advanced Deep Dive 19 — Blob Versioning, Soft Delete, and Immutability

### Concept

Versioning, soft delete, and immutable retention protect against different failure modes: overwrite, accidental deletion, and prohibited modification/deletion.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az storage account blob-service-properties show   --account-name <ACCOUNT> --auth-mode login -o json
```

### Expected Evidence

Protection settings match the data threat and retention model.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Layer recovery controls according to threat model and compliance requirements.

---

## Advanced Deep Dive 20 — Private Endpoint DNS

### Concept

A private endpoint creates a private NIC, but clients normally use the service hostname. Private DNS must return the private address from the relevant VNet.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network private-endpoint list -o table
az network private-dns zone list -o table
nslookup <SERVICE_FQDN>
```

### Expected Evidence

The service FQDN resolves to the private endpoint IP from intended networks.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Design private endpoint and DNS together.

---

## Advanced Deep Dive 21 — Azure Private DNS Resolver

### Concept

Hybrid DNS needs explicit authority and forwarding rules between Azure and on-premises namespaces. A managed resolver can remove the need for custom DNS forwarding VMs.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Validate:
inbound endpoint
outbound endpoint
forwarding ruleset
VNet links
on-prem conditional forwarders
```

### Expected Evidence

Private names resolve consistently from Azure and on-premises.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Document DNS authority and forwarding paths like IP routes.

---

## Advanced Deep Dive 22 — NAT Gateway

### Concept

Private subnets often need controlled outbound Internet without per-VM public IPs. NAT Gateway provides managed SNAT and should be capacity-planned for connection-heavy workloads.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network nat gateway list -o table
az network public-ip list -o table
```

### Expected Evidence

Private workloads initiate outbound traffic through the intended NAT path.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use subnet-level NAT rather than widespread VM public IPs where appropriate.

---

## Advanced Deep Dive 23 — Azure Firewall vs NSG

### Concept

NSGs provide distributed stateful L3/L4 filtering; Azure Firewall provides centralized network/application policy and logging. They solve different layers and can complement each other.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network firewall list -o table
az network nsg list -o table
```

### Expected Evidence

Central inspection and workload segmentation responsibilities are clear.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Do not replace all workload segmentation with one central firewall.

---

## Advanced Deep Dive 24 — Firewall Policy Governance

### Concept

Large firewall estates need priority conventions, rule ownership, expiry, and review to prevent shadowing and rule sprawl.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Record:
priority
source
destination/FQDN
port/protocol
owner
business reason
expiry/review
```

### Expected Evidence

Firewall rules are attributable and deterministic.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Reserve priority bands and require rule ownership.

---

## Advanced Deep Dive 25 — User-Defined Routes / Forced Tunneling

### Concept

UDRs can force traffic through Azure Firewall/NVAs, but asymmetric return paths can break stateful inspection.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network nic show-effective-route-table -g <RG> -n <NIC> -o table
```

### Expected Evidence

The winning route and next hop match the architecture.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Verify both forward and return paths before forcing traffic through stateful appliances.

---

## Advanced Deep Dive 26 — VNet Peering and Transit

### Concept

VNet peering is private and high performance but is not automatically transitive. Hub-spoke designs need explicit forwarded traffic, gateway transit, UDR, firewall, and DNS architecture.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network vnet peering list -g <RG> --vnet-name <VNET> -o table
```

### Expected Evidence

Peering state and transit-related settings match the intended topology.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Document which networks may transit the hub and which remain isolated.

---

## Advanced Deep Dive 27 — Azure Virtual WAN

### Concept

Virtual WAN can centralize branch, VPN, ExpressRoute, and VNet connectivity through managed hubs for large-scale networks.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network vwan list -o table 2>/dev/null || true
az network vhub list -o table 2>/dev/null || true
```

### Expected Evidence

The routing topology is intentionally hub-based instead of pairwise sprawl.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Consider Virtual WAN when connectivity becomes an enterprise network problem.

---

## Advanced Deep Dive 28 — ExpressRoute Resilience

### Concept

One ExpressRoute circuit is not automatically end-to-end highly available. Edge devices, provider paths, peering sessions, gateways, and fallback paths are separate failure domains.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Validate:
dual edge
redundant peering
gateway redundancy
provider diversity where needed
VPN fallback if justified
BGP routes
```

### Expected Evidence

Hybrid applications have a tested failover path.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Test hybrid failover instead of assuming circuit redundancy.

---

## Advanced Deep Dive 29 — Network Watcher Connectivity Tests

### Concept

Use Network Watcher/effective routes/security rules before broad firewall changes. Configuration evidence is usually faster than guessing.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network watcher test-connectivity   --source-resource <VM_RESOURCE_ID>   --dest-address <DEST>   --dest-port <PORT>
```

### Expected Evidence

The blocked or reachable path is identified with evidence.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use network diagnostics before changing NSGs or routes.

---

## Advanced Deep Dive 30 — Azure Bastion

### Concept

Bastion separates administrative access from workload public exposure. VMs can remain private while authorized operators use controlled SSH/RDP paths.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network bastion list -o table
az vm list --show-details -o table
```

### Expected Evidence

Managed VMs do not require public management IPs.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Treat administration as a dedicated access plane.

---

## Advanced Deep Dive 31 — DDoS + WAF + Network Segmentation

### Concept

Volumetric protection, HTTP WAF controls, centralized firewalling, and NSG segmentation address different attack layers.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
DDoS → volumetric/network resilience
WAF → HTTP request filtering/rate controls
Firewall → centralized network/application policy
NSG → workload segmentation
```

### Expected Evidence

Each security layer has a defined purpose and telemetry source.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use layered controls instead of expecting one service to solve every attack.

---

## Advanced Deep Dive 32 — Front Door vs Application Gateway

### Concept

Front Door is global edge/application delivery; Application Gateway is regional and VNet-integrated. Some architectures use both.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az afd profile list -o table 2>/dev/null || true
az network application-gateway list -o table
```

### Expected Evidence

The selected tier matches global versus regional routing and private-backend needs.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Choose global and regional ingress tiers from placement requirements, not product familiarity.

---

## Advanced Deep Dive 33 — Application Gateway Backend Health

### Concept

Application Gateway routing depends on backend probe health. Hostname, path, TLS, NSG, UDR, and application readiness are common causes of 502/503 behavior.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network application-gateway show-backend-health   -g <RG> -n <APPGW> -o json
```

### Expected Evidence

Backend health output identifies the failed probe/path layer.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use explicit readiness probes and inspect backend health before changing routing.

---

## Advanced Deep Dive 34 — Azure Load Balancer Probe Quality

### Concept

A TCP probe can report a port open even when the application is functionally broken. Health checks should represent the highest useful layer supported by the architecture.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az network lb probe list -g <RG> --lb-name <LB> -o table
```

### Expected Evidence

Only backends capable of serving real traffic remain in rotation.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Design meaningful health endpoints instead of testing only port openness.

---

## Advanced Deep Dive 35 — VM Boot Diagnostics

### Concept

When SSH/RDP is unavailable, use instance view, boot diagnostics, and serial/guest evidence to distinguish OS boot failure from network failure.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az vm get-instance-view -g <RG> -n <VM> -o json
```

### Expected Evidence

Provisioning and VM health are known independently of guest network access.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Separate boot problems from NSG/routing problems before remediation.

---

## Advanced Deep Dive 36 — Azure Compute Gallery

### Concept

Golden images should be immutable, versioned, replicated, and traceable to source/build/test. Production scale sets should consume approved image versions.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az sig list -o table
az sig image-definition list -g <RG> --gallery-name <GALLERY> -o table
```

### Expected Evidence

Production instances map to an approved image release.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Treat images as versioned artifacts with provenance.

---

## Advanced Deep Dive 37 — VMSS Upgrade Safety

### Concept

A scale-set model change must be rolled into instances using a deliberate upgrade strategy, health gates, and capacity headroom.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az vmss show -g <RG> -n <VMSS>   --query '{upgradePolicy:upgradePolicy,orchestrationMode:orchestrationMode}' -o json
```

### Expected Evidence

Upgrade behavior and rollback conditions are known before rollout.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use progressive VMSS upgrades gated by application health.

---

## Advanced Deep Dive 38 — Patch Rings / Azure Update Management

### Concept

Patching should progress through dev, staging, production canary, then fleet, with reboot policy and application validation at each stage.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Patch ring:
scope
schedule
update classification
reboot behavior
health gate
rollback/replace path
```

### Expected Evidence

Production is patched only after lower rings validate.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Pair automated patching with staged rollout and image-based recovery.

---

## Advanced Deep Dive 39 — Managed Disk Performance

### Concept

Disk performance is constrained by disk SKU/configuration, VM storage limits, caching, filesystem, and workload access pattern.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az disk list -g <RG> -o table
az vm show -g <RG> -n <VM> --show-details -o json
```

### Expected Evidence

The real bottleneck is identified as disk, VM, or application.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Evaluate disk and VM limits together before buying more IOPS.

---

## Advanced Deep Dive 40 — Customer-Managed Key Availability

### Concept

CMK increases control but introduces Key Vault/Managed HSM, identity, permission, network, and key-state dependencies into storage/compute availability.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Validate:
key state
key location
managed identity
RBAC/key permissions
private networking
rotation/deletion controls
restore path
```

### Expected Evidence

Encrypted resources remain usable after restart, scale, and restore.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Treat encryption keys as availability dependencies and test recovery.

---

## Advanced Deep Dive 41 — ACR Identity and Image Pull

### Concept

Container platforms should pull from Azure Container Registry through managed identity/RBAC instead of registry admin credentials.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az acr list -o table
az role assignment list --scope <ACR_RESOURCE_ID> -o table
```

### Expected Evidence

Runtime identities have pull-only access; CI identities have separate push/deploy permissions.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Separate CI push permissions from runtime pull permissions.

---

## Advanced Deep Dive 42 — Immutable Container Artifact Promotion

### Concept

Build once and promote the same image digest from staging to production. Mutable `latest` tags undermine reproducibility and rollback.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az acr repository show-tags -n <ACR> --repository <REPO> --detail -o table
```

### Expected Evidence

Production can be traced to the exact artifact tested in staging.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Promote immutable digests/releases and retain rollback artifacts.

---

## Advanced Deep Dive 43 — Container Apps Revision Traffic

### Concept

Container Apps revisions support side-by-side releases and weighted traffic. Canary decisions need objective error, latency, business, and dependency thresholds.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az containerapp revision list -g <RG> -n <APP> -o table
```

### Expected Evidence

A bad revision can be rolled back without rebuilding.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Define canary success and rollback thresholds before shifting traffic.

---

## Advanced Deep Dive 44 — Event-Driven Container Apps Scaling

### Concept

Asynchronous workers should scale from backlog/age or another causal signal rather than CPU alone, with maximum replicas constrained by downstream capacity.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Define:
event source
threshold
min/max replicas
cooldown
identity
downstream capacity
```

### Expected Evidence

Replica count responds to work while protecting databases/APIs.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Scale async workers from backlog/latency signals.

---

## Advanced Deep Dive 45 — App Service Deployment Slots

### Concept

Slots allow staged release and swap, but slot-specific configuration and database compatibility determine whether rollback is actually safe.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az webapp deployment slot list -g <RG> -n <APP> -o table
```

### Expected Evidence

Environment-specific settings remain with the intended slot.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Inventory sticky settings and schema compatibility before swaps.

---

## Advanced Deep Dive 46 — App Service VNet Integration vs Private Endpoint

### Concept

VNet integration handles App Service outbound connectivity into a VNet; a private endpoint handles private inbound connectivity to App Service.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az webapp vnet-integration list -g <RG> -n <APP> -o table
az network private-endpoint list -o table
```

### Expected Evidence

Inbound and outbound private networking requirements are separately satisfied.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Identify traffic direction before choosing App Service networking features.

---

## Advanced Deep Dive 47 — App Service Stateless Scale-Out

### Concept

Scale-out assumes instances are replaceable. Sessions, uploaded files, and durable state should live in shared external services rather than local process/disk state.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Check:
session storage
upload storage
background jobs
local temp usage
connection affinity assumptions
```

### Expected Evidence

Any instance can be replaced without losing unique business state.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Externalize durable state before enabling aggressive scale-out.

---

## Advanced Deep Dive 48 — Azure Monitor Metrics vs Logs

### Concept

Metrics are efficient detection signals; logs provide detailed event context. Use metrics to detect and logs/KQL to explain.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az monitor metrics list --resource <RESOURCE_ID> --metric <METRIC_NAME> -o table
```

### Expected Evidence

The observability design uses the right telemetry type for each question.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Alert from stable metrics and investigate using richer logs/traces.

---

## Advanced Deep Dive 49 — Data Collection Rules

### Concept

Azure Monitor Agent collection should be defined centrally through Data Collection Rules rather than manual per-VM configuration.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az monitor data-collection rule list -o table 2>/dev/null || true
```

### Expected Evidence

VM telemetry collection is repeatable and auditable.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Version DCRs and deploy them as code.

---

## Advanced Deep Dive 50 — KQL Incident Queries

### Concept

Administrators should be able to filter logs by time, caller, operation, status, resource, and correlation fields to build an incident timeline.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```kusto
AzureActivity
| where TimeGenerated > ago(2h)
| where ActivityStatusValue != "Success"
| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue, ResourceGroup
| order by TimeGenerated desc
```

### Expected Evidence

Failed administrative operations are narrowed to the relevant actor and scope.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Maintain reusable KQL snippets for common operational questions.

---

## Advanced Deep Dive 51 — Actionable Alerts

### Concept

A production alert needs an owner, severity, action group, user/service impact description, and runbook. Otherwise it is telemetry noise.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az monitor metrics alert list -o table
az monitor action-group list -o table
```

### Expected Evidence

High-severity alerts map to an accountable team and first action.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Page only when timely human action is required.

---

## Advanced Deep Dive 52 — Diagnostic Settings Coverage

### Concept

Many resource logs are not centrally retained unless diagnostic settings route them. A resource can exist without useful forensic logging.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az monitor diagnostic-settings list --resource <RESOURCE_ID> -o json 2>/dev/null || true
```

### Expected Evidence

Critical resources export required logs to approved destinations.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Deploy diagnostic settings by Policy/IaC, not manually after incidents.

---

## Advanced Deep Dive 53 — Backup Security and Restore Testing

### Concept

Backup success does not prove recovery. Protection needs retention/security plus periodic restore, network, identity, key, and application validation.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Restore drill:
recovery point
target network
identity
Key Vault
application config
data validation
actual RTO
```

### Expected Evidence

A restore drill reaches a successful business transaction.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Measure restore success and actual restore time as operational KPIs.

---

## Advanced Deep Dive 54 — RPO from Protection Frequency

### Concept

RPO is the maximum tolerated data loss. Backup interval, PITR/log retention, and replication lag must collectively meet it.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Record:
business RPO
backup interval
PITR/log window
replication lag
last successful restore
```

### Expected Evidence

The latest recoverable state is within the business target.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Derive protection design from RPO, not from default backup schedules.

---

## Advanced Deep Dive 55 — Azure Site Recovery Test Failover

### Concept

Replication status alone does not prove DR. Test failover validates network mapping, DNS, secrets, dependencies, boot order, and application recovery.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Test:
recovery network
boot order
DNS
identity/secrets
database state
business transaction
RTO measurement
```

### Expected Evidence

A test exercise proves the application can run in the recovery region.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Test DR regularly and measure end-to-end RTO.

---

## Advanced Deep Dive 56 — Failback

### Concept

Returning from a recovery region requires data resynchronization, one clear write owner, application/version parity, and controlled traffic shift.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Failback prerequisites:
single write owner
replication healthy
data reconciled
version parity
DNS/routing ready
rollback path
```

### Expected Evidence

No data created during DR is lost during return to primary.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Document and test failback separately from failover.

---

## Advanced Deep Dive 57 — Key Vault Soft Delete and Purge Protection

### Concept

Key/secret deletion can become an availability incident. Recovery controls and restricted purge permissions reduce accidental or malicious permanent deletion.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az keyvault list -o table
az keyvault show -g <RG> -n <VAULT> -o json
```

### Expected Evidence

Critical key/secret objects remain recoverable according to policy.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Protect purge operations more strongly than normal secret usage.

---

## Advanced Deep Dive 58 — Defender for Cloud Triage

### Concept

Security findings should be prioritized using exposure, exploitability, business criticality, identity privilege, and fix availability—not severity label alone.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Triage:
resource owner
Internet exposure
finding severity
exploitability
data sensitivity
business criticality
remediation SLA
```

### Expected Evidence

High-risk findings become owned remediation work.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Prioritize security findings using real asset context.

---

## Advanced Deep Dive 59 — Azure Arc Hybrid Administration

### Concept

Azure Arc can project external servers/Kubernetes into Azure for inventory, policy, monitoring, and selected operations, but the underlying platform still has its own responsibilities.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az connectedmachine list -o table 2>/dev/null || true
```

### Expected Evidence

Connected hybrid resources have known owner, connectivity, and agent health.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use Arc to centralize governance without pretending every platform is identical.

---

## Advanced Deep Dive 60 — FinOps Tagging and Unit Cost

### Concept

Cost visibility should map spend to owner/application/environment and preferably to a business unit metric such as cost per order or active customer.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```python
monthly_cost = 42000
orders = 350000
print("Cost per order:", monthly_cost / orders)
```

### Expected Evidence

Teams can distinguish normal business growth from inefficient spending.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Track both ownership tags and business-aligned unit cost.

---

## Advanced Deep Dive 61 — Quota as Reliability Dependency

### Concept

Autoscale and disaster recovery only work when regional vCPU, public IP, networking, and service quotas have headroom.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az vm list-usage -l <REGION> -o table
```

### Expected Evidence

Peak and recovery scenarios fit inside approved quotas.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Review quota headroom before a traffic surge or regional failover.

---

## Advanced Deep Dive 62 — SLO and Error Budget

### Concept

A production Azure service should define measurable user-facing success and latency targets rather than rely on the phrase 'highly available'.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
Example:
SLI = successful checkout requests / valid checkout requests
SLO = 99.95% monthly
Latency SLO = p95 < 750 ms
```

### Expected Evidence

Dashboards can state whether the user-facing service meets its target.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Use SLOs to connect architecture, alerting, and release risk.

---

## Advanced Deep Dive 63 — Change Evidence Chain

### Concept

A production change should be traceable from Git/Bicep to deployment ID, Activity Log, resulting resource state, telemetry, and rollback/verification.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az deployment group list -g <RG> -o table
az monitor activity-log list --offset 4h -o table
```

### Expected Evidence

An incident can be correlated with the exact change that preceded it.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Link source commit, deployment identity, and runtime evidence.

---

## Advanced Deep Dive 64 — Operational Readiness Review

### Concept

A critical workload is not ready until ownership, SLO, alerts, logs, backup/restore, quota, secrets/keys, deployment rollback, cost, and runbooks are proven.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```text
[ ] owner/on-call
[ ] SLO
[ ] alerts/runbooks
[ ] diagnostics
[ ] backup + restore test
[ ] quota/headroom
[ ] rollback
[ ] secret/key lifecycle
[ ] budget/tags
```

### Expected Evidence

The team can operate and recover the service before production launch.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Make operational readiness a launch gate.

---

## Advanced Deep Dive 65 — Evidence-First Troubleshooting

### Concept

Use a consistent sequence: identity/context, RBAC/Policy, DNS, routing, NSG/firewall, platform health, application, data dependency, monitoring evidence, recent changes.

### Architecture / Mental Model

```text
Requirement
   ↓
Azure control or service
   ↓
Identity + Scope
   ↓
DNS + Network
   ↓
Compute / Data Plane
   ↓
Monitoring Evidence
```

### CLI / PowerShell / KQL / Configuration

```bash
az account show
az monitor activity-log list --offset 1h -o table
```

### Expected Evidence

The failing layer is identified before remediation.

### Why It Works

Azure separates identity, ARM control-plane operations, resource networking, and service data planes. A successful deployment request proves only that the control-plane operation was accepted; production validation must confirm the intended data path and recovery behavior.

### Production Example

Use this topic in a production-style architecture by documenting the requirement, target scope, principal, network path, expected telemetry, failure mode, rollback/recovery plan, and owner.

### Troubleshooting

```text
Reproduce symptom
  ↓
Verify tenant/subscription/identity
  ↓
Inspect RBAC / Policy / lock
  ↓
Resolve DNS
  ↓
Inspect route / NSG / firewall
  ↓
Inspect platform/service health
  ↓
Inspect application/data dependency
  ↓
Check Activity Log / Monitor / KQL
  ↓
Make one controlled correction
  ↓
Verify and prevent recurrence
```

### Common Mistakes

- Granting broad privilege before identifying the denied layer.
- Enabling public network access to bypass private DNS problems.
- Treating a successful ARM deployment as proof that the application works.
- Changing routes, NSGs, DNS, and identity simultaneously.
- Ignoring quota, KMS/Key Vault, backup, and cost implications.

### Best Practice

Change one layer at a time and preserve the evidence that justified the change.

---

# Supplemental Hands-on Lab Series — Microsoft Azure Administration

## Enhanced Lab 1 — Context Safety and Subscription Selection

### Objective

Prove **Context Safety and Subscription Selection** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az account show --query '{subscription:name,id:id,tenant:tenantId,user:user.name}' -o table
az account list -o table
```

```powershell
Get-AzContext
Get-AzSubscription
```

### Expected Result

The active tenant, subscription, and identity match the intended environment.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Fail closed when the expected tenant/subscription does not match.

---

## Enhanced Lab 2 — Management Group Governance

### Objective

Prove **Management Group Governance** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az account management-group list -o table
```

### Expected Result

Subscriptions are attached to the intended governance branch.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Keep the management-group hierarchy shallow, stable, and policy-oriented.

---

## Enhanced Lab 3 — RBAC Effective Access

### Objective

Prove **RBAC Effective Access** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az role assignment list --assignee <OBJECT_ID> --all -o table
```

### Expected Result

All relevant assignments and scopes are visible.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use groups and the lowest practical scope; do not grant Owner to troubleshoot.

---

## Enhanced Lab 4 — Control Plane vs Data Plane Authorization

### Objective

Prove **Control Plane vs Data Plane Authorization** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az role assignment list --scope <RESOURCE_ID> -o table
```

### Expected Result

Control-plane roles and data roles are distinguishable.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Troubleshoot management authorization and data authorization separately.

---

## Enhanced Lab 5 — Privileged Access / Just-in-Time Administration

### Objective

Prove **Privileged Access / Just-in-Time Administration** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Review:
eligible assignment
active assignment
activation duration
MFA/authentication strength
approval requirement
scope
```

### Expected Result

Highly privileged roles are not permanently active for ordinary administration.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use time-bound privileged elevation and a separate break-glass path.

---

## Enhanced Lab 6 — Managed Identity Lifecycle

### Objective

Prove **Managed Identity Lifecycle** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az vm identity show -g <RG> -n <VM>
az identity list -g <RG> -o table
```

### Expected Result

The workload has a known principal ID with narrowly scoped permissions.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prefer managed identities and avoid sharing one identity across unrelated applications.

---

## Enhanced Lab 7 — Federated Credentials for CI/CD

### Objective

Prove **Federated Credentials for CI/CD** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Validate:
issuer
subject
audience
target identity
role assignment scope
token lifetime
```

### Expected Result

CI can deploy without a long-lived Azure client secret.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use separate federation trust per environment/repository boundary.

---

## Enhanced Lab 8 — Azure Policy Effect Selection

### Objective

Prove **Azure Policy Effect Selection** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az policy assignment list -o table
az policy state summarize -o table
```

### Expected Result

Each assignment has an intentional effect and remediation owner.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Roll policy out progressively: observe, test remediation, then enforce.

---

## Enhanced Lab 9 — Policy Remediation Identity

### Objective

Prove **Policy Remediation Identity** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az policy assignment list -o json
az policy remediation list -o table 2>/dev/null || true
```

### Expected Result

Remediation tasks complete using a narrowly scoped policy identity.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Grant the policy identity only the permissions required for remediation.

---

## Enhanced Lab 10 — Policy Exemptions

### Objective

Prove **Policy Exemptions** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az policy exemption list -o table 2>/dev/null || true
```

### Expected Result

All exemptions are documented and time-bounded.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat exemptions as tracked risk, not permanent convenience.

---

## Enhanced Lab 11 — Resource Locks vs RBAC

### Objective

Prove **Resource Locks vs RBAC** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az lock list --resource-group <RG> -o table
```

### Expected Result

Direct and inherited locks are known before maintenance.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use locks as an extra safety barrier, not as a substitute for least privilege.

---

## Enhanced Lab 12 — Azure Resource Graph

### Objective

Prove **Azure Resource Graph** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az graph query -q "Resources | project name, type, resourceGroup, subscriptionId, location | limit 25"
```

### Expected Result

Cross-subscription inventory is returned in a queryable form.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use Resource Graph for inventory, drift, exposure, and ownership investigations.

---

## Enhanced Lab 13 — Activity Log Investigation

### Objective

Prove **Activity Log Investigation** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az monitor activity-log list --offset 2h -o table
```

### Expected Result

Recent control-plane events show caller, operation, scope, and result.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Check Activity Log early when configuration changed unexpectedly.

---

## Enhanced Lab 14 — Bicep What-If

### Objective

Prove **Bicep What-If** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az deployment group what-if   --resource-group <RG>   --template-file main.bicep
```

### Expected Result

High-risk changes are visible before deployment.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Require What-If review for production Bicep changes.

---

## Enhanced Lab 15 — Infrastructure Ownership and Drift

### Objective

Prove **Infrastructure Ownership and Drift** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
For each resource record:
authoritative tool
Git repository/module
owner
environment
deletion behavior
```

### Expected Result

No resource is simultaneously managed by conflicting systems.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Give every production resource one authoritative writer.

---

## Enhanced Lab 16 — Storage Network Access

### Objective

Prove **Storage Network Access** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az storage account show -g <RG> -n <ACCOUNT>   --query '{public:publicNetworkAccess,networkRuleSet:networkRuleSet}' -o json
```

### Expected Result

The intended client network path is allowed.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Troubleshoot Storage identity and network restrictions independently.

---

## Enhanced Lab 17 — User Delegation SAS

### Objective

Prove **User Delegation SAS** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Design:
resource path
permissions
start/expiry
HTTPS only
optional IP restriction
```

### Expected Result

Temporary access is narrow and expires automatically.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use the shortest practical SAS lifetime and narrowest resource scope.

---

## Enhanced Lab 18 — Storage Redundancy vs RPO

### Objective

Prove **Storage Redundancy vs RPO** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az storage account show -g <RG> -n <ACCOUNT>   --query '{sku:sku.name,primary:primaryLocation,secondary:secondaryLocation}' -o json
```

### Expected Result

The selected redundancy mode maps explicitly to zone/region failure requirements.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Do not derive business RPO from the redundancy acronym alone.

---

## Enhanced Lab 19 — Blob Versioning, Soft Delete, and Immutability

### Objective

Prove **Blob Versioning, Soft Delete, and Immutability** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az storage account blob-service-properties show   --account-name <ACCOUNT> --auth-mode login -o json
```

### Expected Result

Protection settings match the data threat and retention model.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Layer recovery controls according to threat model and compliance requirements.

---

## Enhanced Lab 20 — Private Endpoint DNS

### Objective

Prove **Private Endpoint DNS** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network private-endpoint list -o table
az network private-dns zone list -o table
nslookup <SERVICE_FQDN>
```

### Expected Result

The service FQDN resolves to the private endpoint IP from intended networks.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design private endpoint and DNS together.

---

## Enhanced Lab 21 — Azure Private DNS Resolver

### Objective

Prove **Azure Private DNS Resolver** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Validate:
inbound endpoint
outbound endpoint
forwarding ruleset
VNet links
on-prem conditional forwarders
```

### Expected Result

Private names resolve consistently from Azure and on-premises.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Document DNS authority and forwarding paths like IP routes.

---

## Enhanced Lab 22 — NAT Gateway

### Objective

Prove **NAT Gateway** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network nat gateway list -o table
az network public-ip list -o table
```

### Expected Result

Private workloads initiate outbound traffic through the intended NAT path.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use subnet-level NAT rather than widespread VM public IPs where appropriate.

---

## Enhanced Lab 23 — Azure Firewall vs NSG

### Objective

Prove **Azure Firewall vs NSG** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network firewall list -o table
az network nsg list -o table
```

### Expected Result

Central inspection and workload segmentation responsibilities are clear.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Do not replace all workload segmentation with one central firewall.

---

## Enhanced Lab 24 — Firewall Policy Governance

### Objective

Prove **Firewall Policy Governance** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Record:
priority
source
destination/FQDN
port/protocol
owner
business reason
expiry/review
```

### Expected Result

Firewall rules are attributable and deterministic.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Reserve priority bands and require rule ownership.

---

## Enhanced Lab 25 — User-Defined Routes / Forced Tunneling

### Objective

Prove **User-Defined Routes / Forced Tunneling** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network nic show-effective-route-table -g <RG> -n <NIC> -o table
```

### Expected Result

The winning route and next hop match the architecture.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Verify both forward and return paths before forcing traffic through stateful appliances.

---

## Enhanced Lab 26 — VNet Peering and Transit

### Objective

Prove **VNet Peering and Transit** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network vnet peering list -g <RG> --vnet-name <VNET> -o table
```

### Expected Result

Peering state and transit-related settings match the intended topology.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Document which networks may transit the hub and which remain isolated.

---

## Enhanced Lab 27 — Azure Virtual WAN

### Objective

Prove **Azure Virtual WAN** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network vwan list -o table 2>/dev/null || true
az network vhub list -o table 2>/dev/null || true
```

### Expected Result

The routing topology is intentionally hub-based instead of pairwise sprawl.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Consider Virtual WAN when connectivity becomes an enterprise network problem.

---

## Enhanced Lab 28 — ExpressRoute Resilience

### Objective

Prove **ExpressRoute Resilience** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Validate:
dual edge
redundant peering
gateway redundancy
provider diversity where needed
VPN fallback if justified
BGP routes
```

### Expected Result

Hybrid applications have a tested failover path.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Test hybrid failover instead of assuming circuit redundancy.

---

## Enhanced Lab 29 — Network Watcher Connectivity Tests

### Objective

Prove **Network Watcher Connectivity Tests** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network watcher test-connectivity   --source-resource <VM_RESOURCE_ID>   --dest-address <DEST>   --dest-port <PORT>
```

### Expected Result

The blocked or reachable path is identified with evidence.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use network diagnostics before changing NSGs or routes.

---

## Enhanced Lab 30 — Azure Bastion

### Objective

Prove **Azure Bastion** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network bastion list -o table
az vm list --show-details -o table
```

### Expected Result

Managed VMs do not require public management IPs.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat administration as a dedicated access plane.

---

## Enhanced Lab 31 — DDoS + WAF + Network Segmentation

### Objective

Prove **DDoS + WAF + Network Segmentation** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
DDoS → volumetric/network resilience
WAF → HTTP request filtering/rate controls
Firewall → centralized network/application policy
NSG → workload segmentation
```

### Expected Result

Each security layer has a defined purpose and telemetry source.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use layered controls instead of expecting one service to solve every attack.

---

## Enhanced Lab 32 — Front Door vs Application Gateway

### Objective

Prove **Front Door vs Application Gateway** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az afd profile list -o table 2>/dev/null || true
az network application-gateway list -o table
```

### Expected Result

The selected tier matches global versus regional routing and private-backend needs.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Choose global and regional ingress tiers from placement requirements, not product familiarity.

---

## Enhanced Lab 33 — Application Gateway Backend Health

### Objective

Prove **Application Gateway Backend Health** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network application-gateway show-backend-health   -g <RG> -n <APPGW> -o json
```

### Expected Result

Backend health output identifies the failed probe/path layer.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use explicit readiness probes and inspect backend health before changing routing.

---

## Enhanced Lab 34 — Azure Load Balancer Probe Quality

### Objective

Prove **Azure Load Balancer Probe Quality** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az network lb probe list -g <RG> --lb-name <LB> -o table
```

### Expected Result

Only backends capable of serving real traffic remain in rotation.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Design meaningful health endpoints instead of testing only port openness.

---

## Enhanced Lab 35 — VM Boot Diagnostics

### Objective

Prove **VM Boot Diagnostics** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az vm get-instance-view -g <RG> -n <VM> -o json
```

### Expected Result

Provisioning and VM health are known independently of guest network access.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Separate boot problems from NSG/routing problems before remediation.

---

## Enhanced Lab 36 — Azure Compute Gallery

### Objective

Prove **Azure Compute Gallery** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az sig list -o table
az sig image-definition list -g <RG> --gallery-name <GALLERY> -o table
```

### Expected Result

Production instances map to an approved image release.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat images as versioned artifacts with provenance.

---

## Enhanced Lab 37 — VMSS Upgrade Safety

### Objective

Prove **VMSS Upgrade Safety** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az vmss show -g <RG> -n <VMSS>   --query '{upgradePolicy:upgradePolicy,orchestrationMode:orchestrationMode}' -o json
```

### Expected Result

Upgrade behavior and rollback conditions are known before rollout.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use progressive VMSS upgrades gated by application health.

---

## Enhanced Lab 38 — Patch Rings / Azure Update Management

### Objective

Prove **Patch Rings / Azure Update Management** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Patch ring:
scope
schedule
update classification
reboot behavior
health gate
rollback/replace path
```

### Expected Result

Production is patched only after lower rings validate.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Pair automated patching with staged rollout and image-based recovery.

---

## Enhanced Lab 39 — Managed Disk Performance

### Objective

Prove **Managed Disk Performance** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az disk list -g <RG> -o table
az vm show -g <RG> -n <VM> --show-details -o json
```

### Expected Result

The real bottleneck is identified as disk, VM, or application.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Evaluate disk and VM limits together before buying more IOPS.

---

## Enhanced Lab 40 — Customer-Managed Key Availability

### Objective

Prove **Customer-Managed Key Availability** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Validate:
key state
key location
managed identity
RBAC/key permissions
private networking
rotation/deletion controls
restore path
```

### Expected Result

Encrypted resources remain usable after restart, scale, and restore.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Treat encryption keys as availability dependencies and test recovery.

---

## Enhanced Lab 41 — ACR Identity and Image Pull

### Objective

Prove **ACR Identity and Image Pull** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az acr list -o table
az role assignment list --scope <ACR_RESOURCE_ID> -o table
```

### Expected Result

Runtime identities have pull-only access; CI identities have separate push/deploy permissions.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Separate CI push permissions from runtime pull permissions.

---

## Enhanced Lab 42 — Immutable Container Artifact Promotion

### Objective

Prove **Immutable Container Artifact Promotion** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az acr repository show-tags -n <ACR> --repository <REPO> --detail -o table
```

### Expected Result

Production can be traced to the exact artifact tested in staging.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Promote immutable digests/releases and retain rollback artifacts.

---

## Enhanced Lab 43 — Container Apps Revision Traffic

### Objective

Prove **Container Apps Revision Traffic** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az containerapp revision list -g <RG> -n <APP> -o table
```

### Expected Result

A bad revision can be rolled back without rebuilding.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Define canary success and rollback thresholds before shifting traffic.

---

## Enhanced Lab 44 — Event-Driven Container Apps Scaling

### Objective

Prove **Event-Driven Container Apps Scaling** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Define:
event source
threshold
min/max replicas
cooldown
identity
downstream capacity
```

### Expected Result

Replica count responds to work while protecting databases/APIs.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Scale async workers from backlog/latency signals.

---

## Enhanced Lab 45 — App Service Deployment Slots

### Objective

Prove **App Service Deployment Slots** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az webapp deployment slot list -g <RG> -n <APP> -o table
```

### Expected Result

Environment-specific settings remain with the intended slot.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Inventory sticky settings and schema compatibility before swaps.

---

## Enhanced Lab 46 — App Service VNet Integration vs Private Endpoint

### Objective

Prove **App Service VNet Integration vs Private Endpoint** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az webapp vnet-integration list -g <RG> -n <APP> -o table
az network private-endpoint list -o table
```

### Expected Result

Inbound and outbound private networking requirements are separately satisfied.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Identify traffic direction before choosing App Service networking features.

---

## Enhanced Lab 47 — App Service Stateless Scale-Out

### Objective

Prove **App Service Stateless Scale-Out** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Check:
session storage
upload storage
background jobs
local temp usage
connection affinity assumptions
```

### Expected Result

Any instance can be replaced without losing unique business state.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Externalize durable state before enabling aggressive scale-out.

---

## Enhanced Lab 48 — Azure Monitor Metrics vs Logs

### Objective

Prove **Azure Monitor Metrics vs Logs** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az monitor metrics list --resource <RESOURCE_ID> --metric <METRIC_NAME> -o table
```

### Expected Result

The observability design uses the right telemetry type for each question.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Alert from stable metrics and investigate using richer logs/traces.

---

## Enhanced Lab 49 — Data Collection Rules

### Objective

Prove **Data Collection Rules** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az monitor data-collection rule list -o table 2>/dev/null || true
```

### Expected Result

VM telemetry collection is repeatable and auditable.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Version DCRs and deploy them as code.

---

## Enhanced Lab 50 — KQL Incident Queries

### Objective

Prove **KQL Incident Queries** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```kusto
AzureActivity
| where TimeGenerated > ago(2h)
| where ActivityStatusValue != "Success"
| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue, ResourceGroup
| order by TimeGenerated desc
```

### Expected Result

Failed administrative operations are narrowed to the relevant actor and scope.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Maintain reusable KQL snippets for common operational questions.

---

## Enhanced Lab 51 — Actionable Alerts

### Objective

Prove **Actionable Alerts** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az monitor metrics alert list -o table
az monitor action-group list -o table
```

### Expected Result

High-severity alerts map to an accountable team and first action.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Page only when timely human action is required.

---

## Enhanced Lab 52 — Diagnostic Settings Coverage

### Objective

Prove **Diagnostic Settings Coverage** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az monitor diagnostic-settings list --resource <RESOURCE_ID> -o json 2>/dev/null || true
```

### Expected Result

Critical resources export required logs to approved destinations.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Deploy diagnostic settings by Policy/IaC, not manually after incidents.

---

## Enhanced Lab 53 — Backup Security and Restore Testing

### Objective

Prove **Backup Security and Restore Testing** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Restore drill:
recovery point
target network
identity
Key Vault
application config
data validation
actual RTO
```

### Expected Result

A restore drill reaches a successful business transaction.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Measure restore success and actual restore time as operational KPIs.

---

## Enhanced Lab 54 — RPO from Protection Frequency

### Objective

Prove **RPO from Protection Frequency** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Record:
business RPO
backup interval
PITR/log window
replication lag
last successful restore
```

### Expected Result

The latest recoverable state is within the business target.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Derive protection design from RPO, not from default backup schedules.

---

## Enhanced Lab 55 — Azure Site Recovery Test Failover

### Objective

Prove **Azure Site Recovery Test Failover** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Test:
recovery network
boot order
DNS
identity/secrets
database state
business transaction
RTO measurement
```

### Expected Result

A test exercise proves the application can run in the recovery region.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Test DR regularly and measure end-to-end RTO.

---

## Enhanced Lab 56 — Failback

### Objective

Prove **Failback** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Failback prerequisites:
single write owner
replication healthy
data reconciled
version parity
DNS/routing ready
rollback path
```

### Expected Result

No data created during DR is lost during return to primary.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Document and test failback separately from failover.

---

## Enhanced Lab 57 — Key Vault Soft Delete and Purge Protection

### Objective

Prove **Key Vault Soft Delete and Purge Protection** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az keyvault list -o table
az keyvault show -g <RG> -n <VAULT> -o json
```

### Expected Result

Critical key/secret objects remain recoverable according to policy.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Protect purge operations more strongly than normal secret usage.

---

## Enhanced Lab 58 — Defender for Cloud Triage

### Objective

Prove **Defender for Cloud Triage** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Triage:
resource owner
Internet exposure
finding severity
exploitability
data sensitivity
business criticality
remediation SLA
```

### Expected Result

High-risk findings become owned remediation work.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Prioritize security findings using real asset context.

---

## Enhanced Lab 59 — Azure Arc Hybrid Administration

### Objective

Prove **Azure Arc Hybrid Administration** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az connectedmachine list -o table 2>/dev/null || true
```

### Expected Result

Connected hybrid resources have known owner, connectivity, and agent health.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use Arc to centralize governance without pretending every platform is identical.

---

## Enhanced Lab 60 — FinOps Tagging and Unit Cost

### Objective

Prove **FinOps Tagging and Unit Cost** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```python
monthly_cost = 42000
orders = 350000
print("Cost per order:", monthly_cost / orders)
```

### Expected Result

Teams can distinguish normal business growth from inefficient spending.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Track both ownership tags and business-aligned unit cost.

---

## Enhanced Lab 61 — Quota as Reliability Dependency

### Objective

Prove **Quota as Reliability Dependency** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az vm list-usage -l <REGION> -o table
```

### Expected Result

Peak and recovery scenarios fit inside approved quotas.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Review quota headroom before a traffic surge or regional failover.

---

## Enhanced Lab 62 — SLO and Error Budget

### Objective

Prove **SLO and Error Budget** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
Example:
SLI = successful checkout requests / valid checkout requests
SLO = 99.95% monthly
Latency SLO = p95 < 750 ms
```

### Expected Result

Dashboards can state whether the user-facing service meets its target.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Use SLOs to connect architecture, alerting, and release risk.

---

## Enhanced Lab 63 — Change Evidence Chain

### Objective

Prove **Change Evidence Chain** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az deployment group list -g <RG> -o table
az monitor activity-log list --offset 4h -o table
```

### Expected Result

An incident can be correlated with the exact change that preceded it.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Link source commit, deployment identity, and runtime evidence.

---

## Enhanced Lab 64 — Operational Readiness Review

### Objective

Prove **Operational Readiness Review** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```text
[ ] owner/on-call
[ ] SLO
[ ] alerts/runbooks
[ ] diagnostics
[ ] backup + restore test
[ ] quota/headroom
[ ] rollback
[ ] secret/key lifecycle
[ ] budget/tags
```

### Expected Result

The team can operate and recover the service before production launch.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
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

## Enhanced Lab 65 — Evidence-First Troubleshooting

### Objective

Prove **Evidence-First Troubleshooting** through read-only discovery, one controlled failure, and evidence-based recovery.

### Procedure

1. Verify `az account show` / `Get-AzContext`.
2. Draw the expected control/data path.
3. Run the discovery command/query below.
4. Record the expected state.
5. In a disposable sandbox, introduce one reversible misconfiguration where safe.
6. Troubleshoot one layer at a time.
7. Restore the intended configuration.
8. Verify with both control-plane and data-plane evidence.
9. Record security, reliability, and cost impact.
10. Remove billable resources.

### Command / Query

```bash
az account show
az monitor activity-log list --offset 1h -o table
```

### Expected Result

The failing layer is identified before remediation.

### Evidence Record

```text
Symptom
Active identity
Subscription / resource scope
Expected behavior
Observed evidence
Root cause
Correction
Verification
Prevention
Automation opportunity
```

### Best Practice

Change one layer at a time and preserve the evidence that justified the change.

---

## 5. Hands-on Lab / Practical Exercises

> Use an Azure sandbox/training subscription where possible. Check current costs before creating resources and delete lab resources after use.

### Lab 1 — Verify Tenant and Subscription

CLI:

```bash
az account show
az account list -o table
```

PowerShell:

```powershell
Get-AzContext
Get-AzSubscription
```

Record:

```text
Tenant
Subscription
Identity
```

### Lab 2 — Create Users and Groups

Create:

```text
User: lab-admin
User: lab-reader
Group: AZ-Operators
```

Add members and document object IDs.

### Lab 3 — External User Tabletop

Design a B2B guest workflow:

```text
invite
 ↓
group
 ↓
Reader role
 ↓
quarterly review
 ↓
remove
```

### Lab 4 — SSPR Design

Define:

```text
scope
authentication methods
registration
notification
emergency support path
```

### Lab 5 — RBAC Assignment

Assign:

```text
Reader
```

to a group at a resource-group scope.

Verify effective access.

### Lab 6 — RBAC Troubleshooting

Create scenarios:

```text
Reader at subscription
Contributor at RG
Storage Blob Data Reader at storage
deny assignment
```

Determine effective permissions.

### Lab 7 — Management Group Design

Create conceptual hierarchy:

```text
Tenant Root
├─ Platform
├─ Production
├─ NonProduction
└─ Sandbox
```

Assign subscriptions.

### Lab 8 — Azure Policy

Create a policy concept:

```text
Allowed locations = approved regions
```

Then another:

```text
Require tag Owner
```

Compare Audit vs Deny.

### Lab 9 — Resource Lock

Apply `CanNotDelete` to a lab resource group.

Attempt safe delete operation and observe behavior.

Remove lock before cleanup.

### Lab 10 — Budget and Cost Governance

Create a lab budget:

```text
50%
80%
100%
```

Document alert recipients and why budget does not automatically stop services.

### Lab 11 — Storage Account

Create a general-purpose storage account.

Record:

```text
Region
redundancy
network access
encryption
```

### Lab 12 — Storage Access Methods

Compare:

```text
account key
SAS
Entra/RBAC
managed identity
```

for four application scenarios.

### Lab 13 — SAS

Generate a short-lived lab SAS with minimal permissions.

Document:

```text
resource
permissions
expiry
protocol
```

Revoke/remove when finished.

### Lab 14 — Blob Lifecycle

Design:

```text
Hot 0–30d
Cool 31–90d
Cold 91–365d
Archive >365d
Delete after 7y
```

### Lab 15 — Blob Protection

Configure/tabletop:

```text
versioning
soft delete
container soft delete
```

Then simulate accidental overwrite/delete.

### Lab 16 — Azure Files

Create a lab share.

Test:

```text
share quota
snapshot
soft delete
```

### Lab 17 — AzCopy

Copy a small test folder to Blob Storage.

Verify object count and clean up.

### Lab 18 — Bicep Deployment

Create:

```bicep
param location string = resourceGroup().location

resource stg 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'uniquelabstorage'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
```

Run:

```bash
az deployment group what-if ...
az deployment group create ...
```

Use a valid current API version before real deployment.

### Lab 19 — Create VM

Create one disposable Linux VM.

Record:

```text
size
image
disk
NIC
subnet
identity
```

Avoid unnecessary public exposure.

### Lab 20 — VM Managed Identity

Enable managed identity.

Grant read-only access to one lab resource/service.

Explain token-based access.

### Lab 21 — VM Availability

Compare:

```text
single VM
availability set
availability zones
VMSS
```

for four business requirements.

### Lab 22 — VMSS Design

Create conceptual VMSS:

```text
min 2
max 10
two/three zones
autoscale
health
load balancer
```

### Lab 23 — ACR + Container

Build a simple container and design:

```text
build
 ↓
ACR
 ↓
ACI
```

Use managed identity/service principal rather than admin credentials where possible.

### Lab 24 — Container Apps

Deploy/tabletop:

```text
revision 1
revision 2
```

Shift traffic gradually and test rollback.

### Lab 25 — App Service

Deploy a simple web app.

Configure:

```text
App Service Plan
HTTPS
custom setting
logging
```

### Lab 26 — App Service Slots

Create:

```text
production
staging
```

Deploy new version to staging, validate, then swap.

### Lab 27 — VNet Architecture

Create:

```text
10.20.0.0/16

Web     10.20.1.0/24
App     10.20.2.0/24
DB      10.20.3.0/24
Private 10.20.4.0/24
```

### Lab 28 — NSG Chain

Design:

```text
Internet → Web 443
Web → App 8443
App → DB 1433/5432
```

Use ASGs where useful.

### Lab 29 — Effective Security Rules

Use Azure Network Watcher/portal to inspect effective rules for a test VM NIC.

Explain the winning rule.

### Lab 30 — Private Endpoint

Create/design private endpoint for Storage.

Verify:

```text
private DNS
private IP
public access behavior
```

### Lab 31 — Azure Bastion

Design:

```text
Admin
 ↓
Bastion
 ↓
VM private IP
```

Compare with public SSH/RDP.

### Lab 32 — Load Balancer

Configure conceptual/public or internal load balancer with:

```text
frontend
backend pool
health probe
rule
```

Break the health probe and troubleshoot.

### Lab 33 — Network Watcher

Use at least two:

```text
IP flow verify
next hop
Connection Monitor
```

to diagnose a connection.

### Lab 34 — Azure Monitor + KQL

Enable diagnostics and query:

```kusto
AzureActivity
| where TimeGenerated > ago(1h)
| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue
```

Explain findings.

### Lab 35 — Alerts

Create/tabletop:

```text
VM high CPU alert
Action Group
maintenance suppression rule
```

### Lab 36 — Backup and Site Recovery

Design:

```text
daily VM backup
retention
restore test
secondary-region ASR
test failover
```

Define:

```text
RPO
RTO
test frequency
```

---

## 6. Mini Project

# Mini Project — Azure Enterprise Administration Platform

Build/design an Azure environment for a manufacturing/customer portal.

## Business Requirements

```text
production + nonproduction
10,000 daily users
sensitive order/customer data
hybrid corporate access
RPO = 1 hour
RTO = 4 hours
multi-zone application
central monitoring
controlled cost
```

## Hierarchy

```text
Tenant Root
├─ Platform
│  ├─ Connectivity Subscription
│  └─ Management Subscription
└─ Landing Zones
   ├─ Production Subscription
   └─ NonProduction Subscription
```

## Identity

Implement/design:

```text
Entra groups
RBAC
external-user policy
SSPR
MFA strategy
managed identities
least privilege
```

## Governance

```text
Azure Policy
locks
mandatory tags
budgets
Advisor
```

Required tags:

```text
Owner
Environment
Application
CostCenter
Criticality
DataClassification
```

## Network

```text
Hub VNet
├─ Azure Firewall/NVA if justified
├─ Bastion
├─ Private DNS
└─ VPN/ExpressRoute concept

Spoke VNet — Application
├─ Web
├─ App
├─ Data
└─ PrivateEndpoints
```

Implement/design:

```text
peering
NSGs
ASGs
UDRs
private endpoints
service endpoints where justified
Azure DNS
```

## Compute

Select/use:

```text
VMSS
App Service
Container Apps
ACI
```

for different workload parts.

Explain why.

## Storage

Configure:

```text
StorageV2
Blob
Files
redundancy
lifecycle
versioning
soft delete
private access
identity-based authorization
```

## App Service

Configure:

```text
plan
TLS
custom domain
VNet integration
private endpoint if required
deployment slot
backup
```

## Monitoring

```text
Azure Monitor
Log Analytics
VM Insights
diagnostic settings
alerts
action groups
KQL
Network Watcher
```

## Backup / DR

```text
Recovery Services Vault
Backup Vault where applicable
backup policy
restore test
Site Recovery
test failover
```

## Automation

Use:

```text
Git
 ↓
Bicep
 ↓
Azure Resource Manager
```

and safe Azure CLI/PowerShell for operations.

## Deliverables

```text
README.md
HIERARCHY.md
IDENTITY.md
RBAC.md
GOVERNANCE.md
NETWORK.md
COMPUTE.md
CONTAINERS.md
APP_SERVICE.md
STORAGE.md
MONITORING.md
BACKUP_DR.md
COST.md
AUTOMATION.md
RUNBOOKS/
```

Required runbooks:

```text
RUNBOOK_RBAC_DENIED.md
RUNBOOK_STORAGE_403.md
RUNBOOK_VM_UNREACHABLE.md
RUNBOOK_NSG_BLOCK.md
RUNBOOK_PRIVATE_ENDPOINT_DNS.md
RUNBOOK_LOAD_BALANCER_UNHEALTHY.md
RUNBOOK_APP_SERVICE_FAILURE.md
RUNBOOK_BACKUP_FAILURE.md
RUNBOOK_REGION_FAILOVER.md
RUNBOOK_COST_SPIKE.md
```

---

## 7. Recommended Resources

This Markdown is designed to be self-contained for study.

For current production behavior, use official Microsoft documentation:

```text
AZ-104 Study Guide
Microsoft Certified: Azure Administrator Associate
Course AZ-104T00-A
Microsoft Entra ID
Azure RBAC
Azure Policy
Azure Storage
Azure Virtual Machines
Azure Container Apps
Azure App Service
Azure Virtual Network
Azure Bastion
Azure DNS
Azure Load Balancer
Azure Monitor
Network Watcher
Azure Backup
Azure Site Recovery
Bicep
```

---

## 8. Certification Relevance

Direct certification:

```text
Microsoft Certified: Azure Administrator Associate
Exam AZ-104
```

Current Microsoft skills measured as of April 17, 2026:

```text
Manage Azure identities and governance          20–25%
Implement and manage storage                    15–20%
Deploy and manage Azure compute resources       20–25%
Implement and manage virtual networking         15–20%
Monitor and maintain Azure resources            10–15%
```

Current certification page states:

```text
100 minutes exam duration
700+ passing score
12-month renewal frequency
```

This course prepares for later work in:

```text
Azure architecture
Azure networking
Azure security
Terraform
DevOps
Cloud Security
Hybrid Cloud
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Assign Owner everywhere.  
  **Best practice:** least privilege and group-based RBAC.

- **Mistake:** Confuse control-plane Contributor with storage data access.  
  **Best practice:** use data-plane roles where required.

- **Mistake:** Put all resources in one resource group without lifecycle logic.  
  **Best practice:** group by ownership/lifecycle/deployment.

- **Mistake:** Use account storage keys in applications.  
  **Best practice:** managed identity + RBAC where possible.

- **Mistake:** Long-lived SAS with broad permissions.  
  **Best practice:** short expiry and minimal scope.

- **Mistake:** Public storage by default.  
  **Best practice:** network restrictions/private endpoints for sensitive workloads.

- **Mistake:** One VM for production availability.  
  **Best practice:** zones/VMSS/load balancing.

- **Mistake:** Put secrets into Bicep or CLI history.  
  **Best practice:** Key Vault/secure deployment parameters and workload identities.

- **Mistake:** Public SSH/RDP to every VM.  
  **Best practice:** Bastion/controlled private access.

- **Mistake:** NSG rules using broad `Any` everywhere.  
  **Best practice:** ASG/service-specific least privilege.

- **Mistake:** Private endpoint without private DNS.  
  **Best practice:** design endpoint and DNS together.

- **Mistake:** Configure alert without action/runbook owner.  
  **Best practice:** every production alert must be actionable.

- **Mistake:** Backup configured but never restored.  
  **Best practice:** scheduled restore tests and measured RTO.

- **Mistake:** Manual portal changes outside IaC.  
  **Best practice:** Bicep/ARM and controlled operational commands.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Current Azure Administrator exam?

**Answer:** AZ-104.

### Q2. Current skills baseline date?

**Answer:** April 17, 2026.

### Q3. Current exam time?

**Answer:** 100 minutes.

### Q4. Passing score?

**Answer:** 700 or greater.

### Q5. Renewal frequency?

**Answer:** 12 months.

### Q6. Azure scope hierarchy?

**Answer:** Management group → subscription → resource group → resource.

### Q7. RBAC components?

**Answer:** Principal, role definition, scope, role assignment.

### Q8. Contributor vs Owner?

**Answer:** Contributor manages resources; Owner also has broad access-delegation capability.

### Q9. Policy vs RBAC?

**Answer:** RBAC controls who can perform actions; Policy controls allowed/required resource configuration.

### Q10. Resource lock?

**Answer:** Additional protection against deletion or modification.

### Q11. SAS?

**Answer:** Delegated time/permission-scoped access to Azure Storage.

### Q12. ZRS?

**Answer:** Storage redundancy across availability zones in a Region.

### Q13. GRS?

**Answer:** Geo-redundant storage with asynchronous copy to a secondary Region.

### Q14. Blob versioning?

**Answer:** Keeps previous object versions after changes.

### Q15. Bicep?

**Answer:** Azure-native declarative IaC language for ARM resources.

### Q16. VMSS?

**Answer:** Azure Virtual Machine Scale Sets for managed VM fleets and scaling.

### Q17. ACR?

**Answer:** Azure Container Registry.

### Q18. Container Apps?

**Answer:** Managed container application platform with revisions, ingress, and autoscaling.

### Q19. App Service?

**Answer:** Azure PaaS for web applications/APIs.

### Q20. VNet?

**Answer:** Azure regional virtual network.

### Q21. NSG?

**Answer:** Stateful network security rules for subnet/NIC.

### Q22. ASG?

**Answer:** Application Security Group for grouping VM NICs in NSG policies.

### Q23. Service Endpoint vs Private Endpoint?

**Answer:** Service endpoint extends VNet identity to service public endpoint; private endpoint gives the service a private IP in the VNet.

### Q24. Azure Bastion?

**Answer:** Managed private SSH/RDP access without requiring VM public IP.

### Q25. Azure Load Balancer?

**Answer:** Layer-4 TCP/UDP load balancing.

### Q26. Network Watcher?

**Answer:** Azure network monitoring/troubleshooting toolkit.

### Q27. Azure Monitor?

**Answer:** Central platform for metrics, logs, alerts, insights, and observability.

### Q28. Log Analytics?

**Answer:** Azure Monitor Logs workspace/query platform.

### Q29. KQL?

**Answer:** Kusto Query Language used to query Azure Monitor Logs and other Azure data services.

### Q30. Recovery Services Vault?

**Answer:** Vault used by supported Azure Backup and Site Recovery workloads.

### Q31. Azure Site Recovery?

**Answer:** Workload replication and disaster-recovery failover service.

### Q32. Core Azure administrator operating model?

**Answer:** Identity → governance → network → compute/storage → monitoring → backup/recovery → automation → troubleshooting.

---

# Expanded Self-Assessment Bank — Microsoft Azure Administration

### Q1. What is the main engineering lesson from **Context Safety and Subscription Selection**?

**Answer:** Fail closed when the expected tenant/subscription does not match.

### Q2. What is the main engineering lesson from **Management Group Governance**?

**Answer:** Keep the management-group hierarchy shallow, stable, and policy-oriented.

### Q3. What is the main engineering lesson from **RBAC Effective Access**?

**Answer:** Use groups and the lowest practical scope; do not grant Owner to troubleshoot.

### Q4. What is the main engineering lesson from **Control Plane vs Data Plane Authorization**?

**Answer:** Troubleshoot management authorization and data authorization separately.

### Q5. What is the main engineering lesson from **Privileged Access / Just-in-Time Administration**?

**Answer:** Use time-bound privileged elevation and a separate break-glass path.

### Q6. What is the main engineering lesson from **Managed Identity Lifecycle**?

**Answer:** Prefer managed identities and avoid sharing one identity across unrelated applications.

### Q7. What is the main engineering lesson from **Federated Credentials for CI/CD**?

**Answer:** Use separate federation trust per environment/repository boundary.

### Q8. What is the main engineering lesson from **Azure Policy Effect Selection**?

**Answer:** Roll policy out progressively: observe, test remediation, then enforce.

### Q9. What is the main engineering lesson from **Policy Remediation Identity**?

**Answer:** Grant the policy identity only the permissions required for remediation.

### Q10. What is the main engineering lesson from **Policy Exemptions**?

**Answer:** Treat exemptions as tracked risk, not permanent convenience.

### Q11. What is the main engineering lesson from **Resource Locks vs RBAC**?

**Answer:** Use locks as an extra safety barrier, not as a substitute for least privilege.

### Q12. What is the main engineering lesson from **Azure Resource Graph**?

**Answer:** Use Resource Graph for inventory, drift, exposure, and ownership investigations.

### Q13. What is the main engineering lesson from **Activity Log Investigation**?

**Answer:** Check Activity Log early when configuration changed unexpectedly.

### Q14. What is the main engineering lesson from **Bicep What-If**?

**Answer:** Require What-If review for production Bicep changes.

### Q15. What is the main engineering lesson from **Infrastructure Ownership and Drift**?

**Answer:** Give every production resource one authoritative writer.

### Q16. What is the main engineering lesson from **Storage Network Access**?

**Answer:** Troubleshoot Storage identity and network restrictions independently.

### Q17. What is the main engineering lesson from **User Delegation SAS**?

**Answer:** Use the shortest practical SAS lifetime and narrowest resource scope.

### Q18. What is the main engineering lesson from **Storage Redundancy vs RPO**?

**Answer:** Do not derive business RPO from the redundancy acronym alone.

### Q19. What is the main engineering lesson from **Blob Versioning, Soft Delete, and Immutability**?

**Answer:** Layer recovery controls according to threat model and compliance requirements.

### Q20. What is the main engineering lesson from **Private Endpoint DNS**?

**Answer:** Design private endpoint and DNS together.

### Q21. What is the main engineering lesson from **Azure Private DNS Resolver**?

**Answer:** Document DNS authority and forwarding paths like IP routes.

### Q22. What is the main engineering lesson from **NAT Gateway**?

**Answer:** Use subnet-level NAT rather than widespread VM public IPs where appropriate.

### Q23. What is the main engineering lesson from **Azure Firewall vs NSG**?

**Answer:** Do not replace all workload segmentation with one central firewall.

### Q24. What is the main engineering lesson from **Firewall Policy Governance**?

**Answer:** Reserve priority bands and require rule ownership.

### Q25. What is the main engineering lesson from **User-Defined Routes / Forced Tunneling**?

**Answer:** Verify both forward and return paths before forcing traffic through stateful appliances.

### Q26. What is the main engineering lesson from **VNet Peering and Transit**?

**Answer:** Document which networks may transit the hub and which remain isolated.

### Q27. What is the main engineering lesson from **Azure Virtual WAN**?

**Answer:** Consider Virtual WAN when connectivity becomes an enterprise network problem.

### Q28. What is the main engineering lesson from **ExpressRoute Resilience**?

**Answer:** Test hybrid failover instead of assuming circuit redundancy.

### Q29. What is the main engineering lesson from **Network Watcher Connectivity Tests**?

**Answer:** Use network diagnostics before changing NSGs or routes.

### Q30. What is the main engineering lesson from **Azure Bastion**?

**Answer:** Treat administration as a dedicated access plane.

### Q31. What is the main engineering lesson from **DDoS + WAF + Network Segmentation**?

**Answer:** Use layered controls instead of expecting one service to solve every attack.

### Q32. What is the main engineering lesson from **Front Door vs Application Gateway**?

**Answer:** Choose global and regional ingress tiers from placement requirements, not product familiarity.

### Q33. What is the main engineering lesson from **Application Gateway Backend Health**?

**Answer:** Use explicit readiness probes and inspect backend health before changing routing.

### Q34. What is the main engineering lesson from **Azure Load Balancer Probe Quality**?

**Answer:** Design meaningful health endpoints instead of testing only port openness.

### Q35. What is the main engineering lesson from **VM Boot Diagnostics**?

**Answer:** Separate boot problems from NSG/routing problems before remediation.

### Q36. What is the main engineering lesson from **Azure Compute Gallery**?

**Answer:** Treat images as versioned artifacts with provenance.

### Q37. What is the main engineering lesson from **VMSS Upgrade Safety**?

**Answer:** Use progressive VMSS upgrades gated by application health.

### Q38. What is the main engineering lesson from **Patch Rings / Azure Update Management**?

**Answer:** Pair automated patching with staged rollout and image-based recovery.

### Q39. What is the main engineering lesson from **Managed Disk Performance**?

**Answer:** Evaluate disk and VM limits together before buying more IOPS.

### Q40. What is the main engineering lesson from **Customer-Managed Key Availability**?

**Answer:** Treat encryption keys as availability dependencies and test recovery.

### Q41. What is the main engineering lesson from **ACR Identity and Image Pull**?

**Answer:** Separate CI push permissions from runtime pull permissions.

### Q42. What is the main engineering lesson from **Immutable Container Artifact Promotion**?

**Answer:** Promote immutable digests/releases and retain rollback artifacts.

### Q43. What is the main engineering lesson from **Container Apps Revision Traffic**?

**Answer:** Define canary success and rollback thresholds before shifting traffic.

### Q44. What is the main engineering lesson from **Event-Driven Container Apps Scaling**?

**Answer:** Scale async workers from backlog/latency signals.

### Q45. What is the main engineering lesson from **App Service Deployment Slots**?

**Answer:** Inventory sticky settings and schema compatibility before swaps.

### Q46. What is the main engineering lesson from **App Service VNet Integration vs Private Endpoint**?

**Answer:** Identify traffic direction before choosing App Service networking features.

### Q47. What is the main engineering lesson from **App Service Stateless Scale-Out**?

**Answer:** Externalize durable state before enabling aggressive scale-out.

### Q48. What is the main engineering lesson from **Azure Monitor Metrics vs Logs**?

**Answer:** Alert from stable metrics and investigate using richer logs/traces.

### Q49. What is the main engineering lesson from **Data Collection Rules**?

**Answer:** Version DCRs and deploy them as code.

### Q50. What is the main engineering lesson from **KQL Incident Queries**?

**Answer:** Maintain reusable KQL snippets for common operational questions.

### Q51. What is the main engineering lesson from **Actionable Alerts**?

**Answer:** Page only when timely human action is required.

### Q52. What is the main engineering lesson from **Diagnostic Settings Coverage**?

**Answer:** Deploy diagnostic settings by Policy/IaC, not manually after incidents.

### Q53. What is the main engineering lesson from **Backup Security and Restore Testing**?

**Answer:** Measure restore success and actual restore time as operational KPIs.

### Q54. What is the main engineering lesson from **RPO from Protection Frequency**?

**Answer:** Derive protection design from RPO, not from default backup schedules.

### Q55. What is the main engineering lesson from **Azure Site Recovery Test Failover**?

**Answer:** Test DR regularly and measure end-to-end RTO.

### Q56. What is the main engineering lesson from **Failback**?

**Answer:** Document and test failback separately from failover.

### Q57. What is the main engineering lesson from **Key Vault Soft Delete and Purge Protection**?

**Answer:** Protect purge operations more strongly than normal secret usage.

### Q58. What is the main engineering lesson from **Defender for Cloud Triage**?

**Answer:** Prioritize security findings using real asset context.

### Q59. What is the main engineering lesson from **Azure Arc Hybrid Administration**?

**Answer:** Use Arc to centralize governance without pretending every platform is identical.

### Q60. What is the main engineering lesson from **FinOps Tagging and Unit Cost**?

**Answer:** Track both ownership tags and business-aligned unit cost.

### Q61. What is the main engineering lesson from **Quota as Reliability Dependency**?

**Answer:** Review quota headroom before a traffic surge or regional failover.

### Q62. What is the main engineering lesson from **SLO and Error Budget**?

**Answer:** Use SLOs to connect architecture, alerting, and release risk.

### Q63. What is the main engineering lesson from **Change Evidence Chain**?

**Answer:** Link source commit, deployment identity, and runtime evidence.

### Q64. What is the main engineering lesson from **Operational Readiness Review**?

**Answer:** Make operational readiness a launch gate.

### Q65. What is the main engineering lesson from **Evidence-First Troubleshooting**?

**Answer:** Change one layer at a time and preserve the evidence that justified the change.

## Completion Checklist

- [ ] I understand the current AZ-104 domains.
- [ ] I can manage Entra users/groups/external identities.
- [ ] I understand SSPR and identity administration.
- [ ] I can manage Azure RBAC.
- [ ] I understand management groups/subscriptions/resource groups.
- [ ] I can implement Policy/locks/tags.
- [ ] I understand budgets and Advisor.
- [ ] I can create/manage Storage accounts.
- [ ] I understand SAS/access keys/RBAC.
- [ ] I understand Blob/Files lifecycle and protection.
- [ ] I can use AzCopy and Storage Explorer.
- [ ] I understand ARM/Bicep.
- [ ] I can create/configure Azure VMs.
- [ ] I understand disks/encryption/availability.
- [ ] I understand VMSS.
- [ ] I understand ACR/ACI/Container Apps.
- [ ] I understand App Service.
- [ ] I can configure VNet/subnet/peering/routes.
- [ ] I understand NSG/ASG.
- [ ] I understand Bastion/service/private endpoints.
- [ ] I understand Azure DNS.
- [ ] I can configure/troubleshoot Load Balancer.
- [ ] I understand Azure Monitor/Log Analytics/KQL.
- [ ] I understand alerts/action groups.
- [ ] I understand Network Watcher.
- [ ] I understand Azure Backup.
- [ ] I understand Site Recovery.
- [ ] I can use Azure CLI and PowerShell safely.
- [ ] I completed all 36 labs.
- [ ] I completed the Azure Enterprise Administration Platform project.
