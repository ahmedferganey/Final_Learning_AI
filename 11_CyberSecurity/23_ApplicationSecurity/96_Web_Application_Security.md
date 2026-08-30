# 96. Web Application Security

> Phase 23 — Application Security

## 1. Topic Title

**Web Application Security**

## 2. Learning Objectives

- Design the major security controls covered in this course.
- Explain the trust boundaries and threat models behind those controls.
- Implement repeatable automated and manual verification.
- Operate security logging, remediation, and regression prevention.
- Produce a practical security baseline and mini project.

## 3. Prerequisites

95 Application Security, HTTP/HTTPS, JavaScript, REST APIs, authentication/authorization, databases, and the earlier web penetration-testing phase.

## 4. Core Concepts Explanation

# Part 1 — Web Application Security Scope

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 2 — Browser Security Model

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 3 — Origin

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 4 — Same-Origin Policy

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 5 — Cross-Origin Request

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 6 — Secure Context

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 7 — HTTPS Everywhere

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 8 — HSTS

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 9 — TLS Certificates

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 10 — Reverse Proxy Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 11 — Trusted Proxy Configuration

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 12 — Host Header Validation

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 13 — Forwarded Headers

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 14 — HTTP Request Size

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 15 — HTTP Method Control

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 16 — Content-Type Validation

### Core Explanation

Validation constrains untrusted input to the exact type, size, syntax, semantic range, and business rules the server expects before sensitive processing occurs.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 17 — Cookie Scope

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 18 — Secure Cookie

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 19 — HttpOnly Cookie

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 20 — SameSite Cookie

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 21 — Session Identifier

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 22 — Session Rotation

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 23 — Session Expiry

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 24 — Logout

### Core Explanation

Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 25 — Remember Me

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 26 — CSRF

### Core Explanation

CSRF defenses ensure that state-changing requests using ambient browser credentials represent an intentional action from the authenticated session.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 27 — CSRF Token

### Core Explanation

Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation. Issuance, storage, rotation, expiry, and audit all matter.

### Diagram / Code / Configuration Example

```text
issue → protect → rotate → expire → revoke → audit
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 28 — Origin and Referer Validation

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 29 — SameSite and CSRF

### Core Explanation

CSRF defenses ensure that state-changing requests using ambient browser credentials represent an intentional action from the authenticated session.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 30 — XSS

### Core Explanation

Untrusted data must be treated as data, not executable content. Context-aware encoding and proven sanitization prevent downstream interpreters such as browsers from executing attacker-controlled content.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 31 — Reflected XSS Defense

### Core Explanation

Untrusted data must be treated as data, not executable content. Context-aware encoding and proven sanitization prevent downstream interpreters such as browsers from executing attacker-controlled content.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 32 — Stored XSS Defense

### Core Explanation

Untrusted data must be treated as data, not executable content. Context-aware encoding and proven sanitization prevent downstream interpreters such as browsers from executing attacker-controlled content.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 33 — DOM XSS Defense

### Core Explanation

Untrusted data must be treated as data, not executable content. Context-aware encoding and proven sanitization prevent downstream interpreters such as browsers from executing attacker-controlled content.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 34 — HTML Encoding

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 35 — Attribute Encoding

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 36 — JavaScript Context Safety

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 37 — URL Context Safety

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 38 — Trusted Types Awareness

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 39 — CSP

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 40 — CSP Nonce

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 41 — CSP Reporting

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 42 — Clickjacking

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 43 — Frame Ancestors

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 44 — X-Frame-Options

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 45 — CORS

### Core Explanation

CORS controls which browser origins may read cross-origin responses. It is a browser policy and must never substitute for server-side authorization.

### Diagram / Code / Configuration Example

```text
CORS = may this browser origin read the response?
Authorization = may this principal access this object?
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 46 — CORS Allow-Origin

### Core Explanation

CORS controls which browser origins may read cross-origin responses. It is a browser policy and must never substitute for server-side authorization.

### Diagram / Code / Configuration Example

```text
CORS = may this browser origin read the response?
Authorization = may this principal access this object?
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 47 — CORS Credentials

### Core Explanation

Secrets and machine credentials should be minimized, stored outside source code, scoped narrowly, rotated, audited, and replaced with short-lived workload identity where possible.

### Diagram / Code / Configuration Example

```text
CORS = may this browser origin read the response?
Authorization = may this principal access this object?
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 48 — Preflight

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 49 — Cross-Origin Isolation Awareness

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 50 — Cache Control

### Core Explanation

Caches must preserve identity and authorization assumptions. Cache keys, private/public directives, invalidation, and variation dimensions must prevent one user or tenant receiving another user’s response.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 51 — Cache Key

### Core Explanation

Caches must preserve identity and authorization assumptions. Cache keys, private/public directives, invalidation, and variation dimensions must prevent one user or tenant receiving another user’s response.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 52 — Web Cache Poisoning Defense

### Core Explanation

Caches must preserve identity and authorization assumptions. Cache keys, private/public directives, invalidation, and variation dimensions must prevent one user or tenant receiving another user’s response.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 53 — Cache Deception Defense

### Core Explanation

Caches must preserve identity and authorization assumptions. Cache keys, private/public directives, invalidation, and variation dimensions must prevent one user or tenant receiving another user’s response.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 54 — SQL Injection Defense

### Core Explanation

Query construction must keep code and data separate, use least-privilege database accounts, and constrain expensive or attacker-controlled filtering and sorting behavior.

### Diagram / Code / Configuration Example

```python
cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 55 — ORM Safety

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 56 — NoSQL Injection Defense

### Core Explanation

Query construction must keep code and data separate, use least-privilege database accounts, and constrain expensive or attacker-controlled filtering and sorting behavior.

### Diagram / Code / Configuration Example

```python
cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 57 — Command Injection Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 58 — Path Traversal Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 59 — File Inclusion Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 60 — File Upload Defense

### Core Explanation

File handling requires authorization, size and content validation, generated storage names, non-executable storage, safe parsers, malware handling where appropriate, and protected retrieval.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 61 — Upload Name Handling

### Core Explanation

File handling requires authorization, size and content validation, generated storage names, non-executable storage, safe parsers, malware handling where appropriate, and protected retrieval.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 62 — Parser Isolation

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 63 — SSRF Defense

### Core Explanation

Server-side outbound requests create a network trust boundary. Validate schemes and destinations, revalidate redirects, block internal/metadata targets, and enforce egress policy.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 64 — Metadata Service Protection

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 65 — Open Redirect Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 66 — XXE Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 67 — SSTI Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 68 — Deserialization Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 69 — Request Smuggling Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 70 — Request Splitting Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 71 — Business Logic Security

### Core Explanation

Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 72 — Race Condition Defense

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 73 — Idempotency Key

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 74 — Authentication UI

### Core Explanation

Authentication establishes the identity behind a request. Secure design uses mature identity systems, strong authenticators, safe recovery, rate controls, and audit evidence.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 75 — Password Reset

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 76 — MFA UX Security

### Core Explanation

Authentication establishes the identity behind a request. Secure design uses mature identity systems, strong authenticators, safe recovery, rate controls, and audit evidence.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 77 — Account Lockout

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 78 — Authorization Middleware

### Core Explanation

Authorization decides whether an authenticated subject may perform a specific action on a specific resource. It must be enforced server-side and tested for role, object, tenant, and property boundaries.

### Diagram / Code / Configuration Example

```text
Principal + Resource + Action + Context
                ↓
          Policy Decision
             ↓     ↓
           ALLOW  DENY
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 79 — Object Authorization

### Core Explanation

Authorization decides whether an authenticated subject may perform a specific action on a specific resource. It must be enforced server-side and tested for role, object, tenant, and property boundaries.

### Diagram / Code / Configuration Example

```text
Principal + Resource + Action + Context
                ↓
          Policy Decision
             ↓     ↓
           ALLOW  DENY
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 80 — Tenant Boundary

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 81 — Admin Route

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 82 — Debug Endpoint

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 83 — Error Page

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 84 — Source Map

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 85 — Subresource Integrity Awareness

### Core Explanation

Resource controls protect shared capacity by bounding request rate, concurrency, payload size, query complexity, and tenant consumption according to business cost and priority.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 86 — Third-Party Script Risk

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 87 — Tag Manager Risk

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 88 — Content Sanitization

### Core Explanation

Untrusted data must be treated as data, not executable content. Context-aware encoding and proven sanitization prevent downstream interpreters such as browsers from executing attacker-controlled content.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 89 — Markdown Rendering Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 90 — URL Scheme Validation

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 91 — Download Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 92 — WebSocket Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 93 — GraphQL Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 94 — OAuth Security

### Core Explanation

Federated identity protocols require exact redirect and audience handling, state or replay protections, correct signature validation, least privilege, and safe account-linking or recovery workflows.

### Diagram / Code / Configuration Example

```text
Client → IdP → authorization code + PKCE → token → Resource Server
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 95 — OIDC Security

### Core Explanation

Federated identity protocols require exact redirect and audience handling, state or replay protections, correct signature validation, least privilege, and safe account-linking or recovery workflows.

### Diagram / Code / Configuration Example

```text
Client → IdP → authorization code + PKCE → token → Resource Server
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 96 — SAML Security

### Core Explanation

Federated identity protocols require exact redirect and audience handling, state or replay protections, correct signature validation, least privilege, and safe account-linking or recovery workflows.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 97 — SSO Account Linking

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 98 — Webhook Receiver Security

### Core Explanation

Webhooks cross organizational boundaries and require sender authenticity, schema validation, replay resistance, idempotent processing, scoped secrets, and audit.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 99 — Email Link Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 100 — Passwordless Login

### Core Explanation

Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 101 — WebAuthn Awareness

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 102 — Browser Storage

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 103 — localStorage Risk

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 104 — Service Worker Security

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 105 — PWA Security Awareness

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 106 — Web Security Logging

### Core Explanation

Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 107 — WAF Role

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 108 — Bot Management Awareness

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 109 — Rate Limit

### Core Explanation

Resource controls protect shared capacity by bounding request rate, concurrency, payload size, query complexity, and tenant consumption according to business cost and priority.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 110 — DoS Protection

### Core Explanation

Resource controls protect shared capacity by bounding request rate, concurrency, payload size, query complexity, and tenant consumption according to business cost and priority.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 111 — Security Testing

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 112 — Security Regression

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

# Part 113 — Web Application Security Final Mental Model

### Core Explanation

This web-security topic belongs to the browser/server trust boundary and should be implemented with secure browser primitives plus authoritative server-side controls.

### Diagram / Code / Configuration Example

```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Why It Matters

The control protects a specific identity, data, business, or platform boundary. A good design is explicit enough to test both valid and invalid behavior and to investigate failures in production.

### Production Use

Map the topic to an asset, threat scenario, owner, implementation control, automated/manual verification, and operational evidence.

### Common Problems

- Treating scanner output as final proof.
- Relying on client-side checks for server-side policy.
- Granting broad permissions for convenience.
- Fixing one payload rather than the root cause.
- Logging credentials or excessive sensitive data.
- Failing to convert a fixed vulnerability into regression coverage.

### Best Practice

Define expected secure behavior first, implement the smallest reliable control, test allowed and denied cases, monitor the control, and retest after change.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Web Application Security Scope

### Objective
Practice **Web Application Security Scope** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 2 — Browser Security Model

### Objective
Practice **Browser Security Model** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 3 — Origin

### Objective
Practice **Origin** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 4 — Same-Origin Policy

### Objective
Practice **Same-Origin Policy** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 5 — Cross-Origin Request

### Objective
Practice **Cross-Origin Request** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 6 — Secure Context

### Objective
Practice **Secure Context** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 7 — HTTPS Everywhere

### Objective
Practice **HTTPS Everywhere** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 8 — HSTS

### Objective
Practice **HSTS** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 9 — TLS Certificates

### Objective
Practice **TLS Certificates** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 10 — Reverse Proxy Security

### Objective
Practice **Reverse Proxy Security** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 11 — Trusted Proxy Configuration

### Objective
Practice **Trusted Proxy Configuration** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 12 — Host Header Validation

### Objective
Practice **Host Header Validation** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 13 — Forwarded Headers

### Objective
Practice **Forwarded Headers** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 14 — HTTP Request Size

### Objective
Practice **HTTP Request Size** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 15 — HTTP Method Control

### Objective
Practice **HTTP Method Control** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 16 — Content-Type Validation

### Objective
Practice **Content-Type Validation** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 17 — Cookie Scope

### Objective
Practice **Cookie Scope** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 18 — Secure Cookie

### Objective
Practice **Secure Cookie** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 19 — HttpOnly Cookie

### Objective
Practice **HttpOnly Cookie** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 20 — SameSite Cookie

### Objective
Practice **SameSite Cookie** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 21 — Session Identifier

### Objective
Practice **Session Identifier** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 22 — Session Rotation

### Objective
Practice **Session Rotation** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 23 — Session Expiry

### Objective
Practice **Session Expiry** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 24 — Logout

### Objective
Practice **Logout** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 25 — Remember Me

### Objective
Practice **Remember Me** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 26 — CSRF

### Objective
Practice **CSRF** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 27 — CSRF Token

### Objective
Practice **CSRF Token** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
issue → protect → rotate → expire → revoke → audit
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 28 — Origin and Referer Validation

### Objective
Practice **Origin and Referer Validation** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 29 — SameSite and CSRF

### Objective
Practice **SameSite and CSRF** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 30 — XSS

### Objective
Practice **XSS** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 31 — Reflected XSS Defense

### Objective
Practice **Reflected XSS Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 32 — Stored XSS Defense

### Objective
Practice **Stored XSS Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 33 — DOM XSS Defense

### Objective
Practice **DOM XSS Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 34 — HTML Encoding

### Objective
Practice **HTML Encoding** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 35 — Attribute Encoding

### Objective
Practice **Attribute Encoding** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 36 — JavaScript Context Safety

### Objective
Practice **JavaScript Context Safety** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 37 — URL Context Safety

### Objective
Practice **URL Context Safety** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 38 — Trusted Types Awareness

### Objective
Practice **Trusted Types Awareness** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 39 — CSP

### Objective
Practice **CSP** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 40 — CSP Nonce

### Objective
Practice **CSP Nonce** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 41 — CSP Reporting

### Objective
Practice **CSP Reporting** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 42 — Clickjacking

### Objective
Practice **Clickjacking** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 43 — Frame Ancestors

### Objective
Practice **Frame Ancestors** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 44 — X-Frame-Options

### Objective
Practice **X-Frame-Options** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 45 — CORS

### Objective
Practice **CORS** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
CORS = may this browser origin read the response?
Authorization = may this principal access this object?
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 46 — CORS Allow-Origin

### Objective
Practice **CORS Allow-Origin** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
CORS = may this browser origin read the response?
Authorization = may this principal access this object?
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 47 — CORS Credentials

### Objective
Practice **CORS Credentials** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
CORS = may this browser origin read the response?
Authorization = may this principal access this object?
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 48 — Preflight

### Objective
Practice **Preflight** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 49 — Cross-Origin Isolation Awareness

### Objective
Practice **Cross-Origin Isolation Awareness** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 50 — Cache Control

### Objective
Practice **Cache Control** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 51 — Cache Key

### Objective
Practice **Cache Key** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 52 — Web Cache Poisoning Defense

### Objective
Practice **Web Cache Poisoning Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 53 — Cache Deception Defense

### Objective
Practice **Cache Deception Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 54 — SQL Injection Defense

### Objective
Practice **SQL Injection Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```python
cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 55 — ORM Safety

### Objective
Practice **ORM Safety** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 56 — NoSQL Injection Defense

### Objective
Practice **NoSQL Injection Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```python
cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 57 — Command Injection Defense

### Objective
Practice **Command Injection Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 58 — Path Traversal Defense

### Objective
Practice **Path Traversal Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 59 — File Inclusion Defense

### Objective
Practice **File Inclusion Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 60 — File Upload Defense

### Objective
Practice **File Upload Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 61 — Upload Name Handling

### Objective
Practice **Upload Name Handling** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 62 — Parser Isolation

### Objective
Practice **Parser Isolation** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 63 — SSRF Defense

### Objective
Practice **SSRF Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 64 — Metadata Service Protection

### Objective
Practice **Metadata Service Protection** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 65 — Open Redirect Defense

### Objective
Practice **Open Redirect Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 66 — XXE Defense

### Objective
Practice **XXE Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 67 — SSTI Defense

### Objective
Practice **SSTI Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 68 — Deserialization Defense

### Objective
Practice **Deserialization Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 69 — Request Smuggling Defense

### Objective
Practice **Request Smuggling Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## Lab 70 — Request Splitting Defense

### Objective
Practice **Request Splitting Defense** on an application/API you own or an intentionally vulnerable training environment.

### Procedure
1. State the security requirement.
2. Draw the relevant trust boundary.
3. Capture baseline behavior.
4. Implement or review the control.
5. Test one valid case and one denied/invalid case.
6. Preserve request/code/config/log evidence.
7. Document residual risk.
8. Retest after change.

### Starter Example
```text
Requirement → Control → Implementation → Verification → Telemetry → Remediation
```

### Evidence Template
```text
Requirement:
Asset:
Threat:
Expected:
Observed:
Control:
Evidence:
Residual risk:
Retest:
```

---

## 6. Mini Project

# Harden a Web Application

Harden a web application you own: HTTPS/HSTS, cookies/sessions, CSRF, XSS/CSP, CORS, authorization, upload/SSRF protection, secure errors, caching, web logging, and security regression tests.

Required deliverables: architecture/threat model, security requirements, implementation evidence, negative tests, logging, remediation, and retest report.

## 7. Recommended Resources

- https://cheatsheetseries.owasp.org/
- https://owasp.org/www-project-application-security-verification-standard/
- https://developer.mozilla.org/docs/Web/Security
- https://portswigger.net/web-security

## 8. Certification Relevance

Relevant to application-security engineering, product security, DevSecOps, secure software engineering, cloud security, API/web security, and software assurance.

## 9. Common Mistakes & Best Practices

### Common Mistakes
- Adding security only before release.
- Confusing authentication with authorization.
- Hardcoding secrets.
- Trusting clients or internal networks.
- Treating automated results as confirmed risk.
- Shipping fixes without regression tests.

### Best Practices
- Threat-model early.
- Deny by default.
- Enforce policy server-side.
- Prefer established framework/platform security primitives.
- Automate repeatable checks.
- Preserve evidence.
- Fix root causes and retest.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the key lesson from **Web Application Security Scope**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q2. What is the key lesson from **Browser Security Model**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q3. What is the key lesson from **Origin**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q4. What is the key lesson from **Same-Origin Policy**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q5. What is the key lesson from **Cross-Origin Request**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q6. What is the key lesson from **Secure Context**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q7. What is the key lesson from **HTTPS Everywhere**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q8. What is the key lesson from **HSTS**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q9. What is the key lesson from **TLS Certificates**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q10. What is the key lesson from **Reverse Proxy Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q11. What is the key lesson from **Trusted Proxy Configuration**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q12. What is the key lesson from **Host Header Validation**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q13. What is the key lesson from **Forwarded Headers**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q14. What is the key lesson from **HTTP Request Size**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q15. What is the key lesson from **HTTP Method Control**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q16. What is the key lesson from **Content-Type Validation**?

**Short answer:** Validation constrains untrusted input to the exact type, size, syntax, semantic range, and business rules the server expects before sensitive processing occurs.

### Q17. What is the key lesson from **Cookie Scope**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q18. What is the key lesson from **Secure Cookie**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q19. What is the key lesson from **HttpOnly Cookie**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q20. What is the key lesson from **SameSite Cookie**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q21. What is the key lesson from **Session Identifier**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q22. What is the key lesson from **Session Rotation**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q23. What is the key lesson from **Session Expiry**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q24. What is the key lesson from **Logout**?

**Short answer:** Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Q25. What is the key lesson from **Remember Me**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q26. What is the key lesson from **CSRF**?

**Short answer:** CSRF defenses ensure that state-changing requests using ambient browser credentials represent an intentional action from the authenticated session.

### Q27. What is the key lesson from **CSRF Token**?

**Short answer:** Session and token security protects authenticated state from theft, replay, overlong lifetime, confused audience, and weak revocation.

### Q28. What is the key lesson from **Origin and Referer Validation**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q29. What is the key lesson from **SameSite and CSRF**?

**Short answer:** CSRF defenses ensure that state-changing requests using ambient browser credentials represent an intentional action from the authenticated session.

### Q30. What is the key lesson from **XSS**?

**Short answer:** Untrusted data must be treated as data, not executable content.

### Q31. What is the key lesson from **Reflected XSS Defense**?

**Short answer:** Untrusted data must be treated as data, not executable content.

### Q32. What is the key lesson from **Stored XSS Defense**?

**Short answer:** Untrusted data must be treated as data, not executable content.

### Q33. What is the key lesson from **DOM XSS Defense**?

**Short answer:** Untrusted data must be treated as data, not executable content.

### Q34. What is the key lesson from **HTML Encoding**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q35. What is the key lesson from **Attribute Encoding**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q36. What is the key lesson from **JavaScript Context Safety**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q37. What is the key lesson from **URL Context Safety**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q38. What is the key lesson from **Trusted Types Awareness**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q39. What is the key lesson from **CSP**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q40. What is the key lesson from **CSP Nonce**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q41. What is the key lesson from **CSP Reporting**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q42. What is the key lesson from **Clickjacking**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q43. What is the key lesson from **Frame Ancestors**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q44. What is the key lesson from **X-Frame-Options**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q45. What is the key lesson from **CORS**?

**Short answer:** CORS controls which browser origins may read cross-origin responses.

### Q46. What is the key lesson from **CORS Allow-Origin**?

**Short answer:** CORS controls which browser origins may read cross-origin responses.

### Q47. What is the key lesson from **CORS Credentials**?

**Short answer:** Secrets and machine credentials should be minimized, stored outside source code, scoped narrowly, rotated, audited, and replaced with short-lived workload identity where possible.

### Q48. What is the key lesson from **Preflight**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q49. What is the key lesson from **Cross-Origin Isolation Awareness**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q50. What is the key lesson from **Cache Control**?

**Short answer:** Caches must preserve identity and authorization assumptions.

### Q51. What is the key lesson from **Cache Key**?

**Short answer:** Caches must preserve identity and authorization assumptions.

### Q52. What is the key lesson from **Web Cache Poisoning Defense**?

**Short answer:** Caches must preserve identity and authorization assumptions.

### Q53. What is the key lesson from **Cache Deception Defense**?

**Short answer:** Caches must preserve identity and authorization assumptions.

### Q54. What is the key lesson from **SQL Injection Defense**?

**Short answer:** Query construction must keep code and data separate, use least-privilege database accounts, and constrain expensive or attacker-controlled filtering and sorting behavior.

### Q55. What is the key lesson from **ORM Safety**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q56. What is the key lesson from **NoSQL Injection Defense**?

**Short answer:** Query construction must keep code and data separate, use least-privilege database accounts, and constrain expensive or attacker-controlled filtering and sorting behavior.

### Q57. What is the key lesson from **Command Injection Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q58. What is the key lesson from **Path Traversal Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q59. What is the key lesson from **File Inclusion Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q60. What is the key lesson from **File Upload Defense**?

**Short answer:** File handling requires authorization, size and content validation, generated storage names, non-executable storage, safe parsers, malware handling where appropriate, and protected retrieval.

### Q61. What is the key lesson from **Upload Name Handling**?

**Short answer:** File handling requires authorization, size and content validation, generated storage names, non-executable storage, safe parsers, malware handling where appropriate, and protected retrieval.

### Q62. What is the key lesson from **Parser Isolation**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q63. What is the key lesson from **SSRF Defense**?

**Short answer:** Server-side outbound requests create a network trust boundary.

### Q64. What is the key lesson from **Metadata Service Protection**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q65. What is the key lesson from **Open Redirect Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q66. What is the key lesson from **XXE Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q67. What is the key lesson from **SSTI Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q68. What is the key lesson from **Deserialization Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q69. What is the key lesson from **Request Smuggling Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q70. What is the key lesson from **Request Splitting Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q71. What is the key lesson from **Business Logic Security**?

**Short answer:** Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Q72. What is the key lesson from **Race Condition Defense**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q73. What is the key lesson from **Idempotency Key**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q74. What is the key lesson from **Authentication UI**?

**Short answer:** Authentication establishes the identity behind a request.

### Q75. What is the key lesson from **Password Reset**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q76. What is the key lesson from **MFA UX Security**?

**Short answer:** Authentication establishes the identity behind a request.

### Q77. What is the key lesson from **Account Lockout**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q78. What is the key lesson from **Authorization Middleware**?

**Short answer:** Authorization decides whether an authenticated subject may perform a specific action on a specific resource.

### Q79. What is the key lesson from **Object Authorization**?

**Short answer:** Authorization decides whether an authenticated subject may perform a specific action on a specific resource.

### Q80. What is the key lesson from **Tenant Boundary**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q81. What is the key lesson from **Admin Route**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q82. What is the key lesson from **Debug Endpoint**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q83. What is the key lesson from **Error Page**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q84. What is the key lesson from **Source Map**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q85. What is the key lesson from **Subresource Integrity Awareness**?

**Short answer:** Resource controls protect shared capacity by bounding request rate, concurrency, payload size, query complexity, and tenant consumption according to business cost and priority.

### Q86. What is the key lesson from **Third-Party Script Risk**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q87. What is the key lesson from **Tag Manager Risk**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q88. What is the key lesson from **Content Sanitization**?

**Short answer:** Untrusted data must be treated as data, not executable content.

### Q89. What is the key lesson from **Markdown Rendering Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q90. What is the key lesson from **URL Scheme Validation**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q91. What is the key lesson from **Download Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q92. What is the key lesson from **WebSocket Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q93. What is the key lesson from **GraphQL Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q94. What is the key lesson from **OAuth Security**?

**Short answer:** Federated identity protocols require exact redirect and audience handling, state or replay protections, correct signature validation, least privilege, and safe account-linking or recovery workflows.

### Q95. What is the key lesson from **OIDC Security**?

**Short answer:** Federated identity protocols require exact redirect and audience handling, state or replay protections, correct signature validation, least privilege, and safe account-linking or recovery workflows.

### Q96. What is the key lesson from **SAML Security**?

**Short answer:** Federated identity protocols require exact redirect and audience handling, state or replay protections, correct signature validation, least privilege, and safe account-linking or recovery workflows.

### Q97. What is the key lesson from **SSO Account Linking**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q98. What is the key lesson from **Webhook Receiver Security**?

**Short answer:** Webhooks cross organizational boundaries and require sender authenticity, schema validation, replay resistance, idempotent processing, scoped secrets, and audit.

### Q99. What is the key lesson from **Email Link Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q100. What is the key lesson from **Passwordless Login**?

**Short answer:** Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Q101. What is the key lesson from **WebAuthn Awareness**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q102. What is the key lesson from **Browser Storage**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q103. What is the key lesson from **localStorage Risk**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q104. What is the key lesson from **Service Worker Security**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q105. What is the key lesson from **PWA Security Awareness**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q106. What is the key lesson from **Web Security Logging**?

**Short answer:** Security telemetry should make high-value identity, authorization, configuration, and business events attributable and investigable without logging secrets or unnecessary sensitive data.

### Q107. What is the key lesson from **WAF Role**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q108. What is the key lesson from **Bot Management Awareness**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q109. What is the key lesson from **Rate Limit**?

**Short answer:** Resource controls protect shared capacity by bounding request rate, concurrency, payload size, query complexity, and tenant consumption according to business cost and priority.

### Q110. What is the key lesson from **DoS Protection**?

**Short answer:** Resource controls protect shared capacity by bounding request rate, concurrency, payload size, query complexity, and tenant consumption according to business cost and priority.

### Q111. What is the key lesson from **Security Testing**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q112. What is the key lesson from **Security Regression**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

### Q113. What is the key lesson from **Web Application Security Final Mental Model**?

**Short answer:** This application-security topic should be tied to a concrete threat, a verifiable implementation control, an owner, and an operational method for detecting failure or regression.

## Completion Checklist
- [ ] I completed the core topics.
- [ ] I completed at least 35 labs.
- [ ] I completed the mini project.
- [ ] I can explain the trust boundaries.
- [ ] I can test both allowed and denied behavior.
- [ ] I can document remediation and regression coverage.
