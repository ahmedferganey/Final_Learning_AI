# 25. Red Hat High Availability Clustering

> Phase 5 — Linux System Administration

This course completes Phase 5 by moving from single-server administration into **service resiliency across multiple nodes**.

The administration question changes from:

> Is this server running?

to:

> **Can the service remain correct and recover automatically when a node, process, network path, storage path, or power component fails?**

Current Red Hat Enterprise Linux 10 documentation uses the Red Hat High Availability Add-On with **Pacemaker**, **Corosync**, and **pcs**. Proper fencing is a fundamental requirement because an isolated or unresponsive node cannot simply be assumed to have stopped accessing shared resources.

Red Hat's High Availability training scope also includes:

- Pacemaker cluster creation
- node membership and quorum
- fencing
- cluster resources and resource groups
- troubleshooting
- Ansible automation
- two-node clusters
- iSCSI
- multipathing
- cluster-aware LVM
- GFS2
- elimination of single points of failure

This module uses current RHEL 10 administration concepts and commands while covering that broader enterprise HA skill set.

---

## 1. Topic Title

**Red Hat High Availability Clustering**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain availability, redundancy, failover, fault domains, split brain, quorum, and fencing.
- Explain Pacemaker, Corosync, pcs, pcsd, CIB, resource agents, and cluster resources.
- Prepare RHEL nodes and create a basic Pacemaker cluster.
- Configure, inspect, and safely test fencing in an authorized lab environment.
- Create highly available IP, filesystem, LVM, Apache, and NFS services.
- Use groups and ordering, colocation, location, and stickiness constraints.
- Put nodes into standby, move resources, and use maintenance mode safely.
- Diagnose resource failures, fencing failures, quorum loss, and cluster communication problems.
- Explain special issues in two-node clusters and the purpose of quorum devices.
- Explain and configure iSCSI, multipath, active/passive LVM, shared LVM, and GFS2 foundations.
- Design HA systems that reduce single points of failure across compute, storage, power, and network infrastructure.
- Apply safe maintenance, update, backup, and automation practices.

---

## 3. Prerequisites

Strongly recommended:

- 20. Linux Essentials
- 21. Red Hat System Administration I
- 22. Red Hat System Administration II
- 23. Red Hat System Administration III
- 24. Linux Web Server Administration

You should already understand:

```text
systemd
LVM
XFS
NFS
iSCSI basics
IPv4/IPv6
DNS
firewalld
SELinux
SSH
Apache HTTP Server
Ansible fundamentals
```

Recommended lab:

```text
node1.lab.example    192.168.56.31
node2.lab.example    192.168.56.32
client.lab.example   192.168.56.40
storage.lab.example  192.168.56.50

Service VIP:
192.168.56.100
```

For meaningful fencing practice, use a virtualization platform, cloud lab, IPMI-capable lab hardware, or another environment with a supported fence agent.

**Never perform fencing, disk initialization, shared-LUN modification, or cluster experiments on systems you do not own or explicitly administer.**

---

## 4. Core Concepts Explanation

# Part 1 — High Availability Fundamentals

### 1. Availability Is a Service Property

Availability is the fraction of time a service is usable when required.

Conceptually:

```text
Availability =
service uptime / observation time
```

Example:

```text
30 days = 43,200 minutes

Downtime = 30 minutes

Availability =
(43,200 - 30) / 43,200
≈ 99.93%
```

The key point:

```text
server uptime
≠
service availability
```

A server can be powered on while the application, filesystem, database, VIP, or upstream dependency is unavailable.

### 2. High Availability vs Fault Tolerance

**High Availability**

Uses redundancy and automated recovery/failover.

Some interruption may occur.

**Fault Tolerance**

Attempts to continue operation with little or no visible interruption when a component fails.

A normal active/passive Pacemaker cluster is a high-availability design, not perfect fault tolerance.

### 3. Redundancy

Redundancy adds alternate components.

Examples:

```text
2 nodes
2 switches
2 network paths
2 power feeds
2 storage paths
multiple DNS servers
multiple application instances
```

Redundancy alone is not enough.

Two nodes plugged into the same power strip still have a shared power failure domain.

### 4. Single Point of Failure

A single point of failure is one component whose loss removes the service.

Example:

```text
Node1 + Node2
      |
   one switch
      |
   clients
```

Even with two cluster nodes, the switch remains a single point of failure.

### 5. Fault Domain

A fault domain is the set of components affected by one failure.

Examples:

- one rack
- one hypervisor
- one availability zone
- one network switch
- one power circuit
- one storage controller

Good HA design places redundant components in independent fault domains where practical.

### 6. Failover

Normal:

```text
VIP
Filesystem
Apache
   |
 node1
```

Failure:

```text
node1 fails
   ↓
cluster detects failure
   ↓
cluster isolates/fences node1 when required
   ↓
resources move
   ↓
node2 owns VIP/filesystem/Apache
```

Clients continue using the same service identity, such as a virtual IP or DNS endpoint.

---

# Part 2 — Active/Passive and Active/Active

### 7. Active/Passive

One node runs the service.

Another waits.

```text
          Shared Storage
             /     \
          node1   node2
            |
          ACTIVE
```

Typical active/passive resource chain:

```text
LVM activation
    ↓
Filesystem mount
    ↓
Virtual IP
    ↓
Apache
```

Only one node should own the active/passive storage/filesystem at a time.

### 8. Active/Active

Multiple nodes provide service at the same time.

Examples:

- stateless web frontends
- clustered applications designed for concurrent access
- GFS2-based supported shared-filesystem architectures

Active/active requires explicit coordination.

Do **not** take a filesystem such as XFS on one shared block device and simply mount it read-write on multiple independent nodes.

That can corrupt data.

### 9. Choosing Active/Passive vs Active/Active

Ask:

```text
Can the application run concurrently?
Can the storage safely support concurrent access?
Is the application state shared?
How is locking implemented?
What is the failure model?
What is the performance requirement?
```

Use the simplest architecture that meets the requirement.

---

# Part 3 — Red Hat HA Stack

### 10. Pacemaker

Pacemaker is the cluster resource manager.

It decides:

- which node should run a resource
- when a resource should start or stop
- how to recover after failure
- how constraints affect placement
- whether dependencies are satisfied

### 11. Corosync

Corosync provides cluster communication and membership functions.

Conceptually:

```text
node1
  ║
  ║ cluster messaging
  ║
node2
```

If communication is lost, the cluster must avoid the dangerous assumption that the other node is dead.

### 12. pcs

`pcs` is the primary command-line management interface.

Common commands:

```bash
pcs status
pcs cluster status
pcs resource status
pcs property config
pcs constraint config
pcs quorum status
pcs stonith status
```

### 13. pcsd

`pcsd` supports remote management/authentication for pcs operations.

The dedicated `hacluster` account is commonly used for cluster administration authentication.

### 14. CIB — Cluster Information Base

The CIB stores cluster configuration state.

Conceptually it contains:

```text
cluster properties
nodes
resources
resource defaults
constraints
fencing devices
operation definitions
```

Do not manually edit Pacemaker's internal configuration files.

Use supported tools such as `pcs`.

### 15. Resource Agents

A resource agent provides cluster-aware operations such as:

```text
start
stop
monitor
validate
```

Examples:

```text
IPaddr2
Filesystem
LVM-activate
apache
nfsserver
```

Discover agents:

```bash
pcs resource agents
```

Inspect one:

```bash
pcs resource describe ocf:heartbeat:IPaddr2
```

---

# Part 4 — Designing Before Configuring

### 16. Dependency Map

Before creating a cluster, draw the service dependency chain.

Example:

```text
Client
  ↓
DNS
  ↓
VIP
  ↓
Firewall
  ↓
Apache
  ↓
Filesystem
  ↓
LVM
  ↓
Shared LUN
  ↓
Storage network
  ↓
Storage array
```

The cluster can only protect components it can detect/manage or for which redundancy is designed.

### 17. Shared Fate

"Redundant" components may still share the same failure.

Examples:

```text
two VMs on one hypervisor
two NICs connected to one switch
two power supplies using one circuit
two storage paths using one HBA
```

Architecture reviews should explicitly identify shared-fate dependencies.

### 18. Management Network

The cluster may depend on:

- Corosync communication network
- client/service network
- fence-device management network
- storage network

Separating these can improve resiliency and security.

A private cluster network is often useful, though actual supported design depends on environment.

---

# Part 5 — Preparing Cluster Nodes

### 19. Verify Identity and Name Resolution

On both nodes:

```bash
hostnamectl
getent hosts node1.lab.example
getent hosts node2.lab.example
```

Verify connectivity:

```bash
ping -c 2 node2.lab.example
```

Stable name resolution matters.

### 20. Time Synchronization

```bash
timedatectl
chronyc tracking
chronyc sources -v
```

Accurate time helps with:

- logs
- troubleshooting
- security
- distributed operations

### 21. Enable RHEL 10 HA Repository

In an authorized subscribed RHEL x86_64 environment:

```bash
sudo subscription-manager repos \
  --enable=rhel-10-for-x86_64-highavailability-rpms
```

Repository names differ by architecture and distribution.

### 22. Install Cluster Software

```bash
sudo dnf install pcs pacemaker fence-agents-all
```

In production, you can install only the required fence agent rather than all agents.

### 23. Configure firewalld

```bash
sudo firewall-cmd \
  --permanent \
  --add-service=high-availability

sudo firewall-cmd \
  --add-service=high-availability
```

Verify:

```bash
sudo firewall-cmd --list-services
```

The ideal production firewall rules depend on:

- interfaces
- network separation
- off-host firewalling
- actual cluster traffic paths

### 24. Set `hacluster` Password

On each node:

```bash
sudo passwd hacluster
```

Use an organization-approved secure credential.

---

# Part 6 — Creating a Two-node Cluster

### 25. Authenticate Nodes

From the administration node:

```bash
sudo pcs host auth \
  node1.lab.example \
  node2.lab.example
```

The command prompts for the `hacluster` credentials.

### 26. Create and Start Cluster

```bash
sudo pcs cluster setup \
  my_cluster \
  --start \
  node1.lab.example \
  node2.lab.example
```

### 27. Enable Cluster Services at Boot

```bash
sudo pcs cluster enable --all
```

Whether you enable automatic startup in a specific production environment should follow the operational design.

### 28. Verify Status

```bash
pcs cluster status
pcs status
pcs status nodes
pcs quorum status
```

Do not begin adding production resources until:

- membership is stable
- Corosync communication is healthy
- expected quorum behavior is understood
- fencing design is correct

---

# Part 7 — Quorum

### 29. What Quorum Solves

Quorum prevents disconnected portions of a cluster from independently operating the same protected resources.

For a six-node majority-based cluster:

```text
6 total
4 = quorum
3 = no majority
```

### 30. Quorum and Resource Safety

Pacemaker normally stops clustered resources when quorum is lost according to normal cluster policy.

Why?

Because operating without a trusted majority can create split-brain behavior and data corruption.

### 31. votequorum

Inspect:

```bash
pcs quorum status
```

Also:

```bash
corosync-quorumtool -s
```

The quorum system works together with fencing.

### 32. Split Brain

Network partition:

```text
node1        node2
  |            |
  X------------X
 communication lost
```

Danger:

```text
node1 says:
"node2 failed"

node2 says:
"node1 failed"
```

If both independently mount/write the same data, corruption can occur.

### 33. Two-node Challenge

A two-node cluster has a special problem.

If communication stops:

```text
Node1 cannot distinguish:

Node2 is dead
from
the network link is dead
```

Fencing is therefore essential.

### 34. Quorum Device

A quorum device can provide external arbitration.

Concept:

```text
node1 -----\
            \
             qnetd
            /
node2 -----/
```

The quorum device is not an application server.

It participates in quorum decisions.

For two-node/even-node designs, it can provide additional arbitration when architecture supports it.

---

# Part 8 — Fencing / STONITH

### 35. Why Fencing Is Fundamental

Imagine node1 disappears from cluster communication.

You do not know whether node1:

- crashed
- lost only cluster network
- is still serving clients
- still has shared storage mounted
- is still writing data

The safe sequence is:

```text
suspect node
   ↓
isolate/fence node
   ↓
confirm it can no longer own protected resources
   ↓
start resources elsewhere
```

### 36. STONITH

STONITH is the traditional term for cluster node fencing.

Possible mechanisms:

```text
IPMI/BMC
hypervisor API
cloud API
power distribution unit
SBD/watchdog
supported storage isolation
```

### 37. Fence Agents

List:

```bash
pcs stonith list
```

Installed packages:

```bash
rpm -qa | grep '^fence'
```

Describe an agent:

```bash
pcs stonith describe fence_ipmilan
```

### 38. Fence Resource Pattern

**Do not copy parameters without checking the real fence agent.**

Pattern:

```bash
sudo pcs stonith create fence-node1 \
  fence_<agent> \
  ip=<management-address> \
  username=<user> \
  password=<secret> \
  pcmk_host_list="node1.lab.example"
```

Before creation:

```bash
pcs stonith describe fence_<agent>
```

### 39. Fencing Test Safety

A real fence test may:

```text
power off
reset
terminate a VM
isolate storage
```

Before testing:

1. verify node name
2. verify fence target
3. verify management IP
4. verify lab/maintenance authorization
5. ensure no production workload is affected

### 40. Fencing Failure

A cluster can intentionally refuse failover if it cannot prove that the old owner is safely isolated.

This can look like:

```text
service is down even though second node is healthy
```

That can be safer than starting the service in a state that risks double ownership and data corruption.

### 41. Fencing Topology

Some designs use multiple levels.

Example:

```text
Level 1 -> hypervisor fence
Level 2 -> physical power fence
```

This can improve fencing reliability.

### 42. SBD Concept

SBD can use watchdog/storage-based fencing mechanisms in supported environments.

SBD requires precise platform-specific design.

Do not implement it from a generic copied tutorial.

---

# Part 9 — Basic Cluster Resources

### 43. Virtual IP

Create a lab VIP:

```bash
sudo pcs resource create vip \
  ocf:heartbeat:IPaddr2 \
  ip=192.168.56.100 \
  cidr_netmask=24
```

Verify:

```bash
pcs resource status
pcs status
```

On the active node:

```bash
ip address
```

Clients should use the VIP rather than a node-specific IP.

### 44. Resource Monitoring

Pacemaker continually checks resource health according to configured monitor operations.

Inspect:

```bash
pcs resource status
pcs resource config
pcs resource failcount show
```

### 45. Resource Agent Metadata

Before configuring an unfamiliar resource:

```bash
pcs resource describe ocf:heartbeat:Filesystem
```

or:

```bash
pcs resource describe apache
```

Use metadata to learn:

- required parameters
- optional parameters
- supported operations

---

# Part 10 — Active/Passive Storage and Apache

### 46. Why Resource Order Matters

For a stateful Apache service using shared LVM/XFS:

```text
LVM activate
     ↓
mount filesystem
     ↓
assign VIP
     ↓
start Apache
```

Stopping should happen in reverse.

### 47. LVM-activate Resource

Current RHEL HA documentation uses `LVM-activate` for cluster-controlled LVM activation.

Pattern:

```bash
sudo pcs resource create my_lvm \
  ocf:heartbeat:LVM-activate \
  vgname=my_vg \
  vg_access_mode=system_id \
  --group apachegroup
```

Important:

For active/passive use, do not create multiple independent `LVM-activate` resources that activate the same volume group concurrently.

### 48. Filesystem Resource

```bash
sudo pcs resource create my_fs \
  Filesystem \
  device="/dev/my_vg/my_lv" \
  directory="/var/www" \
  fstype="xfs" \
  --group apachegroup
```

### 49. VIP Resource in Group

```bash
sudo pcs resource create vip \
  IPaddr2 \
  ip=192.168.56.100 \
  cidr_netmask=24 \
  --group apachegroup
```

### 50. Apache Resource

Pattern:

```bash
sudo pcs resource create webserver \
  apache \
  configfile="/etc/httpd/conf/httpd.conf" \
  statusurl="http://127.0.0.1/server-status" \
  --group apachegroup
```

Inspect exact supported parameters first:

```bash
pcs resource describe apache
```

### 51. Group Semantics

A resource group:

```text
apachegroup:
my_lvm
my_fs
vip
webserver
```

normally provides:

```text
same-node colocation
ordered startup
reverse ordered shutdown
```

This is extremely useful for active/passive service stacks.

---

# Part 11 — Constraints

### 52. Ordering Constraints

Example:

```bash
pcs constraint order start vip then webserver
```

Meaning:

```text
VIP must start before webserver
```

### 53. Colocation Constraints

```bash
pcs constraint colocation add webserver with vip
```

This expresses placement relationship.

### 54. Location Constraints

Preference example:

```bash
pcs constraint location \
  webserver \
  prefers node1.lab.example=100
```

A positive preference is not the same as a hard requirement.

### 55. Resource Stickiness

Stickiness discourages unnecessary movement.

Example operational goal:

```text
Node1 fails
→ service moves to Node2
→ Node1 comes back

Question:
Should service immediately move back?
```

Immediate failback may cause another outage.

Stickiness and location policy help control this behavior.

### 56. Inspect Constraints

```bash
pcs constraint config
```

Always review existing constraints before adding new ones.

---

# Part 12 — Failures and Recovery

### 57. Failure Counts

```bash
pcs resource failcount show
```

A resource can accumulate failure history.

### 58. Resource Cleanup

After correcting the root cause:

```bash
pcs resource cleanup webserver
```

Cleanup is not the fix.

It clears failure state and allows the cluster to re-evaluate the resource.

### 59. Apache Resource Fails

Investigate the application independently:

```bash
apachectl configtest

journalctl -u httpd

ss -tlnp | grep ':80'
```

Then cluster:

```bash
pcs status
pcs resource status
```

Do not blame Pacemaker for an invalid Apache configuration.

---

# Part 13 — Node Maintenance

### 60. Standby

Before node maintenance:

```bash
pcs node standby node1.lab.example
```

Verify resources moved:

```bash
pcs status
```

Return:

```bash
pcs node unstandby node1.lab.example
```

### 61. Resource Move

```bash
pcs resource move webserver node2.lab.example
```

Inspect:

```bash
pcs status
pcs constraint config
```

Clear temporary move policy when finished:

```bash
pcs resource clear webserver
```

### 62. Maintenance Mode

For controlled cluster-wide maintenance:

```bash
pcs property set maintenance-mode=true
```

Perform approved work.

Then:

```bash
pcs property set maintenance-mode=false
```

Maintenance mode changes normal cluster resource management.

Use it only with a clear procedure.

---

# Part 14 — Cluster Troubleshooting

### 63. Core Status Commands

```bash
pcs status
pcs cluster status
pcs status nodes
pcs resource status
pcs property config
pcs constraint config
pcs quorum status
pcs stonith status
```

### 64. Service Status

```bash
systemctl status corosync
systemctl status pacemaker
systemctl status pcsd
```

### 65. Logs

```bash
journalctl -u corosync
journalctl -u pacemaker
journalctl -u pcsd
```

### 66. Network Checks

```bash
ip -br address
ip route
getent hosts node2.lab.example
ping -c 2 node2.lab.example
```

### 67. Cluster Communication Failure

Possible causes:

```text
node down
Corosync down
network link failure
firewall
name/address mismatch
interface/routing failure
misconfigured Corosync links
```

Separate:

```text
host/network problem
from
cluster resource problem
```

### 68. Fencing Failure Investigation

Check:

- fence-agent availability
- management address
- credentials
- target mapping
- fence API access
- firewall/routing
- timeouts
- device state
- topology levels

Never disable fencing as a casual fix for a production cluster.

---

# Part 15 — Two-node Cluster Design

### 69. Why Two Nodes Are Popular

Advantages:

- lower cost
- simple active/passive design
- easy conceptual model

Risks:

- 50/50 partition ambiguity
- fencing is essential
- limited voting majority options
- shared dependencies are easy to overlook

### 70. Quorum Device Placement

A quorum device should provide **independent** arbitration.

Poor design:

```text
node1 VM
node2 VM
qdevice VM

all on same physical host
```

A single hypervisor failure removes everything.

Better designs spread failure domains.

---

# Part 16 — iSCSI Shared Storage

### 71. iSCSI Concepts

iSCSI transports SCSI block commands over IP.

Architecture:

```text
Storage Target
      |
IP storage network
      |
 +----+----+
 |         |
node1    node2
initiator initiator
```

### 72. Install Initiator Tools

```bash
sudo dnf install iscsi-initiator-utils
```

### 73. Discover Target

```bash
sudo iscsiadm \
  -m discovery \
  -t sendtargets \
  -p storage.lab.example
```

### 74. Log In

```bash
sudo iscsiadm -m node --login
```

Inspect:

```bash
lsblk
sudo iscsiadm -m session
```

### 75. Shared LUN Safety

Before `pvcreate`, `mkfs`, or partitioning:

```bash
lsblk -f
blkid
pvs
vgs
lvs
```

Confirm:

- exact LUN
- no existing required data
- all nodes see expected device
- device ownership architecture is understood

---

# Part 17 — Device Mapper Multipath

### 76. Why Multipath Exists

One storage path is a single point of failure.

```text
                 Path A
node1 ------------------------ storage
   \                            /
    ----------- Path B --------
```

Device Mapper Multipath combines redundant paths into one logical device.

### 77. Inspect Multipath

Typical tools:

```bash
sudo multipath -ll
lsblk
```

The exact configuration depends on:

- storage array
- transport
- HBA/NIC design
- vendor recommendations
- RHEL support matrix

### 78. Multipath Is Not a Backup

Multipath protects storage **path** availability.

It does not protect against:

- accidental deletion
- filesystem corruption
- application corruption
- storage-array total failure

HA and backup solve different problems.

---

# Part 18 — LVM in Active/Passive Clusters

### 79. LVM Ownership

In active/passive architecture:

```text
shared LUN visible to both nodes

but

VG/LV/filesystem active on one node at a time
```

Pacemaker controls activation.

### 80. LVM System ID Concept

Cluster-controlled active/passive LVM can use system-ID-based ownership with the `LVM-activate` resource agent.

This prevents uncontrolled simultaneous activation.

### 81. Resource-controlled Activation

Do not configure the same active/passive VG to auto-activate independently on both nodes while also expecting Pacemaker to own it.

The cluster must be the authority for resource ownership.

---

# Part 19 — Shared LVM for Active/Active Use

### 82. Shared LVM Architecture

When multiple nodes need concurrent access to shared LVM, a lock manager is required.

Current RHEL LVM shared-storage concepts include:

```text
lvmlockd
DLM or sanlock
shared VG
```

### 83. Shared VG Concept

Current RHEL uses:

```bash
vgcreate --shared
```

for shared LVM volume groups in relevant supported designs.

Access is coordinated with locking.

### 84. Do Not Confuse Active/Passive and Shared LVM

```text
Active/passive:
one node activates/uses filesystem

Shared LVM:
multiple nodes can coordinate access
```

Use the correct model for the filesystem/application.

---

# Part 20 — GFS2

### 85. What GFS2 Is

GFS2 is a clustered filesystem designed for simultaneous multi-node access in supported Red Hat cluster architectures.

It uses distributed locking.

### 86. Why GFS2 Is Different from XFS

XFS:

```text
normal local filesystem
one active owner of shared block device in HA design
```

GFS2:

```text
cluster filesystem
multiple cluster nodes can mount concurrently
```

### 87. GFS2 Journals

A GFS2 filesystem requires enough journals for the nodes that will mount it.

Example conceptual creation:

```bash
sudo mkfs.gfs2 \
  -j 2 \
  -p lock_dlm \
  -t my_cluster:sharedfs \
  /dev/vgshared/lvshared
```

Interpretation:

```text
-j 2
two journals

-p lock_dlm
DLM locking protocol

-t my_cluster:sharedfs
cluster/filesystem lock-table identity
```

Exact sizing and architecture must follow current Red Hat documentation.

### 88. Locking Services

Active/active shared-storage designs rely on coordinated locking.

Important concepts:

```text
DLM
lvmlockd
Pacemaker resources
GFS2
```

Do not manage these as unrelated services.

---

# Part 21 — Highly Available NFS

### 89. HA NFS Architecture

```text
Client
   |
   | NFS to VIP
   v
active cluster node
   |
   v
shared filesystem
```

Failover moves:

```text
storage activation
mount
NFS service/resources
VIP
```

The client continues using the stable service identity.

### 90. NFS Resource Dependencies

A highly available NFS design can require resources for:

- LVM
- filesystem
- NFS server
- export
- VIP

Use resource groups and constraints according to the supported resource-agent design.

---

# Part 22 — Highly Available Apache

### 91. HA Apache Architecture

```text
                  VIP 192.168.56.100
                          |
                 +--------+--------+
                 |                 |
               node1             node2
                ACTIVE            READY
                   \               /
                    \             /
                     shared data
```

Normal:

```text
VIP + filesystem + Apache on node1
```

Failover:

```text
fence/isolate node1
start resources on node2
VIP remains the client endpoint
```

### 92. Client Test

From `client.lab.example`:

```bash
curl http://192.168.56.100/
```

Run repeatedly during a controlled failover test.

Measure:

- failed requests
- recovery time
- state consistency

HA does not imply zero failed requests.

---

# Part 23 — Resource Placement and Failback

### 93. Preferred Node

A cluster can prefer node1 without requiring it absolutely.

Benefits:

- predictable normal state
- easier operations

But excessive forced failback can create avoidable outages.

### 94. Avoid Resource Ping-Pong

If a resource repeatedly moves between nodes:

Investigate:

- intermittent application health
- storage path instability
- network loss
- resource-monitor timeout
- aggressive failback policy
- bad constraint design

Do not treat constant movement as normal HA behavior.

---

# Part 24 — Cluster Monitoring

### 95. PCP

Current RHEL HA documentation recommends Performance Co-Pilot data collection as useful for troubleshooting cluster disruptions.

A cluster problem often requires historical evidence:

```text
CPU spike
storage latency
packet loss
fence timeout
resource failure
```

Without historical monitoring, you only see the state after the incident.

### 96. What to Monitor

At minimum:

```text
node availability
cluster membership
quorum
resource state
fencing events
storage latency
network errors
filesystem usage
application response
VIP reachability
```

---

# Part 25 — Updating a Cluster

### 97. Why Cluster Updates Need Procedure

Updating both nodes arbitrarily can:

- remove redundancy
- cause version incompatibility
- restart critical services
- trigger failover unexpectedly

Use a controlled sequence.

Concept:

```text
verify cluster healthy
 ↓
standby node1
 ↓
update/reboot node1
 ↓
verify/rejoin
 ↓
standby node2
 ↓
update/reboot node2
 ↓
verify complete cluster
```

Follow Red Hat's current supported update guidance for the exact release.

### 98. Never Blindly Auto-update Cluster Nodes

Uncoordinated automatic package updates can create unexpected cluster behavior.

Enterprise HA updates should be controlled and tested.

---

# Part 26 — Cluster Configuration Backup

### 99. Why Back Up Cluster Configuration

You need recovery information for:

- resources
- constraints
- fencing
- Corosync configuration
- operational documentation

Use current pcs backup/export functions supported by your release.

Also maintain configuration documentation/version control.

### 100. Recovery Is More Than Configuration

A full HA recovery plan includes:

```text
cluster config
application config
storage metadata
application data backup
DNS/network policy
fence credentials/process
certificates/secrets
runbooks
```

---

# Part 27 — Ansible Automation for HA

### 101. Why Automate Clusters

Clusters contain repeated node configuration:

- packages
- firewall
- users
- time sync
- repository configuration
- cluster packages
- resource definitions

Automation reduces drift.

### 102. RHEL System Role Concept

Red Hat provides an HA cluster system role for supported automation workflows.

Concept:

```yaml
- name: Configure HA cluster
  hosts:
    - node1
    - node2

  tasks:
    - name: Apply HA cluster role
      ansible.builtin.include_role:
        name: redhat.rhel_system_roles.ha_cluster
```

Actual variables depend on current role documentation and should be validated before deployment.

### 103. Automate Carefully

Automation can destroy a cluster faster than manual work if wrong.

Safe rollout:

```text
validate inventory
 ↓
review generated configuration
 ↓
test lab
 ↓
maintenance window
 ↓
one controlled change
 ↓
verify cluster
```

---

# Part 28 — High Availability vs Disaster Recovery

### 104. HA

Usually focuses on:

```text
local service continuity
rapid failover
node/component failures
```

### 105. Disaster Recovery

Usually focuses on:

```text
site loss
regional disaster
large-scale corruption
longer-distance recovery
backup/replication
RPO/RTO
```

A two-node cluster in one data center is not a disaster-recovery solution by itself.

---

# Part 29 — RPO and RTO

### 106. RTO

Recovery Time Objective:

```text
How long can service be unavailable?
```

### 107. RPO

Recovery Point Objective:

```text
How much data loss is acceptable?
```

A cluster can improve RTO but does not automatically give an acceptable RPO.

Data protection still requires:

- replication
- backups
- application-consistent recovery design

---

# Part 30 — Eliminating Single Points of Failure

### 108. Compute

Avoid:

```text
both VMs on one hypervisor
```

where the requirement demands host-level resilience.

### 109. Network

Consider:

```text
multiple switches
bond/team paths where supported
redundant routing
redundant VIP path
```

### 110. Power

Consider:

```text
dual PSU
independent PDU
UPS
separate circuits
```

### 111. Storage

Consider:

```text
multipath
redundant storage controllers
redundant fabric
array-level resilience
backup
```

### 112. DNS

If service depends on DNS, design DNS redundancy too.

### 113. Management

A cluster that cannot be managed during a failure is operationally weak.

Ensure:

- console access
- fence-device access
- monitoring
- logs
- admin authentication

are resilient enough for the requirement.

---

# Part 31 — Troubleshooting Scenarios

### 114. Resource Does Not Start on Node2

Check:

```bash
pcs status
pcs resource failcount show
```

Then:

```text
Can node2 access storage?
Can node2 mount filesystem?
Is application config identical?
Does node2 have required packages?
SELinux?
firewalld?
VIP subnet?
resource constraints?
```

### 115. Cluster Has No Quorum

Check:

```bash
pcs quorum status
pcs status nodes
corosync-quorumtool -s
```

Investigate node membership and communication.

Do not force service start blindly.

### 116. VIP Exists but Service Fails

```bash
ip address
ss -tlnp
curl http://127.0.0.1/
pcs resource status
```

VIP ownership alone does not prove Apache works.

### 117. Shared Filesystem Cannot Mount

Check:

```bash
lsblk -f
pvs
vgs
lvs
findmnt
journalctl
```

Then determine:

- LUN visible?
- multipath healthy?
- VG activated?
- filesystem clean?
- already mounted elsewhere?
- cluster ownership correct?

### 118. Node Keeps Getting Fenced

Potential causes:

- real node instability
- Corosync network loss
- watchdog timeout
- resource failure escalation
- fence topology issue
- storage timeout
- overloaded node

Do not simply increase timeouts without finding the root cause.

### 119. Resource Flaps Between Nodes

Check:

```text
monitor failures
stickiness
location constraints
storage/network instability
application crash
failure threshold
```

### 120. Fence Agent Cannot Reach BMC/Hypervisor

Check:

```text
management routing
DNS
firewall
credentials
API permissions
certificate/API changes
device target mapping
```

---


# Enhanced Deep-Study Layer — Enterprise High Availability and Cluster Engineering

The original high-availability course is preserved below. This enhanced layer adds deeper clustering theory, failure-detection mechanics, Pacemaker/Corosync architecture, quorum mathematics, fencing design, resource-agent behavior, constraints, storage ownership, iSCSI, multipathing, LVM/GFS2, maintenance, monitoring, disaster-recovery boundaries, automation, and fault-injection labs.

The central HA model is:

```text
Failure occurs
    ↓
Failure must be detected
    ↓
Cluster must determine authoritative membership
    ↓
Unsafe old owner must be isolated when required
    ↓
Dependencies must be started in correct order elsewhere
    ↓
Service identity becomes available
    ↓
Client recovery is measured
```

The most important principle in this file is:

```text
Availability without data correctness is failure.
```

A cluster must not recover a service by creating simultaneous ownership of resources that cannot safely be shared.

---

## Enhanced Deep Dive 1 — Availability Is Measured at the Service Boundary

A server being powered on does not prove the service is available.

Service chain:

```text
client
 ↓
DNS
 ↓
network
 ↓
VIP/load balancer
 ↓
application
 ↓
storage/database
```

Availability should be measured where users consume the service.

Conceptually:

```text
Availability =
successful service time /
required service time
```

Example:

```text
Observation window:
30 days
= 43,200 minutes

Downtime:
30 minutes

Availability:
(43,200 - 30) / 43,200
≈ 99.93%
```

A cluster can have healthy nodes and still fail the user because DNS or shared storage is down.

---

## Enhanced Deep Dive 2 — "Nines" and Downtime Budget

Approximate annual downtime budgets help communicate requirements.

Conceptually:

```text
99%
99.9%
99.99%
99.999%
```

Each additional nine dramatically reduces allowed downtime.

The engineering lesson is more important than memorizing exact minutes:

```text
higher availability target
→ stronger redundancy
→ faster detection/recovery
→ stricter maintenance
→ better monitoring
→ more independent fault domains
→ higher cost/complexity
```

Define availability requirement before choosing cluster architecture.

---

## Enhanced Deep Dive 3 — MTBF, MTTR, and Availability

A simplified reliability relationship is often expressed conceptually with:

```text
MTBF
→ mean time between failures

MTTR
→ mean time to repair/recover
```

Higher availability can come from:

```text
fewer failures
AND/OR
faster recovery
```

HA clustering primarily helps reduce recovery time for covered failures.

It does not automatically improve the reliability of the application code or storage array.

---

## Enhanced Deep Dive 4 — HA vs Fault Tolerance vs Disaster Recovery

```text
High Availability
→ recover quickly from local component failures

Fault Tolerance
→ continue with little/no interruption during component failure

Disaster Recovery
→ restore service/data after site/regional/large-scale disaster
```

Example:

```text
two-node Pacemaker cluster
inside one data center
```

can improve local HA.

It is not automatically DR if the entire data center can fail.

---

## Enhanced Deep Dive 5 — Failure Domains

A fault domain is a set of components that fail together.

Examples:

```text
physical server
rack
top-of-rack switch
PDU
power circuit
hypervisor cluster
storage controller
availability zone
data center
```

Poor design:

```text
node1 VM ─┐
node2 VM ─┼→ same physical hypervisor
qdevice  ─┘
```

One hardware failure removes all three.

HA design requires independence, not just duplication.

---

## Enhanced Deep Dive 6 — Single Point of Failure Analysis

Architecture:

```text
node1 -----\
            \ 
             one switch ---- clients
            /
node2 -----/
```

Nodes are redundant.

Switch is not.

Ask for each service dependency:

```text
What single component can still stop the service?
```

Categories:

```text
compute
network
storage
power
DNS
identity
management
monitoring
fencing
```

---

## Enhanced Deep Dive 7 — Active/Passive Ownership

Typical active/passive chain:

```text
Shared block device
      ↓
LVM active on one node
      ↓
XFS mounted on one node
      ↓
VIP on same node
      ↓
Apache on same node
```

Passive node is ready but does not concurrently own unsafe storage.

Failover:

```text
old owner isolated
    ↓
LVM ownership changes
    ↓
filesystem mounts
    ↓
VIP appears
    ↓
service starts
```

---

## Enhanced Deep Dive 8 — Active/Active Is an Application and Storage Property

Two processes serving HTTP at once is easy if state is external/stateless.

Two nodes writing the same block filesystem is not.

Active/active requires all relevant layers to support concurrency:

```text
application
session model
locking
storage
filesystem
database
```

Example:

```text
XFS on one shared LUN
mounted RW by node1 and node2 independently
```

is unsafe.

Cluster filesystem such as GFS2 exists because concurrent block access requires coordinated locking.

---

## Enhanced Deep Dive 9 — Failover vs Switchover

```text
Failover
→ reaction to failure

Switchover
→ planned movement for maintenance/testing
```

Planned switchover should be cleaner:

```text
standby node
move resources
patch old active node
verify
return node
```

Use controlled switchover regularly to prove that failover architecture actually works.

---

## Enhanced Deep Dive 10 — Failure Detection Is Not Instant

Every HA system has detection timing.

Example:

```text
resource monitor every 10 s
failure occurs just after check
next check in ~10 s
timeout/failure decision
recovery starts
```

Client outage includes:

```text
detection time
+
fencing time
+
resource stop/start time
+
application warm-up
+
network neighbor update
```

This is why HA does not mean zero downtime.

---

## Enhanced Deep Dive 11 — Pacemaker as Resource Manager

Pacemaker answers:

```text
What resources exist?
Where should they run?
Which order?
What happens after failure?
What constraints apply?
When should recovery happen?
```

It is not the communication layer.

It consumes cluster membership information and manages resources.

Concept:

```text
Corosync membership
       ↓
Pacemaker scheduler
       ↓
resource actions
       ↓
resource agents
```

---

## Enhanced Deep Dive 12 — Corosync as Membership/Messaging Infrastructure

Corosync lets nodes exchange cluster messages and determine membership.

Simplified:

```text
node1
 ║
 ║ cluster communication
 ║
node2
```

Loss of communication does not automatically prove remote power loss.

That ambiguity is exactly why fencing exists.

Inspect:

```bash
pcs cluster status
corosync-cfgtool -s 2>/dev/null || true
corosync-quorumtool -s
```

---

## Enhanced Deep Dive 13 — pcs and pcsd

`pcs` is the administrative CLI.

`pcsd` supports remote authentication/management workflows used by pcs.

Examples:

```bash
pcs status
pcs cluster status
pcs resource status
pcs constraint config
pcs quorum status
pcs stonith status
```

Do not manually modify cluster internal state behind Pacemaker.

Use supported cluster interfaces.

---

## Enhanced Deep Dive 14 — CIB: Cluster Information Base

The CIB represents desired cluster configuration/state relationships.

Conceptually:

```text
CIB
├── cluster properties
├── nodes
├── resources
├── operations
├── constraints
├── fencing devices
└── defaults
```

The scheduler uses this information plus current status to calculate actions.

Think:

```text
desired cluster graph
+
observed cluster state
=
transition plan
```

---

## Enhanced Deep Dive 15 — Resource Agents and OCF Model

A resource agent exposes standardized operations such as:

```text
start
stop
monitor
validate-all
promote/demote for promotable resources
```

Discover:

```bash
pcs resource agents
pcs resource describe ocf:heartbeat:IPaddr2
```

Resource agent:

```text
does not make a broken application healthy
```

It provides Pacemaker with a consistent way to manage/monitor the application/resource.

---

## Enhanced Deep Dive 16 — Resource Monitor Operations

A resource can be healthy at start and fail later.

Monitoring repeats.

Concept:

```text
start succeeds
    ↓
monitor interval
    ↓
monitor interval
    ↓
monitor fails
    ↓
Pacemaker recovery policy
```

Parameters often include:

```text
interval
timeout
on-fail behavior
```

Do not make timeouts extremely large just to avoid failures. Diagnose the reason operations exceed expected duration.

---

## Enhanced Deep Dive 17 — Operation Timeout vs Monitor Interval

These are different.

```text
interval
→ how often to run a monitor

timeout
→ maximum time one operation may take
```

Example:

```text
monitor every 10 seconds
timeout after 20 seconds
```

A monitor operation itself can run up to its timeout.

Poor settings can delay failure detection or create false failures.

---

## Enhanced Deep Dive 18 — Cluster Properties

Important cluster behavior is influenced by properties.

Inspect:

```bash
pcs property config
```

Examples of conceptual policy include:

```text
stonith/fencing behavior
quorum policy
maintenance mode
resource stickiness defaults
```

Do not change global properties without understanding how every resource can be affected.

---

## Enhanced Deep Dive 19 — Resource Groups

Group:

```text
webgroup
├── lvm
├── filesystem
├── vip
└── apache
```

A group commonly provides:

```text
same-node placement
ordered startup
reverse ordered shutdown
```

Startup:

```text
LVM
 ↓
filesystem
 ↓
VIP
 ↓
Apache
```

Shutdown:

```text
Apache
 ↓
VIP
 ↓
filesystem
 ↓
LVM
```

This mirrors dependency direction.

---

## Enhanced Deep Dive 20 — Explicit Ordering Constraints

When resources are not grouped or need additional relationships:

```bash
pcs constraint order \
  start vip \
  then webserver
```

Order means:

```text
action A before action B
```

It does not necessarily mean both resources must be on the same node.

That is colocation.

---

## Enhanced Deep Dive 21 — Colocation Constraints

Colocation expresses placement relationship.

Example:

```text
Apache must run with filesystem
```

Concept:

```text
Filesystem on node1
        ↓
Apache must also be on node1
```

Order and colocation answer different questions:

```text
order
→ when

colocation
→ where
```

---

## Enhanced Deep Dive 22 — Location Constraints

Location constraints express preference or avoidance.

Example:

```bash
pcs constraint location \
  webserver \
  prefers node1.lab.example=100
```

Positive score:

```text
preference
```

Very strong/mandatory constraints can effectively ban/force placement.

Avoid hard constraints unless architecture truly requires them because they can prevent recovery when a preferred node is unavailable.

---

## Enhanced Deep Dive 23 — Resource Stickiness

Stickiness prefers keeping a resource where it is already running.

Failure example:

```text
normal on node1
node1 fails
resource moves node2
node1 returns
```

Question:

```text
move back immediately?
or stay on node2?
```

Immediate failback causes another outage.

Stickiness often reduces unnecessary movement.

---

## Enhanced Deep Dive 24 — Resource Move Constraints

A manual move can create temporary placement constraints.

Example:

```bash
pcs resource move webserver node2.lab.example
```

Inspect:

```bash
pcs constraint config
```

After maintenance:

```bash
pcs resource clear webserver
```

If you forget to clear the move, future placement can look mysterious.

---

## Enhanced Deep Dive 25 — Failure Counts

Resource failures can accumulate.

Inspect:

```bash
pcs resource failcount show
```

Pacemaker can use failure history to decide:

```text
retry
move resource
stop resource
fence/escalate depending on policy
```

Do not clear failure state before collecting root-cause evidence.

---

## Enhanced Deep Dive 26 — `pcs resource cleanup`

After the actual fault is fixed:

```bash
pcs resource cleanup webserver
```

Concept:

```text
root cause corrected
   ↓
cleanup failure history
   ↓
cluster re-evaluates/retries
```

Cleanup is not a repair command for:

```text
bad Apache config
missing disk
broken network
```

---

## Enhanced Deep Dive 27 — Quorum Majority Model

For an ordinary majority system:

```text
quorum requires more than half voting authority
```

Example six voting members:

```text
4 of 6
→ majority

3 of 6
→ exactly half, not majority
```

Quorum prevents two disconnected partitions from both assuming authority.

Inspect:

```bash
pcs quorum status
corosync-quorumtool -s
```

---

## Enhanced Deep Dive 28 — Split Brain

Network partition:

```text
node1   X   node2
```

Both remain powered.

Node1 observes:

```text
node2 disappeared
```

Node2 observes:

```text
node1 disappeared
```

If both start:

```text
same shared filesystem
same database ownership
same VIP
```

you can get:

```text
data corruption
duplicate IP
inconsistent state
```

Quorum and fencing solve different parts of this safety problem.

---

## Enhanced Deep Dive 29 — Why Two-Node Clusters Are Special

With two nodes:

```text
node1 cannot communicate with node2
```

Node1 cannot distinguish:

```text
node2 dead
```

from:

```text
cluster link failed
```

There is no independent majority among two equal members.

This makes correct two-node quorum/fencing design essential.

Do not weaken safety just because there are only two machines.

---

## Enhanced Deep Dive 30 — Quorum Device / qdevice Concept

External arbitration:

```text
node1 -----\
            \
             qdevice/qnetd
            /
node2 -----/
```

A quorum device participates in vote/arbitration.

It should be in an independent failure domain where possible.

Bad:

```text
node1, node2, qdevice
all on same hypervisor
```

because the "third vote" disappears with the same physical failure.

---

## Enhanced Deep Dive 31 — Quorum Is Not Fencing

Quorum answers:

```text
Which partition has authority to operate?
```

Fencing answers:

```text
Can the old/suspect node still access protected resources?
```

You may have quorum and still need to fence an unresponsive node before safely starting storage elsewhere.

---

## Enhanced Deep Dive 32 — Fencing Safety Model

Suppose node1 stops responding to cluster messages.

Unknown:

```text
powered off?
kernel hung?
network partition?
still writing storage?
still serving clients?
```

Safe transition:

```text
suspect node
   ↓
fence/isolate
   ↓
confirm isolation
   ↓
release/start protected resources elsewhere
```

This is a data-integrity mechanism, not just "restart automation."

---

## Enhanced Deep Dive 33 — Fencing Methods

Examples:

```text
IPMI/BMC power control
hypervisor API
cloud instance fencing
PDU
SBD/watchdog
storage fencing in supported designs
```

Strong fencing should be independent of the failed operating system.

If node1 kernel is frozen, running a command inside node1 is not a reliable fence mechanism.

---

## Enhanced Deep Dive 34 — Fence Agent Metadata

Before configuration:

```bash
pcs stonith list
pcs stonith describe fence_ipmilan
```

Agent parameters can include:

```text
management endpoint
credentials
target ID
power action
SSL behavior
timeouts
```

Never copy a fence configuration from another platform without reading agent metadata.

---

## Enhanced Deep Dive 35 — Node-to-Fence Target Mapping

Critical safety problem:

```text
cluster node name
must map to
correct physical/VM power target
```

Wrong mapping:

```text
fence node1
→ actually powers off node2
```

can cause a serious outage.

Before testing, document:

```text
cluster name
management IP/API
target identifier
serial/VM UUID
expected power action
```

---

## Enhanced Deep Dive 36 — Fence Test Procedure

Before actual fence:

```text
maintenance approval
lab/authorized target
correct node mapping
service impact understood
console access available
cluster healthy
logs being captured
```

During:

```text
initiate fence
observe target power state
observe cluster membership
observe resource recovery
```

After:

```text
verify node status
verify resources
verify data
verify client behavior
```

A fence test is destructive by design. Use dedicated labs/approved windows.

---

## Enhanced Deep Dive 37 — Fencing Failure Can Correctly Block Failover

Scenario:

```text
node1 disappears
fence action fails
node2 healthy
```

Cluster may refuse to start a shared-storage resource on node2.

Why?

Because node1 may still write the disk.

```text
temporary service outage
```

can be safer than:

```text
simultaneous writers
→ corruption
```

This is an essential HA principle.

---

## Enhanced Deep Dive 38 — Fencing Topology

Some environments provide multiple fence paths:

```text
Level 1:
hypervisor API

if unavailable:
Level 2:
PDU/IPMI
```

This can reduce the fencing subsystem itself becoming a single point of failure.

But every method must reliably isolate the same target.

---

## Enhanced Deep Dive 39 — Watchdog / SBD Concept

SBD can participate in fencing/watchdog-based designs.

Conceptually:

```text
cluster heartbeat/monitoring
      ↓
watchdog or shared SBD mechanism
      ↓
node self-isolates if required
```

Exact deployment is platform-specific and must follow supported Red Hat/storage/hardware guidance.

Do not implement from generic commands without understanding watchdog, shared storage, timeout, and cluster relationships.

---

## Enhanced Deep Dive 40 — Corosync Network Redundancy Awareness

Cluster communication is itself critical.

Design may include redundant Corosync links/networks depending on platform/support.

Model:

```text
node1
├── cluster link A ───── node2
└── cluster link B ───── node2
```

Goal:

```text
one link failure
≠
membership loss
```

But redundant links that use the same switch/NIC/failure domain may not be independent.

---

## Enhanced Deep Dive 41 — Service Network vs Cluster Network vs Storage Network

Conceptual separation:

```text
Client network
→ VIP/application traffic

Cluster network
→ Corosync membership

Storage network
→ iSCSI/NFS/shared storage

Management network
→ SSH/BMC/fencing
```

Benefits:

```text
fault isolation
security segmentation
capacity isolation
clearer troubleshooting
```

Exact physical separation depends on architecture.

---

## Enhanced Deep Dive 42 — Virtual IP Mechanics

Cluster VIP is added to an interface on the active node.

```text
node1 active:
physical IP + VIP

node2 passive:
physical IP only
```

Failover:

```text
remove/lose VIP on node1
add VIP on node2
```

Clients must learn the new Layer-2 neighbor mapping.

This can involve ARP/NDP update behavior.

---

## Enhanced Deep Dive 43 — Gratuitous ARP / Neighbor Update Awareness

When IPv4 VIP moves:

```text
same service IP
new MAC/interface owner
```

Clients/switches may still cache the old mapping.

HA IP resource mechanisms typically handle address announcement behavior as designed.

Troubleshooting client delay:

```text
VIP exists on node2
but some clients still fail
```

can involve:

```text
ARP/neighbor cache
switch behavior
network security
duplicate address
```

Inspect:

```bash
ip addr
ip neigh
arping --help 2>/dev/null || true
```

Do not send disruptive ARP operations on networks without authorization.

---

## Enhanced Deep Dive 44 — DNS vs VIP for Service Identity

VIP provides:

```text
same IP after node failover
```

DNS provides:

```text
name → address
```

A common design:

```text
app.example.com
   ↓ DNS
VIP
   ↓
active cluster node
```

If DNS itself is unavailable, cluster resources can be healthy while clients cannot resolve the service.

HA architecture must include dependency analysis beyond the cluster.

---

## Enhanced Deep Dive 45 — Resource Group for Active/Passive Web Service

Desired group:

```text
webgroup
├── LVM activation
├── filesystem
├── VIP
└── Apache
```

Why order?

Apache requires content filesystem.

VIP should be on the node serving Apache.

Storage should be active before filesystem mount.

Group expresses both dependency and same-node placement in a simple design.

---

## Enhanced Deep Dive 46 — LVM-activate Active/Passive Ownership

Shared LUN visible to both nodes:

```text
node1 sees VG
node2 sees VG
```

But active/passive design requires:

```text
only current owner activates/mounts data
```

Pacemaker should control activation.

Do not also configure uncontrolled boot-time activation on every node.

Cluster manager must be the authority.

---

## Enhanced Deep Dive 47 — LVM system_id Concept

LVM system ID can help associate VG activation with one system in active/passive designs.

Cluster resource agent coordinates ownership change.

Concept:

```text
VG owned/active node1
   ↓ failover
cluster-managed ownership transition
   ↓
VG active node2
```

Use current supported resource-agent/RHEL guidance for exact configuration.

---

## Enhanced Deep Dive 48 — XFS in HA

XFS is a normal local filesystem.

Safe shared-block HA model:

```text
shared LUN visible to both
BUT
XFS mounted RW on only one node at a time
```

Unsafe:

```text
node1 mounts same XFS RW
node2 mounts same XFS RW
without cluster filesystem coordination
```

This can corrupt metadata/data.

---

## Enhanced Deep Dive 49 — iSCSI Architecture

```text
Storage target
     |
storage IP network
     |
 +---+---+
 |       |
node1   node2
initiator initiator
```

Terms:

```text
target
→ storage provider

initiator
→ client

LUN
→ logical unit presented to initiators
```

Commands:

```bash
iscsiadm -m session
lsblk -f
```

Shared visibility is not the same as safe concurrent filesystem use.

---

## Enhanced Deep Dive 50 — iSCSI Discovery and Login

Lab:

```bash
sudo iscsiadm \
  -m discovery \
  -t sendtargets \
  -p storage.lab.example
```

Then:

```bash
sudo iscsiadm \
  -m node \
  --login
```

Verify:

```bash
sudo iscsiadm -m session
lsblk
```

Before any destructive action, map:

```text
target IQN
LUN ID
WWID/device identifier
size
existing filesystem/LVM
```

---

## Enhanced Deep Dive 51 — Stable Storage Identity

Device names:

```text
/dev/sdb
/dev/sdc
```

can vary.

Enterprise shared storage should be identified using stable storage identifiers.

Inspect:

```bash
lsblk -o NAME,WWN,SERIAL,SIZE,FSTYPE,MOUNTPOINTS
udevadm info --query=property --name=/dev/sdb 2>/dev/null | head -n 50 || true
```

Multipath uses stable WWID-based identification.

Never build HA storage solely around "the disk happened to be sdb today."

---

## Enhanced Deep Dive 52 — Device Mapper Multipath

Multiple storage paths:

```text
node
├── path A ── switch/controller A ── storage
└── path B ── switch/controller B ── storage
```

Multipath presents:

```text
one logical device
```

despite multiple paths.

Inspect:

```bash
multipath -ll
lsblk
```

HA benefit:

```text
one path fails
I/O continues through another path
```

if the full storage stack is correctly designed.

---

## Enhanced Deep Dive 53 — Multipath Failure Domains

Two paths do not provide true redundancy if both share:

```text
same NIC
same switch
same controller
same cable trunk
```

Path diversity should extend through independent components where required.

Draw each path end-to-end.

---

## Enhanced Deep Dive 54 — Multipath Is Not Backup

Multipath protects:

```text
path availability
```

It does not protect against:

```text
rm -rf
filesystem corruption
application writes bad data
array-wide failure
ransomware
```

HA, redundancy, and backup solve different failure classes.

---

## Enhanced Deep Dive 55 — Shared LVM with Locking

Active/active shared LVM requires coordinated locking.

Concepts include:

```text
shared VG
lvmlockd
DLM or sanlock depending on design
```

Example conceptual command from source scope:

```bash
vgcreate --shared ...
```

The point:

```text
multiple nodes can see storage
+
lock manager coordinates metadata access
```

Do not confuse with active/passive LVM ownership.

---

## Enhanced Deep Dive 56 — DLM

Distributed Lock Manager coordinates locks across cluster nodes.

Used in cluster-aware shared-storage stacks such as GFS2-related architectures.

Model:

```text
node1 asks lock
node2 asks lock
      ↓
DLM coordinates
      ↓
safe concurrent metadata/data access
```

If cluster communication/locking fails, filesystem safety mechanisms must prevent uncontrolled concurrent ownership.

---

## Enhanced Deep Dive 57 — GFS2 Architecture

GFS2 allows supported concurrent mounting by multiple cluster nodes.

Stack:

```text
shared block storage
   ↓
shared LVM / coordinated locking
   ↓
DLM
   ↓
GFS2
   ↓
node1 + node2 concurrent mount
```

This is fundamentally different from XFS active/passive.

---

## Enhanced Deep Dive 58 — GFS2 Journals

Each concurrently mounting node requires journal capacity according to design.

Example concept:

```bash
mkfs.gfs2 \
  -j 2 \
  -p lock_dlm \
  -t webcluster:sharedfs \
  /dev/vgshared/lvshared
```

Fields:

```text
-j 2
→ two journals

lock_dlm
→ distributed locking

webcluster:sharedfs
→ lock table identity
```

Use current supported sizing/growth guidance for actual deployments.

---

## Enhanced Deep Dive 59 — GFS2 Performance Is Different

Cluster filesystem performance includes:

```text
local I/O
storage latency
lock coordination
metadata contention
network/cluster communication
```

A workload that performs well on local XFS may behave differently on GFS2.

Measure:

```text
metadata-heavy workload
shared file contention
storage latency
lock contention
```

Do not choose active/active merely because it sounds more available.

---

## Enhanced Deep Dive 60 — NFS HA Dependency Chain

Highly available NFS can involve:

```text
LVM
 ↓
filesystem
 ↓
NFS server
 ↓
export
 ↓
VIP
```

Clients use stable identity:

```text
VIP:/export/path
```

Failover must preserve:

```text
export availability
storage consistency
client recovery semantics
```

NFS statefulness/version behavior must be understood for real production design.

---

## Enhanced Deep Dive 61 — Highly Available Apache

Architecture:

```text
             VIP
              |
       +------+------+
       |             |
     node1         node2
    ACTIVE         READY
       \             /
        shared content
```

Client:

```bash
curl http://VIP/
```

Failover test should measure:

```text
failed requests
time to first success
resource start sequence
data consistency
```

"pcs status green" is not the user experience.

---

## Enhanced Deep Dive 62 — Clustered Application vs Load-Balanced Application

Pacemaker active/passive:

```text
one active application owner
failover on failure
```

Load-balanced web tier:

```text
multiple active stateless nodes
load balancer distributes requests
```

Many modern web services prefer load balancing rather than clustered shared filesystem.

Choose architecture based on:

```text
application state
storage model
session model
failure requirement
maintenance pattern
```

HA clustering is not automatically the best solution for every web application.

---

## Enhanced Deep Dive 63 — Standby Mode

Before maintenance:

```bash
pcs node standby node1.lab.example
```

Cluster moves resources away.

Verify:

```bash
pcs status
```

Then perform maintenance.

Return:

```bash
pcs node unstandby node1.lab.example
```

Standby is safer than manually stopping cluster-managed services one by one.

---

## Enhanced Deep Dive 64 — Maintenance Mode

Cluster-wide maintenance:

```bash
pcs property set maintenance-mode=true
```

Pacemaker stops normal active management actions.

Use only with a precise procedure.

Risk:

```text
resource fails during maintenance
cluster may intentionally not recover it
```

Exit:

```bash
pcs property set maintenance-mode=false
```

Then verify all resources.

---

## Enhanced Deep Dive 65 — Manual systemctl on Cluster-Owned Resources

If Pacemaker owns Apache:

```text
Pacemaker expects specific state
```

Manual:

```bash
systemctl stop httpd
```

can look like a resource failure and trigger recovery.

Operational rule:

```text
cluster-owned resource
→ manage through cluster tooling
```

unless an approved maintenance procedure explicitly disables cluster management first.

---

## Enhanced Deep Dive 66 — Resource Flapping

Resource repeatedly moves:

```text
node1
 ↓ failure
node2
 ↓ failure
node1
 ↓
...
```

Investigate:

```text
monitor timeout
application crash
network instability
storage latency
constraint conflict
low stickiness
dependency problem
```

Increasing timeout is not a root-cause fix unless evidence proves legitimate operation duration exceeds the old value.

---

## Enhanced Deep Dive 67 — Cluster Communication Failure Decision Tree

```text
node disappeared
   ↓
host powered?
   ↓
Corosync service?
   ↓
cluster interface/link?
   ↓
route?
   ↓
firewall?
   ↓
Corosync config?
   ↓
packet loss/MTU?
```

Commands:

```bash
systemctl status corosync
pcs cluster status
ip -br address
ip route
ping -c 2 peer
journalctl -u corosync -b
```

Separate host/network faults from resource-agent faults.

---

## Enhanced Deep Dive 68 — Fencing Failure Decision Tree

```text
Fence action failed
   ↓
agent installed?
   ↓
management network route?
   ↓
DNS/IP?
   ↓
credentials?
   ↓
API permission?
   ↓
correct target mapping?
   ↓
device reachable?
   ↓
timeout/certificate/API behavior?
```

Test fence agent against only the authorized target and follow platform-specific safe procedures.

Do not disable fencing as a casual workaround.

---

## Enhanced Deep Dive 69 — Storage Failure Decision Tree

```text
filesystem resource fails
   ↓
LUN visible?
   ↓
multipath healthy?
   ↓
PV visible?
   ↓
VG ownership/activation?
   ↓
LV?
   ↓
filesystem?
   ↓
already mounted elsewhere?
   ↓
cluster constraint?
```

Commands:

```bash
lsblk -f
multipath -ll 2>/dev/null || true
pvs
vgs
lvs
findmnt
journalctl -b
```

Collect evidence before attempting filesystem repair.

---

## Enhanced Deep Dive 70 — VIP Conflict

If another host already uses the service VIP:

```text
duplicate address
```

Symptoms:

```text
intermittent connectivity
ARP instability
traffic reaching wrong host
```

Before creating VIP:

```text
verify address allocation
check IPAM
confirm no static host owns it
```

In a lab, use reserved isolated addressing.

---

## Enhanced Deep Dive 71 — Client-Side Failover Observation

A proper HA test includes a client loop.

Example:

```bash
while true; do
    date '+%T'
    curl \
      --max-time 2 \
      -sS \
      http://192.168.56.100/ \
      || echo FAILED
    sleep 1
done
```

Run during controlled switchover.

Measure:

```text
last success before failover
number of failures
first success after recovery
backend identity
```

Use only against your authorized lab.

---

## Enhanced Deep Dive 72 — Failure Detection vs Recovery Time

Break outage into components.

Example:

```text
failure at T0

monitor detects:
+10 s

fencing:
+20 s

storage activation:
+5 s

filesystem mount:
+2 s

application start:
+5 s

client neighbor convergence:
+2 s
```

Total approximate outage:

```text
44 s
```

This decomposition tells you where RTO improvement is possible.

---

## Enhanced Deep Dive 73 — RTO and Cluster Design

RTO:

```text
maximum targeted recovery duration
```

If required RTO is:

```text
5 seconds
```

but fencing alone takes:

```text
30 seconds
```

the architecture cannot meet the requirement.

HA design should be driven by measured recovery components.

---

## Enhanced Deep Dive 74 — RPO and Data Replication

RPO:

```text
maximum acceptable data-loss window
```

A shared-disk cluster often uses the same data, so node failover itself may not lose committed disk data.

But cluster does not protect from:

```text
corruption
accidental deletion
storage failure
malicious change
```

RPO requires:

```text
backup
replication
application consistency
```

as appropriate.

---

## Enhanced Deep Dive 75 — HA Does Not Replace Backups

Example:

```text
node1 writes bad data
shared storage contains bad data
failover to node2
node2 reads same bad data
```

Cluster worked perfectly.

Data is still bad.

Backup/recovery remains required.

---

## Enhanced Deep Dive 76 — Monitoring Cluster Health

Monitor:

```text
node membership
quorum
resource state
resource failures
fence events
Corosync link health
VIP reachability
application health
storage latency
multipath path state
filesystem capacity
CPU/memory
```

Alert on:

```text
resource degraded
fencing repeated
one storage path lost
quorum risk
node unexpectedly standby
```

Do not alert only when everything is already down.

---

## Enhanced Deep Dive 77 — Historical Metrics and PCP Awareness

A cluster incident can disappear before an engineer logs in.

Historical evidence helps answer:

```text
CPU saturation?
packet loss?
storage latency?
memory pressure?
fence delay?
```

Performance Co-Pilot and other monitoring systems can preserve time-series data.

Correlate cluster events with infrastructure metrics.

---

## Enhanced Deep Dive 78 — Rolling Maintenance

Safe conceptual process:

```text
cluster healthy
    ↓
standby node1
    ↓
resources move
    ↓
patch/reboot node1
    ↓
verify/rejoin
    ↓
standby node2
    ↓
patch/reboot node2
    ↓
verify full cluster
```

Do not remove both redundant nodes from service at once.

---

## Enhanced Deep Dive 79 — Version Compatibility During Updates

Cluster software updates can change:

```text
Pacemaker
Corosync
pcs
resource agents
kernel
storage stack
```

Rolling update procedure must follow supported version guidance.

Do not assume arbitrary mixed versions are safe indefinitely.

---

## Enhanced Deep Dive 80 — Cluster Configuration Backup

Recovery data includes more than `pcs status`.

Protect:

```text
cluster resource definitions
constraints
fencing configuration
Corosync config
application config
storage layout
certificates/secrets according to policy
DNS/network assignments
operational runbooks
```

Use supported cluster backup/export mechanisms for your installed release and maintain configuration documentation/version control.

---

## Enhanced Deep Dive 81 — Secret Management in HA

Sensitive values may include:

```text
fence BMC password
cloud API token
storage credentials
cluster admin credentials
TLS keys
```

Do not place them in:

```text
world-readable shell scripts
Git
terminal screenshots
training notes
```

Use supported secret storage/permissions and rotate when exposure is suspected.

---

## Enhanced Deep Dive 82 — Ansible for HA Node Baseline

Automation is excellent for repeated prerequisites:

```text
packages
repositories
firewall
chrony
users
configuration files
```

Example conceptual play:

```yaml
- name: Prepare HA nodes
  hosts: ha_nodes
  become: true

  tasks:
    - name: Ensure cluster packages are present
      ansible.builtin.dnf:
        name:
          - pcs
          - pacemaker
        state: present
```

Use appropriate supported repositories/collections for the actual environment.

---

## Enhanced Deep Dive 83 — RHEL HA System Role Concept

A system role can model cluster desired state.

Conceptually:

```text
inventory
+
cluster variables
+
redhat.rhel_system_roles.ha_cluster
      ↓
consistent node/cluster configuration
```

Automation benefits:

```text
repeatability
review
drift reduction
```

Risk:

```text
wrong inventory or variable
→ cluster-wide impact
```

Use lab/canary/change review.

---

## Enhanced Deep Dive 84 — Automating Fencing Safely

Fencing automation requires extreme guardrails.

Before applying:

```text
exact cluster node
exact fence target
management endpoint
credential scope
environment
platform type
```

Use assertions and explicit mapping.

Never auto-discover a "likely VM" and configure it as the fence target.

---

## Enhanced Deep Dive 85 — Cluster as a Dependency Graph

Think of service as graph:

```text
Shared storage
   ↓
LVM
   ↓
filesystem
   ↓
application
   ↓
VIP
```

Pacemaker constraints turn this architecture into executable dependency policy.

A missing dependency relationship can create:

```text
application starts before mount
VIP moves without service
filesystem mounts on wrong node
```

Diagram first, configure second.

---

## Enhanced Deep Dive 86 — State Machine Thinking

Cluster resources transition through states.

Simplified:

```text
stopped
  ↓ start
started
  ↓ monitor fail
failed
  ↓ recovery
started elsewhere
```

Some resources can have promoted/demoted roles.

Understanding state transitions helps interpret cluster logs.

---

## Enhanced Deep Dive 87 — Failure Policy vs Business Requirement

Not every resource failure should cause node fencing.

Examples:

```text
Apache config error
→ usually resource/service problem

node kernel hung with shared disk
→ node-level isolation may be required
```

Recovery policy should match failure scope.

Over-escalation creates unnecessary reboots.

Under-escalation can create unsafe ownership.

---

## Enhanced Deep Dive 88 — Avoiding False Failures

A monitor can fail because:

```text
timeout too short
temporary I/O latency
DNS dependency
status endpoint overloaded
resource agent bug
real application failure
```

Monitor design should be:

```text
specific
fast
reliable
representative of resource health
```

A health check that depends on an unrelated external Internet service can make local resources fail during an Internet outage.

---

## Enhanced Deep Dive 89 — Health Check Depth

Levels:

```text
process exists
↓
socket listening
↓
local application response
↓
dependency check
↓
end-to-end client transaction
```

Deeper checks detect more real failures but can introduce dependency coupling.

Choose a monitor that reflects what Pacemaker can safely recover.

---

## Enhanced Deep Dive 90 — Network Bonding/Redundancy Awareness

A node with one NIC can be a single point of failure.

Network redundancy can include:

```text
bonding
multiple switches
redundant routing
multiple Corosync links
```

But:

```text
two NICs
→ same switch
```

does not eliminate switch failure.

Always map the physical fault domain.

---

## Enhanced Deep Dive 91 — Power Redundancy

Compute redundancy fails if both nodes depend on one power source.

Design may include:

```text
dual PSU
separate PDU
separate circuit
UPS
generator
```

Do not claim HA solely from software clustering while ignoring infrastructure.

---

## Enhanced Deep Dive 92 — Management Plane Availability

During a cluster incident, administrators need:

```text
SSH/OOB console
BMC/hypervisor access
fence management
monitoring
logs
authentication
DNS/IPAM documentation
```

If all management paths depend on the failed production network, recovery becomes harder.

Management plane is part of HA architecture.

---

## Enhanced Deep Dive 93 — Two Nodes on Same Hypervisor

Two VMs can look redundant at OS layer:

```text
node1 VM
node2 VM
```

But if both run on one host:

```text
hypervisor failure
→ both gone
```

Use anti-affinity/placement rules where supported and required.

Verify physical placement, not only VM names.

---

## Enhanced Deep Dive 94 — Storage Array as SPOF

Multipath can protect:

```text
NIC
HBA
cable
switch
controller path
```

but one storage array can still fail completely.

Higher requirements may require:

```text
array replication
storage clustering
site replication
application replication
```

That moves beyond basic two-node shared-disk HA.

---

## Enhanced Deep Dive 95 — HA vs Database Replication

A database can provide its own replication/failover mechanisms.

Examples conceptually:

```text
primary/replica
consensus cluster
distributed database
```

Putting Pacemaker around an application with its own cluster logic requires understanding both.

Avoid two independent failover managers fighting over ownership.

---

## Enhanced Deep Dive 96 — Service-Level Validation

After failover, verify more than resource state.

```text
VIP exists?
Apache process active?
HTTP returns 200?
correct shared content?
write/read consistency?
client DNS path works?
TLS certificate correct?
```

A green cluster resource can still serve the wrong data.

---

## Enhanced Deep Dive 97 — Planned Failover Testing

A cluster that has never been failed over is unproven.

Regular authorized tests can include:

```text
standby active node
application crash
network path loss
storage path loss
node reboot
fence test
```

Measure:

```text
detection
recovery
client outage
data integrity
alerting
runbook accuracy
```

---

## Enhanced Deep Dive 98 — Chaos Testing Boundaries

Failure injection is valuable only under controlled conditions.

Before:

```text
approved lab/maintenance window
known rollback
monitoring active
business owner aware
scope isolated
```

Do not use uncontrolled production chaos as a learning exercise.

---

## Enhanced Deep Dive 99 — DR Site Boundary

Local cluster:

```text
same building
same storage
same network core
```

can fail together in a site disaster.

DR architecture can involve:

```text
remote replication
backups
secondary site
DNS/global traffic management
restore orchestration
```

HA and DR should be tested separately.

---

## Enhanced Deep Dive 100 — Final HA Design Review

For every design, answer:

```text
What fails if node1 dies?
What fails if node2 dies?
What if cluster link fails?
What if client network fails?
What if one switch fails?
What if one storage path fails?
What if storage array fails?
What if fencing API fails?
What if qdevice fails?
What if DNS fails?
What if both VMs share one hypervisor?
What if the application corrupts data?
What if the entire site fails?
What is the measured RTO?
What is the measured RPO?
```

A successful HA engineer designs around failure domains, not just cluster commands.

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Availability Calculation

Calculate availability for several outage durations and explain why service-level monitoring matters.

## Enhanced Lab 2 — Fault-Domain Diagram

Draw compute, switch, power, storage, DNS, management, and fence dependencies for your lab.

## Enhanced Lab 3 — SPOF Review

Identify at least 10 single points of failure in an intentionally simple two-node design.

## Enhanced Lab 4 — Active/Passive Diagram

Draw LVM→filesystem→VIP→Apache start and reverse stop order.

## Enhanced Lab 5 — Active/Active Safety Review

Explain why shared XFS cannot simply be mounted RW on both nodes and where GFS2 differs.

## Enhanced Lab 6 — Baseline Nodes

Record OS/kernel/time/network/storage/package state for node1/node2 before cluster creation.

## Enhanced Lab 7 — Corosync Communication

Inspect cluster links/membership and map the actual interface/path used.

## Enhanced Lab 8 — pcs/pcsd

Inspect services and authentication path; document what each component does.

## Enhanced Lab 9 — CIB Inspection

Export/read cluster configuration through supported pcs tools and identify resources, properties, constraints, and fencing.

## Enhanced Lab 10 — Resource Agent Metadata

Inspect `IPaddr2`, `Filesystem`, `LVM-activate`, and Apache resource agents.

## Enhanced Lab 11 — Monitor Interval/Timeout

Create a lab resource with explicit monitor timing and explain detection-time implications.

## Enhanced Lab 12 — Two-Node Cluster Build

Authenticate nodes, create cluster, start, inspect status and quorum.

## Enhanced Lab 13 — Quorum Observation

Record votes/quorum in normal state and after one controlled node outage.

## Enhanced Lab 14 — Split-Brain Simulation Design

Without creating unsafe shared writers, diagram what each node can observe during a communication partition.

## Enhanced Lab 15 — Quorum Device Design

Design placement for qdevice in an independent fault domain; explain poor placement examples.

## Enhanced Lab 16 — Fence Agent Research

Read metadata for your actual virtualization/BMC fence agent and document every required parameter.

## Enhanced Lab 17 — Fence Target Mapping

Create a table mapping node name→management endpoint→target ID/VM UUID.

## Enhanced Lab 18 — Fence Validation

Perform real fencing only in dedicated authorized lab; capture power state, membership, recovery.

## Enhanced Lab 19 — Fence Failure

Temporarily make fence management unreachable in a disposable lab and observe safe recovery behavior.

## Enhanced Lab 20 — Fence Topology Design

Design two independent fencing methods for a hypothetical environment.

## Enhanced Lab 21 — VIP

Create `IPaddr2`, locate active node, test from client, move active node, re-test.

## Enhanced Lab 22 — Neighbor Cache Observation

Observe VIP ownership and client ARP/neighbor table before and after controlled failover.

## Enhanced Lab 23 — Resource Group

Create safe ordered group and verify startup/shutdown sequence.

## Enhanced Lab 24 — Explicit Order vs Colocation

Create resources outside group and demonstrate difference between "when" and "where".

## Enhanced Lab 25 — Location Preference

Prefer node1 with finite score, fail node1, prove resource can still recover on node2.

## Enhanced Lab 26 — Stickiness

Fail over to node2, return node1, observe/adjust failback policy in lab.

## Enhanced Lab 27 — Manual Move

Move resource, inspect generated constraints, then clear them.

## Enhanced Lab 28 — Failure Count

Create a safe resource failure, inspect failcount, fix root cause, then cleanup.

## Enhanced Lab 29 — Cluster-Owned Service

Compare `systemctl` state with Pacemaker resource state and document why manual lifecycle is unsafe.

## Enhanced Lab 30 — Shared iSCSI LUN

Present an authorized empty LUN to both nodes and verify stable identity.

## Enhanced Lab 31 — WWID Mapping

Record `/dev` names and stable WWID/serial identity from both nodes.

## Enhanced Lab 32 — Multipath

If supported, configure two paths and inspect one logical multipath device.

## Enhanced Lab 33 — Multipath Path Failure

Fail one lab path and verify I/O remains via alternate path.

## Enhanced Lab 34 — Storage Fault Domain

Draw every HBA/NIC/switch/controller path and identify shared components.

## Enhanced Lab 35 — Active/Passive LVM

Create shared VG/LV according to supported RHEL HA guidance and let cluster manage activation.

## Enhanced Lab 36 — XFS Ownership

Verify filesystem is mounted RW on only the active owner.

## Enhanced Lab 37 — LVM Failure

Make the shared device unavailable on one node and inspect cluster/resource behavior.

## Enhanced Lab 38 — GFS2 Architecture

Draw DLM/lvmlockd/shared VG/GFS2 stack before running commands.

## Enhanced Lab 39 — GFS2 Build

If the supported lab stack exists, create GFS2 with enough journals and mount through cluster-managed design.

## Enhanced Lab 40 — GFS2 Concurrent Access

Write separate files from both authorized cluster nodes and inspect locking-aware behavior.

## Enhanced Lab 41 — NFS HA Design

Create dependency diagram for storage→filesystem→NFS→export→VIP.

## Enhanced Lab 42 — HA NFS

If lab supports it, configure a small HA NFS service and test from client.

## Enhanced Lab 43 — HA Apache

Build active/passive Apache using shared XFS, VIP, resource group.

## Enhanced Lab 44 — Client Loop

Run one-second curl loop during planned failover and measure failures/recovery.

## Enhanced Lab 45 — Detection-Time Breakdown

Record timestamps for failure, monitor detection, fence start/end, resource start, first client success.

## Enhanced Lab 46 — Apache Crash

Kill/stop the application through a controlled fault and observe resource recovery.

## Enhanced Lab 47 — Invalid Apache Config

Deploy invalid config on passive node, failover, observe why resource fails there, then repair.

## Enhanced Lab 48 — Standby Maintenance

Standby node1, patch/reboot or perform harmless maintenance, return node, verify.

## Enhanced Lab 49 — Rolling Maintenance

Repeat on both nodes one at a time while client monitor runs.

## Enhanced Lab 50 — Maintenance Mode

Enter maintenance mode in lab, create a safe resource-state change, observe lack of normal recovery, exit and verify.

## Enhanced Lab 51 — Corosync Failure

Stop Corosync or isolate cluster communication in a disposable lab and observe membership/quorum/fencing consequences.

## Enhanced Lab 52 — Client Network Failure

Break only service network while cluster communication remains healthy and analyze service impact.

## Enhanced Lab 53 — Cluster Network Failure

Break only cluster link in lab and analyze safety behavior.

## Enhanced Lab 54 — Storage Path Failure

Fail one multipath path and distinguish path HA from node failover.

## Enhanced Lab 55 — Storage Array Failure Design

Document why multipath cannot survive total array loss and propose higher-level protection.

## Enhanced Lab 56 — VIP Conflict

Create a safe duplicate-address condition in an isolated lab and observe symptoms.

## Enhanced Lab 57 — Resource Flapping

Create intermittent health failure and analyze failcount/stickiness/monitor timing.

## Enhanced Lab 58 — Monitoring Dashboard Design

Define metrics/alerts for membership, quorum, resources, fencing, storage paths, VIP, HTTP health.

## Enhanced Lab 59 — Historical Incident Correlation

Use synthetic timestamps to correlate CPU/storage/network events with cluster resource failure.

## Enhanced Lab 60 — Backup Package

Create a recovery documentation bundle covering cluster config, storage layout, application config, fencing, DNS, certificates, runbooks.

## Enhanced Lab 61 — RPO/RTO

Define target RPO/RTO for the lab service and compare with measured failover.

## Enhanced Lab 62 — HA vs DR Design

Draw local HA cluster plus remote DR site and identify which failures each covers.

## Enhanced Lab 63 — Ansible Baseline

Automate packages, chrony, firewall, and lab prerequisites across both nodes.

## Enhanced Lab 64 — HA Role Design

Design variables/inventory for a supported HA system role; validate in lab only.

## Enhanced Lab 65 — Fencing Automation Guardrails

Add assertions mapping each node to exact authorized fence target.

## Enhanced Lab 66 — Same-Hypervisor Failure Domain

If using VMs, document actual hypervisor placement and how anti-affinity would improve resilience.

## Enhanced Lab 67 — Power Failure Domain

Draw PSU/PDU/UPS dependencies for a hypothetical physical cluster.

## Enhanced Lab 68 — DNS Failure

Break lab DNS while VIP/service stay healthy and prove user impact lies outside Pacemaker.

## Enhanced Lab 69 — Management Plane Failure

Simulate loss of SSH but preserve console/fence access; document recovery path.

## Enhanced Lab 70 — Full Failure Injection Challenge

Inject at least 20 controlled faults across:

```text
resource
node
Corosync
quorum
fencing
VIP
storage
multipath
LVM
filesystem
Apache
DNS
management
```

For each:

```text
symptom
cluster status
user-visible effect
evidence
root cause
safe recovery
verification
prevention
```



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — HA Node Preparation

1. Create node1 and node2.
2. Configure stable hostnames.
3. Configure name resolution.
4. Verify time synchronization.
5. Install required cluster packages.
6. Configure HA firewalld service.
7. Set `hacluster` passwords.

### Lab 2 — Create Cluster

1. Authenticate both hosts with `pcs host auth`.
2. Run `pcs cluster setup`.
3. Start cluster.
4. Enable services if appropriate in the lab.
5. Verify status.
6. Inspect quorum.

### Lab 3 — Virtual IP

1. Create an `IPaddr2` resource.
2. Determine active node.
3. Verify VIP with `ip address`.
4. Curl or ping VIP from client.
5. Move/standby active node.
6. Verify VIP moves.

### Lab 4 — Fencing Design

1. Identify the fence agent supported by your virtualization/lab platform.
2. Read `pcs stonith describe`.
3. Map each cluster node to the correct fence target.
4. Create fence resources.
5. Verify configuration.
6. Perform a real fence test **only in a dedicated authorized lab**.
7. Document observed failover.

### Lab 5 — Resource Group

1. Prepare a test resource chain.
2. Create VIP.
3. Create Apache resource.
4. Add them to a group or group-compatible design.
5. Verify same-node placement.
6. Stop/restart through cluster management.

### Lab 6 — Shared LVM/XFS

1. Provide a shared lab LUN visible to both nodes.
2. Confirm device identity.
3. Create the active/passive LVM layout according to current RHEL HA guidance.
4. Create XFS.
5. Let Pacemaker manage activation/mount.
6. Verify it is not active read-write on both nodes simultaneously.

### Lab 7 — Active/Passive Apache

1. Place web content on cluster-managed storage.
2. Configure Apache on both nodes.
3. Configure LVM, Filesystem, VIP, and Apache resources.
4. Group them.
5. Test from client.
6. Standby active node.
7. Measure failover behavior.

### Lab 8 — Constraints

1. Add a node preference.
2. Inspect constraint config.
3. Test resource placement.
4. Add/remove a temporary move.
5. Clear temporary constraint.
6. Explain stickiness vs preference.

### Lab 9 — Quorum Failure

1. Use a disposable lab.
2. Observe quorum in normal state.
3. Stop cluster communication/node according to your simulator.
4. Observe quorum behavior.
5. Do not force unsafe data resources.
6. Restore cluster and verify.

### Lab 10 — iSCSI

1. Configure an authorized lab target.
2. Discover target.
3. Log in from both nodes.
4. Confirm shared LUN visibility.
5. Record WWID/device identity.
6. Do not create filesystems until identity is verified.

### Lab 11 — Multipath

1. Build two storage paths if lab supports it.
2. Configure multipath using vendor/RHEL guidance.
3. Inspect with `multipath -ll`.
4. Fail one path.
5. Verify I/O path remains available.
6. Restore path.

### Lab 12 — GFS2 Concept Lab

Only if your environment supports the required cluster locking/shared-storage stack:

1. Configure shared VG.
2. Configure required locking components.
3. Create shared LV.
4. Format GFS2 with enough journals.
5. Mount through the supported cluster design.
6. Verify multi-node access.
7. Never substitute XFS for GFS2 in concurrent-mount tests.

### Lab 13 — Cluster Maintenance

1. Put node1 in standby.
2. Verify resources evacuate.
3. Perform a harmless maintenance task.
4. Return node.
5. Verify cluster.
6. Repeat with node2.
7. Document rolling-maintenance logic.

### Lab 14 — Troubleshooting Challenge

Inject safe failures one at a time:

1. Apache syntax error.
2. missing shared-storage path.
3. stopped Corosync.
4. firewall communication error in a disposable lab.
5. incorrect location preference.
6. failed application resource.
7. unavailable fence management path.
8. VIP conflict.

For each:

```text
Symptom
Cluster state
Resource state
Evidence
Root cause
Safe corrective action
Verification
```

---

## 6. Mini Project

# Mini Project — Highly Available Apache Service

Build:

```text
                    Client
                      |
              VIP 192.168.56.100
                      |
             +--------+--------+
             |                 |
           node1             node2
             \                 /
              \               /
               Shared Storage
```

Optional infrastructure:

```text
         fence management
          /           \
       node1          node2

storage:
iSCSI / multipath lab
```

## Cluster Requirements

Cluster:

```text
webcluster
```

Nodes:

```text
node1.lab.example
node2.lab.example
```

Verify:

```bash
pcs status
pcs quorum status
pcs stonith status
```

## Fencing

Use a real supported lab fence mechanism if possible.

Document:

```text
Fence agent:
Management endpoint:
Node-to-target mapping:
Test procedure:
Observed result:
```

## Shared Storage

Create an active/passive shared LVM/XFS design.

Resources conceptually:

```text
LVM-activate
Filesystem
VIP
Apache
```

Group:

```text
webgroup
```

## Apache

Both nodes:

- same Apache package/config
- same SELinux/firewalld policy
- health/status endpoint as required by resource agent
- shared site data

Client tests:

```bash
curl http://192.168.56.100/
```

## Failover Tests

Test in an authorized lab:

1. put active node in standby
2. stop Apache unexpectedly
3. disconnect one service-network interface if safe
4. simulate shared-storage path failure
5. perform fencing test
6. reboot active node
7. remove one node from service for maintenance

Measure:

```text
failure detection time
fencing time
resource start time
client-visible outage
data consistency
```

## Documentation

Create:

```text
ARCHITECTURE.md
FAULT_DOMAINS.md
CLUSTER_BUILD.md
FENCING.md
QUORUM.md
STORAGE.md
RESOURCES.md
CONSTRAINTS.md
FAILOVER_TESTS.md
MAINTENANCE.md
TROUBLESHOOTING.md
BACKUP_AND_RECOVERY.md
```

## Design Review

Answer:

```text
What happens if one node fails?
What happens if cluster network fails?
What happens if client network fails?
What happens if one switch fails?
What happens if storage path fails?
What happens if storage array fails?
What happens if fencing fails?
What happens if DNS fails?
What happens if both nodes are on one hypervisor?
What is still a single point of failure?
```

This review is more important than merely getting `pcs status` to show green.

---


# Expanded Capstone — Highly Available Web Service with Shared Storage

Build:

```text
                         client01
                            |
                            | HTTP/HTTPS
                            v
                    VIP 192.168.56.100
                            |
                 +----------+----------+
                 |                     |
               node1                 node2
              ACTIVE                 READY
                 \                     /
                  \                   /
                   shared storage
                  /             \
             path A             path B
```

Optional management:

```text
node1 BMC/VM API
node2 BMC/VM API
      ↓
fencing
```

Optional arbitration:

```text
qdevice/qnetd
```

## Required Architecture Documentation

```text
ARCHITECTURE.md
FAULT_DOMAINS.md
NETWORKS.md
QUORUM.md
FENCING.md
STORAGE.md
LVM_AND_FILESYSTEM.md
RESOURCES.md
CONSTRAINTS.md
MONITORING.md
MAINTENANCE.md
FAILOVER_TESTS.md
RPO_RTO.md
BACKUP_RECOVERY.md
DR_BOUNDARY.md
```

## Node Baseline

Both nodes must have:

```text
stable names
time sync
consistent packages/config
HA packages
firewall policy
storage visibility
Apache configuration
```

## Cluster

Create and verify:

```text
webcluster
node1
node2
```

Record:

```bash
pcs status
pcs cluster status
pcs quorum status
pcs stonith status
pcs resource status
pcs constraint config
```

## Fencing

Use a real supported fence mechanism only in an authorized lab.

Document:

```text
agent
management network
node→target mapping
credentials scope
test procedure
observed power action
cluster response
```

## Storage

Preferred active/passive lab stack:

```text
iSCSI shared LUN
   ↓
multipath if supported
   ↓
LVM
   ↓
XFS
   ↓
cluster-managed mount
```

Verify:

```text
one active filesystem owner at a time
stable device identity
no manual autoactivation conflicts
```

## Resource Group

Conceptual order:

```text
LVM-activate
     ↓
Filesystem
     ↓
VIP
     ↓
Apache
```

Group them or implement equivalent safe constraints.

## Client Validation

Run:

```bash
while true; do
    printf '%s ' "$(date '+%T')"
    curl \
      --max-time 2 \
      -sS \
      http://192.168.56.100/ \
      || echo FAILED
    sleep 1
done
```

The page should identify the active node if practical.

## Mandatory Failure Tests

At least 25:

```text
planned standby
active Apache crash
invalid Apache configuration
node reboot
node power fence
cluster communication loss
service-network loss
VIP conflict
fence management network loss
wrong fence target mapping simulation/document review
one storage path loss
all storage paths loss
LUN unavailable on passive node
VG activation failure
filesystem mount failure
full filesystem simulation
resource monitor timeout
resource flapping
manual move constraint forgotten
qdevice unavailable
DNS failure
management SSH failure
one switch failure design review
both VMs same-hypervisor review
storage-array total-failure review
```

For each capture:

```text
T0 failure time
T1 detection
T2 fencing completed if applicable
T3 resources started
T4 first successful client request

user-visible outage
data-integrity result
alerts
root cause
recovery
preventive action
```

## Final Design Review

Answer explicitly:

```text
Does node failure recover?
Does network-link failure recover?
Does Corosync network failure remain safe?
Does client network have redundancy?
Does fencing have redundancy?
Does storage have path redundancy?
Does storage array remain a SPOF?
Are nodes in separate hypervisor/rack/power domains?
What happens if qdevice fails?
What happens if DNS fails?
What happens if the whole site fails?
What is measured RTO?
What is target RPO?
Where are backups?
How is DR performed?
```


## 7. Recommended Resources

Prioritize:

- Red Hat Enterprise Linux 10 — Configuring and managing high availability clusters.
- Red Hat Enterprise Linux 10 — LVM shared-storage documentation.
- Red Hat High Availability Clustering training outline.
- `pcs` manual and built-in help.
- Pacemaker and resource-agent documentation available on the system.
- Red Hat GFS2 documentation.
- Red Hat iSCSI and Device Mapper Multipath documentation.
- Red Hat HA system-role documentation for automation.

Useful discovery commands:

```bash
pcs -h
pcs resource agents
pcs resource describe <agent>
pcs stonith list
pcs stonith describe <agent>
man pcs
```

---

## 8. Certification Relevance

Red Hat's High Availability training and certification path focuses on implementing HA services using the Red Hat High Availability Add-On.

The training scope includes:

- Pacemaker cluster deployment
- quorum and node management
- fencing
- cluster resources
- troubleshooting
- two-node clusters
- iSCSI
- multipath
- LVM
- GFS2
- eliminating single points of failure

The skills are valuable for:

- senior Linux administration
- enterprise infrastructure
- SAP/high-availability environments
- database/application service clusters
- private cloud
- critical web services
- storage engineering
- disaster-recovery architecture

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Calling two servers a cluster before defining failover behavior.  
  **Best practice:** Define service identity, health checks, dependencies, quorum, and fencing.

- **Mistake:** Disabling fencing to make failover easier.  
  **Best practice:** Fix fencing; data integrity depends on safe node isolation.

- **Mistake:** Mounting ordinary XFS read-write from two cluster nodes simultaneously.  
  **Best practice:** Use active/passive ownership or an appropriate cluster filesystem such as GFS2 for supported concurrent access.

- **Mistake:** Testing `pvcreate` on an uncertain shared LUN.  
  **Best practice:** Verify device identity from every node first.

- **Mistake:** Assuming node redundancy means service redundancy.  
  **Best practice:** Analyze DNS, network, power, storage, firewall, and application dependencies.

- **Mistake:** Cleaning a failed resource before finding root cause.  
  **Best practice:** Diagnose first, correct, then clean/recheck.

- **Mistake:** Using manual service start/stop outside Pacemaker for cluster-owned resources.  
  **Best practice:** Let the cluster resource manager own lifecycle unless an approved maintenance procedure says otherwise.

- **Mistake:** Updating all cluster nodes simultaneously.  
  **Best practice:** Use a controlled rolling-maintenance process.

- **Mistake:** Assuming HA replaces backups.  
  **Best practice:** HA improves availability; backups/replication protect data recovery.

- **Mistake:** Putting all redundant VMs on one physical host.  
  **Best practice:** Separate failure domains according to the availability objective.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What does high availability try to achieve?

**Short answer:** Keep or restore service availability quickly despite component failures.

### Q2. What is Pacemaker?

**Short answer:** The cluster resource manager.

### Q3. What is Corosync?

**Short answer:** Cluster communication and membership infrastructure.

### Q4. What is `pcs`?

**Short answer:** The primary command-line interface for configuring and managing Red Hat Pacemaker clusters.

### Q5. What is quorum?

**Short answer:** A voting mechanism ensuring only a sufficiently authoritative cluster partition operates protected resources.

### Q6. What is split brain?

**Short answer:** Disconnected cluster partitions independently act as owners, risking conflicting resource/data access.

### Q7. Why is fencing necessary?

**Short answer:** To guarantee an unresponsive node cannot continue accessing protected resources before failover.

### Q8. What is STONITH?

**Short answer:** The traditional term for node fencing.

### Q9. What is an `IPaddr2` resource?

**Short answer:** A cluster-managed virtual IP resource agent.

### Q10. What is a resource group?

**Short answer:** A set of colocated resources with ordered start and reverse stop behavior.

### Q11. Why use `LVM-activate`?

**Short answer:** To let the cluster safely control LVM activation for shared-storage HA designs.

### Q12. What is resource stickiness?

**Short answer:** A preference that discourages unnecessary movement from the current node.

### Q13. What does standby mode do?

**Short answer:** Moves/keeps cluster resources away from a node for maintenance.

### Q14. What does maintenance mode do?

**Short answer:** Temporarily suspends normal cluster resource management actions for controlled maintenance.

### Q15. What is a quorum device?

**Short answer:** An external arbitration component that contributes to quorum decisions.

### Q16. What does multipath protect against?

**Short answer:** Failure of an individual storage access path.

### Q17. What is GFS2?

**Short answer:** A Red Hat clustered filesystem designed for coordinated concurrent access from multiple cluster nodes.

### Q18. Does HA replace backup?

**Short answer:** No.

### Q19. What is RTO?

**Short answer:** Maximum targeted service recovery time.

### Q20. What is RPO?

**Short answer:** Maximum targeted acceptable data-loss window.

### Q21. What is the most important HA design question?

**Short answer:** What happens to the complete service when each dependency or failure domain fails?

---


# Enhanced Self-Assessment Bank

### Q1. Availability belongs to what?
**Answer:** The service consumed by users, not merely server uptime.

### Q2. HA vs fault tolerance?
**Answer:** HA recovers rapidly and may have interruption; fault tolerance aims for continued operation with little/no interruption.

### Q3. HA vs DR?
**Answer:** HA handles local component failure; DR addresses site/regional/large-scale recovery.

### Q4. What is a fault domain?
**Answer:** Components affected by one common failure.

### Q5. What is a SPOF?
**Answer:** One component whose failure removes the service.

### Q6. Active/passive?
**Answer:** One node owns/runs the protected resource while another waits to take over.

### Q7. Active/active?
**Answer:** Multiple nodes provide the service concurrently using applications/storage designed for concurrency.

### Q8. Why cannot ordinary XFS be mounted RW from two independent cluster nodes on same shared block device?
**Answer:** It lacks clustered concurrent-write coordination and can corrupt data.

### Q9. What is failover?
**Answer:** Unplanned recovery to another node after failure.

### Q10. What is switchover?
**Answer:** Planned movement for maintenance/testing.

### Q11. Why does failover take time?
**Answer:** Detection, quorum/fencing, resource activation, application start, and network convergence all consume time.

### Q12. What is Pacemaker?
**Answer:** Cluster resource manager/scheduler.

### Q13. What is Corosync?
**Answer:** Cluster communication and membership infrastructure.

### Q14. What is pcs?
**Answer:** CLI for configuring/managing the Red Hat HA stack.

### Q15. What is CIB?
**Answer:** Cluster Information Base containing cluster configuration/state relationships.

### Q16. What is a resource agent?
**Answer:** Standardized script/agent implementing start/stop/monitor/other operations for a resource.

### Q17. Monitor interval vs timeout?
**Answer:** Interval is how often operation runs; timeout is maximum duration allowed for one operation.

### Q18. What is a resource group?
**Answer:** Ordered, colocated collection of resources.

### Q19. Order vs colocation?
**Answer:** Order controls when; colocation controls where.

### Q20. Location constraint?
**Answer:** Placement preference/avoidance for nodes.

### Q21. Stickiness?
**Answer:** Preference to keep a resource on its current node.

### Q22. Why clear manual move?
**Answer:** Move creates placement policy that can keep affecting future scheduling.

### Q23. Failcount?
**Answer:** Recorded resource failure history used in recovery decisions.

### Q24. Does cleanup fix a broken resource?
**Answer:** No; fix root cause first, then cleanup failure state.

### Q25. What is quorum?
**Answer:** Mechanism determining which cluster partition has enough voting authority to operate protected resources.

### Q26. Split brain?
**Answer:** Disconnected partitions act independently, risking conflicting resource/data ownership.

### Q27. Why are two-node clusters special?
**Answer:** A communication loss creates 50/50 ambiguity without independent majority.

### Q28. What is qdevice?
**Answer:** External quorum arbitration component.

### Q29. Is quorum the same as fencing?
**Answer:** No.

### Q30. Why fencing?
**Answer:** Guarantee suspect node cannot continue accessing protected resources before failover.

### Q31. Good fencing property?
**Answer:** Independent of the failed operating system and accurately maps to the target node.

### Q32. Why can failed fencing block failover?
**Answer:** Starting shared resources elsewhere may risk simultaneous ownership/data corruption.

### Q33. What is fence topology?
**Answer:** Multiple ordered fencing methods/levels for resilience.

### Q34. What is SBD conceptually?
**Answer:** Watchdog/storage-assisted fencing mechanism in supported designs.

### Q35. Why redundant Corosync links?
**Answer:** Reduce membership loss from one cluster-network path failure.

### Q36. Service network vs cluster network?
**Answer:** Client application traffic vs cluster membership/control communication.

### Q37. Storage network?
**Answer:** Network carrying iSCSI/NFS/storage traffic.

### Q38. VIP?
**Answer:** Cluster-managed service IP that moves between nodes.

### Q39. Why can ARP matter after VIP failover?
**Answer:** Clients/switches may cache old IP-to-MAC mapping.

### Q40. Why does DNS still matter with VIP?
**Answer:** Clients commonly need DNS to find the VIP.

### Q41. What should a web resource group order be?
**Answer:** Storage activation → filesystem → VIP → Apache, with reverse stop order.

### Q42. Why cluster-manage LVM activation?
**Answer:** Prevent uncontrolled simultaneous active/passive ownership.

### Q43. What is LVM system ID used for conceptually?
**Answer:** Support controlled VG ownership/activation in active/passive designs.

### Q44. What is iSCSI?
**Answer:** SCSI block storage transported over IP.

### Q45. Initiator?
**Answer:** iSCSI client.

### Q46. Target?
**Answer:** iSCSI storage provider.

### Q47. Why stable WWID?
**Answer:** Device names can change; stable identity prevents operating on wrong LUN.

### Q48. What is multipath?
**Answer:** One logical block device backed by multiple storage paths.

### Q49. Does multipath protect against array-wide failure?
**Answer:** No.

### Q50. Does multipath replace backup?
**Answer:** No.

### Q51. Shared LVM?
**Answer:** LVM designed for coordinated multi-node access using lock management in supported designs.

### Q52. What is DLM?
**Answer:** Distributed Lock Manager coordinating cluster locks.

### Q53. What is GFS2?
**Answer:** Cluster filesystem supporting coordinated concurrent access from multiple nodes.

### Q54. GFS2 vs XFS?
**Answer:** GFS2 is cluster-aware for concurrent mounts; XFS is normally active/passive on shared block storage.

### Q55. Why GFS2 journals?
**Answer:** Provide per-mounting-node journaling requirements for clustered filesystem operation.

### Q56. Does active/active always improve performance/availability?
**Answer:** No; coordination/locking and application architecture can add complexity.

### Q57. Standby mode?
**Answer:** Evacuates/keeps cluster resources away from a node for maintenance.

### Q58. Maintenance mode?
**Answer:** Suspends normal cluster resource management actions for controlled work.

### Q59. Why not manually stop Pacemaker-owned Apache?
**Answer:** Pacemaker can interpret that as failure and recover/move it.

### Q60. Resource flapping?
**Answer:** Repeated failures/movements between nodes.

### Q61. First cluster communication checks?
**Answer:** Host power, Corosync, interface/link, route, firewall, configuration/logs.

### Q62. First fencing failure checks?
**Answer:** Agent, management route, credentials/API, target mapping, device state/timeouts.

### Q63. Storage failure layers?
**Answer:** LUN → multipath → PV/VG/LV → filesystem → mount/ownership.

### Q64. What is VIP conflict?
**Answer:** Another host uses the same service IP, causing duplicate-address behavior.

### Q65. Why test from client during failover?
**Answer:** Measure real user-visible outage, not just cluster internal state.

### Q66. What contributes to RTO?
**Answer:** Detection, fencing, resource activation, application startup, network/client convergence.

### Q67. What is RTO?
**Answer:** Target maximum recovery time.

### Q68. What is RPO?
**Answer:** Target maximum acceptable data-loss window.

### Q69. Does HA guarantee RPO?
**Answer:** No.

### Q70. Why backup if shared disk is highly available?
**Answer:** Cluster does not protect from corruption, deletion, or malicious changes.

### Q71. What should cluster monitoring include?
**Answer:** Membership, quorum, resources, fencing, network/storage health, VIP/application response.

### Q72. Why historical metrics?
**Answer:** Cluster incident conditions may disappear before investigation.

### Q73. Why rolling maintenance?
**Answer:** Preserve redundancy while updating one node at a time.

### Q74. Why version compatibility matters?
**Answer:** Mixed cluster component versions may have support/behavior constraints.

### Q75. What belongs in cluster backup documentation?
**Answer:** Cluster config, constraints, fencing, app config, storage, DNS/network, secrets/certs, runbooks.

### Q76. Why protect fence credentials?
**Answer:** They can power off/reset infrastructure.

### Q77. Why automate node baseline?
**Answer:** Reduce configuration drift.

### Q78. Main risk of HA automation?
**Answer:** Wrong inventory/variables can affect the whole cluster quickly.

### Q79. Why diagram dependencies before configuring resources?
**Answer:** Constraints must represent the real service dependency graph.

### Q80. What is state-machine thinking?
**Answer:** Understand stopped/started/failed/recovered transitions and cluster actions.

### Q81. Should every app failure fence the node?
**Answer:** No; recovery policy should match failure scope.

### Q82. Why false monitor failures are dangerous?
**Answer:** They can trigger unnecessary failover/fencing.

### Q83. Health check depth trade-off?
**Answer:** Deeper checks reflect user service better but add dependency coupling and failure modes.

### Q84. Two NICs on one switch fully redundant?
**Answer:** No.

### Q85. Why power design matters?
**Answer:** Shared power can remove all redundant nodes.

### Q86. What is management-plane resilience?
**Answer:** Maintaining console/fencing/monitoring/admin access during service failures.

### Q87. Two VMs on one hypervisor fully HA?
**Answer:** No; hypervisor remains common failure domain.

### Q88. Can multipath remove storage-array SPOF?
**Answer:** Not necessarily; it mainly protects access paths.

### Q89. Why can app-native cluster conflict with Pacemaker?
**Answer:** Two independent failover managers can fight over ownership.

### Q90. What should be verified after failover?
**Answer:** VIP, application health, correct data, storage ownership, client access.

### Q91. Why planned failover tests?
**Answer:** Prove architecture/runbooks and measure actual recovery.

### Q92. Failure injection requirement?
**Answer:** Authorized, isolated, monitored, rollback-ready environment.

### Q93. Local HA equals site DR?
**Answer:** No.

### Q94. Most important HA design question?
**Answer:** What happens to the complete service when every dependency/failure domain fails?


## Completion Checklist

- [ ] I can explain Pacemaker, Corosync, pcs, pcsd, CIB, and resource agents.
- [ ] I can create and inspect a basic two-node cluster in a lab.
- [ ] I understand quorum and split brain.
- [ ] I understand why fencing is mandatory for safe failover.
- [ ] I can create basic VIP and service resources.
- [ ] I understand resource groups and constraints.
- [ ] I can use standby, move, cleanup, and maintenance workflows safely.
- [ ] I can explain iSCSI and multipath roles in HA storage.
- [ ] I understand active/passive LVM vs shared LVM.
- [ ] I understand why GFS2 exists.
- [ ] I can troubleshoot cluster, application, storage, quorum, and fencing failures by layer.
- [ ] I can identify remaining single points of failure in an HA architecture.
- [ ] I completed all labs and the highly available Apache mini project.
