# 40. VMware NSX

> Phase 9 — Virtualization

This course builds on Course 39 and moves from **virtual compute** into **software-defined networking and distributed security**.

**Current reference baseline:** VMware NSX **9.1** within the VMware Cloud Foundation 9.1 documentation family.

Current Broadcom documentation uses **NSX** for the networking platform and **VMware vDefend** branding for several security capabilities such as Distributed Firewall. This course teaches the underlying architecture so that both names make sense.

The most important idea is:

```text
Traditional Data Center
=======================

VM
 |
Physical VLAN
 |
Physical Switch
 |
Physical Router
 |
Physical Firewall


NSX Model
=========

VM
 |
Logical Segment
 |
Distributed Switching / Routing / Firewall
 |
Overlay
 |
Physical IP Fabric
```

NSX does not eliminate the physical network. Instead:

```text
Physical Network
    provides IP transport

NSX
    creates logical networks,
    routing,
    security,
    and services
    in software
```

The core mental model is:

```text
Management Plane
      |
      v
NSX Manager Cluster
      |
      v
Control / Policy State
      |
      +-------------------------+
      |                         |
      v                         v
Host Transport Nodes        Edge Transport Nodes
      |                         |
Distributed Data Plane      Centralized Services
      |                         |
Segments / DFW             T0 / T1 Services
      |                         |
VM Workloads               Physical Network
```

Throughout the course:

```text
Concept
   ↓
ASCII Architecture
   ↓
GUI / CLI / REST Example
   ↓
Packet Walk
   ↓
Security Use Case
   ↓
Failure Scenario
   ↓
Troubleshooting
```

---

## 1. Topic Title

**VMware NSX**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain why network virtualization exists.
- Explain NSX management, control, and data-plane architecture.
- Explain NSX Manager cluster responsibilities.
- Explain transport nodes and transport-node profiles.
- Explain host transport nodes versus Edge transport nodes.
- Explain overlay and VLAN transport zones.
- Explain Tunnel Endpoints (TEPs).
- Explain GENEVE overlay encapsulation.
- Explain why the physical underlay still needs correct IP routing and MTU.
- Explain NSX segments and segment ports.
- Differentiate overlay segments and VLAN-backed segments.
- Explain logical switching and distributed routing.
- Explain Tier-0 and Tier-1 gateways.
- Explain distributed-router and service-router concepts.
- Explain North-South and East-West packet flows.
- Explain Tier-0 uplinks and external VLAN segments.
- Explain static routing and BGP fundamentals in NSX.
- Explain ECMP and Tier-0 high-availability concepts.
- Explain Edge clusters and centralized services.
- Explain NAT, DHCP, and DNS forwarding fundamentals.
- Explain distributed firewall and gateway firewall architecture.
- Explain micro-segmentation and application-centric policy.
- Build dynamic groups using tags.
- Explain rule precedence, scope, logging, and stateful inspection.
- Explain default-deny and ring-fencing strategies.
- Explain NSX Projects/VPC fundamentals and multi-tenancy.
- Explain NSX Federation fundamentals.
- Explain VPN concepts including IPsec.
- Explain Kubernetes/Antrea integration at a fundamentals level.
- Explain NSX REST and Policy API concepts.
- Use safe REST examples in a lab.
- Explain NSX Manager backup/restore and lifecycle considerations.
- Monitor managers, hosts, Edges, tunnels, routing, and firewall state.
- Troubleshoot TEP, overlay, routing, BGP, NAT, DFW, and Edge failures systematically.
- Build a complete segmented enterprise network mini project.

---

## 3. Prerequisites

Required:

- Networking courses 16–19
- 38. Virtualization Fundamentals
- 39. VMware vSphere: Install, Configure and Manage
- VLANs and subnetting
- static routing and BGP
- firewall fundamentals
- vSphere distributed switching
- Linux/CLI fundamentals

Recommended lab:

```text
                             vCenter
                                |
                     +----------+----------+
                     |                     |
                   ESX01                 ESX02
                     |                     |
                     +------ vDS ----------+
                             |
                        NSX Manager
                             |
                     +-------+-------+
                     |               |
                  Edge01           Edge02
                     |               |
                     +------ Edge Cluster
                             |
                    Physical Router / FRR
```

Suggested networks:

```text
Management: 10.10.10.0/24
Host TEP:   10.10.20.0/24
Edge TEP:   10.10.21.0/24
T0 Uplink A:10.10.30.0/30
T0 Uplink B:10.10.31.0/30
WEB:        172.16.10.0/24
APP:        172.16.20.0/24
DB:         172.16.30.0/24
```

---

## 4. Core Concepts Explanation

# Part 1 — Why Network Virtualization Exists

Traditional provisioning often requires multiple physical changes:

```text
Create VLAN
   ↓
Configure switch trunks
   ↓
Configure router/SVI
   ↓
Configure firewall
   ↓
Coordinate several teams
```

Virtual compute can provision a VM in minutes, so networking became a bottleneck. NSX expresses much of the network as software objects:

```text
API / Policy
   ↓
Segment
   ↓
Gateway
   ↓
Firewall Policy
```

This makes network/security lifecycle closer to application lifecycle.

# Part 2 — Underlay vs Overlay

Underlay is the physical IP network. Overlay is the logical network created above it.

```text
VM A
 |
Overlay Segment
 |
TEP A
 |==============================|
 |      Physical Underlay        |
 |==============================|
                              TEP B
                                |
                          Overlay Segment
                                |
                              VM B
```

# Part 3 — The Underlay Still Matters

The underlay provides:

```text
Ethernet
IP routing
MTU
link redundancy
bandwidth
ECMP
failure-domain isolation
```

NSX cannot fix a broken switch, wrong VLAN, missing route, or packet-loss problem in the physical fabric.

# Part 4 — Overlay Independence

Example:

```text
Host A                   Host B
VM1                      VM2
172.16.10.11             172.16.10.12
 |                        |
 +------ SEG-WEB ---------+
```

The hosts can be attached to different physical leaf switches while the VMs remain in one logical Layer-2 segment.

# Part 5 — Management, Control, and Data Planes

Use this mental model:

```text
Management / Policy Plane
    defines desired state

Control Plane
    distributes forwarding/security state

Data Plane
    forwards packets
```

This distinction becomes important during failures: management can be degraded while previously programmed data-plane forwarding continues.

# Part 6 — NSX Manager

NSX Manager provides:

```text
UI
API
policy objects
fabric inventory
network configuration
security configuration
system health
```

# Part 7 — NSX Manager Cluster

Production designs normally use multiple manager nodes:

```text
Manager 1
Manager 2
Manager 3
   |
Cluster
```

The cluster provides management/control-plane resilience. Exact node count, sizing, and quorum requirements must match the deployed release.

# Part 8 — What Happens if One Manager Fails?

A manager failure does not usually stop existing VM forwarding immediately because dataplane state exists on transport nodes. However:

```text
management availability decreases
cluster is degraded
configuration changes may be affected
```

Treat manager-cluster health as critical.

# Part 9 — Compute Manager Integration

NSX integrates with vCenter:

```text
NSX Manager
    |
Compute Manager Registration
    |
vCenter
    |
Clusters / Hosts / VMs
```

This lets NSX discover workloads and prepare vSphere hosts.

# Part 10 — Transport Node

A transport node is a system participating in NSX networking.

Types:

```text
Host Transport Node
Edge Transport Node
```

# Part 11 — Host Transport Node

Prepared ESX hosts can perform:

```text
logical switching
distributed routing
distributed firewalling
overlay encapsulation
```

# Part 12 — Edge Transport Node

Edge nodes provide centralized services and North-South connectivity.

```text
Overlay Workloads
      |
     Edge
      |
External Physical Network
```

# Part 13 — Edge Cluster

```text
Edge Cluster
  |
  +-- Edge01
  +-- Edge02
```

The Edge cluster provides placement/resilience for centralized gateway services.

# Part 14 — Transport Zones

A transport zone defines the scope in which a transport node can participate in a class of logical networks.

Common concepts:

```text
Overlay Transport Zone
VLAN Transport Zone
```

# Part 15 — Overlay Transport Zone

```text
ESX01
ESX02
ESX03
  |
TZ-OVERLAY
  |
Overlay Segments
```

# Part 16 — VLAN Transport Zone

Used for VLAN-backed segments such as Edge uplinks or physical integrations.

```text
NSX VLAN Segment
   |
VLAN 301
   |
Physical Router
```

# Part 17 — Tunnel Endpoint (TEP)

TEP is an IP endpoint used for overlay tunnel encapsulation.

Example:

```text
ESX01 TEP: 10.10.20.11
ESX02 TEP: 10.10.20.12
```

# Part 18 — TEP IP Pool

Example pool:

```text
10.10.20.50-10.10.20.100
Gateway: 10.10.20.1
```

TEP traffic needs correct VLAN, routing, uplinks, and MTU.

# Part 19 — GENEVE Encapsulation

Modern NSX overlay uses GENEVE-based encapsulation.

```text
Inner Ethernet/IP Packet
       ↓
GENEVE Header
       ↓
UDP/IP Outer Packet
       ↓
Physical Underlay
```

# Part 20 — Overlay MTU

Encapsulation adds bytes. If underlay MTU is too small:

```text
small test packets may work
large application flows may fail
```

Use a consistent end-to-end MTU according to supported NSX design.

# Part 21 — TEP Packet Walk

Different hosts, same segment:

```text
VM A
 ↓
Host A logical switch
 ↓
Host A TEP encapsulates
 ↓
IP Underlay
 ↓
Host B TEP decapsulates
 ↓
Host B logical switch
 ↓
VM B
```

# Part 22 — NSX Segment

Segment is a logical Layer-2 network.

```text
SEG-WEB 172.16.10.0/24
SEG-APP 172.16.20.0/24
SEG-DB  172.16.30.0/24
```

# Part 23 — Overlay Segment

```text
VM vNIC
  |
Overlay Segment
  |
TEP / GENEVE
```

No end-to-end physical VLAN is required for the tenant subnet.

# Part 24 — VLAN Segment

```text
VM/Edge
  |
VLAN Segment
  |
802.1Q VLAN
  |
Physical Switch
```

# Part 25 — Segment Port

```text
VM vNIC
   |
Segment Port
   |
Segment
```

Security and workload metadata can be associated with the workload/port.

# Part 26 — Logical Switching

Same segment, same host:

```text
VM A → Host Datapath → VM B
```

Same segment, different host:

```text
VM A → TEP → Underlay → TEP → VM B
```

# Part 27 — East-West Traffic

East-West traffic is workload-to-workload traffic inside the data center:

```text
WEB ↔ APP ↔ DB
```

# Part 28 — North-South Traffic

North-South traffic crosses the logical/physical boundary:

```text
VM
 ↓
NSX Gateway
 ↓
Physical Router
 ↓
WAN / Internet / Existing DC
```

# Part 29 — Distributed Routing

Routing can happen directly in the host datapath:

```text
WEB 172.16.10.10
      |
Distributed Router
      |
APP 172.16.20.10
```

# Part 30 — Why Distributed Routing Is Powerful

Traditional hairpin:

```text
VM → physical router → VM
```

Distributed:

```text
VM → host datapath router → VM
```

This reduces unnecessary external hops for East-West traffic.

# Part 31 — Tier-0 Gateway

Tier-0 connects NSX logical networking to external physical infrastructure.

```text
Physical Network
      |
      T0
      |
      T1
      |
Segments
```

# Part 32 — Tier-1 Gateway

Tier-1 provides application/tenant routing and connects segments to Tier-0.

```text
T0
 |
T1-ERP
 |
+-- WEB
+-- APP
+-- DB
```

# Part 33 — T0/T1 Hierarchy

```text
          Physical Routers
                 |
                T0
          +------+------+
          |             |
        T1-ERP        T1-DEV
          |             |
     ERP Segments    Dev Segments
```

# Part 34 — Distributed Router Component

Distributed routing state is programmed on hosts so East-West routing does not require centralized Edge traversal.

# Part 35 — Service Router Component

Centralized/stateful services execute on Edge nodes. Conceptually:

```text
Distributed Router
       +
Service Router on Edge
```

# Part 36 — Tier-0 Uplink

```text
Tier-0
  |
Uplink Interface
  |
VLAN Segment
  |
Physical Router
```

# Part 37 — External VLAN Segment

Example:

```text
VLAN 301
T0:     10.10.30.2/30
Router: 10.10.30.1/30
```

# Part 38 — Static Routing

Simple route:

```text
0.0.0.0/0
next hop 10.10.30.1
```

Useful for small labs, but dynamic routing scales better.

# Part 39 — BGP in NSX

```text
T0 ASN 65010
     |
    BGP
     |
Physical Router ASN 65000
```

BGP provides dynamic route exchange.

# Part 40 — BGP Neighbor State

A healthy adjacency progresses to:

```text
Established
```

If not, check:

```text
IP connectivity
ASN
neighbor IP
TCP/179
authentication
source interface
```

# Part 41 — Route Advertisement

NSX can advertise selected logical prefixes such as:

```text
172.16.10.0/24
172.16.20.0/24
172.16.30.0/24
```

Use route policy to prevent accidental route leakage.

# Part 42 — ECMP

Equal-cost multipath can use multiple external routes simultaneously.

```text
        Router A
        /      \
     Edge      Edge
        \      /
        Router B
```

# Part 43 — Tier-0 HA Concepts

Depending on services/topology, Tier-0 service routing can use conceptual models such as:

```text
Active-Active
Active-Standby
```

Stateful services can constrain the suitable mode.

# Part 44 — Edge Failure

If one Edge fails, services should continue or relocate according to Edge-cluster and gateway HA configuration.

Monitor:

```text
Edge health
service router
BGP neighbors
uplink state
capacity
```

# Part 45 — Tier-1 Services

Tier-1 can host or attach services such as:

```text
NAT
DHCP-related services
gateway firewall
```

where architecture requires them.

# Part 46 — T1 Route Advertisement to T0

```text
T1-ERP owns:
172.16.10.0/24
172.16.20.0/24
172.16.30.0/24

T0 can advertise selected prefixes externally.
```

# Part 47 — NAT

SNAT changes source address. DNAT changes destination address.

```text
SNAT:
172.16.10.10 → 10.10.30.100

DNAT:
203.0.113.10 → 172.16.10.10
```

# Part 48 — SNAT Use Case

```text
Private VM
  ↓
T1/T0
  ↓
SNAT
  ↓
Internet
```

# Part 49 — DNAT Use Case

```text
Public IP
  ↓
DNAT
  ↓
Internal WEB VM
```

# Part 50 — NAT Is Not Firewall

```text
NAT = address translation
Firewall = access control
```

Both may be needed.

# Part 51 — DHCP

Concept:

```text
VM DHCP Discover
   ↓
Segment
   ↓
DHCP Service / Relay
```

# Part 52 — DHCP Relay

```text
VM
 |
Segment
 |
Relay
 |
Existing Corporate DHCP
```

# Part 53 — DNS Forwarding

Conceptual gateway forwarding:

```text
VM DNS query
   ↓
NSX DNS forwarder
   ↓
Corporate DNS
```

# Part 54 — Load Balancing Integration

Modern VMware environments commonly integrate NSX networking with Avi Load Balancer.

```text
Client
  |
Virtual Service
  |
Avi Service Engines
  |
Pool Members
```

NSX provides the network fabric; Avi provides advanced load-balancing services.

# Part 55 — Distributed Firewall

Distributed Firewall (DFW) enforces policy near workload vNICs.

```text
VM
 |
DFW
 |
Logical Network
```

Current VMware documentation often places these security capabilities under the vDefend brand.

# Part 56 — DFW Packet Path

```text
VM A
 ↓
DFW enforcement
 ↓
logical switching/routing
 ↓
DFW enforcement as applicable
 ↓
VM B
```

# Part 57 — Micro-Segmentation

Instead of only subnet-level controls:

```text
WEB subnet → APP subnet
```

use workload-specific policy:

```text
ERP-WEB → ERP-APP TCP/8443
ERP-APP → ERP-DB TCP/5432
Everything else denied
```

# Part 58 — Lateral Movement Reduction

Without segmentation:

```text
Compromised VM → many internal systems
```

With micro-segmentation:

```text
Compromised VM → only explicitly allowed flows
```

# Part 59 — Firewall Policy

Example:

```text
Policy: ERP

Rule 10
ERP-WEB → ERP-APP TCP/8443 ALLOW

Rule 20
ERP-APP → ERP-DB TCP/5432 ALLOW

Rule 99
ERP → ERP ANY DROP
```

# Part 60 — Firewall Rule Fields

Typical fields:

```text
Source
Destination
Service
Context/Profile where applicable
Action
Applied-To
Logging
```

# Part 61 — Groups

Groups can identify workloads by:

```text
VM tags
VM names
IP sets
segments
nested groups
other inventory criteria
```

# Part 62 — Tags

Example:

```text
Scope: App    Tag: ERP
Scope: Tier   Tag: WEB
```

# Part 63 — Dynamic Group Membership

Group expression:

```text
App=ERP
AND
Tier=WEB
```

A newly tagged VM automatically receives matching policy.

# Part 64 — Service Definitions

Create reusable services:

```text
HTTPS = TCP/443
ERP-APP = TCP/8443
POSTGRES = TCP/5432
```

# Part 65 — Stateful Firewalling

Once an allowed connection is established, return traffic is tracked as part of session state according to firewall behavior.

# Part 66 — Default Deny

Strong policy model:

```text
Explicitly allow required flows
Drop everything else
```

Deploy only after application dependencies are understood.

# Part 67 — Ring Fencing

```text
+---------------- ERP Application ----------------+
| WEB      APP      DB                            |
| Only documented internal/external flows allowed |
+--------------------------------------------------+
```

# Part 68 — Applied-To Scope

Applied-To can restrict enforcement to relevant workloads rather than the entire estate.

# Part 69 — Rule Ordering and Precedence

A broad allow above a specific deny can make the deny ineffective. Always analyze policy category and rule order.

# Part 70 — Rule Logging

Enable logging selectively for:

```text
denies
new policies
incident investigation
troubleshooting
```

Avoid unnecessary high-volume logging.

# Part 71 — Gateway Firewall

Gateway firewall protects centralized gateway paths.

```text
Overlay
  |
T0/T1 Gateway
  |
Gateway Firewall
  |
External Network
```

# Part 72 — DFW vs Gateway Firewall

```text
DFW:
workload-distributed
East-West micro-segmentation

Gateway Firewall:
centralized gateway boundary
North-South / transit controls
```

# Part 73 — Exclusion List Risk

A VM in the DFW exclusion list can bypass distributed firewall enforcement. Exclusions should be rare, documented, and audited.

# Part 74 — NSX Management-Plane Security

Protect Manager with:

```text
private management network
RBAC
MFA/identity controls where supported
trusted certificates
API restrictions
backups
central logging
```

# Part 75 — RBAC

Separate duties:

```text
Network Admin
Security Admin
Auditor
Automation Service Account
```

# Part 76 — Certificate Management

Track:

```text
issuer
expiry
hostname identity
API trust
integration trust
```

# Part 77 — NSX Manager Backup

Use supported file-based backup to an independent secure target.

Protect:

```text
network configuration
security policies
manager configuration
recovery state
```

# Part 78 — Supported Restore Thinking

Do not rely on arbitrary VM snapshot rollback of NSX Manager. Use the supported restore workflow for the release.

# Part 79 — Flow Visibility

Security operations need answers to:

```text
Who communicated?
To whom?
On which port?
Allowed or blocked?
By which rule?
```

# Part 80 — Security Intelligence Concept

```text
Observe flows
   ↓
identify dependencies
   ↓
create dynamic groups
   ↓
recommend policy
   ↓
review/test
   ↓
enforce
```

# Part 81 — Packet Capture Strategy

Capture/trace at:

```text
VM
host datapath
TEP
Edge
physical network
```

Ask: **Where did the packet disappear?**

# Part 82 — Traceflow

Traceflow provides a logical packet-path view through NSX switching, routing, and security components.

# Part 83 — Overlay Troubleshooting Stack

```text
VM IP
 ↓
Segment Port
 ↓
Host Transport Node
 ↓
TEP
 ↓
Underlay
 ↓
Remote TEP
 ↓
Remote Segment Port
```

# Part 84 — TEP Failure Pattern

If same-host communication works but cross-host communication fails, investigate TEP/underlay first.

# Part 85 — MTU Failure Pattern

```text
small ping works
large packet fails
```

This strongly suggests MTU inconsistency.

# Part 86 — Host Transport Node Not Ready

Check:

```text
vCenter integration
host preparation
transport zones
uplink profile
vDS mapping
TEP allocation
physical NIC state
```

# Part 87 — Edge Not Ready

Check:

```text
VM power state
management connectivity
DNS/NTP
Manager connectivity
TEP
uplinks
transport zones
Edge cluster
```

# Part 88 — Segment Connectivity Failure

```text
VM vNIC connected?
correct segment?
IP/subnet correct?
DFW?
same-host or cross-host?
TEP healthy?
```

# Part 89 — Distributed Routing Failure

If same-segment works but inter-segment fails, inspect:

```text
gateway IP
T1 attachment
route realization
DFW
neighbor state
```

# Part 90 — North-South Failure

```text
VM
 ↓
T1
 ↓
T0
 ↓
Edge
 ↓
BGP/Uplink
 ↓
Physical Router
```

# Part 91 — BGP Down

Check:

```text
uplink IP
reachability
TCP/179
ASN
neighbor address
authentication
Edge service state
```

# Part 92 — BGP Established but No Routes

Inspect:

```text
T1 advertisement
T0 redistribution
prefix lists
route maps
advertised routes
physical-router filters
```

# Part 93 — Asymmetric Routing

Stateful services can fail when forward and return paths use incompatible paths/Edges. Understand ECMP and stateful-service placement.

# Part 94 — NAT Troubleshooting

Check:

```text
rule enabled
correct gateway
match criteria
translated address
firewall
route
neighbor/ARP
```

# Part 95 — DFW Unexpected Block

Check:

```text
group membership
policy precedence
service
source/destination
Applied-To
default rule
logs
```

# Part 96 — DFW Unexpected Allow

Potential causes:

```text
broad allow
wrong group criteria
excluded VM
wrong policy category
ANY service
```

# Part 97 — Dynamic Group Debugging

Check tags before changing firewall policy.

```text
correct scope?
correct value?
AND/OR expression?
nested group?
realization delay?
```

# Part 98 — Safe Micro-Segmentation Rollout

```text
Observe
  ↓
Document Dependencies
  ↓
Create Groups
  ↓
Create Explicit Allows
  ↓
Log/Test
  ↓
Enforce Default Deny
```

# Part 99 — NSX Projects

Modern NSX/VCF can delegate controlled networking/security through project-style constructs.

```text
Provider NSX
   |
   +-- Project A
   +-- Project B
```

# Part 100 — VPC Concept

```text
Provider
  |
Project
  |
VPC
  |
Subnets + Security
```

This provides cloud-like logical tenancy.

# Part 101 — Multi-Tenancy

Tenant separation requires:

```text
routing isolation
security policy
RBAC
address management
governance
```

# Part 102 — Transit Gateway Concept

```text
VPC A \
       Transit Gateway → Shared Services
VPC B /
```

# Part 103 — Shared Services

Examples:

```text
DNS
AD
NTP
logging
patch repositories
backup services
```

Only required tenant flows should be permitted.

# Part 104 — IPsec VPN

```text
NSX Edge
  |
Encrypted IPsec Tunnel
  |
Remote Router/Firewall
```

# Part 105 — L2 VPN Concept

Layer-2 stretching can preserve IP addressing but increases broadcast and failure domains. Prefer routed designs when possible.

# Part 106 — Route-Based VPN

A logical tunnel interface can carry routes and integrate with routing policy/dynamic routing where supported.

# Part 107 — NSX Federation

```text
Global Manager
   |
   +-- Site A Local Manager
   +-- Site B Local Manager
```

# Part 108 — Global Manager

Global policy can define supported multi-location objects such as groups/security/topology intent.

# Part 109 — Federation Use Case

One global policy can express:

```text
ERP-WEB → ERP-APP TCP/8443
```

for workloads in more than one location.

# Part 110 — Federation Does Not Remove Site Failure

Still design:

```text
local manager survivability
local Edge capacity
inter-site routing
DR procedures
```

# Part 111 — Kubernetes / Antrea Integration

Modern NSX can integrate with Antrea-based Kubernetes networking/security patterns.

```text
Pods
 |
Antrea CNI
 |
NSX Visibility / Policy
```

# Part 112 — Workload Identity Beyond VMs

Policy identity can include:

```text
VM
Pod
Namespace
Tag
IP
Segment
```

# Part 113 — NSX Automation

```text
Terraform / Python / curl
         |
       HTTPS
         |
    NSX Policy API
```

# Part 114 — Policy API

Use desired-state objects for:

```text
Segments
Tier-1/Tier-0
Groups
Security Policies
NAT
```

# Part 115 — REST Authentication Example

Lab-only simple example:

```bash
curl -k \
  -u 'admin:LAB_PASSWORD' \
  https://nsx.lab.example/policy/api/v1/infra
```

`-k` disables TLS validation and is not appropriate for production.

# Part 116 — Trusted REST Read

```bash
curl \
  --cacert ca.pem \
  -u "$NSX_USER:$NSX_PASS" \
  https://nsx.lab.example/policy/api/v1/infra/tier-1s
```

# Part 117 — API JSON

Conceptual object:

```json
{
  "display_name": "T1-ERP",
  "resource_type": "Tier1"
}
```

# Part 118 — Segment JSON Concept

```json
{
  "display_name": "SEG-WEB",
  "subnets": [
    {
      "gateway_address": "172.16.10.1/24"
    }
  ]
}
```

Exact fields/endpoints must match installed API schema.

# Part 119 — Group JSON Concept

```json
{
  "display_name": "ERP-WEB",
  "expression": [
    {
      "resource_type": "Condition",
      "key": "Tag",
      "operator": "EQUALS",
      "value": "ERP|WEB"
    }
  ]
}
```

Use current API schema for exact syntax.

# Part 120 — Infrastructure as Code

```text
Git
 ↓
Review
 ↓
Pipeline
 ↓
Terraform / Policy API
 ↓
NSX
```

# Part 121 — API Safety

Before a write/delete:

```text
export state
confirm endpoint
confirm object ID
review diff
lab test
approval
rollback plan
```

# Part 122 — NSX CLI

NSX appliances expose supported diagnostics for managers/Edges. Exact syntax varies by release, so learn the diagnostic categories rather than memorizing stale commands.

# Part 123 — Edge Routing Diagnostics

Inspect:

```text
gateway realization
service-router location
uplink interfaces
BGP neighbors
route table
NAT
firewall
```

# Part 124 — Tunnel Diagnostics

Inspect:

```text
transport-node status
TEP addresses
tunnel state
underlay reachability
MTU
```

# Part 125 — Realized State

Policy defines desired state. Realized state answers:

```text
Did the infrastructure implement it successfully?
```

# Part 126 — Desired vs Realized Example

```text
Desired:
SEG-WEB exists

Realized:
ESX01 success
ESX02 error
```

# Part 127 — NSX Monitoring

Monitor:

```text
Manager cluster
Transport nodes
Edge cluster
Tunnel health
BGP
Gateways
DFW events
CPU/RAM
Certificates
Backups
```

# Part 128 — Edge Capacity

Edge nodes consume compute and network capacity. North-South throughput and stateful services must be sized explicitly.

# Part 129 — N+1 Edge Capacity

```text
Edge01 = 85% loaded
Edge02 = 85% loaded
```

If one fails, the survivor cannot carry total load. HA requires capacity headroom.

# Part 130 — Backup Monitoring

Monitor:

```text
last successful backup
backup target reachability
retention
restore procedure
credentials
```

# Part 131 — Upgrade Planning

Plan compatibility across:

```text
vSphere/VCF
NSX Managers
Edge clusters
transport nodes
APIs
backups
maintenance windows
```

# Part 132 — API Deprecation

Automation can break after upgrade if endpoints/fields are deprecated. Pin, test, and review API changes.

# Part 133 — vSphere Dependency

NSX depends on:

```text
vCenter
vDS
ESX hosts
physical uplinks
DNS/NTP
```

# Part 134 — Physical Fabric Dependency

A good underlay provides:

```text
simple routing
redundancy
sufficient MTU
low packet loss
capacity
predictable ECMP
```

# Part 135 — TEP Network Blast Radius

A TEP network failure can disrupt many overlay segments simultaneously. Protect it as critical infrastructure.

# Part 136 — Management Failure Blast Radius

Existing forwarding can continue during some management failures, but recovery and change capability are degraded. Therefore Manager HA + backup matter.

# Part 137 — Firewall Change Blast Radius

One broad policy can affect thousands of workloads. Use RBAC, change review, scope, logging, and automation guardrails.

# Part 138 — Application-Centric Policy

Prefer:

```text
ERP-WEB → ERP-APP
```

over only:

```text
10.10.10.0/24 → 10.10.20.0/24
```

when workload identity can be modeled reliably.

# Part 139 — Security Zones

Example:

```text
Internet/DMZ
Web
Application
Database
Management
Backup
```

# Part 140 — Zero Trust Relationship

NSX micro-segmentation supports Zero Trust principles by reducing implicit trust inside the data center. NSX alone is not a complete Zero Trust program.

# Part 141 — Backup Network Segmentation

```text
Backup Proxy → Protected VM: required backup ports
User VM      X Backup Repository
```

# Part 142 — Management Segmentation

Protect:

```text
vCenter
NSX Manager
ESX management
backup management
storage management
```

# Part 143 — DR Networking

Decide deliberately:

```text
stretch same IP?
or
use routed/new-IP recovery?
```

Routed DR is often simpler to operate.

# Part 144 — Stretched L2 Tradeoff

Benefit:

```text
IP preservation
```

Cost:

```text
larger failure domain
more complex troubleshooting
stateful-service complexity
```

# Part 145 — Route Summarization

Plan addressing so external routing can summarize logical networks rather than advertise unnecessary host/application-specific prefixes.

# Part 146 — IP Address Management

Example plan:

```text
172.16.0.0/16 Production
172.17.0.0/16 Development
172.18.0.0/16 DR
```

# Part 147 — Central Logging

```text
Managers
Edges
Hosts/DFW
   |
SIEM / Log Platform
```

Collect admin changes, firewall drops, system events, and authentication events.

# Part 148 — Change Management

Before:

```text
flow impact
backup/export
rollback
maintenance window
```

After:

```text
realization
connectivity
security
BGP
monitoring
```

# Part 149 — Troubleshooting Framework

Ask:

```text
L2?
L3?
Overlay?
Underlay?
Routing?
Firewall?
NAT?
Edge?
Realization?
```

# Part 150 — Same-Host vs Cross-Host Test

If same-host works and cross-host fails, suspect the overlay-tunnel/underlay path.

# Part 151 — Same Segment vs Routed Segment Test

If same-segment works and inter-segment fails, suspect logical routing/gateway/security rather than basic switching.

# Part 152 — East-West vs North-South Test

If East-West works but external access fails, focus on T0/Edge/uplink/BGP/NAT/gateway firewall/physical routing.

# Part 153 — Firewall Binary Search

Do not disable all security. Identify exact source, destination, service, policy, and effective rule.

# Part 154 — BGP Diagnostic Logic

Always inspect:

```text
neighbor state
received routes
advertised routes
selected route
next hop
```

# Part 155 — Packet Walk: WEB to DB

```text
WEB01
172.16.10.10
   |
DFW
   |
T1 Distributed Routing
   |
DB Segment
   |
DFW
   |
DB01
172.16.30.10
```

# Part 156 — Packet Walk: WEB to Internet

```text
WEB01
 ↓
DFW
 ↓
T1
 ↓
T0 Service Path
 ↓
Edge
 ↓
SNAT
 ↓
Physical Router
 ↓
Internet
```

# Part 157 — Packet Walk: Internet to Published App

```text
Internet
 ↓
Physical Router
 ↓
T0 / Edge
 ↓
DNAT / Load Balancer
 ↓
Gateway Firewall
 ↓
DFW
 ↓
WEB01
```

# Part 158 — Daily Operations

Check:

```text
Manager health
Edge health
Transport nodes
Tunnel health
BGP neighbors
Gateway alarms
Backups
Certificates
DFW changes
Capacity
```

# Part 159 — Weekly Operations

Review:

```text
stale rules
ANY rules
DFW exclusions
unused groups
failed realizations
Edge capacity
route growth
backup restore readiness
```

# Part 160 — Documentation Set

Maintain:

```text
NSX_MANAGER.md
TRANSPORT_ZONES.md
TEP_PLAN.md
EDGE_CLUSTER.md
T0_T1.md
BGP.md
SEGMENTS.md
DFW.md
NAT.md
RBAC.md
BACKUP.md
TROUBLESHOOTING.md
```

---

# Enhanced Deep-Study Layer — VMware NSX Networking and Security Engineering

This layer preserves the uploaded Course 40 and expands it with deeper diagrams, packet-path reasoning, security policy mechanics, API/IaC safety, failure-domain design, and troubleshooting. The uploaded source uses **VMware NSX 9.1 within the VCF 9.1 documentation family** as its reference baseline; exact API schemas, CLI syntax, limits, licensing, compatibility, and upgrade procedures must always be matched to the exact installed release.


## Advanced Deep Dive 1 — NSX Management Control and Data Planes

### Concept

The management/policy plane defines desired state, the control plane distributes state, and host/Edge data planes actually forward and filter packets.

### Architecture / Mental Model

```text
API/UI → Policy → Control distribution → Host/Edge realized state → packets
```

### Commands / Practical Example

```text
Record DesiredObject,RealizedState,EnforcementNode,PacketPath
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **NSX Management Control and Data Planes**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 2 — NSX Manager Cluster

### Concept

The Manager cluster provides resilient UI/API/policy/control services; existing dataplane forwarding may continue during some Manager failures while change capability is degraded.

### Architecture / Mental Model

```text
Manager1+Manager2+Manager3 → cluster/quorum → policy/control
```

### Commands / Practical Example

```text
Record node,FQDN,IP,CPU,RAM,disk,DNS,NTP,certificate,cluster state
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **NSX Manager Cluster**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 3 — Compute Manager Integration

### Concept

NSX integrates with vCenter to discover clusters, hosts and VMs and to prepare ESX transport nodes.

### Architecture / Mental Model

```text
NSX Manager → vCenter integration → clusters/hosts/VMs → host preparation
```

### Commands / Practical Example

```text
Validate vCenter FQDN,API reachability,certificate trust,inventory state
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Compute Manager Integration**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 4 — Transport Nodes

### Concept

Host transport nodes provide distributed switching/routing/DFW/TEP; Edge transport nodes provide centralized north-south and stateful services.

### Architecture / Mental Model

```text
Host TN=distributed datapath; Edge TN=centralized service datapath
```

### Commands / Practical Example

```text
Inventory node,type,TEP,TZ,uplink profile,vDS,pNIC,state
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Transport Nodes**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 5 — Transport Zones

### Concept

Transport zones define the scope in which transport nodes can participate in overlay or VLAN-backed networks.

### Architecture / Mental Model

```text
TZ-OVERLAY → ESX hosts; TZ-VLAN → Edge uplink participation
```

### Commands / Practical Example

```text
Document TZ,type,nodes,vDS mapping,purpose
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Transport Zones**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 6 — Host Transport Node Profile

### Concept

A transport-node profile standardizes cluster host preparation by defining vDS mapping, uplink profile, TEP assignment and transport zones.

### Architecture / Mental Model

```text
Cluster → TN Profile → hosts → ready transport nodes
```

### Commands / Practical Example

```text
Record vDS,uplink profile,TEP pool,TZ mappings
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Host Transport Node Profile**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 7 — TEP Architecture

### Concept

Tunnel Endpoints encapsulate and decapsulate GENEVE traffic; cross-host overlays depend on TEP reachability.

### Architecture / Mental Model

```text
VM A → HostA datapath → TEP-A === underlay === TEP-B → HostB → VM B
```

### Commands / Practical Example

```text
Build TEP table: node,IP,VLAN,subnet,gateway,uplink,MTU,state
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **TEP Architecture**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 8 — TEP IP Pool Capacity

### Concept

TEP pools must have enough unique addresses for current hosts/Edges plus replacement and growth.

### Architecture / Mental Model

```text
TEP pool → host/Edge TEP allocations → overlay tunnels
```

### Commands / Practical Example

```text
Record start,end,gateway,prefix,used,free,growth reserve
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **TEP IP Pool Capacity**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 9 — GENEVE Encapsulation

### Concept

NSX carries the inner workload Ethernet/IP packet inside an outer UDP/IP/GENEVE packet between TEPs.

### Architecture / Mental Model

```text
inner VM packet → GENEVE/UDP/IP outer packet → underlay
```

### Commands / Practical Example

```text
Capture outer source/dest TEP and inner source/dest packet fields
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **GENEVE Encapsulation**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 10 — Overlay MTU

### Concept

Encapsulation adds overhead, so underlay MTU must be large enough end-to-end or large application flows may fail while small tests work.

### Architecture / Mental Model

```text
guest frame + GENEVE overhead → smallest underlay MTU decides success
```

### Commands / Practical Example

```text
Create MTU matrix for TEP,vDS,pNIC,ToR,spine,Edge
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Overlay MTU**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 11 — Same-Host vs Cross-Host Overlay Test

### Concept

Same-host traffic stays inside one ESX datapath; cross-host traffic additionally requires TEPs and underlay.

### Architecture / Mental Model

```text
same host: VM→datapath→VM; cross host: VM→TEP→underlay→TEP→VM
```

### Commands / Practical Example

```text
Test same segment same host vs same segment different host
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Same-Host vs Cross-Host Overlay Test**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 12 — Segments and Segment Ports

### Concept

Segments are logical Layer-2 networks; workload vNICs attach through segment ports where identity and DFW policy can be associated.

### Architecture / Mental Model

```text
VM vNIC → segment port → segment → overlay/VLAN transport
```

### Commands / Practical Example

```text
Inventory segment,TZ,gateway,VM,port,tags
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Segments and Segment Ports**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 13 — Overlay vs VLAN Segments

### Concept

Overlay segments use GENEVE; VLAN segments map directly to physical 802.1Q VLANs for uplinks/legacy integration.

### Architecture / Mental Model

```text
Overlay: segment→TEP; VLAN: segment→802.1Q→physical switch
```

### Commands / Practical Example

```text
Document why each segment is overlay or VLAN-backed
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Overlay vs VLAN Segments**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 14 — Logical Switching

### Concept

Same-segment forwarding occurs inside the host datapath locally or across GENEVE tunnels when endpoints are on different hosts.

### Architecture / Mental Model

```text
VM A → logical switch → local VM or TEP→remote host
```

### Commands / Practical Example

```text
Test local and remote endpoints on same segment
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Logical Switching**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 15 — Distributed Routing

### Concept

Inter-segment east-west routing can occur directly in host datapaths without Edge hairpinning.

### Architecture / Mental Model

```text
WEB → DFW → distributed router → DFW → APP
```

### Commands / Practical Example

```text
Build packet walk with segment,gateway,T1,DFW,host location
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Distributed Routing**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 16 — Distributed Router vs Service Router

### Concept

Distributed routing handles scalable east-west paths; centralized/stateful services run in service-router context on Edge.

### Architecture / Mental Model

```text
Distributed Router → if NAT/GW-FW/VPN/external → Service Router on Edge
```

### Commands / Practical Example

```text
For each flow state whether Edge is required and why
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Distributed Router vs Service Router**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 17 — Tier-0 Gateway

### Concept

Tier-0 is the provider-facing north-south boundary connecting NSX logical routing to external physical routers.

### Architecture / Mental Model

```text
Physical Routers ↔ BGP/static ↔ T0 ↔ T1s
```

### Commands / Practical Example

```text
Document T0 EdgeCluster,HA mode,ASN,uplinks,neighbors,route policy
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Tier-0 Gateway**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 18 — Tier-1 Gateway

### Concept

Tier-1 organizes application/tenant segments and connects them upstream toward Tier-0.

### Architecture / Mental Model

```text
T0 → T1-ERP → WEB/APP/DB segments
```

### Commands / Practical Example

```text
Document T1 owner,segments,T0 attachment,advertisement,services
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Tier-1 Gateway**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 19 — T0/T1 Hierarchy

### Concept

Separating provider Tier-0 from tenant/application Tier-1 improves delegation, route policy and multi-tenancy.

### Architecture / Mental Model

```text
Physical → T0 → T1-ERP/T1-DEV → segments
```

### Commands / Practical Example

```text
Map provider-owned and tenant-owned objects
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **T0/T1 Hierarchy**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 20 — Tier-0 Uplink VLAN

### Concept

External Tier-0 interfaces usually connect through VLAN-backed segments to physical routers and depend on Edge uplinks and physical trunks.

### Architecture / Mental Model

```text
T0 SR → uplink interface → VLAN segment → Edge pNIC → physical router
```

### Commands / Practical Example

```text
Record VLAN,T0 IP,router IP,Edge uplink,physical switch port
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Tier-0 Uplink VLAN**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 21 — Static Routing

### Concept

Static routes are simple and predictable for small labs but require manual lifecycle and scale poorly.

### Architecture / Mental Model

```text
T0 → static default/summary → physical next hop
```

### Commands / Practical Example

```text
Record prefix,next hop,scope,owner
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Static Routing**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 22 — BGP Neighbor Session

### Concept

BGP establishes TCP/179 adjacency between Tier-0 and physical routers; session state is only the first layer of routing health.

### Architecture / Mental Model

```text
T0 ASN ↔ TCP/179 ↔ Router ASN
```

### Commands / Practical Example

```text
Record neighbor state,ASNs,source IP,auth,timers
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **BGP Neighbor Session**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 23 — BGP Route Advertisement

### Concept

A healthy BGP session does not prove correct prefixes; T1 advertisement, T0 redistribution and filters determine exported routes.

### Architecture / Mental Model

```text
segment routes → T1 advert → T0 redistribution → BGP export → router
```

### Commands / Practical Example

```text
Record received,advertised,selected routes and next hop
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **BGP Route Advertisement**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 24 — BGP Route Leak Prevention

### Concept

Explicit route policy is needed to prevent internal/tenant prefixes from leaking externally or conflicting with physical routes.

### Architecture / Mental Model

```text
tenant prefixes → policy/filter → approved external advertisements
```

### Commands / Practical Example

```text
Create allowed/denied prefix lists and max-prefix policy
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **BGP Route Leak Prevention**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 25 — Route Summarization

### Concept

Hierarchical IPAM enables summarization and reduces external route scale when aggregates are valid.

### Architecture / Mental Model

```text
many /24 application networks → valid aggregate → external routing
```

### Commands / Practical Example

```text
Document detailed routes and candidate summaries
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Route Summarization**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 26 — ECMP

### Concept

Equal-cost multipath provides scale and resilience across multiple Edge/uplink paths, but stateful services require careful symmetry.

### Architecture / Mental Model

```text
RouterA/B ↔ Edge1/2 ↔ T0
```

### Commands / Practical Example

```text
Record next hops,costs,ECMP state and stateful services
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **ECMP**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 27 — Active-Active vs Active-Standby Edge Services

### Concept

HA mode should reflect whether services are stateless/distributed or require centralized session ownership.

### Architecture / Mental Model

```text
active-active=both forward; active-standby=one service owner + failover
```

### Commands / Practical Example

```text
Document NAT,GW firewall,VPN,throughput and HA requirements
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Active-Active vs Active-Standby Edge Services**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 28 — Asymmetric Routing

### Concept

Stateful NAT/firewall/VPN can fail when forward and return traffic traverse incompatible service paths.

### Architecture / Mental Model

```text
Client→Edge1→App; App→Edge2→Client
```

### Commands / Practical Example

```text
Record forward/return next hops and session placement
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Asymmetric Routing**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 29 — Edge Cluster Capacity

### Concept

Two Edge nodes are not true HA if the survivor cannot carry required north-south throughput and session load after failure.

### Architecture / Mental Model

```text
Edge1+Edge2 normal → Edge1 fails → Edge2 carries service within headroom
```

### Commands / Practical Example

```text
Record normal/failure Gbps,CPU,RAM,sessions,BGP/NAT scale
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Edge Cluster Capacity**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 30 — NAT

### Concept

SNAT changes source addresses; DNAT changes destination addresses; routing and firewall policy still must be correct.

### Architecture / Mental Model

```text
packet → NAT translation → firewall → route → return state
```

### Commands / Practical Example

```text
Record original/translated 5-tuple,NAT rule,gateway,next hop
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **NAT**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 31 — NAT Is Not Firewall

### Concept

Address translation solves addressing/reachability, while firewall policy decides trust and allowed services.

### Architecture / Mental Model

```text
NAT changes address; firewall permits/drops; routing forwards
```

### Commands / Practical Example

```text
Document NAT and security policy as separate controls
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **NAT Is Not Firewall**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 32 — DHCP Service and Relay

### Concept

DHCP can be provided or relayed for logical segments; troubleshooting must follow segment, gateway, relay/server, scope and security.

### Architecture / Mental Model

```text
VM Discover → segment → DHCP service/relay → server → Offer/ACK
```

### Commands / Practical Example

```text
Record segment,mode,relay target,scope,lease range,DFW/GW policy
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DHCP Service and Relay**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 33 — DNS Forwarding

### Concept

Gateway DNS forwarding centralizes tenant queries toward upstream DNS but becomes a service dependency requiring monitoring and policy.

### Architecture / Mental Model

```text
VM DNS → forwarder → corporate DNS
```

### Commands / Practical Example

```text
Record allowed clients,upstream servers,latency,health
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DNS Forwarding**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 34 — Distributed Firewall

### Concept

DFW enforces policy near workload vNICs on host transport nodes, enabling east-west micro-segmentation without central firewall hairpinning.

### Architecture / Mental Model

```text
VM vNIC → DFW → switch/route → DFW → destination
```

### Commands / Practical Example

```text
Record source,destination,service,action,Applied-To,logging,rule ID
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Distributed Firewall**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 35 — Stateful DFW

### Concept

Stateful firewalling tracks established sessions so permitted return traffic is associated with the original allowed connection.

### Architecture / Mental Model

```text
SYN → rule allow → session table → return traffic recognized
```

### Commands / Practical Example

```text
Record 5-tuple,rule ID,session state,timeouts
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Stateful DFW**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 36 — Micro-Segmentation

### Concept

Micro-segmentation defines least-privilege application dependencies such as WEB→APP and APP→DB rather than trusting a whole subnet.

### Architecture / Mental Model

```text
WEB --8443→ APP --5432→ DB; unspecified lateral → drop
```

### Commands / Practical Example

```text
Create dependency matrix with source group,destination group,service,owner
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Micro-Segmentation**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 37 — Tags and Workload Identity

### Concept

Tags allow policy to follow application identity across IP or host changes.

### Architecture / Mental Model

```text
VM tags App/Tier/Env → dynamic group → DFW policy
```

### Commands / Practical Example

```text
Use App=ERP,Tier=WEB,Env=PROD examples
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Tags and Workload Identity**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 38 — Dynamic Groups

### Concept

Dynamic groups calculate membership from tags and inventory expressions; AND/OR mistakes can change policy scope massively.

### Architecture / Mental Model

```text
VM metadata → expression → group → rule membership
```

### Commands / Practical Example

```text
Validate tag scope/value,AND/OR,nested groups,membership count
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Dynamic Groups**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 39 — Applied-To

### Concept

Applied-To limits where distributed rules are instantiated and clarifies enforcement scope.

### Architecture / Mental Model

```text
policy → Applied-To → relevant workloads/segments only
```

### Commands / Practical Example

```text
Record rule,Applied-To,effective members,enforcement hosts
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Applied-To**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 40 — Rule Ordering and Precedence

### Concept

Broad earlier/higher-priority rules can shadow specific later rules, producing unexpected allows or drops.

### Architecture / Mental Model

```text
ANY→ANY allow first → later DEV→ERP drop never used
```

### Commands / Practical Example

```text
Audit category,sequence,source,dest,service,action,scope
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Rule Ordering and Precedence**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 41 — Rule Logging

### Concept

Logging should be selective enough to preserve useful deny/new-policy/incident evidence without overwhelming collectors.

### Architecture / Mental Model

```text
DFW rule → log event → SIEM
```

### Commands / Practical Example

```text
Estimate events/sec,retention and selected rules
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Rule Logging**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 42 — Default Deny

### Concept

Default deny should be implemented only after dependency discovery, explicit allows, logging and staged tests.

### Architecture / Mental Model

```text
observe → model → allow → test/log → default deny
```

### Commands / Practical Example

```text
Dependency matrix must include DNS,NTP,AD,backup,monitoring,patching
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Default Deny**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 43 — Ring Fencing

### Concept

Ring fencing contains an application to approved internal and external dependencies and reduces lateral-movement blast radius.

### Architecture / Mental Model

```text
application boundary with explicit WEB/APP/DB/MGMT/BACKUP flows
```

### Commands / Practical Example

```text
Create application policy package and exception register
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Ring Fencing**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 44 — DFW Exclusion List

### Concept

Excluded VMs bypass DFW and therefore create high-risk exceptions that must be rare, owned and time-bound.

### Architecture / Mental Model

```text
normal VM→DFW; excluded VM→bypass
```

### Commands / Practical Example

```text
Audit VM,reason,owner,approval,created,expiry,compensating control
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DFW Exclusion List**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 45 — Gateway Firewall

### Concept

Gateway firewall protects centralized Tier-0/Tier-1 service paths and complements DFW rather than replacing it.

### Architecture / Mental Model

```text
overlay → T0/T1 service router → gateway firewall → external/transit
```

### Commands / Practical Example

```text
Document north-south and transit rules
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Gateway Firewall**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 46 — DFW vs Gateway Firewall

### Concept

DFW protects workload interfaces and east-west flows; gateway firewall protects centralized routed boundaries.

### Architecture / Mental Model

```text
east-west: VM→DFW→VM; north-south: VM→DFW→Edge→GW-FW→external
```

### Commands / Practical Example

```text
Create packet walks showing both enforcement layers
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DFW vs Gateway Firewall**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 47 — Flow Visibility

### Concept

Micro-segmentation design requires observed flow evidence enriched with workload identity, service, direction, owner and business necessity.

### Architecture / Mental Model

```text
raw flow → identity enrichment → dependency candidate → owner review → policy
```

### Commands / Practical Example

```text
Record source,dest,port,direction,first/last seen,owner,required
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Flow Visibility**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 48 — Security Intelligence Workflow

### Concept

Flow analytics can suggest dependencies and groups, but human/application-owner validation is needed before converting observations to permanent allows.

### Architecture / Mental Model

```text
observe → classify → recommend → owner review → test → enforce
```

### Commands / Practical Example

```text
Never auto-allow every observed flow
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Security Intelligence Workflow**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 49 — Traceflow

### Concept

Traceflow models the logical packet path through NSX switching, routing and policy and identifies a logical drop or decision point.

### Architecture / Mental Model

```text
source → DFW → switch/router → TEP/Edge → destination
```

### Commands / Practical Example

```text
Record source,dest,protocol,logical hops,effective rule,drop point
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Traceflow**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 50 — Packet Capture Strategy

### Concept

Packet capture verifies actual frames at VM, host/TEP, Edge or underlay and complements Traceflow's logical view.

### Architecture / Mental Model

```text
VM capture → host/TEP → underlay → Edge/uplink
```

### Commands / Practical Example

```text
Record last-seen point and next expected transformation
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Packet Capture Strategy**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 51 — Desired vs Realized State

### Concept

Policy objects describe desired intent; realized state shows whether required hosts/Edges actually programmed it.

### Architecture / Mental Model

```text
desired object → realization → HostA OK / HostB Error / Edge OK
```

### Commands / Practical Example

```text
Record policy object,revision,realization status,failed node,error
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Desired vs Realized State**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 52 — Host Transport Node Not Ready

### Concept

A host can be healthy in vSphere while NSX preparation fails because of vDS mapping, uplink profile, TEP allocation, TZ or pNIC/underlay problems.

### Architecture / Mental Model

```text
vCenter host → prep → vDS → uplink profile → TEP → TZ → ready
```

### Commands / Practical Example

```text
Checklist compute manager,host prep,vDS,uplink profile,TEP,TZ,pNIC,MTU
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Host Transport Node Not Ready**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 53 — Edge Not Ready

### Concept

Edge readiness depends on VM power/resources, management connectivity, Manager trust, TEP, uplink VLANs and Edge-cluster placement.

### Architecture / Mental Model

```text
Edge VM → management → Manager → TEP → uplinks → Edge cluster → services
```

### Commands / Practical Example

```text
Record power,CPU/RAM,mgmt,DNS/NTP,Manager,TEP,uplinks,TZ,cluster
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Edge Not Ready**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 54 — TEP Failure Pattern

### Concept

Same-host success with cross-host failure points toward TEP, underlay, pNIC or MTU rather than basic guest/segment configuration.

### Architecture / Mental Model

```text
same host OK; cross host requires TEP/underlay and fails
```

### Commands / Practical Example

```text
Run same-host and cross-host tests and compare
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **TEP Failure Pattern**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 55 — Same Segment vs Routed Test

### Concept

If same-segment works but inter-segment fails, focus on T1/distributed routing/gateway/security instead of basic switching.

### Architecture / Mental Model

```text
WEB→WEB OK; WEB→APP fail → routing/DFW layer
```

### Commands / Practical Example

```text
Test same segment and routed segment pairs
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Same Segment vs Routed Test**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 56 — East-West vs North-South Test

### Concept

If east-west works but external access fails, focus on T0, Edge, uplink, BGP/static routes, NAT, gateway firewall and physical router.

### Architecture / Mental Model

```text
WEB→APP OK; WEB→Internet fail → T0/Edge/external path
```

### Commands / Practical Example

```text
Test internal routed flow and external flow
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **East-West vs North-South Test**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 57 — BGP Down Diagnosis

### Concept

A down BGP session should be debugged from IP reachability and TCP/179 through ASN, neighbor address, authentication and Edge service state.

### Architecture / Mental Model

```text
uplink IP → TCP179 → ASN/auth → Established
```

### Commands / Practical Example

```text
Record neighbor state,source,uplink,ASN,auth,timers
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **BGP Down Diagnosis**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 58 — BGP Established No Prefix Diagnosis

### Concept

An Established session with missing reachability usually means advertisement, redistribution or filtering rather than transport.

### Architecture / Mental Model

```text
session up → T1 advert? → T0 redistribution? → filters? → peer import?
```

### Commands / Practical Example

```text
Build per-prefix route trace
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **BGP Established No Prefix Diagnosis**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 59 — NAT Failure Workflow

### Concept

NAT troubleshooting follows gateway, rule match/order, translated address, firewall, route, neighbor and return path.

### Architecture / Mental Model

```text
original flow → translation → firewall → route → return state
```

### Commands / Practical Example

```text
Record pre/post NAT tuple and effective rule
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **NAT Failure Workflow**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 60 — DFW Unexpected Drop

### Concept

Unexpected drops require exact 5-tuple, group membership, service, category/order, Applied-To, effective rule and logs.

### Architecture / Mental Model

```text
flow → groups → service → scope → effective rule → drop
```

### Commands / Practical Example

```text
Record source/dest tags,groups,service,rule ID,log
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DFW Unexpected Drop**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 61 — DFW Unexpected Allow

### Concept

Unexpected access often comes from a broad allow, wrong group expression, exclusion, ANY service or higher-precedence rule.

### Architecture / Mental Model

```text
expected deny → broad allow/shadow → allowed
```

### Commands / Practical Example

```text
Audit effective rule,category,sequence,groups,service,exclusion
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DFW Unexpected Allow**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 62 — Dynamic Group Debugging

### Concept

Check tags and expression results before changing firewall rules; incorrect membership is often the real root cause.

### Architecture / Mental Model

```text
VM tags → group expression → members → policy
```

### Commands / Practical Example

```text
Record expected vs actual group membership
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Dynamic Group Debugging**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 63 — Projects and VPC

### Concept

Projects/VPCs provide delegated cloud-like networking/security scopes while the provider retains governance.

### Architecture / Mental Model

```text
Provider NSX → Project → VPC → subnets/security/connectivity
```

### Commands / Practical Example

```text
Document tenant,RBAC,quota,address space,external connectivity,shared services
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Projects and VPC**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 64 — Multi-Tenancy

### Concept

True tenant isolation requires routing, security, RBAC, IP management, quota and observability—not just different segments.

### Architecture / Mental Model

```text
TenantA routing/security/RBAC != TenantB
```

### Commands / Practical Example

```text
Create isolation matrix
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Multi-Tenancy**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 65 — Shared Services

### Concept

DNS, AD, NTP, logging, backup and repositories need explicit tenant-to-service policies.

### Architecture / Mental Model

```text
tenants → controlled policy → shared DNS/AD/NTP/logging/backup
```

### Commands / Practical Example

```text
Create tenant,service,ports,direction,owner matrix
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Shared Services**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 66 — IPsec VPN

### Concept

IPsec provides encrypted routed connectivity between NSX Edge and a remote peer and depends on IKE/IPsec parameters, routing and firewall policy.

### Architecture / Mental Model

```text
NSX Edge === encrypted IPsec === remote router/firewall
```

### Commands / Practical Example

```text
Record peer,IKE,proposal,PSK/cert,SA,selectors,routes
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **IPsec VPN**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 67 — L2 VPN and Stretch Trade-Off

### Concept

L2 stretch preserves addressing but expands broadcast/failure domains and complicates stateful service/gateway behavior.

### Architecture / Mental Model

```text
SiteA L2 ===== SiteB L2 same subnet
```

### Commands / Practical Example

```text
Document why stretch is required and its failure implications
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **L2 VPN and Stretch Trade-Off**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 68 — NSX Federation

### Concept

Federation coordinates supported policy/topology across locations through global/local management while sites retain local dataplanes.

### Architecture / Mental Model

```text
Global Manager → Local Manager A/B → site hosts/Edges
```

### Commands / Practical Example

```text
Document global objects,site realization,inter-site routes,failure behavior
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **NSX Federation**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 69 — Federation Failure Domains

### Concept

Global policy does not remove local Manager, Edge, underlay and DR dependencies.

### Architecture / Mental Model

```text
global intent → local realization → local failure still matters
```

### Commands / Practical Example

```text
Test global-manager down,local-manager degraded,site isolated
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Federation Failure Domains**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 70 — Kubernetes Antrea Awareness

### Concept

Modern workload identity can extend beyond VMs to pods, namespaces and labels through container networking/security integrations.

### Architecture / Mental Model

```text
Pod → Antrea/CNI → NSX visibility/policy → fabric
```

### Commands / Practical Example

```text
Record cluster,namespace,pod,label,node VM,NSX group
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Kubernetes Antrea Awareness**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 71 — Policy API

### Concept

The Policy API represents desired networking/security state over HTTPS/JSON and should be used with TLS validation and least-privilege identities.

### Architecture / Mental Model

```text
Git/Terraform/Python/curl → HTTPS JSON → NSX Policy API → realization
```

### Commands / Practical Example

```text
curl --cacert ca.pem -u "$NSX_USER:$NSX_PASS" https://nsx.lab.example/policy/api/v1/infra/tier-1s
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Policy API**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 72 — API Idempotency

### Concept

Idempotent automation converges on stable object paths and does not create duplicates on repeated runs.

### Architecture / Mental Model

```text
GET current → compare desired → PUT/PATCH stable path → verify realization
```

### Commands / Practical Example

```text
Use read-before-write and stable IDs
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **API Idempotency**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 73 — API TLS and Secrets

### Concept

Production automation should validate NSX certificates and retrieve scoped credentials from secret storage rather than using `-k` or hard-coded passwords.

### Architecture / Mental Model

```text
pipeline → secret store → scoped identity → trusted TLS → API
```

### Commands / Practical Example

```text
Avoid curl -k and literal admin passwords
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **API TLS and Secrets**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 74 — API Write Guardrails

### Concept

One API change can realize across thousands of workloads, so environment, object path, member counts, diff, approval and rollback must be validated.

### Architecture / Mental Model

```text
read/export → diff → review → write → realization → flow tests
```

### Commands / Practical Example

```text
Record environment,object path,member counts,approval,rollback version
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **API Write Guardrails**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 75 — Terraform IaC Workflow

### Concept

IaC makes NSX state versioned/reviewable but introduces state-file, provider-version and blast-radius considerations.

### Architecture / Mental Model

```text
Git → validate → plan → review → apply → realization → tests
```

### Commands / Practical Example

```text
Pipeline: fmt,validate,plan,policy-lint,approval,apply,tests
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Terraform IaC Workflow**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 76 — Manager Backup

### Concept

NSX Manager should use the supported independent backup workflow; casual VM snapshot rollback is not a safe recovery model for distributed manager state.

### Architecture / Mental Model

```text
Manager cluster → supported backup → independent repository → restore
```

### Commands / Practical Example

```text
Track last success,target,retention,credentials,restore-test date
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Manager Backup**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 77 — Certificate Lifecycle

### Concept

Manager/API certificate trust affects UI, vCenter integration and automation; track SAN/FQDN, issuer and expiry.

### Architecture / Mental Model

```text
client → TLS → NSX cert → trusted issuer
```

### Commands / Practical Example

```text
Track subject,SAN,issuer,expiry,owner
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Certificate Lifecycle**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 78 — RBAC Separation of Duties

### Concept

Network, security, audit and automation roles should be separate so one compromised identity cannot silently change every route/firewall object.

### Architecture / Mental Model

```text
identity → role/scope → network admin/security admin/auditor/automation
```

### Commands / Practical Example

```text
Audit principal,role,scope,MFA,owner,last used
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **RBAC Separation of Duties**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 79 — API Service Accounts

### Concept

Automation identities should be dedicated, least-privilege, rotated and stored in approved secret systems.

### Architecture / Mental Model

```text
pipeline → secret manager → scoped service identity → NSX API
```

### Commands / Practical Example

```text
Never store admin credentials in Git
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **API Service Accounts**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 80 — Central Logging SIEM

### Concept

Manager, Edge, DFW, routing and authentication logs should be centralized for cross-layer incident correlation.

### Architecture / Mental Model

```text
Managers/Edges/DFW → SIEM → alert/investigation
```

### Commands / Practical Example

```text
Collect admin changes,DFW drops,BGP changes,Edge failover,backup failures
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Central Logging SIEM**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 81 — Underlay Design

### Concept

A good NSX underlay is simple redundant routed IP transport with sufficient MTU, predictable ECMP, low loss and failure-state capacity.

### Architecture / Mental Model

```text
TEP → leaf/spine routed fabric → remote TEP
```

### Commands / Practical Example

```text
Track MTU,latency,packet loss,bandwidth,ECMP,convergence
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Underlay Design**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 82 — TEP Network Blast Radius

### Concept

Many logical segments share TEP infrastructure, so one TEP VLAN/route/MTU error can cause broad overlay impact.

### Architecture / Mental Model

```text
many segments → common TEPs → common underlay failure
```

### Commands / Practical Example

```text
Review affected hosts,Edges,segments,critical apps before TEP changes
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **TEP Network Blast Radius**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 83 — Underlay vs Overlay Routing

### Concept

Underlay routing knows TEP addresses; overlay routing knows tenant/application prefixes.

### Architecture / Mental Model

```text
underlay: TEP IPs; overlay: WEB/APP/DB CIDRs
```

### Commands / Practical Example

```text
Classify inner vs outer packet and underlay vs logical route
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Underlay vs Overlay Routing**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 84 — BUM Traffic and Endpoint Learning

### Concept

Broadcast/unknown/multicast handling and accurate MAC/IP endpoint state matter for scalable overlay switching.

### Architecture / Mental Model

```text
endpoint known → targeted forwarding; unknown/BUM → replication
```

### Commands / Practical Example

```text
Monitor broadcast rate,duplicates,endpoint moves
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **BUM Traffic and Endpoint Learning**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 85 — VM Mobility

### Concept

After vMotion, VM segment and metadata-driven policy should remain while physical host/TEP location changes.

### Architecture / Mental Model

```text
VM ESX01/TEP-A → vMotion → ESX02/TEP-B; same segment/tags/DFW
```

### Commands / Practical Example

```text
Validate host,segment,tags,groups,DFW,TEP before/after
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **VM Mobility**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 86 — North-South Packet Walk

### Concept

External traffic can traverse DFW, T1/T0, Edge service router, NAT/gateway firewall, uplink VLAN, BGP and physical routing.

### Architecture / Mental Model

```text
VM → DFW → T1/T0 → Edge → NAT/GW-FW → VLAN uplink → router
```

### Commands / Practical Example

```text
Document every hop and return path
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **North-South Packet Walk**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 87 — East-West Packet Walk

### Concept

Application traffic often stays in distributed datapaths and adds TEP/underlay only when endpoints are on different hosts.

### Architecture / Mental Model

```text
WEB → DFW → distributed route → DFW → APP; cross-host adds TEP
```

### Commands / Practical Example

```text
Document source/dest groups,DFW,route,same/cross host
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **East-West Packet Walk**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 88 — Published Application Packet Walk

### Concept

Inbound publication may combine physical routing, Tier-0/Edge, DNAT or load balancer, gateway firewall, DFW and destination workload.

### Architecture / Mental Model

```text
Internet → router → T0/Edge → DNAT/LB → GW-FW → DFW → WEB
```

### Commands / Practical Example

```text
Walk forward and return directions
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Published Application Packet Walk**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 89 — Avi Load Balancer Integration Awareness

### Concept

NSX supplies the network/security fabric while Avi-style load balancing provides virtual services, health checks and service-engine paths in integrated designs.

### Architecture / Mental Model

```text
client → VIP → service engines → pool members over NSX fabric
```

### Commands / Practical Example

```text
Validate VIP,pool health,route,DFW/GW-FW
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Avi Load Balancer Integration Awareness**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 90 — Management Segmentation

### Concept

vCenter, NSX Manager, ESX management, backup and storage management should be isolated from normal user/application networks.

### Architecture / Mental Model

```text
PAW/jump → firewall → management zone; user/DEV X
```

### Commands / Practical Example

```text
Create management access matrix
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Management Segmentation**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 91 — Backup Network Segmentation

### Concept

Backup infrastructure contains privileged data paths and repositories that should not be generally reachable from user VMs.

### Architecture / Mental Model

```text
backup proxy→workloads required ports; user VM X backup repository
```

### Commands / Practical Example

```text
Create backup access policy
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Backup Network Segmentation**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 92 — Zero Trust Relationship

### Concept

Micro-segmentation supports Zero Trust by reducing implicit internal trust, but full Zero Trust also includes identity, device, data and continuous verification.

### Architecture / Mental Model

```text
identity/context → explicit policy → enforcement → continuous telemetry
```

### Commands / Practical Example

```text
Map identity,workload,network,app,data,telemetry controls
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Zero Trust Relationship**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 93 — DR Routed vs Stretched L2

### Concept

Disaster recovery must choose between IP-preserving stretch and routed/new-subnet recovery; routed designs usually reduce failure-domain coupling.

### Architecture / Mental Model

```text
Option A L2 stretch; Option B routed DR + DNS/LB changes
```

### Commands / Practical Example

```text
Document RTO,IP dependency,latency,gateway,stateful services
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **DR Routed vs Stretched L2**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 94 — Hierarchical IPAM

### Concept

Structured address planning simplifies route summarization, tenant separation, security policy and DR.

### Architecture / Mental Model

```text
172.16/16 PROD; 172.17/16 DEV; 172.18/16 DR
```

### Commands / Practical Example

```text
Create IPAM table: env,app,segment,CIDR,gateway,T1,T0,owner
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Hierarchical IPAM**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 95 — Change Management

### Concept

NSX changes can realize broadly and quickly, so pre-change flow impact, export/version, member counts, rollback and post-change tests are mandatory.

### Architecture / Mental Model

```text
impact analysis → export → review → change → realization → tests → rollback
```

### Commands / Practical Example

```text
Record objects,members,routes,rules,rollback,test flows
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Change Management**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 96 — Upgrade and API Compatibility

### Concept

NSX lifecycle planning must verify interoperability with vSphere/VCF, Manager/Edge/TNs, backups and API automation.

### Architecture / Mental Model

```text
current stack → compatibility/backup → upgrade path → API regression tests
```

### Commands / Practical Example

```text
Precheck Manager/Edge/TN health,BGP,backup,API tests
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Upgrade and API Compatibility**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 97 — Daily Operations

### Concept

Daily health should cover Manager cluster, TNs, tunnels, Edge, T0/T1, BGP, backups, certificates, failed realization and capacity.

### Architecture / Mental Model

```text
Managers → TNs/tunnels → Edges/routing → security → backup/certs/capacity
```

### Commands / Practical Example

```text
Create daily checklist
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Daily Operations**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 98 — Weekly Security Hygiene

### Concept

Weekly review should identify ANY rules, stale temporary allows, exclusions, unused groups, failed realizations and route growth.

### Architecture / Mental Model

```text
rules/groups/exclusions → ownership/expiry/use → cleanup
```

### Commands / Practical Example

```text
Create weekly policy hygiene report
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Weekly Security Hygiene**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 99 — Manager Degraded Incident

### Concept

A degraded Manager cluster should be triaged without changing healthy dataplane configuration unnecessarily.

### Architecture / Mental Model

```text
manager cluster degraded → quorum/services → failed node/dependency → restore health
```

### Commands / Practical Example

```text
Record node state,DNS/NTP,disk,network,certificate,backup
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Manager Degraded Incident**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 100 — Edge Failure Incident

### Concept

Edge failure affects centralized services and north-south paths; validate service-router relocation, BGP, NAT/GW-FW state and surviving capacity.

### Architecture / Mental Model

```text
Edge1 X → Edge2/service relocation → BGP/NAT/GW-FW
```

### Commands / Practical Example

```text
Check Edge2 load,BGP,routes,sessions,external tests
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Edge Failure Incident**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 101 — MTU Incident

### Concept

Small-packet success and large-packet failure strongly indicates overlay/underlay MTU inconsistency.

### Architecture / Mental Model

```text
small packet OK; large DF packet X → find smallest MTU hop
```

### Commands / Practical Example

```text
Record host TEP,vDS,pNIC,ToR,spine,Edge MTUs
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **MTU Incident**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 102 — Overlay Blackhole

### Concept

Find the last point where the packet is seen: source VM, source TEP, underlay, destination TEP, destination VM.

### Architecture / Mental Model

```text
VM A → TEP A → underlay → TEP B → VM B
```

### Commands / Practical Example

```text
Use Traceflow plus packet captures at successive points
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Overlay Blackhole**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 103 — Route Leak Incident

### Concept

Incorrect advertisement/filtering can leak internal prefixes to external routers or create conflicts.

### Architecture / Mental Model

```text
T1 routes → T0 export policy → BGP → external
```

### Commands / Practical Example

```text
Audit advertised routes and filters
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Route Leak Incident**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 104 — Policy Rollback

### Concept

Rollback should restore a known-good version rather than creating a temporary global allow that weakens unrelated security.

### Architecture / Mental Model

```text
policy v5 → bad v6 → restore known-good v5 → realization/tests
```

### Commands / Practical Example

```text
Keep Git/export revision and critical flow tests
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Policy Rollback**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 105 — Observability Correlation

### Concept

NSX, vSphere and physical network telemetry must be time-synchronized and correlated to identify shared failures.

### Architecture / Mental Model

```text
NSX tunnel down + ToR errors + app alert → timeline → root cause
```

### Commands / Practical Example

```text
Use central logs and NTP
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Observability Correlation**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 106 — Capacity Forecasting

### Concept

Capacity planning includes Edge throughput, Manager resources, route/segment/rule/group/tunnel scale and session growth—not only VM count.

### Architecture / Mental Model

```text
current scale → growth trend → headroom breach date → expansion
```

### Commands / Practical Example

```text
Track segments,routes,rules,groups,Edge Gbps,Manager CPU/RAM
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Capacity Forecasting**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


## Advanced Deep Dive 107 — Runbook-Driven Troubleshooting

### Concept

Runbooks should follow packet paths—TEP, routing, BGP, NAT, DFW, Edge—rather than only UI menus.

### Architecture / Mental Model

```text
symptom → classify path → evidence → decision tree → action → verify
```

### Commands / Practical Example

```text
Maintain RUNBOOK_TEP,BGP,DFW,EDGE,NAT,MANAGER
```

### Expected Behavior

You should be able to identify the NSX policy object, realized state, enforcement node, packet path, and physical underlay dependency involved. A healthy UI object is not enough; verify that the object is realized on the required hosts/Edges and that representative flows take the intended path.

### Why It Works

NSX programs logical switching, routing, and security into distributed host datapaths while Edge nodes provide centralized services. GENEVE tunnels use the physical IP fabric as transport. This separation allows network/security policy to follow workloads, but it also means troubleshooting must distinguish desired state, realized state, distributed forwarding, centralized services, and the underlay.

### Production Example

For **Runbook-Driven Troubleshooting**, document application/tenant owner, affected transport nodes, TEPs, Tier-0/Tier-1/Edge dependencies, routing/security policy, failure domains, capacity assumptions, monitoring signals, and rollback. One logical policy can have a very large blast radius.

### Common Failure Pattern

```text
Symptom
  ↓
same host or cross host?
  ↓
same segment or routed?
  ↓
east-west or north-south?
  ↓
desired state correct?
  ↓
realized state correct?
  ↓
DFW / route / NAT / Edge?
  ↓
TEP / MTU / physical underlay?
  ↓
change one justified component
  ↓
verify forward + return flow
```

### Best Practice

Do not disable DFW globally or rebuild transport objects as first responses. Trace the exact flow, check dynamic group membership and effective rules, verify realized state, and only then move to TEP/underlay or Edge diagnostics as the packet path requires.

---


# Enhanced NSX Practical Lab Sequence


## Enhanced Lab 1 — NSX Management Control and Data Planes

### Goal

Validate **NSX Management Control and Data Planes** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
API/UI → Policy → Control distribution → Host/Edge realized state → packets
```

### Evidence / API / Configuration

```text
Record DesiredObject,RealizedState,EnforcementNode,PacketPath
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 2 — NSX Manager Cluster

### Goal

Validate **NSX Manager Cluster** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Manager1+Manager2+Manager3 → cluster/quorum → policy/control
```

### Evidence / API / Configuration

```text
Record node,FQDN,IP,CPU,RAM,disk,DNS,NTP,certificate,cluster state
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 3 — Compute Manager Integration

### Goal

Validate **Compute Manager Integration** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
NSX Manager → vCenter integration → clusters/hosts/VMs → host preparation
```

### Evidence / API / Configuration

```text
Validate vCenter FQDN,API reachability,certificate trust,inventory state
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 4 — Transport Nodes

### Goal

Validate **Transport Nodes** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Host TN=distributed datapath; Edge TN=centralized service datapath
```

### Evidence / API / Configuration

```text
Inventory node,type,TEP,TZ,uplink profile,vDS,pNIC,state
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 5 — Transport Zones

### Goal

Validate **Transport Zones** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
TZ-OVERLAY → ESX hosts; TZ-VLAN → Edge uplink participation
```

### Evidence / API / Configuration

```text
Document TZ,type,nodes,vDS mapping,purpose
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 6 — Host Transport Node Profile

### Goal

Validate **Host Transport Node Profile** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Cluster → TN Profile → hosts → ready transport nodes
```

### Evidence / API / Configuration

```text
Record vDS,uplink profile,TEP pool,TZ mappings
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 7 — TEP Architecture

### Goal

Validate **TEP Architecture** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM A → HostA datapath → TEP-A === underlay === TEP-B → HostB → VM B
```

### Evidence / API / Configuration

```text
Build TEP table: node,IP,VLAN,subnet,gateway,uplink,MTU,state
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 8 — TEP IP Pool Capacity

### Goal

Validate **TEP IP Pool Capacity** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
TEP pool → host/Edge TEP allocations → overlay tunnels
```

### Evidence / API / Configuration

```text
Record start,end,gateway,prefix,used,free,growth reserve
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 9 — GENEVE Encapsulation

### Goal

Validate **GENEVE Encapsulation** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
inner VM packet → GENEVE/UDP/IP outer packet → underlay
```

### Evidence / API / Configuration

```text
Capture outer source/dest TEP and inner source/dest packet fields
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 10 — Overlay MTU

### Goal

Validate **Overlay MTU** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
guest frame + GENEVE overhead → smallest underlay MTU decides success
```

### Evidence / API / Configuration

```text
Create MTU matrix for TEP,vDS,pNIC,ToR,spine,Edge
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 11 — Same-Host vs Cross-Host Overlay Test

### Goal

Validate **Same-Host vs Cross-Host Overlay Test** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
same host: VM→datapath→VM; cross host: VM→TEP→underlay→TEP→VM
```

### Evidence / API / Configuration

```text
Test same segment same host vs same segment different host
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 12 — Segments and Segment Ports

### Goal

Validate **Segments and Segment Ports** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM vNIC → segment port → segment → overlay/VLAN transport
```

### Evidence / API / Configuration

```text
Inventory segment,TZ,gateway,VM,port,tags
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 13 — Overlay vs VLAN Segments

### Goal

Validate **Overlay vs VLAN Segments** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Overlay: segment→TEP; VLAN: segment→802.1Q→physical switch
```

### Evidence / API / Configuration

```text
Document why each segment is overlay or VLAN-backed
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 14 — Logical Switching

### Goal

Validate **Logical Switching** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM A → logical switch → local VM or TEP→remote host
```

### Evidence / API / Configuration

```text
Test local and remote endpoints on same segment
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 15 — Distributed Routing

### Goal

Validate **Distributed Routing** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
WEB → DFW → distributed router → DFW → APP
```

### Evidence / API / Configuration

```text
Build packet walk with segment,gateway,T1,DFW,host location
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 16 — Distributed Router vs Service Router

### Goal

Validate **Distributed Router vs Service Router** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Distributed Router → if NAT/GW-FW/VPN/external → Service Router on Edge
```

### Evidence / API / Configuration

```text
For each flow state whether Edge is required and why
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 17 — Tier-0 Gateway

### Goal

Validate **Tier-0 Gateway** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Physical Routers ↔ BGP/static ↔ T0 ↔ T1s
```

### Evidence / API / Configuration

```text
Document T0 EdgeCluster,HA mode,ASN,uplinks,neighbors,route policy
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 18 — Tier-1 Gateway

### Goal

Validate **Tier-1 Gateway** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
T0 → T1-ERP → WEB/APP/DB segments
```

### Evidence / API / Configuration

```text
Document T1 owner,segments,T0 attachment,advertisement,services
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 19 — T0/T1 Hierarchy

### Goal

Validate **T0/T1 Hierarchy** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Physical → T0 → T1-ERP/T1-DEV → segments
```

### Evidence / API / Configuration

```text
Map provider-owned and tenant-owned objects
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 20 — Tier-0 Uplink VLAN

### Goal

Validate **Tier-0 Uplink VLAN** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
T0 SR → uplink interface → VLAN segment → Edge pNIC → physical router
```

### Evidence / API / Configuration

```text
Record VLAN,T0 IP,router IP,Edge uplink,physical switch port
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 21 — Static Routing

### Goal

Validate **Static Routing** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
T0 → static default/summary → physical next hop
```

### Evidence / API / Configuration

```text
Record prefix,next hop,scope,owner
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 22 — BGP Neighbor Session

### Goal

Validate **BGP Neighbor Session** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
T0 ASN ↔ TCP/179 ↔ Router ASN
```

### Evidence / API / Configuration

```text
Record neighbor state,ASNs,source IP,auth,timers
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 23 — BGP Route Advertisement

### Goal

Validate **BGP Route Advertisement** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
segment routes → T1 advert → T0 redistribution → BGP export → router
```

### Evidence / API / Configuration

```text
Record received,advertised,selected routes and next hop
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 24 — BGP Route Leak Prevention

### Goal

Validate **BGP Route Leak Prevention** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
tenant prefixes → policy/filter → approved external advertisements
```

### Evidence / API / Configuration

```text
Create allowed/denied prefix lists and max-prefix policy
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 25 — Route Summarization

### Goal

Validate **Route Summarization** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
many /24 application networks → valid aggregate → external routing
```

### Evidence / API / Configuration

```text
Document detailed routes and candidate summaries
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 26 — ECMP

### Goal

Validate **ECMP** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
RouterA/B ↔ Edge1/2 ↔ T0
```

### Evidence / API / Configuration

```text
Record next hops,costs,ECMP state and stateful services
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 27 — Active-Active vs Active-Standby Edge Services

### Goal

Validate **Active-Active vs Active-Standby Edge Services** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
active-active=both forward; active-standby=one service owner + failover
```

### Evidence / API / Configuration

```text
Document NAT,GW firewall,VPN,throughput and HA requirements
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 28 — Asymmetric Routing

### Goal

Validate **Asymmetric Routing** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Client→Edge1→App; App→Edge2→Client
```

### Evidence / API / Configuration

```text
Record forward/return next hops and session placement
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 29 — Edge Cluster Capacity

### Goal

Validate **Edge Cluster Capacity** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Edge1+Edge2 normal → Edge1 fails → Edge2 carries service within headroom
```

### Evidence / API / Configuration

```text
Record normal/failure Gbps,CPU,RAM,sessions,BGP/NAT scale
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 30 — NAT

### Goal

Validate **NAT** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
packet → NAT translation → firewall → route → return state
```

### Evidence / API / Configuration

```text
Record original/translated 5-tuple,NAT rule,gateway,next hop
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 31 — NAT Is Not Firewall

### Goal

Validate **NAT Is Not Firewall** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
NAT changes address; firewall permits/drops; routing forwards
```

### Evidence / API / Configuration

```text
Document NAT and security policy as separate controls
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 32 — DHCP Service and Relay

### Goal

Validate **DHCP Service and Relay** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM Discover → segment → DHCP service/relay → server → Offer/ACK
```

### Evidence / API / Configuration

```text
Record segment,mode,relay target,scope,lease range,DFW/GW policy
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 33 — DNS Forwarding

### Goal

Validate **DNS Forwarding** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM DNS → forwarder → corporate DNS
```

### Evidence / API / Configuration

```text
Record allowed clients,upstream servers,latency,health
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 34 — Distributed Firewall

### Goal

Validate **Distributed Firewall** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM vNIC → DFW → switch/route → DFW → destination
```

### Evidence / API / Configuration

```text
Record source,destination,service,action,Applied-To,logging,rule ID
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 35 — Stateful DFW

### Goal

Validate **Stateful DFW** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
SYN → rule allow → session table → return traffic recognized
```

### Evidence / API / Configuration

```text
Record 5-tuple,rule ID,session state,timeouts
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 36 — Micro-Segmentation

### Goal

Validate **Micro-Segmentation** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
WEB --8443→ APP --5432→ DB; unspecified lateral → drop
```

### Evidence / API / Configuration

```text
Create dependency matrix with source group,destination group,service,owner
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 37 — Tags and Workload Identity

### Goal

Validate **Tags and Workload Identity** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM tags App/Tier/Env → dynamic group → DFW policy
```

### Evidence / API / Configuration

```text
Use App=ERP,Tier=WEB,Env=PROD examples
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 38 — Dynamic Groups

### Goal

Validate **Dynamic Groups** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM metadata → expression → group → rule membership
```

### Evidence / API / Configuration

```text
Validate tag scope/value,AND/OR,nested groups,membership count
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 39 — Applied-To

### Goal

Validate **Applied-To** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
policy → Applied-To → relevant workloads/segments only
```

### Evidence / API / Configuration

```text
Record rule,Applied-To,effective members,enforcement hosts
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 40 — Rule Ordering and Precedence

### Goal

Validate **Rule Ordering and Precedence** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
ANY→ANY allow first → later DEV→ERP drop never used
```

### Evidence / API / Configuration

```text
Audit category,sequence,source,dest,service,action,scope
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 41 — Rule Logging

### Goal

Validate **Rule Logging** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
DFW rule → log event → SIEM
```

### Evidence / API / Configuration

```text
Estimate events/sec,retention and selected rules
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 42 — Default Deny

### Goal

Validate **Default Deny** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
observe → model → allow → test/log → default deny
```

### Evidence / API / Configuration

```text
Dependency matrix must include DNS,NTP,AD,backup,monitoring,patching
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 43 — Ring Fencing

### Goal

Validate **Ring Fencing** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
application boundary with explicit WEB/APP/DB/MGMT/BACKUP flows
```

### Evidence / API / Configuration

```text
Create application policy package and exception register
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 44 — DFW Exclusion List

### Goal

Validate **DFW Exclusion List** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
normal VM→DFW; excluded VM→bypass
```

### Evidence / API / Configuration

```text
Audit VM,reason,owner,approval,created,expiry,compensating control
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 45 — Gateway Firewall

### Goal

Validate **Gateway Firewall** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
overlay → T0/T1 service router → gateway firewall → external/transit
```

### Evidence / API / Configuration

```text
Document north-south and transit rules
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 46 — DFW vs Gateway Firewall

### Goal

Validate **DFW vs Gateway Firewall** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
east-west: VM→DFW→VM; north-south: VM→DFW→Edge→GW-FW→external
```

### Evidence / API / Configuration

```text
Create packet walks showing both enforcement layers
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 47 — Flow Visibility

### Goal

Validate **Flow Visibility** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
raw flow → identity enrichment → dependency candidate → owner review → policy
```

### Evidence / API / Configuration

```text
Record source,dest,port,direction,first/last seen,owner,required
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 48 — Security Intelligence Workflow

### Goal

Validate **Security Intelligence Workflow** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
observe → classify → recommend → owner review → test → enforce
```

### Evidence / API / Configuration

```text
Never auto-allow every observed flow
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 49 — Traceflow

### Goal

Validate **Traceflow** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
source → DFW → switch/router → TEP/Edge → destination
```

### Evidence / API / Configuration

```text
Record source,dest,protocol,logical hops,effective rule,drop point
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 50 — Packet Capture Strategy

### Goal

Validate **Packet Capture Strategy** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM capture → host/TEP → underlay → Edge/uplink
```

### Evidence / API / Configuration

```text
Record last-seen point and next expected transformation
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 51 — Desired vs Realized State

### Goal

Validate **Desired vs Realized State** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
desired object → realization → HostA OK / HostB Error / Edge OK
```

### Evidence / API / Configuration

```text
Record policy object,revision,realization status,failed node,error
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 52 — Host Transport Node Not Ready

### Goal

Validate **Host Transport Node Not Ready** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
vCenter host → prep → vDS → uplink profile → TEP → TZ → ready
```

### Evidence / API / Configuration

```text
Checklist compute manager,host prep,vDS,uplink profile,TEP,TZ,pNIC,MTU
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 53 — Edge Not Ready

### Goal

Validate **Edge Not Ready** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Edge VM → management → Manager → TEP → uplinks → Edge cluster → services
```

### Evidence / API / Configuration

```text
Record power,CPU/RAM,mgmt,DNS/NTP,Manager,TEP,uplinks,TZ,cluster
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 54 — TEP Failure Pattern

### Goal

Validate **TEP Failure Pattern** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
same host OK; cross host requires TEP/underlay and fails
```

### Evidence / API / Configuration

```text
Run same-host and cross-host tests and compare
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 55 — Same Segment vs Routed Test

### Goal

Validate **Same Segment vs Routed Test** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
WEB→WEB OK; WEB→APP fail → routing/DFW layer
```

### Evidence / API / Configuration

```text
Test same segment and routed segment pairs
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 56 — East-West vs North-South Test

### Goal

Validate **East-West vs North-South Test** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
WEB→APP OK; WEB→Internet fail → T0/Edge/external path
```

### Evidence / API / Configuration

```text
Test internal routed flow and external flow
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 57 — BGP Down Diagnosis

### Goal

Validate **BGP Down Diagnosis** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
uplink IP → TCP179 → ASN/auth → Established
```

### Evidence / API / Configuration

```text
Record neighbor state,source,uplink,ASN,auth,timers
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 58 — BGP Established No Prefix Diagnosis

### Goal

Validate **BGP Established No Prefix Diagnosis** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
session up → T1 advert? → T0 redistribution? → filters? → peer import?
```

### Evidence / API / Configuration

```text
Build per-prefix route trace
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 59 — NAT Failure Workflow

### Goal

Validate **NAT Failure Workflow** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
original flow → translation → firewall → route → return state
```

### Evidence / API / Configuration

```text
Record pre/post NAT tuple and effective rule
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 60 — DFW Unexpected Drop

### Goal

Validate **DFW Unexpected Drop** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
flow → groups → service → scope → effective rule → drop
```

### Evidence / API / Configuration

```text
Record source/dest tags,groups,service,rule ID,log
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 61 — DFW Unexpected Allow

### Goal

Validate **DFW Unexpected Allow** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
expected deny → broad allow/shadow → allowed
```

### Evidence / API / Configuration

```text
Audit effective rule,category,sequence,groups,service,exclusion
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 62 — Dynamic Group Debugging

### Goal

Validate **Dynamic Group Debugging** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
VM tags → group expression → members → policy
```

### Evidence / API / Configuration

```text
Record expected vs actual group membership
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 63 — Projects and VPC

### Goal

Validate **Projects and VPC** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Provider NSX → Project → VPC → subnets/security/connectivity
```

### Evidence / API / Configuration

```text
Document tenant,RBAC,quota,address space,external connectivity,shared services
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 64 — Multi-Tenancy

### Goal

Validate **Multi-Tenancy** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
TenantA routing/security/RBAC != TenantB
```

### Evidence / API / Configuration

```text
Create isolation matrix
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 65 — Shared Services

### Goal

Validate **Shared Services** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
tenants → controlled policy → shared DNS/AD/NTP/logging/backup
```

### Evidence / API / Configuration

```text
Create tenant,service,ports,direction,owner matrix
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 66 — IPsec VPN

### Goal

Validate **IPsec VPN** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
NSX Edge === encrypted IPsec === remote router/firewall
```

### Evidence / API / Configuration

```text
Record peer,IKE,proposal,PSK/cert,SA,selectors,routes
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 67 — L2 VPN and Stretch Trade-Off

### Goal

Validate **L2 VPN and Stretch Trade-Off** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
SiteA L2 ===== SiteB L2 same subnet
```

### Evidence / API / Configuration

```text
Document why stretch is required and its failure implications
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 68 — NSX Federation

### Goal

Validate **NSX Federation** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Global Manager → Local Manager A/B → site hosts/Edges
```

### Evidence / API / Configuration

```text
Document global objects,site realization,inter-site routes,failure behavior
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 69 — Federation Failure Domains

### Goal

Validate **Federation Failure Domains** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
global intent → local realization → local failure still matters
```

### Evidence / API / Configuration

```text
Test global-manager down,local-manager degraded,site isolated
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 70 — Kubernetes Antrea Awareness

### Goal

Validate **Kubernetes Antrea Awareness** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Pod → Antrea/CNI → NSX visibility/policy → fabric
```

### Evidence / API / Configuration

```text
Record cluster,namespace,pod,label,node VM,NSX group
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 71 — Policy API

### Goal

Validate **Policy API** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Git/Terraform/Python/curl → HTTPS JSON → NSX Policy API → realization
```

### Evidence / API / Configuration

```text
curl --cacert ca.pem -u "$NSX_USER:$NSX_PASS" https://nsx.lab.example/policy/api/v1/infra/tier-1s
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 72 — API Idempotency

### Goal

Validate **API Idempotency** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
GET current → compare desired → PUT/PATCH stable path → verify realization
```

### Evidence / API / Configuration

```text
Use read-before-write and stable IDs
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 73 — API TLS and Secrets

### Goal

Validate **API TLS and Secrets** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
pipeline → secret store → scoped identity → trusted TLS → API
```

### Evidence / API / Configuration

```text
Avoid curl -k and literal admin passwords
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 74 — API Write Guardrails

### Goal

Validate **API Write Guardrails** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
read/export → diff → review → write → realization → flow tests
```

### Evidence / API / Configuration

```text
Record environment,object path,member counts,approval,rollback version
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## Enhanced Lab 75 — Terraform IaC Workflow

### Goal

Validate **Terraform IaC Workflow** in an authorized NSX lab or complete a detailed tabletop when the feature requires additional hardware/licensing.

### Procedure

1. Record NSX, vCenter, and ESX versions/builds.
2. Identify the exact source, destination, segment, T1/T0, Edge, and transport nodes.
3. Draw the expected packet path before changing anything.
4. Capture desired state and realized state.
5. Run the evidence checks below.
6. Generate one controlled flow or failure.
7. Use Traceflow/logs/events/counters and packet capture where appropriate.
8. Compare forward and return paths.
9. Roll back the lab change.
10. Verify both required **allows** and required **denies**.

### Architecture

```text
Git → validate → plan → review → apply → realization → tests
```

### Evidence / API / Configuration

```text
Pipeline: fmt,validate,plan,policy-lint,approval,apply,tests
```

### Lab Report

```text
NSX build:
vCenter/ESX build:
Source:
Destination:
Segment:
T1/T0:
Edge:
TEPs:
Expected path:
Desired state:
Realized state:
Expected result:
Actual result:
Effective rule/route:
Drop point:
Root cause:
Correction:
Rollback:
Final verification:
Prevention:
```

### Safety

Use only authorized lab systems for firewall enforcement, transport-node/uplink failure, Edge power-off, BGP changes, NAT publication, VPN changes, API writes, or MTU failure injection. Keep management access and rollback independent from the path you are testing.

---


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Draw NSX Planes

Draw Manager, host transport nodes, Edge nodes, underlay, segments, and gateways. Label management/control/data responsibilities.

### Lab 2 — Underlay Plan

Define TEP VLAN/subnet, MTU, physical uplinks, routing, and redundancy.

### Lab 3 — Deploy/Register NSX Manager

In an authorized lab:

1. deploy Manager;
2. assign management IP;
3. configure DNS/NTP;
4. register vCenter;
5. verify health;
6. record certificate state.

### Lab 4 — Create Transport Zones

Create/design:

```text
TZ-OVERLAY
TZ-VLAN
```

### Lab 5 — Prepare ESX Hosts

Create a transport-node profile mapping the vDS, uplink profile, TEP pool, and transport zones. Apply to the lab cluster.

### Lab 6 — Verify TEPs

Build a table:

```text
Host | TEP IP | TZ | Uplink | Status
```

Validate reachability/MTU with supported tools.

### Lab 7 — Overlay Segment

Create `SEG-WEB` and attach two VMs. Test same-host and cross-host communication.

### Lab 8 — App and DB Segments

Create `SEG-APP` and `SEG-DB`. Observe that L2 separation exists before routing.

### Lab 9 — Deploy Edge Cluster

Deploy Edge01 and Edge02, configure TEP/uplinks, and verify Edge-cluster health.

### Lab 10 — Create Tier-0

Create `T0-LAB` and an external VLAN uplink segment. Document centralized service placement.

### Lab 11 — Configure BGP

Using a lab router/FRR:

```text
T0 ASN 65010
Router ASN 65000
```

Establish adjacency and inspect routes.

### Lab 12 — Create Tier-1

Create `T1-ERP`, attach WEB/APP/DB, and test distributed routing.

### Lab 13 — North-South Connectivity

Advertise overlay routes through T0/BGP and test external reachability.

### Lab 14 — SNAT

Configure outbound translation for an internal subnet. Verify the translated source externally.

### Lab 15 — DNAT

Publish one lab web service. Restrict inbound access to the required service only.

### Lab 16 — Dynamic Groups

Tag VMs:

```text
App=ERP
Tier=WEB/APP/DB
```

Create dynamic groups and verify membership.

### Lab 17 — DFW Micro-Segmentation

Implement:

```text
ERP-WEB → ERP-APP TCP/8443 ALLOW
ERP-APP → ERP-DB TCP/5432 ALLOW
ERP groups → ERP groups DROP
```

Test allowed and blocked flows.

### Lab 18 — Rule Logging

Enable logging on a lab deny rule, generate traffic, and locate the evidence.

### Lab 19 — Gateway Firewall

Create a North-South gateway policy and compare its enforcement point to DFW.

### Lab 20 — Traceflow

Trace WEB01 → DB01 and document each logical hop.

### Lab 21 — MTU Failure

In an isolated lab, intentionally create an MTU mismatch, compare small versus large traffic, then restore correct MTU.

### Lab 22 — Host Transport-Node Failure

Disable one lab transport/uplink path safely and observe tunnel/VM effects.

### Lab 23 — Edge Failure

Power off one Edge in a disposable lab and observe gateway/BGP failover.

### Lab 24 — BGP Failure

Break one neighbor parameter, diagnose it systematically, then restore.

### Lab 25 — DFW Policy Staging

Build an application-flow matrix before enforcing default deny.

### Lab 26 — NSX REST Read

```bash
curl \
  --cacert ca.pem \
  -u "$NSX_USER:$NSX_PASS" \
  https://nsx.lab.example/policy/api/v1/infra/tier-1s
```

Save and inspect JSON.

### Lab 27 — API Object Design

Create version-controlled JSON files for segment, group, and security-policy intent. Review before applying.

### Lab 28 — Backup Design

Configure/design file-based Manager backup. Document target, retention, credentials, and restore sequence.

### Lab 29 — Security Review

Audit RBAC, Manager exposure, certificates, DFW exclusions, broad rules, API identities, backups, and logging.

### Lab 30 — Troubleshooting Challenge

Analyze:

1. Manager cluster degraded.
2. Host transport node failed.
3. TEP unreachable.
4. MTU mismatch.
5. Same-host works/cross-host fails.
6. Tier-1 routing failure.
7. Tier-0 uplink failure.
8. BGP down.
9. Routes not advertised.
10. NAT fails.
11. DFW unexpected drop.
12. DFW unexpected allow.
13. Dynamic group wrong.
14. Edge failure.
15. Backup missing.

For each:

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

# Mini Project — NSX Micro-Segmented Enterprise Network

```text
                         Internet
                            |
                     Physical Router
                            |
                           BGP
                            |
                           T0
                            |
                    +-------+-------+
                    |               |
                  T1-ERP          T1-DEV
                    |               |
             +------+------+       DEV
             |      |      |
            WEB    APP     DB
```

### Workloads

```text
ERP-WEB01/02
ERP-APP01/02
ERP-DB01/02
DEV01/02
Management
Backup
```

### Underlay

Document TEP subnet, MTU, physical uplinks, Edge uplinks, BGP peers, and ASNs.

### Logical Networks

Create:

```text
SEG-ERP-WEB
SEG-ERP-APP
SEG-ERP-DB
SEG-DEV
SEG-MGMT-SERVICES
```

### Routing

Design T0, T1-ERP, T1-DEV, BGP, ECMP, and route advertisement.

### Security

Groups:

```text
ERP-WEB
ERP-APP
ERP-DB
DEV
BACKUP
MGMT
```

Rules:

```text
WEB -> APP TCP/8443
APP -> DB TCP/5432
MGMT -> workloads approved admin ports
BACKUP -> workloads approved backup ports
DEV X ERP
Default deny
```

### Resilience

Design:

```text
Manager cluster
2+ Edge nodes
N+1 Edge capacity
dual underlay paths
BGP redundancy
independent Manager backup
```

### Automation

Create a Git structure:

```text
api/
  segments/
  gateways/
  groups/
  firewall/
  nat/
```

### Deliverables

```text
README.md
PHYSICAL_UNDERLAY.md
TEP_PLAN.md
TRANSPORT_ZONES.md
EDGE_CLUSTER.md
T0_T1.md
BGP.md
SEGMENTS.md
NAT.md
DFW_POLICY.md
GROUPS_TAGS.md
RBAC.md
BACKUP_RECOVERY.md
MONITORING.md
API_AUTOMATION.md
RUNBOOKS/
```

---


# Expanded Capstone — NSX Micro-Segmented Enterprise Fabric

Design or build a resilient enterprise NSX environment.

```text
                         Internet / WAN
                              |
                      Physical Routers
                        /           \
                      BGP           BGP
                        \           /
                         Tier-0
                           |
                  +--------+--------+
                  |                 |
                T1-ERP            T1-DEV
            /      |      \           |
         WEB      APP      DB        DEV
           \       |       /
             Distributed FW
                   |
          Host Transport Nodes
                   |
             GENEVE / TEP
                   |
            Physical Underlay
```

Create:

```text
README.md
NSX_MANAGER.md
PHYSICAL_UNDERLAY.md
TRANSPORT_ZONES.md
TRANSPORT_NODES.md
TEP_PLAN.md
EDGE_CLUSTER.md
T0_T1.md
BGP.md
ROUTE_POLICY.md
SEGMENTS.md
GROUPS_TAGS.md
DFW_POLICY.md
GATEWAY_SECURITY.md
NAT.md
RBAC.md
BACKUP_RECOVERY.md
MONITORING.md
API_AUTOMATION.md
PACKET_WALKS.md
runbooks/
failure_tests/
```

Use logical networks:

```text
SEG-ERP-WEB  172.16.10.0/24
SEG-ERP-APP  172.16.20.0/24
SEG-ERP-DB   172.16.30.0/24
SEG-DEV      172.17.10.0/24
SEG-SHARED   172.16.100.0/24
```

Use tags/groups:

```text
App=ERP
Tier=WEB
Tier=APP
Tier=DB
Env=PROD
Env=DEV
Role=MGMT
Role=BACKUP

Groups:
ERP-WEB
ERP-APP
ERP-DB
DEV
MGMT
BACKUP
SHARED-DNS
SHARED-AD
```

Security policy:

```text
ERP-WEB → ERP-APP TCP/8443 ALLOW
ERP-APP → ERP-DB  TCP/5432 ALLOW
MGMT → ERP approved admin ALLOW
BACKUP → ERP approved backup ALLOW
ERP → DNS/NTP/AD required ALLOW
DEV → ERP ANY DROP
ERP unspecified lateral ANY DROP
```

Packet walks must include:

```text
WEB01 → WEB02 same host
WEB01 → WEB02 different hosts
WEB → APP
APP → DB
DEV → ERP denied
WEB → Internet
Internet → published WEB
BACKUP → DB
MGMT → WEB
```

For each packet walk identify:

```text
inner source/destination
segment
DFW rule
distributed route
TEP/GENEVE if cross-host
T1
T0
Edge service router
NAT
gateway firewall
uplink VLAN
BGP route
physical next hop
return path
```

API/IaC pipeline:

```text
Git
 ↓ validate
 ↓ API/schema tests
 ↓ plan/diff
 ↓ member-count guardrail
 ↓ peer approval
 ↓ apply
 ↓ realized-state verification
 ↓ allow/deny flow tests
```

Failure-test at least:

```text
one Manager node failure
host transport-node failure
TEP unreachable
one pNIC failure
one ToR failure
MTU mismatch
same-host works/cross-host fails
T1 routing failure
T0 uplink failure
BGP neighbor down
BGP established/no routes
route leak
Edge node failure
NAT failure
DFW accidental deny
DFW accidental allow
wrong dynamic group membership
backup failure
certificate failure
API schema regression
```


## 7. Recommended Resources

This Markdown file contains the conceptual foundation required for the course. For exact production commands and API schemas, match the installed release.

Current official documentation families relevant to this material include:

```text
VMware Cloud Foundation 9.1 — NSX
NSX Advanced Network Management
NSX-T Data Center REST / Policy API
VMware vDefend Distributed Firewall
VCF Network Design Library
NSX Manager Backup and Restore
NSX Federation
```

Current-version facts reflected here:

- NSX 9.1 is documented in the VMware Cloud Foundation 9.1 family.
- NSX provides software-defined networking for VMs, containers, and supported application environments.
- Tier-0 is the logical North-South boundary toward physical infrastructure.
- Current security documentation brands distributed firewall capabilities under VMware vDefend.
- The NSX API uses HTTPS and JSON and exposes policy-oriented REST resources.

---

## 8. Certification Relevance

Relevant to:

```text
Network Virtualization Engineer
VMware / VCF Engineer
Cloud Infrastructure Engineer
Network Security Engineer
Private Cloud Engineer
Cybersecurity Engineer
Platform Engineer
```

This course also prepares you for OpenStack Neutron, cloud networking, micro-segmentation, Zero Trust design, and Kubernetes network security.

---

## 9. Common Mistakes & Best Practices

- **Mistake:** NSX replaces the physical network.  
  **Best practice:** build a simple, redundant, correctly sized IP underlay.

- **Mistake:** Ignore overlay MTU.  
  **Best practice:** validate MTU end-to-end.

- **Mistake:** Create overlay before testing TEP reachability.  
  **Best practice:** validate underlay first.

- **Mistake:** Assume every East-West packet traverses Edge.  
  **Best practice:** understand distributed switching/routing.

- **Mistake:** NAT treated as security.  
  **Best practice:** use explicit firewall policy.

- **Mistake:** Security rules use only changing IP addresses.  
  **Best practice:** use well-governed application tags/groups.

- **Mistake:** `ANY ANY ALLOW`.  
  **Best practice:** explicit dependencies and default deny.

- **Mistake:** Enforce default deny before dependency discovery.  
  **Best practice:** observe, model, test, then enforce.

- **Mistake:** Exclude workloads from DFW to “fix” an application.  
  **Best practice:** correct policy and audit exclusions.

- **Mistake:** BGP Established means route design is correct.  
  **Best practice:** inspect received/advertised/selected routes.

- **Mistake:** Two Edge nodes with no spare throughput called HA.  
  **Best practice:** maintain N+1 service capacity.

- **Mistake:** Manager backup in the same failure domain only.  
  **Best practice:** use independent protected backup.

- **Mistake:** Hard-code NSX admin credentials in scripts.  
  **Best practice:** use least-privilege automation identity and secret storage.

- **Mistake:** Desired API object assumed fully deployed.  
  **Best practice:** verify realized state.

- **Mistake:** Disable firewall globally for troubleshooting.  
  **Best practice:** trace the exact flow and matching rule.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is NSX?
**Short answer:** VMware software-defined networking and security platform.

### Q2. Underlay vs overlay?
**Short answer:** Underlay is physical IP transport; overlay is logical networking built over it.

### Q3. What is a transport node?
**Short answer:** A host or Edge participating in NSX networking.

### Q4. What is a TEP?
**Short answer:** Tunnel Endpoint used for overlay encapsulation/de-encapsulation.

### Q5. What overlay encapsulation does modern NSX use?
**Short answer:** GENEVE-based encapsulation.

### Q6. Why does MTU matter?
**Short answer:** Overlay headers add overhead; an insufficient underlay MTU can break larger flows.

### Q7. What is a transport zone?
**Short answer:** Scope defining which transport nodes participate in overlay or VLAN networks.

### Q8. What is a segment?
**Short answer:** NSX logical Layer-2 network.

### Q9. Overlay vs VLAN segment?
**Short answer:** Overlay uses NSX tunnels; VLAN segment maps to a physical VLAN.

### Q10. What is distributed routing?
**Short answer:** Logical routing performed in host datapaths close to workloads.

### Q11. What is Tier-0?
**Short answer:** Logical gateway connecting NSX to external physical networks.

### Q12. What is Tier-1?
**Short answer:** Application/tenant logical gateway connecting segments upstream to Tier-0.

### Q13. What is an Edge node?
**Short answer:** NSX transport node providing centralized gateway/service functions.

### Q14. Why use an Edge cluster?
**Short answer:** Resilience and capacity for centralized NSX services.

### Q15. Why use BGP?
**Short answer:** Dynamic route exchange between NSX Tier-0 and external routers.

### Q16. What is ECMP?
**Short answer:** Multiple equal-cost routing paths used concurrently.

### Q17. What is SNAT?
**Short answer:** Translation of source IP, commonly for outbound access.

### Q18. What is DNAT?
**Short answer:** Translation of destination IP, commonly to publish an internal service.

### Q19. NAT vs firewall?
**Short answer:** NAT changes addressing; firewall authorizes/blocks traffic.

### Q20. What is DFW?
**Short answer:** Distributed Firewall enforcing policy near workload interfaces.

### Q21. What is micro-segmentation?
**Short answer:** Fine-grained workload/application-level controls limiting lateral movement.

### Q22. Why use tags?
**Short answer:** They allow security policy to follow workload identity rather than fixed IP/location.

### Q23. What is Applied-To?
**Short answer:** Scope controlling where distributed firewall rules are enforced.

### Q24. DFW vs gateway firewall?
**Short answer:** DFW is distributed around workloads; gateway firewall protects centralized boundaries.

### Q25. Why is exclusion-list use risky?
**Short answer:** Excluded workloads can bypass DFW enforcement.

### Q26. What is Traceflow?
**Short answer:** Logical datapath diagnostic tracing a flow through NSX components.

### Q27. What is realized state?
**Short answer:** Actual infrastructure implementation of desired policy.

### Q28. What is NSX Federation?
**Short answer:** Multi-location coordination of NSX networking/security through global/local management.

### Q29. What is Policy API?
**Short answer:** REST interface used to express desired NSX networking/security intent.

### Q30. Same-host works, cross-host fails: likely area?
**Short answer:** TEP, tunnel, MTU, or physical underlay.

### Q31. East-West works but external access fails: likely area?
**Short answer:** T0, Edge, uplink, BGP, NAT, gateway firewall, or physical routing.

### Q32. BGP established but prefix absent: what next?
**Short answer:** Check T1 advertisement, T0 redistribution, filters/route maps, and external router policy.

### Q33. What is the key design principle?
**Short answer:** Keep the underlay reliable and simple, then express logical network/security intent in software.

---

# Expanded Self-Assessment Bank

### Q1. What is NSX?
**Answer:** Software-defined networking and security over physical IP transport.

### Q2. Underlay vs overlay?
**Answer:** Underlay is physical IP transport; overlay is logical workload networking.

### Q3. What are the three planes?
**Answer:** Management/policy, control, and data plane.

### Q4. Does one Manager failure normally stop all VM traffic?
**Answer:** No; previously realized dataplane state can continue while management is degraded.

### Q5. What is a transport node?
**Answer:** A host or Edge participating in NSX networking.

### Q6. Host TN vs Edge TN?
**Answer:** Host TN runs distributed workload datapath; Edge TN runs centralized services.

### Q7. What is a transport zone?
**Answer:** Scope controlling which transport nodes participate in overlay or VLAN networks.

### Q8. What is a transport-node profile?
**Answer:** Reusable cluster host-preparation definition for vDS/uplink/TEP/TZ settings.

### Q9. What is a TEP?
**Answer:** Tunnel Endpoint for GENEVE encapsulation/decapsulation.

### Q10. Why capacity-plan TEP pools?
**Answer:** Every host/Edge needs unique tunnel IPs and expansion can exhaust the pool.

### Q11. What is GENEVE?
**Answer:** Overlay encapsulation carrying inner tenant packets inside outer TEP-to-TEP packets.

### Q12. Why does overlay MTU matter?
**Answer:** Encapsulation adds header overhead.

### Q13. Same-host works, cross-host fails—likely layer?
**Answer:** TEP, underlay, pNIC, routing or MTU.

### Q14. What is a segment?
**Answer:** Logical Layer-2 network.

### Q15. Overlay vs VLAN segment?
**Answer:** Overlay uses GENEVE; VLAN-backed maps to physical 802.1Q.

### Q16. What is distributed routing?
**Answer:** Routing performed in host datapaths near workloads.

### Q17. Why doesn't every routed packet traverse Edge?
**Answer:** Basic east-west routing can remain distributed on hosts.

### Q18. What is a service router?
**Answer:** Centralized Edge context for NAT/gateway firewall/VPN/external services.

### Q19. What is Tier-0?
**Answer:** Provider-facing gateway to external physical routing.

### Q20. What is Tier-1?
**Answer:** Application/tenant gateway connecting segments upstream to Tier-0.

### Q21. What does BGP Established prove?
**Answer:** Only that the neighbor session is up.

### Q22. What do you check when BGP is up but routes are missing?
**Answer:** T1 advertisement, T0 redistribution, filters, advertised/received/selected routes.

### Q23. What is ECMP?
**Answer:** Multiple equal-cost next hops.

### Q24. Why can ECMP affect stateful services?
**Answer:** Forward and return paths can use different service state.

### Q25. Why are two Edge nodes not automatically HA?
**Answer:** The survivor may lack throughput/session capacity.

### Q26. SNAT vs DNAT?
**Answer:** SNAT changes source; DNAT changes destination.

### Q27. Why is NAT not security?
**Answer:** Translation changes addresses; firewall policy decides authorization.

### Q28. What is DFW?
**Answer:** Distributed Firewall enforced near workload interfaces.

### Q29. What is micro-segmentation?
**Answer:** Fine-grained least-privilege workload/application controls.

### Q30. Why use tags?
**Answer:** Policy can follow workload identity instead of fixed IP/location.

### Q31. What is a dynamic group?
**Answer:** Membership calculated from tags/inventory expressions.

### Q32. Why is AND/OR logic important?
**Answer:** A small expression mistake can massively change group membership.

### Q33. What is Applied-To?
**Answer:** Scope controlling where a DFW rule is instantiated.

### Q34. Why does rule order matter?
**Answer:** An earlier broader match can shadow a later specific rule.

### Q35. Why use selective rule logging?
**Answer:** To preserve useful evidence without overwhelming logging systems.

### Q36. What is default deny?
**Answer:** Allow only documented dependencies and drop unspecified flows.

### Q37. Why must default deny be staged?
**Answer:** Hidden dependencies can otherwise break applications.

### Q38. What is ring fencing?
**Answer:** Containing an application to its required internal/external flows.

### Q39. Why is DFW exclusion risky?
**Answer:** Excluded workloads bypass distributed firewall enforcement.

### Q40. DFW vs gateway firewall?
**Answer:** DFW is distributed workload security; gateway firewall protects centralized boundaries.

### Q41. What is Traceflow?
**Answer:** Logical NSX packet-path diagnostic.

### Q42. Why also use packet capture?
**Answer:** It confirms actual frames and underlay encapsulation.

### Q43. Desired vs realized state?
**Answer:** Desired is policy intent; realized is what nodes actually programmed.

### Q44. Why can a host be vSphere-healthy but NSX-not-ready?
**Answer:** Transport-node preparation adds vDS/uplink/TEP/TZ dependencies.

### Q45. What can make Edge not ready?
**Answer:** Resources, management, Manager connectivity, TEP, uplinks, TZ or cluster placement.

### Q46. Same-segment works, inter-segment fails—where to focus?
**Answer:** T1/distributed routing/gateway/DFW.

### Q47. East-west works, north-south fails—where to focus?
**Answer:** T0, Edge, uplink, BGP/static routing, NAT, GW firewall, physical router.

### Q48. How do you troubleshoot BGP down?
**Answer:** IP reachability→TCP179→neighbor/ASN/auth→session.

### Q49. How do you troubleshoot BGP up/no prefix?
**Answer:** Trace prefix through T1 advertisement→T0 redistribution→filters→peer import.

### Q50. How do you troubleshoot NAT?
**Answer:** Gateway→rule match/order→translation→firewall→route→neighbor→return path.

### Q51. How do you troubleshoot DFW unexpected drop?
**Answer:** 5-tuple→groups/tags→service→scope→effective rule→logs.

### Q52. How do you troubleshoot DFW unexpected allow?
**Answer:** Check broad rules, wrong groups, exclusions, ANY service and precedence.

### Q53. Why check group membership before editing rules?
**Answer:** The wrong identity may be the root cause.

### Q54. What is a Project/VPC?
**Answer:** Delegated cloud-like networking/security scope.

### Q55. What does multi-tenancy require?
**Answer:** Routing isolation, security, RBAC, IP management, quota and observability.

### Q56. Why treat shared services explicitly?
**Answer:** They create common dependencies and possible lateral paths.

### Q57. What is IPsec VPN?
**Answer:** Encrypted routed tunnel between NSX Edge and a remote peer.

### Q58. Why is L2 stretch risky?
**Answer:** It expands broadcast/failure domains and operational complexity.

### Q59. What is Federation?
**Answer:** Multi-location coordination of NSX policy/topology.

### Q60. Does Federation remove local failures?
**Answer:** No; local Managers, Edges, underlay and DR remain important.

### Q61. What is Policy API?
**Answer:** HTTPS/JSON desired-state API for NSX networking/security objects.

### Q62. Why avoid curl -k in production?
**Answer:** It disables TLS certificate validation.

### Q63. What does idempotent automation mean?
**Answer:** Repeated runs converge on the same desired state without duplicates.

### Q64. Why verify realized state after an API write?
**Answer:** A valid central object can fail to program on a node.

### Q65. Why use service accounts for automation?
**Answer:** Least privilege, auditability and credential rotation.

### Q66. Why is Manager VM snapshot rollback risky?
**Answer:** Distributed manager state can become inconsistent; use supported backup/restore.

### Q67. Why centralize logs?
**Answer:** To correlate NSX, vSphere and physical network evidence.

### Q68. What makes a good underlay?
**Answer:** Simple redundant routed IP, correct MTU, low loss, ECMP and capacity.

### Q69. Why is TEP network a large blast radius?
**Answer:** Many overlay segments depend on the same tunnel transport.

### Q70. Underlay routing vs overlay routing?
**Answer:** Underlay routes TEP IPs; overlay routes tenant/application prefixes.

### Q71. Why should policy survive vMotion?
**Answer:** Logical segment/tags/group identity follow the VM while host/TEP location changes.

### Q72. Typical north-south path?
**Answer:** VM→DFW→T1/T0→Edge services→uplink→physical router.

### Q73. Typical east-west path?
**Answer:** VM→DFW→distributed switch/route→DFW→destination, plus TEP if cross-host.

### Q74. How does NSX relate to Zero Trust?
**Answer:** Micro-segmentation reduces implicit trust but is only one part of Zero Trust.

### Q75. Routed DR vs stretched L2?
**Answer:** Routed DR changes network identity but reduces cross-site failure coupling.

### Q76. Why is hierarchical IPAM useful?
**Answer:** It simplifies summarization, policy, multi-tenancy and DR.

### Q77. What is the core NSX troubleshooting rule?
**Answer:** Classify the packet path, compare desired vs realized state, then inspect the exact failing layer.


## Completion Checklist

- [ ] I understand underlay/overlay.
- [ ] I understand NSX Manager architecture.
- [ ] I understand host and Edge transport nodes.
- [ ] I understand transport zones.
- [ ] I understand TEPs and GENEVE.
- [ ] I understand segments.
- [ ] I understand distributed switching and routing.
- [ ] I understand Tier-0/Tier-1.
- [ ] I understand Edge clusters.
- [ ] I understand BGP/ECMP.
- [ ] I understand NAT/DHCP fundamentals.
- [ ] I understand DFW and gateway firewall.
- [ ] I can design basic micro-segmentation.
- [ ] I understand groups/tags.
- [ ] I understand rule scope/precedence/logging.
- [ ] I understand Projects/VPC fundamentals.
- [ ] I understand VPN and Federation fundamentals.
- [ ] I understand REST/Policy API.
- [ ] I understand backup/lifecycle concepts.
- [ ] I can monitor transport, Edge, routing, and security health.
- [ ] I can troubleshoot overlay, BGP, NAT, and DFW failures.
- [ ] I completed all 30 labs.
- [ ] I completed the NSX Micro-Segmented Enterprise Network project.
