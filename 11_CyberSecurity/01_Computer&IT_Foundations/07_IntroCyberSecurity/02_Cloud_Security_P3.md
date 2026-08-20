# Cloud Security — Deep Learning Material

> **Verified:** 2026-08-12  
> **Focus:** Cloud-security architecture, shared responsibility, current cloud-security concerns, CIS Benchmarks, cloud-security platforms/tools, operational priorities for security teams, regional Middle East cloud adoption, and hands-on learning.

---

# Table of Contents

1. [Computer Science vs Computer Engineering](#1-computer-science-vs-computer-engineering)
2. [Solution Architect Role](#2-solution-architect-role)
3. [Introduction to Security in the Cloud](#3-introduction-to-security-in-the-cloud)
4. [Shared Responsibility Model](#4-shared-responsibility-model)
5. [How Responsibility Changes by Service Model](#5-how-responsibility-changes-by-service-model)
6. [AWS Example — EC2 vs RDS vs S3](#6-aws-example--ec2-vs-rds-vs-s3)
7. [Cloud Security Principles](#7-cloud-security-principles)
8. [Top Security Concerns in Cloud Environments](#8-top-security-concerns-in-cloud-environments)
9. [Zero Trust and Assume Breach](#9-zero-trust-and-assume-breach)
10. [What You Must Know You Own](#10-what-you-must-know-you-own)
11. [Top Places Security Teams Should Spend Time](#11-top-places-security-teams-should-spend-time)
12. [CIS Benchmarks Explained](#12-cis-benchmarks-explained)
13. [Security Tools in the Cloud — Category Map](#13-security-tools-in-the-cloud--category-map)
14. [CNAPP](#14-cnapp)
15. [CSPM](#15-cspm)
16. [CWPP](#16-cwpp)
17. [CASB](#17-casb)
18. [DSPM](#18-dspm)
19. [CIEM](#19-ciem)
20. [Other Important Cloud Security Categories](#20-other-important-cloud-security-categories)
21. [In-Depth — Prowler](#21-in-depth--prowler)
22. [In-Depth — ScoutSuite](#22-in-depth--scoutsuite)
23. [In-Depth — CloudSploit](#23-in-depth--cloudsploit)
24. [In-Depth — AWS Trusted Advisor](#24-in-depth--aws-trusted-advisor)
25. [In-Depth — AWS Security Hub CSPM](#25-in-depth--aws-security-hub-cspm)
26. [Other Important AWS Security Services](#26-other-important-aws-security-services)
27. [In-Depth — Google Security Command Center](#27-in-depth--google-security-command-center)
28. [Other Important Google Cloud Security Services](#28-other-important-google-cloud-security-services)
29. [In-Depth — Microsoft Secure Score](#29-in-depth--microsoft-secure-score)
30. [In-Depth — Microsoft Defender for Cloud](#30-in-depth--microsoft-defender-for-cloud)
31. [In-Depth — Microsoft Defender for Cloud Apps](#31-in-depth--microsoft-defender-for-cloud-apps)
32. [Microsoft Entra Permissions Management — Historical Note](#32-microsoft-entra-permissions-management--historical-note)
33. [Cloud Security Tool Comparison](#33-cloud-security-tool-comparison)
34. [Cloud Security Architecture Example](#34-cloud-security-architecture-example)
35. [Cloud Security Predictions and 2026 Directional Trends](#35-cloud-security-predictions-and-2026-directional-trends)
36. [Cloud Adoption in the Middle East](#36-cloud-adoption-in-the-middle-east)
37. [Cloud Security in the Middle East](#37-cloud-security-in-the-middle-east)
38. [Cloud Security Engineer Responsibilities](#38-cloud-security-engineer-responsibilities)
39. [Cloud Security Learning Roadmap](#39-cloud-security-learning-roadmap)
40. [Hands-On Lab Roadmap](#40-hands-on-lab-roadmap)
41. [Interview and Exam Review Questions](#41-interview-and-exam-review-questions)
42. [Final Review Sheet](#42-final-review-sheet)
43. [Official Resources](#43-official-resources)

---


# 1. Computer Science vs Computer Engineering

Cloud security is not isolated from the rest of computing. It depends heavily on operating systems, networking, software, identity, distributed systems, cryptography, and infrastructure.

## 1.1 Computer Science

**Computer Science — CS** focuses mainly on software, computation, algorithms, data, abstractions, and information systems.

Typical areas:

```text
Programming
Algorithms
Data Structures
Operating Systems
Databases
Networking
Distributed Systems
Artificial Intelligence
Software Engineering
Cryptography
Web Systems
Cloud Computing
```

For cybersecurity, CS is particularly relevant to:

- Application Security
- Cloud Security
- Security Automation
- Detection Engineering
- Malware Analysis
- Secure Software Development
- AI Security
- Cryptography
- Security Engineering

Example:

```text
Cloud Security Engineer
        ↓
Needs:
APIs
Operating Systems
Networking
Databases
Identity
Automation
Distributed Systems
```

## 1.2 Computer Engineering

**Computer Engineering — CE** bridges electrical engineering and computer science.

Typical areas:

```text
Computer Architecture
Processors
Digital Logic
Embedded Systems
Firmware
Hardware
Memory
Microcontrollers
Low-Level Programming
Electronics
```

It becomes especially important for:

- IoT Security
- Embedded Security
- Firmware Security
- Hardware Security
- Secure Boot
- Trusted Platform Modules
- Industrial / OT Security
- Edge Security

## 1.3 Comparison

| Area | Computer Science | Computer Engineering |
|---|---|---|
| Main focus | Software and computation | Hardware/software integration |
| Algorithms | Core | Important |
| Programming | Core | Important |
| Electronics | Limited | Core |
| Operating systems | Important | Important |
| Networking | Important | Important |
| Cloud computing | Strong relevance | Moderate relevance |
| Cloud security | Strong relevance | Useful for infrastructure/edge context |
| IoT/firmware security | Useful | Strong relevance |

## 1.4 Best Foundation for Cloud Security

A strong cloud-security foundation is:

```text
Computer Science
+
Networking
+
System Administration
+
Cloud Engineering
+
Cybersecurity
+
Automation
```

---

# 2. Solution Architect Role

A **Cloud Solution Architect** converts business requirements into a technical architecture.

Main question:

> How should cloud components be designed to satisfy functional, security, reliability, performance, compliance, and cost requirements?

## 2.1 Typical Responsibilities

A solution architect works on:

- Requirements analysis
- Architecture design
- Cloud-service selection
- Identity architecture
- Network topology
- Application architecture
- Data architecture
- Security architecture
- Availability and disaster recovery
- Performance
- Scalability
- Cost optimization
- Compliance
- Migration strategy
- Integration design
- Technical trade-offs

## 2.2 Architect vs Engineer vs Security Engineer

### Solution Architect

```text
WHAT should the architecture look like?
WHY should particular services be selected?
HOW should major components interact?
```

### Cloud Engineer

```text
HOW do we build and operate it?
```

### Cloud Security Engineer

```text
HOW do we secure it?
HOW do we continuously validate it?
HOW do we detect attacks?
HOW do we reduce blast radius?
```

## 2.3 Example

```text
                 Internet
                    ↓
                  CDN
                    ↓
                  WAF
                    ↓
             Load Balancer
                    ↓
             Application Tier
              /           \
             /             \
       Containers       Serverless
             \             /
              \           /
                Database
                    ↓
                  Storage
```

Cross-cutting architecture:

```text
Identity → IAM / SSO / MFA
Secrets  → Secrets Manager / Key Vault
Keys     → KMS / HSM
Logs     → Central Logging / SIEM
Network  → Segmentation / Private Endpoints
Security → CSPM / CWPP / Detection
Backup   → Backup / Replication / DR
```

## 2.4 Security Must Start at Architecture

Weak process:

```text
Build System
   ↓
Deploy
   ↓
Ask Security Team to "secure it"
```

Better process:

```text
Business Requirements
        ↓
Architecture
        ↓
Threat Modeling
        ↓
Security Requirements
        ↓
Secure Design
        ↓
Implementation
        ↓
Continuous Validation
```

---

# 3. Introduction to Security in the Cloud

**Cloud Security** is the combination of technologies, architectures, controls, processes, governance, and operational practices used to protect cloud environments.

It protects:

```text
Cloud Data
Cloud Identities
Cloud Applications
Cloud Workloads
Cloud Networks
Cloud Infrastructure
Cloud APIs
Cloud Configuration
Cloud Logs
Cloud Supply Chain
```

Cloud security is not:

> "AWS / Azure / Google secures everything for me."

It is:

> **A shared security relationship between the cloud provider and the customer.**

## 3.1 Why Cloud Security Is Different

On-premises:

```text
Organization manages:
Facilities
Servers
Storage
Network
Virtualization
Operating Systems
Applications
Data
Identity
```

Cloud:

```text
Some layers → CSP manages
Other layers → Customer manages
```

The exact boundary depends on the service.

## 3.2 Major Cloud Security Domains

```text
Identity
Data
Applications
Endpoints
Workloads
Network
Infrastructure
Configuration
Logging
Compliance
DevSecOps
Incident Response
Business Continuity
AI / Agent Security
```

---

# 4. Shared Responsibility Model

The **Shared Responsibility Model** defines which security activities belong to the cloud service provider and which remain the customer's responsibility.

AWS summarizes it as:

```text
AWS
→ Security OF the cloud

Customer
→ Security IN the cloud
```

Microsoft uses the same principle and explicitly shows that responsibility changes across SaaS, PaaS, IaaS, and on-premises.

Google Cloud also documents shared responsibility and extends the concept through its **shared fate** approach, where Google provides additional guidance, secure defaults, and security capabilities to help customers achieve secure outcomes.

## 4.1 CSP Responsibility

The provider generally secures the underlying cloud infrastructure.

Typical examples:

```text
Physical Datacenters
Physical Servers
Storage Hardware
Core Networking
Hypervisor / Virtualization
Underlying Managed-Service Infrastructure
```

## 4.2 Customer Responsibility

The customer retains responsibility for major areas such as:

```text
Customer Data
Identity
Access Decisions
User Accounts
Resource Configuration
Application Security
Data Classification
Compliance Decisions
Business Logic
```

## 4.3 Key Rule

As a service becomes more managed:

```text
More CSP Management
        ↓
Less Customer Infrastructure Management
```

But customers still control critical business/security decisions such as:

```text
Who can access?
What data is stored?
Should it be public?
Which keys are used?
Which logs are retained?
Which policies apply?
```

---

# 5. How Responsibility Changes by Service Model

## 5.1 On-Premises

Customer manages nearly everything:

```text
Applications
Data
Runtime
Middleware
Operating System
Virtualization
Servers
Storage
Networking
Facilities
```

## 5.2 IaaS

Examples:

```text
AWS EC2
Azure Virtual Machines
Google Compute Engine
```

Provider typically manages:

```text
Facilities
Physical Network
Physical Servers
Storage Hardware
Virtualization
```

Customer typically manages:

```text
Guest OS
Guest OS Patching
Applications
Data
IAM
Host Firewall
Network Security Configuration
Secrets
Monitoring
```

## 5.3 PaaS / Managed Platform

Examples:

```text
Managed Databases
Managed App Platforms
Managed Messaging
Managed Kubernetes Control Planes
```

Provider manages more of the platform.

Customer focuses more on:

```text
Data
Identity
Application Logic
Configuration
Network Exposure
Permissions
Secrets
Database Users
```

## 5.4 SaaS

Examples:

```text
Microsoft 365
Google Workspace
Salesforce
```

Provider manages most of the application stack.

Customer still manages:

```text
Users
Authentication Policies
Sharing
Data
Configuration
Endpoints
Data Governance
Compliance Decisions
```

---

# 6. AWS Example — EC2 vs RDS vs S3

The training slide correctly illustrates that the responsibility boundary moves as the service becomes more abstracted.

```text
EC2
↓
Highly Customizable
High Customer Responsibility

RDS
↓
More Managed

S3
↓
Highly Abstracted
Lower Infrastructure Responsibility
```

## 6.1 Amazon EC2

AWS generally handles:

```text
Physical Facility
Physical Server
Core Networking
Hypervisor
```

Customer handles:

```text
Guest OS
OS Patching
Applications
Libraries
Data
IAM
Security Groups
Host Firewall
Secrets
Logging
EDR
Application Security
```

Example:

```text
Ubuntu runs on EC2
      ↓
AWS secures physical infrastructure
      ↓
Customer patches Ubuntu
```

## 6.2 Amazon RDS

AWS manages more of the database platform.

Customer still manages:

```text
Database Users
Database Permissions
Data
Schema
Queries
Application Security
Security Groups
Network Exposure
Encryption Settings
Credentials
Logging Choices
```

## 6.3 Amazon S3

AWS manages the underlying storage service and infrastructure.

Customer controls:

```text
Bucket Policy
IAM
Public Access
Data
Classification
KMS Strategy
Lifecycle
Replication
Logging
Application Access
```

Important:

> Even when the provider enables secure defaults, the customer is still responsible for data access, classification, policy, and business use.

---

# 7. Cloud Security Principles

## 7.1 Least Privilege

Grant only the permissions needed.

Bad:

```text
Developer
→ Administrator
```

Better:

```text
Developer
→ Read Development Logs
→ Deploy to Dev Environment
→ No Production Admin
```

## 7.2 Defense in Depth

```text
Identity
   ↓
Network
   ↓
Application
   ↓
Workload
   ↓
Data Encryption
   ↓
Detection
   ↓
Backups
```

## 7.3 Zero Trust

Do not trust because something is "inside" the network.

```text
Verify Explicitly
Use Least Privilege
Assume Breach
```

## 7.4 Secure by Default

Good defaults:

```text
Private by default
MFA for privileged users
Logging enabled
Encryption enabled
No public admin interfaces
Minimum permissions
```

## 7.5 Automation

Cloud changes too quickly for manual-only security.

Use:

```text
Infrastructure as Code
Policy as Code
Automated Security Checks
Automated Remediation
CI/CD Security Gates
Continuous Monitoring
```

---

# 8. Top Security Concerns in Cloud Environments

Major cloud-security concerns include:

1. Identity compromise
2. Excessive permissions
3. Misconfiguration
4. Public exposure
5. Data leakage
6. Secrets exposure
7. Insecure APIs
8. Weak network segmentation
9. Vulnerable workloads
10. Supply-chain compromise
11. Logging gaps
12. Asset-visibility gaps
13. Insecure CI/CD
14. Compliance/data-residency failures
15. Weak backup/recovery
16. Shadow IT
17. AI/agent security risks

## 8.1 Identity Compromise

Cloud control planes are API-driven.

```text
Attacker
   ↓
Valid Credentials
   ↓
Cloud API
   ↓
Create Resource
Change IAM
Read Data
Disable Logs
```

This is why identity is a primary cloud security perimeter.

## 8.2 Excessive Permissions

```text
Application needs:
Read one bucket

Actual access:
Administrator
```

This creates unnecessary blast radius.

## 8.3 Misconfiguration

Examples:

```text
Public Storage
Open Database
0.0.0.0/0 on Admin Port
Disabled Logging
No MFA
Unencrypted Sensitive Data
Over-Permissive IAM
```

## 8.4 Public Exposure

Examples:

```text
SSH exposed to Internet
RDP exposed to Internet
Database publicly reachable
Object storage publicly readable
Admin API public
```

## 8.5 Hard-Coded Secrets

Bad:

```python
API_KEY = "secret"
DATABASE_PASSWORD = "password123"
```

Better:

```text
Workload Identity
or
Secrets Manager / Key Vault / Secret Manager
```

## 8.6 Long-Lived Keys

Modern cloud design should prefer:

```text
Federation
IAM Roles
Managed Identity
Workload Identity
Temporary Credentials
```

over:

```text
Permanent Access Keys
```

If long-lived credentials remain unavoidable:

```text
Scope them
Monitor them
Protect them
Rotate them
Remove unused keys
```

## 8.7 Lack of Visibility

A foundational principle:

> **You cannot protect what you do not know exists.**

Security teams need inventories for:

```text
Identities
Endpoints
Apps
Infrastructure
Network
Data
```

---

# 9. Zero Trust and Assume Breach

NIST Zero Trust architecture rejects implicit trust based solely on network location or asset ownership.

A useful operational model is:

```text
Verify Explicitly
Use Least Privilege
Assume Breach
```

## 9.1 Verify Explicitly

Evaluate:

```text
Identity
Device
Location
Risk
Resource
Application
Session
Behavior
```

## 9.2 Use Least Privilege

Limit:

```text
Who
Can do what
To which resource
For how long
Under which conditions
```

## 9.3 Assume Breach

Design as if an attacker may already have some access.

Therefore:

```text
Segment
Monitor
Encrypt
Protect Logs
Limit Privileges
Use Strong Identity
Detect Lateral Movement
Reduce Blast Radius
```

---

# 10. What You Must Know You Own

The supplied material highlights six major inventory areas:

```text
Identities
Endpoints
Apps
Infrastructure
Network
Data
```

## 10.1 Identities

Examples:

```text
Employees
Admins
Service Accounts
Applications
Workloads
API Clients
AI Agents
```

Questions:

- Is the identity still needed?
- What permissions does it have?
- Is MFA required?
- Are credentials temporary?
- Can it escalate privileges?
- What data can it reach?

## 10.2 Endpoints

Examples:

```text
Laptops
Phones
Admin Workstations
Developer Machines
Jump Hosts
```

## 10.3 Applications

Examples:

```text
Web Apps
APIs
Microservices
SaaS
Serverless
AI Applications
```

## 10.4 Infrastructure

Examples:

```text
VMs
Containers
Kubernetes
Databases
Storage
Serverless
Cloud Accounts
Subscriptions
Projects
```

## 10.5 Network

Examples:

```text
VPC / VNet
Subnets
Routes
Security Groups
Firewalls
VPN
Peering
Private Endpoints
DNS
Load Balancers
```

## 10.6 Data

Know:

```text
Where it is
What it contains
Who can access it
Whether it is sensitive
Whether it is encrypted
Where backups exist
Where replicas exist
```

---

# 11. Top Places Security Teams Should Spend Time

This section incorporates the additional training slide.

The slide lists:

```text
1. Account contact info
2. Use MFA / Passkey Authentication
3. No hard-coding secrets
4. Rotate your keys
5. Limit security groups
6. Centralize audit & activity logs
7. Use least privilege
8. Take action on security findings
9. Automation
10. Scale and move faster
```

Below is the deeper, modern interpretation.

## 11.1 Keep Account Security Contact Information Current

Cloud providers may need to contact the organization because of:

```text
Abuse
Security Incident
Account Compromise
Billing Problem
Service Event
Compliance Issue
```

Maintain:

```text
Security Contact
Operations Contact
Billing Contact
Escalation Contact
Recovery Contact
```

Do not route critical security messages only to an employee who may leave the company.

Better:

```text
security@company
cloud-ops@company
+
On-call escalation
```

## 11.2 Use Passkeys / Phishing-Resistant MFA

The slide crosses out "MFA" and emphasizes **Passkey Auth**.

The deeper lesson is:

> Use strong, phishing-resistant authentication for privileged access.

Prefer:

```text
Passkeys
FIDO2 Security Keys
Platform Authenticators
Certificate-Based Authentication
```

over weaker factors where possible.

Priority accounts:

```text
AWS Root
Azure / Entra Global Admin
GCP Organization Admin
Security Admin
Billing Admin
Break-Glass Accounts
Cloud Platform Admin
```

## 11.3 Never Hard-Code Secrets

Do not put credentials in:

```text
Source Code
Git Repository
Dockerfile
Terraform File
CI/CD YAML
Container Image
Notebook
Shell History
```

Use:

```text
AWS Secrets Manager
Azure Key Vault
Google Secret Manager
Vault
Workload Identity
Managed Identity
IAM Roles
```

## 11.4 Rotate Keys — But Prefer Eliminating Long-Lived Keys

The slide says:

> Rotate your keys.

This is valid, but modern design goes further.

Best hierarchy:

```text
1. Avoid static credentials
2. Use workload identity / federation
3. Use temporary credentials
4. If static keys remain, rotate and monitor them
```

So:

```text
Temporary Credential
        >
Frequently Rotated Permanent Credential
        >
Never-Rotated Permanent Credential
```

## 11.5 Limit Security Groups

Security groups/firewall policies control network exposure.

Avoid:

```text
0.0.0.0/0 → SSH 22
0.0.0.0/0 → RDP 3389
0.0.0.0/0 → Database Port
```

Prefer:

```text
Private Endpoint
Bastion
VPN
Zero Trust Access
Specific Source CIDR
Application-to-Application Rules
```

Also remove unused rules.

## 11.6 Centralize Audit and Activity Logs

This item from the new slide is critical.

Logs should answer:

```text
Who?
Did what?
When?
From where?
To which resource?
Was it allowed?
What changed?
```

Centralize:

```text
AWS CloudTrail
Azure Activity Logs
Entra Sign-in / Audit Logs
Google Cloud Audit Logs
Kubernetes Audit Logs
Application Logs
WAF Logs
Firewall Logs
Identity Logs
```

Recommended architecture:

```text
Cloud Accounts / Projects / Subscriptions
              ↓
        Central Log Pipeline
              ↓
        Protected Log Storage
              ↓
             SIEM
              ↓
     Detection / Investigation
```

Security properties of the logging platform:

```text
Restricted Write/Delete Access
Retention
Time Synchronization
Integrity Protection
Separation of Duties
Alerting on Logging Changes
```

## 11.7 Use Least Privilege

Review:

```text
Unused Users
Unused Roles
Unused Policies
Unused Permissions
Privilege Escalation Paths
Cross-Account Trust
Service Accounts
Machine Identities
```

Least privilege should apply to:

```text
Humans
Applications
CI/CD
Containers
Serverless
AI Agents
Third Parties
```

## 11.8 Take Action on Security Findings

A scanner that produces findings without remediation does not reduce risk.

Weak model:

```text
Scanner
   ↓
20,000 Findings
   ↓
Dashboard
   ↓
Nothing
```

Mature model:

```text
Finding
   ↓
Context
   ↓
Risk Prioritization
   ↓
Owner
   ↓
Due Date / SLA
   ↓
Remediation
   ↓
Verification
```

Prioritization can include:

```text
Severity
Exploitability
Internet Exposure
Identity Privilege
Data Sensitivity
Asset Criticality
Attack Path
Known Exploitation
Business Context
```

## 11.9 Automation

Automate repeatable controls.

Examples:

```text
IaC Scanning
Policy Enforcement
Secret Scanning
Container Scanning
Security Baseline Deployment
Remediation
Log Routing
Account Provisioning
Tag Enforcement
Finding Enrichment
```

Cloud security should increasingly be:

```text
API-Driven
Policy-Driven
Code-Driven
Continuous
```

## 11.10 Scale and Move Faster

Security should enable the business to move faster **safely**, not create a manual approval bottleneck.

Build reusable guardrails:

```text
Secure Landing Zones
Approved Terraform Modules
Policy as Code
Golden Images
Secure CI/CD Templates
Central Identity
Central Logging
Default Encryption
Private Networking Patterns
```

This changes security from:

```text
Ticket-by-Ticket Review
```

to:

```text
Secure Platform
       ↓
Developers inherit guardrails
       ↓
Safe self-service
```

---

# 12. CIS Benchmarks Explained

**CIS Benchmarks** are consensus-based secure-configuration recommendations maintained by the Center for Internet Security.

They are prescriptive hardening guides.

Examples exist for:

```text
AWS
Microsoft Azure
Google Cloud
Kubernetes
Linux
Windows
Databases
Network Devices
Applications
```

## 12.1 What They Answer

A vulnerability scanner asks:

> Is this software vulnerable?

A CIS Benchmark asks:

> Is this technology configured securely?

Example recommendations may include:

```text
Enable MFA
Enable Audit Logging
Disable Public Access
Restrict Administrative Ports
Configure Encryption
Apply Strong Password Policy
```

## 12.2 CIS Foundations Benchmarks

Cloud Foundations Benchmarks provide account-level configuration guidance for public cloud.

Common areas include:

```text
IAM
Logging
Monitoring
Networking
Storage
Security Configuration
```

## 12.3 Level 1 vs Level 2

Many Benchmarks define profiles such as:

### Level 1

Practical security improvements designed to have limited operational impact.

### Level 2

More restrictive security controls that may require greater operational consideration.

Always read the exact benchmark version and rationale.

## 12.4 Workflow

```text
Cloud Environment
       ↓
Benchmark Controls
       ↓
Automated Assessment
       ↓
Pass / Fail
       ↓
Finding
       ↓
Remediation
       ↓
Continuous Reassessment
```

---

# 13. Security Tools in the Cloud — Category Map

The training slide lists six major categories:

```text
CNAPP
CSPM
CWPP
CASB
DSPM
CIEM
```

A useful mental model:

```text
                    CLOUD SECURITY
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
      Posture          Workload            Data
        │                 │                 │
       CSPM              CWPP              DSPM
        │                 │                 │
        └────────────┬────┴────┬────────────┘
                     │         │
                   CNAPP      CIEM
                     │
                  DevSecOps

SaaS / Cloud App Layer:
CASB / SSPM
```

---

# 14. CNAPP

**CNAPP = Cloud-Native Application Protection Platform**

CNAPP unifies multiple cloud-security capabilities across the cloud application lifecycle.

Typical capabilities:

```text
CSPM
CWPP
DevSecOps Security
IaC Scanning
Container Security
Kubernetes Security
Attack Paths
Vulnerability Management
Entitlement Analysis
Runtime Protection
Cloud Inventory
```

## Why CNAPP Exists

Old model:

```text
Tool A → CSPM
Tool B → Containers
Tool C → Vulnerability
Tool D → Entitlements
Tool E → IaC
```

Modern goal:

```text
Code
 ↓
CI/CD
 ↓
Cloud Configuration
 ↓
Workload
 ↓
Runtime
 ↓
Unified Risk Context
```

Microsoft officially describes **Defender for Cloud** as a CNAPP with major components including CSPM, DevSecOps, and CWPP.

---

# 15. CSPM

**CSPM = Cloud Security Posture Management**

Main question:

> Is my cloud environment configured securely?

Typical checks:

```text
Public Storage
Open Security Group
Missing MFA
Unencrypted Resource
Logging Disabled
Over-Permissive IAM
Public Database
Weak Security Configuration
```

Workflow:

```text
Cloud APIs
    ↓
Read Configuration
    ↓
Evaluate Policies
    ↓
Find Misconfiguration
    ↓
Prioritize
    ↓
Remediate
```

---

# 16. CWPP

**CWPP = Cloud Workload Protection Platform**

Main question:

> Are my running workloads protected?

Workloads may include:

```text
Virtual Machines
Containers
Kubernetes
Databases
Storage Workloads
Serverless
```

Capabilities:

```text
Runtime Threat Detection
Malware Detection
Vulnerability Assessment
Container Runtime Security
Host Protection
Behavior Analytics
Workload Hardening
```

### CSPM vs CWPP

```text
CSPM
→ Configuration/Posture

CWPP
→ Running Workload/Runtime
```

---

# 17. CASB

**CASB = Cloud Access Security Broker**

CASB focuses on cloud/SaaS usage and data movement.

Main questions:

```text
Which SaaS apps are users using?
Are they approved?
What data moves into them?
Are sessions risky?
Are OAuth apps dangerous?
```

Use cases:

```text
Shadow IT Discovery
SaaS Visibility
Session Control
Data Protection
Risky App Detection
OAuth App Governance
Threat Detection
```

Microsoft officially describes **Defender for Cloud Apps** as a CASB.

---

# 18. DSPM

**DSPM = Data Security Posture Management**

Main question:

> Where is sensitive data, who can access it, and what exposes it?

Capabilities:

```text
Data Discovery
Classification
Sensitivity Identification
Access Risk
Exposure Detection
Data Movement
Data Exfiltration Risk
AI Data Risk
```

Example:

```text
Storage Account
      ↓
Contains National IDs
      ↓
Public Access Enabled
      ↓
Critical Data Security Finding
```

---

# 19. CIEM

**CIEM = Cloud Infrastructure Entitlement Management**

Main question:

> Who can do what to which cloud resource?

Cloud permissions become complicated because of:

```text
Users
Groups
Roles
Policies
Resource Policies
Inherited Permissions
Service Accounts
Workload Identities
Cross-Account Trust
```

## 19.1 Permission Creep

```text
Developer
   ↓
Gets Dev Permissions
   ↓
Moves to DevOps
   ↓
Gets More Permissions
   ↓
Old Permissions Remain
   ↓
Permission Creep
```

## 19.2 CIEM Capabilities

```text
Effective Permission Analysis
Unused Permission Detection
Privilege Escalation Analysis
Entitlement Inventory
Least Privilege Recommendations
Identity-to-Resource Mapping
```

---

# 20. Other Important Cloud Security Categories

## SSPM

**SaaS Security Posture Management**

Focus:

```text
SaaS Configuration
Admin Settings
Sharing
Authentication
Security Baselines
```

## KSPM

**Kubernetes Security Posture Management**

Focus:

```text
RBAC
Pod Security
NetworkPolicy
Cluster Hardening
Secrets
Admission Controls
```

## IaC Security

Scans:

```text
Terraform
CloudFormation
Bicep
Kubernetes YAML
```

before deployment.

## SAST

Static analysis of source code.

## SCA

Software composition analysis for dependencies, licenses, and known vulnerabilities.

## SIEM

Central security event collection and analytics.

## SOAR

Security orchestration, automation, and response.

---

# 21. In-Depth — Prowler

**Prowler** is an open-source cloud-security platform that automates security and compliance assessments across cloud environments.

Official project:

```text
github.com/prowler-cloud/prowler
```

## 21.1 Main Use Cases

```text
Cloud Posture Assessment
Compliance Checks
Security Best Practices
Configuration Review
Reporting
Continuous Audit
```

## 21.2 Workflow

```text
Prowler
   ↓
Cloud APIs
   ↓
Read Cloud Configuration
   ↓
Run Security Checks
   ↓
Map Findings to Frameworks
   ↓
Report / Dashboard
```

## 21.3 Security Consideration

Run scanners using dedicated audit permissions.

Preferred:

```text
Dedicated Read-Only / Audit Role
        ↓
Temporary Credential
        ↓
Prowler
```

Avoid unnecessary administrative permissions.

## 21.4 DevSecOps Use

```text
Cloud Environment
      ↓
Scheduled Prowler Scan
      ↓
Findings
      ↓
Ticket / Dashboard
      ↓
Remediation
```

---

# 22. In-Depth — ScoutSuite

**ScoutSuite** is an open-source multi-cloud security auditing tool maintained by NCC Group.

Official project:

```text
github.com/nccgroup/ScoutSuite
```

It gathers configuration data using cloud-provider APIs and produces a consolidated view of security posture and risk areas.

## Workflow

```text
Cloud APIs
    ↓
Configuration Collection
    ↓
Security Analysis
    ↓
HTML Report
    ↓
Human Validation
```

Typical use:

```text
Security Auditor
     ↓
Assume Read-Only Role
     ↓
Run ScoutSuite
     ↓
Review Findings
     ↓
Validate
```

---

# 23. In-Depth — CloudSploit

**CloudSploit by Aqua** is an open-source project for detecting potential cloud misconfigurations and security risks.

Official project:

```text
github.com/aquasecurity/cloudsploit
```

The project documents support for major environments including AWS, Azure, GCP, OCI, and GitHub-related checks.

Workflow:

```text
Cloud Account
     ↓
CloudSploit
     ↓
Configuration Checks
     ↓
Potential Security Risk
     ↓
Report
```

Typical findings:

```text
Public Storage
Weak IAM
Missing Encryption
Open Network Rules
Logging Gaps
```

### Important

Open-source scanners should be validated for:

```text
Maintenance
Cloud API Coverage
False Positives
Dependency Security
Required Permissions
Version Compatibility
```

---

# 24. In-Depth — AWS Trusted Advisor

**AWS Trusted Advisor** inspects AWS environments and provides best-practice recommendations.

Current categories include:

```text
Cost Optimization
Performance
Security
Fault Tolerance
Service Limits
Operational Excellence
```

Security examples can include checks for:

```text
MFA on Root
S3 Bucket Permissions
Public Snapshots
Unrestricted Security Groups
```

Availability of some checks depends on support plan.

### Trusted Advisor vs Security Hub CSPM

```text
Trusted Advisor
→ Broad best-practice advisor

Security Hub CSPM
→ Dedicated security posture, standards, findings
```

---

# 25. In-Depth — AWS Security Hub CSPM

AWS currently documents **AWS Security Hub CSPM** as a cloud security posture management capability that provides a comprehensive view of AWS security state and evaluates environments against security standards and best practices.

Workflow:

```text
AWS Accounts
    ↓
Security Hub CSPM
    ↓
Controls / Findings
    ↓
Security Standards
    ↓
Security Posture
    ↓
Prioritization
```

It can integrate findings from AWS services and supported third-party products.

## Security Standards

Security Hub CSPM supports multiple standards and control sets. These can include AWS foundational best practices and industry frameworks.

Always verify the exact current versions in AWS documentation.

## Security Score

A posture score is useful for tracking control implementation.

But:

> A high score does not prove the environment cannot be breached.

The score may not capture:

```text
Business Logic Vulnerability
Unknown Asset
Stolen Credential
Zero-Day
Application Design Flaw
```

---

# 26. Other Important AWS Security Services

## Amazon GuardDuty

Threat detection for supported AWS data sources and workloads.

Think:

```text
API Activity
Network Activity
Workload Signals
Threat Intelligence
     ↓
GuardDuty
     ↓
Finding
```

## Amazon Inspector

Vulnerability-management capabilities for supported AWS workloads.

## AWS Config

Tracks resource configuration and can evaluate resources against configuration rules.

## IAM Access Analyzer

Helps identify external access and analyze permissions.

## Amazon Macie

Sensitive-data discovery/protection capabilities for Amazon S3.

## AWS CloudTrail

Audit trail for AWS API activity.

Important questions:

```text
Who called the API?
Which API?
When?
From where?
Which resource?
What changed?
```

---

# 27. In-Depth — Google Security Command Center

**Google Security Command Center — SCC** is Google Cloud's centralized security and risk-management service.

Google documents capabilities including:

```text
Asset Discovery
Security Posture
Misconfiguration Detection
Vulnerability Findings
Threat Detection
Risk Management
```

## 27.1 Threat Detection

Google documents multiple detection layers:

```text
Log-Based
Agentless
Runtime
```

## 27.2 Posture

Conceptually:

```text
Desired Security Baseline
       ↓
Actual Environment
       ↓
Compare
       ↓
Drift / Finding
```

## 27.3 Workflow

```text
GCP Organization
      ↓
Assets
      ↓
Security Command Center
      ↓
Findings
      ↓
Risk / Threat Context
      ↓
Security Team
```

---

# 28. Other Important Google Cloud Security Services

Examples:

```text
Cloud Audit Logs
Cloud Logging
IAM
VPC Service Controls
Cloud KMS
Secret Manager
Cloud Armor
Binary Authorization
Google Security Operations
```

---

# 29. In-Depth — Microsoft Secure Score

**Microsoft Secure Score** is a numerical summary of security posture in the Microsoft security ecosystem based on security-related measurements and recommended actions.

Microsoft explicitly warns that it is **not** an absolute measure of the probability of a breach.

Typical categories can include:

```text
Identity
Data
Devices
Apps
```

Workflow:

```text
Security Configuration
       ↓
Recommended Actions
       ↓
Points / Score
       ↓
Prioritization
```

### Important Distinction

Do not confuse:

```text
Microsoft Secure Score
```

with:

```text
Cloud Secure Score in Defender for Cloud
```

Cloud Secure Score is specifically focused on cloud security posture and, in current Microsoft documentation, incorporates risk context and asset criticality.

---

# 30. In-Depth — Microsoft Defender for Cloud

**Microsoft Defender for Cloud** is Microsoft's CNAPP.

Microsoft currently describes three major areas:

```text
CSPM
CWPP
DevSecOps
```

It covers Azure and supports hybrid/multicloud scenarios including AWS and GCP.

## 30.1 CSPM

Finds:

```text
Misconfiguration
Exposure
Weak Security Configuration
Attack Paths
Risky Resources
Identity Risk
```

## 30.2 CWPP

Protects supported workloads such as:

```text
Servers
Containers
Storage
Databases
```

## 30.3 DevSecOps

Connects code and deployment security to runtime posture.

```text
Repository
    ↓
IaC
    ↓
Pipeline
    ↓
Cloud
    ↓
Runtime
```

## 30.4 Regulatory Compliance

Maps supported controls to security standards and benchmarks.

## 30.5 Multicloud

Supported integrations can include:

```text
Azure
AWS
GCP
```

---

# 31. In-Depth — Microsoft Defender for Cloud Apps

**Microsoft Defender for Cloud Apps** is a CASB and SaaS-security platform.

Microsoft documents capabilities including:

```text
CASB
Shadow IT Discovery
SaaS Security Posture
Threat Detection
Data Protection
App Governance
Session Controls
OAuth Governance
```

## 31.1 Shadow IT

```text
Employee
   ↓
Uses Unapproved SaaS
   ↓
Uploads Corporate Data
```

Cloud App discovery helps identify this.

## 31.2 App Governance

OAuth applications can have large permissions.

Example:

```text
OAuth App
   ↓
Files.ReadWrite.All
Mail.ReadWrite
User Data
```

Security teams should review:

```text
High-Permission Apps
Unused Apps
Expired Credentials
Risky OAuth Apps
```

## 31.3 Anomaly Detection

Examples can include:

```text
Impossible Travel
Anonymous IP Activity
Multiple Failed Logins
Unusual Administrative Activity
Suspicious Data Deletion
```

Exact detections evolve over time.

---

# 32. Microsoft Entra Permissions Management — Historical Note

One of the supplied screenshots shows:

> Microsoft Entra Permissions Management

This was Microsoft's dedicated CIEM product.

It analyzed:

```text
Effective Permissions
Permission Creep
Over-Privileged Identities
Multicloud Entitlements
```

However, Microsoft officially retired **Microsoft Entra Permissions Management on October 1, 2025**.

Therefore:

> Do not build a new 2026 learning or deployment plan around Entra Permissions Management as an active standalone product.

The underlying security problem still exists:

```text
CIEM
Least Privilege
Effective Permissions
Attack Paths
Cloud Entitlements
```

Current Microsoft cloud-security capabilities increasingly handle these areas through Defender for Cloud and related identity/security tooling.

---

# 33. Cloud Security Tool Comparison

| Category / Tool | Primary Focus | Core Question |
|---|---|---|
| CSPM | Cloud configuration | Is my cloud configured securely? |
| CWPP | Runtime/workloads | Are my workloads protected? |
| CNAPP | Unified cloud lifecycle | Can code, posture, identity, workload, and runtime risk be connected? |
| CASB | SaaS/cloud app usage | Which cloud apps are being used and is access safe? |
| DSPM | Sensitive data | Where is sensitive data and who can reach it? |
| CIEM | Permissions | Who can do what? |
| SIEM | Logs/events | What security activity is happening? |
| SOAR | Response | What response can be automated? |
| SAST | Source code | Is vulnerable code being written? |
| SCA | Dependencies | Are dependencies risky? |
| IaC Scanner | Deployment configuration | Will this infrastructure code create risk? |

### Tool Examples

| Purpose | AWS | Microsoft | Google Cloud | Open Source |
|---|---|---|---|---|
| Posture | Security Hub CSPM | Defender for Cloud | Security Command Center | Prowler / ScoutSuite / CloudSploit |
| Threat Detection | GuardDuty | Defender for Cloud / Defender XDR | SCC Threat Detection | Depends on tool |
| SaaS Security | — | Defender for Cloud Apps | Security ecosystem integrations | — |
| Audit Logging | CloudTrail | Activity / Entra logs | Cloud Audit Logs | — |
| Permissions | IAM Access Analyzer | Defender/identity capabilities | IAM tooling | Prowler checks etc. |

---

# 34. Cloud Security Architecture Example

```text
                         USERS
                           ↓
                    Identity Provider
                  MFA / Passkeys / SSO
                           ↓
                    Conditional Access
                           ↓
                         WAF/CDN
                           ↓
                      API Gateway
                           ↓
              ┌────────────┴────────────┐
              ↓                         ↓
         Application                 Services
              ↓                         ↓
     Containers / Kubernetes / Serverless
                         ↓
                      Database
                         ↓
                       Storage
```

Cross-cutting controls:

```text
IAM       → Least Privilege
Secrets   → Secrets Manager / Key Vault
Keys      → KMS / HSM
CSPM      → Continuous Configuration Assessment
CWPP      → Runtime Protection
DSPM      → Sensitive Data Risk
CIEM      → Effective Permissions
SIEM      → Central Detection
SOAR      → Response Automation
Backup    → Recovery
IaC       → Shift Left
```

---

# 35. Cloud Security Predictions and 2026 Directional Trends

These are **directional trends**, not guarantees.

## 35.1 AI Accelerates Both Attack and Defense

Attackers can use AI to improve:

```text
Speed
Scale
Reconnaissance
Social Engineering
Automation
```

Defenders use AI for:

```text
Alert Triage
Investigation
Detection
Threat Intelligence
Response Assistance
```

## 35.2 Agentic Security Operations

Security workflows are moving toward:

```text
Security Event
     ↓
AI / Agent
     ↓
Enrich
Correlate
Prioritize
Investigate
     ↓
Human Approval / Policy
     ↓
Response
```

## 35.3 Identity Becomes More Important

Expect continued emphasis on:

```text
Passkeys
Phishing-Resistant MFA
Workload Identity
Machine Identity
AI Agent Identity
Temporary Credentials
Entitlement Governance
```

## 35.4 Continuous Posture Replaces Periodic Review

Old:

```text
Annual Audit
```

Modern:

```text
Continuous Assessment
       ↓
Drift Detection
       ↓
Risk-Based Prioritization
       ↓
Automated Remediation
```

## 35.5 CNAPP Consolidation

Security platforms increasingly correlate:

```text
Code
IaC
Identity
Posture
Workloads
Data
Runtime
```

## 35.6 Data Security and AI Security Converge

```text
AI Security
+
DSPM
+
Identity
+
Application Security
+
Data Governance
```

## 35.7 Data Sovereignty Is an Architecture Requirement

Architects increasingly consider:

```text
Data Residency
Operational Sovereignty
Regional Service Availability
Encryption-Key Control
Regulatory Requirements
```

## 35.8 Security Moves Earlier

```text
Runtime
  ↑
Deployment
  ↑
CI/CD
  ↑
IaC
  ↑
Source Code
  ↑
Architecture
```

This is:

```text
Shift Left
+
DevSecOps
```

---

# 36. Cloud Adoption in the Middle East

Major adoption drivers include:

```text
Government Digital Transformation
Local Cloud Regions
Data Residency
AI Adoption
Financial Digitization
Smart Cities
Telecommunications
Public-Sector Modernization
```

## 36.1 AWS

AWS currently lists active Middle East Regions including:

```text
Middle East (Bahrain)
me-south-1

Middle East (UAE)
me-central-1
```

AWS also lists an announced future Region in Saudi Arabia.

Important:

> An announced region is not the same as a generally available region.

Always verify the live AWS regions list before architecture decisions.

## 36.2 Microsoft Azure

Azure's official global-infrastructure pages list Middle East regional presence including areas such as:

```text
UAE
Qatar
Israel
Saudi Arabia expansion
```

Exact region availability and service availability must be checked per workload because not all Azure services are available in every region.

## 36.3 Google Cloud

Google Cloud currently documents active Middle East regions including:

```text
Doha, Qatar
me-central1

Dammam, Saudi Arabia
me-central2

Tel Aviv
me-west1
```

## 36.4 Saudi Cloud-First Policy

Saudi Arabia's MCIT Cloud-First Policy encourages covered government agencies to consider cloud computing first for new IT investments and encourages similar adoption in the private sector.

## 36.5 Why Local Regions Matter

Local regions may help with:

```text
Latency
Data Residency
Public-Sector Adoption
Regulatory Alignment
Local Disaster Recovery
Financial-Sector Requirements
```

But:

> A local region does not automatically make a workload compliant.

Compliance still depends on:

```text
Architecture
Data Flow
Identity
Service Choice
Encryption
Logging
Contracts
Legal Assessment
```

---

# 37. Cloud Security in the Middle East

## 37.1 Data Residency

Ask:

```text
Where is primary data?
Where are backups?
Where are logs?
Where are encryption keys?
Where are replicas?
Where is support data processed?
```

## 37.2 Regulation and Standards

Map controls to:

```text
National Regulations
Sector Requirements
Privacy Laws
Financial Regulations
CIS Benchmarks
ISO 27001
Cloud Provider Baselines
```

## 37.3 Regional Service Differences

A Middle East region may not support every global cloud service.

Therefore architecture may require:

```text
Primary Region
+
Approved Secondary Region
+
Documented Data Flow
+
Failover Strategy
```

## 37.4 Skills Valuable in the Region

```text
AWS / Azure / GCP
IAM
Networking
Linux
CSPM
SIEM
Kubernetes
Terraform
Cloud Governance
Compliance
Data Residency
```

---

# 38. Cloud Security Engineer Responsibilities

Typical responsibilities:

```text
Identity Security
Network Security
Cloud Configuration
Data Protection
Workload Protection
Cloud Logging
Threat Detection
Security Automation
DevSecOps
Incident Response
Compliance
Architecture Review
```

Daily work may include:

```text
Review CSPM Findings
Analyze IAM
Investigate Cloud Alerts
Review Public Exposure
Validate Terraform
Improve Central Logging
Automate Remediation
Support Incident Response
Review Architecture
```

---

# 39. Cloud Security Learning Roadmap

```text
Cybersecurity Fundamentals
        ↓
Networking
        ↓
Linux
        ↓
Python + Bash
        ↓
Cloud Fundamentals
        ↓
IAM
        ↓
Cloud Networking
        ↓
Encryption / KMS
        ↓
Audit Logging
        ↓
CSPM
        ↓
Threat Detection
        ↓
Docker
        ↓
Kubernetes
        ↓
Terraform
        ↓
CI/CD Security
        ↓
CNAPP / DevSecOps
        ↓
Cloud Security Engineering
```

---

# 40. Hands-On Lab Roadmap

## Lab 1 — Secure Cloud Account

Implement:

```text
Privileged MFA / Passkeys
Security Contacts
Central Identity
Audit Logging
Budget Alerts
Basic Guardrails
```

## Lab 2 — Secure Network

Build:

```text
VPC / VNet
Public Subnet
Private Subnet
NAT
Security Groups
Private Database
```

## Lab 3 — IAM Least Privilege

Create:

```text
Developer Role
Read-Only Role
Security Auditor
Workload Role
```

Avoid static access keys.

## Lab 4 — Centralize Logs

Collect:

```text
Cloud Audit Logs
Identity Logs
Firewall Logs
Application Logs
```

Send them to central storage and/or SIEM.

## Lab 5 — CSPM

Run Prowler or ScoutSuite against a lab account.

Review findings by:

```text
Critical
High
Medium
Low
```

## Lab 6 — CIS Benchmark

Choose one:

```text
CIS AWS Foundations
CIS Microsoft Azure
CIS Google Cloud
```

Evaluate your lab.

## Lab 7 — Infrastructure as Code

Use Terraform to build:

```text
Network
IAM
Compute
Logging
```

Then scan the IaC before deployment.

## Lab 8 — Kubernetes Security

Implement:

```text
RBAC
NetworkPolicy
Secrets
Non-Root Containers
Pod Security
Image Scanning
Audit Logs
```

---

# 41. Interview and Exam Review Questions

## What is the Shared Responsibility Model?

It divides security responsibilities between the cloud provider and the customer.

## What is security "of" the cloud?

Security of the provider's underlying cloud infrastructure.

## What is security "in" the cloud?

Security of customer-controlled identities, configuration, data, workloads, and applications.

## Why is EC2 different from RDS and S3?

Because each service abstracts a different amount of infrastructure.

```text
More Managed Service
→ Less Customer Infrastructure Administration
```

## What is CSPM?

Continuous cloud configuration and posture assessment.

## What is CWPP?

Security for running cloud workloads.

## What is CNAPP?

A unified cloud-native security platform combining multiple lifecycle security capabilities.

## What is CASB?

A security layer for cloud/SaaS application visibility, governance, and data control.

## What is DSPM?

Security posture analysis focused on sensitive data.

## What is CIEM?

Cloud permission and entitlement analysis.

## What is a CIS Benchmark?

A consensus-based secure-configuration recommendation set for a specific technology.

## Why centralize audit logs?

To support detection, investigation, accountability, retention, and incident response across cloud accounts.

## Why are passkeys useful?

They can provide phishing-resistant authentication, especially valuable for privileged identities.

## Why should static keys be avoided?

They are long-lived secrets that can be copied, leaked, and reused. Temporary identity-based credentials reduce this risk.

## What does "Assume Breach" mean?

Design as though an attacker may already have some access, then reduce blast radius and continuously verify behavior.

---

# 42. Final Review Sheet

## Shared Responsibility

```text
Provider
→ Security OF the cloud

Customer
→ Security IN the cloud
```

## Responsibility by Service

```text
EC2
→ More customer responsibility

RDS
→ More provider management

S3
→ Highly abstracted service
```

Customer still retains:

```text
Data
Identity
Access
Configuration
Business Decisions
```

## Six Things to Inventory

```text
Identities
Endpoints
Apps
Infrastructure
Network
Data
```

## Top 10 Security-Team Priorities

```text
1. Maintain account/security contact information
2. Use passkeys / phishing-resistant MFA
3. Never hard-code secrets
4. Prefer temporary credentials; rotate remaining long-lived keys
5. Restrict security groups / firewall exposure
6. Centralize audit and activity logs
7. Enforce least privilege
8. Remediate security findings
9. Automate security controls
10. Build scalable guardrails
```

## Cloud Security Tool Families

```text
CNAPP
CSPM
CWPP
CASB
DSPM
CIEM
SIEM
SOAR
IaC Security
SAST
SCA
```

## Key Tools

```text
AWS
├── Trusted Advisor
├── Security Hub CSPM
├── GuardDuty
├── Config
├── CloudTrail
├── Inspector
└── IAM Access Analyzer

Microsoft
├── Microsoft Secure Score
├── Defender for Cloud
└── Defender for Cloud Apps

Google Cloud
└── Security Command Center

Open Source
├── Prowler
├── ScoutSuite
└── CloudSploit
```

---

# 43. Official Resources

## Shared Responsibility

- AWS Shared Responsibility Model  
  https://aws.amazon.com/compliance/shared-responsibility-model/

- AWS Well-Architected — Shared Responsibility  
  https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/shared-responsibility.html

- Microsoft Azure — Shared Responsibility  
  https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility

- Google Cloud — Shared Fate / Shared Responsibility  
  https://cloud.google.com/security/shared-fate

## Zero Trust

- NIST SP 800-207 — Zero Trust Architecture  
  https://csrc.nist.gov/pubs/sp/800/207/final

## CIS Benchmarks

- CIS Benchmarks  
  https://www.cisecurity.org/cis-benchmarks

- CIS Microsoft Azure Benchmark  
  https://www.cisecurity.org/benchmark/azure

## Microsoft

- Microsoft Defender for Cloud Overview  
  https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction

- Defender for Cloud Apps Overview  
  https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps

- Microsoft Secure Score  
  https://learn.microsoft.com/en-us/defender-xdr/microsoft-secure-score

- Defender for Cloud Secure Score  
  https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls

- Microsoft Entra Release Archive — Permissions Management Retirement  
  https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-archive

## AWS

- AWS Trusted Advisor  
  https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html

- AWS Trusted Advisor Check Reference  
  https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html

- AWS Security Hub CSPM  
  https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html

- AWS Regions  
  https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html

## Google Cloud

- Security Command Center Overview  
  https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview

- Security Command Center Threat Detection  
  https://docs.cloud.google.com/security-command-center/docs/overview-threats

- Google Cloud Regions / Zones  
  https://docs.cloud.google.com/compute/docs/regions-zones

## Open Source

- Prowler  
  https://github.com/prowler-cloud/prowler

- ScoutSuite  
  https://github.com/nccgroup/ScoutSuite

- CloudSploit  
  https://github.com/aquasecurity/cloudsploit

## Middle East Cloud Adoption

- AWS Global Infrastructure  
  https://aws.amazon.com/about-aws/global-infrastructure/

- Azure Global Infrastructure  
  https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies

- Google Cloud Locations  
  https://cloud.google.com/about/locations

- Saudi Arabia MCIT — Cloud-First Policy / Acts and Regulations  
  https://mcit.gov.sa/en/acts-and-regulations

---

# End of Document
