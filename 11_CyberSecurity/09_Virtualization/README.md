# Phase 9 — Virtualization

Phase 9 turns the physical infrastructure from Phase 8 into a software-defined compute, network, storage, private-cloud, and multicloud platform.

The phase progresses in this order:

```text
38. Virtualization Fundamentals
        ↓
39. VMware vSphere: Install, Configure and Manage
        ↓
40. VMware NSX
        ↓
41. OpenStack Fundamentals
        ↓
42. OpenStack Deployment and Operation
        ↓
43. OpenStack APIs
        ↓
44. Nutanix Multicloud Infrastructure
```

The learning logic is:

```text
Understand Virtualization
        ↓
Operate an Enterprise Hypervisor Platform
        ↓
Virtualize Networking and Security
        ↓
Understand an Open Private Cloud
        ↓
Deploy and Operate that Cloud
        ↓
Automate it through APIs
        ↓
Compare/Operate an Integrated HCI Multicloud Platform
```

This phase is intentionally practical.

The course files contain:

```text
ASCII architecture diagrams
Linux/KVM commands
ESXCLI
VCF PowerCLI
NSX packet walks
OpenStack CLI
Kolla Ansible
OpenStack REST APIs
Python/openstacksdk
Nutanix aCLI/nCLI
NCC
capacity calculations
failure-domain analysis
troubleshooting workflows
hands-on labs
mini projects
```

The objective is that you can learn the core material directly from the Markdown files without depending on another tutorial.

---

# Phase Goal

By the end of Phase 9 you should be able to trace a workload from application to physical infrastructure:

```text
Application
    ↓
Guest OS
    ↓
Virtual CPU / RAM / Disk / NIC
    ↓
Hypervisor
    ↓
Virtual Network
    ↓
Distributed / Shared Storage
    ↓
Physical Host
    ↓
Physical Network / Storage
```

and then reason about the higher control layers:

```text
vCenter / Prism / OpenStack Control Plane
             |
             v
        Cluster Policy
             |
      +------+------+
      |             |
     HA            DRS
      |             |
      +------+------+
             |
         Workloads
```

You should also be able to answer:

```text
Where is the VM running?
Where is its storage?
Which network carries its traffic?
What happens if the host fails?
What happens if a datastore fails?
What happens if the management plane fails?
Can the workload migrate?
Can it restart automatically?
How is East-West traffic secured?
How is the cloud automated?
What state is stored in the control plane?
How do we recover the platform?
```

---

# 38. Virtualization Fundamentals

**File:** `38_Virtualization_Fundamentals.md`

This course builds the conceptual base.

Core architecture:

```text
Application
    ↓
Guest OS
    ↓
Virtual Hardware
    ↓
Hypervisor
    ↓
Physical Hardware
```

Main topics:

```text
Physical vs Virtual Servers
Type 1 vs Type 2 Hypervisors
Full Virtualization
Hardware-Assisted Virtualization
Intel VT-x / AMD-V
Paravirtualization
Emulation

vCPU
CPU Scheduling
CPU Overcommit
Reservations
Limits
Shares
NUMA / vNUMA

vRAM
Memory Overcommit
Ballooning
Guest Paging
Hypervisor Swapping

Virtual Disks
VMDK / VHDX / QCOW2 / RAW
Thin / Thick Provisioning
Datastores
SAN / NAS / HCI

Snapshots
Clones
Templates
Golden Images

vNIC
Virtual Switch
VLAN
Bridge
Bond / Team

KVM
QEMU
libvirt
virsh
virt-install

Live Migration
Storage Migration

Clusters
HA
Fault Tolerance
Admission Control
N+1
Affinity / Anti-Affinity
Resource Pools

PCI Passthrough
SR-IOV
GPU Virtualization
Nested Virtualization

VMs vs Containers

Virtualization Security
Monitoring
Capacity
Troubleshooting
```

Practical tools include:

```bash
lscpu
lsmod
qemu-img
virsh
virt-install
ip
iostat
```

### Course Project

**Small Enterprise Virtualization Platform**

You design:

```text
hosts
VM standards
shared storage
virtual networks
HA
N+1
security
backup
monitoring
runbooks
```

---

# 39. VMware vSphere: Install, Configure and Manage

**File:** `39_VMware_vSphere_Install_Configure_and_Manage.md`

Reference baseline:

```text
VMware vSphere 9.1
```

This course maps virtualization fundamentals to VMware.

Architecture:

```text
                     vCenter
                        |
              +---------+---------+
              |         |         |
            ESX01     ESX02     ESX03
              |         |         |
             VMs       VMs       VMs
              \         |         /
               +---- Datastores --+
```

Main topics:

```text
ESX / ESXi
vCenter
vSphere Client
Host Client
DCUI

Installation Planning
DNS
NTP
Hardware Compatibility
UEFI / Secure Boot / TPM

Management Network
VMkernel Adapters
ESXCLI
vmkping

vCenter Appliance
Two-Stage Deployment
SSO

Data Centers
Folders
Clusters
Hosts
Maintenance Mode

vSphere Standard Switch
Distributed Switch
Port Groups
VLAN
MTU
NIC Teaming
NIOC

VMFS
NFS
Fibre Channel
iSCSI
Multipathing
APD / PDL
vVols
SPBM

VM Hardware
VMware Tools
VMXNET3
PVSCSI
Virtual NVMe
Thin / Thick Disks

Snapshots
Templates
Clones
Content Library

vMotion
Storage vMotion
EVC

HA
Admission Control
Isolation
Restart Priority
Fault Tolerance

DRS
Affinity / Anti-Affinity

SSO
RBAC
VMCA
Certificates
Lockdown
Host Security

Host Profiles
Lifecycle Manager

Performance
Tasks
Events
Alarms
esxtop

VCF PowerCLI
Troubleshooting
```

Practical examples:

```bash
esxcli system version get
esxcli network nic list
esxcli storage filesystem list
esxcli storage core path list
vmkping
esxtop
```

PowerShell:

```powershell
Install-Module VCF.PowerCLI

Connect-VIServer vc01.lab.example

Get-VMHost
Get-Cluster
Get-VM
Get-Datastore
```

### Course Project

**Production-Style vSphere Cluster**

---

# 40. VMware NSX

**File:** `40_VMware_NSX.md`

Reference baseline:

```text
VMware NSX 9.1
VMware Cloud Foundation 9.1 family
```

NSX moves networking/security into software.

Architecture:

```text
VM
 |
Logical Segment
 |
Distributed Firewall
 |
Distributed Router
 |
GENEVE Overlay
 |
TEP
 |
Physical IP Underlay
```

Main topics:

```text
Underlay vs Overlay
Management / Control / Data Planes
NSX Manager
Manager Cluster

Transport Nodes
Host Transport Nodes
Edge Transport Nodes
Edge Cluster

Transport Zones
TEPs
GENEVE
MTU

Segments
Overlay Segments
VLAN Segments

Distributed Routing
Tier-0
Tier-1
Service Router
Distributed Router

BGP
ECMP
Static Routes
Route Advertisement

NAT
DHCP
DNS Forwarding

Distributed Firewall
Gateway Firewall
Microsegmentation
Dynamic Groups
Tags
Default Deny
Ring Fencing

Projects
VPC
Multi-Tenancy

VPN
Federation
Global Manager

Kubernetes / Antrea Concepts

NSX Policy API
REST
Infrastructure as Code

Traceflow
Realized State
Monitoring
Troubleshooting
```

Important packet walk:

```text
WEB
 ↓
DFW
 ↓
Tier-1 Distributed Routing
 ↓
APP
 ↓
DFW
 ↓
DB
```

North-South:

```text
VM
 ↓
Tier-1
 ↓
Tier-0
 ↓
Edge
 ↓
BGP / NAT / Gateway Firewall
 ↓
Physical Network
```

### Course Project

**NSX Micro-Segmented Enterprise Network**

---

# 41. OpenStack Fundamentals

**File:** `41_OpenStack_Fundamentals.md`

Reference baseline:

```text
OpenStack 2026.1 — Gazpacho
```

OpenStack introduces a full private-cloud control plane.

Architecture:

```text
                    API / Horizon / CLI
                           |
                        Keystone
                           |
       +-------------------+-------------------+
       |                   |                   |
      Nova              Neutron             Cinder
    Compute             Network             Volumes
       |                   |                   |
   Placement             Ports              Backends
   Scheduler             Routers
       |
  nova-compute
       |
     libvirt
       |
      KVM

Glance     → Images
Swift      → Object Storage
Heat       → Orchestration
Octavia    → Load Balancing
Barbican   → Secrets
Manila     → Shared Filesystems
Ironic     → Bare Metal
Designate  → DNS
```

Main topics:

```text
OpenStack Architecture
Control Plane / Data Plane

Keystone
Domains
Projects
Users
Roles
Tokens
Service Catalog
Application Credentials

Nova
Placement
Scheduler
Cells
KVM / libvirt
Flavors
Instances

Glance
Images

Neutron
Networks
Subnets
Ports
Routers
Floating IPs
Security Groups
Provider Networks
Self-Service Networks
OVS / OVN

Cinder
Volumes
Snapshots
Backups

Swift
Object Storage

Horizon
Heat
Octavia
Barbican
Manila
Ironic
Designate

Multi-Tenancy
Quotas
HA
Security
Operations
Troubleshooting
```

### Course Project

**OpenStack Private Cloud Architecture**

---

# 42. OpenStack Deployment and Operation

**File:** `42_OpenStack_Deployment_and_Operation.md`

This course turns OpenStack concepts into operational deployment.

Primary deployment framework:

```text
Kolla Ansible
```

Architecture:

```text
Deployment Node
      |
   Ansible
      |
+-----+-----------------------------+
|                                   |
Controllers                       Computes
|                                   |
APIs                              nova-compute
HAProxy                           libvirt
MariaDB                           KVM
RabbitMQ                          OVN/OVS
|
Storage / External Services
```

Main topics:

```text
All-in-One vs Multinode

Controller
Compute
Network
Storage
Deployment Node

Management Network
Overlay Network
Storage Network
Provider Network

DNS / NTP / MTU / VLAN

Kolla
Kolla Ansible
Inventory
globals.yml
passwords.yml
globals.d

kolla-genpwd
install-deps
bootstrap-servers
prechecks
pull
deploy
post-deploy

clouds.yaml
OpenStackClient

Keystone Validation
Glance Validation
Nova Validation
Placement
Neutron
Cinder

HAProxy
Keepalived
MariaDB / Galera
RabbitMQ

Nova Cells v2
Compute Maintenance
Live Migration
Evacuation
Host Aggregates
Availability Zones
Quotas

OVN / OVS
Port Binding
Provider Networks
Floating IPs

Ceph
Glance
Cinder
Horizon
Heat
Octavia
Barbican
Manila
Designate
Ironic

docker
Kolla Logs

reconfigure
genconfig
validate-config
deploy-containers

Updates
Upgrades
SLURP
Backup / DR

Monitoring
Request IDs
Troubleshooting
```

Important deployment sequence:

```bash
kolla-ansible install-deps

kolla-genpwd

kolla-ansible bootstrap-servers -i ./multinode

kolla-ansible prechecks -i ./multinode

kolla-ansible pull -i ./multinode

kolla-ansible deploy -i ./multinode

kolla-ansible post-deploy -i ./multinode
```

### Course Project

**Production-Style OpenStack Private Cloud**

---

# 43. OpenStack APIs

**File:** `43_OpenStack_APIs.md`

OpenStack is API-first.

Authentication architecture:

```text
Credentials
   ↓
Keystone
   ↓
Token
   ↓
Service Catalog
   ↓
Service Endpoint
   ↓
Nova / Neutron / Cinder / Glance / ...
```

Main topics:

```text
HTTP
REST
JSON

Keystone v3
POST /v3/auth/tokens
X-Subject-Token
X-Auth-Token

Project / Domain / System Scope
Application Credentials

Service Catalog
Regions
Public / Internal / Admin Endpoints

Major API Versions
Microversions
Nova Microversions
Cinder Microversions

Request IDs

HTTP:
200
201
202
204
400
401
403
404
409
413
429
500
503

Timeouts
Retries
Backoff
Idempotency
Polling
Pagination

curl
openstack --debug
Python requests
keystoneauth
openstacksdk

Nova API
Neutron API
Cinder API
Glance API
Swift API
Heat API
Octavia API
Barbican API
Manila API
Ironic API
Designate API
Placement API

Reconciliation
Drift Detection
Compensating Actions
Ownership Tags
Concurrency
Rate Limits

API Security
Testing
Multi-Cloud Compatibility
Observability
```

Python model:

```python
import openstack

conn = openstack.connect(cloud="lab")

for server in conn.compute.servers():
    print(server.id, server.name, server.status)
```

### Course Project

**OpenStack Infrastructure Automation Service**

---

# 44. Nutanix Multicloud Infrastructure

**File:** `44_Nutanix_Multicloud_Infrastructure.md`

Reference baseline:

```text
NCI / AOS 7.6
```

Architecture:

```text
                    Prism Central
                         |
             +-----------+-----------+
             |                       |
          Cluster A               Cluster B
             |                       |
       +-----+-----+           +-----+-----+
       |     |     |           |     |     |
      AHV   AHV   AHV         AHV   AHV   AHV
       |     |     |           |     |     |
      CVM   CVM   CVM         CVM   CVM   CVM
        \     |     /           \     |     /
         +--- AOS DSF -----------+---+
```

Main topics:

```text
Hyperconverged Infrastructure
NCI
AOS
AHV

Nodes
Blocks
Clusters
CVMs

Distributed Storage Fabric
Storage Pools
Containers
vDisks

Data Locality
Write / Read Path

RF2
RF3
Self-Healing
Checksums
Compression
Deduplication
Erasure Coding
Tiering

Prism Element
Prism Central
Nutanix Central

Categories
Projects
RBAC

AHV VMs
Images
CPU
Memory
vDisks
vNICs
Nutanix Guest Tools

aCLI
nCLI
cluster status
NCC

AHV Networking
Virtual Switches
Bonds
VLANs

Flow Virtual Networking
VPCs

Flow Network Security
Microsegmentation

AHV HA
Live Migration
Affinity / Anti-Affinity
Dynamic Scheduling

Volume Groups
Storage Policies

Protection Policies
Recovery Points
Async Replication
NearSync
Metro / Synchronous Concepts
Recovery Plans
Failover / Failback

NC2
Hybrid Multicloud

LCM
Rolling Upgrades
Cluster Expansion
Foundation

Encryption
KMS
CVM Security
Security Dashboard

Prism v4 APIs
Service Accounts
Automation

Monitoring
Capacity
Troubleshooting
```

Useful operator commands:

```bash
ssh nutanix@<CVM-IP>

cluster status

ncc health_checks run_all

acli vm.list

acli vm.get <VM_NAME>
```

### Course Project

**Nutanix Hybrid Multicloud Infrastructure**

---

# Recommended Study Sequence

Study the phase in exact dependency order.

## Step 1 — Learn Virtualization as a Technology

Finish Course 38 until you can explain:

```text
hypervisor
vCPU
vRAM
vDisk
vNIC
datastore
virtual switch
snapshot
template
live migration
HA
N+1
```

without referring to one vendor.

## Step 2 — Implement Enterprise Virtualization with VMware

Finish Course 39 until you can build:

```text
ESX hosts
vCenter
cluster
vSwitch/vDS
VMkernel networks
shared storage
HA
DRS
vMotion
lifecycle
```

## Step 3 — Virtualize Network and Security

Finish Course 40 until you can trace:

```text
VM
 ↓
DFW
 ↓
Segment
 ↓
Tier-1
 ↓
Tier-0
 ↓
Edge
 ↓
Physical Router
```

## Step 4 — Learn the OpenStack Cloud Model

Finish Course 41 until you can explain why:

```text
OpenStack
≠
one hypervisor
```

and map:

```text
Nova → Compute
Neutron → Network
Cinder → Block Storage
Glance → Images
Keystone → Identity
```

## Step 5 — Deploy and Operate OpenStack

Finish Course 42 until you can reason through:

```text
Kolla
Controllers
Computes
DB
RabbitMQ
HAProxy
OVN
Cinder/Ceph
```

and recover from common failures.

## Step 6 — Automate OpenStack

Finish Course 43 until you can implement:

```text
Keystone authentication
service discovery
microversions
Nova/Neutron/Cinder APIs
polling
retry
idempotency
secure credentials
```

## Step 7 — Operate Nutanix NCI

Finish Course 44 until you understand:

```text
AHV
AOS
CVM
DSF
Prism
Flow
DR
LCM
NC2
```

and can compare the Nutanix integrated model with VMware and OpenStack.

---

# VMware vs OpenStack vs Nutanix Mental Model

Do not treat these platforms as identical products.

A useful comparison is:

```text
VMware vSphere
    strong enterprise virtualization platform

VMware NSX
    software-defined networking/security

OpenStack
    API-driven private-cloud control plane
    built from multiple open services

Nutanix NCI
    integrated HCI / virtualization / storage /
    operations / multicloud infrastructure platform
```

At a conceptual level:

```text
VMware
ESX + vCenter + NSX

OpenStack
Nova + Neutron + Cinder + Glance + Keystone + ...

Nutanix
AHV + AOS + Prism + Flow + DR + LCM
```

The operational philosophy differs, but the same infrastructure fundamentals still apply:

```text
compute
memory
network
storage
identity
HA
capacity
security
backup
automation
```

---

# Integrated Phase 9 Architecture

```text
                         Management / API
                               |
        +----------------------+----------------------+
        |                      |                      |
      vCenter             OpenStack API          Prism Central
        |                      |                      |
     VMware                 Nova/Neutron              |
      ESX                   Cinder/etc.              AHV
        |                      |                      |
      NSX                    KVM                   AOS DSF
        |                      |                      |
 Virtual Network        Software Network       Flow Network
        |                      |                      |
        +----------------------+----------------------+
                               |
                    Physical Data Center
                               |
                  Compute / Network / Storage
```

---

# Phase 9 Integrated Capstone

Design three versions of the same enterprise infrastructure.

Business workload:

```text
100 VMs
ERP
MES
SQL / Oracle
Active Directory
Web / Application tiers
Dev/Test
Monitoring
Backup
```

## Architecture A — VMware

Use:

```text
vSphere
vCenter
HA
DRS
vMotion
vDS
NSX
shared storage
```

## Architecture B — OpenStack

Use:

```text
KVM
Nova
Placement
Neutron
Cinder
Glance
Keystone
Kolla Ansible
HAProxy
MariaDB
RabbitMQ
```

## Architecture C — Nutanix

Use:

```text
AHV
AOS DSF
Prism Central
Flow
Protection Policies
LCM
NC2 / DR
```

Then compare:

```text
deployment complexity
operations
HA
networking
storage
automation
multi-tenancy
security
DR
lifecycle
skills required
failure domains
```

Do not decide that one platform is universally "best."

Choose based on:

```text
business requirements
existing skills
application needs
integration
cost
scale
operating model
support
```

---

# Phase 9 Troubleshooting Framework

For every virtualization/cloud incident ask:

```text
1. Is the application actually unhealthy?
2. Is the guest OS healthy?
3. Is the VM running?
4. Is CPU/memory constrained?
5. Is virtual networking correct?
6. Is the physical network healthy?
7. Is storage reachable and performant?
8. Is the hypervisor healthy?
9. Is the cluster healthy?
10. Is the management/control plane healthy?
11. Is identity/API authorization correct?
12. Is capacity available?
13. Is HA/DR policy working?
14. What changed recently?
15. What evidence exists?
```

Then trace the platform-specific path.

VMware:

```text
VM
→ ESX
→ vSwitch/vDS
→ datastore
→ cluster
→ vCenter
```

NSX:

```text
VM
→ DFW
→ Segment
→ TEP
→ Tier-1
→ Tier-0
→ Edge
→ physical network
```

OpenStack:

```text
Keystone
→ Nova API
→ Scheduler
→ Placement
→ Neutron
→ Glance/Cinder
→ nova-compute
→ KVM
```

Nutanix:

```text
VM
→ AHV
→ CVM
→ AOS DSF
→ physical node
→ Prism
```

---

# Phase 9 Completion Checklist

## Virtualization Fundamentals

- [ ] I understand Type 1/Type 2 hypervisors.
- [ ] I understand CPU/memory virtualization.
- [ ] I understand virtual storage/networking.
- [ ] I understand snapshots/templates/clones.
- [ ] I understand live migration.
- [ ] I understand clusters/HA.
- [ ] I understand N+1.
- [ ] I understand VM security.

## VMware vSphere

- [ ] I understand ESX and vCenter.
- [ ] I can plan/install an ESX host.
- [ ] I understand DCUI and ESXCLI.
- [ ] I understand VMkernel networking.
- [ ] I understand vSS and vDS.
- [ ] I understand VMFS/NFS/iSCSI/FC.
- [ ] I understand vMotion and Storage vMotion.
- [ ] I understand HA/DRS/EVC.
- [ ] I understand Lifecycle Manager.
- [ ] I can use VCF PowerCLI.

## VMware NSX

- [ ] I understand underlay/overlay.
- [ ] I understand TEP/GENEVE.
- [ ] I understand segments.
- [ ] I understand Tier-0/Tier-1.
- [ ] I understand Edge clusters.
- [ ] I understand BGP/ECMP/NAT.
- [ ] I understand DFW and microsegmentation.
- [ ] I understand Flow tracing/realized state.
- [ ] I understand NSX API automation.

## OpenStack

- [ ] I understand Keystone.
- [ ] I understand Nova and Placement.
- [ ] I understand Neutron.
- [ ] I understand Glance and Cinder.
- [ ] I understand Swift.
- [ ] I understand Heat/Octavia/Barbican/Manila/Ironic/Designate.
- [ ] I understand projects/quotas/RBAC.

## OpenStack Operations

- [ ] I understand Kolla/Kolla Ansible.
- [ ] I understand controller/compute roles.
- [ ] I can use bootstrap/prechecks/deploy/post-deploy.
- [ ] I understand HAProxy/Keepalived.
- [ ] I understand MariaDB/RabbitMQ.
- [ ] I understand OVN/OVS.
- [ ] I understand compute maintenance.
- [ ] I understand upgrade/backup/DR.
- [ ] I can troubleshoot core services.

## OpenStack APIs

- [ ] I understand Keystone token flow.
- [ ] I understand service catalogs.
- [ ] I understand API versions/microversions.
- [ ] I understand request IDs.
- [ ] I understand status codes.
- [ ] I understand timeout/retry/idempotency.
- [ ] I can use curl/requests/keystoneauth/openstacksdk.
- [ ] I understand Nova/Neutron/Cinder APIs.
- [ ] I can build secure reconciliation automation.

## Nutanix NCI

- [ ] I understand HCI.
- [ ] I understand AOS vs AHV.
- [ ] I understand CVMs and DSF.
- [ ] I understand RF2/RF3.
- [ ] I understand Prism Element/Central.
- [ ] I understand aCLI/nCLI/NCC.
- [ ] I understand AHV networking/HA/migration.
- [ ] I understand Flow networking/security.
- [ ] I understand categories/projects/RBAC.
- [ ] I understand protection policies/DR.
- [ ] I understand LCM.
- [ ] I understand NC2.
- [ ] I understand API/service-account concepts.
- [ ] I can troubleshoot core NCI failures.

---

# Folder Structure

```text
Phase_9_Virtualization/
│
├── README.md
├── 38_Virtualization_Fundamentals.md
├── 39_VMware_vSphere_Install_Configure_and_Manage.md
├── 40_VMware_NSX.md
├── 41_OpenStack_Fundamentals.md
├── 42_OpenStack_Deployment_and_Operation.md
├── 43_OpenStack_APIs.md
└── 44_Nutanix_Multicloud_Infrastructure.md
```

---

# Next Phase

After Phase 9:

```text
Phase 10 — Git & Configuration Automation

45. Git and Version Control Systems
46. Configuration Management
47. Ansible
```

Dependency:

```text
Operate Infrastructure Manually
        ↓
Version Infrastructure Knowledge
        ↓
Automate Configuration
        ↓
Repeatable Infrastructure Operations
```

Phase 10 is important because later cloud, container, IaC, and DevOps phases assume that infrastructure changes can be reviewed, versioned, and automated rather than performed only through GUIs.
