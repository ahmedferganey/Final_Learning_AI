# Phase 8 — Storage & Data Center

This phase teaches the infrastructure underneath databases, virtualization, cloud platforms, and enterprise applications.

The learning sequence is:

```text
34. Information Storage and Management
        ↓
35. Data Center Infrastructure Design
        ↓
36. Enterprise Backup and Recovery
        ↓
37. Veeam Backup and Replication
```

The logic is:

```text
How Data Is Stored
        ↓
Where Infrastructure Runs
        ↓
How Data Is Protected
        ↓
How Enterprise Protection Is Implemented with Veeam
```

This phase is deliberately **visual and practical**. The Markdown files include:

```text
ASCII diagrams
Linux commands
PowerShell
storage calculations
capacity formulas
backup-chain diagrams
data-center topology
failure-domain analysis
Veeam architecture
recovery runbooks
hands-on labs
mini projects
troubleshooting
```

The objective is that you can learn the required concepts from the Markdown material itself without depending on an external tutorial.

---

# Phase Goal

By the end of Phase 8, you should be able to trace a production service through:

```text
Application
   ↓
Server / VM
   ↓
Filesystem / Volume
   ↓
SAN / NAS / DAS / Object
   ↓
Storage Array
   ↓
Data Center Network
   ↓
Power + Cooling
   ↓
Backup Infrastructure
   ↓
Immutable / Offsite Recovery Copies
```

and answer:

```text
Where is the data?
How is it accessed?
What path carries the I/O?
What happens when a disk fails?
What happens when a SAN path fails?
What happens when power fails?
What happens when a site fails?
Where are the backups?
Are they immutable?
Can we restore them?
How long will recovery take?
```

---

# 34. Information Storage and Management

**File:** `34_Information_Storage_and_Management.md`

This course starts at the I/O path.

```text
Application
    ↓
Filesystem
    ↓
Volume Manager
    ↓
Block Device
    ↓
HBA / NIC
    ↓
SAN / Storage Network
    ↓
Array Controller
    ↓
RAID / Pool
    ↓
SSD / HDD / NVMe
```

Main topics:

```text
Block Storage
File Storage
Object Storage
DAS
NAS
SAN
HDD
SSD
NVMe
RAID 0 / 1 / 5 / 6 / 10
Controllers
Cache
Storage Pools
LUNs
Thick / Thin Provisioning
Fibre Channel
HBA / WWPN
Zoning
LUN Masking
iSCSI
IQN / CHAP
NFS
SMB
Multipathing
Linux LVM
Windows Storage
Snapshots
Clones
Replication
Deduplication
Compression
Tiering
IOPS
Throughput
Latency
Queue Depth
fio
iostat
Object Immutability
Capacity Planning
Troubleshooting
```

Practical command examples include:

```bash
lsblk
blkid
findmnt
lsscsi
iscsiadm
multipath -ll
iostat -xz 1
fio
nvme list
```

and Windows PowerShell:

```powershell
Get-Disk
Get-Partition
Get-Volume
Get-PhysicalDisk
Get-StoragePool
Get-SmbShare
```

### Course Project

**Enterprise Storage Platform**

You design:

```text
SAN
NAS
block storage
object storage
RAID
multipathing
capacity
performance
monitoring
failure response
```

---

# 35. Data Center Infrastructure Design

**File:** `35_Data_Center_Infrastructure_Design.md`

This course moves from storage into the full physical infrastructure.

Dependency model:

```text
Business Service
      ↓
Application
      ↓
Compute
      ↓
Network + Storage
      ↓
Rack
      ↓
Power + Cooling
      ↓
Building / Site
```

Main topics:

```text
Enterprise DC
Colocation
Cloud / Hyperscale
Edge
Modular DC

Site Selection
Failure Domains

Rack Units
Rack Elevation
Rack Power Density

Utility
Switchgear
ATS
UPS
Generator
PDU
Rack PDU
A/B Power

N
N+1
N+2
2N
2N+1

Cooling
CRAC
CRAH
Hot / Cold Aisles
Containment
Airflow
Temperature
Humidity
PUE

Structured Cabling
Copper
Fiber
Patch Panels
MDF / IDF / MMR

ToR
EoR
Leaf-Spine
East-West Traffic
OOB Management

Storage Network Redundancy

Physical Security
CCTV
Access Control
Mantrap

Fire Detection
Fire Suppression
Leak Detection
EPO
Grounding

BMS
DCIM

Capacity Planning
Conceptual Tier I–IV Progression
SLA / SLO
MOU / MOA
Change Management
Runbooks

Hot / Warm / Cold DR Sites
Active/Active
```

### Course Project

**Resilient Manufacturing Data Center**

You create:

```text
rack elevations
power one-line
cooling plan
leaf-spine network
SAN fabrics
security layers
capacity plan
SPOF analysis
DR site
monitoring
runbooks
```

---

# 36. Enterprise Backup and Recovery

**File:** `36_Enterprise_Backup_and_Recovery.md`

This course changes the mindset from:

```text
"Did the backup job finish?"
```

to:

```text
"Can we recover the service
within the required RPO and RTO?"
```

Core architecture:

```text
Production
    |
    v
Primary Backup
    |
    +----> Secondary Copy
    |
    +----> Immutable Copy
    |
    +----> Offsite / Object
    |
    +----> Tape / Offline
```

Main topics:

```text
Backup
Restore
Recovery
Archive
Snapshot
Replication

BIA
RPO
RTO
Recovery Tiers

Full
Incremental
Differential
Incremental Forever
Synthetic Full
Active Full
CDP

Backup Chains
Health / Integrity

Crash Consistency
Application Consistency
VSS
Quiescing

File Backup
VM Backup
Bare Metal
Database Backup
NAS
SaaS
Object Data

Backup Server
Proxy / Media Server
Repository
Configuration / Catalog
Gateway
Tape

Disk
Dedupe Appliance
Object Storage
Tape

Air Gap
Immutability
3-2-1
3-2-1-1-0

GFS
Capacity Planning
Backup Window
Throughput

Compression
Deduplication
Encryption
Key Management

Segmentation
MFA
Least Privilege
Admin Isolation
Ransomware Defense

File Restore
Full VM Restore
Instant Recovery
Application Restore
PITR
Bare-Metal Recovery
Clean Room

Recovery Verification
Automated Testing
DR Orchestration
Failover / Failback

Monitoring
RPO Compliance
Repository Capacity
Troubleshooting
Cyber Recovery
```

### Course Project

**Cyber-Resilient Enterprise Backup Platform**

You design protection for:

```text
VMs
physical servers
SQL
Oracle
NAS
SaaS
```

with:

```text
immutable repository
offsite copy
GFS
tape/object storage
recovery testing
cyber recovery
DR runbooks
```

---

# 37. Veeam Backup and Replication

**File:** `37_Veeam_Backup_and_Replication.md`

Reference baseline:

```text
Veeam Backup & Replication 13.1.1
Build 13.1.1.18
```

The course maps Course 36 into Veeam.

Core architecture:

```text
                  Veeam Backup Server
                         |
            +------------+------------+
            |                         |
         Proxies                  Repositories
            |                         |
      Production VMs              Backup Data
                                      |
                      +---------------+---------------+
                      |                               |
                Hardened Repo                   Object / Tape
```

Main topics:

```text
Backup Server
Software / Infrastructure Appliance
Console / Web UI
Configuration Database
Backup Proxies
VMware / Hyper-V Backup Flow
Transport Modes
Repositories
Mount Server
Gateway
Tape Server

Source Snapshot
CBT

Backup Jobs
Forward Incremental
Forever Forward
Active Full
Synthetic Full
Deprecated Reverse Incremental
Fast Clone Concepts

Short-Term Retention
GFS

Application-Aware Processing
Guest Processing
VSS
Application Log Processing
Health Check

Backup Copy Jobs

SOBR
Performance Tier
Capacity Tier
Archive Tier

Object Storage

Hardened Repository
Immutability
3-2-1-1-0

Proxy / Repository Sizing
Concurrent Tasks
Bottleneck Analysis

Veeam PowerShell

Entire VM Restore
Instant Recovery
File Restore
Disk Restore
Application Item Restore
Veeam Explorer Concepts

SureBackup
Virtual Lab
Application Group
SureReplica

VM Replication
Restore Points
Network Mapping
Re-IP
Failover
Failback
CDP Concepts

Tape
Media Pools
GFS
Virtual Full Concepts

Veeam Agents
Recovery Media

Configuration Backup

Encryption
Credentials
RBAC
MFA
Network Segmentation
Cyber Recovery

Monitoring
Snapshot Problems
Proxy Bottleneck
Source / Network / Target Bottlenecks
Repository Full
Guest Processing Failure
CBT Issues
Restore Failure
SureBackup Failure
```

### Course Project

**Veeam Cyber-Resilient Data Protection Platform**

Design:

```text
Production VMware / Hyper-V
        |
      Proxies
        |
Primary Repository
        |
        +---- Hardened Immutable Repository
        |
        +---- Backup Copy / Object
        |
        +---- Tape
        |
     Replication
        |
      DR Site
```

Test:

```text
file restore
VM restore
Instant Recovery
application recovery
SureBackup
replica failover
failback
ransomware recovery
```

---

# Recommended Study Sequence

Use the files in this exact order.

## Step 1 — Storage

Study Course 34 until you can answer:

```text
What is the I/O path?
Block vs file vs object?
RAID?
SAN?
iSCSI?
NFS?
Multipathing?
IOPS vs throughput vs latency?
```

Then continue.

## Step 2 — Data Center

Study Course 35 until you can draw:

```text
rack
power
cooling
network
storage
security
```

and identify failure domains.

## Step 3 — Backup Concepts

Study Course 36 until you understand:

```text
RPO
RTO
backup chains
immutability
3-2-1-1-0
GFS
recovery verification
```

before touching Veeam configuration.

## Step 4 — Veeam

Then implement the same concepts with:

```text
Veeam Backup Server
Proxy
Repository
SOBR
Hardened Repository
Backup Copy
SureBackup
Replication
Tape
```

---

# Integrated Phase Architecture

```text
                        Business Application
                                |
                         Compute / VM
                                |
                        Storage Access
                                |
                  +-------------+-------------+
                  |                           |
                 SAN                         NAS
                  |                           |
             Storage Array                File Storage
                  |
            Data Center Rack
                  |
       +----------+----------+
       |                     |
     Power                 Network
       |                     |
 UPS / Generator        Leaf / Spine
       |
     Cooling
       |
   Data Center
       |
       v
  Backup Platform
       |
       +-- Primary Repository
       +-- Immutable Repository
       +-- Offsite Object
       +-- Tape
       +-- DR Replica
```

You should be able to trace both:

```text
Production I/O path
```

and:

```text
Recovery path
```

---

# Phase 8 Integrated Capstone

Design a complete infrastructure for a manufacturing company.

## Workloads

```text
100 VMs
5 physical servers
ERP database
MES
Active Directory
File server
20 TB quality/production files
```

## Production

```text
dual power
dual network
dual SAN paths
redundant storage
```

## Backup

```text
primary backup
immutable copy
offsite copy
tape/archive
```

## DR

```text
secondary site
replication
backup restore
```

## Required Deliverables

```text
01_REQUIREMENTS.md
02_STORAGE_ARCHITECTURE.md
03_SAN_NAS.md
04_RACK_LAYOUT.md
05_POWER.md
06_COOLING.md
07_NETWORK.md
08_SECURITY.md
09_CAPACITY.md
10_BACKUP_ARCHITECTURE.md
11_VEEAM_DESIGN.md
12_IMMUTABILITY.md
13_DR.md
14_MONITORING.md
15_RUNBOOKS.md
```

---

# How to Learn from the Files

For every topic:

```text
Read
   ↓
Redraw diagram without looking
   ↓
Type command manually
   ↓
Predict result
   ↓
Run in lab
   ↓
Break something safely
   ↓
Troubleshoot
   ↓
Write your own runbook
```

Examples:

Storage:

```bash
lsblk
iostat -xz 1
multipath -ll
```

Windows:

```powershell
Get-Disk
Get-Volume
```

Veeam:

```powershell
Get-VBRJob
Get-VBRBackup
Get-VBRBackupRepository
```

The goal is to connect every command to an architectural layer.

---

# Phase 8 Completion Checklist

## Storage

- [ ] I understand block/file/object.
- [ ] I understand DAS/NAS/SAN.
- [ ] I understand HDD/SSD/NVMe.
- [ ] I understand RAID.
- [ ] I understand arrays, pools, volumes, LUNs.
- [ ] I understand FC zoning/masking.
- [ ] I understand iSCSI.
- [ ] I understand NFS/SMB.
- [ ] I understand multipathing.
- [ ] I understand snapshots/replication.
- [ ] I can interpret IOPS/throughput/latency.

## Data Center

- [ ] I can create rack elevations.
- [ ] I understand rack power.
- [ ] I understand A/B power.
- [ ] I understand UPS/generator.
- [ ] I understand N+1/2N.
- [ ] I understand cooling/containment.
- [ ] I understand PUE.
- [ ] I understand structured cabling.
- [ ] I understand leaf-spine.
- [ ] I understand OOB.
- [ ] I understand physical security.
- [ ] I can perform SPOF analysis.
- [ ] I understand DR site types.

## Backup

- [ ] I understand backup/snapshot/replication/archive.
- [ ] I understand RPO/RTO.
- [ ] I understand full/incremental/differential.
- [ ] I understand synthetic full.
- [ ] I understand application consistency.
- [ ] I understand backup infrastructure.
- [ ] I understand 3-2-1-1-0.
- [ ] I understand immutability.
- [ ] I understand GFS.
- [ ] I can calculate backup capacity.
- [ ] I understand recovery verification.
- [ ] I understand clean-room recovery.

## Veeam

- [ ] I understand Veeam components.
- [ ] I understand backup-job flow.
- [ ] I understand CBT/application-aware processing.
- [ ] I understand forward/active/synthetic full.
- [ ] I understand GFS.
- [ ] I understand Backup Copy.
- [ ] I understand SOBR.
- [ ] I understand hardened repositories.
- [ ] I understand Instant Recovery.
- [ ] I understand SureBackup.
- [ ] I understand replication/failback.
- [ ] I understand tape/agents.
- [ ] I can use basic Veeam PowerShell.
- [ ] I can troubleshoot Source/Proxy/Network/Target bottlenecks.
- [ ] I understand Veeam cyber-recovery architecture.

---

# Folder Structure

```text
Phase_8_Storage_Data_Center/
│
├── README.md
├── 34_Information_Storage_and_Management.md
├── 35_Data_Center_Infrastructure_Design.md
├── 36_Enterprise_Backup_and_Recovery.md
└── 37_Veeam_Backup_and_Replication.md
```

---

# Next Phase

After Phase 8:

```text
Phase 9 — Virtualization

38. Virtualization Fundamentals
39. VMware vSphere: Install, Configure and Manage
40. VMware NSX
41. OpenStack Fundamentals
42. OpenStack Deployment and Operation
43. OpenStack APIs
44. Nutanix Multicloud Infrastructure
```

The dependency is:

```text
Storage + Data Center
        ↓
Virtualization Infrastructure
        ↓
Private Cloud / Software-Defined Infrastructure
```
