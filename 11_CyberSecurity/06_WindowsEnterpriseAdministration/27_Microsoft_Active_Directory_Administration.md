# 27. Microsoft Active Directory Administration

> Phase 6 — Windows Enterprise Administration

Active Directory Domain Services (AD DS) is one of the most important enterprise identity technologies in Windows infrastructure.

The most useful mental model is:

```text
People / Computers / Services
            ↓
      Directory Objects
            ↓
Active Directory Domain Services
            ↓
Authentication + Authorization + Policy
            ↓
Access to Enterprise Resources
```

AD DS is not merely a list of users. It combines:

```text
Directory database
DNS integration
Kerberos authentication
LDAP directory access
Replication
Group Policy
Trusts
Administrative delegation
Auditing
Recovery
```

This course uses Windows Server 2025 as the current reference baseline while explaining concepts that remain highly relevant across Windows Server 2022/2019 environments.

---

## 1. Topic Title

**Microsoft Active Directory Administration**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain AD DS logical and physical architecture using forests, domains, trees, OUs, sites, domain controllers, and Global Catalogs.
- Install AD DS and create a new forest/domain through PowerShell or Server Manager.
- Explain why DNS is fundamental to AD and troubleshoot AD DNS dependencies.
- Create and manage users, computers, groups, and OUs using GUI tools and PowerShell.
- Design group-based authorization using Global, Domain Local, and Universal groups.
- Apply AGDLP/AGUDLP-style access models.
- Explain distinguished names, SIDs, GUIDs, directory partitions, and object identity.
- Visualize Kerberos authentication, TGTs, service tickets, SPNs, NTLM fallback, and LDAP access.
- Create and troubleshoot Group Policy, including LSDOU, inheritance, enforcement, filtering, and loopback.
- Explain Active Directory replication, sites, subnets, KCC topology, and SYSVOL.
- Understand and manage the five FSMO roles.
- Explain trusts, password policies, fine-grained password policies, service accounts, gMSA, and RODCs.
- Understand AD Recycle Bin, System State, authoritative and non-authoritative recovery.
- Apply modern AD security concepts including LDAP signing, NTLM reduction, Windows LAPS, privileged access separation, and advanced auditing.
- Troubleshoot AD using `dcdiag`, `repadmin`, `nltest`, `klist`, `gpresult`, DNS tools, and Event Logs.

---

## 3. Prerequisites

Required:

- 26. Microsoft Windows Server Infrastructure
- Phase 4 networking
- DNS fundamentals
- PowerShell fundamentals

Recommended lab:

```text
Domain: corp.example

DC01
10.60.0.11
Windows Server 2025
AD DS + DNS

DC02
10.60.0.12
Windows Server 2025
AD DS + DNS

CLIENT01
10.60.0.50
Windows 11

MEMBER01
10.60.0.20
Windows Server
```

Domain members should normally use the AD DNS infrastructure:

```text
CLIENT01
 DNS = 10.60.0.11
       10.60.0.12
```

Avoid pointing domain members directly to public resolvers such as arbitrary Internet DNS servers because they do not contain the private AD service records required for domain discovery.

---

## 4. Core Concepts Explanation

# Part 1 — What Active Directory Domain Services Is

### 1. Directory Service

AD DS stores enterprise objects in a structured directory.

```text
Directory
   |
   +-- Users
   +-- Computers
   +-- Groups
   +-- Organizational Units
   +-- Domain Controllers
   +-- Group Policy links
   +-- Service-related objects
```

Example user lookup:

```powershell
Get-ADUser aferganey
```

The directory is distributed across domain controllers.

```text
DC01
  |
  | replication
  |
DC02
```

This allows identity services to remain available when one domain controller is unavailable.

### 2. Authentication vs Authorization

Authentication asks:

```text
Who are you?
```

Authorization asks:

```text
What are you allowed to do?
```

Example:

```text
Ahmed signs in
      ↓
Kerberos authenticates
      ↓
Windows builds security token
      ↓
Token contains user/group SIDs
      ↓
NTFS/SMB ACL evaluates SIDs
      ↓
Access allowed or denied
```

This distinction is fundamental to Active Directory.

---

# Part 2 — Forests, Domains, Trees, and OUs

### 3. Forest

A forest is the highest-level AD DS directory and trust/security boundary.

```text
Forest: corp.example
        |
        +-- Domain: corp.example
```

Forest-wide components include:

```text
Schema
Configuration partition
Forest-wide FSMO roles
Global Catalog search scope
Forest trusts
```

Creating a separate forest is a major security and architecture decision.

### 4. Domain

A domain is a logical directory partition and administrative/security unit.

```text
corp.example
   |
   +-- Users
   +-- Groups
   +-- Computers
   +-- OUs
   +-- Domain Controllers
```

A domain has:

- DNS name
- domain SID
- domain controllers
- Group Policy
- domain-wide FSMO roles
- authentication boundary behaviors

Inspect:

```powershell
Get-ADDomain
```

### 5. Tree

A tree contains domains sharing a contiguous DNS namespace.

```text
corp.example
   |
   +-- egypt.corp.example
   |
   +-- france.corp.example
```

Do not create child domains merely to represent departments.

Most organizations can use OUs instead.

### 6. Organizational Unit

An OU organizes objects for:

```text
Group Policy
Administrative delegation
Operational structure
```

Example:

```text
corp.example
 |
 +-- OU=Egypt
 |      |
 |      +-- OU=Users
 |      +-- OU=Computers
 |      +-- OU=Servers
 |
 +-- OU=France
```

An OU is **not** a security group.

### 7. OU vs Group

```text
OU
"What administrative/policy container is this object in?"

Group
"What security/access collection does this object belong to?"
```

A user exists in one OU location but can belong to many groups.

---

# Part 3 — Domain Controllers and Physical Architecture

### 8. Domain Controller

A Domain Controller hosts AD DS.

```text
Client
  |
  +-- DNS queries
  +-- Kerberos
  +-- LDAP
  +-- Group Policy
  |
  v
Domain Controller
```

Inspect:

```powershell
Get-ADDomainController -Filter *
```

### 9. Multi-master Directory

Most AD changes can occur on multiple writable DCs.

```text
DC01
  |
  | change user Department
  |
  +-------------> replication -------------> DC02

DC02
  |
  | create another user
  |
  +-------------> replication -------------> DC01
```

FSMO roles exist because certain operations need one authoritative role holder.

### 10. Site

An AD Site represents network topology.

```text
Cairo Site
  |
  +-- 10.60.0.0/24
  +-- DC01
  +-- DC02

Alexandria Site
  |
  +-- 10.70.0.0/24
  +-- DC03
```

Sites influence:

- DC discovery
- replication behavior
- service locality

### 11. Subnet Object

AD subnet objects map IP networks to sites.

```text
10.60.0.0/24
      ↓
Cairo
```

If the subnet is missing, a client can be associated with an unexpected site.

Inspect:

```powershell
Get-ADReplicationSubnet -Filter *
```

### 12. Global Catalog

A Global Catalog stores:

```text
full directory data for its own domain
+
partial selected attributes for objects throughout forest
```

Visualization:

```text
Domain A objects ----\
Domain B objects -----+----> Global Catalog searchable view
Domain C objects ----/
```

GC is important for:

- forest-wide searches
- some logon/group operations
- directory-aware applications

Inspect GC DCs:

```powershell
Get-ADForest |
    Select-Object GlobalCatalogs
```

---

# Part 4 — Directory Partitions and Object Identity

### 13. Directory Partitions

Important naming contexts:

```text
Domain partition
Configuration partition
Schema partition
Application partitions
```

Replication scope differs.

```text
Schema
  ↓
forest-wide

Domain partition
  ↓
domain DCs
```

### 14. Distinguished Name

Example:

```text
CN=Ahmed Ferganey,
OU=Engineers,
OU=Egypt,
DC=corp,
DC=example
```

Read it as:

```text
Ahmed Ferganey
    inside Engineers OU
        inside Egypt OU
            inside corp.example
```

PowerShell:

```powershell
Get-ADUser aferganey |
    Select-Object DistinguishedName
```

### 15. SID

A Security Identifier identifies a Windows security principal.

```text
User name can change
      |
      v
SID remains the security identity used by ACLs
```

Inspect:

```powershell
Get-ADUser aferganey -Properties SID |
    Select-Object Name, SID
```

### 16. GUID

AD objects also have a globally unique object identifier.

```powershell
Get-ADUser aferganey -Properties ObjectGUID |
    Select-Object Name, ObjectGUID
```

Concept:

```text
Display name
    can change

ObjectGUID
    stable directory identity
```

---

# Part 5 — Installing AD DS

### 17. Pre-promotion Checklist

Before promoting a server:

```text
Stable hostname
    ↓
Static IP
    ↓
Correct DNS design
    ↓
Correct time
    ↓
Patched OS
    ↓
AD DS role
    ↓
Promotion
```

Avoid changing critical server identity details casually after promotion.

### 18. Install the AD DS Role

```powershell
Install-WindowsFeature `
    AD-Domain-Services `
    -IncludeManagementTools
```

Verify:

```powershell
Get-WindowsFeature AD-Domain-Services
```

### 19. Create a New Forest

**Isolated disposable lab only.**

```powershell
$DSRM = Read-Host `
    "DSRM Password" `
    -AsSecureString

Install-ADDSForest `
    -DomainName "corp.example" `
    -DomainNetbiosName "CORP" `
    -InstallDNS `
    -SafeModeAdministratorPassword $DSRM
```

Visual result:

```text
Before:
Standalone Windows Server

After reboot:
DC01
 |
 +-- AD DS
 +-- DNS
 +-- corp.example forest
 +-- corp.example domain
```

### 20. Verify the Forest

```powershell
Get-ADForest
Get-ADDomain
Get-ADDomainController -Filter *
```

DNS:

```powershell
Get-DnsServerZone
Resolve-DnsName corp.example
```

Health:

```cmd
dcdiag
```

---

# Part 6 — DNS and Active Directory

### 21. Why DNS Is Critical

AD clients use DNS service records to locate domain services.

```text
Client wants a DC
      ↓
DNS SRV query
      ↓
_ldap._tcp.dc._msdcs.corp.example
      ↓
DNS returns domain controllers
      ↓
Client selects/reaches DC
```

A correct A record alone is not enough.

### 22. SRV Records

LDAP/DC locator:

```powershell
Resolve-DnsName `
    _ldap._tcp.dc._msdcs.corp.example `
    -Type SRV
```

Kerberos:

```powershell
Resolve-DnsName `
    _kerberos._tcp.corp.example `
    -Type SRV
```

### 23. Client DNS Architecture

Correct:

```text
CLIENT01
   |
DNS query
   |
DC01 / DC02
   |
AD zone
   |
forward external query if needed
   |
external DNS
```

Incorrect domain-client pattern:

```text
CLIENT01
   |
8.8.8.8
```

Public DNS cannot discover private AD SRV records.

### 24. DNS Troubleshooting

```powershell
Get-DnsClientServerAddress

Resolve-DnsName corp.example

Resolve-DnsName `
    _ldap._tcp.dc._msdcs.corp.example `
    -Type SRV

Get-DnsServerZone
```

Flow:

```text
client points to correct DNS?
        ↓
DNS reachable?
        ↓
zone healthy?
        ↓
SRV records?
        ↓
DC reachable?
```

---

# Part 7 — Joining Computers to the Domain

### 25. Domain Join Flow

```text
CLIENT01
   |
   | DNS locates DC
   |
   | authenticated join
   v
DC01
   |
   +-- creates/uses computer account
   +-- secure channel established
```

PowerShell:

```powershell
Add-Computer `
    -DomainName "corp.example" `
    -Credential "CORP\Administrator" `
    -Restart
```

### 26. Verify Secure Channel

On member computer:

```powershell
Test-ComputerSecureChannel -Verbose
```

Traditional:

```cmd
nltest /sc_verify:corp.example
```

Broken secure channel can cause:

```text
trust relationship errors
authentication issues
domain resource failures
```

---

# Part 8 — OUs and Directory Objects

### 27. Create OU Structure

```powershell
New-ADOrganizationalUnit `
    -Name "Egypt" `
    -Path "DC=corp,DC=example"

New-ADOrganizationalUnit `
    -Name "Users" `
    -Path "OU=Egypt,DC=corp,DC=example"

New-ADOrganizationalUnit `
    -Name "Computers" `
    -Path "OU=Egypt,DC=corp,DC=example"

New-ADOrganizationalUnit `
    -Name "Servers" `
    -Path "OU=Egypt,DC=corp,DC=example"
```

Result:

```text
corp.example
 |
 +-- Egypt
      |
      +-- Users
      +-- Computers
      +-- Servers
```

### 28. Create User

```powershell
$Password = Read-Host `
    "Initial Password" `
    -AsSecureString

New-ADUser `
    -Name "Ahmed Ferganey" `
    -GivenName "Ahmed" `
    -Surname "Ferganey" `
    -SamAccountName "aferganey" `
    -UserPrincipalName "aferganey@corp.example" `
    -Path "OU=Users,OU=Egypt,DC=corp,DC=example" `
    -AccountPassword $Password `
    -Enabled $true `
    -ChangePasswordAtLogon $true
```

Verify:

```powershell
Get-ADUser aferganey -Properties *
```

### 29. Disable and Enable User

```powershell
Disable-ADAccount aferganey
Enable-ADAccount aferganey
```

Offboarding model:

```text
employee leaves
    ↓
disable account
    ↓
remove privileged memberships
    ↓
preserve data/evidence
    ↓
retention process
    ↓
delete according to policy
```

### 30. Move Object

```powershell
Get-ADUser aferganey |
    Move-ADObject `
        -TargetPath "OU=Users,OU=Egypt,DC=corp,DC=example"
```

Moving an object can change:

- delegated administration
- GPO processing
- operational ownership

### 31. Computer Objects

Inspect:

```powershell
Get-ADComputer -Filter * |
    Select-Object Name, Enabled, DistinguishedName
```

A domain-joined computer has a domain computer account and a secure channel password relationship with the domain.

---

# Part 9 — Active Directory Groups

### 32. Security vs Distribution Group

```text
Security Group
    ↓
authorization / ACL

Distribution Group
    ↓
messaging/distribution use
```

Create:

```powershell
New-ADGroup `
    -Name "GG_Finance_Users" `
    -GroupScope Global `
    -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=example"
```

### 33. Group Scopes

Main scopes:

```text
Global
Domain Local
Universal
```

Simplified model:

```text
Global
collect accounts from domain

Domain Local
grant access to resources in domain

Universal
forest-wide membership scenarios
```

### 34. AGDLP

Classic authorization pattern:

```text
A   Accounts
    ↓
G   Global Group
    ↓
DL  Domain Local Group
    ↓
P   Permission
```

Example:

```text
Ahmed
  ↓
GG_Finance_Users
  ↓
DL_FinanceShare_Modify
  ↓
D:\Finance = Modify
```

This separates identity grouping from resource permission.

### 35. AGUDLP

In multi-domain forests:

```text
Accounts
  ↓
Global Group
  ↓
Universal Group
  ↓
Domain Local Group
  ↓
Permission
```

Use Universal groups only when forest-wide grouping requirements justify them.

### 36. Manage Membership

```powershell
Add-ADGroupMember `
    -Identity "GG_Finance_Users" `
    -Members "aferganey"

Get-ADGroupMember "GG_Finance_Users"
```

Nested authorization:

```powershell
Add-ADGroupMember `
    -Identity "DL_FinanceShare_Modify" `
    -Members "GG_Finance_Users"
```

---

# Part 10 — Kerberos Authentication

### 37. Kerberos Architecture

```text
Client
  |
  | authentication
  v
KDC on Domain Controller
  |
  | TGT
  v
Client
  |
  | request service ticket
  v
KDC
  |
  | service ticket
  v
Client ----------------> File Server / Web Service
```

### 38. Ticket Granting Ticket

The TGT proves that the user has successfully authenticated to the KDC and can request tickets for services.

Inspect:

```cmd
klist
```

Look for ticket names associated with the domain.

### 39. Service Ticket

When a user accesses:

```text
\\MEMBER01\Finance
```

Kerberos can issue a ticket for a CIFS SPN.

After access:

```cmd
klist
```

Look for:

```text
cifs/MEMBER01...
```

### 40. SPN

A Service Principal Name maps a service instance to an account/computer identity.

Concept examples:

```text
HOST/server01
CIFS/fileserver
HTTP/webserver
```

Inspect:

```cmd
setspn -L MEMBER01
```

Duplicate or incorrect SPNs can prevent Kerberos and cause NTLM fallback.

### 41. Time

Kerberos requires reasonable clock synchronization.

```cmd
w32tm /query /status
w32tm /query /source
```

Conceptual hierarchy:

```text
authoritative time source
        ↓
PDC Emulator
        ↓
other DCs
        ↓
domain members
```

---

# Part 11 — NTLM and LDAP

### 42. NTLM

NTLM is a legacy Windows authentication family still required by some older systems.

Modern migration goal:

```text
Audit NTLM
   ↓
Find dependency
   ↓
Fix DNS/SPN/application
   ↓
Validate Kerberos
   ↓
Restrict NTLM carefully
```

Do not disable NTLM across production blindly.

### 43. LDAP

LDAP provides directory access.

```text
Application
    |
 LDAP
    |
Domain Controller
    |
AD database
```

Applications can use LDAP for:

- directory searches
- reading attributes
- directory-integrated authentication workflows
- identity lookup

### 44. LDAP Signing

Signing helps protect LDAP communication integrity.

Security rollout:

```text
Audit clients
   ↓
Identify unsigned LDAP dependencies
   ↓
Remediate
   ↓
Test
   ↓
Enforce
```

Windows Server 2025 strengthens LDAP security behavior for new deployments, so legacy integration testing matters.

### 45. LDAP Channel Binding

Channel binding helps protect certain LDAP-over-TLS authentication flows from credential relay-style risks.

The operational lesson:

```text
security setting
   +
client compatibility
   +
application support
```

must be evaluated together.

---

# Part 12 — Group Policy

### 46. GPO Structure

```text
Group Policy Object
       |
       +-- Computer Configuration
       |
       +-- User Configuration
```

A GPO becomes effective through linking and scope.

Possible link locations:

```text
Site
Domain
OU
```

### 47. LSDOU

Simplified processing:

```text
Local
  ↓
Site
  ↓
Domain
  ↓
OU
  ↓
Child OU
```

Mnemonic:

```text
L S D O U
```

Later policy can override conflicting earlier settings unless policy behavior, inheritance, or enforcement changes the result.

### 48. Create and Link GPO

```powershell
New-GPO `
    -Name "Workstation Security Baseline"

New-GPLink `
    -Name "Workstation Security Baseline" `
    -Target "OU=Computers,OU=Egypt,DC=corp,DC=example"
```

Inspect:

```powershell
Get-GPO -All
```

### 49. Update and Result

Client:

```cmd
gpupdate /force
```

Result:

```cmd
gpresult /r
```

HTML report:

```cmd
gpresult /h C:\Temp\gpresult.html
```

PowerShell:

```powershell
Get-GPResultantSetOfPolicy `
    -ReportType Html `
    -Path C:\Temp\rsop.html
```

### 50. Security Filtering

Visual:

```text
OU
 |
 +-- linked GPO
        |
        +-- permissions/security filtering
```

GPO existence and linking alone do not guarantee the policy applies to a particular object.

### 51. Block Inheritance

```text
Domain Policy
    ↓
Parent OU
    ↓
Child OU [Block Inheritance]
```

The child can stop many inherited GPO links.

Use this sparingly.

### 52. Enforced

An enforced GPO link can override lower-level inheritance blocking behaviors.

Concept:

```text
Parent GPO [Enforced]
        ↓
Child OU with Block Inheritance
        ↓
Enforced parent still matters
```

Excessive Enforced + Block Inheritance makes GPO design hard to troubleshoot.

### 53. Loopback Processing

Normal:

```text
user's OU
   ↓
user policy
```

Loopback:

```text
user signs into special computer
        ↓
computer's policy context
        ↓
user policy altered/replaced
```

Common use cases:

```text
RDS server
kiosk
training room
shared workstation
```

Modes:

```text
Merge
Replace
```

### 54. ADMX Central Store

Conceptual path:

```text
\\corp.example\SYSVOL\corp.example\Policies\PolicyDefinitions
```

Central Store lets administrators use consistent Administrative Template files.

Manage ADMX versions carefully.

---

# Part 13 — Replication

### 55. Multi-master Replication

```text
DC01
  |
 change
  |
  +------ replication ------> DC02
```

AD keeps replication metadata to identify versions/origins and resolve update ordering.

### 56. repadmin

Summary:

```cmd
repadmin /replsummary
```

Detailed partner information:

```cmd
repadmin /showrepl DC01
```

Manual synchronization in a lab:

```cmd
repadmin /syncall /AdeP
```

Do not use manual sync commands as a substitute for fixing persistent DNS/network/topology problems.

### 57. KCC

The Knowledge Consistency Checker helps create replication topology.

```text
DC1 ------ DC2
 |          |
 |          |
DC3 ------ DC4
```

The KCC calculates appropriate connection objects based on site topology.

Administrators should define correct:

- sites
- subnets
- site links

rather than manually controlling every connection.

### 58. Intra-site Replication

Designed for fast/reliable LAN connectivity.

```text
Site Cairo
  |
  +-- DC01
  +-- DC02
```

### 59. Inter-site Replication

Uses site topology and link-cost/schedule concepts.

```text
Cairo Site
   |
 WAN
   |
Alexandria Site
```

This is one reason IP subnet mapping must be accurate.

### 60. Sites and Subnets

Inspect:

```powershell
Get-ADReplicationSite -Filter *
Get-ADReplicationSubnet -Filter *
Get-ADReplicationSiteLink -Filter *
```

Create lab site:

```powershell
New-ADReplicationSite `
    -Name "Alexandria"
```

Map subnet:

```powershell
New-ADReplicationSubnet `
    -Name "10.70.0.0/24" `
    -Site "Alexandria"
```

---

# Part 14 — SYSVOL and Group Policy Replication

### 61. SYSVOL

SYSVOL stores domain-wide policy/script files.

```text
\\corp.example\SYSVOL
```

Concept:

```text
GPO
  |
  +-- AD object metadata
  |
  +-- SYSVOL files
```

Both sides need to replicate correctly.

### 62. DFS Replication

Modern AD domains use DFS Replication for SYSVOL.

```text
DC01 SYSVOL
     |
     | DFSR
     v
DC02 SYSVOL
```

If directory replication is healthy but SYSVOL is inconsistent, Group Policy can behave inconsistently.

---

# Part 15 — FSMO Roles

### 63. Five Roles

Forest-wide:

```text
Schema Master
Domain Naming Master
```

Domain-wide:

```text
RID Master
PDC Emulator
Infrastructure Master
```

### 64. Locate FSMO Roles

```powershell
Get-ADForest |
    Select-Object `
        SchemaMaster,
        DomainNamingMaster

Get-ADDomain |
    Select-Object `
        RIDMaster,
        PDCEmulator,
        InfrastructureMaster
```

Traditional:

```cmd
netdom query fsmo
```

### 65. Schema Master

Controls operations that modify the AD schema.

```text
Application requiring schema extension
        ↓
Schema Master operation
        ↓
schema replication
```

Schema changes are high-impact forest-wide changes.

### 66. Domain Naming Master

Controls certain changes to the forest domain namespace.

Concept:

```text
Add/remove domain
        ↓
Domain Naming Master
```

### 67. RID Master

Security principal SID:

```text
Domain SID + RID
```

The RID Master allocates RID pools to domain controllers.

```text
RID Master
   |
   +-- RID pool -> DC01
   +-- RID pool -> DC02
```

### 68. PDC Emulator

Important functions include:

- password-change coordination
- domain time hierarchy role
- certain legacy compatibility behavior
- important administrative/GPO-related coordination

Monitor this role carefully.

### 69. Infrastructure Master

Tracks certain cross-domain reference updates.

Its practical impact depends on forest/domain/GC design.

### 70. Transfer vs Seizure

Transfer:

```text
old role holder healthy
        ↓
controlled handoff
```

Seize:

```text
old role holder permanently lost
        ↓
emergency takeover
```

Transfer example:

```powershell
Move-ADDirectoryServerOperationMasterRole `
    -Identity "DC02" `
    -OperationMasterRole PDCEmulator
```

Do not seize roles when a healthy transfer is possible.

---

# Part 16 — Trusts

### 71. Trust Concept

```text
Domain A
   |
 trust
   |
Domain B
```

A trust enables authentication relationships across boundaries.

Trust does **not** automatically give resource permissions.

```text
Trust
  ↓
identity can be authenticated

ACL/group permission
  ↓
resource access authorized
```

### 72. One-way and Two-way Trust

```text
A trusts B
one-way

A trusts B
and
B trusts A
two-way
```

Always define the trust direction in terms of which domain accepts identities from which side.

### 73. Transitivity

```text
transitive
trust can extend through domain hierarchy/relationship

non-transitive
limited direct relationship
```

Do not assume every trust type behaves the same.

### 74. Forest Trust

```text
Forest A
   ⇄
Forest B
```

Forest trusts are significant security relationships.

Design:

- authentication scope
- SID filtering/controls
- resource authorization
- DNS name resolution
- administrative ownership

carefully.

---

# Part 17 — Password and Account Policy

### 75. Default Domain Password Policy

Inspect:

```powershell
Get-ADDefaultDomainPasswordPolicy
```

Policy can include:

```text
minimum password length
password history
complexity
minimum/maximum age
account lockout
```

### 76. Account Lockout

Tradeoff:

```text
too permissive
   ↓
brute-force exposure

too aggressive
   ↓
users/attackers can trigger lockouts
```

Choose policy through organizational security requirements rather than arbitrary copied numbers.

### 77. Fine-Grained Password Policy

Different groups can have different policies.

```text
Normal Users
    ↓
Default Domain Policy

Privileged Admins
    ↓
Fine-Grained Password Policy
```

Inspect:

```powershell
Get-ADFineGrainedPasswordPolicy -Filter *
```

Resultant policy:

```powershell
Get-ADUserResultantPasswordPolicy aferganey
```

---

# Part 18 — Delegated Administration

### 78. Delegation Model

Bad:

```text
Help Desk
   ↓
Domain Admins
```

Better:

```text
Help Desk Group
   ↓
delegated rights
   ↓
OU=Egypt,OU=Users
   ↓
reset password / unlock accounts only
```

### 79. Delegation of Control

Concept:

```text
OU ACL
  |
  +-- HelpDesk = Reset Password
  +-- HR Admin = selected user attributes
```

Use:

- Delegation of Control Wizard
- controlled ACL design

Avoid broad rights at the domain root.

---

# Part 19 — Service Accounts and gMSA

### 80. Traditional Service-account Problem

```text
svc_app
   |
static password
   |
Server1
Server2
Server3
```

Problems:

- manual rotation
- password stored in config
- service interruption
- password reuse
- broad privileges

### 81. gMSA

Group Managed Service Account:

```text
AD DS
  |
managed password
  |
gMSA
  |
authorized servers/services
```

Inspect:

```powershell
Get-ADServiceAccount -Filter *
```

gMSA helps remove direct manual password lifecycle management for supported services.

Implement KDS and host authorization according to current Microsoft documentation.

---

# Part 20 — Read-Only Domain Controllers

### 82. RODC

An RODC has a read-only copy of AD DS.

Common branch concept:

```text
HQ
 |
WAN
 |
Branch Office
   |
 RODC
```

Useful where:

- physical security is weaker
- WAN is limited
- local IT administration is constrained

### 83. Password Replication Policy

RODC can cache selected credentials according to policy.

```text
Branch user logs on
     ↓
RODC needs credential
     ↓
Password Replication Policy
     ↓
cache allowed or denied
```

Privileged accounts should not be casually cacheable on branch RODCs.

---

# Part 21 — Functional Levels

### 84. Domain and Forest Functional Levels

Functional levels determine available AD DS features and supported domain-controller OS compatibility.

```text
Forest Functional Level
       |
       +-- Domain A Functional Level
       +-- Domain B Functional Level
```

Inspect:

```powershell
Get-ADForest |
    Select-Object ForestMode

Get-ADDomain |
    Select-Object DomainMode
```

Before raising:

```text
all DC versions supported?
applications compatible?
backup/recovery ready?
change reviewed?
```

---

# Part 22 — Windows LAPS

### 85. Shared Local Administrator Password Risk

Bad:

```text
PC01 local admin = Password123
PC02 local admin = Password123
SRV01 local admin = Password123
```

Compromise one:

```text
one credential
   ↓
many systems exposed
```

### 86. Windows LAPS

Concept:

```text
Managed computer
      |
generates/rotates local admin password
      |
directory storage
      |
authorized admins retrieve
```

Benefits:

- unique password per device
- automatic rotation
- delegated retrieval permissions
- reduced shared-password risk

Use current Windows LAPS policy and directory-preparation guidance.

---

# Part 23 — Active Directory Certificate Services Foundations

### 87. Why Certificates Matter

Certificates can support:

```text
TLS
user/device authentication
802.1X
smart card logon
IPsec
code signing
```

AD CS can provide enterprise PKI.

### 88. CA Hierarchy

Typical conceptual architecture:

```text
Offline Root CA
      |
      v
Issuing CA
  /    |    \
User Server Device certificates
```

The root CA is extremely high value.

### 89. Certificate Templates

Template defines:

```text
who can enroll
what key usage
subject naming
cryptography
validity
autoenrollment
```

Misconfigured certificate-template permissions can create major security risks.

Treat PKI configuration as Tier-0/high-value infrastructure.

---

# Part 24 — Backup and Recovery

### 90. System State

Domain-controller recovery requires AD-aware backup.

Conceptually includes critical components such as:

```text
AD DS
SYSVOL
registry
boot/system state
```

Use supported backup methods and test restores.

### 91. AD Recycle Bin

Concept:

```text
User accidentally deleted
        ↓
Deleted Objects
        ↓
restore object
        ↓
many attributes/memberships preserved
```

Inspect:

```powershell
Get-ADOptionalFeature `
    -Filter 'Name -like "Recycle Bin Feature"'
```

Do not confuse Recycle Bin with full disaster recovery.

### 92. Non-authoritative Restore

```text
Restore DC from backup
       ↓
DC returns
       ↓
healthy DCs replicate newer directory data to it
```

### 93. Authoritative Restore

Used when selected restored data must be reintroduced as authoritative and replicate outward.

This is a specialist recovery procedure.

Practice only in disposable labs and follow current Microsoft recovery documentation.

### 94. Recovery Planning

A real plan includes:

```text
backup schedule
restore procedure
DSRM credentials
FSMO recovery
DNS recovery
SYSVOL recovery
AD Recycle Bin
test restore
documentation
```

---

# Part 25 — Auditing

### 95. Audit Policy

Inspect:

```cmd
auditpol /get /category:*
```

Important categories can include:

```text
Account Logon
Logon/Logoff
Account Management
DS Access
Policy Change
Privilege Use
```

### 96. Security Event Flow

```text
Authentication / AD change
          ↓
Security Event Log
          ↓
Windows Event Forwarding / agent
          ↓
SIEM
          ↓
alert / investigation
```

Identity infrastructure should have centralized monitoring.

### 97. Directory Object Auditing

Advanced auditing can help identify:

- privileged group membership changes
- user creation/deletion
- sensitive directory-object changes
- authentication anomalies

Audit design must balance useful visibility with event volume.

---

# Part 26 — Active Directory Security

### 98. Protect Domain Admin Credentials

Bad:

```text
Domain Admin
   ↓ logs into
ordinary user laptop
   ↓
high-value credential material reaches lower-trust endpoint
```

Better:

```text
Privileged Admin Account
        ↓
Privileged Access Workstation
        ↓
Domain Controller / Tier 0
```

### 99. Separate Normal and Administrative Accounts

Example:

```text
Normal:
aferganey

Privileged:
adm-aferganey
```

Normal account:

```text
email
browser
business apps
```

Privileged account:

```text
controlled admin tasks only
```

### 100. Privileged Tiering Concept

```text
Tier 0
Identity control plane
DCs / PKI / privileged identity

Tier 1
Servers / applications

Tier 2
User workstations
```

Higher-trust credentials should not be exposed to lower-trust systems.

### 101. Reduce NTLM

Security migration:

```text
audit
 ↓
find old application
 ↓
correct DNS/SPN/auth design
 ↓
verify Kerberos
 ↓
restrict NTLM
```

### 102. Secure LDAP

Goals:

```text
LDAP signing
channel binding
TLS where required
strong authentication
```

Security should be strengthened without silently breaking legacy applications.

### 103. Protect SMB and Remote Admin

AD security depends on surrounding infrastructure.

```text
AD
 |
 +-- secure SMB
 +-- secure WinRM
 +-- restricted RDP
 +-- firewall segmentation
 +-- endpoint protection
 +-- patching
 +-- DNS security
```

A secure directory cannot compensate for insecure servers and workstations.

---

# Part 27 — PowerShell Automation

### 104. Bulk User Input

CSV:

```csv
GivenName,Surname,SamAccountName,OU
Sara,Ali,sali,"OU=Users,OU=Egypt,DC=corp,DC=example"
Omar,Hassan,ohassan,"OU=Users,OU=Egypt,DC=corp,DC=example"
```

PowerShell:

```powershell
$Users = Import-Csv C:\Admin\users.csv

foreach ($User in $Users) {

    $Password = Read-Host `
        "Password for $($User.SamAccountName)" `
        -AsSecureString

    New-ADUser `
        -Name "$($User.GivenName) $($User.Surname)" `
        -GivenName $User.GivenName `
        -Surname $User.Surname `
        -SamAccountName $User.SamAccountName `
        -UserPrincipalName "$($User.SamAccountName)@corp.example" `
        -Path $User.OU `
        -AccountPassword $Password `
        -Enabled $true
}
```

Do not store reusable plaintext production passwords in CSV files.

### 105. User Inventory

```powershell
Get-ADUser `
    -Filter * `
    -Properties Enabled, Department, LastLogonDate |
    Select-Object `
        Name,
        SamAccountName,
        Enabled,
        Department,
        LastLogonDate |
    Export-Csv `
        C:\Admin\ADUsers.csv `
        -NoTypeInformation
```

### 106. Disabled Accounts

```powershell
Search-ADAccount `
    -AccountDisabled `
    -UsersOnly |
    Select-Object `
        Name,
        SamAccountName,
        DistinguishedName
```

Treat this as investigation input, not automatic deletion criteria.

### 107. Locked-out Accounts

```powershell
Search-ADAccount -LockedOut -UsersOnly
```

Investigate why lockout occurred before simply unlocking repeatedly.

---

# Part 28 — Troubleshooting Toolkit

### 108. dcdiag

```cmd
dcdiag
dcdiag /v
dcdiag /test:dns
```

Use it to evaluate DC health categories.

### 109. repadmin

```cmd
repadmin /replsummary
repadmin /showrepl
```

Replication failure dependency chain:

```text
DNS
 ↓
IP route
 ↓
RPC/firewall
 ↓
time/authentication
 ↓
AD replication
```

### 110. nltest

DC discovery:

```cmd
nltest /dsgetdc:corp.example
```

Secure channel:

```cmd
nltest /sc_verify:corp.example
```

### 111. klist

```cmd
klist
```

Inspect:

- TGT
- service tickets
- SPNs
- encryption types

Kerberos troubleshooting should verify whether the client actually obtained the intended service ticket.

### 112. gpresult

```cmd
gpresult /r
gpresult /h C:\Temp\gp.html
```

GPO troubleshooting:

```text
GPO exists?
 ↓
linked?
 ↓
object in correct OU?
 ↓
security filter?
 ↓
WMI filter?
 ↓
inheritance/enforced?
 ↓
DC/SYSVOL reachable?
 ↓
policy actually applied?
```

### 113. DNS Checks

```powershell
Resolve-DnsName `
    _ldap._tcp.dc._msdcs.corp.example `
    -Type SRV

Get-DnsClientServerAddress

ipconfig /all
```

Many AD failures are DNS failures in disguise.

### 114. Time Checks

```cmd
w32tm /query /status
w32tm /query /source
```

Authentication can fail when domain time is unhealthy.

### 115. Event Logs

Important sources can include:

```text
Directory Service
DNS Server
DFS Replication
System
Security
GroupPolicy Operational
```

PowerShell:

```powershell
Get-WinEvent `
    -LogName 'Directory Service' `
    -MaxEvents 30
```

### 116. Domain Join Failure Flow

```text
IP correct?
 ↓
DNS points to AD DNS?
 ↓
corp.example resolves?
 ↓
SRV records resolve?
 ↓
time correct?
 ↓
DC reachable?
 ↓
credentials/rights?
 ↓
computer account conflict?
```

Commands:

```powershell
Get-NetIPConfiguration
Resolve-DnsName corp.example
Test-NetConnection DC01 -Port 53
Test-NetConnection DC01 -Port 88
```

### 117. Authentication Failure Flow

```text
Account enabled?
 ↓
locked?
 ↓
DNS/DC discovery?
 ↓
time?
 ↓
Kerberos ticket?
 ↓
SPN?
 ↓
authorization?
```

PowerShell:

```powershell
Get-ADUser aferganey `
    -Properties LockedOut, Enabled

Search-ADAccount -LockedOut

klist

nltest /dsgetdc:corp.example
```

### 118. Replication Failure Flow

```text
Can DCs resolve each other?
      ↓
Can they route/reach required services?
      ↓
Time correct?
      ↓
Corrupt/stale DNS?
      ↓
repadmin evidence?
      ↓
Directory Service events?
```

Commands:

```cmd
repadmin /replsummary
repadmin /showrepl
dcdiag /test:dns
```

---


# Enhanced Deep-Study Layer — Active Directory Identity Engineering

The original course is preserved below. This enhanced layer expands AD DS into a deeper identity-engineering and security-administration course with directory internals, DNS dependency, Kerberos, LDAP, replication, sites, GPO processing, FSMO, trusts, service identities, recovery, auditing, privileged-access design, and defensive troubleshooting.

The core identity model is:

```text
Identity object
   ↓
Authentication
   ↓
Security token / claims / tickets
   ↓
Authorization groups and ACLs
   ↓
Policy
   ↓
Access to resource
```

The core AD infrastructure model is:

```text
DNS
  ↓
DC discovery
  ↓
Kerberos / LDAP / SMB / RPC
  ↓
Domain Controller
  ↓
NTDS database + SYSVOL
  ↓
Replication
  ↓
Other DCs
```

Many "Active Directory problems" are actually failures in:

```text
DNS
time
network
replication
secure channel
SPN
Group Policy scope
or authorization design
```

Therefore troubleshoot by dependency, not by randomly resetting accounts.

---

## Enhanced Deep Dive 1 — AD DS Is a Distributed Identity System

AD DS combines:

```text
directory
authentication
authorization support
policy
replication
service discovery
trust
```

It is distributed:

```text
DC01
  ↕ replication
DC02
  ↕ replication
DC03
```

A writable domain controller holds a replica of domain data and participates in authentication/replication.

---

## Enhanced Deep Dive 2 — Logical vs Physical Architecture

Logical:

```text
Forest
 └── Domain
     └── OU
         └── Objects
```

Physical:

```text
Sites
 ├── subnets
 ├── domain controllers
 └── replication links
```

This distinction is fundamental.

OU structure answers:

```text
administration + policy
```

Sites answer:

```text
network locality + replication topology
```

Do not use OUs as if they were network sites.

---

## Enhanced Deep Dive 3 — Forest as Security Boundary

Forest contains:

```text
schema
configuration partition
forest-wide trusts
enterprise-level identity control
forest FSMO roles
```

Administrators with sufficiently powerful forest-wide rights can affect all domains in the forest.

Therefore:

```text
separate forest
```

is a major security boundary decision, not just an organizational folder choice.

---

## Enhanced Deep Dive 4 — Domain as Replication and Policy Boundary

A domain has:

```text
domain naming context
domain SID
domain controllers
domain-wide FSMO roles
domain password policy
domain GPOs/OUs
```

A domain is not simply a department.

Creating additional domains increases:

```text
DNS complexity
trust relationships
administration
replication design
backup/recovery scope
```

Use OUs unless a real domain boundary requirement exists.

---

## Enhanced Deep Dive 5 — Tree

Tree:

```text
corp.example
├── egypt.corp.example
└── france.corp.example
```

Domains share a contiguous DNS namespace.

A forest can contain more than one tree.

The important lesson:

```text
DNS namespace design
≠
organizational chart
```

---

## Enhanced Deep Dive 6 — OU Design Principles

Good OU design should support:

```text
delegation
GPO scope
administrative ownership
computer/user separation
server/workstation separation
```

Example:

```text
corp.example
├── Workstations
│   ├── Cairo
│   └── Alexandria
├── Servers
│   ├── Member
│   └── Application
├── Users
└── ServiceAccounts
```

Avoid creating hundreds of OUs solely because the HR organization chart has hundreds of teams.

---

## Enhanced Deep Dive 7 — OU Is Not a Security Group

OU:

```text
one directory location
```

Group:

```text
membership-based authorization collection
```

User:

```text
exists in one OU
belongs to many groups
```

Moving an object changes:

```text
GPO scope
delegated administration
```

but does not automatically grant file access.

---

## Enhanced Deep Dive 8 — Directory Object Classes

Objects are instances of schema classes:

```text
user
computer
group
organizationalUnit
contact
service-related objects
```

Each class defines allowed/required attributes.

Example:

```powershell
Get-ADUser aferganey -Properties *
```

The schema controls what attributes the directory understands.

---

## Enhanced Deep Dive 9 — Schema

Schema defines:

```text
object classes
attributes
syntax
relationships
```

Schema changes are forest-wide and difficult to reverse casually.

Applications such as enterprise messaging/identity products may extend schema.

Treat schema modification as:

```text
high-impact change
```

with backup, testing, vendor support, and change control.

---

## Enhanced Deep Dive 10 — Configuration Partition

The Configuration naming context stores forest-wide configuration such as:

```text
sites
services
partitions
replication-related configuration
```

It replicates forest-wide.

This is why site topology is visible across the forest.

---

## Enhanced Deep Dive 11 — Domain Partition

The domain naming context stores domain-specific objects:

```text
users
groups
computers
OUs
domain policy-related objects
```

It replicates to domain controllers in that domain.

---

## Enhanced Deep Dive 12 — Application Partitions

AD-integrated applications can use application directory partitions with customized replication scope.

DNS can use AD-integrated application partitions.

Concept:

```text
DNS application data
→ replicated only to selected DNS/DC scope
```

This helps separate data from the normal domain naming context.

---

## Enhanced Deep Dive 13 — Distinguished Name

Example:

```text
CN=Ahmed Ferganey,
OU=Engineers,
OU=Egypt,
DC=corp,
DC=example
```

This is an LDAP path describing object position.

Moving the user changes DN.

The object identity itself can remain the same.

---

## Enhanced Deep Dive 14 — RDN

Relative Distinguished Name is the first component relative to its parent.

Example:

```text
CN=Ahmed Ferganey
```

inside:

```text
OU=Engineers,OU=Egypt,DC=corp,DC=example
```

Renaming an object changes the RDN/DN but not necessarily SID/ObjectGUID.

---

## Enhanced Deep Dive 15 — SID

Security Identifier:

```text
S-1-5-21-...
```

Authorization model:

```text
user/group SID
  ↓
security token
  ↓
ACL ACE references SID
```

Names are for humans.

SIDs are security identities.

---

## Enhanced Deep Dive 16 — RID

Domain security principal SID:

```text
Domain SID + RID
```

Each DC receives RID pools so it can create new principals without contacting RID Master for every object.

The RID Master manages allocation of RID pools.

---

## Enhanced Deep Dive 17 — ObjectGUID

ObjectGUID is a stable directory object identifier.

```powershell
Get-ADUser aferganey -Properties ObjectGUID |
  Select-Object Name,ObjectGUID
```

Useful when:

```text
name changes
object moves
DN changes
```

---

## Enhanced Deep Dive 18 — sAMAccountName vs UPN

`sAMAccountName`:

```text
legacy-compatible logon name
CORP\aferganey
```

UPN:

```text
aferganey@corp.example
```

UPN resembles email but is a separate identity attribute unless intentionally aligned.

Enterprise design often prefers user-friendly UPN suffixes.

---

## Enhanced Deep Dive 19 — Domain Controller Role

DC provides:

```text
LDAP
Kerberos KDC
Netlogon
AD database
replication
often DNS
SYSVOL/Group Policy access
```

A DC is high-value infrastructure.

Avoid installing unnecessary applications/roles on domain controllers.

---

## Enhanced Deep Dive 20 — NTDS Database

AD database file is commonly associated with:

```text
NTDS.dit
```

It stores directory database contents.

Protect DC storage because compromise of DC/database can expose highly sensitive identity material.

Do not copy or manipulate AD database files manually outside supported backup/recovery procedures.

---

## Enhanced Deep Dive 21 — SYSVOL

SYSVOL contains domain-shared policy/script content.

GPO has two broad components:

```text
Group Policy Container
→ AD object/metadata

Group Policy Template
→ SYSVOL files
```

Healthy Group Policy requires both directory and SYSVOL replication.

---

## Enhanced Deep Dive 22 — DFSR for SYSVOL

Modern domains use DFS Replication for SYSVOL.

```text
DC01 SYSVOL
  ↕ DFSR
DC02 SYSVOL
```

If AD replication works but DFSR/SYSVOL does not:

```text
GPO metadata may exist
but files/templates/scripts can be inconsistent
```

Check both.

---

## Enhanced Deep Dive 23 — AD Database Transaction and Replication Model

Local change:

```text
write on DC01
   ↓
AD database commit
   ↓
replication metadata updated
   ↓
DC02 learns change
```

Replication is not "copy the entire database every time."

It transfers changes using metadata and update tracking.

---

## Enhanced Deep Dive 24 — USN Awareness

Domain controllers track local update sequence numbers.

Concept:

```text
change 1 → USN 1001
change 2 → USN 1002
...
```

Replication partners use metadata to know which changes they have seen.

Do not manipulate VM/DC snapshots in unsupported ways that can interfere with directory replication state.

---

## Enhanced Deep Dive 25 — Invocation ID Awareness

A DC has replication identity metadata including an invocation ID.

When certain supported restore/virtualization events occur, AD can protect replication consistency by changing relevant identity state.

The key principle:

```text
domain controller virtualization/restore
must use supported methods
```

not generic "copy VM folder and boot both."

---

## Enhanced Deep Dive 26 — Multi-Master Replication

Most writable objects can be modified on more than one DC.

```text
DC01 changes telephoneNumber
DC02 creates user
```

Both replicate.

Some specialized operations require FSMO role holders.

Multi-master improves availability but requires conflict-resolution rules.

---

## Enhanced Deep Dive 27 — Replication Metadata

An AD attribute change carries metadata such as:

```text
version
originating DC
originating timestamp
originating USN
```

Tools can expose metadata in advanced troubleshooting.

This helps answer:

```text
where did this change originate?
which version won?
```

---

## Enhanced Deep Dive 28 — Conflict Resolution Awareness

If the same attribute changes on different DCs before replication, AD uses replication metadata rules to converge.

Do not rely on "last clock time wins" as a simplistic model.

Correct time is still critical for authentication/log analysis, but replication convergence uses structured metadata.

---

## Enhanced Deep Dive 29 — Tombstone / Deleted Object Lifecycle

Deleted objects are retained in directory lifecycle states for replication/recovery behavior.

AD Recycle Bin improves restoration capability.

Do not treat deletion as immediate permanent physical erasure.

Deletion lifecycle matters to:

```text
replication
restore
lingering objects
```

---

## Enhanced Deep Dive 30 — Lingering Object Awareness

If a DC remains disconnected beyond supported deletion/replication windows and later returns incorrectly, stale objects can create consistency issues.

The lesson:

```text
do not keep old disconnected DCs and simply reconnect them months later
```

Follow supported demotion/rebuild/recovery procedures.

---

## Enhanced Deep Dive 31 — DNS Service Discovery

Clients locate DCs using SRV records.

Example:

```text
_ldap._tcp.dc._msdcs.corp.example
```

Flow:

```text
client
  ↓ SRV query
AD DNS
  ↓ candidate DCs
client
  ↓ site-aware selection
DC
```

A ping to the domain name is not enough to validate AD DNS.

---

## Enhanced Deep Dive 32 — AD-Integrated DNS

AD-integrated zone data replicates through AD rather than traditional zone-transfer-only models.

Benefits:

```text
multi-master updates
secure dynamic updates
AD replication scope
```

This tightly connects DNS health and AD health.

---

## Enhanced Deep Dive 33 — `_msdcs`

`_msdcs` namespace contains critical DC locator/forest service records.

When troubleshooting:

```powershell
Resolve-DnsName `
  _ldap._tcp.dc._msdcs.corp.example `
  -Type SRV
```

also verify:

```text
returned DC names resolve to correct IPs
```

---

## Enhanced Deep Dive 34 — Dynamic DNS Registration

Domain controllers and clients can dynamically register records according to DNS configuration/policy.

Useful client command:

```cmd
ipconfig /registerdns
```

But do not use it as a substitute for fixing:

```text
wrong DNS suffix
wrong resolver
zone security
service failure
```

---

## Enhanced Deep Dive 35 — DNS Forwarders

AD DNS often handles internal zones and forwards external queries.

Architecture:

```text
Domain client
  ↓
AD DNS
  ├── corp.example authoritative
  └── external name
         ↓ forwarder/upstream resolver
```

This lets domain members use one internal DNS path without pointing directly to public DNS.

---

## Enhanced Deep Dive 36 — Conditional Forwarding Awareness

For multiple DNS namespaces/forests:

```text
corp.example DNS
  ↓ for partner.example
conditional forwarder
  ↓ partner DNS servers
```

This can support trust/name-resolution requirements.

DNS connectivity is required for many inter-domain/forest operations.

---

## Enhanced Deep Dive 37 — DC Locator and Sites

Client IP:

```text
10.60.0.50
```

AD subnet object:

```text
10.60.0.0/24 → Cairo
```

DC Locator can prefer:

```text
Cairo DC
```

instead of a distant site.

Missing/misconfigured subnet can cause:

```text
WAN authentication
slow logon
wrong DC selection
unexpected replication/client traffic
```

---

## Enhanced Deep Dive 38 — Sites Are Network Topology

Site should usually represent:

```text
well-connected network region
```

not business department.

Examples:

```text
Cairo-DC
Alexandria-Branch
Frankfurt-DC
```

Use site links to express WAN replication connectivity.

---

## Enhanced Deep Dive 39 — Site Link Cost

Cost is a relative preference.

Lower-cost path is generally preferred by topology calculations.

Think:

```text
Cairo ↔ Frankfurt cost 100
Cairo ↔ London    cost 200
```

Cost is not measured milliseconds automatically.

It is an administrative topology value.

---

## Enhanced Deep Dive 40 — Replication Schedule

Inter-site replication can be scheduled.

Trade-off:

```text
frequent replication
→ fresher directory
→ more WAN traffic

less frequent
→ reduced WAN usage
→ slower convergence
```

Identity/security changes may need fast convergence, so schedule design should reflect business requirements.

---

## Enhanced Deep Dive 41 — KCC

Knowledge Consistency Checker builds replication topology using site configuration.

Do not manually create every connection object because the KCC already solves topology in normal designs.

Manual topology changes should be exceptional and documented.

---

## Enhanced Deep Dive 42 — `repadmin /replsummary`

Use:

```cmd
repadmin /replsummary
```

to answer:

```text
which DCs have replication errors?
how long since success?
which direction?
```

It is a summary, not a full root-cause diagnosis.

---

## Enhanced Deep Dive 43 — `repadmin /showrepl`

Use:

```cmd
repadmin /showrepl DC01
```

to inspect inbound replication neighbors per naming context.

Correlate failures with:

```text
DNS
RPC
firewall
time
authentication
site topology
```

---

## Enhanced Deep Dive 44 — `dcdiag`

`dcdiag` runs domain-controller diagnostics.

Examples:

```cmd
dcdiag
dcdiag /v
dcdiag /test:dns
```

Treat its results as evidence.

Do not "fix every warning" without understanding whether it is relevant to your architecture.

---

## Enhanced Deep Dive 45 — Domain Join Internals

Join creates/uses a computer account and secure channel.

Simplified:

```text
client DNS finds DC
  ↓
join credentials authorized
  ↓
computer account created/reset
  ↓
machine secret established
  ↓
secure channel
```

Computer account has a password too, managed automatically.

---

## Enhanced Deep Dive 46 — Secure Channel

Member computer and domain maintain machine-account trust.

Check:

```powershell
Test-ComputerSecureChannel -Verbose
```

or:

```cmd
nltest /sc_verify:corp.example
```

Broken secure channel can produce:

```text
trust relationship failed
domain authentication issues
```

Repair should follow supported procedures after confirming DNS/time/connectivity.

---

## Enhanced Deep Dive 47 — Computer Account Lifecycle

Computer object has:

```text
SID
password relationship
DNS/service registration
group memberships
OU/GPO scope
```

Deleting/rejoining a computer should not be the first troubleshooting step.

It can destroy useful evidence and configuration relationships.

---

## Enhanced Deep Dive 48 — Authentication vs Authorization

Authentication:

```text
prove identity
```

Authorization:

```text
evaluate allowed access
```

Example:

```text
Kerberos succeeds
but SMB returns Access Denied
```

That is often an authorization/ACL problem, not authentication.

---

## Enhanced Deep Dive 49 — Kerberos Participants

```text
Client
KDC
Service
```

KDC functionality on DC includes:

```text
Authentication Service
Ticket Granting Service
```

Flow:

```text
user authenticates
  ↓
TGT
  ↓
service ticket request
  ↓
service ticket
  ↓
service
```

---

## Enhanced Deep Dive 50 — TGT

Ticket Granting Ticket lets the user request service tickets without repeatedly sending the original password.

Inspect:

```cmd
klist
```

The TGT is highly sensitive authentication material.

Privileged logons should occur only on trusted systems.

---

## Enhanced Deep Dive 51 — Service Ticket

For SMB:

```text
cifs/fileserver.corp.example
```

For HTTP:

```text
HTTP/webapp.corp.example
```

Service ticket is encrypted for the service account/computer identity associated with the SPN.

---

## Enhanced Deep Dive 52 — SPN

Service Principal Name maps:

```text
service instance
→ security principal
```

Examples:

```text
HOST/server01
CIFS/server01
HTTP/app01
MSSQLSvc/sql01:1433
```

Duplicate or wrong SPNs can break Kerberos.

Inspect:

```cmd
setspn -L SERVER01
```

Use supported SPN management rather than manual arbitrary edits.

---

## Enhanced Deep Dive 53 — Kerberos by Hostname vs IP

Kerberos service identity is name/SPN based.

Accessing:

```text
\\fileserver\share
```

supports a normal CIFS SPN path.

Accessing:

```text
\\10.60.0.20\share
```

can prevent normal Kerberos service-ticket selection and trigger fallback.

This is why correct DNS names matter.

---

## Enhanced Deep Dive 54 — Kerberos Time

Kerberos rejects authentication outside allowed clock skew.

Domain time hierarchy concept:

```text
reliable external source
   ↓
forest-root PDC Emulator
   ↓
other DCs
   ↓
domain members
```

Inspect:

```cmd
w32tm /query /status
w32tm /query /source
```

Time is a security dependency.

---

## Enhanced Deep Dive 55 — PAC Awareness

Kerberos tickets in Windows can carry authorization-related information, including group/security data through the Privilege Attribute Certificate model.

Concept:

```text
authentication ticket
+
authorization context
```

This is one reason group membership can affect access after obtaining a new logon/ticket context.

---

## Enhanced Deep Dive 56 — NTLM Fallback

Kerberos may not be used when:

```text
SPN missing/wrong
name resolution wrong
IP used
legacy application
trust/path issue
```

Windows may fall back to NTLM where permitted.

Defensive goal:

```text
measure NTLM usage
fix Kerberos dependencies
reduce NTLM carefully
```

Do not disable blindly.

---

## Enhanced Deep Dive 57 — NTLM Security Risk Awareness

NTLM lacks some protections/modern characteristics of Kerberos and is associated with credential-relay and legacy authentication risk.

Defensive actions:

```text
audit usage
disable obsolete protocols where supported
SMB signing
LDAP protections
network segmentation
remove legacy dependencies
```

This is a defensive architecture topic, not a reason to run credential attacks in production.

---

## Enhanced Deep Dive 58 — LDAP

LDAP is a directory access protocol.

Clients can:

```text
bind/authenticate
search
read attributes
modify if authorized
```

LDAP itself is not synonymous with AD authentication.

AD uses multiple protocols:

```text
Kerberos
LDAP
SMB
RPC
DNS
```

---

## Enhanced Deep Dive 59 — LDAP Signing

LDAP signing protects integrity of LDAP operations where supported/enforced.

Rollout:

```text
audit clients
identify unsigned bind dependencies
remediate
test
enforce
```

Security hardening must be compatible with applications.

---

## Enhanced Deep Dive 60 — LDAP over TLS

LDAPS/TLS provides encrypted transport.

Certificate trust matters:

```text
DC certificate
  ↓ issued by trusted CA
client trusts CA
  ↓
TLS validated
```

Do not tell applications to ignore TLS certificate validation.

---

## Enhanced Deep Dive 61 — LDAP Channel Binding

Channel binding can protect certain authentication-over-TLS flows from relay-style risks.

Deployment requires:

```text
OS support
client support
application support
testing
```

Do not permanently weaken DC security because one legacy application is unmaintained.

---

## Enhanced Deep Dive 62 — Security Groups vs Distribution Groups

Security group:

```text
included in authorization token where applicable
can appear in ACLs
```

Distribution group:

```text
messaging/distribution purpose
not intended for ACL authorization
```

Choose group category correctly.

---

## Enhanced Deep Dive 63 — Global Group

Use to collect identities that share a business role.

Example:

```text
GG_Finance_Users
```

Members:

```text
Finance accounts from the domain
```

Then nest into resource groups.

---

## Enhanced Deep Dive 64 — Domain Local Group

Use for resource permission within domain.

Example:

```text
DL_FinanceShare_Modify
```

ACL:

```text
D:\Finance
→ Modify granted to DL_FinanceShare_Modify
```

---

## Enhanced Deep Dive 65 — Universal Group

Useful in multi-domain forest scenarios where membership needs forest-wide use.

Universal membership changes can have wider replication implications.

Use only when architecture requires it.

---

## Enhanced Deep Dive 66 — AGDLP

```text
Accounts
  ↓
Global groups
  ↓
Domain Local groups
  ↓
Permissions
```

This separates:

```text
who people are
from
what a resource allows
```

It is easier to audit than assigning users directly to ACLs.

---

## Enhanced Deep Dive 67 — AGUDLP

Multi-domain:

```text
Accounts
  ↓
Global
  ↓
Universal
  ↓
Domain Local
  ↓
Permission
```

This adds a forest-wide role grouping layer.

Do not use it when one-domain AGDLP is enough.

---

## Enhanced Deep Dive 68 — Token Size Awareness

Excessive nested group membership can make security tokens large and complex.

Operational symptoms can include authentication/application issues in extreme environments.

Avoid uncontrolled "group nesting forever."

Group design should be intentional and documented.

---

## Enhanced Deep Dive 69 — Primary Group Is Not Normal Authorization Design

AD users have a `primaryGroupID`, historically important for compatibility.

Most normal Windows authorization should use explicit group memberships, not primary group tricks.

Do not redesign standard access around primary groups.

---

## Enhanced Deep Dive 70 — Group Membership Replication and Logon

Add user to group on DC01:

```text
change must replicate
```

User's existing logon token:

```text
does not automatically rebuild
```

Therefore access may require:

```text
replication convergence
new logon / ticket refresh
```

Troubleshoot both directory state and client token state.

---

## Enhanced Deep Dive 71 — Group Policy Architecture

GPO consists of:

```text
GPC in AD
+
GPT in SYSVOL
```

Effective policy depends on:

```text
link
scope
permissions
WMI filters
inheritance
processing order
client reachability
```

Creating a GPO is only the first step.

---

## Enhanced Deep Dive 72 — LSDOU

Processing order:

```text
Local
Site
Domain
Parent OU
Child OU
```

Later settings often win conflicts, subject to:

```text
policy type
enforced
block inheritance
loopback
security filtering
WMI
```

Do not reduce GPO troubleshooting to memorizing LSDOU only.

---

## Enhanced Deep Dive 73 — Security Filtering

A GPO must have appropriate permissions to apply.

Concept:

```text
linked GPO
   ↓
object in scope
   ↓
security filtering
   ↓
Read + Apply Group Policy
```

If a computer/user is not in the intended filter, GPO can be linked correctly but not apply.

---

## Enhanced Deep Dive 74 — WMI Filtering

WMI filter can condition policy on device properties.

Examples:

```text
OS version
hardware class
selected system characteristic
```

Trade-off:

```text
flexibility
vs
processing complexity/performance
```

Prefer clear OU design over excessive WMI filters when possible.

---

## Enhanced Deep Dive 75 — Block Inheritance

Block Inheritance stops many inherited GPO links from higher containers.

Use sparingly.

Complex environments with many:

```text
Block Inheritance
+
Enforced
```

become hard to reason about.

---

## Enhanced Deep Dive 76 — Enforced

Enforced link gives higher-level GPO stronger precedence and prevents normal blocking behavior.

Use only when a policy truly must apply broadly.

Examples might include:

```text
critical security policy
```

but even security baselines should be designed with test scopes and role compatibility.

---

## Enhanced Deep Dive 77 — Loopback Processing

Use for user experience determined by computer role.

```text
User from any department
  ↓ logs into
RDS server
  ↓
RDS computer OU user policy
```

Modes:

```text
Merge
Replace
```

This is useful for kiosks/RDS/training rooms.

---

## Enhanced Deep Dive 78 — Group Policy Preferences

Preferences can configure:

```text
registry
files
mapped drives
local users/groups
scheduled tasks
printers
```

Preferences differ from many policy settings because users/admins may sometimes change the resulting local value afterward depending on extension/item behavior.

Understand whether you are enforcing policy or applying a preference.

---

## Enhanced Deep Dive 79 — GPP Password Legacy Risk Awareness

Legacy Group Policy Preferences once allowed passwords to be stored in SYSVOL in a recoverable form.

Modern secure environments should not use that legacy password mechanism.

Security lesson:

```text
SYSVOL is broadly readable by authenticated domain users
```

Do not place reusable secrets in scripts/policy files there.

---

## Enhanced Deep Dive 80 — Central Store for ADMX

Central Store:

```text
SYSVOL\...\Policies\PolicyDefinitions
```

Provides common Administrative Templates to management consoles.

Change management:

```text
test ADMX versions
backup current store
avoid random vendor template overwrites
document additions
```

ADMX files define settings UI/registry mapping; they are not the policy values themselves.

---

## Enhanced Deep Dive 81 — Resultant Set of Policy

Use:

```cmd
gpresult /h C:\Temp\gp.html
```

or PowerShell:

```powershell
Get-GPResultantSetOfPolicy `
  -ReportType Html `
  -Path C:\Temp\rsop.html
```

This answers:

```text
what actually applied?
```

which is more useful than only checking what you intended to link.

---

## Enhanced Deep Dive 82 — GPO Troubleshooting Decision Tree

```text
GPO exists?
  ↓
linked where expected?
  ↓
object in correct OU/site/domain?
  ↓
security filtering?
  ↓
WMI filter?
  ↓
inheritance/enforced?
  ↓
client can reach DC/SYSVOL?
  ↓
replication healthy?
  ↓
extension/process error?
```

Use `gpresult` plus GroupPolicy operational logs.

---

## Enhanced Deep Dive 83 — FSMO Overview

Five roles:

```text
Forest:
Schema Master
Domain Naming Master

Domain:
RID Master
PDC Emulator
Infrastructure Master
```

FSMO exists because some operations need a single authoritative coordinator.

---

## Enhanced Deep Dive 84 — Schema Master

Controls schema-update operations.

Because schema is forest-wide:

```text
bad extension
→ forest-wide impact
```

Only authorized, validated change should touch schema.

---

## Enhanced Deep Dive 85 — Domain Naming Master

Coordinates adding/removing domains and certain directory partition operations.

This role is rarely used day-to-day but is critical during namespace changes.

---

## Enhanced Deep Dive 86 — RID Master

Allocates RID pools.

DCs can create users/groups/computers using local RID pool.

If RID Master is temporarily unavailable:

```text
DCs can continue until pools need replenishment
```

Understanding this prevents unnecessary emergency seizure.

---

## Enhanced Deep Dive 87 — PDC Emulator

Important responsibilities include:

```text
time hierarchy anchor
password-change coordination
certain account lockout/password behaviors
legacy compatibility
important admin coordination
```

This is often the most operationally sensitive FSMO role.

---

## Enhanced Deep Dive 88 — Infrastructure Master

Tracks certain cross-domain references.

Its practical significance depends on:

```text
number of domains
Global Catalog placement
forest design
```

Do not apply simplified historical rules without understanding the actual forest topology.

---

## Enhanced Deep Dive 89 — Transfer vs Seize

Transfer:

```text
old holder alive
→ graceful handoff
```

Seize:

```text
old holder permanently unavailable
→ emergency ownership
```

Seizure should be used only after deciding the old holder will not return in the same role state without appropriate rebuild/recovery.

---

## Enhanced Deep Dive 90 — Global Catalog

GC contains:

```text
full writable data for own domain
+
partial attribute set for forest objects
```

Used for:

```text
forest-wide searches
UPN logon-related functions
universal group-related operations
applications
```

Design GC placement with site/user/application needs.

---

## Enhanced Deep Dive 91 — Universal Group Membership Caching Awareness

Remote sites without a local GC can use specific mechanisms to reduce dependency on WAN for some logon-related universal-group information.

The broad lesson:

```text
site/GC placement affects authentication resilience
```

not every branch requires the same DC/GC design.

---

## Enhanced Deep Dive 92 — Trust Direction

If:

```text
Domain A trusts Domain B
```

then A is willing to accept authenticated identities from B for authorization decisions.

Trust direction language is easy to reverse mentally.

Always draw:

```text
trusted identities
  ↓
trusting resource domain
```

---

## Enhanced Deep Dive 93 — Trust ≠ Permission

Trust allows identity authentication across boundary.

Resource still requires authorization.

```text
UserB authenticated
  ↓
ACL in DomainA
  ↓
allowed/denied
```

No ACL/group permission:

```text
no resource access
```

---

## Enhanced Deep Dive 94 — Transitive vs Non-Transitive

Transitive trust can extend through trust relationships according to trust type.

Non-transitive is limited to explicitly configured relationship.

Do not assume every external/forest/domain trust behaves identically.

---

## Enhanced Deep Dive 95 — Forest Trust

Forest trusts connect forests.

Security review should include:

```text
authentication scope
name resolution
SID filtering
selective authentication where used
admin ownership
resource authorization
```

Trust increases the identities that another environment may recognize.

---

## Enhanced Deep Dive 96 — SIDHistory Awareness

SIDHistory can preserve access when identities are migrated between domains.

Security relevance:

```text
old SID can continue contributing to authorization
```

Therefore migration/security teams should monitor and govern SIDHistory.

It should not become a permanent undocumented privilege mechanism.

---

## Enhanced Deep Dive 97 — Password Policy

Domain password policy can include:

```text
minimum length
history
age
complexity
lockout
```

Security policy should reflect modern organization requirements and compatibility.

Avoid choosing arbitrary numbers simply because a tutorial used them.

---

## Enhanced Deep Dive 98 — Fine-Grained Password Policies

FGPP lets selected users/groups receive different password/lockout policy.

Use cases:

```text
privileged identities
service-like identities with justified constraints
special populations
```

Inspect resultant policy:

```powershell
Get-ADUserResultantPasswordPolicy aferganey
```

---

## Enhanced Deep Dive 99 — Account Lockout Investigation

Repeated lockout can originate from:

```text
old password in service
scheduled task
mapped drive
phone/app
RDP session
credential manager
malicious attempts
```

Do not only unlock repeatedly.

Investigate source systems and event logs.

---

## Enhanced Deep Dive 100 — Service Accounts

Service identities should be:

```text
dedicated
least privilege
noninteractive where possible
managed password lifecycle
documented owner
```

Avoid:

```text
normal employee account running service
Domain Admin service account
password never rotated
```

---

## Enhanced Deep Dive 101 — gMSA

gMSA provides AD-managed password lifecycle for supported services.

Concept:

```text
AD/KDS
  ↓ managed secret
gMSA
  ↓ authorized hosts
service
```

Benefits:

```text
automatic password rotation
no human-known static service password
multi-host support where designed
```

---

## Enhanced Deep Dive 102 — KDS Root Key Awareness

gMSA password generation relies on Key Distribution Service infrastructure.

In lab, setup timing/behavior can differ from production.

Follow current Microsoft documentation for KDS root-key creation and safe production deployment.

Do not copy shortcuts intended only for immediate lab testing into production.

---

## Enhanced Deep Dive 103 — SPNs on Service Accounts

When a service runs under domain account/gMSA, required SPNs may belong to that identity.

Incorrect SPN ownership:

```text
Kerberos fails
NTLM fallback
duplicate SPN errors
```

Use:

```cmd
setspn -L account
setspn -Q service/name
```

for authorized troubleshooting.

---

## Enhanced Deep Dive 104 — Delegation of Administration

Principle:

```text
Help Desk needs password reset
≠
Help Desk needs Domain Admin
```

Delegate:

```text
specific object type
specific OU
specific operations
```

Examples:

```text
reset password
unlock account
join computers
manage selected groups
```

---

## Enhanced Deep Dive 105 — OU ACLs

Delegation modifies access control on directory objects.

This is why AD authorization itself uses ACL concepts.

Use GUI wizard for common delegation but understand:

```text
it creates ACEs
on OU/object security descriptors
```

Document delegated groups and scope.

---

## Enhanced Deep Dive 106 — AdminSDHolder Awareness

Highly privileged protected groups/users receive special security-descriptor protection behavior.

Operational symptom:

```text
delegated ACL unexpectedly disappears/changes on privileged account
```

Do not fight this by repeatedly forcing custom ACLs.

Understand protected-account behavior.

---

## Enhanced Deep Dive 107 — Protected Users Awareness

Protected Users is a security group with stronger authentication restrictions for suitable privileged accounts.

It can break legacy authentication workflows.

Test carefully before adding accounts.

Security controls are effective only if administrators understand compatibility.

---

## Enhanced Deep Dive 108 — Privileged Access Tiering

Concept:

```text
Tier 0
DCs, identity, PKI, privileged control plane

Tier 1
servers/application infrastructure

Tier 2
workstations/user endpoints
```

Higher-tier credentials should not log into lower-trust tiers.

This reduces credential theft/lateral movement risk.

---

## Enhanced Deep Dive 109 — Separate Admin Accounts

Example:

```text
Ahmed normal:
aferganey

Ahmed privileged:
adm-aferganey
```

Normal account:

```text
email/web/business apps
```

Admin account:

```text
controlled privileged tasks
```

Do not browse the Internet from highly privileged AD admin sessions.

---

## Enhanced Deep Dive 110 — Privileged Access Workstation Concept

PAW:

```text
hardened administrative endpoint
  ↓
privileged admin account
  ↓
Tier-0 systems
```

Goal:

```text
reduce exposure of high-value credentials to ordinary endpoint malware
```

---

## Enhanced Deep Dive 111 — Windows LAPS

Windows LAPS solves:

```text
same local admin password
across many domain computers
```

Model:

```text
computer
  ↓ generates/rotates
unique local admin password
  ↓ stores protected value
AD
  ↓ delegated retrieval
authorized admin
```

This is a major lateral-movement reduction control.

---

## Enhanced Deep Dive 112 — LAPS Permissions

Security depends on:

```text
who can read passwords
who can reset/rotate
who can modify policy
audit access
```

Deploying LAPS while granting broad read permission defeats the design.

Review delegated rights.

---

## Enhanced Deep Dive 113 — RODC

Read-Only Domain Controller is useful where physical/admin trust is lower.

```text
HQ writable DCs
   ↓ WAN
Branch RODC
```

Benefits:

```text
read-only directory copy
controlled credential caching
delegated local branch admin options
```

It is not appropriate for every site.

---

## Enhanced Deep Dive 114 — Password Replication Policy

RODC PRP decides which credentials may be cached.

Privileged identities should generally not be cached casually on a branch RODC.

Design:

```text
allowed branch users
denied privileged groups
```

If RODC is stolen, cached credential exposure becomes part of incident response.

---

## Enhanced Deep Dive 115 — Functional Levels

Functional levels determine AD capabilities and DC OS compatibility.

Before raising:

```text
inventory all DC versions
application compatibility
replication health
backup/recovery
change approval
```

Raising is an architecture lifecycle event.

---

## Enhanced Deep Dive 116 — AD Recycle Bin

Recycle Bin improves recovery of deleted AD objects/attributes.

It does not replace:

```text
System State backup
forest recovery plan
malware recovery
DC rebuild procedures
```

Use the right recovery mechanism for incident type.

---

## Enhanced Deep Dive 117 — System State Backup

DC System State contains critical AD-related components.

Backup should be:

```text
supported
protected
monitored
restore-tested
```

Do not assume VM-level crash-consistent backup alone satisfies all directory-recovery requirements.

---

## Enhanced Deep Dive 118 — Non-Authoritative Restore

Concept:

```text
restore DC
  ↓
DC comes online
  ↓
healthy partners replicate newer data into it
```

Used when restoring the DC itself without intending old data to overwrite healthy current directory state.

---

## Enhanced Deep Dive 119 — Authoritative Restore

Used when selected restored directory data must be treated as authoritative and replicated outward.

This is specialized/high-impact recovery.

Practice only in isolated labs and follow supported documentation.

---

## Enhanced Deep Dive 120 — Forest Recovery

Catastrophic identity compromise/corruption can require forest-recovery procedures.

Planning includes:

```text
trusted backups
DSRM credentials
clean recovery environment
role-holder recovery
DNS
SYSVOL
privileged credential reset
application dependencies
```

A two-DC topology is resilient to one DC failure but not to malicious changes replicated to all DCs.

---

## Enhanced Deep Dive 121 — DSRM

Directory Services Restore Mode has separate recovery credentials.

Protect:

```text
DSRM password
procedure
access to console/recovery
```

It is part of identity disaster recovery.

Do not wait until an outage to discover nobody knows the recovery credentials.

---

## Enhanced Deep Dive 122 — DC Demotion

Removing a DC should be graceful when possible.

Before demotion:

```text
replication healthy
FSMO role check
DNS/GC role impact
client/site coverage
backup
```

Do not power off and delete a DC VM as a normal decommissioning procedure.

---

## Enhanced Deep Dive 123 — Metadata Cleanup Awareness

If a DC is permanently lost and cannot be normally demoted, directory metadata may require supported cleanup.

This is not routine.

The safe lesson:

```text
document permanent loss
verify role ownership
clean stale DC/DNS/site metadata using supported methods
```

---

## Enhanced Deep Dive 124 — AD CS Is Tier-0-Like Infrastructure

Certificate Services can issue identities trusted for:

```text
TLS
device/user auth
smart card
802.1X
code signing
```

A compromised CA/template can undermine authentication trust.

Treat enterprise PKI as high-value identity infrastructure.

---

## Enhanced Deep Dive 125 — Offline Root CA Concept

Architecture:

```text
Offline Root CA
      ↓ signs
Issuing CA
      ↓ issues
users/devices/servers
```

Offline root reduces exposure of the highest-trust CA key.

PKI design should include:

```text
key protection
backup
CRL/AIA availability
certificate lifecycle
revocation
```

---

## Enhanced Deep Dive 126 — Certificate Templates

Templates define:

```text
who can enroll
subject/SAN source
EKU
key usage
validity
key exportability
autoenrollment
```

Overly broad enrollment rights can create serious privilege/security issues.

Review template permissions as carefully as privileged AD groups.

---

## Enhanced Deep Dive 127 — Kerberos Delegation Awareness

Delegation allows a service to act toward another service on behalf of a user in specific architectures.

Forms include concepts such as:

```text
unconstrained delegation
constrained delegation
resource-based constrained delegation
```

Security principle:

```text
grant only required delegation
```

Do not enable broad delegation merely to solve an application double-hop issue.

---

## Enhanced Deep Dive 128 — Resource-Based Constrained Delegation Concept

RBCD lets the resource service control which front-end identities may delegate to it.

Concept:

```text
Frontend service
  ↓ delegated user context
Backend service
  ↑ backend controls allowed delegators
```

Use only with clear application architecture and least privilege.

---

## Enhanced Deep Dive 129 — krbtgt Account Awareness

The `krbtgt` account is fundamental to Kerberos TGT signing within a domain.

It is extremely sensitive.

Credential-compromise recovery may include carefully planned `krbtgt` password resets following authoritative incident-response guidance.

Do not reset it casually as routine maintenance.

---

## Enhanced Deep Dive 130 — Privileged Group Monitoring

Monitor membership changes for groups such as:

```text
Domain Admins
Enterprise Admins
Schema Admins
Administrators
DNSAdmins and other powerful role-specific groups where applicable
```

Security questions:

```text
who added whom?
when?
from which admin system?
change ticket?
expected?
```

Centralize events in SIEM.

---

## Enhanced Deep Dive 131 — Advanced Audit Policy

Audit categories include:

```text
Account Logon
Account Management
Logon/Logoff
DS Access
Policy Change
Privilege Use
Object Access
```

Use:

```cmd
auditpol /get /category:*
```

Audit should support detection goals.

Logging everything without storage/analysis is not effective monitoring.

---

## Enhanced Deep Dive 132 — Directory Service Change Auditing

Sensitive directory changes can be audited when policy/SACLs are configured.

Examples:

```text
privileged group membership
GPO modification
user creation/deletion
delegation change
trust modification
```

Protect Security logs and forward critical events centrally.

---

## Enhanced Deep Dive 133 — Windows Event Forwarding for AD

Architecture:

```text
DC01 \
DC02  → WEC / SIEM
DC03 /
```

Benefits:

```text
central timeline
retention beyond local log
cross-DC correlation
alerting
```

DC logging should not exist only locally.

---

## Enhanced Deep Dive 134 — Authentication Monitoring

Look for patterns such as:

```text
repeated failures
unusual privileged logon
legacy NTLM usage
lockout bursts
unexpected service-account interactive logon
```

Event interpretation requires context.

One failure is not automatically an attack.

---

## Enhanced Deep Dive 135 — NTLM Reduction Program

Mature migration:

```text
inventory NTLM
  ↓
identify application/device
  ↓
fix DNS/SPN/Kerberos support
  ↓
pilot restrictions
  ↓
monitor
  ↓
expand
```

Do not disable NTLM domain-wide on day one.

---

## Enhanced Deep Dive 136 — LDAP Hardening Program

```text
inventory LDAP clients
  ↓
identify unsigned/simple/legacy binds
  ↓
deploy trusted certificates where needed
  ↓
test signing/channel binding
  ↓
enforce
  ↓
monitor failures
```

Security change plus compatibility engineering.

---

## Enhanced Deep Dive 137 — SMB and AD

AD relies on SMB for important scenarios including SYSVOL/NETLOGON access.

Protect:

```text
SMB signing policy
firewall
server hardening
DNS
Kerberos
```

Blocking SMB indiscriminately between domain members/DCs can break policy/logon operations.

---

## Enhanced Deep Dive 138 — RPC and Dynamic Ports Awareness

AD administration/replication uses RPC-related services.

Network segmentation/firewall design must follow supported port requirements.

Do not "open every port" or "block all dynamic RPC" without understanding role communication.

Use official service-port documentation in production architecture.

---

## Enhanced Deep Dive 139 — DC Firewall Troubleshooting

If replication fails:

```text
DNS resolves?
TCP/UDP required services?
RPC endpoint?
firewall profile/rules?
network ACL?
```

Commands:

```powershell
Test-NetConnection DC02 -Port 53
Test-NetConnection DC02 -Port 88
Test-NetConnection DC02 -Port 445
```

These test only selected ports, not the entire AD communication set.

---

## Enhanced Deep Dive 140 — Domain Admin Is Not a Troubleshooting Tool

Bad pattern:

```text
permission denied
→ add user to Domain Admins
```

This destroys least privilege and hides the real ACL/delegation problem.

Fix:

```text
identify resource
identify required action
delegate exact permission
verify
```

---

## Enhanced Deep Dive 141 — Break-Glass Accounts

Organizations may maintain emergency privileged identities.

Design considerations:

```text
strong authentication
offline/secure credential handling
monitor every use
no daily use
periodic validation
documented activation
```

Break-glass should not become a shared daily admin account.

---

## Enhanced Deep Dive 142 — Stale Accounts

Stale user/computer accounts increase attack surface.

Investigation:

```powershell
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00
```

Treat output as review input.

Do not automatically delete because last-logon data can be nuanced and business ownership matters.

---

## Enhanced Deep Dive 143 — LastLogonTimestamp Awareness

AD exposes several logon-related attributes with different replication/accuracy semantics.

Do not use one timestamp blindly for exact forensic conclusions.

For lifecycle cleanup:

```text
combine directory attributes
asset/HR data
device management
business owner confirmation
```

---

## Enhanced Deep Dive 144 — Locked Accounts

```powershell
Search-ADAccount -LockedOut -UsersOnly
```

Then investigate source.

Repeated unlock without source correction:

```text
does not solve problem
```

It may also hide malicious credential attempts.

---

## Enhanced Deep Dive 145 — Bulk Provisioning Safety

Automation should validate input:

```text
unique SamAccountName
valid OU DN
approved department
UPN uniqueness
manager exists
group mapping
```

Never use CSV with reusable plaintext production passwords.

Prefer controlled initial-password or self-service provisioning workflows.

---

## Enhanced Deep Dive 146 — Offboarding Workflow

Identity lifecycle:

```text
disable
  ↓
terminate active access/session where required
  ↓
remove privileged groups
  ↓
reassign ownership
  ↓
preserve mailbox/data/evidence
  ↓
retain according to policy
  ↓
delete later
```

Deletion is not the first offboarding step.

---

## Enhanced Deep Dive 147 — Joiner/Mover/Leaver

Identity governance model:

```text
Joiner
→ create account + baseline groups

Mover
→ remove old role access + add new role access

Leaver
→ disable/revoke + retain/delete per policy
```

The mover process is especially important because privilege accumulation often occurs when old access is never removed.

---

## Enhanced Deep Dive 148 — Naming Standards

Define standards for:

```text
users
admin accounts
service accounts
groups
computers
servers
OUs
GPOs
```

Example:

```text
GG_Accounting_Users
DL_Finance_Modify
GPO_Workstation_Baseline
SRV-CAI-APP01
```

Consistency improves automation and auditing.

---

## Enhanced Deep Dive 149 — Documentation as Security Control

Maintain:

```text
forest/domain design
DNS topology
sites/subnets
FSMO
GCs
trusts
privileged groups
delegations
GPO ownership
service accounts
PKI
backup/recovery
```

Unknown identity architecture is difficult to secure or recover.

---

## Enhanced Deep Dive 150 — AD Troubleshooting Dependency Tree

For a domain logon problem:

```text
NIC/IP
  ↓
DNS resolver
  ↓
SRV records/DC locator
  ↓
route/firewall
  ↓
time
  ↓
account state
  ↓
Kerberos/NTLM
  ↓
secure channel
  ↓
authorization/GPO/profile
```

Use the tool that tests the current layer:

```text
ipconfig
Resolve-DnsName
nltest
w32tm
Get-ADUser
klist
Test-ComputerSecureChannel
gpresult
dcdiag
repadmin
Event Logs
```

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Logical vs Physical Diagram

Draw forest/domain/OU separately from site/subnet/DC topology.

## Enhanced Lab 2 — Directory Object Identity

Create a lab user, record DN/SID/ObjectGUID/UPN/sAMAccountName, move/rename it, compare identifiers.

## Enhanced Lab 3 — Schema Exploration

Read schema class/attribute information using supported tools; do not modify schema.

## Enhanced Lab 4 — Naming Context Map

Document domain, configuration, schema, and DNS application partitions in your lab.

## Enhanced Lab 5 — DC Baseline

Record services, DNS zones, SYSVOL/NETLOGON shares, time, GC, FSMO, and replication health.

## Enhanced Lab 6 — AD DNS SRV

Query LDAP/Kerberos SRV records and map returned DC names to A/AAAA addresses.

## Enhanced Lab 7 — Dynamic Registration

Inspect DC DNS records, re-register in lab if needed, and verify root cause rather than relying on command blindly.

## Enhanced Lab 8 — Forwarders

Configure a lab DNS forwarder and verify internal vs external resolution path.

## Enhanced Lab 9 — Conditional Forwarder Design

Design name resolution between two hypothetical forests.

## Enhanced Lab 10 — Domain Join Flow

Capture DNS/DC discovery, join, computer object, secure channel, reboot/sign-in.

## Enhanced Lab 11 — Secure Channel Failure

Break a disposable member's trust relationship in a safe lab and repair using supported methods.

## Enhanced Lab 12 — OU Design Review

Build two alternative OU designs and compare GPO/delegation complexity.

## Enhanced Lab 13 — User Provisioning

Create five users with required attributes and group mappings.

## Enhanced Lab 14 — User Move Impact

Move a user/computer to another OU and compare delegated rights/GPO result.

## Enhanced Lab 15 — Group Scope

Create Global, Domain Local, Universal test groups and document valid membership/use.

## Enhanced Lab 16 — AGDLP

Implement Accounts→Global→Domain Local→NTFS/SMB permission.

## Enhanced Lab 17 — Token Refresh

Change group membership, observe old session vs new sign-in access.

## Enhanced Lab 18 — Kerberos TGT

Use `klist` immediately after logon and identify TGT.

## Enhanced Lab 19 — CIFS Ticket

Access SMB by hostname, inspect CIFS ticket.

## Enhanced Lab 20 — Hostname vs IP Authentication

Compare SMB access using server hostname vs IP and document ticket/fallback behavior.

## Enhanced Lab 21 — SPN Inventory

Use `setspn -L` and `-Q` to inspect service identities in your own lab.

## Enhanced Lab 22 — Kerberos Time

Create a small isolated time offset within safe lab bounds and observe authentication/time diagnostics, then restore.

## Enhanced Lab 23 — NTLM Audit Design

Create a migration worksheet identifying applications that still require NTLM.

## Enhanced Lab 24 — LDAP Query

Use approved LDAP/PowerShell tools to search users/groups and map DN/filter concepts.

## Enhanced Lab 25 — LDAP TLS Design

Document certificate trust path for LDAPS; inspect DC certificate if deployed.

## Enhanced Lab 26 — LDAP Signing Rollout Plan

Create audit→remediate→pilot→enforce plan.

## Enhanced Lab 27 — GPO GPC/GPT

Choose a GPO and locate its AD metadata plus SYSVOL template folder.

## Enhanced Lab 28 — LSDOU

Create harmless conflicting settings at domain and child OU; observe resultant policy.

## Enhanced Lab 29 — Security Filtering

Apply GPO to one test group and prove another object is excluded.

## Enhanced Lab 30 — WMI Filter

Create a harmless lab WMI filter and document performance/design trade-offs.

## Enhanced Lab 31 — Block/Enforced

Build controlled inheritance conflict, observe, then revert and document complexity.

## Enhanced Lab 32 — Loopback

Use a dedicated test workstation/RDS-style OU and test Merge/Replace with harmless settings.

## Enhanced Lab 33 — GPP

Create a non-secret preference item and compare behavior with policy setting.

## Enhanced Lab 34 — Central Store

Build/inspect a lab ADMX Central Store and document change-management rules.

## Enhanced Lab 35 — gpresult

Generate HTML RSoP and explain each applied/denied GPO.

## Enhanced Lab 36 — Add DC02

Promote second DC, verify DNS, GC, SYSVOL, replication, and authentication resilience.

## Enhanced Lab 37 — Replication Summary

Run `repadmin /replsummary` before/after several directory changes.

## Enhanced Lab 38 — Show Replication

Use `repadmin /showrepl` and map inbound partners/naming contexts.

## Enhanced Lab 39 — Replication Metadata

Inspect metadata for a test object/attribute using supported tools and identify originating DC/version.

## Enhanced Lab 40 — Sites/Subnets

Create Cairo/Alexandria sites and map lab subnets.

## Enhanced Lab 41 — Site Link

Create site-link cost/schedule model and explain replication preference.

## Enhanced Lab 42 — DC Locator

From a client, use `nltest /dsgetsite` and `/dsgetdc` to identify site/DC selection.

## Enhanced Lab 43 — Mis-Mapped Subnet

Remove/wrongly map a lab subnet and observe client site selection, then fix.

## Enhanced Lab 44 — SYSVOL

Compare policy files on DC01/DC02 and review DFSR-related logs.

## Enhanced Lab 45 — FSMO Inventory

Locate all five roles using PowerShell and `netdom query fsmo`.

## Enhanced Lab 46 — PDC Transfer

Transfer PDC Emulator in lab, verify time/FSMO state, transfer back.

## Enhanced Lab 47 — RID Concept

Create many lab users, inspect RID portions conceptually, explain pool allocation without exhausting RIDs.

## Enhanced Lab 48 — Trust Direction Diagram

Draw one-way trust and clearly identify trusting vs trusted side.

## Enhanced Lab 49 — Trust vs Permission

In a multi-domain/forest lab if available, prove trust alone does not grant file access.

## Enhanced Lab 50 — SIDHistory Design Review

Design a domain migration and explain where SIDHistory assists and why it must be governed.

## Enhanced Lab 51 — Password Policy

Inspect default domain policy and map requirements to actual settings.

## Enhanced Lab 52 — Fine-Grained Policy

Create test FGPP for a privileged lab group and verify resultant policy.

## Enhanced Lab 53 — Lockout Investigation

Create safe lockout with known source and trace events/source rather than merely unlocking.

## Enhanced Lab 54 — gMSA Architecture

Design service→gMSA→authorized hosts→SPN mapping.

## Enhanced Lab 55 — gMSA Lab

If environment supports it, create KDS/gMSA according to current docs and run a harmless service/task.

## Enhanced Lab 56 — Delegated Help Desk

Delegate reset/unlock only on a test OU and verify Help Desk is not Domain Admin.

## Enhanced Lab 57 — Delegation ACL

Inspect OU security after delegation and identify resulting ACEs.

## Enhanced Lab 58 — Protected Account Behavior

In isolated lab, compare ACL behavior of normal vs protected privileged account; do not weaken protected-object design.

## Enhanced Lab 59 — Admin Account Separation

Create normal/admin account pair and document logon restrictions.

## Enhanced Lab 60 — LAPS Design

Prepare directory/policy/retrieval permissions for Windows LAPS in lab and validate least privilege.

## Enhanced Lab 61 — RODC Design

Build branch topology and PRP list; deploy RODC if resources allow.

## Enhanced Lab 62 — RODC Credential Cache Review

Determine which branch identities may/should not be cached.

## Enhanced Lab 63 — Functional Level Inventory

Record forest/domain modes and DC OS versions; create raise-readiness checklist.

## Enhanced Lab 64 — AD Recycle Bin

Enable in disposable lab, delete/restore user/group, compare preserved attributes.

## Enhanced Lab 65 — System State Recovery Plan

Document backup schedule, DSRM, restore host, RPO/RTO, and test procedure.

## Enhanced Lab 66 — Non-Authoritative Restore Diagram

Draw restore→replicate-current-data flow.

## Enhanced Lab 67 — Authoritative Restore Diagram

Draw selected restored-data→mark authoritative→replicate outward flow.

## Enhanced Lab 68 — Forest Recovery Tabletop

Simulate all DCs compromised/corrupted on paper and identify trusted recovery sequence.

## Enhanced Lab 69 — DC Decommission Plan

Create graceful demotion checklist including FSMO/GC/DNS/site/replication checks.

## Enhanced Lab 70 — AD CS Architecture

Draw offline root→issuing CA→templates→certificates.

## Enhanced Lab 71 — Certificate Template Security Review

Without exploitation, review a lab template for who can enroll, EKUs, subject naming, key export, approvals.

## Enhanced Lab 72 — Kerberos Delegation Design

Map front-end→back-end service flow and select least-privileged delegation approach conceptually.

## Enhanced Lab 73 — Privileged Group Monitoring

Create a report of high-value groups and membership owners.

## Enhanced Lab 74 — Audit Policy

Review `auditpol`, enable/plan appropriate lab categories, generate benign test events.

## Enhanced Lab 75 — WEF/SIEM Design

Design DC event forwarding pipeline and retention.

## Enhanced Lab 76 — Stale Account Review

Generate inactive account report and cross-check with business ownership rather than deleting automatically.

## Enhanced Lab 77 — Joiner/Mover/Leaver

Implement synthetic lifecycle for one user including removal of old access on transfer.

## Enhanced Lab 78 — Bulk Provisioning Validation

Import CSV with one duplicate/invalid OU, reject invalid rows safely, provision valid rows.

## Enhanced Lab 79 — Offboarding

Disable test user, remove privileged memberships, preserve data ownership, document later deletion.

## Enhanced Lab 80 — Integrated AD Failure Challenge

Inject at least 25 safe faults across:

```text
DNS
SRV
time
secure channel
account state
group membership
GPO
SYSVOL
replication
sites
FSMO
service account
LAPS
delegation
```

For each:

```text
symptom
expected dependency path
tool/evidence
root cause
safe fix
verification
prevention
```



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — First Domain Controller

1. Deploy DC01.
2. Configure stable hostname.
3. Configure static IP.
4. Configure DNS architecture.
5. Install AD DS + DNS.
6. Create `corp.example`.
7. Verify with `Get-ADForest`, `Get-ADDomain`, `dcdiag`, and DNS SRV queries.

### Lab 2 — Join Client and Member Server

1. Point CLIENT01 DNS to DC01.
2. Point MEMBER01 DNS to DC01.
3. Join both to domain.
4. Verify computer accounts.
5. Verify secure channel.
6. Sign in using a domain account.

### Lab 3 — OU Design

1. Create Egypt OU.
2. Create France OU.
3. Under each, create Users, Computers, Servers, Groups.
4. Move test objects.
5. Explain how OUs differ from security groups.

### Lab 4 — Users and Groups

1. Create 10 users.
2. Create Finance and Operations Global groups.
3. Create Domain Local resource groups.
4. Build AGDLP.
5. Grant a file share permission on MEMBER01.
6. Test access.

### Lab 5 — Kerberos Observation

1. Sign into CLIENT01.
2. Run `klist`.
3. Access an SMB share on MEMBER01.
4. Run `klist` again.
5. Identify CIFS service ticket.
6. Explain TGT vs service ticket.

### Lab 6 — Group Policy

1. Create a Workstation GPO.
2. Link it to Computers OU.
3. Configure a harmless desktop/security setting.
4. Run `gpupdate /force`.
5. Generate `gpresult /h`.
6. Move computer to another OU and observe difference.

### Lab 7 — GPO Inheritance

1. Create parent OU GPO.
2. Create child OU GPO with a controlled conflicting setting.
3. Observe normal precedence.
4. Test Block Inheritance.
5. Test Enforced.
6. Revert.
7. Document why complexity matters.

### Lab 8 — Add Second Domain Controller

1. Deploy DC02.
2. Configure DNS correctly.
3. Install AD DS.
4. Promote as additional domain controller.
5. Verify DNS.
6. Run `repadmin /replsummary`.
7. Verify SYSVOL.
8. Shut down DC01 temporarily and test domain operations through DC02.

### Lab 9 — Sites and Subnets

1. Create Alexandria site.
2. Create `10.70.0.0/24` subnet object.
3. Associate subnet with Alexandria.
4. Inspect PowerShell site/subnet output.
5. Explain DC locality.

### Lab 10 — FSMO

1. Identify all five FSMO role holders.
2. Transfer PDC Emulator to DC02.
3. Verify.
4. Transfer back.
5. Explain transfer vs seizure.
6. Do not seize in production lab unless simulating permanent loss in disposable environment.

### Lab 11 — Password Policy

1. Inspect default domain policy.
2. Create a fine-grained policy for a test privileged group.
3. Verify resultant policy.
4. Test with disposable accounts.
5. Document lockout tradeoffs.

### Lab 12 — Delegation

1. Create HelpDesk group.
2. Delegate password-reset rights on Egypt Users OU.
3. Sign in as delegated operator.
4. Reset/unlock a test user.
5. Confirm operator is not Domain Admin.

### Lab 13 — Windows LAPS

1. Review current prerequisites.
2. Configure lab LAPS policy if supported.
3. Verify rotation/storage.
4. Verify authorized retrieval only.
5. Explain why shared local admin passwords are dangerous.

### Lab 14 — RODC Design

1. Design branch office.
2. Identify accounts safe/unsafe for credential caching.
3. Deploy RODC if lab resources permit.
4. Inspect Password Replication Policy.
5. Document branch failure scenarios.

### Lab 15 — AD Recycle Bin

1. Enable AD Recycle Bin in disposable lab after understanding the change.
2. Create test user.
3. Delete user.
4. Restore object.
5. Verify attributes/membership as applicable.
6. Compare this with backup/authoritative recovery.

### Lab 16 — Audit Review

1. Run `auditpol`.
2. Review privileged groups.
3. Find disabled users.
4. Find locked users.
5. Review directory/security events.
6. Create `AD_SECURITY_BASELINE.md`.

### Lab 17 — Broken AD Challenge

Inject one fault at a time:

1. wrong client DNS
2. stopped DNS service
3. missing/wrong subnet-to-site mapping
4. disabled user
5. locked account
6. GPO security-filter mismatch
7. bad DNS record
8. replication interruption
9. broken secure channel in a disposable client
10. time issue in isolated lab

Use:

```text
dcdiag
repadmin
nltest
klist
gpresult
Resolve-DnsName
Event Viewer
```

Document:

```text
Symptom
Expected AD path
Evidence
Tool used
Root cause
Fix
Verification
```

---

## 6. Mini Project

# Mini Project — Two-DC Enterprise Active Directory

Architecture:

```text
                    corp.example
                         |
              +----------+----------+
              |                     |
            DC01                   DC02
         10.60.0.11             10.60.0.12
        AD DS + DNS             AD DS + DNS
              |                     |
              +----------+----------+
                         |
                   10.60.0.0/24
                         |
              +----------+----------+
              |                     |
          CLIENT01               MEMBER01
          Windows 11            File Server
```

## OU Design

```text
corp.example
 |
 +-- Egypt
 |    +-- Users
 |    +-- Computers
 |    +-- Servers
 |    +-- Groups
 |
 +-- France
      +-- Users
      +-- Computers
      +-- Servers
      +-- Groups
```

## Identity

Create departments:

```text
Finance
HR
IT
Operations
```

Create at least 20 lab users.

Create:

```text
Global department groups
Domain Local resource groups
```

Use AGDLP.

## Group Policy

Create:

```text
Workstation Baseline
Server Baseline
Egypt User Policy
Privileged Admin Policy
```

Use:

- clear OU links
- security filtering only when justified
- `gpresult` verification

Avoid unnecessary Enforced/Block Inheritance.

## DNS

Verify:

```text
domain zone
DC A records
SRV records
reverse records where used
DC locator queries
```

Use:

```powershell
Resolve-DnsName
```

## Replication

Verify:

```cmd
repadmin /replsummary
repadmin /showrepl
dcdiag /test:dns
```

## Sites

Create:

```text
Cairo
Alexandria
```

Map:

```text
10.60.0.0/24 -> Cairo
10.70.0.0/24 -> Alexandria
```

Even if VMs are on one host, document the intended WAN topology.

## Security

Design/implement:

- separate privileged admin account
- delegated Help Desk
- Windows LAPS
- privileged group review
- LDAP signing/channel-binding compatibility plan
- NTLM audit/reduction plan
- advanced audit policy
- event-forwarding/SIEM plan
- privileged access workstation concept

## Resilience Test

1. shut down DC01
2. verify DNS/authentication through DC02
3. restore DC01
4. verify replication
5. inspect event logs
6. confirm clients rediscover healthy DCs

## Recovery

Document:

```text
AD Recycle Bin
System State backup
DSRM
FSMO role failure
DNS recovery
authoritative/non-authoritative restore concepts
```

## Documentation

```text
README.md
FOREST_DOMAIN_DESIGN.md
OU_DESIGN.md
GROUP_MODEL.md
AGDLP.md
GPO_DESIGN.md
DNS_DESIGN.md
SITE_REPLICATION.md
FSMO.md
DELEGATION.md
KERBEROS.md
LDAP_NTLM_SECURITY.md
LAPS.md
BACKUP_RECOVERY.md
TROUBLESHOOTING.md
SECURITY_BASELINE.md
```

## Failure Tests

Inject and solve:

```text
wrong DNS client
missing SRV lookup
locked user
disabled user
broken secure channel
GPO link mismatch
GPO security filter mismatch
replication failure
DC unavailable
incorrect site mapping
time issue
SMB group-membership error
```

For each:

```text
Symptom
Expected flow
Evidence
Failed component
Root cause
Fix
Verification
Prevention
```

---


# Expanded Capstone — Enterprise Active Directory Identity Platform

Build:

```text
                     corp.example
                          |
              +-----------+-----------+
              |                       |
             DC01                    DC02
        AD DS + DNS + GC        AD DS + DNS + GC
              |                       |
              +-----------+-----------+
                          |
              +-----------+-----------+
              |                       |
          CLIENT01                 MEMBER01
        Windows client            SMB server
```

Optional logical sites:

```text
Cairo       10.60.0.0/24
Alexandria  10.70.0.0/24
```

## Directory Design

Create:

```text
OU=Users
OU=Workstations
OU=Servers
OU=ServiceAccounts
OU=Groups
OU=Admins
```

Optionally nest geographic/operational OUs only where delegation/GPO requires.

## Identity Model

Departments:

```text
Finance
HR
IT
Operations
Engineering
```

Create:

```text
20+ lab users
normal/admin account separation for admins
Global role groups
Domain Local resource groups
one gMSA if supported
```

Use AGDLP.

## DNS

Verify:

```text
AD-integrated forward zone
_msdcs records
LDAP/Kerberos SRV
A records for DCs
reverse zone where used
forwarder for external queries
```

## Kerberos

Demonstrate:

```text
TGT after sign-in
CIFS ticket after SMB access
SPN inspection
hostname vs IP difference
time-source verification
```

Do not weaken Kerberos/NTLM policy merely to make tests pass.

## Group Policy

Create:

```text
GPO_Workstation_Baseline
GPO_Server_Baseline
GPO_User_Baseline
GPO_Admin_Baseline
```

Document:

```text
link target
security filtering
settings owner
test scope
rollback
gpresult evidence
```

Avoid unnecessary Enforced/Block Inheritance.

## Sites and Replication

Create:

```text
Cairo
Alexandria
```

Map subnets.

Document:

```text
site-link design
DC placement
GC placement
replication verification
```

Use:

```cmd
repadmin /replsummary
repadmin /showrepl
dcdiag /test:dns
```

## Delegation

Create HelpDesk role:

```text
reset password
unlock account
selected OU only
```

No Domain Admin membership.

## Security

Implement/design:

```text
Windows LAPS
privileged admin separation
PAW concept
NTLM audit/reduction
LDAP signing/channel-binding rollout
privileged group monitoring
advanced audit policy
WEF/SIEM
gMSA
RODC branch strategy
break-glass accounts
stale account review
```

## Recovery

Document:

```text
AD Recycle Bin
System State
DSRM
non-authoritative restore
authoritative restore
forest recovery
FSMO transfer/seizure decision
DC decommission
```

## Optional PKI

Design:

```text
offline root CA
issuing CA
server certificate template
user/device template
revocation publication
```

Do not deploy a real production PKI from the lab design without a full PKI architecture review.

## Failure Matrix

At least 30:

```text
client DNS points public
DC DNS service stopped
SRV record missing
wrong A record
client site/subnet missing
DC time wrong
user disabled
user locked
group membership missing
old token after group change
SPN missing/wrong
SMB accessed by IP
secure channel broken
GPO linked wrong OU
GPO security filter excludes target
WMI filter excludes target
Block Inheritance unexpected
SYSVOL issue
replication DNS failure
replication firewall failure
DC01 unavailable
PDC transfer needed
FGPP unexpected
service account password issue
LAPS retrieval over-permission
delegation too broad
stale account
RODC cache policy error
trust name-resolution problem design
backup/recovery documentation gap
```

For each record:

```text
User-visible symptom
Expected AD dependency path
Evidence/tool
Failed component
Root cause
Fix
Verification
Prevention
```

## Documentation

```text
README.md
FOREST_DOMAIN.md
OU_MODEL.md
NAMING_STANDARD.md
DNS_DESIGN.md
SITE_SUBNET_REPLICATION.md
KERBEROS.md
NTLM_REDUCTION.md
LDAP_SECURITY.md
GROUP_MODEL_AGDLP.md
GPO_DESIGN.md
FSMO.md
DELEGATION.md
SERVICE_ACCOUNTS_GMSA.md
LAPS.md
RODC.md
PRIVILEGED_ACCESS.md
AUDITING_WEF.md
PKI_FOUNDATIONS.md
BACKUP_RECOVERY.md
FOREST_RECOVERY.md
TROUBLESHOOTING.md
FAILURE_TESTS.md
```


## 7. Recommended Resources

Prioritize official Microsoft Learn:

- Active Directory Domain Services overview
- Install AD DS
- Functional levels
- AD security best practices
- FSMO roles
- Group Policy
- AD replication
- Sites and subnets
- Kerberos
- NTLM
- LDAP signing and channel binding
- Windows LAPS
- Active Directory Certificate Services
- Advanced Audit Policy
- backup and recovery

PowerShell discovery:

```powershell
Get-Command -Module ActiveDirectory

Get-Help New-ADUser -Examples

Get-Help Install-ADDSForest -Full

Get-Help New-GPO -Examples
```

---

## 8. Certification Relevance

This course supports:

- Windows Server Administration
- Active Directory Administration
- Identity and Access Management
- Windows Security Engineering
- SOC / Incident Response
- hybrid identity foundations
- enterprise infrastructure engineering

It is also a prerequisite for later study of:

- Active Directory penetration testing
- AD security hardening
- certificate services
- Microsoft hybrid identity
- Windows enterprise forensics

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Using public DNS directly on domain members.  
  **Best practice:** Use AD-aware DNS and configure forwarding for external resolution.

- **Mistake:** Giving Help Desk Domain Admin.  
  **Best practice:** Delegate narrowly scoped OU tasks.

- **Mistake:** Designing OUs only as an organization chart.  
  **Best practice:** Design around administration and GPO requirements.

- **Mistake:** Granting file permissions directly to users.  
  **Best practice:** Use group-based authorization such as AGDLP.

- **Mistake:** Creating many domains for departments.  
  **Best practice:** Use OUs unless a genuine domain boundary requirement exists.

- **Mistake:** Ignoring sites and subnets.  
  **Best practice:** Map physical network topology correctly.

- **Mistake:** Using Domain Admin on user workstations.  
  **Best practice:** Separate privileged accounts and access paths.

- **Mistake:** Disabling NTLM immediately.  
  **Best practice:** Audit, remediate, validate Kerberos, then restrict.

- **Mistake:** Weakening LDAP security permanently for one legacy app.  
  **Best practice:** Remediate application compatibility and move toward secure LDAP behavior.

- **Mistake:** Seizing FSMO when transfer is possible.  
  **Best practice:** Transfer from healthy holder; seize only after permanent loss.

- **Mistake:** Excessive GPO Enforced/Block Inheritance.  
  **Best practice:** Keep hierarchy simple and documented.

- **Mistake:** Treating Recycle Bin as full disaster recovery.  
  **Best practice:** Maintain tested System State and recovery procedures.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the highest-level AD DS boundary?

**Short answer:** The forest.

### Q2. What is an OU mainly for?

**Short answer:** Administrative delegation and Group Policy structure.

### Q3. Is an OU a security group?

**Short answer:** No.

### Q4. What is a Domain Controller?

**Short answer:** A server running AD DS that stores/replicates directory data and provides domain services.

### Q5. What is a Global Catalog?

**Short answer:** A DC role containing complete data for its own domain plus selected forest-wide attributes.

### Q6. Why is DNS essential to AD?

**Short answer:** Clients use DNS, especially SRV records, to locate domain controllers and services.

### Q7. What is a Distinguished Name?

**Short answer:** A hierarchical LDAP name describing an object's location in the directory.

### Q8. What is a SID?

**Short answer:** A Windows Security Identifier used to identify security principals for authorization.

### Q9. What does AGDLP mean?

**Short answer:** Accounts → Global Groups → Domain Local Groups → Permissions.

### Q10. What does Kerberos issue first after authentication?

**Short answer:** A Ticket Granting Ticket.

### Q11. What is an SPN?

**Short answer:** A Service Principal Name uniquely identifying a service instance for Kerberos.

### Q12. What does `klist` show?

**Short answer:** Kerberos tickets in the current logon session.

### Q13. What is LSDOU?

**Short answer:** Local → Site → Domain → OU Group Policy processing order.

### Q14. What does `gpresult` show?

**Short answer:** Resultant/applied Group Policy information.

### Q15. What summarizes AD replication?

**Short answer:** `repadmin /replsummary`.

### Q16. What does `dcdiag` evaluate?

**Short answer:** Domain controller health and related AD service tests.

### Q17. What are the five FSMO roles?

**Short answer:** Schema Master, Domain Naming Master, RID Master, PDC Emulator, Infrastructure Master.

### Q18. Transfer vs seizure?

**Short answer:** Transfer is controlled handoff from a healthy holder; seizure is emergency takeover after permanent loss.

### Q19. What is an RODC?

**Short answer:** A Read-Only Domain Controller.

### Q20. What is gMSA?

**Short answer:** A Group Managed Service Account whose password lifecycle is managed by Active Directory for supported services.

### Q21. What problem does Windows LAPS solve?

**Short answer:** Reuse and manual management of local administrator passwords.

### Q22. Authentication vs authorization?

**Short answer:** Authentication proves identity; authorization determines permitted access.

### Q23. What should you check early in many AD failures?

**Short answer:** DNS.

### Q24. What is the safest AD troubleshooting flow?

**Short answer:** DNS/DC discovery → time/authentication → replication/directory → policy/authorization.

---


# Enhanced Self-Assessment Bank

### Q1. What is AD DS?
**Answer:** Distributed directory, authentication, policy, and identity infrastructure for Windows enterprise environments.

### Q2. Logical vs physical AD architecture?
**Answer:** Forest/domain/OU vs sites/subnets/DC placement/replication.

### Q3. Highest security boundary?
**Answer:** Forest.

### Q4. Domain should represent every department?
**Answer:** No; use OUs unless a real domain boundary is required.

### Q5. What is an OU for?
**Answer:** Delegation and Group Policy/administrative structure.

### Q6. OU equals security group?
**Answer:** No.

### Q7. What is schema?
**Answer:** Definitions of AD object classes and attributes.

### Q8. Why schema changes high impact?
**Answer:** They replicate forest-wide and affect directory structure.

### Q9. Configuration partition?
**Answer:** Forest-wide configuration such as sites/services/partitions.

### Q10. Domain partition?
**Answer:** Domain-specific users/groups/computers/OUs and related data.

### Q11. Distinguished Name?
**Answer:** LDAP path identifying object's location.

### Q12. SID?
**Answer:** Security identifier used for authorization.

### Q13. RID?
**Answer:** Relative identifier appended to domain SID for security principal uniqueness.

### Q14. ObjectGUID?
**Answer:** Stable GUID identity for an AD object.

### Q15. UPN vs sAMAccountName?
**Answer:** Modern user principal name vs legacy-compatible logon name.

### Q16. What does a DC provide?
**Answer:** AD database, Kerberos, LDAP, replication, Netlogon, SYSVOL, often DNS.

### Q17. What is NTDS.dit?
**Answer:** AD DS database file.

### Q18. What is SYSVOL?
**Answer:** Replicated domain policy/script content.

### Q19. GPC vs GPT?
**Answer:** GPO metadata in AD vs policy files in SYSVOL.

### Q20. What replicates SYSVOL?
**Answer:** DFS Replication in modern domains.

### Q21. Multi-master?
**Answer:** Most directory changes can originate on multiple writable DCs.

### Q22. USN?
**Answer:** DC-local update sequence tracking value used in replication.

### Q23. Why supported DC restore methods?
**Answer:** Protect replication consistency and DC identity metadata.

### Q24. Lingering object?
**Answer:** Stale directory object remaining after improper long disconnection/replication lifecycle.

### Q25. Why is DNS critical?
**Answer:** Clients locate DCs and services via DNS SRV records.

### Q26. What does `_msdcs` contain?
**Answer:** Critical AD/DC locator DNS records.

### Q27. Why use AD DNS on members?
**Answer:** Public DNS does not know private AD SRV/service records.

### Q28. Conditional forwarder?
**Answer:** Sends queries for selected namespace to designated DNS servers.

### Q29. What maps client subnet to site?
**Answer:** AD subnet object.

### Q30. Site link cost?
**Answer:** Relative replication path preference.

### Q31. KCC?
**Answer:** Builds/maintains AD replication topology.

### Q32. `repadmin /replsummary`?
**Answer:** Summarizes replication health/errors.

### Q33. `repadmin /showrepl`?
**Answer:** Shows inbound replication partners/status by naming context.

### Q34. `dcdiag`?
**Answer:** Runs DC health diagnostics.

### Q35. Domain join creates what?
**Answer:** Computer account and machine secure channel relationship.

### Q36. How verify secure channel?
**Answer:** `Test-ComputerSecureChannel` or `nltest /sc_verify`.

### Q37. Authentication vs authorization?
**Answer:** Prove identity vs decide permitted access.

### Q38. KDC?
**Answer:** Kerberos Key Distribution Center function on domain controllers.

### Q39. TGT?
**Answer:** Ticket used to request Kerberos service tickets.

### Q40. Service ticket?
**Answer:** Kerberos ticket for a specific service/SPN.

### Q41. SPN?
**Answer:** Service Principal Name mapping a service instance to an account/computer identity.

### Q42. Why hostname matters for Kerberos?
**Answer:** Service identity/SPN is name-based.

### Q43. Why time matters?
**Answer:** Kerberos requires bounded clock skew.

### Q44. PAC?
**Answer:** Windows Kerberos authorization-related data structure carried with tickets.

### Q45. NTLM fallback means?
**Answer:** Kerberos was not used and legacy authentication may be used where allowed.

### Q46. Why reduce NTLM?
**Answer:** Reduce legacy authentication and relay/credential exposure risk.

### Q47. LDAP?
**Answer:** Directory access/search/modify protocol.

### Q48. LDAP signing?
**Answer:** Protects integrity/authenticity of LDAP communication.

### Q49. LDAPS?
**Answer:** LDAP protected by TLS.

### Q50. Channel binding?
**Answer:** Binds authentication to TLS channel to reduce relay-style risk in applicable flows.

### Q51. Security vs distribution group?
**Answer:** Authorization-capable group vs messaging/distribution group.

### Q52. Global group?
**Answer:** Usually groups accounts/roles within domain for nesting.

### Q53. Domain Local?
**Answer:** Usually represents permission to resource in its domain.

### Q54. Universal?
**Answer:** Forest-wide group scope for multi-domain scenarios.

### Q55. AGDLP?
**Answer:** Accounts → Global → Domain Local → Permission.

### Q56. AGUDLP?
**Answer:** Accounts → Global → Universal → Domain Local → Permission.

### Q57. Why excessive nesting bad?
**Answer:** Complexity and token-size/authorization troubleshooting risk.

### Q58. Why group change may need re-logon?
**Answer:** Existing access token/tickets may not include new membership.

### Q59. LSDOU?
**Answer:** Local → Site → Domain → OU processing order.

### Q60. Security filtering?
**Answer:** GPO permissions determining who can read/apply policy.

### Q61. WMI filter?
**Answer:** Applies GPO conditionally based on system WMI data.

### Q62. Block Inheritance?
**Answer:** Stops many inherited GPO links from higher containers.

### Q63. Enforced?
**Answer:** Gives a linked GPO strong precedence and prevents normal blocking behavior.

### Q64. Loopback?
**Answer:** Makes user policy depend on computer context, commonly Merge/Replace.

### Q65. Group Policy Preferences?
**Answer:** GPO extension for configurable preferences such as registry/files/tasks/drives.

### Q66. Why no passwords in SYSVOL?
**Answer:** Authenticated users can broadly read SYSVOL; secrets can be exposed.

### Q67. Central Store?
**Answer:** SYSVOL location for common ADMX templates.

### Q68. Best GPO troubleshooting command?
**Answer:** `gpresult`/RSoP plus operational logs.

### Q69. Five FSMO roles?
**Answer:** Schema, Domain Naming, RID, PDC Emulator, Infrastructure.

### Q70. Forest-wide FSMO?
**Answer:** Schema Master and Domain Naming Master.

### Q71. Domain-wide FSMO?
**Answer:** RID, PDC Emulator, Infrastructure.

### Q72. Transfer vs seize?
**Answer:** Graceful handoff vs emergency takeover after permanent loss.

### Q73. Most operationally sensitive FSMO?
**Answer:** Often PDC Emulator due time/password and other coordination functions.

### Q74. Global Catalog?
**Answer:** Full local-domain data plus selected forest-wide attributes.

### Q75. Trust direction?
**Answer:** Trusting side accepts authentication from trusted side.

### Q76. Trust grants permissions?
**Answer:** No.

### Q77. Forest trust?
**Answer:** Authentication trust relationship between forests.

### Q78. SIDHistory?
**Answer:** Attribute preserving old SID authorization during migrations.

### Q79. Fine-Grained Password Policy?
**Answer:** Different password/lockout policy for selected users/groups.

### Q80. Why investigate lockout source?
**Answer:** Repeated unlock does not fix stale credentials or malicious attempts.

### Q81. gMSA?
**Answer:** AD-managed service account with automated password lifecycle for supported services.

### Q82. KDS root key?
**Answer:** Key infrastructure used for gMSA password generation.

### Q83. Why SPN ownership matters?
**Answer:** Kerberos ticket encryption/service identity depends on correct principal.

### Q84. Delegation principle?
**Answer:** Grant only exact admin tasks on exact scope.

### Q85. Why Help Desk should not be Domain Admin?
**Answer:** Password reset/unlock needs far less privilege.

### Q86. AdminSDHolder?
**Answer:** Protected privileged-account security descriptor mechanism.

### Q87. Protected Users?
**Answer:** Security group enforcing stronger authentication restrictions for suitable privileged accounts.

### Q88. Privileged tiering?
**Answer:** Separate Tier 0 identity, Tier 1 servers, Tier 2 workstations and avoid credential crossover.

### Q89. PAW?
**Answer:** Hardened privileged administration workstation.

### Q90. Windows LAPS?
**Answer:** Unique rotating local admin password management with controlled directory storage/retrieval.

### Q91. RODC?
**Answer:** Read-only DC for lower-trust/branch scenarios.

### Q92. PRP?
**Answer:** RODC Password Replication Policy controlling credential caching.

### Q93. Functional level?
**Answer:** Controls AD capabilities/DC OS compatibility.

### Q94. AD Recycle Bin?
**Answer:** Restores deleted AD objects with many attributes preserved.

### Q95. Recycle Bin replaces backup?
**Answer:** No.

### Q96. System State?
**Answer:** Backup scope including critical AD/DC system components.

### Q97. Non-authoritative restore?
**Answer:** Restored DC receives newer current data from healthy replication partners.

### Q98. Authoritative restore?
**Answer:** Selected restored data is marked to replicate outward as authoritative.

### Q99. Forest recovery?
**Answer:** Controlled rebuild/recovery after catastrophic forest-wide compromise/corruption.

### Q100. DSRM?
**Answer:** Directory Services Restore Mode recovery credentials/environment.

### Q101. Why graceful demotion?
**Answer:** Cleanly removes DC role/metadata after health/role checks.

### Q102. AD CS?
**Answer:** Enterprise certificate authority infrastructure integrated with Windows/AD.

### Q103. Why CA is high value?
**Answer:** It can issue identities trusted for authentication/encryption/signing.

### Q104. Certificate template?
**Answer:** Policy defining who can enroll and certificate properties/usage.

### Q105. Kerberos delegation?
**Answer:** Allows service to access downstream service on user's behalf under controlled rules.

### Q106. Why delegation least privilege?
**Answer:** Delegation can expand credential/service impersonation capability.

### Q107. krbtgt?
**Answer:** Domain account fundamental to Kerberos TGT signing.

### Q108. Should krbtgt be reset casually?
**Answer:** No.

### Q109. Why monitor privileged groups?
**Answer:** Membership directly changes high-impact access.

### Q110. Advanced Audit Policy?
**Answer:** Granular Windows security auditing categories/subcategories.

### Q111. Why centralize DC logs?
**Answer:** Better retention, correlation, detection, and resistance to local loss/clearing.

### Q112. What is NTLM reduction process?
**Answer:** Audit → remediate dependencies → pilot restrictions → monitor → expand.

### Q113. LDAP hardening process?
**Answer:** Inventory → certificate/client remediation → test signing/channel binding → enforce → monitor.

### Q114. Why SMB matters to AD?
**Answer:** SYSVOL/NETLOGON and other domain operations use SMB.

### Q115. Why RPC matters?
**Answer:** AD administration/replication relies on RPC services/dynamic communication.

### Q116. Domain Admin as troubleshooting fix?
**Answer:** Never; identify and delegate actual required permission.

### Q117. Break-glass account?
**Answer:** Emergency privileged identity with tightly controlled use/monitoring.

### Q118. Stale accounts risk?
**Answer:** Unused identities expand attack surface and may retain access.

### Q119. Why LastLogonTimestamp not exact forensic timestamp?
**Answer:** Logon attributes have different replication/accuracy semantics.

### Q120. Joiner/Mover/Leaver?
**Answer:** Identity lifecycle for provisioning, role changes, and offboarding.

### Q121. Why mover process matters?
**Answer:** Old permissions can accumulate if not removed.

### Q122. Why naming standard?
**Answer:** Improves automation, review, ownership, and auditing.

### Q123. Main AD troubleshooting path?
**Answer:** Network/DNS → DC discovery → time → account/authentication → replication → policy/authorization.

### Q124. First thing to check in many AD incidents?
**Answer:** DNS.

### Q125. Main goal of Course 27?
**Answer:** Understand AD as a distributed identity/security system, not merely user administration.


## Completion Checklist

- [ ] I can explain forest, domain, OU, site, DC, and Global Catalog.
- [ ] I can build a new AD forest in an isolated lab.
- [ ] I can configure domain clients to use AD DNS.
- [ ] I can join clients and servers to the domain.
- [ ] I can create OUs, users, groups, and computer objects with PowerShell.
- [ ] I can implement AGDLP.
- [ ] I can explain Kerberos TGT/service-ticket flow.
- [ ] I can troubleshoot DNS, Kerberos, secure channel, and join failures.
- [ ] I can create and verify GPOs.
- [ ] I can explain replication, sites, subnets, and SYSVOL.
- [ ] I can locate and transfer FSMO roles.
- [ ] I understand trusts, gMSA, RODC, functional levels, and AD CS foundations.
- [ ] I understand Windows LAPS and privileged-access separation.
- [ ] I can use `dcdiag`, `repadmin`, `nltest`, `klist`, and `gpresult`.
- [ ] I completed all labs and the two-DC enterprise mini project.
