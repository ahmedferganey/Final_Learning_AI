# 92. Web Application Penetration Testing

> Phase 22 — Penetration Testing

This course is **lab-first, authorization-first, and evidence-driven**. The material is designed for deliberately vulnerable applications, owned devices/emulators, disposable AD domains, or other systems explicitly covered by written authorization.

---

## 1. Topic Title

**Web Application Penetration Testing**

---

## 2. Learning Objectives

- Build an application/API attack-surface and role matrix before testing.
- Use Burp/ZAP/browser tools to inspect and replay requests safely.
- Assess authentication, sessions, JWT/OAuth/SSO, authorization, tenant isolation, and business logic.
- Test common injection and server-side weakness classes with minimal proof.
- Assess file handling, SSRF, cache, CORS, WebSocket, GraphQL, API, and webhook security.
- Test race/idempotency/business-state issues using synthetic data.
- Validate security logging and WAF/API-gateway visibility.
- Write reproducible findings with clear impact and remediation.
- Retest root-cause fixes rather than one blocked payload.
- Operate entirely within authorized application scope.

---

## 3. Prerequisites

Required:

```text
91 Bug Hunting
90 Ethical Hacking and Security Assessment
85 Ethical Hacking Fundamentals
Web Fundamentals
HTTP / HTTPS
REST APIs
JavaScript basics
Databases / SQL basics
Authentication / authorization fundamentals
```

Recommended lab targets:

```text
OWASP Juice Shop
OWASP WebGoat
DVWA
PortSwigger Web Security Academy labs
your own test API
```

---

## 4. Core Concepts Explanation

# Part 1 — Web Application Penetration Testing Purpose

### Core Explanation

Web application penetration testing validates whether application, API, browser, identity, and business-logic weaknesses create meaningful security impact within an authorized scope.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 2 — Authorization

### Core Explanation

Written authorization must cover the application, API, test accounts, data, techniques, and supporting infrastructure involved.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 3 — Scope

### Core Explanation

Scope should identify exact hosts, applications, API versions, environments, accounts, roles, and third-party dependencies.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 4 — Rules of Engagement

### Core Explanation

Rules of engagement define rate limits, prohibited actions, sensitive-data handling, maintenance windows, test accounts, and stop conditions.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 5 — Test Data

### Core Explanation

Use synthetic accounts, objects, payments, files, and identifiers so impact can be demonstrated without touching real users.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 6 — Application Architecture Review

### Core Explanation

Understand the browser/client, reverse proxy, application tier, APIs, data stores, object storage, identity provider, and integrations before testing.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 7 — Trust Boundary

### Core Explanation

Mark every place where untrusted user input, identity, network, or third-party data crosses into a trusted component.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 8 — Route Inventory

### Core Explanation

Build an inventory of application routes, methods, parameters, authentication requirements, and expected roles.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 9 — API Inventory

### Core Explanation

Map REST, GraphQL, WebSocket, webhook, and internal API endpoints relevant to the authorized application.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 10 — Role Matrix

### Core Explanation

Create representative test identities and document exactly which functions and objects each role should access.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 11 — Business Workflow Map

### Core Explanation

Document state transitions such as signup, invite, purchase, approval, refund, password reset, sharing, and deletion.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 12 — HTTP Request

### Core Explanation

Understand method, path, query parameters, headers, cookies, and body as independent security-relevant inputs.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 13 — HTTP Response

### Core Explanation

Review status code, headers, cookies, caching, body content, and error behavior.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 14 — HTTP Methods

### Core Explanation

Assess whether methods such as GET, POST, PUT, PATCH, DELETE, and OPTIONS are required and correctly authorized.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 15 — Content Type

### Core Explanation

Applications should parse only supported content types and reject ambiguous or unexpected representations.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 16 — Host Header

### Core Explanation

Validate trusted host/proxy headers where they influence routing, links, security decisions, or generated URLs.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 17 — Forwarded Headers

### Core Explanation

Only trusted proxies should set client identity and forwarding headers used by the application.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 18 — Security Headers

### Core Explanation

Review HSTS, CSP, frame protections, MIME sniffing controls, referrer policy, and cookie attributes according to context.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 19 — Burp Proxy

### Core Explanation

Use Burp or another intercepting proxy to observe and replay requests in the authorized application.

### Diagram / Code / Command Example

```text
Browser
  ↓
Local interception proxy
  ↓
Authorized lab application

Workflow:
capture → send to repeater → change one variable → compare result
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 20 — Repeater Workflow

### Core Explanation

Send one captured request to a repeater, change one variable at a time, and compare the response.

### Diagram / Code / Command Example

```text
Browser
  ↓
Local interception proxy
  ↓
Authorized lab application

Workflow:
capture → send to repeater → change one variable → compare result
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 21 — Intruder Awareness

### Core Explanation

Automated request variation can help testing but must remain bounded and within program rate limits.

### Diagram / Code / Command Example

```text
Browser
  ↓
Local interception proxy
  ↓
Authorized lab application

Workflow:
capture → send to repeater → change one variable → compare result
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 22 — OWASP ZAP

### Core Explanation

ZAP can provide interception, passive analysis, and controlled automation in lab or authorized applications.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 23 — Browser DevTools

### Core Explanation

Use browser developer tools to inspect network requests, storage, JavaScript, source maps, and runtime behavior.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 24 — Authentication Surface

### Core Explanation

Map registration, login, MFA, password reset, device trust, recovery, session renewal, and logout.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 25 — User Enumeration

### Core Explanation

Check whether differences in responses or timing disclose whether a username/email exists.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 26 — Password Policy

### Core Explanation

Assess minimum password quality, compromised-password screening where applicable, and safe reset flows.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 27 — Rate Limiting for Login

### Core Explanation

Verify that login defenses slow or stop repeated synthetic failures without requiring large credential attacks.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 28 — MFA Coverage

### Core Explanation

Confirm MFA applies consistently to primary login, recovery, sensitive actions, and alternate authentication paths.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 29 — Password Reset Token

### Core Explanation

Reset tokens should be unpredictable, scoped, time-limited, single-use, and invalidated after successful reset.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 30 — Account Recovery

### Core Explanation

Recovery should not become a weaker path that bypasses MFA or identity proofing.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 31 — Session Creation

### Core Explanation

A successful login should create a new authenticated session with appropriate security attributes.

### Diagram / Code / Command Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 32 — Session Fixation

### Core Explanation

Session identifiers should rotate when authentication level changes.

### Diagram / Code / Command Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 33 — Session Expiration

### Core Explanation

Assess idle timeout and absolute lifetime according to risk.

### Diagram / Code / Command Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 34 — Logout

### Core Explanation

Logout should invalidate the relevant session or refresh token state.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 35 — Concurrent Sessions

### Core Explanation

Understand whether simultaneous sessions are allowed and how revocation is handled.

### Diagram / Code / Command Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 36 — Cookie Security

### Core Explanation

Review Secure, HttpOnly, SameSite, Domain, Path, lifetime, and exposure across subdomains.

### Diagram / Code / Command Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 37 — CSRF

### Core Explanation

State-changing browser requests using ambient credentials need anti-CSRF protections appropriate to the architecture.

### Diagram / Code / Command Example

```text
Browser carries ambient credential
      ↓
state-changing request
      ↓
server must require anti-CSRF mechanism
and validate origin/context where appropriate
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 38 — SameSite

### Core Explanation

SameSite cookies reduce some cross-site request risks but do not replace complete CSRF design.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 39 — JWT Structure

### Core Explanation

JWTs contain header, payload, and signature; decoded contents are not proof of authenticity.

### Diagram / Code / Command Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 40 — JWT Signature Validation

### Core Explanation

Servers must verify signatures using trusted algorithms and keys.

### Diagram / Code / Command Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 41 — JWT Issuer and Audience

### Core Explanation

Validate issuer and audience so tokens cannot be replayed across unrelated services.

### Diagram / Code / Command Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 42 — JWT Time Claims

### Core Explanation

Validate expiration and not-before claims with reasonable clock handling.

### Diagram / Code / Command Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 43 — JWT Authorization Claims

### Core Explanation

Roles/scopes in tokens must still be evaluated against current server-side authorization policy.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 44 — Token Storage

### Core Explanation

Avoid exposing bearer tokens in URLs, logs, insecure browser storage, or client-visible error messages.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 45 — Refresh Token

### Core Explanation

Refresh tokens need stronger storage, rotation/reuse detection where applicable, expiry, and revocation.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 46 — Object-Level Authorization

### Core Explanation

Every object request must verify the authenticated subject may access that exact object.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 47 — BOLA / IDOR

### Core Explanation

Changing an identifier should never bypass ownership or tenant authorization.

### Diagram / Code / Command Example

```text
Test user A owns object A
Test user B owns object B

B requests A
   ↓
expected: DENY

Use synthetic objects only.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 48 — Function-Level Authorization

### Core Explanation

Sensitive routes and actions require server-side authorization even if the UI hides them.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 49 — Tenant Isolation

### Core Explanation

Tenant identity must come from trusted authentication context and be enforced consistently in data access.

### Diagram / Code / Command Example

```text
Test user A owns object A
Test user B owns object B

B requests A
   ↓
expected: DENY

Use synthetic objects only.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 50 — Role Escalation

### Core Explanation

Inputs such as role, isAdmin, owner, or tenant should not be client-controlled unless explicitly authorized.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 51 — Mass Assignment

### Core Explanation

Automatic model binding should not allow unexpected modification of security-sensitive fields.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 52 — Horizontal Authorization

### Core Explanation

A user should not access another user's peer-level object without permission.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 53 — Vertical Authorization

### Core Explanation

A lower-privilege role should not invoke administrative or higher-privilege actions.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 54 — Business Logic

### Core Explanation

Test application rules that scanners cannot infer, including limits, approvals, sequence, price, ownership, and state.

### Diagram / Code / Command Example

```text
Expected state machine:

CREATED
  ↓
PAID
  ↓
FULFILLED

Invalid:
FULFILLED → PAID
PAID → PAID (duplicate effect)
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 55 — State Machine

### Core Explanation

Attempt invalid or reordered transitions using synthetic data to verify server-side workflow enforcement.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 56 — Idempotency

### Core Explanation

Repeated requests should not duplicate irreversible operations when the API contract promises idempotency.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 57 — Replay

### Core Explanation

One-time links, coupons, reset operations, payment actions, and approval tokens should resist unauthorized reuse.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 58 — Race Condition

### Core Explanation

Concurrent requests can break otherwise valid sequential checks and should be tested conservatively.

### Diagram / Code / Command Example

```text
Request A ─┐
           ├─ concurrently hit same state
Request B ─┘
      ↓
atomic business invariant?
      ↓
one valid outcome
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 59 — Quantity and Price Validation

### Core Explanation

Server-side business rules must validate quantity, amount, discount, currency, and account eligibility.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 60 — SQL Injection

### Core Explanation

SQL injection occurs when untrusted input changes SQL structure because code and data are mixed.

### Diagram / Code / Command Example

```python
# Vulnerable concept
query = "SELECT * FROM users WHERE email = '" + user_input + "'"

# Safer
cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (user_input,)
)
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 61 — Parameterized Queries

### Core Explanation

Parameterized statements keep SQL syntax separate from untrusted values.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 62 — NoSQL Injection Awareness

### Core Explanation

Document/query APIs can be vulnerable when attacker-controlled operators or expressions are accepted.

### Diagram / Code / Command Example

```python
# Vulnerable concept
query = "SELECT * FROM users WHERE email = '" + user_input + "'"

# Safer
cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (user_input,)
)
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 63 — Cross-Site Scripting

### Core Explanation

XSS occurs when untrusted data reaches an executable browser context without correct encoding or safe DOM handling.

### Diagram / Code / Command Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 64 — Reflected XSS

### Core Explanation

Reflected XSS immediately returns untrusted request data into a browser execution context.

### Diagram / Code / Command Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 65 — Stored XSS

### Core Explanation

Stored XSS persists untrusted content that later executes when another user views it.

### Diagram / Code / Command Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 66 — DOM XSS

### Core Explanation

DOM XSS occurs when client-side code moves untrusted data into dangerous browser sinks.

### Diagram / Code / Command Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 67 — Output Encoding

### Core Explanation

Encode according to HTML, attribute, JavaScript, CSS, URL, or other output context.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 68 — Content Security Policy

### Core Explanation

CSP can reduce exploitability and provide telemetry but does not fix unsafe application code.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 69 — Command Injection

### Core Explanation

Command injection occurs when untrusted input changes operating-system command syntax.

### Diagram / Code / Command Example

```python
import subprocess

# Prefer fixed executable + argument list.
subprocess.run(
    ["ping", "-c", "1", "127.0.0.1"],
    shell=False,
    check=False
)
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 70 — Shell Avoidance

### Core Explanation

Use direct process APIs and fixed argument arrays rather than concatenating user input into a shell command.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 71 — Path Traversal

### Core Explanation

Path traversal escapes an intended storage directory through untrusted path manipulation.

### Diagram / Code / Command Example

```python
from pathlib import Path

root = Path("/srv/app/files").resolve()
candidate = (root / user_supplied_name).resolve()

if candidate != root and root not in candidate.parents:
    raise ValueError("path escaped allowed directory")
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 72 — Canonical Path Validation

### Core Explanation

Resolve and compare canonical paths against an allowed root.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 73 — Local File Inclusion Awareness

### Core Explanation

Unsafe path handling may expose local application/server files depending on the framework.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 74 — Remote File Inclusion Awareness

### Core Explanation

Some legacy/framework designs can load remote content as executable/include material and should be disabled.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 75 — File Upload

### Core Explanation

Validate authorization, size, content, type, storage location, processing, scanning, and download permissions.

### Diagram / Code / Command Example

```text
Upload
  ↓
authorization
  ↓
size / type / content validation
  ↓
store outside executable web root
  ↓
generated object name
  ↓
scan / process safely
  ↓
authorized download
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 76 — Upload Execution Risk

### Core Explanation

Uploaded content should not become directly executable merely because it was stored on the server.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 77 — MIME Validation

### Core Explanation

Do not trust only filename extension or client-provided MIME type.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 78 — Archive Upload Risk

### Core Explanation

Archive extraction can introduce path traversal, excessive expansion, or nested-content risks.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 79 — Image / Document Processing Risk

### Core Explanation

Parsers and converters expand attack surface and should be patched, sandboxed, and resource-bounded.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 80 — SSRF

### Core Explanation

Server-side request forgery lets untrusted input influence outbound requests to unintended destinations.

### Diagram / Code / Command Example

```text
User URL
  ↓
application fetcher
  ↓
destination validation
  ↓
DNS/IP resolution
  ↓
approved public destination

Deny:
loopback
private/internal ranges unless required
metadata endpoints
unsafe redirect chains
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 81 — SSRF Destination Validation

### Core Explanation

Validate scheme, host, resolved IP, redirects, and destination class before making outbound requests.

### Diagram / Code / Command Example

```text
User URL
  ↓
application fetcher
  ↓
destination validation
  ↓
DNS/IP resolution
  ↓
approved public destination

Deny:
loopback
private/internal ranges unless required
metadata endpoints
unsafe redirect chains
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 82 — Cloud Metadata Protection

### Core Explanation

Applications should prevent untrusted request flows from reaching cloud metadata or credential services.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 83 — Open Redirect

### Core Explanation

Unvalidated redirects can support phishing or token leakage in some authentication flows.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 84 — XXE

### Core Explanation

Unsafe XML external entity processing can expose local files or make outbound requests.

### Diagram / Code / Command Example

```text
Secure parser posture:
external entities disabled
network access disabled unless required
DTD handling minimized
input size bounded
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 85 — XML Parser Hardening

### Core Explanation

Disable unneeded external entities, DTDs, and network resolution.

### Diagram / Code / Command Example

```text
Secure parser posture:
external entities disabled
network access disabled unless required
DTD handling minimized
input size bounded
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 86 — Server-Side Template Injection

### Core Explanation

Template injection occurs when user input becomes template code rather than template data.

### Diagram / Code / Command Example

```text
User data
  ↓
template variable
  ↓
escaped rendering

Never treat untrusted text as template code.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 87 — Template Data Separation

### Core Explanation

Treat untrusted content as variables, not executable template instructions.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 88 — Insecure Deserialization

### Core Explanation

Unsafe object deserialization can instantiate attacker-influenced types or invoke dangerous behaviors.

### Diagram / Code / Command Example

```text
Untrusted data
  ↓
safe schema / primitive data types
  ↓
validated object construction

Avoid interpreting attacker-controlled serialized object graphs
with executable types.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 89 — Safe Serialization

### Core Explanation

Prefer simple data formats and explicit schemas over arbitrary object graphs.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 90 — Request Smuggling Awareness

### Core Explanation

HTTP parser disagreements between front-end and back-end components can desynchronize request boundaries.

### Diagram / Code / Command Example

```text
Front-end HTTP parser
        ↓
same request boundary?
        ↓
Back-end HTTP parser

Parser disagreement can desynchronize connections.
Test only in dedicated labs / explicit scope.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 91 — Request Smuggling Safety

### Core Explanation

Test request-smuggling behavior only in dedicated labs or explicit programs because shared connections can affect other users.

### Diagram / Code / Command Example

```text
Front-end HTTP parser
        ↓
same request boundary?
        ↓
Back-end HTTP parser

Parser disagreement can desynchronize connections.
Test only in dedicated labs / explicit scope.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 92 — HTTP Response Splitting Awareness

### Core Explanation

Unvalidated header values can corrupt response structure in vulnerable frameworks.

### Diagram / Code / Command Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 93 — Cache Poisoning

### Core Explanation

If a cache key omits security-relevant request inputs, attacker-controlled content may be served to other users.

### Diagram / Code / Command Example

```text
Request
  ↓
cache key
  ↓
cached representation
  ↓
future users

Security question:
Does the cache key include every input
that changes security-sensitive output?
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 94 — Cache Deception Awareness

### Core Explanation

Improper caching of authenticated/private responses can expose sensitive content.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 95 — CORS

### Core Explanation

CORS controls browser cross-origin response access, not server-side authorization.

### Diagram / Code / Command Example

```text
CORS decides:
Which browser origins may read a response?

It does NOT decide:
Whether the authenticated user is authorized
to access the underlying object.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 96 — CORS Credentials

### Core Explanation

Credentialed cross-origin access requires exact trusted origins rather than wildcard reflection.

### Diagram / Code / Command Example

```text
CORS decides:
Which browser origins may read a response?

It does NOT decide:
Whether the authenticated user is authorized
to access the underlying object.
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 97 — Clickjacking

### Core Explanation

Sensitive user actions should be protected from untrusted framing when UI redress would create impact.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 98 — WebSocket Authentication

### Core Explanation

Authenticate the WebSocket upgrade and bind the connection to the correct user.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 99 — WebSocket Authorization

### Core Explanation

Authorize each message/action, not only the initial connection.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 100 — GraphQL Introspection

### Core Explanation

Schema visibility can aid testing but does not itself create authorization failure.

### Diagram / Code / Command Example

```graphql
query {
  profile {
    id
    displayName
  }
}
```

Review:
resolver authorization
query depth/cost
field-level exposure
introspection policy
error leakage
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 101 — GraphQL Resolver Authorization

### Core Explanation

Each resolver must enforce the same object and role rules expected in REST or other interfaces.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 102 — GraphQL Query Cost

### Core Explanation

Bound depth, complexity, batch size, and expensive resolver fan-out.

### Diagram / Code / Command Example

```graphql
query {
  profile {
    id
    displayName
  }
}
```

Review:
resolver authorization
query depth/cost
field-level exposure
introspection policy
error leakage
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 103 — REST API Authorization

### Core Explanation

REST resources must enforce object and function authorization independent of client UI.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 104 — API Schema Validation

### Core Explanation

Reject malformed, oversized, unexpected, or unknown fields according to the API contract.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 105 — API Error Handling

### Core Explanation

Avoid returning stack traces, SQL, internal hostnames, or secret values.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 106 — API Rate Limiting

### Core Explanation

Protect expensive or sensitive endpoints using identity- and cost-aware limits.

### Diagram / Code / Command Example

```text
Identity / client
  ↓
cost-aware rate / concurrency limit
  ↓
bounded queue / worker capacity
  ↓
dependency protection
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 107 — API Pagination

### Core Explanation

Bound page size and prevent filters/sorts from becoming unbounded expensive operations.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 108 — API Idempotency

### Core Explanation

Use scoped idempotency keys for operations where duplicate side effects would be harmful.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 109 — OAuth Redirect URI

### Core Explanation

Redirect URIs should be exact or tightly constrained to approved destinations.

### Diagram / Code / Command Example

```text
Client
  ↓ authorization request
Identity Provider
  ↓ authorization code
Client
  ↓ token exchange + PKCE
Token
  ↓
Resource Server

Check:
redirect URI, state, PKCE, issuer, audience, scope
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 110 — OAuth State

### Core Explanation

State protects the authorization response from cross-site request confusion.

### Diagram / Code / Command Example

```text
Client
  ↓ authorization request
Identity Provider
  ↓ authorization code
Client
  ↓ token exchange + PKCE
Token
  ↓
Resource Server

Check:
redirect URI, state, PKCE, issuer, audience, scope
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 111 — PKCE

### Core Explanation

PKCE binds an authorization-code exchange to the initiating client and is important for public clients.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 112 — OAuth Scope

### Core Explanation

Tokens should receive only the scopes required by the application.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 113 — OIDC Nonce Awareness

### Core Explanation

Nonce helps bind an ID token to an authentication request in appropriate OIDC flows.

### Diagram / Code / Command Example

```text
Client
  ↓ authorization request
Identity Provider
  ↓ authorization code
Client
  ↓ token exchange + PKCE
Token
  ↓
Resource Server

Check:
redirect URI, state, PKCE, issuer, audience, scope
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 114 — SAML Assertion Validation

### Core Explanation

Validate signature, issuer, audience, recipient, time, and replay requirements.

### Diagram / Code / Command Example

```text
Service Provider
   ↓ Authn request
Identity Provider
   ↓ signed assertion
Service Provider validates:
issuer + audience + signature + time + recipient
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 115 — Account Linking

### Core Explanation

SSO/OAuth account-linking workflows must verify both identities before merging accounts.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 116 — Webhook Authentication

### Core Explanation

Verify webhook authenticity with signatures, shared secrets, mTLS, or provider-specific mechanisms.

### Diagram / Code / Command Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 117 — Webhook Replay Protection

### Core Explanation

Use timestamps/nonces/idempotency to prevent repeated valid webhook delivery from creating duplicate effects.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 118 — Signed URL

### Core Explanation

Signed URLs should be short-lived, object-scoped, method-scoped, and created only after authorization.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 119 — Object Storage Authorization

### Core Explanation

Bucket/container/object policy must not expose private files beyond intended users.

### Diagram / Code / Command Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 120 — Information Disclosure

### Core Explanation

Stack traces, source maps, debug endpoints, backups, logs, and headers can reveal sensitive internals.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 121 — Debug Mode

### Core Explanation

Production debug features should be disabled or strongly restricted.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 122 — Dependency Vulnerability

### Core Explanation

Validate whether the vulnerable component and affected execution path actually exist before reporting.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 123 — SCA Correlation

### Core Explanation

Use software-composition results together with runtime reachability and vendor guidance.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 124 — Security Logging

### Core Explanation

Critical authentication, authorization, admin, and suspicious application events should be logged without secrets.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 125 — Detection Validation

### Core Explanation

Confirm whether test requests are visible in WAF, application, API gateway, identity, and SIEM telemetry.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 126 — Evidence

### Core Explanation

Preserve exact requests/responses, test roles, timestamps, and minimal sensitive content.

### Diagram / Code / Command Example

```text
Finding:
Title
Affected route
Test role/account
Request
Response
Security property violated
Impact
Remediation
Retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 127 — Finding Report

### Core Explanation

Write reproducible findings tied to the violated security property and business impact.

### Diagram / Code / Command Example

```text
Finding:
Title
Affected route
Test role/account
Request
Response
Security property violated
Impact
Remediation
Retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 128 — Retest

### Core Explanation

Repeat the original safe request after remediation.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

# Part 129 — Web Application Penetration Testing Final Mental Model

### Core Explanation

Map the application, understand roles and data flows, test one security property at a time, prove impact minimally, and retest the root-cause fix.

### Diagram / Code / Command Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Why It Matters

This topic changes how a real attacker could cross an application, device, identity, or trust boundary. The goal is to **understand and validate the security property with the least intrusive authorized method**.

### Practical Use

Use deliberately vulnerable applications, owned devices/emulators, isolated test domains, synthetic data, or systems explicitly covered by written authorization.

### Common Problems

- Testing beyond the defined target or program scope.
- Treating a client-side restriction as a server-side authorization control.
- Collecting real sensitive data after minimal proof is already available.
- Running high-rate automation without understanding side effects.
- Assuming tool output proves exploitability.
- Failing to document test account/role, exact request, host, app version, or directory object.
- Leaving test accounts, sessions, tokens, app artifacts, or domain changes behind.

### Best Practice

Map the trust boundary first, define expected behavior, test one hypothesis at a time, preserve evidence, stop after proof, remediate the root cause, and retest.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Web Application Penetration Testing Purpose

### Objective

Practice **Web Application Penetration Testing Purpose** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 2 — Authorization

### Objective

Practice **Authorization** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 3 — Scope

### Objective

Practice **Scope** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 4 — Rules of Engagement

### Objective

Practice **Rules of Engagement** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 5 — Test Data

### Objective

Practice **Test Data** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 6 — Application Architecture Review

### Objective

Practice **Application Architecture Review** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 7 — Trust Boundary

### Objective

Practice **Trust Boundary** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 8 — Route Inventory

### Objective

Practice **Route Inventory** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 9 — API Inventory

### Objective

Practice **API Inventory** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 10 — Role Matrix

### Objective

Practice **Role Matrix** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 11 — Business Workflow Map

### Objective

Practice **Business Workflow Map** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 12 — HTTP Request

### Objective

Practice **HTTP Request** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 13 — HTTP Response

### Objective

Practice **HTTP Response** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 14 — HTTP Methods

### Objective

Practice **HTTP Methods** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 15 — Content Type

### Objective

Practice **Content Type** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 16 — Host Header

### Objective

Practice **Host Header** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 17 — Forwarded Headers

### Objective

Practice **Forwarded Headers** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 18 — Security Headers

### Objective

Practice **Security Headers** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```http
GET /api/profile HTTP/1.1
Host: lab.example
Authorization: Bearer <TEST_TOKEN>
Accept: application/json
```

```text
Method + path + headers + cookies + body
      ↓
routing
      ↓
authentication
      ↓
authorization
      ↓
business logic
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 19 — Burp Proxy

### Objective

Practice **Burp Proxy** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Browser
  ↓
Local interception proxy
  ↓
Authorized lab application

Workflow:
capture → send to repeater → change one variable → compare result
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 20 — Repeater Workflow

### Objective

Practice **Repeater Workflow** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Browser
  ↓
Local interception proxy
  ↓
Authorized lab application

Workflow:
capture → send to repeater → change one variable → compare result
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 21 — Intruder Awareness

### Objective

Practice **Intruder Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Browser
  ↓
Local interception proxy
  ↓
Authorized lab application

Workflow:
capture → send to repeater → change one variable → compare result
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 22 — OWASP ZAP

### Objective

Practice **OWASP ZAP** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 23 — Browser DevTools

### Objective

Practice **Browser DevTools** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 24 — Authentication Surface

### Objective

Practice **Authentication Surface** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 25 — User Enumeration

### Objective

Practice **User Enumeration** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 26 — Password Policy

### Objective

Practice **Password Policy** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 27 — Rate Limiting for Login

### Objective

Practice **Rate Limiting for Login** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 28 — MFA Coverage

### Objective

Practice **MFA Coverage** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 29 — Password Reset Token

### Objective

Practice **Password Reset Token** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 30 — Account Recovery

### Objective

Practice **Account Recovery** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Authentication review:
enrollment
  ↓
login
  ↓
MFA
  ↓
session issuance
  ↓
recovery/reset
  ↓
logout/revocation
  ↓
audit
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 31 — Session Creation

### Objective

Practice **Session Creation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 32 — Session Fixation

### Objective

Practice **Session Fixation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 33 — Session Expiration

### Objective

Practice **Session Expiration** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 34 — Logout

### Objective

Practice **Logout** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 35 — Concurrent Sessions

### Objective

Practice **Concurrent Sessions** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 36 — Cookie Security

### Objective

Practice **Cookie Security** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Session:
issue
  ↓
Secure / HttpOnly / SameSite
  ↓
rotation after authentication
  ↓
idle / absolute expiration
  ↓
logout / revocation
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 37 — CSRF

### Objective

Practice **CSRF** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Browser carries ambient credential
      ↓
state-changing request
      ↓
server must require anti-CSRF mechanism
and validate origin/context where appropriate
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 38 — SameSite

### Objective

Practice **SameSite** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 39 — JWT Structure

### Objective

Practice **JWT Structure** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 40 — JWT Signature Validation

### Objective

Practice **JWT Signature Validation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 41 — JWT Issuer and Audience

### Objective

Practice **JWT Issuer and Audience** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 42 — JWT Time Claims

### Objective

Practice **JWT Time Claims** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
JWT validation:
signature
issuer
audience
expiration
not-before
required claims
scope / role

Base64 decoding ≠ signature verification.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 43 — JWT Authorization Claims

### Objective

Practice **JWT Authorization Claims** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 44 — Token Storage

### Objective

Practice **Token Storage** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 45 — Refresh Token

### Objective

Practice **Refresh Token** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 46 — Object-Level Authorization

### Objective

Practice **Object-Level Authorization** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 47 — BOLA / IDOR

### Objective

Practice **BOLA / IDOR** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Test user A owns object A
Test user B owns object B

B requests A
   ↓
expected: DENY

Use synthetic objects only.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 48 — Function-Level Authorization

### Objective

Practice **Function-Level Authorization** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 49 — Tenant Isolation

### Objective

Practice **Tenant Isolation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Test user A owns object A
Test user B owns object B

B requests A
   ↓
expected: DENY

Use synthetic objects only.
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 50 — Role Escalation

### Objective

Practice **Role Escalation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 51 — Mass Assignment

### Objective

Practice **Mass Assignment** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 52 — Horizontal Authorization

### Objective

Practice **Horizontal Authorization** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 53 — Vertical Authorization

### Objective

Practice **Vertical Authorization** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Written authorization
      ↓
In-scope application / API
      ↓
Allowed accounts / roles
      ↓
Permitted techniques
      ↓
Rate limits / maintenance window
      ↓
Sensitive-data handling
      ↓
Stop conditions
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 54 — Business Logic

### Objective

Practice **Business Logic** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Expected state machine:

CREATED
  ↓
PAID
  ↓
FULFILLED

Invalid:
FULFILLED → PAID
PAID → PAID (duplicate effect)
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 55 — State Machine

### Objective

Practice **State Machine** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 56 — Idempotency

### Objective

Practice **Idempotency** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 57 — Replay

### Objective

Practice **Replay** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 58 — Race Condition

### Objective

Practice **Race Condition** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Request A ─┐
           ├─ concurrently hit same state
Request B ─┘
      ↓
atomic business invariant?
      ↓
one valid outcome
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 59 — Quantity and Price Validation

### Objective

Practice **Quantity and Price Validation** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 60 — SQL Injection

### Objective

Practice **SQL Injection** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```python
# Vulnerable concept
query = "SELECT * FROM users WHERE email = '" + user_input + "'"

# Safer
cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (user_input,)
)
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 61 — Parameterized Queries

### Objective

Practice **Parameterized Queries** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 62 — NoSQL Injection Awareness

### Objective

Practice **NoSQL Injection Awareness** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```python
# Vulnerable concept
query = "SELECT * FROM users WHERE email = '" + user_input + "'"

# Safer
cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (user_input,)
)
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 63 — Cross-Site Scripting

### Objective

Practice **Cross-Site Scripting** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 64 — Reflected XSS

### Objective

Practice **Reflected XSS** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 65 — Stored XSS

### Objective

Practice **Stored XSS** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 66 — DOM XSS

### Objective

Practice **DOM XSS** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```html
<!-- Risky concept -->
<div id="out"></div>
<script>
  // out.innerHTML = untrustedValue;

  // safer for plain text
  out.textContent = untrustedValue;
</script>
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 67 — Output Encoding

### Objective

Practice **Output Encoding** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 68 — Content Security Policy

### Objective

Practice **Content Security Policy** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 69 — Command Injection

### Objective

Practice **Command Injection** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```python
import subprocess

# Prefer fixed executable + argument list.
subprocess.run(
    ["ping", "-c", "1", "127.0.0.1"],
    shell=False,
    check=False
)
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## Lab 70 — Shell Avoidance

### Objective

Practice **Shell Avoidance** in a controlled lab.

### Safety Boundary

Use only an intentionally vulnerable web/mobile application, your own emulator/device, your own AD lab, synthetic users/data, or another explicitly authorized environment.

### Procedure

1. Record authorization and scope.
2. Record the exact target/component.
3. State the expected secure behavior.
4. Capture baseline evidence.
5. Perform the minimum safe test.
6. Stop after sufficient proof.
7. Save evidence.
8. Explain impact.
9. Apply or document remediation.
10. Remove test artifacts.
11. Retest.

### Starter Example

```text
Policy / Scope
   ↓
Map route / role / data flow
   ↓
Form hypothesis
   ↓
Minimal request
   ↓
Compare expected vs observed
   ↓
Evidence
   ↓
Remediation / retest
```

### Evidence Template

```text
Lab:
Target / component:
Test account / role:
Expected:
Observed:
Request / command / action:
Evidence:
Impact:
Remediation:
Cleanup:
Retest:
```

---

## 6. Mini Project

# Mini Project — Web Application Penetration Test

Use an intentionally vulnerable web application with two or more synthetic roles. Build a route/API inventory and role matrix, then validate at least ten distinct security findings across authentication, authorization, business logic, injection, browser security, file handling, and API controls. For each finding, preserve the exact request/response, explain the violated security property, remediate at least five findings, and retest.

### Required Deliverables

1. Authorization / lab scope
2. Architecture or trust-boundary diagram
3. Asset / component inventory
4. Test accounts / roles
5. Test plan
6. Evidence repository
7. Validated findings
8. Impact and attack-path explanation
9. Remediation plan
10. Detection / logging observations
11. Cleanup checklist
12. Retest evidence
13. Executive / triage-ready summary
14. Technical appendix

---

## 7. Recommended Resources

- OWASP Web Security Testing Guide — https://owasp.org/www-project-web-security-testing-guide/
- OWASP ASVS — https://owasp.org/www-project-application-security-verification-standard/
- OWASP Top 10 — https://owasp.org/www-project-top-ten/
- PortSwigger Web Security Academy — https://portswigger.net/web-security
- OWASP Juice Shop — https://owasp.org/www-project-juice-shop/

---

## 8. Certification Relevance

Strong preparation for application-security analyst, web penetration-testing, bug-bounty, PenTest+-style, eJPT/eWPT-style, and secure-development roles.

Certification objectives and platform versions change over time. Verify current official exam and platform documentation when preparing for certification or production work.

---

## 9. Common Mistakes & Best Practices

### Common Mistakes

- Testing beyond written scope.
- Using real sensitive data when synthetic proof is sufficient.
- Trusting the mobile/web client as an authorization boundary.
- Treating scanner/decompiler/graph output as a confirmed exploit path.
- Running high-impact techniques before validating preconditions.
- Continuing after enough evidence has already been collected.
- Failing to record app/OS/domain versions and test-account context.
- Leaving test accounts, ACL changes, tokens, sessions, instrumentation, or lab artifacts behind.

### Best Practices

- Map trust boundaries before tools.
- Change one variable at a time.
- Prefer low-impact evidence before exploitation.
- Use synthetic identities and data.
- Use disposable lab snapshots.
- Preserve exact requests, commands, object IDs, and timestamps.
- Correlate tests with defensive telemetry.
- Fix the root cause.
- Retest with the original safe proof.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the key lesson from **Web Application Penetration Testing Purpose**?

**Short answer:** Web application penetration testing validates whether application, API, browser, identity, and business-logic weaknesses create meaningful security impact within an authorized scope.

### Q2. What is the key lesson from **Authorization**?

**Short answer:** Written authorization must cover the application, API, test accounts, data, techniques, and supporting infrastructure involved.

### Q3. What is the key lesson from **Scope**?

**Short answer:** Scope should identify exact hosts, applications, API versions, environments, accounts, roles, and third-party dependencies.

### Q4. What is the key lesson from **Rules of Engagement**?

**Short answer:** Rules of engagement define rate limits, prohibited actions, sensitive-data handling, maintenance windows, test accounts, and stop conditions.

### Q5. What is the key lesson from **Test Data**?

**Short answer:** Use synthetic accounts, objects, payments, files, and identifiers so impact can be demonstrated without touching real users.

### Q6. What is the key lesson from **Application Architecture Review**?

**Short answer:** Understand the browser/client, reverse proxy, application tier, APIs, data stores, object storage, identity provider, and integrations before testing.

### Q7. What is the key lesson from **Trust Boundary**?

**Short answer:** Mark every place where untrusted user input, identity, network, or third-party data crosses into a trusted component.

### Q8. What is the key lesson from **Route Inventory**?

**Short answer:** Build an inventory of application routes, methods, parameters, authentication requirements, and expected roles.

### Q9. What is the key lesson from **API Inventory**?

**Short answer:** Map REST, GraphQL, WebSocket, webhook, and internal API endpoints relevant to the authorized application.

### Q10. What is the key lesson from **Role Matrix**?

**Short answer:** Create representative test identities and document exactly which functions and objects each role should access.

### Q11. What is the key lesson from **Business Workflow Map**?

**Short answer:** Document state transitions such as signup, invite, purchase, approval, refund, password reset, sharing, and deletion.

### Q12. What is the key lesson from **HTTP Request**?

**Short answer:** Understand method, path, query parameters, headers, cookies, and body as independent security-relevant inputs.

### Q13. What is the key lesson from **HTTP Response**?

**Short answer:** Review status code, headers, cookies, caching, body content, and error behavior.

### Q14. What is the key lesson from **HTTP Methods**?

**Short answer:** Assess whether methods such as GET, POST, PUT, PATCH, DELETE, and OPTIONS are required and correctly authorized.

### Q15. What is the key lesson from **Content Type**?

**Short answer:** Applications should parse only supported content types and reject ambiguous or unexpected representations.

### Q16. What is the key lesson from **Host Header**?

**Short answer:** Validate trusted host/proxy headers where they influence routing, links, security decisions, or generated URLs.

### Q17. What is the key lesson from **Forwarded Headers**?

**Short answer:** Only trusted proxies should set client identity and forwarding headers used by the application.

### Q18. What is the key lesson from **Security Headers**?

**Short answer:** Review HSTS, CSP, frame protections, MIME sniffing controls, referrer policy, and cookie attributes according to context.

### Q19. What is the key lesson from **Burp Proxy**?

**Short answer:** Use Burp or another intercepting proxy to observe and replay requests in the authorized application.

### Q20. What is the key lesson from **Repeater Workflow**?

**Short answer:** Send one captured request to a repeater, change one variable at a time, and compare the response.

### Q21. What is the key lesson from **Intruder Awareness**?

**Short answer:** Automated request variation can help testing but must remain bounded and within program rate limits.

### Q22. What is the key lesson from **OWASP ZAP**?

**Short answer:** ZAP can provide interception, passive analysis, and controlled automation in lab or authorized applications.

### Q23. What is the key lesson from **Browser DevTools**?

**Short answer:** Use browser developer tools to inspect network requests, storage, JavaScript, source maps, and runtime behavior.

### Q24. What is the key lesson from **Authentication Surface**?

**Short answer:** Map registration, login, MFA, password reset, device trust, recovery, session renewal, and logout.

### Q25. What is the key lesson from **User Enumeration**?

**Short answer:** Check whether differences in responses or timing disclose whether a username/email exists.

### Q26. What is the key lesson from **Password Policy**?

**Short answer:** Assess minimum password quality, compromised-password screening where applicable, and safe reset flows.

### Q27. What is the key lesson from **Rate Limiting for Login**?

**Short answer:** Verify that login defenses slow or stop repeated synthetic failures without requiring large credential attacks.

### Q28. What is the key lesson from **MFA Coverage**?

**Short answer:** Confirm MFA applies consistently to primary login, recovery, sensitive actions, and alternate authentication paths.

### Q29. What is the key lesson from **Password Reset Token**?

**Short answer:** Reset tokens should be unpredictable, scoped, time-limited, single-use, and invalidated after successful reset.

### Q30. What is the key lesson from **Account Recovery**?

**Short answer:** Recovery should not become a weaker path that bypasses MFA or identity proofing.

### Q31. What is the key lesson from **Session Creation**?

**Short answer:** A successful login should create a new authenticated session with appropriate security attributes.

### Q32. What is the key lesson from **Session Fixation**?

**Short answer:** Session identifiers should rotate when authentication level changes.

### Q33. What is the key lesson from **Session Expiration**?

**Short answer:** Assess idle timeout and absolute lifetime according to risk.

### Q34. What is the key lesson from **Logout**?

**Short answer:** Logout should invalidate the relevant session or refresh token state.

### Q35. What is the key lesson from **Concurrent Sessions**?

**Short answer:** Understand whether simultaneous sessions are allowed and how revocation is handled.

### Q36. What is the key lesson from **Cookie Security**?

**Short answer:** Review Secure, HttpOnly, SameSite, Domain, Path, lifetime, and exposure across subdomains.

### Q37. What is the key lesson from **CSRF**?

**Short answer:** State-changing browser requests using ambient credentials need anti-CSRF protections appropriate to the architecture.

### Q38. What is the key lesson from **SameSite**?

**Short answer:** SameSite cookies reduce some cross-site request risks but do not replace complete CSRF design.

### Q39. What is the key lesson from **JWT Structure**?

**Short answer:** JWTs contain header, payload, and signature; decoded contents are not proof of authenticity.

### Q40. What is the key lesson from **JWT Signature Validation**?

**Short answer:** Servers must verify signatures using trusted algorithms and keys.

### Q41. What is the key lesson from **JWT Issuer and Audience**?

**Short answer:** Validate issuer and audience so tokens cannot be replayed across unrelated services.

### Q42. What is the key lesson from **JWT Time Claims**?

**Short answer:** Validate expiration and not-before claims with reasonable clock handling.

### Q43. What is the key lesson from **JWT Authorization Claims**?

**Short answer:** Roles/scopes in tokens must still be evaluated against current server-side authorization policy.

### Q44. What is the key lesson from **Token Storage**?

**Short answer:** Avoid exposing bearer tokens in URLs, logs, insecure browser storage, or client-visible error messages.

### Q45. What is the key lesson from **Refresh Token**?

**Short answer:** Refresh tokens need stronger storage, rotation/reuse detection where applicable, expiry, and revocation.

### Q46. What is the key lesson from **Object-Level Authorization**?

**Short answer:** Every object request must verify the authenticated subject may access that exact object.

### Q47. What is the key lesson from **BOLA / IDOR**?

**Short answer:** Changing an identifier should never bypass ownership or tenant authorization.

### Q48. What is the key lesson from **Function-Level Authorization**?

**Short answer:** Sensitive routes and actions require server-side authorization even if the UI hides them.

### Q49. What is the key lesson from **Tenant Isolation**?

**Short answer:** Tenant identity must come from trusted authentication context and be enforced consistently in data access.

### Q50. What is the key lesson from **Role Escalation**?

**Short answer:** Inputs such as role, isAdmin, owner, or tenant should not be client-controlled unless explicitly authorized.

### Q51. What is the key lesson from **Mass Assignment**?

**Short answer:** Automatic model binding should not allow unexpected modification of security-sensitive fields.

### Q52. What is the key lesson from **Horizontal Authorization**?

**Short answer:** A user should not access another user's peer-level object without permission.

### Q53. What is the key lesson from **Vertical Authorization**?

**Short answer:** A lower-privilege role should not invoke administrative or higher-privilege actions.

### Q54. What is the key lesson from **Business Logic**?

**Short answer:** Test application rules that scanners cannot infer, including limits, approvals, sequence, price, ownership, and state.

### Q55. What is the key lesson from **State Machine**?

**Short answer:** Attempt invalid or reordered transitions using synthetic data to verify server-side workflow enforcement.

### Q56. What is the key lesson from **Idempotency**?

**Short answer:** Repeated requests should not duplicate irreversible operations when the API contract promises idempotency.

### Q57. What is the key lesson from **Replay**?

**Short answer:** One-time links, coupons, reset operations, payment actions, and approval tokens should resist unauthorized reuse.

### Q58. What is the key lesson from **Race Condition**?

**Short answer:** Concurrent requests can break otherwise valid sequential checks and should be tested conservatively.

### Q59. What is the key lesson from **Quantity and Price Validation**?

**Short answer:** Server-side business rules must validate quantity, amount, discount, currency, and account eligibility.

### Q60. What is the key lesson from **SQL Injection**?

**Short answer:** SQL injection occurs when untrusted input changes SQL structure because code and data are mixed.

### Q61. What is the key lesson from **Parameterized Queries**?

**Short answer:** Parameterized statements keep SQL syntax separate from untrusted values.

### Q62. What is the key lesson from **NoSQL Injection Awareness**?

**Short answer:** Document/query APIs can be vulnerable when attacker-controlled operators or expressions are accepted.

### Q63. What is the key lesson from **Cross-Site Scripting**?

**Short answer:** XSS occurs when untrusted data reaches an executable browser context without correct encoding or safe DOM handling.

### Q64. What is the key lesson from **Reflected XSS**?

**Short answer:** Reflected XSS immediately returns untrusted request data into a browser execution context.

### Q65. What is the key lesson from **Stored XSS**?

**Short answer:** Stored XSS persists untrusted content that later executes when another user views it.

### Q66. What is the key lesson from **DOM XSS**?

**Short answer:** DOM XSS occurs when client-side code moves untrusted data into dangerous browser sinks.

### Q67. What is the key lesson from **Output Encoding**?

**Short answer:** Encode according to HTML, attribute, JavaScript, CSS, URL, or other output context.

### Q68. What is the key lesson from **Content Security Policy**?

**Short answer:** CSP can reduce exploitability and provide telemetry but does not fix unsafe application code.

### Q69. What is the key lesson from **Command Injection**?

**Short answer:** Command injection occurs when untrusted input changes operating-system command syntax.

### Q70. What is the key lesson from **Shell Avoidance**?

**Short answer:** Use direct process APIs and fixed argument arrays rather than concatenating user input into a shell command.

### Q71. What is the key lesson from **Path Traversal**?

**Short answer:** Path traversal escapes an intended storage directory through untrusted path manipulation.

### Q72. What is the key lesson from **Canonical Path Validation**?

**Short answer:** Resolve and compare canonical paths against an allowed root.

### Q73. What is the key lesson from **Local File Inclusion Awareness**?

**Short answer:** Unsafe path handling may expose local application/server files depending on the framework.

### Q74. What is the key lesson from **Remote File Inclusion Awareness**?

**Short answer:** Some legacy/framework designs can load remote content as executable/include material and should be disabled.

### Q75. What is the key lesson from **File Upload**?

**Short answer:** Validate authorization, size, content, type, storage location, processing, scanning, and download permissions.

### Q76. What is the key lesson from **Upload Execution Risk**?

**Short answer:** Uploaded content should not become directly executable merely because it was stored on the server.

### Q77. What is the key lesson from **MIME Validation**?

**Short answer:** Do not trust only filename extension or client-provided MIME type.

### Q78. What is the key lesson from **Archive Upload Risk**?

**Short answer:** Archive extraction can introduce path traversal, excessive expansion, or nested-content risks.

### Q79. What is the key lesson from **Image / Document Processing Risk**?

**Short answer:** Parsers and converters expand attack surface and should be patched, sandboxed, and resource-bounded.

### Q80. What is the key lesson from **SSRF**?

**Short answer:** Server-side request forgery lets untrusted input influence outbound requests to unintended destinations.

### Q81. What is the key lesson from **SSRF Destination Validation**?

**Short answer:** Validate scheme, host, resolved IP, redirects, and destination class before making outbound requests.

### Q82. What is the key lesson from **Cloud Metadata Protection**?

**Short answer:** Applications should prevent untrusted request flows from reaching cloud metadata or credential services.

### Q83. What is the key lesson from **Open Redirect**?

**Short answer:** Unvalidated redirects can support phishing or token leakage in some authentication flows.

### Q84. What is the key lesson from **XXE**?

**Short answer:** Unsafe XML external entity processing can expose local files or make outbound requests.

### Q85. What is the key lesson from **XML Parser Hardening**?

**Short answer:** Disable unneeded external entities, DTDs, and network resolution.

### Q86. What is the key lesson from **Server-Side Template Injection**?

**Short answer:** Template injection occurs when user input becomes template code rather than template data.

### Q87. What is the key lesson from **Template Data Separation**?

**Short answer:** Treat untrusted content as variables, not executable template instructions.

### Q88. What is the key lesson from **Insecure Deserialization**?

**Short answer:** Unsafe object deserialization can instantiate attacker-influenced types or invoke dangerous behaviors.

### Q89. What is the key lesson from **Safe Serialization**?

**Short answer:** Prefer simple data formats and explicit schemas over arbitrary object graphs.

### Q90. What is the key lesson from **Request Smuggling Awareness**?

**Short answer:** HTTP parser disagreements between front-end and back-end components can desynchronize request boundaries.

### Q91. What is the key lesson from **Request Smuggling Safety**?

**Short answer:** Test request-smuggling behavior only in dedicated labs or explicit programs because shared connections can affect other users.

### Q92. What is the key lesson from **HTTP Response Splitting Awareness**?

**Short answer:** Unvalidated header values can corrupt response structure in vulnerable frameworks.

### Q93. What is the key lesson from **Cache Poisoning**?

**Short answer:** If a cache key omits security-relevant request inputs, attacker-controlled content may be served to other users.

### Q94. What is the key lesson from **Cache Deception Awareness**?

**Short answer:** Improper caching of authenticated/private responses can expose sensitive content.

### Q95. What is the key lesson from **CORS**?

**Short answer:** CORS controls browser cross-origin response access, not server-side authorization.

### Q96. What is the key lesson from **CORS Credentials**?

**Short answer:** Credentialed cross-origin access requires exact trusted origins rather than wildcard reflection.

### Q97. What is the key lesson from **Clickjacking**?

**Short answer:** Sensitive user actions should be protected from untrusted framing when UI redress would create impact.

### Q98. What is the key lesson from **WebSocket Authentication**?

**Short answer:** Authenticate the WebSocket upgrade and bind the connection to the correct user.

### Q99. What is the key lesson from **WebSocket Authorization**?

**Short answer:** Authorize each message/action, not only the initial connection.

### Q100. What is the key lesson from **GraphQL Introspection**?

**Short answer:** Schema visibility can aid testing but does not itself create authorization failure.

### Q101. What is the key lesson from **GraphQL Resolver Authorization**?

**Short answer:** Each resolver must enforce the same object and role rules expected in REST or other interfaces.

### Q102. What is the key lesson from **GraphQL Query Cost**?

**Short answer:** Bound depth, complexity, batch size, and expensive resolver fan-out.

### Q103. What is the key lesson from **REST API Authorization**?

**Short answer:** REST resources must enforce object and function authorization independent of client UI.

### Q104. What is the key lesson from **API Schema Validation**?

**Short answer:** Reject malformed, oversized, unexpected, or unknown fields according to the API contract.

### Q105. What is the key lesson from **API Error Handling**?

**Short answer:** Avoid returning stack traces, SQL, internal hostnames, or secret values.

### Q106. What is the key lesson from **API Rate Limiting**?

**Short answer:** Protect expensive or sensitive endpoints using identity- and cost-aware limits.

### Q107. What is the key lesson from **API Pagination**?

**Short answer:** Bound page size and prevent filters/sorts from becoming unbounded expensive operations.

### Q108. What is the key lesson from **API Idempotency**?

**Short answer:** Use scoped idempotency keys for operations where duplicate side effects would be harmful.

### Q109. What is the key lesson from **OAuth Redirect URI**?

**Short answer:** Redirect URIs should be exact or tightly constrained to approved destinations.

### Q110. What is the key lesson from **OAuth State**?

**Short answer:** State protects the authorization response from cross-site request confusion.

### Q111. What is the key lesson from **PKCE**?

**Short answer:** PKCE binds an authorization-code exchange to the initiating client and is important for public clients.

### Q112. What is the key lesson from **OAuth Scope**?

**Short answer:** Tokens should receive only the scopes required by the application.

### Q113. What is the key lesson from **OIDC Nonce Awareness**?

**Short answer:** Nonce helps bind an ID token to an authentication request in appropriate OIDC flows.

### Q114. What is the key lesson from **SAML Assertion Validation**?

**Short answer:** Validate signature, issuer, audience, recipient, time, and replay requirements.

### Q115. What is the key lesson from **Account Linking**?

**Short answer:** SSO/OAuth account-linking workflows must verify both identities before merging accounts.

### Q116. What is the key lesson from **Webhook Authentication**?

**Short answer:** Verify webhook authenticity with signatures, shared secrets, mTLS, or provider-specific mechanisms.

### Q117. What is the key lesson from **Webhook Replay Protection**?

**Short answer:** Use timestamps/nonces/idempotency to prevent repeated valid webhook delivery from creating duplicate effects.

### Q118. What is the key lesson from **Signed URL**?

**Short answer:** Signed URLs should be short-lived, object-scoped, method-scoped, and created only after authorization.

### Q119. What is the key lesson from **Object Storage Authorization**?

**Short answer:** Bucket/container/object policy must not expose private files beyond intended users.

### Q120. What is the key lesson from **Information Disclosure**?

**Short answer:** Stack traces, source maps, debug endpoints, backups, logs, and headers can reveal sensitive internals.

### Q121. What is the key lesson from **Debug Mode**?

**Short answer:** Production debug features should be disabled or strongly restricted.

### Q122. What is the key lesson from **Dependency Vulnerability**?

**Short answer:** Validate whether the vulnerable component and affected execution path actually exist before reporting.

### Q123. What is the key lesson from **SCA Correlation**?

**Short answer:** Use software-composition results together with runtime reachability and vendor guidance.

### Q124. What is the key lesson from **Security Logging**?

**Short answer:** Critical authentication, authorization, admin, and suspicious application events should be logged without secrets.

### Q125. What is the key lesson from **Detection Validation**?

**Short answer:** Confirm whether test requests are visible in WAF, application, API gateway, identity, and SIEM telemetry.

### Q126. What is the key lesson from **Evidence**?

**Short answer:** Preserve exact requests/responses, test roles, timestamps, and minimal sensitive content.

### Q127. What is the key lesson from **Finding Report**?

**Short answer:** Write reproducible findings tied to the violated security property and business impact.

### Q128. What is the key lesson from **Retest**?

**Short answer:** Repeat the original safe request after remediation.

### Q129. What is the key lesson from **Web Application Penetration Testing Final Mental Model**?

**Short answer:** Map the application, understand roles and data flows, test one security property at a time, prove impact minimally, and retest the root-cause fix.

---

## Completion Checklist

- [ ] I completed the core topics.
- [ ] I completed at least 35 labs.
- [ ] I completed the mini project.
- [ ] I can explain the trust boundary before using a tool.
- [ ] I can use synthetic test identities safely.
- [ ] I can demonstrate impact with minimal evidence.
- [ ] I can document remediation and retest.
- [ ] I cleaned up the lab.
