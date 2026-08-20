# 19. Advanced Switching Design and Implementation

> Phase 4 — Networking

This course completes Phase 4 by focusing on resilient enterprise campus switching and Layer-2/Layer-3 design.

The central question is:

> **How do we build large switched networks without loops, broadcast storms, unstable gateways, weak access-layer security, or single points of failure?**

You will move from VLAN/trunk basics into campus architecture, STP/RSTP, EtherChannel, first-hop redundancy, multilayer switching, port security, DHCP Snooping, Dynamic ARP Inspection, IP Source Guard, high availability, management, and systematic troubleshooting.
## 1. Topic Title

**Advanced Switching Design and Implementation**

## 2. Learning Objectives

- Design two-tier and three-tier enterprise campus networks.
- Plan VLANs, trunks, native VLANs, and Layer-3 boundaries deliberately.
- Explain STP root election, path cost, port roles, states, and RSTP convergence.
- Configure root placement, PortFast, BPDU Guard, Root Guard, and Loop Guard appropriately.
- Build EtherChannel using LACP/PAgP where supported and troubleshoot bundle inconsistency.
- Implement first-hop redundancy using HSRP concepts and verify gateway failover.
- Configure routed access, SVIs, routed uplinks, and dynamic routing on multilayer switches.
- Apply access-layer security including port security, DHCP Snooping, DAI, and IP Source Guard.
- Design resilient management, logging, NTP, SNMP, and configuration-backup practices.
- Troubleshoot VLAN, trunk, STP, EtherChannel, HSRP, DHCP Snooping, and MAC-table failures.

## 3. Prerequisites

Required:

- 16. Cisco Network Associate
- 17. Cisco Internetworking
- 18. Advanced Routing Design and Implementation is recommended before the final integrated campus design
- VLANs and trunks
- Inter-VLAN routing
- Static and OSPF routing
- Basic ACL/security concepts
- Cisco IOS switching CLI

You should be able to configure VLANs, access ports, trunks, SVIs, and basic routing without a step-by-step guide.
## 4. Core Concepts Explanation

# Part 1 — Enterprise Switching Architecture

### 1. Campus Network Architecture

A campus network connects users, phones, APs, printers, and services across one site or related buildings using hierarchical switching and routing.

### 2. Access Layer

Connects endpoints and applies edge policy such as VLAN assignment, 802.1X, PoE, port security, QoS trust boundaries, DHCP Snooping, and DAI.

### 3. Distribution Layer

Aggregates access switches, provides Layer-3 boundaries, policy, route summarization, redundancy, and often first-hop gateways.

### 4. Core Layer

Provides fast, resilient transport between distribution blocks and major services with minimal unnecessary policy complexity.

### 5. Two-Tier Design

Access plus collapsed core/distribution. Common in small/medium campuses.

### 6. Three-Tier Design

Access, distribution, and core are separate layers. Useful in larger campuses.

### 7. Collapsed Core

Core and distribution functions are combined into one resilient layer.

### 8. Layer-2 Boundaries

Define where broadcasts, STP, and VLANs extend.

### 9. Layer-3 Boundaries

Define routed separation, fault isolation, and where dynamic routing can replace STP-dependent links.

```text
Three-tier:

             CORE1 ===== CORE2
              /            \
           DIST1          DIST2
           /  \           /  \
        ACC1  ACC2     ACC3  ACC4
         |     |        |     |
       Users  APs     Phones Servers

Two-tier / collapsed core:

        CORE-DIST1 ==== CORE-DIST2
           /   \          /   \
        ACC1  ACC2      ACC3  ACC4
```
# Part 2 — Ethernet Switching Review

### 10. Ethernet Frames

Layer-2 delivery units containing destination/source MAC, payload-type information, payload, and FCS.

### 11. MAC Learning

Switch learns source MAC on ingress VLAN/port.

### 12. MAC Forwarding

Known destination MAC is forwarded toward the learned egress port.

### 13. Flooding

Unknown unicast, broadcast, and relevant multicast traffic are flooded within the VLAN.

### 14. Unknown Unicast

A unicast frame whose destination MAC is not yet in the switch forwarding table.

### 15. Broadcast

Sent to FF:FF:FF:FF:FF:FF and flooded within the VLAN.

### 16. MAC Table Aging

Dynamic entries age out after inactivity.

### 17. CAM Table

Hardware forwarding table implementing MAC/VLAN lookup.

# Part 3 — VLAN Design

### 18. VLAN Architecture

Plan VLANs around trust, function, broadcast scope, policy, and operational requirements.

### 19. User VLANs

General endpoint/user access.

### 20. Server VLANs

Server/workload segments, commonly subject to stricter east-west policy.

### 21. Management VLANs

Administrative interfaces should be isolated from general user traffic.

### 22. Voice VLANs

Separate IP phone traffic for policy/QoS/security purposes.

### 23. Guest VLANs

Untrusted access typically limited to Internet and selected captive-portal/services.

### 24. Native VLAN

The VLAN associated with untagged traffic on a typical 802.1Q trunk; mismatches are risky.

### 25. VLAN Numbering Strategy

Use documented ranges/naming conventions that reflect site/function without becoming overly rigid.

### 26. VLAN-to-Subnet Mapping

A common design maps one IP subnet per VLAN.

```text
VLAN 10  USERS        10.10.10.0/24
VLAN 20  SERVERS      10.10.20.0/24
VLAN 30  MANAGEMENT   10.10.30.0/24
VLAN 40  VOICE        10.10.40.0/24
VLAN 50  GUEST        10.10.50.0/24
```
# Part 4 — VLAN Configuration

```cisco
vlan 10
 name USERS
vlan 20
 name SERVERS
vlan 30
 name MANAGEMENT
vlan 40
 name VOICE
vlan 50
 name GUEST

interface range g1/0/1-12
 switchport mode access
 switchport access vlan 10

interface g1/0/13
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 40

show vlan brief
```
# Part 5 — Trunking Advanced Concepts

### 27. IEEE 802.1Q

Adds VLAN tag information so multiple VLANs can share one Ethernet trunk.

### 28. VLAN Tagging

Tagged frames carry a VLAN identifier across trunks.

### 29. Native VLAN

Typically untagged on classic Cisco 802.1Q trunk behavior unless configured otherwise.

### 30. Trunk Negotiation

Some Cisco switch platforms support DTP negotiation; explicit trunk/access configuration is safer.

### 31. DTP Concept

Dynamic Trunking Protocol can negotiate trunking between compatible Cisco switches.

### 32. Allowed VLANs

Restrict which VLANs may traverse a trunk.

### 33. Trunk Security

Use explicit trunk mode, disable unnecessary DTP negotiation where supported, restrict allowed VLANs, and avoid using production access VLANs as native.

### 34. Native VLAN Mismatch

Two trunk ends using different native VLANs can leak/misclassify untagged traffic and generate warnings.

```cisco
interface g1/0/48
 description TRUNK-TO-DIST1
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,40,50,999
 switchport nonegotiate

show interfaces trunk
show interfaces g1/0/48 switchport
```
Command support varies by switch model/simulator. The design principle is explicit trunk configuration and a controlled allowed-VLAN list.
# Part 6 — Inter-VLAN Routing

### 35. Router-on-a-Stick Review

External router subinterfaces provide VLAN gateways through one trunk.

### 36. Layer-3 Switching

Multilayer switch routes directly between VLAN SVIs.

### 37. SVI

Logical Layer-3 interface for a VLAN.

### 38. Routed Ports

Physical port configured as Layer 3 rather than switchport.

```cisco
ip routing

interface vlan 10
 ip address 10.10.10.1 255.255.255.0
 no shutdown

interface vlan 20
 ip address 10.10.20.1 255.255.255.0
 no shutdown

interface g1/0/48
 no switchport
 ip address 10.255.0.1 255.255.255.252
 no shutdown
```
# Part 7 — Spanning Tree Protocol

### 39. Layer-2 Loops

Redundant Layer-2 links can create loops because Ethernet frames do not have a TTL field.

### 40. Broadcast Storms

Broadcast frames can circulate and multiply indefinitely in a loop, consuming bandwidth and switch CPU.

### 41. MAC Table Instability

The same source MAC appears on multiple ports as looped frames arrive, causing constant table relearning.

### 42. Duplicate Frames

Endpoints can receive multiple copies of the same frame.

### 43. STP

Spanning Tree Protocol logically blocks redundant Layer-2 paths to create a loop-free tree.

### 44. IEEE 802.1D

Original/common STP standard foundation.

### 45. Root Bridge

The switch elected as root of the spanning tree.

### 46. Root ID

Combination of bridge priority/system ID extension and MAC-related identifier.

### 47. Bridge Priority

Lower bridge ID wins root election; administrators manipulate priority to control root placement.

### 48. Root Port

Each non-root switch selects one best port toward the root.

### 49. Designated Port

Best forwarding port for a segment.

### 50. Blocked Port

A redundant port placed into non-forwarding state to prevent a Layer-2 loop.

### 51. Root Bridge Election

Lowest bridge ID becomes root.

### 52. Root Path Cost

Each switch computes total path cost toward the root.

### 53. Port Roles

Root, designated, alternate/blocking-related roles depend on STP variant.

### 54. Tie Breakers

When costs tie, STP uses bridge IDs and port identifiers according to the algorithm.

### 55. Blocking

Classic STP non-forwarding state used to prevent loops.

### 56. Listening

Classic STP transition state; processes BPDUs but does not learn user MACs or forward user frames.

### 57. Learning

Learns source MAC addresses but does not yet forward user frames.

### 58. Forwarding

Forwards user frames and learns MAC addresses.

### 59. Disabled

Interface not participating/administratively down.

### Why STP Is Necessary

```text
Without STP:

      SW1 ===== SW2
       |         |
       |         |
      SW3 ===== SW4

A broadcast can circulate around the square repeatedly.

With STP:
one redundant path is logically blocked,
creating a loop-free active topology.
```
### Root Bridge Configuration

```cisco
! Preferred root
spanning-tree vlan 10,20,30 root primary

! Backup root
spanning-tree vlan 10,20,30 root secondary

show spanning-tree
show spanning-tree vlan 10
```
# Part 8 — RSTP

### 60. Rapid Spanning Tree

RSTP improves convergence compared with classic STP.

### 61. IEEE 802.1w

Standard defining Rapid Spanning Tree behavior.

### 62. RSTP Port Roles

Root, designated, alternate, and backup roles.

### 63. Alternate Ports

Provide alternate path toward root and can transition rapidly under appropriate conditions.

### 64. Backup Ports

Backup path for a designated port on the same shared segment; uncommon in modern switched Ethernet.

### 65. Faster Convergence

RSTP uses proposal/agreement mechanisms and edge-port concepts to transition faster.

# Part 9 — Cisco STP Variants

### 66. PVST+

Cisco per-VLAN Spanning Tree implementation, running an STP instance per VLAN.

### 67. Rapid PVST+

Cisco per-VLAN implementation using RSTP behavior.

### 68. MST Introduction

Multiple Spanning Tree maps many VLANs to fewer STP instances, improving scalability in larger Layer-2 domains.

```cisco
spanning-tree mode rapid-pvst

show spanning-tree summary
```
# Part 10 — STP Optimization and Protection

### 69. Root Bridge Placement

Choose root switches near the logical Layer-2 center/gateway to align forwarding paths with design intent.

### 70. Primary Root

Preferred root under normal operation.

### 71. Secondary Root

Backup root if the primary fails.

### 72. PortFast

Treats an edge access port as edge, allowing rapid forwarding. Use only toward endpoints, not switches.

### 73. BPDU Guard

Disables/protects an edge port if BPDUs are received, helping stop accidental/unauthorized switches.

### 74. Root Guard

Prevents a port from becoming a path to an unexpected superior root bridge.

### 75. Loop Guard

Helps protect against certain unidirectional/STP BPDU-loss conditions that could otherwise cause a blocked port to incorrectly forward.

```cisco
interface range g1/0/1-24
 spanning-tree portfast
 spanning-tree bpduguard enable

interface g1/0/48
 spanning-tree guard root
```
Never enable PortFast blindly on an inter-switch link. Edge-port optimizations assume no switching loop can be introduced from that port.
# Part 11 — EtherChannel

### 76. Link Aggregation

Combines multiple physical links into one logical bundle.

### 77. Why EtherChannel

Adds bandwidth and redundancy while STP treats the bundle as one logical path.

### 78. Port Channel

Logical interface representing the aggregated members.

### 79. LACP

IEEE standards-based aggregation protocol. Common modes: active/passive.

### 80. PAgP

Cisco proprietary negotiation protocol on supported platforms.

### 81. Static EtherChannel

Manual bundle without negotiation; both ends must be configured consistently.

### 82. EtherChannel Load Balancing

Traffic is distributed using a hashing algorithm over selected header fields, not usually round-robin per packet.

### 83. Configuration Consistency

Member ports must agree on speed/duplex/trunk/access/VLAN and related settings or they may suspend/fail to bundle.

### LACP Example

```cisco
interface range g1/0/47-48
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 channel-group 1 mode active

interface port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30

show etherchannel summary
show interfaces port-channel 1
```
# Part 12 — First-Hop Redundancy

### 84. Gateway Failure Problem

If all hosts depend on one physical default gateway and it fails, inter-subnet communication stops.

### 85. First-Hop Redundancy Protocols

Provide a shared virtual gateway backed by multiple routers/switches.

### 86. HSRP

Cisco protocol using active and standby roles.

### 87. Active Router

Currently forwards for the virtual gateway.

### 88. Standby Router

Prepared to become active if needed.

### 89. Virtual IP

Shared gateway IP configured on hosts.

### 90. Virtual MAC

Shared MAC associated with the HSRP group.

### 91. HSRP Priority

Higher priority generally becomes active.

### 92. Preemption

Allows a higher-priority router to reclaim active role after recovery.

### 93. VRRP

Standards-based FHRP with master/backup roles.

### 94. GLBP Concept

Cisco FHRP that can provide gateway redundancy plus load sharing.

```cisco
interface vlan 10
 ip address 10.10.10.2 255.255.255.0
 standby 10 ip 10.10.10.1
 standby 10 priority 110
 standby 10 preempt

show standby brief
```
```text
Hosts:
Default gateway = 10.10.10.1

DIST1 real SVI = 10.10.10.2
DIST2 real SVI = 10.10.10.3
HSRP virtual    = 10.10.10.1
```
# Part 13 — Advanced Layer-3 Switching

### 95. Routed Access

Access switch uses Layer-3 uplinks rather than extending user VLANs through the distribution layer.

### 96. SVI Design

Gateways are placed where policy and failure-domain requirements dictate.

### 97. Routed Links

Point-to-point Layer-3 links eliminate STP dependence on uplinks.

### 98. Dynamic Routing on Multilayer Switches

OSPF can run between distribution/core/access switches when supported.

### 99. ECMP

Multiple equal Layer-3 paths can be installed for redundancy and capacity.

```text
Routed-access design:

        CORE1 ===== CORE2
          | \       / |
          |  \     /  |
         ACC1     ACC2

Access uplinks are Layer 3.
User VLANs stay local to each access block.
OSPF/ECMP handles redundant paths.
```
# Part 14 — Switch Security

### 100. Port Security

Limits/controls which source MAC addresses may use an access port.

### 101. Maximum MAC Addresses

Defines how many secure MAC addresses can be learned/configured.

### 102. Sticky MAC

Dynamically learns secure MAC addresses and adds them to running configuration on supported Cisco switches.

### 103. Violation Modes

Actions when an unauthorized/extra MAC appears.

### 104. Shutdown

Typically error-disables the port on violation.

### 105. Restrict

Drops violating traffic and records/increments violation counters.

### 106. Protect

Drops violating traffic with less notification than restrict.

### 107. DHCP Snooping

Switch validates DHCP messages and builds a binding table from trusted server-facing and untrusted client-facing ports.

### 108. Rogue DHCP Problem

Unauthorized DHCP server can provide malicious gateway/DNS settings.

### 109. Trusted Ports

Ports where legitimate DHCP server messages are accepted.

### 110. Untrusted Ports

Client-facing ports where server-type DHCP responses should be blocked.

### 111. Binding Database

Tracks client MAC, IP, VLAN, port, and lease information.

### 112. Dynamic ARP Inspection

Validates ARP messages, commonly using DHCP Snooping bindings.

### 113. ARP Spoofing Problem

Attackers can send false ARP mappings to redirect traffic.

### 114. DAI

Drops invalid ARP according to bindings/validation policy.

### 115. DHCP Snooping Dependency

DAI commonly relies on DHCP Snooping binding information for dynamically addressed hosts.

### 116. Trusted Interfaces

Uplinks/server-facing interfaces can be marked trusted where appropriate.

### 117. IP Source Guard

Restricts IP source addresses on access ports using binding information.

### 118. Source Address Validation

Prevents an endpoint from simply using an unauthorized source IP.

### 119. VLAN Hopping

Category of attacks attempting to access traffic in other VLANs.

### 120. Switch Spoofing

A device attempts to negotiate a trunk and gain access to multiple VLANs.

### 121. Double Tagging

Attack concept involving nested 802.1Q tags and native-VLAN behavior.

### 122. Storm Control

Limits broadcast/multicast/unknown-unicast rates to protect switch/network resources.

### 123. Broadcast/Multicast/Unknown-Unicast Control

Storm-control thresholds can be applied to one or more traffic types depending on platform.

### Port Security Example

```cisco
interface g1/0/10
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict

show port-security interface g1/0/10
```
### DHCP Snooping Example

```cisco
ip dhcp snooping
ip dhcp snooping vlan 10,20

interface g1/0/48
 ip dhcp snooping trust

interface range g1/0/1-24
 ip dhcp snooping limit rate 20

show ip dhcp snooping
show ip dhcp snooping binding
```
### DAI Example

```cisco
ip arp inspection vlan 10,20

interface g1/0/48
 ip arp inspection trust

show ip arp inspection
```
### IP Source Guard Example

```cisco
interface g1/0/10
 ip verify source
```
Feature syntax/support varies. Apply these controls only after understanding static-IP devices, DHCP relay paths, trusted ports, and operational exceptions.
# Part 15 — Network Management

### 124. Management VLAN

Dedicated segment for switch/router management interfaces.

### 125. SSH Management

Encrypted remote CLI administration; disable Telnet in normal secure deployments.

### 126. SNMP

Monitoring/management protocol; SNMPv3 adds authentication/privacy.

### 127. Syslog

Central logging for events and troubleshooting.

### 128. NTP

Time synchronization across network devices.

### 129. AAA Introduction

Centralized Authentication, Authorization, and Accounting using systems such as RADIUS/TACACS+.

### 130. Configuration Backup

Maintain versioned, secure backups and restore procedures for network-device configuration.

```cisco
interface vlan 30
 ip address 10.10.30.11 255.255.255.0
 no shutdown

ip default-gateway 10.10.30.1

ip domain-name corp.example
username netadmin privilege 15 secret <strong-secret>
crypto key generate rsa

line vty 0 4
 login local
 transport input ssh

logging host 10.10.30.50
ntp server 10.10.30.60
```
# Part 16 — High Availability Design

### 131. Device Redundancy

Deploy redundant switches/routers where outage impact justifies it.

### 132. Link Redundancy

Use alternate links, EtherChannel, or routed ECMP.

### 133. Gateway Redundancy

Use HSRP/VRRP/GLBP or equivalent designs.

### 134. Power Redundancy

Dual PSUs, UPS, and diverse power feeds can protect against infrastructure failure.

### 135. Layer-2 vs Layer-3 Redundancy

Layer-2 redundancy depends on loop prevention; Layer-3 redundancy can use routing convergence/ECMP and often scales more predictably.

### 136. Failure Domains

Keep VLAN/STP and fault domains no larger than required.

# Part 17 — Campus Design

### 137. Small Campus

Often uses collapsed core/distribution with a small number of access switches.

### 138. Medium Campus

May use redundant distribution switches and multiple access blocks.

### 139. Enterprise Campus

Uses hierarchy, redundancy, routed boundaries, centralized services, automation, monitoring, and consistent policy.

### 140. Data Center Access Considerations

Server access emphasizes redundancy, high bandwidth, east-west traffic, virtualization integration, and often different architectures from user campus.

### 141. Wireless Integration

APs connect through access switches; SSIDs commonly map to VLANs/central policy.

### 142. Voice Networks

Phones may use voice VLANs, PoE, QoS, DHCP options, and call-control services.

### 143. IoT Segmentation

IoT endpoints should be segmented because they often have limited security capabilities and unusual traffic requirements.

### Example Medium Campus

```text
CORE/DIST1 ===== CORE/DIST2
                    /    \          /    \
                  ACC1   ACC2      ACC3   ACC4
                   |       |        |      |
                 Users    APs     Voice   IoT

VLANs:
10 Users
20 Voice
30 Wireless-Corp
40 Guest
50 IoT
99 Management

Design questions:
- Where are gateways?
- Which VLANs span multiple access switches?
- Which uplinks are L2 trunks vs L3 routed?
- Which switch is STP root?
- Which access ports require DHCP Snooping/DAI?
```
# Part 18 — Switching Troubleshooting

### 144. VLAN Mismatch

Endpoint/access port assigned to wrong VLAN or VLAN missing.

### 145. Trunk Failure

Port not trunking, negotiation mismatch, or physical/link issue.

### 146. Allowed VLAN Error

Required VLAN absent from trunk allowed list.

### 147. Native VLAN Mismatch

Trunk ends assign different VLANs to untagged traffic.

### 148. STP Blocking Unexpected Port

Root placement or path cost causes a different link to block than intended.

### 149. EtherChannel Failure

Member interfaces differ in trunk/access/VLAN/speed/channel protocol settings.

### 150. HSRP Failure

Priority, preemption, virtual IP/group, tracking, or Layer-2 reachability problems.

### 151. Port Security Violation

Unexpected MAC count/address triggers configured action.

### 152. DHCP Snooping Problems

Legitimate DHCP server messages may be blocked because the uplink/server port is not trusted or VLAN is missing from snooping config.

### 153. MAC Address Table Troubleshooting

Use MAC learning to determine where a device is seen and whether frames follow expected VLAN/port paths.

### Core Switching Verification Commands

```cisco
show vlan brief
show interfaces trunk
show interfaces switchport
show spanning-tree
show spanning-tree vlan 10
show etherchannel summary
show interfaces port-channel 1
show mac address-table
show standby brief
show port-security
show port-security interface g1/0/10
show ip dhcp snooping
show ip dhcp snooping binding
show ip arp inspection
show ip interface brief
show ip route
```
### Wireshark Switching Analysis

Useful packet types to inspect:

- ARP
- 802.1Q VLAN tags
- STP/RSTP BPDUs
- DHCP Discover/Offer/Request/Ack
- ICMP
- HSRP where your capture environment exposes it

Example display filters:

```text
arp
stp
vlan
bootp
icmp
```

Wireshark commonly labels DHCPv4 traffic under the BOOTP dissector/filter name.

# Enhanced Engineering Layer — Advanced Switching and Campus Design

The original switching course already covers hierarchy, VLANs, trunks, STP/RSTP, EtherChannel, HSRP, routed access, DHCP Snooping, DAI, IP Source Guard, management, high availability, and troubleshooting. This enhanced layer adds the deeper campus-design, STP mechanics, Layer-2 protection, FHRP tracking, NAC, QoS, multicast, telemetry, high-availability, and automation concepts needed for enterprise operations and network security.

Use these five models.

## Model 1 — Campus Hierarchy

```text
Endpoints
   ↓
Access
   ↓
Distribution
   ↓
Core
   ↓
WAN / Data Center / Internet
```

## Model 2 — Layer-2 Loop Control

```text
Physical redundancy
      ↓
STP/RSTP computes logical tree
      ↓
one forwarding path per loop condition
      ↓
backup path retained
```

## Model 3 — Access Security

```text
Endpoint
   ↓
802.1X / MAB
   ↓
Access VLAN / Voice VLAN
   ↓
DHCP Snooping
   ↓
DAI / IP Source Guard
   ↓
ACL / routed policy
```

## Model 4 — Gateway Resilience

```text
Host default gateway = Virtual IP
             ↓
      HSRP/VRRP group
       /            \
 real gateway A   real gateway B
```

## Model 5 — Troubleshooting

```text
Physical link
   ↓
port mode
   ↓
VLAN
   ↓
trunk allowed/native
   ↓
STP state
   ↓
EtherChannel state
   ↓
gateway/FHRP
   ↓
routing
   ↓
security feature
```


### Enhanced Deep Dive — Access–Distribution–Core Responsibilities

The three campus layers should have different responsibilities.

**Access**
Endpoint connectivity and edge policy.

**Distribution**
Layer-3 boundary, summarization, FHRP, policy aggregation, failure isolation.

**Core**
Fast resilient transport with minimal unnecessary complexity.

#### Diagram / Mental Model

```text
Users/APs/Phones
      ↓
ACCESS
VLAN/NAC/PoE
      ↓
DISTRIBUTION
L3 gateways/policy
      ↓
CORE
fast routed transit
```

#### Why It Works / Why It Matters

Mixing every policy/function into every layer makes failures harder to isolate.



### Enhanced Deep Dive — Layer-2 Access vs Routed Access

A traditional campus can extend VLANs from access to distribution using trunks. A routed-access design moves the Layer-3 boundary down to the access switch and uses routed uplinks.

**Layer-2 access**
- FHRP at distribution
- STP controls redundant access uplinks
- VLANs can span access switches

**Routed access**
- user VLANs remain local
- OSPF/ECMP handles uplink redundancy
- smaller STP domains

#### Diagram / Mental Model

```text
L2 Access:
ACC ==trunks== DIST pair

Routed Access:
ACC ==L3/OSPF== DIST/Core
```

#### Why It Works / Why It Matters

Routed access reduces Layer-2 failure scope but requires capable access switching and routing design.



### Enhanced Deep Dive — Collapsed Core Trade-Off

A collapsed core combines distribution and core roles.

Benefits:
- fewer devices
- lower cost
- simpler topology

Trade-offs:
- larger impact when the combined layer fails
- capacity and policy concentration

#### Design Note

Use it when scale and availability requirements fit; do not copy a three-tier diagram merely because it looks more enterprise.



### Enhanced Deep Dive — Stacking and Multi-Chassis Systems Awareness

Enterprise switches can operate as logical systems using vendor technologies such as Cisco StackWise, StackWise Virtual, VSS, or other multi-chassis mechanisms.

Benefits can include:
- simplified management
- multi-chassis EtherChannel
- reduced STP blocking
- supervisor/control redundancy

Failure behavior differs by technology.

#### Why It Works / Why It Matters

Two physical chassis do not automatically mean two independent control planes.



### Enhanced Deep Dive — MLAG / Multi-Chassis EtherChannel Concept

Multi-chassis link aggregation lets one downstream device form one logical port-channel across two physical upstream switches when the platform supports a multi-chassis system.

This can provide active/active Layer-2 forwarding.

#### Diagram / Mental Model

```text
DIST1 ===== DIST2
   \           /
    \         /
     \       /
      ACC1
one logical LAG
```

#### Why It Works / Why It Matters

This avoids STP blocking one of the uplinks while retaining chassis redundancy.



### Enhanced Deep Dive — VTP Awareness

Cisco VLAN Trunking Protocol can distribute VLAN database information between switches.

Because a mistake can propagate VLAN changes, many environments either use transparent/off designs or tightly controlled modern VTP deployment.

#### Security Implication

Do not enable VLAN-distribution mechanisms casually on production trunks.



### Enhanced Deep Dive — VLAN Pruning

A VLAN should traverse only trunks where it is actually required.

Restricting VLAN propagation:
- reduces broadcast/flood scope
- reduces attack surface
- simplifies troubleshooting

#### Cisco IOS / IOS XE Example

```cisco
interface g1/0/48
 switchport trunk allowed vlan 10,20,99
```

#### Why It Works / Why It Matters

An allowed-VLAN list is both an operational and security boundary.



### Enhanced Deep Dive — Private VLAN Awareness

Private VLANs provide Layer-2 isolation among ports inside the same primary VLAN structure using isolated/community roles on supported platforms.

They are useful where endpoints share an IP subnet but should not freely communicate at Layer 2.

#### Diagram / Mental Model

```text
Primary VLAN
├─ Promiscuous port → gateway
├─ Isolated hosts ─X─ each other
└─ Community hosts ↔ same community
```

#### Why It Works / Why It Matters

PVLANs solve a specific L2 isolation problem and do not replace Layer-3 firewall policy.



### Enhanced Deep Dive — Q-in-Q Awareness

802.1Q tunneling (Q-in-Q) can encapsulate a customer's VLAN tag inside a provider/service VLAN tag.

It is common in provider/metro Ethernet contexts rather than ordinary campus access.

#### Diagram / Mental Model

```text
Customer frame
[ C-tag ][payload]
      ↓ provider adds
[ S-tag ][ C-tag ][payload]
```

#### Why It Works / Why It Matters

Nested VLAN tags are legitimate in some designs; not every double-tagged frame is an attack.



### Enhanced Deep Dive — STP Bridge ID in Detail

The bridge ID combines a configurable bridge priority plus system-ID extension information and a MAC-related identifier.

The lowest bridge ID becomes root.

#### Diagram / Mental Model

```text
Bridge ID
├─ priority / extended system ID
└─ bridge MAC identifier
```

#### Why It Works / Why It Matters

If priorities tie, MAC-related values can decide the root unintentionally.



### Enhanced Deep Dive — STP Root Election Determinism

Do not allow the lowest factory MAC address to choose your campus root.

Place primary/secondary root intentionally near the Layer-3 gateway/distribution role.

#### Cisco IOS / IOS XE Example

```cisco
spanning-tree vlan 10,20 root primary
spanning-tree vlan 10,20 root secondary
```

#### Why It Works / Why It Matters

Predictable root placement produces predictable traffic paths.



### Enhanced Deep Dive — STP Path Cost

Each STP interface has a path cost related to link speed under the selected cost method. A switch adds costs along the path to determine total root-path cost.

Lower total cost wins.

#### Diagram / Mental Model

```text
SW3 → SW2 → ROOT
 cost 4 + 4 = 8

SW3 → SW1 → ROOT
 cost 19 + 4 = 23

SW3 selects first path.
```

#### Why It Works / Why It Matters

STP chooses a logical tree using cost, not hop count alone.



### Enhanced Deep Dive — STP Root-Port Tie Breakers

If two candidate root paths have equal cost, STP uses deterministic tie-breakers such as upstream bridge ID and port identifiers.

The exact sequence follows STP algorithm rules.

#### Why It Works / Why It Matters

When the wrong link becomes root port despite equal bandwidth, inspect bridge/port IDs.



### Enhanced Deep Dive — Designated Port Election

For each shared segment, the switch advertising the best BPDU toward the root becomes designated for that segment.

The root bridge's active ports are designated ports in ordinary operation.

#### Why It Works / Why It Matters

Root port is chosen per non-root switch; designated port is chosen per segment.



### Enhanced Deep Dive — Classic STP States vs RSTP States

Classic STP:
- blocking
- listening
- learning
- forwarding
- disabled

RSTP simplifies operational states to:
- discarding
- learning
- forwarding

RSTP uses port roles and proposal/agreement behavior to converge faster.

#### Why It Works / Why It Matters

Do not mix classic state names with RSTP role terminology.



### Enhanced Deep Dive — RSTP Proposal/Agreement

RSTP can rapidly transition point-to-point links by using a proposal/agreement handshake instead of waiting through classic timer-driven listening/learning transitions.

This works only when the topology is safe to transition.

#### Diagram / Mental Model

```text
Switch A ---- proposal ----> Switch B
Switch A <--- agreement ---- Switch B
             ↓
rapid forwarding transition
```

#### Why It Works / Why It Matters

RSTP convergence is topology- and role-aware, not merely 'shorter timers'.



### Enhanced Deep Dive — RSTP Edge Port

An RSTP edge port connects to an endpoint and can enter forwarding immediately.

Cisco PortFast provides this edge behavior.

#### Security Implication

An edge port that receives BPDUs should be treated as suspicious or miswired; pair PortFast with BPDU Guard where appropriate.



### Enhanced Deep Dive — RSTP Link Types Awareness

RSTP behavior distinguishes point-to-point full-duplex links from shared links because rapid proposal/agreement requires a predictable two-switch relationship.

#### Why It Works / Why It Matters

Duplex and topology affect convergence semantics.



### Enhanced Deep Dive — Topology Change Behavior

STP/RSTP topology changes influence MAC-table aging/learning so switches can quickly forget paths that are no longer correct.

Excessive topology changes can cause repeated flooding and performance instability.

#### Cisco IOS / IOS XE Example

```cisco
show spanning-tree detail
```

#### Why It Works / Why It Matters

A topology-change counter increasing rapidly is evidence of unstable edge/link behavior.



### Enhanced Deep Dive — Rapid-PVST+

Rapid-PVST+ runs an RSTP-like instance per VLAN.

Advantages:
- per-VLAN root placement
- rapid convergence

Trade-off:
- many VLANs mean many STP instances/control state.

#### Why It Works / Why It Matters

This motivates MST in larger Layer-2 environments.



### Enhanced Deep Dive — MST Region

Multiple Spanning Tree maps many VLANs into a smaller number of STP instances.

Switches must agree on region parameters such as:
- region name
- revision
- VLAN-to-instance mapping

#### Diagram / Mental Model

```text
VLANs 10,20,30 → MST instance 1
VLANs 40,50    → MST instance 2
```

#### Why It Works / Why It Matters

MST scales better than one STP instance per VLAN in large Layer-2 networks.



### Enhanced Deep Dive — MST Region Mismatch

If neighboring switches disagree on MST region configuration, they behave as separate regions/boundaries.

This can create unexpected root/path behavior.

#### Troubleshooting

Verify region name, revision, and VLAN-to-instance mapping exactly.



### Enhanced Deep Dive — Root Guard

Root Guard protects designated/downstream-facing ports from accepting a superior BPDU that would move the STP root through that port.

The port enters a root-inconsistent condition while superior BPDUs continue.

#### Security Implication

Use on ports where the root must never appear, such as access-facing/downstream links according to the design.



### Enhanced Deep Dive — Loop Guard

Loop Guard protects against certain unidirectional/BPDU-loss conditions where a non-designated port might otherwise transition to forwarding.

It is typically used on non-edge point-to-point switch links where BPDUs are expected.

#### Why It Works / Why It Matters

Root Guard and Loop Guard solve different STP failure modes.



### Enhanced Deep Dive — BPDU Filter Awareness

BPDU Filter suppresses/filters BPDUs under certain configurations.

Because it can effectively remove STP protection and create loops, it is dangerous when misunderstood.

#### Security Implication

Do not use BPDU filtering simply to make an STP warning disappear.



### Enhanced Deep Dive — UDLD Awareness

Unidirectional Link Detection can detect a fiber/Ethernet condition where one direction works but the reverse does not.

This is important because STP assumes bidirectional BPDU exchange.

#### Diagram / Mental Model

```text
SW1 TX ----> SW2 RX works
SW1 RX <---- SW2 TX broken

link may appear partially up
```

#### Why It Works / Why It Matters

Unidirectional links can create severe STP failures.



### Enhanced Deep Dive — Bridge Assurance Awareness

Bridge Assurance is a Cisco high-availability STP protection mechanism on supported platforms that expects BPDUs on certain network ports and can block a port if they disappear.

It complements loop-prevention designs in specific topologies.

#### Why It Works / Why It Matters

Platform-specific high-availability protections should match the intended inter-switch topology.



### Enhanced Deep Dive — Storm Control in Depth

Storm control monitors broadcast, multicast, and/or unknown-unicast traffic levels and takes action when configured thresholds are exceeded.

It protects the switch/network from traffic storms but can also drop legitimate bursts if thresholds are too low.

#### Cisco IOS / IOS XE Example

```cisco
interface g1/0/10
 storm-control broadcast level 1.00 0.50
```

#### Design Note

Threshold syntax and units vary by platform.



### Enhanced Deep Dive — Errdisable

Cisco switches can place a port into an error-disabled state after protection events such as BPDU Guard or port-security violations.

Troubleshooting requires identifying the **reason**, not just re-enabling the port.

#### Cisco IOS / IOS XE Example

```cisco
show interfaces status err-disabled
show errdisable recovery
```

#### Why It Works / Why It Matters

Automatic recovery without correcting root cause can repeatedly reintroduce the fault.



### Enhanced Deep Dive — EtherChannel Negotiation Matrix

For LACP:
- active + active → forms
- active + passive → forms
- passive + passive → does not negotiate

For PAgP:
- desirable + desirable → forms
- desirable + auto → forms
- auto + auto → does not negotiate

Static `on` requires exact manual consistency.

#### Why It Works / Why It Matters

Both ends must have compatible channel intent.



### Enhanced Deep Dive — LACP System and Port Priority Awareness

LACP has system and port priority mechanisms used when deciding which links participate when more candidates exist than the bundle allows.

These are advanced tuning tools rather than ordinary first-line configuration.

#### Why It Works / Why It Matters

Know they exist before troubleshooting why a member stays standby/inactive.



### Enhanced Deep Dive — EtherChannel Member Consistency

Member links must be compatible for attributes such as:
- switchport mode
- access VLAN
- native VLAN
- allowed VLANs
- speed/duplex where required
- channel protocol/mode

Configuration belongs preferably on the Port-Channel logical interface after formation, while member settings remain consistent.

#### Troubleshooting

Use `show etherchannel summary`, interface details, and consistency messages.



### Enhanced Deep Dive — Routed EtherChannel

A Port-Channel can also be a Layer-3 routed interface.

This bundles physical routed links and removes STP/VLAN trunking from that uplink.

#### Cisco IOS / IOS XE Example

```cisco
interface range g1/0/47-48
 no switchport
 channel-group 10 mode active

interface port-channel10
 no switchport
 ip address 10.255.0.1 255.255.255.252
```

#### Why It Works / Why It Matters

Routed port-channels are common in resilient distribution/core designs.



### Enhanced Deep Dive — EtherChannel Load-Balancing Hash

A switch does not normally split every packet evenly across members. It hashes selected fields such as source/destination MAC/IP/ports depending on platform.

One large flow may therefore use only one physical member.

#### Why It Works / Why It Matters

Bundle capacity is aggregate across multiple flows, not guaranteed per single flow.



### Enhanced Deep Dive — Minimum Links Awareness

Some platforms can require a minimum number of active members before the Port-Channel is considered usable.

This prevents a heavily loaded bundle from continuing with insufficient capacity.

#### Design Note

Capacity protection must be balanced against availability requirements.



### Enhanced Deep Dive — HSRP Versions Awareness

Cisco HSRP has multiple versions with differences including group-number ranges and virtual-MAC behavior.

Use the platform/version intended by the deployment and keep both peers consistent.

#### Why It Works / Why It Matters

Version mismatch can prevent proper group formation.



### Enhanced Deep Dive — HSRP Hello/Hold Timers

HSRP peers exchange Hellos and use hold timers to detect peer failure.

Timers can be tuned, but aggressive values increase control-plane sensitivity.

#### Cisco IOS / IOS XE Example

```cisco
show standby
show standby brief
```

#### Why It Works / Why It Matters

Failure detection is part of convergence, just like routing protocol timers.



### Enhanced Deep Dive — HSRP Object Tracking

A gateway can remain alive on the client VLAN but lose its upstream/core route.

Object/interface tracking can reduce HSRP priority so the healthier peer becomes active.

#### Diagram / Mental Model

```text
DIST1 SVI up
DIST1 core uplink down
       ↓ track
priority decreases
       ↓
DIST2 becomes active
```

#### Why It Works / Why It Matters

FHRP should protect actual end-to-end gateway usefulness, not only device power.



### Enhanced Deep Dive — Align STP Root with HSRP Active

In a Layer-2 access design, align the HSRP active gateway with the STP root for that VLAN.

Otherwise, traffic can cross the inter-distribution link unnecessarily.

#### Diagram / Mental Model

```text
BAD:
ACC → STP root DIST1 → L2 crosslink → HSRP active DIST2

GOOD:
ACC → STP root + HSRP active on same DIST
```

#### Why It Works / Why It Matters

This reduces hairpinning and makes failure behavior easier to reason about.



### Enhanced Deep Dive — Per-VLAN Gateway Load Sharing

With Rapid-PVST+/HSRP, VLAN groups can use different preferred roots/active gateways.

Example:
- VLANs 10,30 → DIST1 active/root
- VLANs 20,40 → DIST2 active/root

This balances traffic while retaining deterministic paths.

#### Why It Works / Why It Matters

Do not randomly split roots/gateways; document the VLAN-to-device ownership.



### Enhanced Deep Dive — VRRP and GLBP Comparison Awareness

VRRP provides standards-based master/backup first-hop redundancy.

GLBP is Cisco-specific and can provide FHRP redundancy plus gateway load balancing.

Availability, licensing, and platform support vary.

#### Why It Works / Why It Matters

Choose FHRP based on interoperability and operational needs.



### Enhanced Deep Dive — Anycast Gateway Awareness

Modern data-center/fabric designs can use the same default-gateway IP/MAC on multiple leaf devices, often integrated with VXLAN EVPN.

This differs from active/standby HSRP.

#### Diagram / Mental Model

```text
Host in Rack A → local leaf gateway
Host in Rack B → local leaf gateway

same anycast gateway identity
```

#### Why It Works / Why It Matters

This is a bridge toward data-center fabrics, not a replacement for campus HSRP without supporting architecture.



### Enhanced Deep Dive — Routed Access and ECMP

With routed access, each access switch can have two equal-cost Layer-3 uplinks.

OSPF/IS-IS/EIGRP-style routing handles redundancy and can use both links actively.

#### Diagram / Mental Model

```text
DIST1       DIST2
   \         /
    \       /
      ACC
 L3 ECMP uplinks
```

#### Why It Works / Why It Matters

This removes the need for STP to block one redundant uplink.



### Enhanced Deep Dive — IPv6 on Multilayer Switching

SVIs and routed ports can support IPv6 just as IPv4.

Gateway design must account for:
- Router Advertisements
- NDP
- IPv6 ACLs
- first-hop redundancy support
- multicast dependency

#### Security Implication

Do not block all ICMPv6; NDP and PMTUD depend on it.



### Enhanced Deep Dive — DHCP Snooping Binding Contents

A DHCP Snooping binding commonly records:
- MAC
- assigned IP
- lease
- VLAN
- switchport

DAI and IP Source Guard can use this binding as a source of truth.

#### Diagram / Mental Model

```text
DHCP ACK
   ↓
Snooping switch
   ↓
binding:
MAC ↔ IP ↔ VLAN ↔ port
```

#### Why It Works / Why It Matters

Binding quality determines downstream anti-spoofing accuracy.



### Enhanced Deep Dive — DHCP Snooping Option 82 Awareness

A relay/snooping device can insert DHCP Option 82 circuit/relay information to identify where a request entered the access network.

DHCP servers can use it for policy/assignment.

#### Why It Works / Why It Matters

Option 82 is useful in enterprise/provider access networks but must be trusted and handled consistently end to end.



### Enhanced Deep Dive — DHCP Snooping Rate Limiting

Client-facing ports can rate-limit DHCP messages to reduce starvation/flood behavior.

Thresholds must allow legitimate boot/retry bursts.

#### Cisco IOS / IOS XE Example

```cisco
interface g1/0/10
 ip dhcp snooping limit rate 20
```

#### Security Implication

Rate limiting is a mitigation, not an authentication mechanism.



### Enhanced Deep Dive — DHCP Snooping Database Persistence Awareness

Some platforms can persist snooping bindings so a reboot does not temporarily remove the information DAI/IP Source Guard rely on.

Implementation details are platform-specific.

#### Why It Works / Why It Matters

Access security should survive planned/unplanned switch restart where possible.



### Enhanced Deep Dive — DAI with Static IP Hosts

A static-IP endpoint may not exist in the DHCP Snooping binding database.

DAI designs may require:
- static bindings
- ARP ACLs
- trusted paths
- alternative NAC/policy

Do not simply disable DAI globally when one static device fails.

#### Why It Works / Why It Matters

Security controls need an exception process.



### Enhanced Deep Dive — IP Source Guard

IP Source Guard restricts source IP/MAC behavior at the access port using binding/policy information.

It reduces simple source-IP spoofing from edge devices.

#### Security Implication

It complements routed ACLs/firewalls; it does not authenticate the application/user by itself.



### Enhanced Deep Dive — Port Security Limitations

Port security is useful for simple MAC limits but has limitations in modern endpoint environments:
- phones plus PCs
- hypervisors/VMs
- docking stations
- virtual desktops
- MAC randomization
- device replacement

802.1X/NAC provides stronger identity-based access control.

#### Why It Works / Why It Matters

Do not use MAC count as a complete identity system.



### Enhanced Deep Dive — 802.1X, MAB, and NAC

Enterprise access control can authenticate a device/user before granting network access.

**802.1X**
Uses EAP through the switch/AP authenticator to RADIUS.

**MAB**
Uses the device MAC as a fallback identity for devices that cannot perform 802.1X.

**NAC**
Applies identity, device, posture, role, and policy decisions.

#### Diagram / Mental Model

```text
Endpoint
 ↓ 802.1X / MAB
Access switch
 ↓ RADIUS
Identity/NAC platform
 ↓
VLAN / ACL / role
```

#### Security Implication

MAB is weaker because MAC addresses can be copied/spoofed; use it for constrained device classes with additional controls.



### Enhanced Deep Dive — Dynamic VLAN / Downloadable ACL Awareness

NAC/RADIUS systems can assign network access dynamically, such as:
- VLAN
- downloadable ACL
- security role
- session policy

The physical port no longer needs one permanently assigned trust level.

#### Why It Works / Why It Matters

This is how identity becomes network policy.



### Enhanced Deep Dive — VLAN Hopping Defense

Defensive switching practices include:
- explicit access mode on edge ports
- disable DTP where appropriate
- restrict allowed VLANs
- dedicated unused native VLAN
- do not use user VLAN as native
- shut unused ports

#### Security Implication

These controls reduce switch-spoofing/double-tagging opportunities.



### Enhanced Deep Dive — MAC Flooding Defense Context

Modern switches have finite MAC-table resources. Excessive source MAC churn can create forwarding pressure.

Defenses can include:
- port security
- storm/control-plane protections
- access authentication
- monitoring MAC move/churn events

#### Security Implication

Practice only in isolated authorized labs; do not intentionally exhaust production switch tables.



### Enhanced Deep Dive — MAC Move and Flap Detection

The same MAC repeatedly appearing on different ports can indicate:
- physical loop
- virtualization mobility
- misconfigured port-channel
- duplicate MAC
- malicious/abnormal behavior

#### Cisco IOS / IOS XE Example

```cisco
show mac address-table
show logging
```

#### Why It Works / Why It Matters

Interpret MAC moves in topology context before assuming an attack.



### Enhanced Deep Dive — IGMP Snooping

IGMP Snooping lets a Layer-2 switch observe IPv4 multicast membership signaling and forward multicast only toward interested ports instead of flooding it everywhere.

IPv6 has corresponding multicast-listener mechanisms.

#### Diagram / Mental Model

```text
Multicast source
      ↓
Switch with IGMP Snooping
   ├─ interested port → forward
   └─ non-member port → avoid flooding
```

#### Why It Works / Why It Matters

Multicast control is important for video, discovery, and some enterprise applications.



### Enhanced Deep Dive — Unknown Multicast Handling

When membership state is unknown, switch behavior depends on platform/configuration and multicast design.

Do not assume all multicast is always flooded exactly like broadcast.

#### Why It Works / Why It Matters

Troubleshooting multicast requires both Layer-2 snooping and Layer-3 multicast-routing awareness.



### Enhanced Deep Dive — QoS Trust Boundary

Access switches often define where QoS markings become trusted.

An IP phone can be trusted for voice markings while an attached PC may be remarked/classified differently.

#### Diagram / Mental Model

```text
PC → Phone → Switch
      voice DSCP trusted?
      PC DSCP trusted?
         ↓
QoS policy
```

#### Security Implication

Endpoints should not automatically be allowed to mark arbitrary traffic as highest priority.



### Enhanced Deep Dive — Voice VLAN and LLDP-MED/CDP

IP phones can learn voice-related network information from mechanisms such as CDP or LLDP-MED depending on vendor/platform.

This supports:
- voice VLAN
- PoE information
- network policy

#### Why It Works / Why It Matters

The switch edge is both a data and device-discovery/control point.



### Enhanced Deep Dive — PoE Budget and Redundancy

Access switches power phones/APs/cameras using PoE.

Design must consider:
- per-port requirement
- total switch power budget
- PSU redundancy
- UPS/generator runtime

#### Why It Works / Why It Matters

A switch can stay logically up while attached APs/phones lose power due to insufficient PoE budget.



### Enhanced Deep Dive — Jumbo Frames and MTU Consistency

Some campus/data-center segments use MTUs above 1500.

Every device/link in the path must support the intended frame/packet size.

#### Troubleshooting

A mismatched MTU can cause large transfers to fail while small pings succeed.



### Enhanced Deep Dive — Microbursts and Buffering Awareness

A microburst is a short high-rate traffic burst that can overflow switch egress buffers even when average utilization appears low.

Symptoms:
- output drops
- transient packet loss
- TCP retransmissions

#### Why It Works / Why It Matters

Average link utilization can hide instantaneous congestion.



### Enhanced Deep Dive — Switch Queueing Awareness

QoS queues determine which traffic waits or drops under egress congestion.

Enterprise switching can use:
- priority queues
- weighted queues
- shaping/policing
- congestion avoidance depending on platform

#### Why It Works / Why It Matters

QoS matters primarily when there is contention.



### Enhanced Deep Dive — SPAN, RSPAN, and ERSPAN

Switch port analyzers mirror traffic for packet capture.

**SPAN**
local mirror.

**RSPAN**
mirror across a dedicated Layer-2 VLAN.

**ERSPAN**
encapsulates mirrored traffic over Layer 3 on supported platforms.

#### Diagram / Mental Model

```text
Source port/VLAN
      ↓
Switch mirror
      ↓
Analyzer/Wireshark
```

#### Security Implication

Packet captures can contain credentials/data. Restrict who can configure or receive mirrored traffic.



### Enhanced Deep Dive — MACsec Awareness

MACsec (IEEE 802.1AE) can provide Layer-2 encryption/integrity on supported Ethernet links.

It is useful for protecting traffic across untrusted/shared physical Ethernet segments.

#### Why It Works / Why It Matters

MACsec protects a link; it does not replace application encryption or access control.



### Enhanced Deep Dive — Out-of-Band vs In-Band Management

**In-band management**
Uses the production network.

**Out-of-band management**
Uses a separate management network/console path.

OOB management can remain available during production routing/switching failures.

#### Diagram / Mental Model

```text
Production:
Admin → campus → switch mgmt IP

OOB:
Admin → management network → console/OOB port
```

#### Security Implication

Critical infrastructure benefits from management paths isolated from user traffic.



### Enhanced Deep Dive — Management VRF Awareness

A management VRF isolates management routing from production routing on supported switches.

This reduces accidental reachability between user traffic and device-control interfaces.

#### Why It Works / Why It Matters

Management separation should exist at both VLAN and routing-table/policy levels when appropriate.



### Enhanced Deep Dive — AAA with TACACS+/RADIUS

Centralized AAA improves accountability and removes dependence on shared local administrator passwords.

For device administration, organizations commonly use TACACS+ or RADIUS according to policy/platform.

#### Security Implication

Keep an emergency local account through a controlled break-glass process.



### Enhanced Deep Dive — Configuration Archive and Rollback

Switch configuration changes should be versioned.

A safe process:
- save pre-change config
- record diff
- define rollback
- apply
- verify
- save startup config

#### Why It Works / Why It Matters

A trunk/STP change can instantly remove remote management access.



### Enhanced Deep Dive — SNMPv3 and Telemetry

SNMPv3 provides authenticated/private polling where supported.

Modern switches can also export streaming telemetry using structured models.

Useful metrics:
- interface counters
- STP changes
- MAC moves
- PoE usage
- CPU/memory
- temperatures
- FHRP state

#### Why It Works / Why It Matters

Campus resilience requires visibility into both slow trends and event changes.



### Enhanced Deep Dive — Syslog Severity and Correlation

Central syslog captures topology/protection events such as:
- link up/down
- STP topology change
- port security
- BPDU Guard
- EtherChannel member changes
- HSRP state changes

#### Why It Works / Why It Matters

NTP-synchronized timestamps let operators correlate events across switches.



### Enhanced Deep Dive — High Availability: Supervisor Redundancy Awareness

Modular/enterprise switches may support redundant supervisors/control planes with features such as Stateful Switchover and Nonstop Forwarding.

The goal is to preserve forwarding/control continuity during supervisor failure.

#### Why It Works / Why It Matters

Device redundancy exists inside a chassis as well as across chassis.



### Enhanced Deep Dive — SSO / NSF Awareness

Stateful Switchover preserves control-plane state between active/standby supervisors. Nonstop Forwarding aims to preserve data forwarding while control protocols recover.

Exact behavior depends on platform and protocol support.

#### Why It Works / Why It Matters

High availability is not simply 'two power supplies'.



### Enhanced Deep Dive — Dual Power and Physical Diversity

True resiliency includes:
- separate PSUs
- separate power feeds
- separate UPS/PDU
- diverse cable paths
- separate uplink modules/line cards where justified

#### Why It Works / Why It Matters

Two logical uplinks in the same conduit or PSU are not fully independent.



### Enhanced Deep Dive — Failure-Domain Mapping

For every campus component, identify what fails with it.

Example:
- access switch → one user block
- distribution switch → multiple access blocks/gateways
- core switch → campus-wide transit capacity
- DHCP server → address acquisition

#### Why It Works / Why It Matters

Architecture should align redundancy cost with business impact.



### Enhanced Deep Dive — STP + FHRP + Routing Failure Interaction

A campus outage can involve several control planes at once.

Example distribution failure:
- STP recalculates Layer-2 topology
- HSRP changes active gateway
- OSPF withdraws/changes routed paths
- MAC tables relearn

#### Diagram / Mental Model

```text
DIST1 fails
 ├─ STP reconverges
 ├─ HSRP failover
 ├─ OSPF convergence
 └─ traffic resumes
```

#### Why It Works / Why It Matters

Measure end-to-end recovery rather than each protocol independently.



### Enhanced Deep Dive — Broadcast Containment

A VLAN is a broadcast domain. Large VLANs increase:
- broadcast scope
- unknown-unicast flood scope
- failure blast radius
- troubleshooting complexity

Do not create campus-wide VLANs without a clear need.

#### Why It Works / Why It Matters

Routed boundaries are one of the best scaling tools in campus design.



### Enhanced Deep Dive — ARP/ND Scale

Large Layer-2 domains increase ARP/NDP neighbor state and broadcast/multicast control traffic.

Moving Layer-3 boundaries closer to endpoints can reduce this scale.

#### Why It Works / Why It Matters

Subnet size is an operations choice, not only an address-count calculation.



### Enhanced Deep Dive — Wireless Controller / AP Switching Paths Awareness

Enterprise WLAN traffic can be:
- locally switched at the AP/access layer
- tunneled centrally to a controller
- segmented into different VLAN/VRF policy domains

The physical AP switchport may carry management and/or tunneled/tagged traffic depending on architecture.

#### Why It Works / Why It Matters

Do not assume every SSID maps directly to a local access VLAN in every wireless design.



### Enhanced Deep Dive — IoT Access Design

IoT devices often lack 802.1X supplicant support and may require:
- MAB
- dedicated VLAN/VRF
- strict ACL/firewall policy
- limited DNS/NTP/app destinations
- monitoring

#### Security Implication

IoT segmentation should be least-privilege, not simply a different VLAN name.



### Enhanced Deep Dive — Guest Access Design

Guest networks should generally:
- avoid internal routing access
- use dedicated DNS/DHCP/Internet path
- enforce client isolation where appropriate
- prevent management-plane access

#### Why It Works / Why It Matters

Guest access is an untrusted security zone.



### Enhanced Deep Dive — Campus Automation

Switch configuration is highly repetitive, making it a good automation target.

Represent intent as structured data:

#### Diagram / Mental Model

```text
YAML/JSON intent
   ↓ validation
Template/model
   ↓
candidate configuration
   ↓
switch
   ↓
show/API verification
```

#### Why It Works / Why It Matters

Automation should make policy more consistent, not push mistakes faster.



### Enhanced Deep Dive — Configuration Validation Assertions

Before pushing a campus change, assert things such as:
- access port has exactly one access VLAN
- trunks have approved allowed lists
- edge ports have PortFast/BPDU Guard
- no user port is trusted for DHCP Snooping
- STP root priorities match design

#### Why It Works / Why It Matters

Validation catches policy errors before the network sees them.



### Enhanced Deep Dive — Structured Operational Data Awareness

Modern platforms can expose interface/VLAN/STP/PoE data through structured APIs such as NETCONF/RESTCONF/telemetry.

This is easier to validate programmatically than parsing human-formatted CLI text.

#### Why It Works / Why It Matters

The same networking concepts appear whether state is viewed through CLI or APIs.



### Enhanced Deep Dive — Campus Security Layering

No single switching feature provides complete access security.

A stronger model is:

#### Diagram / Mental Model

```text
802.1X/MAB identity
      ↓
VLAN/VRF segmentation
      ↓
DHCP Snooping
      ↓
DAI / Source Guard
      ↓
ACL / Firewall
      ↓
Endpoint security
      ↓
Application authorization
```

#### Security Implication

Each layer limits a different class of failure or abuse.



### Enhanced Deep Dive — Troubleshooting STP Unexpected Blocking

If the wrong port blocks:
1. identify root
2. calculate root path cost
3. inspect upstream bridge IDs
4. inspect port cost/priority
5. verify EtherChannel state
6. verify no unexpected switch/root exists

#### Cisco IOS / IOS XE Example

```cisco
show spanning-tree vlan 10
show spanning-tree detail
show etherchannel summary
```

#### Why It Works / Why It Matters

Changing port cost before understanding the root election can make topology less predictable.



### Enhanced Deep Dive — Troubleshooting EtherChannel

If a bundle is down/suspended:
- physical link up?
- same channel protocol?
- compatible modes?
- same trunk/access mode?
- same native/allowed VLANs?
- speed/duplex compatible?
- member accidentally configured independently?

#### Cisco IOS / IOS XE Example

```cisco
show etherchannel summary
show interfaces port-channel 1
show interfaces g1/0/47 switchport
```

#### Why It Works / Why It Matters

Treat the Port-Channel as one logical interface and members as consistency participants.



### Enhanced Deep Dive — Troubleshooting HSRP

Check:
- group number/version
- virtual IP
- real SVI addresses
- priority
- preempt
- timers
- tracking
- VLAN/STP reachability between peers

#### Cisco IOS / IOS XE Example

```cisco
show standby brief
show standby
show track
```

#### Why It Works / Why It Matters

HSRP can be configured correctly but fail because the two peers are not in the same Layer-2 domain.



### Enhanced Deep Dive — Troubleshooting DHCP Snooping

When clients stop receiving addresses:
- is VLAN enabled for snooping?
- client port untrusted as expected?
- server/uplink trusted?
- DHCP relay correct?
- Option 82 policy compatible?
- rate limit too low?
- binding database healthy?

#### Cisco IOS / IOS XE Example

```cisco
show ip dhcp snooping
show ip dhcp snooping binding
show interfaces <port>
```

#### Why It Works / Why It Matters

A security feature can block legitimate service traffic when the trust path is wrong.



### Enhanced Deep Dive — Troubleshooting DAI

If ARP is dropped:
- binding exists?
- client static or DHCP?
- VLAN enabled?
- correct trust boundary?
- ARP ACL/static binding required?
- duplicate address/spoof event?

#### Cisco IOS / IOS XE Example

```cisco
show ip arp inspection
show ip dhcp snooping binding
```

#### Why It Works / Why It Matters

Do not disable DAI globally before identifying which identity/binding assumption failed.



### Enhanced Deep Dive — Troubleshooting MAC Address Location

Use MAC learning to trace an endpoint through the campus.

At each switch:
1. find MAC
2. identify VLAN
3. identify egress port
4. move to next switch
5. repeat

#### Cisco IOS / IOS XE Example

```cisco
show mac address-table address <mac>
```

#### Why It Works / Why It Matters

This is the Layer-2 equivalent of hop-by-hop route tracing.



### Enhanced Deep Dive — Packet Capture in Switched Networks

A normal switched port sees mostly its own unicast plus broadcast/multicast—not all traffic.

Use SPAN/RSPAN/ERSPAN or an appropriate tap to capture another flow.

#### Security Implication

Mirroring traffic requires authorization and careful handling of sensitive packet data.



### Enhanced Deep Dive — Final Campus Design Checklist

Before approving a campus design, answer:

- Which VLANs exist and why?
- Which VLANs span access switches?
- Where is the Layer-3 boundary?
- Which switch is STP root per VLAN/instance?
- Is HSRP active aligned with root?
- Are redundant uplinks L2, EtherChannel, or routed?
- Which edge ports use PortFast/BPDU Guard?
- Where is DHCP Snooping trusted?
- How are static-IP devices handled with DAI?
- How are users/devices authenticated?
- Is management in-band or OOB?
- What is the failure domain of each access/distribution/core device?
- What is the rollback path for a trunk/STP change?

#### Why It Works / Why It Matters

Advanced switching is topology, control-plane design, security, operations, and failure behavior together.



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Campus VLAN and Trunk Design

1. Create Users, Servers, Voice, Guest, and Management VLANs.
2. Configure access and voice VLANs.
3. Configure explicit trunks.
4. Restrict allowed VLANs.
5. Verify native VLAN and trunk state.

### Lab 2 — STP Root Election

1. Build four switches with redundant links.
2. Observe default root election.
3. Predict root from bridge IDs.
4. Force DIST1 as primary root and DIST2 as secondary.
5. Verify blocked and forwarding ports.

### Lab 3 — RSTP and Edge Protection

1. Enable Rapid PVST+ where supported.
2. Configure PortFast on endpoint ports.
3. Enable BPDU Guard.
4. Connect a switch to an edge port in the lab and observe protection behavior.
5. Recover the port safely.

### Lab 4 — EtherChannel

1. Create two parallel links between switches.
2. Bundle using LACP.
3. Configure the Port-Channel as trunk.
4. Verify member status.
5. Intentionally mismatch one member and troubleshoot.

### Lab 5 — HSRP

1. Configure two distribution switches with a virtual gateway.
2. Set priorities and preemption.
3. Verify active/standby roles.
4. Fail the active uplink/device.
5. Observe gateway continuity.

### Lab 6 — Routed Access

1. Convert access-to-distribution uplinks to Layer 3.
2. Run OSPF between access and distribution switches.
3. Keep user VLANs local.
4. Verify ECMP where available.
5. Compare failure domains with an L2 trunk design.

### Lab 7 — Port Security

1. Configure sticky MAC and maximum addresses.
2. Test an authorized endpoint.
3. Introduce an additional lab endpoint.
4. Observe violation behavior.
5. Compare protect/restrict/shutdown modes conceptually or in the simulator.

### Lab 8 — DHCP Snooping and DAI

1. Enable DHCP Snooping for one VLAN.
2. Trust only the legitimate server/uplink path.
3. Verify binding creation.
4. Enable DAI.
5. Verify legitimate ARP traffic.
6. Document what breaks for static hosts if policy is incomplete.

### Lab 9 — Management Plane

1. Create management VLAN.
2. Configure SSH.
3. Configure NTP and Syslog.
4. Use SNMPv3 concepts or simulator-supported configuration.
5. Restrict management access using an ACL where supported.

### Lab 10 — Broken Campus Troubleshooting

1. Inject wrong VLAN, missing trunk VLAN, native mismatch, wrong STP root, broken EtherChannel member, HSRP priority error, port-security violation, untrusted DHCP uplink.
2. Troubleshoot systematically using show commands.
3. Record root cause and prevention.


## Enhanced Practical Lab Sequence

### Enhanced Lab 1 — Campus Layer Roles

Classify 30 functions into access, distribution, core, or shared responsibility.

### Enhanced Lab 2 — L2 vs Routed Access

Build both designs in Packet Tracer and compare STP/routing failure domains.

### Enhanced Lab 3 — Collapsed Core

Design a 6-switch small campus and justify collapsed-core choice.

### Enhanced Lab 4 — Stacking Awareness

Compare standalone pair vs stacking/multi-chassis logical system in a design table.

### Enhanced Lab 5 — MLAG Concept

Draw a multi-chassis port-channel and compare with ordinary STP-blocked dual uplinks.

### Enhanced Lab 6 — VTP

Document server/client/transparent/off concepts and risks without enabling it on production.

### Enhanced Lab 7 — VLAN Pruning

Remove unnecessary VLANs from three trunks and prove user reachability remains correct.

### Enhanced Lab 8 — Private VLAN

Design isolated/community/promiscuous port roles for a shared hosting segment.

### Enhanced Lab 9 — Q-in-Q

Draw customer tag + provider tag and explain valid use vs VLAN-hopping confusion.

### Enhanced Lab 10 — Bridge ID

Calculate/predict root election from four switch bridge IDs.

### Enhanced Lab 11 — Root Placement

Force root primary/secondary and verify.

### Enhanced Lab 12 — Path Cost

Calculate root path cost through 10G/1G/100M mixed topology using the platform cost method.

### Enhanced Lab 13 — Root Port Tie

Create equal-cost paths and identify the tie-breaker.

### Enhanced Lab 14 — Designated Port

Determine designated ports on a multi-switch shared topology.

### Enhanced Lab 15 — Classic vs RSTP States

Map blocking/listening/learning/forwarding to RSTP discarding/learning/forwarding.

### Enhanced Lab 16 — RSTP Proposal

Use a topology diagram to explain proposal/agreement convergence.

### Enhanced Lab 17 — Edge Port

Configure PortFast only on endpoint links and verify.

### Enhanced Lab 18 — Topology Changes

Observe STP topology-change counters while manually changing an edge/trunk link.

### Enhanced Lab 19 — Rapid-PVST

Run per-VLAN roots on two VLAN groups.

### Enhanced Lab 20 — MST

Map 20 VLANs into 2 MST instances and define a matching region configuration.

### Enhanced Lab 21 — MST Mismatch

Create a documentation example of mismatched region revision/mapping and predict boundary behavior.

### Enhanced Lab 22 — Root Guard

Protect an access-facing switch port from becoming root path.

### Enhanced Lab 23 — Loop Guard

Identify which redundant switch links are candidates for loop guard.

### Enhanced Lab 24 — BPDU Filter

Explain why filtering BPDUs can create loops; do not use it merely to hide BPDUs.

### Enhanced Lab 25 — UDLD

Design a unidirectional-fiber failure and explain why STP needs link-direction detection.

### Enhanced Lab 26 — Bridge Assurance

Document its supported-use case and relation to network ports.

### Enhanced Lab 27 — Storm Control

Configure a safe lab threshold and observe counters/behavior if simulator supports it.

### Enhanced Lab 28 — Errdisable

Trigger BPDU Guard/port-security in lab, identify errdisable reason, fix root cause, recover.

### Enhanced Lab 29 — LACP Matrix

Predict bundle formation for active/passive combinations.

### Enhanced Lab 30 — LACP Priority

Explain when system/port priority changes member selection.

### Enhanced Lab 31 — Member Consistency

Break allowed VLAN/native mode on one member and troubleshoot suspension.

### Enhanced Lab 32 — Routed Port-Channel

Build an L3 EtherChannel between distribution/core and run OSPF over it.

### Enhanced Lab 33 — Hashing

Generate several flows and explain why one flow does not use every link.

### Enhanced Lab 34 — Minimum Links

Design a 4-member bundle requiring at least 2 members for operation.

### Enhanced Lab 35 — HSRP Versions

Document group/version consistency requirements.

### Enhanced Lab 36 — HSRP Timers

Observe failover time before/after safe lab tuning.

### Enhanced Lab 37 — HSRP Tracking

Track a core uplink so failed distribution stops being preferred gateway.

### Enhanced Lab 38 — STP-HSRP Alignment

Intentionally misalign active gateway/root and draw the hairpin path, then align.

### Enhanced Lab 39 — Per-VLAN Load Sharing

Make DIST1 active/root for VLAN10 and DIST2 for VLAN20.

### Enhanced Lab 40 — VRRP/GLBP

Compare redundancy/load-sharing behavior conceptually.

### Enhanced Lab 41 — Anycast Gateway

Explain how EVPN/VXLAN anycast differs from HSRP.

### Enhanced Lab 42 — Routed Access ECMP

Build dual L3 uplinks and observe route-table ECMP.

### Enhanced Lab 43 — IPv6 SVI

Configure IPv6 gateway/RA on a lab SVI and inspect NDP.

### Enhanced Lab 44 — Snooping Binding

Capture/inspect MAC-IP-VLAN-port binding after DHCP.

### Enhanced Lab 45 — Option 82

Document circuit information flow through an access switch and relay/server.

### Enhanced Lab 46 — DHCP Rate

Design a reasonable client-port rate limit and discuss boot-storm risk.

### Enhanced Lab 47 — Binding Persistence

Document what happens to DAI/Source Guard after switch reboot if bindings disappear.

### Enhanced Lab 48 — Static DAI

Create a plan for printers/servers with static IP under DAI.

### Enhanced Lab 49 — IP Source Guard

Apply in a controlled DHCP client lab and verify approved source works.

### Enhanced Lab 50 — Port Security Limits

Compare phone+PC, hypervisor, docking station, and MAC randomization cases.

### Enhanced Lab 51 — 802.1X

Draw EAPOL→switch→RADIUS authentication flow.

### Enhanced Lab 52 — MAB

Design a printer fallback policy and state its weaknesses.

### Enhanced Lab 53 — Dynamic Policy

Design RADIUS-returned VLAN/dACL policy for employees vs contractors.

### Enhanced Lab 54 — VLAN Hopping Defense

Audit ten access/trunk configuration items against defensive checklist.

### Enhanced Lab 55 — MAC Flood Defense

Design monitoring/port-security response without generating an actual production attack.

### Enhanced Lab 56 — MAC Move

Create legitimate virtualization-move vs loop indicators comparison.

### Enhanced Lab 57 — IGMP Snooping

Observe or model multicast membership forwarding.

### Enhanced Lab 58 — QoS Trust

Set a conceptual trust boundary for phone+PC access port.

### Enhanced Lab 59 — LLDP-MED

Document how phone can learn voice policy.

### Enhanced Lab 60 — PoE Budget

Calculate switch power consumption for 24 phones + 8 APs.

### Enhanced Lab 61 — MTU

Create a mixed-MTU path and troubleshoot large-frame failure.

### Enhanced Lab 62 — Microbursts

Interpret interface output drops with low average utilization.

### Enhanced Lab 63 — Queueing

Design voice/video/data/bulk queue priorities under congestion.

### Enhanced Lab 64 — SPAN

Mirror one authorized lab port to Wireshark and identify VLAN/ARP traffic.

### Enhanced Lab 65 — RSPAN/ERSPAN

Compare local L2 remote mirror vs L3 encapsulated remote mirror.

### Enhanced Lab 66 — MACsec

Design a campus uplink needing L2 encryption and state what MACsec does/doesn't protect.

### Enhanced Lab 67 — OOB Management

Draw production vs OOB management paths.

### Enhanced Lab 68 — Management VRF

Design MGMT VRF routing isolated from CORP.

### Enhanced Lab 69 — AAA

Build TACACS+/RADIUS management flow and break-glass local-account policy.

### Enhanced Lab 70 — Config Archive

Write change/rollback steps for a trunk allowed-VLAN change.

### Enhanced Lab 71 — Telemetry

Define metrics for port errors, STP changes, MAC moves, PoE, HSRP, CPU.

### Enhanced Lab 72 — Syslog

Correlate a manual link failure with STP/HSRP/OSPF log events.

### Enhanced Lab 73 — Supervisor HA

Compare redundant chassis vs two independent switches.

### Enhanced Lab 74 — SSO/NSF

Explain forwarding behavior during supervisor switchover.

### Enhanced Lab 75 — Physical Diversity

Audit whether two uplinks really have independent power/path/module.

### Enhanced Lab 76 — Failure Domains

Map the blast radius of access, distribution, core, DHCP, and AAA failures.

### Enhanced Lab 77 — Multi-Control-Plane Failure

Fail a distribution switch and document STP+HSRP+OSPF reactions.

### Enhanced Lab 78 — Broadcast Scope

Compare /22 campus VLAN vs four /24 routed VLANs.

### Enhanced Lab 79 — ARP/ND Scale

Estimate neighbor/broadcast impact as VLAN grows.

### Enhanced Lab 80 — Wireless Path

Compare local-switched WLAN vs controller-tunneled WLAN topology.

### Enhanced Lab 81 — IoT

Design least-privilege IoT VLAN/NAC/firewall flow matrix.

### Enhanced Lab 82 — Guest

Design Internet-only guest policy with DNS/DHCP and management isolation.

### Enhanced Lab 83 — Automation

Represent 48 switchports as structured intent data and render/validate configuration conceptually.

### Enhanced Lab 84 — Validation

Write assertions for trunk allowed lists, PortFast/BPDU Guard, snooping trust, root priorities.

### Enhanced Lab 85 — Structured State

Design RESTCONF/telemetry queries conceptually for interfaces/VLAN/STP.

### Enhanced Lab 86 — Security Layers

Map 802.1X, VLAN, snooping, DAI, ACL, endpoint security to different threats.

### Enhanced Lab 87 — STP Troubleshooting

Solve five unexpected-blocking cases from root/cost/port evidence.

### Enhanced Lab 88 — EtherChannel Troubleshooting

Solve five suspension cases.

### Enhanced Lab 89 — HSRP Troubleshooting

Solve five active/standby/track failures.

### Enhanced Lab 90 — Snooping Troubleshooting

Solve five DHCP failures caused by trust/VLAN/rate/relay.

### Enhanced Lab 91 — DAI Troubleshooting

Solve static host vs spoofed ARP cases.

### Enhanced Lab 92 — MAC Trace

Trace one endpoint MAC across access→distribution using MAC tables.

### Enhanced Lab 93 — Capture Placement

Choose SPAN source/destination to observe a specific host-to-gateway flow.

### Enhanced Lab 94 — Capstone

Complete the expanded resilient enterprise campus.


## 6. Mini Project

# Mini Project — Resilient Enterprise Campus

Build:

```text
                        CORE1 ===== CORE2
                          | \       / |
                          |  \     /  |
                        DIST1 ===== DIST2
                         / \         / \
                       ACC1 ACC2   ACC3 ACC4
                        |    |      |    |
                      Users APs   Voice IoT
```

## Required VLANs

```text
VLAN 10  Users
VLAN 20  Servers
VLAN 30  Management
VLAN 40  Voice
VLAN 50  Guest
VLAN 60  IoT
VLAN 999 Native/unused
```

## Requirements

### Switching
- Explicit trunks
- Restricted allowed-VLAN lists
- Documented native VLAN
- Rapid PVST+ or simulator-supported equivalent
- DIST1 root primary for selected VLANs
- DIST2 root primary for another set of VLANs
- Secondary root placement
- EtherChannel between distribution switches or selected uplinks

### Gateways
- HSRP for key user/server VLANs
- Align active HSRP gateway with STP root where using Layer-2 access design

### Layer 3
- Routed links from distribution to core
- OSPF in the core/distribution
- Default route toward edge

### Security
- PortFast + BPDU Guard on endpoint ports
- Port security on selected access ports
- DHCP Snooping
- DAI
- IP Source Guard where supported
- Guest and IoT segmentation
- Management VLAN restricted from user access

### Management
- SSH
- NTP
- Syslog
- SNMPv3 concept/config where supported
- configuration backup procedure

### Failure Tests
Test:
1. Access uplink failure
2. Distribution-switch failure
3. EtherChannel member failure
4. STP root failure
5. HSRP active failure
6. Rogue DHCP attempt in lab
7. Port-security violation
8. Incorrect trunk allowed list
9. Native VLAN mismatch
10. OSPF routed-uplink failure

For each:
- symptom
- expected control-plane behavior
- expected data-plane behavior
- verification commands
- recovery
- prevention

## Enhanced Capstone — Resilient Secure Enterprise Campus

Extend the original resilient campus into a complete operations/security design.

```text
                         CORE1 ===== CORE2
                          ||          ||
                       routed ECMP core
                          ||          ||
                   DIST1 ============= DIST2
                    || \               / ||
                    ||  \             /  ||
                  ACC1 ACC2         ACC3 ACC4
                   |    |            |    |
                Users  APs         Voice  IoT

Separate:
OOB/MGMT network
DHCP/DNS/NTP/Syslog/AAA services
Internet/Firewall edge
```

### VLANs

```text
10 USERS-A
11 USERS-B
20 SERVERS
30 MANAGEMENT
40 VOICE
50 CORP-WLAN
60 GUEST
70 IOT
80 PRINTERS
999 NATIVE/UNUSED
```

### Layer-2

Implement/document:

```text
Rapid-PVST+ or MST
intentional root primary/secondary
PortFast
BPDU Guard
Root Guard where appropriate
Loop Guard where appropriate
explicit trunks
nonegotiate where supported
restricted VLAN lists
native VLAN strategy
EtherChannel
storm control
UDLD awareness on fiber
```

### FHRP

For Layer-2 access VLANs:

```text
HSRP virtual gateway
priority/preempt
upstream tracking
STP root alignment
per-VLAN load sharing
```

### Routed Core / Access Exercise

Use routed Port-Channels or routed uplinks between distribution/core.

Run OSPF.

Create a comparison document:

```text
L2 access + HSRP/STP
vs
Routed access + ECMP
```

### Access Security

Configure/document:

```text
Port security where appropriate
DHCP Snooping
DHCP rate limits
Option 82 awareness
DAI
static-IP exception plan
IP Source Guard
802.1X
MAB fallback
RADIUS/NAC role assignment
guest/IoT segmentation
```

### Management

Implement:

```text
SSH only
AAA
management VLAN/VRF
OOB design
SNMPv3
Syslog
NTP
configuration archive
backup/restore
```

### Monitoring

Define alerts for:

```text
STP root change
topology change spike
MAC flapping
EtherChannel member loss
HSRP state change
DHCP Snooping violation
DAI drop spike
port-security violation
PoE budget high
interface errors/drops
CPU/memory
temperature/fan/PSU
```

### Packet Analysis

Use a legal lab/SPAN capture to inspect:

```text
802.1Q tags
STP/RSTP BPDUs
LACP
HSRP
DHCP DORA
ARP
IPv6 NDP/RA
802.1X EAPOL if available
```

### Failure Tests

Test/document at least:

```text
1. wrong access VLAN
2. allowed-VLAN omission
3. native VLAN mismatch
4. unexpected root bridge
5. root guard event
6. BPDU Guard errdisable
7. loop-guard scenario concept
8. EtherChannel mode mismatch
9. member trunk mismatch
10. port-channel member failure
11. HSRP active device failure
12. HSRP upstream tracking failure
13. STP-HSRP misalignment
14. DHCP server path not trusted
15. DHCP rate limit too low
16. DAI blocks static printer
17. IP Source Guard wrong binding
18. port-security violation
19. PoE capacity exhaustion
20. MTU mismatch
21. routed core OSPF failure
22. management ACL lockout
23. NTP failure causing log-time drift
24. MAC-flap condition
```

For each:

```text
Symptom
Affected VLAN/users
Expected control-plane behavior
Observed STP/FHRP/LACP/routing state
Data-plane path
Security feature involved
Root cause
Fix
Verification
Preventive design control
```

### Deliverables

```text
CAMPUS_ARCHITECTURE.md
VLAN_PLAN.md
TRUNK_POLICY.md
STP_ROOT_PLAN.md
MST_OR_RPVST_DESIGN.md
ETHERCHANNEL_PLAN.md
FHRP_PLAN.md
ROUTED_ACCESS_COMPARISON.md
ACCESS_SECURITY.md
NAC_8021X.md
DHCP_SNOOPING_DAI.md
QOS_AND_VOICE.md
MANAGEMENT_PLANE.md
OOB_DESIGN.md
MONITORING_AND_TELEMETRY.md
PACKET_CAPTURE_ANALYSIS.md
FAILURE_DOMAIN_MAP.md
FAILURE_TESTS.md
CHANGE_AND_ROLLBACK.md
```


## 7. Recommended Resources

Primary references:

- Cisco switching configuration guides.
- Cisco Spanning Tree Protocol documentation.
- Cisco EtherChannel/LACP configuration guides.
- Cisco HSRP/FHRP documentation.
- Cisco campus design guides.
- Cisco DHCP Snooping, DAI, IP Source Guard, and Port Security guides.
- Cisco Learning Network.
- Wireshark official documentation for STP, VLAN, DHCP, and ARP packet analysis.

Use the exact guide for the switch family/IOS image in your lab because command support differs.
## 8. Certification Relevance

This course extends far beyond basic VLAN configuration and moves toward enterprise campus design and professional-level switching operations.

It directly supports later work in:

- enterprise network engineering,
- wireless infrastructure,
- NAC/802.1X,
- data-center networking,
- network security,
- cloud connectivity,
- SOC troubleshooting,
- infrastructure automation.
## 9. Common Mistakes & Best Practices

- **Mistake:** Letting STP choose the root accidentally.
  - **Best practice:** Set root primary/secondary intentionally according to topology.
- **Mistake:** Using PortFast on switch-to-switch links.
  - **Best practice:** Use PortFast only on true edge ports.
- **Mistake:** Leaving all VLANs allowed on every trunk.
  - **Best practice:** Permit only required VLANs.
- **Mistake:** Relying on DTP negotiation in secure designs.
  - **Best practice:** Use explicit access/trunk mode and disable negotiation where appropriate.
- **Mistake:** Bundling links with inconsistent configs.
  - **Best practice:** Configure members consistently and verify the port-channel.
- **Mistake:** Using HSRP without aligning Layer-2 path design.
  - **Best practice:** Where L2 access is used, align FHRP active gateway and STP root to avoid inefficient paths.
- **Mistake:** Enabling DHCP Snooping without trusting the legitimate server path.
  - **Best practice:** Map the DHCP packet path first.
- **Mistake:** Enabling DAI without considering static-IP hosts.
  - **Best practice:** Plan static bindings/ARP ACLs or exceptions appropriately.
- **Mistake:** Treating VLANs as a complete security control.
  - **Best practice:** Use Layer-3/firewall/ACL/NAC policy in addition to segmentation.
- **Mistake:** Ignoring management-plane isolation.
  - **Best practice:** Separate management and restrict administrative protocols.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the access layer?

**Short answer:** The campus layer connecting endpoints and applying edge policy.

### Q2. What is a collapsed core?

**Short answer:** A design combining core and distribution functions.

### Q3. Why does STP exist?

**Short answer:** To prevent Layer-2 loops while preserving redundant links.

### Q4. How is the STP root selected?

**Short answer:** Lowest bridge ID wins.

### Q5. What is a root port?

**Short answer:** A non-root switch's best path toward the root.

### Q6. What is a designated port?

**Short answer:** The best forwarding port for a segment.

### Q7. What does RSTP improve?

**Short answer:** Convergence speed and role/state handling.

### Q8. What is PortFast?

**Short answer:** An edge-port behavior that transitions rapidly to forwarding.

### Q9. What does BPDU Guard do?

**Short answer:** Protects edge ports by disabling/error-protecting them when BPDUs are received.

### Q10. What does Root Guard do?

**Short answer:** Prevents an unexpected superior root from being accepted through a protected port.

### Q11. What is EtherChannel?

**Short answer:** Multiple physical links combined into one logical port-channel.

### Q12. What is LACP?

**Short answer:** Standards-based link aggregation negotiation protocol.

### Q13. What is HSRP?

**Short answer:** Cisco first-hop gateway redundancy protocol.

### Q14. What does HSRP preempt do?

**Short answer:** Allows a higher-priority device to retake active role.

### Q15. What is routed access?

**Short answer:** Access uplinks are Layer 3 rather than extending VLAN trunks.

### Q16. What is port security?

**Short answer:** Controls which/how many MAC addresses may use an access port.

### Q17. What is DHCP Snooping?

**Short answer:** Switch feature that blocks rogue DHCP server responses and builds bindings.

### Q18. What is DAI?

**Short answer:** Dynamic ARP Inspection validates ARP against trusted/binding information.

### Q19. What is IP Source Guard?

**Short answer:** Restricts source IP usage on access ports according to bindings/policy.

### Q20. What is VLAN hopping?

**Short answer:** A class of attempts to cross VLAN boundaries through switching/trunk weaknesses.

### Q21. What is storm control?

**Short answer:** Limits broadcast/multicast/unknown-unicast traffic rates.

### Q22. Why use a management VLAN?

**Short answer:** To isolate administrative interfaces from general user traffic.

### Q23. Why is NTP important?

**Short answer:** Accurate time supports logs, security, authentication, and troubleshooting.

### Q24. What command checks EtherChannel?

**Short answer:** `show etherchannel summary`.

### Q25. What command checks STP?

**Short answer:** `show spanning-tree`.

### Q26. What command checks HSRP?

**Short answer:** `show standby brief`.

### Q27. What command checks DHCP Snooping bindings?

**Short answer:** `show ip dhcp snooping binding`.

### Q28. What is the core switching troubleshooting habit?

**Short answer:** Verify VLAN membership, trunking, STP, bundle state, gateway state, and security features in the actual packet path.


## Enhanced Self-Assessment Questions

### Enhanced Q1. Access layer responsibility?

**Short answer:** Endpoint connectivity and edge policy.

### Enhanced Q2. Distribution layer responsibility?

**Short answer:** L3 boundary, policy, summarization, gateway redundancy, failure isolation.

### Enhanced Q3. Core responsibility?

**Short answer:** Fast resilient transport with minimal unnecessary policy.

### Enhanced Q4. Routed access main benefit?

**Short answer:** Smaller L2/STP domains and active L3 ECMP uplinks.

### Enhanced Q5. What is a collapsed core?

**Short answer:** Combined core and distribution functions.

### Enhanced Q6. What does switch stacking change?

**Short answer:** Multiple physical members can operate as one logical/control system depending on technology.

### Enhanced Q7. What is MLAG/multi-chassis EtherChannel?

**Short answer:** One logical LAG spanning two physical upstream switches.

### Enhanced Q8. Why prune VLANs?

**Short answer:** Reduce broadcast/flood scope and attack/troubleshooting surface.

### Enhanced Q9. What are private VLANs?

**Short answer:** L2 isolation roles inside a primary VLAN structure.

### Enhanced Q10. What is Q-in-Q?

**Short answer:** Nested customer VLAN tag inside provider/service VLAN tag.

### Enhanced Q11. How root bridge selected?

**Short answer:** Lowest bridge ID.

### Enhanced Q12. Why set root priority?

**Short answer:** Prevent accidental MAC-based root election.

### Enhanced Q13. What does STP path cost represent?

**Short answer:** Relative path cost toward root.

### Enhanced Q14. Root port?

**Short answer:** Best port toward root on a non-root switch.

### Enhanced Q15. Designated port?

**Short answer:** Best forwarding port for a segment.

### Enhanced Q16. RSTP states?

**Short answer:** Discarding, learning, forwarding.

### Enhanced Q17. Why RSTP faster?

**Short answer:** Proposal/agreement and role-based rapid transitions.

### Enhanced Q18. What is an edge port?

**Short answer:** Endpoint-facing port eligible for rapid forwarding.

### Enhanced Q19. What is topology-change effect?

**Short answer:** Accelerates relearning/aging so stale MAC paths clear.

### Enhanced Q20. Rapid-PVST+ scalability issue?

**Short answer:** One instance per VLAN.

### Enhanced Q21. MST purpose?

**Short answer:** Map many VLANs to fewer STP instances.

### Enhanced Q22. MST region must match what?

**Short answer:** Name, revision, VLAN-to-instance mapping.

### Enhanced Q23. Root Guard purpose?

**Short answer:** Prevent superior root appearing through protected port.

### Enhanced Q24. Loop Guard purpose?

**Short answer:** Prevent blocked/non-designated link from forwarding after BPDU loss.

### Enhanced Q25. Why BPDU Filter dangerous?

**Short answer:** Can remove STP protection and create loops.

### Enhanced Q26. UDLD purpose?

**Short answer:** Detect unidirectional links.

### Enhanced Q27. Storm control?

**Short answer:** Limit broadcast/multicast/unknown-unicast storms.

### Enhanced Q28. What is errdisable?

**Short answer:** Protective disabled state after certain faults.

### Enhanced Q29. LACP active/passive works?

**Short answer:** Yes; passive/passive does not negotiate.

### Enhanced Q30. EtherChannel member requirement?

**Short answer:** Compatible L2/L3 settings and negotiation.

### Enhanced Q31. Can EtherChannel be routed?

**Short answer:** Yes.

### Enhanced Q32. Why one big flow may not use full bundle?

**Short answer:** Hash normally maps a flow to one member.

### Enhanced Q33. HSRP tracking purpose?

**Short answer:** Move active gateway when upstream path fails.

### Enhanced Q34. Why align HSRP active and STP root?

**Short answer:** Avoid unnecessary Layer-2 hairpin path.

### Enhanced Q35. How per-VLAN load share?

**Short answer:** Split root/active-gateway ownership across distribution switches.

### Enhanced Q36. Anycast gateway vs HSRP?

**Short answer:** Same gateway present on multiple fabric nodes vs active/standby FHRP.

### Enhanced Q37. IPv6 first-hop dependency?

**Short answer:** RA/NDP/ICMPv6.

### Enhanced Q38. What does snooping binding record?

**Short answer:** MAC, IP, VLAN, port, lease.

### Enhanced Q39. Option 82 purpose?

**Short answer:** Identify relay/circuit access location in DHCP.

### Enhanced Q40. Why snooping rate limit?

**Short answer:** Reduce DHCP flood/starvation behavior.

### Enhanced Q41. Why persistent bindings?

**Short answer:** DAI/Source Guard continue functioning after reboot.

### Enhanced Q42. How DAI handles static hosts?

**Short answer:** Static binding/ARP ACL/trust/exception policy may be needed.

### Enhanced Q43. IP Source Guard purpose?

**Short answer:** Restrict source IP/MAC behavior at edge port.

### Enhanced Q44. Port security limitation?

**Short answer:** MAC limits do not equal strong device/user identity.

### Enhanced Q45. 802.1X roles?

**Short answer:** Supplicant, authenticator, authentication server.

### Enhanced Q46. MAB weakness?

**Short answer:** MAC address is easy to copy and is weaker than credential/certificate auth.

### Enhanced Q47. What can NAC dynamically assign?

**Short answer:** VLAN, ACL, role, session policy.

### Enhanced Q48. VLAN hopping defense?

**Short answer:** Explicit access mode, disable DTP, restrict trunks, safe native VLAN, shut unused ports.

### Enhanced Q49. MAC move may indicate?

**Short answer:** Loop, mobility, duplicate MAC, port-channel issue, or suspicious behavior.

### Enhanced Q50. IGMP snooping purpose?

**Short answer:** Forward multicast toward interested receivers rather than flood all ports.

### Enhanced Q51. QoS trust boundary?

**Short answer:** Point where packet markings become trusted/remarked.

### Enhanced Q52. LLDP-MED use?

**Short answer:** Phone/network policy discovery such as voice VLAN/PoE info.

### Enhanced Q53. PoE budget?

**Short answer:** Total switch power available for powered endpoints.

### Enhanced Q54. Why jumbo MTU must match?

**Short answer:** Any smaller path element can drop/fragment large traffic.

### Enhanced Q55. What are microbursts?

**Short answer:** Short traffic bursts overflowing buffers despite low average utilization.

### Enhanced Q56. SPAN?

**Short answer:** Local switch traffic mirroring.

### Enhanced Q57. RSPAN?

**Short answer:** Remote SPAN over an L2 VLAN.

### Enhanced Q58. ERSPAN?

**Short answer:** Remote mirrored traffic encapsulated over L3.

### Enhanced Q59. MACsec?

**Short answer:** Layer-2 Ethernet encryption/integrity on supported links.

### Enhanced Q60. OOB management benefit?

**Short answer:** Access infrastructure during production network failure.

### Enhanced Q61. Management VRF?

**Short answer:** Separate routing table for management traffic.

### Enhanced Q62. Why AAA?

**Short answer:** Centralized identity, authorization, and accounting.

### Enhanced Q63. Why config archive?

**Short answer:** Versioning/rollback for high-impact changes.

### Enhanced Q64. Why NTP with syslog?

**Short answer:** Correlate events accurately across devices.

### Enhanced Q65. SSO/NSF awareness?

**Short answer:** Preserve control/forwarding continuity during supervisor failures.

### Enhanced Q66. True physical redundancy requires?

**Short answer:** Independent power, paths, modules/chassis where justified.

### Enhanced Q67. Why map failure domains?

**Short answer:** Match redundancy investment to outage impact.

### Enhanced Q68. What happens when distribution fails?

**Short answer:** STP/FHRP/routing and MAC state may all reconverge.

### Enhanced Q69. Why avoid huge VLANs?

**Short answer:** Large broadcast/ARP/failure/troubleshooting scope.

### Enhanced Q70. Why NAC for IoT?

**Short answer:** Constrain weak/non-802.1X devices using identity/role/segmentation.

### Enhanced Q71. Why automation validation?

**Short answer:** Prevent repetitive policy mistakes at scale.

### Enhanced Q72. Best STP troubleshooting first step?

**Short answer:** Identify actual root and calculate path selection.

### Enhanced Q73. Best EtherChannel evidence?

**Short answer:** `show etherchannel summary` plus member/port-channel config.

### Enhanced Q74. Best DHCP Snooping troubleshooting question?

**Short answer:** Is the legitimate server path trusted and VLAN enabled?

### Enhanced Q75. Best MAC tracing method?

**Short answer:** Follow MAC table entry switch by switch.


## Completion Checklist

- [ ] I can design two-tier and three-tier campus architectures.
- [ ] I can plan VLANs, trunks, and Layer-3 boundaries.
- [ ] I can calculate/predict STP root and port roles.
- [ ] I can configure RSTP protections safely.
- [ ] I can build and troubleshoot LACP EtherChannels.
- [ ] I can configure and verify HSRP.
- [ ] I can implement routed access and OSPF uplinks.
- [ ] I can configure port security, DHCP Snooping, DAI, and IP Source Guard at foundation level.
- [ ] I can design a management plane with SSH/NTP/Syslog/SNMP concepts.
- [ ] I completed all labs and the resilient-campus mini project.
