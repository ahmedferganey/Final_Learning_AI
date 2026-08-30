# Phase 30 — DevSecOps

Dependency:

```text
Software Engineering + Git + CI/CD
Cloud + Containers + Kubernetes + IaC
Application Security + Cloud Security + GRC
                  ↓
116 DevSecOps Fundamentals
                  ↓
117 DevSecOps CI/CD Security
                  ↓
118 Container Security
                  ↓
119 Kubernetes Security
                  ↓
120 Infrastructure as Code Security
```

## Phase Goal

Build a trusted software/infrastructure delivery chain:

```text
Secure Design
   ↓
Trusted Source
   ↓
Trusted Pipeline Identity
   ↓
Isolated Build
   ↓
Security Verification
   ↓
Immutable Artifact / Desired State
   ↓
SBOM + Provenance + Signature / Policy Evidence
   ↓
Controlled Deployment
   ↓
Hardened Runtime
   ↓
Monitoring / Incident Response
   ↓
Engineering Feedback
```

## Current Standards Notes — August 2026

- The current **final** NIST SSDF is **SP 800-218 / SSDF v1.1**.
- NIST's **SSDF v1.2 / SP 800-218 Rev.1** is currently an Initial Public Draft.
- **SLSA v1.2** is the current approved SLSA specification and includes Build and Source tracks.
- Kubernetes Pod Security Standards define **Privileged, Baseline, and Restricted** profiles.

## Courses

| # | Course | Focus |
|---|---|---|
| 116 | DevSecOps Fundamentals | Secure SDLC, culture, risk, supply chain, testing, findings, feedback |
| 117 | DevSecOps CI/CD Security | Source, runners, credentials, builds, artifacts, provenance, deployment |
| 118 | Container Security | Images, registries, Dockerfiles, Linux isolation, runtime, response |
| 119 | Kubernetes Security | API/RBAC, PSS/PSA, workloads, NetworkPolicy, secrets, nodes, audit, IR |
| 120 | Infrastructure as Code Security | Terraform/state, policy as code, scanning, cloud rules, GitOps, drift |

## Recommended Lab Architecture

```text
Developer
  ↓
Git Repository
  ↓
CI Runner
  ↓
SAST / SCA / Secret / IaC Checks
  ↓
Container Build
  ↓
SBOM / Provenance / Signature
  ↓
Registry
  ↓
Terraform
  ↓
Kubernetes
  ↓
Runtime Logging / Detection
```

## Phase Capstone

Build one integrated trusted-delivery sandbox containing:

1. protected source repository;
2. pull-request security controls;
3. short-lived CI identity;
4. isolated runner/builder;
5. SAST, SCA, secret and IaC checks;
6. secure Dockerfile;
7. SBOM;
8. immutable image digest;
9. signature/provenance verification;
10. protected registry;
11. Terraform remote-state controls;
12. plan/apply separation;
13. policy-as-code checks;
14. Kubernetes RBAC;
15. dedicated ServiceAccount;
16. Pod Security Admission;
17. hardened Pod securityContext;
18. default-deny NetworkPolicy;
19. audit/runtime logs;
20. exception workflow;
21. incident-response playbook;
22. recovery/rebuild test;
23. metrics dashboard;
24. architecture decision records.

## Statistics

| Course | Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 116 | 115 | 70 | 115 | 13,792 |
| 117 | 110 | 70 | 110 | 13,332 |
| 118 | 106 | 70 | 106 | 13,007 |
| 119 | 123 | 70 | 123 | 14,478 |
| 120 | 126 | 70 | 126 | 14,733 |
| **Total** | **580** | **350** | **580** | **69,342** |

## Completion Criteria

You should be able to explain from evidence:

- who may change source;
- which identities execute CI/CD;
- how untrusted PR code is isolated;
- how dependencies and third-party workflows are governed;
- how artifacts are identified immutably;
- where SBOM/provenance/signature evidence lives;
- how production deployment is authorized;
- whether containers run with unnecessary privilege;
- who can create Kubernetes privilege;
- how Pod and network policy are enforced;
- how Terraform state is protected;
- whether PR identities can apply production;
- how drift is detected and reconciled;
- which logs reconstruct a release;
- how a compromised pipeline/workload is revoked and rebuilt.

## Next Phase

```text
Phase 31 — AI for IT, Cloud & Security
121 Introduction to Generative AI and Prompt Engineering
122 AI for System Administrators
123 AI for Cloud Engineers
124 Generative AI for DevOps Engineers
125 AI Security
```
