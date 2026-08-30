# 117. DevSecOps CI/CD Security

> Phase 30 — DevSecOps

## 1. Topic Title

**DevSecOps CI/CD Security**

## 2. Learning Objectives

- Threat-model repository, CI, runner, builder, registry, deployment, and production boundaries.
- Use short-lived pipeline identities instead of permanent cloud credentials.
- Protect untrusted pull requests, third-party workflow code, caches, secrets, and self-hosted runners.
- Generate/verify SBOM, signatures, provenance, and SLSA evidence.
- Build once, promote immutable artifacts, enforce environment policy, monitor the pipeline, and recover from compromise.

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

Complete Course 116 first.

## 4. Core Concepts Explanation

# Part 1 — CI/CD Security Purpose

### Core Concept

CI/CD Security Purpose belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **CI/CD Security Purpose** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 2 — Pipeline as High-Privilege System

### Core Concept

Pipeline as High-Privilege System belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pipeline as High-Privilege System** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 3 — CI/CD Threat Model

### Core Concept

CI/CD Threat Model belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **CI/CD Threat Model** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 4 — Source Repository Trust Boundary

### Core Concept

Source Repository Trust Boundary belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Source Repository Trust Boundary** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 5 — Build System Trust Boundary

### Core Concept

Build System Trust Boundary belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Build System Trust Boundary** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 6 — Artifact Registry Trust Boundary

### Core Concept

Artifact Registry Trust Boundary belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Registry Trust Boundary** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 7 — Deployment Trust Boundary

### Core Concept

Deployment Trust Boundary belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Deployment Trust Boundary** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 8 — Production Trust Boundary

### Core Concept

Production Trust Boundary belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Production Trust Boundary** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 9 — Developer Account Compromise

### Core Concept

Developer Account Compromise belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Developer Account Compromise** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 10 — Runner Compromise

### Core Concept

Runner Compromise belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runner Compromise** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 11 — Dependency Compromise

### Core Concept

Dependency Compromise belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Dependency Compromise** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 12 — Artifact Tampering

### Core Concept

Artifact Tampering belongs to the **Pipeline Threat Model** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Tampering** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 13 — Protected Branch

### Core Concept

Protected Branch belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Protected Branch** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
feature branch
   ↓ pull request
required checks
   ↓
review / CODEOWNER
   ↓
protected main
   ↓
trusted build
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


# Part 14 — Protected Tag

### Core Concept

Protected Tag belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Protected Tag** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 15 — Mandatory Review

### Core Concept

Mandatory Review belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Mandatory Review** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
feature branch
   ↓ pull request
required checks
   ↓
review / CODEOWNER
   ↓
protected main
   ↓
trusted build
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


# Part 16 — CODEOWNERS

### Core Concept

CODEOWNERS belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **CODEOWNERS** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
feature branch
   ↓ pull request
required checks
   ↓
review / CODEOWNER
   ↓
protected main
   ↓
trusted build
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


# Part 17 — Two-Person Approval

### Core Concept

Two-Person Approval belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Two-Person Approval** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 18 — Commit Signing Awareness

### Core Concept

Commit Signing Awareness belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Commit Signing Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 19 — Release Tag Security

### Core Concept

Release Tag Security belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Release Tag Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 20 — Untrusted Pull Request Risk

### Core Concept

Untrusted Pull Request Risk belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Untrusted Pull Request Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 21 — Fork Pull Request Risk

### Core Concept

Fork Pull Request Risk belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Fork Pull Request Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 22 — Third-Party Workflow Risk

### Core Concept

Third-Party Workflow Risk belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Third-Party Workflow Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 23 — Pinned Workflow Versions

### Core Concept

Pinned Workflow Versions belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pinned Workflow Versions** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 24 — Commit SHA Pinning

### Core Concept

Commit SHA Pinning belongs to the **Repository Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Commit SHA Pinning** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 25 — Hosted Runner Security Model

### Core Concept

Hosted Runner Security Model belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Hosted Runner Security Model** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 26 — Self-Hosted Runner Risk

### Core Concept

Self-Hosted Runner Risk belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Self-Hosted Runner Risk** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 27 — Ephemeral Runner

### Core Concept

Ephemeral Runner belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Ephemeral Runner** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 28 — Runner Isolation

### Core Concept

Runner Isolation belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runner Isolation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 29 — Runner Network Segmentation

### Core Concept

Runner Network Segmentation belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runner Network Segmentation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 30 — Runner Egress Control

### Core Concept

Runner Egress Control belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runner Egress Control** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 31 — Runner Cache Security

### Core Concept

Runner Cache Security belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runner Cache Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 32 — Build Cache Poisoning

### Core Concept

Build Cache Poisoning belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Build Cache Poisoning** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 33 — Workspace Cleanup

### Core Concept

Workspace Cleanup belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Workspace Cleanup** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 34 — Temporary File Security

### Core Concept

Temporary File Security belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Temporary File Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 35 — Pipeline Logs and Secret Leakage

### Core Concept

Pipeline Logs and Secret Leakage belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pipeline Logs and Secret Leakage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 36 — Runner Patch Compliance

### Core Concept

Runner Patch Compliance belongs to the **Runner Security** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Runner Patch Compliance** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 37 — OIDC Federation for CI/CD

### Core Concept

OIDC Federation for CI/CD belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **OIDC Federation for CI/CD** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 38 — Workload Identity Federation

### Core Concept

Workload Identity Federation belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

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


# Part 39 — Short-Lived Cloud Credentials

### Core Concept

Short-Lived Cloud Credentials belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Short-Lived Cloud Credentials** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 40 — Least Privilege Pipeline Role

### Core Concept

Least Privilege Pipeline Role belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Least Privilege Pipeline Role** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 41 — Environment-Specific Pipeline Identity

### Core Concept

Environment-Specific Pipeline Identity belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Environment-Specific Pipeline Identity** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 42 — Production Deployment Identity

### Core Concept

Production Deployment Identity belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Production Deployment Identity** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 43 — Separate Build and Deploy Roles

### Core Concept

Separate Build and Deploy Roles belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Separate Build and Deploy Roles** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 44 — Secret Manager Integration

### Core Concept

Secret Manager Integration belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Secret Manager Integration** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 45 — Pipeline Secret Rotation

### Core Concept

Pipeline Secret Rotation belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pipeline Secret Rotation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 46 — Avoiding Static Cloud Keys

### Core Concept

Avoiding Static Cloud Keys belongs to the **Pipeline Identity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Avoiding Static Cloud Keys** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 47 — Immutable Artifact

### Core Concept

Immutable Artifact belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Immutable Artifact** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 48 — Artifact Digest

### Core Concept

Artifact Digest belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Digest** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 49 — Image Digest Pinning

### Core Concept

Image Digest Pinning belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

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


# Part 50 — Build Once Promote Many

### Core Concept

Build Once Promote Many belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Build Once Promote Many** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 51 — Promotion of Immutable Artifact

### Core Concept

Promotion of Immutable Artifact belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Promotion of Immutable Artifact** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 52 — Artifact Repository Immutability

### Core Concept

Artifact Repository Immutability belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Repository Immutability** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 53 — Artifact Retention

### Core Concept

Artifact Retention belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Retention** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 54 — Artifact Quarantine

### Core Concept

Artifact Quarantine belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Quarantine** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 55 — Release Manifest

### Core Concept

Release Manifest belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Release Manifest** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 56 — Release Evidence

### Core Concept

Release Evidence belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Release Evidence** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 57 — Rollback Artifact Integrity

### Core Concept

Rollback Artifact Integrity belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Rollback Artifact Integrity** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 58 — Trusted Builder

### Core Concept

Trusted Builder belongs to the **Build Integrity** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Trusted Builder** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 59 — SLSA Version 1.2

### Core Concept

SLSA Version 1.2 is the current approved specification and includes Build and Source tracks for improving software supply-chain security.

### Detailed Explanation

Treat **SLSA Version 1.2** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 60 — SLSA Build Track

### Core Concept

SLSA Build Track belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SLSA Build Track** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 61 — SLSA Source Track

### Core Concept

SLSA Source Track belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SLSA Source Track** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 62 — Provenance Attestation

### Core Concept

Provenance Attestation belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Provenance Attestation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 63 — Verification Summary Attestation Awareness

### Core Concept

Verification Summary Attestation Awareness belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Verification Summary Attestation Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 64 — in-toto Attestation Awareness

### Core Concept

in-toto Attestation Awareness belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **in-toto Attestation Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 65 — SBOM Generation

### Core Concept

SBOM Generation belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SBOM Generation** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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


# Part 66 — CycloneDX SBOM

### Core Concept

CycloneDX SBOM belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **CycloneDX SBOM** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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


# Part 67 — SPDX SBOM

### Core Concept

SPDX SBOM belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SPDX SBOM** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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


# Part 68 — Artifact Signing

### Core Concept

Artifact Signing belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Signing** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 69 — Cosign

### Core Concept

Cosign belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Cosign** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 70 — Keyless Signing

### Core Concept

Keyless Signing belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Keyless Signing** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 71 — Artifact Verification

### Core Concept

Artifact Verification belongs to the **Supply Chain Evidence** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Verification** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 72 — SAST in Pipeline

### Core Concept

SAST in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SAST in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 73 — SCA in Pipeline

### Core Concept

SCA in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SCA in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 74 — Secret Scanning in Pipeline

### Core Concept

Secret Scanning in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Secret Scanning in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 75 — IaC Scanning in Pipeline

### Core Concept

IaC Scanning in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **IaC Scanning in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 76 — Container Scanning in Pipeline

### Core Concept

Container Scanning in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Container Scanning in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 77 — DAST in Pipeline

### Core Concept

DAST in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **DAST in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 78 — API Security Tests in Pipeline

### Core Concept

API Security Tests in Pipeline belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **API Security Tests in Pipeline** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 79 — Fuzzing Awareness

### Core Concept

Fuzzing Awareness belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Fuzzing Awareness** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 80 — License Compliance Gate

### Core Concept

License Compliance Gate belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **License Compliance Gate** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 81 — Fast Feedback Stage

### Core Concept

Fast Feedback Stage belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Fast Feedback Stage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 82 — Deep Security Stage

### Core Concept

Deep Security Stage belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Deep Security Stage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 83 — Pre-Merge Security Checks

### Core Concept

Pre-Merge Security Checks belongs to the **Security Tests** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pre-Merge Security Checks** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 84 — Pre-Deployment Security Gate

### Core Concept

Pre-Deployment Security Gate belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pre-Deployment Security Gate** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 85 — Environment Protection Rules

### Core Concept

Environment Protection Rules belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Environment Protection Rules** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 86 — Manual Approval

### Core Concept

Manual Approval belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Manual Approval** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 87 — Deployment Approval

### Core Concept

Deployment Approval belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Deployment Approval** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 88 — Progressive Delivery

### Core Concept

Progressive Delivery belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Progressive Delivery** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 89 — Canary Deployment Security

### Core Concept

Canary Deployment Security belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Canary Deployment Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 90 — Blue-Green Deployment Security

### Core Concept

Blue-Green Deployment Security belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Blue-Green Deployment Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 91 — Feature Flag Security

### Core Concept

Feature Flag Security belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Feature Flag Security** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 92 — Policy as Code Gate

### Core Concept

Policy as Code Gate belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Policy as Code Gate** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 93 — Admission Policy Integration

### Core Concept

Admission Policy Integration belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Admission Policy Integration** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 94 — Terraform Plan Security Review

### Core Concept

Terraform Plan Security Review belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Terraform Plan Security Review** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
feature branch
   ↓ pull request
required checks
   ↓
review / CODEOWNER
   ↓
protected main
   ↓
trusted build
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


# Part 95 — Production Break-Glass

### Core Concept

Production Break-Glass belongs to the **Deployment Controls** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Production Break-Glass** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 96 — Pipeline Audit Logging

### Core Concept

Pipeline Audit Logging belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pipeline Audit Logging** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 97 — SCM Audit Logging

### Core Concept

SCM Audit Logging belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SCM Audit Logging** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 98 — Artifact Registry Audit Logging

### Core Concept

Artifact Registry Audit Logging belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Artifact Registry Audit Logging** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 99 — Deployment Log Integrity

### Core Concept

Deployment Log Integrity belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Deployment Log Integrity** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 100 — Suspicious Pipeline Behavior

### Core Concept

Suspicious Pipeline Behavior belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Suspicious Pipeline Behavior** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 101 — Unexpected Secret Access

### Core Concept

Unexpected Secret Access belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Unexpected Secret Access** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 102 — Unexpected Runner Egress

### Core Concept

Unexpected Runner Egress belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Unexpected Runner Egress** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 103 — Pipeline Incident Response

### Core Concept

Pipeline Incident Response belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pipeline Incident Response** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 104 — Revoke Pipeline Credentials

### Core Concept

Revoke Pipeline Credentials belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Revoke Pipeline Credentials** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 105 — Quarantine Artifact

### Core Concept

Quarantine Artifact belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Quarantine Artifact** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 106 — Rebuild from Trusted Source

### Core Concept

Rebuild from Trusted Source belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Rebuild from Trusted Source** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 107 — Pipeline Disaster Recovery

### Core Concept

Pipeline Disaster Recovery belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Pipeline Disaster Recovery** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 108 — Signed Build Percentage

### Core Concept

Signed Build Percentage belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Signed Build Percentage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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


# Part 109 — Provenance Coverage

### Core Concept

Provenance Coverage belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **Provenance Coverage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


# Part 110 — SBOM Coverage

### Core Concept

SBOM Coverage belongs to the **Monitoring and Recovery** layer of DevSecOps. It should be implemented as a repeatable engineering control with a defined threat, owner, enforcement point, evidence source, exception path, and remediation workflow.

### Detailed Explanation

Treat **SBOM Coverage** as part of the end-to-end trusted delivery chain rather than an isolated product feature. Identify the asset, threat, identity, trust boundary, control owner, enforcement location, evidence source, and failure/recovery path.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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

## Lab 1 — CI/CD Security Purpose

### Objective

Validate **CI/CD Security Purpose** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 2 — CI/CD Threat Model

### Objective

Validate **CI/CD Threat Model** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 3 — Source Repository Trust Boundary

### Objective

Validate **Source Repository Trust Boundary** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 4 — Artifact Registry Trust Boundary

### Objective

Validate **Artifact Registry Trust Boundary** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 5 — Deployment Trust Boundary

### Objective

Validate **Deployment Trust Boundary** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 6 — Developer Account Compromise

### Objective

Validate **Developer Account Compromise** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 7 — Runner Compromise

### Objective

Validate **Runner Compromise** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 8 — Artifact Tampering

### Objective

Validate **Artifact Tampering** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 9 — Protected Tag

### Objective

Validate **Protected Tag** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 10 — Mandatory Review

### Objective

Validate **Mandatory Review** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
feature branch
   ↓ pull request
required checks
   ↓
review / CODEOWNER
   ↓
protected main
   ↓
trusted build
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


## Lab 11 — Two-Person Approval

### Objective

Validate **Two-Person Approval** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 12 — Commit Signing Awareness

### Objective

Validate **Commit Signing Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
# Verify an artifact in a registry you control
cosign verify <registry>/<image>@sha256:<digest>
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


## Lab 13 — Untrusted Pull Request Risk

### Objective

Validate **Untrusted Pull Request Risk** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 14 — Third-Party Workflow Risk

### Objective

Validate **Third-Party Workflow Risk** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 15 — Pinned Workflow Versions

### Objective

Validate **Pinned Workflow Versions** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 16 — Hosted Runner Security Model

### Objective

Validate **Hosted Runner Security Model** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 17 — Self-Hosted Runner Risk

### Objective

Validate **Self-Hosted Runner Risk** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 18 — Runner Isolation

### Objective

Validate **Runner Isolation** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 19 — Runner Network Segmentation

### Objective

Validate **Runner Network Segmentation** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 20 — Runner Cache Security

### Objective

Validate **Runner Cache Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 21 — Workspace Cleanup

### Objective

Validate **Workspace Cleanup** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 22 — Temporary File Security

### Objective

Validate **Temporary File Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 23 — Runner Patch Compliance

### Objective

Validate **Runner Patch Compliance** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 24 — OIDC Federation for CI/CD

### Objective

Validate **OIDC Federation for CI/CD** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 25 — Short-Lived Cloud Credentials

### Objective

Validate **Short-Lived Cloud Credentials** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 26 — Least Privilege Pipeline Role

### Objective

Validate **Least Privilege Pipeline Role** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 27 — Production Deployment Identity

### Objective

Validate **Production Deployment Identity** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 28 — Secret Manager Integration

### Objective

Validate **Secret Manager Integration** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 29 — Pipeline Secret Rotation

### Objective

Validate **Pipeline Secret Rotation** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 30 — Immutable Artifact

### Objective

Validate **Immutable Artifact** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 31 — Artifact Digest

### Objective

Validate **Artifact Digest** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 32 — Build Once Promote Many

### Objective

Validate **Build Once Promote Many** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 33 — Artifact Repository Immutability

### Objective

Validate **Artifact Repository Immutability** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 34 — Artifact Retention

### Objective

Validate **Artifact Retention** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 35 — Release Manifest

### Objective

Validate **Release Manifest** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 36 — Release Evidence

### Objective

Validate **Release Evidence** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 37 — Trusted Builder

### Objective

Validate **Trusted Builder** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 38 — SLSA Version 1.2

### Objective

Validate **SLSA Version 1.2** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


## Lab 39 — SLSA Source Track

### Objective

Validate **SLSA Source Track** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


## Lab 40 — Verification Summary Attestation Awareness

### Objective

Validate **Verification Summary Attestation Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


## Lab 41 — in-toto Attestation Awareness

### Objective

Validate **in-toto Attestation Awareness** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
source revision
   ↓ controlled build
artifact + provenance
   ↓ verification
trusted promotion
   ↓ deployment
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


## Lab 42 — CycloneDX SBOM

### Objective

Validate **CycloneDX SBOM** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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


## Lab 43 — SPDX SBOM

### Objective

Validate **SPDX SBOM** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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


## Lab 44 — Cosign

### Objective

Validate **Cosign** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
# Verify an artifact in a registry you control
cosign verify <registry>/<image>@sha256:<digest>
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


## Lab 45 — Artifact Verification

### Objective

Validate **Artifact Verification** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 46 — SAST in Pipeline

### Objective

Validate **SAST in Pipeline** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 47 — Secret Scanning in Pipeline

### Objective

Validate **Secret Scanning in Pipeline** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 48 — IaC Scanning in Pipeline

### Objective

Validate **IaC Scanning in Pipeline** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 49 — DAST in Pipeline

### Objective

Validate **DAST in Pipeline** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 50 — API Security Tests in Pipeline

### Objective

Validate **API Security Tests in Pipeline** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 51 — License Compliance Gate

### Objective

Validate **License Compliance Gate** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 52 — Deep Security Stage

### Objective

Validate **Deep Security Stage** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 53 — Pre-Merge Security Checks

### Objective

Validate **Pre-Merge Security Checks** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 54 — Environment Protection Rules

### Objective

Validate **Environment Protection Rules** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 55 — Manual Approval

### Objective

Validate **Manual Approval** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 56 — Progressive Delivery

### Objective

Validate **Progressive Delivery** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 57 — Canary Deployment Security

### Objective

Validate **Canary Deployment Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 58 — Feature Flag Security

### Objective

Validate **Feature Flag Security** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 59 — Admission Policy Integration

### Objective

Validate **Admission Policy Integration** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 60 — Terraform Plan Security Review

### Objective

Validate **Terraform Plan Security Review** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
feature branch
   ↓ pull request
required checks
   ↓
review / CODEOWNER
   ↓
protected main
   ↓
trusted build
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


## Lab 61 — Pipeline Audit Logging

### Objective

Validate **Pipeline Audit Logging** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 62 — SCM Audit Logging

### Objective

Validate **SCM Audit Logging** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 63 — Deployment Log Integrity

### Objective

Validate **Deployment Log Integrity** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 64 — Unexpected Secret Access

### Objective

Validate **Unexpected Secret Access** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 65 — Unexpected Runner Egress

### Objective

Validate **Unexpected Runner Egress** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 66 — Revoke Pipeline Credentials

### Objective

Validate **Revoke Pipeline Credentials** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 67 — Quarantine Artifact

### Objective

Validate **Quarantine Artifact** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 68 — Pipeline Disaster Recovery

### Objective

Validate **Pipeline Disaster Recovery** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 69 — Signed Build Percentage

### Objective

Validate **Signed Build Percentage** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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


## Lab 70 — SBOM Coverage

### Objective

Validate **SBOM Coverage** in a repository, container/Kubernetes lab, CI sandbox, or disposable infrastructure environment that you control.

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
artifact
  ↓
SBOM
  ├─ components
  ├─ versions
  ├─ package IDs
  └─ dependency relationships
      ↓
vulnerability / incident correlation
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

Build a controlled **DevSecOps CI/CD Security** capstone that connects source control, automation identity, policy, evidence, runtime validation, incident response, and remediation. The implementation must use only repositories, clusters, registries, and cloud resources you control.

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

### Q1. What must you understand about **CI/CD Security Purpose**?

**Short answer:** CI/CD Security Purpose belongs to the Pipeline Threat Model layer of DevSecOps.

### Q2. What must you understand about **Pipeline as High-Privilege System**?

**Short answer:** Pipeline as High-Privilege System belongs to the Pipeline Threat Model layer of DevSecOps.

### Q3. What must you understand about **CI/CD Threat Model**?

**Short answer:** CI/CD Threat Model belongs to the Pipeline Threat Model layer of DevSecOps.

### Q4. What must you understand about **Source Repository Trust Boundary**?

**Short answer:** Source Repository Trust Boundary belongs to the Pipeline Threat Model layer of DevSecOps.

### Q5. What must you understand about **Build System Trust Boundary**?

**Short answer:** Build System Trust Boundary belongs to the Pipeline Threat Model layer of DevSecOps.

### Q6. What must you understand about **Artifact Registry Trust Boundary**?

**Short answer:** Artifact Registry Trust Boundary belongs to the Pipeline Threat Model layer of DevSecOps.

### Q7. What must you understand about **Deployment Trust Boundary**?

**Short answer:** Deployment Trust Boundary belongs to the Pipeline Threat Model layer of DevSecOps.

### Q8. What must you understand about **Production Trust Boundary**?

**Short answer:** Production Trust Boundary belongs to the Pipeline Threat Model layer of DevSecOps.

### Q9. What must you understand about **Developer Account Compromise**?

**Short answer:** Developer Account Compromise belongs to the Pipeline Threat Model layer of DevSecOps.

### Q10. What must you understand about **Runner Compromise**?

**Short answer:** Runner Compromise belongs to the Pipeline Threat Model layer of DevSecOps.

### Q11. What must you understand about **Dependency Compromise**?

**Short answer:** Dependency Compromise belongs to the Pipeline Threat Model layer of DevSecOps.

### Q12. What must you understand about **Artifact Tampering**?

**Short answer:** Artifact Tampering belongs to the Pipeline Threat Model layer of DevSecOps.

### Q13. What must you understand about **Protected Branch**?

**Short answer:** Protected Branch belongs to the Repository Controls layer of DevSecOps.

### Q14. What must you understand about **Protected Tag**?

**Short answer:** Protected Tag belongs to the Repository Controls layer of DevSecOps.

### Q15. What must you understand about **Mandatory Review**?

**Short answer:** Mandatory Review belongs to the Repository Controls layer of DevSecOps.

### Q16. What must you understand about **CODEOWNERS**?

**Short answer:** CODEOWNERS belongs to the Repository Controls layer of DevSecOps.

### Q17. What must you understand about **Two-Person Approval**?

**Short answer:** Two-Person Approval belongs to the Repository Controls layer of DevSecOps.

### Q18. What must you understand about **Commit Signing Awareness**?

**Short answer:** Commit Signing Awareness belongs to the Repository Controls layer of DevSecOps.

### Q19. What must you understand about **Release Tag Security**?

**Short answer:** Release Tag Security belongs to the Repository Controls layer of DevSecOps.

### Q20. What must you understand about **Untrusted Pull Request Risk**?

**Short answer:** Untrusted Pull Request Risk belongs to the Repository Controls layer of DevSecOps.

### Q21. What must you understand about **Fork Pull Request Risk**?

**Short answer:** Fork Pull Request Risk belongs to the Repository Controls layer of DevSecOps.

### Q22. What must you understand about **Third-Party Workflow Risk**?

**Short answer:** Third-Party Workflow Risk belongs to the Repository Controls layer of DevSecOps.

### Q23. What must you understand about **Pinned Workflow Versions**?

**Short answer:** Pinned Workflow Versions belongs to the Repository Controls layer of DevSecOps.

### Q24. What must you understand about **Commit SHA Pinning**?

**Short answer:** Commit SHA Pinning belongs to the Repository Controls layer of DevSecOps.

### Q25. What must you understand about **Hosted Runner Security Model**?

**Short answer:** Hosted Runner Security Model belongs to the Runner Security layer of DevSecOps.

### Q26. What must you understand about **Self-Hosted Runner Risk**?

**Short answer:** Self-Hosted Runner Risk belongs to the Runner Security layer of DevSecOps.

### Q27. What must you understand about **Ephemeral Runner**?

**Short answer:** Ephemeral Runner belongs to the Runner Security layer of DevSecOps.

### Q28. What must you understand about **Runner Isolation**?

**Short answer:** Runner Isolation belongs to the Runner Security layer of DevSecOps.

### Q29. What must you understand about **Runner Network Segmentation**?

**Short answer:** Runner Network Segmentation belongs to the Runner Security layer of DevSecOps.

### Q30. What must you understand about **Runner Egress Control**?

**Short answer:** Runner Egress Control belongs to the Runner Security layer of DevSecOps.

### Q31. What must you understand about **Runner Cache Security**?

**Short answer:** Runner Cache Security belongs to the Runner Security layer of DevSecOps.

### Q32. What must you understand about **Build Cache Poisoning**?

**Short answer:** Build Cache Poisoning belongs to the Runner Security layer of DevSecOps.

### Q33. What must you understand about **Workspace Cleanup**?

**Short answer:** Workspace Cleanup belongs to the Runner Security layer of DevSecOps.

### Q34. What must you understand about **Temporary File Security**?

**Short answer:** Temporary File Security belongs to the Runner Security layer of DevSecOps.

### Q35. What must you understand about **Pipeline Logs and Secret Leakage**?

**Short answer:** Pipeline Logs and Secret Leakage belongs to the Runner Security layer of DevSecOps.

### Q36. What must you understand about **Runner Patch Compliance**?

**Short answer:** Runner Patch Compliance belongs to the Runner Security layer of DevSecOps.

### Q37. What must you understand about **OIDC Federation for CI/CD**?

**Short answer:** OIDC Federation for CI/CD belongs to the Pipeline Identity layer of DevSecOps.

### Q38. What must you understand about **Workload Identity Federation**?

**Short answer:** Workload Identity Federation belongs to the Pipeline Identity layer of DevSecOps.

### Q39. What must you understand about **Short-Lived Cloud Credentials**?

**Short answer:** Short-Lived Cloud Credentials belongs to the Pipeline Identity layer of DevSecOps.

### Q40. What must you understand about **Least Privilege Pipeline Role**?

**Short answer:** Least Privilege Pipeline Role belongs to the Pipeline Identity layer of DevSecOps.

### Q41. What must you understand about **Environment-Specific Pipeline Identity**?

**Short answer:** Environment-Specific Pipeline Identity belongs to the Pipeline Identity layer of DevSecOps.

### Q42. What must you understand about **Production Deployment Identity**?

**Short answer:** Production Deployment Identity belongs to the Pipeline Identity layer of DevSecOps.

### Q43. What must you understand about **Separate Build and Deploy Roles**?

**Short answer:** Separate Build and Deploy Roles belongs to the Pipeline Identity layer of DevSecOps.

### Q44. What must you understand about **Secret Manager Integration**?

**Short answer:** Secret Manager Integration belongs to the Pipeline Identity layer of DevSecOps.

### Q45. What must you understand about **Pipeline Secret Rotation**?

**Short answer:** Pipeline Secret Rotation belongs to the Pipeline Identity layer of DevSecOps.

### Q46. What must you understand about **Avoiding Static Cloud Keys**?

**Short answer:** Avoiding Static Cloud Keys belongs to the Pipeline Identity layer of DevSecOps.

### Q47. What must you understand about **Immutable Artifact**?

**Short answer:** Immutable Artifact belongs to the Build Integrity layer of DevSecOps.

### Q48. What must you understand about **Artifact Digest**?

**Short answer:** Artifact Digest belongs to the Build Integrity layer of DevSecOps.

### Q49. What must you understand about **Image Digest Pinning**?

**Short answer:** Image Digest Pinning belongs to the Build Integrity layer of DevSecOps.

### Q50. What must you understand about **Build Once Promote Many**?

**Short answer:** Build Once Promote Many belongs to the Build Integrity layer of DevSecOps.

### Q51. What must you understand about **Promotion of Immutable Artifact**?

**Short answer:** Promotion of Immutable Artifact belongs to the Build Integrity layer of DevSecOps.

### Q52. What must you understand about **Artifact Repository Immutability**?

**Short answer:** Artifact Repository Immutability belongs to the Build Integrity layer of DevSecOps.

### Q53. What must you understand about **Artifact Retention**?

**Short answer:** Artifact Retention belongs to the Build Integrity layer of DevSecOps.

### Q54. What must you understand about **Artifact Quarantine**?

**Short answer:** Artifact Quarantine belongs to the Build Integrity layer of DevSecOps.

### Q55. What must you understand about **Release Manifest**?

**Short answer:** Release Manifest belongs to the Build Integrity layer of DevSecOps.

### Q56. What must you understand about **Release Evidence**?

**Short answer:** Release Evidence belongs to the Build Integrity layer of DevSecOps.

### Q57. What must you understand about **Rollback Artifact Integrity**?

**Short answer:** Rollback Artifact Integrity belongs to the Build Integrity layer of DevSecOps.

### Q58. What must you understand about **Trusted Builder**?

**Short answer:** Trusted Builder belongs to the Build Integrity layer of DevSecOps.

### Q59. What must you understand about **SLSA Version 1.2**?

**Short answer:** SLSA Version 1.

### Q60. What must you understand about **SLSA Build Track**?

**Short answer:** SLSA Build Track belongs to the Supply Chain Evidence layer of DevSecOps.

### Q61. What must you understand about **SLSA Source Track**?

**Short answer:** SLSA Source Track belongs to the Supply Chain Evidence layer of DevSecOps.

### Q62. What must you understand about **Provenance Attestation**?

**Short answer:** Provenance Attestation belongs to the Supply Chain Evidence layer of DevSecOps.

### Q63. What must you understand about **Verification Summary Attestation Awareness**?

**Short answer:** Verification Summary Attestation Awareness belongs to the Supply Chain Evidence layer of DevSecOps.

### Q64. What must you understand about **in-toto Attestation Awareness**?

**Short answer:** in-toto Attestation Awareness belongs to the Supply Chain Evidence layer of DevSecOps.

### Q65. What must you understand about **SBOM Generation**?

**Short answer:** SBOM Generation belongs to the Supply Chain Evidence layer of DevSecOps.

### Q66. What must you understand about **CycloneDX SBOM**?

**Short answer:** CycloneDX SBOM belongs to the Supply Chain Evidence layer of DevSecOps.

### Q67. What must you understand about **SPDX SBOM**?

**Short answer:** SPDX SBOM belongs to the Supply Chain Evidence layer of DevSecOps.

### Q68. What must you understand about **Artifact Signing**?

**Short answer:** Artifact Signing belongs to the Supply Chain Evidence layer of DevSecOps.

### Q69. What must you understand about **Cosign**?

**Short answer:** Cosign belongs to the Supply Chain Evidence layer of DevSecOps.

### Q70. What must you understand about **Keyless Signing**?

**Short answer:** Keyless Signing belongs to the Supply Chain Evidence layer of DevSecOps.

### Q71. What must you understand about **Artifact Verification**?

**Short answer:** Artifact Verification belongs to the Supply Chain Evidence layer of DevSecOps.

### Q72. What must you understand about **SAST in Pipeline**?

**Short answer:** SAST in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q73. What must you understand about **SCA in Pipeline**?

**Short answer:** SCA in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q74. What must you understand about **Secret Scanning in Pipeline**?

**Short answer:** Secret Scanning in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q75. What must you understand about **IaC Scanning in Pipeline**?

**Short answer:** IaC Scanning in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q76. What must you understand about **Container Scanning in Pipeline**?

**Short answer:** Container Scanning in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q77. What must you understand about **DAST in Pipeline**?

**Short answer:** DAST in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q78. What must you understand about **API Security Tests in Pipeline**?

**Short answer:** API Security Tests in Pipeline belongs to the Security Tests layer of DevSecOps.

### Q79. What must you understand about **Fuzzing Awareness**?

**Short answer:** Fuzzing Awareness belongs to the Security Tests layer of DevSecOps.

### Q80. What must you understand about **License Compliance Gate**?

**Short answer:** License Compliance Gate belongs to the Security Tests layer of DevSecOps.

### Q81. What must you understand about **Fast Feedback Stage**?

**Short answer:** Fast Feedback Stage belongs to the Security Tests layer of DevSecOps.

### Q82. What must you understand about **Deep Security Stage**?

**Short answer:** Deep Security Stage belongs to the Security Tests layer of DevSecOps.

### Q83. What must you understand about **Pre-Merge Security Checks**?

**Short answer:** Pre-Merge Security Checks belongs to the Security Tests layer of DevSecOps.

### Q84. What must you understand about **Pre-Deployment Security Gate**?

**Short answer:** Pre-Deployment Security Gate belongs to the Deployment Controls layer of DevSecOps.

### Q85. What must you understand about **Environment Protection Rules**?

**Short answer:** Environment Protection Rules belongs to the Deployment Controls layer of DevSecOps.

### Q86. What must you understand about **Manual Approval**?

**Short answer:** Manual Approval belongs to the Deployment Controls layer of DevSecOps.

### Q87. What must you understand about **Deployment Approval**?

**Short answer:** Deployment Approval belongs to the Deployment Controls layer of DevSecOps.

### Q88. What must you understand about **Progressive Delivery**?

**Short answer:** Progressive Delivery belongs to the Deployment Controls layer of DevSecOps.

### Q89. What must you understand about **Canary Deployment Security**?

**Short answer:** Canary Deployment Security belongs to the Deployment Controls layer of DevSecOps.

### Q90. What must you understand about **Blue-Green Deployment Security**?

**Short answer:** Blue-Green Deployment Security belongs to the Deployment Controls layer of DevSecOps.

### Q91. What must you understand about **Feature Flag Security**?

**Short answer:** Feature Flag Security belongs to the Deployment Controls layer of DevSecOps.

### Q92. What must you understand about **Policy as Code Gate**?

**Short answer:** Policy as Code Gate belongs to the Deployment Controls layer of DevSecOps.

### Q93. What must you understand about **Admission Policy Integration**?

**Short answer:** Admission Policy Integration belongs to the Deployment Controls layer of DevSecOps.

### Q94. What must you understand about **Terraform Plan Security Review**?

**Short answer:** Terraform Plan Security Review belongs to the Deployment Controls layer of DevSecOps.

### Q95. What must you understand about **Production Break-Glass**?

**Short answer:** Production Break-Glass belongs to the Deployment Controls layer of DevSecOps.

### Q96. What must you understand about **Pipeline Audit Logging**?

**Short answer:** Pipeline Audit Logging belongs to the Monitoring and Recovery layer of DevSecOps.

### Q97. What must you understand about **SCM Audit Logging**?

**Short answer:** SCM Audit Logging belongs to the Monitoring and Recovery layer of DevSecOps.

### Q98. What must you understand about **Artifact Registry Audit Logging**?

**Short answer:** Artifact Registry Audit Logging belongs to the Monitoring and Recovery layer of DevSecOps.

### Q99. What must you understand about **Deployment Log Integrity**?

**Short answer:** Deployment Log Integrity belongs to the Monitoring and Recovery layer of DevSecOps.

### Q100. What must you understand about **Suspicious Pipeline Behavior**?

**Short answer:** Suspicious Pipeline Behavior belongs to the Monitoring and Recovery layer of DevSecOps.

### Q101. What must you understand about **Unexpected Secret Access**?

**Short answer:** Unexpected Secret Access belongs to the Monitoring and Recovery layer of DevSecOps.

### Q102. What must you understand about **Unexpected Runner Egress**?

**Short answer:** Unexpected Runner Egress belongs to the Monitoring and Recovery layer of DevSecOps.

### Q103. What must you understand about **Pipeline Incident Response**?

**Short answer:** Pipeline Incident Response belongs to the Monitoring and Recovery layer of DevSecOps.

### Q104. What must you understand about **Revoke Pipeline Credentials**?

**Short answer:** Revoke Pipeline Credentials belongs to the Monitoring and Recovery layer of DevSecOps.

### Q105. What must you understand about **Quarantine Artifact**?

**Short answer:** Quarantine Artifact belongs to the Monitoring and Recovery layer of DevSecOps.

### Q106. What must you understand about **Rebuild from Trusted Source**?

**Short answer:** Rebuild from Trusted Source belongs to the Monitoring and Recovery layer of DevSecOps.

### Q107. What must you understand about **Pipeline Disaster Recovery**?

**Short answer:** Pipeline Disaster Recovery belongs to the Monitoring and Recovery layer of DevSecOps.

### Q108. What must you understand about **Signed Build Percentage**?

**Short answer:** Signed Build Percentage belongs to the Monitoring and Recovery layer of DevSecOps.

### Q109. What must you understand about **Provenance Coverage**?

**Short answer:** Provenance Coverage belongs to the Monitoring and Recovery layer of DevSecOps.

### Q110. What must you understand about **SBOM Coverage**?

**Short answer:** SBOM Coverage belongs to the Monitoring and Recovery layer of DevSecOps.

## Completion Gate

You are complete when you can explain why a change is trusted from **source → pipeline → artifact/state → deployment → runtime → monitoring → feedback**.
