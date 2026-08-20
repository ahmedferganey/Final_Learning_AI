# Network Security — Deep Learning Material

## Table of Contents

1. Network Security Overview
2. Types of Networks
3. Network Topologies
4. Network Devices
5. MAC and IP Addresses
6. OSI Model
7. TCP/IP Model
8. Encapsulation and PDUs
9. Ethernet and ARP
10. IPv4
11. Private and Public IPv4
12. Subnetting and CIDR
13. IPv6
14. IPv4 vs IPv6
15. NAT and PAT
16. Core Network Protocols
17. Physical and Logical Ports
18. Port Ranges
19. Common Protocols and Ports
20. Secure vs Insecure Protocols
21. TCP vs UDP
22. TCP Three-Way Handshake
23. Firewalls
24. Network Segmentation
25. VLAN, DMZ, and Microsegmentation
26. NAC, VPN, and ZTNA
27. Active vs Passive Network Attacks
28. DoS and DDoS
29. Fragmentation and Oversized-Packet Attacks
30. Spoofing
31. MITM
32. Passive Attacks
33. Wireless Network Security
34. Secure Network Design
35. Logging and Monitoring
36. Network Security Tools
37. Data Center Networking
38. Cloud Networking
39. Python Examples
40. Corrections to the Supplied Slides
41. Interview and Exam Questions
42. Final Review
43. Authoritative References

---

# 1. Network Security Overview

**Network security** protects network devices, communications, services, and data in transit.

The main security objectives are:

```text
Confidentiality
Integrity
Availability
```

Applied to networking:

```text
Confidentiality
→ Prevent unauthorized reading of traffic.

Integrity
→ Prevent unauthorized modification of traffic.

Availability
→ Keep network services reachable.
```

Other important goals:

```text
Authentication
Authorization
Segmentation
Accountability
Monitoring
Resilience
```

A secure network combines:

```text
Architecture
+
Technical Controls
+
Operational Controls
+
Monitoring
+
Incident Response
```

---

# 2. Types of Networks

## PAN — Personal Area Network

Very small network around a person.

```text
Phone ↔ Smartwatch
Laptop ↔ Headset
```

## LAN — Local Area Network

Covers a small geographic area.

Examples:

```text
Home
Office
School
Factory
```

Usually uses:

```text
Ethernet
Wi-Fi
```

## WLAN — Wireless LAN

LAN using wireless communication.

```text
Laptop
 ↓
Wi-Fi AP
 ↓
Switch
```

## CAN — Campus Area Network

Connects multiple LANs within:

```text
University
Factory
Corporate Campus
```

## MAN — Metropolitan Area Network

Covers a city or metropolitan region.

## WAN — Wide Area Network

Connects geographically separated networks.

```text
Cairo Office
     ↓
    WAN
     ↓
Dubai Office
```

## SAN — Storage Area Network

Dedicated network for storage.

```text
Servers
  ↓
SAN Fabric
  ↓
Storage
```

## VPN — Virtual Private Network

Protected logical tunnel over another network.

## Intranet

Private internal organizational network.

## Extranet

Controlled access for external partners.

---

# 3. Network Topologies

## Star

Most common enterprise LAN pattern.

```text
     PC
      |
PC — Switch — Server
      |
     AP
```

Advantages:

```text
Simple
Easy to troubleshoot
Endpoint-link failure is localized
```

## Bus

All nodes share one common medium.

Mostly historical in Ethernet contexts.

## Ring

Nodes form a logical/physical ring.

## Mesh

Multiple paths between devices.

```text
A ----- B
|\     /|
| \   / |
|  \ /  |
C ----- D
```

Advantages:

```text
Redundancy
High availability
Multiple paths
```

## Hybrid

Combination of multiple topologies.

---

# 4. Network Devices

## Hub

Layer 1 device.

Repeats received traffic to all ports.

```text
Sender
  ↓
 Hub
↓ ↓ ↓
A B C
```

Weaknesses:

```text
No intelligent forwarding
High collision/shared traffic exposure
Poor security
```

Modern networks normally use switches.

## Switch

Primarily Layer 2.

Learns MAC addresses and forwards Ethernet frames.

```text
MAC Table

AA:AA:AA → Port 1
BB:BB:BB → Port 5
```

Managed switches may provide:

```text
VLAN
802.1X
Port Security
ACL
STP
SPAN
```

## Router

Primarily Layer 3.

Moves IP packets between networks.

```text
192.168.1.0/24
       ↓
     Router
       ↓
10.0.0.0/24
```

Uses a routing table.

## Server

Provides services such as:

```text
Web
DNS
DHCP
Database
Email
File Sharing
Directory Services
```

## Endpoint

End-user or workload device.

Examples:

```text
Laptop
Desktop
Phone
VM
Server
IoT Device
```

## Wireless Access Point

Connects Wi-Fi clients to a wired network.

## Modem / ONT

Connects local network equipment to ISP access technology.

## Gateway

Connects systems or networks.

A common example is the:

```text
Default Gateway
```

## Firewall

Enforces traffic policy.

```text
Source
Destination
Protocol
Port
State
Application
 ↓
ALLOW / DENY
```

## IDS

**Intrusion Detection System**

Detects suspicious traffic.

## IPS

**Intrusion Prevention System**

Can detect and block suspicious traffic.

## Proxy

### Forward Proxy

```text
Client
 ↓
Proxy
 ↓
Internet
```

### Reverse Proxy

```text
Internet
 ↓
Reverse Proxy
 ↓
Servers
```

## Load Balancer

```text
Clients
 ↓
Load Balancer
 ↓
S1 S2 S3
```

Improves:

```text
Scalability
Availability
Failover
```

---

# 5. MAC and IP Addresses

## MAC Address

Layer 2 identifier for an interface.

Example:

```text
00:1A:2B:3C:4D:5E
```

Traditional Ethernet MAC address:

```text
48 bits
```

Used by switches for local-frame forwarding.

MAC addresses can be spoofed.

Do not treat a MAC address alone as strong identity.

## IP Address

Logical Layer 3 address.

Examples:

```text
IPv4:
192.168.1.10

IPv6:
2001:db8::10
```

Used by routers for packet forwarding.

## MAC vs IP

```text
MAC
→ Local link delivery

IP
→ Routed network delivery
```

| MAC | IP |
|---|---|
| Layer 2 | Layer 3 |
| Frames | Packets |
| Switches use it | Routers use it |
| Local link | Routed networks |

---

# 6. OSI Model

The OSI model has seven layers:

```text
7 Application
6 Presentation
5 Session
4 Transport
3 Network
2 Data Link
1 Physical
```

Memory phrase:

```text
All People Seem To Need Data Processing
```

## Layer 1 — Physical

Concerned with raw transmission.

Examples:

```text
Copper
Fiber
Radio
Connectors
Signals
Repeaters
```

PDU:

```text
Bits
```

Security concerns:

```text
Physical tapping
Cable damage
Wireless jamming
Unauthorized access
```

## Layer 2 — Data Link

Examples:

```text
Ethernet
MAC Addresses
Switches
VLANs
```

PDU:

```text
Frame
```

Security concerns:

```text
ARP spoofing
MAC spoofing
VLAN hopping
Rogue switches
```

## Layer 3 — Network

Examples:

```text
IPv4
IPv6
ICMP
Routers
IPsec
```

PDU:

```text
Packet
```

Security concerns:

```text
IP spoofing
Routing attacks
ICMP abuse
```

## Layer 4 — Transport

Protocols:

```text
TCP
UDP
```

PDU:

```text
TCP → Segment
UDP → Datagram
```

Security concerns:

```text
SYN flood
Port scanning
Session attacks
UDP flooding
```

## Layer 5 — Session

Session creation, management, and teardown concepts.

Security concerns:

```text
Session hijacking
Token abuse
Session fixation
```

## Layer 6 — Presentation

Data representation.

Concepts:

```text
Encoding
Serialization
Compression
Encryption
```

## Layer 7 — Application

Network-facing services.

Examples:

```text
HTTP
DNS
SMTP
SSH
FTP
DHCP
```

---

# 7. TCP/IP Model

Common 4-layer model:

```text
4 Application
3 Transport
2 Internet
1 Network Access
```

Mapping:

```text
OSI 7,6,5
→ TCP/IP Application

OSI 4
→ TCP/IP Transport

OSI 3
→ TCP/IP Internet

OSI 2,1
→ TCP/IP Network Access
```

---

# 8. Encapsulation and PDUs

Sending:

```text
Application Data
   ↓
TCP/UDP Header
   ↓
IP Header
   ↓
Ethernet Header/Trailer
   ↓
Bits
```

This is:

```text
Encapsulation
```

Receiving reverses the process:

```text
Decapsulation
```

PDU names:

```text
Application → Data
TCP → Segment
UDP → Datagram
IP → Packet
Ethernet → Frame
Physical → Bits
```

---

# 9. Ethernet and ARP

## Ethernet

Typical Ethernet frame contains:

```text
Destination MAC
Source MAC
EtherType
Payload
Frame Check Sequence
```

## ARP

**Address Resolution Protocol**

Maps IPv4 address to MAC address on the local network.

```text
IPv4
 ↓ ARP
MAC
```

Example:

```text
Who has 192.168.1.20?
```

The owner replies with its MAC.

Security issue:

```text
ARP Spoofing / Poisoning
```

IPv6 uses Neighbor Discovery rather than ARP.

---

# 10. IPv4

IPv4 addresses are 32 bits.

Example:

```text
192.168.1.10
```

Four 8-bit sections:

```text
192 . 168 . 1 . 10
 8     8    8    8
```

Total address space:

```text
2^32
≈ 4.29 billion
```

Not all are globally usable host addresses.

---

# 11. Private and Public IPv4

RFC1918 private ranges:

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

Expanded:

```text
10.0.0.0 - 10.255.255.255

172.16.0.0 - 172.31.255.255

192.168.0.0 - 192.168.255.255
```

Private addresses are intended for private networks and are not globally routed on the public Internet.

## Public IP

Globally routable address assigned through the Internet addressing ecosystem.

## Loopback

Block:

```text
127.0.0.0/8
```

Most familiar:

```text
127.0.0.1
```

## IPv4 Link-Local

```text
169.254.0.0/16
```

May appear when normal address configuration is unavailable.

---

# 12. Subnetting and CIDR

Example:

```text
192.168.1.25/24
```

`/24` means:

```text
24 network bits
8 host bits
```

Equivalent mask:

```text
255.255.255.0
```

For:

```text
192.168.1.0/24
```

traditional subnet values:

```text
Network:
192.168.1.0

Typical hosts:
192.168.1.1 - 192.168.1.254

Broadcast:
192.168.1.255
```

## /26 Example

```text
192.168.1.0/26
```

Host bits:

```text
32 - 26 = 6
```

Total addresses:

```text
2^6 = 64
```

Subnets of a `/24` divided into `/26`:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

---

# 13. IPv6

IPv6 uses 128-bit addresses.

Example:

```text
2001:db8:1234:5678::10
```

Important characteristics:

```text
128-bit address space
No IPv4-style broadcast
Neighbor Discovery
SLAAC support
Extension headers
Large end-to-end addressing space
```

## Address Types

### Global Unicast

Globally routable.

Much current global unicast space falls under:

```text
2000::/3
```

### Link-Local

```text
fe80::/10
```

Used only on local link.

### Unique Local

```text
fc00::/7
```

Intended for local communications.

Common locally assigned portion:

```text
fd00::/8
```

### Loopback

```text
::1
```

### Unspecified

```text
::
```

### Multicast

```text
ff00::/8
```

IPv6 has no IPv4-style broadcast.

## Shortening

Full:

```text
2001:0db8:0000:0000:0000:ffff:0000:0001
```

Remove leading zeros:

```text
2001:db8:0:0:0:ffff:0:1
```

Compress one longest sequence of zero fields:

```text
2001:db8::ffff:0:1
```

`::` should appear only once in one IPv6 address.

---

# 14. IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address size | 32-bit | 128-bit |
| Loopback | `127.0.0.1` | `::1` |
| Broadcast | Yes | No IPv4-style broadcast |
| Local address resolution | ARP | Neighbor Discovery |
| Private/local concept | RFC1918 | ULA |
| NAT | Very common | Not needed for address conservation the same way |

## Important IPv6 Security Note

IPv6 traffic is **not automatically encrypted**.

Older training often says:

```text
IPv6 requires IPsec
```

Modern operational guidance does not mean all IPv6 traffic automatically uses IPsec.

You still need explicit:

```text
TLS
VPN
IPsec configuration
Firewall rules
Monitoring
```

IPv6 security concerns include:

```text
Rogue Router Advertisements
Neighbor Discovery abuse
Dual-stack blind spots
IPv6 tunneling
Extension-header inspection
IPv6 firewall gaps
```

---

# 15. NAT and PAT

**NAT = Network Address Translation**

Example:

```text
192.168.1.10
      ↓
NAT
      ↓
203.0.113.10
      ↓
Internet
```

## Static NAT

Fixed mapping:

```text
10.0.0.10
↔
203.0.113.10
```

## Dynamic NAT

Uses an external address pool.

## PAT / NAPT

Multiple internal connections share an external IP using translated ports.

```text
192.168.1.10:50001
        ↓
203.0.113.10:40001
```

```text
192.168.1.11:50002
        ↓
203.0.113.10:40002
```

## NAT Is Not a Firewall

```text
NAT
→ Address translation

Firewall
→ Security policy enforcement
```

A single appliance may perform both.

---

# 16. Core Network Protocols

Important protocols:

```text
ARP
IPv4
IPv6
ICMP
TCP
UDP
DNS
DHCP
NTP
HTTP
TLS
SSH
SMTP
```

## DNS

Maps names to records.

```text
example.com
 ↓
DNS
 ↓
IP address
```

Common records:

```text
A → IPv4
AAAA → IPv6
CNAME → Alias
MX → Mail
NS → Name server
TXT → Text
```

Security concerns:

```text
Cache poisoning
Spoofing
DNS tunneling
DDoS amplification
```

## DHCP

Provides:

```text
IP address
Subnet mask
Gateway
DNS
Lease
```

IPv4 DORA:

```text
Discover
Offer
Request
Acknowledge
```

## ICMP

Used for:

```text
Diagnostics
Error reporting
Control messages
```

Examples:

```text
Ping
Destination Unreachable
Time Exceeded
```

## NTP

Commonly:

```text
UDP 123
```

Used for time synchronization.

Secure NTP deployments can use:

```text
Network Time Security — NTS
```

---

# 17. Physical and Logical Ports

## Physical Port

Hardware connection.

Examples:

```text
RJ45 Ethernet
Fiber
Console
USB
```

## Logical Port

Transport-layer number associated with network services.

Example:

```text
192.168.1.10:443
```

means a service endpoint at logical TCP/UDP port 443 depending on protocol.

One IP can host many services because ports distinguish endpoints.

---

# 18. Port Ranges

IANA port categories:

```text
0-1023
System Ports

1024-49151
User Ports

49152-65535
Dynamic / Private Ports
```

Common terminology:

```text
System Ports
≈ Well-known ports

User Ports
≈ Often called registered ports
```

---

# 19. Common Protocols and Ports

| Port | Service | Transport | Purpose |
|---:|---|---|---|
| 20/21 | FTP | TCP | File transfer |
| 22 | SSH | TCP | Secure remote access |
| 23 | Telnet | TCP | Legacy remote terminal |
| 25 | SMTP | TCP | Mail transfer |
| 53 | DNS | TCP/UDP | Name resolution |
| 67/68 | DHCPv4 | UDP | Address configuration |
| 69 | TFTP | UDP | Simple file transfer |
| 80 | HTTP | TCP | Web |
| 110 | POP3 | TCP | Mail retrieval |
| 123 | NTP | UDP | Time |
| 143 | IMAP | TCP | Mail access |
| 161/162 | SNMP | UDP | Management/traps |
| 389 | LDAP | TCP/UDP | Directory |
| 443 | HTTPS | TCP | Secure web |
| 445 | SMB | TCP | File/service sharing |
| 465 | Mail submission TLS | TCP | Implicit TLS submission |
| 587 | Mail submission | TCP | Often STARTTLS |
| 636 | LDAPS | TCP | LDAP over TLS |
| 853 | DNS over TLS | TCP | Encrypted DNS transport |
| 993 | IMAPS | TCP | IMAP over TLS |
| 995 | POP3S | TCP | POP3 over TLS |
| 1433 | SQL Server | TCP | Database |
| 3306 | MySQL | TCP | Database |
| 3389 | RDP | TCP/UDP | Remote Desktop |
| 5432 | PostgreSQL | TCP | Database |

A port number does not prove which application is actually running.

---

# 20. Secure vs Insecure Protocols

| Legacy / Cleartext | Preferred Secure Approach |
|---|---|
| Telnet | SSH |
| HTTP | HTTPS |
| FTP | SFTP or FTPS |
| LDAP without TLS | LDAP over TLS / StartTLS |
| POP3 cleartext | POP3 with TLS |
| IMAP cleartext | IMAP with TLS |
| SNMPv1/v2c | SNMPv3 |
| Plain DNS when privacy is needed | DoT / DoH |

## FTP vs FTPS vs SFTP

```text
FTP
→ Original FTP protocol

FTPS
→ FTP protected with TLS

SFTP
→ SSH File Transfer Protocol
```

SFTP is a different protocol, not simply "FTP with SSH added."

## DNS

Traditional:

```text
53
```

DNS over TLS:

```text
TCP 853
```

DNS over HTTPS:

```text
HTTPS / 443
```

## DNSSEC vs DoT/DoH

```text
DNSSEC
→ Authenticity/integrity of DNS data

DoT / DoH
→ Encryption of DNS transport
```

## Email

More accurate than saying "SMTP 25 becomes secure on 587":

```text
25
→ SMTP server-to-server

587
→ Message submission, commonly STARTTLS

465
→ Message submission using implicit TLS
```

---

# 21. TCP vs UDP

## TCP

```text
Connection-oriented
Reliable
Ordered
Stateful
Byte stream
```

Features:

```text
Three-way handshake
Sequence numbers
Acknowledgments
Retransmission
Flow control
Congestion control
```

Examples:

```text
HTTPS
SSH
Email
Database connections
```

## UDP

```text
Connectionless
Message-oriented
No built-in delivery guarantee
No built-in ordering guarantee
Lower transport-layer overhead
```

Examples:

```text
DNS
DHCP
NTP
VoIP
Streaming
QUIC transport
```

Applications may implement their own reliability above UDP.

---

# 22. TCP Three-Way Handshake

TCP connection establishment:

```text
Client                    Server

SYN  -------------------->

     <---------------- SYN-ACK

ACK  -------------------->
```

Steps:

```text
1. Client sends SYN.
2. Server replies SYN-ACK.
3. Client sends ACK.
```

Connection is then established.

## Important Flags

```text
SYN
ACK
FIN
RST
PSH
URG
ECE
CWR
```

Simplified:

```text
SYN → Start/synchronize
ACK → Acknowledge
FIN → Graceful close
RST → Reset
```

---

# 23. Firewalls

A firewall enforces network policy.

May inspect:

```text
Source IP
Destination IP
Protocol
Port
Connection state
Application
Identity
Threat information
```

Example:

```text
ALLOW
Internet → Web Server
TCP 443
```

```text
DENY
Internet → Database
TCP 5432
```

## Firewall Types

### Packet Filtering

Checks headers.

### Stateful Firewall

Tracks session state.

```text
NEW
ESTABLISHED
RELATED
INVALID
```

### Proxy/Application Firewall

Intermediates application communication.

### NGFW

May combine:

```text
Stateful inspection
Application awareness
IPS
URL filtering
User identity
Malware detection
TLS inspection
```

### Host Firewall

Runs on endpoint/server.

### WAF

Protects HTTP applications specifically.

## Rule Design

Good practices:

```text
Default deny
Least privilege
Log important events
Document rules
Remove unused rules
Restrict management
Review regularly
```

---

# 24. Network Segmentation

Segmentation separates systems into controlled zones.

Bad:

```text
Flat Network
Everything talks to everything
```

Better:

```text
Users
Servers
Databases
Management
Guests
IoT
Production
Development
```

Benefits:

```text
Reduced lateral movement
Reduced blast radius
Better monitoring
Different policies
```

---

# 25. VLAN, DMZ, and Microsegmentation

## VLAN

Logical Layer 2 segmentation.

Example:

```text
VLAN 10 → Employees
VLAN 20 → Servers
VLAN 30 → Guests
```

VLANs are segmentation mechanics, but secure policy between segments still matters.

## DMZ

A neutral segment between untrusted external networks and internal trusted networks.

```text
Internet
 ↓
Firewall
 ↓
DMZ
 ↓
Firewall / Policy
 ↓
Internal Network
```

## Microsegmentation

Fine-grained workload policy.

```text
Web
 ↓ only required port
App
 ↓ only required DB port
Database
```

Common in:

```text
Cloud
Kubernetes
Virtualized data centers
Zero Trust
```

---

# 26. NAC, VPN, and ZTNA

## NAC

**Network Access Control**

May check:

```text
Identity
Device certificate
Patch state
EDR status
Device compliance
```

Example:

```text
Device
 ↓
802.1X / NAC
 ↓
Identity + Posture
 ↓
Corporate VLAN
or
Quarantine
```

## VPN

### Remote Access

```text
Remote User
 ↓
Encrypted Tunnel
 ↓
Company Network
```

### Site-to-Site

```text
Office A
 ↓
VPN
 ↓
Office B
```

## ZTNA

Zero Trust Network Access aims for:

```text
Identity-based
Application-specific
Context-aware
Least-privilege
```

instead of broad internal network access.

---

# 27. Active vs Passive Network Attacks

## Active

Attacker interacts with, injects, alters, or disrupts traffic/systems.

Examples:

```text
DoS
DDoS
SYN Flood
Spoofing
ARP Poisoning
DNS Poisoning
MITM manipulation
Replay
Session hijacking
```

## Passive

Attacker observes communications without intentionally changing them.

Examples:

```text
Packet sniffing
Eavesdropping
Traffic analysis
```

---

# 28. DoS and DDoS

## DoS

One or limited sources try to make a service unavailable.

## DDoS

Distributed sources attack the same target.

```text
Bot 1 ─┐
Bot 2 ─┤
Bot 3 ─┼→ Target
Bot 4 ─┘
```

Possible exhaustion:

```text
Bandwidth
CPU
Memory
Connection tables
Application capacity
```

Defenses:

```text
DDoS protection
CDN/Anycast
Rate limiting
Filtering
Autoscaling
SYN cookies
WAF
```

---

# 29. Fragmentation and Oversized-Packet Attacks

## Teardrop / Fragmentation

Historical attacks used malformed/overlapping fragments to break vulnerable reassembly.

Modern systems are more robust, but fragmentation remains relevant for:

```text
Evasion
Inspection bypass
Resource exhaustion
Parser bugs
```

## Oversized Packet / Ping-of-Death Style

Historical attacks attempted to exploit invalid or oversized reconstructed packets.

Modern lesson:

```text
Validate packet size
Validate fragments
Handle malformed input safely
```

---

# 30. Spoofing

Spoofing falsifies an identity/address.

Examples:

```text
IP spoofing
MAC spoofing
ARP spoofing
DNS spoofing
Email spoofing
```

Defenses can include:

```text
Ingress filtering
Egress filtering
Authentication
Stateful filtering
Anti-spoofing ACLs
```

## ARP Spoofing

Attacker sends false ARP information.

```text
Victim
 ↓
Attacker pretends to be gateway
 ↓
Gateway
```

Defenses:

```text
Dynamic ARP Inspection
DHCP Snooping
802.1X
Segmentation
Encryption
```

## DNS Spoofing

False DNS information causes a user to reach a malicious destination.

Defenses:

```text
DNSSEC validation
Secure resolver configuration
Patching
Transport protection
```

---

# 31. MITM

**Man-in-the-Middle**

```text
User
 ↓
Attacker
 ↓
Server
```

Attacker may:

```text
Observe
Relay
Modify
Inject
```

Defenses:

```text
TLS
Certificate validation
VPN
Mutual authentication
Secure Wi-Fi
Strong identity
```

Other related attacks:

```text
Replay
Session hijacking
Token theft
```

---

# 32. Passive Attacks

## Packet Sniffing

Captures traffic.

If traffic is cleartext, it may expose:

```text
Credentials
Email
Session data
Application content
```

Defenses:

```text
TLS
SSH
VPN
WPA3
Secure protocols
```

## Traffic Analysis

Even encrypted traffic exposes metadata:

```text
Source
Destination
Timing
Volume
Frequency
Packet sizes
```

## Important Scanning Correction

Port scanning is generally:

```text
Active Reconnaissance
```

because the scanner sends packets to the target.

Passive reconnaissance collects information without directly interacting with the target.

---

# 33. Wireless Network Security

Important controls:

```text
WPA2
WPA3
802.1X
Certificate authentication
Guest isolation
Rogue AP detection
Segmentation
Strong admin access
```

Avoid:

```text
WEP
Weak PSKs
Open management interfaces
Default credentials
```

---

# 34. Secure Network Design

Core principles:

```text
Least privilege
Default deny
Segmentation
Defense in depth
Strong authentication
Encryption
Monitoring
Redundancy
Secure management
Minimize public exposure
```

Example:

```text
Internet
 ↓
DDoS Protection
 ↓
Edge Firewall
 ↓
DMZ
 ↓
Internal Firewall
 ↓
┌────────┬────────┬────────┐
Users  Servers  Management
          ↓
       Database
```

---

# 35. Logging and Monitoring

Useful network logs:

```text
Firewall
DNS
DHCP
VPN
IDS/IPS
Authentication
Proxy
Flow logs
Wireless
Router
Switch
```

Architecture:

```text
Network Devices
 ↓
Central Logging
 ↓
SIEM
 ↓
Detection
 ↓
Incident Response
```

---

# 36. Network Security Tools

## Wireshark

Packet analysis.

Uses:

```text
Troubleshooting
Protocol analysis
Incident investigation
```

## tcpdump

Command-line packet capture.

## ping

Basic reachability/latency test where ICMP is permitted.

## traceroute / tracert

Shows network path behavior.

## nslookup / dig

DNS investigation.

## ipconfig / ip

Windows:

```text
ipconfig
```

Linux:

```text
ip address
ip route
```

## netstat / ss

Local sockets and connections.

## Nmap

Authorized network discovery/service identification.

Use only on systems and networks you own or have explicit permission to assess.

---

# 37. Data Center Networking

Terms:

```text
Rack
Rack Unit
Top-of-Rack Switch
Core
Aggregation
Access
Leaf
Spine
Redundant Links
High Availability
```

## Traditional Three-Tier

```text
Core
 ↓
Distribution
 ↓
Access
 ↓
Servers
```

## Leaf-Spine

```text
      Spine 1   Spine 2
       / | \     / | \
      /  |  \   /  |  \
   Leaf Leaf Leaf Leaf
     ↓    ↓    ↓
  Workloads
```

Benefits:

```text
Redundancy
Scalability
Predictable east-west paths
```

---

# 38. Cloud Networking

Cloud networking implements familiar concepts through software-defined services.

## AWS

```text
VPC
Subnet
Route Table
Security Group
Network ACL
Internet Gateway
NAT Gateway
Transit Gateway
PrivateLink
Load Balancer
```

## Azure

```text
VNet
Subnet
NSG
Route Table
Azure Firewall
Private Endpoint
Load Balancer
Application Gateway
```

## Google Cloud

```text
VPC
Subnet
Firewall Policy
Cloud NAT
Cloud Router
Private Service Connectivity
Load Balancer
```

Cloud-security principles:

```text
Private by default
Least privilege
Segment workloads
Control egress
Central logging
Private endpoints
Restrict administration
```

---

# 39. Python Examples

## IP Classification

```python
import ipaddress

addresses = [
    "192.168.1.10",
    "10.10.5.20",
    "8.8.8.8",
    "127.0.0.1",
    "169.254.10.20",
    "2001:db8::1",
    "::1",
]

for value in addresses:
    address = ipaddress.ip_address(value)

    print(
        value,
        "version=", address.version,
        "private=", address.is_private,
        "loopback=", address.is_loopback,
        "link_local=", address.is_link_local,
    )
```

## Subnet Calculation

```python
import ipaddress

network = ipaddress.ip_network(
    "192.168.10.0/26"
)

print("Network:", network.network_address)
print("Broadcast:", network.broadcast_address)
print("Mask:", network.netmask)
print("Total:", network.num_addresses)

hosts = list(network.hosts())

print("First host:", hosts[0])
print("Last host:", hosts[-1])
```

## Split a /24 into /26

```python
import ipaddress

network = ipaddress.ip_network(
    "192.168.1.0/24"
)

for subnet in network.subnets(
    new_prefix=26
):
    print(subnet)
```

Output:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

## Port Range Classifier

```python
def port_category(port: int) -> str:
    if not 0 <= port <= 65535:
        raise ValueError("Invalid port")

    if port <= 1023:
        return "System / Well-Known"

    if port <= 49151:
        return "User / Registered"

    return "Dynamic / Private"


for port in [22, 443, 3306, 50000]:
    print(port, port_category(port))
```

## TCP Localhost Server

```python
import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
) as server:

    server.bind((HOST, PORT))
    server.listen(1)

    connection, address = server.accept()

    with connection:
        data = connection.recv(1024)
        print(data.decode())

        connection.sendall(
            b"Hello from TCP server"
        )
```

## TCP Localhost Client

```python
import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
) as client:

    client.connect((HOST, PORT))

    client.sendall(
        b"Hello from TCP client"
    )

    print(
        client.recv(1024).decode()
    )
```

These examples use localhost only.

---

# 40. Corrections to the Supplied Slides

## IPv6 and IPsec

Do not memorize:

```text
IPv6 automatically uses IPsec.
```

Correct concept:

```text
IPv6 does not automatically encrypt traffic.
```

IPsec must actually be configured/used where required.

## Port Scanning

The passive-attack slide places scanning under passive attacks.

More accurate:

```text
Port scanning
→ Usually active reconnaissance
```

## SFTP

Do not memorize:

```text
SFTP = Secure FTP
```

Better:

```text
SFTP
→ SSH File Transfer Protocol

FTPS
→ FTP protected by TLS
```

## NTP

NTP is not simply the secure version of the legacy Time Protocol.

For secured NTP study:

```text
NTS
Network Time Security
```

## SMTP

Better mapping:

```text
25
→ SMTP transport

587
→ Message submission + commonly STARTTLS

465
→ Implicit TLS message submission
```

## NAT

```text
NAT ≠ Firewall
```

## TCP vs UDP

Too simple:

```text
TCP slow
UDP fast
```

Better:

```text
TCP has reliability/state/congestion mechanisms.

UDP has less transport-layer machinery.

Actual application performance depends on design and network conditions.
```

---

# 41. Interview and Exam Questions

## What is a network?

A group of connected computing devices that exchange data and resources.

## LAN vs WAN?

```text
LAN
→ Local area

WAN
→ Geographically separated networks
```

## Hub vs switch?

```text
Hub
→ Repeats to all ports

Switch
→ Uses MAC table to forward frames
```

## Switch vs router?

```text
Switch
→ Primarily Layer 2

Router
→ Primarily Layer 3
```

## MAC vs IP?

```text
MAC
→ Local link

IP
→ Routed network
```

## OSI layers?

```text
Application
Presentation
Session
Transport
Network
Data Link
Physical
```

## TCP/IP layers?

```text
Application
Transport
Internet
Network Access
```

## RFC1918 ranges?

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

## IPv4 loopback?

```text
127.0.0.1
```

## IPv6 loopback?

```text
::1
```

## NAT?

Translation of IP addresses, often combined with port translation.

## PAT?

Allows multiple internal connections to share an external address by translating port numbers.

## Three port ranges?

```text
0-1023
1024-49151
49152-65535
```

## TCP vs UDP?

```text
TCP
→ Connection-oriented, reliable, ordered

UDP
→ Connectionless, no built-in ordering or retransmission
```

## TCP handshake?

```text
SYN
SYN-ACK
ACK
```

## Firewall?

Security device/software that permits or denies traffic based on policy.

## VLAN?

Logical Layer 2 segmentation.

## DMZ?

Network segment between an untrusted external network and protected internal network.

## DDoS?

Distributed sources attempt to make a service unavailable.

## MITM?

Adversary intercepts communication between two parties.

## Passive attack?

Observes communication without intentionally modifying it.

## Is port scanning passive?

Usually no; it is active reconnaissance.

---

# 42. Final Review

## Network Types

```text
PAN
LAN
WLAN
CAN
MAN
WAN
SAN
VPN
Intranet
Extranet
```

## Devices

```text
Hub
Switch
Router
Server
Endpoint
AP
Modem
Gateway
Firewall
IDS
IPS
Proxy
Load Balancer
```

## OSI

```text
7 Application
6 Presentation
5 Session
4 Transport
3 Network
2 Data Link
1 Physical
```

## IPv4 Private

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

## IPv6

```text
Link-local:
fe80::/10

ULA:
fc00::/7

Loopback:
::1

Multicast:
ff00::/8
```

## Ports

```text
21 FTP
22 SSH
23 Telnet
25 SMTP
53 DNS
67/68 DHCP
80 HTTP
123 NTP
443 HTTPS
445 SMB
465 SMTP submission TLS
587 Mail submission
636 LDAPS
853 DoT
993 IMAPS
995 POP3S
3389 RDP
```

## Port Ranges

```text
0-1023
System

1024-49151
User

49152-65535
Dynamic / Private
```

## TCP

```text
Connection-oriented
Reliable
Ordered
Stateful

SYN
SYN-ACK
ACK
```

## UDP

```text
Connectionless
No built-in retransmission
No built-in ordering
Low transport overhead
```

## Defenses

```text
Firewall
IDS/IPS
VLAN
DMZ
Microsegmentation
NAC
VPN
ZTNA
Encryption
Logging
SIEM
```

## Active Attacks

```text
DoS
DDoS
SYN Flood
Spoofing
ARP Poisoning
DNS Poisoning
MITM
Replay
Session Hijacking
```

## Passive Attacks

```text
Sniffing
Eavesdropping
Traffic Analysis
```

---

# 43. Authoritative References

Use these standards for deeper study:

- **RFC 1918** — Address Allocation for Private Internets
- **RFC 9293** — Transmission Control Protocol
- **RFC 8200** — IPv6 Specification
- **RFC 8504** — IPv6 Node Requirements
- **RFC 9099** — Operational Security Considerations for IPv6 Networks
- **RFC 4193** — Unique Local IPv6 Unicast Addresses
- **RFC 4291** — IPv6 Addressing Architecture
- **RFC 8415** — DHCPv6
- **RFC 7858** — DNS over TLS
- **RFC 8314** — TLS for Email Submission and Access
- **RFC 8915** — Network Time Security
- **IANA Service Name and Transport Protocol Port Number Registry**
- **NIST SP 800-41 Rev. 1** — Guidelines on Firewalls and Firewall Policy
- **NIST SP 800-215** — Guide to a Secure Enterprise Network Landscape

---

# End of Document
