# Access Control Concepts — Deep Learning Material

## Table of Contents

1. [Access Control Overview](#1-access-control-overview)
2. [Subject, Object, Action, and Policy](#2-subject-object-action-and-policy)
3. [Security Controls](#3-security-controls)
   - [Technical Controls](#31-technical-controls)
   - [Physical Controls](#32-physical-controls)
   - [Administrative Controls](#33-administrative-controls)
4. [Security Control Functions](#4-security-control-functions)
   - [Preventive](#41-preventive-controls)
   - [Detective](#42-detective-controls)
   - [Corrective](#43-corrective-controls)
   - [Recovery](#44-recovery-controls)
   - [Deterrent](#45-deterrent-controls)
   - [Compensating](#46-compensating-controls)
5. [Security Controls and Risk Reduction](#5-security-controls-and-risk-reduction)
6. [Defense in Depth](#6-defense-in-depth)
   - [Least Privilege](#61-least-privilege)
   - [Need to Know](#62-need-to-know)
7. [Privileged Access Management — PAM](#7-privileged-access-management--pam)
8. [Segregation of Duties — SoD](#8-segregation-of-duties--sod)
9. [Two-Person Integrity and Dual Control](#9-two-person-integrity-and-dual-control)
10. [User Provisioning Lifecycle](#10-user-provisioning-lifecycle)
11. [Physical Access Controls](#11-physical-access-controls)
12. [Access Card Technologies](#12-access-card-technologies)
13. [Technical Access Controls](#13-technical-access-controls)
14. [Federated Identity](#14-federated-identity)
15. [SSO and Federation](#15-sso-and-federation)
16. [Access Control Models](#16-access-control-models)
17. [DAC vs RBAC vs MAC vs Rule-Based vs ABAC](#17-dac-vs-rbac-vs-mac-vs-rule-based-vs-abac)
18. [Administrative Access Controls](#18-administrative-access-controls)
19. [Policy Decision and Enforcement Components](#19-policy-decision-and-enforcement-components)
20. [Python Example — Simple Authorization Engine](#20-python-example--simple-authorization-engine)
21. [Python Example — RBAC](#21-python-example--rbac)
22. [Python Example — ABAC](#22-python-example--abac)
23. [Python Example — SoD](#23-python-example--sod)
24. [Python Example — User Provisioning](#24-python-example--user-provisioning)
25. [Python Example — PAM Checkout Concept](#25-python-example--pam-checkout-concept)
26. [Practical Enterprise Access-Control Architecture](#26-practical-enterprise-access-control-architecture)
27. [Common Access-Control Failures](#27-common-access-control-failures)
28. [Access Reviews and Recertification](#28-access-reviews-and-recertification)
29. [Access Control in Cloud Environments](#29-access-control-in-cloud-environments)
30. [Interview and Exam Questions](#30-interview-and-exam-questions)
31. [Final Review Sheet](#31-final-review-sheet)

---

# 1. Access Control Overview

**Access control** is the process of deciding who or what is allowed to access which resource, perform which action, and under which conditions.

```text
Subject
   ↓
Requests Action
   ↓
On Object
   ↓
Policy / Rules Evaluated
   ↓
ALLOW or DENY
```

Example:

```text
Subject:
Ahmed

Action:
Read

Object:
Payroll.xlsx

Policy:
Only HR employees may read payroll files.

Decision:
DENY
```

---

# 2. Subject, Object, Action, and Policy

## Subject

A **subject** is an active entity requesting access.

Examples:

```text
Human User
Application
Service Account
Process
Device
Container
AI Agent
```

## Object

An **object** is the resource being accessed.

Examples:

```text
File
Database
API
Server
Folder
Cloud Bucket
Application
Network Device
Secret
```

## Action

The requested operation.

Examples:

```text
Read
Write
Delete
Execute
Approve
Create
Modify
Download
Share
```

## Policy / Rule

The rule that determines whether the requested access should be allowed.

Example:

```text
ALLOW if:
role == "HR"
AND action == "read"
AND resource == "payroll"
```

## Access-Control Decision

The policy engine evaluates:

```text
Subject
Object
Action
Environment
Policy
```

then returns:

```text
ALLOW
or
DENY
```

---

# 3. Security Controls

A **security control** is a safeguard or countermeasure used to reduce security risk.

Controls can be classified by implementation as:

```text
Technical
Physical
Administrative
```

## 3.1 Technical Controls

Implemented through technology.

Examples:

```text
MFA
Firewall
Encryption
RBAC
ABAC
SIEM
IDS / IPS
EDR
DLP
PAM
Federated Identity
Access-Control Lists
```

## 3.2 Physical Controls

Protect facilities, equipment, and people.

Examples:

```text
Fences
Gates
Bollards
Lighting
Mantraps
Turnstiles
CCTV
Locks
Guards
Access Cards
```

## 3.3 Administrative Controls

Policies, processes, procedures, and governance mechanisms.

Examples:

```text
Access Control Policy
Joiner-Mover-Leaver Procedure
Security Awareness
Access Reviews
Background Checks
Segregation of Duties
Change Management
Incident Response Procedures
Risk Assessments
```

---

# 4. Security Control Functions

Controls can also be classified by what they do.

## 4.1 Preventive Controls

Designed to stop an unwanted action before it happens.

Examples:

```text
MFA
Firewall
Door Lock
RBAC
Encryption
Security Guard
```

## 4.2 Detective Controls

Designed to discover suspicious or unauthorized activity.

Examples:

```text
SIEM
CCTV
IDS
Audit Logs
Security Alerts
```

## 4.3 Corrective Controls

Designed to correct a problem after detection.

Examples:

```text
Disable Compromised Account
Patch Vulnerability
Remove Malware
Correct Misconfiguration
```

## 4.4 Recovery Controls

Restore service after disruption.

Examples:

```text
Backups
Disaster Recovery
Failover
System Restore
```

## 4.5 Deterrent Controls

Discourage attackers.

Examples:

```text
Warning Signs
Visible CCTV
Security Guards
Login Banners
```

## 4.6 Compensating Controls

Alternative controls used when the preferred control cannot be implemented.

Example:

```text
Preferred:
MFA

Legacy System:
No MFA Support

Compensating Controls:
Restricted Network Access
Jump Host
Additional Monitoring
Strong Password
Limited Privileges
```

---

# 5. Security Controls and Risk Reduction

Risk reduction depends on the effectiveness of the control.

```text
Risk Before Control
       ↓
Security Control
       ↓
Residual Risk
```

Example:

```text
Risk:
Unauthorized administrator login

Control:
MFA

Result:
Reduced likelihood of credential-only compromise
```

Controls must adapt as the environment changes.

```text
New Technology
New Threats
New Users
New Business Processes
New Regulations
New Cloud Services
```

---

# 6. Defense in Depth

**Defense in Depth** means using multiple layers of security controls so that failure of one control does not automatically lead to compromise.

```text
Internet
   ↓
Firewall
   ↓
WAF
   ↓
Authentication
   ↓
MFA
   ↓
Authorization
   ↓
Application Security
   ↓
Database Permissions
   ↓
Encryption
   ↓
Logging
```

## 6.1 Least Privilege

Give only the minimum permissions necessary.

Bad:

```text
Developer
→ Global Administrator
```

Better:

```text
Developer
→ Read Development Logs
→ Deploy Development App
→ No Production Admin
```

Least privilege reduces:

```text
Attack Surface
Blast Radius
Insider Risk
Accidental Damage
Privilege Abuse
```

## 6.2 Need to Know

Grant access only to information required for the subject's work.

```text
Least Privilege
→ Minimum permissions

Need to Know
→ Minimum information
```

---

# 7. Privileged Access Management — PAM

**PAM = Privileged Access Management**

PAM identifies, controls, monitors, and protects privileged accounts.

Examples:

```text
Domain Admin
Cloud Global Admin
Root
Database Admin
Network Admin
Local Administrator
Service Accounts
Emergency Accounts
```

## PAM Objectives

```text
Discover Privileged Accounts
Control Privileged Access
Protect Credentials
Monitor Sessions
Record Activity
Enforce Approval
Use Just-in-Time Access
Rotate Secrets
Reduce Standing Privilege
```

## PAM Workflow

```text
Administrator
    ↓
Requests Privileged Access
    ↓
Approval / Policy Check
    ↓
Temporary Credential or Session
    ↓
Privileged System
    ↓
Session Recorded
    ↓
Access Expires
```

## Just-in-Time — JIT

```text
Admin Access
Only when needed
For limited time
```

## Just Enough Administration — JEA

Provide only the required administrative capabilities.

```text
Operator can:
Restart Service

Operator cannot:
Create Users
Change Firewall
Read Secrets
```

---

# 8. Segregation of Duties — SoD

**Segregation of Duties — SoD** divides a sensitive process among different individuals.

```text
Person A
Creates Payment

Person B
Approves Payment
```

Not:

```text
Person A
Creates + Approves + Pays
```

SoD reduces:

```text
Fraud
Insider Abuse
Unauthorized Changes
Accidental Error
Conflict of Interest
```

Examples:

```text
Create Vendor
≠
Approve Vendor

Developer
≠
Production Approver

Access Requestor
≠
Access Approver
```

---

# 9. Two-Person Integrity and Dual Control

## Two-Person Integrity

Requires at least two authorized people to be present or involved.

```text
Sensitive Server Room
     ↓
Two Authorized Staff Required
```

## Dual Control

Requires two independent entities to jointly authorize or complete a sensitive action.

Example:

```text
Critical Encryption Key Recovery
        ↓
Two Custodians Required
```

---

# 10. User Provisioning Lifecycle

User provisioning should follow the **Joiner-Mover-Leaver** model.

```text
Onboarding
Role Change
Offboarding
```

## 10.1 Onboarding

```text
HR Record Created
      ↓
Identity Created
      ↓
Role Identified
      ↓
Manager Approval
      ↓
Minimum Access Assigned
      ↓
MFA Enrolled
      ↓
Access Logged
```

## 10.2 Role Change

```text
Old Role
   ↓
Remove Old Permissions
   ↓
Review New Responsibilities
   ↓
Assign New Permissions
   ↓
Manager / Owner Approval
```

Avoid:

```text
Privilege Creep
```

## 10.3 Offboarding

```text
Termination Trigger
      ↓
Disable Account
      ↓
Revoke Sessions
      ↓
Revoke VPN
      ↓
Remove Cloud Access
      ↓
Revoke Tokens
      ↓
Rotate Shared Secrets
      ↓
Recover Devices
```

---

# 11. Physical Access Controls

## 11.1 Fences

Define and protect a physical perimeter.

Functions:

```text
Deterrent
Preventive
Boundary Definition
```

## 11.2 Gates

Control entry and exit.

May use:

```text
Guard
Card Reader
PIN
Biometric
License Plate Recognition
```

## 11.3 Bollards

Protect facilities from vehicle access or vehicle-based attacks.

## 11.4 Lighting

Improves visibility and supports:

```text
CCTV
Guards
Natural Surveillance
Intrusion Detection
```

## 11.5 Mantraps

Two-door controlled entry area.

```text
Door 1 Opens
   ↓
Person Enters
   ↓
Door 1 Closes
   ↓
Authentication
   ↓
Door 2 Opens
```

## 11.6 Turnstiles

Restrict entry to one person at a time.

Useful against:

```text
Tailgating
Piggybacking
Unauthorized Group Entry
```

## 11.7 CCTV

Provides:

```text
Monitoring
Detection
Deterrence
Evidence
```

## 11.8 Locks

Types include:

```text
Mechanical
Electronic
Combination
Smart Lock
Biometric Lock
```

## 11.9 Security Guards

Can perform:

```text
Identity Verification
Patrol
Incident Response
Visitor Control
Deterrence
Escalation
```

## 11.10 Access Cards

Examples:

```text
Barcode
QR Code
Magnetic Stripe
Proximity Card
Smart Card
Hybrid Card
```

## 11.11 CPTED

**CPTED = Crime Prevention Through Environmental Design**

Core ideas:

```text
Natural Surveillance
Natural Access Control
Territorial Reinforcement
Maintenance
Activity Support
```

---

# 12. Access Card Technologies

## Barcode / QR Code

Advantages:

```text
Cheap
Easy to Issue
```

Limitations:

```text
Easy to Copy
Visible Credential
```

## Magnetic Stripe

Advantages:

```text
Low Cost
Widely Supported
```

Limitations:

```text
Can Be Cloned
Physical Wear
```

## Proximity Card

Contactless credential, commonly RFID-based.

## Smart Card

Contains an embedded chip and can support:

```text
Cryptographic Authentication
Certificates
Strong Identity
```

## Hybrid Card

Combines multiple technologies.

```text
Chip
+
RFID
+
Barcode
+
Magnetic Stripe
```

---

# 13. Technical Access Controls

Examples:

```text
Authentication
Authorization
MFA
Federated Identity
SSO
ACL
RBAC
ABAC
MAC
DAC
PAM
Conditional Access
Session Management
```

---

# 14. Federated Identity

**Federated Identity** allows identities managed by one system to be trusted by another.

```text
Company Identity Provider
        ↓
Federation
        ↓
AWS
Azure
Salesforce
GitHub
Other SaaS
```

## Identity Provider — IdP

Authenticates the user.

Examples:

```text
Microsoft Entra ID
Okta
Google Identity
ADFS
```

## Service Provider — SP

The application trusting the IdP.

Common federation technologies:

```text
SAML 2.0
OpenID Connect
OAuth 2.0
WS-Federation
```

Important:

```text
OAuth 2.0
→ Primarily authorization

OpenID Connect
→ Authentication layer on OAuth 2.0
```

---

# 15. SSO and Federation

**SSO = Single Sign-On**

```text
User
 ↓
Identity Provider
 ↓
Authenticated Once
 ↓
App A
App B
App C
```

Federation establishes trust between identity domains.

SSO often uses federation.

---

# 16. Access Control Models

The major models are:

```text
DAC
RBAC
MAC
Rule-Based Access Control
ABAC
```

## 16.1 Discretionary Access Control — DAC

The owner of an object decides who can access it.

```text
Ahmed owns:
report.docx

Ahmed grants:
Sara → Read
Omar → Read + Write
```

Common implementation:

```text
ACL
```

## 16.2 Role-Based Access Control — RBAC

Permissions are assigned to roles.

```text
User
  ↓
Role
  ↓
Permissions
```

Example:

```text
Role:
DatabaseReader

Permission:
SELECT
```

## 16.3 Mandatory Access Control — MAC

Uses centrally enforced labels and clearances.

Important correction:

> In true MAC, users do not freely grant access merely because they own a file. The system enforces centrally defined security labels and policy.

Example:

```text
Subject Clearance:
SECRET

Object Classification:
TOP SECRET

Decision:
DENY
```

Typical use:

```text
Military
Government
Highly Sensitive Systems
```

## 16.4 Rule-Based Access Control — RuBAC

Decisions are based on predefined rules.

Examples:

```text
Allow only during business hours
Deny from blocked countries
Allow admin only from corporate device
Deny if device is non-compliant
```

## 16.5 Attribute-Based Access Control — ABAC

Uses:

```text
Subject Attributes
Object Attributes
Action
Environment
```

Example:

```text
ALLOW if:

subject.department == "Finance"
AND object.classification <= subject.clearance
AND action == "read"
AND device.compliant == True
AND time < 18:00
```

---

# 17. DAC vs RBAC vs MAC vs Rule-Based vs ABAC

| Model | Decision Based On | Main Controller | Example |
|---|---|---|---|
| DAC | Object ownership | Owner | File permissions |
| RBAC | Role | Administrator | HR role |
| MAC | Labels + clearance | Central authority | Military classification |
| Rule-Based | Rules | Administrator | Time/location restrictions |
| ABAC | Attributes | Policy engine | User + resource + context |

Memory:

```text
DAC
→ Owner decides

RBAC
→ Role decides

MAC
→ Classification decides

Rule-Based
→ Rule decides

ABAC
→ Attributes decide
```

---

# 18. Administrative Access Controls

Examples:

```text
Access Control Policy
Acceptable Use Policy
Password Policy
Provisioning Procedure
Access Review
Background Checks
SoD Policy
PAM Procedure
Termination Procedure
Security Awareness
Change Management
```

## Access Control Policy

Defines:

```text
Who may receive access
Who approves access
How access is reviewed
When access expires
How privileged access is handled
```

## Access Reviews

Review:

```text
Who has access?
Do they still need it?
Is the role correct?
Are permissions excessive?
```

---

# 19. Policy Decision and Enforcement Components

A modern authorization architecture can be viewed as:

```text
User / Subject
      ↓
Policy Enforcement Point
      ↓
Policy Decision Point
      ↓
Policy / Attributes / Context
      ↓
ALLOW / DENY
```

## Policy Enforcement Point — PEP

Intercepts and enforces.

Examples:

```text
API Gateway
Reverse Proxy
Operating System
Cloud IAM
```

## Policy Decision Point — PDP

Evaluates policy.

Examples:

```text
Authorization Engine
IAM Policy Engine
OPA
```

## Policy Information Point — PIP

Provides attributes.

Examples:

```text
User Department
Device Compliance
Risk Score
Resource Classification
Current Time
```

---

# 20. Python Example — Simple Authorization Engine

```python
from dataclasses import dataclass


@dataclass
class AccessRequest:
    subject: str
    action: str
    resource: str


def authorize(request: AccessRequest) -> bool:
    if request.subject == "admin":
        return True

    if request.subject == "analyst":
        return request.action == "read"

    return False


request = AccessRequest(
    subject="analyst",
    action="read",
    resource="security_report",
)

print("ALLOW" if authorize(request) else "DENY")
```

---

# 21. Python Example — RBAC

```python
ROLE_PERMISSIONS = {
    "viewer": {
        "report:read",
    },
    "analyst": {
        "report:read",
        "report:create",
    },
    "admin": {
        "report:read",
        "report:create",
        "report:delete",
        "user:manage",
    },
}

USERS = {
    "ahmed": "analyst",
    "sara": "viewer",
    "omar": "admin",
}


def can(user: str, permission: str) -> bool:
    role = USERS.get(user)

    if role is None:
        return False

    return permission in ROLE_PERMISSIONS.get(role, set())


print(can("ahmed", "report:create"))
print(can("sara", "report:create"))
print(can("omar", "user:manage"))
```

---

# 22. Python Example — ABAC

```python
from dataclasses import dataclass


@dataclass
class Subject:
    department: str
    clearance: int
    device_compliant: bool


@dataclass
class Resource:
    department: str
    classification: int


def abac_authorize(
    subject: Subject,
    resource: Resource,
    action: str,
    hour: int,
) -> bool:

    if action != "read":
        return False

    if subject.department != resource.department:
        return False

    if subject.clearance < resource.classification:
        return False

    if not subject.device_compliant:
        return False

    if not 8 <= hour <= 18:
        return False

    return True


user = Subject(
    department="Finance",
    clearance=3,
    device_compliant=True,
)

file = Resource(
    department="Finance",
    classification=2,
)

print(
    abac_authorize(
        subject=user,
        resource=file,
        action="read",
        hour=10,
    )
)
```

---

# 23. Python Example — SoD

```python
payments = {}


def create_payment(
    user: str,
    payment_id: str,
    amount: float,
) -> None:

    payments[payment_id] = {
        "creator": user,
        "amount": amount,
        "approved_by": None,
    }


def approve_payment(
    user: str,
    payment_id: str,
) -> None:

    payment = payments[payment_id]

    if payment["creator"] == user:
        raise PermissionError(
            "SoD violation: creator cannot approve the same payment."
        )

    payment["approved_by"] = user


create_payment(
    user="ahmed",
    payment_id="P-1001",
    amount=50000,
)

approve_payment(
    user="sara",
    payment_id="P-1001",
)

print(payments["P-1001"])
```

---

# 24. Python Example — User Provisioning

```python
USERS = {}


def onboard_user(username: str, role: str) -> None:
    USERS[username] = {
        "enabled": True,
        "role": role,
    }


def change_role(username: str, new_role: str) -> None:
    if username not in USERS:
        raise KeyError("User does not exist")

    USERS[username]["role"] = new_role


def offboard_user(username: str) -> None:
    if username not in USERS:
        raise KeyError("User does not exist")

    USERS[username]["enabled"] = False
    USERS[username]["role"] = None


onboard_user("ahmed", "developer")
change_role("ahmed", "security_engineer")
offboard_user("ahmed")

print(USERS["ahmed"])
```

A real enterprise offboarding flow would also:

```text
Revoke Sessions
Revoke Tokens
Remove Group Membership
Remove Cloud Roles
Disable VPN
Remove SaaS Access
Record Audit Log
```

---

# 25. Python Example — PAM Checkout Concept

```python
from datetime import datetime, timedelta


class PrivilegedAccess:
    def __init__(self):
        self.sessions = {}

    def grant(
        self,
        user: str,
        role: str,
        minutes: int,
    ):
        expires_at = datetime.utcnow() + timedelta(
            minutes=minutes
        )

        self.sessions[user] = {
            "role": role,
            "expires_at": expires_at,
        }

        return expires_at

    def is_active(self, user: str) -> bool:
        session = self.sessions.get(user)

        if not session:
            return False

        return datetime.utcnow() < session["expires_at"]


pam = PrivilegedAccess()

expiry = pam.grant(
    user="ahmed",
    role="database_admin",
    minutes=30,
)

print("Expires:", expiry)
print("Active:", pam.is_active("ahmed"))
```

Concept:

```text
Request
 ↓
Temporary Privilege
 ↓
Time Limit
 ↓
Automatic Expiration
```

---

# 26. Practical Enterprise Access-Control Architecture

```text
                    Employee
                       ↓
                 Identity Provider
                 MFA / Passkey
                       ↓
                Conditional Access
                       ↓
                  SSO / Federation
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      SaaS           Cloud          Internal
        │              │              │
        ↓              ↓              ↓
       RBAC           ABAC           ACL
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                 Central Logging
                       ↓
                      SIEM
```

Privileged access:

```text
Admin
 ↓
PAM
 ↓
Approval
 ↓
JIT Privilege
 ↓
Session Recording
 ↓
Sensitive System
```

---

# 27. Common Access-Control Failures

## Excessive Privilege

```text
User needs:
Read

User receives:
Full Control
```

## Shared Accounts

Problem:

```text
No Accountability
```

## Orphaned Accounts

Former employees retain access.

## Privilege Creep

Old permissions remain after role changes.

## Weak Offboarding

Accounts remain enabled after termination.

## Weak Service Account Management

Examples:

```text
Never-Expiring Password
Administrator Privilege
No Owner
No Monitoring
```

## Missing MFA

Especially dangerous for privileged accounts.

## Incomplete Logging

Cannot determine:

```text
Who accessed what?
When?
What changed?
```

---

# 28. Access Reviews and Recertification

Periodic access reviews confirm that permissions remain appropriate.

```text
Collect Current Access
       ↓
Send to Manager / Data Owner
       ↓
Approve / Remove / Modify
       ↓
Apply Changes
       ↓
Audit Evidence
```

Priority:

```text
Privileged Accounts
Sensitive Data
Finance
HR
Production
Cloud Admin
Third Parties
```

---

# 29. Access Control in Cloud Environments

## AWS

```text
Users
Roles
Policies
Resource Policies
Permission Boundaries
Service Control Policies
```

## Azure

```text
Microsoft Entra ID
Azure RBAC
Conditional Access
Managed Identities
Privileged Identity Management
```

## Google Cloud

```text
IAM Principals
Roles
Policies
Service Accounts
Conditions
Organization Policies
```

Cloud access-control priorities:

```text
Federation
MFA / Passkeys
Least Privilege
JIT Privilege
Temporary Credentials
Central Logging
Access Reviews
Workload Identity
```

---

# 30. Interview and Exam Questions

## What is a subject?

An active entity requesting access.

## What is an object?

A resource the subject wants to access.

## What is least privilege?

Giving only the minimum permissions necessary.

## What is need to know?

Granting access only to required information.

## What is PAM?

A system and process for controlling, monitoring, and protecting privileged accounts and sessions.

## What is SoD?

Dividing a sensitive process so one person cannot control the whole transaction.

## What is two-person integrity?

A mechanism requiring at least two authorized people to be present or involved.

## What is dual control?

A process requiring two independent entities to complete a sensitive action.

## What is the JML model?

```text
Joiner
Mover
Leaver
```

## What is federated identity?

A trust relationship allowing an identity managed by one system to access another trusted system.

## What is DAC?

Object owners determine access.

## What is RBAC?

Permissions are assigned to roles.

## What is MAC?

A centrally enforced model using labels and clearances.

## What is Rule-Based Access Control?

Access is determined by predefined system rules.

## What is ABAC?

Access is determined using subject, object, action, and environmental attributes.

---

# 31. Final Review Sheet

## Access Decision

```text
Subject
   +
Object
   +
Action
   +
Policy
   ↓
ALLOW / DENY
```

## Security Controls by Implementation

```text
Technical
Physical
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
```

## Defense in Depth

```text
Multiple Security Layers
        ↓
Failure of One Control
        ↓
Other Controls Still Protect
```

## Least Privilege

```text
Minimum Permissions
```

## Need to Know

```text
Minimum Information
```

## PAM

```text
Privileged Account
      ↓
Request
      ↓
Approval
      ↓
Temporary Access
      ↓
Monitoring
      ↓
Expiration
```

## SoD

```text
Person A
Creates

Person B
Approves
```

## User Provisioning

```text
Onboarding
   ↓
Role Change
   ↓
Offboarding
```

## Physical Controls

```text
Fences
Gates
Bollards
Lighting
Mantraps
Turnstiles
CCTV
Locks
Guards
Access Cards
CPTED
```

## Federated Identity

```text
Identity Provider
       ↓
Trust
       ↓
Multiple Applications
```

## Access-Control Models

```text
DAC
→ Owner decides

RBAC
→ Role decides

MAC
→ Clearance + classification

Rule-Based
→ Rule decides

ABAC
→ Attributes decide
```

## RBAC vs ABAC

```text
RBAC:
Role = Security Analyst

ABAC:
Role = Security Analyst
AND Device = Compliant
AND Location = Office
AND Time = Business Hours
AND Resource = Security Data
```

ABAC is usually more context-aware and granular.

---

# End of Document
