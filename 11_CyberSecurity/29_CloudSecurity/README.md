# Phase 29 — Cloud Security

This phase intentionally comes late.

```text
Cloud architecture
 + Networking
 + OS administration
 + Containers / Kubernetes
 + IaC / DevOps
 + Cybersecurity / AppSec
 + SOC / Incident Response
 + GRC
       |
       v
112 Cloud Security Fundamentals
       |
       v
113 AWS Security Fundamentals
       |
       v
114 Azure Security Fundamentals
       |
       v
115 Cloud Security and Governance
```

> **You cannot reliably secure a cloud architecture that you do not understand.**

---

# Current Reference Notes — August 2026

AWS and Microsoft both document cloud security as a shared responsibility. AWS describes responsibility as security **of** the cloud versus security **in** the cloud. Microsoft documents that customer responsibility remains for important areas including data, identities, accounts, and access management, while other responsibilities change across IaaS, PaaS, and SaaS.

The current AWS Well-Architected Security Pillar groups guidance into:

```text
Security foundations
Identity and access management
Detection
Infrastructure protection
Data protection
Incident response
Application security
```

AWS Security Hub CSPM currently supports AWS Foundational Security Best Practices and CIS AWS Foundations Benchmark versions including **v5.0.0**.

Microsoft Defender for Cloud currently provides CSPM and workload-protection capabilities for Azure and supported multicloud environments. Azure Policy provides policy definitions and effects to audit or enforce cloud-resource state.

NIST SP 800-207 defines zero trust without implicit trust based solely on network location or ownership. NIST SP 800-207A extends the model to cloud-native applications in multi-cloud environments and emphasizes application/service identity.

CSA released Cloud Controls Matrix **v4.1** in January 2026. The current version defines **207 cloud security/privacy controls across 17 domains**.

---

# Course Map

| # | Course | Primary Outcome |
|---|---|---|
| 112 | Cloud Security Fundamentals | Design provider-neutral cloud security architecture |
| 113 | AWS Security Fundamentals | Implement cloud security deeply in AWS |
| 114 | Azure Security Fundamentals | Implement cloud security deeply in Azure |
| 115 | Cloud Security and Governance | Govern multi-cloud security at enterprise scale |

---

# Phase Mental Model

```text
BUSINESS / DATA
      |
CLOUD ARCHITECTURE
      |
IDENTITY
      |
NETWORK
      |
WORKLOAD
      |
DATA / KEYS / SECRETS
      |
LOGGING / DETECTION
      |
INCIDENT RESPONSE / RECOVERY
      |
GOVERNANCE / RISK / COMPLIANCE
```

Cloud security is the interaction of all layers.

---

# Course 112 — Cloud Security Fundamentals

Learn the control categories before provider products:

```text
Shared responsibility
Identity / workload identity
Network exposure / private paths
Data / KMS / HSM / secrets
Compute / serverless / container / Kubernetes
IaC / CI/CD / software supply chain
Central audit logging
CSPM / CWPP / CIEM / CNAPP
Incident response / forensic readiness
Landing zones / guardrails
Risk / compliance
```

---

# Course 113 — AWS Security Fundamentals

Reference architecture:

```text
AWS Organization
 |- Management
 |- Security OU
 |   |- Log Archive
 |   `- Security Tooling / Audit
 |- Infrastructure
 |- Workloads-Prod
 |- Workloads-NonProd
 `- Sandbox

Identity:
IdP / IAM Identity Center -> temporary roles -> least privilege

Evidence:
CloudTrail + Config + GuardDuty + Inspector + Macie
+ Security Hub CSPM + centralized logs

Governance:
Organizations + SCPs + Control Tower + IaC + Config/posture controls
```

---

# Course 114 — Azure Security Fundamentals

Reference architecture:

```text
Microsoft Entra Tenant
      |
Management Groups
 |- Platform
 |   |- Identity
 |   |- Management
 |   `- Connectivity
 `- Application Landing Zones
      |
Subscriptions -> Resource Groups -> Resources

Identity:
Entra ID + MFA + Conditional Access + PIM
+ Managed Identities + Workload Federation

Governance:
Azure Policy + Defender for Cloud + MCSB

Monitoring:
Activity Logs + Diagnostic Settings
+ Log Analytics + Sentinel + Defender findings
```

---

# Course 115 — Cloud Security and Governance

The objective changes from:

```text
How do I secure one resource?
```

to:

```text
How do thousands of resources across many teams and clouds
remain inside one approved security model?
```

Pattern:

```text
Vendor-neutral control objective
        |
   +----+----+
   |         |
  AWS       Azure
   |         |
   +----+----+
        |
common evidence
        |
risk / compliance
        |
exception / remediation
        |
continuous control monitoring
```

---

# Cloud Security Capability Map

```text
IAM / IGA / PAM
KMS / HSM / secrets
Network firewall / WAF / DDoS
Private connectivity
CSPM
CWPP
CIEM
DSPM
CNAPP
Exposure / attack-path management
Vulnerability management
Cloud audit logging
SIEM / SOAR
IaC / policy as code
Backup / recovery
GRC / continuous control monitoring
```

---

# Recommended Repository

```text
Phase_29_Cloud_Security/
├── 112_Fundamentals/
│   ├── threat_models/
│   ├── identity/
│   ├── network/
│   ├── data/
│   ├── workloads/
│   ├── logging/
│   └── incident_response/
├── 113_AWS/
│   ├── organizations/
│   ├── iam/
│   ├── network/
│   ├── kms_data/
│   ├── detection/
│   ├── workloads/
│   └── ir/
├── 114_Azure/
│   ├── entra/
│   ├── management_groups/
│   ├── policy/
│   ├── network/
│   ├── keyvault_data/
│   ├── defender_sentinel/
│   └── ir/
├── 115_Governance/
│   ├── control_library/
│   ├── ccm/
│   ├── guardrails/
│   ├── exceptions/
│   ├── metrics/
│   ├── risk/
│   └── assurance/
└── README.md
```

---

# Combined Capstone

Design a regulated SaaS company using AWS, Azure, Kubernetes, SaaS, and hybrid connectivity.

Deliver at least:

1. Shared responsibility matrix
2. AWS Organization
3. Azure management-group hierarchy
4. Account/subscription vending
5. Human privileged-access architecture
6. Workload-identity architecture
7. Public/private network architecture
8. WAF / DDoS design
9. Data classification
10. KMS / Key Vault / HSM / secrets design
11. Centralized logging
12. AWS detection/posture architecture
13. Azure Defender/Sentinel architecture
14. CSPM/CWPP/CIEM/DSPM/CNAPP model
15. IaC / policy-as-code guardrails
16. Vulnerability management
17. Incident response and forensic readiness
18. Immutable backup / recovery
19. CSA CCM v4.1 mapping
20. NIST CSF mapping
21. Cloud risk register
22. Exception process
23. Metrics / KRIs / KCIs
24. Executive dashboard
25. 12-month maturity roadmap

---

# Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 112 — Cloud Security Fundamentals | 194 | 80 | 194 | 30,606 |
| 113 — AWS Security Fundamentals | 190 | 80 | 190 | 29,832 |
| 114 — Azure Security Fundamentals | 194 | 80 | 194 | 30,221 |
| 115 — Cloud Security and Governance | 206 | 80 | 206 | 31,895 |
| **TOTAL** | **784** | **320** | **784** | **122,554** |

---

# Completion Criteria

You should be able to:

- explain shared responsibility by service model;
- design short-lived human and workload identity;
- build AWS and Azure landing-zone security models;
- apply least privilege and guardrails at scale;
- design public and private service paths;
- secure keys, secrets, certificates, storage, databases, and backups;
- harden VM, container, Kubernetes, serverless, and CI/CD workloads;
- centralize protected cloud audit evidence;
- operate posture, workload, entitlement, and attack-path security;
- investigate a compromised cloud identity;
- preserve cloud evidence and recover workloads;
- map vendor-neutral controls to AWS and Azure implementations;
- manage cloud risk, compliance, exceptions, metrics, and continuous assurance;
- explain why a posture score is not proof of complete security.

---

# Next Phase

```text
Phase 30 — DevSecOps
116 DevSecOps Fundamentals
117 DevSecOps CI/CD Security
118 Container Security
119 Kubernetes Security
120 Infrastructure as Code Security
```
