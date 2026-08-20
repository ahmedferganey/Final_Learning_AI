# 94. Active Directory Penetration Testing

> Phase 22 — Penetration Testing

This course is **lab-first, authorization-first, and evidence-driven**. The material is designed for deliberately vulnerable applications, owned devices/emulators, disposable AD domains, or other systems explicitly covered by written authorization.

---

## 1. Topic Title

**Active Directory Penetration Testing**

---

## 2. Learning Objectives

- Model AD forests, domains, users, groups, computers, GPOs, ACLs, trusts, and authentication.
- Use PowerShell and authorized directory queries to build an identity/privilege inventory.
- Assess privileged groups, service accounts, password policy, LAPS/gMSA, and admin tiering.
- Understand Kerberos, NTLM, SPNs, delegation, SMB/LDAP signing, and trust security.
- Review AD object permissions and identify dangerous control relationships.
- Use graph-based path analysis such as BloodHound conceptually and in isolated labs.
- Understand common AD credential/privilege attack classes and their defenses without using real-user credentials.
- Validate one synthetic privilege path in a disposable lab.
- Correlate directory tests with Windows/EDR/SIEM telemetry.
- Clean up directory changes, remediate root causes, and retest.

---

## 3. Prerequisites

Required:

```text
90 Ethical Hacking and Security Assessment
88 Network Penetration Testing
Microsoft Active Directory Administration
Windows Server
PowerShell
DNS
Kerberos/NTLM foundation
SMB / Windows networking
```

Recommended lab:

```text
1-2 domain controllers
2 Windows member hosts
1 admin workstation
synthetic users/groups/service accounts
isolated virtual network
snapshots
```

Do not practice AD attack techniques against real organizational domains without explicit written authorization.

---

## 4. Core Concepts Explanation

# Part 1 — Active Directory Penetration Testing Purpose

### Core Explanation

Active Directory penetration testing validates whether identity, authentication, directory permissions, delegation, endpoint privilege, and network relationships create unauthorized privilege paths in an authorized lab or test domain.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 2 — AD Authorization

### Core Explanation

Written authorization should identify domains, forests, domain controllers, accounts, hosts, techniques, and lockout-safe credential rules.

### Diagram / Code / Command Example

```text
Written authorization
   ↓
Lab/test domain
   ↓
approved accounts
   ↓
approved hosts
   ↓
allowed identity techniques
   ↓
lockout-safe test plan
   ↓
cleanup / reset
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

# Part 3 — AD Rules of Engagement

### Core Explanation

Define account lockout protections, service-impact limits, password-testing restrictions, replication-sensitive systems, and cleanup.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 4 — AD Lab Design

### Core Explanation

Build a disposable Windows Server domain with synthetic users, groups, service accounts, workstations, and intentionally weak permissions.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 5 — Snapshot Strategy

### Core Explanation

Snapshot domain controllers and member servers before privilege-path labs so the directory can be restored.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 6 — Forest

### Core Explanation

A forest is the highest AD DS security/administrative boundary containing one or more domains that share schema and configuration.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 7 — Domain

### Core Explanation

A domain contains directory objects, policies, authentication services, and domain controllers under one namespace.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 8 — Domain Controller

### Core Explanation

Domain controllers host AD DS, perform authentication, and replicate directory data.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 9 — OU

### Core Explanation

Organizational Units organize objects and provide delegation and Group Policy scope.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 10 — User Object

### Core Explanation

User objects represent human or service identities and have group memberships, attributes, credentials, and permissions.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 11 — Computer Object

### Core Explanation

Computer accounts represent domain-joined systems and participate in Kerberos and directory authorization.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 12 — Group

### Core Explanation

Groups aggregate security principals for authorization and administration.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 13 — Security Group

### Core Explanation

Security groups can be included in access-control lists and privilege assignments.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 14 — Distribution Group Awareness

### Core Explanation

Distribution groups are primarily for messaging and are not normally used as security principals.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 15 — Group Scope Awareness

### Core Explanation

Domain Local, Global, and Universal groups have different membership and resource-assignment semantics.

### Diagram / Code / Command Example

```text
Written authorization
   ↓
Lab/test domain
   ↓
approved accounts
   ↓
approved hosts
   ↓
allowed identity techniques
   ↓
lockout-safe test plan
   ↓
cleanup / reset
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

# Part 16 — Nested Group

### Core Explanation

Nested group membership can create indirect privilege that is easy to overlook.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 17 — Privileged Group

### Core Explanation

Groups such as Domain Admins or other delegated administrative groups need strict membership and monitoring.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 18 — Tiered Administration

### Core Explanation

Separate privileged admin identities and administrative workstations from normal user activity.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 19 — Joiner-Mover-Leaver in AD

### Core Explanation

User and group membership should change promptly with role or employment changes.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 20 — Stale Account

### Core Explanation

Disabled or unused accounts can retain privilege and should be reviewed.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 21 — Service Account

### Core Explanation

Service accounts require ownership, least privilege, noninteractive use where possible, and managed credentials.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 22 — gMSA

### Core Explanation

Group Managed Service Accounts provide automatically managed domain credentials to approved services/hosts.

### Diagram / Code / Command Example

```text
gMSA
  ↓
managed service identity
  ↓
domain-managed password rotation
  ↓
authorized hosts retrieve secret automatically
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

# Part 23 — LAPS

### Core Explanation

Managed local administrator passwords reduce reuse by providing unique automatically rotated local credentials.

### Diagram / Code / Command Example

```text
Managed local admin password solution:
unique per-device password
  ↓
directory stores protected secret
  ↓
access limited to authorized admins
  ↓
automatic rotation
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

# Part 24 — LDAP

### Core Explanation

LDAP is used to query and modify directory objects according to authentication and ACL permissions.

### Diagram / Code / Command Example

```powershell
# Own test domain / approved credentials
Get-ADDomain
Get-ADUser -Filter * -Properties Enabled |
  Select-Object SamAccountName, Enabled |
  Select-Object -First 10
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

# Part 25 — LDAP Signing

### Core Explanation

LDAP signing protects integrity of directory protocol traffic and reduces some relay/tampering risks.

### Diagram / Code / Command Example

```powershell
# Own test domain / approved credentials
Get-ADDomain
Get-ADUser -Filter * -Properties Enabled |
  Select-Object SamAccountName, Enabled |
  Select-Object -First 10
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

# Part 26 — LDAP Channel Binding Awareness

### Core Explanation

Channel binding helps tie authentication to the protected TLS channel where applicable.

### Diagram / Code / Command Example

```powershell
# Own test domain / approved credentials
Get-ADDomain
Get-ADUser -Filter * -Properties Enabled |
  Select-Object SamAccountName, Enabled |
  Select-Object -First 10
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

# Part 27 — Kerberos

### Core Explanation

Kerberos is the primary AD authentication protocol using tickets issued by the Key Distribution Center.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 28 — KDC

### Core Explanation

The KDC runs on domain controllers and provides ticket-granting and authentication services.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 29 — TGT

### Core Explanation

A Ticket Granting Ticket allows a client to request service tickets after successful authentication.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 30 — TGS

### Core Explanation

A service ticket authenticates a user/service context to a specific service principal.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 31 — SPN

### Core Explanation

Service Principal Names identify Kerberos-enabled service instances.

### Diagram / Code / Command Example

```powershell
Get-ADUser -Filter * -Properties ServicePrincipalName |
  Where-Object {$_.ServicePrincipalName} |
  Select-Object SamAccountName, ServicePrincipalName
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

# Part 32 — Kerberos Clock Dependency

### Core Explanation

Kerberos depends on synchronized time, making NTP and domain time hierarchy security-relevant.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 33 — NTLM

### Core Explanation

NTLM is legacy challenge-response authentication still used in some compatibility scenarios.

### Diagram / Code / Command Example

```text
NTLM is legacy challenge-response authentication.
Security review asks:
- where is it still required?
- can Kerberos replace it?
- are signing/channel protections enforced?
- is privileged admin use separated?
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

# Part 34 — NTLM Reduction

### Core Explanation

Reducing NTLM lowers exposure to relay and credential-theft classes but requires compatibility planning.

### Diagram / Code / Command Example

```text
NTLM is legacy challenge-response authentication.
Security review asks:
- where is it still required?
- can Kerberos replace it?
- are signing/channel protections enforced?
- is privileged admin use separated?
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

# Part 35 — SMB Signing

### Core Explanation

SMB signing protects integrity and helps reduce certain relay/tampering scenarios.

### Diagram / Code / Command Example

```text
Protocol hardening:
authenticate peer
  ↓
integrity protection / signing
  ↓
channel binding where supported
  ↓
reduce relay / tampering risk
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

# Part 36 — Extended Protection Awareness

### Core Explanation

Channel binding and service protections can reduce credential relay opportunities in supported services.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 37 — Password Policy

### Core Explanation

Review minimum length, history, age, complexity strategy, lockout, and compromised-password defenses.

### Diagram / Code / Command Example

```powershell
Get-ADDefaultDomainPasswordPolicy |
  Select-Object MinPasswordLength, LockoutThreshold, MaxPasswordAge
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

# Part 38 — Account Lockout

### Core Explanation

Lockout can slow password attacks but also creates denial-of-service risk and requires careful test planning.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 39 — Fine-Grained Password Policy

### Core Explanation

Different AD groups may receive different password/lockout policies through fine-grained policy objects.

### Diagram / Code / Command Example

```powershell
Get-ADDefaultDomainPasswordPolicy |
  Select-Object MinPasswordLength, LockoutThreshold, MaxPasswordAge
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

# Part 40 — Password Reuse

### Core Explanation

Reusing local or domain admin passwords across systems increases lateral-movement risk.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 41 — Credential Hygiene

### Core Explanation

Privileged credentials should not be used on lower-trust endpoints unnecessarily.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 42 — Cached Credential Awareness

### Core Explanation

Windows can cache logon information for offline use, which changes the impact of endpoint compromise.

### Diagram / Code / Command Example

```text
Credential defense review:
admin tiering
Credential Guard / protections
least privilege
no shared admin credentials
restricted interactive logon
EDR
patching

Course labs use synthetic accounts only.
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

# Part 43 — Credential Guard Awareness

### Core Explanation

Credential Guard uses virtualization-based security to protect selected secrets from normal OS access.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 44 — LSASS Protection Awareness

### Core Explanation

LSASS protections can reduce credential theft and should be combined with admin tiering and EDR.

### Diagram / Code / Command Example

```text
Credential defense review:
admin tiering
Credential Guard / protections
least privilege
no shared admin credentials
restricted interactive logon
EDR
patching

Course labs use synthetic accounts only.
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

# Part 45 — PowerShell for AD Assessment

### Core Explanation

PowerShell and the ActiveDirectory module provide authoritative directory queries in authorized environments.

### Diagram / Code / Command Example

```powershell
# Defensive/assessment example in own domain
Get-ADComputer -Filter * -Properties OperatingSystem |
  Select-Object Name, OperatingSystem |
  Select-Object -First 20
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

# Part 46 — Get-ADDomain

### Core Explanation

Get-ADDomain returns domain-level properties useful for inventory.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 47 — Get-ADForest

### Core Explanation

Get-ADForest returns forest structure and trust-related information.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 48 — Get-ADUser

### Core Explanation

Get-ADUser supports authorized inventory of users and security-relevant attributes.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 49 — Get-ADComputer

### Core Explanation

Get-ADComputer inventories domain-joined systems and operating-system metadata.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 50 — Get-ADGroup

### Core Explanation

Get-ADGroup inventories security groups and scope.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 51 — Get-ADGroupMember

### Core Explanation

Group membership queries reveal direct and nested privilege relationships.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 52 — Get-ADDefaultDomainPasswordPolicy

### Core Explanation

The default domain password policy provides baseline credential and lockout settings.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 53 — GPO

### Core Explanation

Group Policy centrally configures Windows systems and users and can create either strong security or broad privilege.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 54 — GPO Scope

### Core Explanation

GPO links, inheritance, security filtering, and WMI filtering determine where policy applies.

### Diagram / Code / Command Example

```text
Written authorization
   ↓
Lab/test domain
   ↓
approved accounts
   ↓
approved hosts
   ↓
allowed identity techniques
   ↓
lockout-safe test plan
   ↓
cleanup / reset
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

# Part 55 — GPO Modification Risk

### Core Explanation

A principal able to modify a GPO affecting privileged systems may gain broad control.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 56 — GPO Permission Review

### Core Explanation

Review which principals can edit, link, or take ownership of sensitive Group Policy objects.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 57 — SYSVOL

### Core Explanation

SYSVOL stores Group Policy and domain scripts replicated across domain controllers.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 58 — Logon Script Security

### Core Explanation

Scripts executed through Group Policy should not be writable by unprivileged users.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 59 — AD ACL

### Core Explanation

AD objects have ACLs that control read, write, ownership, inheritance, and extended rights.

### Diagram / Code / Command Example

```text
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

# Part 60 — ACE

### Core Explanation

Access Control Entries grant or deny rights to security principals.

### Diagram / Code / Command Example

```text
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

# Part 61 — Object Ownership

### Core Explanation

Owners can often modify permissions, making ownership a powerful control path.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 62 — GenericAll Awareness

### Core Explanation

Broad full-control permissions over privileged directory objects can create direct privilege paths.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 63 — GenericWrite Awareness

### Core Explanation

Broad write permission can permit security-sensitive attribute changes depending on the object.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 64 — WriteDACL Awareness

### Core Explanation

Permission to modify an object's DACL can allow the principal to grant itself additional rights.

### Diagram / Code / Command Example

```text
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

# Part 65 — WriteOwner Awareness

### Core Explanation

Permission to change ownership can enable later ACL modification.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 66 — Group Membership Write

### Core Explanation

Permission to add members to a privileged group is itself a high-risk privilege path.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 67 — User Attribute Write

### Core Explanation

Ability to modify sensitive user attributes can sometimes create identity or delegation impact.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 68 — Computer Object Control

### Core Explanation

Control over computer objects can affect authentication, delegation, and service relationships.

### Diagram / Code / Command Example

```text
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

# Part 69 — Delegation

### Core Explanation

Kerberos delegation allows services to act on behalf of users and requires careful scope.

### Diagram / Code / Command Example

```text
Delegation
  ↓
service acts on behalf of user
  ↓
scope must be tightly controlled
  ↓
review unconstrained / constrained / resource-based settings
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

# Part 70 — Unconstrained Delegation Awareness

### Core Explanation

Legacy unconstrained delegation creates broad ticket exposure and should be minimized.

### Diagram / Code / Command Example

```text
Delegation
  ↓
service acts on behalf of user
  ↓
scope must be tightly controlled
  ↓
review unconstrained / constrained / resource-based settings
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

# Part 71 — Constrained Delegation Awareness

### Core Explanation

Constrained delegation limits target services but still needs strict service-account governance.

### Diagram / Code / Command Example

```text
Delegation
  ↓
service acts on behalf of user
  ↓
scope must be tightly controlled
  ↓
review unconstrained / constrained / resource-based settings
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

# Part 72 — Resource-Based Constrained Delegation Awareness

### Core Explanation

Resource-based constrained delegation places delegation control on the destination resource and requires careful ACL review.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 73 — Trusted for Delegation Flag Review

### Core Explanation

Sensitive accounts should generally not be delegable where platform controls support protection.

### Diagram / Code / Command Example

```text
Delegation
  ↓
service acts on behalf of user
  ↓
scope must be tightly controlled
  ↓
review unconstrained / constrained / resource-based settings
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

# Part 74 — Protected Users Awareness

### Core Explanation

Protected Users group can reduce use of legacy authentication and credential caching for selected privileged identities.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 75 — AdminSDHolder Awareness

### Core Explanation

AD protects ACLs of many privileged accounts through AdminSDHolder/SDProp behavior; stale privileged membership can have long-term effects.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 76 — AdminCount Awareness

### Core Explanation

AdminCount can indicate past or present protected-group membership but is not by itself proof of current privilege.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 77 — Trust

### Core Explanation

Domain/forest trusts define authentication relationships across naming/security boundaries.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 78 — Trust Direction

### Core Explanation

Trust direction determines which side accepts authentication from the other and must be interpreted carefully.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 79 — Transitive Trust

### Core Explanation

Transitivity can extend trust relationships across domains and affect attack-path scope.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 80 — External Trust Awareness

### Core Explanation

External trusts connect separate domains with narrower trust characteristics.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 81 — Forest Trust Awareness

### Core Explanation

Forest trusts can enable authentication across forests and require explicit filtering/governance.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 82 — SID Filtering Awareness

### Core Explanation

SID filtering protects trust boundaries from some forged/foreign SID abuse and should be correctly configured.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 83 — DNS in AD

### Core Explanation

AD depends heavily on DNS service discovery and domain-controller location.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 84 — SRV Records

### Core Explanation

Kerberos, LDAP, and domain-controller services are discovered through DNS SRV records.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 85 — AD-Integrated DNS Security

### Core Explanation

Directory-integrated zones inherit AD permissions and should avoid unauthorized record modification.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 86 — Dynamic DNS Update

### Core Explanation

Secure dynamic updates help ensure only authorized principals modify relevant records.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 87 — SMB

### Core Explanation

SMB is used for file sharing, SYSVOL, management, and domain operations and therefore is a major AD security surface.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 88 — WinRM

### Core Explanation

Windows Remote Management enables administrative PowerShell remoting and should be restricted to approved admin paths.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 89 — RDP

### Core Explanation

Remote Desktop provides interactive access and should be restricted through admin segmentation, MFA/gateways, and monitoring.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 90 — Remote Registry Awareness

### Core Explanation

Remote registry access should be disabled or restricted when not operationally required.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 91 — Administrative Shares Awareness

### Core Explanation

Administrative shares support remote administration and can increase lateral-movement capability when admin credentials are compromised.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 92 — Local Administrator Group

### Core Explanation

Local admin membership on endpoints/servers should be minimized and managed centrally.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 93 — Local Admin Password Reuse

### Core Explanation

Reusing one local admin password across many hosts turns one compromise into a lateral-movement path.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 94 — Windows Firewall

### Core Explanation

Host firewalls should restrict administrative protocols even inside internal networks.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 95 — Endpoint Tiering

### Core Explanation

Domain controllers, servers, and workstations should have different administrative trust and credential exposure.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 96 — Privileged Access Workstation Awareness

### Core Explanation

Dedicated privileged workstations reduce exposure of high-value admin credentials.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 97 — BloodHound Awareness

### Core Explanation

BloodHound models AD relationships to identify potential privilege and attack paths from directory/session/ACL data.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 98 — Graph Relationship

### Core Explanation

Graph edges represent relationships such as group membership, local admin, ACL control, sessions, delegation, or remote access.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 99 — BloodHound Data Sensitivity

### Core Explanation

Collected directory relationship data is sensitive and should remain inside the authorized assessment environment.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 100 — Attack Path Hypothesis

### Core Explanation

A graph path indicates a possible relationship chain that still requires manual validation of prerequisites.

### Diagram / Code / Command Example

```text
Directory data
  ↓
relationship graph
  ↓
users / groups / sessions / ACLs / computers
  ↓
potential privilege paths
  ↓
manual validation
  ↓
remediation

Graph output is a hypothesis, not automatic proof.
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

# Part 101 — Shortest Path Risk

### Core Explanation

The shortest graph path is not automatically the most realistic attack path; operational context matters.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 102 — Privilege Path

### Core Explanation

A privilege path chains permissions, credentials, sessions, delegation, or host control into higher privilege.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 103 — Chained Misconfiguration

### Core Explanation

Several individually moderate AD weaknesses can combine into domain-level risk.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 104 — Kerberoasting Awareness

### Core Explanation

Service accounts with SPNs can expose offline password-guessing risk because service tickets are encrypted with service-account secrets; lab exercises should use synthetic weak accounts only.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 105 — Kerberoasting Defense

### Core Explanation

Use gMSA or long random service-account passwords, least privilege, service ownership, and monitoring.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 106 — AS-REP Roasting Awareness

### Core Explanation

Accounts configured without Kerberos preauthentication can expose offline password-guessing material and should be corrected.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 107 — AS-REP Roasting Defense

### Core Explanation

Require Kerberos preauthentication unless there is a documented compatibility exception.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 108 — Password Spraying Boundary

### Core Explanation

Password spraying against real users can cause lockouts and is not appropriate without explicit authorization and safeguards.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 109 — Synthetic Password Audit

### Core Explanation

Use synthetic lab accounts to demonstrate password policy and detection rather than real employee accounts.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 110 — NTLM Relay Awareness

### Core Explanation

If authentication can be induced and target services lack appropriate signing/channel protections, credentials may be relayed; hands-on relay should remain in dedicated isolated labs.

### Diagram / Code / Command Example

```text
NTLM is legacy challenge-response authentication.
Security review asks:
- where is it still required?
- can Kerberos replace it?
- are signing/channel protections enforced?
- is privileged admin use separated?
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

# Part 111 — NTLM Relay Defense

### Core Explanation

Reduce NTLM, require SMB/LDAP signing/channel binding where appropriate, segment admin protocols, and protect privileged credentials.

### Diagram / Code / Command Example

```text
NTLM is legacy challenge-response authentication.
Security review asks:
- where is it still required?
- can Kerberos replace it?
- are signing/channel protections enforced?
- is privileged admin use separated?
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

# Part 112 — Pass-the-Hash Awareness

### Core Explanation

Possession of an NTLM hash can sometimes authenticate without knowing the plaintext password; this illustrates why credential material is high-value.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 113 — Pass-the-Ticket Awareness

### Core Explanation

Stolen Kerberos tickets can be reused within their validity/context, emphasizing ticket and endpoint protection.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 114 — Credential Material Handling

### Core Explanation

Any password/hash/ticket generated in labs must be synthetic and treated as sensitive evidence.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 115 — DCSync Awareness

### Core Explanation

Directory replication rights can permit retrieval of credential material; such rights should be restricted to legitimate domain controllers/services.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 116 — Replication Rights Review

### Core Explanation

Review principals holding directory replication permissions and remove unnecessary assignments.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 117 — Golden Ticket Awareness

### Core Explanation

Compromise of the KRBTGT secret can undermine domain Kerberos trust and requires specialized recovery.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 118 — KRBTGT Protection

### Core Explanation

Domain controllers and privileged directory backups require exceptional protection because KRBTGT compromise has broad impact.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 119 — Silver Ticket Awareness

### Core Explanation

Compromise of a service-account key can allow forged tickets for that specific service context.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 120 — Service Account Protection

### Core Explanation

Use managed identities, strong random credentials, least privilege, and monitoring for service principals.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 121 — Machine Account Quota Awareness

### Core Explanation

Domain settings may permit users to create computer accounts; evaluate whether this is required and governed.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 122 — ACL-Based Privilege Escalation

### Core Explanation

Weak directory permissions can be more important than software vulnerabilities in AD environments.

### Diagram / Code / Command Example

```text
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

# Part 123 — Local Privilege to Domain Impact

### Core Explanation

Local admin on a system used by privileged users can expose credentials or sessions that create higher-domain risk.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 124 — Session Exposure

### Core Explanation

Privileged users logging onto lower-trust systems increase credential/session exposure.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 125 — Admin Logon Restriction

### Core Explanation

Restrict privileged logon to approved administrative systems.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 126 — Tier Violation Detection

### Core Explanation

Monitor and review cases where high-tier identities authenticate to lower-tier hosts.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 127 — Event Logging

### Core Explanation

Domain controllers and endpoints should retain authentication, group-change, policy, and privileged-operation logs.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 128 — Kerberos Events Awareness

### Core Explanation

Kerberos ticket events can support troubleshooting and detection when interpreted with account and host context.

### Diagram / Code / Command Example

```text
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

# Part 129 — Group Membership Change Monitoring

### Core Explanation

Privileged group additions/removals should generate high-value security telemetry.

### Diagram / Code / Command Example

```text
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

# Part 130 — Directory Service Change Monitoring

### Core Explanation

Sensitive ACL, delegation, GPO, and object changes should be monitored.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 131 — PowerShell Logging Awareness

### Core Explanation

Script block/module/transcription logging can improve investigation of administrative and test activity where configured.

### Diagram / Code / Command Example

```powershell
# Defensive/assessment example in own domain
Get-ADComputer -Filter * -Properties OperatingSystem |
  Select-Object Name, OperatingSystem |
  Select-Object -First 20
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

# Part 132 — EDR in AD Testing

### Core Explanation

Endpoint telemetry helps validate whether directory and lateral-movement behaviors are visible to defenders.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 133 — SIEM Correlation

### Core Explanation

Correlate identity, endpoint, firewall, and directory logs to reconstruct privilege paths.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 134 — Detection Validation

### Core Explanation

An AD pentest should test whether meaningful privilege-path activity generates actionable defender visibility.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 135 — Purple Team AD

### Core Explanation

Controlled replay of synthetic AD techniques can improve directory detections without pursuing full compromise.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 136 — Cleanup

### Core Explanation

Remove test users/groups/computer objects, revert ACLs/GPOs/delegation, reset synthetic credentials, and restore snapshots.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 137 — AD Finding

### Core Explanation

Document principal, affected object, right/path, preconditions, evidence, impact, remediation, and retest.

### Diagram / Code / Command Example

```text
AD finding:
principal
controlled object
permission / path
preconditions
business impact
evidence
remediation
owner
retest
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

# Part 138 — AD Remediation

### Core Explanation

Break privilege paths through permission cleanup, credential hygiene, segmentation, managed service accounts, signing, tiering, and monitoring.

### Diagram / Code / Command Example

```text
AD finding:
principal
controlled object
permission / path
preconditions
business impact
evidence
remediation
owner
retest
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

# Part 139 — AD Retest

### Core Explanation

Repeat the same safe permission/query/relationship validation after remediation.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

# Part 140 — Active Directory Penetration Testing Final Mental Model

### Core Explanation

Model identity as a graph of privileges and trust: enumerate safely, identify paths, validate only the minimum authorized path, harden the root causes, and retest.

### Diagram / Code / Command Example

```text
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 1 — Active Directory Penetration Testing Purpose

### Objective

Practice **Active Directory Penetration Testing Purpose** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 2 — AD Authorization

### Objective

Practice **AD Authorization** in a controlled lab.

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
Lab/test domain
   ↓
approved accounts
   ↓
approved hosts
   ↓
allowed identity techniques
   ↓
lockout-safe test plan
   ↓
cleanup / reset
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

## Lab 3 — AD Rules of Engagement

### Objective

Practice **AD Rules of Engagement** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 4 — AD Lab Design

### Objective

Practice **AD Lab Design** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 5 — Snapshot Strategy

### Objective

Practice **Snapshot Strategy** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 6 — Forest

### Objective

Practice **Forest** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 7 — Domain

### Objective

Practice **Domain** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 8 — Domain Controller

### Objective

Practice **Domain Controller** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 9 — OU

### Objective

Practice **OU** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 10 — User Object

### Objective

Practice **User Object** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 11 — Computer Object

### Objective

Practice **Computer Object** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 12 — Group

### Objective

Practice **Group** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 13 — Security Group

### Objective

Practice **Security Group** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 14 — Distribution Group Awareness

### Objective

Practice **Distribution Group Awareness** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 15 — Group Scope Awareness

### Objective

Practice **Group Scope Awareness** in a controlled lab.

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
Lab/test domain
   ↓
approved accounts
   ↓
approved hosts
   ↓
allowed identity techniques
   ↓
lockout-safe test plan
   ↓
cleanup / reset
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

## Lab 16 — Nested Group

### Objective

Practice **Nested Group** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 17 — Privileged Group

### Objective

Practice **Privileged Group** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 18 — Tiered Administration

### Objective

Practice **Tiered Administration** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 19 — Joiner-Mover-Leaver in AD

### Objective

Practice **Joiner-Mover-Leaver in AD** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 20 — Stale Account

### Objective

Practice **Stale Account** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 21 — Service Account

### Objective

Practice **Service Account** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 22 — gMSA

### Objective

Practice **gMSA** in a controlled lab.

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
gMSA
  ↓
managed service identity
  ↓
domain-managed password rotation
  ↓
authorized hosts retrieve secret automatically
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

## Lab 23 — LAPS

### Objective

Practice **LAPS** in a controlled lab.

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
Managed local admin password solution:
unique per-device password
  ↓
directory stores protected secret
  ↓
access limited to authorized admins
  ↓
automatic rotation
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

## Lab 24 — LDAP

### Objective

Practice **LDAP** in a controlled lab.

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

```powershell
# Own test domain / approved credentials
Get-ADDomain
Get-ADUser -Filter * -Properties Enabled |
  Select-Object SamAccountName, Enabled |
  Select-Object -First 10
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

## Lab 25 — LDAP Signing

### Objective

Practice **LDAP Signing** in a controlled lab.

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

```powershell
# Own test domain / approved credentials
Get-ADDomain
Get-ADUser -Filter * -Properties Enabled |
  Select-Object SamAccountName, Enabled |
  Select-Object -First 10
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

## Lab 26 — LDAP Channel Binding Awareness

### Objective

Practice **LDAP Channel Binding Awareness** in a controlled lab.

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

```powershell
# Own test domain / approved credentials
Get-ADDomain
Get-ADUser -Filter * -Properties Enabled |
  Select-Object SamAccountName, Enabled |
  Select-Object -First 10
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

## Lab 27 — Kerberos

### Objective

Practice **Kerberos** in a controlled lab.

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
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

## Lab 28 — KDC

### Objective

Practice **KDC** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 29 — TGT

### Objective

Practice **TGT** in a controlled lab.

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
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

## Lab 30 — TGS

### Objective

Practice **TGS** in a controlled lab.

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
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

## Lab 31 — SPN

### Objective

Practice **SPN** in a controlled lab.

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

```powershell
Get-ADUser -Filter * -Properties ServicePrincipalName |
  Where-Object {$_.ServicePrincipalName} |
  Select-Object SamAccountName, ServicePrincipalName
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

## Lab 32 — Kerberos Clock Dependency

### Objective

Practice **Kerberos Clock Dependency** in a controlled lab.

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
User proves identity
   ↓
KDC issues TGT
   ↓
client requests service ticket
   ↓
service validates ticket

Security depends on credential protection,
service identity, clock, delegation, and policy.
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

## Lab 33 — NTLM

### Objective

Practice **NTLM** in a controlled lab.

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
NTLM is legacy challenge-response authentication.
Security review asks:
- where is it still required?
- can Kerberos replace it?
- are signing/channel protections enforced?
- is privileged admin use separated?
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

## Lab 34 — NTLM Reduction

### Objective

Practice **NTLM Reduction** in a controlled lab.

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
NTLM is legacy challenge-response authentication.
Security review asks:
- where is it still required?
- can Kerberos replace it?
- are signing/channel protections enforced?
- is privileged admin use separated?
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

## Lab 35 — SMB Signing

### Objective

Practice **SMB Signing** in a controlled lab.

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
Protocol hardening:
authenticate peer
  ↓
integrity protection / signing
  ↓
channel binding where supported
  ↓
reduce relay / tampering risk
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

## Lab 36 — Extended Protection Awareness

### Objective

Practice **Extended Protection Awareness** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 37 — Password Policy

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

```powershell
Get-ADDefaultDomainPasswordPolicy |
  Select-Object MinPasswordLength, LockoutThreshold, MaxPasswordAge
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

## Lab 38 — Account Lockout

### Objective

Practice **Account Lockout** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 39 — Fine-Grained Password Policy

### Objective

Practice **Fine-Grained Password Policy** in a controlled lab.

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

```powershell
Get-ADDefaultDomainPasswordPolicy |
  Select-Object MinPasswordLength, LockoutThreshold, MaxPasswordAge
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

## Lab 40 — Password Reuse

### Objective

Practice **Password Reuse** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 41 — Credential Hygiene

### Objective

Practice **Credential Hygiene** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 42 — Cached Credential Awareness

### Objective

Practice **Cached Credential Awareness** in a controlled lab.

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
Credential defense review:
admin tiering
Credential Guard / protections
least privilege
no shared admin credentials
restricted interactive logon
EDR
patching

Course labs use synthetic accounts only.
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

## Lab 43 — Credential Guard Awareness

### Objective

Practice **Credential Guard Awareness** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 44 — LSASS Protection Awareness

### Objective

Practice **LSASS Protection Awareness** in a controlled lab.

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
Credential defense review:
admin tiering
Credential Guard / protections
least privilege
no shared admin credentials
restricted interactive logon
EDR
patching

Course labs use synthetic accounts only.
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

## Lab 45 — PowerShell for AD Assessment

### Objective

Practice **PowerShell for AD Assessment** in a controlled lab.

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

```powershell
# Defensive/assessment example in own domain
Get-ADComputer -Filter * -Properties OperatingSystem |
  Select-Object Name, OperatingSystem |
  Select-Object -First 20
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

## Lab 46 — Get-ADDomain

### Objective

Practice **Get-ADDomain** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 47 — Get-ADForest

### Objective

Practice **Get-ADForest** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 48 — Get-ADUser

### Objective

Practice **Get-ADUser** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 49 — Get-ADComputer

### Objective

Practice **Get-ADComputer** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 50 — Get-ADGroup

### Objective

Practice **Get-ADGroup** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 51 — Get-ADGroupMember

### Objective

Practice **Get-ADGroupMember** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 52 — Get-ADDefaultDomainPasswordPolicy

### Objective

Practice **Get-ADDefaultDomainPasswordPolicy** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 53 — GPO

### Objective

Practice **GPO** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 54 — GPO Scope

### Objective

Practice **GPO Scope** in a controlled lab.

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
Lab/test domain
   ↓
approved accounts
   ↓
approved hosts
   ↓
allowed identity techniques
   ↓
lockout-safe test plan
   ↓
cleanup / reset
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

## Lab 55 — GPO Modification Risk

### Objective

Practice **GPO Modification Risk** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 56 — GPO Permission Review

### Objective

Practice **GPO Permission Review** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 57 — SYSVOL

### Objective

Practice **SYSVOL** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 58 — Logon Script Security

### Objective

Practice **Logon Script Security** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 59 — AD ACL

### Objective

Practice **AD ACL** in a controlled lab.

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
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

## Lab 60 — ACE

### Objective

Practice **ACE** in a controlled lab.

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
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

## Lab 61 — Object Ownership

### Objective

Practice **Object Ownership** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 62 — GenericAll Awareness

### Objective

Practice **GenericAll Awareness** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 63 — GenericWrite Awareness

### Objective

Practice **GenericWrite Awareness** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 64 — WriteDACL Awareness

### Objective

Practice **WriteDACL Awareness** in a controlled lab.

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
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

## Lab 65 — WriteOwner Awareness

### Objective

Practice **WriteOwner Awareness** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 66 — Group Membership Write

### Objective

Practice **Group Membership Write** in a controlled lab.

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
Forest
  └─ Domain
      ├─ Domain Controllers
      ├─ OUs
      ├─ Users
      ├─ Groups
      ├─ Computers
      └─ Group Policy
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

## Lab 67 — User Attribute Write

### Objective

Practice **User Attribute Write** in a controlled lab.

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
Identity / directory inventory
   ↓
privilege relationships
   ↓
authentication configuration
   ↓
delegation / ACL / group paths
   ↓
minimal lab validation
   ↓
hardening / retest
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

## Lab 68 — Computer Object Control

### Objective

Practice **Computer Object Control** in a controlled lab.

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
AD object
  ↓
ACL
  ├─ owner
  ├─ allow ACE
  └─ deny ACE

Risk appears when low-privilege principals
can modify privileged users/groups/computers/GPOs.
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

## Lab 69 — Delegation

### Objective

Practice **Delegation** in a controlled lab.

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
Delegation
  ↓
service acts on behalf of user
  ↓
scope must be tightly controlled
  ↓
review unconstrained / constrained / resource-based settings
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

## Lab 70 — Unconstrained Delegation Awareness

### Objective

Practice **Unconstrained Delegation Awareness** in a controlled lab.

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
Delegation
  ↓
service acts on behalf of user
  ↓
scope must be tightly controlled
  ↓
review unconstrained / constrained / resource-based settings
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

# Mini Project — Disposable Active Directory Privilege-Path Lab

Create a synthetic AD domain with users, groups, service accounts, OUs, GPOs, and one intentionally weak directory permission or delegation relationship. Inventory the directory with PowerShell, model privilege relationships, identify one synthetic path from low privilege to a higher-privilege test object, validate only the minimum necessary step, correlate Windows/security logs, restore the directory state, remediate the weak ACL/delegation/account configuration, and retest.

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

- Microsoft Active Directory Domain Services documentation — https://learn.microsoft.com/windows-server/identity/ad-ds/
- Microsoft Kerberos documentation — https://learn.microsoft.com/windows-server/security/kerberos/kerberos-authentication-overview
- Microsoft LAPS documentation — https://learn.microsoft.com/windows-server/identity/laps/laps-overview
- BloodHound documentation — https://bloodhound.specterops.io/
- MITRE ATT&CK Enterprise — https://attack.mitre.org/

---

## 8. Certification Relevance

Relevant to Windows enterprise security, identity security, purple-team work, internal penetration testing, Active Directory hardening, and later advanced red-team learning.

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

### Q1. What is the key lesson from **Active Directory Penetration Testing Purpose**?

**Short answer:** Active Directory penetration testing validates whether identity, authentication, directory permissions, delegation, endpoint privilege, and network relationships create unauthorized privilege paths in an authorized lab or test domain.

### Q2. What is the key lesson from **AD Authorization**?

**Short answer:** Written authorization should identify domains, forests, domain controllers, accounts, hosts, techniques, and lockout-safe credential rules.

### Q3. What is the key lesson from **AD Rules of Engagement**?

**Short answer:** Define account lockout protections, service-impact limits, password-testing restrictions, replication-sensitive systems, and cleanup.

### Q4. What is the key lesson from **AD Lab Design**?

**Short answer:** Build a disposable Windows Server domain with synthetic users, groups, service accounts, workstations, and intentionally weak permissions.

### Q5. What is the key lesson from **Snapshot Strategy**?

**Short answer:** Snapshot domain controllers and member servers before privilege-path labs so the directory can be restored.

### Q6. What is the key lesson from **Forest**?

**Short answer:** A forest is the highest AD DS security/administrative boundary containing one or more domains that share schema and configuration.

### Q7. What is the key lesson from **Domain**?

**Short answer:** A domain contains directory objects, policies, authentication services, and domain controllers under one namespace.

### Q8. What is the key lesson from **Domain Controller**?

**Short answer:** Domain controllers host AD DS, perform authentication, and replicate directory data.

### Q9. What is the key lesson from **OU**?

**Short answer:** Organizational Units organize objects and provide delegation and Group Policy scope.

### Q10. What is the key lesson from **User Object**?

**Short answer:** User objects represent human or service identities and have group memberships, attributes, credentials, and permissions.

### Q11. What is the key lesson from **Computer Object**?

**Short answer:** Computer accounts represent domain-joined systems and participate in Kerberos and directory authorization.

### Q12. What is the key lesson from **Group**?

**Short answer:** Groups aggregate security principals for authorization and administration.

### Q13. What is the key lesson from **Security Group**?

**Short answer:** Security groups can be included in access-control lists and privilege assignments.

### Q14. What is the key lesson from **Distribution Group Awareness**?

**Short answer:** Distribution groups are primarily for messaging and are not normally used as security principals.

### Q15. What is the key lesson from **Group Scope Awareness**?

**Short answer:** Domain Local, Global, and Universal groups have different membership and resource-assignment semantics.

### Q16. What is the key lesson from **Nested Group**?

**Short answer:** Nested group membership can create indirect privilege that is easy to overlook.

### Q17. What is the key lesson from **Privileged Group**?

**Short answer:** Groups such as Domain Admins or other delegated administrative groups need strict membership and monitoring.

### Q18. What is the key lesson from **Tiered Administration**?

**Short answer:** Separate privileged admin identities and administrative workstations from normal user activity.

### Q19. What is the key lesson from **Joiner-Mover-Leaver in AD**?

**Short answer:** User and group membership should change promptly with role or employment changes.

### Q20. What is the key lesson from **Stale Account**?

**Short answer:** Disabled or unused accounts can retain privilege and should be reviewed.

### Q21. What is the key lesson from **Service Account**?

**Short answer:** Service accounts require ownership, least privilege, noninteractive use where possible, and managed credentials.

### Q22. What is the key lesson from **gMSA**?

**Short answer:** Group Managed Service Accounts provide automatically managed domain credentials to approved services/hosts.

### Q23. What is the key lesson from **LAPS**?

**Short answer:** Managed local administrator passwords reduce reuse by providing unique automatically rotated local credentials.

### Q24. What is the key lesson from **LDAP**?

**Short answer:** LDAP is used to query and modify directory objects according to authentication and ACL permissions.

### Q25. What is the key lesson from **LDAP Signing**?

**Short answer:** LDAP signing protects integrity of directory protocol traffic and reduces some relay/tampering risks.

### Q26. What is the key lesson from **LDAP Channel Binding Awareness**?

**Short answer:** Channel binding helps tie authentication to the protected TLS channel where applicable.

### Q27. What is the key lesson from **Kerberos**?

**Short answer:** Kerberos is the primary AD authentication protocol using tickets issued by the Key Distribution Center.

### Q28. What is the key lesson from **KDC**?

**Short answer:** The KDC runs on domain controllers and provides ticket-granting and authentication services.

### Q29. What is the key lesson from **TGT**?

**Short answer:** A Ticket Granting Ticket allows a client to request service tickets after successful authentication.

### Q30. What is the key lesson from **TGS**?

**Short answer:** A service ticket authenticates a user/service context to a specific service principal.

### Q31. What is the key lesson from **SPN**?

**Short answer:** Service Principal Names identify Kerberos-enabled service instances.

### Q32. What is the key lesson from **Kerberos Clock Dependency**?

**Short answer:** Kerberos depends on synchronized time, making NTP and domain time hierarchy security-relevant.

### Q33. What is the key lesson from **NTLM**?

**Short answer:** NTLM is legacy challenge-response authentication still used in some compatibility scenarios.

### Q34. What is the key lesson from **NTLM Reduction**?

**Short answer:** Reducing NTLM lowers exposure to relay and credential-theft classes but requires compatibility planning.

### Q35. What is the key lesson from **SMB Signing**?

**Short answer:** SMB signing protects integrity and helps reduce certain relay/tampering scenarios.

### Q36. What is the key lesson from **Extended Protection Awareness**?

**Short answer:** Channel binding and service protections can reduce credential relay opportunities in supported services.

### Q37. What is the key lesson from **Password Policy**?

**Short answer:** Review minimum length, history, age, complexity strategy, lockout, and compromised-password defenses.

### Q38. What is the key lesson from **Account Lockout**?

**Short answer:** Lockout can slow password attacks but also creates denial-of-service risk and requires careful test planning.

### Q39. What is the key lesson from **Fine-Grained Password Policy**?

**Short answer:** Different AD groups may receive different password/lockout policies through fine-grained policy objects.

### Q40. What is the key lesson from **Password Reuse**?

**Short answer:** Reusing local or domain admin passwords across systems increases lateral-movement risk.

### Q41. What is the key lesson from **Credential Hygiene**?

**Short answer:** Privileged credentials should not be used on lower-trust endpoints unnecessarily.

### Q42. What is the key lesson from **Cached Credential Awareness**?

**Short answer:** Windows can cache logon information for offline use, which changes the impact of endpoint compromise.

### Q43. What is the key lesson from **Credential Guard Awareness**?

**Short answer:** Credential Guard uses virtualization-based security to protect selected secrets from normal OS access.

### Q44. What is the key lesson from **LSASS Protection Awareness**?

**Short answer:** LSASS protections can reduce credential theft and should be combined with admin tiering and EDR.

### Q45. What is the key lesson from **PowerShell for AD Assessment**?

**Short answer:** PowerShell and the ActiveDirectory module provide authoritative directory queries in authorized environments.

### Q46. What is the key lesson from **Get-ADDomain**?

**Short answer:** Get-ADDomain returns domain-level properties useful for inventory.

### Q47. What is the key lesson from **Get-ADForest**?

**Short answer:** Get-ADForest returns forest structure and trust-related information.

### Q48. What is the key lesson from **Get-ADUser**?

**Short answer:** Get-ADUser supports authorized inventory of users and security-relevant attributes.

### Q49. What is the key lesson from **Get-ADComputer**?

**Short answer:** Get-ADComputer inventories domain-joined systems and operating-system metadata.

### Q50. What is the key lesson from **Get-ADGroup**?

**Short answer:** Get-ADGroup inventories security groups and scope.

### Q51. What is the key lesson from **Get-ADGroupMember**?

**Short answer:** Group membership queries reveal direct and nested privilege relationships.

### Q52. What is the key lesson from **Get-ADDefaultDomainPasswordPolicy**?

**Short answer:** The default domain password policy provides baseline credential and lockout settings.

### Q53. What is the key lesson from **GPO**?

**Short answer:** Group Policy centrally configures Windows systems and users and can create either strong security or broad privilege.

### Q54. What is the key lesson from **GPO Scope**?

**Short answer:** GPO links, inheritance, security filtering, and WMI filtering determine where policy applies.

### Q55. What is the key lesson from **GPO Modification Risk**?

**Short answer:** A principal able to modify a GPO affecting privileged systems may gain broad control.

### Q56. What is the key lesson from **GPO Permission Review**?

**Short answer:** Review which principals can edit, link, or take ownership of sensitive Group Policy objects.

### Q57. What is the key lesson from **SYSVOL**?

**Short answer:** SYSVOL stores Group Policy and domain scripts replicated across domain controllers.

### Q58. What is the key lesson from **Logon Script Security**?

**Short answer:** Scripts executed through Group Policy should not be writable by unprivileged users.

### Q59. What is the key lesson from **AD ACL**?

**Short answer:** AD objects have ACLs that control read, write, ownership, inheritance, and extended rights.

### Q60. What is the key lesson from **ACE**?

**Short answer:** Access Control Entries grant or deny rights to security principals.

### Q61. What is the key lesson from **Object Ownership**?

**Short answer:** Owners can often modify permissions, making ownership a powerful control path.

### Q62. What is the key lesson from **GenericAll Awareness**?

**Short answer:** Broad full-control permissions over privileged directory objects can create direct privilege paths.

### Q63. What is the key lesson from **GenericWrite Awareness**?

**Short answer:** Broad write permission can permit security-sensitive attribute changes depending on the object.

### Q64. What is the key lesson from **WriteDACL Awareness**?

**Short answer:** Permission to modify an object's DACL can allow the principal to grant itself additional rights.

### Q65. What is the key lesson from **WriteOwner Awareness**?

**Short answer:** Permission to change ownership can enable later ACL modification.

### Q66. What is the key lesson from **Group Membership Write**?

**Short answer:** Permission to add members to a privileged group is itself a high-risk privilege path.

### Q67. What is the key lesson from **User Attribute Write**?

**Short answer:** Ability to modify sensitive user attributes can sometimes create identity or delegation impact.

### Q68. What is the key lesson from **Computer Object Control**?

**Short answer:** Control over computer objects can affect authentication, delegation, and service relationships.

### Q69. What is the key lesson from **Delegation**?

**Short answer:** Kerberos delegation allows services to act on behalf of users and requires careful scope.

### Q70. What is the key lesson from **Unconstrained Delegation Awareness**?

**Short answer:** Legacy unconstrained delegation creates broad ticket exposure and should be minimized.

### Q71. What is the key lesson from **Constrained Delegation Awareness**?

**Short answer:** Constrained delegation limits target services but still needs strict service-account governance.

### Q72. What is the key lesson from **Resource-Based Constrained Delegation Awareness**?

**Short answer:** Resource-based constrained delegation places delegation control on the destination resource and requires careful ACL review.

### Q73. What is the key lesson from **Trusted for Delegation Flag Review**?

**Short answer:** Sensitive accounts should generally not be delegable where platform controls support protection.

### Q74. What is the key lesson from **Protected Users Awareness**?

**Short answer:** Protected Users group can reduce use of legacy authentication and credential caching for selected privileged identities.

### Q75. What is the key lesson from **AdminSDHolder Awareness**?

**Short answer:** AD protects ACLs of many privileged accounts through AdminSDHolder/SDProp behavior; stale privileged membership can have long-term effects.

### Q76. What is the key lesson from **AdminCount Awareness**?

**Short answer:** AdminCount can indicate past or present protected-group membership but is not by itself proof of current privilege.

### Q77. What is the key lesson from **Trust**?

**Short answer:** Domain/forest trusts define authentication relationships across naming/security boundaries.

### Q78. What is the key lesson from **Trust Direction**?

**Short answer:** Trust direction determines which side accepts authentication from the other and must be interpreted carefully.

### Q79. What is the key lesson from **Transitive Trust**?

**Short answer:** Transitivity can extend trust relationships across domains and affect attack-path scope.

### Q80. What is the key lesson from **External Trust Awareness**?

**Short answer:** External trusts connect separate domains with narrower trust characteristics.

### Q81. What is the key lesson from **Forest Trust Awareness**?

**Short answer:** Forest trusts can enable authentication across forests and require explicit filtering/governance.

### Q82. What is the key lesson from **SID Filtering Awareness**?

**Short answer:** SID filtering protects trust boundaries from some forged/foreign SID abuse and should be correctly configured.

### Q83. What is the key lesson from **DNS in AD**?

**Short answer:** AD depends heavily on DNS service discovery and domain-controller location.

### Q84. What is the key lesson from **SRV Records**?

**Short answer:** Kerberos, LDAP, and domain-controller services are discovered through DNS SRV records.

### Q85. What is the key lesson from **AD-Integrated DNS Security**?

**Short answer:** Directory-integrated zones inherit AD permissions and should avoid unauthorized record modification.

### Q86. What is the key lesson from **Dynamic DNS Update**?

**Short answer:** Secure dynamic updates help ensure only authorized principals modify relevant records.

### Q87. What is the key lesson from **SMB**?

**Short answer:** SMB is used for file sharing, SYSVOL, management, and domain operations and therefore is a major AD security surface.

### Q88. What is the key lesson from **WinRM**?

**Short answer:** Windows Remote Management enables administrative PowerShell remoting and should be restricted to approved admin paths.

### Q89. What is the key lesson from **RDP**?

**Short answer:** Remote Desktop provides interactive access and should be restricted through admin segmentation, MFA/gateways, and monitoring.

### Q90. What is the key lesson from **Remote Registry Awareness**?

**Short answer:** Remote registry access should be disabled or restricted when not operationally required.

### Q91. What is the key lesson from **Administrative Shares Awareness**?

**Short answer:** Administrative shares support remote administration and can increase lateral-movement capability when admin credentials are compromised.

### Q92. What is the key lesson from **Local Administrator Group**?

**Short answer:** Local admin membership on endpoints/servers should be minimized and managed centrally.

### Q93. What is the key lesson from **Local Admin Password Reuse**?

**Short answer:** Reusing one local admin password across many hosts turns one compromise into a lateral-movement path.

### Q94. What is the key lesson from **Windows Firewall**?

**Short answer:** Host firewalls should restrict administrative protocols even inside internal networks.

### Q95. What is the key lesson from **Endpoint Tiering**?

**Short answer:** Domain controllers, servers, and workstations should have different administrative trust and credential exposure.

### Q96. What is the key lesson from **Privileged Access Workstation Awareness**?

**Short answer:** Dedicated privileged workstations reduce exposure of high-value admin credentials.

### Q97. What is the key lesson from **BloodHound Awareness**?

**Short answer:** BloodHound models AD relationships to identify potential privilege and attack paths from directory/session/ACL data.

### Q98. What is the key lesson from **Graph Relationship**?

**Short answer:** Graph edges represent relationships such as group membership, local admin, ACL control, sessions, delegation, or remote access.

### Q99. What is the key lesson from **BloodHound Data Sensitivity**?

**Short answer:** Collected directory relationship data is sensitive and should remain inside the authorized assessment environment.

### Q100. What is the key lesson from **Attack Path Hypothesis**?

**Short answer:** A graph path indicates a possible relationship chain that still requires manual validation of prerequisites.

### Q101. What is the key lesson from **Shortest Path Risk**?

**Short answer:** The shortest graph path is not automatically the most realistic attack path; operational context matters.

### Q102. What is the key lesson from **Privilege Path**?

**Short answer:** A privilege path chains permissions, credentials, sessions, delegation, or host control into higher privilege.

### Q103. What is the key lesson from **Chained Misconfiguration**?

**Short answer:** Several individually moderate AD weaknesses can combine into domain-level risk.

### Q104. What is the key lesson from **Kerberoasting Awareness**?

**Short answer:** Service accounts with SPNs can expose offline password-guessing risk because service tickets are encrypted with service-account secrets; lab exercises should use synthetic weak accounts only.

### Q105. What is the key lesson from **Kerberoasting Defense**?

**Short answer:** Use gMSA or long random service-account passwords, least privilege, service ownership, and monitoring.

### Q106. What is the key lesson from **AS-REP Roasting Awareness**?

**Short answer:** Accounts configured without Kerberos preauthentication can expose offline password-guessing material and should be corrected.

### Q107. What is the key lesson from **AS-REP Roasting Defense**?

**Short answer:** Require Kerberos preauthentication unless there is a documented compatibility exception.

### Q108. What is the key lesson from **Password Spraying Boundary**?

**Short answer:** Password spraying against real users can cause lockouts and is not appropriate without explicit authorization and safeguards.

### Q109. What is the key lesson from **Synthetic Password Audit**?

**Short answer:** Use synthetic lab accounts to demonstrate password policy and detection rather than real employee accounts.

### Q110. What is the key lesson from **NTLM Relay Awareness**?

**Short answer:** If authentication can be induced and target services lack appropriate signing/channel protections, credentials may be relayed; hands-on relay should remain in dedicated isolated labs.

### Q111. What is the key lesson from **NTLM Relay Defense**?

**Short answer:** Reduce NTLM, require SMB/LDAP signing/channel binding where appropriate, segment admin protocols, and protect privileged credentials.

### Q112. What is the key lesson from **Pass-the-Hash Awareness**?

**Short answer:** Possession of an NTLM hash can sometimes authenticate without knowing the plaintext password; this illustrates why credential material is high-value.

### Q113. What is the key lesson from **Pass-the-Ticket Awareness**?

**Short answer:** Stolen Kerberos tickets can be reused within their validity/context, emphasizing ticket and endpoint protection.

### Q114. What is the key lesson from **Credential Material Handling**?

**Short answer:** Any password/hash/ticket generated in labs must be synthetic and treated as sensitive evidence.

### Q115. What is the key lesson from **DCSync Awareness**?

**Short answer:** Directory replication rights can permit retrieval of credential material; such rights should be restricted to legitimate domain controllers/services.

### Q116. What is the key lesson from **Replication Rights Review**?

**Short answer:** Review principals holding directory replication permissions and remove unnecessary assignments.

### Q117. What is the key lesson from **Golden Ticket Awareness**?

**Short answer:** Compromise of the KRBTGT secret can undermine domain Kerberos trust and requires specialized recovery.

### Q118. What is the key lesson from **KRBTGT Protection**?

**Short answer:** Domain controllers and privileged directory backups require exceptional protection because KRBTGT compromise has broad impact.

### Q119. What is the key lesson from **Silver Ticket Awareness**?

**Short answer:** Compromise of a service-account key can allow forged tickets for that specific service context.

### Q120. What is the key lesson from **Service Account Protection**?

**Short answer:** Use managed identities, strong random credentials, least privilege, and monitoring for service principals.

### Q121. What is the key lesson from **Machine Account Quota Awareness**?

**Short answer:** Domain settings may permit users to create computer accounts; evaluate whether this is required and governed.

### Q122. What is the key lesson from **ACL-Based Privilege Escalation**?

**Short answer:** Weak directory permissions can be more important than software vulnerabilities in AD environments.

### Q123. What is the key lesson from **Local Privilege to Domain Impact**?

**Short answer:** Local admin on a system used by privileged users can expose credentials or sessions that create higher-domain risk.

### Q124. What is the key lesson from **Session Exposure**?

**Short answer:** Privileged users logging onto lower-trust systems increase credential/session exposure.

### Q125. What is the key lesson from **Admin Logon Restriction**?

**Short answer:** Restrict privileged logon to approved administrative systems.

### Q126. What is the key lesson from **Tier Violation Detection**?

**Short answer:** Monitor and review cases where high-tier identities authenticate to lower-tier hosts.

### Q127. What is the key lesson from **Event Logging**?

**Short answer:** Domain controllers and endpoints should retain authentication, group-change, policy, and privileged-operation logs.

### Q128. What is the key lesson from **Kerberos Events Awareness**?

**Short answer:** Kerberos ticket events can support troubleshooting and detection when interpreted with account and host context.

### Q129. What is the key lesson from **Group Membership Change Monitoring**?

**Short answer:** Privileged group additions/removals should generate high-value security telemetry.

### Q130. What is the key lesson from **Directory Service Change Monitoring**?

**Short answer:** Sensitive ACL, delegation, GPO, and object changes should be monitored.

### Q131. What is the key lesson from **PowerShell Logging Awareness**?

**Short answer:** Script block/module/transcription logging can improve investigation of administrative and test activity where configured.

### Q132. What is the key lesson from **EDR in AD Testing**?

**Short answer:** Endpoint telemetry helps validate whether directory and lateral-movement behaviors are visible to defenders.

### Q133. What is the key lesson from **SIEM Correlation**?

**Short answer:** Correlate identity, endpoint, firewall, and directory logs to reconstruct privilege paths.

### Q134. What is the key lesson from **Detection Validation**?

**Short answer:** An AD pentest should test whether meaningful privilege-path activity generates actionable defender visibility.

### Q135. What is the key lesson from **Purple Team AD**?

**Short answer:** Controlled replay of synthetic AD techniques can improve directory detections without pursuing full compromise.

### Q136. What is the key lesson from **Cleanup**?

**Short answer:** Remove test users/groups/computer objects, revert ACLs/GPOs/delegation, reset synthetic credentials, and restore snapshots.

### Q137. What is the key lesson from **AD Finding**?

**Short answer:** Document principal, affected object, right/path, preconditions, evidence, impact, remediation, and retest.

### Q138. What is the key lesson from **AD Remediation**?

**Short answer:** Break privilege paths through permission cleanup, credential hygiene, segmentation, managed service accounts, signing, tiering, and monitoring.

### Q139. What is the key lesson from **AD Retest**?

**Short answer:** Repeat the same safe permission/query/relationship validation after remediation.

### Q140. What is the key lesson from **Active Directory Penetration Testing Final Mental Model**?

**Short answer:** Model identity as a graph of privileges and trust: enumerate safely, identify paths, validate only the minimum authorized path, harden the root causes, and retest.

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
