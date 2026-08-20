# Phase 21 — Network Security

Phase 21 turns the Phase 20 cybersecurity foundation into a focused **network-security engineering and testing sequence**.

The correct order is:

```text
86 Firewall Technologies
        ↓
87 Network Security Assessment
        ↓
88 Network Penetration Testing
```

You first learn **how network policy is enforced**, then **how to assess whether that policy is correct**, and finally **how to validate real attack paths safely inside an authorized scope**.

---

# Phase Objectives

By the end of Phase 21, you should be able to:

- design a zone-based firewall architecture;
- understand stateful packet/session processing;
- distinguish routing, NAT, firewall policy, and application behavior;
- build and review least-privilege firewall rulebases;
- explain NGFW, IDS/IPS, TLS inspection, VPN, HA, and logging;
- assess routers, switches, firewalls, VPNs, wireless, DNS, cloud networking, and Kubernetes network controls;
- validate segmentation and default-deny behavior safely;
- use packet, flow, configuration, and scanner evidence correctly;
- identify false positives and assessment limitations;
- perform controlled network penetration-testing exercises in isolated labs;
- map service, credential, privilege, and segmentation weaknesses into attack paths;
- correlate test activity with firewall, endpoint, identity, and SIEM telemetry;
- clean up, remediate, and retest.

---

# Courses

| # | Course | Main Focus |
|---|---|---|
| **86** | **Firewall Technologies** | Stateful/stateless filtering, zones, rulebases, NAT, routing interaction, NGFW, IPS, TLS inspection, VPN, HA, logging, cloud firewalls, troubleshooting |
| **87** | **Network Security Assessment** | Authorized network assessment, asset/service discovery, segmentation validation, device/firewall/VPN/wireless/cloud review, evidence, findings, retest |
| **88** | **Network Penetration Testing** | Controlled network attack-path validation, service weaknesses, credential testing in labs, privilege escalation concepts, pivoting/lateral movement concepts, detection validation |

---

# Prerequisites

You should already be comfortable with:

```text
83 Network Security Fundamentals
84 Security Assessment Fundamentals
85 Ethical Hacking Fundamentals
TCP/IP
IPv4 / IPv6
Routing
Switching
VLANs
DNS / DHCP
Linux
Windows
Active Directory fundamentals
Cloud networking
Wireshark / tcpdump
Basic Bash / PowerShell / Python
```

---

# Mandatory Lab Safety Rule

Use only:

```text
localhost
your own VMs
your own containers
your own cloud lab
intentionally vulnerable training systems
systems explicitly covered by written authorization
```

Do not test:

```text
random Internet systems
third-party Wi-Fi
unknown public IPs
out-of-scope corporate systems
real employee accounts without authorization
systems found through Internet search engines
```

For Course 88, use snapshots and isolated networks before exploit or privilege-escalation exercises.

---

# Recommended Phase 21 Lab Topology

```text
                           Internet Simulation
                                  │
                             Edge Firewall
                   ┌──────────────┼──────────────┐
                   │              │              │
                  DMZ            USER           MGMT
                   │              │              │
              Web / SSH         Client        Admin Host
                   │
                  APP
                   │
                  DATA

Security Workstation
   ├─ Nmap
   ├─ Wireshark / tcpdump
   ├─ curl / OpenSSL
   ├─ Bash / PowerShell / Python
   ├─ optional Metasploit lab
   └─ evidence repository
```

Optional components:

```text
Windows Server / AD
VPN gateway
Wi-Fi lab
Cloud VPC/VNet
Kubernetes
SIEM / log collector
IDS / IPS / NDR
```

---

# Course 86 — Firewall Technologies

## Core Mental Model

A firewall is not simply:

```text
open port / closed port
```

A real packet/session decision can involve:

```text
Ingress Interface
      ↓
Security Zone
      ↓
Routing / VRF
      ↓
NAT
      ↓
Policy
      ↓
Session / State
      ↓
Application / Threat Inspection
      ↓
Egress Interface
      ↓
Logging
```

The exact packet-processing order is platform-specific, so production troubleshooting must use the relevant vendor packet-flow documentation.

## Firewall Rule Model

Each rule should answer:

```text
WHO is the source?
WHAT is the destination?
WHICH service/application is required?
WHY is the flow required?
WHO owns the rule?
HOW LONG is it needed?
WHAT gets logged?
WHEN is it reviewed?
```

Example:

| Rule | Source | Destination | Service | Action | Owner |
|---|---|---|---|---|---|
| 10 | User Zone | App VIP | HTTPS | Allow | App Team |
| 20 | App Zone | DB | PostgreSQL | Allow | Data Team |
| 30 | Mgmt Zone | Firewalls | SSH/HTTPS | Allow | NetOps |
| 999 | Any | Any | Any | Deny | Security |

## NAT vs Firewall vs Routing

```text
Firewall Policy
  → Should the flow be permitted?

NAT
  → Which source/destination address is translated?

Routing
  → Which path/interface carries the packet?
```

Confusing these three is one of the most common troubleshooting mistakes.

## Stateful Firewall

```text
Initial packet
   ↓
policy permits
   ↓
session created
   ↓
return traffic
   ↓
matches session state
   ↓
allowed
```

This is why asymmetric routing can break traffic even when rules appear correct.

## NGFW Capabilities

Understand these as separate controls:

```text
stateful filtering
application identification
user/group-aware policy
URL filtering
IPS/threat prevention
malware inspection
DNS controls
TLS inspection
VPN
logging
```

No single NGFW feature replaces endpoint security, application security, or identity controls.

## Firewall Operations

You should know how to reason about:

```text
HA
failover
state synchronization
config synchronization
rule hit counters
unused rules
shadowed rules
session tables
packet captures
commit/publish
rollback
configuration backup
change control
capacity
DDoS interaction
log forwarding
SIEM integration
```

---

# Course 87 — Network Security Assessment

The primary question is:

> **Does the network behave the way the security architecture says it should?**

Assessment flow:

```text
Authorization
    ↓
Architecture review
    ↓
Asset inventory
    ↓
Passive evidence
    ↓
Bounded discovery
    ↓
Configuration review
    ↓
Segmentation validation
    ↓
Exposure analysis
    ↓
Telemetry validation
    ↓
Findings
    ↓
Remediation
    ↓
Retest
```

## Evidence Hierarchy

Prefer more authoritative evidence where possible:

```text
Configuration / cloud API
        ↓
Local host/device state
        ↓
Firewall / flow logs
        ↓
Protocol response
        ↓
Scanner fingerprint
        ↓
Assumption
```

## Network Assessment Domains

You should assess:

```text
routers
switches
firewalls
NAT
VLANs
routing
DNS
DHCP
NTP
VPN
Wi-Fi
802.1X / NAC
AAA
SSH / SNMP
IDS / IPS / NDR
flow logs
packet capture
cloud VPC/VNet
security groups / NSGs
private endpoints
Kubernetes NetworkPolicy
service mesh
```

## Segmentation Testing

Expected matrix:

```text
Users → App HTTPS          ALLOW
Users → Database           DENY
App   → Database           ALLOW
Guest → Corporate          DENY
Mgmt  → Network Devices    ALLOW
```

Validate **both allowed and denied flows**.

A segmentation assessment that checks only successful connections is incomplete.

## Finding Structure

```text
Title
Affected assets
Expected policy
Observed behavior
Evidence
Security impact
Business impact
Exposure
Priority
Remediation
Compensating control
Owner
Retest method
```

---

# Course 88 — Network Penetration Testing

Network penetration testing asks a deeper question:

> **Can exposed services, credentials, privilege weaknesses, and network paths combine into meaningful unauthorized access?**

## Attack Path Model

```text
External / Initial Reachability
          ↓
Weak Service / Misconfiguration
          ↓
Initial Foothold
          ↓
Credential / Privilege Weakness
          ↓
Allowed Network Path
          ↓
Internal Target
          ↓
Business Impact
```

## Safe Validation Rule

```text
Is the weakness already proven?
    ├─ Yes → STOP.
    └─ No
         ↓
Is one additional authorized step necessary?
    ├─ No → report limitation.
    └─ Yes
         ↓
perform minimum proof
         ↓
STOP
```

The goal is not maximum access.

The goal is **sufficient evidence with minimum risk**.

## Course 88 Boundaries

Allowed in isolated labs or explicit scope:

```text
service enumeration
intentional vulnerable-service validation
synthetic credential testing
lab privilege escalation
segmentation testing
attack-path mapping
detection validation
controlled Metasploit introduction
```

Not a default objective:

```text
persistence
stealth
evasion
real-data exfiltration
destructive commands
ransomware behavior
out-of-scope pivoting
```

## Detection Validation

Every meaningful lab should ask:

```text
Did the firewall see it?
Did the endpoint see it?
Did identity logs see it?
Did the SIEM alert?
Was the alert actionable?
What telemetry was missing?
```

This creates the bridge from penetration testing to later purple-team and SOC work.

---

# Recommended Tools

## Firewall and Network Operations

```text
ip
ss
nft
iptables
tcpdump
Wireshark
dig
nslookup
traceroute / tracepath
curl
OpenSSL
```

## Security Assessment

```text
Nmap
Wireshark
vendor configuration exports
cloud network APIs
flow logs
CIS Benchmarks
Bash
PowerShell
Python
```

## Penetration-Testing Lab

```text
Nmap
curl
OpenSSL
Wireshark
basic protocol clients
Metasploit — isolated lab only
local privilege-enumeration commands
Bash / PowerShell / Python
```

Tool count is not the goal.

Use this sequence:

```text
Understand
   ↓
Form a testable question
   ↓
Choose the least intrusive method
   ↓
Gather evidence
   ↓
Explain impact
   ↓
Fix
   ↓
Retest
```

---

# Recommended Folder Structure

```text
Phase_21_Lab/
├── 86_Firewall_Technologies/
│   ├── architecture/
│   ├── firewall_rules/
│   ├── nat/
│   ├── vpn/
│   ├── logs/
│   └── troubleshooting/
├── 87_Network_Security_Assessment/
│   ├── scope/
│   ├── inventory/
│   ├── configs/
│   ├── scans/
│   ├── pcaps/
│   ├── findings/
│   └── retest/
├── 88_Network_Penetration_Testing/
│   ├── roe/
│   ├── recon/
│   ├── enumeration/
│   ├── evidence/
│   ├── attack_paths/
│   ├── detection_validation/
│   ├── cleanup/
│   └── retest/
└── README.md
```

---

# Combined Phase 21 Capstone

Build a multi-zone isolated enterprise network:

```text
Internet Simulation
        ↓
Edge Firewall
   ┌────┼─────┐
   │    │     │
  DMZ  USER  MGMT
   │
  APP
   │
  DATA

Optional:
VPN
Cloud
AD
Kubernetes
SIEM
IDS/IPS
```

Required deliverables:

1. `Network_Architecture.md`
2. `Zone_Matrix.csv`
3. `Firewall_Rules.csv`
4. `NAT_Plan.csv`
5. `VPN_Architecture.md`
6. `Firewall_HA_and_Management.md`
7. `Rules_of_Engagement.md`
8. `Network_Assessment_Plan.md`
9. `Asset_and_Service_Inventory.csv`
10. `Segmentation_Test_Matrix.csv`
11. `Firewall_Assessment.md`
12. `Cloud_Network_Assessment.md`
13. `Pentest_Attack_Path.md`
14. `Detection_Validation.md`
15. `Findings_Report.md`
16. `Cleanup_Checklist.md`
17. `Remediation_Plan.md`
18. `Retest_Report.md`
19. `Executive_Summary.md`

---

# What to Know Before Leaving Phase 21

## Firewall Technologies

You should explain:

```text
stateless filtering
stateful filtering
state table
zones
rule order
shadowed rules
default deny
NAT
SNAT
DNAT
PAT
HA
asymmetric routing
NGFW
IPS
TLS inspection
VPN
logging
policy recertification
cloud firewalls
```

## Network Security Assessment

You should explain:

```text
scope
RoE
passive discovery
Nmap
service validation
VLAN assessment
routing review
firewall review
VPN assessment
wireless assessment
cloud network review
packet capture
flow logs
false positives
risk prioritization
retest
```

## Network Penetration Testing

You should explain:

```text
attack surface
enumeration
service misconfiguration
safe exploit validation
credential testing boundaries
privilege escalation concepts
attack paths
segmentation bypass concepts
pivoting concepts
lateral movement concepts
detection validation
cleanup
reporting
retest
```

---

# What Phase 21 Does Not Cover Deeply

These are intentionally deferred:

```text
advanced Metasploit operations
web application penetration testing
bug bounty methodology
mobile application penetration testing
advanced Active Directory attack chains
malware analysis
reverse engineering
exploit development
red-team infrastructure
evasion / stealth
persistence tradecraft
```

---

# Transition to Phase 22

Next:

# Phase 22 — Penetration Testing

```text
89. Metasploit Essentials
90. Ethical Hacking and Security Assessment
91. Bug Hunting
92. Web Application Penetration Testing
93. Mobile Application Penetration Testing
94. Active Directory Penetration Testing
```

Dependency:

```text
85 Ethical Hacking Fundamentals
       ↓
87 Network Security Assessment
       ↓
88 Network Penetration Testing
       ↓
89 Metasploit Essentials
       ↓
specialized penetration-testing courses
```

---

# Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 86 — Firewall Technologies | 138 | 70 | 138 | 11,836 |
| 87 — Network Security Assessment | 115 | 70 | 115 | 10,950 |
| 88 — Network Penetration Testing | 123 | 70 | 123 | 11,096 |
| **Total** | **376** | **210** | **376** | **33,882** |

---

# Completion Criteria

Phase 21 is complete when you can:

- design a firewall rulebase from business flows;
- explain session state, NAT, routing, and asymmetric-path failures;
- harden firewall management and HA;
- analyze firewall logs and hit counters;
- perform a safe network-security assessment;
- validate expected segmentation;
- assess cloud and Kubernetes network controls;
- distinguish a potential weakness from a validated finding;
- map multiple weaknesses into an attack path;
- demonstrate one controlled network attack path in an isolated lab;
- correlate the test with defensive telemetry;
- clean up;
- remediate;
- retest.

---

# Final Mental Model

```text
              NETWORK SECURITY
                     │
      ┌──────────────┼──────────────┐
      │              │              │
   ENFORCE          ASSESS        VALIDATE
      │              │              │
  Firewalls       Inventory       Recon
  Zones           Exposure        Enumerate
  NAT             Config          Minimal exploit
  VPN             Segmentation    Attack paths
  Policy          Telemetry       Detection
      │              │              │
      └──────────────┼──────────────┘
                     ↓
                REMEDIATE
                     ↓
                  RETEST
```

**Phase 21 is complete when you can explain what the network should allow, prove what it actually allows, validate meaningful weaknesses safely, and help the organization close those paths.**
