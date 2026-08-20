# 91. Bug Hunting

> Phase 22 — Penetration Testing

This course is **authorization-first and lab-first**. It builds on Phase 21 and increases testing depth while keeping scope, safety, evidence, and cleanup mandatory.

---

## 1. Topic Title

**Bug Hunting**

---

## 2. Learning Objectives

- Interpret bug-bounty and disclosure program policies before testing.
- Build an in-scope application/API attack-surface inventory.
- Use intercepting proxies and browser tools to test one hypothesis at a time.
- Assess authentication, sessions, object authorization, tenant isolation, and business logic.
- Recognize common injection, SSRF, upload, CORS, OAuth, GraphQL, WebSocket, and cache issues.
- Use automation conservatively and within program rate limits.
- Prove impact using synthetic data and minimal evidence.
- Write clear, reproducible bug reports with remediation suggestions.
- Distinguish false positives, duplicates, and real vulnerabilities.
- Practice responsible disclosure and professional triage communication.

---

## 3. Prerequisites

Required:

```text
85 Ethical Hacking Fundamentals
84 Security Assessment Fundamentals
Web Fundamentals
REST APIs
Browser Developer Tools
Basic JavaScript
Basic HTTP
```

Recommended:
Course 90 before real program participation.

---

## 4. Core Concepts Explanation

# Part 1 — Bug Hunting Definition

### Core Explanation

Bug hunting is systematic security testing of applications and services within an explicit program policy or authorization to identify reportable vulnerabilities.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 2 — Bug Bounty Program

### Core Explanation

A bug bounty program defines eligible assets, rules, severity/reward expectations, reporting workflow, and often safe-harbor conditions.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 3 — Vulnerability Disclosure Program

### Core Explanation

A disclosure program provides a channel and rules for reporting vulnerabilities and may authorize less testing than a bounty program.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 4 — Program Policy

### Core Explanation

The program policy is the primary authority for what may be tested and how.

### Diagram / Command / Workflow Example

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 5 — Safe Harbor

### Core Explanation

Safe-harbor language may protect good-faith research only when the researcher follows the exact program terms.

### Diagram / Command / Workflow Example

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 6 — In-Scope Asset

### Core Explanation

Only assets explicitly listed or unambiguously included by the program should be tested.

### Diagram / Command / Workflow Example

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 7 — Out-of-Scope Asset

### Core Explanation

Do not test assets excluded by policy even if they share infrastructure or credentials with in-scope systems.

### Diagram / Command / Workflow Example

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 8 — Third-Party Asset

### Core Explanation

Third-party SaaS, CDN, analytics, payment, or hosting systems may be out of scope unless explicitly included.

### Diagram / Command / Workflow Example

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 9 — Testing Prohibitions

### Core Explanation

Programs may prohibit denial of service, social engineering, credential attacks, automated scanning, data access, or destructive testing.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 10 — Rate Limits

### Core Explanation

Respect program-specified request rates and keep automation conservative.

### Diagram / Command / Workflow Example

```text
Automation rule:
narrow scope
  ↓
low request rate
  ↓
deduplicate requests
  ↓
stop on instability / WAF abuse signal
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 11 — Account Rules

### Core Explanation

Use your own test accounts unless the program explicitly permits other account types.

### Diagram / Command / Workflow Example

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 12 — Data Handling

### Core Explanation

Avoid accessing or retaining real personal or business data beyond minimal proof.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 13 — Stop After Proof

### Core Explanation

Once a vulnerability is demonstrated, stop further access or escalation unless needed to establish impact safely.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 14 — Recon Strategy

### Core Explanation

Bug hunting starts by understanding the in-scope application, routes, technologies, APIs, roles, and business workflows.

### Diagram / Command / Workflow Example

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 15 — Asset Inventory

### Core Explanation

Maintain a program-specific list of approved hosts, applications, APIs, and test accounts.

### Diagram / Command / Workflow Example

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 16 — Subdomain Discovery Boundary

### Core Explanation

Subdomain discovery should remain tied to in-scope organization-owned domains and program rules.

### Diagram / Command / Workflow Example

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 17 — DNS Review

### Core Explanation

DNS records can reveal application and infrastructure relationships.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 18 — Certificate Transparency Awareness

### Core Explanation

Certificate-transparency data can support asset inventory when the associated host is actually in scope.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 19 — Public Repository Review

### Core Explanation

Organization-owned public repositories may reveal client code, routes, configuration, or accidentally committed secrets.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 20 — JavaScript Review

### Core Explanation

Client-side JavaScript can reveal API routes, feature flags, object models, and application logic.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 21 — Source Map Awareness

### Core Explanation

Published source maps can reveal original source structure and should be assessed according to program policy.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 22 — Technology Fingerprinting

### Core Explanation

Identify frameworks, servers, libraries, and security headers with appropriate uncertainty.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 23 — Route Inventory

### Core Explanation

Build a route/method inventory instead of randomly fuzzing.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 24 — API Inventory

### Core Explanation

Map API base URLs, versions, methods, schemas, roles, and authentication flows.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 25 — Role Matrix

### Core Explanation

Create test accounts representing available roles and document expected permissions.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 26 — Business Workflow Map

### Core Explanation

Document important state transitions such as registration, purchase, refund, approval, invite, sharing, and deletion.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 27 — Authentication Surface

### Core Explanation

Map login, registration, MFA, reset, recovery, session renewal, logout, and device trust.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 28 — Authorization Surface

### Core Explanation

Map object ownership, role-only functions, tenant boundaries, and administrative actions.

### Diagram / Command / Workflow Example

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 29 — Input Surface

### Core Explanation

Map query parameters, JSON fields, headers, cookies, uploads, path segments, GraphQL variables, and WebSocket messages.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 30 — Output Surface

### Core Explanation

Identify where untrusted data is rendered, exported, emailed, logged, or passed to downstream systems.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 31 — File Handling Surface

### Core Explanation

Map upload, import, preview, conversion, download, attachment, and avatar/document workflows.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 32 — Integration Surface

### Core Explanation

Third-party callbacks, webhooks, OAuth, SSO, payment, storage, and messaging integrations may introduce unique trust boundaries.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 33 — Burp Suite Workflow

### Core Explanation

An intercepting proxy helps organize requests, replay test cases, compare roles, and preserve evidence.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 34 — OWASP ZAP Workflow

### Core Explanation

ZAP can support proxying and controlled scanning against approved targets.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 35 — Browser DevTools

### Core Explanation

Developer tools help inspect network requests, storage, client code, and security behavior.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 36 — HTTP Request Repeater

### Core Explanation

Manual request replay is useful for testing one hypothesis at a time without high-rate automation.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 37 — Request Comparison

### Core Explanation

Compare two roles or object IDs while changing only one variable so authorization conclusions are reliable.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 38 — Authentication Testing

### Core Explanation

Test account enumeration, MFA consistency, reset behavior, session creation, and lockout/rate controls safely.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 39 — Account Enumeration

### Core Explanation

Differences in messages, timing, or status can reveal whether an account exists.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 40 — Password Reset

### Core Explanation

Reset tokens should be unpredictable, short-lived, single-use, scoped to one account/action, and invalidated after use.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 41 — MFA Bypass Awareness

### Core Explanation

Check whether alternate login or recovery flows unexpectedly avoid MFA.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 42 — Session Fixation Awareness

### Core Explanation

Applications should rotate session identifiers across authentication changes.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 43 — Session Expiry

### Core Explanation

Validate inactivity and absolute session expiration according to risk.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 44 — Logout

### Core Explanation

Logout should invalidate the relevant server-side session or token state where applicable.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 45 — Cookie Security

### Core Explanation

Review Secure, HttpOnly, SameSite, domain, path, lifetime, and session binding.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 46 — JWT Review

### Core Explanation

Validate signature, issuer, audience, expiration, required claims, and authorization behavior rather than trusting decoded content.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 47 — Object-Level Authorization

### Core Explanation

Test whether one test user can access another user's object by changing only the object reference.

### Diagram / Command / Workflow Example

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 48 — BOLA / IDOR Awareness

### Core Explanation

Broken object-level authorization is a common API/application weakness where object identifiers are accepted without ownership checks.

### Diagram / Command / Workflow Example

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 49 — Function-Level Authorization

### Core Explanation

Administrative or role-restricted actions require server-side authorization even if the UI hides them.

### Diagram / Command / Workflow Example

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 50 — Tenant Isolation

### Core Explanation

A user in one tenant must not read or modify another tenant's data or configuration.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 51 — Mass Assignment

### Core Explanation

Unexpected writable fields can allow changes to role, price, owner, tenant, or security-sensitive state.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 52 — Business Logic

### Core Explanation

High-value bugs often arise from workflow mistakes rather than generic injection.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 53 — State Machine Testing

### Core Explanation

Try invalid transitions such as approving before creation or reusing one-time actions.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 54 — Double-Spend / Replay Awareness

### Core Explanation

Repeated requests may reveal missing idempotency or race controls; use synthetic transactions and bounded testing.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 55 — Race Condition Awareness

### Core Explanation

Concurrent requests can bypass limits or create duplicate effects and should be tested only when program policy permits.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 56 — Price / Quantity Logic

### Core Explanation

Client-controlled price, discount, currency, or quantity fields require server-side validation.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 57 — Privilege Workflow

### Core Explanation

Invite, role change, approval, refund, password reset, and account-linking workflows deserve detailed authorization review.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 58 — SQL Injection Awareness

### Core Explanation

Test only with minimal non-destructive payloads and stop after confirming behavior.

### Diagram / Command / Workflow Example

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 59 — Cross-Site Scripting

### Core Explanation

Test reflected, stored, and DOM sinks safely using harmless proof strings.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 60 — Command Injection Awareness

### Core Explanation

Command-injection testing should avoid destructive commands and use fixed harmless proof where permitted.

### Diagram / Command / Workflow Example

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 61 — Path Traversal

### Core Explanation

Validate whether file path input can escape an intended directory boundary without reading unrelated sensitive files.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 62 — SSRF

### Core Explanation

Test whether server-side fetch functions can reach unintended destinations using safe endpoints and never third-party/internal sensitive systems without authorization.

### Diagram / Command / Workflow Example

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 63 — Open Redirect

### Core Explanation

Validate untrusted redirect destinations where they create phishing or token-flow impact.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 64 — XXE Awareness

### Core Explanation

XML parsers should disable unsafe external entities or network resolution.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 65 — Template Injection Awareness

### Core Explanation

Template code/data separation should prevent user input from becoming template instructions.

### Diagram / Command / Workflow Example

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 66 — Deserialization Awareness

### Core Explanation

Unsafe object deserialization can create serious vulnerabilities and should be assessed conservatively.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 67 — File Upload Security

### Core Explanation

Review file type, size, content, storage path, execution risk, scanning, and authorization.

### Diagram / Command / Workflow Example

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 68 — Content-Type Trust

### Core Explanation

Do not assume a client-supplied Content-Type proves file content.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 69 — Image Processing Risk Awareness

### Core Explanation

Image/document conversion libraries can expand attack surface and should be patched and sandboxed.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 70 — CORS

### Core Explanation

Review whether allowed origins, credentials, and methods enable unintended browser access.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 71 — CSP

### Core Explanation

CSP can reduce exploitability of some browser injection issues but does not fix the underlying sink.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 72 — Clickjacking Awareness

### Core Explanation

Framing controls matter when sensitive actions can be embedded in attacker-controlled pages.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 73 — CSRF Awareness

### Core Explanation

State-changing browser requests require anti-CSRF design when cookies or ambient credentials are used.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 74 — Cache Security

### Core Explanation

Shared caches must not serve one user's private response to another.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 75 — Host Header Awareness

### Core Explanation

Applications should validate trusted host/proxy headers where they influence links, routing, or security decisions.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 76 — HTTP Request Smuggling Awareness

### Core Explanation

Front-end/back-end HTTP parsing disagreement is an advanced class and should be tested only in dedicated labs or programs explicitly permitting it.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 77 — Web Cache Poisoning Awareness

### Core Explanation

Cache-key differences can create unintended cross-user behavior; advanced testing should remain controlled.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 78 — GraphQL Introspection Awareness

### Core Explanation

GraphQL schema visibility can aid testing but authorization must still be enforced at resolvers.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 79 — GraphQL Query Complexity

### Core Explanation

Unbounded query depth or cost can create resource exhaustion and requires careful non-disruptive testing.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 80 — WebSocket Authorization

### Core Explanation

Long-lived connections require authentication and per-message authorization.

### Diagram / Command / Workflow Example

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 81 — OAuth Security Awareness

### Core Explanation

Review redirect URIs, state/PKCE, scopes, token audience, and account-linking logic.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 82 — SSO / SAML Awareness

### Core Explanation

Federated login requires correct issuer, audience, signature, assertion, and account-linking validation.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 83 — Webhook Security

### Core Explanation

Webhooks need authenticity verification, replay protection, destination controls, and secret rotation.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 84 — API Key Exposure

### Core Explanation

Keys in client code, logs, URLs, repositories, or mobile apps may be exposed and should be scoped and rotated.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 85 — Secret Reporting

### Core Explanation

Do not use exposed credentials beyond minimal proof; report and encourage immediate rotation.

### Diagram / Command / Workflow Example

```text
Report quality:
clear title
reproducible steps
minimal proof
impact
affected asset
evidence
suggested remediation
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 86 — Information Disclosure

### Core Explanation

Debug pages, stack traces, source maps, headers, backups, and verbose errors can leak sensitive implementation details.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 87 — Sensitive Data Exposure

### Core Explanation

Avoid collecting real sensitive records; use metadata or synthetic evidence where possible.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 88 — Security Misconfiguration

### Core Explanation

Default credentials, debug mode, public admin interfaces, permissive CORS, weak headers, and broad storage access are common bugs.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 89 — Dependency Vulnerability

### Core Explanation

A vulnerable dependency matters only when the affected code/version and exploit conditions actually apply.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 90 — Cloud-Backed Web App Awareness

### Core Explanation

Web bugs may interact with cloud storage, metadata, IAM, and signed URLs, but program scope still controls testing.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 91 — Signed URL Review

### Core Explanation

Validate expiry, object scope, method, and authorization before issuing signed URLs.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 92 — Object Storage Exposure

### Core Explanation

Public or predictable object access can create data exposure and should be tested minimally.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 93 — Bug Hypothesis

### Core Explanation

Write a specific hypothesis before testing instead of spraying random payloads.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 94 — One Variable at a Time

### Core Explanation

Change one request element at a time so the cause of a result is clear.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 95 — Minimal Reproduction

### Core Explanation

A strong bug report contains the shortest reliable steps that demonstrate the condition.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 96 — Impact Proof

### Core Explanation

Prove impact with synthetic data or metadata rather than escalating unnecessarily.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 97 — Severity

### Core Explanation

Severity should reflect realistic impact and exploitability rather than novelty.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 98 — Duplicate Awareness

### Core Explanation

Search program guidance and your own reports to reduce duplicate submissions.

### Diagram / Command / Workflow Example

```text
Report quality:
clear title
reproducible steps
minimal proof
impact
affected asset
evidence
suggested remediation
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 99 — Report Title

### Core Explanation

Use a precise vulnerability condition and affected feature in the title.

### Diagram / Command / Workflow Example

```text
Report quality:
clear title
reproducible steps
minimal proof
impact
affected asset
evidence
suggested remediation
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 100 — Report Summary

### Core Explanation

Explain what is wrong and why it matters in one short paragraph.

### Diagram / Command / Workflow Example

```text
Report quality:
clear title
reproducible steps
minimal proof
impact
affected asset
evidence
suggested remediation
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 101 — Reproduction Steps

### Core Explanation

Provide numbered steps using test accounts and reproducible requests.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 102 — Evidence

### Core Explanation

Attach screenshots or request/response excerpts while redacting secrets.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 103 — Impact

### Core Explanation

Explain confidentiality, integrity, availability, financial, identity, or tenant impact.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 104 — Remediation Suggestion

### Core Explanation

Offer root-cause-oriented remediation rather than only blocking one payload.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 105 — Program Communication

### Core Explanation

Respond professionally to triage questions and provide clarification without expanding scope.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 106 — Retest After Fix

### Core Explanation

Verify the fix using the original safe proof when the program requests retesting.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 107 — Research Notes

### Core Explanation

Keep private notes on hypotheses, tested routes, roles, parameters, and results.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 108 — Automation Boundary

### Core Explanation

Automate repetitive in-scope discovery or parameter handling conservatively and respect rate limits.

### Diagram / Command / Workflow Example

```text
Automation rule:
narrow scope
  ↓
low request rate
  ↓
deduplicate requests
  ↓
stop on instability / WAF abuse signal
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 109 — Wordlist Discipline

### Core Explanation

Use narrow context-specific wordlists instead of indiscriminate huge scans.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 110 — Scanner Noise

### Core Explanation

Automated scanners can create duplicates and false positives; manual validation remains necessary.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 111 — WAF Interaction

### Core Explanation

A WAF can change behavior but does not prove the underlying vulnerability is fixed.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 112 — False Positive

### Core Explanation

A strange response is not a vulnerability until the security property is clearly violated.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 113 — False Negative

### Core Explanation

Absence of scanner output does not prove the application is secure.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 114 — Responsible Disclosure

### Core Explanation

Report privately through the approved channel and avoid public disclosure before coordinated resolution.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 115 — Bug Hunting Ethics

### Core Explanation

Respect program terms, privacy, availability, and other users.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

# Part 116 — Bug Hunting Final Mental Model

### Core Explanation

Read the policy, map the application, form hypotheses, test minimally, prove impact safely, report clearly, and stop.

### Diagram / Command / Workflow Example

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Why It Matters

The purpose is to understand **what security condition is being tested, why the test is authorized, what minimum evidence is sufficient, and how the result improves defense**.

### Practical Use

Use only an isolated lab, a deliberately vulnerable target, a bug-bounty program whose current policy explicitly authorizes the action, or another written scope.

### Common Problems

- Treating tool output as proof without understanding the target.
- Expanding scope because another system is reachable.
- Using high-impact techniques where configuration or low-impact proof is enough.
- Collecting unnecessary credentials, personal data, or business information.
- Failing to record exact requests, commands, module options, and timestamps.
- Continuing after sufficient evidence is obtained.
- Forgetting cleanup and retest.

### Best Practice

Start from authorization and a testable hypothesis, use the least intrusive technique that answers it, preserve evidence, stop after proof, and connect the finding to remediation and retest.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Bug Hunting Definition

### Objective

Practice **Bug Hunting Definition** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 2 — Bug Bounty Program

### Objective

Practice **Bug Bounty Program** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 3 — Vulnerability Disclosure Program

### Objective

Practice **Vulnerability Disclosure Program** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 4 — Program Policy

### Objective

Practice **Program Policy** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 5 — Safe Harbor

### Objective

Practice **Safe Harbor** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 6 — In-Scope Asset

### Objective

Practice **In-Scope Asset** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 7 — Out-of-Scope Asset

### Objective

Practice **Out-of-Scope Asset** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 8 — Third-Party Asset

### Objective

Practice **Third-Party Asset** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 9 — Testing Prohibitions

### Objective

Practice **Testing Prohibitions** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 10 — Rate Limits

### Objective

Practice **Rate Limits** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Automation rule:
narrow scope
  ↓
low request rate
  ↓
deduplicate requests
  ↓
stop on instability / WAF abuse signal
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 11 — Account Rules

### Objective

Practice **Account Rules** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Program policy
  ↓
in-scope assets
  ↓
allowed testing
  ↓
prohibited testing
  ↓
rate limits
  ↓
reporting channel
  ↓
safe-harbor terms
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 12 — Data Handling

### Objective

Practice **Data Handling** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 13 — Stop After Proof

### Objective

Practice **Stop After Proof** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 14 — Recon Strategy

### Objective

Practice **Recon Strategy** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 15 — Asset Inventory

### Objective

Practice **Asset Inventory** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 16 — Subdomain Discovery Boundary

### Objective

Practice **Subdomain Discovery Boundary** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
In-scope root domain
   ↓
owned subdomains / apps / APIs
   ↓
technology / route inventory
   ↓
prioritized test surface
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 17 — DNS Review

### Objective

Practice **DNS Review** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 18 — Certificate Transparency Awareness

### Objective

Practice **Certificate Transparency Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 19 — Public Repository Review

### Objective

Practice **Public Repository Review** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 20 — JavaScript Review

### Objective

Practice **JavaScript Review** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 21 — Source Map Awareness

### Objective

Practice **Source Map Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 22 — Technology Fingerprinting

### Objective

Practice **Technology Fingerprinting** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 23 — Route Inventory

### Objective

Practice **Route Inventory** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 24 — API Inventory

### Objective

Practice **API Inventory** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 25 — Role Matrix

### Objective

Practice **Role Matrix** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 26 — Business Workflow Map

### Objective

Practice **Business Workflow Map** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 27 — Authentication Surface

### Objective

Practice **Authentication Surface** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 28 — Authorization Surface

### Objective

Practice **Authorization Surface** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 29 — Input Surface

### Objective

Practice **Input Surface** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 30 — Output Surface

### Objective

Practice **Output Surface** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 31 — File Handling Surface

### Objective

Practice **File Handling Surface** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 32 — Integration Surface

### Objective

Practice **Integration Surface** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 33 — Burp Suite Workflow

### Objective

Practice **Burp Suite Workflow** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 34 — OWASP ZAP Workflow

### Objective

Practice **OWASP ZAP Workflow** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 35 — Browser DevTools

### Objective

Practice **Browser DevTools** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 36 — HTTP Request Repeater

### Objective

Practice **HTTP Request Repeater** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 37 — Request Comparison

### Objective

Practice **Request Comparison** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 38 — Authentication Testing

### Objective

Practice **Authentication Testing** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 39 — Account Enumeration

### Objective

Practice **Account Enumeration** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 40 — Password Reset

### Objective

Practice **Password Reset** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 41 — MFA Bypass Awareness

### Objective

Practice **MFA Bypass Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 42 — Session Fixation Awareness

### Objective

Practice **Session Fixation Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 43 — Session Expiry

### Objective

Practice **Session Expiry** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 44 — Logout

### Objective

Practice **Logout** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 45 — Cookie Security

### Objective

Practice **Cookie Security** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 46 — JWT Review

### Objective

Practice **JWT Review** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 47 — Object-Level Authorization

### Objective

Practice **Object-Level Authorization** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 48 — BOLA / IDOR Awareness

### Objective

Practice **BOLA / IDOR Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 49 — Function-Level Authorization

### Objective

Practice **Function-Level Authorization** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Test account A owns object A
Test account B owns object B

B requests A
  ↓
expected DENY

Use only synthetic / program-approved data.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 50 — Tenant Isolation

### Objective

Practice **Tenant Isolation** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 51 — Mass Assignment

### Objective

Practice **Mass Assignment** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 52 — Business Logic

### Objective

Practice **Business Logic** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 53 — State Machine Testing

### Objective

Practice **State Machine Testing** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 54 — Double-Spend / Replay Awareness

### Objective

Practice **Double-Spend / Replay Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 55 — Race Condition Awareness

### Objective

Practice **Race Condition Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 56 — Price / Quantity Logic

### Objective

Practice **Price / Quantity Logic** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 57 — Privilege Workflow

### Objective

Practice **Privilege Workflow** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 58 — SQL Injection Awareness

### Objective

Practice **SQL Injection Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 59 — Cross-Site Scripting

### Objective

Practice **Cross-Site Scripting** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 60 — Command Injection Awareness

### Objective

Practice **Command Injection Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 61 — Path Traversal

### Objective

Practice **Path Traversal** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 62 — SSRF

### Objective

Practice **SSRF** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 63 — Open Redirect

### Objective

Practice **Open Redirect** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 64 — XXE Awareness

### Objective

Practice **XXE Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 65 — Template Injection Awareness

### Objective

Practice **Template Injection Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 66 — Deserialization Awareness

### Objective

Practice **Deserialization Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 67 — File Upload Security

### Objective

Practice **File Upload Security** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Input
  ↓
trusted boundary
  ↓
server processing
  ↓
output / downstream action

Goal:
prove the class safely
without destructive or third-party impact.
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 68 — Content-Type Trust

### Objective

Practice **Content-Type Trust** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 69 — Image Processing Risk Awareness

### Objective

Practice **Image Processing Risk Awareness** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 70 — CORS

### Objective

Practice **CORS** in an isolated or explicitly authorized environment.

### Safety Boundary

Use only your own lab systems, intentionally vulnerable applications, synthetic accounts/data, or systems clearly covered by written authorization or a bug-bounty program policy.

### Procedure

1. Record scope.
2. Record target and owner.
3. State the expected secure behavior.
4. Start with passive/read-only evidence.
5. Perform the minimum authorized test.
6. Stop once sufficient proof is obtained.
7. Save evidence.
8. Explain impact.
9. Recommend remediation.
10. Clean up.
11. Retest after the fix.

### Starter Workflow

```text
Policy
  ↓
Scope
  ↓
Hypothesis
  ↓
Minimal test
  ↓
Proof
  ↓
Impact
  ↓
Report
```

### Evidence Template

```text
Lab:
Target:
Authorization source:
Objective:
Method:
Expected result:
Observed result:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## 6. Mini Project

# Mini Project — Bug Hunting Practice Program

Use only an intentionally vulnerable web application or a self-hosted lab. Write a mock bounty policy, define scope, create two synthetic user roles, map routes/APIs, identify at least five reportable security issues, produce triage-ready reports with minimal proof and remediation, then fix and retest at least three.

### Required Deliverables

1. Authorization / program policy reference
2. Scope
3. Test plan
4. Asset / route / service inventory
5. Evidence repository
6. Validated findings
7. Risk / impact analysis
8. Remediation recommendations
9. Detection or monitoring observations where applicable
10. Cleanup
11. Retest notes
12. Executive or triage-ready summary

---

## 7. Recommended Resources

- OWASP Web Security Testing Guide — https://owasp.org/www-project-web-security-testing-guide/
- OWASP ASVS — https://owasp.org/www-project-application-security-verification-standard/
- PortSwigger Web Security Academy — https://portswigger.net/web-security
- HackerOne Hacktivity / policy learning — https://hackerone.com/hacktivity
- Bugcrowd University — https://www.bugcrowd.com/hackers/bugcrowd-university/

---

## 8. Certification Relevance

Relevant to application-security testing, vulnerability research, bug-bounty participation, web penetration testing, and later Course 92.

---

## 9. Common Mistakes & Best Practices

### Common Mistakes

- Treating a tool as a substitute for methodology.
- Testing assets outside explicit scope.
- Using production credentials or real sensitive data unnecessarily.
- Running an exploit before verifying preconditions.
- Continuing after sufficient proof is available.
- Reporting raw scanner/module output without validation.
- Failing to record tool/module versions and exact steps.
- Leaving sessions, jobs, files, test accounts, or temporary rules behind.
- Ignoring defensive telemetry and remediation.

### Best Practices

- Verify authorization before every meaningful step.
- Prefer the least intrusive proof that answers the question.
- Use snapshots and intentionally vulnerable targets for exploit labs.
- Keep test data synthetic.
- Record exact steps and timestamps.
- Stop on instability or scope uncertainty.
- Explain business impact, not only technical behavior.
- Clean up and retest.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the core lesson of **Bug Hunting Definition**?

**Short answer:** Bug hunting is systematic security testing of applications and services within an explicit program policy or authorization to identify reportable vulnerabilities.

### Q2. What is the core lesson of **Bug Bounty Program**?

**Short answer:** A bug bounty program defines eligible assets, rules, severity/reward expectations, reporting workflow, and often safe-harbor conditions.

### Q3. What is the core lesson of **Vulnerability Disclosure Program**?

**Short answer:** A disclosure program provides a channel and rules for reporting vulnerabilities and may authorize less testing than a bounty program.

### Q4. What is the core lesson of **Program Policy**?

**Short answer:** The program policy is the primary authority for what may be tested and how.

### Q5. What is the core lesson of **Safe Harbor**?

**Short answer:** Safe-harbor language may protect good-faith research only when the researcher follows the exact program terms.

### Q6. What is the core lesson of **In-Scope Asset**?

**Short answer:** Only assets explicitly listed or unambiguously included by the program should be tested.

### Q7. What is the core lesson of **Out-of-Scope Asset**?

**Short answer:** Do not test assets excluded by policy even if they share infrastructure or credentials with in-scope systems.

### Q8. What is the core lesson of **Third-Party Asset**?

**Short answer:** Third-party SaaS, CDN, analytics, payment, or hosting systems may be out of scope unless explicitly included.

### Q9. What is the core lesson of **Testing Prohibitions**?

**Short answer:** Programs may prohibit denial of service, social engineering, credential attacks, automated scanning, data access, or destructive testing.

### Q10. What is the core lesson of **Rate Limits**?

**Short answer:** Respect program-specified request rates and keep automation conservative.

### Q11. What is the core lesson of **Account Rules**?

**Short answer:** Use your own test accounts unless the program explicitly permits other account types.

### Q12. What is the core lesson of **Data Handling**?

**Short answer:** Avoid accessing or retaining real personal or business data beyond minimal proof.

### Q13. What is the core lesson of **Stop After Proof**?

**Short answer:** Once a vulnerability is demonstrated, stop further access or escalation unless needed to establish impact safely.

### Q14. What is the core lesson of **Recon Strategy**?

**Short answer:** Bug hunting starts by understanding the in-scope application, routes, technologies, APIs, roles, and business workflows.

### Q15. What is the core lesson of **Asset Inventory**?

**Short answer:** Maintain a program-specific list of approved hosts, applications, APIs, and test accounts.

### Q16. What is the core lesson of **Subdomain Discovery Boundary**?

**Short answer:** Subdomain discovery should remain tied to in-scope organization-owned domains and program rules.

### Q17. What is the core lesson of **DNS Review**?

**Short answer:** DNS records can reveal application and infrastructure relationships.

### Q18. What is the core lesson of **Certificate Transparency Awareness**?

**Short answer:** Certificate-transparency data can support asset inventory when the associated host is actually in scope.

### Q19. What is the core lesson of **Public Repository Review**?

**Short answer:** Organization-owned public repositories may reveal client code, routes, configuration, or accidentally committed secrets.

### Q20. What is the core lesson of **JavaScript Review**?

**Short answer:** Client-side JavaScript can reveal API routes, feature flags, object models, and application logic.

### Q21. What is the core lesson of **Source Map Awareness**?

**Short answer:** Published source maps can reveal original source structure and should be assessed according to program policy.

### Q22. What is the core lesson of **Technology Fingerprinting**?

**Short answer:** Identify frameworks, servers, libraries, and security headers with appropriate uncertainty.

### Q23. What is the core lesson of **Route Inventory**?

**Short answer:** Build a route/method inventory instead of randomly fuzzing.

### Q24. What is the core lesson of **API Inventory**?

**Short answer:** Map API base URLs, versions, methods, schemas, roles, and authentication flows.

### Q25. What is the core lesson of **Role Matrix**?

**Short answer:** Create test accounts representing available roles and document expected permissions.

### Q26. What is the core lesson of **Business Workflow Map**?

**Short answer:** Document important state transitions such as registration, purchase, refund, approval, invite, sharing, and deletion.

### Q27. What is the core lesson of **Authentication Surface**?

**Short answer:** Map login, registration, MFA, reset, recovery, session renewal, logout, and device trust.

### Q28. What is the core lesson of **Authorization Surface**?

**Short answer:** Map object ownership, role-only functions, tenant boundaries, and administrative actions.

### Q29. What is the core lesson of **Input Surface**?

**Short answer:** Map query parameters, JSON fields, headers, cookies, uploads, path segments, GraphQL variables, and WebSocket messages.

### Q30. What is the core lesson of **Output Surface**?

**Short answer:** Identify where untrusted data is rendered, exported, emailed, logged, or passed to downstream systems.

### Q31. What is the core lesson of **File Handling Surface**?

**Short answer:** Map upload, import, preview, conversion, download, attachment, and avatar/document workflows.

### Q32. What is the core lesson of **Integration Surface**?

**Short answer:** Third-party callbacks, webhooks, OAuth, SSO, payment, storage, and messaging integrations may introduce unique trust boundaries.

### Q33. What is the core lesson of **Burp Suite Workflow**?

**Short answer:** An intercepting proxy helps organize requests, replay test cases, compare roles, and preserve evidence.

### Q34. What is the core lesson of **OWASP ZAP Workflow**?

**Short answer:** ZAP can support proxying and controlled scanning against approved targets.

### Q35. What is the core lesson of **Browser DevTools**?

**Short answer:** Developer tools help inspect network requests, storage, client code, and security behavior.

### Q36. What is the core lesson of **HTTP Request Repeater**?

**Short answer:** Manual request replay is useful for testing one hypothesis at a time without high-rate automation.

### Q37. What is the core lesson of **Request Comparison**?

**Short answer:** Compare two roles or object IDs while changing only one variable so authorization conclusions are reliable.

### Q38. What is the core lesson of **Authentication Testing**?

**Short answer:** Test account enumeration, MFA consistency, reset behavior, session creation, and lockout/rate controls safely.

### Q39. What is the core lesson of **Account Enumeration**?

**Short answer:** Differences in messages, timing, or status can reveal whether an account exists.

### Q40. What is the core lesson of **Password Reset**?

**Short answer:** Reset tokens should be unpredictable, short-lived, single-use, scoped to one account/action, and invalidated after use.

### Q41. What is the core lesson of **MFA Bypass Awareness**?

**Short answer:** Check whether alternate login or recovery flows unexpectedly avoid MFA.

### Q42. What is the core lesson of **Session Fixation Awareness**?

**Short answer:** Applications should rotate session identifiers across authentication changes.

### Q43. What is the core lesson of **Session Expiry**?

**Short answer:** Validate inactivity and absolute session expiration according to risk.

### Q44. What is the core lesson of **Logout**?

**Short answer:** Logout should invalidate the relevant server-side session or token state where applicable.

### Q45. What is the core lesson of **Cookie Security**?

**Short answer:** Review Secure, HttpOnly, SameSite, domain, path, lifetime, and session binding.

### Q46. What is the core lesson of **JWT Review**?

**Short answer:** Validate signature, issuer, audience, expiration, required claims, and authorization behavior rather than trusting decoded content.

### Q47. What is the core lesson of **Object-Level Authorization**?

**Short answer:** Test whether one test user can access another user's object by changing only the object reference.

### Q48. What is the core lesson of **BOLA / IDOR Awareness**?

**Short answer:** Broken object-level authorization is a common API/application weakness where object identifiers are accepted without ownership checks.

### Q49. What is the core lesson of **Function-Level Authorization**?

**Short answer:** Administrative or role-restricted actions require server-side authorization even if the UI hides them.

### Q50. What is the core lesson of **Tenant Isolation**?

**Short answer:** A user in one tenant must not read or modify another tenant's data or configuration.

### Q51. What is the core lesson of **Mass Assignment**?

**Short answer:** Unexpected writable fields can allow changes to role, price, owner, tenant, or security-sensitive state.

### Q52. What is the core lesson of **Business Logic**?

**Short answer:** High-value bugs often arise from workflow mistakes rather than generic injection.

### Q53. What is the core lesson of **State Machine Testing**?

**Short answer:** Try invalid transitions such as approving before creation or reusing one-time actions.

### Q54. What is the core lesson of **Double-Spend / Replay Awareness**?

**Short answer:** Repeated requests may reveal missing idempotency or race controls; use synthetic transactions and bounded testing.

### Q55. What is the core lesson of **Race Condition Awareness**?

**Short answer:** Concurrent requests can bypass limits or create duplicate effects and should be tested only when program policy permits.

### Q56. What is the core lesson of **Price / Quantity Logic**?

**Short answer:** Client-controlled price, discount, currency, or quantity fields require server-side validation.

### Q57. What is the core lesson of **Privilege Workflow**?

**Short answer:** Invite, role change, approval, refund, password reset, and account-linking workflows deserve detailed authorization review.

### Q58. What is the core lesson of **SQL Injection Awareness**?

**Short answer:** Test only with minimal non-destructive payloads and stop after confirming behavior.

### Q59. What is the core lesson of **Cross-Site Scripting**?

**Short answer:** Test reflected, stored, and DOM sinks safely using harmless proof strings.

### Q60. What is the core lesson of **Command Injection Awareness**?

**Short answer:** Command-injection testing should avoid destructive commands and use fixed harmless proof where permitted.

### Q61. What is the core lesson of **Path Traversal**?

**Short answer:** Validate whether file path input can escape an intended directory boundary without reading unrelated sensitive files.

### Q62. What is the core lesson of **SSRF**?

**Short answer:** Test whether server-side fetch functions can reach unintended destinations using safe endpoints and never third-party/internal sensitive systems without authorization.

### Q63. What is the core lesson of **Open Redirect**?

**Short answer:** Validate untrusted redirect destinations where they create phishing or token-flow impact.

### Q64. What is the core lesson of **XXE Awareness**?

**Short answer:** XML parsers should disable unsafe external entities or network resolution.

### Q65. What is the core lesson of **Template Injection Awareness**?

**Short answer:** Template code/data separation should prevent user input from becoming template instructions.

### Q66. What is the core lesson of **Deserialization Awareness**?

**Short answer:** Unsafe object deserialization can create serious vulnerabilities and should be assessed conservatively.

### Q67. What is the core lesson of **File Upload Security**?

**Short answer:** Review file type, size, content, storage path, execution risk, scanning, and authorization.

### Q68. What is the core lesson of **Content-Type Trust**?

**Short answer:** Do not assume a client-supplied Content-Type proves file content.

### Q69. What is the core lesson of **Image Processing Risk Awareness**?

**Short answer:** Image/document conversion libraries can expand attack surface and should be patched and sandboxed.

### Q70. What is the core lesson of **CORS**?

**Short answer:** Review whether allowed origins, credentials, and methods enable unintended browser access.

### Q71. What is the core lesson of **CSP**?

**Short answer:** CSP can reduce exploitability of some browser injection issues but does not fix the underlying sink.

### Q72. What is the core lesson of **Clickjacking Awareness**?

**Short answer:** Framing controls matter when sensitive actions can be embedded in attacker-controlled pages.

### Q73. What is the core lesson of **CSRF Awareness**?

**Short answer:** State-changing browser requests require anti-CSRF design when cookies or ambient credentials are used.

### Q74. What is the core lesson of **Cache Security**?

**Short answer:** Shared caches must not serve one user's private response to another.

### Q75. What is the core lesson of **Host Header Awareness**?

**Short answer:** Applications should validate trusted host/proxy headers where they influence links, routing, or security decisions.

### Q76. What is the core lesson of **HTTP Request Smuggling Awareness**?

**Short answer:** Front-end/back-end HTTP parsing disagreement is an advanced class and should be tested only in dedicated labs or programs explicitly permitting it.

### Q77. What is the core lesson of **Web Cache Poisoning Awareness**?

**Short answer:** Cache-key differences can create unintended cross-user behavior; advanced testing should remain controlled.

### Q78. What is the core lesson of **GraphQL Introspection Awareness**?

**Short answer:** GraphQL schema visibility can aid testing but authorization must still be enforced at resolvers.

### Q79. What is the core lesson of **GraphQL Query Complexity**?

**Short answer:** Unbounded query depth or cost can create resource exhaustion and requires careful non-disruptive testing.

### Q80. What is the core lesson of **WebSocket Authorization**?

**Short answer:** Long-lived connections require authentication and per-message authorization.

### Q81. What is the core lesson of **OAuth Security Awareness**?

**Short answer:** Review redirect URIs, state/PKCE, scopes, token audience, and account-linking logic.

### Q82. What is the core lesson of **SSO / SAML Awareness**?

**Short answer:** Federated login requires correct issuer, audience, signature, assertion, and account-linking validation.

### Q83. What is the core lesson of **Webhook Security**?

**Short answer:** Webhooks need authenticity verification, replay protection, destination controls, and secret rotation.

### Q84. What is the core lesson of **API Key Exposure**?

**Short answer:** Keys in client code, logs, URLs, repositories, or mobile apps may be exposed and should be scoped and rotated.

### Q85. What is the core lesson of **Secret Reporting**?

**Short answer:** Do not use exposed credentials beyond minimal proof; report and encourage immediate rotation.

### Q86. What is the core lesson of **Information Disclosure**?

**Short answer:** Debug pages, stack traces, source maps, headers, backups, and verbose errors can leak sensitive implementation details.

### Q87. What is the core lesson of **Sensitive Data Exposure**?

**Short answer:** Avoid collecting real sensitive records; use metadata or synthetic evidence where possible.

### Q88. What is the core lesson of **Security Misconfiguration**?

**Short answer:** Default credentials, debug mode, public admin interfaces, permissive CORS, weak headers, and broad storage access are common bugs.

### Q89. What is the core lesson of **Dependency Vulnerability**?

**Short answer:** A vulnerable dependency matters only when the affected code/version and exploit conditions actually apply.

### Q90. What is the core lesson of **Cloud-Backed Web App Awareness**?

**Short answer:** Web bugs may interact with cloud storage, metadata, IAM, and signed URLs, but program scope still controls testing.

### Q91. What is the core lesson of **Signed URL Review**?

**Short answer:** Validate expiry, object scope, method, and authorization before issuing signed URLs.

### Q92. What is the core lesson of **Object Storage Exposure**?

**Short answer:** Public or predictable object access can create data exposure and should be tested minimally.

### Q93. What is the core lesson of **Bug Hypothesis**?

**Short answer:** Write a specific hypothesis before testing instead of spraying random payloads.

### Q94. What is the core lesson of **One Variable at a Time**?

**Short answer:** Change one request element at a time so the cause of a result is clear.

### Q95. What is the core lesson of **Minimal Reproduction**?

**Short answer:** A strong bug report contains the shortest reliable steps that demonstrate the condition.

### Q96. What is the core lesson of **Impact Proof**?

**Short answer:** Prove impact with synthetic data or metadata rather than escalating unnecessarily.

### Q97. What is the core lesson of **Severity**?

**Short answer:** Severity should reflect realistic impact and exploitability rather than novelty.

### Q98. What is the core lesson of **Duplicate Awareness**?

**Short answer:** Search program guidance and your own reports to reduce duplicate submissions.

### Q99. What is the core lesson of **Report Title**?

**Short answer:** Use a precise vulnerability condition and affected feature in the title.

### Q100. What is the core lesson of **Report Summary**?

**Short answer:** Explain what is wrong and why it matters in one short paragraph.

### Q101. What is the core lesson of **Reproduction Steps**?

**Short answer:** Provide numbered steps using test accounts and reproducible requests.

### Q102. What is the core lesson of **Evidence**?

**Short answer:** Attach screenshots or request/response excerpts while redacting secrets.

### Q103. What is the core lesson of **Impact**?

**Short answer:** Explain confidentiality, integrity, availability, financial, identity, or tenant impact.

### Q104. What is the core lesson of **Remediation Suggestion**?

**Short answer:** Offer root-cause-oriented remediation rather than only blocking one payload.

### Q105. What is the core lesson of **Program Communication**?

**Short answer:** Respond professionally to triage questions and provide clarification without expanding scope.

### Q106. What is the core lesson of **Retest After Fix**?

**Short answer:** Verify the fix using the original safe proof when the program requests retesting.

### Q107. What is the core lesson of **Research Notes**?

**Short answer:** Keep private notes on hypotheses, tested routes, roles, parameters, and results.

### Q108. What is the core lesson of **Automation Boundary**?

**Short answer:** Automate repetitive in-scope discovery or parameter handling conservatively and respect rate limits.

### Q109. What is the core lesson of **Wordlist Discipline**?

**Short answer:** Use narrow context-specific wordlists instead of indiscriminate huge scans.

### Q110. What is the core lesson of **Scanner Noise**?

**Short answer:** Automated scanners can create duplicates and false positives; manual validation remains necessary.

### Q111. What is the core lesson of **WAF Interaction**?

**Short answer:** A WAF can change behavior but does not prove the underlying vulnerability is fixed.

### Q112. What is the core lesson of **False Positive**?

**Short answer:** A strange response is not a vulnerability until the security property is clearly violated.

### Q113. What is the core lesson of **False Negative**?

**Short answer:** Absence of scanner output does not prove the application is secure.

### Q114. What is the core lesson of **Responsible Disclosure**?

**Short answer:** Report privately through the approved channel and avoid public disclosure before coordinated resolution.

### Q115. What is the core lesson of **Bug Hunting Ethics**?

**Short answer:** Respect program terms, privacy, availability, and other users.

### Q116. What is the core lesson of **Bug Hunting Final Mental Model**?

**Short answer:** Read the policy, map the application, form hypotheses, test minimally, prove impact safely, report clearly, and stop.

---

## Completion Checklist

- [ ] I completed the core topics.
- [ ] I completed at least 35 labs.
- [ ] I completed the mini project.
- [ ] I can explain authorization and scope before tooling.
- [ ] I can validate findings with minimal impact.
- [ ] I can document reproducible evidence.
- [ ] I can recommend remediation and retest.
