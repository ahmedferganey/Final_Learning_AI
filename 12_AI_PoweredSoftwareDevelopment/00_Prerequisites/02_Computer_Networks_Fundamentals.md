# 1. Topic Title

## Computer Networks Fundamentals

Networking is the foundation beneath cloud platforms, distributed applications, DevOps pipelines, remote administration, virtualization, containers, and cybersecurity.

The goal of this topic is not to memorize every protocol field. The goal is to build a mental model for what happens when one host communicates with another.

A useful high-level view is:

```text
Application
   ↓
Transport
   ↓
IP
   ↓
Ethernet / Wi-Fi
   ↓
Physical Network
   ↓
Ethernet / Wi-Fi
   ↓
IP
   ↓
Transport
   ↓
Application
```

For example, when a browser opens:

```text
https://example.com
```

the computer may need to perform:

```text
DNS Resolution
      ↓
Route Selection
      ↓
ARP / Neighbor Resolution
      ↓
TCP Connection
      ↓
TLS Negotiation
      ↓
HTTP Request
      ↓
HTTP Response
```

If any one of these steps fails, the user may simply see:

```text
"Website cannot be reached"
```

Networking fundamentals teach you how to determine **where the communication path failed and why**.

---

# 2. Learning Objectives

By the end of this topic, you should be able to:

1. Explain why networks use layers.
2. Map common protocols to the TCP/IP and OSI models.
3. Explain Ethernet frames and MAC addressing.
4. Explain how switches learn and forward traffic.
5. Explain IPv4 addressing and subnet prefixes.
6. Explain network, host, broadcast, and usable-address concepts.
7. Explain private and public IPv4 addressing.
8. Explain IPv6 at a foundational level.
9. Explain default gateways and routing tables.
10. Explain longest-prefix match.
11. Explain ARP and IPv6 Neighbor Discovery.
12. Explain TCP connection establishment, reliability, sequencing, acknowledgements, flow control, and congestion awareness.
13. Explain UDP and when it is appropriate.
14. Explain ports and sockets.
15. Explain DNS resolution and common record types.
16. Explain DHCP address assignment.
17. Explain NAT and PAT.
18. Explain stateful firewall behavior.
19. Explain ICMP and its troubleshooting role.
20. Explain common network devices such as switches, routers, firewalls, wireless access points, and load balancers.
21. Explain collision domains and broadcast domains conceptually.
22. Explain VLAN awareness and network segmentation.
23. Explain unicast, broadcast, multicast, and anycast awareness.
24. Explain MTU and fragmentation awareness.
25. Explain latency, bandwidth, throughput, packet loss, and jitter.
26. Use Windows and Linux tools to inspect network configuration.
27. Use `ping`, `traceroute`/`tracert`, `curl`, `ss`, `netstat`, DNS tools, and route inspection.
28. Distinguish DNS failure from IP reachability failure.
29. Distinguish a network failure from an application failure.
30. Build a two-host virtual network.
31. Design a simple office network.
32. Apply structured network troubleshooting.
33. Explain how networking fundamentals connect to cloud, Kubernetes, and cybersecurity.

---

# 3. Prerequisites

Required:

```text
00. Computer Architecture
01. Operating Systems Fundamentals
```

You should understand:

```text
Processes
Sockets
Ports
Operating-system network stack
Network interfaces
Drivers
IP configuration
Command-line basics
```

Basic binary arithmetic is useful but not required before beginning.

Subnetting will be introduced from first principles.

---

# 4. Core Concepts Explanation

# Part 1 — What a Computer Network Is

A computer network is a collection of devices connected so that they can exchange information.

Devices may include:

```text
Laptops
Servers
Phones
Routers
Switches
Firewalls
Printers
IoT devices
Cloud instances
Virtual machines
Containers
```

A simple network:

```text
Laptop A
   │
   │ Ethernet / Wi-Fi
   ↓
Switch / Access Point
   │
   ↓
Laptop B
```

A larger network:

```text
Client
  ↓
Switch
  ↓
Router
  ↓
ISP
  ↓
Internet
  ↓
Remote Router
  ↓
Server Network
  ↓
Server
```

The network's job is to move data between endpoints according to addressing, routing, protocol, and policy.

---

# Part 2 — Why Networks Use Layers

Networking is divided into layers because one giant protocol would be difficult to design, troubleshoot, replace, and scale.

Instead:

```text
Application Layer
      ↓
Transport Layer
      ↓
Internet / Network Layer
      ↓
Link Layer
      ↓
Physical Layer
```

Each layer solves a narrower problem.

For example:

```text
HTTP:
What does the application request?

TCP:
How are bytes reliably transported?

IP:
How does the packet reach another network?

Ethernet:
How does the frame reach a device on the local link?

Physical:
How are bits transmitted electrically, optically, or by radio?
```

Layering means HTTP does not need to understand the electrical signaling of Ethernet.

---

# Part 3 — Encapsulation

As data moves down the network stack, each layer adds information.

Conceptually:

```text
Application Data
      ↓
TCP Header + Data
      ↓
IP Header + TCP Segment
      ↓
Ethernet Header + IP Packet + Trailer
      ↓
Bits on wire/radio
```

At the receiving side, headers are processed in reverse:

```text
Bits
 ↓
Ethernet Frame
 ↓
IP Packet
 ↓
TCP Segment
 ↓
Application Data
```

This is called **encapsulation** and **decapsulation**.

---

# Part 4 — OSI Model

The OSI model has seven conceptual layers:

```text
7 Application
6 Presentation
5 Session
4 Transport
3 Network
2 Data Link
1 Physical
```

A simplified mapping:

```text
OSI                    TCP/IP

Application  ┐
Presentation ├──────→ Application
Session      ┘

Transport    ───────→ Transport

Network      ───────→ Internet

Data Link    ┐
Physical     ┴──────→ Link / Network Access
```

The OSI model is especially useful for troubleshooting vocabulary.

Example:

```text
Layer 1 issue:
Cable disconnected

Layer 2 issue:
Wrong VLAN

Layer 3 issue:
No route

Layer 4 issue:
TCP port blocked

Layer 7 issue:
Web application returns HTTP 500
```

---

# Part 5 — TCP/IP Model

A practical TCP/IP model is:

```text
Application
Transport
Internet
Link
Physical (often discussed separately)
```

Common protocols:

```text
Application:
HTTP
HTTPS
DNS
SSH
SMTP
DHCP

Transport:
TCP
UDP

Internet:
IPv4
IPv6
ICMP

Link:
Ethernet
Wi-Fi
ARP-related local delivery behavior
```

A packet capture becomes easier to understand when you recognize these layers.

---

# Part 6 — Physical Layer

The physical layer carries bits.

Media include:

```text
Copper cable
Fiber optic cable
Radio / Wi-Fi
```

Problems include:

```text
Disconnected cable
Damaged cable
Bad transceiver
Signal interference
Incorrect speed/duplex in some environments
Wi-Fi signal loss
```

No higher-layer troubleshooting will succeed if the physical link is down.

---

# Part 7 — Ethernet

Ethernet is a common local-network technology.

A simplified Ethernet frame:

```text
+----------------+----------------+-----------+---------+
| Destination MAC| Source MAC     | Type      | Payload |
+----------------+----------------+-----------+---------+
                                         + FCS/trailer concept
```

The payload may contain an IPv4 or IPv6 packet.

Ethernet generally operates within a local Layer-2 broadcast domain.

---

# Part 8 — MAC Address

A MAC address identifies a network interface at the link layer.

Example format:

```text
00:1A:2B:3C:4D:5E
```

MAC addresses are used for local frame delivery.

Important:

```text
MAC address != IP address
```

MAC addresses are primarily local-link identifiers.

IP addresses are logical addresses used for communication across networks.

---

# Part 9 — MAC vs IP

A useful analogy:

```text
MAC = local delivery identity
IP  = routed logical address
```

Suppose:

```text
PC:
IP 192.168.1.10
MAC AA:AA:AA:AA:AA:AA

Gateway:
IP 192.168.1.1
MAC BB:BB:BB:BB:BB:BB
```

When the PC sends traffic to a remote Internet server:

```text
Ethernet destination MAC:
Gateway MAC

IP destination:
Remote server IP
```

The Layer-2 destination changes at each routed hop, while the Layer-3 destination normally remains the remote IP end-to-end unless translation occurs.

---

# Part 10 — Network Switch

A switch connects devices on a Layer-2 network.

```text
PC1 ─┐
PC2 ─┼─ Switch ─ Server
PC3 ─┘
```

A switch learns source MAC addresses.

Conceptually:

```text
Frame arrives:
Source MAC = AA
Ingress port = 1

Switch learns:
AA → Port 1
```

Later:

```text
Destination MAC = AA
      ↓
Forward only to Port 1
```

---

# Part 11 — MAC Address Table

A switch maintains a forwarding table:

```text
MAC Address          Port
AA:AA:AA:AA:AA:AA    1
BB:BB:BB:BB:BB:BB    2
CC:CC:CC:CC:CC:CC    5
```

If the destination MAC is unknown, the switch may flood the frame within the relevant broadcast domain.

Once the destination responds, the switch learns the location.

---

# Part 12 — Broadcast

A broadcast is delivered to all devices in a broadcast domain.

Ethernet broadcast MAC:

```text
FF:FF:FF:FF:FF:FF
```

ARP requests commonly use Ethernet broadcast.

Broadcast traffic is not normally routed across routers.

This is one reason routers and VLANs divide broadcast domains.

---

# Part 13 — Collision Domain Awareness

Historically, shared Ethernet hubs created one collision domain.

Modern switched Ethernet generally gives each switch port its own collision domain.

Conceptually:

```text
Hub:
many devices share medium

Switch:
each port is separate switched link
```

This greatly improves Ethernet efficiency.

---

# Part 14 — Broadcast Domain

A broadcast domain is the set of devices that receive the same Layer-2 broadcast.

A router separates broadcast domains.

```text
LAN A
  ↓
Router
  ↓
LAN B
```

Broadcast from LAN A does not simply pass into LAN B.

VLANs can also create separate logical broadcast domains on switches.

---

# Part 15 — VLAN Awareness

A VLAN creates logical Layer-2 segmentation.

Example:

```text
Switch

VLAN 10:
PC1
PC2

VLAN 20:
Server1
Server2
```

Devices in different VLANs require Layer-3 routing to communicate.

Why VLANs matter:

```text
Segmentation
Broadcast control
Security boundaries
Department separation
Voice/data separation
```

Detailed VLAN configuration belongs to later Cisco courses.

---

# Part 16 — Router

A router forwards IP packets between networks.

Example:

```text
192.168.10.0/24
       ↓
     Router
       ↓
192.168.20.0/24
```

A router examines the destination IP and its routing table.

It does not route based on the final destination MAC address across the whole Internet.

---

# Part 17 — IPv4 Address

IPv4 uses 32 bits.

Example:

```text
192.168.10.25
```

In binary:

```text
192      168       10       25

11000000 10101000 00001010 00011001
```

Four groups of 8 bits are called octets.

---

# Part 18 — Subnet Prefix

A prefix length indicates how many leading bits represent the network.

Example:

```text
192.168.10.25/24
```

`/24` means:

```text
Network bits = 24
Host bits    = 8
```

Mask:

```text
255.255.255.0
```

Binary:

```text
11111111.11111111.11111111.00000000
```

---

# Part 19 — Network Address

For:

```text
192.168.10.25/24
```

network:

```text
192.168.10.0
```

Conceptually:

```text
192.168.10 = network
25         = host portion
```

The network address identifies the subnet itself.

---

# Part 20 — Broadcast Address

For:

```text
192.168.10.0/24
```

traditional IPv4 subnet broadcast address:

```text
192.168.10.255
```

This represents all host bits set to `1`.

Normal host addresses in that traditional subnet range:

```text
192.168.10.1
through
192.168.10.254
```

---

# Part 21 — /24 Subnet Capacity

A `/24` leaves 8 host bits.

```text
2^8 = 256 total addresses
```

Traditional usable host count:

```text
256 - network address - broadcast address
= 254
```

This traditional formula is useful for normal LAN subnetting.

Some point-to-point and provider environments use special prefix semantics, so treat it as the standard introductory rule rather than a universal law.

---

# Part 22 — Common Prefixes

Useful examples:

```text
/8   → 255.0.0.0
/16  → 255.255.0.0
/24  → 255.255.255.0
/25  → 255.255.255.128
/26  → 255.255.255.192
/27  → 255.255.255.224
/28  → 255.255.255.240
/30  → 255.255.255.252
```

The more network bits:

```text
larger prefix
      ↓
smaller subnet
```

---

# Part 23 — Simple Subnetting Method

Suppose:

```text
192.168.1.0/24
```

Need two equal subnets.

Borrow one host bit:

```text
/24 → /25
```

Result:

```text
192.168.1.0/25
192.168.1.128/25
```

Each has 128 total addresses.

Traditional usable hosts:

```text
126
```

---

# Part 24 — Four /26 Subnets

Split:

```text
192.168.1.0/24
```

into four equal subnets:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

Block size:

```text
256 - 192 = 64
```

That block-size technique is useful when learning subnetting.

---

# Part 25 — Private IPv4 Ranges

Private IPv4 address ranges commonly used internally:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

They are not globally routed on the public Internet.

Organizations reuse them internally.

A NAT device often translates private addresses when hosts access the Internet.

---

# Part 26 — Public IPv4 Address

A public IP is globally routable according to Internet routing and allocation.

Example conceptual flow:

```text
Private Host:
192.168.1.50

NAT Router:
Public IP 203.0.113.10

Internet sees:
203.0.113.10
```

The example addresses in documentation ranges are illustrative only.

---

# Part 27 — Loopback Address

IPv4 loopback:

```text
127.0.0.1
```

IPv6 loopback:

```text
::1
```

A loopback test verifies the local networking stack without sending traffic to the external network.

Example:

```bash
ping 127.0.0.1
```

If loopback fails, the problem is local to the host/network stack rather than the physical LAN.

---

# Part 28 — Link-Local Address Awareness

IPv4 link-local addresses may appear in:

```text
169.254.0.0/16
```

on systems unable to obtain normal configuration in certain environments.

A machine unexpectedly showing a `169.254.x.x` address may indicate DHCP failure.

Do not assume this is always an error; understand the intended network design.

---

# Part 29 — IPv6 Fundamentals

IPv6 uses 128-bit addresses.

Example:

```text
2001:db8:1234:1::10
```

IPv6 was designed to provide a vastly larger address space and modernize network behavior.

Common concepts:

```text
128-bit addresses
hexadecimal notation
prefix lengths
link-local addresses
Neighbor Discovery
no broadcast in the IPv4 sense
```

---

# Part 30 — IPv6 Address Compression

IPv6 allows leading zeros in groups to be omitted.

Example:

```text
2001:0db8:0000:0000:0000:0000:0000:0010
```

can become:

```text
2001:db8::10
```

The `::` compression can normally be used once in one textual address representation.

---

# Part 31 — IPv6 Prefix

A common LAN prefix:

```text
/64
```

Example:

```text
2001:db8:1234:1::10/64
```

The first 64 bits identify the subnet in common IPv6 LAN design.

Detailed IPv6 addressing and subnet planning belong later in the networking track.

---

# Part 32 — Link-Local IPv6

IPv6 interfaces normally have link-local addresses in:

```text
fe80::/10
```

These addresses are important for local-link operations including Neighbor Discovery and routing behavior.

They are not globally routed across the Internet.

---

# Part 33 — Default Gateway

A default gateway is the router used when no more-specific route matches the destination.

Host:

```text
IP:      192.168.10.25/24
Gateway: 192.168.10.1
```

Destination:

```text
8.8.8.8
```

The host determines:

```text
8.8.8.8 is not local
      ↓
Send packet to gateway
```

---

# Part 34 — Host Routing Table

Every IP host has a routing table.

Linux:

```bash
ip route
```

Windows:

```powershell
Get-NetRoute
```

Example conceptual table:

```text
Destination        Next Hop
192.168.10.0/24    directly connected
10.10.0.0/16       192.168.10.2
0.0.0.0/0          192.168.10.1
```

---

# Part 35 — Longest-Prefix Match

If multiple routes match, the most specific route wins.

Example:

```text
10.0.0.0/8       → Router A
10.10.0.0/16     → Router B
10.10.10.0/24    → Router C
```

Destination:

```text
10.10.10.25
```

All three routes match.

Most specific:

```text
/24
```

Therefore Router C is selected.

---

# Part 36 — Directly Connected Destination

Suppose host:

```text
192.168.1.10/24
```

Destination:

```text
192.168.1.20
```

The destination is in the same subnet.

The host does **not** need to send the packet to the default gateway.

Instead:

```text
Resolve destination MAC
      ↓
Send frame directly to host
```

---

# Part 37 — Remote Destination

Host:

```text
192.168.1.10/24
```

Destination:

```text
10.20.30.40
```

The host determines it is remote.

It resolves the gateway's MAC, not the remote server's MAC.

```text
Ethernet:
Destination MAC = gateway

IP:
Destination IP = 10.20.30.40
```

This is one of the most important networking concepts.

---

# Part 38 — ARP

ARP resolves local IPv4 addresses to MAC addresses.

Example:

```text
Host wants 192.168.1.20
      ↓
"Who has 192.168.1.20?"
      ↓ broadcast
192.168.1.20 replies:
"I am at AA:BB:CC:DD:EE:FF"
```

The mapping is cached temporarily.

---

# Part 39 — ARP Table

Linux:

```bash
ip neigh
```

Windows:

```powershell
arp -a
```

or neighbor-related cmdlets where available.

Example:

```text
192.168.1.1 → 00:11:22:33:44:55
```

If a local host was recently contacted, its MAC may appear in the neighbor table.

---

# Part 40 — IPv6 Neighbor Discovery

IPv6 does not use ARP.

It uses Neighbor Discovery Protocol behavior carried through ICMPv6.

It handles functions such as:

```text
Neighbor address resolution
Router discovery
Reachability
Prefix information
```

ICMPv6 is therefore essential to normal IPv6 operation.

Blocking all ICMPv6 blindly can break IPv6 networking.

---

# Part 41 — ICMP

ICMP provides network control and diagnostic messages.

Common uses:

```text
Echo request/reply → ping
Destination unreachable
Time exceeded
Path MTU-related signaling
```

ICMP is not an application transport protocol like TCP or UDP.

---

# Part 42 — ping

`ping` usually sends ICMP Echo Request messages.

Example:

```bash
ping 192.168.1.1
```

Useful questions:

```text
Does DNS need to work?
If using IP directly, no.

Does ping prove TCP/443 works?
No.

Can firewall block ping while web works?
Yes.
```

Therefore ping is one test, not a universal connectivity test.

---

# Part 43 — TTL / Hop Limit

IPv4 uses TTL; IPv6 uses Hop Limit.

Each router reduces the value.

If it reaches zero, the packet is discarded.

This prevents routing loops from circulating packets forever.

Conceptually:

```text
TTL 64
 ↓ router
63
 ↓ router
62
```

Traceroute techniques take advantage of this behavior.

---

# Part 44 — traceroute / tracert

Linux:

```bash
traceroute example.com
```

or:

```bash
tracepath example.com
```

Windows:

```powershell
tracert example.com
```

Traceroute estimates the sequence of routed hops.

Important:

Some routers do not reply to probes.

Therefore:

```text
* * *
```

does not automatically mean traffic cannot pass beyond that router.

---

# Part 45 — TCP

TCP provides a connection-oriented byte stream.

Major properties:

```text
Connection establishment
Sequencing
Acknowledgements
Retransmission
Flow control
Congestion control
Ordered delivery to application
```

TCP is used by protocols such as:

```text
HTTPS
SSH
SMTP
Many database connections
```

---

# Part 46 — TCP Three-Way Handshake

Simplified:

```text
Client                     Server

SYN  --------------------→
     ←------------------- SYN-ACK
ACK  --------------------→
```

After this:

```text
Connection established
```

The handshake synchronizes connection state.

---

# Part 47 — TCP Sequence Numbers

TCP numbers bytes in the stream.

Conceptually:

```text
Client sends:
bytes 1–1000

Server acknowledges:
next expected = 1001
```

If data is lost, TCP can retransmit it.

This is how TCP provides reliable ordered delivery.

---

# Part 48 — TCP Acknowledgement

Acknowledgements tell the sender which data has been received.

Simplified:

```text
Sender:
Segment A
Segment B
Segment C

Receiver:
ACK next expected byte
```

TCP implementations optimize this behavior significantly, but the concept is:

```text
Send
Track
Acknowledge
Retransmit if needed
```

---

# Part 49 — TCP Retransmission

If a segment is lost:

```text
Sender sends segment
      ↓
No expected acknowledgement
      ↓
Retransmit
```

Packet loss therefore may not immediately break a TCP application.

But high loss can reduce throughput and increase latency dramatically.

---

# Part 50 — TCP Flow Control

Flow control prevents the sender from overwhelming the receiver.

Receiver advertises how much buffer space is available.

Conceptually:

```text
Receiver:
"I can accept X more bytes."
```

This is different from congestion control.

---

# Part 51 — TCP Congestion Control Awareness

Congestion control adjusts sending behavior based on network conditions.

Goal:

```text
Do not overwhelm network paths.
```

TCP performance therefore depends on:

```text
Latency
Packet loss
Bandwidth
Congestion
Window behavior
```

A high-bandwidth link with severe loss can perform poorly.

---

# Part 52 — TCP Connection Termination

A graceful TCP close typically exchanges FIN/ACK signaling.

Conceptually:

```text
Side A: FIN
Side B: ACK
Side B: FIN
Side A: ACK
```

A reset (`RST`) indicates an abrupt connection termination or refusal in certain circumstances.

---

# Part 53 — UDP

UDP sends independent datagrams.

It does not provide TCP's built-in:

```text
Connection establishment
Reliable retransmission
Ordered byte stream
Flow control
```

This reduces transport overhead and latency.

Applications choose UDP when these semantics fit the workload.

---

# Part 54 — TCP vs UDP

Comparison:

```text
TCP                          UDP

Connection-oriented         Connectionless
Reliable byte stream        Datagram-oriented
Ordered delivery            No built-in ordering
Retransmission               No built-in retransmission
More transport state        Less transport state
```

Use case matters more than declaring one "better."

---

# Part 55 — Common UDP Uses

Examples include:

```text
Many DNS queries
Real-time voice/video
Some gaming traffic
Telemetry
Modern protocols that implement reliability above UDP
```

For example, QUIC uses UDP as a substrate while implementing richer transport behavior above it.

---

# Part 56 — Port

A port identifies a transport endpoint on a host.

Example:

```text
Server IP: 192.168.1.50
TCP Port: 443
```

Together:

```text
192.168.1.50:443
```

A web server may listen on TCP/443.

---

# Part 57 — Well-Known Ports

Common examples:

```text
20/21  FTP concepts
22     SSH
25     SMTP
53     DNS
67/68  DHCPv4
80     HTTP
110    POP3
123    NTP
143    IMAP
443    HTTPS
445    SMB
3389   RDP
```

Ports are conventions, not magic.

An administrator could run HTTP on:

```text
8080
```

or SSH on another configured port.

Do not infer application identity from port number alone.

---

# Part 58 — Client Ephemeral Port

A client usually uses a temporary high-numbered source port.

Example:

```text
Client:
192.168.1.10:53000

Server:
203.0.113.20:443
```

Connection:

```text
192.168.1.10:53000
       →
203.0.113.20:443
```

The server's port identifies the service.

The client's ephemeral port distinguishes concurrent connections.

---

# Part 59 — Socket

A socket represents a communication endpoint.

A TCP connection can be identified by:

```text
Protocol
Source IP
Source Port
Destination IP
Destination Port
```

Example:

```text
TCP
192.168.1.10:53000
203.0.113.20:443
```

This tuple lets many connections coexist.

---

# Part 60 — Listening Socket

A server process creates a listening socket.

Linux:

```bash
ss -ltnp
```

Windows:

```powershell
Get-NetTCPConnection -State Listen
```

Example:

```text
0.0.0.0:8080 LISTEN
```

Meaning:

The process is listening on TCP/8080 on all IPv4 interfaces, subject to OS/network policy.

---

# Part 61 — Established Connection

Linux:

```bash
ss -tnp
```

Windows:

```powershell
Get-NetTCPConnection -State Established
```

An established TCP connection indicates handshake completion and active connection state.

It does **not** guarantee the application-level transaction succeeded.

---

# Part 62 — DNS

DNS translates names into records.

Example:

```text
www.example.com
      ↓
DNS resolver
      ↓
IP address
      ↓
TCP/TLS/HTTP connection
```

Without DNS, users could theoretically connect to IP addresses, but modern Internet applications depend heavily on names.

---

# Part 63 — DNS Resolver

Your operating system usually sends DNS queries to a configured recursive resolver.

Flow:

```text
Application
   ↓
OS resolver
   ↓
Recursive DNS server
   ↓
DNS hierarchy / cache
   ↓
Answer
```

The resolver may return cached information without querying authoritative servers every time.

---

# Part 64 — DNS Hierarchy

Simplified:

```text
Root
 ↓
Top-Level Domain (.com)
 ↓
Authoritative server for example.com
 ↓
Record for www.example.com
```

Recursive resolvers perform/cache this process on behalf of clients.

---

# Part 65 — A Record

An `A` record maps a name to an IPv4 address.

Example:

```text
app.example.com
      ↓
192.0.2.10
```

Query Windows:

```powershell
Resolve-DnsName example.com -Type A
```

Linux if available:

```bash
dig example.com A
```

or:

```bash
getent ahostsv4 example.com
```

---

# Part 66 — AAAA Record

An `AAAA` record maps a name to IPv6.

Example:

```text
app.example.com
      ↓
2001:db8::10
```

Query:

```powershell
Resolve-DnsName example.com -Type AAAA
```

---

# Part 67 — CNAME

A CNAME creates an alias.

Example:

```text
www.example.com
      ↓ CNAME
frontend.example.net
```

The resolver then obtains address records for the canonical name.

---

# Part 68 — MX

MX records identify mail exchangers for a domain.

Example conceptual:

```text
example.com
MX 10 mail1.example.com
MX 20 mail2.example.com
```

Lower preference values are generally preferred.

---

# Part 69 — TXT

TXT records store text.

They are used for many purposes such as:

```text
Domain verification
Email-security metadata
Service configuration metadata
```

Do not assume all TXT records are human-readable documentation.

---

# Part 70 — DNS Cache

Resolvers and operating systems cache DNS results.

Benefits:

```text
Lower latency
Less DNS traffic
```

But cache means changes may not appear immediately everywhere.

TTL controls how long DNS information may be cached.

---

# Part 71 — DNS Failure vs Network Failure

Suppose:

```text
ping 8.8.8.8 works
ping example.com fails
```

Potential issue:

```text
DNS
```

But:

```text
ping example.com resolves to IP
yet HTTPS fails
```

Then DNS may be working and the issue may be TCP/443, TLS, firewall, or application.

Always test layers separately.

---

# Part 72 — DHCP

DHCP automatically supplies network configuration.

Typical information:

```text
IP address
Subnet mask/prefix
Default gateway
DNS server
Lease duration
```

Without DHCP, administrators can assign static addresses manually.

---

# Part 73 — DHCP DORA Process

A classic DHCPv4 sequence:

```text
Client                DHCP Server

DISCOVER  ----------→
         ←----------- OFFER
REQUEST   ----------→
         ←----------- ACK
```

Remember:

```text
D O R A
Discover
Offer
Request
Acknowledge
```

This is a useful introductory model.

---

# Part 74 — DHCP Lease

DHCP addresses are leased for a period.

The client attempts to renew before expiration.

Benefits:

```text
Automatic configuration
Address reuse
Central management
```

Potential issue:

If DHCP fails, new clients may lack valid addressing.

---

# Part 75 — Static IP

A static IP is manually or centrally assigned rather than dynamically leased in the normal client sense.

Often used for:

```text
Routers
Servers
Network devices
Infrastructure
```

But many environments use DHCP reservations instead of manual local static configuration.

The important requirement is predictable addressing, not the specific method.

---

# Part 76 — NAT

Network Address Translation changes IP address information as packets cross a translation point.

Common example:

```text
Inside:
192.168.1.10

Router public address:
203.0.113.5

Internet sees:
203.0.113.5
```

NAT is commonly used because private IPv4 addresses are not public Internet addresses.

---

# Part 77 — PAT / NAT Overload

Many private hosts can share one public IPv4 address by translating transport ports.

Example:

```text
192.168.1.10:50000 ─┐
192.168.1.11:51000 ─┼→ 203.0.113.5:translated ports
192.168.1.12:52000 ─┘
```

The translation table tracks flows.

This is commonly called Port Address Translation or NAT overload.

---

# Part 78 — NAT Is Not a Firewall

NAT changes addresses.

A firewall enforces traffic policy.

They may exist on the same device:

```text
Home Router
├── NAT
├── Firewall
├── DHCP
├── DNS forwarding
└── Wi-Fi
```

But they are conceptually different functions.

---

# Part 79 — Firewall

A firewall evaluates traffic against rules.

Example policy:

```text
Allow:
Internet → Web Server TCP/443

Deny:
Internet → Database TCP/5432
```

Firewalls may exist:

```text
On host
On router
At cloud security layer
As dedicated appliance
In Kubernetes/network policy
```

---

# Part 80 — Stateless Firewall Awareness

A simple stateless firewall evaluates individual packets using rule criteria.

Example:

```text
Source IP
Destination IP
Protocol
Source port
Destination port
```

It does not necessarily remember connection state.

---

# Part 81 — Stateful Firewall

A stateful firewall tracks connections.

Example:

```text
Client → Server TCP/443
Allowed

Server reply
Allowed because related to established connection
```

This is common in modern firewalls.

State tables are therefore operational resources that can also become exhausted under extreme loads.

---

# Part 82 — Allowlist vs Denylist

Allowlist approach:

```text
Deny by default
Allow explicitly required traffic
```

Denylist approach:

```text
Allow broadly
Block known unwanted traffic
```

For security boundaries, default-deny with explicit required access is generally easier to reason about.

---

# Part 83 — Wireless Access Point

A wireless access point bridges Wi-Fi clients into a network.

```text
Laptop
  )) Wi-Fi ((
Access Point
      │
    Ethernet
      │
    Switch
```

Wi-Fi introduces additional considerations:

```text
Signal strength
Interference
Channel use
Authentication
Encryption
Roaming
```

Detailed wireless engineering comes later.

---

# Part 84 — Hub vs Switch

Hub:

```text
Frame received
  ↓
Repeats to all ports
```

Switch:

```text
Frame received
  ↓
Looks at destination MAC
  ↓
Forwards intelligently
```

Hubs are largely obsolete in modern Ethernet networks.

---

# Part 85 — Router vs Switch

Switch:

```text
Layer 2
MAC-based forwarding
within broadcast domain/VLAN
```

Router:

```text
Layer 3
IP-based forwarding
between networks
```

Modern devices can combine both functions, but the conceptual distinction remains important.

---

# Part 86 — Firewall vs Router

Router decides:

```text
Where should this packet go?
```

Firewall decides:

```text
Should this traffic be allowed?
```

One device can do both.

---

# Part 87 — Load Balancer Awareness

A load balancer distributes client traffic among backend servers.

```text
Clients
   ↓
Load Balancer
 ┌─┼─┐
 ↓ ↓ ↓
S1 S2 S3
```

It may operate at:

```text
Layer 4
or
Layer 7
```

depending on design.

Cloud application architectures rely heavily on load balancers.

---

# Part 88 — Proxy Awareness

A proxy acts as an intermediary.

Forward proxy:

```text
Client → Proxy → Internet
```

Reverse proxy:

```text
Internet → Reverse Proxy → Servers
```

Reverse proxies often provide:

```text
TLS termination
Routing
Load balancing
Caching
Security controls
```

---

# Part 89 — Bandwidth

Bandwidth is the theoretical/available capacity of a link.

Example:

```text
1 Gbit/s
```

It does not mean every application will always achieve 1 Gbit/s.

Actual performance depends on:

```text
Protocol overhead
Latency
Loss
Server/client capability
Congestion
Storage performance
```

---

# Part 90 — Throughput

Throughput is the rate of useful data actually transferred.

Example:

```text
Link capacity: 1 Gbit/s
Measured throughput: 600 Mbit/s
```

The difference may be normal depending on workload and overhead.

---

# Part 91 — Latency

Latency is the time for data to travel and be processed.

Often measured in milliseconds.

Example:

```text
Local LAN: low latency
Intercontinental path: much higher latency
```

Application performance can be latency-sensitive even when bandwidth is high.

---

# Part 92 — Round-Trip Time

RTT is the time for traffic to travel to a destination and for a response to return.

`ping` commonly reports RTT.

Example:

```text
time=25 ms
```

RTT influences protocols such as TCP and interactive application performance.

---

# Part 93 — Packet Loss

Packet loss means transmitted packets do not reach the destination.

Causes may include:

```text
Congestion
Faulty link
Wireless interference
Overloaded device
Policy/rate limiting
Hardware issue
```

TCP retransmits lost data, but repeated loss reduces performance.

---

# Part 94 — Jitter

Jitter is variation in packet delay.

Example:

```text
Packet 1: 10 ms
Packet 2: 12 ms
Packet 3: 80 ms
Packet 4: 11 ms
```

Average latency may look acceptable while jitter harms:

```text
Voice
Video
Gaming
Real-time systems
```

---

# Part 95 — MTU

MTU is the maximum packet/frame payload size supported by a link at a relevant layer.

Common Ethernet IP MTU:

```text
1500 bytes
```

If packets exceed path constraints, fragmentation or Path MTU mechanisms become relevant.

Incorrect MTU can produce strange symptoms where:

```text
small pings work
large transfers fail or stall
```

---

# Part 96 — Fragmentation Awareness

IPv4 may fragment packets under certain conditions.

Fragmentation increases overhead and can cause operational/security complications.

IPv6 routers do not fragment packets in the same way; endpoints rely on Path MTU Discovery behavior.

At fundamentals level, remember:

```text
Avoid unnecessary fragmentation.
Understand path MTU.
```

---

# Part 97 — Unicast

Unicast is one sender to one destination.

```text
Host A → Host B
```

Most ordinary client/server traffic is unicast.

---

# Part 98 — Broadcast

Broadcast is one sender to all devices in a local broadcast domain.

```text
Host → all local hosts
```

IPv4 uses broadcast for certain local functions.

IPv6 does not use broadcast in the same way.

---

# Part 99 — Multicast Awareness

Multicast sends traffic to members of a group.

```text
Sender → multicast group → subscribed receivers
```

Useful for certain streaming, routing, and discovery protocols.

Network devices may require multicast-specific handling.

---

# Part 100 — Anycast Awareness

Anycast uses the same IP address from multiple network locations.

Routing directs a client to one reachable/best location.

Common uses include:

```text
Global DNS services
CDN edge services
Distributed infrastructure
```

Anycast is a routing technique, not a transport protocol.

---

# Part 101 — Network Interface

An OS network interface represents a physical or virtual network adapter.

Linux:

```bash
ip link
ip addr
```

Windows:

```powershell
Get-NetAdapter
Get-NetIPAddress
```

Interfaces can be:

```text
Ethernet
Wi-Fi
Loopback
VPN
Virtual machine adapters
Container bridges
Tunnel interfaces
```

---

# Part 102 — Interface State

An interface may be:

```text
Administratively enabled
Link up/down
Configured/unconfigured
```

Linux:

```bash
ip link
```

Windows:

```powershell
Get-NetAdapter
```

Before troubleshooting DNS or routing, confirm the interface itself is operational.

---

# Part 103 — Default Route

A default route matches destinations not covered by more-specific routes.

IPv4 default:

```text
0.0.0.0/0
```

IPv6 default:

```text
::/0
```

Linux:

```bash
ip route
```

Windows:

```powershell
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```

---

# Part 104 — DNS Configuration Inspection

Linux:

```bash
resolvectl status
```

or:

```bash
cat /etc/resolv.conf
```

depending on system.

Windows:

```powershell
Get-DnsClientServerAddress
```

Record which resolver the host actually uses.

---

# Part 105 — Windows Network Inspection

Useful PowerShell commands:

```powershell
Get-NetAdapter
Get-NetIPConfiguration
Get-NetIPAddress
Get-NetRoute
Get-DnsClientServerAddress
Get-NetTCPConnection
Test-NetConnection
Resolve-DnsName
```

These correspond to:

```text
Interface
Address
Route
DNS
Sockets
Connectivity
Resolution
```

---

# Part 106 — Linux Network Inspection

Useful commands:

```bash
ip link
ip addr
ip route
ip neigh
ss -tulpen
resolvectl status
ping
tracepath
curl
```

Do not memorize commands in isolation.

Map each command to a networking concept.

---

# Part 107 — curl as Network/Application Test

Example:

```bash
curl -I https://example.com
```

This may test:

```text
DNS
Routing
TCP
TLS
HTTP
```

If `curl` fails, inspect the error.

Examples:

```text
Could not resolve host
→ DNS

Connection refused
→ host reachable but service not listening/refusing

Timeout
→ routing/firewall/service path issue

TLS certificate error
→ TLS/trust/name problem
```

---

# Part 108 — Test-NetConnection

Windows:

```powershell
Test-NetConnection example.com -Port 443
```

Useful output may include:

```text
Resolved remote IP
Ping status
TCP test result
```

This is more useful than relying only on `ping` when testing a TCP service.

---

# Part 109 — Network Troubleshooting Layers

Use this order:

```text
1. Physical/link
2. Interface state
3. IP configuration
4. Local subnet
5. Default gateway
6. Routing
7. DNS
8. Transport port
9. Firewall/policy
10. Application
```

This is much faster than random testing.

---

# Part 110 — Define the Expected Flow First

Before troubleshooting, write:

```text
Source:
192.168.10.25

Destination:
10.20.30.50

Protocol:
TCP

Port:
443

Expected path:
PC → Gateway → Firewall → Server
```

Now each test has meaning.

Without this, troubleshooting becomes guesswork.

---

# Part 111 — Local Stack Test

Start with:

```text
127.0.0.1
```

If a local application listens on loopback:

```bash
curl http://127.0.0.1:8080
```

If this fails, the problem may be application/listener rather than external network.

---

# Part 112 — Interface Test

Check:

```text
Enabled?
Carrier/link?
Correct adapter?
```

Linux:

```bash
ip link
```

Windows:

```powershell
Get-NetAdapter
```

A disabled interface invalidates most higher-layer tests.

---

# Part 113 — Address Test

Check:

```text
Correct IP?
Correct prefix?
Duplicate IP?
Unexpected link-local address?
```

Linux:

```bash
ip addr
```

Windows:

```powershell
Get-NetIPConfiguration
```

A wrong subnet mask can cause confusing local/remote routing behavior.

---

# Part 114 — Gateway Test

Try to reach the local default gateway.

Example:

```bash
ping 192.168.1.1
```

If this fails:

Possible areas:

```text
Layer 2
VLAN
ARP
Host firewall
Gateway down
Wrong subnet
Wrong gateway
Wi-Fi/link
```

Do not jump to DNS troubleshooting yet.

---

# Part 115 — Remote IP Test

Test a known remote IP when appropriate.

If remote IP works but name fails:

```text
Likely DNS-related
```

If both fail:

```text
Routing/firewall/link/provider issue may exist
```

This separation is fundamental.

---

# Part 116 — DNS Test

Windows:

```powershell
Resolve-DnsName example.com
```

Linux:

```bash
getent hosts example.com
```

If DNS resolves but application fails, move higher:

```text
TCP
TLS
HTTP
Application
```

---

# Part 117 — Port Test

Windows:

```powershell
Test-NetConnection example.com -Port 443
```

Linux options:

```bash
curl -I https://example.com
```

or an authorized TCP test tool.

Do not test arbitrary third-party ports without authorization.

The purpose is to verify:

```text
Can I establish communication to the expected service?
```

---

# Part 118 — Application Test

A successful TCP connection does not mean the application is healthy.

Example:

```text
TCP/443 connects
HTTP response = 500
```

Network path works.

Application is failing.

This distinction saves significant troubleshooting time.

---

# Part 119 — Firewall Troubleshooting

A firewall issue can appear as:

```text
Timeout
Reset
Explicit reject
No return traffic
```

depending on implementation.

Check:

```text
Source rule
Destination rule
Host firewall
Network firewall
Cloud security controls
Return path
```

Never disable an entire firewall as the first troubleshooting step.

---

# Part 120 — Asymmetric Routing Awareness

Traffic can leave through one path and return through another.

Some stateful firewalls/load balancers require seeing both directions of a connection.

Example:

```text
Client → Firewall A → Server
Server → Firewall B → Client
```

This can cause stateful policy problems.

Detailed routing design comes later, but the concept is important.

---

# Part 121 — Cloud Networking Connection

Cloud networks use the same core ideas:

```text
VPC / VNet
Subnets
Route Tables
Security Groups / Firewalls
NAT
Load Balancers
DNS
Private Endpoints
```

Cloud may hide the physical switches/routers, but the logical networking model remains.

---

# Part 122 — Kubernetes Networking Connection

Kubernetes relies on:

```text
Pod IPs
Service IPs
DNS
Routing
Network Policies
Ingress/Gateway
Load Balancing
Ports
```

If IP addressing and routing are unclear, Kubernetes networking becomes difficult.

---

# Part 123 — Cybersecurity Connection

Network security depends on understanding normal traffic.

Examples:

```text
Firewall policy
Network segmentation
Packet capture
IDS/IPS
Port exposure
Lateral movement
Command-and-control traffic
DNS behavior
VPN
Zero Trust
```

You cannot reliably identify suspicious network behavior without first understanding normal communication.

---

# Part 124 — Packet Capture Awareness

Packet-capture tools such as Wireshark or tcpdump let you inspect traffic.

Conceptual packet:

```text
Ethernet
  ↓
IPv4
  ↓
TCP
  ↓
TLS
  ↓
Encrypted Application Data
```

A packet capture can answer:

```text
Did DNS query leave?
Did SYN leave?
Did SYN-ACK return?
Was TCP reset?
Did TLS start?
```

Capture only on networks and systems you are authorized to inspect.

---

# Part 125 — Final Networking Mental Model

When one application talks to another:

```text
Application decides destination name
       ↓
DNS resolves name to IP
       ↓
OS checks route
       ↓
If local:
resolve destination MAC

If remote:
resolve gateway MAC
       ↓
Build Ethernet frame
       ↓
Send IP packet
       ↓
Routers forward by destination IP
       ↓
Destination host receives packet
       ↓
Transport layer identifies port
       ↓
Operating system delivers data to socket
       ↓
Application handles request
```

And when troubleshooting:

```text
Interface
  ↓
IP
  ↓
Local subnet
  ↓
Gateway
  ↓
Route
  ↓
DNS
  ↓
TCP/UDP Port
  ↓
Firewall
  ↓
Application
```

If you understand these two flows, you have a strong foundation for Cisco networking, cloud networking, Kubernetes networking, and cybersecurity.

---

# 5. Hands-on Lab / Practical Exercises

## Lab 1 — Local Network Inventory

### Linux

```bash
ip link
ip addr
ip route
ip neigh
resolvectl status 2>/dev/null || cat /etc/resolv.conf
```

### Windows

```powershell
Get-NetAdapter
Get-NetIPConfiguration
Get-NetIPAddress
Get-NetRoute
Get-DnsClientServerAddress
```

Record:

```text
Interface
MAC address
IPv4
IPv6
Prefix
Gateway
DNS server
```

---

## Lab 2 — Identify Your Subnet

Take your IPv4 address and prefix.

Example:

```text
192.168.1.25/24
```

Determine:

```text
Network:   192.168.1.0
Broadcast: 192.168.1.255
Traditional usable range:
192.168.1.1–192.168.1.254
```

Repeat with a `/25` or `/26` example.

---

## Lab 3 — Subnetting Practice

Split:

```text
10.10.10.0/24
```

into four equal subnets.

Expected:

```text
10.10.10.0/26
10.10.10.64/26
10.10.10.128/26
10.10.10.192/26
```

For each, identify:

```text
Network
First host
Last host
Broadcast
```

---

## Lab 4 — Loopback Test

Linux/Windows:

```text
ping 127.0.0.1
```

Then:

```text
ping ::1
```

where IPv6 is available.

Explain what this tests and what it does **not** test.

---

## Lab 5 — Gateway Test

Find your default gateway.

Linux:

```bash
ip route
```

Windows:

```powershell
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```

Then ping the gateway where ICMP is permitted.

Explain possible causes if it fails.

---

## Lab 6 — DNS vs IP Reachability

Test:

```text
remote IP
remote hostname
```

Windows:

```powershell
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
```

Linux:

```bash
getent hosts example.com
curl -I https://example.com
```

Write which test covers which layer.

---

## Lab 7 — Trace Route

Windows:

```powershell
tracert example.com
```

Linux:

```bash
tracepath example.com
```

Record:

```text
Hop count
First hop
Any non-responsive hops
Destination
```

Explain why a `*` does not automatically prove failure.

---

## Lab 8 — Neighbor Table

Before communicating with a local host:

Linux:

```bash
ip neigh
```

Windows:

```powershell
arp -a
```

Ping the local host, then inspect again.

Explain the new IP-to-MAC mapping.

---

## Lab 9 — Inspect Listening Ports

Linux:

```bash
ss -lntup
```

Windows:

```powershell
Get-NetTCPConnection -State Listen
```

Record:

```text
Local address
Port
Protocol
Owning process
Expected?
```

---

## Lab 10 — Inspect Established TCP Connections

Linux:

```bash
ss -tnp
```

Windows:

```powershell
Get-NetTCPConnection -State Established
```

Open a browser connection and observe connections appearing.

---

## Lab 11 — Temporary Local Web Server

On an isolated lab host:

```bash
python3 -m http.server 8080
```

Inspect:

```bash
ss -ltnp
```

From the same host:

```bash
curl http://127.0.0.1:8080
```

Explain:

```text
Application
Port
Listening socket
TCP connection
HTTP response
```

---

## Lab 12 — Bind Address Experiment

Run a test service bound only to:

```text
127.0.0.1
```

then compare with:

```text
0.0.0.0
```

Observe listening addresses.

Explain remote reachability difference.

---

## Lab 13 — Two-Host Virtual Network

Create:

```text
VM1: 10.10.10.10/24
VM2: 10.10.10.20/24
```

Same isolated virtual switch/network.

Steps:

1. Verify interface.
2. Verify route.
3. Ping.
4. Inspect neighbor table.
5. Start web server on VM2.
6. `curl` from VM1.

---

## Lab 14 — Application Down vs Network Down

With VM2 web server running:

```bash
curl http://10.10.10.20:8080
```

Stop server.

Run again.

Compare:

```text
Ping
TCP connection
HTTP behavior
```

Explain:

```text
Network reachable
Application unavailable
```

---

## Lab 15 — Wrong Subnet Mask

In an isolated VM lab only, intentionally configure one host with the wrong prefix.

Example:

```text
VM1: 10.10.10.10/24
VM2: 10.10.20.20/8
```

Observe unexpected local/remote decisions.

Restore configuration afterward.

---

## Lab 16 — Static Route Concept

Design:

```text
Host A:
10.0.1.10/24

Router:
10.0.1.1
10.0.2.1

Host B:
10.0.2.10/24
```

Write the routes each host needs.

If using a lab router, implement only on authorized infrastructure.

---

## Lab 17 — Longest Prefix Match

Given:

```text
10.0.0.0/8 → Gateway A
10.10.0.0/16 → Gateway B
10.10.10.0/24 → Gateway C
```

Determine route for:

```text
10.10.10.50
10.10.20.50
10.20.1.1
```

Explain every result.

---

## Lab 18 — TCP Handshake Visualization

Create a text diagram:

```text
Client → SYN → Server
Client ← SYN-ACK ← Server
Client → ACK → Server
```

Then use a packet-capture tool on your own lab traffic if available and identify the handshake.

---

## Lab 19 — DNS Record Inspection

Windows:

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName example.com -Type AAAA
Resolve-DnsName example.com -Type MX
```

Linux with `dig` if installed:

```bash
dig example.com A
dig example.com AAAA
dig example.com MX
```

Explain each record type.

---

## Lab 20 — DNS Failure Simulation

In an isolated VM, temporarily configure an invalid DNS resolver while preserving IP/gateway.

Test:

```text
ping gateway
connect to known IP
resolve hostname
```

Restore DNS.

Explain why IP communication can work while name resolution fails.

---

## Lab 21 — DHCP Observation

Windows:

```powershell
ipconfig /all
```

Linux depending on environment:

```bash
ip addr
resolvectl status
```

Record:

```text
DHCP enabled?
Lease information if exposed
Gateway
DNS
Address
```

Explain the DORA process.

---

## Lab 22 — Firewall Concept Lab

On a disposable lab VM, run the temporary HTTP server.

Confirm access.

Then use the operating system's supported firewall tooling to block TCP/8080 only.

Retest.

Restore rule.

Document:

```text
Ping result
TCP result
Application result
```

Do not disable the whole firewall.

---

## Lab 23 — Latency and Packet Loss

Use:

```bash
ping -c 20 <authorized-target>
```

or Windows:

```powershell
ping -n 20 <authorized-target>
```

Record:

```text
Min latency
Average latency
Max latency
Packet loss
```

Explain the difference between latency and loss.

---

## Lab 24 — MTU Awareness

Use safe local/controlled path tests to compare small and larger ping payloads where supported.

Do not aggressively probe third-party systems.

Document:

```text
Payload size
Result
Path behavior
```

Explain Path MTU concept.

---

## Lab 25 — Packet Capture Fundamentals

On your own lab network:

1. Start a packet capture.
2. Generate one DNS lookup.
3. Open one HTTP/HTTPS connection.
4. Stop capture.
5. Identify:

```text
Ethernet
IP
TCP or UDP
DNS
TCP handshake
TLS if present
```

Do not decrypt or intercept traffic that you are not authorized to inspect.

---

## Lab 26 — Build a VLAN Design

Without configuring physical switches yet, design:

```text
VLAN 10 — Users
VLAN 20 — Servers
VLAN 30 — Management
```

Assign:

```text
10.10.10.0/24
10.10.20.0/24
10.10.30.0/24
```

Define allowed flows.

---

## Lab 27 — Small Office Address Plan

Design:

```text
Users:   192.168.10.0/24
Servers: 192.168.20.0/24
Guest:   192.168.30.0/24
Mgmt:    192.168.40.0/24
```

For every network identify:

```text
Gateway
DHCP/static strategy
DNS
Allowed destinations
```

---

## Lab 28 — Troubleshooting Runbook

Write a runbook for:

```text
"Client cannot access internal web server"
```

Mandatory sequence:

```text
Interface
IP/prefix
Gateway
Route
DNS
TCP port
Firewall
Application
```

For each stage provide one Windows and one Linux command.

---

## Lab 29 — Cloud Mapping

Map local networking concepts to cloud:

```text
LAN       → cloud subnet
Router    → route table/gateway
Firewall  → security group/network firewall
NAT       → NAT gateway
DNS       → managed DNS
LB        → cloud load balancer
```

Explain which concepts are identical and which are abstracted.

---

## Lab 30 — Network Baseline

Create a network baseline report containing:

```text
Interfaces
MAC addresses
IPv4/IPv6
Routes
Default gateway
DNS
Neighbor table
Listening ports
Established connections
Host firewall status
Latency to gateway
Latency to approved remote target
```

Save it for comparison during later troubleshooting.

---

# 6. Mini Project

## Mini Project — Small Office Network Design and Troubleshooting Pack

Design a small business network.

Required logical segments:

```text
Users
Servers
Guest Wi-Fi
Management
```

Example:

```text
                 Internet
                    │
                Firewall
                    │
                 Router/L3
              ┌─────┼─────┐
              │     │     │
             Users Servers Guest
              │     │     │
           Switch  Switch AP
```

## Deliverable 1 — Logical Diagram

Show:

```text
Internet
Firewall
Router
Switch
Access Point
Client VLAN
Server VLAN
Guest VLAN
Management VLAN
DNS
DHCP
Internal Web Server
```

## Deliverable 2 — Addressing Plan

Example structure:

| Segment | Network | Gateway | Allocation |
|---|---|---|---|
| Users | 10.10.10.0/24 | 10.10.10.1 | DHCP |
| Servers | 10.10.20.0/24 | 10.10.20.1 | Static/Reservation |
| Guest | 10.10.30.0/24 | 10.10.30.1 | DHCP |
| Management | 10.10.40.0/24 | 10.10.40.1 | Controlled |

## Deliverable 3 — Service Table

Record:

```text
Service
Protocol
Port
Source
Destination
Reason
```

Example:

```text
HTTPS
TCP
443
Users
Internal Web Server
Business application
```

## Deliverable 4 — Security Policy

Example:

```text
Users → Web Server TCP/443      ALLOW
Users → Database TCP/5432       DENY
Guest → Internal Networks       DENY
Management → Network Devices    ALLOW
Server → Internet               LIMITED
```

## Deliverable 5 — DNS and DHCP

Define:

```text
DHCP scopes
DNS resolver
Internal DNS name
Gateway handed to clients
Lease strategy
```

## Deliverable 6 — Troubleshooting Runbook

For:

```text
"User cannot open internal web application"
```

Use:

```text
1. Physical/interface
2. Address
3. Gateway
4. Route
5. DNS
6. TCP/443
7. Firewall
8. Server listening
9. Application
```

## Deliverable 7 — Packet Flow Explanation

Explain one HTTPS request:

```text
Client
  ↓ ARP gateway if remote subnet
Switch
  ↓
Router/Firewall
  ↓ routing/security
Server network
  ↓
Server TCP/443
  ↓
TLS
  ↓
HTTP
```

## Deliverable 8 — Optional Packet Tracer Implementation

If Cisco Packet Tracer is available:

- Create VLANs.
- Configure basic addressing.
- Configure default gateways.
- Add DHCP/DNS assumptions.
- Test connectivity.
- Document failures.

Do not expose the lab to untrusted external networks unnecessarily.

---

# 7. Recommended Resources

This Markdown is designed to be sufficient for the fundamentals phase.

For deeper practice, use current official or high-quality vendor training:

- Cisco Networking Academy / Skills for All — Networking Basics.
- Cisco Packet Tracer training.
- Microsoft Learn networking fundamentals.
- Linux distribution networking documentation.
- Windows networking documentation.
- Wireshark official documentation for packet analysis.

Use external references mainly for simulator-specific steps, packet-capture tooling, or vendor-specific configuration.

---

# 8. Certification Relevance

## CCNA

Direct foundation for:

```text
Ethernet
MAC addresses
Switching
IPv4/IPv6
Subnetting
Routing
ARP
TCP/UDP
DNS
DHCP
VLANs
NAT
ACL/firewall concepts
Troubleshooting
```

## AWS / Azure / Google Cloud

Cloud networking is built from the same ideas:

```text
VPC / VNet
Subnets
Routes
NAT
Firewalls
Load Balancers
DNS
Private/Public addressing
```

## CKA / Kubernetes

Kubernetes networking relies on:

```text
IP routing
DNS
Ports
Services
Load balancing
Network policy
Ingress
```

## Cybersecurity

Essential for:

```text
Network segmentation
Firewall analysis
Packet capture
IDS/IPS
VPNs
Traffic analysis
Incident response
Penetration testing concepts
Zero Trust
Cloud security
```

---

# 9. Common Mistakes & Best Practices

## Common Mistakes

- Confusing MAC and IP addresses.
- Assuming every destination uses the default gateway.
- Forgetting directly connected routes.
- Memorizing subnet masks without understanding host/network bits.
- Treating `ping` as proof that an application works.
- Treating DNS failure as full Internet failure.
- Treating NAT as a firewall.
- Assuming a port number guarantees which application is running.
- Ignoring host firewalls.
- Ignoring return routing.
- Assuming `traceroute` `*` means the path is broken.
- Exposing services on `0.0.0.0` without understanding firewall policy.
- Putting all hosts in one large broadcast domain.
- Using public IPs where private addressing is appropriate.
- Testing arbitrary third-party ports without authorization.
- Disabling firewalls instead of creating narrow test rules.
- Troubleshooting applications before checking IP/routing.
- Ignoring IPv6 because IPv4 works.
- Blocking all ICMP/ICMPv6 blindly.
- Ignoring MTU when small traffic works but larger traffic fails.

## Best Practices

- Define the expected source, destination, protocol, port, and path first.
- Troubleshoot from lower layers upward.
- Separate name resolution from IP reachability.
- Separate network reachability from application availability.
- Use diagrams.
- Document subnet plans.
- Use private addressing internally where appropriate.
- Segment networks by trust and function.
- Use default-deny firewall policies where practical.
- Expose only required services.
- Verify both forward and return paths.
- Inspect routes on the host.
- Inspect neighbor/ARP state for local delivery issues.
- Use packet captures only on authorized systems.
- Build baselines for routes, DNS, ports, and interfaces.
- Remember that cloud and Kubernetes networking still follow IP, routing, DNS, and port fundamentals.

---

# 10. Self-Assessment Questions (with short answers)

1. **Why use network layers?**  
   To separate responsibilities and make protocols easier to design, replace, and troubleshoot.

2. **What is encapsulation?**  
   Adding layer-specific headers/trailers as data moves down the network stack.

3. **What is the OSI model used for?**  
   A conceptual seven-layer model useful for learning and troubleshooting.

4. **What layer does IP belong to conceptually?**  
   Network/Internet layer.

5. **What layer does TCP belong to?**  
   Transport layer.

6. **What is Ethernet?**  
   A common Layer-2 local-network technology using frames and MAC addresses.

7. **What is a MAC address?**  
   Link-layer identifier used for local frame delivery.

8. **Switch vs router?**  
   Switch forwards frames by MAC within Layer 2; router forwards IP packets between networks.

9. **What does a switch learn?**  
   Source MAC addresses and the ports on which they were observed.

10. **What is a broadcast domain?**  
    Set of devices receiving the same Layer-2 broadcast.

11. **What is a VLAN?**  
    Logical Layer-2 broadcast-domain segmentation.

12. **IPv4 size?**  
    32 bits.

13. **What does `/24` mean?**  
    First 24 IP bits identify the network portion.

14. **Mask for `/24`?**  
    255.255.255.0.

15. **Network for 192.168.10.25/24?**  
    192.168.10.0.

16. **Traditional broadcast for 192.168.10.0/24?**  
    192.168.10.255.

17. **Traditional usable hosts in /24?**  
    254.

18. **Private IPv4 ranges?**  
    10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.

19. **What is a default gateway?**  
    Router used when no more-specific local/remote route matches.

20. **What is longest-prefix match?**  
    The most specific matching route is selected.

21. **What is ARP?**  
    IPv4 local address-to-MAC resolution protocol.

22. **What replaces ARP in IPv6?**  
    Neighbor Discovery.

23. **What is ICMP used for?**  
    Network control and diagnostics such as echo and unreachable/time-exceeded messages.

24. **What does TTL do?**  
    Prevents packets from looping indefinitely by decreasing at each router.

25. **What is TCP?**  
    Connection-oriented reliable ordered byte-stream transport.

26. **TCP handshake?**  
    SYN → SYN-ACK → ACK.

27. **Why TCP sequence numbers?**  
    Track byte ordering and missing data.

28. **What is TCP retransmission?**  
    Resending data believed lost.

29. **Flow control?**  
    Prevent sender from overwhelming receiver.

30. **UDP?**  
    Connectionless datagram transport with minimal built-in delivery guarantees.

31. **TCP vs UDP?**  
    TCP provides reliable ordered stream semantics; UDP provides lightweight datagrams.

32. **What is a port?**  
    Transport-layer application endpoint number.

33. **What is a socket?**  
    OS abstraction for network communication endpoint.

34. **Why client ephemeral ports?**  
    Distinguish multiple client-side connections.

35. **What is DNS?**  
    Distributed naming system mapping names to records.

36. **A record?**  
    Name to IPv4 address.

37. **AAAA record?**  
    Name to IPv6 address.

38. **CNAME?**  
    Alias to another DNS name.

39. **MX?**  
    Mail exchanger record.

40. **What does DHCP provide?**  
    IP address, prefix/mask, gateway, DNS, lease information.

41. **DORA?**  
    Discover, Offer, Request, Acknowledge.

42. **What is NAT?**  
    Address translation at a network boundary.

43. **PAT?**  
    Many internal flows share an address using translated transport ports.

44. **Why is NAT not a firewall?**  
    NAT translates addresses; firewall enforces allow/deny policy.

45. **Stateful firewall?**  
    Firewall that tracks connection state.

46. **What does ping test?**  
    ICMP reachability where allowed, not application availability.

47. **Why can ping work while HTTPS fails?**  
    ICMP may pass while TCP/443, TLS, or the web application fails.

48. **What is throughput?**  
    Actual achieved data-transfer rate.

49. **What is latency?**  
    Time required for traffic to travel/process.

50. **What is jitter?**  
    Variation in packet delay.

51. **What is packet loss?**  
    Packets failing to reach destination.

52. **What is MTU?**  
    Maximum transmission size supported by a link/path context.

53. **What is unicast?**  
    One sender to one destination.

54. **Broadcast?**  
    One sender to all devices in a local broadcast domain.

55. **Multicast?**  
    One sender to a subscribed group.

56. **Anycast?**  
    Same IP announced from multiple locations, with routing selecting one.

57. **Why inspect host routes?**  
    Hosts make routing decisions before packets leave the machine.

58. **Why inspect neighbor table?**  
    Local IPv4/IPv6 delivery depends on neighbor resolution.

59. **Why use `Test-NetConnection` instead of only ping?**  
    It can directly test a TCP service port.

60. **What is the best network troubleshooting sequence?**  
    Interface → IP → local subnet → gateway → route → DNS → transport port → firewall → application.
