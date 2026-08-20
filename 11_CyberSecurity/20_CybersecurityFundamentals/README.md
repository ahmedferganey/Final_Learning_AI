# Phase 20 — Cybersecurity Fundamentals

Phase 20 is the transition from broad IT, cloud, systems, networking, software, and cloud-native engineering into the dedicated cybersecurity sequence.

It is intentionally ordered so that you first understand **security concepts and risk**, then **information protection**, then **network defense**, then **security assessment**, and only after that begin **ethical-hacking methodology**.

---

## Phase Goal

By the end of this phase, you should be able to reason about cybersecurity as a complete defensive system:

```text
Business / Mission
      ↓
Assets + Information
      ↓
Threats + Vulnerabilities + Exposure
      ↓
Risk
      ↓
Preventive / Detective / Corrective / Recovery Controls
      ↓
Security Monitoring
      ↓
Assessment
      ↓
Authorized Ethical Validation
      ↓
Remediation
      ↓
Retest
      ↓
Continuous Improvement
```

This phase prepares you for later specialization in:

```text
Network Security
Penetration Testing
Application Security
Malware Analysis / Reverse Engineering
SOC / Defensive Security
Incident Response / Forensics
OT Security
GRC
Cloud Security
DevSecOps
AI Security
```

---

# Courses

| # | Course | Primary Focus |
|---|---|---|
| **81** | **Cybersecurity Fundamentals** | Security principles, risk, CIA, IAM, controls, endpoint/application/cloud/security-operations foundations |
| **82** | **Information Security Fundamentals** | Information lifecycle, classification, handling, risk, governance, ISMS, privacy, retention, sanitization, audit |
| **83** | **Network Security Fundamentals** | Segmentation, firewalls, secure protocols, VPN, NAC, IDS/IPS/NDR, packet/flow visibility, cloud networking |
| **84** | **Security Assessment Fundamentals** | Scope, evidence, vulnerability/configuration assessment, safe validation, reporting, remediation, retest |
| **85** | **Ethical Hacking Fundamentals** | Authorization-first attacker thinking, reconnaissance, enumeration, safe vulnerability validation, evidence and reporting |

---

# Recommended Study Order

Follow the courses strictly in this order:

```text
81 Cybersecurity Fundamentals
        ↓
82 Information Security Fundamentals
        ↓
83 Network Security Fundamentals
        ↓
84 Security Assessment Fundamentals
        ↓
85 Ethical Hacking Fundamentals
```

Do **not** jump directly to exploitation tools.

The intended progression is:

```text
Understand security
      ↓
Understand what information requires protection
      ↓
Understand network trust boundaries
      ↓
Learn how to assess controls
      ↓
Learn how to validate weaknesses safely
```

---

# Prerequisites

You should already have working foundations in:

```text
Operating Systems
Computer Networks
Linux
Windows Server / Active Directory
Databases
Web Technologies
Programming / Scripting
Cloud Computing
Virtualization
Docker / Kubernetes
Git
Backend / API Fundamentals
Cloud-Native Architecture
```

That earlier technical background matters because cybersecurity becomes much easier when you already understand how systems are expected to operate.

---

# How to Study Each Course

Every course uses the same learning loop:

```text
Concept
  ↓
Detailed Explanation
  ↓
Diagram / Mental Model
  ↓
Command / Code / Configuration
  ↓
Expected Behavior
  ↓
Why It Works
  ↓
Real Security Scenario
  ↓
Common Problems
  ↓
Best Practices
  ↓
Hands-on Lab
  ↓
Self-Assessment
```

Recommended approach:

1. Read the core topic.
2. Redraw the diagram yourself.
3. Reproduce commands only in your own lab.
4. Explain the security objective before touching a tool.
5. Record evidence from the lab.
6. Explain what control prevents or detects the problem.
7. Write the remediation.
8. Retest after remediation.
9. Answer the self-assessment questions without looking at the answer first.

---

# Phase 20 Security Lab Rules

All technical exercises in this phase must follow one rule:

> **Only test systems, accounts, applications, networks, cloud resources, or devices that you own or are explicitly authorized to assess.**

Use:

```text
localhost
your own VMs
your own containers
your own cloud test account
intentionally vulnerable training applications
isolated lab networks
synthetic users and data
```

Do not use:

```text
random public IP addresses
third-party Wi-Fi networks
systems found through Internet search engines
other people's cloud infrastructure
real user credentials
out-of-scope company systems
unapproved production scanning
```

Recommended lab layout:

```text
                     ┌──────────────────────┐
                     │ Security Workstation │
                     │ Kali / Ubuntu / etc. │
                     └──────────┬───────────┘
                                │
                        isolated lab network
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
   ┌──────▼──────┐       ┌──────▼──────┐      ┌──────▼──────┐
   │ Linux Server │       │ Windows Lab │      │ Web / API   │
   │              │       │ / AD Lab    │      │ Training App│
   └──────────────┘       └─────────────┘      └─────────────┘
```

Take snapshots before experiments and keep intentionally vulnerable targets isolated from the public Internet.

---

# Core Mental Models to Master

## 1. Risk

```text
Asset
  +
Threat
  +
Vulnerability / Exposure
  ↓
Likelihood
  ×
Impact
  ↓
Risk
  ↓
Control
  ↓
Residual Risk
```

---

## 2. Security Controls

```text
Prevent
  ↓
Detect
  ↓
Respond
  ↓
Recover
```

Controls can also be categorized as:

```text
Administrative
Technical
Physical
```

---

## 3. Identity and Access

```text
Identity
  ↓
Authentication
  ↓
Authorization
  ↓
Least Privilege
  ↓
Audit
```

---

## 4. Network Security

```text
Source
  ↓
Identity / Device Context
  ↓
Network Zone
  ↓
Firewall / ACL / Policy
  ↓
Destination
  ↓
Network Telemetry
```

The main design question is not only:

> Can this host reach that host?

It is:

> **Should this identity or workload be able to reach this exact service, under which conditions, and how will that access be monitored?**

---

## 5. Information Security

```text
Create / Collect
      ↓
Classify
      ↓
Store
      ↓
Use
      ↓
Share / Transfer
      ↓
Archive / Retain
      ↓
Sanitize / Destroy
```

Classification should determine:

```text
Who can access it?
Where may it be stored?
How must it be transmitted?
Is encryption required?
May it be printed or copied?
How long is it retained?
How must it be destroyed?
```

---

## 6. Security Assessment

```text
Authorization
      ↓
Scope
      ↓
Expected Secure State
      ↓
Evidence Collection
      ↓
Analysis
      ↓
Safe Validation
      ↓
Finding
      ↓
Risk Priority
      ↓
Remediation
      ↓
Retest
```

A scanner result is **not automatically a finding**.

You must verify:

```text
Is the condition real?
Is the asset actually affected?
Is it exposed?
What privileges are required?
What controls already exist?
What is the real business impact?
```

---

## 7. Ethical Hacking

```text
Authorization
      ↓
Reconnaissance
      ↓
Enumeration
      ↓
Vulnerability Analysis
      ↓
Minimal Safe Proof
      ↓
Impact
      ↓
Evidence
      ↓
Remediation
      ↓
Retest
```

The goal is **not maximum access**.

The goal is:

> Obtain enough evidence to prove the security condition safely, then stop.

---

# Course 81 — Cybersecurity Fundamentals

## Main Outcome

You should finish Course 81 able to explain security without immediately naming a product or tool.

You should understand:

```text
Assets
Threats
Vulnerabilities
Exposure
Likelihood
Impact
Inherent Risk
Residual Risk
Risk Appetite
Risk Tolerance
Risk Treatment
```

And connect them to:

```text
CIA
Identity
Network Security
Endpoint Security
Application Security
Cloud Security
Logging
Incident Response
Recovery
Governance
```

### Key Design Question

```text
What business outcome are we protecting,
what can prevent that outcome,
and what evidence tells us the controls are working?
```

---

# Course 82 — Information Security Fundamentals

## Main Outcome

You should understand that **information** is the primary asset—not merely servers or applications.

You should be able to create:

- information classification levels;
- handling rules;
- retention schedules;
- access-review processes;
- data-owner / steward / custodian responsibilities;
- sanitization and destruction requirements;
- risk registers;
- control matrices;
- evidence requirements;
- basic ISMS structure.

### Important Distinction

```text
Delete != Securely Sanitize
```

Normal deletion often changes filesystem/object metadata while underlying data can remain recoverable.

Sanitization decisions should consider:

```text
Media type
Information sensitivity
Reuse requirement
Disposal destination
Technology limitations
Organizational policy
```

---

# Course 83 — Network Security Fundamentals

## Main Outcome

You should be able to look at a network diagram and identify:

```text
trust zones
management plane
control plane
data plane
Internet exposure
remote access
routing boundaries
firewall boundaries
DNS/DHCP dependencies
monitoring points
high-risk east-west paths
```

### Core Defensive Model

```text
Internet
   ↓
Edge Security
   ↓
DMZ / Public Services
   ↓
Application Zone
   ↓
Data Zone

Separate:
Management Zone
User Zone
Guest Zone
Backup Zone
OT Zone where applicable
```

### Troubleshooting Model

```text
DNS
 ↓
IP Route
 ↓
Firewall / ACL
 ↓
Service Listener
 ↓
TLS
 ↓
Authentication
 ↓
Authorization
 ↓
Application
```

Do not randomly restart systems before determining which layer is failing.

---

# Course 84 — Security Assessment Fundamentals

## Main Outcome

You should be able to conduct a professional **authorized security assessment** without relying on exploitation.

You should be comfortable with:

```text
asset inventory review
service discovery
configuration assessment
credentialed vulnerability scanning
baseline comparison
web/API review
cloud IAM review
container/Kubernetes review
code / dependency / IaC assessment
evidence validation
finding prioritization
professional reporting
retesting
```

### Professional Finding Structure

```text
Title
Affected Asset
Condition
Evidence
Security Impact
Business Impact
Exposure / Preconditions
Severity / Priority
Remediation
Compensating Control
Owner
Retest Method
Status
```

---

# Course 85 — Ethical Hacking Fundamentals

## Main Outcome

Course 85 changes the question from:

> Is the configuration insecure?

to:

> Can the weakness be safely demonstrated under authorization?

This introduces attacker-style thinking while keeping strict boundaries.

### Ethical Hacking Rule

```text
Can configuration / code / version evidence prove the problem?
        │
        ├── Yes → stop there.
        │
        └── No
             ↓
     Is minimal validation authorized?
             │
             ├── No → report limitation.
             │
             └── Yes
                  ↓
           perform minimal proof
                  ↓
                  STOP
```

You do not continue deeper merely because additional access is technically possible.

---

# Recommended Tools for Phase 20

The phase is intentionally **tool-light compared with later penetration-testing phases**.

Use tools to understand and verify concepts.

## Networking

```text
ip
ss
ping
traceroute / tracepath
dig
nslookup
curl
openssl
tcpdump
Wireshark
Nmap — only within authorized lab scope
```

## Linux

```text
journalctl
systemctl
ss
ip
find
stat
ls
sudo
sha256sum
openssl
```

## Windows / PowerShell

```text
Get-WinEvent
Get-NetTCPConnection
Get-Service
Get-ComputerInfo
Get-LocalUser
Get-LocalGroupMember
Get-FileHash
```

## Web / API

```text
Browser developer tools
curl
Burp Suite Community
OWASP ZAP
Postman / Bruno / equivalent API client
```

## Defensive / Assessment

```text
Nmap
Wireshark
CIS Benchmarks
vulnerability scanners in authorized environments
SAST
SCA
secret scanning
IaC security scanning
cloud security configuration tools
```

Do not make the mistake of thinking:

```text
more tools = more cybersecurity knowledge
```

The more important skill is:

```text
understand architecture
   ↓
ask the correct security question
   ↓
choose the correct evidence
   ↓
use the smallest appropriate tool
```

---

# Recommended Phase 20 Lab Portfolio

Create one folder for the entire phase:

```text
Phase_20_Lab/
├── 01_Risk/
├── 02_Information_Security/
├── 03_Network_Security/
├── 04_Security_Assessment/
├── 05_Ethical_Hacking/
├── diagrams/
├── evidence/
├── reports/
└── README.md
```

Example structure:

```text
01_Risk/
├── asset_inventory.csv
├── risk_register.csv
├── control_matrix.csv
└── risk_notes.md

02_Information_Security/
├── classification_policy.md
├── handling_standard.md
├── retention_schedule.csv
└── sanitization_matrix.csv

03_Network_Security/
├── network_diagram.md
├── firewall_matrix.csv
├── segmentation_plan.md
├── pcap/
└── network_baseline.md

04_Security_Assessment/
├── scope.md
├── rules_of_engagement.md
├── evidence/
├── findings.md
└── retest.md

05_Ethical_Hacking/
├── lab_scope.md
├── recon_notes.md
├── enumeration/
├── findings/
├── remediation/
└── cleanup_checklist.md
```

---

# Recommended Evidence Template

For every security lab:

```text
Lab ID:
Date:
Scope:
Asset:
Owner:
Objective:
Expected secure state:
Method:
Command / configuration:
Observed result:
Evidence path:
Security impact:
Recommended control:
Residual risk:
Retest:
```

This habit becomes extremely important later in:

```text
penetration testing
SOC
incident response
forensics
cloud security
GRC
security audits
```

---

# Phase 20 Capstone

After finishing Course 85, combine the five course projects into one capstone.

## Scenario

You are responsible for the initial security program of a medium-sized company with:

```text
150 employees
Windows / Active Directory
Linux servers
Cloud workloads
Microsoft 365 / SaaS
Corporate + guest Wi-Fi
Remote workers
Public web/API
Databases
Docker / Kubernetes workload
Backups
Third-party suppliers
```

## Deliverables

Create:

1. `Asset_Inventory.csv`
2. `Information_Classification.md`
3. `Risk_Register.csv`
4. `Network_Security_Architecture.md`
5. `Firewall_Rule_Matrix.csv`
6. `IAM_Model.md`
7. `Hardening_Baseline.md`
8. `Vulnerability_Assessment.md`
9. `Rules_of_Engagement.md`
10. `Ethical_Hacking_Report.md`
11. `Logging_and_Detection_Plan.md`
12. `Incident_Response_Runbook.md`
13. `Backup_and_Recovery_Plan.md`
14. `Security_Metrics.md`
15. `Executive_Security_Summary.md`

### Capstone Architecture

```text
                        Internet
                           │
                    CDN / WAF / Edge
                           │
                  Public Application/API
                           │
                    Application Zone
                           │
                       Data Zone
                           │
                     Backup / DR

Users ── Identity / MFA ── Access Policy
  │
Corporate LAN
  ├─ User VLAN
  ├─ Server VLAN
  ├─ Management VLAN
  └─ Guest VLAN → Internet only

Security Telemetry
  ├─ Identity logs
  ├─ Endpoint logs
  ├─ Firewall / VPN
  ├─ DNS
  ├─ Cloud audit
  ├─ Application
  └─ Kubernetes
          ↓
         SIEM
          ↓
Detection → Investigation → Incident Response
```

---

# Knowledge Check Before Leaving Phase 20

Do not move on until you can explain, without notes:

### Security Fundamentals

```text
CIA
asset
threat
vulnerability
exposure
risk
inherent risk
residual risk
risk appetite
risk tolerance
control
defense in depth
Zero Trust
```

### Identity

```text
authentication
authorization
MFA
RBAC
ABAC
least privilege
privileged access
service accounts
workload identity
```

### Information Security

```text
classification
handling
retention
legal hold
data minimization
encryption
hashing
digital signature
sanitization
clear / purge / destroy
ISMS
```

### Network Security

```text
VLAN
routing
ACL
stateful firewall
DMZ
segmentation
ingress / egress
DNS
DHCP
VPN
802.1X
NAC
IDS / IPS / NDR
packet capture
flow logs
```

### Assessment

```text
authorization
scope
Rules of Engagement
passive / active
credentialed / unauthenticated
CVE
CWE
CVSS
EPSS
false positive
finding
remediation
retest
```

### Ethical Hacking

```text
reconnaissance
enumeration
attack surface
safe validation
PoC
authentication testing
authorization testing
SQL injection concept
XSS concept
command injection concept
SSRF concept
privilege escalation concept
evidence
cleanup
```

---

# What Phase 20 Does NOT Try to Make You Yet

After this phase, you are **not yet expected to be an advanced penetration tester**.

You are not expected to have mastered:

```text
advanced exploit development
evasion
malware development
advanced Active Directory attack chains
advanced web exploitation
mobile exploitation
binary exploitation
reverse engineering
red-team infrastructure
advanced post-exploitation
```

Those topics belong to later specialized phases.

Phase 20's purpose is to make sure your later offensive and defensive work is based on correct security reasoning.

---

# Transition to Phase 21

After Phase 20, move to:

# Phase 21 — Network Security

```text
86. Firewall Technologies
87. Network Security Assessment
88. Network Penetration Testing
```

The dependency is:

```text
83 Network Security Fundamentals
          ↓
84 Security Assessment Fundamentals
          ↓
85 Ethical Hacking Fundamentals
          ↓
86 Firewall Technologies
          ↓
87 Network Security Assessment
          ↓
88 Network Penetration Testing
```

This means Phase 21 should not repeat basic VLAN, TCP/IP, firewall, or assessment definitions in full.

Instead it can go deeper into:

```text
firewall architectures
state tables
NAT and policy interaction
NGFW capabilities
VPN policy
rulebase engineering
firewall troubleshooting
network reconnaissance
service validation
segmentation testing
network attack-path analysis
safe exploitation in labs
network reporting
```

---

# Phase Statistics

Current generated Phase 20 materials:

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 81 — Cybersecurity Fundamentals | 144 | 80 | 144 | 11,882 |
| 82 — Information Security Fundamentals | 171 | 80 | 171 | 13,293 |
| 83 — Network Security Fundamentals | 165 | 80 | 165 | 13,605 |
| 84 — Security Assessment Fundamentals | 168 | 80 | 168 | 13,697 |
| 85 — Ethical Hacking Fundamentals | 247 | 80 | 247 | 19,830 |
| **Total** | **895** | **400** | **895** | **72,307** |

---

# Phase Completion Criteria

Consider Phase 20 complete when you can:

- explain cybersecurity in risk language rather than only tool names;
- identify assets, threats, vulnerabilities, exposures, controls, and residual risk;
- classify and protect information through its lifecycle;
- design basic network segmentation and firewall policy;
- explain authentication vs authorization correctly;
- inspect a system/network/application safely;
- distinguish scanner output from a validated finding;
- write a professional security finding;
- perform a small authorized lab assessment;
- demonstrate a vulnerability with minimal impact;
- remediate and retest;
- explain which logs/detections should observe the activity;
- maintain clear evidence and cleanup procedures.

---

# Final Phase Mental Model

```text
                      CYBERSECURITY
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
     GOVERN             PROTECT            OPERATE
        │                  │                  │
     Risk / Policy      Identity           Logging
     Ownership          Network            Detection
     Assurance          Endpoint           Response
                        Application         Recovery
                        Data
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ↓
                       ASSESS
                           ↓
                 Authorized Validation
                           ↓
                      REMEDIATE
                           ↓
                        RETEST
                           ↓
                       IMPROVE
```

**Phase 20 is complete when you can connect every tool, control, finding, and test back to a risk, asset, owner, expected security outcome, and evidence.**
