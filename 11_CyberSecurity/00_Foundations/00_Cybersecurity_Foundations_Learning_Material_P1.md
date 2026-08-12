# Cybersecurity Foundations — Learning Material

## Table of Contents

1. [CIA Triad](#1-cia-triad)
   - [Confidentiality](#11-confidentiality)
   - [Integrity](#12-integrity)
   - [Availability](#13-availability)
2. [Authentication](#2-authentication)
   - [Authentication Factors](#21-authentication-factors)
   - [Single-Factor Authentication](#22-single-factor-authentication-sfa)
   - [Two-Factor and Multi-Factor Authentication](#23-two-factor-and-multi-factor-authentication)
   - [Password-Based Authentication](#24-password-based-authentication)
   - [OTP Authentication](#25-otp-authentication)
   - [Token-Based Authentication](#26-token-based-authentication)
   - [JWT](#27-jwt)
   - [Certificate-Based Authentication](#28-certificate-based-authentication)
   - [Biometric Authentication](#29-biometric-authentication)
   - [Passkeys, FIDO2, and WebAuthn](#210-passkeys-fido2-and-webauthn)
   - [SSO](#211-single-sign-on-sso)
   - [OAuth 2.0 and OpenID Connect](#212-oauth-20-and-openid-connect)
3. [Authorization](#3-authorization)
   - [RBAC](#31-role-based-access-control-rbac)
   - [ABAC](#32-attribute-based-access-control-abac)
   - [ACL](#33-access-control-list-acl)
   - [Authentication vs Authorization](#34-authentication-vs-authorization)
4. [Non-Repudiation](#4-non-repudiation)
   - [Digital Signatures](#41-digital-signatures)
   - [Integrity vs Non-Repudiation](#42-integrity-vs-non-repudiation)
5. [Privacy and GDPR](#5-privacy-and-gdpr)
   - [Privacy vs Security](#51-privacy-vs-security)
   - [Personal Data](#52-personal-data)
   - [What Is GDPR?](#53-what-is-gdpr)
   - [GDPR Roles](#54-gdpr-roles)
   - [GDPR Principles](#55-gdpr-principles)
   - [Lawful Bases for Processing](#56-lawful-bases-for-processing)
   - [Data Subject Rights](#57-data-subject-rights)
   - [Data Breaches](#58-data-breaches)
   - [GDPR Penalties](#59-gdpr-penalties)
6. [Cybersecurity Risk Management Process](#6-cybersecurity-risk-management-process)
   - [Asset, Threat, Vulnerability, and Risk](#61-asset-threat-vulnerability-and-risk)
   - [Identify Assets](#62-identify-assets)
   - [Identify Threats](#63-identify-threats)
   - [Identify Vulnerabilities](#64-identify-vulnerabilities)
   - [Assess Risk](#65-assess-risk)
   - [Prioritize Risk](#66-prioritize-risk)
   - [Risk Treatment](#67-risk-treatment)
   - [Residual Risk](#68-residual-risk)
   - [Risk Register](#69-risk-register)
   - [Monitor and Review](#610-monitor-and-review)
7. [Types of Cybersecurity Threats](#7-types-of-cybersecurity-threats)
   - [Malware](#71-malware)
   - [Social Engineering](#72-social-engineering)
   - [Credential and Authentication Attacks](#73-credential-and-authentication-attacks)
   - [Network Threats](#74-network-threats)
   - [Web Application and API Threats](#75-web-application-and-api-threats)
   - [Insider Threats](#76-insider-threats)
   - [Physical and Environmental Threats](#77-physical-and-environmental-threats)
   - [Supply-Chain Threats](#78-supply-chain-threats)
   - [Threat Classification by Source](#79-threat-classification-by-source)
8. [Qualitative vs Quantitative Risk Analysis](#8-qualitative-vs-quantitative-risk-analysis)
   - [Qualitative Risk Analysis](#81-qualitative-risk-analysis)
   - [Quantitative Risk Analysis](#82-quantitative-risk-analysis)
   - [AV, EF, SLE, ARO, and ALE](#83-av-ef-sle-aro-and-ale)
9. [Risk Appetite, Risk Tolerance, Risk Capacity, and Thresholds](#9-risk-appetite-risk-tolerance-risk-capacity-and-thresholds)
   - [Risk Appetite](#91-risk-appetite)
   - [Risk Tolerance](#92-risk-tolerance)
   - [Risk Capacity](#93-risk-capacity)
   - [Risk Threshold](#94-risk-threshold)
10. [Security Controls](#10-security-controls)
    - [Physical Controls](#101-physical-controls)
    - [Technical Controls](#102-technical-controls)
    - [Administrative Controls](#103-administrative-controls)
    - [Preventive Controls](#104-preventive-controls)
    - [Detective Controls](#105-detective-controls)
    - [Corrective Controls](#106-corrective-controls)
    - [Recovery Controls](#107-recovery-controls)
    - [Deterrent Controls](#108-deterrent-controls)
    - [Compensating Controls](#109-compensating-controls)
    - [Directive Controls](#1010-directive-controls)
    - [Defense in Depth](#1011-defense-in-depth)
11. [Cybersecurity Governance Elements](#11-cybersecurity-governance-elements)
    - [Regulations](#111-regulations)
    - [Standards and Frameworks](#112-standards-and-frameworks)
    - [Policies](#113-policies)
    - [Procedures](#114-procedures)
    - [Guidelines](#115-guidelines)
12. [ISC2 Code of Ethics](#12-isc2-code-of-ethics)
    - [Protect Society and the Common Good](#121-protect-society-and-the-common-good)
    - [Act Honorably, Honestly, Justly, Responsibly, and Legally](#122-act-honorably-honestly-justly-responsibly-and-legally)
    - [Provide Diligent and Competent Service to Principals](#123-provide-diligent-and-competent-service-to-principals)
    - [Advance and Protect the Profession](#124-advance-and-protect-the-profession)
13. [Final Review Sheet](#13-final-review-sheet)

---

# 1. CIA Triad

The **CIA Triad** is one of the most fundamental models in cybersecurity.

CIA stands for:

- **C — Confidentiality**
- **I — Integrity**
- **A — Availability**

It describes three major security objectives that organizations try to protect.

## 1.1 Confidentiality

**Confidentiality** means ensuring that information is accessible only to authorized people, systems, or processes.

Main question:

> Who is allowed to see this information?

Common controls include:

- Authentication
- Authorization
- Encryption
- Access control
- Data classification
- Least privilege

Example:

```text
Customer Database
        ↓
Only authorized employees can access it
        ↓
Confidentiality protected
```

## 1.2 Integrity

**Integrity** means ensuring that information remains accurate, complete, and protected from unauthorized modification.

Main question:

> Has the information been changed improperly?

Common controls include:

- Hashing
- Digital signatures
- File integrity monitoring
- Database permissions
- Audit logs
- Version control

Example:

```text
Original Transaction = 10,000 EGP

Unauthorized change → 100,000 EGP

Integrity has been violated
```

## 1.3 Availability

**Availability** means ensuring that systems and data are accessible to authorized users when needed.

Main question:

> Can users access the system when they need it?

Common controls include:

- Backups
- Redundancy
- High availability
- Failover systems
- DDoS protection
- Disaster recovery
- UPS and generators

Example:

```text
Online Banking System
        ↓
Available 24/7
        ↓
Customers can access services
```

### CIA Example — Online Banking

```text
Confidentiality → Only you can see your account
Integrity       → Nobody can secretly alter your balance
Availability    → The service is accessible when needed
```

---

# 2. Authentication

**Authentication** is the process of verifying the identity of a user, device, or system.

Main question:

> Who are you?

Example:

```text
User claims:
"I am Ahmed"
      ↓
Authentication process
      ↓
Identity verified
```

## 2.1 Authentication Factors

Authentication factors are categories of evidence used to prove identity.

### Something You Know

Examples:

- Password
- PIN
- Passphrase

### Something You Have

Examples:

- Mobile phone
- Smart card
- Hardware security key
- Authenticator application
- OTP token

### Something You Are

Examples:

- Fingerprint
- Face
- Iris
- Voice

### Somewhere You Are

Examples:

- Corporate office
- Trusted network
- Known geographic region

Location is often used as part of adaptive or risk-based authentication.

### Something You Do

Examples:

- Typing rhythm
- Mouse behavior
- Behavioral biometrics

## 2.2 Single-Factor Authentication — SFA

**SFA** uses only one authentication factor.

Example:

```text
Password only
```

If the password is stolen, the account may be compromised.

## 2.3 Two-Factor and Multi-Factor Authentication

### Two-Factor Authentication — 2FA

Uses two **different** authentication factors.

Example:

```text
Password
   +
Security Key
```

This combines:

- Something you know
- Something you have

A password plus a PIN is usually **not** true 2FA because both are knowledge factors.

### Multi-Factor Authentication — MFA

Uses two or more different authentication factors.

Example:

```text
Password + Security Key + Fingerprint
```

## 2.4 Password-Based Authentication

Traditional authentication uses a username and password.

A secure system should **not store plaintext passwords**.

Instead, it should use a password-hashing algorithm such as:

- Argon2id
- bcrypt
- scrypt
- PBKDF2

Conceptually:

```text
Password
   ↓
Password-hashing algorithm + salt
   ↓
Stored password hash
```

## 2.5 OTP Authentication

**OTP = One-Time Password**

It is a short-lived or single-use authentication code.

### TOTP

**Time-Based One-Time Password**

Generated based on time, commonly by authenticator applications.

### HOTP

**HMAC-Based One-Time Password**

Generated using a counter.

### SMS OTP

A code is sent through SMS.

SMS OTP is generally weaker than authenticator apps or hardware security keys because of threats such as SIM swapping.

## 2.6 Token-Based Authentication

After authentication, a server can issue a token.

```text
Client
   ↓
Login
   ↓
Authentication Server
   ↓
Token issued
   ↓
Client sends token with future requests
```

Example API request:

```http
GET /api/profile
Authorization: Bearer <token>
```

## 2.7 JWT

**JWT = JSON Web Token**

JWT is a **token format**, not an authentication protocol.

A JWT typically contains:

```text
Header.Payload.Signature
```

JWTs are common in APIs and distributed applications.

Important security considerations include:

- Signature verification
- Token expiration
- Secure storage
- Key management
- Revocation strategy
- Correct algorithm configuration

## 2.8 Certificate-Based Authentication

Authentication may use digital certificates and public-key cryptography.

Common uses:

- Enterprise authentication
- VPNs
- Device authentication
- Service-to-service authentication
- Mutual TLS — mTLS

## 2.9 Biometric Authentication

Uses biological characteristics.

Examples:

- Fingerprint
- Face
- Iris
- Voice

Biometrics are frequently used to unlock a local cryptographic credential rather than sending raw biometric data to a server.

## 2.10 Passkeys, FIDO2, and WebAuthn

Modern passwordless authentication often uses:

- FIDO2
- WebAuthn
- Passkeys
- Hardware security keys

The device generates a cryptographic key pair:

```text
Private Key → stays securely on device
Public Key  → registered with service
```

These methods can provide strong resistance to phishing.

## 2.11 Single Sign-On — SSO

**SSO** allows users to authenticate once and access multiple applications.

```text
             Identity Provider
                    │
             Authenticate once
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      App A       App B       App C
```

Technologies associated with SSO include:

- SAML 2.0
- OpenID Connect
- Kerberos

## 2.12 OAuth 2.0 and OpenID Connect

### OAuth 2.0

OAuth 2.0 is primarily an **authorization framework**.

It allows an application to obtain limited access to resources without receiving the user's password.

### OpenID Connect — OIDC

OIDC adds an **identity/authentication layer** on top of OAuth 2.0.

Example:

```text
Continue with Google
       ↓
Identity Provider
       ↓
User authenticates
       ↓
Application receives identity information
```

---

# 3. Authorization

**Authorization** determines what an authenticated user is allowed to access or do.

Main question:

> What are you allowed to do?

Example:

```text
User authenticates
       ↓
Identity = Ahmed
       ↓
Authorization check
       ↓
Can Ahmed delete users?
       ↓
No → Access denied
```

## 3.1 Role-Based Access Control — RBAC

Permissions are assigned to roles.

```text
User → Role → Permissions
```

Example:

```text
Ahmed → Employee → Read
Sara  → Manager  → Read + Write
Omar  → Admin    → Read + Write + Delete
```

## 3.2 Attribute-Based Access Control — ABAC

Authorization decisions are based on attributes.

Examples:

- Department
- Location
- Job title
- Device security state
- Time
- Resource classification

Example:

```text
User.department = HR
Resource.department = HR
Time = Working Hours

→ Allow
```

## 3.3 Access Control List — ACL

An ACL defines permissions for a specific resource.

Example:

```text
Report.pdf

Ahmed → Read
Sara  → Read + Write
Omar  → Full Control
```

## 3.4 Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Verifies identity | Verifies permissions |
| Who are you? | What can you do? |
| Usually happens first | Usually follows authentication |
| Password, MFA, passkey | RBAC, ABAC, ACL |
| Login | Access decision |

---

# 4. Non-Repudiation

**Non-repudiation** provides evidence so that a person or system cannot credibly deny performing a specific action.

Example:

```text
User digitally signs a contract
        ↓
Signature can be verified
        ↓
Evidence links the action to the signer
```

Common technologies that support non-repudiation include:

- Digital signatures
- PKI
- Certificates
- Trusted timestamps
- Audit trails
- Transaction records

## 4.1 Digital Signatures

A digital signature uses asymmetric cryptography.

Simplified signing process:

```text
Document
   ↓
Hash
   ↓
Document Hash
   ↓
Sign with Private Key
   ↓
Digital Signature
```

Verification:

```text
Signed Document
       ↓
Verify using Public Key
       ↓
Valid / Invalid
```

Digital signatures can support:

- Integrity
- Authenticity
- Non-repudiation

## 4.2 Integrity vs Non-Repudiation

### Integrity

Asks:

> Has the data been changed?

Common mechanisms:

- Hashing
- MACs
- Digital signatures

### Non-Repudiation

Asks:

> Can a party credibly deny performing the action?

Common mechanisms:

- Digital signatures
- Certificates
- Trusted timestamps
- Audit records

A normal hash alone does **not** prove who created or approved information.

---

# 5. Privacy and GDPR

## 5.1 Privacy vs Security

**Privacy** concerns how personal information is collected, used, stored, shared, retained, and deleted.

**Security** concerns how information and systems are protected.

Think:

```text
Security → How do we protect the data?

Privacy  → Why do we collect it, how should we use it,
           and who should have access?
```

A system can be technically secure but still violate privacy requirements.

## 5.2 Personal Data

Personal data is information relating to an identified or identifiable person.

Examples:

- Name
- Email
- Phone number
- Address
- Identification number
- IP address
- Location information
- Device identifiers

Special categories may receive stronger legal protection.

Examples include:

- Health data
- Biometric data used for identification
- Genetic data
- Religious beliefs
- Political opinions
- Sexual orientation

## 5.3 What Is GDPR?

**GDPR = General Data Protection Regulation**

It is a major European Union data protection regulation.

It became applicable on **25 May 2018**.

It can apply to organizations outside the EU in certain situations, such as offering goods or services to people in the EU or monitoring their behavior.

## 5.4 GDPR Roles

### Data Subject

The individual whose personal data is processed.

### Data Controller

Determines **why and how** personal data is processed.

### Data Processor

Processes personal data on behalf of the controller.

Simplified relationship:

```text
Individual
   ↓
Data Subject

Organization deciding purpose
   ↓
Controller

Service provider processing data
   ↓
Processor
```

## 5.5 GDPR Principles

### Lawfulness, Fairness, and Transparency

Data processing must be lawful, fair, and transparent.

### Purpose Limitation

Collect data for specified, explicit, legitimate purposes.

### Data Minimization

Collect only what is necessary.

### Accuracy

Keep personal data accurate and up to date where necessary.

### Storage Limitation

Do not retain personal data longer than necessary.

### Integrity and Confidentiality

Protect data with appropriate security controls.

### Accountability

Organizations must be able to demonstrate compliance.

## 5.6 Lawful Bases for Processing

Consent is **not** the only lawful basis.

Common lawful bases include:

- Consent
- Contract
- Legal obligation
- Vital interests
- Public task
- Legitimate interests

## 5.7 Data Subject Rights

GDPR provides rights including, subject to conditions:

- Access
- Rectification
- Erasure
- Restriction
- Data portability
- Objection
- Protections relating to certain automated decision-making

## 5.8 Data Breaches

A personal data breach can involve:

- Unauthorized access
- Unauthorized disclosure
- Loss
- Destruction
- Alteration

For certain breaches, GDPR requires notification of the relevant supervisory authority **without undue delay and, where feasible, within 72 hours after becoming aware of the breach**.

## 5.9 GDPR Penalties

For the higher tier of GDPR infringements, fines can reach:

- **€20 million**, or
- **4% of total worldwide annual turnover of the preceding financial year**

whichever is higher.

A lower tier can reach:

- €10 million, or
- 2% of worldwide annual turnover

depending on the violated provision.

---

# 6. Cybersecurity Risk Management Process

Cybersecurity risk management is the continuous process of identifying, assessing, treating, and monitoring risk.

```text
Identify Assets
      ↓
Identify Threats
      ↓
Identify Vulnerabilities
      ↓
Assess Risk
      ↓
Prioritize Risk
      ↓
Treat Risk
      ↓
Monitor and Review
```

## 6.1 Asset, Threat, Vulnerability, and Risk

### Asset

Something valuable that needs protection.

Examples:

- Customer data
- Servers
- Applications
- Credentials
- Source code
- Cloud infrastructure
- Business reputation

### Threat

Something capable of causing harm.

Examples:

- Attacker
- Malware
- Fire
- Insider
- Hardware failure

### Vulnerability

A weakness that a threat may exploit.

Examples:

- Weak password
- Missing patch
- SQL injection
- Public cloud storage
- Excessive permissions

### Risk

The possibility that a threat will exploit a vulnerability and cause impact.

Simplified model:

```text
Risk ≈ Likelihood × Impact
```

## 6.2 Identify Assets

Determine what must be protected and its business value.

Examples:

```text
Company Assets
│
├── Customer Database
├── ERP
├── Website
├── Employee Devices
├── Source Code
└── Cloud Systems
```

## 6.3 Identify Threats

Ask:

> What could harm this asset?

Examples:

- External attacker
- Ransomware
- Malicious insider
- Accidental deletion
- Hardware failure
- Fire

## 6.4 Identify Vulnerabilities

Ask:

> What weakness could allow the threat to succeed?

Examples:

| Asset | Vulnerability |
|---|---|
| Web app | SQL injection |
| Server | Missing patches |
| Account | Weak password |
| Admin account | No MFA |
| Database | Excessive permissions |

## 6.5 Assess Risk

Assess:

### Likelihood

Example scale:

```text
1 = Rare
2 = Unlikely
3 = Possible
4 = Likely
5 = Almost Certain
```

### Impact

Example:

```text
1 = Insignificant
2 = Minor
3 = Moderate
4 = Major
5 = Severe
```

A common simple scoring model:

```text
Risk Score = Likelihood × Impact
```

## 6.6 Prioritize Risk

Risks can be prioritized according to:

- Risk score
- Asset criticality
- Business impact
- Regulatory obligations
- Threat intelligence
- Cost of remediation
- Existing controls

## 6.7 Risk Treatment

Four common treatments:

### Avoid

Stop the activity creating the risk.

### Mitigate

Implement controls to reduce likelihood and/or impact.

### Transfer / Share

Shift or share part of the financial or operational consequence.

Examples:

- Cyber insurance
- Contractual allocation
- Outsourcing

### Accept

Knowingly accept the remaining risk when it is within approved tolerance.

Memory aid:

```text
Avoid
Mitigate
Transfer
Accept
```

## 6.8 Residual Risk

### Inherent Risk

Risk before controls.

### Residual Risk

Risk remaining after controls.

```text
Inherent Risk
     ↓
Security Controls
     ↓
Residual Risk
```

## 6.9 Risk Register

A risk register documents identified risks.

Typical fields:

| Field |
|---|
| Risk ID |
| Asset |
| Threat |
| Vulnerability |
| Likelihood |
| Impact |
| Risk Score |
| Treatment |
| Risk Owner |
| Status |

## 6.10 Monitor and Review

Risk management is continuous because:

- New vulnerabilities appear
- Threats evolve
- Infrastructure changes
- New systems are deployed
- Regulations change
- Business priorities change

---

# 7. Types of Cybersecurity Threats

## 7.1 Malware

**Malware = Malicious Software**

Common types:

### Virus

Attaches to files or programs and spreads when executed.

### Worm

Self-replicates and can spread across networks.

### Trojan

Pretends to be legitimate software.

### Ransomware

Encrypts or blocks access to data and demands payment.

### Spyware

Secretly collects information.

### Keylogger

Records keystrokes.

### Rootkit

Helps hide malicious privileged access.

### Bot / Botnet Malware

Turns infected devices into remotely controlled systems.

## 7.2 Social Engineering

Manipulates people rather than attacking only technology.

### Phishing

Fraudulent messages designed to steal information or trigger malicious actions.

Variants:

- Spear phishing
- Whaling
- Smishing
- Vishing

Other techniques:

- Pretexting
- Baiting
- Impersonation
- Tailgating

## 7.3 Credential and Authentication Attacks

Examples:

- Brute-force attacks
- Dictionary attacks
- Password spraying
- Credential stuffing
- MFA fatigue
- Session theft
- Token theft

## 7.4 Network Threats

Examples:

- Man-in-the-Middle
- DNS attacks
- ARP spoofing
- Packet sniffing
- Rogue access points
- DoS
- DDoS

### DDoS

Many systems attack one service simultaneously to overwhelm it.

This mainly threatens **Availability**.

## 7.5 Web Application and API Threats

Examples:

- SQL Injection
- Cross-Site Scripting — XSS
- Broken Access Control
- Authentication failures
- SSRF
- API authorization vulnerabilities
- Security misconfiguration
- Supply-chain vulnerabilities

## 7.6 Insider Threats

### Malicious Insider

Intentionally causes harm.

### Negligent or Accidental Insider

Causes harm unintentionally through error or poor security behavior.

## 7.7 Physical and Environmental Threats

Examples:

- Fire
- Flood
- Theft
- Physical intrusion
- Power failure
- Equipment damage
- Natural disasters

## 7.8 Supply-Chain Threats

Attackers compromise a trusted supplier, dependency, software vendor, or service provider.

```text
Vendor Compromise
      ↓
Compromised Update
      ↓
Customers receive malicious software
```

## 7.9 Threat Classification by Source

| Source | Examples |
|---|---|
| External | Cybercriminals |
| Internal | Employees, contractors |
| Nation-state | State-sponsored actors |
| Third-party | Vendors |
| Accidental | Human error |
| Environmental | Fire, flood |
| Technical | Hardware/software failure |

---

# 8. Qualitative vs Quantitative Risk Analysis

## 8.1 Qualitative Risk Analysis

Uses descriptive or ordinal categories.

Example:

```text
Likelihood = High
Impact     = High
Risk       = Critical
```

A risk matrix may use:

- Low
- Medium
- High
- Critical

Or scores such as 1–5.

Advantages:

- Fast
- Easy to understand
- Requires less data
- Useful for prioritization

Disadvantages:

- More subjective
- Different analysts may score differently
- Does not directly express monetary loss

## 8.2 Quantitative Risk Analysis

Uses measurable numerical values such as:

- Money
- Probability
- Frequency
- Expected loss

Example:

```text
Expected Annual Loss = $25,000
```

Advantages:

- Supports financial decision-making
- Helps justify security investment
- Provides measurable estimates

Disadvantages:

- Requires reliable data
- Can be time-consuming
- Still depends on assumptions

## 8.3 AV, EF, SLE, ARO, and ALE

### Asset Value — AV

Value of the asset.

Example:

```text
AV = $200,000
```

### Exposure Factor — EF

Percentage of asset value expected to be lost in one incident.

Example:

```text
EF = 40% = 0.40
```

### Single Loss Expectancy — SLE

Expected loss from one occurrence.

Formula:

```text
SLE = AV × EF
```

Example:

```text
SLE = $200,000 × 0.40
SLE = $80,000
```

### Annualized Rate of Occurrence — ARO

Estimated frequency per year.

Examples:

```text
Once per year       → ARO = 1
Once every 2 years  → ARO = 0.5
Twice per year      → ARO = 2
```

### Annualized Loss Expectancy — ALE

Expected annualized loss.

Formula:

```text
ALE = SLE × ARO
```

Example:

```text
SLE = $80,000
ARO = 0.25

ALE = $20,000/year
```

### Core Formulas

```text
SLE = Asset Value × Exposure Factor

ALE = Single Loss Expectancy × Annualized Rate of Occurrence
```

---

# 9. Risk Appetite, Risk Tolerance, Risk Capacity, and Thresholds

## 9.1 Risk Appetite

**Risk appetite** is the overall amount and type of risk an organization is willing to accept while pursuing its objectives.

Question:

> How much risk are we generally willing to take?

Example:

> The company has a very low appetite for unauthorized access to customer data.

## 9.2 Risk Tolerance

**Risk tolerance** is the specific acceptable limit or variation around a risk objective.

Question:

> Exactly how far can we go before action is required?

Example:

```text
Maximum acceptable downtime:
30 minutes per month
```

## 9.3 Risk Capacity

**Risk capacity** is the maximum amount of risk the organization can absorb without threatening its survival or core objectives.

Generally:

```text
Risk Appetite < Risk Capacity
```

## 9.4 Risk Threshold

A specific point at which escalation or corrective action is required.

Example:

```text
Critical vulnerability age:

0–3 days  → Normal remediation
4–7 days  → Warning
> 7 days  → Escalation
```

### Comparison

| Concept | Meaning |
|---|---|
| Risk Capacity | Maximum risk the organization can withstand |
| Risk Appetite | Amount/type of risk it is willing to take |
| Risk Tolerance | Specific acceptable variation or limit |
| Risk Threshold | Point at which action/escalation occurs |

---

# 10. Security Controls

A **security control** is a safeguard or countermeasure used to prevent, detect, reduce, respond to, or recover from security risks.

Security controls can be classified in two main ways:

### By Implementation

- Physical
- Technical
- Administrative

### By Function

- Preventive
- Detective
- Corrective
- Recovery
- Deterrent
- Compensating
- Directive

## 10.1 Physical Controls

Protect people, facilities, equipment, and other physical assets.

Examples:

- Locks
- Security guards
- CCTV
- Fences
- Gates
- Access cards
- Biometric entry
- Mantraps
- Fire suppression
- UPS

## 10.2 Technical Controls

Implemented through technology.

Examples:

- Firewall
- MFA
- Encryption
- Antivirus/EDR
- IDS/IPS
- RBAC
- SIEM
- DLP
- WAF
- Backups
- VPN
- Network segmentation

## 10.3 Administrative Controls

Policies, procedures, governance, and management activities.

Examples:

- Security policies
- Security awareness training
- Risk assessments
- Background checks
- Incident response plans
- Business continuity plans
- Vendor risk management
- Access reviews
- Change management
- Security audits

## 10.4 Preventive Controls

Try to stop an incident before it happens.

Examples:

- Firewall
- MFA
- Access control
- Door locks
- Secure configuration

## 10.5 Detective Controls

Identify suspicious activity or incidents.

Examples:

- SIEM
- IDS
- CCTV monitoring
- Audit logs
- EDR alerts

## 10.6 Corrective Controls

Correct problems and reduce consequences after detection.

Examples:

- Removing malware
- Disabling a compromised account
- Reconfiguring a firewall
- Patching a vulnerability

## 10.7 Recovery Controls

Restore systems and operations.

Examples:

- Backups
- Disaster recovery
- Failover
- System restoration

## 10.8 Deterrent Controls

Discourage unwanted actions.

Examples:

- Warning signs
- Visible CCTV
- Guards
- Login warning banners

## 10.9 Compensating Controls

Alternative controls used when the preferred control cannot be implemented.

Example:

```text
Preferred Control:
MFA

Legacy System:
Does not support MFA

Compensating Controls:
- Restricted network access
- Stronger monitoring
- Limited permissions
```

## 10.10 Directive Controls

Tell people what behavior is expected.

Examples:

- Policies
- Standards
- Security procedures
- Acceptable-use rules

## 10.11 Defense in Depth

**Defense in Depth** means using multiple layers of controls rather than depending on one safeguard.

Example:

```text
Internet
   ↓
Firewall
   ↓
WAF
   ↓
Application Authentication
   ↓
Authorization
   ↓
Database Encryption
   ↓
Logging and Monitoring
```

---

# 11. Cybersecurity Governance Elements

Cybersecurity governance defines how security is directed, controlled, and managed across an organization.

A useful hierarchy is:

```text
Regulations
    ↓
Standards
    ↓
Policies
    ↓
Procedures
```

## 11.1 Regulations

Mandatory legal requirements imposed by governments or regulators.

Question:

> What are we legally required to do?

Examples:

- GDPR
- Sector-specific cybersecurity laws
- Financial regulations
- Healthcare regulations

Violation can result in:

- Fines
- Legal action
- Regulatory sanctions
- Reputational damage

## 11.2 Standards and Frameworks

Recognized sets of requirements, controls, or practices.

Examples:

- ISO/IEC 27001
- ISO/IEC 27002
- NIST Cybersecurity Framework
- NIST SP 800-series
- CIS Controls
- PCI DSS

A standard is not automatically a law, although contracts or regulators may require compliance.

## 11.3 Policies

High-level internal rules established by an organization.

Question:

> What must we do?

Examples:

- Information Security Policy
- Access Control Policy
- Password Policy
- Backup Policy
- Remote Access Policy
- Data Classification Policy

## 11.4 Procedures

Detailed step-by-step instructions.

Question:

> How exactly do we do it?

Example:

```text
Employee Termination Procedure

1. HR sends termination notification.
2. IT disables the account.
3. VPN access is revoked.
4. Cloud sessions are revoked.
5. Application permissions are removed.
6. Company devices are recovered.
7. Completion is recorded.
```

## 11.5 Guidelines

Recommended practices rather than mandatory requirements.

Question:

> What is the recommended way to do it?

### Summary

| Element | Main Question |
|---|---|
| Regulation | What does the law require? |
| Standard | What recognized requirements should we follow? |
| Policy | What must our organization do? |
| Procedure | How exactly do we do it? |
| Guideline | What is recommended? |

---

# 12. ISC2 Code of Ethics

The **ISC2 Code of Ethics** establishes professional ethical responsibilities for ISC2-certified cybersecurity professionals.

It contains four major canons.

## 12.1 Protect Society and the Common Good

Cybersecurity professionals should prioritize:

- Society
- Public safety
- Public trust
- Critical infrastructure
- Responsible security practices

Example:

```text
Critical vulnerability discovered
        ↓
Do not exploit irresponsibly
        ↓
Follow responsible reporting and remediation
```

Memory:

> Society comes first.

## 12.2 Act Honorably, Honestly, Justly, Responsibly, and Legally

Security professionals frequently have privileged access.

That access must not be abused.

Examples:

- Do not steal data
- Do not misuse administrator privileges
- Do not falsify reports
- Do not hide important findings
- Do not perform unauthorized penetration testing
- Follow applicable laws

Memory:

> Have integrity and act legally.

## 12.3 Provide Diligent and Competent Service to Principals

**Principals** can include:

- Employers
- Clients
- Customers
- Organizations

Professionals should:

- Understand scope
- Work carefully
- Protect confidential information
- Report findings accurately
- Maintain competence
- Recognize limits of expertise

Memory:

> Serve clients and employers competently.

## 12.4 Advance and Protect the Profession

Cybersecurity professionals should help strengthen the profession.

Examples:

- Continue learning
- Share knowledge responsibly
- Mentor others
- Avoid false claims
- Maintain professional standards
- Protect the reputation of the profession

Memory:

> Make the cybersecurity profession better.

### The Four Canons — Memory Model

```text
1. SOCIETY
   Protect society and the common good

2. YOUR CONDUCT
   Act honestly, responsibly, and legally

3. PRINCIPALS
   Provide diligent and competent service

4. PROFESSION
   Advance and protect the profession
```

---

# 13. Final Review Sheet

## CIA

```text
Confidentiality → Who can see the data?
Integrity       → Has the data been changed improperly?
Availability    → Can authorized users access it?
```

## Identity and Access

```text
Authentication → Who are you?
Authorization  → What are you allowed to do?
Non-Repudiation → Can you credibly deny the action later?
```

## Authentication Factors

```text
Know     → Password / PIN
Have     → Phone / Security Key
Are      → Fingerprint / Face
Location → Trusted location/network
Do       → Behavioral biometrics
```

## Privacy

```text
Security → How do we protect data?
Privacy  → How should personal data be collected and used?
GDPR     → Legal framework governing personal data processing
```

## Risk

```text
Asset
  ↓
Threat
  ↓
Vulnerability
  ↓
Risk
  ↓
Assessment
  ↓
Treatment
  ↓
Residual Risk
  ↓
Monitoring
```

## Risk Treatment

```text
Avoid
Mitigate
Transfer
Accept
```

## Quantitative Risk Formulas

```text
SLE = AV × EF

ALE = SLE × ARO
```

Where:

- AV = Asset Value
- EF = Exposure Factor
- SLE = Single Loss Expectancy
- ARO = Annualized Rate of Occurrence
- ALE = Annualized Loss Expectancy

## Risk Governance

```text
Risk Capacity
     ↓
Risk Appetite
     ↓
Risk Tolerance
     ↓
Risk Threshold
```

## Security Controls by Implementation

```text
Physical
Technical
Administrative
```

## Security Controls by Function

```text
Preventive
Detective
Corrective
Recovery
Deterrent
Compensating
Directive
```

## Governance Hierarchy

```text
Regulation → Legal requirement
Standard   → Recognized security requirement/framework
Policy     → Organization's mandatory rule
Procedure  → Step-by-step implementation
Guideline  → Recommended approach
```

## ISC2 Ethics

```text
1. Protect society
2. Act honestly and legally
3. Serve principals competently
4. Advance and protect the profession
```

---

# Suggested Next Topics

After completing this material, a logical next sequence is:

1. Cryptography fundamentals
2. Symmetric vs asymmetric encryption
3. Hashing and salting
4. PKI and digital certificates
5. Network security fundamentals
6. Common ports and protocols
7. Firewalls, IDS, and IPS
8. Secure network architecture
9. Vulnerability management
10. Incident response
11. Business continuity and disaster recovery
12. Security operations and monitoring
