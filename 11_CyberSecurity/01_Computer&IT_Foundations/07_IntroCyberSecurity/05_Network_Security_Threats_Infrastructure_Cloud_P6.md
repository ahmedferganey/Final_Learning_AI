# Network Security — Threats, Detection, Infrastructure & Cloud Security

> Companion module focused on threat actors, attacks, detection/prevention technologies, firewalls, data centers, service agreements, cloud computing, managed providers, and secure network/cloud architecture.

---

# Table of Contents

1. Network Security Threat Landscape
2. Threat Sources — Insider vs Outsider
3. Threat Actor Categories
4. Threat, Vulnerability, Exploit, and Risk
5. Spoofing Attacks
6. DoS and DDoS
7. On-Path / MITM Attacks
8. Side-Channel Attacks
9. Phishing vs Spear Phishing
10. Social Engineering Variants
11. Malware Overview
12. Virus vs Worm vs Trojan
13. Ransomware
14. Advanced Persistent Threat — APT
15. Other Important Threats
16. Threat Identification and Prevention Strategy
17. System Hardening
18. IDS — Intrusion Detection System
19. IPS — Intrusion Prevention System
20. IDS vs IPS
21. HIDS/HIPS vs NIDS/NIPS
22. SIEM
23. SOAR
24. Antivirus and Antimalware
25. EDR, XDR, and NDR
26. Security Scanners
27. Vulnerability Scanners vs Network Scanners
28. Firewalls
29. Firewall Types
30. Traditional Firewall vs NGFW
31. FWaaS — Firewall as a Service
32. WAF vs Network Firewall
33. DLP
34. Threat Prevention Architecture
35. Network Security Infrastructure
36. Data Center Types
37. Data Center Components
38. Data Center Physical & Environmental Security
39. Data Center Redundancy
40. JOA, MOU, MOA, and SLA
41. SLA Availability and the Nines
42. Cloud Computing Fundamentals
43. Essential Cloud Characteristics
44. IaaS, PaaS, SaaS
45. Cloud Deployment Models
46. Regions and Availability Zones
47. Cloud Shared Responsibility
48. MSP and MSSP
49. Network and Cloud Security Architecture
50. Segmentation
51. VLANs
52. DMZ
53. Microsegmentation
54. Zero Trust
55. NAC
56. VPN
57. ZTNA
58. SASE and SSE
59. Defense in Depth
60. Security Monitoring Architecture
61. Incident Detection Flow
62. Example Enterprise Security Architecture
63. Threat-to-Control Mapping
64. Common Misconceptions
65. Interview and Exam Questions
66. Final Review Sheet
67. Authoritative References

---

# 1. Network Security Threat Landscape

A **threat** is a potential cause of harm to systems, networks, applications, identities, or data.

Network-security threats may target:

```text
Confidentiality
Integrity
Availability
Authentication
Authorization
Accountability
Privacy
```

A useful model is:

```text
Threat Actor
    ↓
Technique
    ↓
Vulnerability / Weakness
    ↓
Attack
    ↓
Impact
```

Example:

```text
Threat Actor
    ↓
Phishing Email
    ↓
Weak User Awareness
    ↓
Credential Theft
    ↓
VPN Account Compromise
    ↓
Internal Access
```

---

# 2. Threat Sources — Insider vs Outsider

## Insider Threat

An insider has legitimate or previously legitimate organizational access.

Examples:

```text
Employee
Administrator
Contractor
Business Partner
Former Employee
Third-Party Support Engineer
```

Insider threats can be:

```text
Malicious
Negligent
Accidental
Compromised
```

### Malicious Insider

```text
Employee
   ↓
Copies Confidential Data
   ↓
Sells / Leaks Data
```

### Negligent Insider

```text
Employee
   ↓
Uploads sensitive file to public storage
```

### Compromised Insider

```text
External Attacker
       ↓
Steals Employee Credentials
       ↓
Logs in as Valid User
       ↓
Appears to be Insider
```

## Outsider Threat

An outsider starts without legitimate access.

Examples:

```text
Cybercriminal
Hacktivist
Competitor
State-Sponsored Actor
Botnet Operator
Fraud Group
```

Typical methods:

```text
Phishing
Exploitation
Credential Stuffing
DDoS
Malware
Reconnaissance
Supply Chain Compromise
```

---

# 3. Threat Actor Categories

| Threat Actor | Typical Motivation |
|---|---|
| Cybercriminal | Financial gain |
| State-sponsored | Espionage, strategic advantage |
| Hacktivist | Ideological/political goals |
| Insider | Revenge, fraud, error, negligence |
| Competitor | Economic advantage |
| Script kiddie | Curiosity, reputation, disruption |
| Organized crime | Large-scale fraud/extortion |

Motivation influences:

```text
Target Selection
Persistence
Resources
Sophistication
Risk Tolerance
```

---

# 4. Threat, Vulnerability, Exploit, and Risk

```text
Threat
→ Potential source of harm

Vulnerability
→ Weakness

Exploit
→ Method/code used to take advantage of weakness

Risk
→ Potential loss based on likelihood and impact
```

Example:

```text
Threat:
Internet attacker

Vulnerability:
Unpatched VPN appliance

Exploit:
Technique/code targeting the vulnerability

Impact:
Unauthorized remote access
```

---

# 5. Spoofing Attacks

**Spoofing** means falsifying an identity or address so traffic appears to come from another entity.

Examples:

```text
IP Spoofing
MAC Spoofing
ARP Spoofing
DNS Spoofing
Email Spoofing
```

Diagram:

```text
Attacker
   |
   | Source = Victim
   v
Server
   |
   | Response
   v
Victim
```

Potential defenses:

```text
Ingress Filtering
Egress Filtering
Stateful Firewalls
Authentication
Cryptographic Protocols
Anti-Spoofing ACLs
uRPF where appropriate
```

---

# 6. DoS and DDoS

## DoS

**Denial of Service** attempts to make a service unavailable.

```text
Attacker
    ↓
Large / Malicious Traffic
    ↓
Target
    ↓
Unavailable
```

## DDoS

**Distributed Denial of Service** uses many sources.

```text
Bot 1 ─┐
Bot 2 ─┤
Bot 3 ─┼────> Target
Bot 4 ─┤
Bot 5 ─┘
```

Targets may include:

```text
Bandwidth
CPU
Memory
Connection Tables
Application Threads
Database Capacity
API Rate Limits
```

Common categories:

```text
Volumetric
Protocol / State Exhaustion
Application-Layer
```

Defenses:

```text
DDoS Scrubbing
CDN
Anycast
Rate Limiting
WAF
SYN Cookies
Autoscaling
Load Balancing
Upstream Filtering
Cloud DDoS Protection
```

---

# 7. On-Path / MITM Attacks

An **on-path attack** is the modern term often used for what is historically called MITM.

```text
Normal:
User ─────────────> Server

On-Path:
User ──> Attacker ──> Server
```

The attacker may:

```text
Observe
Relay
Modify
Inject
Redirect
```

Examples:

```text
Rogue Wi-Fi
ARP Poisoning
DNS Manipulation
Proxy Interception
TLS Downgrade Attempts
```

Defenses:

```text
TLS
Certificate Validation
VPN
Mutual TLS
HSTS
Secure Wi-Fi
Strong Authentication
Segmentation
```

---

# 8. Side-Channel Attacks

A **side-channel attack** extracts information from physical or implementation leakage rather than directly breaking a cryptographic algorithm.

Possible channels:

```text
Execution Time
Power Consumption
Electromagnetic Radiation
CPU Cache Behavior
Acoustic Signals
Memory Access Patterns
```

Diagram:

```text
Cryptographic Operation
       │
       ├── Correct Output
       │
       └── Side Effects
              ↓
         Timing / Power /
         Cache / EM Signals
              ↓
           Attacker
```

Examples:

```text
Timing Analysis
Power Analysis
Cache Timing
Electromagnetic Analysis
```

## Side-Channel vs On-Path

| Side Channel | On-Path |
|---|---|
| Observes implementation leakage | Intercepts communication path |
| Often hardware/physical related | Network communication related |
| Often passive observation | Can observe and modify |
| Example: power analysis | Example: MITM |

---

# 9. Phishing vs Spear Phishing

## Phishing

Broad social-engineering campaign.

```text
Attacker
   ↓
Thousands of Messages
   ↓
Many Users
   ↓
Some Victims
```

Common goals:

```text
Credential Theft
Malware Delivery
Payment Fraud
Account Takeover
```

## Spear Phishing

Targeted phishing against a specific person or organization.

```text
Research Victim
      ↓
Personalized Message
      ↓
Specific Target
```

May reference:

```text
Job Role
Manager
Current Project
Supplier
Invoice
Internal Terminology
```

| Phishing | Spear Phishing |
|---|---|
| Broad | Targeted |
| Generic | Personalized |
| High volume | Lower volume |
| Less research | More research |

---

# 10. Social Engineering Variants

```text
Whaling
Smishing
Vishing
Business Email Compromise
Pretexting
Baiting
Quid Pro Quo
Tailgating
```

## Whaling

Targets executives.

## Smishing

Phishing through SMS/messages.

## Vishing

Voice-based phishing.

## BEC

```text
Attacker Impersonates CEO
          ↓
Requests Urgent Transfer
          ↓
Finance Employee
```

---

# 11. Malware Overview

**Malware** is malicious software designed to harm, spy, disrupt, or gain unauthorized access.

Examples:

```text
Virus
Worm
Trojan
Ransomware
Spyware
Rootkit
Keylogger
Bot
Backdoor
Logic Bomb
Wiper
Cryptominer
```

---

# 12. Virus vs Worm vs Trojan

## Virus

Typically attaches to another file/program and replicates when the infected host is executed or shared.

```text
Clean Program
     +
Virus Code
     ↓
Infected Program
```

## Worm

Self-propagating malware.

```text
Host A
 ↓
Worm
 ↓ ↓ ↓
B C D
```

Can spread rapidly between vulnerable systems.

## Trojan

Malware disguised as legitimate software/content.

```text
Looks Legitimate
      ↓
User Executes
      ↓
Malicious Function
```

| Virus | Worm | Trojan |
|---|---|---|
| Infects files/programs | Self-propagates | Disguises itself |
| Often requires user/system action | Often network-based spread | User installs/runs it |
| Replicates | Replicates | May not replicate |

---

# 13. Ransomware

Ransomware is malware used for extortion.

Typical modern sequence:

```text
Initial Access
    ↓
Execution
    ↓
Privilege Escalation
    ↓
Lateral Movement
    ↓
Data Theft
    ↓
Encryption
    ↓
Ransom Demand
```

Common access paths:

```text
Phishing
Stolen Credentials
Unpatched Internet Services
RDP/VPN Exposure
Malware Loaders
Supply Chain
```

Defenses:

```text
Offline / Immutable Backups
EDR
MFA
Patch Management
Segmentation
Least Privilege
Email Security
Application Control
Logging
Incident Response Plan
```

---

# 14. Advanced Persistent Threat — APT

An **APT** is a sustained, targeted intrusion campaign characterized by persistence, resources, and strategic objectives.

Characteristics:

```text
Targeted
Persistent
Well-Resourced
Stealthy
Multi-Stage
Long-Term
```

Lifecycle:

```text
Target Selection
      ↓
Reconnaissance
      ↓
Initial Access
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Credential Access
      ↓
Lateral Movement
      ↓
Collection
      ↓
Exfiltration / Impact
      ↓
Maintain Access
```

Defenses:

```text
Threat Intelligence
EDR/XDR
SIEM
NDR
Least Privilege
MFA
Segmentation
Threat Hunting
Incident Response
```

---

# 15. Other Important Threats

Add these to your learning path:

```text
Credential Stuffing
Password Spraying
Brute Force
ARP Poisoning
DNS Poisoning
Session Hijacking
Replay Attacks
Rogue Access Points
Evil Twin Wi-Fi
Routing Attacks
DNS Tunneling
Data Exfiltration
Supply Chain Attacks
Cloud Misconfiguration
```

---

# 16. Threat Identification and Prevention Strategy

Security should combine:

```text
Prevent
+
Detect
+
Respond
+
Recover
```

Diagram:

```text
         PREVENT
Firewall / MFA / Hardening
          ↓
        SYSTEM
          ↓
         DETECT
IDS / EDR / NDR / SIEM
          ↓
        RESPOND
IR / SOAR / Isolation
          ↓
        RECOVER
Backup / DR / Lessons Learned
```

---

# 17. System Hardening

Hardening reduces attack surface.

```text
Disable Unused Services
Close Unused Ports
Remove Unneeded Software
Patch Systems
Use Secure Baselines
Use MFA
Least Privilege
Host Firewall
Enable Logging
Disable Default Accounts
Session Timeouts
```

Concept:

```text
Default System
   ↓
Remove Unnecessary Features
   ↓
Patch
   ↓
Secure Configuration
   ↓
Smaller Attack Surface
```

---

# 18. IDS — Intrusion Detection System

An IDS monitors and alerts.

```text
Traffic
   ↓
IDS
   ↓
Analyze
   ↓
Alert
```

IDS is primarily a **detective** control.

## NIDS

Network-based IDS.

```text
Internet
   ↓
Firewall
   ↓
Switch ───> NIDS
   ↓
Internal Network
```

Traffic may be mirrored using:

```text
SPAN
Network TAP
Virtual Traffic Mirror
```

## HIDS

Host-based IDS.

Monitors:

```text
Logs
File Integrity
Processes
Authentication
Configuration
```

---

# 19. IPS — Intrusion Prevention System

An IPS detects and can block.

```text
Traffic
  ↓
IPS
  ↓
Analyze
  ↓
Allow / Block
```

Usually inline:

```text
Internet
   ↓
Firewall
   ↓
IPS
   ↓
Internal Network
```

## NIPS

Network-based IPS.

## HIPS

Host-based intrusion prevention.

---

# 20. IDS vs IPS

| IDS | IPS |
|---|---|
| Detects | Detects + blocks |
| Often passive | Usually inline/active |
| Alerts | Prevents/blocks |
| Lower disruption risk | False positives can block valid traffic |

Diagram:

```text
IDS:

Traffic ─────────────> Destination
           |
           +----> IDS
                  |
                 Alert
```

```text
IPS:

Traffic ──> IPS ──> Destination
           |
        Allow/Block
```

---

# 21. HIDS/HIPS vs NIDS/NIPS

| Host-Based | Network-Based |
|---|---|
| Endpoint telemetry | Network traffic |
| Processes/files/logs | Packets/flows |
| HIDS/HIPS/EDR | NIDS/NIPS/NDR |

Best results often come from combining both.

---

# 22. SIEM

**Security Information and Event Management** centralizes and correlates security telemetry.

Sources:

```text
Firewalls
Windows Events
Linux Logs
Cloud Audit Logs
DNS
VPN
EDR
IDS/IPS
Authentication
Applications
Databases
Proxies
```

Architecture:

```text
Firewall ─┐
EDR ──────┤
VPN ──────┤
DNS ──────┼──> SIEM ──> Correlation ──> Alert
Cloud ────┤
Servers ──┤
Apps ─────┘
```

Functions:

```text
Log Collection
Normalization
Correlation
Detection Rules
Search
Dashboards
Alerting
Investigation
Retention
Compliance Reporting
```

Correlation example:

```text
5 Failed Logins
      +
Successful Login
      +
New Country
      +
Admin Action
      ↓
High-Risk Alert
```

---

# 23. SOAR

**Security Orchestration, Automation and Response** automates security workflows.

```text
SIEM Alert
   ↓
SOAR
   ↓
Enrich IP
   ↓
Threat Intelligence
   ↓
Disable Account
   ↓
Block IP
   ↓
Create Ticket
   ↓
Notify Analyst
```

High-impact responses may require human approval.

---

# 24. Antivirus and Antimalware

Detection approaches can include:

```text
Signatures
Heuristics
Behavior Analysis
Reputation
Machine Learning
Sandboxing
```

Modern endpoint security extends beyond signature antivirus.

---

# 25. EDR, XDR, and NDR

## EDR

Endpoint Detection and Response.

Observes:

```text
Processes
Files
Registry
Network Connections
User Actions
Persistence
Commands
```

Can respond by:

```text
Isolate Endpoint
Kill Process
Quarantine File
Collect Forensics
```

## NDR

Network Detection and Response.

Useful for:

```text
Lateral Movement
C2 Traffic
Anomalous Flows
Unmanaged Devices
Encrypted-Traffic Metadata
```

## XDR

Extends detection across multiple telemetry domains.

```text
Endpoint
+
Identity
+
Email
+
Cloud
+
Network
      ↓
     XDR
```

---

# 26. Security Scanners

Categories:

```text
Network Scanner
Port Scanner
Vulnerability Scanner
Web Scanner
Cloud Posture Scanner
Configuration Scanner
Container Scanner
IaC Scanner
```

## Nmap

Used for authorized:

```text
Host Discovery
Port Scanning
Service Identification
Network Mapping
```

## Zenmap

Graphical front-end for Nmap.

Only scan systems you own or are explicitly authorized to assess.

---

# 27. Vulnerability Scanners vs Network Scanners

## Network Scanner

Answers:

```text
What hosts exist?
Which ports are open?
Which services respond?
```

## Vulnerability Scanner

Answers:

```text
Is software vulnerable?
Is configuration unsafe?
Is a known CVE present?
```

Findings should be validated and prioritized by context.

---

# 28. Firewalls

A firewall enforces traffic policy.

```text
Traffic
  ↓
Firewall Rules
  ↓
Allow / Deny
```

Attributes may include:

```text
Source IP
Destination IP
Protocol
Source Port
Destination Port
Connection State
Application
User
URL
Threat Intelligence
```

---

# 29. Firewall Types

```text
Packet-Filtering Firewall
Stateful Inspection Firewall
Circuit-Level Gateway
Application Proxy Firewall
Host-Based Firewall
Network Firewall
WAF
NGFW
FWaaS
```

## Packet Filter

Checks basic header fields.

## Stateful Firewall

Tracks:

```text
NEW
ESTABLISHED
RELATED
INVALID
```

## Application Proxy

Terminates/proxies application connections.

## Host Firewall

Runs locally on endpoint/server.

## WAF

Protects web applications.

---

# 30. Traditional Firewall vs NGFW

## Traditional Firewall

Focuses mainly on:

```text
IP
Port
Protocol
State
```

## NGFW

Adds capabilities such as:

```text
Application Identification
User Awareness
Integrated IPS
URL Filtering
Threat Prevention
TLS Inspection
Malware Analysis
DNS Security
```

Diagram:

```text
Traffic
  ↓
Stateful Inspection
  ↓
Application Identification
  ↓
User / Identity Context
  ↓
IPS / Threat Inspection
  ↓
Policy
  ↓
Allow / Block
```

---

# 31. FWaaS — Firewall as a Service

FWaaS provides firewall capabilities through a cloud-delivered platform.

Traditional:

```text
Branch
  ↓
Physical Firewall
  ↓
Internet
```

FWaaS:

```text
Branch / User / Cloud
        ↓
Cloud Security Service
        ↓
FWaaS Policy
        ↓
Internet / SaaS / Apps
```

Benefits:

```text
Central Policy
Elastic Scale
Remote User Support
Cloud Workload Support
Consistent Enforcement
```

Often associated with SASE/SSE architectures.

---

# 32. WAF vs Network Firewall

## Network Firewall

Focus:

```text
IP
Port
Protocol
State
Application
```

## WAF

Focus:

```text
HTTP Methods
URLs
Headers
Cookies
Payloads
Web Attack Patterns
```

Use cases:

```text
SQL Injection Filtering
XSS Filtering
Bot Management
Rate Limiting
```

---

# 33. DLP

**Data Loss Prevention** helps detect/prevent unauthorized movement of sensitive data.

Deployment points:

```text
Endpoint
Network
Email
Cloud
SaaS
```

Example:

```text
Employee Uploads
Customer Database
      ↓
DLP detects sensitive data
      ↓
Block / Warn / Log
```

---

# 34. Threat Prevention Architecture

```text
                   Internet
                      ↓
               DDoS Protection
                      ↓
                    NGFW
                      ↓
                    IPS
                      ↓
                     WAF
                      ↓
                  Application
                      ↓
                   Database
```

Cross-cutting:

```text
EDR
NDR
SIEM
SOAR
DLP
MFA
PAM
Backups
Threat Intelligence
```

---

# 35. Network Security Infrastructure

Security depends on reliable infrastructure.

```text
Physical Facility
Power
Cooling
Network
Compute
Storage
Security Systems
Monitoring
Operational Procedures
```

---

# 36. Data Center Types

## On-Premises

Organization owns/controls the facility and infrastructure.

## Colocation

Customer equipment is placed in a provider facility.

## Cloud Data Center

Cloud provider owns/operates physical infrastructure; customers consume services.

## Hybrid

```text
On-Premises
+
Cloud
```

with integrated connectivity/operations.

---

# 37. Data Center Components

```text
Server Racks
Network Closets
Switches
Routers
Firewalls
Storage
UPS
Generators
HVAC
Fire Detection/Suppression
CCTV
Access Control
Mantraps
Monitoring Room
Environmental Sensors
```

Diagram:

```text
          Utility Power
               ↓
              UPS
               ↓
           PDU / Rack
               ↓
       Servers + Network
               ↓
             Apps

Generator ─────────┘

HVAC → Cooling
CCTV → Monitoring
Mantrap → Physical Access
Fire Suppression → Safety
```

---

# 38. Data Center Physical & Environmental Security

```text
Fences
Guards
CCTV
Access Cards
Biometrics
Mantraps
Locked Racks
UPS
Generators
HVAC
Fire Detection
Fire Suppression
Water Detection
Environmental Sensors
```

Defense in depth:

```text
Site Perimeter
    ↓
Building Access
    ↓
Data Hall Access
    ↓
Rack Access
    ↓
System Authentication
```

---

# 39. Data Center Redundancy

Examples:

```text
Dual Power Feeds
UPS
Backup Generators
Redundant Switches
Multiple ISPs
Multiple Routers
RAID
Clustered Servers
Multiple Cooling Units
```

Goal:

```text
Component A fails
      ↓
Component B continues service
```

Avoid a:

```text
Single Point of Failure — SPOF
```

---

# 40. JOA, MOU, MOA, and SLA

These terms appear in continuity, outsourcing, and inter-organizational support.

## JOA — Joint Operating Agreement

Defines how organizations jointly operate or share certain activities/resources.

In continuity/security training it may describe coordinated operational support during disruption.

Exact legal meaning depends on context and jurisdiction.

## MOU — Memorandum of Understanding

Documents mutual understanding and intent.

Typical contents:

```text
Purpose
Roles
Responsibilities
Cooperation
General Terms
```

## MOA — Memorandum of Agreement

Similar to an MOU, often used to document more detailed responsibilities/support arrangements.

## SLA — Service Level Agreement

Defines measurable service expectations.

Examples:

```text
Availability
Response Time
Resolution Time
Support Hours
Performance
Backup Recovery
Security Obligations
Escalation
Service Credits
```

Simple memory:

```text
JOA
→ Joint operations

MOU
→ Shared understanding / intent

MOA
→ Agreement on cooperation/responsibilities

SLA
→ Measurable service commitments
```

---

# 41. SLA Availability and the Nines

| Availability | Approx. Downtime / Year |
|---|---:|
| 99% | 3.65 days |
| 99.9% | 8.76 hours |
| 99.95% | 4.38 hours |
| 99.99% | 52.6 minutes |
| 99.999% | 5.26 minutes |

Formula:

```text
Allowed Downtime
=
Total Time × (1 - Availability)
```

Read SLA exclusions carefully:

```text
Maintenance Windows
Measurement Window
Regional Scope
Service Credits
Eligibility Conditions
```

---

# 42. Cloud Computing Fundamentals

Cloud computing provides shared computing resources that can be provisioned rapidly and accessed over networks.

Resources include:

```text
Compute
Storage
Database
Networking
Identity
Analytics
AI
Security
```

Traditional:

```text
Buy Server
Wait
Install
Configure
```

Cloud:

```text
API Request
    ↓
Resource Provisioned
```

---

# 43. Essential Cloud Characteristics

NIST defines five essential cloud characteristics:

```text
On-Demand Self-Service
Broad Network Access
Resource Pooling
Rapid Elasticity
Measured Service
```

## On-Demand Self-Service

Provision resources when needed.

## Broad Network Access

Capabilities are available through networks and standard mechanisms.

## Resource Pooling

Provider resources serve multiple consumers.

## Rapid Elasticity

Scale up/down quickly.

## Measured Service

Usage is monitored/metered.

---

# 44. IaaS, PaaS, SaaS

## IaaS

Customer manages more of the stack.

```text
Customer:
OS
Applications
Data
Configuration
Identity

Provider:
Physical Infrastructure
Virtualization
```

## PaaS

Provider manages more runtime/platform components.

Customer focuses more on:

```text
Application
Data
Identity
Configuration
```

## SaaS

Provider operates most of the application stack.

Customer mainly manages:

```text
Users
Data
Configuration
Access
Governance
```

Diagram:

```text
More Customer Management
          ↑
On-Prem
IaaS
PaaS
SaaS
          ↓
More Provider Management
```

---

# 45. Cloud Deployment Models

```text
Public Cloud
Private Cloud
Hybrid Cloud
Community Cloud
```

## Public

Shared provider infrastructure offered to customers.

## Private

Dedicated cloud environment for one organization.

## Hybrid

Integrates private/on-premises and public cloud.

## Community

Provisioned for a specific community with shared concerns/requirements.

---

# 46. Regions and Availability Zones

A **Region** is a geographic cloud-service area.

An **Availability Zone** is an isolated provider-defined location/failure domain within a region.

```text
Region
├── AZ A
├── AZ B
└── AZ C
```

High availability often uses:

```text
Multiple AZs
```

Disaster recovery may use:

```text
Multiple Regions
```

when requirements justify it.

---

# 47. Cloud Shared Responsibility

Simplified:

```text
Provider
→ Security OF the cloud

Customer
→ Security IN the cloud
```

Responsibility varies by service model.

Customers still control critical areas such as:

```text
Data
Identity
Access
Configuration
Business Decisions
```

---

# 48. MSP and MSSP

## MSP — Managed Service Provider

Outsourced IT services.

Examples:

```text
Help Desk
Infrastructure Management
Backup
Cloud Operations
Network Management
Patch Management
```

## MSSP — Managed Security Service Provider

Outsourced security operations.

Examples:

```text
SOC Monitoring
SIEM Management
MDR
Firewall Management
Vulnerability Management
Incident Response
```

```text
MSP
→ General Managed IT

MSSP
→ Managed Cybersecurity
```

---

# 49. Network and Cloud Security Architecture

Security architecture must control:

```text
North-South Traffic
East-West Traffic
Identity
Endpoints
Applications
Cloud Resources
Data
Management Plane
```

## North-South

Traffic entering/leaving environment.

## East-West

Traffic between internal workloads.

Lateral movement commonly uses east-west paths.

---

# 50. Segmentation

Bad:

```text
One Flat Network
```

Better:

```text
Users
Servers
Databases
Guests
IoT
Management
Production
Development
```

Diagram:

```text
            Firewall
               |
    ┌──────────┼──────────┐
    |          |          |
 Users      Servers      Guest
    |          |
    |       Firewall
    |          |
    └────> Database
```

Benefits:

```text
Reduce Lateral Movement
Reduce Blast Radius
Improve Monitoring
Apply Least Privilege
```

---

# 51. VLANs

**Virtual LAN** creates logical Layer 2 segments.

```text
Switch
├── VLAN 10 — Employees
├── VLAN 20 — Servers
└── VLAN 30 — Guests
```

VLANs separate broadcast domains.

Inter-VLAN communication requires Layer 3 routing.

Important:

```text
VLAN != Complete Security Boundary
```

Add:

```text
Firewall Rules
ACLs
NAC
Monitoring
```

---

# 52. DMZ

**Demilitarized Zone** hosts systems exposed to untrusted networks.

```text
Internet
   ↓
Firewall
   ↓
DMZ
   ↓
Internal Firewall
   ↓
Internal Network
```

Typical DMZ systems:

```text
Reverse Proxy
Public Web Server
Mail Gateway
DNS Server
VPN Gateway
```

Goal:

```text
Compromise of public service
should not directly expose
internal systems.
```

---

# 53. Microsegmentation

Fine-grained workload communication policy.

```text
Web-01
  ↓ only required app port
App-01
  ↓ only DB port
DB-01
```

Useful in:

```text
Cloud
Kubernetes
Virtualized Data Centers
Zero Trust
```

---

# 54. Zero Trust

Core principles:

```text
Verify Explicitly
Use Least Privilege
Assume Breach
```

Old:

```text
Inside Network
= Trusted
```

Zero Trust:

```text
Request
  ↓
Identity
Device
Location
Risk
Resource
Context
  ↓
Policy
  ↓
Allow / Deny
```

---

# 55. NAC

**Network Access Control** determines whether a user/device can connect.

Checks may include:

```text
Identity
Certificate
Device Health
Patch Status
EDR Status
OS Version
Compliance
```

Diagram:

```text
Device
  ↓
Switch / AP
  ↓
802.1X / NAC
  ↓
Identity + Posture
  ↓
 ┌─────────────┬──────────────┐
 |             |              |
Corporate   Guest         Quarantine
```

---

# 56. VPN

## Remote Access

```text
Remote User
    ↓
Encrypted Tunnel
    ↓
VPN Gateway
    ↓
Corporate Network
```

## Site-to-Site

```text
Office A
   ↓
IPsec Tunnel
   ↓
Office B
```

Common technologies:

```text
IPsec
TLS VPN
WireGuard
```

---

# 57. ZTNA

**Zero Trust Network Access** provides application-specific access based on identity/context.

VPN-style broad access:

```text
User
 ↓
Large Internal Network
```

ZTNA:

```text
User
 ↓
Identity + Device + Policy
 ↓
Specific Application Only
```

---

# 58. SASE and SSE

## SASE

Secure Access Service Edge combines networking and cloud-delivered security.

Common components:

```text
SD-WAN
FWaaS
SWG
CASB
ZTNA
DNS Security
```

Diagram:

```text
User / Branch / Cloud
        ↓
Cloud Security Edge
        ↓
Internet / SaaS / Private Apps
```

## SSE

Security-focused subset of SASE.

Often includes:

```text
ZTNA
SWG
CASB
FWaaS-related security services
```

---

# 59. Defense in Depth

```text
Physical Security
      ↓
DDoS Protection
      ↓
Firewall
      ↓
IPS
      ↓
Segmentation
      ↓
NAC
      ↓
EDR
      ↓
Application Security
      ↓
Identity / MFA
      ↓
Encryption
      ↓
SIEM
```

One control failing should not mean total compromise.

---

# 60. Security Monitoring Architecture

```text
Endpoints ───┐
Firewalls ───┤
Cloud ───────┤
DNS ─────────┤
VPN ─────────┤
Identity ────┤
Apps ────────┤
IDS/IPS ─────┘
      ↓
    SIEM
      ↓
Correlation / Analytics
      ↓
    Alerts
      ↓
 SOC Analyst / SOAR
      ↓
 Investigation
      ↓
 Response
```

---

# 61. Incident Detection Flow

```text
User receives phishing email
          ↓
Credential stolen
          ↓
Attacker logs into VPN
          ↓
Identity logs unusual login
          ↓
VPN logs new source
          ↓
NDR sees lateral movement
          ↓
SIEM correlates events
          ↓
High severity incident
          ↓
SOAR enriches alert
          ↓
Analyst confirms
          ↓
Account disabled
          ↓
Sessions revoked
          ↓
Endpoint isolated
```

---

# 62. Example Enterprise Security Architecture

```text
                        Internet
                           |
                    DDoS Protection
                           |
                        NGFW
                           |
                 +---------+---------+
                 |                   |
                DMZ                VPN/ZTNA
                 |                   |
          Reverse Proxy/WAF          |
                 |                   |
                 +---------+---------+
                           |
                     Core Firewall
                           |
          +----------------+----------------+
          |                |                |
        Users            Servers        Management
          |                |                |
         NAC              IPS              PAM
          |                |
         EDR           Microsegmentation
                           |
                       Databases
```

Monitoring:

```text
All Logs
   ↓
SIEM
   ↓
SOAR / SOC
```

Data controls:

```text
Encryption
DLP
Backups
Access Control
```

---

# 63. Threat-to-Control Mapping

| Threat | Useful Controls |
|---|---|
| Phishing | Email security, awareness, MFA/passkeys |
| Credential theft | MFA, conditional access, PAM, monitoring |
| DDoS | DDoS protection, CDN, rate limiting |
| Spoofing | Authentication, anti-spoofing filters, stateful firewall |
| MITM | TLS, VPN, certificate validation |
| Worm | Patching, segmentation, EDR, IPS |
| Ransomware | EDR, backups, MFA, segmentation, hardening |
| Insider threat | Least privilege, DLP, logging, SoD |
| APT | EDR/XDR, SIEM, NDR, threat hunting |
| Lateral movement | Segmentation, microsegmentation, NAC |
| Data exfiltration | DLP, egress controls, NDR, CASB |
| Public web attack | WAF, NGFW, DDoS protection |

---

# 64. Common Misconceptions

## IDS and IPS Are the Same

Incorrect.

```text
IDS
→ Detect + Alert

IPS
→ Detect + Block
```

## Antivirus Is Enough

Incorrect.

Modern environments may also need:

```text
EDR
SIEM
Identity Protection
Network Detection
Email Security
Backups
```

## Firewall Stops Every Attack

Incorrect.

A firewall alone does not solve:

```text
Phishing
Stolen Credentials
Insider Abuse
Application Logic Bugs
Malicious Approved Traffic
```

## VLAN = Complete Security

Incorrect.

Use proper firewall/ACL policy between segments.

## VPN = Zero Trust

Not necessarily.

VPN may provide broad network access; ZTNA is typically more application-specific.

## Cloud Provider Secures Everything

Incorrect.

Cloud follows shared responsibility.

---

# 65. Interview and Exam Questions

## Insider vs outsider threat?

```text
Insider:
Has or had legitimate organizational access.

Outsider:
Starts outside organizational access.
```

## What is spoofing?

Falsifying an identity/address to impersonate another entity.

## DoS vs DDoS?

```text
DoS:
Limited source(s)

DDoS:
Distributed sources
```

## What is an on-path attack?

An attacker intercepts communications between endpoints.

## What is a side-channel attack?

Extracts information from implementation leakage such as timing, power, cache behavior, or EM signals.

## Phishing vs spear phishing?

```text
Phishing:
Broad

Spear phishing:
Targeted and personalized
```

## Virus vs worm?

```text
Virus:
Typically attaches to host files/programs.

Worm:
Self-propagates across systems/networks.
```

## Trojan?

Malware disguised as legitimate software/content.

## APT?

A long-term targeted intrusion campaign involving persistence and sophisticated operations.

## Ransomware?

Malware/extortion operation that commonly encrypts and/or steals data for ransom.

## IDS vs IPS?

```text
IDS:
Alert

IPS:
Block
```

## SIEM?

Central platform for collecting, correlating, detecting, and investigating security events.

## EDR?

Endpoint Detection and Response.

## NDR?

Network Detection and Response.

## NGFW?

Firewall combining stateful filtering with advanced application/security inspection.

## FWaaS?

Cloud-delivered firewall capability.

## What is an SLA?

Agreement defining measurable service expectations.

## MOU?

Documents mutual understanding and intent.

## MOA?

Documents cooperation/responsibilities, often in more operational detail.

## JOA?

Joint Operating Agreement defining coordinated/shared operations.

## What is segmentation?

Dividing a network into controlled security zones.

## Microsegmentation?

Fine-grained workload-level communication controls.

## DMZ?

Segment for public/exposed systems separated from internal resources.

## NAC?

Controls network admission based on identity/device posture.

## Zero Trust?

```text
Verify explicitly
Least privilege
Assume breach
```

---

# 66. Final Review Sheet

## Threat Sources

```text
Insider
Outsider
```

## Major Threats

```text
Spoofing
DoS
DDoS
On-Path / MITM
Side Channel
Phishing
Spear Phishing
Virus
Worm
Trojan
APT
Ransomware
```

## Detection / Prevention

```text
Hardening
Firewall
IDS
IPS
Antimalware
EDR
NDR
XDR
SIEM
SOAR
DLP
Scanners
```

## IDS vs IPS

```text
IDS
→ Detect

IPS
→ Detect + Prevent
```

## Firewall Family

```text
Packet Filter
Stateful Firewall
Proxy Firewall
Host Firewall
Network Firewall
WAF
NGFW
FWaaS
```

## Data Center Types

```text
On-Premises
Colocation
Cloud
Hybrid
```

## Data Center Components

```text
Racks
Servers
Storage
Switches
Routers
Firewalls
UPS
Generators
HVAC
Fire Suppression
CCTV
Mantraps
Monitoring
```

## Agreements

```text
JOA
→ Joint Operations

MOU
→ Mutual Understanding

MOA
→ Agreement / Cooperation

SLA
→ Measurable Service Levels
```

## Cloud Characteristics

```text
On-Demand Self-Service
Broad Network Access
Resource Pooling
Rapid Elasticity
Measured Service
```

## Cloud Service Models

```text
IaaS
PaaS
SaaS
```

## Cloud Deployment Models

```text
Public
Private
Hybrid
Community
```

## Secure Network / Cloud Design

```text
Segmentation
VLAN
DMZ
Microsegmentation
Zero Trust
NAC
VPN
ZTNA
SASE
FWaaS
```

---

# 67. Authoritative References

## NIST

- NIST Cybersecurity Framework 2.0  
  https://www.nist.gov/cyberframework

- NIST SP 800-207 — Zero Trust Architecture  
  https://csrc.nist.gov/pubs/sp/800/207/final

- NIST SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy  
  https://csrc.nist.gov/pubs/sp/800/41/r1/final

- NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide  
  https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

- NIST SP 800-145 — The NIST Definition of Cloud Computing  
  https://csrc.nist.gov/pubs/sp/800/145/final

- NIST Glossary — Memorandum of Understanding / Agreement  
  https://csrc.nist.gov/glossary/term/memorandum_of_understanding_or_agreement

## Threat Knowledge

- MITRE ATT&CK  
  https://attack.mitre.org/

- CISA Cyber Threats and Advisories  
  https://www.cisa.gov/topics/cyber-threats-and-advisories

---

# End of Document
