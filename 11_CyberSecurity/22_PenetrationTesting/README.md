# Phase 22 — Penetration Testing

Phase 22 is the first phase dedicated entirely to **structured penetration testing and application/identity attack-path validation**.

It builds on:

```text
Phase 20 — Cybersecurity Fundamentals
        ↓
Phase 21 — Network Security
        ↓
Phase 22 — Penetration Testing
```

Inside Phase 22, the dependency order is:

```text
89 Metasploit Essentials
        ↓
90 Ethical Hacking and Security Assessment
        ↓
91 Bug Hunting
        ↓
92 Web Application Penetration Testing
        ↓
93 Mobile Application Penetration Testing
        ↓
94 Active Directory Penetration Testing
```

---

# Phase Goal

By the end of Phase 22 you should be able to:

```text
Authorize
   ↓
Define Scope / RoE
   ↓
Map Attack Surface
   ↓
Enumerate Safely
   ↓
Analyze Weaknesses
   ↓
Validate Minimally
   ↓
Map Attack Paths
   ↓
Measure Detection
   ↓
Document Evidence
   ↓
Remediate
   ↓
Retest
```

The objective is **not maximum access**.

The objective is:

> Prove meaningful security conditions with the minimum authorized impact, then help close the path.

---

# Courses

| # | Course | Primary Focus |
|---|---|---|
| **89** | **Metasploit Essentials** | Framework workflow, modules, payloads, sessions, auxiliary scanners, minimal exploit validation, evidence, cleanup |
| **90** | **Ethical Hacking and Security Assessment** | End-to-end methodology across network, host, application, cloud, identity, containers, and reporting |
| **91** | **Bug Hunting** | Program policy, attack-surface mapping, web/API hypotheses, minimal proof, triage-quality reporting |
| **92** | **Web Application Penetration Testing** | Authentication, authorization, sessions, business logic, injection, SSRF, file handling, APIs, OAuth, GraphQL, WebSockets |
| **93** | **Mobile Application Penetration Testing** | Android/iOS static and dynamic analysis, local storage, IPC, deep links, WebViews, TLS, tokens, APIs |
| **94** | **Active Directory Penetration Testing** | AD identity graph, Kerberos/NTLM, groups, ACLs, GPOs, delegation, trusts, service accounts, privilege paths |

---

# Prerequisites

You should already know:

```text
Linux
Windows Server
Active Directory Administration
Networking
Firewalls
DNS
HTTP / HTTPS
REST APIs
Databases / SQL
Basic Python
Bash
PowerShell
Docker / Kubernetes fundamentals
Cloud fundamentals
```

Security dependencies:

```text
84 Security Assessment Fundamentals
85 Ethical Hacking Fundamentals
87 Network Security Assessment
88 Network Penetration Testing
```

---

# Mandatory Safety Model

All practical work must use:

```text
your own VMs
your own containers
your own mobile app/device/emulator
your own cloud lab
intentionally vulnerable training applications
disposable Active Directory labs
or explicit written authorization
```

Do not use:

```text
random public targets
third-party Wi-Fi
real employee credentials
out-of-scope company systems
unapproved SaaS or cloud tenants
real sensitive data for impact proof
unapproved pivoting
```

Use synthetic data whenever possible:

```text
test users
dummy passwords
marker files
fake customer records
test tenants
fake payment objects
test service accounts
```

---

# Recommended Phase 22 Lab Environment

```text
                         Security Workstation
                    Kali / Ubuntu / Windows
                              │
                     isolated virtual network
         ┌────────────────────┼────────────────────┐
         │                    │                    │
   Vulnerable Web        Mobile Lab          AD Lab Domain
   App / API             Emulator            ├─ DC
   ├─ Juice Shop         ├─ Android           ├─ Server
   ├─ WebGoat            └─ test app          └─ Workstation
   └─ custom API
         │
         └────────────── Logging / SIEM ──────────────┘
```

Take snapshots before:

```text
Metasploit exploitation
privilege-escalation labs
directory ACL changes
GPO changes
delegation labs
mobile runtime instrumentation
```

---

# Course 89 — Metasploit Essentials

Core workflow:

```text
msfconsole
   ↓
workspace
   ↓
hosts / services / evidence
   ↓
search
   ↓
info module
   ↓
verify target
   ↓
check if possible
   ↓
minimal validation
   ↓
session evidence
   ↓
cleanup
```

The framework should never replace understanding.

Before using a module, know:

```text
target product
target version/build
required configuration
authentication requirement
network reachability
side effects
payload architecture
expected output
rollback / recovery
```

---

# Course 90 — Ethical Hacking and Security Assessment

This course connects all testing domains into one methodology:

```text
Network
Host
Application
API
Cloud
Container
Kubernetes
Identity
```

A mature tester moves from:

```text
"scanner says vulnerable"
```

to:

```text
expected secure state
  ↓
observed evidence
  ↓
validated weakness
  ↓
real preconditions
  ↓
business impact
  ↓
remediation
  ↓
retest
```

---

# Course 91 — Bug Hunting

Before any bounty-style testing:

```text
READ THE PROGRAM POLICY
```

Then identify:

```text
in-scope assets
out-of-scope assets
allowed automation
rate limits
test-account rules
prohibited techniques
data-handling requirements
disclosure process
safe-harbor terms
```

Bug hunting mental model:

```text
Policy
  ↓
Map Application
  ↓
Create Role Matrix
  ↓
Form Hypothesis
  ↓
Change One Variable
  ↓
Minimal Proof
  ↓
Impact
  ↓
Report
```

---

# Course 92 — Web Application Penetration Testing

## Core Testing Matrix

```text
Authentication
Authorization
Session Management
Business Logic
Input Validation
Server-Side Requests
File Handling
Browser Security
API Security
SSO / OAuth
GraphQL
WebSocket
Caching
Logging
```

## Authorization Test Matrix

Example:

| Test | User A | User B | Admin |
|---|---:|---:|---:|
| Read A's profile | ✅ | ❌ | Policy-dependent |
| Edit A's profile | ✅ | ❌ | Policy-dependent |
| Delete account | Own only | Own only | Policy-dependent |
| Admin route | ❌ | ❌ | ✅ |

Use synthetic accounts and objects.

## Application Trust Model

```text
Browser / Mobile / User Input
          ↓ UNTRUSTED
Application Boundary
          ↓
Authentication
          ↓
Authorization
          ↓
Business Logic
          ↓
Database / Queue / Storage
```

Client-side validation is useful UX.

It is **not** a trusted authorization control.

---

# Course 93 — Mobile Application Penetration Testing

Treat the mobile client as user-controlled.

```text
Android / iOS App
    ↓
Local Storage
    ↓
Platform IPC / Deep Links
    ↓
TLS
    ↓
Backend API
    ↓
Trusted Authorization
```

## Android Review

```text
AndroidManifest.xml
permissions
exported components
intents
deep links
WebViews
network security config
local storage
logs
Keystore
debuggable flag
native libraries
```

## iOS Review

```text
Info.plist
entitlements
ATS
URL schemes
Universal Links
Keychain
file-protection classes
app groups
pasteboard
local files
networking
```

## Key Principle

A user can modify their own client.

Therefore:

```text
"button hidden"
"screen locked"
"Java/Kotlin check passed"
"Swift flag is false"
```

must never be the only mechanism protecting server-side data or privileges.

---

# Course 94 — Active Directory Penetration Testing

Think of Active Directory as a graph:

```text
Users
  ↓ member of
Groups
  ↓ rights over
Computers / Users / GPOs / OUs
  ↓ authenticate using
Kerberos / NTLM
  ↓ interact through
SMB / LDAP / WinRM / RDP
```

An AD pentest asks:

> Which combination of identities, permissions, sessions, delegation, host privilege, and trust relationships creates a path to higher privilege?

## Important AD Areas

```text
privileged groups
service accounts
SPNs
gMSA
LAPS
password policy
Kerberos
NTLM
SMB signing
LDAP signing
delegation
AD ACLs
GPO permissions
trusts
local admin rights
admin logon locations
directory replication rights
BloodHound-style relationship graphs
```

## AD Testing Boundary

Use:

```text
synthetic users
synthetic service accounts
intentionally weak ACLs
lab-only passwords
disposable domains
snapshots
```

Do not practice credential attacks or privilege-path validation against real employee accounts or production domains without explicit written authorization.

---

# Evidence Folder Structure

```text
Phase_22_Lab/
├── 89_Metasploit/
│   ├── scope/
│   ├── modules/
│   ├── console_logs/
│   ├── evidence/
│   └── cleanup/
├── 90_Assessment/
│   ├── roe/
│   ├── inventory/
│   ├── findings/
│   └── retest/
├── 91_Bug_Hunting/
│   ├── policy/
│   ├── recon/
│   ├── requests/
│   ├── reports/
│   └── retest/
├── 92_Web_Pentest/
│   ├── routes/
│   ├── role_matrix/
│   ├── burp/
│   ├── findings/
│   └── retest/
├── 93_Mobile_Pentest/
│   ├── static/
│   ├── dynamic/
│   ├── api/
│   ├── findings/
│   └── retest/
└── 94_AD_Pentest/
    ├── inventory/
    ├── powershell/
    ├── acl/
    ├── attack_paths/
    ├── detection/
    └── cleanup/
```

---

# Standard Finding Template

```text
Finding ID:
Title:
Scope:
Affected asset / component:
Test account / role:
Preconditions:
Expected security behavior:
Observed behavior:
Evidence:
Security impact:
Business impact:
Severity / priority:
Root cause:
Remediation:
Compensating control:
Owner:
Retest method:
Status:
```

---

# Phase 22 Combined Capstone

Create one integrated security lab:

```text
External/Test Network
       ↓
Firewall
       ↓
Web/API Application
       ↓
Windows / Linux Services
       ↓
AD Domain

Mobile Test App
       ↓
same API backend

Logging / SIEM
       ↑
Firewall + App + Windows + Identity + API
```

Deliver:

1. `Authorization.md`
2. `Rules_of_Engagement.md`
3. `Architecture.md`
4. `Asset_Inventory.csv`
5. `Role_Matrix.csv`
6. `Attack_Surface.md`
7. `Metasploit_Validation.md`
8. `Web_Pentest_Report.md`
9. `Mobile_Pentest_Report.md`
10. `AD_Privilege_Path.md`
11. `Detection_Validation.md`
12. `Findings_Register.csv`
13. `Remediation_Plan.md`
14. `Cleanup_Checklist.md`
15. `Retest_Report.md`
16. `Executive_Summary.md`

---

# What You Should Know Before Leaving Phase 22

## Metasploit

```text
workspace
modules
exploit
auxiliary
payload
post
options
RHOSTS
RPORT
check
sessions
jobs
handler
evidence
cleanup
```

## Assessment

```text
authorization
scope
RoE
attack surface
false positive
exploit preconditions
risk
finding
remediation
retest
```

## Bug Hunting / Web

```text
role matrix
BOLA / IDOR
function authorization
tenant isolation
session security
JWT
CSRF
SQLi
XSS
command injection
path traversal
SSRF
file upload
CORS
OAuth
GraphQL
WebSocket
business logic
race conditions
```

## Mobile

```text
APK / IPA
manifest / plist
permissions
exported components
deep links
WebViews
local storage
Keystore / Keychain
TLS
pinning
ADB
JADX
Frida awareness
backend API authorization
```

## Active Directory

```text
forest
domain
DC
Kerberos
NTLM
SPN
groups
service accounts
LAPS
gMSA
GPO
ACL / ACE
delegation
trusts
SMB / LDAP signing
BloodHound concepts
privilege paths
detection
```

---

# What Phase 22 Does Not Cover Deeply

Still later:

```text
advanced exploit development
binary exploitation
malware analysis
reverse engineering
red-team infrastructure
advanced evasion
stealth persistence
malware command-and-control
```

The later roadmap covers malware/reverse engineering, SOC, IR/forensics, cloud security, DevSecOps, and related specialties separately.

---

# Transition to Phase 23

Next:

# Phase 23 — Application Security

```text
95. Application Security
96. Web Application Security
97. API Security
```

The transition is deliberate:

```text
Phase 22
"How can the application be broken?"
      ↓
Phase 23
"How should we design, build, test, and operate it securely?"
```

---

# Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 89 — Metasploit Essentials | 105 | 70 | 105 | 9,268 |
| 90 — Ethical Hacking and Security Assessment | 80 | 70 | 80 | 8,405 |
| 91 — Bug Hunting | 116 | 70 | 116 | 10,285 |
| 92 — Web Application Penetration Testing | 129 | 70 | 129 | 10,825 |
| 93 — Mobile Application Penetration Testing | 109 | 70 | 109 | 9,522 |
| 94 — Active Directory Penetration Testing | 140 | 70 | 140 | 10,842 |
| **Total** | **679** | **420** | **679** | **59,147** |

---

# Completion Criteria

Phase 22 is complete when you can:

- define authorization and scope before testing;
- build an attack-surface and role matrix;
- use Metasploit only after validating module preconditions;
- perform minimal proof rather than unnecessary post-exploitation;
- assess web authentication, authorization, business logic, injection, API, and browser controls;
- statically and dynamically assess an owned mobile application;
- explain why backend authorization cannot trust the mobile client;
- inventory an AD domain and reason about privilege relationships;
- identify a synthetic AD privilege path and validate it safely;
- correlate application/mobile/AD test behavior with defensive telemetry;
- write reproducible findings;
- clean up;
- remediate;
- retest.

---

# Final Mental Model

```text
                 PENETRATION TESTING
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
   DISCOVER            VALIDATE           IMPROVE
      │                  │                  │
 Recon / Map        Minimal Proof       Remediation
 Enumerate          Attack Path         Detection
 Research           Impact              Retest
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ↓
                   EVIDENCE + ETHICS
```

**Phase 22 is complete when you can think like an attacker while behaving like a responsible security engineer.**
