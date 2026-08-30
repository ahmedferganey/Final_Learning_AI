# 119. Kubernetes Security

> Phase 30 — DevSecOps

## 1. Topic Title

**Kubernetes Security**

## 2. Learning Objectives

- Secure Kubernetes API/control-plane, etcd, nodes, kubelet, CNI/CSI, and cluster access.
- Build least-privilege RBAC, ServiceAccount, and workload identity.
- Apply Pod Security Standards/Admission, secure securityContext, NetworkPolicy, admission controls, and secret protection.
- Secure supply chain, Helm/GitOps, ingress, audit logging, runtime monitoring, and backups.
- Respond to compromised Pods, identities, nodes, or cluster-admin access.

## 3. Prerequisites

```text
Git and source control
Software Engineering
CI/CD
Cloud
Docker
Kubernetes fundamentals
Terraform / IaC fundamentals
Application Security
Cloud Security
GRC
SOC / Incident Response
```

Complete Course 118 before securing Kubernetes orchestration.

## 4. Core Concepts Explanation

# Part 1 — Kubernetes Security Purpose

### Core Concept

Kubernetes Security Purpose belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes Security Purpose** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 2 — Kubernetes Threat Model

### Core Concept

Kubernetes Threat Model belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes Threat Model** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 3 — Cluster Trust Boundaries

### Core Concept

Cluster Trust Boundaries belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cluster Trust Boundaries** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 4 — Control Plane

### Core Concept

Control Plane belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Control Plane** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 5 — Worker Node

### Core Concept

Worker Node belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Worker Node** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 6 — API Server

### Core Concept

API Server belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **API Server** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 7 — etcd

### Core Concept

etcd belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **etcd** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 8 — Scheduler

### Core Concept

Scheduler belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Scheduler** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 9 — Controller Manager

### Core Concept

Controller Manager belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Controller Manager** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 10 — kubelet

### Core Concept

kubelet belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **kubelet** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 11 — CNI Plugin

### Core Concept

CNI Plugin belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **CNI Plugin** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 12 — CSI Plugin

### Core Concept

CSI Plugin belongs to the **Cluster Architecture** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **CSI Plugin** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 13 — API Server Authentication

### Core Concept

API Server Authentication belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **API Server Authentication** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 14 — API Server Authorization

### Core Concept

API Server Authorization belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **API Server Authorization** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 15 — Kubernetes RBAC

### Core Concept

Kubernetes RBAC belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes RBAC** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 16 — Role

### Core Concept

Role belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Role** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 17 — ClusterRole

### Core Concept

ClusterRole belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **ClusterRole** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 18 — RoleBinding

### Core Concept

RoleBinding belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **RoleBinding** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 19 — ClusterRoleBinding

### Core Concept

ClusterRoleBinding belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **ClusterRoleBinding** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 20 — Namespace-Scoped Permissions

### Core Concept

Namespace-Scoped Permissions belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Namespace-Scoped Permissions** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 21 — Least Privilege RBAC

### Core Concept

Least Privilege RBAC belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Least Privilege RBAC** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 22 — Wildcard RBAC Risk

### Core Concept

Wildcard RBAC Risk belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Wildcard RBAC Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 23 — Secrets Permission Risk

### Core Concept

Secrets Permission Risk belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Secrets Permission Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 24 — Pod Exec Permission Risk

### Core Concept

Pod Exec Permission Risk belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pod Exec Permission Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 25 — RBAC Privilege Escalation Paths

### Core Concept

RBAC Privilege Escalation Paths belongs to the **Authentication and RBAC** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **RBAC Privilege Escalation Paths** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 26 — ServiceAccount

### Core Concept

ServiceAccount belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **ServiceAccount** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 27 — Default ServiceAccount

### Core Concept

Default ServiceAccount belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Default ServiceAccount** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 28 — automountServiceAccountToken

### Core Concept

automountServiceAccountToken belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **automountServiceAccountToken** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 29 — Projected Service Account Token

### Core Concept

Projected Service Account Token belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Projected Service Account Token** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 30 — Workload Identity Federation

### Core Concept

Workload Identity Federation belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Workload Identity Federation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
CI / workload
   ↓ signed identity token
platform trust policy
   ↓
short-lived scoped credential
   ↓
cloud / registry / deployment API
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 31 — Cloud Provider Workload Identity

### Core Concept

Cloud Provider Workload Identity belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cloud Provider Workload Identity** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
CI / workload
   ↓ signed identity token
platform trust policy
   ↓
short-lived scoped credential
   ↓
cloud / registry / deployment API
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 32 — OIDC Authentication

### Core Concept

OIDC Authentication belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **OIDC Authentication** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
CI / workload
   ↓ signed identity token
platform trust policy
   ↓
short-lived scoped credential
   ↓
cloud / registry / deployment API
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 33 — Short-Lived kubectl Credentials

### Core Concept

Short-Lived kubectl Credentials belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Short-Lived kubectl Credentials** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 34 — kubeconfig Security

### Core Concept

kubeconfig Security belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **kubeconfig Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 35 — Cluster Admin Risk

### Core Concept

Cluster Admin Risk belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cluster Admin Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 36 — Break-Glass Cluster Access

### Core Concept

Break-Glass Cluster Access belongs to the **Service Accounts and Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Break-Glass Cluster Access** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 37 — Pod Security Context

### Core Concept

Pod Security Context belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pod Security Context** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 38 — runAsNonRoot

### Core Concept

runAsNonRoot belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **runAsNonRoot** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 39 — allowPrivilegeEscalation

### Core Concept

allowPrivilegeEscalation belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **allowPrivilegeEscalation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 40 — readOnlyRootFilesystem

### Core Concept

readOnlyRootFilesystem belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **readOnlyRootFilesystem** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 41 — Linux Capabilities

### Core Concept

Linux Capabilities belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Linux Capabilities** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 42 — seccompProfile

### Core Concept

seccompProfile belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **seccompProfile** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 43 — AppArmor Awareness

### Core Concept

AppArmor Awareness belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **AppArmor Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 44 — SELinux Awareness

### Core Concept

SELinux Awareness belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SELinux Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 45 — privileged Container

### Core Concept

privileged Container belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **privileged Container** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 46 — hostNetwork

### Core Concept

hostNetwork belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **hostNetwork** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 47 — hostPID

### Core Concept

hostPID belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **hostPID** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 48 — hostIPC

### Core Concept

hostIPC belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **hostIPC** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 49 — hostPath

### Core Concept

hostPath belongs to the **Pod Hardening** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **hostPath** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 50 — Pod Security Standards

### Core Concept

Kubernetes Pod Security Standards define three cumulative security profiles—Privileged, Baseline, and Restricted—for common Pod hardening expectations.

### Detailed Explanation

Treat **Pod Security Standards** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 51 — Privileged Profile

### Core Concept

Privileged Profile belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Privileged Profile** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 52 — Baseline Profile

### Core Concept

Baseline Profile belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Baseline Profile** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 53 — Restricted Profile

### Core Concept

Restricted Profile belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Restricted Profile** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 54 — Pod Security Admission

### Core Concept

Pod Security Admission belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pod Security Admission** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 55 — Namespace PSA Labels

### Core Concept

Namespace PSA Labels belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Namespace PSA Labels** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 56 — PSA Enforce

### Core Concept

PSA Enforce belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **PSA Enforce** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 57 — PSA Audit

### Core Concept

PSA Audit belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **PSA Audit** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 58 — PSA Warn

### Core Concept

PSA Warn belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **PSA Warn** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 59 — PSS Version Pinning Awareness

### Core Concept

PSS Version Pinning Awareness belongs to the **Pod Security Standards** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **PSS Version Pinning Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 60 — Admission Control

### Core Concept

Admission Control belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Admission Control** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 61 — Validating Admission Policy Awareness

### Core Concept

Validating Admission Policy Awareness belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Validating Admission Policy Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 62 — OPA Gatekeeper

### Core Concept

OPA Gatekeeper belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **OPA Gatekeeper** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 63 — Kyverno

### Core Concept

Kyverno belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kyverno** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 64 — Policy Exceptions

### Core Concept

Policy Exceptions belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Policy Exceptions** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 65 — Image Digest Pinning

### Core Concept

Image Digest Pinning belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Image Digest Pinning** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 66 — Image Signature Verification

### Core Concept

Image Signature Verification belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Image Signature Verification** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 67 — Cosign in Kubernetes Awareness

### Core Concept

Cosign in Kubernetes Awareness belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cosign in Kubernetes Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```bash
# Verify an artifact in a registry you control
cosign verify <registry>/<image>@sha256:<digest>
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 68 — Registry Allowlist

### Core Concept

Registry Allowlist belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Registry Allowlist** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 69 — Private Registry

### Core Concept

Private Registry belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Private Registry** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 70 — Helm Security

### Core Concept

Helm Security belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Helm Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 71 — GitOps Repository Trust

### Core Concept

GitOps Repository Trust belongs to the **Admission and Supply Chain** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **GitOps Repository Trust** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 72 — Kubernetes Secrets

### Core Concept

Kubernetes Secrets belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes Secrets** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 73 — Secrets Are Not Encryption by Default Awareness

### Core Concept

Secrets Are Not Encryption by Default Awareness belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Secrets Are Not Encryption by Default Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 74 — etcd Encryption at Rest

### Core Concept

etcd Encryption at Rest belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **etcd Encryption at Rest** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 75 — KMS Provider Awareness

### Core Concept

KMS Provider Awareness belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **KMS Provider Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 76 — External Secrets

### Core Concept

External Secrets belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **External Secrets** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 77 — Secrets Store CSI Driver Awareness

### Core Concept

Secrets Store CSI Driver Awareness belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Secrets Store CSI Driver Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 78 — Secret Rotation

### Core Concept

Secret Rotation belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Secret Rotation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 79 — ConfigMap vs Secret

### Core Concept

ConfigMap vs Secret belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **ConfigMap vs Secret** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 80 — Persistent Volume Security

### Core Concept

Persistent Volume Security belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Persistent Volume Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 81 — Backup Encryption

### Core Concept

Backup Encryption belongs to the **Secrets and Data** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Backup Encryption** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 82 — NetworkPolicy

### Core Concept

NetworkPolicy belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **NetworkPolicy** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 83 — Default Deny NetworkPolicy

### Core Concept

Default Deny NetworkPolicy belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Default Deny NetworkPolicy** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 84 — Ingress Policy

### Core Concept

Ingress Policy belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Ingress Policy** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 85 — Egress Policy

### Core Concept

Egress Policy belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Egress Policy** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 86 — Namespace Selector

### Core Concept

Namespace Selector belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Namespace Selector** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 87 — Pod Selector

### Core Concept

Pod Selector belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pod Selector** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 88 — NetworkPolicy Limitations

### Core Concept

NetworkPolicy Limitations belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **NetworkPolicy Limitations** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 89 — Service Mesh Awareness

### Core Concept

Service Mesh Awareness belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Service Mesh Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 90 — mTLS Between Workloads

### Core Concept

mTLS Between Workloads belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **mTLS Between Workloads** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 91 — Ingress Security

### Core Concept

Ingress Security belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Ingress Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 92 — TLS at Ingress

### Core Concept

TLS at Ingress belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **TLS at Ingress** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 93 — LoadBalancer Service Exposure

### Core Concept

LoadBalancer Service Exposure belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **LoadBalancer Service Exposure** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 94 — NodePort Exposure

### Core Concept

NodePort Exposure belongs to the **Network Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **NodePort Exposure** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 95 — API Server Network Exposure

### Core Concept

API Server Network Exposure belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **API Server Network Exposure** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 96 — Private Cluster

### Core Concept

Private Cluster belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Private Cluster** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 97 — Kubelet Security

### Core Concept

Kubelet Security belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubelet Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 98 — Node Authorization

### Core Concept

Node Authorization belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Node Authorization** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 99 — NodeRestriction Admission

### Core Concept

NodeRestriction Admission belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **NodeRestriction Admission** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 100 — etcd Network Isolation

### Core Concept

etcd Network Isolation belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **etcd Network Isolation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 101 — Control Plane Certificate Management

### Core Concept

Control Plane Certificate Management belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Control Plane Certificate Management** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 102 — Kubernetes PKI

### Core Concept

Kubernetes PKI belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes PKI** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 103 — Node Hardening

### Core Concept

Node Hardening belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Node Hardening** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 104 — Node Patch Management

### Core Concept

Node Patch Management belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Node Patch Management** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 105 — Avoiding Direct Node Administration

### Core Concept

Avoiding Direct Node Administration belongs to the **Control Plane and Nodes** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Avoiding Direct Node Administration** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 106 — Kubernetes Audit Logging

### Core Concept

Kubernetes Audit Logging belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes Audit Logging** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 107 — Audit Policy

### Core Concept

Audit Policy belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Audit Policy** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 108 — Centralized Audit Logs

### Core Concept

Centralized Audit Logs belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Centralized Audit Logs** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 109 — Runtime Security

### Core Concept

Runtime Security belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runtime Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 110 — Suspicious kubectl exec

### Core Concept

Suspicious kubectl exec belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Suspicious kubectl exec** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 111 — Suspicious Secret Access

### Core Concept

Suspicious Secret Access belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Suspicious Secret Access** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 112 — Unexpected ClusterRoleBinding

### Core Concept

Unexpected ClusterRoleBinding belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Unexpected ClusterRoleBinding** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 113 — Unexpected Privileged Pod

### Core Concept

Unexpected Privileged Pod belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Unexpected Privileged Pod** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 114 — Kubernetes Vulnerability Management

### Core Concept

Kubernetes Vulnerability Management belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes Vulnerability Management** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 115 — Cluster Version Management

### Core Concept

Cluster Version Management belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cluster Version Management** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 116 — Kubernetes Incident Response

### Core Concept

Kubernetes Incident Response belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Kubernetes Incident Response** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 117 — Compromised ServiceAccount Response

### Core Concept

Compromised ServiceAccount Response belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Compromised ServiceAccount Response** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 118 — Compromised Pod Response

### Core Concept

Compromised Pod Response belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Compromised Pod Response** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 119 — Compromised Node Response

### Core Concept

Compromised Node Response belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Compromised Node Response** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 120 — Cluster Rebuild Decision

### Core Concept

Cluster Rebuild Decision belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cluster Rebuild Decision** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 121 — PSS Restricted Coverage

### Core Concept

PSS Restricted Coverage belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **PSS Restricted Coverage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 122 — NetworkPolicy Coverage

### Core Concept

NetworkPolicy Coverage belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **NetworkPolicy Coverage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


# Part 123 — Audit Logging Coverage

### Core Concept

Audit Logging Coverage belongs to the **Monitoring and IR** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Audit Logging Coverage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

A useful engineering checklist is:

```text
WHAT is protected?
WHO or WHAT identity acts?
WHERE is policy enforced?
HOW is the control tested?
WHAT evidence proves it operated?
HOW is an exception approved?
HOW is compromise contained?
HOW is the trusted state restored?
```

### Diagram / Code / Configuration Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Why It Works

DevSecOps scales when controls are versioned, automated, observable, and reproducible. The same rule should produce predictable results for every repository, build, artifact, environment, cluster, or infrastructure change in scope.

### Production Example

A pull request changes code or infrastructure. Automated checks provide fast feedback, sensitive changes require human review, the build uses scoped short-lived identity, artifacts are immutable, and promotion is policy-controlled. Runtime evidence later confirms whether the expected security state remained intact.

### Common Problems

- using a tool with no policy or owner;
- giving automation permanent administrator credentials;
- trusting mutable artifacts;
- storing secrets in source, logs, caches, images, state, or manifests;
- blocking noisy low-confidence findings until developers bypass the control;
- fixing production manually without reconciling source;
- confusing a passing scan with proof of security.

### Troubleshooting

1. Confirm source revision.
2. Confirm pipeline/policy revision.
3. Confirm executing identity.
4. Confirm effective permissions.
5. Confirm tool/rule version.
6. Confirm artifact or desired-state identity.
7. Confirm audit evidence.
8. Confirm runtime state and drift.

### Best Practices

- least privilege and short-lived credentials;
- immutable artifact references;
- policy and pipeline configuration in version control;
- progressive enforcement;
- auditable exceptions;
- runtime feedback into engineering;
- regression tests for escaped vulnerabilities;
- tested incident and recovery workflows.

---


## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Kubernetes Security Purpose

### Objective

Validate **Kubernetes Security Purpose** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 2 — Cluster Trust Boundaries

### Objective

Validate **Cluster Trust Boundaries** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 3 — Worker Node

### Objective

Validate **Worker Node** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 4 — API Server

### Objective

Validate **API Server** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 5 — Scheduler

### Objective

Validate **Scheduler** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 6 — kubelet

### Objective

Validate **kubelet** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 7 — CSI Plugin

### Objective

Validate **CSI Plugin** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 8 — API Server Authentication

### Objective

Validate **API Server Authentication** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 9 — Kubernetes RBAC

### Objective

Validate **Kubernetes RBAC** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 10 — ClusterRole

### Objective

Validate **ClusterRole** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 11 — ClusterRoleBinding

### Objective

Validate **ClusterRoleBinding** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 12 — Namespace-Scoped Permissions

### Objective

Validate **Namespace-Scoped Permissions** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 13 — Wildcard RBAC Risk

### Objective

Validate **Wildcard RBAC Risk** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 14 — Pod Exec Permission Risk

### Objective

Validate **Pod Exec Permission Risk** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 15 — ServiceAccount

### Objective

Validate **ServiceAccount** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 16 — automountServiceAccountToken

### Objective

Validate **automountServiceAccountToken** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 17 — Projected Service Account Token

### Objective

Validate **Projected Service Account Token** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 18 — Cloud Provider Workload Identity

### Objective

Validate **Cloud Provider Workload Identity** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
CI / workload
   ↓ signed identity token
platform trust policy
   ↓
short-lived scoped credential
   ↓
cloud / registry / deployment API
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 19 — Short-Lived kubectl Credentials

### Objective

Validate **Short-Lived kubectl Credentials** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 20 — Cluster Admin Risk

### Objective

Validate **Cluster Admin Risk** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 21 — Break-Glass Cluster Access

### Objective

Validate **Break-Glass Cluster Access** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 22 — runAsNonRoot

### Objective

Validate **runAsNonRoot** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```yaml
securityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop: ["ALL"]
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 23 — readOnlyRootFilesystem

### Objective

Validate **readOnlyRootFilesystem** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 24 — seccompProfile

### Objective

Validate **seccompProfile** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 25 — AppArmor Awareness

### Objective

Validate **AppArmor Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 26 — privileged Container

### Objective

Validate **privileged Container** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 27 — hostPID

### Objective

Validate **hostPID** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 28 — hostPath

### Objective

Validate **hostPath** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 29 — Privileged Profile

### Objective

Validate **Privileged Profile** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 30 — Baseline Profile

### Objective

Validate **Baseline Profile** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 31 — Pod Security Admission

### Objective

Validate **Pod Security Admission** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 32 — PSA Enforce

### Objective

Validate **PSA Enforce** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 33 — PSA Warn

### Objective

Validate **PSA Warn** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```bash
kubectl label namespace app   pod-security.kubernetes.io/enforce=restricted   pod-security.kubernetes.io/audit=restricted   pod-security.kubernetes.io/warn=restricted
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 34 — PSS Version Pinning Awareness

### Objective

Validate **PSS Version Pinning Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 35 — Validating Admission Policy Awareness

### Objective

Validate **Validating Admission Policy Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 36 — Kyverno

### Objective

Validate **Kyverno** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 37 — Image Digest Pinning

### Objective

Validate **Image Digest Pinning** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 38 — Image Signature Verification

### Objective

Validate **Image Signature Verification** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 39 — Registry Allowlist

### Objective

Validate **Registry Allowlist** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 40 — Helm Security

### Objective

Validate **Helm Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 41 — Kubernetes Secrets

### Objective

Validate **Kubernetes Secrets** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 42 — Secrets Are Not Encryption by Default Awareness

### Objective

Validate **Secrets Are Not Encryption by Default Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 43 — KMS Provider Awareness

### Objective

Validate **KMS Provider Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 44 — Secrets Store CSI Driver Awareness

### Objective

Validate **Secrets Store CSI Driver Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 45 — ConfigMap vs Secret

### Objective

Validate **ConfigMap vs Secret** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 46 — Backup Encryption

### Objective

Validate **Backup Encryption** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 47 — NetworkPolicy

### Objective

Validate **NetworkPolicy** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 48 — Ingress Policy

### Objective

Validate **Ingress Policy** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 49 — Namespace Selector

### Objective

Validate **Namespace Selector** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 50 — NetworkPolicy Limitations

### Objective

Validate **NetworkPolicy Limitations** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 51 — Service Mesh Awareness

### Objective

Validate **Service Mesh Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 52 — Ingress Security

### Objective

Validate **Ingress Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 53 — LoadBalancer Service Exposure

### Objective

Validate **LoadBalancer Service Exposure** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 54 — API Server Network Exposure

### Objective

Validate **API Server Network Exposure** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 55 — Private Cluster

### Objective

Validate **Private Cluster** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 56 — Node Authorization

### Objective

Validate **Node Authorization** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 57 — etcd Network Isolation

### Objective

Validate **etcd Network Isolation** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 58 — Kubernetes PKI

### Objective

Validate **Kubernetes PKI** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 59 — Node Patch Management

### Objective

Validate **Node Patch Management** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 60 — Avoiding Direct Node Administration

### Objective

Validate **Avoiding Direct Node Administration** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 61 — Audit Policy

### Objective

Validate **Audit Policy** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 62 — Runtime Security

### Objective

Validate **Runtime Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 63 — Suspicious Secret Access

### Objective

Validate **Suspicious Secret Access** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 64 — Unexpected ClusterRoleBinding

### Objective

Validate **Unexpected ClusterRoleBinding** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 65 — Kubernetes Vulnerability Management

### Objective

Validate **Kubernetes Vulnerability Management** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 66 — Kubernetes Incident Response

### Objective

Validate **Kubernetes Incident Response** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 67 — Compromised Pod Response

### Objective

Validate **Compromised Pod Response** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 68 — Compromised Node Response

### Objective

Validate **Compromised Node Response** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 69 — PSS Restricted Coverage

### Objective

Validate **PSS Restricted Coverage** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## Lab 70 — Audit Logging Coverage

### Objective

Validate **Audit Logging Coverage** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

### Procedure

1. Write the expected security requirement.
2. Map the trust boundary.
3. Identify the executing identity.
4. Capture current configuration.
5. Implement or inspect the control.
6. Test an allowed case.
7. Test a denied/noncompliant case.
8. Capture policy, audit, or artifact evidence.
9. Restore the approved state.
10. Add a regression check where useful.

### Starter Example

```text
requirement / threat
     ↓
preventive control
     ↓
automated verification
     ↓
evidence
     ↓
delivery decision
     ↓
runtime feedback
```

### Evidence Template

```text
Lab:
Repository / environment:
Commit:
Identity:
Expected:
Observed:
Policy / scanner:
Artifact / state:
Evidence:
Finding:
Remediation:
Retest:
Exception:
```

---


## 6. Mini Project

Build a controlled **Kubernetes Security** capstone that connects source control, automation identity, policy, evidence, runtime validation, incident response, and remediation. The implementation must use only repositories, clusters, registries, and cloud resources you control.

### Required Deliverables

1. Threat model
2. Trust-boundary diagram
3. Identity model
4. Policy/security configuration
5. Automated checks
6. Artifact/state evidence
7. Logging/audit evidence
8. Exception workflow
9. Incident-response procedure
10. Retest evidence
11. Metrics
12. Architecture decision record

## 7. Recommended Resources

- NIST SP 800-218 SSDF v1.1 — https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF publications/status — https://csrc.nist.gov/projects/ssdf/publications
- OWASP DevSecOps Guideline — https://owasp.org/www-project-devsecops-guideline/
- SLSA v1.2 — https://slsa.dev/spec/v1.2/
- Sigstore — https://docs.sigstore.dev/
- Kubernetes Security — https://kubernetes.io/docs/concepts/security/
- Open Policy Agent — https://www.openpolicyagent.org/docs/

## 8. Certification Relevance

Relevant to DevSecOps engineering, product/application security, platform security, cloud security, software supply-chain security, container/Kubernetes security, and secure infrastructure engineering.

## 9. Common Mistakes & Best Practices

### Common Mistakes

- treating DevSecOps as scanner installation;
- permanent CI/CD admin credentials;
- privileged self-hosted runners processing untrusted code;
- mutable tags without digest/provenance evidence;
- secrets in code, state, images, logs, or caches;
- security gates with no risk logic or exception lifecycle;
- manual runtime changes not reconciled to source.

### Best Practices

- threat-model the delivery platform;
- use short-lived workload identity;
- build once and promote immutable artifacts;
- preserve SBOM/provenance/signature evidence;
- use least privilege;
- test policy before enforcing it broadly;
- feed runtime incidents back into regression controls;
- keep exceptions owned and time-bound.

## 10. Self-Assessment Questions (with short answers)

### Q1. What must you understand about **Kubernetes Security Purpose**?

**Short answer:** Kubernetes Security Purpose belongs to the Cluster Architecture layer of DevSecOps.

### Q2. What must you understand about **Kubernetes Threat Model**?

**Short answer:** Kubernetes Threat Model belongs to the Cluster Architecture layer of DevSecOps.

### Q3. What must you understand about **Cluster Trust Boundaries**?

**Short answer:** Cluster Trust Boundaries belongs to the Cluster Architecture layer of DevSecOps.

### Q4. What must you understand about **Control Plane**?

**Short answer:** Control Plane belongs to the Cluster Architecture layer of DevSecOps.

### Q5. What must you understand about **Worker Node**?

**Short answer:** Worker Node belongs to the Cluster Architecture layer of DevSecOps.

### Q6. What must you understand about **API Server**?

**Short answer:** API Server belongs to the Cluster Architecture layer of DevSecOps.

### Q7. What must you understand about **etcd**?

**Short answer:** etcd belongs to the Cluster Architecture layer of DevSecOps.

### Q8. What must you understand about **Scheduler**?

**Short answer:** Scheduler belongs to the Cluster Architecture layer of DevSecOps.

### Q9. What must you understand about **Controller Manager**?

**Short answer:** Controller Manager belongs to the Cluster Architecture layer of DevSecOps.

### Q10. What must you understand about **kubelet**?

**Short answer:** kubelet belongs to the Cluster Architecture layer of DevSecOps.

### Q11. What must you understand about **CNI Plugin**?

**Short answer:** CNI Plugin belongs to the Cluster Architecture layer of DevSecOps.

### Q12. What must you understand about **CSI Plugin**?

**Short answer:** CSI Plugin belongs to the Cluster Architecture layer of DevSecOps.

### Q13. What must you understand about **API Server Authentication**?

**Short answer:** API Server Authentication belongs to the Authentication and RBAC layer of DevSecOps.

### Q14. What must you understand about **API Server Authorization**?

**Short answer:** API Server Authorization belongs to the Authentication and RBAC layer of DevSecOps.

### Q15. What must you understand about **Kubernetes RBAC**?

**Short answer:** Kubernetes RBAC belongs to the Authentication and RBAC layer of DevSecOps.

### Q16. What must you understand about **Role**?

**Short answer:** Role belongs to the Authentication and RBAC layer of DevSecOps.

### Q17. What must you understand about **ClusterRole**?

**Short answer:** ClusterRole belongs to the Authentication and RBAC layer of DevSecOps.

### Q18. What must you understand about **RoleBinding**?

**Short answer:** RoleBinding belongs to the Authentication and RBAC layer of DevSecOps.

### Q19. What must you understand about **ClusterRoleBinding**?

**Short answer:** ClusterRoleBinding belongs to the Authentication and RBAC layer of DevSecOps.

### Q20. What must you understand about **Namespace-Scoped Permissions**?

**Short answer:** Namespace-Scoped Permissions belongs to the Authentication and RBAC layer of DevSecOps.

### Q21. What must you understand about **Least Privilege RBAC**?

**Short answer:** Least Privilege RBAC belongs to the Authentication and RBAC layer of DevSecOps.

### Q22. What must you understand about **Wildcard RBAC Risk**?

**Short answer:** Wildcard RBAC Risk belongs to the Authentication and RBAC layer of DevSecOps.

### Q23. What must you understand about **Secrets Permission Risk**?

**Short answer:** Secrets Permission Risk belongs to the Authentication and RBAC layer of DevSecOps.

### Q24. What must you understand about **Pod Exec Permission Risk**?

**Short answer:** Pod Exec Permission Risk belongs to the Authentication and RBAC layer of DevSecOps.

### Q25. What must you understand about **RBAC Privilege Escalation Paths**?

**Short answer:** RBAC Privilege Escalation Paths belongs to the Authentication and RBAC layer of DevSecOps.

### Q26. What must you understand about **ServiceAccount**?

**Short answer:** ServiceAccount belongs to the Service Accounts and Identity layer of DevSecOps.

### Q27. What must you understand about **Default ServiceAccount**?

**Short answer:** Default ServiceAccount belongs to the Service Accounts and Identity layer of DevSecOps.

### Q28. What must you understand about **automountServiceAccountToken**?

**Short answer:** automountServiceAccountToken belongs to the Service Accounts and Identity layer of DevSecOps.

### Q29. What must you understand about **Projected Service Account Token**?

**Short answer:** Projected Service Account Token belongs to the Service Accounts and Identity layer of DevSecOps.

### Q30. What must you understand about **Workload Identity Federation**?

**Short answer:** Workload Identity Federation belongs to the Service Accounts and Identity layer of DevSecOps.

### Q31. What must you understand about **Cloud Provider Workload Identity**?

**Short answer:** Cloud Provider Workload Identity belongs to the Service Accounts and Identity layer of DevSecOps.

### Q32. What must you understand about **OIDC Authentication**?

**Short answer:** OIDC Authentication belongs to the Service Accounts and Identity layer of DevSecOps.

### Q33. What must you understand about **Short-Lived kubectl Credentials**?

**Short answer:** Short-Lived kubectl Credentials belongs to the Service Accounts and Identity layer of DevSecOps.

### Q34. What must you understand about **kubeconfig Security**?

**Short answer:** kubeconfig Security belongs to the Service Accounts and Identity layer of DevSecOps.

### Q35. What must you understand about **Cluster Admin Risk**?

**Short answer:** Cluster Admin Risk belongs to the Service Accounts and Identity layer of DevSecOps.

### Q36. What must you understand about **Break-Glass Cluster Access**?

**Short answer:** Break-Glass Cluster Access belongs to the Service Accounts and Identity layer of DevSecOps.

### Q37. What must you understand about **Pod Security Context**?

**Short answer:** Pod Security Context belongs to the Pod Hardening layer of DevSecOps.

### Q38. What must you understand about **runAsNonRoot**?

**Short answer:** runAsNonRoot belongs to the Pod Hardening layer of DevSecOps.

### Q39. What must you understand about **allowPrivilegeEscalation**?

**Short answer:** allowPrivilegeEscalation belongs to the Pod Hardening layer of DevSecOps.

### Q40. What must you understand about **readOnlyRootFilesystem**?

**Short answer:** readOnlyRootFilesystem belongs to the Pod Hardening layer of DevSecOps.

### Q41. What must you understand about **Linux Capabilities**?

**Short answer:** Linux Capabilities belongs to the Pod Hardening layer of DevSecOps.

### Q42. What must you understand about **seccompProfile**?

**Short answer:** seccompProfile belongs to the Pod Hardening layer of DevSecOps.

### Q43. What must you understand about **AppArmor Awareness**?

**Short answer:** AppArmor Awareness belongs to the Pod Hardening layer of DevSecOps.

### Q44. What must you understand about **SELinux Awareness**?

**Short answer:** SELinux Awareness belongs to the Pod Hardening layer of DevSecOps.

### Q45. What must you understand about **privileged Container**?

**Short answer:** privileged Container belongs to the Pod Hardening layer of DevSecOps.

### Q46. What must you understand about **hostNetwork**?

**Short answer:** hostNetwork belongs to the Pod Hardening layer of DevSecOps.

### Q47. What must you understand about **hostPID**?

**Short answer:** hostPID belongs to the Pod Hardening layer of DevSecOps.

### Q48. What must you understand about **hostIPC**?

**Short answer:** hostIPC belongs to the Pod Hardening layer of DevSecOps.

### Q49. What must you understand about **hostPath**?

**Short answer:** hostPath belongs to the Pod Hardening layer of DevSecOps.

### Q50. What must you understand about **Pod Security Standards**?

**Short answer:** Kubernetes Pod Security Standards define three cumulative security profiles—Privileged, Baseline, and Restricted—for common Pod hardening expectations.

### Q51. What must you understand about **Privileged Profile**?

**Short answer:** Privileged Profile belongs to the Pod Security Standards layer of DevSecOps.

### Q52. What must you understand about **Baseline Profile**?

**Short answer:** Baseline Profile belongs to the Pod Security Standards layer of DevSecOps.

### Q53. What must you understand about **Restricted Profile**?

**Short answer:** Restricted Profile belongs to the Pod Security Standards layer of DevSecOps.

### Q54. What must you understand about **Pod Security Admission**?

**Short answer:** Pod Security Admission belongs to the Pod Security Standards layer of DevSecOps.

### Q55. What must you understand about **Namespace PSA Labels**?

**Short answer:** Namespace PSA Labels belongs to the Pod Security Standards layer of DevSecOps.

### Q56. What must you understand about **PSA Enforce**?

**Short answer:** PSA Enforce belongs to the Pod Security Standards layer of DevSecOps.

### Q57. What must you understand about **PSA Audit**?

**Short answer:** PSA Audit belongs to the Pod Security Standards layer of DevSecOps.

### Q58. What must you understand about **PSA Warn**?

**Short answer:** PSA Warn belongs to the Pod Security Standards layer of DevSecOps.

### Q59. What must you understand about **PSS Version Pinning Awareness**?

**Short answer:** PSS Version Pinning Awareness belongs to the Pod Security Standards layer of DevSecOps.

### Q60. What must you understand about **Admission Control**?

**Short answer:** Admission Control belongs to the Admission and Supply Chain layer of DevSecOps.

### Q61. What must you understand about **Validating Admission Policy Awareness**?

**Short answer:** Validating Admission Policy Awareness belongs to the Admission and Supply Chain layer of DevSecOps.

### Q62. What must you understand about **OPA Gatekeeper**?

**Short answer:** OPA Gatekeeper belongs to the Admission and Supply Chain layer of DevSecOps.

### Q63. What must you understand about **Kyverno**?

**Short answer:** Kyverno belongs to the Admission and Supply Chain layer of DevSecOps.

### Q64. What must you understand about **Policy Exceptions**?

**Short answer:** Policy Exceptions belongs to the Admission and Supply Chain layer of DevSecOps.

### Q65. What must you understand about **Image Digest Pinning**?

**Short answer:** Image Digest Pinning belongs to the Admission and Supply Chain layer of DevSecOps.

### Q66. What must you understand about **Image Signature Verification**?

**Short answer:** Image Signature Verification belongs to the Admission and Supply Chain layer of DevSecOps.

### Q67. What must you understand about **Cosign in Kubernetes Awareness**?

**Short answer:** Cosign in Kubernetes Awareness belongs to the Admission and Supply Chain layer of DevSecOps.

### Q68. What must you understand about **Registry Allowlist**?

**Short answer:** Registry Allowlist belongs to the Admission and Supply Chain layer of DevSecOps.

### Q69. What must you understand about **Private Registry**?

**Short answer:** Private Registry belongs to the Admission and Supply Chain layer of DevSecOps.

### Q70. What must you understand about **Helm Security**?

**Short answer:** Helm Security belongs to the Admission and Supply Chain layer of DevSecOps.

### Q71. What must you understand about **GitOps Repository Trust**?

**Short answer:** GitOps Repository Trust belongs to the Admission and Supply Chain layer of DevSecOps.

### Q72. What must you understand about **Kubernetes Secrets**?

**Short answer:** Kubernetes Secrets belongs to the Secrets and Data layer of DevSecOps.

### Q73. What must you understand about **Secrets Are Not Encryption by Default Awareness**?

**Short answer:** Secrets Are Not Encryption by Default Awareness belongs to the Secrets and Data layer of DevSecOps.

### Q74. What must you understand about **etcd Encryption at Rest**?

**Short answer:** etcd Encryption at Rest belongs to the Secrets and Data layer of DevSecOps.

### Q75. What must you understand about **KMS Provider Awareness**?

**Short answer:** KMS Provider Awareness belongs to the Secrets and Data layer of DevSecOps.

### Q76. What must you understand about **External Secrets**?

**Short answer:** External Secrets belongs to the Secrets and Data layer of DevSecOps.

### Q77. What must you understand about **Secrets Store CSI Driver Awareness**?

**Short answer:** Secrets Store CSI Driver Awareness belongs to the Secrets and Data layer of DevSecOps.

### Q78. What must you understand about **Secret Rotation**?

**Short answer:** Secret Rotation belongs to the Secrets and Data layer of DevSecOps.

### Q79. What must you understand about **ConfigMap vs Secret**?

**Short answer:** ConfigMap vs Secret belongs to the Secrets and Data layer of DevSecOps.

### Q80. What must you understand about **Persistent Volume Security**?

**Short answer:** Persistent Volume Security belongs to the Secrets and Data layer of DevSecOps.

### Q81. What must you understand about **Backup Encryption**?

**Short answer:** Backup Encryption belongs to the Secrets and Data layer of DevSecOps.

### Q82. What must you understand about **NetworkPolicy**?

**Short answer:** NetworkPolicy belongs to the Network Security layer of DevSecOps.

### Q83. What must you understand about **Default Deny NetworkPolicy**?

**Short answer:** Default Deny NetworkPolicy belongs to the Network Security layer of DevSecOps.

### Q84. What must you understand about **Ingress Policy**?

**Short answer:** Ingress Policy belongs to the Network Security layer of DevSecOps.

### Q85. What must you understand about **Egress Policy**?

**Short answer:** Egress Policy belongs to the Network Security layer of DevSecOps.

### Q86. What must you understand about **Namespace Selector**?

**Short answer:** Namespace Selector belongs to the Network Security layer of DevSecOps.

### Q87. What must you understand about **Pod Selector**?

**Short answer:** Pod Selector belongs to the Network Security layer of DevSecOps.

### Q88. What must you understand about **NetworkPolicy Limitations**?

**Short answer:** NetworkPolicy Limitations belongs to the Network Security layer of DevSecOps.

### Q89. What must you understand about **Service Mesh Awareness**?

**Short answer:** Service Mesh Awareness belongs to the Network Security layer of DevSecOps.

### Q90. What must you understand about **mTLS Between Workloads**?

**Short answer:** mTLS Between Workloads belongs to the Network Security layer of DevSecOps.

### Q91. What must you understand about **Ingress Security**?

**Short answer:** Ingress Security belongs to the Network Security layer of DevSecOps.

### Q92. What must you understand about **TLS at Ingress**?

**Short answer:** TLS at Ingress belongs to the Network Security layer of DevSecOps.

### Q93. What must you understand about **LoadBalancer Service Exposure**?

**Short answer:** LoadBalancer Service Exposure belongs to the Network Security layer of DevSecOps.

### Q94. What must you understand about **NodePort Exposure**?

**Short answer:** NodePort Exposure belongs to the Network Security layer of DevSecOps.

### Q95. What must you understand about **API Server Network Exposure**?

**Short answer:** API Server Network Exposure belongs to the Control Plane and Nodes layer of DevSecOps.

### Q96. What must you understand about **Private Cluster**?

**Short answer:** Private Cluster belongs to the Control Plane and Nodes layer of DevSecOps.

### Q97. What must you understand about **Kubelet Security**?

**Short answer:** Kubelet Security belongs to the Control Plane and Nodes layer of DevSecOps.

### Q98. What must you understand about **Node Authorization**?

**Short answer:** Node Authorization belongs to the Control Plane and Nodes layer of DevSecOps.

### Q99. What must you understand about **NodeRestriction Admission**?

**Short answer:** NodeRestriction Admission belongs to the Control Plane and Nodes layer of DevSecOps.

### Q100. What must you understand about **etcd Network Isolation**?

**Short answer:** etcd Network Isolation belongs to the Control Plane and Nodes layer of DevSecOps.

### Q101. What must you understand about **Control Plane Certificate Management**?

**Short answer:** Control Plane Certificate Management belongs to the Control Plane and Nodes layer of DevSecOps.

### Q102. What must you understand about **Kubernetes PKI**?

**Short answer:** Kubernetes PKI belongs to the Control Plane and Nodes layer of DevSecOps.

### Q103. What must you understand about **Node Hardening**?

**Short answer:** Node Hardening belongs to the Control Plane and Nodes layer of DevSecOps.

### Q104. What must you understand about **Node Patch Management**?

**Short answer:** Node Patch Management belongs to the Control Plane and Nodes layer of DevSecOps.

### Q105. What must you understand about **Avoiding Direct Node Administration**?

**Short answer:** Avoiding Direct Node Administration belongs to the Control Plane and Nodes layer of DevSecOps.

### Q106. What must you understand about **Kubernetes Audit Logging**?

**Short answer:** Kubernetes Audit Logging belongs to the Monitoring and IR layer of DevSecOps.

### Q107. What must you understand about **Audit Policy**?

**Short answer:** Audit Policy belongs to the Monitoring and IR layer of DevSecOps.

### Q108. What must you understand about **Centralized Audit Logs**?

**Short answer:** Centralized Audit Logs belongs to the Monitoring and IR layer of DevSecOps.

### Q109. What must you understand about **Runtime Security**?

**Short answer:** Runtime Security belongs to the Monitoring and IR layer of DevSecOps.

### Q110. What must you understand about **Suspicious kubectl exec**?

**Short answer:** Suspicious kubectl exec belongs to the Monitoring and IR layer of DevSecOps.

### Q111. What must you understand about **Suspicious Secret Access**?

**Short answer:** Suspicious Secret Access belongs to the Monitoring and IR layer of DevSecOps.

### Q112. What must you understand about **Unexpected ClusterRoleBinding**?

**Short answer:** Unexpected ClusterRoleBinding belongs to the Monitoring and IR layer of DevSecOps.

### Q113. What must you understand about **Unexpected Privileged Pod**?

**Short answer:** Unexpected Privileged Pod belongs to the Monitoring and IR layer of DevSecOps.

### Q114. What must you understand about **Kubernetes Vulnerability Management**?

**Short answer:** Kubernetes Vulnerability Management belongs to the Monitoring and IR layer of DevSecOps.

### Q115. What must you understand about **Cluster Version Management**?

**Short answer:** Cluster Version Management belongs to the Monitoring and IR layer of DevSecOps.

### Q116. What must you understand about **Kubernetes Incident Response**?

**Short answer:** Kubernetes Incident Response belongs to the Monitoring and IR layer of DevSecOps.

### Q117. What must you understand about **Compromised ServiceAccount Response**?

**Short answer:** Compromised ServiceAccount Response belongs to the Monitoring and IR layer of DevSecOps.

### Q118. What must you understand about **Compromised Pod Response**?

**Short answer:** Compromised Pod Response belongs to the Monitoring and IR layer of DevSecOps.

### Q119. What must you understand about **Compromised Node Response**?

**Short answer:** Compromised Node Response belongs to the Monitoring and IR layer of DevSecOps.

### Q120. What must you understand about **Cluster Rebuild Decision**?

**Short answer:** Cluster Rebuild Decision belongs to the Monitoring and IR layer of DevSecOps.

### Q121. What must you understand about **PSS Restricted Coverage**?

**Short answer:** PSS Restricted Coverage belongs to the Monitoring and IR layer of DevSecOps.

### Q122. What must you understand about **NetworkPolicy Coverage**?

**Short answer:** NetworkPolicy Coverage belongs to the Monitoring and IR layer of DevSecOps.

### Q123. What must you understand about **Audit Logging Coverage**?

**Short answer:** Audit Logging Coverage belongs to the Monitoring and IR layer of DevSecOps.

## Completion Gate

You are complete when you can explain why a change is trusted from **source → pipeline → artifact/state → deployment → runtime → monitoring → feedback**.
