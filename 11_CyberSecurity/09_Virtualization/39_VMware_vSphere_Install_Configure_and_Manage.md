# 39. VMware vSphere: Install, Configure and Manage

> Phase 9 — Virtualization

This course converts the general virtualization concepts from Course 38 into a complete VMware vSphere administration workflow.

**Current reference baseline:** VMware vSphere **9.1**.

Broadcom's current vSphere 9.1 documentation uses the term **ESX** in several installation and management guides, while many existing commands, knowledge-base articles, product histories, and administrator habits still use **ESXi**. In this learning material, **ESX/ESXi host** refers to the VMware bare-metal hypervisor host unless a release-specific distinction is important.

The course is built around one complete infrastructure path:

```text
Physical Server
      ↓
ESX / ESXi
      ↓
Management Network
      ↓
vCenter Server
      ↓
Data Center
      ↓
Cluster
      ↓
Virtual Networking
      ↓
Shared / Local Storage
      ↓
Virtual Machines
      ↓
vMotion / HA / DRS
      ↓
Lifecycle / Security / Monitoring
      ↓
Automation / Troubleshooting
```

The goal is not to memorize vSphere Client menus.

You should be able to reason about:

```text
What component owns the function?
What network carries the traffic?
What datastore contains the VM?
What host currently runs the VM?
What happens if the host fails?
What happens if the SAN path fails?
What happens if vCenter fails?
What configuration survives?
What evidence should I collect before changing anything?
```

The learning method throughout the file is:

```text
Concept
   ↓
Architecture Diagram
   ↓
GUI / ESXCLI / PowerCLI Example
   ↓
Expected Behavior
   ↓
Why It Works
   ↓
Failure Scenario
   ↓
Troubleshooting
```

---

## 1. Topic Title

**VMware vSphere: Install, Configure and Manage**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain VMware vSphere architecture.
- Explain the roles of ESX/ESXi and vCenter Server.
- Plan DNS, NTP, networking, storage, hardware compatibility, and addressing before installation.
- Install an ESX/ESXi host in a lab.
- Configure the ESX management network through the DCUI.
- Use VMware Host Client for standalone-host administration.
- Use ESXCLI and selected native tools for evidence collection and troubleshooting.
- Deploy the vCenter Server appliance using the current two-stage deployment model.
- Explain vCenter appliance sizing, FQDN, DNS, NTP, and SSO-domain planning.
- Build vCenter inventory using data centers, folders, clusters, hosts, resource pools, networks, and datastores.
- Add/remove hosts safely.
- Explain maintenance mode and host lifecycle.
- Configure vSphere Standard Switches.
- Configure VMkernel adapters.
- Configure management, vMotion, NFS, and iSCSI network paths.
- Explain VLAN tagging and MTU.
- Explain NIC teaming, failover order, load-balancing policies, and link-failure behavior.
- Explain vSphere Distributed Switch architecture.
- Explain distributed port groups, uplinks, Network I/O Control, and rollback/recovery considerations.
- Explain virtual-machine port groups versus VMkernel networking.
- Configure and troubleshoot VMFS datastores.
- Configure and troubleshoot NFS datastores.
- Explain Fibre Channel, iSCSI, multipathing, path-selection, and datastore presentation.
- Explain vSphere Virtual Volumes (vVols).
- Explain Storage Policy Based Management (SPBM).
- Create and configure virtual machines.
- Explain virtual hardware versions, firmware, VMware Tools, VMXNET3, PVSCSI, virtual NVMe, and device selection.
- Create and use templates, clones, customization specifications, and Content Libraries.
- Explain VM snapshots and consolidation.
- Configure VM CPU, memory, disk, and network resources.
- Explain shares, reservations, limits, and resource pools.
- Explain vMotion.
- Explain Storage vMotion.
- Explain EVC.
- Configure and reason about vSphere HA.
- Explain datastore/network heartbeats, isolation, restart priority, admission control, and N+1 capacity.
- Explain vSphere Fault Tolerance.
- Explain DRS and automated resource placement.
- Explain affinity/anti-affinity rules.
- Explain vCenter Single Sign-On, roles, permissions, and least privilege.
- Explain certificate and VMCA concepts.
- Explain host lockdown, ESX Shell/SSH exposure, Secure Boot, TPM, and logging concepts.
- Explain host profiles and configuration consistency.
- Explain vSphere Lifecycle Manager images and remediation.
- Explain cluster image compliance.
- Explain VM hardware/VMware Tools lifecycle.
- Monitor tasks, events, alarms, performance, hosts, VMs, networks, and storage.
- Use `esxtop` for host-level troubleshooting.
- Install and use current VCF PowerCLI for vSphere automation.
- Build inventory, health, configuration, and capacity reports with PowerCLI.
- Troubleshoot host disconnects, VM startup failures, vMotion failures, storage issues, network failures, HA events, snapshots, and capacity problems.
- Build a complete small-enterprise vSphere platform mini project.

---

## 3. Prerequisites

Required:

- 38. Virtualization Fundamentals
- Networking fundamentals
- Linux/Windows administration
- 34. Information Storage and Management
- 35. Data Center Infrastructure Design
- 36. Enterprise Backup and Recovery

Recommended lab:

```text
Management Workstation
     |
     +-- DNS/NTP
     |
     +-- ESX Host 01
     |
     +-- ESX Host 02
     |
     +-- optional ESX Host 03
     |
     +-- vCenter Server Appliance
     |
     +-- shared NFS/iSCSI storage
```

Nested lab option:

```text
Physical PC
   |
VMware Workstation / Fusion / compatible hypervisor
   |
   +-- Nested ESX01
   +-- Nested ESX02
   +-- Nested Storage VM
   +-- vCenter Appliance
```

Recommended minimum conceptual networks:

```text
Management
VM Production
vMotion
Storage
Backup
```

Example addressing:

```text
Management:
10.10.10.0/24

vMotion:
10.10.20.0/24

Storage:
10.10.30.0/24

VM Network:
10.10.100.0/24
```

Before building production vSphere, always verify:

```text
server compatibility
CPU compatibility
NIC/HBA support
storage support
firmware
drivers
release interoperability
```

against the current vendor/Broadcom compatibility information.

---

## 4. Core Concepts Explanation

# Part 1 — VMware vSphere Architecture

vSphere is the virtualization platform.

Core architecture:

```text
                 vCenter Server
                      |
        +-------------+-------------+
        |             |             |
      ESX01         ESX02         ESX03
        |             |             |
      VMs           VMs           VMs
        \             |             /
         \            |            /
          +-------- Storage -------+
                   Network
```

Two most important components:

```text
ESX / ESXi
  runs VMs

vCenter Server
  centrally manages hosts, clusters, networks,
  storage, permissions, HA/DRS, lifecycle, automation
```

---

# Part 2 — ESX / ESXi

The host is the bare-metal virtualization layer.

```text
Physical Hardware
      ↓
VMware ESX / ESXi
      ↓
Virtual Machines
```

The host manages:

```text
CPU scheduling
memory
virtual devices
VM networking
datastore access
local services
VM lifecycle
```

---

# Part 3 — vCenter Server

vCenter provides centralized management.

```text
Administrator
      |
vSphere Client / API / PowerCLI
      |
      v
vCenter Server
      |
      +-- Host A
      +-- Host B
      +-- Cluster
      +-- Datastores
      +-- Networks
      +-- VMs
```

vCenter enables or coordinates features such as:

```text
clusters
vMotion
HA
DRS
permissions
templates
Content Library
Lifecycle Manager
alarms/events
central inventory
```

---

# Part 4 — What Happens if vCenter Fails?

A common misconception:

```text
vCenter down
=
all VMs down
```

Normally:

```text
running VMs continue
ESX hosts continue running
```

But you lose or impair:

```text
central management
many cluster operations
vMotion initiation
central automation
inventory workflows
some lifecycle functions
central monitoring
```

Therefore vCenter is management-plane critical even though it is not the runtime process for each VM.

---

# Part 5 — vSphere Client

Primary administration UI:

```text
Browser
   ↓
vSphere Client
   ↓
vCenter
```

Inventory tree usually includes:

```text
vCenter
 └── Data Center
      └── Cluster
           ├── Host
           ├── Host
           └── VMs
```

Learn object hierarchy because permissions and settings can inherit through it.

---

# Part 6 — VMware Host Client

Standalone host UI:

```text
Browser
   ↓
ESX Host Client
   ↓
One Host
```

Useful when:

```text
vCenter unavailable
initial configuration
standalone lab
host troubleshooting
```

It does not provide full multi-host vCenter functionality.

---

# Part 7 — Planning Before Installation

Do not begin installation before defining:

```text
Hostnames
IP addresses
DNS
NTP
VLANs
MTU
physical NIC mappings
storage
root/admin access
vCenter FQDN
SSO domain
cluster layout
```

Example planning sheet:

```text
esx01.lab.example  10.10.10.11
esx02.lab.example  10.10.10.12
vc01.lab.example   10.10.10.20
nfs01.lab.example  10.10.30.10
```

---

# Part 8 — DNS Planning

vCenter and hosts depend heavily on correct name resolution.

Verify before deployment:

```text
A record:
vc01.lab.example -> 10.10.10.20

A record:
esx01.lab.example -> 10.10.10.11
```

From admin system:

```bash
nslookup vc01.lab.example
nslookup esx01.lab.example
```

Reverse DNS is also useful in many environments.

---

# Part 9 — Time Synchronization

Time affects:

```text
authentication
certificates
logs
Kerberos
troubleshooting
cluster behavior
```

Architecture:

```text
Authoritative NTP
      |
      +-- ESX01
      +-- ESX02
      +-- vCenter
```

All management systems should use trustworthy, consistent time.

---

# Part 10 — Hardware Compatibility

Before production installation verify:

```text
server model
CPU
NICs
HBAs
storage controller
firmware
driver
ESX release
```

A server that boots the installer is not automatically a supported production platform.

---

# Part 11 — Boot Mode

Modern servers commonly use:

```text
UEFI
```

Security design can include:

```text
Secure Boot
TPM
```

Do not casually change firmware boot mode after installation.

It can affect bootability and security configuration.

---

# Part 12 — ESX Installation Media

Installation methods can include:

```text
ISO
remote management virtual media
PXE / network boot
scripted installation
automated deployment
```

For a lab:

```text
mount ISO
boot
choose installation disk
set root/admin credential
reboot
```

---

# Part 13 — Installation Disk

The boot device can be:

```text
local SSD
RAID logical disk
vendor-supported boot device
```

Production design must follow current VMware and server-vendor guidance.

Do not place boot storage on an unsupported transient device.

---

# Part 14 — ESX Installation Flow

```text
Boot Installer
    ↓
Hardware Discovery
    ↓
Accept License
    ↓
Select Disk
    ↓
Keyboard
    ↓
Set Password
    ↓
Install
    ↓
Reboot
    ↓
DCUI
```

After installation, network configuration becomes the next critical step.

---

# Part 15 — DCUI

Direct Console User Interface provides local host configuration.

Used for:

```text
management network
hostname/DNS
restart management network
test management network
troubleshooting
ESX Shell access configuration
```

It is your emergency local path when remote management is broken.

---

# Part 16 — Management Network

Management network carries:

```text
Host Client
vCenter connection
host API
management traffic
```

Concept:

```text
Admin / vCenter
       |
Management VLAN
       |
vmk0
       |
ESX Host
```

Protect it strongly.

---

# Part 17 — VMkernel Adapter

VMkernel adapter (`vmk`) is a host-side virtual network interface.

Examples:

```text
vmk0
Management

vmk1
vMotion

vmk2
iSCSI / NFS
```

It is not a VM vNIC.

---

# Part 18 — Management IP

Example:

```text
esx01
vmk0
10.10.10.11/24
gateway 10.10.10.1
```

After setting:

```text
IP
mask
gateway
DNS
hostname
```

test connectivity from DCUI.

---

# Part 19 — DCUI Network Test

Use:

```text
Test Management Network
```

Validate:

```text
gateway
DNS
vCenter/admin target
```

If this fails, fix networking before adding the host to vCenter.

---

# Part 20 — ESXCLI

ESXCLI exposes many host operations.

Check version:

```bash
esxcli system version get
```

Typical output concepts:

```text
Product
Version
Build
Update
```

Use CLI for diagnosis and automation, not random experimentation on production.

---

# Part 21 — Enable Shell / SSH Carefully

ESX Shell/SSH are powerful.

Security model:

```text
normally disabled/restricted
   ↓
enable temporarily for support
   ↓
perform task
   ↓
disable again
```

Prefer API/Host Client/vCenter where practical.

---

# Part 22 — Host Network Inventory

```bash
esxcli network nic list
```

Shows physical adapters such as:

```text
vmnic0
vmnic1
vmnic2
vmnic3
```

Inspect:

```text
link state
speed
driver
MAC
```

---

# Part 23 — VMkernel Interfaces

```bash
esxcli network ip interface list
```

Use to inspect:

```text
vmk interfaces
enabled state
port group/switch attachment
```

IP configuration:

```bash
esxcli network ip interface ipv4 get
```

---

# Part 24 — IP Routes

```bash
esxcli network ip route ipv4 list
```

Troubleshooting sequence:

```text
vmk IP
   ↓
route
   ↓
gateway
   ↓
remote destination
```

---

# Part 25 — vmkping

Use VMkernel networking test:

```bash
vmkping 10.10.20.12
```

Useful for:

```text
vMotion network
storage network
management
MTU tests
```

Choose the correct VMkernel interface/network context.

---

# Part 26 — Jumbo Frame Testing

If using larger MTU, every device in the path must support it.

Concept:

```text
vmk
 ↓
vSwitch
 ↓
vmnic
 ↓
physical switch
 ↓
storage/host
```

One mismatch can cause silent fragmentation/drop behavior.

Use supported `vmkping` options for DF/size testing in your release.

---

# Part 27 — ESX Host Services

Hosts run management services.

Do not restart services blindly.

First identify:

```text
what service failed?
what dependency?
what logs?
what effect?
```

A management-agent problem is different from a VM runtime failure.

---

# Part 28 — Host Logs

Important host log categories include:

```text
host management
kernel
VMkernel
storage
network
authentication
VM processes
```

Collect support bundles before destructive troubleshooting when appropriate.

---

# Part 29 — Deploying vCenter Server

Current vCenter deployment uses an appliance-based model.

High-level:

```text
Mount vCenter Installer ISO
       ↓
Run Installer
       ↓
Stage 1
Deploy Appliance OVA
       ↓
Stage 2
Configure Appliance / SSO
```

---

# Part 30 — vCenter Deployment Stage 1

Stage 1 deploys the appliance VM.

You provide:

```text
target ESX/vCenter
VM name
deployment size
datastore
network
IP
FQDN
```

Result:

```text
vCenter appliance VM exists
```

but full vCenter service setup is not yet complete.

---

# Part 31 — vCenter Deployment Stage 2

Stage 2 configures:

```text
time
SSO domain
administrator
telemetry choices
service configuration
```

After completion:

```text
vSphere Client becomes available
```

---

# Part 32 — vCenter FQDN

Plan FQDN before deployment.

Example:

```text
vc01.lab.example
```

DNS must resolve consistently.

Changing vCenter identity later is far more complex than planning correctly at deployment.

---

# Part 33 — vCenter SSO Domain

A common internal SSO domain example is:

```text
vsphere.local
```

This is **not** your Active Directory DNS domain.

Example:

```text
AD domain:
corp.example

vCenter SSO domain:
vsphere.local
```

Keep these concepts separate.

---

# Part 34 — vCenter Administrator

Initial SSO admin identity is separate from operating-system or AD identities.

You later integrate enterprise identity/permissions according to design.

Avoid using the top-level SSO admin for daily VM operations.

---

# Part 35 — vCenter Inventory

Core hierarchy:

```text
vCenter
  |
  +-- Data Center
       |
       +-- Cluster
       |    |
       |    +-- Hosts
       |
       +-- Datastores
       +-- Networks
       +-- VMs / Folders
```

Inventory structure affects:

```text
permissions
organization
automation
policies
```

---

# Part 36 — Data Center Object

vCenter Data Center object is a logical management container.

It is not the physical building.

It groups:

```text
clusters
hosts
networks
datastores
VMs
```

---

# Part 37 — Folder Objects

Folders organize:

```text
VMs
hosts/clusters
networks
datastores
```

Use folders for:

```text
permissions
ownership
environment separation
automation targeting
```

Example:

```text
VMs
 ├── Production
 ├── Development
 └── Infrastructure
```

---

# Part 38 — Create Cluster

A cluster groups hosts for shared management.

```text
Cluster-01
  |
  +-- ESX01
  +-- ESX02
  +-- ESX03
```

Features can include:

```text
HA
DRS
EVC
shared lifecycle image
resource pools
```

---

# Part 39 — Add Host to vCenter

Workflow:

```text
vCenter
   ↓
Add Host
   ↓
FQDN/IP
   ↓
credentials
   ↓
certificate fingerprint
   ↓
license/location
   ↓
host managed centrally
```

Verify DNS and management connectivity first.

---

# Part 40 — Host Disconnect vs Remove

Disconnect:

```text
host remains inventory object
but vCenter management communication stops
```

Remove:

```text
host removed from inventory
```

Do not remove a host as the first troubleshooting reaction to connectivity problems.

---

# Part 41 — Maintenance Mode

Before planned host maintenance:

```text
enter maintenance mode
   ↓
migrate or shut down VMs
   ↓
perform maintenance
   ↓
validate host
   ↓
exit maintenance
```

Cluster capacity must support evacuation.

---

# Part 42 — Reboot Host Safely

Before reboot:

```text
maintenance mode
VM evacuation
storage/path health
cluster health
no concurrent risky maintenance
```

Then reboot through supported management.

After:

```text
verify networking
storage
cluster
VM placement
```

---

# Part 43 — Standard Virtual Switch

vSphere Standard Switch (vSS) exists per host.

```text
ESX01
  |
  vSS0
  |
  +-- Management PG
  +-- VM Network PG
  |
  +-- vmnic0
  +-- vmnic1
```

Configuration is host-local.

---

# Part 44 — Standard Switch Architecture

```text
VM vNIC ----\
             \
VMkernel ----- vSS ----- vmnic ----- Physical Switch
             /
VM vNIC ----/
```

The switch handles Layer-2 forwarding within the host.

---

# Part 45 — Standard Port Group

Port group applies network settings to attached ports.

Example:

```text
PG-PROD-WEB
VLAN 100

PG-PROD-APP
VLAN 200
```

VM vNIC attaches to a port group.

---

# Part 46 — VMkernel Port Group

A VMkernel adapter attaches to a VMkernel-capable port group/network.

Used for host services:

```text
management
vMotion
NFS
iSCSI
provisioning
other platform services
```

---

# Part 47 — Virtual Machine Port Group

VM port group:

```text
VM traffic
```

VMkernel port:

```text
host service traffic
```

This distinction prevents many configuration mistakes.

---

# Part 48 — VLAN Tagging

Example:

```text
Port Group VLAN ID = 100
```

Physical switch trunk carries VLAN 100.

Architecture:

```text
VM
 ↓
Port Group VLAN 100
 ↓
vSwitch
 ↓
vmnic
 ↓
802.1Q trunk
 ↓
Physical Switch
```

Both virtual and physical sides must agree.

---

# Part 49 — VLAN 0 / Untagged Concepts

Depending on topology, port groups can use:

```text
untagged/native-style traffic
specific VLAN
trunking for specialized designs
```

Do not guess VLAN IDs.

Document physical switch configuration.

---

# Part 50 — NIC Teaming

Multiple uplinks:

```text
vmnic0 \
         vSwitch
vmnic1 /
```

Benefits:

```text
redundancy
traffic distribution
```

The virtual and physical switch policy must align.

---

# Part 51 — Active / Standby Uplinks

Example:

```text
Management:
vmnic0 active
vmnic1 standby

vMotion:
vmnic1 active
vmnic0 standby
```

This can separate normal traffic while maintaining failover.

---

# Part 52 — Load Balancing Policy

Policies can distribute VM/port traffic based on platform-supported algorithms.

Conceptual examples:

```text
originating virtual port
source MAC
IP hash
load-based policies on distributed switches
```

IP-hash/LACP-style designs require matching physical-switch configuration.

---

# Part 53 — Failback Policy

After failed uplink returns:

```text
failback enabled
  → traffic can return automatically

failback disabled
  → traffic may remain on surviving uplink
```

Choose deliberately.

---

# Part 54 — Link Status vs Beacon Probing

Link status detects local physical-link failure.

It might not detect failures beyond the immediate switch port.

Other failure-detection mechanisms can provide broader detection in certain designs.

Use supported network architecture rather than enabling advanced options randomly.

---

# Part 55 — MTU

Standard Ethernet commonly:

```text
1500
```

Jumbo designs commonly use a larger MTU such as:

```text
9000
```

but exact value must be consistent across the full path.

---

# Part 56 — Physical Switch Dependency

Virtual networking cannot fix:

```text
wrong trunk
wrong VLAN
port shutdown
LACP mismatch
MTU mismatch
physical loop
```

Always coordinate virtual and physical network configuration.

---

# Part 57 — vSphere Distributed Switch

vDS centralizes switch configuration across hosts through vCenter.

```text
vCenter
   |
Distributed Switch
   |
   +-- Host A uplinks
   +-- Host B uplinks
   +-- Host C uplinks
```

Benefits:

```text
consistency
central configuration
advanced networking features
```

---

# Part 58 — vDS Control vs Data Plane

vCenter manages configuration.

Actual VM traffic continues on ESX hosts.

```text
vCenter unavailable
   ↓
existing distributed-switch forwarding can continue
```

But management changes are impaired.

---

# Part 59 — Distributed Port Group

Logical network on vDS.

Example:

```text
DVPG-WEB
VLAN 100

DVPG-APP
VLAN 200

DVPG-DB
VLAN 300
```

Applied consistently to all participating hosts.

---

# Part 60 — vDS Uplinks

Distributed uplinks are logical names mapped to physical NICs.

Example:

```text
Uplink1 -> vmnic0
Uplink2 -> vmnic1
```

Mapping should be consistent across hosts.

---

# Part 61 — Migrating vSS to vDS

High-risk sequence if management network is involved.

Safe principle:

```text
create vDS
   ↓
add hosts
   ↓
add one uplink carefully
   ↓
migrate VMkernel/management
   ↓
test
   ↓
migrate remaining uplinks
```

Avoid migrating every management uplink at once.

---

# Part 62 — vDS Rollback Thinking

Before networking change:

```text
console/DCUI access?
spare uplink?
management reachability?
physical switch ready?
rollback path?
```

A bad vDS migration can disconnect many hosts simultaneously.

---

# Part 63 — Network I/O Control

NIOC allocates relative/guaranteed bandwidth among traffic classes on supported distributed-switch designs.

Traffic examples:

```text
management
vMotion
storage
VM traffic
backup
```

It matters during contention.

---

# Part 64 — VMkernel Service: vMotion

vMotion VMkernel network carries live-migration traffic.

Design:

```text
ESX01 vmk1
10.10.20.11

ESX02 vmk1
10.10.20.12
```

Prefer:

```text
low latency
high bandwidth
isolated/controlled network
```

---

# Part 65 — VMkernel Service: NFS

NFS datastore traffic uses host VMkernel networking.

```text
ESX vmk
   |
Storage VLAN
   |
NFS Server
```

Route/VLAN/MTU must be correct.

---

# Part 66 — VMkernel Service: iSCSI

Software iSCSI uses VMkernel networking.

```text
ESX
 |
vmk2 / vmk3
 |
Storage Network A/B
 |
iSCSI Target
```

Multipathing and port-binding design must follow supported topology.

---

# Part 67 — VMFS

VMware VMFS is a clustered filesystem designed for vSphere datastore use.

```text
SAN LUN
   ↓
VMFS Datastore
   ↓
Multiple ESX Hosts
   ↓
VM Files
```

Multiple hosts can safely access the same datastore.

---

# Part 68 — VMFS Datastore Contents

A VM directory can contain:

```text
configuration
virtual disks
snapshot deltas
logs
swap
NVRAM/firmware state
```

Do not delete VM files manually unless you fully understand their role.

---

# Part 69 — List Datastores from Host CLI

```bash
esxcli storage filesystem list
```

Inspect:

```text
mount point
volume name
UUID
filesystem type
size
free
```

---

# Part 70 — Storage Device Inventory

```bash
esxcli storage core device list
```

Use to inspect:

```text
device identifier
vendor/model
size
queue characteristics
state
```

---

# Part 71 — Storage Paths

```bash
esxcli storage core path list
```

Concept:

```text
Device
  |
  +-- Path A
  +-- Path B
  +-- Path C
  +-- Path D
```

A device may remain available after one path fails.

---

# Part 72 — Fibre Channel Architecture

```text
ESX HBA A -> Fabric A -> Array Port A
ESX HBA B -> Fabric B -> Array Port B
```

Storage team configures:

```text
WWPN zoning
LUN masking
array host objects
```

ESX then discovers devices.

---

# Part 73 — Rescan Storage

After presenting a LUN, rescan adapters through vSphere Client or supported CLI/API.

Concept:

```text
Array presents LUN
   ↓
ESX rescan
   ↓
device discovered
   ↓
create/mount datastore
```

Do not repeatedly rescan as a substitute for fixing SAN zoning/masking errors.

---

# Part 74 — Software iSCSI Adapter

Architecture:

```text
VMkernel
   ↓
Software iSCSI Adapter
   ↓
TCP/IP
   ↓
Target
```

Requires:

```text
network
target discovery
authentication if used
LUN mapping
multipath design
```

---

# Part 75 — iSCSI Target Discovery

Concepts:

```text
dynamic discovery
static target
```

Before storage appears, verify:

```text
vmk connectivity
TCP path
target portal
IQN/access
```

---

# Part 76 — NFS Datastore

Architecture:

```text
ESX
 |
VMkernel
 |
NFS
 |
NAS
 |
Export
```

The NAS owns the filesystem.

vSphere mounts the export as datastore.

---

# Part 77 — NFS Permissions

Storage server controls:

```text
export path
allowed ESX IPs
read/write
root/security behavior
```

A network ping does not prove the NFS export is authorized correctly.

---

# Part 78 — Multipathing

vSphere uses multipathing to maintain storage access across path failures.

```text
ESX
 |\
 | \
A  B
|  |
Storage
```

Inspect path health before maintenance.

---

# Part 79 — Path Selection Policy

Path-selection strategies decide how I/O uses available paths.

Concepts include:

```text
fixed/preferred path
most recently used style
round-robin style
vendor/storage-specific policy
```

Follow storage-vendor support guidance.

---

# Part 80 — APD and PDL Concepts

Two important storage-loss concepts:

```text
APD
All Paths Down
temporary/unknown reachability loss

PDL
Permanent Device Loss
array reports device permanently unavailable
```

Host/VM response differs.

Understand before designing HA reactions.

---

# Part 81 — Virtual Volumes (vVols)

vVols shifts storage management toward VM/object-level policy.

Traditional:

```text
Many VMs
inside
one datastore/LUN
```

vVols:

```text
VM objects
mapped through storage policy
to array capabilities
```

---

# Part 82 — VASA / Storage Provider Concept

vVols relies on storage-provider integration exposing array capabilities.

Concept:

```text
vCenter / SPBM
      |
Storage Provider
      |
Array Capabilities
```

Exact deployment is storage-vendor specific.

---

# Part 83 — Storage Policy Based Management

SPBM lets you express requirements such as:

```text
performance
replication
encryption
failure tolerance
```

Then assign a storage policy to VM/virtual disks.

Concept:

```text
VM Requirement
   ↓
Storage Policy
   ↓
Compatible Datastore/Storage
```

---

# Part 84 — Datastore Capacity

Monitor:

```text
total
used
free
growth
snapshot growth
thin provisioning
```

A datastore is not safe merely because underlying array has unallocated capacity.

---

# Part 85 — Datastore Full Failure

Possible effects:

```text
VM writes fail
snapshots fail
VM pauses
swap cannot grow
vMotion/storage tasks fail
```

Respond with supported capacity operations.

Never delete unknown VMDKs manually.

---

# Part 86 — Virtual Machine Creation

Workflow:

```text
New VM
  ↓
name/folder
  ↓
compute resource
  ↓
datastore
  ↓
compatibility/hardware version
  ↓
guest OS
  ↓
CPU/RAM
  ↓
disk/network
  ↓
install OS
```

---

# Part 87 — VM Hardware Version / Compatibility

Virtual hardware version determines which virtual-device/features are available.

Newer compatibility can require newer ESX.

Do not upgrade VM compatibility before verifying:

```text
host compatibility
backup
rollback limitations
application support
```

---

# Part 88 — Firmware: BIOS vs UEFI

Modern VMs often use UEFI.

UEFI enables features such as:

```text
Secure Boot
modern OS requirements
vTPM integration
```

Changing firmware type after OS installation can make VM unbootable.

---

# Part 89 — VMware Tools

VMware Tools improves guest integration.

Functions can include:

```text
optimized drivers
guest heartbeat
clean shutdown
time integration
IP reporting
quiescing support
```

Keep Tools lifecycle aligned with host/guest compatibility.

---

# Part 90 — VMXNET3

VMXNET3 is a paravirtualized VMware network adapter designed for efficient virtual networking.

Use supported VMware Tools/guest drivers.

Compared with legacy emulated NICs:

```text
lower overhead
better throughput/features
```

---

# Part 91 — PVSCSI

Paravirtualized SCSI adapter for high-performance VM storage workloads.

Good candidates:

```text
database
high I/O servers
```

Ensure guest OS has the driver before switching a boot disk controller.

---

# Part 92 — Virtual NVMe

Modern guests can use virtual NVMe devices where supported.

Benefits can include:

```text
parallel queues
modern storage semantics
lower overhead
```

Choose based on guest/application compatibility.

---

# Part 93 — Add CPU and Memory

VM settings define:

```text
vCPU
cores/socket topology
vRAM
hot-add capabilities
```

Do not oversize automatically.

Course 38 right-sizing concepts still apply.

---

# Part 94 — CPU Hot Add

Some guest/platform combinations allow CPU hot-add.

Tradeoff:

```text
operational flexibility
```

but CPU topology/NUMA behavior and guest licensing can be affected.

Plan rather than enabling every feature blindly.

---

# Part 95 — Memory Hot Add

Allows supported guest to add memory while running.

Again, verify:

```text
guest support
NUMA implications
application support
```

---

# Part 96 — Add Virtual Disk

Choose:

```text
size
provisioning
controller
datastore
sharing mode if special cluster case
storage policy
```

VMware provisioning modes must be understood in context of datastore/storage features.

---

# Part 97 — Thin Provisioned VMDK

Logical disk larger than currently consumed physical capacity.

Example:

```text
VMDK logical = 500 GB
used blocks = 90 GB
```

Monitor datastore and array thin provisioning together.

---

# Part 98 — Thick Provisioning Concepts

Different thick modes can allocate blocks up front with different zeroing behaviors.

The important operational lesson:

```text
thick consumes/reserves more immediately
thin delays physical consumption
```

Performance/features depend on storage and mode.

---

# Part 99 — Virtual Disk Expansion

Expanding VMDK:

```text
increase virtual disk
   ↓
guest discovers larger block device
   ↓
extend partition/LVM/filesystem
```

Hypervisor expansion alone does not automatically enlarge guest filesystem.

---

# Part 100 — VM Snapshots in vSphere

Snapshot can capture:

```text
virtual disk state
optionally memory
```

Writes go to delta files after snapshot.

```text
Base VMDK
   ↓
Delta
```

Use for short-term operational rollback.

---

# Part 101 — Snapshot Chain

```text
Base
  ↓
Snap A Delta
  ↓
Snap B Delta
  ↓
Current Delta
```

Long chains can cause:

```text
capacity growth
performance impact
backup complexity
consolidation risk
```

---

# Part 102 — Snapshot Deletion

Deleting snapshot generally means:

```text
merge/consolidate delta data
```

It does **not** mean deleting the VM data captured after the snapshot in the simple sense.

Large consolidation may require heavy storage I/O and free space.

---

# Part 103 — Snapshot Consolidation

Consolidation can be required when snapshot metadata/delta state is inconsistent after backup or failed task.

Before consolidation:

```text
check datastore space
check backup jobs
check storage performance
check VM I/O
```

---

# Part 104 — Clone

Create VM copy:

```text
Source VM
   ↓
Clone
   ↓
New VM
```

Set:

```text
new name
network
customization
datastore
compute location
```

---

# Part 105 — Template

Convert or clone VM into reusable deployment source.

Golden-template workflow:

```text
Build OS
  ↓
Patch
  ↓
VMware Tools
  ↓
Security baseline
  ↓
Remove secrets
  ↓
Generalize
  ↓
Template
```

---

# Part 106 — Guest Customization Specification

Automates guest identity settings during clone deployment.

Can include:

```text
hostname
network
domain/workgroup
Windows Sysprep-style settings
Linux customization
```

This prevents manually editing every clone.

---

# Part 107 — Content Library

Content Library stores/distributes:

```text
templates
OVF/OVA
ISO
other deployment content
```

Useful for:

```text
standardization
multi-vCenter distribution
versioned deployment content
```

---

# Part 108 — Local vs Subscribed Content Library

Concept:

```text
Publisher Library
      ↓
Subscribed Library
```

Can distribute standardized templates across sites.

Plan storage and synchronization bandwidth.

---

# Part 109 — OVF / OVA

OVF:

```text
virtual appliance descriptor + files
```

OVA:

```text
single packaged archive
```

Used to distribute appliances such as:

```text
vCenter
network/security appliances
vendor management systems
```

---

# Part 110 — VM Resource Settings

Core:

```text
CPU
Memory
Storage
Network
```

Advanced policies:

```text
shares
reservations
limits
```

Do not confuse configured VM size with guaranteed physical resource.

---

# Part 111 — CPU Reservation

Guarantees minimum CPU capacity when available according to resource-management semantics.

Useful for:

```text
critical workloads
```

Too many reservations can prevent VM power-on/migration due to admission constraints.

---

# Part 112 — CPU Limit

Caps VM CPU consumption.

Common hidden performance problem:

```text
Host CPU free
but
VM CPU limited
```

Check limits before adding vCPU.

---

# Part 113 — CPU Shares

Relative priority during contention.

```text
Production
High

Development
Low
```

Shares matter primarily when resources are contested.

---

# Part 114 — Memory Reservation

Guarantees physical memory backing according to policy.

Large reservations reduce cluster flexibility.

Some workloads/features can require special reservation behavior.

---

# Part 115 — Memory Limit

Caps VM memory resource use.

A low limit can induce guest/hypervisor memory pressure even if configured memory is large.

---

# Part 116 — Resource Pool

Logical container for resource entitlement.

```text
Cluster
  |
  +-- Production Pool
  +-- Test Pool
```

Use for policy/organizational requirements.

Do not create deep resource-pool hierarchies without understanding share normalization.

---

# Part 117 — Resource Pool Mistake

Bad:

```text
Resource pool used only as a folder
```

Resource pools have resource-allocation semantics.

Use VM folders for organization if you do not need resource policy.

---

# Part 118 — vMotion

vMotion moves running VM compute execution between hosts.

```text
ESX01
  VM running
     |
     | memory/state transfer
     v
ESX02
  VM continues
```

Minimal interruption.

---

# Part 119 — vMotion Requirements

Conceptually check:

```text
vMotion VMkernel connectivity
CPU compatibility
target resources
network compatibility
VM device compatibility
storage accessibility or migration mode
```

Exact requirements depend on migration type.

---

# Part 120 — vMotion Data Flow

```text
VM runs on source
   ↓
memory copied
   ↓
dirty pages recopied
   ↓
brief switchover
   ↓
VM resumes target
```

High dirty-page workloads can extend migration time.

---

# Part 121 — EVC

Enhanced vMotion Compatibility masks/selects CPU feature baseline across cluster.

Goal:

```text
hosts with different CPU generations
   ↓
common CPU feature baseline
   ↓
VMs can vMotion safely
```

It cannot make incompatible CPU vendors equivalent.

---

# Part 122 — Per-VM EVC Concept

Some environments allow VM-specific EVC baselines.

Useful for portability/migration planning.

Always understand the lowest CPU capability exposed to the guest.

---

# Part 123 — Storage vMotion

Moves VM storage between datastores while VM remains running.

```text
Datastore A
    |
    | block copy
    v
Datastore B
```

Uses:

```text
storage maintenance
capacity
performance
migration
```

---

# Part 124 — Compute + Storage Migration

You can migrate:

```text
host
+
datastore
```

in one coordinated workflow where supported.

This enables shared-nothing or cross-storage migrations in suitable designs.

---

# Part 125 — vSphere HA

HA restarts VMs after host failure.

```text
ESX01 fails
   ↓
HA detects
   ↓
VMs restart
on ESX02/03
```

HA is **restart-based** availability.

---

# Part 126 — HA Agent / Cluster Control

HA uses host agents and cluster coordination.

The cluster needs:

```text
management connectivity
host health detection
datastore/network evidence
sufficient failover capacity
```

Do not troubleshoot HA only from VM state.

---

# Part 127 — HA Heartbeats

HA can use multiple signals.

Concept:

```text
Network heartbeat
+
Datastore heartbeat
```

This helps distinguish:

```text
host failure
network isolation
management partition
```

---

# Part 128 — Host Isolation

Host may be alive but lose management network.

```text
ESX01
  X
Management Network
```

HA isolation-response policy defines how VMs are handled.

Possible conceptual actions include:

```text
leave powered on
power off/restart elsewhere
shut down/restart elsewhere
```

Exact options depend on current platform behavior/configuration.

---

# Part 129 — Isolation Address

HA needs reliable network evidence to determine isolation.

Design management-network redundancy first rather than trying to fix poor topology only through extra detection settings.

---

# Part 130 — HA Restart Priority

Not all VMs are equally critical.

Example:

```text
Priority 1
Domain Controllers / DNS

Priority 2
Databases

Priority 3
Applications

Priority 4
Web / noncritical
```

Application dependency still requires proper service orchestration.

---

# Part 131 — HA Admission Control

Admission control asks:

```text
Can cluster tolerate required host failure(s)?
```

Example:

```text
3 hosts
workload needs all 3
```

There is no capacity for one host failure.

HA checkbox alone does not create spare compute.

---

# Part 132 — N+1 Cluster

```text
Workload requires 2 hosts
Installed = 3 hosts
```

One host can fail and workload can fit on the remaining 2.

This connects directly to Course 38 capacity planning.

---

# Part 133 — HA VM Monitoring

HA can monitor VM/guest/application health under supported configurations.

Concept:

```text
VM process running
but
guest/application not responsive
```

VM monitoring can initiate recovery according to policy.

Test carefully to avoid restart loops.

---

# Part 134 — vSphere Fault Tolerance

FT provides a higher availability model for supported VMs.

Concept:

```text
Primary VM
   ↔
Secondary VM
```

Both maintain synchronized execution state.

Host failure can allow secondary to continue with much lower interruption than ordinary HA restart.

---

# Part 135 — FT vs HA

```text
HA:
failure
→ VM restart
→ guest boot
→ app start

FT:
synchronized secondary
→ continued execution/failover
```

FT consumes more resources and has workload/platform restrictions.

---

# Part 136 — DRS

Distributed Resource Scheduler balances VM placement across cluster.

Inputs include:

```text
CPU
memory
policy
VM/host rules
resource pools
```

Actions can include migration recommendations/automation.

---

# Part 137 — DRS Automation

Conceptual levels:

```text
manual
partially automated
fully automated
```

Higher automation allows DRS to perform more placement/migration actions automatically.

Use change governance and monitoring.

---

# Part 138 — Initial Placement

When powering on VM, DRS can determine a suitable host based on:

```text
capacity
reservations
rules
resource state
```

This is better than always selecting the least-used host by human observation.

---

# Part 139 — DRS Rebalancing

If:

```text
Host A overloaded
Host B lightly used
```

DRS can recommend/use vMotion to rebalance.

Do not expect DRS to fix:

```text
bad SQL
storage bottleneck
guest memory leak
network congestion outside its control
```

---

# Part 140 — Affinity Rule

```text
VM A with VM B
```

Potential use:

```text
tight dependency
licensing
special topology
```

But it increases shared failure risk.

---

# Part 141 — VM Anti-Affinity Rule

```text
DC01
must separate from
DC02
```

Use to distribute redundant service instances.

---

# Part 142 — VM-to-Host Rules

Can pin/prefer certain VMs to host groups.

Use cases:

```text
license restrictions
hardware dependency
regulatory locality
```

Hard pinning reduces DRS/HA flexibility.

---

# Part 143 — Cluster Groups

You can logically group:

```text
VM groups
host groups
```

and create placement relationships.

Document why each rule exists.

---

# Part 144 — Cluster Capacity and Maintenance

Before host maintenance:

```text
normal load
+
one host evacuated
+
possible another failure
```

consider whether remaining cluster can sustain service.

Maintenance is a temporary degraded-resilience state.

---

# Part 145 — vCenter Single Sign-On

SSO authenticates identities for vSphere management.

Architecture:

```text
User
  ↓
Identity Source / SSO
  ↓
vCenter
  ↓
Role + Permission
```

Authentication and authorization are different steps.

---

# Part 146 — Role

Role is a set of privileges.

Examples:

```text
Read-Only
VM Operator
Virtualization Administrator
Network Administrator
```

Avoid giving full Administrator when a narrower role is sufficient.

---

# Part 147 — Permission

Permission combines:

```text
User/Group
+
Role
+
Inventory Object
+
Propagation
```

Example:

```text
AD Group: AppTeam
Role: VM Operator
Object: Production/AppTeam Folder
Propagate: Yes
```

---

# Part 148 — Permission Inheritance

Inventory hierarchy matters.

Permission at:

```text
vCenter
```

can propagate widely.

Permission at:

```text
one VM folder
```

can limit scope.

Use least privilege at the lowest practical object level.

---

# Part 149 — Identity Integration

Enterprise environments commonly integrate central identity services.

Design:

```text
identity group
   ↓
vCenter role
   ↓
inventory scope
```

Avoid individually assigning hundreds of users.

---

# Part 150 — Service Accounts

Automation/backup tools should use dedicated identities.

Examples:

```text
backup service
monitoring service
PowerCLI automation
```

Use:

```text
least privilege
credential rotation
auditability
```

---

# Part 151 — VMCA Concept

VMware Certificate Authority manages vSphere certificates in standard architectures.

Certificate trust affects:

```text
vCenter
hosts
browser/API clients
solution integrations
```

Do not replace certificates casually without a lifecycle plan.

---

# Part 152 — Certificate Expiration

Expired certificates can break:

```text
authentication
API
host connectivity
solution integration
```

Monitor certificate validity proactively.

---

# Part 153 — Secure Management Plane

Management components should use:

```text
private network
firewall restrictions
MFA where supported
RBAC
central logging
patched systems
trusted admin endpoints
```

Never expose host/vCenter administration openly to the Internet.

---

# Part 154 — Lockdown Mode

Lockdown reduces direct host-management paths and encourages administration through vCenter.

Useful for hardened environments.

But emergency access procedures must exist.

---

# Part 155 — ESX Shell Security

Keep:

```text
Shell
SSH
```

disabled when not needed.

If enabled:

```text
time-bound
authorized
logged
disabled afterward
```

---

# Part 156 — Secure Boot

Secure Boot helps ensure trusted boot components are used.

Requires compatible:

```text
UEFI
host firmware
ESX configuration
```

Do not disable security features simply to accommodate an unsupported driver.

---

# Part 157 — TPM

Trusted Platform Module can support host attestation/security features.

Architecture:

```text
Firmware
  ↓
TPM measurements
  ↓
attestation/trust evaluation
```

Protect TPM-backed recovery/ownership procedures.

---

# Part 158 — Host Firewall

ESX host firewall restricts management/service traffic.

Do not simply allow all services for troubleshooting.

Instead:

```text
identify required service
enable narrow rule
test
disable if temporary
```

---

# Part 159 — VM Network Security Policy

Virtual switch/port-group security settings can govern behaviors such as:

```text
promiscuous mode
MAC address changes
forged transmits
```

Default-secure behavior should be preserved unless a legitimate workload requires otherwise.

---

# Part 160 — Host Profiles

Host Profiles capture desired host configuration patterns.

Use:

```text
reference host/profile
   ↓
attach hosts/cluster
   ↓
check compliance
   ↓
remediate/customize
```

Helpful for consistency at scale.

---

# Part 161 — Host Profile Exceptions

Hosts may require host-specific values:

```text
IP
hostname
storage identifiers
```

Customization data handles these differences.

Do not force identical values where uniqueness is required.

---

# Part 162 — vSphere Lifecycle Manager

vSphere Lifecycle Manager manages host/cluster software lifecycle.

Modern cluster-image approach defines desired:

```text
ESX version
vendor add-on
firmware/driver integration where supported
components
```

Then checks compliance.

---

# Part 163 — Desired Cluster Image

Concept:

```text
Desired Image
   |
   +-- ESX version
   +-- vendor add-on
   +-- components
   +-- firmware integration
```

All hosts in cluster should converge on desired state.

---

# Part 164 — Compliance Check

```text
Host Current State
       vs
Desired Image
```

Result:

```text
Compliant
Noncompliant
Unknown / error
```

Investigate unknown state before remediation.

---

# Part 165 — Remediation

Remediation can require:

```text
maintenance mode
VM evacuation
software update
reboot
health check
exit maintenance
```

Cluster capacity and HA matter.

---

# Part 166 — Rolling Cluster Remediation

```text
Host A
evacuate → patch → reboot → return

Host B
evacuate → patch → reboot → return
```

This reduces service interruption.

Never remediate all hosts simultaneously unless the platform/workload design explicitly supports it.

---

# Part 167 — Firmware and Driver Compatibility

A newer driver is not automatically better.

Maintain supported combinations:

```text
ESX build
driver
NIC/HBA firmware
server BIOS
storage firmware
```

Use vendor-certified image/add-on strategy.

---

# Part 168 — VMware Tools Lifecycle

VMware Tools can be upgraded independently according to compatibility policy.

Sequence often considered:

```text
host lifecycle
   ↓
VMware Tools
   ↓
VM hardware compatibility
```

But application/vendor support must be checked.

---

# Part 169 — VM Hardware Upgrade

Virtual hardware upgrades can unlock features but may reduce backward compatibility.

Do not automatically upgrade every VM immediately after host upgrade.

Test first.

---

# Part 170 — vCenter Backup

vCenter appliance should have supported file-based configuration backup.

Protect:

```text
inventory/configuration
SSO-related state
vCenter services/config
```

This is separate from ordinary VM image backup considerations.

Test restore procedure.

---

# Part 171 — Backup of ESX Host Configuration

Host configuration can be recreated through:

```text
Host Profiles
automation
documented networking/storage
configuration backup approaches
```

Treat vCenter + configuration automation as critical recovery assets.

---

# Part 172 — Tasks and Events

Tasks answer:

```text
what operation ran?
```

Events answer:

```text
what happened?
```

Use them during troubleshooting before guessing.

Examples:

```text
VM reconfigured
host entered maintenance
vMotion started
datastore disconnected
HA restarted VM
```

---

# Part 173 — Alarms

Alarm model:

```text
Condition
   ↓
Warning/Critical
   ↓
Notification / Action
```

Useful conditions:

```text
host disconnected
datastore space low
VM CPU high
snapshot age
hardware sensor
HA issue
```

Every alarm should have an owner/runbook.

---

# Part 174 — Performance Overview

Monitor:

```text
CPU
memory
network
storage
VM
host
cluster
```

At each layer ask:

```text
usage?
contention?
latency?
errors?
```

---

# Part 175 — CPU Performance

Host/VM metrics include concepts such as:

```text
usage
demand
ready/scheduling wait
co-stop for SMP workloads
```

High guest CPU is not identical to high CPU ready.

---

# Part 176 — Memory Performance

Inspect concepts:

```text
configured
consumed
active
ballooning
swap
compression/reclamation
reservation
limit
```

Do not add guest RAM without checking host contention.

---

# Part 177 — Storage Performance

Measure:

```text
IOPS
throughput
latency
queue
path state
datastore free
```

Break latency into:

```text
guest
kernel
device/storage
```

where the platform exposes those views.

---

# Part 178 — Network Performance

Monitor:

```text
pNIC utilization
drops
errors
VM traffic
uplink distribution
MTU
team failover
```

High VM network latency may originate outside ESX.

---

# Part 179 — `esxtop`

`esxtop` is a host-level interactive performance tool.

Launch:

```bash
esxtop
```

Views include:

```text
CPU
memory
network
disk adapter
disk device
disk VM
```

Use evidence, not one number in isolation.

---

# Part 180 — `esxtop` CPU Thinking

Look for:

```text
host saturation
VM CPU demand
scheduling wait
large SMP contention
```

Do not memorize universal threshold numbers without workload context.

Trend and symptom correlation matter.

---

# Part 181 — `esxtop` Memory Thinking

Look for:

```text
ballooning
swapping
host memory pressure
VM memory behavior
```

Sustained swap activity is a strong sign of memory contention.

---

# Part 182 — `esxtop` Storage Thinking

Correlate:

```text
device latency
kernel latency
queue
IOPS
throughput
```

Then move down the stack:

```text
ESX
  ↓
HBA/NIC
  ↓
SAN/NAS
  ↓
array
```

---

# Part 183 — `esxtop` Network Thinking

Inspect:

```text
packets
Mb/s
drops
uplink
VM port
```

Drops require finding where queue/speed/policy causes loss.

---

# Part 184 — PowerCLI Becomes VCF PowerCLI

Current Broadcom automation package is **VCF PowerCLI**, the continuation/renaming of VMware PowerCLI.

Install current package:

```powershell
Install-Module -Name VCF.PowerCLI
```

Do not install an old `VMware.PowerCLI` package when building a new current lab unless compatibility requires it.

---

# Part 185 — Connect to vCenter with PowerCLI

```powershell
Connect-VIServer vc01.lab.example
```

Use secure certificate/credential handling.

Avoid scripts such as:

```powershell
$password = "SuperSecret123"
```

Prefer approved credential/secret mechanisms.

---

# Part 186 — Basic PowerCLI Inventory

Hosts:

```powershell
Get-VMHost
```

VMs:

```powershell
Get-VM
```

Datastores:

```powershell
Get-Datastore
```

Clusters:

```powershell
Get-Cluster
```

---

# Part 187 — PowerCLI VM Inventory Report

```powershell
Get-VM |
    Select-Object `
        Name,
        PowerState,
        NumCpu,
        MemoryGB
```

This converts GUI inventory into repeatable reporting.

---

# Part 188 — Host Inventory Report

```powershell
Get-VMHost |
    Select-Object `
        Name,
        ConnectionState,
        PowerState,
        NumCpu,
        MemoryTotalGB
```

Use for daily health reporting.

---

# Part 189 — Datastore Capacity Report

```powershell
Get-Datastore |
    Select-Object `
        Name,
        Type,
        CapacityGB,
        FreeSpaceGB
```

Add calculated percentage:

```powershell
Get-Datastore |
    Select-Object Name,
        @{N='UsedPct';E={
            [math]::Round(
                (1 - $_.FreeSpaceGB / $_.CapacityGB) * 100,
                1
            )
        }}
```

---

# Part 190 — VM Snapshot Inventory with PowerCLI

```powershell
Get-VM |
    Get-Snapshot |
    Select-Object `
        VM,
        Name,
        Created,
        SizeGB
```

Use for snapshot-sprawl reporting.

Do not automatically delete all snapshots from an unattended script without approval.

---

# Part 191 — VM Network Inventory

```powershell
Get-VM |
    Get-NetworkAdapter |
    Select-Object `
        Parent,
        Name,
        NetworkName,
        MacAddress,
        ConnectionState
```

Useful for VLAN/port-group audits.

---

# Part 192 — Host Network Inventory

```powershell
Get-VMHost |
    Get-VirtualSwitch
```

For distributed networking, use the current VCF PowerCLI distributed-switch cmdlets/modules appropriate to your build.

---

# Part 193 — Maintenance Mode with PowerCLI

Conceptual:

```powershell
$hostObj = Get-VMHost -Name esx01.lab.example

Set-VMHost `
    -VMHost $hostObj `
    -State Maintenance
```

Before doing this:

```text
verify DRS/evacuation
cluster capacity
VM exceptions
storage state
```

---

# Part 194 — Exit Maintenance Mode

```powershell
Set-VMHost `
    -VMHost $hostObj `
    -State Connected
```

Then validate:

```text
host health
datastores
network
VM placement
cluster compliance
```

---

# Part 195 — PowerCLI Safety

Before automation:

```text
scope
target vCenter
selected objects
dry-run/report where possible
approval
logging
rollback
```

Dangerous:

```powershell
Get-VM | Remove-VM -DeletePermanently
```

Never use destructive bulk commands casually.

---

# Part 196 — REST / API Automation Concept

vSphere exposes APIs.

Architecture:

```text
Automation
   |
API
   |
vCenter
   |
Inventory/Tasks
```

Use cases:

```text
provisioning
inventory
CMDB
monitoring
policy
CI/CD
```

PowerCLI uses VMware APIs under the hood.

---

# Part 197 — Host Disconnected Troubleshooting

Workflow:

```text
Host disconnected
   ↓
VMs still running?
   ↓
management IP reachable?
   ↓
DNS?
   ↓
TCP/API path?
   ↓
host management agents?
   ↓
certificate/time?
   ↓
vCenter service?
```

Do not reboot host immediately.

---

# Part 198 — Host Not Responding vs Disconnected

Disconnected can be administrative/manual or communication state.

Not Responding indicates vCenter lost expected communication.

Check:

```text
physical host
network
management vmk
switch
DNS
gateway
vCenter
```

---

# Part 199 — VM Will Not Power On

Possible:

```text
insufficient CPU/memory reservation
datastore full
file lock
invalid device
ISO inaccessible
host incompatible
license/policy
```

Read exact task/event error.

---

# Part 200 — vMotion Failure

Check:

```text
vMotion vmk reachability
MTU
CPU/EVC
target resources
network name/port group
storage accessibility
VM device
host version/compatibility
```

Test:

```bash
vmkping
```

on the relevant VMkernel network.

---

# Part 201 — Storage vMotion Failure

Check:

```text
destination free space
storage policy
datastore state
disk mode
snapshot
host path
storage latency
permissions
```

Do not assume network is the problem.

---

# Part 202 — NFS Datastore Disconnected

Check:

```text
vmk IP
route
VLAN
NFS server
export permission
NFS service
MTU
firewall
```

Use host/storage logs and `vmkping` appropriately.

---

# Part 203 — iSCSI Device Missing

Workflow:

```text
Storage target configured?
   ↓
VMkernel network?
   ↓
target portal reachable?
   ↓
iSCSI adapter?
   ↓
IQN authorization?
   ↓
LUN mapping?
   ↓
rescan?
```

Then inspect:

```bash
esxcli storage core device list
```

---

# Part 204 — Fibre Channel LUN Missing

Check with storage/network teams:

```text
HBA link
WWPN
fabric login
zoning
array host mapping
LUN masking
rescan
```

Do not recreate datastore if the real problem is FC visibility.

---

# Part 205 — One Storage Path Down

```text
Device still online
but
one path failed
```

Inspect:

```bash
esxcli storage core path list
```

Check:

```text
HBA
cable
SAN switch
array port
maintenance
```

Do not ignore redundancy degradation.

---

# Part 206 — APD Troubleshooting

All paths unavailable.

Check:

```text
fabric/network
array
target
maintenance
path state
other hosts
```

Protect workload and identify whether outage is temporary or permanent.

---

# Part 207 — Datastore Nearly Full

Response:

```text
identify largest consumers
snapshots?
thin growth?
swap?
ISO?
logs?
```

Then:

```text
extend datastore/storage
migrate VMs
consolidate supported snapshots
clean approved files
```

Never delete VMDKs manually based on filename alone.

---

# Part 208 — Snapshot Sprawl

PowerCLI report:

```powershell
Get-VM |
    Get-Snapshot |
    Where-Object {
        $_.Created -lt (Get-Date).AddDays(-7)
    }
```

This identifies old snapshots.

Review ownership/change ticket before removal.

---

# Part 209 — Snapshot Consolidation Failure

Check:

```text
datastore free space
active backup
file locks
storage latency
snapshot size
VM activity
```

Large merges can heavily load storage.

---

# Part 210 — HA Did Not Restart VM

Check:

```text
HA enabled?
VM protected?
cluster partition?
admission capacity?
datastore available?
restart priority/rules?
host failure correctly detected?
```

Read HA events before changing cluster settings.

---

# Part 211 — DRS Not Migrating VM

Possible:

```text
automation level
rules
reservations
EVC/CPU
device passthrough
vMotion issue
host capacity
VM pinned
```

DRS obeys constraints.

---

# Part 212 — VM CPU Performance Issue

Workflow:

```text
guest CPU high?
   ↓
host CPU high?
   ↓
CPU ready?
   ↓
vCPU oversized?
   ↓
limit?
   ↓
NUMA/topology?
```

Do not immediately add vCPU.

---

# Part 213 — VM Memory Performance Issue

Check:

```text
guest paging
ballooning
host swap
reservation
limit
active memory
cluster contention
```

Adding RAM can worsen host pressure.

---

# Part 214 — VM Disk Latency Issue

Trace:

```text
Guest
 ↓
VMDK/controller
 ↓
Datastore
 ↓
ESX path
 ↓
SAN/NFS
 ↓
Array
```

Use both vSphere metrics and storage-team evidence.

---

# Part 215 — VM Network Issue

Trace:

```text
guest IP
 ↓
vNIC connected?
 ↓
port group?
 ↓
VLAN?
 ↓
vSwitch/vDS?
 ↓
vmnic?
 ↓
physical switch?
 ↓
routing/firewall?
```

---

# Part 216 — Management Network Loss

If remote management disappears:

```text
use DCUI / OOB console
```

Check:

```text
vmk0
physical NIC
VLAN
switch port
gateway
DNS
```

Have an out-of-band recovery path before making network changes.

---

# Part 217 — vCenter Service Failure

If vCenter UI unavailable:

```text
ping/DNS
appliance VM running?
appliance management interface?
disk capacity?
services?
certificates?
time?
```

Running VMs usually continue.

Avoid rebooting all ESX hosts.

---

# Part 218 — vCenter Appliance Disk Full

Symptoms:

```text
services fail
UI unstable
database/log issues
```

Investigate appliance partitions and log growth using supported appliance-management tools.

Do not delete random PostgreSQL/vCenter files.

---

# Part 219 — Certificate Failure

Symptoms can include:

```text
login failure
host disconnect
API errors
solution integration failure
```

Check:

```text
time
expiry
trust chain
certificate identity
```

Use supported certificate workflows.

---

# Part 220 — Lifecycle Manager Failure

Check:

```text
depot/download access
desired image
cluster state
host compliance
vendor add-on compatibility
maintenance mode
space/reboot requirement
```

Do not force-remediate an unknown compliance state without diagnosis.

---

# Part 221 — Physical Hardware Alarm

vSphere can report hardware sensor issues.

Examples:

```text
fan
PSU
temperature
memory
disk/controller
```

Virtualization team must coordinate with data-center/server hardware operations.

---

# Part 222 — Capacity Dashboard

At cluster level monitor:

```text
CPU used/demand
memory consumed/active
datastore free
network
VM count
largest VMs
reservations
HA failover capacity
growth
```

Capacity planning is continuous.

---

# Part 223 — N+1 Validation

If cluster has:

```text
4 hosts
```

simulate one unavailable:

```text
Can remaining 3 hosts carry:
CPU?
RAM?
reservations?
network?
storage?
```

If not, the cluster is not operationally N+1.

---

# Part 224 — Documentation Set

A production vSphere environment should document:

```text
inventory
host hardware
IP/VLAN
vmnic mapping
vSwitch/vDS
VMkernel networks
datastores
storage paths
cluster policy
HA/DRS
roles/permissions
lifecycle image
backup
DR
runbooks
```

Documentation is part of availability.

---

# Enhanced Deep-Study Layer — VMware vSphere Administration and Engineering

This layer preserves the uploaded Course 39 and adds deeper engineering explanations, diagrams, command examples, failure reasoning, troubleshooting paths, and operational practice. The uploaded source uses **vSphere 9.1** as its reference baseline; release-specific syntax, build numbers, compatibility, licensing, and patch procedures must always be matched to the exact installed release.


## Advanced Deep Dive 1 — vCenter vs ESX Runtime Plane

### Concept

vCenter coordinates inventory, policy, cluster workflows, permissions, lifecycle and automation; ESX hosts execute VMs and keep host-local CPU, memory, network and storage runtime state.

### Architecture / Mental Model

```text
Admin/API → vCenter → desired configuration → ESX host runtime → VM
```

### Commands / Practical Example

```text
Get-VMHost; Get-VM; esxcli system version get
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vCenter vs ESX Runtime Plane**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 2 — DNS, FQDN and Certificate Identity

### Concept

Stable forward/reverse name resolution and consistent FQDNs underpin host registration, TLS trust, SSO and integrations.

### Architecture / Mental Model

```text
Client → DNS → FQDN/IP → TLS certificate SAN → vCenter/ESX
```

### Commands / Practical Example

```text
nslookup vc01.lab.example; Resolve-DnsName esx01.lab.example
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **DNS, FQDN and Certificate Identity**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 3 — NTP and Time Trust

### Concept

Time synchronization is a security and operations dependency for SSO tokens, certificates, Kerberos, logs and incident correlation.

### Architecture / Mental Model

```text
Authoritative NTP → vCenter + ESX + identity + admin systems
```

### Commands / Practical Example

```text
timedatectl; chronyc sources -v; w32tm /query /status
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **NTP and Time Trust**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 4 — Hardware Compatibility Matrix

### Concept

Production support depends on the combined ESX build, server model, CPU, NIC/HBA, driver, firmware, BIOS and storage stack—not merely on whether installation succeeds.

### Architecture / Mental Model

```text
ESX build + OEM add-on + driver + firmware + hardware → supported platform
```

### Commands / Practical Example

```text
esxcli hardware platform get; esxcli network nic list; esxcli storage core adapter list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Hardware Compatibility Matrix**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 5 — UEFI Secure Boot and TPM

### Concept

UEFI Secure Boot verifies trusted boot components while TPM-backed measurements support host trust and attestation-oriented designs.

### Architecture / Mental Model

```text
UEFI → Secure Boot → ESX boot chain → TPM measurement → trust evidence
```

### Commands / Practical Example

```text
Record firmware mode, Secure Boot state, TPM state, attestation state
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **UEFI Secure Boot and TPM**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 6 — DCUI and Out-of-Band Recovery

### Concept

DCUI is the host-local emergency recovery interface when management networking or vCenter connectivity is broken.

### Architecture / Mental Model

```text
Remote admin X → BMC/OOB → DCUI → vmk0 → management network
```

### Commands / Practical Example

```text
Prechange: test BMC/OOB, record vmk0 IP/VLAN/uplinks, write rollback
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **DCUI and Out-of-Band Recovery**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 7 — VMkernel Adapters

### Concept

VMkernel adapters are host IP interfaces for management, vMotion, NFS, iSCSI and other host services; they are not VM vNICs.

### Architecture / Mental Model

```text
Host service → vmk → vSS/vDS → vmnic → physical network
```

### Commands / Practical Example

```text
esxcli network ip interface list; esxcli network ip interface ipv4 get
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VMkernel Adapters**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 8 — VMkernel Routing and TCP/IP Stacks

### Concept

Each host-service flow follows a VMkernel routing context; success from one vmk does not prove another service path is healthy.

### Architecture / Mental Model

```text
vmk1/vMotion → route → peer; vmk2/storage → route → storage
```

### Commands / Practical Example

```text
esxcli network ip route ipv4 list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VMkernel Routing and TCP/IP Stacks**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 9 — vmkping Path Testing

### Concept

vmkping validates VMkernel-source connectivity and is more relevant than a guest ping for vMotion and storage paths.

### Architecture / Mental Model

```text
source vmk → virtual switch → uplink → network → remote vmk/storage
```

### Commands / Practical Example

```text
vmkping 10.10.20.12
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vmkping Path Testing**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 10 — vSphere Standard Switch

### Concept

vSS is host-local and therefore vulnerable to cross-host configuration drift unless automation or profiles keep port groups, VLANs and uplinks aligned.

### Architecture / Mental Model

```text
ESX01 vSS ↔ physical network ↔ ESX02 vSS
```

### Commands / Practical Example

```text
Get-VMHost | Get-VirtualSwitch; Get-VMHost | Get-VirtualPortGroup
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vSphere Standard Switch**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 11 — vSphere Distributed Switch

### Concept

vDS centralizes switch configuration in vCenter while each host retains local forwarding state through its distributed-switch proxy.

### Architecture / Mental Model

```text
vCenter vDS config → host proxy switches → VM/vmk traffic
```

### Commands / Practical Example

```text
Get-VDSwitch; Get-VDPortgroup
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vSphere Distributed Switch**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 12 — vSS to vDS Migration

### Concept

Management-network migration to vDS must be staged because one VLAN or uplink mistake can remove the path required to repair the host remotely.

### Architecture / Mental Model

```text
vSS mgmt → add vDS → migrate one uplink → migrate vmk0 → verify → migrate remainder
```

### Commands / Practical Example

```text
Get-VMHostNetworkAdapter -VMKernel; Get-VirtualSwitch; Get-VDSwitch
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vSS to vDS Migration**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 13 — VLAN End-to-End Mapping

### Concept

A port-group VLAN only works when the physical switch path carries the same tagging semantics end to end.

### Architecture / Mental Model

```text
VM/vmk → port group VLAN → vSwitch → vmnic → physical trunk → gateway
```

### Commands / Practical Example

```text
Document PortGroup,VLAN,vmnic,SwitchPort,AllowedVLANs
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VLAN End-to-End Mapping**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 14 — NIC Teaming and Failure Domains

### Concept

Redundancy depends on independent physical paths; multiple vmnics into one switch or power domain are not full resilience.

### Architecture / Mental Model

```text
vmnic0 → ToR-A; vmnic1 → ToR-B; both → vDS/vSS
```

### Commands / Practical Example

```text
esxcli network nic list; Get-VMHostNetworkAdapter -Physical
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **NIC Teaming and Failure Domains**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 15 — LACP and IP Hash

### Concept

LACP/IP-hash designs require matching aggregation state on both vSphere and the physical switch; mismatches can blackhole selected flows.

### Architecture / Mental Model

```text
ESX LAG ⇄ physical port-channel ⇄ upstream
```

### Commands / Practical Example

```text
Inventory vDS LAG, member uplinks, physical port-channel, VLANs
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **LACP and IP Hash**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 16 — NIOC

### Concept

Network I/O Control allocates shared uplink bandwidth among management, vMotion, storage, VM and backup classes during contention.

### Architecture / Mental Model

```text
Shared uplink → NIOC → traffic classes
```

### Commands / Practical Example

```text
Create table: class,normalGbps,peakGbps,failureGbps,shares,reservation,limit
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **NIOC**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 17 — End-to-End MTU

### Concept

Jumbo frames are an end-to-end contract across VMkernel, vSwitch/vDS, pNIC, physical switching/routing and the peer.

### Architecture / Mental Model

```text
vmk MTU → vDS MTU → vmnic → ToR/spine/router → peer
```

### Commands / Practical Example

```text
vmkping <peer> with release-supported DF/size testing
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **End-to-End MTU**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 18 — VMFS Shared Storage

### Concept

VMFS is a clustered filesystem allowing multiple ESX hosts to use the same block-storage datastore safely.

### Architecture / Mental Model

```text
ESX hosts → FC/iSCSI LUN → VMFS → VMDKs
```

### Commands / Practical Example

```text
esxcli storage filesystem list; esxcli storage core device list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VMFS Shared Storage**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 19 — NFS Datastore

### Concept

NFS combines VMkernel IP networking with NAS export authorization; a successful ping does not prove the export is mountable.

### Architecture / Mental Model

```text
ESX storage vmk → VLAN/route/MTU → NAS → export → datastore
```

### Commands / Practical Example

```text
vmkping <nfs-ip>; esxcli storage filesystem list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **NFS Datastore**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 20 — Fibre Channel Visibility Chain

### Concept

FC visibility traverses HBA, fabric login, zoning, array host mapping, LUN masking, rescan and VMFS mount.

### Architecture / Mental Model

```text
HBA → fabric → array port → host object → LUN mask → ESX device
```

### Commands / Practical Example

```text
esxcli storage core adapter list; esxcli storage core path list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Fibre Channel Visibility Chain**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 21 — Software iSCSI Path

### Concept

Software iSCSI transports SCSI over VMkernel TCP/IP and depends on vmk design, target discovery, IQN authorization and LUN mapping.

### Architecture / Mental Model

```text
vmk → software iSCSI adapter → IP network → target → LUN → VMFS
```

### Commands / Practical Example

```text
esxcli iscsi adapter list; esxcli storage core device list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Software iSCSI Path**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 22 — Multipathing

### Concept

Multipathing maintains alternate storage paths so a single HBA/NIC/cable/switch/array-port failure does not remove the device.

### Architecture / Mental Model

```text
Path A + Path B → same storage device
```

### Commands / Practical Example

```text
esxcli storage core path list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Multipathing**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 23 — Path Selection Policy

### Concept

Path selection decides how healthy storage paths are used and must align with the array vendor's supported design.

### Architecture / Mental Model

```text
Device → PSP → healthy paths → storage
```

### Commands / Practical Example

```text
esxcli storage nmp device list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Path Selection Policy**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 24 — APD vs PDL

### Concept

APD means all paths are unavailable with permanence unknown; PDL means the device is reported permanently unavailable.

### Architecture / Mental Model

```text
APD=temp/unknown all paths down; PDL=permanent device loss
```

### Commands / Practical Example

```text
Inspect path/device state, vSphere events and VMkernel storage logs
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **APD vs PDL**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 25 — vVols and VASA

### Concept

vVols shift storage from coarse datastore/LUN management toward VM-object policy backed by array capabilities exposed through VASA.

### Architecture / Mental Model

```text
VM storage requirement → SPBM → VASA → array capability
```

### Commands / Practical Example

```text
Get-SpbmStoragePolicy; Get-Datastore
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vVols and VASA**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 26 — SPBM Compliance

### Concept

Storage Policy Based Management expresses requirements such as replication, encryption or performance and reports whether placement is compliant.

### Architecture / Mental Model

```text
VM/VMDK → storage policy → compatible storage → compliance
```

### Commands / Practical Example

```text
Get-SpbmStoragePolicy
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **SPBM Compliance**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 27 — Thin Provisioning at Two Layers

### Concept

Thin VMDKs on thin array pools can create double overcommit, so datastore free space alone is not sufficient capacity evidence.

### Architecture / Mental Model

```text
VM logical → thin VMDK → datastore → thin array pool → physical disks
```

### Commands / Practical Example

```text
Get-Datastore | Select Name,CapacityGB,FreeSpaceGB
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Thin Provisioning at Two Layers**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 28 — VM Hardware Compatibility

### Concept

Virtual hardware version determines available devices and host compatibility; upgrades can reduce backward compatibility.

### Architecture / Mental Model

```text
ESX cluster capability → VM hardware level → virtual devices/features
```

### Commands / Practical Example

```text
Get-VM | Select Name,Version
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VM Hardware Compatibility**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 29 — VMware Tools

### Concept

VMware Tools provides optimized drivers, heartbeat, clean shutdown, quiescing and guest metadata integration.

### Architecture / Mental Model

```text
vCenter/ESX ↔ VMware Tools ↔ guest OS
```

### Commands / Practical Example

```text
Get-VM | Select Name,@{N='ToolsStatus';E={$_.ExtensionData.Guest.ToolsStatus}}
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VMware Tools**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 30 — VMXNET3

### Concept

VMXNET3 is a paravirtualized NIC that reduces legacy device-emulation overhead and supports modern network features.

### Architecture / Mental Model

```text
Guest VMXNET3 driver → virtual datapath → vSwitch/vDS
```

### Commands / Practical Example

```text
Get-VM | Get-NetworkAdapter | Select Parent,Type,NetworkName
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VMXNET3**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 31 — PVSCSI and Virtual NVMe

### Concept

PVSCSI and virtual NVMe provide optimized virtual storage interfaces; guest driver and application support must be checked before changing boot/data controllers.

### Architecture / Mental Model

```text
Guest storage stack → PVSCSI/vNVMe → ESX → datastore
```

### Commands / Practical Example

```text
Get-VM | Get-ScsiController; Get-VM | Get-HardDisk
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **PVSCSI and Virtual NVMe**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 32 — CPU Topology and vNUMA

### Concept

vCPU count, cores-per-socket and VM size relative to host NUMA nodes affect scheduler efficiency and memory locality.

### Architecture / Mental Model

```text
VM vNUMA → ESX scheduler → physical NUMA node CPU+RAM
```

### Commands / Practical Example

```text
Get-VM | Select Name,NumCpu,CoresPerSocket,MemoryGB
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **CPU Topology and vNUMA**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 33 — CPU Ready and Co-Stop

### Concept

CPU usage alone does not show scheduling pressure; ready/co-stop reveal time a VM waits for suitable pCPU scheduling.

### Architecture / Mental Model

```text
VM runnable → scheduler wait → pCPU execution
```

### Commands / Practical Example

```text
esxtop CPU view
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **CPU Ready and Co-Stop**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 34 — Reservations Limits and Shares

### Concept

Reservations guarantee minimums, limits cap maximums and shares define relative priority during contention.

### Architecture / Mental Model

```text
reservation=min guarantee; limit=max cap; shares=relative priority
```

### Commands / Practical Example

```text
Get-VMResourceConfiguration -VM (Get-VM linux01)
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Reservations Limits and Shares**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 35 — Resource Pool Semantics

### Concept

Resource pools are entitlement hierarchies, not folders; nested shares are normalized within parents and can change effective priority.

### Architecture / Mental Model

```text
Cluster → Prod/Dev resource pools → child VMs
```

### Commands / Practical Example

```text
Get-ResourcePool; Get-VMResourceConfiguration
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Resource Pool Semantics**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 36 — Snapshot Chain

### Concept

Snapshots redirect writes into delta files and form a chain whose size and depth affect capacity, I/O and consolidation.

### Architecture / Mental Model

```text
Base VMDK → Snap1 delta → Snap2 delta → current delta
```

### Commands / Practical Example

```text
Get-VM | Get-Snapshot | Select VM,Name,Created,SizeGB
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Snapshot Chain**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 37 — Snapshot Consolidation

### Concept

Snapshot deletion/consolidation merges delta data into the surviving disk chain and may require heavy I/O and free space.

### Architecture / Mental Model

```text
base + deltas → merge/commit → current disk state
```

### Commands / Practical Example

```text
Get-VM | Get-Snapshot; inspect datastore free space and active backups
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Snapshot Consolidation**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 38 — Templates and Guest Customization

### Concept

Templates standardize virtual hardware and OS baseline while customization provides unique hostname/network/domain identity.

### Architecture / Mental Model

```text
Golden VM → harden/generalize → template → clone + customization → unique VM
```

### Commands / Practical Example

```text
Get-Template; Get-OSCustomizationSpec
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Templates and Guest Customization**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 39 — Content Library

### Concept

Content Library distributes templates, OVF/OVA and ISO artifacts across sites and should be treated as a controlled software supply chain.

### Architecture / Mental Model

```text
Publisher library → subscribed library → standardized deployment
```

### Commands / Practical Example

```text
Inventory content libraries using current VCF PowerCLI modules
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Content Library**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 40 — vMotion Pre-Copy

### Concept

vMotion copies memory while the VM runs, recopies dirty pages and performs a brief final switchover.

### Architecture / Mental Model

```text
Source VM → memory copy → dirty-page recopies → brief cutover → target VM
```

### Commands / Practical Example

```text
Get-VMHostNetworkAdapter -VMKernel; Get-Cluster | Select Name,EVCMode
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vMotion Pre-Copy**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 41 — vMotion Network Capacity

### Concept

vMotion is a bulk memory-transfer workload and can compete with storage or VM traffic if bandwidth/QoS are poorly designed.

### Architecture / Mental Model

```text
Host A RAM → vMotion network → Host B RAM
```

### Commands / Practical Example

```text
Estimate memory GB / effective transfer GBps and compare to maintenance window
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vMotion Network Capacity**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 42 — EVC

### Concept

Enhanced vMotion Compatibility exposes a common CPU feature baseline across compatible host generations.

### Architecture / Mental Model

```text
HostA features ∩ HostB features ∩ HostC features → EVC baseline
```

### Commands / Practical Example

```text
Get-Cluster | Select Name,EVCMode
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **EVC**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 43 — Storage vMotion

### Concept

Storage vMotion moves VMDKs between datastores while tracking writes until final convergence.

### Architecture / Mental Model

```text
Datastore A → disk copy/changed blocks → Datastore B
```

### Commands / Practical Example

```text
Get-Datastore; Get-VM linux01 | Get-HardDisk
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Storage vMotion**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 44 — HA Network Heartbeats

### Concept

HA uses management-network heartbeats to determine host liveness; redundant management networking reduces false isolation.

### Architecture / Mental Model

```text
Host A ⇄ management heartbeat ⇄ Host B/C
```

### Commands / Practical Example

```text
Get-Cluster | Select Name,HAEnabled; Get-VMHost | Select Name,ConnectionState
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **HA Network Heartbeats**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 45 — Datastore Heartbeating

### Concept

Datastore heartbeat evidence helps HA distinguish a host failure from a management-network isolation/partition.

### Architecture / Mental Model

```text
management heartbeat uncertain + datastore heartbeat evidence → failure classification
```

### Commands / Practical Example

```text
Review HA heartbeat datastore configuration and events
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Datastore Heartbeating**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 46 — Host Isolation Response

### Concept

A host can be alive but isolated from HA peers; isolation response controls whether VMs remain or are stopped for restart elsewhere.

### Architecture / Mental Model

```text
Host alive X mgmt network → isolation detection → configured response
```

### Commands / Practical Example

```text
Document management redundancy, isolation addresses and response policy
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Host Isolation Response**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 47 — HA Restart Priority and Dependencies

### Concept

VM restart priority should reflect service dependencies such as DNS/identity → database → application → web.

### Architecture / Mental Model

```text
DNS/AD → DB → APP → WEB/LB → business health test
```

### Commands / Practical Example

```text
Create restart/dependency table with VM,priority,dependency,healthcheck
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **HA Restart Priority and Dependencies**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 48 — Admission Control

### Concept

Admission control preserves enough CPU/memory headroom to satisfy configured failover requirements.

### Architecture / Mental Model

```text
normal demand + failover reserve → one host loss → survivors fit
```

### Commands / Practical Example

```text
Create N+1 capacity table for CPU,RAM,reservations
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Admission Control**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 49 — N+1 and Maintenance State

### Concept

A planned maintenance host outage consumes the same spare capacity needed for an unexpected failure, so resilience is temporarily reduced.

### Architecture / Mental Model

```text
4 hosts → 1 maintenance → 3 active → another failure → 2 active
```

### Commands / Practical Example

```text
Model normal, maintenance and failure-state capacity
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **N+1 and Maintenance State**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 50 — Fault Tolerance

### Concept

FT maintains synchronized secondary execution for supported workloads, reducing interruption versus restart-based HA but using more resources.

### Architecture / Mental Model

```text
Primary VM ⇄ synchronized secondary → failover
```

### Commands / Practical Example

```text
Document FT candidate, resources, network, storage, compatibility
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Fault Tolerance**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 51 — DRS Placement

### Concept

DRS considers demand, entitlement, rules and migration benefit rather than simply moving VMs off the highest-utilization host.

### Architecture / Mental Model

```text
telemetry + policy + rules → DRS → initial placement/migration
```

### Commands / Practical Example

```text
Get-Cluster | Select Name,DrsEnabled,DrsAutomationLevel
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **DRS Placement**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 52 — Affinity and Anti-Affinity

### Concept

Affinity keeps selected objects together; anti-affinity spreads redundant VMs across hosts to reduce correlated failure.

### Architecture / Mental Model

```text
DC01 → HostA; DC02 → HostB
```

### Commands / Practical Example

```text
Get-DrsRule -Cluster (Get-Cluster LAB-CLUSTER) 2>$null
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Affinity and Anti-Affinity**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 53 — VM-to-Host Rules

### Concept

VM-to-host rules support licensing/hardware/locality constraints but reduce DRS/HA flexibility.

### Architecture / Mental Model

```text
VM group → placement rule → eligible host group
```

### Commands / Practical Example

```text
Document reason, owner, hard/soft nature and recovery implication
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VM-to-Host Rules**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 54 — SSO Roles Permissions and Inheritance

### Concept

Authentication establishes identity; roles define privileges; permissions apply those privileges to an inventory object with optional propagation.

### Architecture / Mental Model

```text
User/Group → SSO → Role + Object + Propagate → authorized action
```

### Commands / Practical Example

```text
Get-VIRole; Get-VIPermission
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **SSO Roles Permissions and Inheritance**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 55 — Service Accounts

### Concept

Backup, monitoring and automation should use dedicated least-privilege identities with rotation and audit.

### Architecture / Mental Model

```text
Integration → service identity → scoped role → objects
```

### Commands / Practical Example

```text
Get-VIPermission | Where-Object {$_.Principal -match 'svc|service'}
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Service Accounts**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 56 — VMCA and Certificate Lifecycle

### Concept

vSphere certificate trust affects browsers, APIs, hosts and integrations; expiry/FQDN mismatch can disrupt management.

### Architecture / Mental Model

```text
Client → TLS → vCenter/ESX cert → VMCA/trusted CA
```

### Commands / Practical Example

```text
Track subject,SAN,issuer,expiry,owner,renewal date
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VMCA and Certificate Lifecycle**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 57 — Lockdown Mode

### Concept

Lockdown mode reduces direct host-management paths and encourages administration through vCenter while preserving planned emergency access.

### Architecture / Mental Model

```text
Admin → vCenter → host; direct host access restricted
```

### Commands / Practical Example

```text
Document lockdown mode and emergency access identities
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Lockdown Mode**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 58 — ESX Shell SSH and Host Firewall

### Concept

Shell/SSH should be time-bound exceptions; the host firewall should permit only required services.

### Architecture / Mental Model

```text
Admin → approved window → SSH/Shell → collect evidence → disable
```

### Commands / Practical Example

```text
esxcli network firewall ruleset list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **ESX Shell SSH and Host Firewall**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 59 — Host Profiles

### Concept

Host Profiles capture desired host configuration and expose drift while allowing host-specific values such as IPs and hostnames.

### Architecture / Mental Model

```text
reference desired state → profile → compliance → customization/remediation
```

### Commands / Practical Example

```text
Get-VMHostProfile 2>$null
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Host Profiles**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 60 — Lifecycle Manager Desired Images

### Concept

Desired cluster images define the target ESX version plus supported OEM add-ons/components and firmware/driver integration.

### Architecture / Mental Model

```text
desired image → compliance → maintenance → remediation → validation
```

### Commands / Practical Example

```text
Record desired image, host builds, vendor add-on, compatibility and backup
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Lifecycle Manager Desired Images**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 61 — Rolling Remediation

### Concept

Remediate one host at a time so the cluster carries workload on survivors and each updated host is validated before continuing.

### Architecture / Mental Model

```text
HostA patch/validate → HostB → HostC
```

### Commands / Practical Example

```text
Precheck HA,DRS,N+1,storage paths,backup,OOB
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Rolling Remediation**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 62 — Driver Firmware Coupling

### Concept

NIC/HBA drivers, firmware, BIOS and ESX build must remain in a validated combination; newer is not automatically safer.

### Architecture / Mental Model

```text
ESX build ↔ driver ↔ firmware ↔ server BIOS ↔ storage firmware
```

### Commands / Practical Example

```text
esxcli network nic get -n vmnic0; esxcli storage core adapter list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Driver Firmware Coupling**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 63 — vCenter File-Based Backup

### Concept

vCenter needs supported independent configuration/state backup and a tested restore procedure; an ordinary VM snapshot is not equivalent.

### Architecture / Mental Model

```text
vCenter → supported backup → independent repository → restore workflow
```

### Commands / Practical Example

```text
Track last success,target,retention,credentials,restore-test date
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vCenter File-Based Backup**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 64 — Host Rebuildability

### Concept

A failed host should be reproducible from approved ESX image, lifecycle state, networking/storage documentation and profiles/automation.

### Architecture / Mental Model

```text
bare metal → ESX image → network/storage/profile → cluster
```

### Commands / Practical Example

```text
Record vmnic mapping, vmk IPs, storage paths, desired image, OOB info
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Host Rebuildability**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 65 — Tasks Events Logs

### Concept

Tasks record requested operations; events record state changes; component logs provide detailed evidence and should be collected before destructive troubleshooting.

### Architecture / Mental Model

```text
user/API action → task → event → logs/metrics → root cause
```

### Commands / Practical Example

```text
Get-VIEvent -MaxSamples 100 | Select CreatedTime,UserName,FullFormattedMessage
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Tasks Events Logs**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 66 — Alarms and Runbooks

### Concept

An alarm is useful only when it has an owner, threshold rationale and response runbook.

### Architecture / Mental Model

```text
condition → warning/critical → owner → runbook/escalation
```

### Commands / Practical Example

```text
Create alarm inventory: name,entity,trigger,owner,runbook
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Alarms and Runbooks**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 67 — esxtop CPU

### Concept

esxtop CPU helps distinguish guest utilization from scheduler contention such as ready and co-stop.

### Architecture / Mental Model

```text
guest demand → ESX scheduler → pCPU; wait shown by ready/co-stop
```

### Commands / Practical Example

```text
esxtop
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **esxtop CPU**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 68 — esxtop Memory

### Concept

esxtop memory exposes host memory pressure, ballooning and swapping that guest-only monitoring cannot see.

### Architecture / Mental Model

```text
guest working set → host RAM → reclaim → swap
```

### Commands / Practical Example

```text
esxtop; guest free -h; vmstat 1
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **esxtop Memory**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 69 — esxtop Storage

### Concept

Storage analysis traces VM I/O through ESX queues/device latency toward HBA/NIC and SAN/NAS backend.

### Architecture / Mental Model

```text
VM → VMDK/controller → ESX storage → HBA/NIC → SAN/NAS → array
```

### Commands / Practical Example

```text
esxtop; esxcli storage core path list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **esxtop Storage**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 70 — esxtop Network

### Concept

Network analysis correlates VM port traffic, pNIC throughput, drops, teaming and physical network state.

### Architecture / Mental Model

```text
VM vNIC → vSwitch/vDS → vmnic → physical switch → route/firewall
```

### Commands / Practical Example

```text
esxtop; esxcli network nic list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **esxtop Network**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 71 — VCF PowerCLI

### Concept

The source baseline uses VCF PowerCLI as the current PowerCLI package family; automation should standardize module versions and avoid conflicting legacy modules.

### Architecture / Mental Model

```text
PowerShell → VCF.PowerCLI → vSphere API → vCenter
```

### Commands / Practical Example

```text
Install-Module -Name VCF.PowerCLI; Connect-VIServer vc01.lab.example
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VCF PowerCLI**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 72 — PowerCLI Read-First Safety

### Concept

Safe automation queries and previews exact objects before mutating them because one pipeline can affect hundreds of VMs or hosts.

### Architecture / Mental Model

```text
Get-* → filter → preview/count → approval → Set/New/Remove → verify
```

### Commands / Practical Example

```text
$targets=Get-VM -Location (Get-Folder Development); $targets | Select Name; $targets.Count
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **PowerCLI Read-First Safety**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 73 — Inventory and Capacity Reporting

### Concept

Structured reports turn vSphere state into repeatable operational evidence and make drift/capacity trends visible.

### Architecture / Mental Model

```text
vCenter API → PowerCLI → CSV/JSON → trend/dashboard/action
```

### Commands / Practical Example

```text
Get-VMHost; Get-VM; Get-Datastore; Get-VM | Get-Snapshot
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Inventory and Capacity Reporting**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 74 — Host Disconnected Diagnosis

### Concept

A host can lose vCenter management communication while continuing to run VMs, so diagnosis must separate management-path failure from host/runtime failure.

### Architecture / Mental Model

```text
vCenter X host → check OOB → vmk0 → VLAN/uplink → DNS/time/cert/agents
```

### Commands / Practical Example

```text
vmkping <mgmt-peer>; esxcli network ip interface ipv4 get
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Host Disconnected Diagnosis**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 75 — vMotion Failure Decision Tree

### Concept

vMotion can fail because of VMkernel reachability/MTU, CPU/EVC, target resources, network mapping, storage access or VM device constraints.

### Architecture / Mental Model

```text
source → compatibility checks → vMotion path → target → cutover
```

### Commands / Practical Example

```text
vmkping <target-vmotion-ip>; Get-Cluster | Select Name,EVCMode
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vMotion Failure Decision Tree**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 76 — NFS Outage Diagnosis

### Concept

An NFS outage must be traced through vmk IP/route/VLAN/MTU, NAS service, export authorization and backend NAS health.

### Architecture / Mental Model

```text
storage vmk → network → NAS → export → filesystem/controller
```

### Commands / Practical Example

```text
vmkping <nfs-ip>; esxcli storage filesystem list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **NFS Outage Diagnosis**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 77 — Missing iSCSI LUN Diagnosis

### Concept

Trace from storage VMkernel connectivity through software iSCSI adapter, target portal, IQN authorization, LUN mapping and rescan.

### Architecture / Mental Model

```text
vmk → adapter → target → IQN ACL → LUN → path → VMFS
```

### Commands / Practical Example

```text
esxcli iscsi adapter list; esxcli storage core device list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Missing iSCSI LUN Diagnosis**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 78 — Missing FC LUN Diagnosis

### Concept

Trace HBA link, fabric login, zoning, array host object and LUN masking before any rescan or formatting decision.

### Architecture / Mental Model

```text
HBA → fabric → zoning → array host → LUN mask → ESX
```

### Commands / Practical Example

```text
esxcli storage core adapter list; esxcli storage core path list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Missing FC LUN Diagnosis**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 79 — Datastore Full Runbook

### Concept

Datastore exhaustion can pause or fail many VMs; identify snapshots, thin growth, swap/log files and backend free space before supported extension/migration.

### Architecture / Mental Model

```text
capacity ↓ → snapshots/thin growth → 0% free → VM write/task failures
```

### Commands / Practical Example

```text
Get-Datastore | Sort FreeSpaceGB; Get-VM | Get-Snapshot | Sort SizeGB -Descending
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Datastore Full Runbook**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 80 — Snapshot Sprawl Governance

### Concept

Snapshots should have owner, purpose, change ticket and expiry; automation should report old snapshots but not blindly delete them.

### Architecture / Mental Model

```text
change ticket → snapshot → short rollback window → remove/consolidate
```

### Commands / Practical Example

```text
Get-VM | Get-Snapshot | Where-Object {$_.Created -lt (Get-Date).AddDays(-7)}
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Snapshot Sprawl Governance**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 81 — VM CPU Troubleshooting

### Concept

CPU troubleshooting separates application thread demand, guest CPU, host saturation, ready/co-stop, limits, oversizing and NUMA.

### Architecture / Mental Model

```text
app → guest CPU → host scheduler → ready/co-stop → pCPU
```

### Commands / Practical Example

```text
Get-VM linux01 | Select NumCpu,CoresPerSocket; esxtop
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VM CPU Troubleshooting**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 82 — VM Memory Troubleshooting

### Concept

Memory troubleshooting separates guest paging from ballooning, host swap, limits, reservations and cluster capacity.

### Architecture / Mental Model

```text
guest paging → host memory manager → balloon/reclaim → swap
```

### Commands / Practical Example

```text
Get-VMResourceConfiguration -VM (Get-VM linux01); esxtop
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VM Memory Troubleshooting**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 83 — VM Disk Latency Troubleshooting

### Concept

Disk latency must be traced from guest filesystem through virtual controller/VMDK, datastore, ESX path, network/fabric and array.

### Architecture / Mental Model

```text
guest → VMDK/controller → datastore → ESX path → SAN/NAS → array
```

### Commands / Practical Example

```text
esxtop; esxcli storage core path list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VM Disk Latency Troubleshooting**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 84 — VM Network Troubleshooting

### Concept

Network diagnosis follows guest vNIC, port group, VLAN, vSwitch/vDS, vmnic, physical switch, routing and firewall.

### Architecture / Mental Model

```text
guest → vNIC → port group/VLAN → vSwitch → vmnic → physical network
```

### Commands / Practical Example

```text
Get-VM linux01 | Get-NetworkAdapter; esxcli network nic list
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **VM Network Troubleshooting**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 85 — vCenter Disk-Full Failure

### Concept

A full vCenter appliance partition can destabilize UI/API/database/services even though hosts and VMs continue running.

### Architecture / Mental Model

```text
logs/DB growth → appliance partition full → service failures
```

### Commands / Practical Example

```text
Use supported vCenter appliance management tools to inspect partition and service health
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **vCenter Disk-Full Failure**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 86 — Capacity Planning in Failure State

### Concept

Cluster capacity must be tested after removing the largest credible failure domain and should include CPU, RAM, reservations, storage, network and growth.

### Architecture / Mental Model

```text
normal capacity → remove host/link/path → survivor capacity → critical workload fit?
```

### Commands / Practical Example

```text
Build N+1 worksheet for CPU,RAM,reservations,datastore,network
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Capacity Planning in Failure State**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 87 — Boot Storm

### Concept

HA restart can create bursty storage, network, DNS/AD and application dependency load when many VMs start simultaneously.

### Architecture / Mental Model

```text
host failure → many VM boots → IOPS/auth/network spike
```

### Commands / Practical Example

```text
Create restart tiers, delays, health checks and dependency order
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Boot Storm**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 88 — Configuration Drift

### Concept

Emergency host changes accumulate unless desired-state tools and audits detect differences in networking, storage, security and services.

### Architecture / Mental Model

```text
desired state → compare hosts → compliant/drifted → remediate
```

### Commands / Practical Example

```text
Get-VMHost | Get-VMHostNetworkAdapter -VMKernel
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Configuration Drift**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


## Advanced Deep Dive 89 — Change Management

### Concept

High-risk host, vDS, storage and lifecycle changes should define prerequisites, blast radius, rollback and post-change health tests.

### Architecture / Mental Model

```text
plan → review → precheck → change → verify → monitor/rollback
```

### Commands / Practical Example

```text
Record objects,before-state,desired-state,rollback,validation,owner
```

### Expected Behavior

You should be able to identify the exact vSphere object or host layer involved, predict the healthy state, and collect evidence from the same layer that owns the function. Do not treat a green GUI icon as sufficient proof; correlate object state with network, storage, host, guest, task/event, and application evidence where relevant.

### Why It Works

vSphere separates management intent from host runtime execution. ESX schedules compute and memory, VMkernel carries host-service traffic, virtual switches forward frames, the storage stack submits I/O, and vCenter coordinates multi-host policy and workflows. Understanding which component owns each step makes troubleshooting deterministic.

### Production Example

For **Change Management**, document the object owner, dependency path, normal baseline, failure domain, security implications, capacity assumptions, monitoring signal, and rollback. Production engineering is not only configuration—it is proving that the design still works after a host, link, path, or management component fails.

### Common Failure Pattern

```text
Symptom
  ↓
identify affected VM/host/network/datastore/cluster
  ↓
read task/event and exact error
  ↓
collect evidence at owning layer
  ↓
compare with known-good host/path
  ↓
make one controlled change
  ↓
verify VM + application
```

### Best Practice

Use supported, build-matched procedures; preserve OOB recovery before networking changes; never recreate/format storage when visibility is uncertain; and automate **read/report/validate** before automating **change**.

---


# Enhanced vSphere Practical Lab Sequence


## Enhanced Lab 1 — vCenter vs ESX Runtime Plane

### Goal

Validate **vCenter vs ESX Runtime Plane** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Admin/API → vCenter → desired configuration → ESX host runtime → VM
```

### Evidence Commands

```text
Get-VMHost; Get-VM; esxcli system version get
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 2 — DNS, FQDN and Certificate Identity

### Goal

Validate **DNS, FQDN and Certificate Identity** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Client → DNS → FQDN/IP → TLS certificate SAN → vCenter/ESX
```

### Evidence Commands

```text
nslookup vc01.lab.example; Resolve-DnsName esx01.lab.example
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 3 — NTP and Time Trust

### Goal

Validate **NTP and Time Trust** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Authoritative NTP → vCenter + ESX + identity + admin systems
```

### Evidence Commands

```text
timedatectl; chronyc sources -v; w32tm /query /status
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 4 — Hardware Compatibility Matrix

### Goal

Validate **Hardware Compatibility Matrix** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX build + OEM add-on + driver + firmware + hardware → supported platform
```

### Evidence Commands

```text
esxcli hardware platform get; esxcli network nic list; esxcli storage core adapter list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 5 — UEFI Secure Boot and TPM

### Goal

Validate **UEFI Secure Boot and TPM** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
UEFI → Secure Boot → ESX boot chain → TPM measurement → trust evidence
```

### Evidence Commands

```text
Record firmware mode, Secure Boot state, TPM state, attestation state
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 6 — DCUI and Out-of-Band Recovery

### Goal

Validate **DCUI and Out-of-Band Recovery** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Remote admin X → BMC/OOB → DCUI → vmk0 → management network
```

### Evidence Commands

```text
Prechange: test BMC/OOB, record vmk0 IP/VLAN/uplinks, write rollback
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 7 — VMkernel Adapters

### Goal

Validate **VMkernel Adapters** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Host service → vmk → vSS/vDS → vmnic → physical network
```

### Evidence Commands

```text
esxcli network ip interface list; esxcli network ip interface ipv4 get
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 8 — VMkernel Routing and TCP/IP Stacks

### Goal

Validate **VMkernel Routing and TCP/IP Stacks** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vmk1/vMotion → route → peer; vmk2/storage → route → storage
```

### Evidence Commands

```text
esxcli network ip route ipv4 list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 9 — vmkping Path Testing

### Goal

Validate **vmkping Path Testing** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
source vmk → virtual switch → uplink → network → remote vmk/storage
```

### Evidence Commands

```text
vmkping 10.10.20.12
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 10 — vSphere Standard Switch

### Goal

Validate **vSphere Standard Switch** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX01 vSS ↔ physical network ↔ ESX02 vSS
```

### Evidence Commands

```text
Get-VMHost | Get-VirtualSwitch; Get-VMHost | Get-VirtualPortGroup
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 11 — vSphere Distributed Switch

### Goal

Validate **vSphere Distributed Switch** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vCenter vDS config → host proxy switches → VM/vmk traffic
```

### Evidence Commands

```text
Get-VDSwitch; Get-VDPortgroup
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 12 — vSS to vDS Migration

### Goal

Validate **vSS to vDS Migration** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vSS mgmt → add vDS → migrate one uplink → migrate vmk0 → verify → migrate remainder
```

### Evidence Commands

```text
Get-VMHostNetworkAdapter -VMKernel; Get-VirtualSwitch; Get-VDSwitch
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 13 — VLAN End-to-End Mapping

### Goal

Validate **VLAN End-to-End Mapping** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM/vmk → port group VLAN → vSwitch → vmnic → physical trunk → gateway
```

### Evidence Commands

```text
Document PortGroup,VLAN,vmnic,SwitchPort,AllowedVLANs
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 14 — NIC Teaming and Failure Domains

### Goal

Validate **NIC Teaming and Failure Domains** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vmnic0 → ToR-A; vmnic1 → ToR-B; both → vDS/vSS
```

### Evidence Commands

```text
esxcli network nic list; Get-VMHostNetworkAdapter -Physical
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 15 — LACP and IP Hash

### Goal

Validate **LACP and IP Hash** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX LAG ⇄ physical port-channel ⇄ upstream
```

### Evidence Commands

```text
Inventory vDS LAG, member uplinks, physical port-channel, VLANs
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 16 — NIOC

### Goal

Validate **NIOC** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Shared uplink → NIOC → traffic classes
```

### Evidence Commands

```text
Create table: class,normalGbps,peakGbps,failureGbps,shares,reservation,limit
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 17 — End-to-End MTU

### Goal

Validate **End-to-End MTU** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vmk MTU → vDS MTU → vmnic → ToR/spine/router → peer
```

### Evidence Commands

```text
vmkping <peer> with release-supported DF/size testing
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 18 — VMFS Shared Storage

### Goal

Validate **VMFS Shared Storage** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX hosts → FC/iSCSI LUN → VMFS → VMDKs
```

### Evidence Commands

```text
esxcli storage filesystem list; esxcli storage core device list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 19 — NFS Datastore

### Goal

Validate **NFS Datastore** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX storage vmk → VLAN/route/MTU → NAS → export → datastore
```

### Evidence Commands

```text
vmkping <nfs-ip>; esxcli storage filesystem list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 20 — Fibre Channel Visibility Chain

### Goal

Validate **Fibre Channel Visibility Chain** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
HBA → fabric → array port → host object → LUN mask → ESX device
```

### Evidence Commands

```text
esxcli storage core adapter list; esxcli storage core path list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 21 — Software iSCSI Path

### Goal

Validate **Software iSCSI Path** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vmk → software iSCSI adapter → IP network → target → LUN → VMFS
```

### Evidence Commands

```text
esxcli iscsi adapter list; esxcli storage core device list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 22 — Multipathing

### Goal

Validate **Multipathing** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Path A + Path B → same storage device
```

### Evidence Commands

```text
esxcli storage core path list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 23 — Path Selection Policy

### Goal

Validate **Path Selection Policy** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Device → PSP → healthy paths → storage
```

### Evidence Commands

```text
esxcli storage nmp device list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 24 — APD vs PDL

### Goal

Validate **APD vs PDL** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
APD=temp/unknown all paths down; PDL=permanent device loss
```

### Evidence Commands

```text
Inspect path/device state, vSphere events and VMkernel storage logs
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 25 — vVols and VASA

### Goal

Validate **vVols and VASA** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM storage requirement → SPBM → VASA → array capability
```

### Evidence Commands

```text
Get-SpbmStoragePolicy; Get-Datastore
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 26 — SPBM Compliance

### Goal

Validate **SPBM Compliance** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM/VMDK → storage policy → compatible storage → compliance
```

### Evidence Commands

```text
Get-SpbmStoragePolicy
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 27 — Thin Provisioning at Two Layers

### Goal

Validate **Thin Provisioning at Two Layers** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM logical → thin VMDK → datastore → thin array pool → physical disks
```

### Evidence Commands

```text
Get-Datastore | Select Name,CapacityGB,FreeSpaceGB
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 28 — VM Hardware Compatibility

### Goal

Validate **VM Hardware Compatibility** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX cluster capability → VM hardware level → virtual devices/features
```

### Evidence Commands

```text
Get-VM | Select Name,Version
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 29 — VMware Tools

### Goal

Validate **VMware Tools** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vCenter/ESX ↔ VMware Tools ↔ guest OS
```

### Evidence Commands

```text
Get-VM | Select Name,@{N='ToolsStatus';E={$_.ExtensionData.Guest.ToolsStatus}}
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 30 — VMXNET3

### Goal

Validate **VMXNET3** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Guest VMXNET3 driver → virtual datapath → vSwitch/vDS
```

### Evidence Commands

```text
Get-VM | Get-NetworkAdapter | Select Parent,Type,NetworkName
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 31 — PVSCSI and Virtual NVMe

### Goal

Validate **PVSCSI and Virtual NVMe** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Guest storage stack → PVSCSI/vNVMe → ESX → datastore
```

### Evidence Commands

```text
Get-VM | Get-ScsiController; Get-VM | Get-HardDisk
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 32 — CPU Topology and vNUMA

### Goal

Validate **CPU Topology and vNUMA** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM vNUMA → ESX scheduler → physical NUMA node CPU+RAM
```

### Evidence Commands

```text
Get-VM | Select Name,NumCpu,CoresPerSocket,MemoryGB
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 33 — CPU Ready and Co-Stop

### Goal

Validate **CPU Ready and Co-Stop** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM runnable → scheduler wait → pCPU execution
```

### Evidence Commands

```text
esxtop CPU view
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 34 — Reservations Limits and Shares

### Goal

Validate **Reservations Limits and Shares** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
reservation=min guarantee; limit=max cap; shares=relative priority
```

### Evidence Commands

```text
Get-VMResourceConfiguration -VM (Get-VM linux01)
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 35 — Resource Pool Semantics

### Goal

Validate **Resource Pool Semantics** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Cluster → Prod/Dev resource pools → child VMs
```

### Evidence Commands

```text
Get-ResourcePool; Get-VMResourceConfiguration
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 36 — Snapshot Chain

### Goal

Validate **Snapshot Chain** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Base VMDK → Snap1 delta → Snap2 delta → current delta
```

### Evidence Commands

```text
Get-VM | Get-Snapshot | Select VM,Name,Created,SizeGB
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 37 — Snapshot Consolidation

### Goal

Validate **Snapshot Consolidation** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
base + deltas → merge/commit → current disk state
```

### Evidence Commands

```text
Get-VM | Get-Snapshot; inspect datastore free space and active backups
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 38 — Templates and Guest Customization

### Goal

Validate **Templates and Guest Customization** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Golden VM → harden/generalize → template → clone + customization → unique VM
```

### Evidence Commands

```text
Get-Template; Get-OSCustomizationSpec
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 39 — Content Library

### Goal

Validate **Content Library** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Publisher library → subscribed library → standardized deployment
```

### Evidence Commands

```text
Inventory content libraries using current VCF PowerCLI modules
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 40 — vMotion Pre-Copy

### Goal

Validate **vMotion Pre-Copy** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Source VM → memory copy → dirty-page recopies → brief cutover → target VM
```

### Evidence Commands

```text
Get-VMHostNetworkAdapter -VMKernel; Get-Cluster | Select Name,EVCMode
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 41 — vMotion Network Capacity

### Goal

Validate **vMotion Network Capacity** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Host A RAM → vMotion network → Host B RAM
```

### Evidence Commands

```text
Estimate memory GB / effective transfer GBps and compare to maintenance window
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 42 — EVC

### Goal

Validate **EVC** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
HostA features ∩ HostB features ∩ HostC features → EVC baseline
```

### Evidence Commands

```text
Get-Cluster | Select Name,EVCMode
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 43 — Storage vMotion

### Goal

Validate **Storage vMotion** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Datastore A → disk copy/changed blocks → Datastore B
```

### Evidence Commands

```text
Get-Datastore; Get-VM linux01 | Get-HardDisk
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 44 — HA Network Heartbeats

### Goal

Validate **HA Network Heartbeats** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Host A ⇄ management heartbeat ⇄ Host B/C
```

### Evidence Commands

```text
Get-Cluster | Select Name,HAEnabled; Get-VMHost | Select Name,ConnectionState
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 45 — Datastore Heartbeating

### Goal

Validate **Datastore Heartbeating** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
management heartbeat uncertain + datastore heartbeat evidence → failure classification
```

### Evidence Commands

```text
Review HA heartbeat datastore configuration and events
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 46 — Host Isolation Response

### Goal

Validate **Host Isolation Response** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Host alive X mgmt network → isolation detection → configured response
```

### Evidence Commands

```text
Document management redundancy, isolation addresses and response policy
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 47 — HA Restart Priority and Dependencies

### Goal

Validate **HA Restart Priority and Dependencies** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
DNS/AD → DB → APP → WEB/LB → business health test
```

### Evidence Commands

```text
Create restart/dependency table with VM,priority,dependency,healthcheck
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 48 — Admission Control

### Goal

Validate **Admission Control** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
normal demand + failover reserve → one host loss → survivors fit
```

### Evidence Commands

```text
Create N+1 capacity table for CPU,RAM,reservations
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 49 — N+1 and Maintenance State

### Goal

Validate **N+1 and Maintenance State** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
4 hosts → 1 maintenance → 3 active → another failure → 2 active
```

### Evidence Commands

```text
Model normal, maintenance and failure-state capacity
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 50 — Fault Tolerance

### Goal

Validate **Fault Tolerance** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Primary VM ⇄ synchronized secondary → failover
```

### Evidence Commands

```text
Document FT candidate, resources, network, storage, compatibility
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 51 — DRS Placement

### Goal

Validate **DRS Placement** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
telemetry + policy + rules → DRS → initial placement/migration
```

### Evidence Commands

```text
Get-Cluster | Select Name,DrsEnabled,DrsAutomationLevel
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 52 — Affinity and Anti-Affinity

### Goal

Validate **Affinity and Anti-Affinity** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
DC01 → HostA; DC02 → HostB
```

### Evidence Commands

```text
Get-DrsRule -Cluster (Get-Cluster LAB-CLUSTER) 2>$null
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 53 — VM-to-Host Rules

### Goal

Validate **VM-to-Host Rules** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM group → placement rule → eligible host group
```

### Evidence Commands

```text
Document reason, owner, hard/soft nature and recovery implication
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 54 — SSO Roles Permissions and Inheritance

### Goal

Validate **SSO Roles Permissions and Inheritance** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
User/Group → SSO → Role + Object + Propagate → authorized action
```

### Evidence Commands

```text
Get-VIRole; Get-VIPermission
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 55 — Service Accounts

### Goal

Validate **Service Accounts** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Integration → service identity → scoped role → objects
```

### Evidence Commands

```text
Get-VIPermission | Where-Object {$_.Principal -match 'svc|service'}
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 56 — VMCA and Certificate Lifecycle

### Goal

Validate **VMCA and Certificate Lifecycle** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Client → TLS → vCenter/ESX cert → VMCA/trusted CA
```

### Evidence Commands

```text
Track subject,SAN,issuer,expiry,owner,renewal date
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 57 — Lockdown Mode

### Goal

Validate **Lockdown Mode** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Admin → vCenter → host; direct host access restricted
```

### Evidence Commands

```text
Document lockdown mode and emergency access identities
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 58 — ESX Shell SSH and Host Firewall

### Goal

Validate **ESX Shell SSH and Host Firewall** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
Admin → approved window → SSH/Shell → collect evidence → disable
```

### Evidence Commands

```text
esxcli network firewall ruleset list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 59 — Host Profiles

### Goal

Validate **Host Profiles** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
reference desired state → profile → compliance → customization/remediation
```

### Evidence Commands

```text
Get-VMHostProfile 2>$null
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 60 — Lifecycle Manager Desired Images

### Goal

Validate **Lifecycle Manager Desired Images** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
desired image → compliance → maintenance → remediation → validation
```

### Evidence Commands

```text
Record desired image, host builds, vendor add-on, compatibility and backup
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 61 — Rolling Remediation

### Goal

Validate **Rolling Remediation** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
HostA patch/validate → HostB → HostC
```

### Evidence Commands

```text
Precheck HA,DRS,N+1,storage paths,backup,OOB
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 62 — Driver Firmware Coupling

### Goal

Validate **Driver Firmware Coupling** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
ESX build ↔ driver ↔ firmware ↔ server BIOS ↔ storage firmware
```

### Evidence Commands

```text
esxcli network nic get -n vmnic0; esxcli storage core adapter list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 63 — vCenter File-Based Backup

### Goal

Validate **vCenter File-Based Backup** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
vCenter → supported backup → independent repository → restore workflow
```

### Evidence Commands

```text
Track last success,target,retention,credentials,restore-test date
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 64 — Host Rebuildability

### Goal

Validate **Host Rebuildability** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
bare metal → ESX image → network/storage/profile → cluster
```

### Evidence Commands

```text
Record vmnic mapping, vmk IPs, storage paths, desired image, OOB info
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 65 — Tasks Events Logs

### Goal

Validate **Tasks Events Logs** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
user/API action → task → event → logs/metrics → root cause
```

### Evidence Commands

```text
Get-VIEvent -MaxSamples 100 | Select CreatedTime,UserName,FullFormattedMessage
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 66 — Alarms and Runbooks

### Goal

Validate **Alarms and Runbooks** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
condition → warning/critical → owner → runbook/escalation
```

### Evidence Commands

```text
Create alarm inventory: name,entity,trigger,owner,runbook
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 67 — esxtop CPU

### Goal

Validate **esxtop CPU** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
guest demand → ESX scheduler → pCPU; wait shown by ready/co-stop
```

### Evidence Commands

```text
esxtop
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 68 — esxtop Memory

### Goal

Validate **esxtop Memory** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
guest working set → host RAM → reclaim → swap
```

### Evidence Commands

```text
esxtop; guest free -h; vmstat 1
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 69 — esxtop Storage

### Goal

Validate **esxtop Storage** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM → VMDK/controller → ESX storage → HBA/NIC → SAN/NAS → array
```

### Evidence Commands

```text
esxtop; esxcli storage core path list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## Enhanced Lab 70 — esxtop Network

### Goal

Validate **esxtop Network** in a nested/disposable vSphere lab or complete a full architecture tabletop if the feature requires hardware/licensing you do not have.

### Procedure

1. Record vCenter/ESX build and the exact objects involved.
2. Draw the path before changing anything.
3. Capture a **before** state in vSphere Client and with CLI/PowerCLI.
4. Run the evidence commands below.
5. Trigger one controlled condition or failure if safe.
6. Collect tasks, events, logs, counters, and application symptoms.
7. Explain which vSphere layer owned the behavior.
8. Roll back the lab change.
9. Verify VM and application health.
10. Save a short incident report.

### Architecture

```text
VM vNIC → vSwitch/vDS → vmnic → physical switch → route/firewall
```

### Evidence Commands

```text
esxtop; esxcli network nic list
```

### Lab Report

```text
Build:
Object:
Before state:
Change/failure:
Expected:
Actual:
Task/Event:
Relevant log/metric:
Root cause:
Correction:
Rollback:
Application verification:
Prevention:
```

### Safety

Do not perform destructive datastore, host-network, snapshot, certificate, lifecycle, or bulk automation actions on systems containing needed data. Maintain console/OOB access before any management-network migration.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Plan the vSphere Lab

Create:

```text
LAB_IP_PLAN.md
LAB_DNS.md
LAB_NETWORKS.md
LAB_STORAGE.md
```

Use at least:

```text
Management
vMotion
Storage
VM Network
```

### Lab 2 — Install ESX/ESXi

1. boot approved ISO.
2. select lab installation disk.
3. configure password.
4. reboot.
5. record build/version.
6. photograph/document DCUI values.

### Lab 3 — Configure Management Network

From DCUI:

1. choose management NIC.
2. set VLAN if required.
3. assign static IP.
4. configure DNS.
5. configure hostname.
6. test gateway/DNS.
7. verify Host Client access.

### Lab 4 — ESXCLI Baseline

Run:

```bash
esxcli system version get
esxcli network nic list
esxcli network ip interface list
esxcli network ip interface ipv4 get
esxcli network ip route ipv4 list
esxcli storage filesystem list
esxcli storage core device list
```

Save output in:

```text
ESX_BASELINE.txt
```

### Lab 5 — Deploy vCenter

Complete:

```text
Stage 1
OVA appliance deployment

Stage 2
SSO/configuration
```

Verify:

```text
FQDN
DNS
NTP
vSphere Client
```

### Lab 6 — Build Inventory

Create:

```text
Data Center: LAB-DC
Cluster: LAB-CLUSTER
Folder: Infrastructure
Folder: Production
Folder: Development
```

Add ESX hosts.

### Lab 7 — Standard Switch

Create/inspect:

```text
vSwitch0
Management
VM Network
```

Add a second vSS in lab if NICs allow.

Document:

```text
port group
VLAN
uplinks
```

### Lab 8 — VMkernel Networking

Create:

```text
vmk0 Management
vmk1 vMotion
vmk2 Storage
```

Use different test subnets.

Verify:

```bash
vmkping
```

between hosts.

### Lab 9 — NIC Teaming

Configure:

```text
2 uplinks
active/standby
```

Disconnect one lab uplink if safe.

Observe:

```text
management continuity
VM traffic continuity
```

### Lab 10 — Distributed Switch Design

Create a vDS if licensing/lab supports it.

Create:

```text
DVPG-MGMT
DVPG-VM
DVPG-VMOTION
```

Migrate one noncritical network first.

Document rollback.

### Lab 11 — NFS Datastore

On a lab NAS/Linux NFS server:

1. create export.
2. permit ESX storage VMkernel IPs.
3. add NFS datastore.
4. create small VM disk.
5. test storage path.
6. stop NFS service and observe behavior only in disposable lab.

### Lab 12 — iSCSI Datastore

Authorized lab:

1. build iSCSI target.
2. configure storage VMkernel.
3. enable software iSCSI adapter.
4. discover target.
5. present LUN.
6. rescan.
7. create VMFS datastore.
8. document paths.

### Lab 13 — Multipathing

If two paths are available:

1. inspect device paths.
2. record active paths.
3. fail one path in a controlled lab.
4. observe continued datastore access.
5. restore path.
6. verify all paths.

### Lab 14 — Create VM

Create:

```text
VM name: linux01
2 vCPU
4 GB RAM
40 GB disk
VMXNET3
supported virtual storage controller
```

Install Linux and VMware Tools/open-vm-tools as appropriate.

### Lab 15 — VM Template

1. patch Linux VM.
2. install guest tools.
3. remove secrets.
4. generalize.
5. convert/clone to template.
6. deploy `linux02`.
7. customize hostname/IP.

### Lab 16 — Content Library

If available:

1. create local Content Library.
2. add ISO/template.
3. deploy from library.
4. document use case for multi-site distribution.

### Lab 17 — Snapshot

1. create file in VM.
2. snapshot `before-change`.
3. modify file.
4. inspect snapshot.
5. revert in lab.
6. delete/consolidate snapshot.
7. explain why this was not backup.

### Lab 18 — CPU / Memory Resource Settings

On test VM:

1. inspect shares.
2. create a small CPU limit temporarily.
3. generate CPU workload.
4. observe effect.
5. remove limit.
6. compare.

Repeat conceptually with memory limit only if lab capacity makes it safe.

### Lab 19 — vMotion

Requirements:

```text
two hosts
vMotion VMkernel
compatible networking
shared/compatible storage
```

1. start test VM.
2. continuously ping it.
3. migrate ESX01 → ESX02.
4. record packet interruption if any.
5. verify target host.

### Lab 20 — Storage vMotion

1. create Datastore A and B.
2. run test VM.
3. migrate VMDK A → B.
4. monitor storage activity.
5. verify VM remains operational.

### Lab 21 — EVC

If hosts support:

1. inspect CPU generations.
2. create cluster EVC baseline.
3. explain exposed CPU feature set.
4. test migration compatibility.

### Lab 22 — vSphere HA

In disposable lab:

1. enable HA.
2. verify cluster health.
3. run test VM.
4. simulate/perform safe host power failure if lab supports.
5. measure detection time.
6. measure VM restart time.
7. calculate observed RTO.

### Lab 23 — HA Admission Control

Create capacity table:

```text
Host CPU
Host RAM
VM demand
Reservations
```

Determine whether one-host failure can be tolerated.

### Lab 24 — DRS

If licensing supports:

1. enable DRS.
2. inspect automation level.
3. create a resource imbalance.
4. observe recommendation/migration.
5. create anti-affinity for two test VMs.

If not available, complete as architecture exercise.

### Lab 25 — Permissions

Create:

```text
Role: Lab-VM-Operator
Group/User: lab-operator
Scope: Development folder
```

Test:

```text
can power VM
cannot change host networking
```

### Lab 26 — Lifecycle Manager

1. inspect cluster desired image.
2. run compliance check.
3. document ESX version/vendor add-on.
4. simulate planned remediation workflow.
5. verify maintenance/HA capacity before actual remediation.

Do not patch production from a learning lab instruction.

### Lab 27 — Install VCF PowerCLI

PowerShell:

```powershell
Install-Module -Name VCF.PowerCLI
```

Connect:

```powershell
Connect-VIServer vc01.lab.example
```

Run:

```powershell
Get-VMHost
Get-Cluster
Get-VM
Get-Datastore
```

### Lab 28 — Build Health Report

Create PowerShell report containing:

```text
host connection state
VM power state
cluster
datastore free %
snapshots older than 7 days
```

Export:

```powershell
Export-Csv
```

### Lab 29 — `esxtop`

On one host:

```bash
esxtop
```

Observe:

```text
CPU
memory
network
disk
```

Generate controlled VM CPU/disk activity and correlate.

### Lab 30 — Troubleshooting Challenge

Simulate/analyze these incidents:

1. host not responding in vCenter.
2. management VLAN wrong.
3. vMotion VMkernel unreachable.
4. wrong VLAN on VM port group.
5. NFS datastore unavailable.
6. iSCSI LUN missing.
7. one SAN path down.
8. datastore 95% full.
9. old snapshot.
10. VM will not power on.
11. HA does not restart VM.
12. Lifecycle Manager noncompliance.
13. vCenter unavailable.
14. certificate/time failure scenario.

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

# Mini Project — Production-Style vSphere Cluster

Design and build a small enterprise vSphere environment for:

```text
40 VMs
2 domain controllers
2 database servers
6 application servers
8 web servers
monitoring
backup
file services
development workloads
```

## Target Architecture

```text
                         Admin / API
                             |
                        vCenter
                             |
                 +-----------+-----------+
                 |           |           |
               ESX01       ESX02       ESX03
                 |           |           |
                 +----- vDS / Networks --+
                 |           |           |
                 +------ Shared Storage -+
                             |
                         SAN / NAS
```

Physical/logical networks:

```text
Management
vMotion
Storage
Production VM
DMZ
Backup
```

Storage:

```text
DS-PROD
DS-INFRA
DS-DEV
```

## Deliverable 1 — Planning

Create:

```text
01_REQUIREMENTS.md
02_IP_PLAN.md
03_DNS_NTP.md
04_HOST_HARDWARE.md
```

## Deliverable 2 — Host Build

Document:

```text
installation
boot mode
management NIC
firmware/driver baseline
ESX build
DCUI settings
```

## Deliverable 3 — vCenter

Document:

```text
FQDN
SSO domain
deployment size
datastore
backup
roles
```

## Deliverable 4 — Network

Create:

```text
NETWORK_ARCHITECTURE.md
```

Include:

```text
vmnic mapping
vDS/vSS
VLAN IDs
VMkernel interfaces
MTU
active/standby
physical-switch dependencies
```

Example:

```text
vmnic0 -> Fabric A
vmnic1 -> Fabric B

Management:
Uplink1 active
Uplink2 standby

vMotion:
Uplink2 active
Uplink1 standby
```

## Deliverable 5 — Storage

Create:

```text
STORAGE_ARCHITECTURE.md
```

Include:

```text
NFS/iSCSI/FC
datastores
LUNs
multipathing
path policy
capacity
SPBM
```

## Deliverable 6 — VM Standard

Define:

```text
Small:
2 vCPU
4 GB

Medium:
4 vCPU
8 GB

Large:
8 vCPU
32 GB
```

These are starting profiles only.

Also define:

```text
VMXNET3
PVSCSI/virtual NVMe where justified
UEFI
VMware Tools
template policy
snapshot policy
```

## Deliverable 7 — HA / DRS

Create:

```text
HA_DRS.md
```

Include:

```text
N+1
admission control
restart priority
host isolation
anti-affinity
EVC
DRS automation
maintenance capacity
```

## Deliverable 8 — Security

Create:

```text
SECURITY.md
```

Include:

```text
SSO
RBAC
MFA
management isolation
ESX Shell/SSH policy
lockdown mode
certificate lifecycle
Secure Boot/TPM
logging
service accounts
```

## Deliverable 9 — Lifecycle

Create:

```text
LIFECYCLE.md
```

Include:

```text
desired cluster image
vendor add-on
firmware
driver
compliance
rolling remediation
VMware Tools
VM hardware upgrade policy
```

## Deliverable 10 — Monitoring

Create:

```text
DAILY_HEALTH.md
```

Check:

```text
hosts
HA
DRS
datastore
snapshots
storage paths
alarms
VMs
capacity
backup
certificate status
```

## Deliverable 11 — Automation

Create PowerCLI:

```text
inventory.ps1
datastore-capacity.ps1
snapshot-report.ps1
host-health.ps1
```

## Deliverable 12 — Runbooks

Create:

```text
RUNBOOK_HOST_FAILURE.md
RUNBOOK_VCENTER_FAILURE.md
RUNBOOK_VMOTION_FAILURE.md
RUNBOOK_DATASTORE_FULL.md
RUNBOOK_STORAGE_PATH.md
RUNBOOK_VM_NETWORK.md
RUNBOOK_SNAPSHOT.md
RUNBOOK_PATCHING.md
```

## Failure Tests

Analyze:

```text
one host failure
one vmnic failure
one physical switch failure
one storage path failure
NFS/iSCSI outage
vCenter outage
datastore capacity exhaustion
snapshot sprawl
CPU contention
memory contention
```

For every failure:

```text
automatic behavior
service impact
monitoring evidence
operator action
remaining risk
```

---


# Expanded Capstone — Production-Style vSphere Platform

Design or build a three-host-or-larger environment for 40–60 VMs.

```text
                    Privileged Admin / API
                              |
                           vCenter
                              |
                 +------------+------------+
                 |            |            |
               ESX01        ESX02        ESX03
                 |            |            |
                 +--------- vDS -----------+
                 | Mgmt | vMotion | VM | Storage
                 |
            Shared Storage
        FC / iSCSI / NFS / vVol
                 |
          Backup / Immutable Copy
                 |
                 DR
```

Create:

```text
README.md
HOST_BUILD_STANDARD.md
DNS_NTP.md
NETWORK_ARCHITECTURE.md
VDS_PORTGROUPS.md
STORAGE_ARCHITECTURE.md
VM_STANDARD.md
HA_DRS.md
RBAC.md
SECURITY.md
CERTIFICATES.md
LIFECYCLE.md
BACKUP_RECOVERY.md
MONITORING.md
CAPACITY.md
automation/
runbooks/
failure_tests/
```

Your design must include Management, vMotion, Storage-A, Storage-B, VM-Production, DMZ, Backup, and Out-of-Band networks. For each, document subnet, VLAN, MTU, VMkernel/VM traffic role, vDS/vSS, uplinks, physical switch ports, failure-state bandwidth, firewall policy, and owner.

Storage documentation must trace:

```text
Guest
 ↓
Virtual Controller
 ↓
VMDK
 ↓
Datastore
 ↓
ESX Storage Stack
 ↓
HBA/NIC
 ↓
SAN/NAS
 ↓
Array
```

HA/DRS documentation must include N+1/N+2, admission control, management and datastore heartbeats, isolation response, restart tiers, application dependency order, EVC, DRS automation, anti-affinity, VM-to-host constraints, maintenance capacity, and boot-storm handling.

Security must include MFA/identity, least-privilege RBAC, service accounts, PAW/jump host, management segmentation, lockdown decision, SSH/Shell policy, host firewall, Secure Boot/TPM, vTPM/key-provider recovery, certificate lifecycle, and central logging.

Create VCF PowerCLI scripts for inventory, host health, datastore capacity, snapshot age, network audit, permissions audit, and capacity reporting. Every script must query before changing, print the target vCenter, validate target count, avoid hard-coded credentials, and produce structured output.

Failure-test at least:

```text
one vmnic failure
one physical-switch failure
one FC/iSCSI path failure
NFS outage
host failure
management-network isolation
vCenter outage
DNS failure
time skew
datastore 95% full
snapshot growth
vMotion failure
HA restart failure
DRS blocked by rule
lifecycle noncompliance
vCenter disk-full
certificate failure
```


## 7. Recommended Resources

This Markdown file is designed to contain the complete conceptual and lab foundation for the course.

For production changes, exact compatibility, and release-specific syntax, use the documentation for the exact installed vSphere release.

The primary official documentation families relevant to this course are:

```text
VMware vSphere 9.1 Documentation
ESX Installation and Setup
vCenter Deployment and Setup
vCenter and Host Management
vSphere Networking
vSphere Storage
vSphere Virtual Machine Administration
vSphere Resource Management
vSphere Availability
vSphere Security
vSphere Monitoring and Performance
vSphere Lifecycle Manager / Host Lifecycle
Host Profiles
VCF PowerCLI
```

Current-version notes used in this course:

- vSphere 9.1 is the current documentation baseline used here.
- Current vCenter deployment remains a two-stage appliance deployment: Stage 1 deploys the OVA, Stage 2 configures the appliance.
- Current Broadcom automation tooling is **VCF PowerCLI**, installed with `Install-Module -Name VCF.PowerCLI`.
- Current vSphere Lifecycle Manager supports desired-image-based host/cluster lifecycle.
- Release-specific build numbers and security patches change frequently; verify current Broadcom advisories before production patching.

---

## 8. Certification Relevance

This course develops skills directly relevant to:

```text
VMware / vSphere Administrator
Virtualization Engineer
Infrastructure Engineer
Private Cloud Engineer
Systems Administrator
Data Center Engineer
Cloud Engineer
SRE / Platform Engineer
Backup Engineer
```

It provides the direct VMware foundation needed before:

```text
40. VMware NSX
```

It also makes the later courses easier:

```text
OpenStack
Nutanix
Cloud platforms
Kubernetes infrastructure
Infrastructure as Code
DevOps
Cloud Security
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Install ESX first and plan networking later.  
  **Best practice:** pre-plan FQDN, DNS, IPs, VLANs, vmnic mappings, NTP, storage, and rollback.

- **Mistake:** Assume vCenter outage powers off VMs.  
  **Best practice:** separate management-plane availability from VM runtime.

- **Mistake:** Put management, storage, vMotion, and VM traffic on one unplanned network.  
  **Best practice:** separate logically/physically according to performance and security requirements.

- **Mistake:** Change all management uplinks simultaneously.  
  **Best practice:** maintain console access and a staged rollback path.

- **Mistake:** Configure VLAN only in vSphere.  
  **Best practice:** virtual and physical switches must agree.

- **Mistake:** Enable jumbo frames only on ESX.  
  **Best practice:** MTU must match end-to-end.

- **Mistake:** Dual vmnics into one physical switch equals complete redundancy.  
  **Best practice:** map independent failure domains.

- **Mistake:** Recreate datastore when LUN disappears.  
  **Best practice:** troubleshoot HBA/zoning/masking/path visibility first.

- **Mistake:** Use snapshots as backups.  
  **Best practice:** use short-lived snapshots and independent backup.

- **Mistake:** Keep snapshots for weeks/months.  
  **Best practice:** monitor age, capacity, and consolidation.

- **Mistake:** Increase vCPU whenever VM is slow.  
  **Best practice:** inspect guest demand, host contention, ready time, limits, and NUMA.

- **Mistake:** Resource pool used only as a folder.  
  **Best practice:** use folders for organization; resource pools for resource policy.

- **Mistake:** Enable HA with no spare capacity.  
  **Best practice:** validate admission control/N+1.

- **Mistake:** Put redundant VMs on the same host.  
  **Best practice:** use anti-affinity.

- **Mistake:** Hard VM-to-host pinning everywhere.  
  **Best practice:** preserve DRS/HA flexibility unless hardware/licensing requires pinning.

- **Mistake:** Expose vCenter/ESX management publicly.  
  **Best practice:** private management network, MFA, RBAC, admin workstations.

- **Mistake:** Leave SSH enabled permanently.  
  **Best practice:** enable only for approved troubleshooting windows.

- **Mistake:** Apply newest driver without checking firmware compatibility.  
  **Best practice:** maintain validated ESX/driver/firmware combinations.

- **Mistake:** Upgrade VM hardware immediately after ESX patching.  
  **Best practice:** test compatibility and rollback implications first.

- **Mistake:** Use old `VMware.PowerCLI` installation instructions for a new current environment.  
  **Best practice:** current tooling is VCF PowerCLI.

- **Mistake:** Run bulk PowerCLI changes without scoping targets.  
  **Best practice:** query/report first, confirm object scope, log actions, then change.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is VMware vSphere?

**Short answer:** VMware's virtualization platform combining ESX/ESXi hosts with centralized vCenter-based management and cluster/network/storage services.

### Q2. What does ESX/ESXi do?

**Short answer:** Runs virtual machines directly on physical server hardware and manages their compute, memory, networking, and storage access.

### Q3. What does vCenter do?

**Short answer:** Centrally manages hosts, clusters, VMs, storage, networking, permissions, HA/DRS, lifecycle, and automation.

### Q4. If vCenter fails, do running VMs normally stop?

**Short answer:** No; hosts normally continue running their existing VMs, but centralized management/functions are impaired.

### Q5. What is DCUI?

**Short answer:** Direct Console User Interface used for local ESX host configuration and recovery.

### Q6. What is a VMkernel adapter?

**Short answer:** Host-side virtual network interface used for services such as management, vMotion, and storage traffic.

### Q7. What is `vmk0` commonly used for?

**Short answer:** Initial host management networking.

### Q8. Why is DNS important to vSphere?

**Short answer:** vCenter/hosts/certificates/services and administrative workflows depend on consistent hostname resolution.

### Q9. How is current vCenter deployed?

**Short answer:** Appliance deployment in Stage 1 followed by appliance/SSO setup in Stage 2.

### Q10. What is a vCenter SSO domain?

**Short answer:** vSphere authentication domain such as `vsphere.local`, separate from an enterprise AD DNS domain.

### Q11. What is a vSphere Data Center object?

**Short answer:** Logical inventory container for clusters, hosts, networks, datastores, and VMs.

### Q12. What is maintenance mode?

**Short answer:** Host state used to evacuate/shut down workloads before planned maintenance.

### Q13. vSS vs vDS?

**Short answer:** vSS is configured per host; vDS is centrally managed across hosts through vCenter.

### Q14. VM port group vs VMkernel network?

**Short answer:** VM port group carries VM traffic; VMkernel networking carries host service traffic.

### Q15. What is NIC teaming?

**Short answer:** Using multiple physical uplinks for redundancy and/or traffic distribution.

### Q16. Why must VLAN configuration match the physical switch?

**Short answer:** vSphere tagging and the physical trunk/access topology must agree for frames to reach the intended Layer-2 network.

### Q17. What is NIOC?

**Short answer:** Network I/O Control, used on supported distributed-switch designs to manage bandwidth allocation during contention.

### Q18. What is VMFS?

**Short answer:** VMware clustered filesystem used for vSphere datastores on block storage.

### Q19. What is an NFS datastore?

**Short answer:** NAS-exported filesystem mounted by ESX hosts as VM datastore storage.

### Q20. What is multipathing?

**Short answer:** Multiple storage paths between ESX and a device so I/O can survive/use alternate paths.

### Q21. APD vs PDL?

**Short answer:** APD means all paths are unavailable without permanent-loss declaration; PDL means storage reports the device permanently lost.

### Q22. What are vVols?

**Short answer:** VM/object-oriented storage model exposing array capabilities through policy rather than managing many VMs only as files within traditional LUN datastores.

### Q23. What is SPBM?

**Short answer:** Storage Policy Based Management, mapping VM storage requirements to compatible storage capabilities.

### Q24. What is VMware Tools?

**Short answer:** Guest integration/driver package improving VM performance and manageability.

### Q25. What is VMXNET3?

**Short answer:** VMware paravirtualized high-performance virtual network adapter.

### Q26. What is PVSCSI?

**Short answer:** VMware paravirtualized SCSI controller suited for high-I/O virtual workloads.

### Q27. Why are VM snapshots not backups?

**Short answer:** They remain dependent on the primary VM/datastore and are intended mainly for short-term state management.

### Q28. What does deleting a snapshot usually require?

**Short answer:** Consolidating/merging delta data into the remaining virtual disk chain.

### Q29. What is vMotion?

**Short answer:** Migration of a running VM's compute execution between ESX hosts with minimal interruption.

### Q30. What is EVC?

**Short answer:** Enhanced vMotion Compatibility, providing a common CPU feature baseline across compatible hosts.

### Q31. What is Storage vMotion?

**Short answer:** Online movement of VM virtual disks between datastores.

### Q32. What does vSphere HA do?

**Short answer:** Detects host failure and restarts protected VMs on surviving hosts.

### Q33. HA vs FT?

**Short answer:** HA restarts after failure; Fault Tolerance maintains synchronized secondary execution for much lower interruption.

### Q34. What is HA admission control?

**Short answer:** Capacity policy that protects enough cluster resources to satisfy configured failover requirements.

### Q35. What does DRS do?

**Short answer:** Places and balances VMs across cluster hosts based on resource state and policies.

### Q36. What is anti-affinity?

**Short answer:** Placement rule designed to keep selected VMs on different hosts.

### Q37. Role vs permission?

**Short answer:** Role is a privilege set; permission assigns a user/group that role on an inventory object with scope/propagation.

### Q38. What is VMCA?

**Short answer:** VMware Certificate Authority used to manage vSphere certificate trust in standard architectures.

### Q39. What is Host Profile?

**Short answer:** Desired host-configuration profile used to check and enforce host consistency.

### Q40. What is vSphere Lifecycle Manager?

**Short answer:** vSphere service for managing ESX/cluster software lifecycle and desired-image compliance.

### Q41. What is a desired cluster image?

**Short answer:** Defined target combination of ESX version, vendor add-on, components, and supported firmware/driver integration.

### Q42. What is `esxtop`?

**Short answer:** ESX host performance diagnostic tool for CPU, memory, storage, and networking.

### Q43. What is the current PowerCLI package name?

**Short answer:** VCF PowerCLI.

### Q44. How do you install current PowerCLI?

**Short answer:** `Install-Module -Name VCF.PowerCLI`.

### Q45. What does `Connect-VIServer` do?

**Short answer:** Establishes PowerCLI connection to vCenter/compatible VMware management endpoint.

### Q46. What is the first step when vMotion fails?

**Short answer:** Read the exact task/event error, then validate vMotion network, compatibility, resources, network mapping, storage, and VM devices.

### Q47. What should you do if a SAN LUN disappears?

**Short answer:** Investigate HBA/fabric/zoning/masking/path visibility before recreating or formatting anything.

### Q48. What should you do when datastore reaches critical capacity?

**Short answer:** Identify consumption, snapshots/thin growth, extend/migrate safely, and avoid manually deleting unknown VM files.

### Q49. Why is vCenter management-network security critical?

**Short answer:** Management-plane compromise gives broad control over hosts, VMs, networks, storage, and credentials/integrations.

### Q50. What is the core vSphere troubleshooting principle?

**Short answer:** Identify the failed layer, collect tasks/events/logs/metrics, trace network/storage/compute dependencies, then change the smallest justified component.

---

# Expanded Self-Assessment Bank

### Q1. Why do VMs normally continue when vCenter is down?
**Answer:** Because ESX hosts own VM runtime CPU, memory, network and storage state.

### Q2. What is DCUI?
**Answer:** Host-local ESX configuration/recovery interface.

### Q3. What is a VMkernel adapter?
**Answer:** Host-side IP interface for management, vMotion, NFS, iSCSI and other host services.

### Q4. Why use vmkping?
**Answer:** It tests the actual VMkernel path used by host services.

### Q5. vSS vs vDS?
**Answer:** vSS is host-local; vDS is centrally configured through vCenter with host-local forwarding.

### Q6. Why is vSS-to-vDS management migration risky?
**Answer:** One bad VLAN/uplink mapping can disconnect the host.

### Q7. Why are two vmnics not automatically redundant?
**Answer:** They can share the same switch, cable path or power domain.

### Q8. What does NIOC do?
**Answer:** Arbitrates uplink bandwidth among traffic classes during contention.

### Q9. Why must MTU be consistent?
**Answer:** One smaller hop can drop oversized frames.

### Q10. What is VMFS?
**Answer:** A VMware clustered filesystem for shared block-storage datastores.

### Q11. Why doesn't ping prove NFS is usable?
**Answer:** Ping proves IP reachability, not export authorization or NFS service health.

### Q12. What should be checked for a missing FC LUN?
**Answer:** HBA, fabric login, zoning, array host mapping, LUN masking and rescan.

### Q13. APD vs PDL?
**Answer:** APD is all paths unavailable with permanence unknown; PDL is permanent device loss.

### Q14. What is SPBM?
**Answer:** Storage Policy Based Management maps VM requirements to storage capabilities.

### Q15. Why is double thin provisioning risky?
**Answer:** Both vSphere and array layers may overcommit the same physical storage.

### Q16. What is VMXNET3?
**Answer:** A VMware paravirtualized virtual NIC.

### Q17. What is PVSCSI?
**Answer:** A VMware paravirtualized SCSI controller.

### Q18. Why can too many vCPUs hurt?
**Answer:** They increase scheduling and NUMA overhead without helping a nonparallel workload.

### Q19. Reservation vs limit vs shares?
**Answer:** Reservation guarantees minimum, limit caps maximum, shares define relative priority.

### Q20. Why is a resource pool not a folder?
**Answer:** It changes resource-entitlement semantics.

### Q21. Why is a snapshot not a backup?
**Answer:** It remains dependent on the primary VM/datastore and is short-term state.

### Q22. What is snapshot consolidation?
**Answer:** Merging snapshot delta data into the surviving disk chain.

### Q23. What is vMotion?
**Answer:** Live migration of VM execution between hosts.

### Q24. Why do dirty pages matter to vMotion?
**Answer:** They must be recopied, extending migration.

### Q25. What is EVC?
**Answer:** A common CPU feature baseline for compatible live migration.

### Q26. What is Storage vMotion?
**Answer:** Online movement of VM disks between datastores.

### Q27. What does HA do?
**Answer:** Detects eligible host failures and restarts protected VMs on survivors.

### Q28. Why does HA use datastore heartbeats?
**Answer:** To add evidence when management-network status is ambiguous.

### Q29. What is host isolation?
**Answer:** A host is alive but loses required HA management connectivity.

### Q30. What is admission control?
**Answer:** Policy reserving enough failover capacity for configured failures.

### Q31. Why is N+1 a failure-state calculation?
**Answer:** Surviving hosts must fit all protected workload after one host is gone.

### Q32. HA vs FT?
**Answer:** HA restarts; FT maintains synchronized secondary execution for supported VMs.

### Q33. What does DRS do?
**Answer:** Optimizes placement using demand, entitlement, rules and migration benefit.

### Q34. Why can DRS refuse a move?
**Answer:** Rules, reservations, devices, EVC, vMotion health or capacity can block it.

### Q35. What is anti-affinity?
**Answer:** A rule that spreads redundant VMs across hosts.

### Q36. Authentication vs authorization?
**Answer:** Authentication proves identity; authorization determines allowed actions.

### Q37. Why use service accounts?
**Answer:** They provide least-privilege, auditable integration identities.

### Q38. What is VMCA?
**Answer:** The vSphere certificate authority/trust component in standard architectures.

### Q39. Why monitor certificates?
**Answer:** Expiry or identity mismatch can break login, APIs, host connectivity and integrations.

### Q40. Why use lockdown mode?
**Answer:** To reduce direct host administration paths.

### Q41. Why disable SSH when unused?
**Answer:** To reduce attack surface and unmanaged changes.

### Q42. What do Host Profiles solve?
**Answer:** Desired-state consistency and drift detection.

### Q43. What is a desired cluster image?
**Answer:** Target ESX software stack including base version and supported add-ons/components.

### Q44. Why remediate one host at a time?
**Answer:** To preserve service and validate each host before continuing.

### Q45. Why pair driver and firmware lifecycle?
**Answer:** Unsupported combinations can destabilize NIC/HBA behavior.

### Q46. Why separately back up vCenter?
**Answer:** Its management/SSO/inventory state is not replaced by running VMs.

### Q47. Why start troubleshooting with tasks/events?
**Answer:** They reveal exact operations, errors, timestamps and objects.

### Q48. What does esxtop CPU show beyond guest CPU?
**Answer:** Scheduler pressure such as ready/co-stop.

### Q49. What does sustained hypervisor swap indicate?
**Answer:** Serious host memory pressure.

### Q50. How do you trace storage latency?
**Answer:** Guest→controller/VMDK→datastore→ESX path→SAN/NAS→array.

### Q51. What is the current PowerCLI family used by the source?
**Answer:** VCF PowerCLI.

### Q52. Why query before changing with PowerCLI?
**Answer:** To validate scope and prevent bulk mistakes.

### Q53. Why can a 'Not Responding' host still run VMs?
**Answer:** Only management communication may have failed.

### Q54. First step for vMotion failure?
**Answer:** Read the exact task/event error.

### Q55. First principle for missing storage?
**Answer:** Troubleshoot visibility/pathing before formatting or recreating anything.

### Q56. Why is datastore-full severe?
**Answer:** Many VMs can lose write, snapshot, swap or power-on capacity at once.

### Q57. Why should snapshot cleanup not be blind automation?
**Answer:** Consolidation can be heavy and requires owner/change awareness.

### Q58. How do you troubleshoot VM CPU slowness?
**Answer:** Check guest demand, host saturation, ready/co-stop, limits, oversizing and NUMA.

### Q59. How do you troubleshoot VM memory?
**Answer:** Separate guest paging from ballooning, host swap, limits, reservations and capacity.

### Q60. How do you troubleshoot VM networking?
**Answer:** Trace vNIC→port group/VLAN→vSwitch→vmnic→physical network→routing/firewall.

### Q61. What is the core vSphere troubleshooting rule?
**Answer:** Identify the owning layer, collect evidence, and change the smallest justified component.


## Completion Checklist

- [ ] I understand vSphere architecture.
- [ ] I understand ESX/ESXi vs vCenter.
- [ ] I can plan DNS/NTP/IP/VLAN/storage before installation.
- [ ] I can install and configure an ESX host in a lab.
- [ ] I can use DCUI.
- [ ] I can use Host Client.
- [ ] I can use essential ESXCLI commands.
- [ ] I understand current two-stage vCenter deployment.
- [ ] I understand SSO-domain planning.
- [ ] I can build vCenter inventory.
- [ ] I understand maintenance mode.
- [ ] I can explain/configure vSS.
- [ ] I can explain/configure vDS.
- [ ] I understand port groups and VMkernel adapters.
- [ ] I understand VLAN, MTU, and NIC teaming.
- [ ] I understand VMFS, NFS, FC, and iSCSI.
- [ ] I understand multipathing, APD, and PDL.
- [ ] I understand vVols and SPBM.
- [ ] I can create/configure VMs.
- [ ] I understand VMware Tools, VMXNET3, PVSCSI, and virtual NVMe.
- [ ] I understand thin/thick VM disk provisioning.
- [ ] I understand snapshots/consolidation.
- [ ] I understand templates, clones, customization, and Content Library.
- [ ] I understand shares/reservations/limits/resource pools.
- [ ] I understand vMotion and Storage vMotion.
- [ ] I understand EVC.
- [ ] I understand HA/admission control/isolation/restart priority.
- [ ] I understand FT.
- [ ] I understand DRS and placement rules.
- [ ] I understand SSO/RBAC/permissions.
- [ ] I understand VMCA/certificate basics.
- [ ] I understand host hardening fundamentals.
- [ ] I understand Host Profiles.
- [ ] I understand vSphere Lifecycle Manager desired images.
- [ ] I can monitor tasks/events/alarms/performance.
- [ ] I can use `esxtop`.
- [ ] I can install/use VCF PowerCLI.
- [ ] I can build PowerCLI inventory/health reports.
- [ ] I can troubleshoot major vSphere compute/network/storage/cluster failures.
- [ ] I completed all 30 labs.
- [ ] I completed the Production-Style vSphere Cluster mini project.
