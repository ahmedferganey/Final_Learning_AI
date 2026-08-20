# 1. Topic Title

## Introduction to Cybersecurity

Cybersecurity is the disciplined management of risk to information, identities, systems, applications, networks, cloud resources, physical infrastructure, and business operations.

It is not equivalent to “hacking,” antivirus, or installing a firewall. A mature security program combines governance, architecture, identity, hardening, monitoring, response, recovery, and human processes.

The enhanced edition preserves the original topics—risk, assets, threats, vulnerabilities, CIA, authentication/authorization, MFA, least privilege, separation of duties, defense in depth, controls, common threat categories, vulnerability management, logging, incident response, and NIST CSF—and adds critical bridge topics required before later phases: attack surface, exposure, data classification and lifecycle, cryptography foundations, IAM/PAM awareness, Zero Trust principles, network/application/cloud security foundations, threat modeling, security baselines, SIEM awareness, business continuity, governance documentation, supply-chain risk, security awareness, and safe authorization boundaries.

The central mental model is:

```text
Business Mission
      ↓
Assets / Data / Services
      ↓
Threats + Vulnerabilities + Exposure
      ↓
Risk
      ↓
Controls
├─ Govern
├─ Protect
├─ Detect
├─ Respond
└─ Recover
      ↓
Evidence / Monitoring / Improvement
      ↺
```

Every lab in this file is defensive and must be performed only on systems you own or are explicitly authorized to administer.

# 2. Learning Objectives

1. Explain cybersecurity as business and technical risk management.
2. Distinguish asset, threat, threat actor, vulnerability, exposure, attack surface, exploit, event, incident, likelihood, impact, and risk.
3. Apply confidentiality, integrity, and availability to real systems.
4. Explain authenticity, accountability, auditing, and non-repudiation awareness.
5. Distinguish authentication, authorization, and accounting/auditing.
6. Explain password security, MFA, phishing-resistant MFA awareness, and account recovery risk.
7. Apply least privilege, need-to-know, separation of duties, and privileged-access awareness.
8. Explain defense in depth, secure defaults, fail-safe behavior, minimization, and segmentation.
9. Distinguish administrative, technical, and physical controls.
10. Distinguish preventive, detective, corrective, deterrent, recovery, and compensating controls.
11. Explain data classification and the data lifecycle from creation through destruction.
12. Explain hashing, encryption, symmetric/asymmetric cryptography, digital signatures, certificates, and TLS conceptually.
13. Explain host hardening, patching, service minimization, firewalling, endpoint protection, and secure configuration baselines.
14. Explain network security foundations including segmentation, firewalls, IDS/IPS awareness, VPN, and secure protocols.
15. Explain application security foundations including validation, parameterized queries, authorization, secrets, and dependency risk.
16. Explain cloud shared responsibility and cloud identity/configuration risk conceptually.
17. Explain social engineering, phishing, credential abuse, malware, ransomware, exploitation, misconfiguration, insider, supply-chain, and denial-of-service categories.
18. Explain vulnerability management lifecycle and risk-based prioritization.
19. Explain threat modeling and attack-path thinking defensively.
20. Explain Zero Trust principles at a foundational level.
21. Explain logging, monitoring, alerting, SIEM awareness, baselines, and detection.
22. Explain incident-response stages and evidence preservation.
23. Explain business continuity, disaster recovery, backup, RPO, and RTO awareness.
24. Explain security governance: policies, standards, procedures, guidelines, risk acceptance, and exceptions.
25. Explain security awareness and human-factor controls.
26. Explain NIST CSF 2.0 Functions as an organizing framework.
27. Build an asset inventory, data classification, risk register, access matrix, hardening baseline, monitoring plan, and incident runbook for a small cloud-ready application.

# 3. Prerequisites

Required foundation:

```text
01. Operating Systems Fundamentals
02. Computer Networks Fundamentals
```

Helpful:

```text
03. Introduction to Programming
04. Database Fundamentals
06. Cloud Computing and Virtualization Foundations
```

Safety boundary:

```text
Use only systems, accounts, logs, networks, and cloud resources you own
or are explicitly authorized to administer.
```

This module teaches defensive reasoning and safe observation. Later ethical-hacking phases introduce assessment techniques under explicit authorization.

# 4. Core Concepts Explanation

# Part 1 — Cybersecurity as Risk Management

### Core Explanation

Security aims to reduce risk to an acceptable level while enabling the business. Eliminating all risk is usually impossible because controls have cost, usability, operational, and performance trade-offs.

### Diagram / Mental Model

```text
Business objective
 ↓
Assets
 ↓
Threat scenarios
 ↓
Risk assessment
 ↓
Controls / treatment
 ↓
Residual risk
```

### Why It Matters

Security decisions should be prioritized by business impact rather than fear or tool popularity.

# Part 2 — Asset

### Core Explanation

An asset is anything of value requiring protection: data, identities, hardware, software, services, intellectual property, reputation, or business processes.

### Diagram / Mental Model

```text
Assets
├─ Customer data
├─ Credentials
├─ Source code
├─ Cloud account
├─ Production API
├─ Backups
└─ Business operations
```

### Why It Matters

You cannot manage risk to assets you do not know exist.

# Part 3 — Asset Owner

### Core Explanation

An asset owner is the accountable person or function responsible for business value, classification, and risk decisions for an asset.

### Why It Matters

Security teams advise and operate controls, but business ownership is needed for prioritization and risk acceptance.

# Part 4 — Threat

### Core Explanation

A threat is a potential cause of harm. It may be malicious or non-malicious.

### Diagram / Mental Model

```text
Malicious: cybercrime, insider abuse
Non-malicious: human error, hardware failure, fire
```

### Why It Matters

Cybersecurity includes operational and environmental threats where they affect security objectives.

# Part 5 — Threat Actor

### Core Explanation

A threat actor is an entity that intentionally attempts to cause harm or gain unauthorized access.

### Diagram / Mental Model

```text
Examples:
cybercriminal
malicious insider
state-aligned actor
hacktivist awareness
```

### Why It Matters

Motivation, capability, and access affect likelihood and control selection.

# Part 6 — Vulnerability

### Core Explanation

A vulnerability is a weakness that can be exploited or triggered to compromise security.

### Diagram / Mental Model

```text
unpatched software
weak access control
unsafe input handling
misconfiguration
excessive privilege
```

### Why It Matters

A vulnerability is potential risk, not automatically an incident.

# Part 7 — Misconfiguration

### Core Explanation

A misconfiguration is an insecure or unintended setting that creates exposure even when software has no coding defect.

### Diagram / Mental Model

```text
database bound to public interface
cloud bucket shared publicly
default password
firewall rule 0.0.0.0/0 to admin port
```

### Why It Matters

Cloud and infrastructure incidents frequently arise from configuration rather than novel exploits.

# Part 8 — Exposure

### Core Explanation

Exposure describes how reachable or accessible an asset or weakness is to a potential threat.

### Diagram / Mental Model

```text
vulnerable service
+ Internet reachable
+ no compensating control
= higher exposure
```

### Why It Matters

The same vulnerability can have very different risk depending on exposure.

# Part 9 — Attack Surface

### Core Explanation

The attack surface is the set of reachable interfaces, identities, services, software, APIs, data paths, and physical access points that could be abused.

### Diagram / Mental Model

```text
Attack surface
├─ login pages
├─ open ports
├─ APIs
├─ admin consoles
├─ cloud roles
├─ email users
└─ third-party integrations
```

### Why It Matters

Minimization reduces opportunities for failure or abuse.

# Part 10 — Exploit — Conceptual

### Core Explanation

An exploit is a technique or code that takes advantage of a vulnerability to produce unintended behavior. This phase focuses on defensive understanding, not exploitation steps.

### Why It Matters

Separating vulnerability from exploitation helps prioritize realistic attack paths.

# Part 11 — Security Event vs Incident

### Core Explanation

A security event is an observable occurrence. A security incident is an event or series of events that actually or potentially violates security policy or causes harm and requires response.

### Diagram / Mental Model

```text
Event: failed login
Incident: confirmed credential compromise and unauthorized access
```

### Why It Matters

Not every alert/event is an incident.

# Part 12 — Likelihood

### Core Explanation

Likelihood estimates how probable a risk scenario is given threat capability, exposure, controls, history, and context.

### Why It Matters

Qualitative scales such as Low/Medium/High are common in foundations.

# Part 13 — Impact

### Core Explanation

Impact measures consequences such as financial loss, safety, downtime, data disclosure, legal exposure, or reputational damage.

### Why It Matters

A technically simple event can be high impact if it affects a critical business process.

# Part 14 — Risk

### Core Explanation

Risk combines the likelihood and impact of a defined scenario. A simple foundational model is `risk ≈ likelihood × impact`, while real methodologies can be more detailed.

### Diagram / Mental Model

```text
Scenario: phishing privileged admin
Likelihood: Medium
Impact: High
Risk: High-ish / prioritized
```

### Why It Matters

Risk must be tied to a scenario, not just a vulnerability score.

# Part 15 — Inherent vs Residual Risk Awareness

### Core Explanation

Inherent risk is risk before controls. Residual risk is what remains after controls are applied.

### Diagram / Mental Model

```text
Inherent risk
 ↓ controls
Residual risk
```

### Why It Matters

Controls reduce risk but rarely eliminate it.

# Part 16 — Risk Treatment

### Core Explanation

Common treatments are mitigate/reduce, avoid, transfer/share, and accept.

### Diagram / Mental Model

```text
Mitigate: add MFA
Avoid: retire unsafe service
Transfer: insurance/contractual transfer awareness
Accept: documented residual risk
```

### Why It Matters

Acceptance should be authorized and time-bounded where appropriate.

# Part 17 — Risk Appetite vs Tolerance Awareness

### Core Explanation

Risk appetite is the amount/type of risk an organization is broadly willing to pursue or retain. Tolerance is the acceptable variation around objectives or specific thresholds.

### Why It Matters

These concepts connect security decisions to business governance.

# Part 18 — Confidentiality

### Core Explanation

Confidentiality protects information from unauthorized disclosure.

### Diagram / Mental Model

```text
Data
 ↓ access control + encryption + classification
Authorized users only
```

### Why It Matters

A confidentiality incident can occur without changing or destroying data.

# Part 19 — Integrity

### Core Explanation

Integrity protects accuracy, completeness, and authorized state of data and systems.

### Diagram / Mental Model

```text
baseline/config
 ↓ hash/signature/change control
verify expected state
```

### Why It Matters

Unauthorized modification can be as damaging as theft.

# Part 20 — Availability

### Core Explanation

Availability ensures authorized users can access required systems/data when needed.

### Diagram / Mental Model

```text
redundancy + capacity + monitoring + backups + recovery
```

### Why It Matters

Security includes resilience against outages and denial of service.

# Part 21 — CIA Trade-Offs

### Core Explanation

Controls can affect multiple objectives and create trade-offs.

### Diagram / Mental Model

```text
Strict access control
+ confidentiality
- possible usability/availability if badly designed
```

### Why It Matters

Security architecture balances business requirements rather than maximizing one property blindly.

# Part 22 — Authenticity Awareness

### Core Explanation

Authenticity is confidence that an identity, message, system, or artifact is genuine.

### Why It Matters

Certificates, signatures, authentication, and provenance can support authenticity.

# Part 23 — Accountability

### Core Explanation

Accountability means actions can be associated with responsible identities and processes.

### Diagram / Mental Model

```text
named account + protected logs + time sync → stronger accountability
```

### Why It Matters

Shared accounts weaken accountability.

# Part 24 — Auditing

### Core Explanation

Auditing records and reviews actions/configuration to verify policy, detect misuse, and provide evidence.

### Why It Matters

Logging without review or protection provides limited value.

# Part 25 — Non-Repudiation Awareness

### Core Explanation

Non-repudiation aims to provide evidence that an actor performed an action such that they cannot plausibly deny it later, often using signatures, trusted records, and process controls.

### Why It Matters

It is stronger than ordinary logging and depends on legal/technical context.

# Part 26 — Authentication

### Core Explanation

Authentication establishes or verifies identity.

### Diagram / Mental Model

```text
Claim: I am user A
 ↓ password/MFA/certificate
Authenticated identity
```

### Why It Matters

Authentication does not decide what the identity can access.

# Part 27 — Authorization

### Core Explanation

Authorization decides what an authenticated identity is allowed to do to a resource.

### Diagram / Mental Model

```text
Authenticated user A
 ↓ policy
Can read report
Cannot administer database
```

### Why It Matters

Many serious vulnerabilities are authorization failures, not login failures.

# Part 28 — Accounting / Audit

### Core Explanation

Accounting records activity such as logins, changes, API calls, and resource use.

### Diagram / Mental Model

```text
AAA mental model:
Authentication
Authorization
Accounting
```

### Why It Matters

Provides traceability and supports detection.

# Part 29 — Password Security

### Core Explanation

Passwords should be unique, sufficiently strong, protected by secure password managers where appropriate, and never shared or reused across critical services.

### Why It Matters

Credential reuse converts one breach into many account compromises.

# Part 30 — Password Hashing Awareness

### Core Explanation

Systems should store passwords using dedicated slow password-hashing algorithms with salts, not reversible encryption or fast general-purpose hashes.

### Diagram / Mental Model

```text
password
 + salt
 ↓ password hashing function
stored verifier
```

### Why It Matters

If a credential database is stolen, slow salted hashing increases attacker cost.

# Part 31 — MFA

### Core Explanation

Multi-factor authentication combines factors from different categories such as something you know, have, or are.

### Diagram / Mental Model

```text
Password (know)
+ hardware/app factor (have)
= MFA
```

### Why It Matters

Two passwords are not two factors.

# Part 32 — Phishing-Resistant MFA Awareness

### Core Explanation

Some MFA methods cryptographically bind authentication to the legitimate service and resist credential phishing better than codes that users can manually relay.

### Why It Matters

Privileged and high-value accounts should use stronger authentication where feasible.

# Part 33 — Account Recovery Risk

### Core Explanation

Recovery mechanisms can become a weaker path than normal authentication.

### Diagram / Mental Model

```text
Strong MFA
 but weak help-desk reset
→ attacker targets reset process
```

### Why It Matters

Secure identity lifecycle includes recovery and support processes.

# Part 34 — Least Privilege

### Core Explanation

Grant only the permissions required for a task and only for as long as needed.

### Why It Matters

Reduces blast radius of compromised users and applications.

# Part 35 — Need-to-Know

### Core Explanation

Access to sensitive information should be limited to people/processes with a legitimate business need.

### Why It Matters

A user may have general system access but not need specific confidential data.

# Part 36 — Separation of Duties

### Core Explanation

Sensitive workflows are divided so one identity cannot complete every critical step alone.

### Diagram / Mental Model

```text
Developer proposes change
Reviewer approves
Automation deploys
```

### Why It Matters

Reduces fraud, misuse, and accidental changes.

# Part 37 — Privileged Access Management Awareness

### Core Explanation

Privileged Access Management controls, monitors, limits, and often time-bounds administrative access.

### Diagram / Mental Model

```text
Normal account → request elevation → approved privileged session → audit
```

### Why It Matters

Permanent administrator access is high risk.

# Part 38 — Service Accounts

### Core Explanation

Applications and automation use non-human identities that should have scoped permissions, rotated credentials or workload identity, and monitored use.

### Why It Matters

Service credentials are commonly forgotten and overprivileged.

# Part 39 — Identity Lifecycle

### Core Explanation

Identity management includes onboarding, role changes, periodic access review, and offboarding.

### Diagram / Mental Model

```text
Join → provision
Move → adjust
Leave → revoke
```

### Why It Matters

Dormant or stale accounts create unnecessary access paths.

# Part 40 — Access Review

### Core Explanation

Periodic review verifies that permissions still match current job/business need.

### Why It Matters

Least privilege degrades over time without review.

# Part 41 — Security Control

### Core Explanation

A security control is a safeguard that changes likelihood or impact of a risk scenario.

### Why It Matters

Controls should map to defined risks and outcomes.

# Part 42 — Administrative Controls

### Core Explanation

Policies, standards, procedures, training, risk management, vendor management, and change control are administrative/managerial controls.

### Why It Matters

Security technology fails without governance and process.

# Part 43 — Technical Controls

### Core Explanation

Firewalls, MFA, EDR, encryption, access controls, SIEM, and secure configurations are technical/logical controls.

# Part 44 — Physical Controls

### Core Explanation

Locks, guards, CCTV, badges, barriers, fire suppression, and environmental controls protect facilities and hardware.

### Why It Matters

Physical access can bypass many technical controls.

# Part 45 — Preventive Control

### Core Explanation

A preventive control attempts to stop an unwanted event before it occurs.

### Example / Commands / Configuration

```text
MFA, firewall rule, least privilege
```

# Part 46 — Detective Control

### Core Explanation

A detective control identifies suspicious or undesired activity.

### Example / Commands / Configuration

```text
SIEM alert, IDS detection, file-integrity monitoring
```

# Part 47 — Corrective Control

### Core Explanation

A corrective control repairs or reduces damage after a problem is detected.

### Example / Commands / Configuration

```text
patching a vulnerable component, removing malicious persistence
```

# Part 48 — Recovery Control

### Core Explanation

A recovery control restores normal operation/data after disruption.

### Example / Commands / Configuration

```text
tested backup restore, disaster recovery site
```

# Part 49 — Deterrent Control

### Core Explanation

A deterrent control discourages undesirable behavior by increasing perceived consequences.

### Example / Commands / Configuration

```text
warning banners, visible guards, sanctions policy
```

# Part 50 — Compensating Control

### Core Explanation

A compensating control provides alternative protection when the preferred control cannot be implemented.

### Why It Matters

It should address the same underlying risk and be documented.

# Part 51 — Defense in Depth

### Core Explanation

Defense in depth uses independent layers so one control failure does not expose the entire asset.

### Diagram / Mental Model

```text
Identity
 + Network
 + Host
 + Application
 + Data
 + Detection
 + Recovery
```

### Why It Matters

No single security product is sufficient.

# Part 52 — Secure by Default

### Core Explanation

Default configuration should choose the safer option unless a user deliberately enables additional exposure.

### Diagram / Mental Model

```text
Default:
admin interface local/private
unused ports closed
least privilege role
```

### Why It Matters

Most users do not change defaults.

# Part 53 — Fail Secure / Fail Safe Awareness

### Core Explanation

When components fail, the design should default to a state appropriate to the risk—often denying sensitive access rather than silently allowing it.

### Why It Matters

Failure behavior must be designed, not accidental.

# Part 54 — Minimize Attack Surface

### Core Explanation

Remove or disable unnecessary services, accounts, ports, packages, APIs, and privileges.

### Why It Matters

Every exposed capability requires patching, monitoring, and protection.

# Part 55 — Segmentation

### Core Explanation

Segmentation divides systems by trust/function and controls communication between them.

### Diagram / Mental Model

```text
Users → App Tier → DB Tier
          only required flows
```

### Why It Matters

Limits lateral movement and blast radius.

# Part 56 — Zero Trust Awareness

### Core Explanation

Zero Trust assumes network location alone does not establish trust. Access decisions continuously consider identity, device/workload, resource, policy, and context.

### Diagram / Mental Model

```text
Never trust solely because "inside network"
Verify identity + authorize resource + monitor
```

### Why It Matters

It is an architecture principle, not a single product.

# Part 57 — Data Classification

### Core Explanation

Classification assigns protection requirements based on sensitivity, business value, regulation, and impact.

### Diagram / Mental Model

```text
Public
Internal
Confidential
Restricted/Critical
```

### Why It Matters

Controls should follow data value rather than be identical everywhere.

# Part 58 — Data Owner vs Custodian Awareness

### Core Explanation

A data owner determines classification and permitted use; custodians/operators implement storage, backup, and controls.

### Why It Matters

Clear accountability prevents security decisions from falling between teams.

# Part 59 — Data Lifecycle

### Core Explanation

Data security must cover creation, collection, use, sharing, storage, archival, retention, and destruction.

### Diagram / Mental Model

```text
Create → Use → Share → Store → Archive → Destroy
```

### Why It Matters

Protecting only live production data ignores backups, exports, logs, and old copies.

# Part 60 — Data Minimization

### Core Explanation

Collect and retain only data necessary for a defined purpose.

### Why It Matters

Less sensitive data means less breach impact and compliance burden.

# Part 61 — Retention

### Core Explanation

Retention defines how long data must or may be kept.

### Why It Matters

Keeping everything forever increases risk and cost.

# Part 62 — Secure Deletion Awareness

### Core Explanation

Deleting a file often removes references rather than immediately overwriting every storage location. Secure destruction methods depend on storage technology, encryption, lifecycle, and organizational requirements.

### Why It Matters

Cloud/object/SSD/backup systems require lifecycle-aware destruction rather than simplistic overwrite assumptions.

# Part 63 — Backup Security

### Core Explanation

Backups contain valuable data and should have access control, encryption where required, retention, isolation, monitoring, and restore testing.

### Why It Matters

Ransomware and destructive actors often target backups.

# Part 64 — Cryptography Purpose

### Core Explanation

Cryptography supports confidentiality, integrity, authenticity, and sometimes non-repudiation by using mathematical algorithms and keys.

### Why It Matters

Cryptography is a component of security, not a substitute for access control or secure design.

# Part 65 — Hash Function

### Core Explanation

A cryptographic hash maps arbitrary input to a fixed-size digest and is designed so small input changes produce very different outputs.

### Diagram / Mental Model

```text
file → SHA-256 → digest
modify file → different digest
```

### Why It Matters

Useful for integrity checks and artifact verification.

# Part 66 — Hash Is Not Encryption

### Core Explanation

Hashing is one-way by design; encryption is reversible with the correct key.

### Diagram / Mental Model

```text
Hash: data → digest
Encryption: plaintext ⇄ ciphertext using key
```

### Why It Matters

Confusing them leads to insecure password/data designs.

# Part 67 — Symmetric Encryption

### Core Explanation

Symmetric encryption uses the same secret key (or directly related shared secret) to encrypt and decrypt.

### Diagram / Mental Model

```text
Plaintext + shared key → Ciphertext
Ciphertext + shared key → Plaintext
```

### Why It Matters

Fast and widely used for bulk data encryption; key distribution is the challenge.

# Part 68 — Asymmetric Encryption Awareness

### Core Explanation

Asymmetric cryptography uses a public/private key pair for operations such as encryption/key exchange/signatures depending on algorithm.

### Diagram / Mental Model

```text
Public key ↔ Private key pair
```

### Why It Matters

Enables secure key establishment and digital identity mechanisms.

# Part 69 — Digital Signature

### Core Explanation

A digital signature uses a private key operation so others can verify integrity/authenticity with the corresponding public key.

### Diagram / Mental Model

```text
Message hash
 ↓ sign with private key
Signature
 ↓ verify with public key
```

### Why It Matters

A signature does not encrypt the message by itself.

# Part 70 — Certificate / PKI Awareness

### Core Explanation

Digital certificates bind public keys to identities under a trust model, commonly using certificate authorities.

### Diagram / Mental Model

```text
CA trust
 ↓ certificate
example.com public key identity
```

### Why It Matters

TLS depends on certificate validation to prevent impersonation.

# Part 71 — TLS Awareness

### Core Explanation

TLS protects network sessions through authenticated key establishment and encryption/integrity mechanisms.

### Diagram / Mental Model

```text
Client
 ↓ TLS handshake / certificate verification
Encrypted channel
 ↓
Server
```

### Why It Matters

HTTPS is HTTP carried over TLS, not a separate application concept.

# Part 72 — Key Management Awareness

### Core Explanation

Security of encryption depends heavily on how keys are generated, stored, rotated, authorized, backed up, and destroyed.

### Why It Matters

Strong algorithms with exposed keys provide little protection.

# Part 73 — Security Baseline

### Core Explanation

A security baseline defines approved minimum configuration for a class of system.

### Diagram / Mental Model

```text
Baseline:
patches
accounts
firewall
logging
time sync
services
backup
endpoint protection
```

### Why It Matters

Standard baselines reduce configuration drift and repeated mistakes.

# Part 74 — Hardening

### Core Explanation

Hardening reduces attack surface and strengthens configuration while preserving required functionality.

### Diagram / Mental Model

```text
inventory → remove unused → patch → restrict access → log → verify
```

### Why It Matters

Hardening is risk-based, not “disable everything.”

# Part 75 — Patching

### Core Explanation

Patching fixes known defects/vulnerabilities but must be controlled to reduce outage risk.

### Diagram / Mental Model

```text
inventory → assess → test → backup/rollback → deploy → verify
```

### Why It Matters

Never patching and blindly patching are both poor practices.

# Part 76 — Endpoint Protection Awareness

### Core Explanation

Endpoint controls can include antivirus/anti-malware, EDR, application control, host firewall, disk encryption, and telemetry.

### Why It Matters

Endpoint security provides prevention and detection but does not replace least privilege and patching.

# Part 77 — Host Firewall

### Core Explanation

Host firewalls restrict inbound/outbound network communication at the endpoint.

### Why It Matters

They provide a layer independent of perimeter/cloud controls.

# Part 78 — Secure Protocols

### Core Explanation

Prefer protocols that provide authentication and encryption where required, such as SSH and HTTPS/TLS rather than cleartext alternatives.

### Why It Matters

Network segmentation alone does not protect data traversing a compromised network.

# Part 79 — Network Firewall

### Core Explanation

Network firewalls enforce policy between network zones based on addresses, ports, protocols, connection state, and sometimes application context.

### Why It Matters

Rules should implement required flows, not broad convenience access.

# Part 80 — IDS / IPS Awareness

### Core Explanation

Intrusion Detection Systems identify suspicious traffic/activity; Intrusion Prevention Systems can additionally block according to policy.

### Why It Matters

Detection quality depends on visibility, tuning, and context.

# Part 81 — VPN Awareness

### Core Explanation

A VPN creates an encrypted/authenticated tunnel across an untrusted network to connect users or sites according to policy.

### Why It Matters

VPN access should still use strong identity and least privilege.

# Part 82 — Network Access Control Awareness

### Core Explanation

NAC systems evaluate devices/users before or during network access and may place them into appropriate segments.

### Why It Matters

Network presence alone should not imply unrestricted trust.

# Part 83 — Application Input Validation

### Core Explanation

Applications must validate data type, length, format, range, and business rules at trust boundaries.

### Diagram / Mental Model

```text
External input → validate → normalize if appropriate → business logic
```

### Why It Matters

Malformed input can cause reliability and security defects.

# Part 84 — Parameterized Queries

### Core Explanation

Database queries should bind untrusted values as parameters rather than concatenate them into SQL.

### Diagram / Mental Model

```text
SQL structure + bound data → DB driver
```

### Why It Matters

Separates data from SQL syntax and prevents injection through values.

# Part 85 — Object-Level Authorization

### Core Explanation

Applications must verify whether the current identity may access the specific requested object, not only whether they are logged in.

### Diagram / Mental Model

```text
User A authenticated
requests Order B
→ authorization check for Order B
```

### Why It Matters

Authentication alone does not prevent cross-user data access.

# Part 86 — Secret Management

### Core Explanation

Application secrets should be stored and delivered through controlled secret mechanisms, not hardcoded in source, images, or documentation.

### Why It Matters

Source repositories preserve history and are widely accessible.

# Part 87 — Dependency / Supply-Chain Risk

### Core Explanation

Applications depend on third-party libraries, packages, build systems, vendors, and update channels that can introduce vulnerabilities or compromise.

### Diagram / Mental Model

```text
Developer → dependency registry → build → artifact → production
```

### Why It Matters

Security must cover the software supply chain, not only your own code.

# Part 88 — Cloud Shared Responsibility

### Core Explanation

Cloud providers secure underlying service layers; customers remain responsible for identities, configuration, data, workloads, and service-specific controls according to the exact model.

### Why It Matters

Misconfigured cloud resources remain customer risk even on secure provider infrastructure.

# Part 89 — Cloud IAM Risk

### Core Explanation

Cloud administrative roles and access keys can control large portions of an environment, making identity compromise particularly high impact.

### Why It Matters

Use MFA, least privilege, service identities, and audit logs.

# Part 90 — Cloud Misconfiguration Risk

### Core Explanation

Public storage, broad firewall rules, overly permissive roles, disabled logs, and exposed secrets are common cloud risk scenarios.

### Why It Matters

Automated policy checks and secure templates reduce repeated errors.

# Part 91 — Social Engineering

### Core Explanation

Social engineering manipulates people into revealing information, performing actions, or bypassing normal controls.

### Why It Matters

Humans are part of the security system.

# Part 92 — Phishing

### Core Explanation

Phishing uses deceptive messages/sites to steal credentials, deliver malware, or persuade victims to take harmful actions.

### Diagram / Mental Model

```text
Message → urgency/trust cue → link/attachment/request → victim action
```

### Why It Matters

Technical controls and awareness both matter.

# Part 93 — Spear Phishing Awareness

### Core Explanation

Spear phishing is targeted phishing tailored to a particular person, role, or organization.

### Why It Matters

Personalized context can make attacks more convincing.

# Part 94 — Credential Stuffing Awareness

### Core Explanation

Credential stuffing uses username/password pairs leaked from one service against other services where users reused credentials.

### Why It Matters

Unique passwords and MFA reduce impact.

# Part 95 — Password Spraying Awareness

### Core Explanation

Password spraying tries a small number of common passwords across many accounts to avoid lockouts. This is a conceptual threat description only.

### Why It Matters

Strong passwords, MFA, rate controls, and detection help mitigate it.

# Part 96 — Malware

### Core Explanation

Malware is malicious software designed to disrupt, spy, gain access, persist, or manipulate systems.

### Why It Matters

Malware is a category containing many behaviors rather than one technology.

# Part 97 — Virus Awareness

### Core Explanation

A virus typically attaches to other files/programs and spreads when infected content executes.

# Part 98 — Worm Awareness

### Core Explanation

A worm can self-propagate across systems/networks by exploiting weaknesses or abusing trust.

### Why It Matters

Rapid patching and segmentation limit propagation.

# Part 99 — Trojan Awareness

### Core Explanation

A trojan disguises malicious behavior as legitimate software/content.

### Why It Matters

Trusted software sources and application control reduce risk.

# Part 100 — Ransomware

### Core Explanation

Ransomware aims to deny access to data/systems, often by encryption or disruption, and may combine data theft with extortion.

### Diagram / Mental Model

```text
Initial access → privilege/lateral movement → impact → extortion
```

### Why It Matters

Defense requires identity protection, segmentation, hardening, monitoring, and protected backups.

# Part 101 — Exploitation of Vulnerabilities

### Core Explanation

Attackers may use known or unknown software weaknesses to execute unauthorized actions.

### Why It Matters

Asset inventory and timely risk-based remediation are foundational controls.

# Part 102 — Denial of Service

### Core Explanation

DoS attempts to exhaust capacity or disrupt availability. Distributed DoS uses many sources.

### Why It Matters

Availability is part of security; resilience and provider protections may be required.

# Part 103 — Insider Risk

### Core Explanation

Insider risk may be malicious or accidental and comes from authorized access being misused or mishandled.

### Why It Matters

Least privilege, separation of duties, monitoring, and good process reduce risk without assuming every insider is malicious.

# Part 104 — Supply-Chain Compromise

### Core Explanation

A trusted supplier, package, build system, software update, or service can become a path to downstream customers.

### Why It Matters

Trust relationships must be governed and monitored.

# Part 105 — Asset Inventory for Vulnerability Management

### Core Explanation

Vulnerability management begins with knowing what systems, software, services, and owners exist.

### Why It Matters

A scanner cannot protect an unknown or unmanaged asset.

# Part 106 — Vulnerability Identification

### Core Explanation

Weaknesses may be identified through vendor advisories, authenticated scanning, configuration assessment, code analysis, penetration testing, or incident findings.

### Why It Matters

No single detection method finds every class of weakness.

# Part 107 — Risk-Based Prioritization

### Core Explanation

Prioritize vulnerabilities using severity plus exposure, exploitability evidence, asset criticality, compensating controls, and business context.

### Diagram / Mental Model

```text
CVSS/severity signal
+ Internet exposure
+ critical asset
+ known exploitation
+ controls
→ remediation priority
```

### Why It Matters

A raw severity score is not the same as business risk.

# Part 108 — Remediation

### Core Explanation

Remediation removes the root weakness through patching, configuration change, code fix, upgrade, or decommissioning.

# Part 109 — Mitigation

### Core Explanation

Mitigation reduces risk without fully removing the vulnerability, for example isolating a service or applying a virtual-patching control until upgrade is possible.

### Why It Matters

Mitigation may be temporary and should be tracked.

# Part 110 — Verification

### Core Explanation

After remediation, verify that the vulnerability/exposure is actually gone and the system still functions.

### Why It Matters

Change completion is evidence, not assumption.

# Part 111 — Exception / Risk Acceptance

### Core Explanation

If remediation cannot occur immediately, document owner, justification, compensating controls, expiration, and review.

### Why It Matters

Permanent undocumented exceptions become hidden risk.

# Part 112 — Threat Modeling

### Core Explanation

Threat modeling systematically analyzes assets, trust boundaries, entry points, threat scenarios, and mitigations during design.

### Diagram / Mental Model

```text
System diagram
 ↓
assets + trust boundaries
 ↓
threat scenarios
 ↓
controls/tests
```

### Why It Matters

Finding design weaknesses before deployment is cheaper than incident response.

# Part 113 — Trust Boundary

### Core Explanation

A trust boundary is a point where identity, privilege, data sensitivity, or control assumptions change.

### Diagram / Mental Model

```text
Internet | boundary | Web App | boundary | Database
```

### Why It Matters

Validate/authenticate/authorize when crossing boundaries.

# Part 114 — Attack Path Thinking

### Core Explanation

An attack path is a sequence of weaknesses/permissions that could let a threat move from initial access to a valuable asset.

### Diagram / Mental Model

```text
Phished user
 ↓
VPN access
 ↓
overprivileged share
 ↓
admin credential
 ↓
critical server
```

### Why It Matters

Defensive teams can break paths at multiple points with layered controls.

# Part 115 — Security Logging

### Core Explanation

Security-relevant logs should capture identity, action, resource, time, source, result, and context where appropriate.

### Diagram / Mental Model

```text
who + what + where + when + result
```

### Why It Matters

Logs enable detection and investigation.

# Part 116 — Time Synchronization Awareness

### Core Explanation

Accurate synchronized clocks allow events from different systems to be correlated.

### Why It Matters

Without consistent time, incident timelines become unreliable.

# Part 117 — Log Protection

### Core Explanation

Logs should be access-controlled, retained, backed up or centralized as required, and protected from easy tampering/deletion.

### Why It Matters

Attackers may attempt to erase evidence.

# Part 118 — Security Baseline Monitoring

### Core Explanation

A baseline describes expected users, services, ports, software, traffic, and behavior. Detection looks for meaningful deviations.

### Diagram / Mental Model

```text
Normal state → deviation → investigate
```

### Why It Matters

Without context, every event appears equally suspicious.

# Part 119 — SIEM Awareness

### Core Explanation

A Security Information and Event Management platform centralizes and analyzes logs/events and supports correlation, searches, alerts, and investigation workflows.

### Diagram / Mental Model

```text
Endpoints
Network
Cloud
Apps
Identity
  ↓
 SIEM
  ↓
Detection / Investigation
```

### Why It Matters

SIEM is a visibility platform, not an automatic guarantee of security.

# Part 120 — Alert

### Core Explanation

An alert is a rule/model-generated signal that something may require attention.

### Why It Matters

Alerts need triage; false positives and false negatives exist.

# Part 121 — Triage

### Core Explanation

Triage evaluates alert context, severity, scope, evidence, and whether escalation is required.

### Why It Matters

Efficient triage prevents analysts from treating every event as an incident.

# Part 122 — Incident Response Lifecycle

### Core Explanation

A foundational lifecycle is preparation, detection/identification, containment, eradication/remediation, recovery, and lessons learned.

### Diagram / Mental Model

```text
Prepare → Detect → Contain → Eradicate → Recover → Learn
```

### Why It Matters

Response succeeds when procedures and evidence sources exist before the incident.

# Part 123 — Containment

### Core Explanation

Containment limits ongoing damage while preserving enough evidence and business function.

### Diagram / Mental Model

```text
isolate account/host/network path
without unnecessary destruction of evidence
```

### Why It Matters

Immediate destructive actions can erase evidence or cause wider outage.

# Part 124 — Eradication / Remediation

### Core Explanation

Remove the root cause such as malicious persistence, compromised credentials, vulnerable software, or unsafe configuration.

# Part 125 — Recovery

### Core Explanation

Restore systems to trusted operation, monitor for recurrence, and validate business function.

### Why It Matters

Restoring service too early can reintroduce the threat.

# Part 126 — Lessons Learned

### Core Explanation

After response, identify root causes, control gaps, detection gaps, process weaknesses, and tracked corrective actions.

### Why It Matters

Incidents should improve the system.

# Part 127 — Evidence Preservation Awareness

### Core Explanation

Preserve logs, timestamps, volatile data, relevant files, and chain-of-custody practices when incidents may require forensic/legal review.

### Why It Matters

Do not alter evidence unnecessarily.

# Part 128 — Business Continuity

### Core Explanation

Business continuity keeps critical business processes operating at acceptable levels during disruption.

### Why It Matters

It is broader than restoring IT systems.

# Part 129 — Disaster Recovery

### Core Explanation

Disaster recovery restores technology services and data after major disruption.

### Why It Matters

DR supports business continuity.

# Part 130 — RPO

### Core Explanation

Recovery Point Objective is maximum acceptable data loss in time.

# Part 131 — RTO

### Core Explanation

Recovery Time Objective is maximum acceptable time to restore service.

# Part 132 — Backup Restore Testing

### Core Explanation

A backup is only useful if it can be restored within required RPO/RTO and with integrity.

### Why It Matters

Test restores, not only backup-job success.

# Part 133 — Governance

### Core Explanation

Security governance sets accountability, objectives, risk direction, decision rights, and oversight.

### Why It Matters

Security controls need ownership and business alignment.

# Part 134 — Policy

### Core Explanation

A policy is a high-level mandatory statement of management intent.

### Example / Commands / Configuration

```text
All privileged accounts shall use approved MFA.
```

# Part 135 — Standard

### Core Explanation

A standard defines mandatory specific requirements that support policy.

### Example / Commands / Configuration

```text
Privileged passwords must follow defined length/manager rules; approved MFA methods X/Y.
```

# Part 136 — Procedure

### Core Explanation

A procedure gives step-by-step instructions for performing a task.

### Example / Commands / Configuration

```text
How to onboard a privileged administrator account.
```

# Part 137 — Guideline

### Core Explanation

A guideline provides recommended practices that allow informed flexibility.

### Why It Matters

Not every document has the same mandatory force.

# Part 138 — Exception Process

### Core Explanation

A formal exception records why a mandatory control cannot be met, risk owner, compensating controls, expiration, and review.

### Why It Matters

Exceptions should not silently become permanent architecture.

# Part 139 — Compliance Awareness

### Core Explanation

Compliance means satisfying applicable laws, regulations, contracts, or standards. Compliance can support security but does not guarantee security.

### Why It Matters

An organization can be compliant and still vulnerable.

# Part 140 — Security Awareness Training

### Core Explanation

Awareness helps users recognize phishing, protect credentials, report incidents, handle data, and follow safe processes.

### Why It Matters

Human behavior is part of the control environment.

# Part 141 — Security Culture

### Core Explanation

A healthy security culture makes safe behavior practical, encourages reporting, and avoids punishing honest mistakes in ways that drive incidents underground.

### Why It Matters

Controls work better when users understand purpose and can report problems safely.

# Part 142 — NIST CSF 2.0 — Govern

### Core Explanation

Govern establishes cybersecurity strategy, expectations, roles, policy, oversight, and risk-management context.

# Part 143 — NIST CSF 2.0 — Identify

### Core Explanation

Identify develops understanding of assets, risks, dependencies, and current cybersecurity posture.

# Part 144 — NIST CSF 2.0 — Protect

### Core Explanation

Protect implements safeguards such as identity, training, data security, platform security, and resilience.

# Part 145 — NIST CSF 2.0 — Detect

### Core Explanation

Detect identifies possible cybersecurity attacks and compromises through monitoring and analysis.

# Part 146 — NIST CSF 2.0 — Respond

### Core Explanation

Respond contains, communicates, analyzes, and mitigates detected incidents.

# Part 147 — NIST CSF 2.0 — Recover

### Core Explanation

Recover restores assets/operations and improves resilience after incidents.

# Part 148 — Ethics and Authorization Boundary

### Core Explanation

Security work must be performed only with explicit authorization and within approved scope. Curiosity does not create permission.

### Diagram / Mental Model

```text
Authorized lab → inspect/test safely
Third-party system without permission → do not probe/exploit
```

### Why It Matters

Ethical and legal boundaries are foundational professional requirements.

# Part 149 — Final Cybersecurity Mental Model

### Core Explanation

Cybersecurity is a continuous cycle of understanding assets and business needs, assessing threats and vulnerabilities, applying controls, detecting failures, responding, recovering, and improving governance.

### Diagram / Mental Model

```text
Govern
 ↓
Identify assets/risk
 ↓
Protect
 ↓
Detect
 ↓
Respond
 ↓
Recover
 ↺ learn / improve
```

### Why It Matters

This model connects every later security specialization.

# 5. Hands-on Lab / Practical Exercises

## Lab 1 — Asset Inventory

Create at least 15 lab/home/synthetic assets with:
```text
asset ID
name
owner
purpose
location/environment
data classification
criticality
Internet exposure
backup status
```
Do not store credentials.

## Lab 2 — Asset Criticality

For each asset rate impact of:
```text
confidentiality loss
integrity loss
availability loss
```
Explain why a public web server and payroll database have different CIA profiles.

## Lab 3 — Threat Scenario Writing

Write 10 scenarios in the format:
```text
threat actor/source + action + asset + weakness/exposure + impact
```

## Lab 4 — Risk Register

For 10 scenarios record:
```text
likelihood
impact
inherent risk
existing controls
residual risk
treatment
owner
due date
```

## Lab 5 — Attack Surface Inventory

For one lab machine list:
```text
users
services
listening ports
installed software
remote admin interfaces
shared folders
cloud accounts/API keys awareness
```
Identify what is required vs unnecessary.

## Lab 6 — Listening Services Review

Windows:
```powershell
Get-NetTCPConnection -State Listen | Sort-Object LocalPort
```
Linux:
```bash
ss -tulpen
```
For each lab listener identify process, bind address, business need, and expected exposure. Do not disable unknown services until dependencies are understood.

## Lab 7 — Host Firewall Status

Windows:
```powershell
Get-NetFirewallProfile
```
Linux: inspect the firewall framework already installed, such as `ufw status verbose` or `firewall-cmd --state`. Do not create broad allow rules.

## Lab 8 — CIA Mapping

Choose:
```text
customer database
public website
source repository
backup system
```
Map top confidentiality/integrity/availability controls and trade-offs.

## Lab 9 — AAA Matrix

For a small application define:
```text
how users authenticate
what roles authorize
what actions are logged
```

## Lab 10 — MFA Factor Analysis

Classify examples into:
```text
something you know
something you have
something you are
```
Explain why password + PIN is not two-factor.

## Lab 11 — Least Privilege Matrix

Define roles:
```text
admin
developer
analyst
application service
database service
user
```
List required and prohibited permissions.

## Lab 12 — Identity Lifecycle

Design joiner/mover/leaver steps with approvals, provisioning, access review, offboarding, and evidence.

## Lab 13 — Separation of Duties

Design a production-change workflow where author, approver, and deployment mechanism are separated.

## Lab 14 — Defense in Depth Diagram

For a web app draw:
```text
Identity
Network
Host
Application
Data
Detection
Recovery
```
and map at least one control to each.

## Lab 15 — Control Classification

Classify 20 controls by:
```text
administrative / technical / physical
preventive / detective / corrective / recovery / deterrent / compensating
```
Some controls may fit multiple functional categories; explain why.

## Lab 16 — Data Classification

Create a four-level classification scheme and classify synthetic:
```text
marketing brochure
internal procedure
customer PII
password reset secret
source code
logs
backups
```

## Lab 17 — Data Lifecycle Mapping

For confidential customer data map:
```text
collect → process → share → store → backup → retain → destroy
```
Identify a control at every stage.

## Lab 18 — Integrity Hash Lab

Windows:
```powershell
Set-Content integrity-test.txt "baseline configuration"
Get-FileHash integrity-test.txt -Algorithm SHA256
```
Linux:
```bash
echo "baseline configuration" > integrity-test.txt
sha256sum integrity-test.txt
```
Modify the file and compare hashes. Explain why the hash detects change but does not identify who changed it.

## Lab 19 — Hash vs Encryption Concept

Create a comparison table covering:
```text
reversible?
uses key?
purpose
password storage fit
data confidentiality fit
```

## Lab 20 — TLS Inspection Awareness

On an authorized website you own or a public documentation site, use your browser certificate viewer to inspect:
```text
subject/name
issuer
validity
certificate chain
```
Do not attempt interception or bypass.

## Lab 21 — Security Baseline

Create a baseline checklist for Windows/Linux lab:
```text
patches
accounts
admin rights
services
firewall
logging
time sync
disk encryption awareness
backup
endpoint protection
```

## Lab 22 — Patching Workflow

Design:
```text
inventory → advisory → prioritize → test → backup/rollback → deploy → verify → document
```
for a critical server.

## Lab 23 — Network Segmentation Design

Design:
```text
Users VLAN/subnet
App subnet
DB subnet
Management subnet
Guest network
```
Specify only required flows.

## Lab 24 — Secure Protocol Review

For each pair explain the secure preference and why:
```text
HTTP vs HTTPS
Telnet vs SSH
FTP vs secure transfer alternatives awareness
```

## Lab 25 — Application Trust Boundaries

Draw browser → web app → API → database. Mark where authentication, validation, authorization, TLS, and logging occur.

## Lab 26 — SQL Parameterization Review

Compare:
```python
# unsafe pattern
query = "SELECT * FROM users WHERE name='" + name + "'"

# conceptual safe pattern
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```
Explain structurally why binding data is safer. Placeholder syntax varies by driver.

## Lab 27 — Secrets Review

Create a synthetic project and identify places secrets must not be stored:
```text
Git
Docker image
README
logs
plain config
chat screenshots
```
Design a secret-delivery approach conceptually.

## Lab 28 — Cloud Shared Responsibility Matrix

For IaaS/PaaS/SaaS map responsibility for:
```text
physical facility
hypervisor
OS patching
application code
identities
data classification
network configuration
backup settings
```

## Lab 29 — Threat Modeling

For the Server Health application identify:
```text
assets
entry points
trust boundaries
threat scenarios
controls
security tests
```

## Lab 30 — Vulnerability Prioritization

Given 8 synthetic findings, prioritize using:
```text
severity
Internet exposure
known exploitation awareness
asset criticality
privileges required
compensating controls
```
Do not rely on score alone.

## Lab 31 — Risk Exception

Write a temporary exception for a hypothetical application that cannot yet patch:
```text
owner
reason
residual risk
compensating controls
expiry
review date
```

## Lab 32 — Security Log Design

Define required event fields:
```text
timestamp
identity
source
action
resource
result
correlation ID
```
for login and admin-change events.

## Lab 33 — Baseline vs Anomaly

Create a normal baseline for:
```text
login times
admin accounts
listening ports
services
network destinations
```
Then write five deviations that should trigger investigation.

## Lab 34 — SIEM Data-Source Map

Draw:
```text
Endpoint logs
Firewall
Identity
Cloud audit
Application
Database
    ↓
   SIEM
    ↓
Alerts / Investigation
```

## Lab 35 — Incident Runbook — Credential Compromise

Write one-page steps:
```text
validate signal
contain account/session
reset/rotate credentials
review MFA/recovery
search activity
assess affected assets
recover
monitor
document
```
Avoid destroying evidence before scope is understood.

## Lab 36 — Backup and Recovery Exercise

For a critical database define:
```text
backup frequency
RPO
RTO
offline/isolated copy awareness
restore test schedule
access control
```

## Lab 37 — Governance Document Mapping

For these examples decide whether each is policy, standard, procedure, or guideline and explain why.

## Lab 38 — NIST CSF Mapping

Map your asset inventory, hardening, monitoring, incident plan, and backup plan to Govern, Identify, Protect, Detect, Respond, Recover.

## Lab 39 — Security Awareness Scenario

Design a 10-minute awareness lesson for phishing that includes cues, safe response, reporting path, and one knowledge check.

## Lab 40 — Final Security Baseline Review

Review the capstone environment against:
```text
assets
risk
identity
network
host
application
data
logging
response
recovery
governance
```

# 6. Mini Project

## Mini Project — Security Baseline for a Small Cloud-Ready Application

Assume the environment contains:

```text
Administrator Laptop
       ↓
Internet / VPN / Management Path
       ↓
Application Server / Cloud Workload
       ↓
Database
       ↓
Backup / Recovery Storage
```

It also includes:

```text
Human users
Developer accounts
Application service identity
Cloud/admin identity
Source repository
CI/CD awareness
Logs / monitoring
DNS / TLS certificate
```

### Required Project Structure

```text
security-baseline-project/
├── README.md
├── asset-inventory.md
├── data-classification.md
├── architecture.md
├── trust-boundaries.md
├── threat-model.md
├── risk-register.md
├── access-control-matrix.md
├── hardening-baseline.md
├── network-flow-matrix.md
├── cryptography-and-secrets.md
├── vulnerability-management.md
├── logging-and-monitoring.md
├── incident-response-runbook.md
├── backup-and-recovery.md
├── governance-map.md
└── nist-csf-map.md
```

### 1. Asset Inventory

At least 15 assets with:

```text
ID
owner
purpose
criticality
classification
Internet exposure
backup requirement
```

### 2. Data Classification

Define a classification scheme and apply it to:

```text
customer records
credentials
source code
logs
backups
public website content
configuration
```

### 3. Threat Model

Draw trust boundaries and write at least 15 threat scenarios.

Use the structure:

```text
Threat source
→ entry point
→ weakness/exposure
→ target asset
→ security impact
→ controls
```

### 4. Risk Register

For each scenario:

```text
likelihood
impact
inherent risk
existing controls
residual risk
treatment
owner
review date
```

### 5. Access Control Matrix

Roles:

```text
Administrator
Developer
Operations Analyst
Application Service
Database Service
End User
Auditor
```

Resources:

```text
source repository
production app
production DB
backups
logs
cloud control plane
secrets
```

Apply least privilege, need-to-know, and separation of duties.

### 6. Hardening Baseline

At minimum:

```text
supported OS/runtime
patching
minimal services
host firewall
MFA
admin separation
secure protocols
logging
time synchronization
endpoint protection awareness
backup
secure defaults
```

### 7. Network Flow Matrix

Document:

```text
source
destination
protocol
port/service
business justification
control
```

Everything not justified should be denied by design.

### 8. Cryptography and Secrets

Explain use of:

```text
TLS for data in transit
storage encryption where required
password hashing for credentials
hashes for integrity
secret manager/workload identity awareness
certificate lifecycle
key-management ownership
```

### 9. Vulnerability Management

Create the lifecycle:

```text
Inventory
 ↓
Identify
 ↓
Prioritize by risk
 ↓
Remediate / Mitigate
 ↓
Verify
 ↓
Track exceptions
```

### 10. Logging and Monitoring

Required sources:

```text
OS
Application
Identity
Cloud audit
Firewall/network
Database security events awareness
```

Define at least 10 detection ideas such as:

```text
privileged login from unusual source
MFA disabled
new admin role assignment
unexpected public network rule
repeated authentication failures
logging disabled
backup failure
critical service stopped
```

### 11. Incident Runbook

Create a one-page response plan for **suspected privileged credential compromise**:

```text
validate
contain
preserve evidence
rotate/revoke
scope
remediate
recover
monitor
communicate
lessons learned
```

### 12. Backup and Recovery

Define:

```text
RPO
RTO
backup frequency
retention
access control
isolation
restore-test frequency
```

### 13. NIST CSF Mapping

Map major controls to:

```text
Govern
Identify
Protect
Detect
Respond
Recover
```

### Final Review Questions

You should be able to answer:

```text
What are we protecting?
From what?
Why does it matter?
Which weaknesses/exposures make the scenario possible?
Which controls prevent it?
Which controls detect failure?
How do we respond?
How do we recover?
Who owns residual risk?
```

# 7. Recommended Resources

This enhanced Markdown is designed to be self-contained for the Phase 1 security foundation.

Optional authoritative references:

```text
NIST Cybersecurity Framework 2.0
CISA cybersecurity best-practice material
NIST publications on risk, identity, incident response, and controls as needed later
vendor security-baseline documentation for the systems you actually use
```

Later phases deepen network security, penetration testing, SOC, incident response, forensics, GRC, cloud security, and DevSecOps. Do not use later offensive tooling outside explicit authorization.

# 8. Certification Relevance

Direct foundation for:

```text
Phase 20 — Cybersecurity Fundamentals
Network Security
Security Assessment
Ethical Hacking
SOC / SIEM
Incident Response
Forensics
GRC
Cloud Security
DevSecOps
OT Security
```

It also supports infrastructure and cloud certifications because identity, patching, network exposure, backups, logging, and least privilege are universal operational concerns.

# 9. Common Mistakes & Best Practices

- **Mistake:** Thinking cybersecurity means installing antivirus.  
  **Best practice:** Use risk management plus identity, hardening, network, application, monitoring, response, and recovery controls.
- **Mistake:** Starting with tools before identifying assets and risks.  
  **Best practice:** Inventory assets, owners, criticality, data, and threat scenarios first.
- **Mistake:** Treating vulnerability severity as business risk.  
  **Best practice:** Include exposure, asset criticality, exploitation evidence, and controls.
- **Mistake:** Confusing authentication and authorization.  
  **Best practice:** Authenticate identity, then separately authorize each resource/action.
- **Mistake:** Using shared administrator accounts.  
  **Best practice:** Use named accounts and protected audit trails.
- **Mistake:** Using password + PIN and calling it MFA.  
  **Best practice:** Use factors from different categories.
- **Mistake:** Giving permanent administrator rights for convenience.  
  **Best practice:** Use least privilege and time-bound elevation where feasible.
- **Mistake:** Trusting internal network location automatically.  
  **Best practice:** Verify identity and authorization; segment by trust and purpose.
- **Mistake:** Relying on one control.  
  **Best practice:** Use defense in depth.
- **Mistake:** Keeping unnecessary services enabled.  
  **Best practice:** Minimize attack surface after dependency review.
- **Mistake:** Using `= NULL`-style conceptual mistakes in security data handling?  
  **Best practice:** Model missing/unknown values carefully and validate data semantics.
- **Mistake:** Storing passwords/API keys in source or docs.  
  **Best practice:** Use secret-management mechanisms and rotate leaked secrets.
- **Mistake:** Using general-purpose fast hashes to store passwords.  
  **Best practice:** Use dedicated salted password-hashing functions.
- **Mistake:** Calling hashing encryption.  
  **Best practice:** Hashing is one-way integrity/verifier functionality; encryption is reversible with keys.
- **Mistake:** Blocking all ICMP/ICMPv6 or all security telemetry blindly.  
  **Best practice:** Understand protocol/visibility requirements before applying restrictive controls.
- **Mistake:** Patching production without testing/recovery or never patching.  
  **Best practice:** Use a risk-based controlled patch lifecycle.
- **Mistake:** Opening firewall rules broadly to troubleshoot.  
  **Best practice:** Test specific required flows and keep default-deny posture.
- **Mistake:** Logging everything including secrets.  
  **Best practice:** Collect useful security context while minimizing sensitive values.
- **Mistake:** Treating every alert as an incident.  
  **Best practice:** Triage using context, baseline, evidence, and impact.
- **Mistake:** Destroying evidence during containment.  
  **Best practice:** Contain proportionately while preserving investigation evidence.
- **Mistake:** Assuming backup job success means recovery works.  
  **Best practice:** Test restores against RPO/RTO.
- **Mistake:** Assuming cloud provider owns all security.  
  **Best practice:** Apply the exact shared-responsibility model.
- **Mistake:** Keeping risk exceptions indefinitely.  
  **Best practice:** Assign owner, compensating controls, expiry, and review.
- **Mistake:** Treating compliance as proof of security.  
  **Best practice:** Use compliance as one governance input, not the final security outcome.
- **Mistake:** Running security tests against systems without permission.  
  **Best practice:** Operate only within explicit authorization and defined scope.

# 10. Self-Assessment Questions (with short answers)

1. **What is cybersecurity?**  
   Management of risk to information, identities, systems, networks, applications, and business operations.

2. **What is an asset?**  
   Something of value requiring protection.

3. **What is a threat?**  
   Potential cause of harm.

4. **What is a threat actor?**  
   Entity intentionally attempting to cause harm or unauthorized access.

5. **What is a vulnerability?**  
   Weakness that can be exploited or triggered.

6. **What is exposure?**  
   How reachable/accessibile an asset or weakness is to a threat.

7. **What is attack surface?**  
   Set of accessible interfaces, identities, services, software, and paths that could be abused.

8. **Event vs incident?**  
   An event is an occurrence; an incident is a security-impacting event requiring response.

9. **What is likelihood?**  
   Estimated probability of a risk scenario.

10. **What is impact?**  
   Consequence if the scenario occurs.

11. **What is risk?**  
   Combination of likelihood and impact for a defined scenario.

12. **Inherent vs residual risk?**  
   Risk before controls vs risk remaining after controls.

13. **Common risk treatments?**  
   Mitigate, avoid, transfer/share, accept.

14. **Confidentiality?**  
   Prevent unauthorized disclosure.

15. **Integrity?**  
   Protect accuracy and authorized state.

16. **Availability?**  
   Ensure authorized access when required.

17. **Authenticity?**  
   Confidence an identity/message/system is genuine.

18. **Accountability?**  
   Ability to associate actions with responsible identities/processes.

19. **Non-repudiation?**  
   Evidence supporting that an actor cannot plausibly deny a performed action.

20. **Authentication?**  
   Establish/verify identity.

21. **Authorization?**  
   Decide permitted actions/resources.

22. **Accounting/audit?**  
   Record actions and usage for traceability.

23. **What is MFA?**  
   Authentication using factors from different factor categories.

24. **Why are two passwords not MFA?**  
   Both are the same knowledge factor type.

25. **What is phishing-resistant MFA?**  
   Authentication methods designed to resist credential relay/phishing through cryptographic binding.

26. **Least privilege?**  
   Only minimum required permissions.

27. **Need-to-know?**  
   Access to information only when required for legitimate task.

28. **Separation of duties?**  
   Divide sensitive workflow responsibilities across identities/roles.

29. **PAM?**  
   Controls and monitors privileged administrative access.

30. **Identity lifecycle?**  
   Provision, change, review, and revoke access across join/move/leave stages.

31. **What is defense in depth?**  
   Multiple independent layers of protection.

32. **Administrative control?**  
   Policy/process/training/risk-management safeguard.

33. **Technical control?**  
   Logical/technology safeguard such as MFA/firewall/encryption.

34. **Physical control?**  
   Facility/hardware safeguard such as locks/guards/CCTV.

35. **Preventive control?**  
   Attempts to stop an event.

36. **Detective control?**  
   Identifies an event.

37. **Corrective control?**  
   Fixes/reduces harm after detection.

38. **Recovery control?**  
   Restores systems/data after disruption.

39. **Compensating control?**  
   Alternative safeguard when preferred control is unavailable.

40. **Secure by default?**  
   Default configuration favors safer behavior.

41. **What is attack-surface minimization?**  
   Remove unnecessary services, privileges, interfaces, and software.

42. **Segmentation?**  
   Divide systems by trust/function and control communication.

43. **Zero Trust concept?**  
   Do not grant trust solely based on network location; verify identity/context and authorize resources explicitly.

44. **Data classification?**  
   Assign protection level based on sensitivity/value/impact.

45. **Data lifecycle?**  
   Create/collect, use, share, store, archive/retain, destroy.

46. **Data minimization?**  
   Collect and keep only what is necessary.

47. **Why is file deletion not always secure destruction?**  
   Deletion may remove references while copies remain on storage, backups, snapshots, or remapped media.

48. **What does a cryptographic hash do?**  
   Produces fixed-size digest used for integrity/verifier purposes.

49. **Hash vs encryption?**  
   Hash is designed one-way; encryption is reversible with key.

50. **Symmetric encryption?**  
   Same shared secret used for encryption/decryption.

51. **Asymmetric cryptography?**  
   Uses public/private key pair for suitable operations.

52. **Digital signature?**  
   Private-key operation verifiable with public key to support integrity/authenticity.

53. **Certificate?**  
   Binds public key to identity under a trust model.

54. **TLS?**  
   Protocol protecting network sessions using authenticated key establishment and encryption/integrity.

55. **Why does key management matter?**  
   Exposed or poorly managed keys defeat strong cryptography.

56. **What is hardening?**  
   Reduce attack surface and strengthen configuration while preserving required function.

57. **Why patch?**  
   Remove known defects/vulnerabilities under controlled change.

58. **What is EDR awareness?**  
   Endpoint detection/response tooling that monitors and supports investigation/response on endpoints.

59. **What does a firewall do?**  
   Enforces network communication policy.

60. **IDS vs IPS?**  
   IDS detects; IPS may also block/prevent according to policy.

61. **VPN?**  
   Encrypted/authenticated tunnel across an untrusted network.

62. **Why validate application input?**  
   External data can violate assumptions and create security/reliability defects.

63. **Why parameterized SQL?**  
   Keeps untrusted values separate from SQL syntax.

64. **Object-level authorization?**  
   Verify user may access the specific requested object.

65. **Why not hardcode secrets?**  
   They can leak through source history, images, logs, or sharing.

66. **Supply-chain risk?**  
   Risk introduced through suppliers, dependencies, build/update systems, and services.

67. **Cloud shared responsibility?**  
   Provider/customer security duties vary by service and configuration.

68. **Phishing?**  
   Deceptive communication intended to steal credentials, deliver malware, or induce harmful actions.

69. **Credential stuffing?**  
   Reuse of breached credential pairs against other services.

70. **Ransomware?**  
   Malware/extortion activity designed to deny access and often steal data.

71. **Insider risk?**  
   Risk from authorized people misusing or accidentally mishandling access.

72. **Vulnerability management cycle?**  
   Inventory → identify → prioritize → remediate/mitigate → verify → track exceptions.

73. **Why severity is not risk?**  
   Risk also depends on exposure, asset value, exploitability, and controls.

74. **What is threat modeling?**  
   Design-time analysis of assets, trust boundaries, threats, and controls.

75. **What is a trust boundary?**  
   Point where identity/privilege/data/control assumptions change.

76. **What is an attack path?**  
   Sequence of weaknesses/permissions leading from entry point to valuable asset.

77. **What should security logs answer?**  
   Who did what, where/from where, when, to which resource, and with what result.

78. **Why time synchronization?**  
   Allows reliable cross-system event correlation.

79. **What is a SIEM?**  
   Platform centralizing/analyzing security logs/events for search, correlation, alerts, and investigation.

80. **What is triage?**  
   Evaluate alert context, evidence, severity, scope, and escalation need.

81. **Incident-response stages?**  
   Preparation, detection/identification, containment, eradication/remediation, recovery, lessons learned.

82. **Why preserve evidence?**  
   For reliable investigation, timeline reconstruction, and possible legal/forensic needs.

83. **Business continuity vs DR?**  
   BC keeps critical business processes operating; DR restores technology/data.

84. **RPO?**  
   Maximum acceptable data loss in time.

85. **RTO?**  
   Maximum acceptable recovery time.

86. **Policy?**  
   High-level mandatory management intent.

87. **Standard?**  
   Specific mandatory requirement supporting policy.

88. **Procedure?**  
   Step-by-step instructions.

89. **Guideline?**  
   Recommended practice with flexibility.

90. **Compliance vs security?**  
   Compliance meets specified obligations; it does not guarantee adequate security.

91. **NIST CSF 2.0 Functions?**  
   Govern, Identify, Protect, Detect, Respond, Recover.

92. **Most important authorization rule for security labs?**  
   Use only systems/accounts/resources you own or are explicitly authorized to test/administer.

93. **Final cybersecurity mental model?**  
   Govern and identify risk, protect assets, detect failures, respond, recover, and continuously improve.

