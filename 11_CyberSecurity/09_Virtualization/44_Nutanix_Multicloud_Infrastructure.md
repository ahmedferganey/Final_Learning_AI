# 44. Nutanix Multicloud Infrastructure

> Phase 9 — Virtualization

This course closes Phase 9 by connecting **virtualization, distributed storage, software-defined networking, operations, lifecycle management, data protection, and hybrid multicloud** into the Nutanix Cloud Infrastructure (NCI) operating model.

**Reference baseline:** Nutanix Cloud Infrastructure **7.6 / AOS 7.6**, released in July 2026.

The current Nutanix Certified Professional – Multicloud Infrastructure certification is **NCP-MCI 7.5**. The concepts taught here remain aligned with the current administration model while using NCI 7.6 as the technical platform baseline.

The central architecture is:

```text
                    Prism Central
                 Global Management
                        |
          +-------------+-------------+
          |                           |
     Nutanix Cluster A            Nutanix Cluster B
          |                           |
  +-------+-------+           +-------+-------+
  |       |       |           |       |       |
Node 1  Node 2  Node 3      Node 1  Node 2  Node 3
  |       |       |           |       |       |
 AHV     AHV     AHV         AHV     AHV     AHV
  |       |       |           |       |       |
 CVM     CVM     CVM         CVM     CVM     CVM
  \       |       /           \       |       /
   +------ AOS DSF ------------+------+
          |
   Distributed Storage
          |
   VMs / Volume Groups
```

A Nutanix node combines:

```text
CPU
RAM
local SSD/NVMe/HDD
network interfaces
hypervisor
Controller VM
```

Multiple nodes form a distributed cluster.

The core mental model is:

```text
AHV
    → Virtualization

AOS / DSF
    → Distributed storage and data services

Prism Element
    → Cluster-local management

Prism Central
    → Multicluster/global management

Flow
    → Networking and microsegmentation

Nutanix DR
    → Protection policies, recovery points and recovery plans

LCM
    → Full-stack lifecycle management

NC2
    → Nutanix operating model in public cloud
```

The course uses this learning pattern:

```text
Concept
   ↓
Architecture Diagram
   ↓
Prism / CLI Example
   ↓
Expected Behavior
   ↓
Failure Scenario
   ↓
Troubleshooting
```

---

## 1. Topic Title

**Nutanix Multicloud Infrastructure**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain hyperconverged infrastructure and why Nutanix uses a distributed architecture.
- Explain NCI, AOS, AHV, DSF, Prism Element, Prism Central, Flow, LCM, DR, and NC2.
- Explain Nutanix node, block, cluster, CVM, hypervisor, disk, storage pool, storage container, and vDisk relationships.
- Explain the Controller VM architecture.
- Explain local data access and distributed resilience.
- Explain RF2 and RF3 conceptually.
- Explain self-healing and re-replication.
- Explain storage containers, capacity optimization, compression, deduplication, erasure coding concepts, and checksums.
- Explain AOS distributed storage I/O paths.
- Explain AHV architecture.
- Create and manage virtual machines in Prism.
- Understand aCLI and nCLI.
- Use `cluster status` and NCC for operational health.
- Explain virtual switches, VLANs, bridges, bonds, and AHV networking.
- Explain Flow Virtual Networking and VPC concepts.
- Explain Flow Network Security and microsegmentation.
- Explain categories, projects, and RBAC.
- Explain Prism Element versus Prism Central.
- Explain Prism Central scale-out concepts.
- Explain alerts, tasks, events, capacity, and performance monitoring.
- Explain VM CPU, memory, disks, NICs, images, clones, snapshots, and guest tools.
- Explain AHV live migration and HA behavior.
- Explain affinity and anti-affinity.
- Explain Acropolis Dynamic Scheduling conceptually.
- Explain volume groups.
- Explain storage policies.
- Explain protection policies, recovery points, replication, and recovery plans.
- Explain asynchronous, near-sync, and synchronous/Metro concepts at a fundamentals level.
- Explain disaster-recovery testing and failover orchestration.
- Explain Nutanix Cloud Clusters (NC2).
- Explain hybrid multicloud management concepts.
- Explain cluster expansion and node maintenance.
- Explain Life Cycle Manager and rolling upgrades.
- Explain Foundation conceptually.
- Explain licensing fundamentals.
- Explain data-at-rest encryption and key-management concepts.
- Explain CVM and management-plane hardening.
- Explain security dashboards and network segmentation.
- Explain Nutanix REST API and current v4 API concepts.
- Explain service accounts/API keys at a fundamentals level.
- Troubleshoot CVM, storage, node, network, VM, Prism, replication, and lifecycle issues.
- Design and operate a production-style Nutanix private/multicloud environment.
- Prepare for the administration domains represented by NCP-MCI.

---

## 3. Prerequisites

Required:

- 38. Virtualization Fundamentals
- 39. VMware vSphere: Install, Configure and Manage
- 40. VMware NSX
- 34. Information Storage and Management
- 35. Data Center Infrastructure Design
- 36. Enterprise Backup and Recovery
- Networking
- Linux administration

Recommended lab:

```text
3-node Nutanix Community Edition / authorized NCI lab
or
Nutanix Test Drive / training environment
```

Conceptual production topology:

```text
Prism Central
     |
+----+----------------------+
|                           |
Cluster-DC1              Cluster-DR
3+ Nodes                 3+ Nodes
AHV                      AHV
```

Suggested networks:

```text
CVM / Host Management
VM Production
Storage / Backplane
Migration
Backup / DR
Flow VPC / Overlay where used
```

Never experiment with destructive cluster or storage commands against production systems.

---

## 4. Core Concepts Explanation

# Part 1 — Why Hyperconverged Infrastructure Exists

Traditional infrastructure separates:

```text
Compute
SAN
Storage Array
Virtualization
Management
```

HCI collapses compute and software-defined storage into clustered nodes.

```text
Node = Compute + Local Storage + Hypervisor + Storage Services
```

Adding nodes can increase both compute and storage resources.

# Part 2 — Nutanix Cloud Infrastructure

NCI is the infrastructure layer of the Nutanix Cloud Platform.

It combines:

```text
virtualization
distributed storage
networking
security
data protection
lifecycle operations
```

for datacenter, edge, and cloud deployments.

# Part 3 — AOS

AOS is the core Nutanix software foundation for storage and infrastructure services.

Think:

```text
AOS
  ↓
Distributed Storage Fabric
  ↓
resilient storage presented to hypervisor/workloads
```

AHV and AOS have different responsibilities.

# Part 4 — AHV

AHV is Nutanix's integrated enterprise hypervisor.

```text
VM
 ↓
AHV
 ↓
physical CPU/RAM/NIC
```

AOS provides the distributed storage underneath the virtual workloads.

# Part 5 — AOS vs AHV

```text
AHV
  runs VMs

AOS
  provides distributed storage/data services
```

AOS can also support qualified non-AHV hypervisors in supported architectures.

# Part 6 — Node

A Nutanix node is one physical server participating in a cluster.

```text
Node
├─ CPU
├─ RAM
├─ NICs
├─ local storage
├─ hypervisor
└─ CVM
```

# Part 7 — Block

A hardware block can contain one or more nodes depending on platform.

Operationally distinguish:

```text
node failure
block/chassis failure
rack failure
```

because they are different failure domains.

# Part 8 — Cluster

Multiple nodes form one Nutanix cluster.

```text
Node1
Node2
Node3
  |
Nutanix Cluster
```

The cluster presents shared infrastructure services despite using distributed local resources.

# Part 9 — Controller VM

Each Nutanix node normally runs a Controller VM (CVM).

```text
Host
 ├─ tenant VMs
 └─ CVM
```

The CVM provides AOS storage/control services and has direct access to storage resources according to platform architecture.

# Part 10 — Why the CVM Matters

The CVM is not an ordinary application VM.

It participates in:

```text
storage I/O
metadata
cluster services
Prism
data protection
health
```

Do not power off or resize CVMs casually.

# Part 11 — Distributed Storage Fabric

DSF aggregates storage resources across cluster nodes into a resilient distributed storage system.

```text
Node1 Disks Node2 Disks  > Distributed Storage Fabric
Node3 Disks /
```

The hypervisor and VMs consume storage without manually managing individual physical disks.

# Part 12 — Shared-Nothing Principle

Each node contributes local resources.

There is no requirement for one traditional dual-controller SAN array to own all VM data.

Resilience is created through software distribution and replication across nodes.

# Part 13 — Storage Pool

A storage pool aggregates physical storage resources.

Concept:

```text
SSD/NVMe/HDD devices
      ↓
Storage Pool
      ↓
Containers
```

Modern deployments typically minimize unnecessary manual pool fragmentation.

# Part 14 — Storage Container

A storage container is a logical storage construct presented for VM/storage consumption.

```text
Storage Pool
   |
   +-- Container-Prod
   +-- Container-Dev
```

Policies and capacity behavior can be applied at logical storage layers.

# Part 15 — vDisk

A VM's virtual disk ultimately maps to distributed AOS storage.

```text
Guest disk
  ↓
AHV virtual disk
  ↓
AOS DSF
  ↓
distributed physical extents
```

# Part 16 — VM Data Path

For a VM running on AHV:

```text
Application
 ↓
Guest filesystem
 ↓
virtual disk
 ↓
AHV
 ↓
local CVM/storage path
 ↓
DSF
 ↓
replicated distributed data
```

The platform optimizes local access while maintaining distributed resilience.

# Part 17 — Data Locality

Nutanix can keep frequently accessed VM data local to the node where the VM runs while maintaining replicated copies elsewhere.

Benefit:

```text
local storage latency
+
cluster resilience
```

After migration, locality can adapt over time.

# Part 18 — Write Path

A write must satisfy resiliency policy before acknowledgement.

Conceptually:

```text
VM write
 ↓
CVM
 ↓
local/primary copy
 +
remote replica
 ↓
acknowledge when required copies safely written
```

# Part 19 — Read Path

Reads prefer efficient/local access where possible.

If a local copy is unavailable:

```text
read from another healthy replica
```

The distributed layer hides many disk/node failures from the guest.

# Part 20 — Replication Factor 2

RF2 maintains two copies of protected data across failure domains.

```text
Copy A → Node1
Copy B → Node2
```

It is designed to tolerate the appropriate single failure while data remains available.

# Part 21 — Replication Factor 3

RF3 maintains three copies.

```text
Copy A
Copy B
Copy C
```

It supports higher resilience but consumes more raw capacity and has cluster-size/design requirements.

# Part 22 — RF Is Not RAID Level

Do not equate:

```text
RF2 = RAID1
RF3 = RAID5
```

Nutanix uses distributed replicas/data services across nodes rather than a traditional local RAID-only model.

# Part 23 — Self-Healing

After a disk/node failure:

```text
detect lost replica
   ↓
identify surviving data
   ↓
re-replicate to healthy resources
   ↓
restore desired protection level
```

This happens as a distributed background process.

# Part 24 — Rebuild vs Re-Replication

Traditional arrays often rebuild a failed drive into one replacement disk.

Distributed systems can rebuild missing data across many healthy resources in parallel.

This changes how recovery performance scales.

# Part 25 — Checksums

AOS uses data-integrity checks to detect silent corruption.

Concept:

```text
write data + checksum
read data
verify checksum
```

If corruption is detected, a healthy replica can be used where possible.

# Part 26 — Compression

Compression reduces physical storage consumption.

```text
logical data
   ↓
compression
   ↓
smaller stored representation
```

Effectiveness depends on workload compressibility.

# Part 27 — Deduplication

Deduplication identifies duplicate data patterns and avoids storing redundant copies when beneficial.

Do not assume every workload gets the same reduction ratio.

# Part 28 — Erasure Coding Concept

Erasure coding can reduce capacity overhead for suitable colder/less frequently changed data compared with full replication.

Tradeoff:

```text
capacity efficiency
vs
compute/reconstruction overhead
```

Use policy/platform guidance rather than enabling blindly.

# Part 29 — Tiering

DSF can place data across storage classes according to access patterns.

Concept:

```text
hot data → faster media
cold data → capacity media
```

Modern all-flash/NVMe platforms may reduce visible tier complexity.

# Part 30 — Storage Capacity

Never calculate usable capacity as:

```text
sum of disk labels only
```

Account for:

```text
RF
metadata
system/CVM needs
snapshots
data reduction
free-space headroom
failures
growth
```

# Part 31 — CVM Resource Reservation

CVMs consume CPU and memory because they provide storage services.

Cluster sizing must include:

```text
tenant workload demand
+
CVM overhead
+
failover headroom
```

# Part 32 — AOS Core Services Concept

AOS consists of distributed services. Historical/common internal process names include storage, metadata, cluster coordination, and background-maintenance components.

Operators should primarily use Prism, NCC, and supported diagnostic tools rather than manually manipulating internal processes.

# Part 33 — Stargate Concept

Stargate is associated with the AOS storage I/O datapath.

Operational implication:

```text
CVM CPU/storage service load
can affect I/O performance
```

Use Prism/NCC metrics before restarting storage services.

# Part 34 — Metadata Services Concept

Distributed metadata tracks where data/resources live across the cluster.

Metadata availability must itself be distributed and resilient.

This is why arbitrary CVM/service manipulation can have cluster-wide effects.

# Part 35 — Curator Concept

Background maintenance services perform tasks such as data balancing, scanning, and optimization.

A busy cluster may show background work after expansion or failure recovery.

Distinguish expected maintenance activity from workload problems.

# Part 36 — Prism Element

Prism Element is cluster-local management.

```text
Browser
  ↓
Prism Element
  ↓
one Nutanix cluster
```

Use it for cluster-local configuration, monitoring, and emergency access.

# Part 37 — Prism Central

Prism Central provides centralized multicluster management.

```text
Prism Central
  |
  +-- Cluster A
  +-- Cluster B
  +-- Cluster C
```

It is the main control plane for many modern NCI workflows.

# Part 38 — Prism Element vs Prism Central

```text
Prism Element
  cluster-local

Prism Central
  multicluster/global services
```

Some modern features are Prism Central only.

# Part 39 — Prism Central Deployment

Prism Central can be deployed as a single VM or a three-VM scale-out architecture according to requirements and current support.

Production design should account for:

```text
VM count
features
availability
capacity
```

# Part 40 — Prism Central Failure

If Prism Central is unavailable:

```text
AHV hosts and VMs continue
cluster storage continues
Prism Element remains important
```

but centralized management and PC-dependent services are impaired.

# Part 41 — Prism Inventory

Prism provides inventory for:

```text
clusters
hosts
VMs
storage
networks
images
protection
alerts
tasks
```

Use consistent naming and ownership.

# Part 42 — Categories

Categories attach logical metadata to entities.

Examples:

```text
App=ERP
Environment=Prod
Tier=Database
Owner=Finance
```

They support policy and automation.

# Part 43 — Dynamic Policy from Categories

A category can drive:

```text
security
protection
governance
automation
```

This is better than tying every policy to IP address or manually selected VM lists.

# Part 44 — Projects

Projects provide controlled multi-user/self-service boundaries around resources.

They can support:

```text
users/groups
quotas
networks
VM resources
governance
```

Modern NCI 7.6 expands project/multitenancy capabilities.

# Part 45 — RBAC

Role-based access controls what administrators/users can do.

Separate:

```text
platform admin
VM operator
storage admin
security admin
auditor
project user
```

Use least privilege.

# Part 46 — AHV VM Architecture

AHV VM:

```text
vCPU
vRAM
vDisks
vNICs
firmware
devices
```

AHV schedules those resources across a physical host while AOS supplies distributed storage.

# Part 47 — Create VM in Prism

Generic workflow:

```text
Create VM
 ↓
name
CPU
memory
disk
network
image/ISO
 ↓
save
 ↓
power on
```

Then install/configure the guest OS.

# Part 48 — Images

Prism Central can manage centralized images.

Examples:

```text
ISO
qcow2/raw-compatible disk image
golden OS image
```

Use versioned, patched, controlled images.

# Part 49 — VM CPU

Assign vCPU based on measured demand.

Oversizing can reduce scheduling flexibility.

Use:

```text
CPU utilization
ready/scheduling indicators
NUMA awareness
application behavior
```

# Part 50 — VM Memory

Monitor:

```text
configured
used
reclaimed/swapped
host pressure
```

NCI 7.6 adds richer AHV infrastructure metrics for memory visibility.

# Part 51 — VM Disk

A VM disk resides on an AOS storage container.

You can manage:

```text
size
container/policy
bus/controller
clone/snapshot relationships
```

# Part 52 — VM NIC

A virtual NIC connects to an AHV network/virtual switch construct.

```text
VM vNIC
 ↓
AHV virtual switch
 ↓
physical uplinks
```

# Part 53 — Guest Tools

Nutanix Guest Tools can provide guest integration for supported workflows such as:

```text
guest operations
application-consistent protection
self-service restore/features
```

Keep guest tooling lifecycle controlled.

# Part 54 — aCLI

Acropolis CLI manages AHV/Acropolis resources.

Access from a CVM:

```bash
ssh nutanix@<CVM-IP>
acli
```

Then use tab completion and the installed command reference.

# Part 55 — aCLI VM Listing

Typical read-only inventory workflow:

```bash
acli vm.list
```

Inspect a VM:

```bash
acli vm.get <VM_NAME>
```

Use read commands first during troubleshooting.

# Part 56 — nCLI

nCLI manages Nutanix cluster/storage/configuration resources.

Conceptual examples include:

```bash
ncli cluster info
ncli host list
ncli container list
```

Exact syntax should always match the installed AOS release.

# Part 57 — `cluster status`

On a CVM:

```bash
cluster status
```

This gives a quick view of cluster service health across CVMs.

Use it as evidence, not an invitation to restart services.

# Part 58 — NCC

Nutanix Cluster Check validates health and recommended configuration.

Full check:

```bash
ncc health_checks run_all
```

Run before and after significant maintenance where appropriate.

# Part 59 — NCC Interpretation

NCC output includes:

```text
PASS
WARN
FAIL
INFO
```

Do not blindly "fix" every warning without reading the specific check's guidance and scope.

# Part 60 — AHV Host Networking

AHV uses Linux/OVS-based networking constructs under the platform.

Concept:

```text
VM
 ↓
virtual switch
 ↓
bond/uplinks
 ↓
physical switch
```

Prism should be the normal configuration path.

# Part 61 — Virtual Switch

A Nutanix virtual switch provides logical switching for VM and host traffic.

NCI supports standard network use and more advanced multicluster/VPC workflows.

# Part 62 — Uplinks and Bonds

Multiple physical NICs provide redundancy and bandwidth.

```text
NIC1       bond / virtual switch
NIC2 /
```

Physical-switch LACP/VLAN configuration must match the chosen mode.

# Part 63 — VLAN Network

Typical VM network:

```text
Network: PROD-WEB
VLAN: 100
```

The physical switch trunk must carry VLAN 100 to the AHV hosts.

# Part 64 — AHV Network Failure Path

Trace:

```text
guest IP
 ↓
vNIC
 ↓
AHV network/VLAN
 ↓
virtual switch
 ↓
bond
 ↓
physical NIC
 ↓
ToR switch
 ↓
routing/firewall
```

# Part 65 — Flow Virtual Networking

Flow Virtual Networking provides software-defined networking capabilities such as VPCs and overlay-style logical networks.

```text
VPC
 ├─ Subnet A
 ├─ Subnet B
 └─ routing/services
```

It brings cloud-like network constructs to NCI.

# Part 66 — VPC

A VPC provides an isolated logical networking boundary.

```text
VPC-Prod
  |
  +-- Web subnet
  +-- App subnet
  +-- DB subnet
```

This supports tenant/application isolation beyond basic VLAN-only design.

# Part 67 — Flow Network Security

Flow Network Security provides policy-based microsegmentation integrated with AHV and Prism Central.

```text
VM
 ↓
distributed policy
 ↓
allowed/blocked workload traffic
```

# Part 68 — Microsegmentation

Instead of trusting an entire VLAN:

```text
WEB → APP TCP/8443
APP → DB TCP/5432
everything else denied
```

Policy can use categories rather than only IP addresses.

# Part 69 — Security Categories

Example:

```text
App=ERP
Tier=Web

App=ERP
Tier=DB
```

Flow policy can automatically apply when new VMs receive matching categories.

# Part 70 — Network Security Troubleshooting

If a flow fails:

```text
category membership
policy/rule
source
destination
service
network/VLAN/VPC
guest firewall
```

Do not immediately disable all security.

# Part 71 — AHV High Availability

If an AHV host fails:

```text
host failure detected
   ↓
VMs restarted on healthy hosts
```

This is restart-based availability, so guest/application boot time contributes to RTO.

# Part 72 — HA Capacity

HA needs spare resources.

If all hosts run at near 100%:

```text
host fails
→ no place for restarted VMs
```

Design N+1 or stronger capacity according to business requirements.

# Part 73 — Live Migration

AHV can live migrate supported running VMs between hosts.

```text
Host A
 VM running
   ↓
memory/state transfer
   ↓
Host B
```

Storage remains available through the distributed fabric.

# Part 74 — Migration Requirements

Check:

```text
target capacity
CPU compatibility
network availability
device/passthrough constraints
host health
```

Special hardware devices can restrict mobility.

# Part 75 — Affinity

Affinity keeps a VM associated with selected hosts according to policy.

Use cases:

```text
licensing
hardware dependency
locality requirements
```

Hard constraints reduce HA flexibility.

# Part 76 — Anti-Affinity

Anti-affinity separates redundant VMs.

Example:

```text
DC01 ≠ same host as DC02
```

Use for clustered application components.

# Part 77 — Acropolis Dynamic Scheduling

ADS monitors resource contention and can rebalance VM/resource placement according to platform capabilities.

Concept:

```text
detect hotspot
   ↓
evaluate alternatives
   ↓
migrate/rebalance
```

# Part 78 — Host Maintenance

Before maintenance:

```text
run health checks
verify resilience/capacity
enter maintenance workflow
migrate VMs
service node
return node
validate cluster
```

Do not power off an arbitrary host without cluster preparation.

# Part 79 — CVM Maintenance

CVM maintenance is platform-controlled.

AOS rolling operations temporarily redirect storage responsibilities while maintaining service.

Never manually shut down multiple CVMs simultaneously.

# Part 80 — Cluster Expansion

Scale-out:

```text
existing cluster
   +
new node(s)
   ↓
discovery/configuration
   ↓
storage/compute resources expand
```

Prism Central/Element can guide supported expansion workflows.

# Part 81 — Expansion Validation

Before adding nodes check:

```text
hardware compatibility
AOS/AHV version
network/VLAN
IP addressing
rack power
firmware
cluster limits
```

After expansion, run NCC and review rebalance activity.

# Part 82 — Compute-Only / Storage-Oriented Scale Concepts

Modern Nutanix designs can include architectures where compute and storage scaling are not always strictly tied one-for-one.

NCI 7.6 also expands external-storage and specialized compute options.

Always validate the specific platform support matrix.

# Part 83 — External Storage

NCI 7.6 supports additional validated external-storage integrations in selected platforms.

This introduces a model where:

```text
AHV compute
+
Nutanix management
+
qualified external storage
```

can coexist.

Do not assume every array is supported.

# Part 84 — Volume Groups

A volume group is a collection of virtual disks used for workloads requiring block-device style organization/performance.

It can be attached to supported AHV VMs or exposed through supported storage services.

# Part 85 — Volume Group Use Cases

Examples:

```text
database data disks
high-I/O application storage
shared/block workflows
```

Design attachment and protection based on application requirements.

# Part 86 — Storage Policies

Policies can express storage behavior for entities.

Concept:

```text
VM/volume
 ↓
storage policy
 ↓
protection/storage behavior
```

This moves administration from manual per-disk configuration toward intent.

# Part 87 — Snapshots

A Nutanix recovery point/snapshot captures data state efficiently at the storage layer.

Snapshots are useful for local recovery but do not automatically replace independent backup/DR copies.

# Part 88 — Protection Policies

Modern Nutanix DR uses protection policies to define:

```text
which entities
how often
where replicated
retention
replication type
```

# Part 89 — Recovery Point

Recovery point:

```text
consistent point-in-time state
```

DR workflows replicate/retain recovery points according to protection policy.

# Part 90 — Asynchronous Replication

Async replication sends recovery points on a schedule.

```text
Primary
  ↓ periodic recovery point
WAN
  ↓
Recovery cluster
```

RPO is tied to replication schedule and completion.

# Part 91 — NearSync Concept

Near-sync reduces RPO compared with conventional longer-interval asynchronous replication.

It requires network/storage design capable of sustaining the tighter replication cadence.

# Part 92 — Synchronous / Metro Concept

Synchronous/Metro-style protection coordinates writes across sites for very low/zero-data-loss designs according to supported topology.

Tradeoffs:

```text
latency constraints
bandwidth
witness/quorum
site design
```

# Part 93 — Recovery Plan

Recovery plans orchestrate application recovery.

```text
Group 1: DNS / AD
   ↓
Group 2: Database
   ↓
Group 3: Application
   ↓
Group 4: Web
```

Order matters.

# Part 94 — Failover

Failover activates protected workloads at recovery location.

A good plan includes:

```text
network mapping
IP changes
boot order
dependencies
verification
```

# Part 95 — Failback

After primary site returns:

```text
synchronize changes
validate
planned return
```

DR is incomplete if failback is never tested.

# Part 96 — Test Recovery

A DR test should avoid disrupting production.

Validate:

```text
recovery point
VM boot
network
application
data consistency
RTO
```

Document measured results.

# Part 97 — Backup vs Native DR

Native replication/DR:

```text
fast site recovery
```

Backup:

```text
independent historical/cyber recovery
```

Use both when required.

A replicated ransomware event can reach the recovery site.

# Part 98 — NC2

Nutanix Cloud Clusters extends the Nutanix operating model to supported public clouds.

Concept:

```text
On-prem NCI
   ↔
NC2 in AWS/Azure/Google Cloud
```

The goal is operational consistency across locations.

# Part 99 — Why NC2 Matters

Use cases:

```text
DR
datacenter exit
cloud bursting
migration
temporary capacity
hybrid applications
```

Cloud networking and cost models still matter.

# Part 100 — Hybrid Multicloud

Multicloud infrastructure is not simply "run VMs in many clouds."

It requires:

```text
consistent operations
identity
networking
security
data mobility
DR
governance
cost awareness
```

# Part 101 — Prism Central Multicluster Management

Prism Central centralizes:

```text
inventory
VM operations
alerts
capacity
security
DR
projects
images
```

across registered clusters according to feature support.

# Part 102 — Nutanix Central Concept

Nutanix Central provides broader fleet-level visibility/operations across Prism Central domains.

Think:

```text
Prism Element → one cluster
Prism Central → one/many clusters in management domain
Nutanix Central → broader global fleet view
```

# Part 103 — Alerts

Prism alerts tell you:

```text
what condition
severity
affected entity
recommended action
```

Read the alert details before changing infrastructure.

# Part 104 — Tasks

Tasks show operations in progress/completed.

Examples:

```text
VM create
migration
upgrade
snapshot
expansion
```

Use task IDs/history when troubleshooting long-running operations.

# Part 105 — Events

Events record changes and state transitions.

Correlate:

```text
time
user
entity
task
alert
```

to reconstruct incidents.

# Part 106 — Performance Monitoring

Monitor hierarchy:

```text
VM
 ↓
Host
 ↓
Cluster
 ↓
Storage
 ↓
Network
```

One slow VM does not automatically mean the cluster is overloaded.

# Part 107 — CPU Monitoring

Inspect:

```text
VM CPU
host CPU
CVM CPU
contention
NUMA
```

High CVM CPU under heavy storage load is different from tenant VM CPU saturation.

# Part 108 — Memory Monitoring

Monitor:

```text
VM configured
VM active
host consumption
reclamation
swap
CVM memory
```

NCI 7.6 provides enhanced AHV infrastructure memory metrics.

# Part 109 — Storage Monitoring

Watch:

```text
latency
IOPS
throughput
capacity
rebuild/re-replication
CVM/storage-service utilization
```

Always correlate VM and cluster views.

# Part 110 — Network Monitoring

Watch:

```text
host NIC errors
link state
bond health
VLAN
throughput
drops
CVM/host communication
```

NCC includes checks for several NIC/network conditions.

# Part 111 — Capacity Planning

Plan:

```text
CPU
RAM
CVM overhead
usable storage
RF
growth
failure headroom
snapshots
DR
network
```

Do not size only from current average usage.

# Part 112 — Failure-Domain Planning

Spread resilience across:

```text
node
block
rack
PDU
ToR
site
```

Two VM replicas on two hosts can still share one rack/PDU failure domain.

# Part 113 — Life Cycle Manager

LCM inventories and upgrades supported infrastructure software/firmware.

Concept:

```text
Inventory
 ↓
available updates
 ↓
prechecks
 ↓
rolling upgrade
 ↓
post-check
```

# Part 114 — Full-Stack Lifecycle

LCM can coordinate multiple stack components according to compatibility.

This reduces manual firmware/driver/hypervisor sequencing, but operators must still review impact and prerequisites.

# Part 115 — LCM Inventory

LCM first discovers current component versions.

If inventory is stale:

```text
upgrade recommendations may be wrong/incomplete
```

Run inventory and resolve errors before planning updates.

# Part 116 — LCM Prechecks

Prechecks verify:

```text
cluster health
capacity
compatibility
service state
```

Never bypass health warnings casually before a rolling upgrade.

# Part 117 — Rolling Upgrade

Typical pattern:

```text
Node 1 maintenance/update/reboot
 ↓
return healthy
 ↓
Node 2
 ↓
Node 3
```

Workloads and storage remain available if capacity/resilience requirements are met.

# Part 118 — Upgrade Order

Prism Central, AOS, AHV, firmware, and feature components have compatibility relationships.

Use LCM/support matrices rather than inventing your own upgrade sequence.

# Part 119 — Foundation

Foundation is used for imaging/deploying Nutanix nodes/clusters in supported workflows.

Concept:

```text
bare node
 ↓
Foundation
 ↓
hypervisor + CVM/AOS image
 ↓
cluster creation
```

# Part 120 — Cluster Creation

Initial cluster setup defines:

```text
node membership
cluster IP/name
DNS
NTP
network
storage resources
```

Accurate IP planning is essential.

# Part 121 — Licensing

NCI capabilities depend on edition/subscription licensing.

Plan licensing for:

```text
AOS
AHV/NCI features
Prism
Flow
DR
management
```

Check current Nutanix licensing documentation before procurement.

# Part 122 — Data-at-Rest Encryption

Nutanix supports data-at-rest encryption through supported software/drive/key-management approaches.

```text
data
 ↓
encryption
 ↓
storage media
```

Encryption design must include key recovery.

# Part 123 — Key Management

Possible architecture:

```text
Nutanix
  ↔
KMS / native supported key service
```

Protect:

```text
keys
certificates
availability
backup
DR
```

Losing the key can make data unrecoverable.

# Part 124 — CVM Security

CVMs are privileged infrastructure appliances.

Controls:

```text
restricted SSH
strong credentials/keys
supported hardening
logging
no arbitrary software
```

Do not treat a CVM like a general Linux server.

# Part 125 — Management Network Security

Protect:

```text
Prism
CVM
AHV host management
IPMI/BMC
LCM/Foundation
```

with isolated administrative networks and controlled access.

# Part 126 — Backplane Segmentation

Nutanix supports network-segmentation designs for cluster/backplane traffic in supported architectures.

Purpose:

```text
isolate infrastructure traffic
reduce exposure
improve security control
```

Follow the exact platform procedure.

# Part 127 — Security Dashboard

Current AOS/Prism provides security posture views for registered clusters.

Use dashboards to track configuration posture, but combine them with vulnerability management and operational review.

# Part 128 — Service Accounts

Prism Central supports service-account patterns for automation.

Use:

```text
dedicated identity
API key/credential
least privilege
rotation
```

instead of a human administrator's password.

# Part 129 — REST APIs

Nutanix exposes REST APIs for automation.

Modern Prism Central workflows increasingly use **v4 APIs**.

Architecture:

```text
Terraform / Python / curl
        |
      HTTPS
        |
   Prism Central
```

# Part 130 — API Automation Principle

Prefer declarative/idempotent automation.

```text
desired VM exists
 ↓
query
 ↓
create only if missing
```

Do not blindly create resources every run.

# Part 131 — API Security

Production API use:

```text
TLS verification
service accounts
least privilege
secret manager
request logging without secrets
```

Never embed Prism admin passwords in source code.

# Part 132 — Cluster Health Workflow

Start:

```bash
cluster status
ncc health_checks run_all
```

Then inspect:

```text
Prism alerts
tasks
hardware
storage
network
```

before modifying services.

# Part 133 — CVM Down Scenario

If one CVM is unavailable:

```text
storage sessions/services redistribute
cluster remains available if resilience is healthy
```

Investigate why it failed rather than immediately restarting multiple CVMs.

# Part 134 — Host Down Scenario

If an AHV host fails:

```text
VMs on host stop
HA restarts them elsewhere
AOS re-replicates if required
```

Check compute and storage effects separately.

# Part 135 — Disk Failure Scenario

AOS detects failed media and restores protection using surviving replicas.

Operator checks:

```text
hardware alert
RF health
rebuild progress
capacity headroom
```

# Part 136 — Storage Latency Troubleshooting

Trace:

```text
VM/application
 ↓
vDisk
 ↓
AHV
 ↓
CVM/storage service
 ↓
DSF
 ↓
physical media/network
```

Correlate VM latency with cluster-wide behavior.

# Part 137 — VM Performance Troubleshooting

Check:

```text
guest CPU/memory
vCPU sizing
host load
CVM/storage
network
storage latency
snapshot/protection activity
```

Do not assume virtualization is the root cause.

# Part 138 — Prism Unavailable

If Prism Element UI is unavailable:

```text
cluster services?
Prism process?
CVM health?
network?
certificate?
disk/capacity?
```

Use CLI read-only evidence and supported recovery procedures.

# Part 139 — Prism Central Unavailable

Check:

```text
PCVM power
PC cluster state
network/DNS/NTP
capacity
certificates
service health
```

Managed clusters can continue independently, but PC-dependent services degrade.

# Part 140 — Network Connectivity Failure

If one VM cannot communicate:

```text
guest
vNIC
VLAN/VPC
virtual switch
bond
physical NIC
switch
route/firewall/Flow
```

If many VMs across one host fail, move the investigation lower in the stack.

# Part 141 — Replication Failure

Check:

```text
site pairing
network reachability
bandwidth
protection policy
recovery-point state
target capacity
authentication
```

A local snapshot success does not prove remote replication succeeded.

# Part 142 — LCM Failure

If LCM inventory/update fails:

```text
cluster health
Internet/dark-site bundle
compatibility
credentials
available space
firmware
NCC
```

Do not force firmware/hypervisor changes outside the supported stack unless directed by validated procedures.

# Part 143 — NCC Failure

An NCC `FAIL` is a diagnostic result.

Workflow:

```text
read check name
identify affected entity
read KB/guidance
collect evidence
correct root cause
rerun specific/full check
```

# Part 144 — Operational Runbook

Daily:

```text
critical alerts
cluster health
CVM/host status
capacity
failed tasks
protection status
```

Weekly:

```text
NCC
LCM inventory
snapshot/DR status
security review
capacity trend
```

Monthly:

```text
restore/DR test
patch/lifecycle review
RBAC review
documentation
```

# Part 145 — NCP-MCI Administration Mindset

The administration mindset is not:

```text
memorize Prism buttons
```

It is:

```text
understand cluster architecture
verify health
operate VMs/storage/networking
protect data
perform lifecycle maintenance
troubleshoot methodically
manage multicluster environments
```

That is the foundation of Nutanix Multicloud Infrastructure administration.

---

# Enhanced Deep-Study Layer — Nutanix Multicloud Infrastructure

This layer **adds** deeper architecture, operations, calculations, diagrams, CLI/API reasoning, failure analysis, and production practices while preserving the complete uploaded Course 44. The uploaded course remains the source baseline; the material below is an expansion layer. Release-specific commands and procedures must be matched to the installed AOS/AHV/Prism release.

```text
Concept
  ↓
Detailed Explanation
  ↓
Architecture / Mental Model
  ↓
Commands / Code / Configuration
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

## Advanced Deep Dive 1 — Nutanix HCI as a Distributed System

### Concept and Detailed Explanation
A Nutanix cluster is more than several hypervisor hosts with local disks. Each node contributes compute, network, storage, and a Controller VM (CVM), while AOS coordinates resilient data placement and cluster services across the nodes. Operators therefore have to reason about both local-node health and cluster-wide behavior.

### Architecture / Mental Model
```text
Prism / API
                   |
           Cluster Control Plane
                   |
    +--------------+--------------+
    |              |              |
  Node 1         Node 2         Node 3
AHV + CVM      AHV + CVM      AHV + CVM
CPU/RAM/Disk   CPU/RAM/Disk   CPU/RAM/Disk
    \              |              /
     +-------- AOS / DSF ----------+
                   |
           Shared Logical Storage
```

### Commands / Code / Configuration
```text
cluster status
ncc health_checks run_all
acli vm.list
ncli host list
```

### Expected Behavior
Healthy cluster services, healthy node participation, visible VMs, and no unresolved critical NCC failures.

### Why It Works
Distributed software allows the cluster to keep serving workloads when one component fails, provided remaining copies, CVMs, network paths, and capacity remain healthy.

### Real Production Example
A single SSD fails on one node. Applications stay online while AOS restores protection using healthy resources elsewhere.

### Troubleshooting Workflow
```text
symptom
  ↓
one VM, one host, one CVM, or cluster-wide?
  ↓
Prism alert/task/event
  ↓
cluster status + NCC
  ↓
compute / storage / network evidence
  ↓
physical component
  ↓
verify resilience restored
```

### Best Practice
Establish the blast radius before changing cluster services.

---

## Advanced Deep Dive 2 — Node, Block, Rack, and Site Failure Domains

### Concept and Detailed Explanation
Logical redundancy only protects against failures that are physically independent. Two replicas on two nodes can still share the same block, rack, PDU, top-of-rack switch, or site. Architecture must therefore map replication and HA to real physical failure domains.

### Architecture / Mental Model
```text
Site
├── Rack A
│   ├── PDU A
│   ├── ToR A
│   ├── Node 1
│   └── Node 2
└── Rack B
    ├── PDU B
    ├── ToR B
    ├── Node 3
    └── Node 4
```

### Commands / Code / Configuration
```text
Node | Block | Rack | PDU | ToR | Site | CVM IP | Host IP
-----|-------|------|-----|-----|------|--------|--------
N1   | B1    | R1   | P1  | T1  | DC1  | ...    | ...
```

### Expected Behavior
You can state exactly what happens if any one node, block, rack, PDU, ToR, or site fails.

### Why It Works
Distributed resilience is only as strong as the independence of the resources that hold the copies and run the surviving services.

### Real Production Example
A four-node cluster spans two racks, but both network uplinks terminate on one switch. The switch remains a hidden common failure domain.

### Troubleshooting Workflow
```text
resilience concern
  ↓
map copies/resources to node/block/rack/site
  ↓
identify shared dependencies
  ↓
verify topology awareness
  ↓
correct placement or physical design
```

### Best Practice
Maintain a physical failure-domain map and update it whenever nodes are added.

---

## Advanced Deep Dive 3 — RF2 and RF3 Capacity Mathematics

### Concept and Detailed Explanation
RF2 and RF3 protect data by maintaining multiple distributed copies. The replication factor directly affects usable capacity, but real planning must also subtract metadata, snapshots, free-space headroom, rebuild reserve, and growth reserve.

### Architecture / Mental Model
```text
Raw Capacity
    |
Replication Overhead
    |
System / Metadata
    |
Snapshots
    |
Failure-Rebuild Headroom
    |
Growth Reserve
    |
Safe Usable Capacity
```

### Commands / Code / Configuration
```text
raw_tb = 120
rf = 2
system = 0.08
snapshots = 0.10
failure_headroom = 0.15
growth = 0.15

after_rf = raw_tb / rf
safe_tb = after_rf * (1 - system - snapshots - failure_headroom - growth)
print(round(safe_tb, 2))
```

### Expected Behavior
A conservative planning estimate that is lower than simple raw-capacity-divided-by-RF.

### Why It Works
A distributed cluster needs free resources to heal after failures, not just enough space for steady-state workload data.

### Real Production Example
A cluster at 92% raw utilization may continue serving I/O but have insufficient free space to restore RF after a node failure.

### Troubleshooting Workflow
```text
capacity issue
  ↓
raw capacity
  ↓
RF
  ↓
current logical/physical use
  ↓
snapshots/protection
  ↓
free space by node
  ↓
failure-state requirement
```

### Best Practice
Capacity-plan for the failure state, not only the normal state.

---

## Advanced Deep Dive 4 — Resilience State vs Availability

### Concept and Detailed Explanation
A workload can remain available while the cluster is operating below its intended protection level. After a disk or node failure, VMs may keep running from surviving replicas while AOS re-replicates data. Availability and resilience are therefore separate operational states.

### Architecture / Mental Model
```text
Failure
  ↓
VMs may remain online
  ↓
Protection reduced
  ↓
Re-replication / healing
  ↓
Protection restored
```

### Commands / Code / Configuration
```text
cluster status
ncc health_checks run_all
# Prism: Health / Resilience / Hardware / Storage
```

### Expected Behavior
You can distinguish service availability, current data protection, recovery progress, and remaining failure tolerance.

### Why It Works
Distributed storage can mask a first failure from the application while background healing restores the desired copy count.

### Real Production Example
A host fails, VMs restart successfully, but the cluster remains at reduced resilience until data is re-protected.

### Troubleshooting Workflow
```text
failure
  ↓
application available?
  ↓
resilience healthy?
  ↓
re-replication progress?
  ↓
capacity sufficient?
  ↓
safe for maintenance?
```

### Best Practice
Do not begin elective maintenance while the cluster is already below intended resilience.

---

## Advanced Deep Dive 5 — CVM Architecture and Privilege Boundary

### Concept and Detailed Explanation
The CVM is a privileged infrastructure appliance, not a general-purpose Linux VM. It participates in storage I/O, metadata, health, cluster control, data protection, and management. Unsupported packages, service manipulation, or casual resource changes can create platform-wide problems.

### Architecture / Mental Model
```text
AHV Host
├── Tenant VM 1
├── Tenant VM 2
└── CVM
    ├── AOS services
    ├── storage path
    ├── metadata/control
    └── Prism/health integration
```

### Commands / Code / Configuration
```text
cluster status
ncc health_checks run_all
acli vm.list
ncli cluster info
```

### Expected Behavior
The CVM participates normally in cluster services and is reachable over the intended management/backplane networks.

### Why It Works
Each CVM is part of the storage/control architecture, so unsupported changes can affect more than one workload.

### Real Production Example
An administrator installs arbitrary third-party software inside all CVMs and later a supported lifecycle update fails because the appliance state no longer matches expected assumptions.

### Troubleshooting Workflow
```text
CVM issue
  ↓
one CVM or many?
  ↓
host state
  ↓
cluster status
  ↓
Prism alert/task
  ↓
CPU/RAM/network evidence
  ↓
supported remediation
```

### Best Practice
Use Prism, NCC, LCM, and supported procedures; keep arbitrary software off CVMs.

---

## Advanced Deep Dive 6 — CVM Resource Sizing and Workload Impact

### Concept and Detailed Explanation
CVM CPU and memory are part of the infrastructure budget. Storage-heavy workloads can raise CVM CPU and network demand even when tenant VM CPU is moderate. Node sizing must therefore include CVM overhead plus HA and maintenance reserve before calculating tenant capacity.

### Architecture / Mental Model
```text
Physical Node
  |
  +-- CVM CPU/RAM
  +-- AHV/platform overhead
  +-- HA reserve
  `-- Tenant VM capacity
```

### Commands / Code / Configuration
```text
Capacity worksheet:
Host RAM
CVM/platform reserve
N+1 reserve
Tenant configured RAM
Tenant active RAM

Track:
VM CPU
Host CPU
CVM CPU
Storage latency
IOPS / throughput
```

### Expected Behavior
You can explain whether a performance issue is guest compute pressure or infrastructure storage/control pressure.

### Why It Works
The CVM is in the I/O path, so storage demand can consume infrastructure CPU and memory.

### Real Production Example
A database workload drives high IOPS; CVM CPU and storage latency rise while guest CPU remains low.

### Troubleshooting Workflow
```text
slow VM
  ↓
guest CPU?
  ↓
host CPU?
  ↓
CVM CPU?
  ↓
storage IOPS/latency?
  ↓
network or rebuild activity?
```

### Best Practice
Include CVM performance in every storage-performance investigation.

---

## Advanced Deep Dive 7 — Data Locality and VM Mobility

### Concept and Detailed Explanation
Nutanix can serve VM reads efficiently using local data where possible while keeping protected replicas elsewhere. After live migration, the VM does not need its entire virtual disk copied before it can run; storage remains available through DSF and locality can adapt afterward.

### Architecture / Mental Model
```text
Before:
VM on Node 1
  |
local preferred reads
  |
distributed replicas

After migration:
VM on Node 2
  |
DSF access remains available
  |
locality adapts over time
```

### Commands / Code / Configuration
```text
acli vm.get <VM_NAME>
# Compare Prism VM/host/storage metrics before and after migration.
```

### Expected Behavior
Migration changes compute placement without requiring a complete storage move first.

### Why It Works
Distributed storage decouples VM execution location from rigid local-disk ownership.

### Real Production Example
A multi-terabyte VM can migrate between AHV hosts without first copying the full virtual-disk footprint.

### Troubleshooting Workflow
```text
post-migration latency
  ↓
VM metrics
  ↓
CVM/storage metrics
  ↓
inter-node network
  ↓
background locality behavior
```

### Best Practice
Correlate short post-migration behavior with cluster metrics before concluding that migration caused a storage fault.

---

## Advanced Deep Dive 8 — Distributed Write Path

### Concept and Detailed Explanation
A protected write depends on local storage processing plus the required remote copy/replica before acknowledgment. Inter-node network quality therefore directly influences write latency and storage behavior.

### Architecture / Mental Model
```text
VM write
   |
local CVM
   |
+----------+
|          |
local copy remote protected copy
|          |
+---- required durability ----+
              |
             ACK
```

### Commands / Code / Configuration
```text
# Observe:
# Prism VM storage latency
# Prism cluster storage latency
# CVM CPU
# host/CVM network counters
ip -s link
```

### Expected Behavior
Write latency should remain stable and required protection should complete without sustained errors.

### Why It Works
Data protection requires more than one component to participate before a write is considered safely stored.

### Real Production Example
A ToR link develops packet loss between nodes. Application write latency rises even though physical SSD health is normal.

### Troubleshooting Workflow
```text
write latency
  ↓
one VM or many?
  ↓
CVM CPU
  ↓
disk health
  ↓
inter-node network
  ↓
rebuild/replication
```

### Best Practice
Treat the inter-node network as part of the storage subsystem.

---

## Advanced Deep Dive 9 — Checksums and Silent Corruption

### Concept and Detailed Explanation
Availability does not guarantee correctness. Integrity checks such as checksums help detect silent media corruption so that a healthy copy can be used and the bad data repaired.

### Architecture / Mental Model
```text
Write:
data + checksum
   |
Read:
verify checksum
   |
valid → return
invalid → healthy replica / repair
```

### Commands / Code / Configuration
```text
Operational evidence:
Prism hardware/storage alerts
NCC health checks
repeated media/integrity warnings
```

### Expected Behavior
No persistent integrity or media errors remain after hardware remediation and data protection is restored.

### Why It Works
Storage devices can return incorrect data without fully failing. Integrity metadata detects this class of fault.

### Real Production Example
A drive remains online but returns corrupted sectors; checksum validation detects bad data and a healthy replica is used.

### Troubleshooting Workflow
```text
integrity alert
  ↓
affected device/node
  ↓
verify resilience
  ↓
review hardware health
  ↓
confirm healthy replicas
  ↓
replace/remediate
  ↓
verify clean health
```

### Best Practice
Investigate repeated integrity errors even if applications remain online.

---

## Advanced Deep Dive 10 — Compression, Deduplication, and Erasure Coding

### Concept and Detailed Explanation
Compression, deduplication, and erasure coding are different capacity-efficiency tools. Compression reduces data size, deduplication avoids duplicate patterns where useful, and erasure coding can reduce replica overhead for suitable data at the cost of reconstruction and compute overhead.

### Architecture / Mental Model
```text
Logical Data
  |
  +-- Compression
  +-- Deduplication
  `-- Erasure Coding
  |
Physical Capacity Used
```

### Commands / Code / Configuration
```text
Capacity test:
1. record logical used;
2. record physical used;
3. identify enabled policies;
4. observe representative workload;
5. exclude temporary rebuild/snapshot effects;
6. calculate realized ratio.
```

### Expected Behavior
Measured data reduction matches the actual workload rather than a generic marketing ratio.

### Why It Works
Encrypted, already-compressed, VDI, database, and backup data have very different reduction characteristics.

### Real Production Example
Encrypted backup files often compress poorly while similar VDI OS images may exhibit far more duplicate data.

### Troubleshooting Workflow
```text
saving lower than expected
  ↓
already compressed/encrypted?
  ↓
policy enabled?
  ↓
snapshot overhead?
  ↓
change rate?
  ↓
compare logical vs physical correctly
```

### Best Practice
Treat data reduction as measured efficiency, not guaranteed baseline capacity.

---

## Advanced Deep Dive 11 — Storage Containers as Policy Boundaries

### Concept and Detailed Explanation
A storage container is a logical storage construct, not a physical disk group. Containers should exist for a real policy, ownership, protection, or administrative reason. Creating one container per VM usually adds complexity without meaningful isolation.

### Architecture / Mental Model
```text
Physical Disks
   |
Storage Pool / DSF
   |
+-- Container-Prod
+-- Container-Dev
+-- Container-DB
   |
VM vDisks
```

### Commands / Code / Configuration
```text
ncli container list

Container | Purpose | Protection | Encryption | Snapshot Policy | Owner
```

### Expected Behavior
Every container has a documented purpose and policy.

### Why It Works
DSF distributes data independently of the logical container boundary, so excessive logical fragmentation does not create traditional SAN-style physical isolation.

### Real Production Example
An environment accumulates hundreds of one-VM containers, making policy and capacity administration inconsistent.

### Troubleshooting Workflow
```text
container sprawl
  ↓
identify actual policy differences
  ↓
group workloads
  ↓
standardize
  ↓
document owner
```

### Best Practice
Use the minimum number of containers needed to express real operational policy.

---

## Advanced Deep Dive 12 — Storage Pool Fragmentation

### Concept and Detailed Explanation
Storage pools aggregate physical resources. Excessive fragmentation can strand capacity and reduce flexibility for balancing and healing. Broad distributed resource pools are usually more efficient unless a supported technical requirement demands separation.

### Architecture / Mental Model
```text
Pool A nearly full
Pool B mostly empty
  |
capacity is physically present
but administratively stranded

Broad pool:
more resources for placement/healing
```

### Commands / Code / Configuration
```text
ncli storagepool list
ncli container list

Review:
pool purpose
capacity
hardware/media
container mappings
```

### Expected Behavior
Every storage pool has a clear technical justification and enough headroom for failure recovery.

### Why It Works
A distributed system gains balancing flexibility from a larger common resource set.

### Real Production Example
A small isolated pool reaches 90% while another pool has tens of terabytes free.

### Troubleshooting Workflow
```text
pool pressure
  ↓
is separation required?
  ↓
capacity by pool
  ↓
container mapping
  ↓
supported consolidation/migration
```

### Best Practice
Avoid recreating legacy SAN-LUN habits in HCI unless there is a real requirement.

---

## Advanced Deep Dive 13 — AHV, KVM, and VM Execution

### Concept and Detailed Explanation
AHV runs VMs using Linux/KVM-based virtualization while AOS/CVM provides the distributed storage layer. The two functions are integrated operationally but must be separated during diagnosis.

### Architecture / Mental Model
```text
VM
 ↓
AHV / KVM
 ↓
CPU / RAM

VM vDisk
 ↓
AOS / CVM / DSF
 ↓
distributed storage
```

### Commands / Code / Configuration
```text
acli vm.list
acli vm.get <VM_NAME>
```

### Expected Behavior
You can identify the current AHV host and separately inspect storage/network dependencies.

### Why It Works
A VM can fail for CPU/device reasons even when its AOS storage is healthy, or suffer storage latency while compute scheduling is healthy.

### Real Production Example
A VM cannot start because of a special device constraint even though its disk is fully accessible.

### Troubleshooting Workflow
```text
VM failure
  ↓
power/state
  ↓
AHV host capacity
  ↓
device/CPU constraints
  ↓
AOS storage
  ↓
network
  ↓
guest OS
```

### Best Practice
Classify the fault as compute, storage, network, or guest before acting.

---

## Advanced Deep Dive 14 — vCPU Right-Sizing

### Concept and Detailed Explanation
More vCPUs are not automatically faster. Oversized VMs reduce scheduler flexibility, can increase NUMA complexity, and consume failure-state capacity. Size from measured demand and application threading behavior.

### Architecture / Mental Model
```text
Application threads
   |
vCPU request
   |
AHV scheduler
   |
physical cores / NUMA
```

### Commands / Code / Configuration
```text
VM | Configured vCPU | P95 CPU | Peak CPU | Proposed vCPU | Owner

# Prism:
# VM → CPU metrics
# Host → CPU metrics
```

### Expected Behavior
VMs meet application SLOs without persistent contention or large amounts of unused vCPU.

### Why It Works
Hypervisors schedule finite physical execution resources; unused vCPUs still constrain placement and HA calculations.

### Real Production Example
A 32-vCPU VM averages 5% CPU and performs no better than at 8 vCPU, but greatly reduces placement options.

### Troubleshooting Workflow
```text
CPU complaint
  ↓
guest CPU
  ↓
configured vs used
  ↓
host contention
  ↓
NUMA
  ↓
application thread model
```

### Best Practice
Right-size from representative metrics, not from fear-based overprovisioning.

---

## Advanced Deep Dive 15 — Memory and N+1 Headroom

### Concept and Detailed Explanation
Memory planning must show both normal capacity and the surviving capacity after one host is unavailable. CVM/platform reserve must be subtracted before tenant VM capacity is calculated.

### Architecture / Mental Model
```text
Normal:
N hosts

Failure:
N-1 hosts
must carry:
tenant VMs + CVMs + platform reserve
```

### Commands / Code / Configuration
```text
hosts = 4
ram_per_host = 768
platform_reserve = 48

safe_per_host = ram_per_host - platform_reserve
normal = safe_per_host * hosts
n_minus_1 = safe_per_host * (hosts - 1)

print(normal, n_minus_1)
```

### Expected Behavior
Capacity documentation reports safe normal and N-1 RAM, not just installed memory.

### Why It Works
HA restart requires surviving hosts to absorb the failed host's workload.

### Real Production Example
A cluster appears comfortable at 75% memory, but after losing one of four hosts the remaining three have almost no restart headroom.

### Troubleshooting Workflow
```text
memory risk
  ↓
installed RAM
  ↓
CVM/platform reserve
  ↓
tenant configured/active
  ↓
N-1 requirement
  ↓
growth
```

### Best Practice
Set operational limits from failure-state capacity.

---

## Advanced Deep Dive 16 — AHV Virtual Networking Mental Model

### Concept and Detailed Explanation
A VM packet traverses several layers: guest networking, vNIC, AHV virtual switching, VLAN or Flow logical networking, bond/uplink, physical NIC, top-of-rack switch, and routing/firewall infrastructure. Troubleshooting should move one layer at a time rather than changing several layers simultaneously.

### Architecture / Mental Model
```text
Guest
  |
vNIC
  |
AHV virtual switch / OVS
  |
VLAN / Flow VPC
  |
bond/uplink
  |
physical NIC
  |
ToR
  |
router/firewall
```

### Commands / Code / Configuration
```text
# Guest
ip addr
ip route
ping <gateway>

# CVM/host evidence where authorized
acli vm.get <VM_NAME>
ip -s link
```

### Expected Behavior
You can localize the fault to guest, virtual network, host uplink, physical switching, or upstream routing/security.

### Why It Works
Each networking layer has independent configuration and failure modes.

### Real Production Example
Every VM on one host loses VLAN 200 while identical VMs on other hosts remain healthy, pointing to host/uplink/ToR rather than guest configuration.

### Troubleshooting Workflow
```text
network issue
  ↓
one VM or many?
  ↓
guest IP/route/firewall
  ↓
vNIC/network
  ↓
VLAN/VPC/Flow
  ↓
bond/NIC
  ↓
ToR/routing
```

### Best Practice
Use blast radius to decide where to start.

---

## Advanced Deep Dive 17 — VLAN and Physical Trunk Consistency

### Concept and Detailed Explanation
Creating a VLAN-backed network in Prism does not make the physical switches carry that VLAN. Every host that may run the workload needs consistent virtual-switch and upstream trunk configuration.

### Architecture / Mental Model
```text
VM Network VLAN 100
       |
AHV Host 1 ---- ToR trunk includes 100
AHV Host 2 ---- ToR trunk includes 100
AHV Host 3 ---- ToR trunk includes 100
```

### Commands / Code / Configuration
```text
AHV Network | VLAN | Host Uplink | Switch Ports | Gateway | MTU
PROD-WEB    | 100  | bond0       | Eth1/1-1/3  | ...     | ...
```

### Expected Behavior
A VM retains network connectivity after migration to any eligible host.

### Why It Works
Live migration changes compute placement, so the destination host must have equivalent network reachability.

### Real Production Example
A VM works on Node 1 but loses connectivity immediately after migration to Node 3 because VLAN 100 is missing on Node 3's ToR trunk.

### Troubleshooting Workflow
```text
migration causes network loss
  ↓
VM network
  ↓
destination virtual switch
  ↓
bond/uplink
  ↓
ToR VLAN trunk
  ↓
gateway
```

### Best Practice
Validate network equivalence before enabling a new host for workload placement.

---

## Advanced Deep Dive 18 — Bonding and Physical Network Redundancy

### Concept and Detailed Explanation
Multiple NICs provide redundancy only when the host bond mode, switch configuration, cabling, and physical failure domains are all aligned. Two uplinks connected to one switch protect against cable failure but not switch failure.

### Architecture / Mental Model
```text
AHV Host
   |
  bond
 /    NIC1  NIC2
 |      |
ToR-A  ToR-B
```

### Commands / Code / Configuration
```text
ip -s link

Review:
bond mode
NIC speed
switch pair
VLAN consistency
MTU
LACP requirements where used
failover test
```

### Expected Behavior
A single approved link failure should not isolate the host if the design claims link redundancy.

### Why It Works
Software redundancy depends on independent physical paths and compatible switch behavior.

### Real Production Example
Both host NICs are accidentally connected to the same ToR, leaving a hidden single-switch failure domain.

### Troubleshooting Workflow
```text
host network issue
  ↓
bond state
  ↓
individual NIC counters
  ↓
switch-port state
  ↓
VLAN/LACP
  ↓
failover behavior
```

### Best Practice
Test uplink failure during maintenance and document the observed behavior.

---

## Advanced Deep Dive 19 — MTU and Jumbo-Frame Validation

### Concept and Detailed Explanation
MTU mismatch often creates deceptive symptoms: small ping packets work while large transfers, replication, or storage traffic stalls. The smallest MTU in the path determines what can pass without fragmentation.

### Architecture / Mental Model
```text
Host/CVM
  |
NIC
  |
ToR
  |
Spine
  |
Remote Host/Site

Smallest MTU wins
```

### Commands / Code / Configuration
```text
ip link show
ping -M do -s <payload-size> <peer>
```

### Expected Behavior
Large-packet tests pass end to end on networks designed for a larger MTU.

### Why It Works
Encapsulation and large frames require every hop to support the chosen size.

### Real Production Example
Replication falls behind only during large transfers because one intermediate network segment remains at 1500 MTU.

### Troubleshooting Workflow
```text
small works / large fails
  ↓
host/CVM MTU
  ↓
bond/NIC
  ↓
switches
  ↓
router/firewall
  ↓
WAN
```

### Best Practice
Never enable jumbo frames on only part of the path.

---

## Advanced Deep Dive 20 — Flow Virtual Networking VPC Architecture

### Concept and Detailed Explanation
Flow Virtual Networking introduces cloud-style logical VPCs and subnets above the physical underlay. The underlay transports packets; the overlay expresses logical tenancy, routing, and isolation.

### Architecture / Mental Model
```text
Applications
   |
VPC-Prod
├── Web subnet
├── App subnet
└── DB subnet
   |
logical routing/policy
   |
overlay transport
   |
physical underlay
```

### Commands / Code / Configuration
```text
VPC: PROD
  WEB 10.10.10.0/24
  APP 10.10.20.0/24
  DB  10.10.30.0/24

Document:
external connectivity
DNS/NTP
routing
security policy
```

### Expected Behavior
You can trace a packet through logical VPC routing and then through the physical network.

### Why It Works
Logical topology can be changed independently of physical VLAN topology while the underlay remains the transport.

### Real Production Example
A new application receives isolated web/app/db networks without requesting three new physical VLANs.

### Troubleshooting Workflow
```text
VPC traffic fails
  ↓
VM IP/subnet
  ↓
logical route
  ↓
Flow policy
  ↓
VPC uplink/external path
  ↓
overlay
  ↓
physical underlay
```

### Best Practice
Troubleshoot overlay and underlay as separate layers.

---

## Advanced Deep Dive 21 — Flow Microsegmentation with Categories

### Concept and Detailed Explanation
Flow Network Security can apply policy to workload categories instead of static IP addresses. Policy therefore follows workload identity as VMs move or scale, but only if category data is accurate.

### Architecture / Mental Model
```text
Categories:
App=ERP
Tier=Web/App/DB
Environment=Prod

Policy:
ERP-Web → ERP-App TCP/8443
ERP-App → ERP-DB TCP/5432
Other lateral traffic denied
```

### Commands / Code / Configuration
```text
Source Category | Destination Category | Service | Action | Reason
ERP/Web         | ERP/App              | 8443    | Allow  | API
ERP/App         | ERP/DB               | 5432    | Allow  | DB
```

### Expected Behavior
A newly provisioned ERP web VM with correct categories inherits the expected security policy automatically.

### Why It Works
Identity-driven grouping avoids repeated rule changes when addresses or host placement change.

### Real Production Example
A VM is deployed without the expected category and does not receive the intended microsegmentation policy.

### Troubleshooting Workflow
```text
unexpected allow/block
  ↓
VM categories
  ↓
policy scope/priority
  ↓
source/destination
  ↓
service/port
  ↓
guest firewall
  ↓
network
```

### Best Practice
Make category assignment mandatory in provisioning workflows.

---

## Advanced Deep Dive 22 — Microsegmentation Policy Lifecycle

### Concept and Detailed Explanation
Security policy should move through discovery, design, testing, enforcement, monitoring, review, and retirement. Enforcing a deny-heavy policy without understanding application dependencies can create outages.

### Architecture / Mental Model
```text
Discover traffic
   ↓
Design policy
   ↓
Test / observe
   ↓
Enforce
   ↓
Monitor violations
   ↓
Review / refine
```

### Commands / Code / Configuration
```text
Policy record:
application owner
dependency map
allowed services
scope
rollback
exception expiry
monitoring owner
```

### Expected Behavior
Unauthorized lateral flows are blocked while approved application dependencies continue to work.

### Why It Works
Staged enforcement reduces risk from undocumented application dependencies.

### Real Production Example
A backup agent is accidentally blocked by a new database microsegmentation rule because the backup dependency was never documented.

### Troubleshooting Workflow
```text
after policy change outage
  ↓
affected flows
  ↓
category membership
  ↓
rule/priority
  ↓
dependency map
  ↓
narrow temporary exception
  ↓
fix documented policy
```

### Best Practice
Use time-bounded exceptions and remove them after the dependency is modeled.

---

## Advanced Deep Dive 23 — Prism Element vs Prism Central Boundaries

### Concept and Detailed Explanation
Prism Element manages a cluster locally. Prism Central provides multicluster inventory and many advanced centralized services. When Prism Central is unavailable, cluster-local runtime can continue, so operators must know which workflows depend on each management plane.

### Architecture / Mental Model
```text
Prism Central
  |
  +-- Cluster A / Prism Element
  +-- Cluster B / Prism Element
  +-- Cluster C / Prism Element
```

### Commands / Code / Configuration
```text
Document:
Prism Central address
each Prism Element address
PC-dependent features
break-glass local access
```

### Expected Behavior
Operators can continue essential cluster-local validation through Prism Element during a Prism Central outage.

### Why It Works
Centralized management sits above autonomous cluster runtime services.

### Real Production Example
Prism Central is down, but VMs and DSF remain healthy and Prism Element is still reachable.

### Troubleshooting Workflow
```text
PC unavailable
  ↓
managed clusters healthy?
  ↓
PE reachable?
  ↓
PC VM/state
  ↓
DNS/NTP/TLS
  ↓
PC service/capacity
```

### Best Practice
Maintain a Prism Central outage runbook that begins with workload and Prism Element validation.

---

## Advanced Deep Dive 24 — Prism Central Capacity and Scale-Out

### Concept and Detailed Explanation
Prism Central is itself a production management platform. Its CPU, memory, disk, availability architecture, and protection must scale with cluster count, VM count, API demand, Flow, DR, images, projects, and other enabled services.

### Architecture / Mental Model
```text
Managed Clusters
      |
  Prism Central
  one VM or scale-out
      |
inventory / Flow / DR / APIs / projects
```

### Commands / Code / Configuration
```text
Capacity checklist:
clusters managed
VMs managed
enabled PC services
CPU/RAM/disk
PC VM availability
backup/recovery
certificate lifecycle
```

### Expected Behavior
Prism Central remains responsive during normal inventory, policy, DR, and API operations.

### Why It Works
Centralized services add compute and storage load to Prism Central beyond simple UI functions.

### Real Production Example
A small Prism Central deployment is later used for Flow and DR across many clusters and becomes resource constrained.

### Troubleshooting Workflow
```text
PC slow
  ↓
PC VM CPU/RAM/disk
  ↓
enabled services
  ↓
managed object count
  ↓
network/DNS
  ↓
resize/scale guidance
```

### Best Practice
Reassess Prism Central sizing when major services or fleet size increases.

---

## Advanced Deep Dive 25 — Categories as a Governance Data Model

### Concept and Detailed Explanation
Categories should be treated as a controlled metadata model because security, protection, reporting, ownership, and automation can all depend on them.

### Architecture / Mental Model
```text
Category Dimensions
App
Environment
Tier
Owner
Criticality
DataClass
BackupPolicy
DRPolicy
```

### Commands / Code / Configuration
```text
App=ERP
Environment=Prod
Tier=DB
Criticality=Tier1
BackupPolicy=Gold
DRPolicy=NearSync
Owner=Business-Apps
```

### Expected Behavior
Every production VM carries the required category dimensions using approved values.

### Why It Works
Policy automation only works reliably when the metadata feeding it is consistent.

### Real Production Example
One team uses Env=Prod while another uses Environment=Production, causing security/protection policies to match only part of the fleet.

### Troubleshooting Workflow
```text
policy mismatch
  ↓
category taxonomy
  ↓
VM values
  ↓
legacy/duplicate values
  ↓
normalize
  ↓
automate validation
```

### Best Practice
Create and enforce a small approved category dictionary.

---

## Advanced Deep Dive 26 — Projects, Quotas, and Self-Service

### Concept and Detailed Explanation
Projects can delegate VM and resource creation without giving users platform-admin rights. Safe self-service requires quotas, approved networks/images, ownership, and lifecycle rules.

### Architecture / Mental Model
```text
Prism Central
  |
Project: Dev-Team-A
├── users/groups
├── quotas
├── networks
├── images
└── VMs
```

### Commands / Code / Configuration
```text
Project standard:
CPU quota
RAM quota
VM count
approved networks
approved images
expiry rule
owner
cost center
```

### Expected Behavior
Project users can create resources within the intended scope and limits without administrative control of the entire platform.

### Why It Works
Self-service is safe when resource rights are delegated without delegating infrastructure control.

### Real Production Example
A developer is given Prism admin merely to create VMs, unnecessarily exposing network, LCM, and security administration.

### Troubleshooting Workflow
```text
self-service issue
  ↓
project
  ↓
role
  ↓
quota
  ↓
network/image access
  ↓
ownership/lifecycle
```

### Best Practice
Use projects and least privilege instead of shared administrator accounts.

---

## Advanced Deep Dive 27 — RBAC and Separation of Duties

### Concept and Detailed Explanation
Platform administration, VM operations, security, audit, backup, and automation should be separated where practical. Broad all-powerful accounts increase both accidental and malicious blast radius.

### Architecture / Mental Model
```text
Identity Provider
     |
Prism Central RBAC
     |
+----+----+----+----+
Admin VM-Op Security Auditor
```

### Commands / Code / Configuration
```text
Role | VM Create | Network | Flow | LCM | Audit | RBAC
-----|-----------|---------|------|-----|-------|-----
...
```

### Expected Behavior
Each role contains only the actions required for the user's operational responsibility.

### Why It Works
Separation of duties limits privilege and improves accountability.

### Real Production Example
A backup operator accidentally changes a Flow policy because the account also has full platform admin rights.

### Troubleshooting Workflow
```text
authorization issue
  ↓
user/group
  ↓
role
  ↓
scope/project
  ↓
requested action
  ↓
least privilege correction
```

### Best Practice
Assign permissions through groups/roles rather than individual exceptions.

---

## Advanced Deep Dive 28 — Service Accounts for Automation

### Concept and Detailed Explanation
Automation should use dedicated machine identities or supported API credentials, not a human Prism administrator's password. Each credential needs an owner, purpose, scope, secret store, rotation, and revoke procedure.

### Architecture / Mental Model
```text
CI / Terraform / Python
       |
Service Account / API Credential
       |
Prism Central API
       |
limited resources/actions
```

### Commands / Code / Configuration
```text
Identity record:
name
owner
purpose
role
scope
secret location
rotation date
last used
revoke procedure
```

### Expected Behavior
Automation runs using a scoped machine identity and fails cleanly when that credential is revoked.

### Why It Works
Machine credentials have a different lifecycle and risk model from interactive human identities.

### Real Production Example
A former employee's Prism password remains embedded in an automation script because no service-account model existed.

### Troubleshooting Workflow
```text
automation auth/leak
  ↓
credential identity
  ↓
scope/role
  ↓
secret store
  ↓
rotation/revocation
  ↓
audit activity
```

### Best Practice
Never place broad Prism administrator credentials in source code or CI logs.

---

## Advanced Deep Dive 29 — Tasks, Events, and Alerts as Evidence

### Concept and Detailed Explanation
Prism tasks, events, and alerts answer different questions. Tasks show operations, events show state changes, and alerts show conditions that require attention. Correlating them by entity and timestamp often identifies the trigger of an incident.

### Architecture / Mental Model
```text
User/API action
   |
Task
   |
Events
   |
Alert if unhealthy
   |
metrics
```

### Commands / Code / Configuration
```text
Time | Entity | Task ID | Event | Alert | User | Result
```

### Expected Behavior
You can reconstruct what changed immediately before a failure or performance event.

### Why It Works
Management-plane history provides causal evidence that raw metrics alone may not show.

### Real Production Example
A VM loses network after a live migration; Prism tasks reveal the destination host change just before the outage.

### Troubleshooting Workflow
```text
incident
  ↓
time/entity
  ↓
tasks
  ↓
events
  ↓
alerts
  ↓
metrics
  ↓
CLI evidence if needed
```

### Best Practice
Capture Prism history before disruptive changes.

---

## Advanced Deep Dive 30 — AHV High Availability and Restart RTO

### Concept and Detailed Explanation
AHV HA restores VM availability after host failure by restarting eligible VMs on surviving hosts. Application recovery time therefore includes host-failure detection, VM restart scheduling, guest boot, and application initialization.

### Architecture / Mental Model
```text
Host A fails
  ↓
VMs stop
  ↓
HA selects surviving hosts
  ↓
VMs restart
  ↓
guest boots
  ↓
application becomes ready
```

### Commands / Code / Configuration
```text
HA test record:
failure detected
VM restart started
VM powered on
guest ready
application ready
business transaction passed
```

### Expected Behavior
Measured application recovery meets the business RTO, not merely the VM power-on target.

### Why It Works
Infrastructure HA restores compute execution, but application crash recovery and service startup still take time.

### Real Production Example
A database VM restarts in one minute but requires ten more minutes for database recovery.

### Troubleshooting Workflow
```text
host failure
  ↓
HA restart?
  ↓
destination capacity?
  ↓
VM boot?
  ↓
application service?
  ↓
data consistency?
```

### Best Practice
Measure application RTO during controlled HA tests.

---

## Advanced Deep Dive 31 — HA Capacity: N+1 and Beyond

### Concept and Detailed Explanation
HA requires spare compute, memory, storage, and network resources. A cluster operating near saturation can have every component healthy yet fail to restart all workloads after one node or one rack is lost.

### Architecture / Mental Model
```text
Normal: N hosts
Failure: N-1 hosts
must absorb:
workloads + CVMs + platform reserve
```

### Commands / Code / Configuration
```text
safe_cluster_capacity =
  surviving_host_capacity
  - CVM/platform reserve
  - maintenance reserve

Compare with tenant demand.
```

### Expected Behavior
The failure-state model shows enough headroom to meet workload and storage-performance requirements.

### Why It Works
Redundancy only works when surviving resources have capacity to absorb the failed domain.

### Real Production Example
A three-node cluster at 70% RAM can exceed safe capacity after one node disappears.

### Troubleshooting Workflow
```text
HA risk
  ↓
chosen failure domain
  ↓
surviving nodes
  ↓
RAM/CPU/storage/network reserve
  ↓
expand/right-size
```

### Best Practice
Set alert thresholds from failure-state headroom rather than normal-state percentages.

---

## Advanced Deep Dive 32 — Live Migration as a Validation Tool

### Concept and Detailed Explanation
Live migration is useful for maintenance and balancing, but it also validates that destination hosts have compatible CPU, networking, and capacity. A VM that loses connectivity only after migration often exposes a host-specific network inconsistency.

### Architecture / Mental Model
```text
Host A
  VM running
    |
live migration
    |
Host B
  VM continues
```

### Commands / Code / Configuration
```text
Before:
acli vm.get <VM_NAME>

During:
continuous ping / application transaction

After:
verify host placement
verify network
verify storage latency
```

### Expected Behavior
The VM remains available with acceptable interruption and preserves network/storage connectivity.

### Why It Works
DSF keeps storage available independently of compute placement, so live migration mainly transfers execution state.

### Real Production Example
A VM works on Host A but loses network on Host B because the destination trunk lacks the VM VLAN.

### Troubleshooting Workflow
```text
migration fail
  ↓
target capacity
  ↓
CPU/device constraints
  ↓
network/VLAN
  ↓
host health
  ↓
special passthrough
```

### Best Practice
Use a representative migration test before placing production workloads on new hosts.

---

## Advanced Deep Dive 33 — Affinity and Anti-Affinity Tradeoffs

### Concept and Detailed Explanation
Placement rules express business intent but reduce scheduler freedom. Affinity can satisfy licensing or hardware requirements; anti-affinity can improve application resilience. Hard constraints should be used only when enough eligible hosts remain for maintenance and HA.

### Architecture / Mental Model
```text
Affinity:
VM → host group

Anti-affinity:
VM-A != VM-B on same host

More constraints
  ↓
fewer scheduling options
```

### Commands / Code / Configuration
```text
VM/Group | Rule | Hard/Soft | Reason | Eligible Hosts | Failure Impact
```

### Expected Behavior
Every placement rule has a documented reason and enough eligible hosts to survive expected maintenance/failure.

### Why It Works
Scheduling can only choose from hosts that satisfy all constraints.

### Real Production Example
Two redundant application VMs have a hard affinity to the same small host group, undermining HA flexibility.

### Troubleshooting Workflow
```text
cannot place/migrate
  ↓
capacity
  ↓
affinity/anti-affinity
  ↓
eligible hosts
  ↓
device/licensing constraints
```

### Best Practice
Use hard placement rules only for true non-negotiable requirements.

---

## Advanced Deep Dive 34 — Acropolis Dynamic Scheduling and Hotspots

### Concept and Detailed Explanation
Dynamic scheduling can rebalance workloads based on resource pressure, but manual operators still need to identify which resource is actually constrained before forcing migrations.

### Architecture / Mental Model
```text
Metrics
  ↓
detect hotspot
  ↓
evaluate alternatives
  ↓
migrate/rebalance
  ↓
observe new state
```

### Commands / Code / Configuration
```text
Compare:
VM CPU
Host CPU
CVM CPU
Storage latency
Network throughput
before and after movement
```

### Expected Behavior
Rebalancing reduces the actual bottleneck rather than simply moving the symptom.

### Why It Works
CPU, memory, storage, and network hotspots have different causes and different useful migrations.

### Real Production Example
A host shows high CPU because its CVM is busy during re-replication; moving unrelated compute-light VMs changes little.

### Troubleshooting Workflow
```text
hotspot
  ↓
identify constrained resource
  ↓
top consumers
  ↓
background activity
  ↓
placement options
  ↓
migrate/right-size/add capacity
```

### Best Practice
Diagnose the resource bottleneck before overriding automated placement.

---

## Advanced Deep Dive 35 — Volume Groups and Orphan Risk

### Concept and Detailed Explanation
Volume groups are block-oriented storage objects with their own lifecycle. They can outlive VMs and therefore require ownership, protection, capacity, and cleanup governance.

### Architecture / Mental Model
```text
Application VM
   |
Volume Group
├── data disk
├── log disk
└── archive disk
   |
AOS / DSF
```

### Commands / Code / Configuration
```text
Volume Group | Attached VM(s) | Capacity | Owner | Protection | Backup
```

### Expected Behavior
Every volume group has a known attachment, owner, and data-protection policy.

### Why It Works
Independent storage lifecycles provide flexibility but can create orphaned capacity when VM cleanup is incomplete.

### Real Production Example
A deleted database VM leaves several terabytes of volume-group storage behind because ownership was unclear.

### Troubleshooting Workflow
```text
orphan volume group
  ↓
attachment?
  ↓
owner?
  ↓
backup/retention?
  ↓
application dependency?
  ↓
approved cleanup
```

### Best Practice
Include volume groups in periodic orphan-resource reviews.

---

## Advanced Deep Dive 36 — Snapshots, Recovery Points, and Backups

### Concept and Detailed Explanation
Snapshots and recovery points provide fast local recovery, while remote replication provides site recovery. Independent backups provide historical or cyber-recovery protection. These are complementary controls rather than substitutes.

### Architecture / Mental Model
```text
Production Data
  |
  +-- local recovery point
  +-- remote DR copy
  `-- independent backup / immutable copy
```

### Commands / Code / Configuration
```text
Workload | Local RPO | Remote RPO | Backup Freq | Immutability | Retention | Restore Test
```

### Expected Behavior
Critical workloads have a recovery method that survives the specific failure or attack scenario being modeled.

### Why It Works
Replication can reproduce deletion, corruption, or ransomware; independent backups create a separate recovery path.

### Real Production Example
Ransomware encrypts production data and the encrypted changes replicate to the DR site, but an immutable backup still provides a clean point.

### Troubleshooting Workflow
```text
recovery event
  ↓
failure type
  ↓
local point clean?
  ↓
remote point clean?
  ↓
backup/immutable copy?
  ↓
restore and validate
```

### Best Practice
Design backup and DR together, but never treat them as the same control.

---

## Advanced Deep Dive 37 — Protection Policies as Intent

### Concept and Detailed Explanation
Protection policies should define scope, RPO, retention, replication target, and mode. Categories can attach policy dynamically so newly created workloads inherit protection automatically.

### Architecture / Mental Model
```text
Category: Criticality=Tier1
        |
Protection Policy
        |
local recovery points
remote replication
retention
        |
Recovery Plan
```

### Commands / Code / Configuration
```text
Policy:
Scope:
Local RPO:
Remote RPO:
Retention:
Target:
Mode:
Owner:
Test Frequency:
```

### Expected Behavior
A new workload with the correct category automatically receives the expected protection behavior.

### Why It Works
Intent-based protection reduces manual omissions and expresses business recovery objectives directly.

### Real Production Example
A new production database is created but never added to a legacy manually maintained snapshot job.

### Troubleshooting Workflow
```text
VM not protected
  ↓
category/scope
  ↓
policy
  ↓
target
  ↓
replication state
  ↓
capacity/network
```

### Best Practice
Make protection assignment part of workload onboarding.

---

## Advanced Deep Dive 38 — Asynchronous Replication and Achieved RPO

### Concept and Detailed Explanation
The configured replication interval is only a target. If the WAN, source, or target cannot complete transfer fast enough, actual replication lag can exceed the nominal RPO.

### Architecture / Mental Model
```text
Primary
  |
recovery point
  |
WAN
  |
DR target

Configured 30 min
Actual lag may be >30 min
```

### Commands / Code / Configuration
```text
Monitor:
last successful recovery point
configured interval
transfer duration
backlog
WAN throughput
target capacity
```

### Expected Behavior
Achieved replication lag remains inside the business RPO under normal and degraded conditions.

### Why It Works
RPO is about how much data could be lost, not simply how often a job is scheduled.

### Real Production Example
A 15-minute policy is 90 minutes behind because the WAN is saturated.

### Troubleshooting Workflow
```text
replication behind
  ↓
source recovery point?
  ↓
WAN reachability/bandwidth
  ↓
target health/capacity
  ↓
backlog
  ↓
policy cadence
```

### Best Practice
Alert on actual replication lag, not only job-failure status.

---

## Advanced Deep Dive 39 — NearSync Throughput Planning

### Concept and Detailed Explanation
NearSync reduces RPO by creating and transferring recovery points more frequently. The source change rate must remain below sustainable replication throughput with enough margin for bursts and transient network problems.

### Architecture / Mental Model
```text
Workload change rate
   |
frequent recovery points
   |
WAN
   |
DR target
```

### Commands / Code / Configuration
```text
Inputs:
Change rate MB/s
WAN usable MB/s
Latency
Packet loss
Target write capability
Required RPO
```

### Expected Behavior
The replication path sustains average and burst change rate with headroom.

### Why It Works
A tighter RPO creates less time to catch up after a slowdown.

### Real Production Example
A workload changes 800 GB/hour while the effective WAN can move only 500 GB/hour; the lag grows indefinitely.

### Troubleshooting Workflow
```text
NearSync lag
  ↓
change rate
  ↓
WAN throughput
  ↓
latency/loss
  ↓
target performance
  ↓
competing traffic
```

### Best Practice
Validate low-RPO designs with measured change rate and effective throughput.

---

## Advanced Deep Dive 40 — Synchronous / Metro Protection

### Concept and Detailed Explanation
Synchronous protection coordinates local and remote durability before acknowledging writes. It can support extremely low data-loss objectives but depends heavily on inter-site latency, bandwidth, and quorum/witness design.

### Architecture / Mental Model
```text
Site A write
  |
local persistence
  +
remote persistence
  |
ACK

Witness/quorum
prevents split-brain
```

### Commands / Code / Configuration
```text
Design:
RTT latency
bandwidth
loss
witness placement
failure domains
application write-latency budget
site isolation behavior
```

### Expected Behavior
The application meets its latency SLO while synchronous protection remains healthy.

### Why It Works
Remote acknowledgement adds network distance directly to the write path.

### Real Production Example
A database requiring very low storage latency may be incompatible with a distant synchronous site.

### Troubleshooting Workflow
```text
Metro issue
  ↓
inter-site latency/loss
  ↓
witness/quorum
  ↓
site health
  ↓
storage latency
  ↓
application SLO
```

### Best Practice
Choose synchronous protection only when the network and application latency budgets support it.

---

## Advanced Deep Dive 41 — Recovery Plans and Dependency Order

### Concept and Detailed Explanation
A recovery plan must recover application dependencies in the correct order and validate readiness between stages. VM power-on order alone is insufficient.

### Architecture / Mental Model
```text
1. DNS / AD / Core
      ↓
2. Database
      ↓
3. Application
      ↓
4. Web / API
      ↓
External Traffic
```

### Commands / Code / Configuration
```text
Recovery plan:
boot order
readiness condition
network mapping
IP/DNS changes
application health check
data consistency check
external cutover
```

### Expected Behavior
Each tier starts only after its dependency is actually ready.

### Why It Works
Downstream services can be powered on while still unusable if identity, database, or network dependencies are not ready.

### Real Production Example
A web server starts immediately but fails health checks because the database is still in crash recovery.

### Troubleshooting Workflow
```text
DR plan fails
  ↓
which group?
  ↓
VM power?
  ↓
network mapping?
  ↓
dependency ready?
  ↓
DNS/IP?
  ↓
application test?
```

### Best Practice
Use readiness checks rather than fixed sleep timers where possible.

---

## Advanced Deep Dive 42 — Failback and Reverse Replication

### Concept and Detailed Explanation
After failover, the DR site becomes the active source of truth. Returning to the primary site requires reverse synchronization, validation, a controlled cutover, and restoration of the original protection direction.

### Architecture / Mental Model
```text
Normal:
Primary → DR

Failover:
DR active

Failback:
DR data
  ↓ reverse sync
Primary updated
  ↓ validate
planned cutover
  ↓
restore protection
```

### Commands / Code / Configuration
```text
Failback:
1. identify active source of truth;
2. synchronize back;
3. validate primary;
4. freeze/cut over;
5. update DNS/network;
6. verify app;
7. restore DR protection.
```

### Expected Behavior
The primary is not made active until it contains current, consistent production data.

### Why It Works
Failover creates new writes at DR; powering on an old primary without synchronization can lose those changes.

### Real Production Example
Users process orders at DR for several days, then an unsynchronized primary is brought back online with stale database state.

### Troubleshooting Workflow
```text
failback
  ↓
source of truth
  ↓
reverse sync
  ↓
consistency validation
  ↓
planned cutover
  ↓
application verification
```

### Best Practice
Test failback during DR exercises, not only failover.

---

## Advanced Deep Dive 43 — Isolated DR Testing

### Concept and Detailed Explanation
DR tests should validate real application recovery without colliding with production IP addresses, DNS, or write paths. Isolated test networking is essential.

### Architecture / Mental Model
```text
Production
   |
protected copy
   |
isolated DR test network
   |
recovered VMs
   |
application validation
   |
clean teardown
```

### Commands / Code / Configuration
```text
Evidence:
selected recovery point
VM boot
network mapping
dependency readiness
database consistency
application transaction
measured RTO
cleanup
```

### Expected Behavior
The test proves recoverability without disrupting live production.

### Why It Works
Recovery copies are useful only if they can actually boot, connect, and complete application transactions.

### Real Production Example
A test domain controller boots onto the production network and causes identity conflicts.

### Troubleshooting Workflow
```text
DR test
  ↓
isolated network
  ↓
DNS/IP mapping
  ↓
data writes isolated
  ↓
validate application
  ↓
collect RTO
  ↓
clean up
```

### Best Practice
Treat test-network isolation as a mandatory DR control.

---

## Advanced Deep Dive 44 — NC2 Operating Model

### Concept and Detailed Explanation
Nutanix Cloud Clusters extends the Nutanix operating model into supported public-cloud infrastructure. Operational consistency is valuable, but public-cloud networking, quotas, regional design, data transfer, and cost still matter.

### Architecture / Mental Model
```text
On-Prem NCI
   |
Prism / Nutanix operations
   |
NC2 cluster
   |
Public-cloud network / compute / billing
```

### Commands / Code / Configuration
```text
NC2 design:
Cloud
Region
AZs
Network CIDRs
Connectivity
DNS
Identity
Cluster size
DR mode
Monthly cost
Exit plan
```

### Expected Behavior
You can explain which responsibilities remain Nutanix responsibilities and which remain public-cloud/customer responsibilities.

### Why It Works
NC2 runs the Nutanix stack on cloud infrastructure rather than removing the cloud-provider underlay.

### Real Production Example
A technically successful DR design becomes financially unsuitable because egress and idle-cluster cost were never modeled.

### Troubleshooting Workflow
```text
NC2 issue
  ↓
Nutanix cluster health
  ↓
cloud resource/quota
  ↓
VPC/VNet routing/security
  ↓
hybrid connectivity
  ↓
cost/capacity
```

### Best Practice
Include provider quotas and cost in NC2 architecture reviews.

---

## Advanced Deep Dive 45 — Hybrid Connectivity and Routing

### Concept and Detailed Explanation
Hybrid multicloud depends on correct routing, DNS, MTU, security, and address planning between on-prem and cloud. Overlapping CIDRs are a common source of migration and DR complexity.

### Architecture / Mental Model
```text
On-Prem NCI
   |
edge/firewall
   |
VPN / private circuit
   |
Cloud VPC/VNet
   |
NC2
```

### Commands / Code / Configuration
```text
Network plan:
on-prem CIDRs
NC2 CIDRs
route propagation
firewall rules
DNS
MTU
BGP/static routes
failover path
```

### Expected Behavior
Application dependencies remain reachable after migration/failover without ambiguous routes.

### Why It Works
Hybrid infrastructure adds a routed failure domain between workload and dependency.

### Real Production Example
A recovered VM in NC2 cannot reach on-prem identity because the DR subnet is not advertised over the hybrid link.

### Troubleshooting Workflow
```text
hybrid reachability
  ↓
VM subnet
  ↓
cloud route
  ↓
hybrid gateway
  ↓
on-prem firewall
  ↓
return route
```

### Best Practice
Avoid overlapping address space before it becomes a DR emergency.

---

## Advanced Deep Dive 46 — LCM Inventory as Lifecycle Foundation

### Concept and Detailed Explanation
LCM needs an accurate inventory of current AOS, AHV, firmware, and platform components before it can recommend compatible lifecycle actions. Inventory errors should be resolved before upgrade planning.

### Architecture / Mental Model
```text
Platform components
      |
LCM inventory
      |
compatibility graph
      |
available updates
```

### Commands / Code / Configuration
```text
1. run LCM inventory
2. resolve inventory errors
3. record current versions
4. review compatible target
5. run prechecks
6. schedule change
```

### Expected Behavior
LCM shows a complete, current inventory without unresolved unknown components.

### Why It Works
Upgrade compatibility depends on the exact starting state.

### Real Production Example
A node with failed inventory is accidentally excluded from compatibility analysis and becomes the source of an upgrade issue.

### Troubleshooting Workflow
```text
inventory fails
  ↓
cluster/NCC health
  ↓
repository/network
  ↓
credentials
  ↓
component detection
  ↓
space
  ↓
rerun
```

### Best Practice
Never plan a broad upgrade from stale inventory.

---

## Advanced Deep Dive 47 — LCM Prechecks and Maintenance Headroom

### Concept and Detailed Explanation
Rolling lifecycle operations temporarily remove capacity or redundancy. LCM prechecks must be combined with operator verification of NCC health, resilience, free capacity, and workload mobility.

### Architecture / Mental Model
```text
Healthy cluster
  |
NCC
resilience
N+1 capacity
no major rebuild
  |
LCM prechecks
  |
rolling change
```

### Commands / Code / Configuration
```text
Pre-upgrade:
NCC
resilience
critical alerts
free capacity
HA headroom
replication status
backup status
compatibility
maintenance window
```

### Expected Behavior
The cluster remains inside safe compute, storage, and network limits when one node is in maintenance.

### Why It Works
Rolling upgrade assumes surviving resources can absorb the temporarily unavailable node.

### Real Production Example
A three-node cluster begins an upgrade at high RAM utilization and surviving hosts cannot comfortably absorb workloads.

### Troubleshooting Workflow
```text
precheck warning
  ↓
understand risk
  ↓
capacity/resilience
  ↓
correct issue
  ↓
rerun NCC/LCM
```

### Best Practice
Do not override health warnings merely to meet a change window.

---

## Advanced Deep Dive 48 — Rolling Upgrade Mechanics

### Concept and Detailed Explanation
A rolling upgrade updates one node/component at a time and validates recovery before progressing. The safety property depends on preserving quorum, protection, and workload capacity at every step.

### Architecture / Mental Model
```text
Node 1 update/reboot
  ↓
validate host + CVM + cluster
  ↓
Node 2
  ↓
validate
  ↓
Node 3
```

### Commands / Code / Configuration
```text
After each node:
host healthy
CVM healthy
cluster services healthy
network links healthy
resilience healthy
VMs stable
NCC/LCM acceptable
```

### Expected Behavior
Each node returns fully healthy before the next node is removed from service.

### Why It Works
Sequential changes limit blast radius and preserve redundancy.

### Real Production Example
An operator manually reboots several hosts simultaneously to save time and defeats the rolling-availability design.

### Troubleshooting Workflow
```text
rolling upgrade problem
  ↓
stop progression
  ↓
stabilize current node
  ↓
cluster health
  ↓
resilience
  ↓
supported rollback/forward fix
```

### Best Practice
Never parallelize node maintenance unless the supported procedure explicitly allows it.

---

## Advanced Deep Dive 49 — Dark-Site Lifecycle Management

### Concept and Detailed Explanation
Disconnected environments still need controlled software supply chains. Lifecycle bundles must be downloaded from trusted sources, verified, transferred securely, staged, and approved before use.

### Architecture / Mental Model
```text
Vendor source
  |
approved download station
  |
hash/signature verification
  |
secure transfer
  |
dark-site repository
  |
LCM
```

### Commands / Code / Configuration
```text
Checklist:
exact target versions
bundle provenance
hash/signature
malware scan
repository capacity
approval
rollback artifacts
```

### Expected Behavior
The offline cluster discovers only approved, complete bundles and does not depend on Internet access during the maintenance window.

### Why It Works
Air-gapping changes distribution mechanics but not authenticity or compatibility requirements.

### Real Production Example
A partially copied firmware bundle causes LCM inventory/update failure during the window.

### Troubleshooting Workflow
```text
dark-site failure
  ↓
bundle completeness
  ↓
hash/provenance
  ↓
repository path
  ↓
LCM inventory
  ↓
compatibility
```

### Best Practice
Treat lifecycle bundles as controlled software artifacts.

---

## Advanced Deep Dive 50 — Foundation and Initial Cluster Bring-Up

### Concept and Detailed Explanation
Foundation automates supported node imaging and cluster creation, but it still depends on correct BMC access, network design, IP uniqueness, DNS/NTP, compatible images, and supported hardware.

### Architecture / Mental Model
```text
Bare Nodes
  |
BMC + imaging network
  |
Foundation
  |
AHV + CVM/AOS
  |
cluster creation
  |
Prism + NCC validation
```

### Commands / Code / Configuration
```text
Node | Host IP | CVM IP | BMC IP | VLAN | GW | DNS | NTP | AOS | AHV
```

### Expected Behavior
Every node joins with the intended identity and network configuration and the cluster passes baseline health checks.

### Why It Works
Automation reproduces the supplied design; it cannot make an incorrect IP/VLAN plan correct.

### Real Production Example
Two nodes receive the same CVM address and the cluster cannot form reliably.

### Troubleshooting Workflow
```text
Foundation failure
  ↓
BMC
  ↓
imaging network
  ↓
IP uniqueness
  ↓
DNS/NTP
  ↓
image compatibility
  ↓
hardware
```

### Best Practice
Validate the complete IP/VLAN table before imaging the first node.

---

## Advanced Deep Dive 51 — Cluster Expansion and Rebalancing

### Concept and Detailed Explanation
Adding nodes increases compute and storage resources, but the platform also rebalances data and workload distribution. Expansion must account for rack power, switch ports, IPs, version compatibility, and temporary rebalance traffic.

### Architecture / Mental Model
```text
Existing Cluster
   +
New Node
   |
validate
   |
join
   |
capacity increases
   |
background rebalance
```

### Commands / Code / Configuration
```text
Before:
NCC
LCM inventory
version compatibility
IP/VLAN
rack/PDU
ToR ports
BMC

After:
cluster status
NCC
host inventory
capacity
rebalance activity
```

### Expected Behavior
The new node joins healthy and rebalance completes without unacceptable workload impact.

### Why It Works
Distributed systems move data and responsibilities to exploit new capacity.

### Real Production Example
Expansion during peak production causes rebalance traffic to compete with a latency-sensitive database.

### Troubleshooting Workflow
```text
expansion issue
  ↓
node health
  ↓
version/firmware
  ↓
network
  ↓
storage
  ↓
rebalance load
```

### Best Practice
Schedule expansion with enough performance headroom for rebalancing.

---

## Advanced Deep Dive 52 — Data-at-Rest Encryption and KMS

### Concept and Detailed Explanation
Encryption protects data on storage media, but encrypted data remains dependent on key availability. Key-management architecture therefore requires HA, backup, certificate trust, access control, and DR planning.

### Architecture / Mental Model
```text
VM Data
  |
AOS encryption
  |
encrypted media
  |
KMS / supported key service
  |
protected keys
```

### Commands / Code / Configuration
```text
KMS design:
provider
HA
network path
certificate trust
backup
restore
admin separation
rotation
DR availability
```

### Expected Behavior
The cluster can access required keys during normal operation, maintenance, and documented recovery scenarios.

### Why It Works
Encryption without recoverable keys converts hardware/data availability into an unrecoverable data-access problem.

### Real Production Example
A DR site has replicated encrypted data but no functioning key service, so the data cannot be used.

### Troubleshooting Workflow
```text
encryption access issue
  ↓
cluster health
  ↓
KMS reachability
  ↓
TLS/trust
  ↓
key existence/version
  ↓
KMS HA/backup
```

### Best Practice
Test KMS recovery as part of DR.

---

## Advanced Deep Dive 53 — Management Plane Segmentation

### Concept and Detailed Explanation
Prism, CVMs, AHV management, BMC, Foundation, LCM, backup, and KMS are privileged infrastructure surfaces. They should not be openly reachable from ordinary user or VM networks.

### Architecture / Mental Model
```text
Admin / Bastion
      |
Management Firewall
      |
+-----+-----+------+-----+
Prism CVM   AHV    BMC   LCM/KMS
```

### Commands / Code / Configuration
```text
Review:
management subnet
allowed sources
MFA/jump host
TLS
SSH
BMC access
logging
patch process
```

### Expected Behavior
Only approved administrative sources can reach management interfaces.

### Why It Works
Compromise of management interfaces can grant control over compute, storage, VM lifecycle, or physical power.

### Real Production Example
A malware-infected user VM can reach CVM SSH because the management network is not segmented.

### Troubleshooting Workflow
```text
management exposure
  ↓
source/destination reachability
  ↓
firewall/ACL
  ↓
service exposure
  ↓
credentials
  ↓
segment/restrict
```

### Best Practice
Route privileged management through controlled administrative networks.

---

## Advanced Deep Dive 54 — BMC / Out-of-Band Security

### Concept and Detailed Explanation
BMC/IPMI/Redfish interfaces can control physical power and firmware independently of AHV. BMC credentials and networks should therefore be treated as equivalent to physical-console access.

### Architecture / Mental Model
```text
Admin
  |
isolated OOB network
  |
BMC / Redfish / IPMI
  |
physical server
```

### Commands / Code / Configuration
```text
Controls:
separate VLAN/VRF
unique credentials
certificate management
firmware updates
audit
restricted source networks
no Internet exposure
```

### Expected Behavior
BMC interfaces are reachable only from authorized management systems.

### Why It Works
Out-of-band control bypasses the hypervisor and can affect a node even when the host OS is unavailable.

### Real Production Example
Compromised BMC credentials allow an attacker to power off multiple cluster nodes despite strong Prism RBAC.

### Troubleshooting Workflow
```text
BMC compromise
  ↓
isolate OOB
  ↓
rotate credentials
  ↓
review audit/power events
  ↓
firmware/integrity
  ↓
restore carefully
```

### Best Practice
Treat BMC access as one of the highest-privilege infrastructure controls.

---

## Advanced Deep Dive 55 — Prism Central v4 API Automation

### Concept and Detailed Explanation
Modern Prism Central automation increasingly uses v4 APIs. Production automation should use dedicated identities, TLS verification, task tracking, bounded retries, and reconciliation. Exact endpoint paths and schemas must match the installed release.

### Architecture / Mental Model
```text
Python / Terraform / curl
        |
TLS
        |
Prism Central v4 API
        |
resource request
        |
async task
        |
poll task/result
```

### Commands / Code / Configuration
```text
# Generic pattern; use installed-release documentation for exact endpoint/auth.
curl --fail --silent --show-error   --cacert /path/to/ca.pem   -H "Accept: application/json"   "https://prism-central.example/api/<v4-resource>"
```

### Expected Behavior
The client verifies TLS, uses a dedicated machine identity, captures task identifiers, and handles non-success responses.

### Why It Works
Cloud infrastructure APIs are asynchronous and privileged; clients must track final state rather than equating request acceptance with success.

### Real Production Example
A script retries VM creation after a timeout without checking task state and creates duplicate VMs.

### Troubleshooting Workflow
```text
API failure
  ↓
identity
  ↓
TLS
  ↓
endpoint/version
  ↓
HTTP status/body
  ↓
task ID
  ↓
actual resource state
```

### Best Practice
Build API automation around reconciliation and task tracking.

---

## Advanced Deep Dive 56 — Idempotent Infrastructure Automation

### Concept and Detailed Explanation
Idempotent automation compares desired and actual state. The second run should make no duplicate resources and should detect drift instead of blindly recreating objects.

### Architecture / Mental Model
```text
Desired VM app01
   |
GET actual
   |
missing → create
matches → no-op
drifted → update/replace/fail
```

### Commands / Code / Configuration
```text
desired = {"name": "app01", "cpu": 4, "memory_gib": 16}
current = find_vm(desired["name"])

if current is None:
    create_vm(desired)
else:
    validate_or_reconcile(current, desired)
```

### Expected Behavior
Running the workflow twice results in one correct VM rather than duplicates.

### Why It Works
Distributed API timeouts can hide whether a create request already committed, so state reconciliation is safer than blind retries.

### Real Production Example
A CI job times out after VM creation and produces a second VM on retry because it never queried actual state.

### Troubleshooting Workflow
```text
ambiguous timeout
  ↓
query by ID/name/tag
  ↓
inspect task
  ↓
determine committed state
  ↓
reconcile
```

### Best Practice
Persist resource IDs and ownership metadata immediately.

---

## Advanced Deep Dive 57 — API Secret Redaction and Audit

### Concept and Detailed Explanation
Automation logs should contain operation, entity, status, task/request ID, latency, and safe error details—but never passwords, API keys, tokens, or secret payloads.

### Architecture / Mental Model
```text
API request
  |
redaction layer
  |
safe log:
operation
resource ID
task ID
status
latency
```

### Commands / Code / Configuration
```text
SENSITIVE = {
    "authorization",
    "token",
    "password",
    "api_key",
    "secret",
}
```

### Expected Behavior
Support logs remain useful without containing reusable credentials.

### Why It Works
Bearer credentials copied into logs become attack material when logs are shared or retained.

### Real Production Example
Debug logging captures an automation API credential and sends it to a ticketing system.

### Troubleshooting Workflow
```text
secret exposure
  ↓
revoke/rotate
  ↓
restrict/remove logs
  ↓
audit use
  ↓
fix redaction
```

### Best Practice
Redact credentials before logs leave the application process.

---

## Advanced Deep Dive 58 — Performance Troubleshooting by Layer

### Concept and Detailed Explanation
A slow application can originate in the guest, AHV scheduling, host memory/CPU, CVM, DSF, physical media, network, replication, or background healing. Performance diagnosis should correlate the same time window across layers.

### Architecture / Mental Model
```text
Application
  |
Guest
  |
VM
  |
AHV Host
  |
CVM
  |
DSF
  |
Media / Network
```

### Commands / Code / Configuration
```text
Collect same time window:
Guest: top, vmstat, iostat
Prism: VM CPU/RAM/storage
Host CPU/RAM/network
CVM CPU
Cluster storage latency/IOPS
alerts/tasks/events
```

### Expected Behavior
You identify the first layer where abnormal latency or contention appears.

### Why It Works
Layered systems propagate lower-level delays upward into application symptoms.

### Real Production Example
Many VMs across all hosts show high disk latency while a large re-replication job is active, pointing to cluster storage pressure.

### Troubleshooting Workflow
```text
slow workload
  ↓
blast radius
  ↓
guest metrics
  ↓
host metrics
  ↓
CVM/storage
  ↓
network
  ↓
background tasks
```

### Best Practice
Compare an affected VM with a healthy peer and the cluster-wide timeline.

---

## Advanced Deep Dive 59 — Storage Latency Decomposition

### Concept and Detailed Explanation
Storage latency should be interpreted together with IOPS, throughput, queueing, CVM CPU, physical-device health, network errors, snapshots, replication, and rebuild activity. One latency number does not explain the bottleneck.

### Architecture / Mental Model
```text
Application I/O
   |
Guest queue
   |
vDisk
   |
CVM / AOS
   |
network / media
   |
replicas
```

### Commands / Code / Configuration
```text
Metric | Before | Incident | After
IOPS
Throughput
Latency
CVM CPU
Disk errors
Network drops
Rebuild state
Protection activity
```

### Expected Behavior
The incident can be tied to a measurable bottleneck or recovery activity rather than a generic statement that storage is slow.

### Why It Works
Storage latency is the sum of work and waiting across several infrastructure layers.

### Real Production Example
Latency rises during node re-replication because surviving nodes handle application I/O and healing traffic simultaneously.

### Troubleshooting Workflow
```text
latency
  ↓
one VM or cluster?
  ↓
IOPS/throughput
  ↓
CVM CPU
  ↓
media health
  ↓
network
  ↓
rebuild/DR/backup
```

### Best Practice
Correlate latency with workload intensity and background activity.

---

## Advanced Deep Dive 60 — Network Troubleshooting by Blast Radius

### Concept and Detailed Explanation
The affected scope is a strong diagnostic signal. One VM suggests guest/vNIC/policy. Many VMs on one host suggest host uplink/bond. One VLAN across all hosts suggests trunk/gateway. One VPC or category group suggests Flow policy.

### Architecture / Mental Model
```text
Scope
 |
+-- one VM → guest/vNIC/Flow
+-- one host → bond/NIC/ToR port
+-- one VLAN → trunk/gateway
+-- one VPC → logical routing/policy
+-- whole cluster → upstream/core
```

### Commands / Code / Configuration
```text
Evidence:
affected VM list
host placement
network/VLAN/VPC
Flow categories
NIC counters
switch alarms
gateway reachability
```

### Expected Behavior
You localize the probable layer before changing network configuration.

### Why It Works
Shared infrastructure produces recognizable failure patterns.

### Real Production Example
Every VM on Host 2 loses connectivity while equivalent VMs on other hosts are healthy, making Host 2's network path the first focus.

### Troubleshooting Workflow
```text
network outage
  ↓
count affected
  ↓
common host?
  ↓
common VLAN/VPC?
  ↓
common Flow policy?
  ↓
common gateway/uplink?
```

### Best Practice
Use scope correlation before packet capture or policy changes.

---

## Advanced Deep Dive 61 — Prism Unavailable: Management vs Runtime

### Concept and Detailed Explanation
Prism UI or API unavailability is a management-plane symptom. The first question is whether VM execution and storage remain healthy. Avoid turning a management issue into a workload outage by restarting unrelated services.

### Architecture / Mental Model
```text
Prism unavailable
   |
check applications/VMs
   |
check cluster services
   |
check CVM/network/TLS
   |
repair management plane
```

### Commands / Code / Configuration
```text
cluster status
ncc health_checks run_all

Check:
application reachability
DNS
TLS certificate
CVM state
management network
```

### Expected Behavior
You know whether the incident is management-only or affects cluster runtime.

### Why It Works
Management and data-plane functions can fail independently.

### Real Production Example
A Prism certificate issue prevents browser/API access while VMs and storage continue operating.

### Troubleshooting Workflow
```text
Prism down
  ↓
workload runtime?
  ↓
cluster status
  ↓
CVM health
  ↓
management network
  ↓
DNS/TLS
  ↓
supported recovery
```

### Best Practice
Prove workload state before restarting anything.

---

## Advanced Deep Dive 62 — NCC as a Diagnostic Framework

### Concept and Detailed Explanation
NCC is most useful as structured evidence. A FAIL should lead to understanding the named check, affected entity, operational consequence, and supported remediation. WARN does not always mean the same severity, so context matters.

### Architecture / Mental Model
```text
NCC Result
  |
PASS / INFO / WARN / FAIL
  |
check name
  |
affected entity
  |
risk
  |
supported correction
  |
rerun
```

### Commands / Code / Configuration
```text
ncc health_checks run_all
```

### Expected Behavior
After correction, the specific failed health check and related platform health return to acceptable state.

### Why It Works
NCC encodes known platform health/configuration expectations.

### Real Production Example
A network redundancy warning is ignored before maintenance; a single NIC failure during the window isolates a host.

### Troubleshooting Workflow
```text
NCC issue
  ↓
read check name/details
  ↓
identify entity
  ↓
understand consequence
  ↓
collect supporting evidence
  ↓
correct
  ↓
rerun
```

### Best Practice
Never apply random fixes simply because an NCC result is red.

---

## Advanced Deep Dive 63 — cluster status as First-Line Triage

### Concept and Detailed Explanation
`cluster status` gives a fast comparison of service participation across CVMs. It is especially useful for identifying whether one CVM differs from its peers before any restart decision.

### Architecture / Mental Model
```text
CVM1 services
CVM2 services
CVM3 services
   |
compare
   |
local anomaly or cluster-wide anomaly
```

### Commands / Code / Configuration
```text
cluster status

Record:
timestamp
CVMs
service state
missing/unresponsive services
```

### Expected Behavior
A stable cluster shows expected service participation on intended CVMs.

### Why It Works
Peer comparison quickly distinguishes local and distributed failures.

### Real Production Example
One CVM is missing one service while others are healthy; targeted investigation is safer than restarting the full cluster.

### Troubleshooting Workflow
```text
cluster status anomaly
  ↓
which CVM?
  ↓
host health
  ↓
CVM CPU/RAM/network
  ↓
Prism alert
  ↓
service-specific evidence
```

### Best Practice
Capture `cluster status` output before disruptive intervention.

---

## Advanced Deep Dive 64 — One CVM Down Scenario

### Concept and Detailed Explanation
Loss of one CVM should be treated as both a service redistribution event and a resilience/capacity event. The cluster may remain available, but surviving CVMs can carry more load and the root cause still needs correction.

### Architecture / Mental Model
```text
Node 1 CVM down
   |
other CVMs continue services
   |
VMs may remain online
   |
verify performance/resilience
   |
recover CVM/root cause
```

### Commands / Code / Configuration
```text
cluster status
ncc health_checks run_all

Prism:
affected node
CVM VM state
storage latency
resilience alerts
```

### Expected Behavior
The cluster remains available if designed for the failure and surviving CVMs remain within safe load.

### Why It Works
Distributed CVM services avoid dependence on one controller appliance.

### Real Production Example
A CVM fails because of a host issue; surviving CVMs keep storage available but show elevated CPU until recovery.

### Troubleshooting Workflow
```text
CVM down
  ↓
one or many?
  ↓
host healthy?
  ↓
CVM state
  ↓
cluster status
  ↓
storage/resilience
  ↓
supported recovery
```

### Best Practice
Do not manually shut down additional CVMs while one is already unavailable.

---

## Advanced Deep Dive 65 — One AHV Host Down Scenario

### Concept and Detailed Explanation
Host failure combines loss of tenant VM execution and that node's CVM/storage contribution. AHV HA restarts eligible VMs while AOS uses surviving copies and restores protection.

### Architecture / Mental Model
```text
AHV Host fails
  |
CVM lost
  |
VMs stop
  |
HA restarts VMs
  |
AOS serves replicas
  |
re-replication
```

### Commands / Code / Configuration
```text
Prism:
host state
affected VM list
HA tasks
storage resilience
rebuild progress

cluster status
ncc health_checks run_all
```

### Expected Behavior
Critical VMs restart inside the expected RTO and cluster storage returns to full protection without exhausting headroom.

### Why It Works
Host failure affects both compute and distributed-storage resources.

### Real Production Example
A host motherboard fails; VM HA succeeds, but surviving nodes are heavily loaded because N+1 capacity was too small.

### Troubleshooting Workflow
```text
host down
  ↓
hardware/BMC
  ↓
VM HA
  ↓
destination capacity
  ↓
CVM/storage resilience
  ↓
application verification
```

### Best Practice
Maintain enough headroom to absorb the failure of the domain you promise to tolerate.

---

## Advanced Deep Dive 66 — Disk Failure and Re-Replication

### Concept and Detailed Explanation
A disk failure workflow is not complete when applications remain online. Operators must verify the hardware fault, current protection level, free healing capacity, re-replication progress, and eventual return to healthy state.

### Architecture / Mental Model
```text
Disk fails
  |
surviving replica serves data
  |
hardware alert
  |
re-replication
  |
replace/remediate
  |
protection restored
```

### Commands / Code / Configuration
```text
Prism:
hardware
storage/resilience
tasks/events
capacity

ncc health_checks run_all
```

### Expected Behavior
Protection returns to the intended level and no persistent device or resilience alert remains.

### Why It Works
Distributed replicas allow the cluster to rebuild across healthy resources rather than waiting for a single replacement target.

### Real Production Example
A failed disk is replaced, but low free capacity slows re-protection and extends the vulnerability window.

### Troubleshooting Workflow
```text
disk failure
  ↓
identify device/node
  ↓
resilience
  ↓
free capacity
  ↓
re-replication
  ↓
replace hardware
  ↓
verify clean state
```

### Best Practice
Capacity headroom is part of disk-failure resilience.

---

## Advanced Deep Dive 67 — Reduced Resilience as a Change-Control Blocker

### Concept and Detailed Explanation
When cluster resilience is reduced, elective node maintenance, upgrades, and disruptive testing should normally stop until protection is restored. Maintenance intentionally removes redundancy and should not be stacked on top of an existing fault.

### Architecture / Mental Model
```text
Existing fault
  |
reduced resilience
  |
STOP elective maintenance
  |
restore protection
  |
verify healthy
  |
resume change
```

### Commands / Code / Configuration
```text
Change gate:
if resilience != healthy:
    stop
    investigate
    restore
    rerun NCC
```

### Expected Behavior
No planned node removal begins until the required protection and capacity state is healthy.

### Why It Works
Combining maintenance with an unresolved fault can turn a tolerated first failure into a serious second failure.

### Real Production Example
A firmware update takes one host offline while another node has an unresolved storage fault.

### Troubleshooting Workflow
```text
maintenance request
  ↓
resilience status
  ↓
hardware alerts
  ↓
capacity
  ↓
if degraded: STOP
  ↓
restore health
```

### Best Practice
Make resilience a formal maintenance prerequisite.

---

## Advanced Deep Dive 68 — Capacity Forecasting by Bottleneck

### Concept and Detailed Explanation
HCI scales multiple resources together, but workload growth is rarely balanced. CPU, RAM, storage, IOPS, network, or DR bandwidth may become the limiting resource first. Forecast both normal and N-1 states.

### Architecture / Mental Model
```text
CPU forecast
RAM forecast
Storage forecast
IOPS
Network
DR bandwidth
CVM reserve
HA reserve
   |
earliest bottleneck
```

### Commands / Code / Configuration
```text
Month | CPU Peak | RAM Peak | Storage | IOPS | DR Lag | N-1 Headroom
```

### Expected Behavior
Planning identifies the first limiting resource and a date by which expansion or right-sizing must occur.

### Why It Works
A cluster can be storage-rich but memory-full, or compute-rich but constrained by replication bandwidth.

### Real Production Example
Storage is only 55% used, but RAM growth means the cluster will violate N+1 headroom next quarter.

### Troubleshooting Workflow
```text
capacity warning
  ↓
which resource?
  ↓
normal trend
  ↓
N-1 trend
  ↓
growth rate
  ↓
procurement lead time
```

### Best Practice
Trigger expansion from forecasted failure-state headroom, not only from 90% utilization.

---

## Advanced Deep Dive 69 — Backup and Cyber-Recovery Separation

### Concept and Detailed Explanation
Native snapshots and replication are excellent operational recovery tools but can share administrative trust and can propagate malicious changes. Cyber recovery requires independent copies, credential separation, retention/immutability where required, and clean restore testing.

### Architecture / Mental Model
```text
Production NCI
   |
snapshots / DR
   |
Backup Platform
   |
immutable / isolated copy
   |
clean restore environment
```

### Commands / Code / Configuration
```text
Controls:
separate backup admin
MFA
immutable retention
isolated repository
restore network
malware validation
restore tests
```

### Expected Behavior
The organization has at least one recovery path that does not rely on the compromised production management plane.

### Why It Works
Replication protects availability, while independent backup protects against historical corruption and some administrative/security failures.

### Real Production Example
A compromised Prism administrator deletes snapshots and DR copies but cannot delete a separately controlled immutable backup.

### Troubleshooting Workflow
```text
cyber incident
  ↓
isolate production
  ↓
protect backup control plane
  ↓
select clean recovery point
  ↓
restore isolated
  ↓
validate integrity
```

### Best Practice
Separate backup credentials and trust from primary infrastructure administration.

---

## Advanced Deep Dive 70 — Configuration Drift Across Clusters

### Concept and Detailed Explanation
Multicluster environments drift over time in AOS/AHV versions, DNS/NTP, VLAN naming, categories, RBAC, protection policies, and security settings. Drift makes automation, DR, and troubleshooting less predictable.

### Architecture / Mental Model
```text
Desired Standard
   |
+-- Cluster A actual
+-- Cluster B actual
+-- Cluster C actual
   |
drift report
   |
approved remediation
```

### Commands / Code / Configuration
```text
Compare:
AOS/AHV
DNS/NTP
networks/VLANs
categories
RBAC
protection
NCC baseline
LCM status
service accounts
```

### Expected Behavior
Every cluster difference is either intentional/documented or corrected.

### Why It Works
Standardization allows the same runbooks, DR plans, and automation to work across the fleet.

### Real Production Example
The DR cluster uses different category names, so Flow and protection rules behave differently after failover.

### Troubleshooting Workflow
```text
drift
  ↓
desired vs actual
  ↓
intentional?
  ↓
document or remediate
  ↓
revalidate
```

### Best Practice
Maintain machine-readable platform standards where possible.

---

## Advanced Deep Dive 71 — Change Management with Pre/Post Evidence

### Concept and Detailed Explanation
Every infrastructure change should record the before state, expected result, validation plan, and recovery path. This is critical for LCM, networking, Flow, protection, and management-plane changes.

### Architecture / Mental Model
```text
Before:
NCC
cluster status
alerts/tasks
capacity
SLO baseline
   |
Change
   |
After:
same checks
workload transaction
no unexplained new alerts
```

### Commands / Code / Configuration
```text
Change record:
purpose
scope
risk
prerequisites
procedure
expected result
validation
recovery
owner
evidence
```

### Expected Behavior
Post-change health is equal to or better than baseline and required business transactions pass.

### Why It Works
Without baseline evidence, operators cannot distinguish pre-existing faults from change-induced regressions.

### Real Production Example
An upgrade is blamed for a storage warning that had existed for days because no pre-change health capture was taken.

### Troubleshooting Workflow
```text
post-change problem
  ↓
compare pre/post
  ↓
tasks/events
  ↓
affected layer
  ↓
rollback/forward fix
  ↓
revalidate
```

### Best Practice
Automate health evidence collection before maintenance.

---

## Advanced Deep Dive 72 — Time Synchronization and Incident Correlation

### Concept and Detailed Explanation
NTP accuracy supports certificates, authentication, cluster coordination, DR, and incident timelines. Time drift can make a harmless dependency failure appear as several unrelated problems.

### Architecture / Mental Model
```text
Authoritative NTP
   |
+-- CVMs
+-- AHV hosts
+-- Prism Central
+-- admin systems
+-- backup/DR systems
```

### Commands / Code / Configuration
```text
date
timedatectl 2>/dev/null || true
chronyc sources -v 2>/dev/null || true
```

### Expected Behavior
Infrastructure systems use known healthy time sources and incident logs can be correlated reliably.

### Why It Works
Distributed troubleshooting requires a trustworthy common timeline.

### Real Production Example
One system clock is several minutes behind, making a certificate appear not-yet-valid and logs appear out of order.

### Troubleshooting Workflow
```text
time issue
  ↓
NTP source reachability
  ↓
offset
  ↓
firewall
  ↓
DNS
  ↓
peer consistency
```

### Best Practice
Treat NTP failure as a production infrastructure alert.

---

## Advanced Deep Dive 73 — DNS as a Management Dependency

### Concept and Detailed Explanation
Prism, LCM, DR, APIs, repositories, certificates, and NC2 can depend on correct DNS. A DNS failure may masquerade as an application or platform-service failure.

### Architecture / Mental Model
```text
Prism / LCM / DR / NC2
       |
      DNS
       |
service FQDNs/endpoints
```

### Commands / Code / Configuration
```text
getent hosts prism-central.example
dig prism-central.example 2>/dev/null || true
nslookup prism-central.example 2>/dev/null || true
```

### Expected Behavior
Infrastructure endpoints resolve consistently from the networks that consume them.

### Why It Works
Modern management systems use names in TLS certificates, APIs, repositories, and site-pair configuration.

### Real Production Example
LCM inventory fails because its repository name stops resolving while local cluster services remain healthy.

### Troubleshooting Workflow
```text
service timeout
  ↓
resolve FQDN
  ↓
DNS reachability
  ↓
record correctness
  ↓
cache/search domain
  ↓
TLS hostname
```

### Best Practice
Include DNS near the start of management-plane troubleshooting.

---


# Enhanced Practical Lab Series

These labs extend the original 30 labs. Use only **authorized Nutanix training, Community Edition/Test Drive, or disposable enterprise lab resources**. Begin with read-only evidence and do not run destructive cluster/storage operations in production.

## Enhanced Lab 1 — Nutanix HCI as a Distributed System

### Objective
Validate **Nutanix HCI as a Distributed System** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
cluster status
ncc health_checks run_all
acli vm.list
ncli host list
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Healthy cluster services, healthy node participation, visible VMs, and no unresolved critical NCC failures.

### Diagnostic Decision Tree
```text
symptom
  ↓
one VM, one host, one CVM, or cluster-wide?
  ↓
Prism alert/task/event
  ↓
cluster status + NCC
  ↓
compute / storage / network evidence
  ↓
physical component
  ↓
verify resilience restored
```

### Why This Lab Matters
Distributed software allows the cluster to keep serving workloads when one component fails, provided remaining copies, CVMs, network paths, and capacity remain healthy.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 2 — Node, Block, Rack, and Site Failure Domains

### Objective
Validate **Node, Block, Rack, and Site Failure Domains** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Node | Block | Rack | PDU | ToR | Site | CVM IP | Host IP
-----|-------|------|-----|-----|------|--------|--------
N1   | B1    | R1   | P1  | T1  | DC1  | ...    | ...
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can state exactly what happens if any one node, block, rack, PDU, ToR, or site fails.

### Diagnostic Decision Tree
```text
resilience concern
  ↓
map copies/resources to node/block/rack/site
  ↓
identify shared dependencies
  ↓
verify topology awareness
  ↓
correct placement or physical design
```

### Why This Lab Matters
Distributed resilience is only as strong as the independence of the resources that hold the copies and run the surviving services.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 3 — RF2 and RF3 Capacity Mathematics

### Objective
Validate **RF2 and RF3 Capacity Mathematics** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
raw_tb = 120
rf = 2
system = 0.08
snapshots = 0.10
failure_headroom = 0.15
growth = 0.15

after_rf = raw_tb / rf
safe_tb = after_rf * (1 - system - snapshots - failure_headroom - growth)
print(round(safe_tb, 2))
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
A conservative planning estimate that is lower than simple raw-capacity-divided-by-RF.

### Diagnostic Decision Tree
```text
capacity issue
  ↓
raw capacity
  ↓
RF
  ↓
current logical/physical use
  ↓
snapshots/protection
  ↓
free space by node
  ↓
failure-state requirement
```

### Why This Lab Matters
A distributed cluster needs free resources to heal after failures, not just enough space for steady-state workload data.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 4 — Resilience State vs Availability

### Objective
Validate **Resilience State vs Availability** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
cluster status
ncc health_checks run_all
# Prism: Health / Resilience / Hardware / Storage
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can distinguish service availability, current data protection, recovery progress, and remaining failure tolerance.

### Diagnostic Decision Tree
```text
failure
  ↓
application available?
  ↓
resilience healthy?
  ↓
re-replication progress?
  ↓
capacity sufficient?
  ↓
safe for maintenance?
```

### Why This Lab Matters
Distributed storage can mask a first failure from the application while background healing restores the desired copy count.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 5 — CVM Architecture and Privilege Boundary

### Objective
Validate **CVM Architecture and Privilege Boundary** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
cluster status
ncc health_checks run_all
acli vm.list
ncli cluster info
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The CVM participates normally in cluster services and is reachable over the intended management/backplane networks.

### Diagnostic Decision Tree
```text
CVM issue
  ↓
one CVM or many?
  ↓
host state
  ↓
cluster status
  ↓
Prism alert/task
  ↓
CPU/RAM/network evidence
  ↓
supported remediation
```

### Why This Lab Matters
Each CVM is part of the storage/control architecture, so unsupported changes can affect more than one workload.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 6 — CVM Resource Sizing and Workload Impact

### Objective
Validate **CVM Resource Sizing and Workload Impact** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Capacity worksheet:
Host RAM
CVM/platform reserve
N+1 reserve
Tenant configured RAM
Tenant active RAM

Track:
VM CPU
Host CPU
CVM CPU
Storage latency
IOPS / throughput
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can explain whether a performance issue is guest compute pressure or infrastructure storage/control pressure.

### Diagnostic Decision Tree
```text
slow VM
  ↓
guest CPU?
  ↓
host CPU?
  ↓
CVM CPU?
  ↓
storage IOPS/latency?
  ↓
network or rebuild activity?
```

### Why This Lab Matters
The CVM is in the I/O path, so storage demand can consume infrastructure CPU and memory.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 7 — Data Locality and VM Mobility

### Objective
Validate **Data Locality and VM Mobility** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
acli vm.get <VM_NAME>
# Compare Prism VM/host/storage metrics before and after migration.
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Migration changes compute placement without requiring a complete storage move first.

### Diagnostic Decision Tree
```text
post-migration latency
  ↓
VM metrics
  ↓
CVM/storage metrics
  ↓
inter-node network
  ↓
background locality behavior
```

### Why This Lab Matters
Distributed storage decouples VM execution location from rigid local-disk ownership.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 8 — Distributed Write Path

### Objective
Validate **Distributed Write Path** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
# Observe:
# Prism VM storage latency
# Prism cluster storage latency
# CVM CPU
# host/CVM network counters
ip -s link
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Write latency should remain stable and required protection should complete without sustained errors.

### Diagnostic Decision Tree
```text
write latency
  ↓
one VM or many?
  ↓
CVM CPU
  ↓
disk health
  ↓
inter-node network
  ↓
rebuild/replication
```

### Why This Lab Matters
Data protection requires more than one component to participate before a write is considered safely stored.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 9 — Checksums and Silent Corruption

### Objective
Validate **Checksums and Silent Corruption** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Operational evidence:
Prism hardware/storage alerts
NCC health checks
repeated media/integrity warnings
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
No persistent integrity or media errors remain after hardware remediation and data protection is restored.

### Diagnostic Decision Tree
```text
integrity alert
  ↓
affected device/node
  ↓
verify resilience
  ↓
review hardware health
  ↓
confirm healthy replicas
  ↓
replace/remediate
  ↓
verify clean health
```

### Why This Lab Matters
Storage devices can return incorrect data without fully failing. Integrity metadata detects this class of fault.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 10 — Compression, Deduplication, and Erasure Coding

### Objective
Validate **Compression, Deduplication, and Erasure Coding** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Capacity test:
1. record logical used;
2. record physical used;
3. identify enabled policies;
4. observe representative workload;
5. exclude temporary rebuild/snapshot effects;
6. calculate realized ratio.
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Measured data reduction matches the actual workload rather than a generic marketing ratio.

### Diagnostic Decision Tree
```text
saving lower than expected
  ↓
already compressed/encrypted?
  ↓
policy enabled?
  ↓
snapshot overhead?
  ↓
change rate?
  ↓
compare logical vs physical correctly
```

### Why This Lab Matters
Encrypted, already-compressed, VDI, database, and backup data have very different reduction characteristics.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 11 — Storage Containers as Policy Boundaries

### Objective
Validate **Storage Containers as Policy Boundaries** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
ncli container list

Container | Purpose | Protection | Encryption | Snapshot Policy | Owner
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every container has a documented purpose and policy.

### Diagnostic Decision Tree
```text
container sprawl
  ↓
identify actual policy differences
  ↓
group workloads
  ↓
standardize
  ↓
document owner
```

### Why This Lab Matters
DSF distributes data independently of the logical container boundary, so excessive logical fragmentation does not create traditional SAN-style physical isolation.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 12 — Storage Pool Fragmentation

### Objective
Validate **Storage Pool Fragmentation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
ncli storagepool list
ncli container list

Review:
pool purpose
capacity
hardware/media
container mappings
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every storage pool has a clear technical justification and enough headroom for failure recovery.

### Diagnostic Decision Tree
```text
pool pressure
  ↓
is separation required?
  ↓
capacity by pool
  ↓
container mapping
  ↓
supported consolidation/migration
```

### Why This Lab Matters
A distributed system gains balancing flexibility from a larger common resource set.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 13 — AHV, KVM, and VM Execution

### Objective
Validate **AHV, KVM, and VM Execution** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
acli vm.list
acli vm.get <VM_NAME>
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can identify the current AHV host and separately inspect storage/network dependencies.

### Diagnostic Decision Tree
```text
VM failure
  ↓
power/state
  ↓
AHV host capacity
  ↓
device/CPU constraints
  ↓
AOS storage
  ↓
network
  ↓
guest OS
```

### Why This Lab Matters
A VM can fail for CPU/device reasons even when its AOS storage is healthy, or suffer storage latency while compute scheduling is healthy.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 14 — vCPU Right-Sizing

### Objective
Validate **vCPU Right-Sizing** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
VM | Configured vCPU | P95 CPU | Peak CPU | Proposed vCPU | Owner

# Prism:
# VM → CPU metrics
# Host → CPU metrics
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
VMs meet application SLOs without persistent contention or large amounts of unused vCPU.

### Diagnostic Decision Tree
```text
CPU complaint
  ↓
guest CPU
  ↓
configured vs used
  ↓
host contention
  ↓
NUMA
  ↓
application thread model
```

### Why This Lab Matters
Hypervisors schedule finite physical execution resources; unused vCPUs still constrain placement and HA calculations.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 15 — Memory and N+1 Headroom

### Objective
Validate **Memory and N+1 Headroom** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
hosts = 4
ram_per_host = 768
platform_reserve = 48

safe_per_host = ram_per_host - platform_reserve
normal = safe_per_host * hosts
n_minus_1 = safe_per_host * (hosts - 1)

print(normal, n_minus_1)
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Capacity documentation reports safe normal and N-1 RAM, not just installed memory.

### Diagnostic Decision Tree
```text
memory risk
  ↓
installed RAM
  ↓
CVM/platform reserve
  ↓
tenant configured/active
  ↓
N-1 requirement
  ↓
growth
```

### Why This Lab Matters
HA restart requires surviving hosts to absorb the failed host's workload.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 16 — AHV Virtual Networking Mental Model

### Objective
Validate **AHV Virtual Networking Mental Model** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
# Guest
ip addr
ip route
ping <gateway>

# CVM/host evidence where authorized
acli vm.get <VM_NAME>
ip -s link
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can localize the fault to guest, virtual network, host uplink, physical switching, or upstream routing/security.

### Diagnostic Decision Tree
```text
network issue
  ↓
one VM or many?
  ↓
guest IP/route/firewall
  ↓
vNIC/network
  ↓
VLAN/VPC/Flow
  ↓
bond/NIC
  ↓
ToR/routing
```

### Why This Lab Matters
Each networking layer has independent configuration and failure modes.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 17 — VLAN and Physical Trunk Consistency

### Objective
Validate **VLAN and Physical Trunk Consistency** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
AHV Network | VLAN | Host Uplink | Switch Ports | Gateway | MTU
PROD-WEB    | 100  | bond0       | Eth1/1-1/3  | ...     | ...
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
A VM retains network connectivity after migration to any eligible host.

### Diagnostic Decision Tree
```text
migration causes network loss
  ↓
VM network
  ↓
destination virtual switch
  ↓
bond/uplink
  ↓
ToR VLAN trunk
  ↓
gateway
```

### Why This Lab Matters
Live migration changes compute placement, so the destination host must have equivalent network reachability.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 18 — Bonding and Physical Network Redundancy

### Objective
Validate **Bonding and Physical Network Redundancy** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
ip -s link

Review:
bond mode
NIC speed
switch pair
VLAN consistency
MTU
LACP requirements where used
failover test
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
A single approved link failure should not isolate the host if the design claims link redundancy.

### Diagnostic Decision Tree
```text
host network issue
  ↓
bond state
  ↓
individual NIC counters
  ↓
switch-port state
  ↓
VLAN/LACP
  ↓
failover behavior
```

### Why This Lab Matters
Software redundancy depends on independent physical paths and compatible switch behavior.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 19 — MTU and Jumbo-Frame Validation

### Objective
Validate **MTU and Jumbo-Frame Validation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
ip link show
ping -M do -s <payload-size> <peer>
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Large-packet tests pass end to end on networks designed for a larger MTU.

### Diagnostic Decision Tree
```text
small works / large fails
  ↓
host/CVM MTU
  ↓
bond/NIC
  ↓
switches
  ↓
router/firewall
  ↓
WAN
```

### Why This Lab Matters
Encapsulation and large frames require every hop to support the chosen size.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 20 — Flow Virtual Networking VPC Architecture

### Objective
Validate **Flow Virtual Networking VPC Architecture** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
VPC: PROD
  WEB 10.10.10.0/24
  APP 10.10.20.0/24
  DB  10.10.30.0/24

Document:
external connectivity
DNS/NTP
routing
security policy
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can trace a packet through logical VPC routing and then through the physical network.

### Diagnostic Decision Tree
```text
VPC traffic fails
  ↓
VM IP/subnet
  ↓
logical route
  ↓
Flow policy
  ↓
VPC uplink/external path
  ↓
overlay
  ↓
physical underlay
```

### Why This Lab Matters
Logical topology can be changed independently of physical VLAN topology while the underlay remains the transport.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 21 — Flow Microsegmentation with Categories

### Objective
Validate **Flow Microsegmentation with Categories** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Source Category | Destination Category | Service | Action | Reason
ERP/Web         | ERP/App              | 8443    | Allow  | API
ERP/App         | ERP/DB               | 5432    | Allow  | DB
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
A newly provisioned ERP web VM with correct categories inherits the expected security policy automatically.

### Diagnostic Decision Tree
```text
unexpected allow/block
  ↓
VM categories
  ↓
policy scope/priority
  ↓
source/destination
  ↓
service/port
  ↓
guest firewall
  ↓
network
```

### Why This Lab Matters
Identity-driven grouping avoids repeated rule changes when addresses or host placement change.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 22 — Microsegmentation Policy Lifecycle

### Objective
Validate **Microsegmentation Policy Lifecycle** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Policy record:
application owner
dependency map
allowed services
scope
rollback
exception expiry
monitoring owner
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Unauthorized lateral flows are blocked while approved application dependencies continue to work.

### Diagnostic Decision Tree
```text
after policy change outage
  ↓
affected flows
  ↓
category membership
  ↓
rule/priority
  ↓
dependency map
  ↓
narrow temporary exception
  ↓
fix documented policy
```

### Why This Lab Matters
Staged enforcement reduces risk from undocumented application dependencies.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 23 — Prism Element vs Prism Central Boundaries

### Objective
Validate **Prism Element vs Prism Central Boundaries** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Document:
Prism Central address
each Prism Element address
PC-dependent features
break-glass local access
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Operators can continue essential cluster-local validation through Prism Element during a Prism Central outage.

### Diagnostic Decision Tree
```text
PC unavailable
  ↓
managed clusters healthy?
  ↓
PE reachable?
  ↓
PC VM/state
  ↓
DNS/NTP/TLS
  ↓
PC service/capacity
```

### Why This Lab Matters
Centralized management sits above autonomous cluster runtime services.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 24 — Prism Central Capacity and Scale-Out

### Objective
Validate **Prism Central Capacity and Scale-Out** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Capacity checklist:
clusters managed
VMs managed
enabled PC services
CPU/RAM/disk
PC VM availability
backup/recovery
certificate lifecycle
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Prism Central remains responsive during normal inventory, policy, DR, and API operations.

### Diagnostic Decision Tree
```text
PC slow
  ↓
PC VM CPU/RAM/disk
  ↓
enabled services
  ↓
managed object count
  ↓
network/DNS
  ↓
resize/scale guidance
```

### Why This Lab Matters
Centralized services add compute and storage load to Prism Central beyond simple UI functions.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 25 — Categories as a Governance Data Model

### Objective
Validate **Categories as a Governance Data Model** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
App=ERP
Environment=Prod
Tier=DB
Criticality=Tier1
BackupPolicy=Gold
DRPolicy=NearSync
Owner=Business-Apps
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every production VM carries the required category dimensions using approved values.

### Diagnostic Decision Tree
```text
policy mismatch
  ↓
category taxonomy
  ↓
VM values
  ↓
legacy/duplicate values
  ↓
normalize
  ↓
automate validation
```

### Why This Lab Matters
Policy automation only works reliably when the metadata feeding it is consistent.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 26 — Projects, Quotas, and Self-Service

### Objective
Validate **Projects, Quotas, and Self-Service** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Project standard:
CPU quota
RAM quota
VM count
approved networks
approved images
expiry rule
owner
cost center
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Project users can create resources within the intended scope and limits without administrative control of the entire platform.

### Diagnostic Decision Tree
```text
self-service issue
  ↓
project
  ↓
role
  ↓
quota
  ↓
network/image access
  ↓
ownership/lifecycle
```

### Why This Lab Matters
Self-service is safe when resource rights are delegated without delegating infrastructure control.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 27 — RBAC and Separation of Duties

### Objective
Validate **RBAC and Separation of Duties** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Role | VM Create | Network | Flow | LCM | Audit | RBAC
-----|-----------|---------|------|-----|-------|-----
...
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Each role contains only the actions required for the user's operational responsibility.

### Diagnostic Decision Tree
```text
authorization issue
  ↓
user/group
  ↓
role
  ↓
scope/project
  ↓
requested action
  ↓
least privilege correction
```

### Why This Lab Matters
Separation of duties limits privilege and improves accountability.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 28 — Service Accounts for Automation

### Objective
Validate **Service Accounts for Automation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Identity record:
name
owner
purpose
role
scope
secret location
rotation date
last used
revoke procedure
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Automation runs using a scoped machine identity and fails cleanly when that credential is revoked.

### Diagnostic Decision Tree
```text
automation auth/leak
  ↓
credential identity
  ↓
scope/role
  ↓
secret store
  ↓
rotation/revocation
  ↓
audit activity
```

### Why This Lab Matters
Machine credentials have a different lifecycle and risk model from interactive human identities.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 29 — Tasks, Events, and Alerts as Evidence

### Objective
Validate **Tasks, Events, and Alerts as Evidence** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Time | Entity | Task ID | Event | Alert | User | Result
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can reconstruct what changed immediately before a failure or performance event.

### Diagnostic Decision Tree
```text
incident
  ↓
time/entity
  ↓
tasks
  ↓
events
  ↓
alerts
  ↓
metrics
  ↓
CLI evidence if needed
```

### Why This Lab Matters
Management-plane history provides causal evidence that raw metrics alone may not show.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 30 — AHV High Availability and Restart RTO

### Objective
Validate **AHV High Availability and Restart RTO** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
HA test record:
failure detected
VM restart started
VM powered on
guest ready
application ready
business transaction passed
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Measured application recovery meets the business RTO, not merely the VM power-on target.

### Diagnostic Decision Tree
```text
host failure
  ↓
HA restart?
  ↓
destination capacity?
  ↓
VM boot?
  ↓
application service?
  ↓
data consistency?
```

### Why This Lab Matters
Infrastructure HA restores compute execution, but application crash recovery and service startup still take time.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 31 — HA Capacity: N+1 and Beyond

### Objective
Validate **HA Capacity: N+1 and Beyond** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
safe_cluster_capacity =
  surviving_host_capacity
  - CVM/platform reserve
  - maintenance reserve

Compare with tenant demand.
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The failure-state model shows enough headroom to meet workload and storage-performance requirements.

### Diagnostic Decision Tree
```text
HA risk
  ↓
chosen failure domain
  ↓
surviving nodes
  ↓
RAM/CPU/storage/network reserve
  ↓
expand/right-size
```

### Why This Lab Matters
Redundancy only works when surviving resources have capacity to absorb the failed domain.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 32 — Live Migration as a Validation Tool

### Objective
Validate **Live Migration as a Validation Tool** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Before:
acli vm.get <VM_NAME>

During:
continuous ping / application transaction

After:
verify host placement
verify network
verify storage latency
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The VM remains available with acceptable interruption and preserves network/storage connectivity.

### Diagnostic Decision Tree
```text
migration fail
  ↓
target capacity
  ↓
CPU/device constraints
  ↓
network/VLAN
  ↓
host health
  ↓
special passthrough
```

### Why This Lab Matters
DSF keeps storage available independently of compute placement, so live migration mainly transfers execution state.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 33 — Affinity and Anti-Affinity Tradeoffs

### Objective
Validate **Affinity and Anti-Affinity Tradeoffs** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
VM/Group | Rule | Hard/Soft | Reason | Eligible Hosts | Failure Impact
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every placement rule has a documented reason and enough eligible hosts to survive expected maintenance/failure.

### Diagnostic Decision Tree
```text
cannot place/migrate
  ↓
capacity
  ↓
affinity/anti-affinity
  ↓
eligible hosts
  ↓
device/licensing constraints
```

### Why This Lab Matters
Scheduling can only choose from hosts that satisfy all constraints.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 34 — Acropolis Dynamic Scheduling and Hotspots

### Objective
Validate **Acropolis Dynamic Scheduling and Hotspots** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Compare:
VM CPU
Host CPU
CVM CPU
Storage latency
Network throughput
before and after movement
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Rebalancing reduces the actual bottleneck rather than simply moving the symptom.

### Diagnostic Decision Tree
```text
hotspot
  ↓
identify constrained resource
  ↓
top consumers
  ↓
background activity
  ↓
placement options
  ↓
migrate/right-size/add capacity
```

### Why This Lab Matters
CPU, memory, storage, and network hotspots have different causes and different useful migrations.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 35 — Volume Groups and Orphan Risk

### Objective
Validate **Volume Groups and Orphan Risk** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Volume Group | Attached VM(s) | Capacity | Owner | Protection | Backup
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every volume group has a known attachment, owner, and data-protection policy.

### Diagnostic Decision Tree
```text
orphan volume group
  ↓
attachment?
  ↓
owner?
  ↓
backup/retention?
  ↓
application dependency?
  ↓
approved cleanup
```

### Why This Lab Matters
Independent storage lifecycles provide flexibility but can create orphaned capacity when VM cleanup is incomplete.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 36 — Snapshots, Recovery Points, and Backups

### Objective
Validate **Snapshots, Recovery Points, and Backups** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Workload | Local RPO | Remote RPO | Backup Freq | Immutability | Retention | Restore Test
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Critical workloads have a recovery method that survives the specific failure or attack scenario being modeled.

### Diagnostic Decision Tree
```text
recovery event
  ↓
failure type
  ↓
local point clean?
  ↓
remote point clean?
  ↓
backup/immutable copy?
  ↓
restore and validate
```

### Why This Lab Matters
Replication can reproduce deletion, corruption, or ransomware; independent backups create a separate recovery path.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 37 — Protection Policies as Intent

### Objective
Validate **Protection Policies as Intent** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Policy:
Scope:
Local RPO:
Remote RPO:
Retention:
Target:
Mode:
Owner:
Test Frequency:
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
A new workload with the correct category automatically receives the expected protection behavior.

### Diagnostic Decision Tree
```text
VM not protected
  ↓
category/scope
  ↓
policy
  ↓
target
  ↓
replication state
  ↓
capacity/network
```

### Why This Lab Matters
Intent-based protection reduces manual omissions and expresses business recovery objectives directly.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 38 — Asynchronous Replication and Achieved RPO

### Objective
Validate **Asynchronous Replication and Achieved RPO** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Monitor:
last successful recovery point
configured interval
transfer duration
backlog
WAN throughput
target capacity
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Achieved replication lag remains inside the business RPO under normal and degraded conditions.

### Diagnostic Decision Tree
```text
replication behind
  ↓
source recovery point?
  ↓
WAN reachability/bandwidth
  ↓
target health/capacity
  ↓
backlog
  ↓
policy cadence
```

### Why This Lab Matters
RPO is about how much data could be lost, not simply how often a job is scheduled.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 39 — NearSync Throughput Planning

### Objective
Validate **NearSync Throughput Planning** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Inputs:
Change rate MB/s
WAN usable MB/s
Latency
Packet loss
Target write capability
Required RPO
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The replication path sustains average and burst change rate with headroom.

### Diagnostic Decision Tree
```text
NearSync lag
  ↓
change rate
  ↓
WAN throughput
  ↓
latency/loss
  ↓
target performance
  ↓
competing traffic
```

### Why This Lab Matters
A tighter RPO creates less time to catch up after a slowdown.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 40 — Synchronous / Metro Protection

### Objective
Validate **Synchronous / Metro Protection** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Design:
RTT latency
bandwidth
loss
witness placement
failure domains
application write-latency budget
site isolation behavior
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The application meets its latency SLO while synchronous protection remains healthy.

### Diagnostic Decision Tree
```text
Metro issue
  ↓
inter-site latency/loss
  ↓
witness/quorum
  ↓
site health
  ↓
storage latency
  ↓
application SLO
```

### Why This Lab Matters
Remote acknowledgement adds network distance directly to the write path.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 41 — Recovery Plans and Dependency Order

### Objective
Validate **Recovery Plans and Dependency Order** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Recovery plan:
boot order
readiness condition
network mapping
IP/DNS changes
application health check
data consistency check
external cutover
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Each tier starts only after its dependency is actually ready.

### Diagnostic Decision Tree
```text
DR plan fails
  ↓
which group?
  ↓
VM power?
  ↓
network mapping?
  ↓
dependency ready?
  ↓
DNS/IP?
  ↓
application test?
```

### Why This Lab Matters
Downstream services can be powered on while still unusable if identity, database, or network dependencies are not ready.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 42 — Failback and Reverse Replication

### Objective
Validate **Failback and Reverse Replication** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Failback:
1. identify active source of truth;
2. synchronize back;
3. validate primary;
4. freeze/cut over;
5. update DNS/network;
6. verify app;
7. restore DR protection.
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The primary is not made active until it contains current, consistent production data.

### Diagnostic Decision Tree
```text
failback
  ↓
source of truth
  ↓
reverse sync
  ↓
consistency validation
  ↓
planned cutover
  ↓
application verification
```

### Why This Lab Matters
Failover creates new writes at DR; powering on an old primary without synchronization can lose those changes.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 43 — Isolated DR Testing

### Objective
Validate **Isolated DR Testing** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Evidence:
selected recovery point
VM boot
network mapping
dependency readiness
database consistency
application transaction
measured RTO
cleanup
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The test proves recoverability without disrupting live production.

### Diagnostic Decision Tree
```text
DR test
  ↓
isolated network
  ↓
DNS/IP mapping
  ↓
data writes isolated
  ↓
validate application
  ↓
collect RTO
  ↓
clean up
```

### Why This Lab Matters
Recovery copies are useful only if they can actually boot, connect, and complete application transactions.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 44 — NC2 Operating Model

### Objective
Validate **NC2 Operating Model** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
NC2 design:
Cloud
Region
AZs
Network CIDRs
Connectivity
DNS
Identity
Cluster size
DR mode
Monthly cost
Exit plan
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You can explain which responsibilities remain Nutanix responsibilities and which remain public-cloud/customer responsibilities.

### Diagnostic Decision Tree
```text
NC2 issue
  ↓
Nutanix cluster health
  ↓
cloud resource/quota
  ↓
VPC/VNet routing/security
  ↓
hybrid connectivity
  ↓
cost/capacity
```

### Why This Lab Matters
NC2 runs the Nutanix stack on cloud infrastructure rather than removing the cloud-provider underlay.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 45 — Hybrid Connectivity and Routing

### Objective
Validate **Hybrid Connectivity and Routing** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Network plan:
on-prem CIDRs
NC2 CIDRs
route propagation
firewall rules
DNS
MTU
BGP/static routes
failover path
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Application dependencies remain reachable after migration/failover without ambiguous routes.

### Diagnostic Decision Tree
```text
hybrid reachability
  ↓
VM subnet
  ↓
cloud route
  ↓
hybrid gateway
  ↓
on-prem firewall
  ↓
return route
```

### Why This Lab Matters
Hybrid infrastructure adds a routed failure domain between workload and dependency.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 46 — LCM Inventory as Lifecycle Foundation

### Objective
Validate **LCM Inventory as Lifecycle Foundation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
1. run LCM inventory
2. resolve inventory errors
3. record current versions
4. review compatible target
5. run prechecks
6. schedule change
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
LCM shows a complete, current inventory without unresolved unknown components.

### Diagnostic Decision Tree
```text
inventory fails
  ↓
cluster/NCC health
  ↓
repository/network
  ↓
credentials
  ↓
component detection
  ↓
space
  ↓
rerun
```

### Why This Lab Matters
Upgrade compatibility depends on the exact starting state.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 47 — LCM Prechecks and Maintenance Headroom

### Objective
Validate **LCM Prechecks and Maintenance Headroom** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Pre-upgrade:
NCC
resilience
critical alerts
free capacity
HA headroom
replication status
backup status
compatibility
maintenance window
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The cluster remains inside safe compute, storage, and network limits when one node is in maintenance.

### Diagnostic Decision Tree
```text
precheck warning
  ↓
understand risk
  ↓
capacity/resilience
  ↓
correct issue
  ↓
rerun NCC/LCM
```

### Why This Lab Matters
Rolling upgrade assumes surviving resources can absorb the temporarily unavailable node.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 48 — Rolling Upgrade Mechanics

### Objective
Validate **Rolling Upgrade Mechanics** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
After each node:
host healthy
CVM healthy
cluster services healthy
network links healthy
resilience healthy
VMs stable
NCC/LCM acceptable
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Each node returns fully healthy before the next node is removed from service.

### Diagnostic Decision Tree
```text
rolling upgrade problem
  ↓
stop progression
  ↓
stabilize current node
  ↓
cluster health
  ↓
resilience
  ↓
supported rollback/forward fix
```

### Why This Lab Matters
Sequential changes limit blast radius and preserve redundancy.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 49 — Dark-Site Lifecycle Management

### Objective
Validate **Dark-Site Lifecycle Management** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Checklist:
exact target versions
bundle provenance
hash/signature
malware scan
repository capacity
approval
rollback artifacts
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The offline cluster discovers only approved, complete bundles and does not depend on Internet access during the maintenance window.

### Diagnostic Decision Tree
```text
dark-site failure
  ↓
bundle completeness
  ↓
hash/provenance
  ↓
repository path
  ↓
LCM inventory
  ↓
compatibility
```

### Why This Lab Matters
Air-gapping changes distribution mechanics but not authenticity or compatibility requirements.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 50 — Foundation and Initial Cluster Bring-Up

### Objective
Validate **Foundation and Initial Cluster Bring-Up** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Node | Host IP | CVM IP | BMC IP | VLAN | GW | DNS | NTP | AOS | AHV
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every node joins with the intended identity and network configuration and the cluster passes baseline health checks.

### Diagnostic Decision Tree
```text
Foundation failure
  ↓
BMC
  ↓
imaging network
  ↓
IP uniqueness
  ↓
DNS/NTP
  ↓
image compatibility
  ↓
hardware
```

### Why This Lab Matters
Automation reproduces the supplied design; it cannot make an incorrect IP/VLAN plan correct.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 51 — Cluster Expansion and Rebalancing

### Objective
Validate **Cluster Expansion and Rebalancing** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Before:
NCC
LCM inventory
version compatibility
IP/VLAN
rack/PDU
ToR ports
BMC

After:
cluster status
NCC
host inventory
capacity
rebalance activity
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The new node joins healthy and rebalance completes without unacceptable workload impact.

### Diagnostic Decision Tree
```text
expansion issue
  ↓
node health
  ↓
version/firmware
  ↓
network
  ↓
storage
  ↓
rebalance load
```

### Why This Lab Matters
Distributed systems move data and responsibilities to exploit new capacity.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 52 — Data-at-Rest Encryption and KMS

### Objective
Validate **Data-at-Rest Encryption and KMS** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
KMS design:
provider
HA
network path
certificate trust
backup
restore
admin separation
rotation
DR availability
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The cluster can access required keys during normal operation, maintenance, and documented recovery scenarios.

### Diagnostic Decision Tree
```text
encryption access issue
  ↓
cluster health
  ↓
KMS reachability
  ↓
TLS/trust
  ↓
key existence/version
  ↓
KMS HA/backup
```

### Why This Lab Matters
Encryption without recoverable keys converts hardware/data availability into an unrecoverable data-access problem.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 53 — Management Plane Segmentation

### Objective
Validate **Management Plane Segmentation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Review:
management subnet
allowed sources
MFA/jump host
TLS
SSH
BMC access
logging
patch process
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Only approved administrative sources can reach management interfaces.

### Diagnostic Decision Tree
```text
management exposure
  ↓
source/destination reachability
  ↓
firewall/ACL
  ↓
service exposure
  ↓
credentials
  ↓
segment/restrict
```

### Why This Lab Matters
Compromise of management interfaces can grant control over compute, storage, VM lifecycle, or physical power.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 54 — BMC / Out-of-Band Security

### Objective
Validate **BMC / Out-of-Band Security** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Controls:
separate VLAN/VRF
unique credentials
certificate management
firmware updates
audit
restricted source networks
no Internet exposure
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
BMC interfaces are reachable only from authorized management systems.

### Diagnostic Decision Tree
```text
BMC compromise
  ↓
isolate OOB
  ↓
rotate credentials
  ↓
review audit/power events
  ↓
firmware/integrity
  ↓
restore carefully
```

### Why This Lab Matters
Out-of-band control bypasses the hypervisor and can affect a node even when the host OS is unavailable.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 55 — Prism Central v4 API Automation

### Objective
Validate **Prism Central v4 API Automation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
# Generic pattern; use installed-release documentation for exact endpoint/auth.
curl --fail --silent --show-error   --cacert /path/to/ca.pem   -H "Accept: application/json"   "https://prism-central.example/api/<v4-resource>"
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The client verifies TLS, uses a dedicated machine identity, captures task identifiers, and handles non-success responses.

### Diagnostic Decision Tree
```text
API failure
  ↓
identity
  ↓
TLS
  ↓
endpoint/version
  ↓
HTTP status/body
  ↓
task ID
  ↓
actual resource state
```

### Why This Lab Matters
Cloud infrastructure APIs are asynchronous and privileged; clients must track final state rather than equating request acceptance with success.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 56 — Idempotent Infrastructure Automation

### Objective
Validate **Idempotent Infrastructure Automation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
desired = {"name": "app01", "cpu": 4, "memory_gib": 16}
current = find_vm(desired["name"])

if current is None:
    create_vm(desired)
else:
    validate_or_reconcile(current, desired)
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Running the workflow twice results in one correct VM rather than duplicates.

### Diagnostic Decision Tree
```text
ambiguous timeout
  ↓
query by ID/name/tag
  ↓
inspect task
  ↓
determine committed state
  ↓
reconcile
```

### Why This Lab Matters
Distributed API timeouts can hide whether a create request already committed, so state reconciliation is safer than blind retries.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 57 — API Secret Redaction and Audit

### Objective
Validate **API Secret Redaction and Audit** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
SENSITIVE = {
    "authorization",
    "token",
    "password",
    "api_key",
    "secret",
}
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Support logs remain useful without containing reusable credentials.

### Diagnostic Decision Tree
```text
secret exposure
  ↓
revoke/rotate
  ↓
restrict/remove logs
  ↓
audit use
  ↓
fix redaction
```

### Why This Lab Matters
Bearer credentials copied into logs become attack material when logs are shared or retained.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 58 — Performance Troubleshooting by Layer

### Objective
Validate **Performance Troubleshooting by Layer** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Collect same time window:
Guest: top, vmstat, iostat
Prism: VM CPU/RAM/storage
Host CPU/RAM/network
CVM CPU
Cluster storage latency/IOPS
alerts/tasks/events
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You identify the first layer where abnormal latency or contention appears.

### Diagnostic Decision Tree
```text
slow workload
  ↓
blast radius
  ↓
guest metrics
  ↓
host metrics
  ↓
CVM/storage
  ↓
network
  ↓
background tasks
```

### Why This Lab Matters
Layered systems propagate lower-level delays upward into application symptoms.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 59 — Storage Latency Decomposition

### Objective
Validate **Storage Latency Decomposition** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Metric | Before | Incident | After
IOPS
Throughput
Latency
CVM CPU
Disk errors
Network drops
Rebuild state
Protection activity
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The incident can be tied to a measurable bottleneck or recovery activity rather than a generic statement that storage is slow.

### Diagnostic Decision Tree
```text
latency
  ↓
one VM or cluster?
  ↓
IOPS/throughput
  ↓
CVM CPU
  ↓
media health
  ↓
network
  ↓
rebuild/DR/backup
```

### Why This Lab Matters
Storage latency is the sum of work and waiting across several infrastructure layers.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 60 — Network Troubleshooting by Blast Radius

### Objective
Validate **Network Troubleshooting by Blast Radius** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Evidence:
affected VM list
host placement
network/VLAN/VPC
Flow categories
NIC counters
switch alarms
gateway reachability
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You localize the probable layer before changing network configuration.

### Diagnostic Decision Tree
```text
network outage
  ↓
count affected
  ↓
common host?
  ↓
common VLAN/VPC?
  ↓
common Flow policy?
  ↓
common gateway/uplink?
```

### Why This Lab Matters
Shared infrastructure produces recognizable failure patterns.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 61 — Prism Unavailable: Management vs Runtime

### Objective
Validate **Prism Unavailable: Management vs Runtime** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
cluster status
ncc health_checks run_all

Check:
application reachability
DNS
TLS certificate
CVM state
management network
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
You know whether the incident is management-only or affects cluster runtime.

### Diagnostic Decision Tree
```text
Prism down
  ↓
workload runtime?
  ↓
cluster status
  ↓
CVM health
  ↓
management network
  ↓
DNS/TLS
  ↓
supported recovery
```

### Why This Lab Matters
Management and data-plane functions can fail independently.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 62 — NCC as a Diagnostic Framework

### Objective
Validate **NCC as a Diagnostic Framework** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
ncc health_checks run_all
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
After correction, the specific failed health check and related platform health return to acceptable state.

### Diagnostic Decision Tree
```text
NCC issue
  ↓
read check name/details
  ↓
identify entity
  ↓
understand consequence
  ↓
collect supporting evidence
  ↓
correct
  ↓
rerun
```

### Why This Lab Matters
NCC encodes known platform health/configuration expectations.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 63 — cluster status as First-Line Triage

### Objective
Validate **cluster status as First-Line Triage** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
cluster status

Record:
timestamp
CVMs
service state
missing/unresponsive services
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
A stable cluster shows expected service participation on intended CVMs.

### Diagnostic Decision Tree
```text
cluster status anomaly
  ↓
which CVM?
  ↓
host health
  ↓
CVM CPU/RAM/network
  ↓
Prism alert
  ↓
service-specific evidence
```

### Why This Lab Matters
Peer comparison quickly distinguishes local and distributed failures.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 64 — One CVM Down Scenario

### Objective
Validate **One CVM Down Scenario** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
cluster status
ncc health_checks run_all

Prism:
affected node
CVM VM state
storage latency
resilience alerts
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The cluster remains available if designed for the failure and surviving CVMs remain within safe load.

### Diagnostic Decision Tree
```text
CVM down
  ↓
one or many?
  ↓
host healthy?
  ↓
CVM state
  ↓
cluster status
  ↓
storage/resilience
  ↓
supported recovery
```

### Why This Lab Matters
Distributed CVM services avoid dependence on one controller appliance.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 65 — One AHV Host Down Scenario

### Objective
Validate **One AHV Host Down Scenario** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Prism:
host state
affected VM list
HA tasks
storage resilience
rebuild progress

cluster status
ncc health_checks run_all
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Critical VMs restart inside the expected RTO and cluster storage returns to full protection without exhausting headroom.

### Diagnostic Decision Tree
```text
host down
  ↓
hardware/BMC
  ↓
VM HA
  ↓
destination capacity
  ↓
CVM/storage resilience
  ↓
application verification
```

### Why This Lab Matters
Host failure affects both compute and distributed-storage resources.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 66 — Disk Failure and Re-Replication

### Objective
Validate **Disk Failure and Re-Replication** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Prism:
hardware
storage/resilience
tasks/events
capacity

ncc health_checks run_all
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Protection returns to the intended level and no persistent device or resilience alert remains.

### Diagnostic Decision Tree
```text
disk failure
  ↓
identify device/node
  ↓
resilience
  ↓
free capacity
  ↓
re-replication
  ↓
replace hardware
  ↓
verify clean state
```

### Why This Lab Matters
Distributed replicas allow the cluster to rebuild across healthy resources rather than waiting for a single replacement target.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 67 — Reduced Resilience as a Change-Control Blocker

### Objective
Validate **Reduced Resilience as a Change-Control Blocker** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Change gate:
if resilience != healthy:
    stop
    investigate
    restore
    rerun NCC
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
No planned node removal begins until the required protection and capacity state is healthy.

### Diagnostic Decision Tree
```text
maintenance request
  ↓
resilience status
  ↓
hardware alerts
  ↓
capacity
  ↓
if degraded: STOP
  ↓
restore health
```

### Why This Lab Matters
Combining maintenance with an unresolved fault can turn a tolerated first failure into a serious second failure.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 68 — Capacity Forecasting by Bottleneck

### Objective
Validate **Capacity Forecasting by Bottleneck** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Month | CPU Peak | RAM Peak | Storage | IOPS | DR Lag | N-1 Headroom
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Planning identifies the first limiting resource and a date by which expansion or right-sizing must occur.

### Diagnostic Decision Tree
```text
capacity warning
  ↓
which resource?
  ↓
normal trend
  ↓
N-1 trend
  ↓
growth rate
  ↓
procurement lead time
```

### Why This Lab Matters
A cluster can be storage-rich but memory-full, or compute-rich but constrained by replication bandwidth.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 69 — Backup and Cyber-Recovery Separation

### Objective
Validate **Backup and Cyber-Recovery Separation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Controls:
separate backup admin
MFA
immutable retention
isolated repository
restore network
malware validation
restore tests
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
The organization has at least one recovery path that does not rely on the compromised production management plane.

### Diagnostic Decision Tree
```text
cyber incident
  ↓
isolate production
  ↓
protect backup control plane
  ↓
select clean recovery point
  ↓
restore isolated
  ↓
validate integrity
```

### Why This Lab Matters
Replication protects availability, while independent backup protects against historical corruption and some administrative/security failures.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 70 — Configuration Drift Across Clusters

### Objective
Validate **Configuration Drift Across Clusters** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Compare:
AOS/AHV
DNS/NTP
networks/VLANs
categories
RBAC
protection
NCC baseline
LCM status
service accounts
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Every cluster difference is either intentional/documented or corrected.

### Diagnostic Decision Tree
```text
drift
  ↓
desired vs actual
  ↓
intentional?
  ↓
document or remediate
  ↓
revalidate
```

### Why This Lab Matters
Standardization allows the same runbooks, DR plans, and automation to work across the fleet.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 71 — Change Management with Pre/Post Evidence

### Objective
Validate **Change Management with Pre/Post Evidence** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
Change record:
purpose
scope
risk
prerequisites
procedure
expected result
validation
recovery
owner
evidence
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Post-change health is equal to or better than baseline and required business transactions pass.

### Diagnostic Decision Tree
```text
post-change problem
  ↓
compare pre/post
  ↓
tasks/events
  ↓
affected layer
  ↓
rollback/forward fix
  ↓
revalidate
```

### Why This Lab Matters
Without baseline evidence, operators cannot distinguish pre-existing faults from change-induced regressions.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 72 — Time Synchronization and Incident Correlation

### Objective
Validate **Time Synchronization and Incident Correlation** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
date
timedatectl 2>/dev/null || true
chronyc sources -v 2>/dev/null || true
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Infrastructure systems use known healthy time sources and incident logs can be correlated reliably.

### Diagnostic Decision Tree
```text
time issue
  ↓
NTP source reachability
  ↓
offset
  ↓
firewall
  ↓
DNS
  ↓
peer consistency
```

### Why This Lab Matters
Distributed troubleshooting requires a trustworthy common timeline.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---

## Enhanced Lab 73 — DNS as a Management Dependency

### Objective
Validate **DNS as a Management Dependency** using an evidence-first Nutanix operations workflow.

### Preparation
1. Record cluster, Prism Element, Prism Central, AOS/AHV version, and maintenance state.
2. Confirm no active reduced-resilience condition or unrelated critical incident is in progress.
3. Identify the lab VM/node/network/storage object and record its ID/name.
4. Capture a read-only before-state.

### Mental Model
```text
User / Application
      |
Prism / API
      |
AHV / CVM / AOS
      |
Network / Storage / Hardware
      |
Observed Result
```

### Commands / Data
```text
getent hosts prism-central.example
dig prism-central.example 2>/dev/null || true
nslookup prism-central.example 2>/dev/null || true
```

### Procedure
1. Draw the expected dependency path before making any change.
2. Capture Prism alerts, tasks, events, and relevant entity metrics.
3. Run the read-only commands above where applicable.
4. Compare the observed state with the expected architecture.
5. In a disposable lab only, simulate one narrow, reversible failure/configuration mismatch when safe.
6. Repeat the evidence collection and identify the first layer that changed.
7. Restore the supported state/configuration.
8. Re-run NCC/cluster health checks when appropriate.
9. Verify workload/application behavior, not only infrastructure status.
10. Write: `Symptom → Evidence → Root Cause → Correction → Verification → Prevention`.

### Expected Result
Infrastructure endpoints resolve consistently from the networks that consume them.

### Diagnostic Decision Tree
```text
service timeout
  ↓
resolve FQDN
  ↓
DNS reachability
  ↓
record correctness
  ↓
cache/search domain
  ↓
TLS hostname
```

### Why This Lab Matters
Modern management systems use names in TLS certificates, APIs, repositories, and site-pair configuration.

### Safety
Do not shut down multiple CVMs, bypass NCC/LCM safety checks, force internal AOS processes, or perform destructive storage/cluster actions outside an approved disposable lab.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Draw the Nutanix Architecture

Draw:

```text
Prism Central
Cluster
Nodes
AHV
CVM
DSF
VMs
Physical Storage
```

Explain every arrow.

### Lab 2 — Map a Node

For one lab node document:

```text
host IP
CVM IP
BMC/IPMI IP
CPU
RAM
NICs
storage devices
AHV version
AOS version
```

### Lab 3 — Prism Element Exploration

Open Prism Element and locate:

```text
cluster
hosts
VMs
storage
hardware
alerts
tasks
health
```

Create your own navigation map.

### Lab 4 — Prism Central Exploration

Locate:

```text
clusters
VMs
categories
images
projects
alerts
operations
DR
LCM
```

Compare what is cluster-local versus centralized.

### Lab 5 — CLI Health Baseline

SSH to a lab CVM:

```bash
cluster status
ncc health_checks run_all
```

Save output and classify:

```text
PASS
WARN
FAIL
```

Do not change anything yet.

### Lab 6 — aCLI Inventory

Run:

```bash
acli vm.list
acli vm.get <VM_NAME>
```

Identify:

```text
CPU
RAM
disks
NICs
host placement
```

### Lab 7 — nCLI Inventory

Use read-only commands matching the installed release to inspect:

```text
cluster
hosts
containers
alerts
```

Build a CLI cheat sheet.

### Lab 8 — Create a VM

Create:

```text
2 vCPU
4 GB RAM
40 GB disk
1 vNIC
```

Install Linux.

Record:

```text
host
container
network
IP
```

### Lab 9 — Clone and Image Workflow

Create a patched base VM.

Convert/use it as an image or clone source according to your lab.

Deploy two identical test VMs and customize identity.

### Lab 10 — Live Migration

Run continuous ping to a VM.

Migrate it between AHV hosts.

Measure interruption and verify new host placement.

### Lab 11 — Anti-Affinity

Create two redundant lab VMs.

Configure/design anti-affinity so they do not share the same host.

Explain the failure-domain benefit.

### Lab 12 — VLAN Networking

Create/use:

```text
LAB-WEB VLAN 100
LAB-APP VLAN 200
```

Verify physical trunk configuration and guest connectivity.

### Lab 13 — Network Failure Tabletop

For a VM that cannot reach its gateway, trace:

```text
guest
vNIC
network/VLAN
virtual switch
bond
NIC
physical switch
gateway
```

### Lab 14 — Storage Container

Inspect current storage containers.

Document:

```text
capacity
usage
policy
VM mapping
```

Explain why containers are logical rather than individual disks.

### Lab 15 — RF Capacity Exercise

Given:

```text
raw capacity = 30 TB
RF2
snapshots/growth/headroom
```

Create a realistic usable-capacity model.

Repeat conceptually for RF3.

### Lab 16 — Disk Failure Tabletop

Scenario:

```text
one SSD fails
```

Document:

```text
what AOS does
what Prism reports
what NCC checks
what operator verifies
```

### Lab 17 — Node Failure Tabletop

Scenario:

```text
AHV host abruptly fails
```

Document:

```text
VM HA
CVM/storage resilience
re-replication
capacity
alerts
```

### Lab 18 — Categories

Create:

```text
App=ERP
Tier=Web
Environment=Lab
```

Apply to lab VMs.

Explain how security/protection automation can consume them.

### Lab 19 — Flow Security Design

Design:

```text
ERP-Web → ERP-App TCP/8443
ERP-App → ERP-DB TCP/5432
all other lateral traffic denied
```

If Flow is licensed in the lab, implement and test.

### Lab 20 — Protection Policy

Create/design a policy:

```text
VM group: ERP
RPO: 1 hour
Retention: 24 local points
Remote replication: DR cluster
```

Explain each choice.

### Lab 21 — Recovery Plan

Build a plan:

```text
1. DNS/AD
2. Database
3. Application
4. Web
```

Include network mapping and validation tests.

### Lab 22 — DR Test

Perform or tabletop:

```text
select recovery point
test failover
verify VM
verify application
measure RTO
clean up
```

### Lab 23 — Prism Alerts and Tasks

Generate a harmless lab task.

Find:

```text
task ID
user
start/end time
entity
result
```

Correlate with events.

### Lab 24 — NCC Before/After Maintenance

Run:

```bash
ncc health_checks run_all
```

before a safe lab maintenance action and again afterward.

Compare results.

### Lab 25 — LCM Planning

Without applying a production upgrade:

1. run/inspect inventory;
2. identify current versions;
3. identify available compatible updates;
4. write precheck/rollback plan;
5. calculate cluster headroom during rolling maintenance.

### Lab 26 — Cluster Expansion Design

Given a 3-node cluster at:

```text
CPU 70%
RAM 75%
Storage 72%
```

design addition of one or more nodes.

Explain:

```text
power
rack
network
AOS/AHV compatibility
IP
rebalance
N+1
```

### Lab 27 — Security Review

Audit:

```text
Prism admins
CVM SSH
BMC
network segmentation
encryption
KMS
service accounts
API access
Flow exclusions
```

Create `NCI_SECURITY_REVIEW.md`.

### Lab 28 — REST API Read

Use a dedicated lab service account and current Prism Central API documentation.

Perform a safe read operation against a v4 API endpoint.

Requirements:

```text
TLS validation
no hard-coded admin password
log status/request ID
```

### Lab 29 — Multicloud Architecture

Design:

```text
On-Prem NCI
   |
   +-- NC2 public-cloud recovery site
   |
   +-- second on-prem cluster
```

Compare:

```text
latency
RPO
RTO
cost
network
data sovereignty
```

### Lab 30 — Troubleshooting Challenge

Analyze:

1. one CVM down.
2. one AHV host down.
3. one disk failed.
4. cluster reports reduced resilience.
5. storage latency high.
6. one VM CPU slow.
7. one VM cannot reach gateway.
8. one host has NIC errors.
9. Prism Element unavailable.
10. Prism Central unavailable.
11. NCC reports failure.
12. LCM inventory fails.
13. migration fails.
14. replication behind RPO.
15. DR plan fails.

For each write:

```text
Symptom
Layer
Evidence
Root Cause
Correction
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — Nutanix Hybrid Multicloud Infrastructure

Design a production platform for:

```text
120 VMs
ERP
MES
Active Directory
SQL/Oracle databases
file services
monitoring
backup
development workloads
```

Architecture:

```text
                        Prism Central
                              |
                 +------------+------------+
                 |                         |
             Primary NCI                DR NCI / NC2
                 |                         |
       +---------+---------+               |
       |         |         |               |
      Node1     Node2     Node3+       Recovery Cluster
       |         |         |
      AHV       AHV       AHV
       |         |         |
      CVM       CVM       CVM
        \        |        /
         +-------DSF------+
                 |
              Workloads
```

## Requirements

Define:

```text
CPU
RAM
CVM overhead
raw/usable storage
RF
network bandwidth
N+1 capacity
RPO
RTO
growth
security
```

## Networking

Design:

```text
management
CVM/backplane
VM VLANs
Flow VPCs
backup
replication
BMC
```

## VM Standards

Create:

```text
Small
Medium
Large
Database
GPU/AI if applicable
```

with justified CPU/RAM/storage profiles.

## Storage

Define:

```text
containers
storage policies
RF
capacity headroom
volume groups
data reduction assumptions
```

## Security

Include:

```text
RBAC
categories
Flow microsegmentation
CVM hardening
management isolation
BMC isolation
encryption
KMS
service accounts
API keys
logging
```

## Data Protection

Create:

```text
protection policies
recovery points
remote replication
recovery plan
backup integration
DR test schedule
```

## Lifecycle

Create:

```text
LCM inventory process
NCC precheck
rolling upgrade
capacity during maintenance
firmware/AHV/AOS compatibility
```

## Automation

Use/design:

```text
Prism Central v4 APIs
service account
Git-controlled desired state
```

## Deliverables

```text
README.md
ARCHITECTURE.md
NODE_DESIGN.md
CAPACITY.md
NETWORK.md
STORAGE.md
VM_STANDARDS.md
PRISM.md
FLOW_SECURITY.md
RBAC.md
DR.md
BACKUP.md
LCM.md
MONITORING.md
API_AUTOMATION.md
RUNBOOKS/
```

## Required Runbooks

```text
RUNBOOK_CVM_DOWN.md
RUNBOOK_HOST_FAILURE.md
RUNBOOK_DISK_FAILURE.md
RUNBOOK_STORAGE_LATENCY.md
RUNBOOK_VM_NETWORK.md
RUNBOOK_PRISM_FAILURE.md
RUNBOOK_NCC_FAILURE.md
RUNBOOK_LCM_FAILURE.md
RUNBOOK_REPLICATION.md
RUNBOOK_DR_FAILOVER.md
```

---


# Expanded Capstone — Production Nutanix Hybrid Multicloud Platform

Design a production Nutanix platform for a manufacturing organization running:

```text
ERP
MES
Active Directory
SQL / Oracle databases
file services
monitoring
backup
engineering applications
development/test workloads
```

## Target Architecture

```text
                           Prism Central
                                |
              +-----------------+------------------+
              |                                    |
       Primary NCI Clusters                 DR NCI / NC2
              |                                    |
      +-------+-------+                    +-------+-------+
      |       |       |                    |               |
    Node1   Node2   Node3+              DR Cluster      NC2
      |       |       |
     AHV     AHV     AHV
      |       |       |
     CVM     CVM     CVM
       \      |      /
        +-----DSF---+
              |
           Workloads
```

## 1. Failure-Domain Model

Create `FAILURE_DOMAINS.md` containing:

```text
Node
Block
Rack
PDU
Top-of-Rack Switch
Site
Host IP
CVM IP
BMC IP
```

Model failure of:

```text
one disk
one CVM
one node
one block
one rack network
one site
```

For each case document:

```text
What remains available?
What protection is reduced?
What HA action occurs?
What capacity is required?
What must the operator verify?
What is the remaining risk?
```

## 2. Capacity Model

Create `CAPACITY.md` with:

```text
raw storage
RF2 / RF3
system reserve
snapshot reserve
data-reduction assumption
growth reserve
rebuild reserve
CVM overhead
normal CPU/RAM
N-1 CPU/RAM
failure-state network
DR replication bandwidth
```

Provide both **normal-state** and **failure-state** capacity.

## 3. Network Architecture

Create:

```text
management network
CVM/backplane network
VM VLANs
Flow VPCs
backup network
replication network
BMC/OOB network
NC2 hybrid connectivity
```

For every network document:

```text
CIDR
VLAN/VPC
MTU
gateway
DNS
routing
firewall
bond/uplinks
ToR ports
failure path
owner
```

## 4. Workload Standards

Define standard profiles:

```text
General-Small
General-Medium
General-Large
Database
Latency-Sensitive
GPU/Accelerated
Development
```

For each:

```text
vCPU
RAM
vDisk layout
network
categories
protection tier
anti-affinity
SLO
```

## 5. Category Taxonomy

Required dimensions:

```text
App
Environment
Tier
Owner
Criticality
DataClass
BackupPolicy
DRPolicy
CostCenter
```

Example:

```text
App=ERP
Environment=Prod
Tier=DB
Criticality=Tier1
BackupPolicy=Gold
DRPolicy=NearSync
Owner=Business-Apps
```

## 6. Flow Security

Design:

```text
Users → ERP-Web TCP/443
ERP-Web → ERP-App TCP/8443
ERP-App → ERP-DB on approved DB port
Backup → protected workloads on approved backup ports
Monitoring → workloads on approved monitoring ports
Deny unnecessary lateral movement
```

Include:

```text
policy owner
dependency map
test method
exception expiry
rollback
logging
```

## 7. Storage Design

Define:

```text
storage pools
containers
RF
snapshots
volume groups
capacity headroom
data-reduction assumptions
database layout
```

Explain why each logical storage object exists.

## 8. Protection / DR Tiers

Create three tiers:

```text
Gold:
low RPO / low RTO
remote replication
frequent recovery points
monthly DR test

Silver:
periodic replication
quarterly DR test

Bronze:
backup-led recovery
longer RTO
```

For Tier1 workloads include:

```text
Protection Policy
Recovery Plan
Network Mapping
DNS Plan
Failover
Failback
Reverse Replication
Application Validation
```

## 9. Cyber Recovery

Require:

```text
independent backup
immutable retention where required
separate backup administrator
MFA
isolated restore network
clean restore validation
periodic recovery exercise
```

## 10. Lifecycle Standard

Create `LCM_STANDARD.md`:

```text
LCM inventory
NCC baseline
compatibility review
upgrade rings
prechecks
N+1 capacity
maintenance window
rolling update
post-check
recovery plan
evidence retention
```

Use rollout rings:

```text
Ring 0 — Lab
Ring 1 — Dev/Test
Ring 2 — Noncritical Production
Ring 3 — Tier1 Production
```

## 11. Security Architecture

Create `SECURITY_ARCHITECTURE.md` covering:

```text
Prism RBAC
service accounts
MFA
CVM access
BMC isolation
management segmentation
Flow microsegmentation
encryption/KMS
API credential storage
audit
backup credential separation
```

## 12. API Automation

Design:

```text
nutanix-platform-automation/
├── README.md
├── config/
│   ├── clusters.yaml
│   ├── networks.yaml
│   ├── categories.yaml
│   └── policies.yaml
├── src/
│   ├── client.py
│   ├── inventory.py
│   ├── vm_reconcile.py
│   ├── category_reconcile.py
│   ├── network_reconcile.py
│   ├── protection_reconcile.py
│   └── logging_utils.py
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
    ├── SECURITY.md
    ├── API_COMPATIBILITY.md
    └── RUNBOOK.md
```

Automation requirements:

```text
TLS verification
dedicated service identity
no human admin password in code
secret redaction
query before create
persist IDs
track asynchronous tasks
bounded retries
idempotent reconciliation
safe cleanup
```

## 13. Monitoring and SLOs

Track:

```text
Prism API availability
VM provisioning time
VM HA restart time
Tier1 storage latency
CVM CPU
host CPU/RAM
network errors
capacity trend
resilience state
replication lag
backup success
restore success
LCM/NCC status
```

## 14. Required Runbooks

```text
RUNBOOK_CVM_DOWN.md
RUNBOOK_HOST_DOWN.md
RUNBOOK_DISK_FAILURE.md
RUNBOOK_REDUCED_RESILIENCE.md
RUNBOOK_STORAGE_LATENCY.md
RUNBOOK_VM_CPU.md
RUNBOOK_VM_NETWORK.md
RUNBOOK_FLOW_POLICY.md
RUNBOOK_PRISM_ELEMENT.md
RUNBOOK_PRISM_CENTRAL.md
RUNBOOK_NCC_FAILURE.md
RUNBOOK_LCM_FAILURE.md
RUNBOOK_REPLICATION_LAG.md
RUNBOOK_DR_FAILOVER.md
RUNBOOK_DR_FAILBACK.md
RUNBOOK_KMS_FAILURE.md
RUNBOOK_BMC_SECURITY.md
RUNBOOK_NC2_NETWORK.md
```

Each runbook must include:

```text
trigger
business impact
safety limits
evidence
decision tree
remediation
verification
escalation
prevention
```


## 7. Recommended Resources

This file is designed to provide the complete conceptual foundation for Course 44.

For exact production procedures and release-specific commands, use the documentation matching the installed NCI release.

Primary official documentation families:

```text
Nutanix Cloud Infrastructure
AOS 7.6 Advanced Administration Guide
Prism 7.6
Prism Central 7.6
AOS 7.6 Command Reference
Nutanix Security Guide 7.6
Nutanix Disaster Recovery 7.6
Flow Network Security
Flow Virtual Networking
Nutanix Cloud Clusters (NC2)
Life Cycle Manager
NCC
```

Current baseline facts reflected in this course:

- NCI/AOS 7.6 is the current July 2026 release baseline.
- DSF is the core software-defined distributed storage technology of AOS.
- AHV is Nutanix's integrated virtualization platform.
- Prism is the unified NCI management plane.
- Prism Central can use single-VM or three-VM scale-out deployment architectures according to requirements.
- Flow Network Security integrates policy-based security with AHV/Prism Central.
- Current Prism Central workflows increasingly expose v4 APIs.
- NCP-MCI 7.5 is the current professional multicloud-infrastructure certification exam.

---

## 8. Certification Relevance

This course is directly relevant to:

```text
NCP-MCI — Nutanix Certified Professional, Multicloud Infrastructure
```

The current NCP-MCI 7.5 exam focuses on the ability to interpret documented standards and perform administrative tasks such as:

```text
deploying
configuring
migrating
troubleshooting
expanding
managing
```

Nutanix multicloud environments.

Also relevant to:

```text
Virtualization Engineer
Nutanix Administrator
Private Cloud Engineer
Infrastructure Engineer
HCI Engineer
Platform Engineer
DR Engineer
Cloud Engineer
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Treat CVM as an ordinary Linux VM.  
  **Best practice:** use Prism/NCC/supported procedures and avoid arbitrary service manipulation.

- **Mistake:** Assume AHV and AOS are the same component.  
  **Best practice:** AHV is hypervisor; AOS provides distributed infrastructure/storage services.

- **Mistake:** Treat RF2/RF3 like local RAID labels.  
  **Best practice:** reason in distributed copies and failure domains.

- **Mistake:** Size only tenant VMs.  
  **Best practice:** include CVM overhead and failover headroom.

- **Mistake:** Fill cluster storage to 95% before expanding.  
  **Best practice:** forecast growth and preserve recovery/rebuild headroom.

- **Mistake:** Power off a host before maintenance preparation.  
  **Best practice:** validate health, capacity, and supported maintenance workflow.

- **Mistake:** Shut down multiple CVMs manually.  
  **Best practice:** let supported rolling maintenance manage CVM/service movement.

- **Mistake:** Treat Prism Central outage as total VM/storage outage.  
  **Best practice:** distinguish centralized management from cluster-local runtime.

- **Mistake:** Use VLAN alone as full security policy.  
  **Best practice:** use Flow microsegmentation/categories where appropriate.

- **Mistake:** Use replication as the only backup.  
  **Best practice:** maintain independent cyber-recovery copies.

- **Mistake:** Upgrade because LCM shows a newer component without reading health/compatibility.  
  **Best practice:** inventory, precheck, compatibility review, then rolling update.

- **Mistake:** Ignore NCC warnings/failures.  
  **Best practice:** understand the check and correct root cause.

- **Mistake:** Use human Prism admin credentials in automation.  
  **Best practice:** dedicated service account/API credential with least privilege.

- **Mistake:** Hard-code current API behavior forever.  
  **Best practice:** version/test v4 API integrations against the installed Prism Central release.

- **Mistake:** Design HA without spare compute/storage/network capacity.  
  **Best practice:** validate N+1/failure scenarios quantitatively.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is NCI?

**Short answer:** Nutanix Cloud Infrastructure, combining software-defined compute, storage, networking, protection, and infrastructure operations.

### Q2. AOS vs AHV?

**Short answer:** AOS provides core distributed infrastructure/storage services; AHV is the integrated hypervisor.

### Q3. What is a CVM?

**Short answer:** Controller VM running Nutanix AOS storage/control services on each cluster node.

### Q4. What is DSF?

**Short answer:** Distributed Storage Fabric that pools and protects storage across Nutanix nodes.

### Q5. What is a Nutanix node?

**Short answer:** Physical server contributing compute, local storage, network, hypervisor, and a CVM to the cluster.

### Q6. What is RF2?

**Short answer:** Data-resilience policy maintaining two distributed copies of protected data.

### Q7. What is RF3?

**Short answer:** Policy maintaining three distributed copies for stronger failure tolerance at greater capacity cost.

### Q8. What happens after a disk/node failure?

**Short answer:** AOS uses surviving copies and re-replicates data to restore the required protection level.

### Q9. What is a storage container?

**Short answer:** Logical AOS storage construct used to present/manage storage for workloads.

### Q10. Prism Element vs Prism Central?

**Short answer:** Prism Element manages one cluster locally; Prism Central provides centralized multicluster management and advanced services.

### Q11. What is aCLI?

**Short answer:** Acropolis CLI used primarily for AHV/VM/network resource management.

### Q12. What is nCLI?

**Short answer:** Nutanix CLI used for cluster/storage/configuration administration.

### Q13. What does `cluster status` do?

**Short answer:** Provides a quick view of Nutanix cluster service state across CVMs.

### Q14. What does NCC do?

**Short answer:** Runs health/configuration checks and reports issues/recommendations.

### Q15. What is AHV live migration?

**Short answer:** Moving a running VM between AHV hosts with minimal service interruption.

### Q16. What is anti-affinity?

**Short answer:** Policy used to keep redundant VMs on separate hosts/failure domains.

### Q17. What is Flow Virtual Networking?

**Short answer:** Nutanix software-defined networking capability providing constructs such as VPCs and logical subnets.

### Q18. What is Flow Network Security?

**Short answer:** Policy-based microsegmentation/security integrated with AHV and Prism Central.

### Q19. Why are categories important?

**Short answer:** They provide workload metadata that can drive security, protection, governance, and automation.

### Q20. What is a protection policy?

**Short answer:** Policy defining which workloads are protected and their recovery-point/replication behavior.

### Q21. What is a recovery plan?

**Short answer:** Orchestrated order and configuration for recovering protected workloads at a recovery location.

### Q22. What is LCM?

**Short answer:** Life Cycle Manager for inventorying and updating compatible Nutanix/hardware software stack components.

### Q23. Why run NCC before upgrades?

**Short answer:** To confirm cluster health before intentionally reducing redundancy during rolling maintenance.

### Q24. What is NC2?

**Short answer:** Nutanix Cloud Clusters, extending Nutanix infrastructure/operations into supported public clouds.

### Q25. Why is Prism Central not the same as a hypervisor?

**Short answer:** Prism Central is management/control infrastructure; AHV hosts actually execute VMs.

### Q26. Why does N+1 still matter in HCI?

**Short answer:** VMs and storage services need enough surviving CPU/RAM/storage/network resources after a node failure.

### Q27. Why isn't native DR a complete ransomware strategy?

**Short answer:** Replication can copy malicious changes; independent immutable/offline backups are still needed.

### Q28. Why protect management and CVM networks?

**Short answer:** They control high-privilege infrastructure operations and storage services.

### Q29. What API model is increasingly used in current Prism Central?

**Short answer:** Nutanix v4 APIs.

### Q30. What is the main NCI troubleshooting principle?

**Short answer:** Identify whether the problem is VM, AHV, CVM/AOS, storage, network, Prism, protection, or physical infrastructure; collect evidence before changing services.

---

# Expanded Self-Assessment Bank

The uploaded course already contains its original self-assessment. The following questions add architecture and production-operations checks.

### Q1. What is the key operational principle behind **Nutanix HCI as a Distributed System**?
**Answer:** Establish the blast radius before changing cluster services.

### Q2. What is the key operational principle behind **Node, Block, Rack, and Site Failure Domains**?
**Answer:** Maintain a physical failure-domain map and update it whenever nodes are added.

### Q3. What is the key operational principle behind **RF2 and RF3 Capacity Mathematics**?
**Answer:** Capacity-plan for the failure state, not only the normal state.

### Q4. What is the key operational principle behind **Resilience State vs Availability**?
**Answer:** Do not begin elective maintenance while the cluster is already below intended resilience.

### Q5. What is the key operational principle behind **CVM Architecture and Privilege Boundary**?
**Answer:** Use Prism, NCC, LCM, and supported procedures; keep arbitrary software off CVMs.

### Q6. What is the key operational principle behind **CVM Resource Sizing and Workload Impact**?
**Answer:** Include CVM performance in every storage-performance investigation.

### Q7. What is the key operational principle behind **Data Locality and VM Mobility**?
**Answer:** Correlate short post-migration behavior with cluster metrics before concluding that migration caused a storage fault.

### Q8. What is the key operational principle behind **Distributed Write Path**?
**Answer:** Treat the inter-node network as part of the storage subsystem.

### Q9. What is the key operational principle behind **Checksums and Silent Corruption**?
**Answer:** Investigate repeated integrity errors even if applications remain online.

### Q10. What is the key operational principle behind **Compression, Deduplication, and Erasure Coding**?
**Answer:** Treat data reduction as measured efficiency, not guaranteed baseline capacity.

### Q11. What is the key operational principle behind **Storage Containers as Policy Boundaries**?
**Answer:** Use the minimum number of containers needed to express real operational policy.

### Q12. What is the key operational principle behind **Storage Pool Fragmentation**?
**Answer:** Avoid recreating legacy SAN-LUN habits in HCI unless there is a real requirement.

### Q13. What is the key operational principle behind **AHV, KVM, and VM Execution**?
**Answer:** Classify the fault as compute, storage, network, or guest before acting.

### Q14. What is the key operational principle behind **vCPU Right-Sizing**?
**Answer:** Right-size from representative metrics, not from fear-based overprovisioning.

### Q15. What is the key operational principle behind **Memory and N+1 Headroom**?
**Answer:** Set operational limits from failure-state capacity.

### Q16. What is the key operational principle behind **AHV Virtual Networking Mental Model**?
**Answer:** Use blast radius to decide where to start.

### Q17. What is the key operational principle behind **VLAN and Physical Trunk Consistency**?
**Answer:** Validate network equivalence before enabling a new host for workload placement.

### Q18. What is the key operational principle behind **Bonding and Physical Network Redundancy**?
**Answer:** Test uplink failure during maintenance and document the observed behavior.

### Q19. What is the key operational principle behind **MTU and Jumbo-Frame Validation**?
**Answer:** Never enable jumbo frames on only part of the path.

### Q20. What is the key operational principle behind **Flow Virtual Networking VPC Architecture**?
**Answer:** Troubleshoot overlay and underlay as separate layers.

### Q21. What is the key operational principle behind **Flow Microsegmentation with Categories**?
**Answer:** Make category assignment mandatory in provisioning workflows.

### Q22. What is the key operational principle behind **Microsegmentation Policy Lifecycle**?
**Answer:** Use time-bounded exceptions and remove them after the dependency is modeled.

### Q23. What is the key operational principle behind **Prism Element vs Prism Central Boundaries**?
**Answer:** Maintain a Prism Central outage runbook that begins with workload and Prism Element validation.

### Q24. What is the key operational principle behind **Prism Central Capacity and Scale-Out**?
**Answer:** Reassess Prism Central sizing when major services or fleet size increases.

### Q25. What is the key operational principle behind **Categories as a Governance Data Model**?
**Answer:** Create and enforce a small approved category dictionary.

### Q26. What is the key operational principle behind **Projects, Quotas, and Self-Service**?
**Answer:** Use projects and least privilege instead of shared administrator accounts.

### Q27. What is the key operational principle behind **RBAC and Separation of Duties**?
**Answer:** Assign permissions through groups/roles rather than individual exceptions.

### Q28. What is the key operational principle behind **Service Accounts for Automation**?
**Answer:** Never place broad Prism administrator credentials in source code or CI logs.

### Q29. What is the key operational principle behind **Tasks, Events, and Alerts as Evidence**?
**Answer:** Capture Prism history before disruptive changes.

### Q30. What is the key operational principle behind **AHV High Availability and Restart RTO**?
**Answer:** Measure application RTO during controlled HA tests.

### Q31. What is the key operational principle behind **HA Capacity: N+1 and Beyond**?
**Answer:** Set alert thresholds from failure-state headroom rather than normal-state percentages.

### Q32. What is the key operational principle behind **Live Migration as a Validation Tool**?
**Answer:** Use a representative migration test before placing production workloads on new hosts.

### Q33. What is the key operational principle behind **Affinity and Anti-Affinity Tradeoffs**?
**Answer:** Use hard placement rules only for true non-negotiable requirements.

### Q34. What is the key operational principle behind **Acropolis Dynamic Scheduling and Hotspots**?
**Answer:** Diagnose the resource bottleneck before overriding automated placement.

### Q35. What is the key operational principle behind **Volume Groups and Orphan Risk**?
**Answer:** Include volume groups in periodic orphan-resource reviews.

### Q36. What is the key operational principle behind **Snapshots, Recovery Points, and Backups**?
**Answer:** Design backup and DR together, but never treat them as the same control.

### Q37. What is the key operational principle behind **Protection Policies as Intent**?
**Answer:** Make protection assignment part of workload onboarding.

### Q38. What is the key operational principle behind **Asynchronous Replication and Achieved RPO**?
**Answer:** Alert on actual replication lag, not only job-failure status.

### Q39. What is the key operational principle behind **NearSync Throughput Planning**?
**Answer:** Validate low-RPO designs with measured change rate and effective throughput.

### Q40. What is the key operational principle behind **Synchronous / Metro Protection**?
**Answer:** Choose synchronous protection only when the network and application latency budgets support it.

### Q41. What is the key operational principle behind **Recovery Plans and Dependency Order**?
**Answer:** Use readiness checks rather than fixed sleep timers where possible.

### Q42. What is the key operational principle behind **Failback and Reverse Replication**?
**Answer:** Test failback during DR exercises, not only failover.

### Q43. What is the key operational principle behind **Isolated DR Testing**?
**Answer:** Treat test-network isolation as a mandatory DR control.

### Q44. What is the key operational principle behind **NC2 Operating Model**?
**Answer:** Include provider quotas and cost in NC2 architecture reviews.

### Q45. What is the key operational principle behind **Hybrid Connectivity and Routing**?
**Answer:** Avoid overlapping address space before it becomes a DR emergency.

### Q46. What is the key operational principle behind **LCM Inventory as Lifecycle Foundation**?
**Answer:** Never plan a broad upgrade from stale inventory.

### Q47. What is the key operational principle behind **LCM Prechecks and Maintenance Headroom**?
**Answer:** Do not override health warnings merely to meet a change window.

### Q48. What is the key operational principle behind **Rolling Upgrade Mechanics**?
**Answer:** Never parallelize node maintenance unless the supported procedure explicitly allows it.

### Q49. What is the key operational principle behind **Dark-Site Lifecycle Management**?
**Answer:** Treat lifecycle bundles as controlled software artifacts.

### Q50. What is the key operational principle behind **Foundation and Initial Cluster Bring-Up**?
**Answer:** Validate the complete IP/VLAN table before imaging the first node.

### Q51. What is the key operational principle behind **Cluster Expansion and Rebalancing**?
**Answer:** Schedule expansion with enough performance headroom for rebalancing.

### Q52. What is the key operational principle behind **Data-at-Rest Encryption and KMS**?
**Answer:** Test KMS recovery as part of DR.

### Q53. What is the key operational principle behind **Management Plane Segmentation**?
**Answer:** Route privileged management through controlled administrative networks.

### Q54. What is the key operational principle behind **BMC / Out-of-Band Security**?
**Answer:** Treat BMC access as one of the highest-privilege infrastructure controls.

### Q55. What is the key operational principle behind **Prism Central v4 API Automation**?
**Answer:** Build API automation around reconciliation and task tracking.

### Q56. What is the key operational principle behind **Idempotent Infrastructure Automation**?
**Answer:** Persist resource IDs and ownership metadata immediately.

### Q57. What is the key operational principle behind **API Secret Redaction and Audit**?
**Answer:** Redact credentials before logs leave the application process.

### Q58. What is the key operational principle behind **Performance Troubleshooting by Layer**?
**Answer:** Compare an affected VM with a healthy peer and the cluster-wide timeline.

### Q59. What is the key operational principle behind **Storage Latency Decomposition**?
**Answer:** Correlate latency with workload intensity and background activity.

### Q60. What is the key operational principle behind **Network Troubleshooting by Blast Radius**?
**Answer:** Use scope correlation before packet capture or policy changes.

### Q61. What is the key operational principle behind **Prism Unavailable: Management vs Runtime**?
**Answer:** Prove workload state before restarting anything.

### Q62. What is the key operational principle behind **NCC as a Diagnostic Framework**?
**Answer:** Never apply random fixes simply because an NCC result is red.

### Q63. What is the key operational principle behind **cluster status as First-Line Triage**?
**Answer:** Capture `cluster status` output before disruptive intervention.

### Q64. What is the key operational principle behind **One CVM Down Scenario**?
**Answer:** Do not manually shut down additional CVMs while one is already unavailable.

### Q65. What is the key operational principle behind **One AHV Host Down Scenario**?
**Answer:** Maintain enough headroom to absorb the failure of the domain you promise to tolerate.

### Q66. What is the key operational principle behind **Disk Failure and Re-Replication**?
**Answer:** Capacity headroom is part of disk-failure resilience.

### Q67. What is the key operational principle behind **Reduced Resilience as a Change-Control Blocker**?
**Answer:** Make resilience a formal maintenance prerequisite.

### Q68. What is the key operational principle behind **Capacity Forecasting by Bottleneck**?
**Answer:** Trigger expansion from forecasted failure-state headroom, not only from 90% utilization.

### Q69. What is the key operational principle behind **Backup and Cyber-Recovery Separation**?
**Answer:** Separate backup credentials and trust from primary infrastructure administration.

### Q70. What is the key operational principle behind **Configuration Drift Across Clusters**?
**Answer:** Maintain machine-readable platform standards where possible.

### Q71. What is the key operational principle behind **Change Management with Pre/Post Evidence**?
**Answer:** Automate health evidence collection before maintenance.

### Q72. What is the key operational principle behind **Time Synchronization and Incident Correlation**?
**Answer:** Treat NTP failure as a production infrastructure alert.

### Q73. What is the key operational principle behind **DNS as a Management Dependency**?
**Answer:** Include DNS near the start of management-plane troubleshooting.


## Completion Checklist

- [ ] I understand NCI architecture.
- [ ] I understand AOS vs AHV.
- [ ] I understand nodes, clusters, CVMs, pools and containers.
- [ ] I understand DSF.
- [ ] I understand RF2/RF3 and self-healing.
- [ ] I understand VM storage I/O path.
- [ ] I understand Prism Element vs Prism Central.
- [ ] I can use basic aCLI/nCLI read operations.
- [ ] I can use `cluster status`.
- [ ] I can run and interpret NCC.
- [ ] I understand AHV VM lifecycle.
- [ ] I understand AHV networking/VLANs.
- [ ] I understand live migration and HA.
- [ ] I understand affinity/anti-affinity.
- [ ] I understand Flow Virtual Networking.
- [ ] I understand Flow Network Security.
- [ ] I understand categories/projects/RBAC.
- [ ] I understand storage policies and volume groups.
- [ ] I understand protection policies/recovery points/recovery plans.
- [ ] I understand asynchronous/NearSync/Metro concepts.
- [ ] I understand NC2/hybrid multicloud.
- [ ] I understand LCM and rolling upgrades.
- [ ] I understand cluster expansion/maintenance.
- [ ] I understand encryption and CVM security.
- [ ] I understand v4 API/service-account concepts.
- [ ] I can troubleshoot major NCI failures.
- [ ] I completed all 30 labs.
- [ ] I completed the Nutanix Hybrid Multicloud Infrastructure project.
