# 113. AWS Security Fundamentals

> Phase 29 — Cloud Security  
> Depth: architecture + implementation + operations + incident response + governance.

---

## 1. Topic Title

**AWS Security Fundamentals**

---

## 2. Learning Objectives

- Design an AWS multi-account security architecture using Organizations, OUs, Control Tower concepts, and centralized security accounts.
- Implement least-privilege IAM using roles, STS, federation, Identity Center, boundaries, resource policies, and Access Analyzer.
- Secure VPCs, endpoints, transit, firewalls, DNS, WAF, Shield, and hybrid connectivity.
- Secure KMS, Secrets Manager, S3, EBS, RDS, DynamoDB, and backups.
- Harden EC2, metadata, Session Manager, Lambda, ECS/EKS, and ECR.
- Use CloudTrail, Config, GuardDuty, Inspector, Macie, Security Hub CSPM, Security Lake, and automation coherently.
- Apply AWS Well-Architected Security Pillar and AWS Security Reference Architecture concepts.
- Perform AWS incident response using identity revocation, isolation, snapshots, centralized logs, and recovery.
- Understand FSBP and current CIS AWS Foundations Benchmark v5.0.0 awareness.
- Build a secure AWS landing-zone and workload baseline.

---

## 3. Prerequisites

Required:

```text
112 Cloud Security Fundamentals
AWS fundamentals
AWS architecture / networking / IAM
EC2 / S3 / RDS / Lambda
containers and Kubernetes
Terraform / IaC
incident response
```

Use a dedicated AWS sandbox for labs.

---

## 4. Core Concepts Explanation

# Part 1 — AWS Shared Responsibility Model

### Concept

AWS describes responsibility as security of the cloud versus security in the cloud, with the customer's responsibilities changing according to the AWS services selected and their configuration.

### Detailed Explanation

Do not study **AWS Shared Responsibility Model** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
On-Prem       IaaS           PaaS           SaaS
customer      customer       customer       customer
owns stack    owns more      owns less      owns identity/data/config
   |             |              |              |
provider      provider       provider        provider
none          infrastructure infrastructure+  most service stack

The exact boundary is service-specific.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Shared Responsibility Model** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 2 — AWS Account as a Security Boundary

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **AWS Account as a Security Boundary** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Account as a Security Boundary** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 3 — AWS Organizations

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **AWS Organizations** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Organization
 |- Security OU
 |   |- Log Archive
 |   `- Security Tooling
 |- Infrastructure OU
 |- Workloads-Prod OU
 |- Workloads-NonProd OU
 `- Sandbox OU
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Organizations** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 4 — Organizational Units

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Organizational Units** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Organization
 |- Security OU
 |   |- Log Archive
 |   `- Security Tooling
 |- Infrastructure OU
 |- Workloads-Prod OU
 |- Workloads-NonProd OU
 `- Sandbox OU
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Organizational Units** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 5 — Management Account Protection

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Management Account Protection** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Management Account Protection** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 6 — Member Accounts

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Member Accounts** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Member Accounts** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 7 — Multi-Account Security Strategy

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Multi-Account Security Strategy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Multi-Account Security Strategy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 8 — AWS Control Tower

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **AWS Control Tower** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Control Tower
     |
AWS Organizations
     |
OUs + accounts
     |
preventive controls + detective checks
     |
account provisioning baseline
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Control Tower** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 9 — AWS Landing Zone

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **AWS Landing Zone** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Control Tower
     |
AWS Organizations
     |
OUs + accounts
     |
preventive controls + detective checks
     |
account provisioning baseline
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Landing Zone** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 10 — Account Factory and Account Vending

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Account Factory and Account Vending** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Organization / Tenant
  |- Security
  |- Log Archive
  |- Shared Services
  |- Production
  |- Nonproduction
  `- Sandbox

New environment -> approved vending -> inherited baseline
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Account Factory and Account Vending** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 11 — Log Archive Account

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **Log Archive Account** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
workload environments
     |
organization-level audit events
     |
central security boundary
     |
restricted / immutable retention
     |
SIEM + hunting + forensics
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Log Archive Account** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 12 — Security and Audit Account

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Security and Audit Account** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Security and Audit Account** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 13 — Service Control Policies

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Service Control Policies** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": ["cloudtrail:StopLogging", "cloudtrail:DeleteTrail"],
    "Resource": "*"
  }]
}
```

An SCP is a permissions guardrail; it does not grant permissions by itself.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Service Control Policies** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 14 — SCP Evaluation Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **SCP Evaluation Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": ["cloudtrail:StopLogging", "cloudtrail:DeleteTrail"],
    "Resource": "*"
  }]
}
```

An SCP is a permissions guardrail; it does not grant permissions by itself.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **SCP Evaluation Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 15 — AWS Resource Control Policy Awareness

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **AWS Resource Control Policy Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Resource Control Policy Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 16 — Organization-Wide Guardrails

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Organization-Wide Guardrails** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Organization-Wide Guardrails** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 17 — Region Governance

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Region Governance** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Region Governance** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 18 — AWS Root User

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Root User** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Root User** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 19 — Root User MFA

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Root User MFA** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Root User MFA** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 20 — Root Access Key Risk

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Root Access Key Risk** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Root Access Key Risk** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 21 — AWS IAM

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **AWS IAM** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS IAM** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 22 — IAM User

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IAM User** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IAM User** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 23 — IAM Group

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IAM Group** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IAM Group** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 24 — IAM Role

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IAM Role** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws sts assume-role           --role-arn arn:aws:iam::111122223333:role/SecurityReadOnly           --role-session-name training-session
```

Prefer temporary role sessions to long-lived IAM user access keys.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IAM Role** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 25 — IAM Policy

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IAM Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IAM Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 26 — Identity-Based Policy

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Identity-Based Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Identity-Based Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 27 — Resource-Based Policy

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Resource-Based Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Resource-Based Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 28 — Trust Policy

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Trust Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::111122223333:root"},
    "Action": "sts:AssumeRole"
  }]
}
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Trust Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 29 — Permissions Boundary

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Permissions Boundary** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Identity policy: requested permission
Permissions boundary: maximum identity permission
SCP: organization maximum
Resource policy: resource-side permission
Explicit deny: wins
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Permissions Boundary** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 30 — Session Policy

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Session Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Session Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 31 — Policy Evaluation Logic

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **Policy Evaluation Logic** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Policy Evaluation Logic** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 32 — Explicit Deny

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Explicit Deny** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Explicit Deny** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 33 — Least Privilege in AWS

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Least Privilege in AWS** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Least Privilege in AWS** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 34 — AWS STS

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS STS** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS STS** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 35 — Temporary Credentials

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Temporary Credentials** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws sts assume-role           --role-arn arn:aws:iam::111122223333:role/SecurityReadOnly           --role-session-name training-session
```

Prefer temporary role sessions to long-lived IAM user access keys.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Temporary Credentials** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 36 — AssumeRole

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **AssumeRole** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws sts assume-role           --role-arn arn:aws:iam::111122223333:role/SecurityReadOnly           --role-session-name training-session
```

Prefer temporary role sessions to long-lived IAM user access keys.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AssumeRole** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 37 — Role Chaining Awareness

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Role Chaining Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Role Chaining Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 38 — Cross-Account Role

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Cross-Account Role** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Cross-Account Role** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 39 — Federation

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Federation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Federation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 40 — AWS IAM Identity Center

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **AWS IAM Identity Center** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS IAM Identity Center** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 41 — External Identity Provider

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **External Identity Provider** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **External Identity Provider** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 42 — Permission Sets

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Permission Sets** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Permission Sets** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 43 — MFA

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **MFA** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **MFA** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 44 — Passkeys and Phishing-Resistant MFA Awareness

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Passkeys and Phishing-Resistant MFA Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Passkeys and Phishing-Resistant MFA Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 45 — Emergency Access

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Emergency Access** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Emergency Access** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 46 — IAM Access Analyzer

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IAM Access Analyzer** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IAM Access Analyzer** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 47 — External Access Findings

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **External Access Findings** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **External Access Findings** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 48 — Unused Access Analysis Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Unused Access Analysis Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Unused Access Analysis Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 49 — IAM Credential Report

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IAM Credential Report** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IAM Credential Report** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 50 — Access Key Rotation

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Access Key Rotation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Access Key Rotation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 51 — Service-Linked Roles

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Service-Linked Roles** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Service-Linked Roles** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 52 — Workload Identity in AWS

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Workload Identity in AWS** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Workload
  |
  v
platform / federated identity
  |
  v
short-lived token
  |
  v
cloud API / database / secret store

Avoid source-code access keys and long-lived service passwords.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Workload Identity in AWS** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 53 — EC2 Instance Profile

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **EC2 Instance Profile** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EC2 Instance Profile** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 54 — Lambda Execution Role

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Lambda Execution Role** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Lambda Execution Role** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 55 — ECS Task Role

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **ECS Task Role** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **ECS Task Role** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 56 — EKS IAM Integration Awareness

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **EKS IAM Integration Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EKS IAM Integration Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 57 — IRSA and Pod Identity Awareness

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **IRSA and Pod Identity Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **IRSA and Pod Identity Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 58 — Secrets Manager

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Secrets Manager** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Secrets Manager** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 59 — Systems Manager Parameter Store

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Systems Manager Parameter Store** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Systems Manager Parameter Store** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 60 — AWS KMS

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **AWS KMS** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS KMS** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 61 — KMS Key

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **KMS Key** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **KMS Key** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 62 — Key Policy

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Key Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Key Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 63 — KMS Grant

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **KMS Grant** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **KMS Grant** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 64 — Envelope Encryption

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Envelope Encryption** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Envelope Encryption** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 65 — Automatic Key Rotation Awareness

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Automatic Key Rotation Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Automatic Key Rotation Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 66 — CloudHSM Awareness

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **CloudHSM Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
plaintext data
    |
encrypt with data key
    |
ciphertext data

data key
    |
protected by KMS/HSM key
    |
encrypted data key

Store ciphertext + encrypted data key.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudHSM Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 67 — AWS Certificate Manager

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **AWS Certificate Manager** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Certificate Manager** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 68 — Private CA Awareness

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Private CA Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Private CA Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 69 — Amazon VPC

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Amazon VPC** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Amazon VPC** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 70 — VPC CIDR Planning

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **VPC CIDR Planning** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **VPC CIDR Planning** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 71 — Public Subnet

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Public Subnet** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Public Subnet** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 72 — Private Subnet

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Private Subnet** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Private Subnet** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 73 — Route Table

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Route Table** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Route Table** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 74 — Internet Gateway

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Internet Gateway** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Internet Gateway** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 75 — NAT Gateway

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **NAT Gateway** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **NAT Gateway** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 76 — Security Group

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Security Group** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws ec2 describe-security-groups           --query 'SecurityGroups[].{Id:GroupId,Name:GroupName,Vpc:VpcId}'
```

Security groups are stateful resource-associated network controls.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Security Group** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 77 — Network ACL

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Network ACL** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Network ACL** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 78 — VPC Peering

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **VPC Peering** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **VPC Peering** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 79 — Transit Gateway

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Transit Gateway** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Transit Gateway** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 80 — AWS PrivateLink

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **AWS PrivateLink** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS PrivateLink** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 81 — VPC Interface Endpoint

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **VPC Interface Endpoint** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **VPC Interface Endpoint** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 82 — VPC Gateway Endpoint

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **VPC Gateway Endpoint** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **VPC Gateway Endpoint** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 83 — VPC Endpoint Policy

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **VPC Endpoint Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **VPC Endpoint Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 84 — Route 53 Resolver

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Route 53 Resolver** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Route 53 Resolver** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 85 — Route 53 Resolver DNS Firewall Awareness

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Route 53 Resolver DNS Firewall Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Route 53 Resolver DNS Firewall Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 86 — AWS Network Firewall

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **AWS Network Firewall** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Network Firewall** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 87 — Gateway Load Balancer Awareness

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Gateway Load Balancer Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Gateway Load Balancer Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 88 — Elastic Load Balancing Security

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Elastic Load Balancing Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Elastic Load Balancing Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 89 — Application Load Balancer

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Application Load Balancer** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Application Load Balancer** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 90 — Network Load Balancer

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Network Load Balancer** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Network Load Balancer** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 91 — AWS WAF

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **AWS WAF** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS WAF** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 92 — AWS Shield

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Shield** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Shield** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 93 — Shield Advanced Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Shield Advanced Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Shield Advanced Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 94 — AWS Firewall Manager

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **AWS Firewall Manager** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Firewall Manager** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 95 — VPC Flow Logs

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **VPC Flow Logs** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **VPC Flow Logs** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 96 — Traffic Mirroring Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Traffic Mirroring Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Traffic Mirroring Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 97 — Hybrid VPN

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Hybrid VPN** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Hybrid VPN** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 98 — Direct Connect Security Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Direct Connect Security Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Direct Connect Security Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 99 — S3 Security

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 100 — S3 Block Public Access

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Block Public Access** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws s3api get-public-access-block --bucket example-private-bucket
```

Target baseline:
BlockPublicAcls=true
IgnorePublicAcls=true
BlockPublicPolicy=true
RestrictPublicBuckets=true

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Block Public Access** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 101 — S3 Bucket Policy

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Bucket Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Bucket Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 102 — S3 Access Points

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Access Points** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Access Points** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 103 — S3 Object Ownership

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Object Ownership** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Object Ownership** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 104 — S3 Versioning

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Versioning** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Versioning** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 105 — S3 Object Lock

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Object Lock** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Object Lock** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 106 — S3 Encryption

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 Encryption** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
plaintext data
    |
encrypt with data key
    |
ciphertext data

data key
    |
protected by KMS/HSM key
    |
encrypted data key

Store ciphertext + encrypted data key.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 Encryption** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 107 — S3 KMS Keys

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **S3 KMS Keys** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **S3 KMS Keys** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 108 — Amazon Macie

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Amazon Macie** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Amazon Macie** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 109 — EBS Encryption

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **EBS Encryption** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
plaintext data
    |
encrypt with data key
    |
ciphertext data

data key
    |
protected by KMS/HSM key
    |
encrypted data key

Store ciphertext + encrypted data key.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EBS Encryption** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 110 — EBS Snapshot Security

### Concept

In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Detailed Explanation

Do not study **EBS Snapshot Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EBS Snapshot Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 111 — RDS Security

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **RDS Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **RDS Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 112 — RDS IAM Authentication Awareness

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **RDS IAM Authentication Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **RDS IAM Authentication Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 113 — RDS Network Isolation

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **RDS Network Isolation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **RDS Network Isolation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 114 — DynamoDB Security

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **DynamoDB Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **DynamoDB Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 115 — Database Secrets Rotation

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Database Secrets Rotation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Database Secrets Rotation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 116 — AWS Backup

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **AWS Backup** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Backup** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 117 — Backup Vault

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Backup Vault** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Backup Vault** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 118 — Backup Vault Lock Awareness

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Backup Vault Lock Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Backup Vault Lock Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 119 — EC2 Security

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **EC2 Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EC2 Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 120 — AMI Hardening

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AMI Hardening** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AMI Hardening** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 121 — EC2 IMDSv2

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **EC2 IMDSv2** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
EC2 workload -> IMDSv2 -> temporary instance-role credential -> AWS API

Defense:
least privilege + hardened metadata settings + telemetry.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EC2 IMDSv2** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 122 — Systems Manager Session Manager

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Systems Manager Session Manager** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Administrator
  |
IAM / federation / MFA
  |
Systems Manager Session Manager
  |
private EC2 instance

Many admin workflows need no inbound SSH/RDP.
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Systems Manager Session Manager** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 123 — Avoiding Public SSH RDP

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Avoiding Public SSH RDP** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Avoiding Public SSH RDP** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 124 — Systems Manager Patch Management Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Systems Manager Patch Management Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Systems Manager Patch Management Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 125 — Amazon Inspector

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Amazon Inspector** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Amazon Inspector** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 126 — Vulnerability Management

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Vulnerability Management** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Vulnerability Management** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 127 — ECR Security

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **ECR Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **ECR Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 128 — ECR Image Scanning Awareness

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **ECR Image Scanning Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **ECR Image Scanning Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 129 — ECS Security

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **ECS Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **ECS Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 130 — EKS Security

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **EKS Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EKS Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 131 — EKS RBAC and IAM Boundary

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **EKS RBAC and IAM Boundary** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EKS RBAC and IAM Boundary** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 132 — EKS Network Security

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **EKS Network Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EKS Network Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 133 — EKS Secrets Awareness

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **EKS Secrets Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EKS Secrets Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 134 — Lambda Security

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **Lambda Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Lambda Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 135 — Lambda Resource Policy

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **Lambda Resource Policy** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Lambda Resource Policy** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 136 — Lambda Environment Variable Secrets Risk

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Lambda Environment Variable Secrets Risk** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Lambda Environment Variable Secrets Risk** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 137 — API Gateway Security

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **API Gateway Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **API Gateway Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 138 — CloudFront Security

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **CloudFront Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudFront Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 139 — CloudFront Origin Access Control Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **CloudFront Origin Access Control Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudFront Origin Access Control Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 140 — CloudTrail

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **CloudTrail** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudTrail** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 141 — Organization Trail

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **Organization Trail** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Organization Trail** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 142 — CloudTrail Log Integrity

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **CloudTrail Log Integrity** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudTrail Log Integrity** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 143 — CloudTrail Lake Awareness

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **CloudTrail Lake Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudTrail Lake Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 144 — AWS Config

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Config** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Config** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 145 — Config Rules

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Config Rules** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Config Rules** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 146 — Conformance Packs Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Conformance Packs Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Conformance Packs Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 147 — CloudWatch Security Monitoring

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **CloudWatch Security Monitoring** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudWatch Security Monitoring** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 148 — EventBridge for Security Automation

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **EventBridge for Security Automation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **EventBridge for Security Automation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 149 — Amazon GuardDuty

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **Amazon GuardDuty** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
cloud / network / service signals
     |
GuardDuty analytics
     |
finding
     |
Security Hub / EventBridge
     |
investigation / automation
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Amazon GuardDuty** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 150 — GuardDuty Organization Management

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **GuardDuty Organization Management** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
cloud / network / service signals
     |
GuardDuty analytics
     |
finding
     |
Security Hub / EventBridge
     |
investigation / automation
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **GuardDuty Organization Management** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 151 — GuardDuty Protection Plans Awareness

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **GuardDuty Protection Plans Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
cloud / network / service signals
     |
GuardDuty analytics
     |
finding
     |
Security Hub / EventBridge
     |
investigation / automation
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **GuardDuty Protection Plans Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 152 — AWS Security Hub CSPM

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **AWS Security Hub CSPM** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Security Hub CSPM** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 153 — AWS Foundational Security Best Practices

### Concept

AWS Security Hub CSPM includes the AWS Foundational Security Best Practices standard to identify AWS accounts and resources that deviate from AWS security best practices.

### Detailed Explanation

Do not study **AWS Foundational Security Best Practices** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Foundational Security Best Practices** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 154 — CIS AWS Foundations Benchmark v5.0.0 Awareness

### Concept

AWS Security Hub CSPM documentation currently supports CIS AWS Foundations Benchmark v5.0.0 and recommends current benchmark use for foundational AWS configuration assessment.

### Detailed Explanation

Do not study **CIS AWS Foundations Benchmark v5.0.0 Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CIS AWS Foundations Benchmark v5.0.0 Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 155 — Security Hub Central Configuration

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Security Hub Central Configuration** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Security Hub Central Configuration** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 156 — Security Hub Findings

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **Security Hub Findings** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Security Hub Findings** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 157 — Amazon Detective Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Amazon Detective Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Amazon Detective Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 158 — Amazon Security Lake

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Amazon Security Lake** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Amazon Security Lake** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 159 — Open Cybersecurity Schema Framework Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Open Cybersecurity Schema Framework Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Open Cybersecurity Schema Framework Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 160 — Centralized Security Logging

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Centralized Security Logging** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Centralized Security Logging** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 161 — AWS Security Reference Architecture

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Security Reference Architecture** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Security Reference Architecture** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 162 — AWS Well-Architected Security Pillar

### Concept

AWS Well-Architected security guidance groups best practices into security foundations, identity and access management, detection, infrastructure protection, data protection, incident response, and application security.

### Detailed Explanation

Do not study **AWS Well-Architected Security Pillar** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Well-Architected Security Pillar** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 163 — Strong Identity Foundation

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Strong Identity Foundation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Strong Identity Foundation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 164 — Traceability

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Traceability** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Traceability** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 165 — Security at All Layers

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Security at All Layers** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Security at All Layers** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 166 — Automating AWS Security Best Practices

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Automating AWS Security Best Practices** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Automating AWS Security Best Practices** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 167 — Protecting Data at Rest and in Transit

### Concept

In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Detailed Explanation

Do not study **Protecting Data at Rest and in Transit** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Protecting Data at Rest and in Transit** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 168 — Preparing for AWS Security Events

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Preparing for AWS Security Events** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Preparing for AWS Security Events** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 169 — AWS Incident Response

### Concept

In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Detailed Explanation

Do not study **AWS Incident Response** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Finding -> CloudTrail scope -> role/session analysis
        -> revoke/restrict identity
        -> isolate affected workload
        -> preserve logs/snapshots
        -> rebuild/recover
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Incident Response** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 170 — Compromised Access Key Response

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **Compromised Access Key Response** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Finding -> CloudTrail scope -> role/session analysis
        -> revoke/restrict identity
        -> isolate affected workload
        -> preserve logs/snapshots
        -> rebuild/recover
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Compromised Access Key Response** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 171 — Compromised EC2 Response

### Concept

In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Detailed Explanation

Do not study **Compromised EC2 Response** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Finding -> CloudTrail scope -> role/session analysis
        -> revoke/restrict identity
        -> isolate affected workload
        -> preserve logs/snapshots
        -> rebuild/recover
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Compromised EC2 Response** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 172 — Compromised IAM Role Response

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Compromised IAM Role Response** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws sts assume-role           --role-arn arn:aws:iam::111122223333:role/SecurityReadOnly           --role-session-name training-session
```

Prefer temporary role sessions to long-lived IAM user access keys.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Compromised IAM Role Response** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 173 — CloudTrail Investigation

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **CloudTrail Investigation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **CloudTrail Investigation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 174 — GuardDuty Investigation

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **GuardDuty Investigation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
cloud / network / service signals
     |
GuardDuty analytics
     |
finding
     |
Security Hub / EventBridge
     |
investigation / automation
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **GuardDuty Investigation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 175 — Snapshot for Forensics

### Concept

In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Detailed Explanation

Do not study **Snapshot for Forensics** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Alert
  |
preserve cloud audit evidence
  |
scope identities + resources + regions
  |
revoke credentials / isolate workload
  |
snapshot when useful
  |
eradicate -> recover -> new guardrail
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Snapshot for Forensics** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 176 — Isolation Security Group Pattern

### Concept

In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Detailed Explanation

Do not study **Isolation Security Group Pattern** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```bash
aws ec2 describe-security-groups           --query 'SecurityGroups[].{Id:GroupId,Name:GroupName,Vpc:VpcId}'
```

Security groups are stateful resource-associated network controls.

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Isolation Security Group Pattern** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 177 — Credential Revocation

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Credential Revocation** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Credential Revocation** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 178 — AWS Config Remediation Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Config Remediation Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Config Remediation Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 179 — Security Hub Automation Awareness

### Concept

In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Detailed Explanation

Do not study **Security Hub Automation Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Security Hub Automation Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 180 — AWS Organizations Delegated Administrator

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **AWS Organizations Delegated Administrator** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
AWS Organization
 |- Security OU
 |   |- Log Archive
 |   `- Security Tooling
 |- Infrastructure OU
 |- Workloads-Prod OU
 |- Workloads-NonProd OU
 `- Sandbox OU
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Organizations Delegated Administrator** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 181 — Centralized Security Services

### Concept

In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Detailed Explanation

Do not study **Centralized Security Services** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Centralized Security Services** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 182 — AWS Backup and Recovery Security

### Concept

In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Detailed Explanation

Do not study **AWS Backup and Recovery Security** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Backup and Recovery Security** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 183 — Multi-Region Security Considerations

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **Multi-Region Security Considerations** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Multi-Region Security Considerations** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 184 — Service Quotas and Abuse

### Concept

In AWS, this topic treats abnormal resource consumption and uncontrolled provisioning as both governance and potential security signals.

### Detailed Explanation

Do not study **Service Quotas and Abuse** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Service Quotas and Abuse** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 185 — Budget and Cost Anomaly Security Awareness

### Concept

In AWS, this topic treats abnormal resource consumption and uncontrolled provisioning as both governance and potential security signals.

### Detailed Explanation

Do not study **Budget and Cost Anomaly Security Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Budget and Cost Anomaly Security Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 186 — Tagging Governance

### Concept

In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Detailed Explanation

Do not study **Tagging Governance** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **Tagging Governance** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 187 — AWS Compliance Programs Awareness

### Concept

In AWS, this topic relates cloud implementations and evidence to explicit security-control or assurance objectives without confusing a posture score with full compliance.

### Detailed Explanation

Do not study **AWS Compliance Programs Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Compliance Programs Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 188 — AWS Artifact Awareness

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Artifact Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Artifact Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 189 — AWS Audit Manager Awareness

### Concept

In AWS, this topic relates cloud implementations and evidence to explicit security-control or assurance objectives without confusing a posture score with full compliance.

### Detailed Explanation

Do not study **AWS Audit Manager Awareness** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Audit Manager Awareness** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


# Part 190 — AWS Security Final Architecture

### Concept

In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Detailed Explanation

Do not study **AWS Security Final Architecture** as a product checkbox. In a real AWS environment, it interacts with identity, resource policy, network reachability, data sensitivity, telemetry, automation, business ownership, and recovery.

Use this six-question model:

```text
1. WHAT resource or business capability is protected?
2. WHO or WHAT identity interacts with it?
3. WHERE is access or configuration enforced?
4. WHICH exact state is considered secure?
5. WHAT evidence proves the control operates?
6. HOW do we revoke, recover, or handle an exception?
```

A technically correct control can still fail if another policy grants broader access, if a workload retains a long-lived credential, if logs are missing, or if no team owns remediation.

### Architecture / Code / Command / Visualization

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Why It Works

Cloud platforms expose security configuration through APIs and declarative resources. This enables an organization to make security **repeatable, testable, reviewable, and scalable**.

Evaluate both:

```text
DESIGN EFFECTIVENESS
Would the control prevent or detect the intended threat?

OPERATING EFFECTIVENESS
Is the control actually enabled, correctly scoped,
producing evidence, and remaining enabled over time?
```

### Production Engineering Example

A platform team makes **AWS Security Final Architecture** part of a landing-zone or workload baseline. Workload teams inherit the safe state automatically. A posture or audit system verifies the state continuously. If a team needs to deviate, it uses a documented exception with risk owner, compensating control, and expiry date.

### Expected Evidence

Depending on the topic, acceptable evidence may include:

- provider API output;
- IAM or resource policy;
- network route / firewall / private-endpoint configuration;
- IaC source and CI policy result;
- centralized audit-log event;
- CSPM recommendation or control result;
- KMS / Key Vault key policy and access log;
- workload runtime telemetry;
- incident-response action record;
- exception or risk-acceptance record.

### Common Failure Modes

- assuming the provider secures customer-controlled configuration;
- broad administrator or owner permissions;
- long-lived human/workload credentials;
- public exposure added for convenience;
- encryption enabled but key access left too broad;
- audit logs stored inside the same compromise boundary;
- policy enabled with no exception workflow;
- posture scores treated as proof of complete security;
- controls deployed once but never checked for drift;
- recovery designed only after an incident.

### Troubleshooting Sequence

```text
Expected policy
   |
Effective identity / permission
   |
Resource policy
   |
Network path / DNS
   |
Service configuration
   |
Encryption / key authorization
   |
Audit evidence
   |
Recent deployment / drift
   |
Quota / provider service condition
```

Change one variable at a time. Preserve enough evidence to explain the root cause.

### Best Practices

- Prefer short-lived identity and federation.
- Deny by default; grant only required actions.
- Separate human administration from workload identity.
- Use private connectivity when it materially reduces risk.
- Centralize protected audit evidence.
- Enforce policy before deployment and verify after deployment.
- Give every control an owner.
- Time-bound exceptions.
- Test incident response and restore operations.
- Reassess whenever cloud service behavior, architecture, or business requirements change.

---


## 5. Hands-on Lab / Practical Exercises

## Lab 1 — AWS Shared Responsibility Model

### Objective

Implement, inspect, model, or validate **AWS Shared Responsibility Model** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
On-Prem       IaaS           PaaS           SaaS
customer      customer       customer       customer
owns stack    owns more      owns less      owns identity/data/config
   |             |              |              |
provider      provider       provider        provider
none          infrastructure infrastructure+  most service stack

The exact boundary is service-specific.
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 2 — AWS Organizations

### Objective

Implement, inspect, model, or validate **AWS Organizations** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
AWS Organization
 |- Security OU
 |   |- Log Archive
 |   `- Security Tooling
 |- Infrastructure OU
 |- Workloads-Prod OU
 |- Workloads-NonProd OU
 `- Sandbox OU
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 3 — Member Accounts

### Objective

Implement, inspect, model, or validate **Member Accounts** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 4 — AWS Control Tower

### Objective

Implement, inspect, model, or validate **AWS Control Tower** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
AWS Control Tower
     |
AWS Organizations
     |
OUs + accounts
     |
preventive controls + detective checks
     |
account provisioning baseline
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 5 — Log Archive Account

### Objective

Implement, inspect, model, or validate **Log Archive Account** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
workload environments
     |
organization-level audit events
     |
central security boundary
     |
restricted / immutable retention
     |
SIEM + hunting + forensics
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 6 — Service Control Policies

### Objective

Implement, inspect, model, or validate **Service Control Policies** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": ["cloudtrail:StopLogging", "cloudtrail:DeleteTrail"],
    "Resource": "*"
  }]
}
```

An SCP is a permissions guardrail; it does not grant permissions by itself.

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 7 — AWS Resource Control Policy Awareness

### Objective

Implement, inspect, model, or validate **AWS Resource Control Policy Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 8 — AWS Root User

### Objective

Implement, inspect, model, or validate **AWS Root User** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 9 — Root Access Key Risk

### Objective

Implement, inspect, model, or validate **Root Access Key Risk** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 10 — IAM Group

### Objective

Implement, inspect, model, or validate **IAM Group** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 11 — IAM Policy

### Objective

Implement, inspect, model, or validate **IAM Policy** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 12 — Resource-Based Policy

### Objective

Implement, inspect, model, or validate **Resource-Based Policy** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 13 — Session Policy

### Objective

Implement, inspect, model, or validate **Session Policy** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 14 — Explicit Deny

### Objective

Implement, inspect, model, or validate **Explicit Deny** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 15 — AWS STS

### Objective

Implement, inspect, model, or validate **AWS STS** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 16 — Role Chaining Awareness

### Objective

Implement, inspect, model, or validate **Role Chaining Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 17 — Federation

### Objective

Implement, inspect, model, or validate **Federation** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 18 — Permission Sets

### Objective

Implement, inspect, model, or validate **Permission Sets** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 19 — Passkeys and Phishing-Resistant MFA Awareness

### Objective

Implement, inspect, model, or validate **Passkeys and Phishing-Resistant MFA Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 20 — IAM Access Analyzer

### Objective

Implement, inspect, model, or validate **IAM Access Analyzer** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 21 — IAM Credential Report

### Objective

Implement, inspect, model, or validate **IAM Credential Report** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 22 — Service-Linked Roles

### Objective

Implement, inspect, model, or validate **Service-Linked Roles** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 23 — Lambda Execution Role

### Objective

Implement, inspect, model, or validate **Lambda Execution Role** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 24 — EKS IAM Integration Awareness

### Objective

Implement, inspect, model, or validate **EKS IAM Integration Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 25 — Secrets Manager

### Objective

Implement, inspect, model, or validate **Secrets Manager** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 26 — KMS Key

### Objective

Implement, inspect, model, or validate **KMS Key** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 27 — KMS Grant

### Objective

Implement, inspect, model, or validate **KMS Grant** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Application -> GenerateDataKey -> AWS KMS key
                      |
             plaintext data key (memory)
             encrypted data key
                      |
workload data -> ciphertext + encrypted data key
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 28 — CloudHSM Awareness

### Objective

Implement, inspect, model, or validate **CloudHSM Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
plaintext data
    |
encrypt with data key
    |
ciphertext data

data key
    |
protected by KMS/HSM key
    |
encrypted data key

Store ciphertext + encrypted data key.
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 29 — Private CA Awareness

### Objective

Implement, inspect, model, or validate **Private CA Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 30 — VPC CIDR Planning

### Objective

Implement, inspect, model, or validate **VPC CIDR Planning** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 31 — Route Table

### Objective

Implement, inspect, model, or validate **Route Table** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 32 — NAT Gateway

### Objective

Implement, inspect, model, or validate **NAT Gateway** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 33 — VPC Peering

### Objective

Implement, inspect, model, or validate **VPC Peering** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 34 — AWS PrivateLink

### Objective

Implement, inspect, model, or validate **AWS PrivateLink** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 35 — VPC Gateway Endpoint

### Objective

Implement, inspect, model, or validate **VPC Gateway Endpoint** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 36 — Route 53 Resolver DNS Firewall Awareness

### Objective

Implement, inspect, model, or validate **Route 53 Resolver DNS Firewall Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 37 — Gateway Load Balancer Awareness

### Objective

Implement, inspect, model, or validate **Gateway Load Balancer Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 38 — Network Load Balancer

### Objective

Implement, inspect, model, or validate **Network Load Balancer** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 39 — AWS Shield

### Objective

Implement, inspect, model, or validate **AWS Shield** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 40 — AWS Firewall Manager

### Objective

Implement, inspect, model, or validate **AWS Firewall Manager** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 41 — Hybrid VPN

### Objective

Implement, inspect, model, or validate **Hybrid VPN** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 42 — S3 Security

### Objective

Implement, inspect, model, or validate **S3 Security** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 43 — S3 Bucket Policy

### Objective

Implement, inspect, model, or validate **S3 Bucket Policy** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 44 — S3 Versioning

### Objective

Implement, inspect, model, or validate **S3 Versioning** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 45 — S3 Encryption

### Objective

Implement, inspect, model, or validate **S3 Encryption** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
plaintext data
    |
encrypt with data key
    |
ciphertext data

data key
    |
protected by KMS/HSM key
    |
encrypted data key

Store ciphertext + encrypted data key.
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 46 — EBS Encryption

### Objective

Implement, inspect, model, or validate **EBS Encryption** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
plaintext data
    |
encrypt with data key
    |
ciphertext data

data key
    |
protected by KMS/HSM key
    |
encrypted data key

Store ciphertext + encrypted data key.
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 47 — RDS Security

### Objective

Implement, inspect, model, or validate **RDS Security** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 48 — RDS Network Isolation

### Objective

Implement, inspect, model, or validate **RDS Network Isolation** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Internet
   |
Edge / WAF
   |
Public ingress tier
   |
Private application tier
   |
Private data tier

Sensitive provider services:
private path + identity + resource policy
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 49 — AWS Backup

### Objective

Implement, inspect, model, or validate **AWS Backup** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 50 — Backup Vault Lock Awareness

### Objective

Implement, inspect, model, or validate **Backup Vault Lock Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 51 — EC2 IMDSv2

### Objective

Implement, inspect, model, or validate **EC2 IMDSv2** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
EC2 workload -> IMDSv2 -> temporary instance-role credential -> AWS API

Defense:
least privilege + hardened metadata settings + telemetry.
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 52 — Avoiding Public SSH RDP

### Objective

Implement, inspect, model, or validate **Avoiding Public SSH RDP** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 53 — Amazon Inspector

### Objective

Implement, inspect, model, or validate **Amazon Inspector** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 54 — ECR Image Scanning Awareness

### Objective

Implement, inspect, model, or validate **ECR Image Scanning Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 55 — EKS Security

### Objective

Implement, inspect, model, or validate **EKS Security** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 56 — EKS Secrets Awareness

### Objective

Implement, inspect, model, or validate **EKS Secrets Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 57 — Lambda Resource Policy

### Objective

Implement, inspect, model, or validate **Lambda Resource Policy** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 58 — API Gateway Security

### Objective

Implement, inspect, model, or validate **API Gateway Security** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 59 — CloudTrail

### Objective

Implement, inspect, model, or validate **CloudTrail** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 60 — CloudTrail Log Integrity

### Objective

Implement, inspect, model, or validate **CloudTrail Log Integrity** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 61 — Config Rules

### Objective

Implement, inspect, model, or validate **Config Rules** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 62 — CloudWatch Security Monitoring

### Objective

Implement, inspect, model, or validate **CloudWatch Security Monitoring** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 63 — Amazon GuardDuty

### Objective

Implement, inspect, model, or validate **Amazon GuardDuty** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
cloud / network / service signals
     |
GuardDuty analytics
     |
finding
     |
Security Hub / EventBridge
     |
investigation / automation
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 64 — AWS Security Hub CSPM

### Objective

Implement, inspect, model, or validate **AWS Security Hub CSPM** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 65 — CIS AWS Foundations Benchmark v5.0.0 Awareness

### Objective

Implement, inspect, model, or validate **CIS AWS Foundations Benchmark v5.0.0 Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
AWS Security Hub CSPM
  |- AWS Foundational Security Best Practices
  |- CIS AWS Foundations Benchmark
  |- other supported standards
  `- integrated security findings
       |
       v
prioritization / remediation workflow
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 66 — Amazon Detective Awareness

### Objective

Implement, inspect, model, or validate **Amazon Detective Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 67 — Open Cybersecurity Schema Framework Awareness

### Objective

Implement, inspect, model, or validate **Open Cybersecurity Schema Framework Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 68 — AWS Security Reference Architecture

### Objective

Implement, inspect, model, or validate **AWS Security Reference Architecture** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 69 — Traceability

### Objective

Implement, inspect, model, or validate **Traceability** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 70 — Automating AWS Security Best Practices

### Objective

Implement, inspect, model, or validate **Automating AWS Security Best Practices** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 71 — Preparing for AWS Security Events

### Objective

Implement, inspect, model, or validate **Preparing for AWS Security Events** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 72 — Compromised EC2 Response

### Objective

Implement, inspect, model, or validate **Compromised EC2 Response** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Finding -> CloudTrail scope -> role/session analysis
        -> revoke/restrict identity
        -> isolate affected workload
        -> preserve logs/snapshots
        -> rebuild/recover
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 73 — CloudTrail Investigation

### Objective

Implement, inspect, model, or validate **CloudTrail Investigation** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```bash
aws cloudtrail describe-trails
aws cloudtrail get-trail-status --name org-trail
```

```text
Organization trail -> central log account -> restricted deletion -> SIEM
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 74 — Isolation Security Group Pattern

### Objective

Implement, inspect, model, or validate **Isolation Security Group Pattern** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```bash
aws ec2 describe-security-groups           --query 'SecurityGroups[].{Id:GroupId,Name:GroupName,Vpc:VpcId}'
```

Security groups are stateful resource-associated network controls.

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 75 — AWS Config Remediation Awareness

### Objective

Implement, inspect, model, or validate **AWS Config Remediation Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 76 — AWS Organizations Delegated Administrator

### Objective

Implement, inspect, model, or validate **AWS Organizations Delegated Administrator** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
AWS Organization
 |- Security OU
 |   |- Log Archive
 |   `- Security Tooling
 |- Infrastructure OU
 |- Workloads-Prod OU
 |- Workloads-NonProd OU
 `- Sandbox OU
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 77 — Multi-Region Security Considerations

### Objective

Implement, inspect, model, or validate **Multi-Region Security Considerations** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 78 — Budget and Cost Anomaly Security Awareness

### Objective

Implement, inspect, model, or validate **Budget and Cost Anomaly Security Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 79 — AWS Artifact Awareness

### Objective

Implement, inspect, model, or validate **AWS Artifact Awareness** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## Lab 80 — AWS Security Final Architecture

### Objective

Implement, inspect, model, or validate **AWS Security Final Architecture** in a dedicated cloud lab.

### Safety and Cost Boundary

Use sandbox accounts/subscriptions, synthetic identities/data, minimal resource sizes, and explicit cleanup. Do not make production changes merely to complete a lab.

### Procedure

1. Draw the relevant architecture.
2. Write the expected secure state.
3. Identify human and workload identities.
4. Identify the effective policy/configuration.
5. Capture the initial state.
6. Make one controlled change or query.
7. Validate an allowed case.
8. Validate a denied or noncompliant case where practical.
9. Capture audit/posture evidence.
10. Restore the approved state.
11. Record cleanup and cost impact.
12. Write a prevention or governance improvement.

### Starter Example

```text
Business / threat requirement
        |
Cloud architecture
        |
Preventive control
        |
Detective evidence
        |
Response / recovery
        |
Governance feedback
```

### Evidence Template

```text
Lab:
Provider:
Account / subscription:
Region:
Resource:
Owner:
Identity:
Expected secure state:
Observed state:
Policy / command:
Audit evidence:
Finding:
Remediation:
Retest:
Cleanup:
Exception needed?:
```

---


## 6. Mini Project

# Mini Project — Secure AWS Multi-Account Platform

Design an AWS Organization containing security, log archive, infrastructure, production, nonproduction, and sandbox accounts. Apply federation, IAM Identity Center permission sets, selected SCP guardrails, organization CloudTrail/Config, Security Hub CSPM, GuardDuty, Inspector/Macie where relevant, private networking, KMS/secrets, S3 security, Session Manager, workload roles, and an incident-response workflow.

Include sample IAM/SCP policies, a VPC flow matrix, central logging architecture, FSBP/CIS posture plan, one compromised-role tabletop, forensic evidence checklist, and Well-Architected security review.

### Required Deliverables

1. Architecture diagram
2. Threat model
3. Identity model
4. Network flow / segmentation matrix
5. Data and cryptography model
6. Logging / detection architecture
7. IaC / policy-as-code controls
8. Vulnerability / posture workflow
9. Incident-response design
10. Backup / recovery design
11. Governance / ownership matrix
12. Exception process
13. Metrics
14. Validation evidence
15. Executive summary

---

## 7. Recommended Resources

- AWS Well-Architected Security Pillar — https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/
- AWS Security Reference Architecture — https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/
- AWS IAM Security — https://docs.aws.amazon.com/IAM/latest/UserGuide/security.html
- AWS Security Hub CSPM — https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html
- AWS Control Tower — https://docs.aws.amazon.com/controltower/

---

## 8. Certification Relevance

Relevant to AWS security engineering and architecture roles and security-focused AWS certification study. Verify current official exam objectives because AWS certifications evolve.

Cloud products, service names, benchmark versions, licensing, and certification objectives change. Verify current official documentation before production deployment or exam preparation.

---

## 9. Common Mistakes & Best Practices

### Common Mistakes

- Learning security products without understanding architecture.
- Assuming a private subnet or VNet automatically creates trust.
- Permanent administrator privileges for convenience.
- Static workload credentials.
- Encryption without key-governance design.
- Audit logs stored inside the same compromise boundary.
- CSPM score treated as proof of complete security.
- One-off manual exceptions.
- Security policies with no drift monitoring.
- Prevention without tested recovery.

### Best Practices

- Secure the landing zone before scaling workloads.
- Centralize human identity and prefer short-lived sessions.
- Give workloads their own identities.
- Apply least privilege continuously.
- Use private service connectivity when justified by risk.
- Centralize and protect audit evidence.
- Implement controls through IaC and policy as code.
- Combine preventive, detective, and corrective guardrails.
- Map vendor-neutral objectives to provider-specific implementations.
- Continuously validate control health and drift.
- Build incident response and forensic readiness into platform design.
- Track ownership, residual risk, and exception expiry.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the operational meaning of **AWS Shared Responsibility Model**?

**Short answer:** AWS describes responsibility as security of the cloud versus security in the cloud, with the customer's responsibilities changing according to the AWS services selected and their configuration.

### Q2. What is the operational meaning of **AWS Account as a Security Boundary**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q3. What is the operational meaning of **AWS Organizations**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q4. What is the operational meaning of **Organizational Units**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q5. What is the operational meaning of **Management Account Protection**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q6. What is the operational meaning of **Member Accounts**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q7. What is the operational meaning of **Multi-Account Security Strategy**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q8. What is the operational meaning of **AWS Control Tower**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q9. What is the operational meaning of **AWS Landing Zone**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q10. What is the operational meaning of **Account Factory and Account Vending**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q11. What is the operational meaning of **Log Archive Account**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q12. What is the operational meaning of **Security and Audit Account**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q13. What is the operational meaning of **Service Control Policies**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q14. What is the operational meaning of **SCP Evaluation Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q15. What is the operational meaning of **AWS Resource Control Policy Awareness**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q16. What is the operational meaning of **Organization-Wide Guardrails**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q17. What is the operational meaning of **Region Governance**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q18. What is the operational meaning of **AWS Root User**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q19. What is the operational meaning of **Root User MFA**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q20. What is the operational meaning of **Root Access Key Risk**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q21. What is the operational meaning of **AWS IAM**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q22. What is the operational meaning of **IAM User**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q23. What is the operational meaning of **IAM Group**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q24. What is the operational meaning of **IAM Role**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q25. What is the operational meaning of **IAM Policy**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q26. What is the operational meaning of **Identity-Based Policy**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q27. What is the operational meaning of **Resource-Based Policy**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q28. What is the operational meaning of **Trust Policy**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q29. What is the operational meaning of **Permissions Boundary**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q30. What is the operational meaning of **Session Policy**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q31. What is the operational meaning of **Policy Evaluation Logic**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q32. What is the operational meaning of **Explicit Deny**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q33. What is the operational meaning of **Least Privilege in AWS**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q34. What is the operational meaning of **AWS STS**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q35. What is the operational meaning of **Temporary Credentials**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q36. What is the operational meaning of **AssumeRole**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q37. What is the operational meaning of **Role Chaining Awareness**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q38. What is the operational meaning of **Cross-Account Role**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q39. What is the operational meaning of **Federation**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q40. What is the operational meaning of **AWS IAM Identity Center**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q41. What is the operational meaning of **External Identity Provider**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q42. What is the operational meaning of **Permission Sets**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q43. What is the operational meaning of **MFA**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q44. What is the operational meaning of **Passkeys and Phishing-Resistant MFA Awareness**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q45. What is the operational meaning of **Emergency Access**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q46. What is the operational meaning of **IAM Access Analyzer**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q47. What is the operational meaning of **External Access Findings**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q48. What is the operational meaning of **Unused Access Analysis Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q49. What is the operational meaning of **IAM Credential Report**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q50. What is the operational meaning of **Access Key Rotation**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q51. What is the operational meaning of **Service-Linked Roles**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q52. What is the operational meaning of **Workload Identity in AWS**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q53. What is the operational meaning of **EC2 Instance Profile**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q54. What is the operational meaning of **Lambda Execution Role**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q55. What is the operational meaning of **ECS Task Role**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q56. What is the operational meaning of **EKS IAM Integration Awareness**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q57. What is the operational meaning of **IRSA and Pod Identity Awareness**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q58. What is the operational meaning of **Secrets Manager**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q59. What is the operational meaning of **Systems Manager Parameter Store**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q60. What is the operational meaning of **AWS KMS**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q61. What is the operational meaning of **KMS Key**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q62. What is the operational meaning of **Key Policy**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q63. What is the operational meaning of **KMS Grant**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q64. What is the operational meaning of **Envelope Encryption**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q65. What is the operational meaning of **Automatic Key Rotation Awareness**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q66. What is the operational meaning of **CloudHSM Awareness**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q67. What is the operational meaning of **AWS Certificate Manager**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q68. What is the operational meaning of **Private CA Awareness**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q69. What is the operational meaning of **Amazon VPC**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q70. What is the operational meaning of **VPC CIDR Planning**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q71. What is the operational meaning of **Public Subnet**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q72. What is the operational meaning of **Private Subnet**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q73. What is the operational meaning of **Route Table**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q74. What is the operational meaning of **Internet Gateway**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q75. What is the operational meaning of **NAT Gateway**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q76. What is the operational meaning of **Security Group**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q77. What is the operational meaning of **Network ACL**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q78. What is the operational meaning of **VPC Peering**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q79. What is the operational meaning of **Transit Gateway**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q80. What is the operational meaning of **AWS PrivateLink**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q81. What is the operational meaning of **VPC Interface Endpoint**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q82. What is the operational meaning of **VPC Gateway Endpoint**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q83. What is the operational meaning of **VPC Endpoint Policy**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q84. What is the operational meaning of **Route 53 Resolver**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q85. What is the operational meaning of **Route 53 Resolver DNS Firewall Awareness**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q86. What is the operational meaning of **AWS Network Firewall**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q87. What is the operational meaning of **Gateway Load Balancer Awareness**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q88. What is the operational meaning of **Elastic Load Balancing Security**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q89. What is the operational meaning of **Application Load Balancer**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q90. What is the operational meaning of **Network Load Balancer**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q91. What is the operational meaning of **AWS WAF**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q92. What is the operational meaning of **AWS Shield**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q93. What is the operational meaning of **Shield Advanced Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q94. What is the operational meaning of **AWS Firewall Manager**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q95. What is the operational meaning of **VPC Flow Logs**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q96. What is the operational meaning of **Traffic Mirroring Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q97. What is the operational meaning of **Hybrid VPN**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q98. What is the operational meaning of **Direct Connect Security Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q99. What is the operational meaning of **S3 Security**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q100. What is the operational meaning of **S3 Block Public Access**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q101. What is the operational meaning of **S3 Bucket Policy**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q102. What is the operational meaning of **S3 Access Points**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q103. What is the operational meaning of **S3 Object Ownership**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q104. What is the operational meaning of **S3 Versioning**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q105. What is the operational meaning of **S3 Object Lock**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q106. What is the operational meaning of **S3 Encryption**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q107. What is the operational meaning of **S3 KMS Keys**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q108. What is the operational meaning of **Amazon Macie**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q109. What is the operational meaning of **EBS Encryption**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q110. What is the operational meaning of **EBS Snapshot Security**?

**Short answer:** In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Q111. What is the operational meaning of **RDS Security**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q112. What is the operational meaning of **RDS IAM Authentication Awareness**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q113. What is the operational meaning of **RDS Network Isolation**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q114. What is the operational meaning of **DynamoDB Security**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q115. What is the operational meaning of **Database Secrets Rotation**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q116. What is the operational meaning of **AWS Backup**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q117. What is the operational meaning of **Backup Vault**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q118. What is the operational meaning of **Backup Vault Lock Awareness**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q119. What is the operational meaning of **EC2 Security**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q120. What is the operational meaning of **AMI Hardening**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q121. What is the operational meaning of **EC2 IMDSv2**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q122. What is the operational meaning of **Systems Manager Session Manager**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q123. What is the operational meaning of **Avoiding Public SSH RDP**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q124. What is the operational meaning of **Systems Manager Patch Management Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q125. What is the operational meaning of **Amazon Inspector**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q126. What is the operational meaning of **Vulnerability Management**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q127. What is the operational meaning of **ECR Security**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q128. What is the operational meaning of **ECR Image Scanning Awareness**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q129. What is the operational meaning of **ECS Security**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q130. What is the operational meaning of **EKS Security**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q131. What is the operational meaning of **EKS RBAC and IAM Boundary**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q132. What is the operational meaning of **EKS Network Security**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q133. What is the operational meaning of **EKS Secrets Awareness**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q134. What is the operational meaning of **Lambda Security**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q135. What is the operational meaning of **Lambda Resource Policy**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q136. What is the operational meaning of **Lambda Environment Variable Secrets Risk**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q137. What is the operational meaning of **API Gateway Security**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q138. What is the operational meaning of **CloudFront Security**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q139. What is the operational meaning of **CloudFront Origin Access Control Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q140. What is the operational meaning of **CloudTrail**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q141. What is the operational meaning of **Organization Trail**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q142. What is the operational meaning of **CloudTrail Log Integrity**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q143. What is the operational meaning of **CloudTrail Lake Awareness**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q144. What is the operational meaning of **AWS Config**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q145. What is the operational meaning of **Config Rules**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q146. What is the operational meaning of **Conformance Packs Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q147. What is the operational meaning of **CloudWatch Security Monitoring**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q148. What is the operational meaning of **EventBridge for Security Automation**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q149. What is the operational meaning of **Amazon GuardDuty**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q150. What is the operational meaning of **GuardDuty Organization Management**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q151. What is the operational meaning of **GuardDuty Protection Plans Awareness**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q152. What is the operational meaning of **AWS Security Hub CSPM**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q153. What is the operational meaning of **AWS Foundational Security Best Practices**?

**Short answer:** AWS Security Hub CSPM includes the AWS Foundational Security Best Practices standard to identify AWS accounts and resources that deviate from AWS security best practices.

### Q154. What is the operational meaning of **CIS AWS Foundations Benchmark v5.0.0 Awareness**?

**Short answer:** AWS Security Hub CSPM documentation currently supports CIS AWS Foundations Benchmark v5.0.0 and recommends current benchmark use for foundational AWS configuration assessment.

### Q155. What is the operational meaning of **Security Hub Central Configuration**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q156. What is the operational meaning of **Security Hub Findings**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q157. What is the operational meaning of **Amazon Detective Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q158. What is the operational meaning of **Amazon Security Lake**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q159. What is the operational meaning of **Open Cybersecurity Schema Framework Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q160. What is the operational meaning of **Centralized Security Logging**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q161. What is the operational meaning of **AWS Security Reference Architecture**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q162. What is the operational meaning of **AWS Well-Architected Security Pillar**?

**Short answer:** AWS Well-Architected security guidance groups best practices into security foundations, identity and access management, detection, infrastructure protection, data protection, incident response, and application security.

### Q163. What is the operational meaning of **Strong Identity Foundation**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q164. What is the operational meaning of **Traceability**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q165. What is the operational meaning of **Security at All Layers**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q166. What is the operational meaning of **Automating AWS Security Best Practices**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q167. What is the operational meaning of **Protecting Data at Rest and in Transit**?

**Short answer:** In AWS, this topic controls reachability, segmentation, service exposure, ingress, egress, inspection, and private connectivity.

### Q168. What is the operational meaning of **Preparing for AWS Security Events**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q169. What is the operational meaning of **AWS Incident Response**?

**Short answer:** In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Q170. What is the operational meaning of **Compromised Access Key Response**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q171. What is the operational meaning of **Compromised EC2 Response**?

**Short answer:** In AWS, this topic protects cloud workloads across build, deployment, identity, runtime, network, vulnerability, and administrative-access layers.

### Q172. What is the operational meaning of **Compromised IAM Role Response**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q173. What is the operational meaning of **CloudTrail Investigation**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q174. What is the operational meaning of **GuardDuty Investigation**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q175. What is the operational meaning of **Snapshot for Forensics**?

**Short answer:** In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Q176. What is the operational meaning of **Isolation Security Group Pattern**?

**Short answer:** In AWS, this topic supports evidence preservation, identity containment, resource isolation, investigation, recovery, and prevention of recurrence.

### Q177. What is the operational meaning of **Credential Revocation**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q178. What is the operational meaning of **AWS Config Remediation Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q179. What is the operational meaning of **Security Hub Automation Awareness**?

**Short answer:** In AWS, this topic creates or analyzes security evidence used for posture management, detection, investigation, compliance, and incident response.

### Q180. What is the operational meaning of **AWS Organizations Delegated Administrator**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q181. What is the operational meaning of **Centralized Security Services**?

**Short answer:** In AWS, this topic controls which human or workload identity may perform which action on which cloud resource and under which conditions.

### Q182. What is the operational meaning of **AWS Backup and Recovery Security**?

**Short answer:** In AWS, this topic protects sensitive data through classification, authorization, cryptography, lifecycle, backup, and recovery controls.

### Q183. What is the operational meaning of **Multi-Region Security Considerations**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q184. What is the operational meaning of **Service Quotas and Abuse**?

**Short answer:** In AWS, this topic treats abnormal resource consumption and uncontrolled provisioning as both governance and potential security signals.

### Q185. What is the operational meaning of **Budget and Cost Anomaly Security Awareness**?

**Short answer:** In AWS, this topic treats abnormal resource consumption and uncontrolled provisioning as both governance and potential security signals.

### Q186. What is the operational meaning of **Tagging Governance**?

**Short answer:** In AWS, this topic scales security through hierarchy, ownership, baselines, policy, account or subscription boundaries, and automated guardrails.

### Q187. What is the operational meaning of **AWS Compliance Programs Awareness**?

**Short answer:** In AWS, this topic relates cloud implementations and evidence to explicit security-control or assurance objectives without confusing a posture score with full compliance.

### Q188. What is the operational meaning of **AWS Artifact Awareness**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

### Q189. What is the operational meaning of **AWS Audit Manager Awareness**?

**Short answer:** In AWS, this topic relates cloud implementations and evidence to explicit security-control or assurance objectives without confusing a posture score with full compliance.

### Q190. What is the operational meaning of **AWS Security Final Architecture**?

**Short answer:** In AWS, this topic is a cloud-security architecture or governance building block that must have an owner, enforcement point, evidence source, failure mode, and recovery or exception path.

---

# Course Completion Gate

You should be able to take a new cloud workload and answer:

```text
Who owns it?
What data does it process?
Which human identities administer it?
Which workload identities call it?
What is publicly reachable?
What is privately reachable?
Which policies authorize each path?
Where are keys and secrets?
Which logs prove access and change?
Which posture controls detect drift?
How is a compromised identity revoked?
How is a workload isolated?
How is evidence preserved?
How is the workload rebuilt or recovered?
Which guardrails prevent recurrence?
Who can approve an exception?
```
