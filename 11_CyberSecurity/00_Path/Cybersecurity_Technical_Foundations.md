# Cybersecurity Technical Foundations — Learning Material

## Table of Contents

1. [Overview](#1-overview)
2. [Programming and Scripting](#2-programming-and-scripting)
   - [Python](#21-python)
   - [Bash](#22-bash)
   - [PowerShell](#23-powershell)
   - [C and C++](#24-c-and-c)
   - [JavaScript](#25-javascript)
   - [SQL](#26-sql)
   - [Go and Rust](#27-go-and-rust)
3. [Operating Systems](#3-operating-systems)
   - [Linux](#31-linux)
   - [Windows](#32-windows)
   - [Processes, Services, and Permissions](#33-processes-services-and-permissions)
4. [System Administration](#4-system-administration)
   - [User and Group Management](#41-user-and-group-management)
   - [File and Permission Management](#42-file-and-permission-management)
   - [Services and Daemons](#43-services-and-daemons)
   - [Patching and Updates](#44-patching-and-updates)
   - [Logging and Monitoring](#45-logging-and-monitoring)
   - [Backup and Recovery](#46-backup-and-recovery)
5. [Networking](#5-networking)
   - [OSI and TCP/IP Models](#51-osi-and-tcpip-models)
   - [IP Addressing and Subnetting](#52-ip-addressing-and-subnetting)
   - [TCP and UDP](#53-tcp-and-udp)
   - [Ports and Protocols](#54-ports-and-protocols)
   - [DNS](#55-dns)
   - [DHCP](#56-dhcp)
   - [Routing and Switching](#57-routing-and-switching)
   - [NAT](#58-nat)
   - [VPN](#59-vpn)
   - [Firewalls](#510-firewalls)
   - [Proxies and Load Balancers](#511-proxies-and-load-balancers)
6. [Web and Internet Fundamentals](#6-web-and-internet-fundamentals)
   - [HTTP and HTTPS](#61-http-and-https)
   - [Headers, Cookies, and Sessions](#62-headers-cookies-and-sessions)
   - [REST APIs](#63-rest-apis)
   - [Authentication and Authorization](#64-authentication-and-authorization)
   - [Frontend Basics](#65-frontend-basics)
7. [Databases](#7-databases)
   - [Relational Databases](#71-relational-databases)
   - [SQL Fundamentals](#72-sql-fundamentals)
   - [Database Security](#73-database-security)
8. [Cryptography](#8-cryptography)
   - [Encryption](#81-encryption)
   - [Symmetric Encryption](#82-symmetric-encryption)
   - [Asymmetric Encryption](#83-asymmetric-encryption)
   - [Hashing](#84-hashing)
   - [Salting](#85-salting)
   - [Digital Signatures](#86-digital-signatures)
   - [PKI and Certificates](#87-pki-and-certificates)
   - [TLS](#88-tls)
9. [Identity and Access Management](#9-identity-and-access-management)
   - [Authentication](#91-authentication)
   - [Authorization](#92-authorization)
   - [MFA](#93-mfa)
   - [RBAC and ABAC](#94-rbac-and-abac)
   - [SSO, OAuth, OIDC, and SAML](#95-sso-oauth-oidc-and-saml)
10. [Virtualization and Containers](#10-virtualization-and-containers)
    - [Virtual Machines](#101-virtual-machines)
    - [Docker](#102-docker)
    - [Kubernetes](#103-kubernetes)
11. [Cloud Computing](#11-cloud-computing)
    - [Cloud Service Models](#111-cloud-service-models)
    - [Cloud Deployment Models](#112-cloud-deployment-models)
    - [AWS, Azure, and GCP Fundamentals](#113-aws-azure-and-gcp-fundamentals)
    - [Cloud Security Basics](#114-cloud-security-basics)
12. [Software Development and DevOps Fundamentals](#12-software-development-and-devops-fundamentals)
    - [Git](#121-git)
    - [CI/CD](#122-cicd)
    - [Infrastructure as Code](#123-infrastructure-as-code)
    - [DevSecOps](#124-devsecops)
13. [Security Fundamentals](#13-security-fundamentals)
    - [CIA Triad](#131-cia-triad)
    - [Threat, Vulnerability, and Risk](#132-threat-vulnerability-and-risk)
    - [Security Controls](#133-security-controls)
    - [Least Privilege](#134-least-privilege)
    - [Defense in Depth](#135-defense-in-depth)
14. [Security Operations Fundamentals](#14-security-operations-fundamentals)
    - [Logs](#141-logs)
    - [SIEM](#142-siem)
    - [IDS and IPS](#143-ids-and-ips)
    - [EDR](#144-edr)
    - [Incident Response](#145-incident-response)
15. [Application Security Foundations](#15-application-security-foundations)
    - [OWASP Top 10](#151-owasp-top-10)
    - [Common Web Vulnerabilities](#152-common-web-vulnerabilities)
    - [API Security](#153-api-security)
    - [Secure Coding](#154-secure-coding)
16. [Offensive Security Foundations](#16-offensive-security-foundations)
    - [Reconnaissance](#161-reconnaissance)
    - [Scanning and Enumeration](#162-scanning-and-enumeration)
    - [Vulnerability Assessment](#163-vulnerability-assessment)
    - [Penetration Testing](#164-penetration-testing)
17. [Defensive Security Foundations](#17-defensive-security-foundations)
18. [Recommended Learning Order](#18-recommended-learning-order)
19. [Skills by Cybersecurity Career Path](#19-skills-by-cybersecurity-career-path)
20. [Final Summary](#20-final-summary)

---

# 1. Overview

Cybersecurity is not based on one technology.

To become strong in cybersecurity, you need foundations from multiple computer-science and IT domains.

The most important foundation areas are:

```text
Programming
System Administration
Operating Systems
Networking
Web Technologies
Databases
Cryptography
Identity and Access Management
Cloud
Virtualization
Containers
DevOps
Security Fundamentals
```

A simple view is:

```text
Computer Fundamentals
        ↓
Operating Systems
        ↓
Networking
        ↓
System Administration
        ↓
Programming / Scripting
        ↓
Web + Databases
        ↓
Cryptography
        ↓
Security Fundamentals
        ↓
Cybersecurity Specialization
```

---

# 2. Programming and Scripting

Programming is important in cybersecurity because security engineers frequently need to:

- Automate tasks
- Parse logs
- Analyze data
- Build security tools
- Interact with APIs
- Investigate malware
- Write detection scripts
- Test applications
- Automate cloud security

## 2.1 Python

Python is one of the most useful languages in cybersecurity.

Used for:

```text
Automation
Log Analysis
API Integration
Security Tools
Malware Analysis
Data Processing
Machine Learning
Threat Detection
Cloud Automation
```

Important topics:

- Variables
- Data types
- Conditions
- Loops
- Functions
- Classes
- Files
- JSON
- Regular expressions
- HTTP requests
- APIs
- Sockets
- Exceptions
- Virtual environments

Useful libraries include:

```text
requests
socket
re
json
pandas
scapy
cryptography
```

---

## 2.2 Bash

Bash is important for Linux security.

Used for:

- System automation
- File processing
- Log analysis
- Network commands
- Server administration
- Security testing

Learn:

```bash
ls
cd
cat
grep
awk
sed
find
chmod
chown
ps
kill
curl
wget
ssh
netstat
ss
```

---

## 2.3 PowerShell

PowerShell is essential for Windows-heavy environments.

Used for:

- Windows administration
- Active Directory
- Security automation
- Incident response
- Log collection
- Microsoft cloud environments

Learn:

- Cmdlets
- Pipelines
- Objects
- Variables
- Functions
- Scripts
- Windows services
- Registry
- Event logs

---

## 2.4 C and C++

C and C++ become important for advanced cybersecurity.

Used for:

- Malware analysis
- Reverse engineering
- Exploit development
- Memory vulnerabilities
- Operating system internals

Important concepts:

```text
Pointers
Memory
Stack
Heap
Buffers
Processes
System Calls
Compilation
```

---

## 2.5 JavaScript

JavaScript is important in web security.

Used to understand:

- XSS
- Browser behavior
- DOM manipulation
- Client-side security
- Web applications

Learn:

```text
Variables
Functions
Objects
DOM
Events
Promises
Fetch API
Cookies
Local Storage
```

---

## 2.6 SQL

SQL is important for:

- Database security
- Security analytics
- Log analysis
- Understanding SQL injection

Learn:

```sql
SELECT
INSERT
UPDATE
DELETE
JOIN
GROUP BY
ORDER BY
WHERE
UNION
```

---

## 2.7 Go and Rust

These are useful but not required initially.

### Go

Common in:

- Cloud-native tools
- Networking tools
- Security tooling
- Kubernetes ecosystem

### Rust

Useful for:

- Secure systems programming
- Memory-safe tools
- Modern security engineering

---

# 3. Operating Systems

Cybersecurity professionals must understand how operating systems work.

The two most important are:

```text
Linux
Windows
```

## 3.1 Linux

Linux is essential in cybersecurity.

Learn:

- Filesystem hierarchy
- Users
- Groups
- Permissions
- Processes
- Services
- SSH
- Logs
- Networking
- Package management
- Cron jobs

Important directories:

```text
/etc
/var
/home
/tmp
/usr
/bin
```

---

## 3.2 Windows

Windows knowledge is important because many enterprise environments use:

- Windows Server
- Active Directory
- Microsoft 365
- Entra ID

Learn:

- Users
- Groups
- NTFS permissions
- Services
- Registry
- Event Viewer
- PowerShell
- Active Directory
- Group Policy

---

## 3.3 Processes, Services, and Permissions

You should understand:

```text
Process
Thread
Service
Daemon
User
Group
Privilege
Permission
```

Security depends heavily on controlling who can execute what.

---

# 4. System Administration

System administration is one of the strongest foundations for cybersecurity.

A security engineer must understand how systems are configured before securing them.

## 4.1 User and Group Management

Learn:

```text
Create users
Delete users
Groups
Roles
Permissions
Password policies
Privileged accounts
```

---

## 4.2 File and Permission Management

Linux examples:

```text
chmod
chown
rwx
sudo
```

Windows concepts:

```text
NTFS Permissions
ACLs
Ownership
Inheritance
```

---

## 4.3 Services and Daemons

Understand:

- Start/stop services
- Service accounts
- Listening ports
- Startup services
- Misconfigured services

---

## 4.4 Patching and Updates

Unpatched software is a major source of vulnerabilities.

Learn:

```text
Operating System Updates
Application Patching
Firmware Updates
Vulnerability Remediation
```

---

## 4.5 Logging and Monitoring

Important logs include:

- Authentication logs
- System logs
- Application logs
- Security logs
- Network logs

Linux examples:

```text
/var/log/auth.log
/var/log/syslog
journalctl
```

Windows:

```text
Event Viewer
Security Logs
System Logs
PowerShell Logs
```

---

## 4.6 Backup and Recovery

Learn:

- Full backup
- Incremental backup
- Differential backup
- Restore testing
- Disaster recovery
- RPO
- RTO

---

# 5. Networking

Networking is one of the most important cybersecurity prerequisites.

You cannot secure a network if you do not understand how traffic moves.

## 5.1 OSI and TCP/IP Models

OSI layers:

```text
7 Application
6 Presentation
5 Session
4 Transport
3 Network
2 Data Link
1 Physical
```

TCP/IP model:

```text
Application
Transport
Internet
Network Access
```

---

## 5.2 IP Addressing and Subnetting

Learn:

```text
IPv4
IPv6
Private IP
Public IP
Subnet Mask
CIDR
Default Gateway
```

Example:

```text
192.168.1.0/24
```

---

## 5.3 TCP and UDP

### TCP

Connection-oriented and reliable.

Used by:

- HTTPS
- SSH
- FTP

### UDP

Connectionless and faster.

Used by:

- DNS
- Streaming
- VoIP

---

## 5.4 Ports and Protocols

Important ports:

| Port | Protocol |
|---|---|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCP |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

---

## 5.5 DNS

DNS converts names into IP addresses.

Example:

```text
example.com
     ↓
DNS
     ↓
93.184.x.x
```

Security topics:

- DNS spoofing
- DNS poisoning
- DNS tunneling

---

## 5.6 DHCP

DHCP automatically assigns:

- IP address
- Subnet mask
- Gateway
- DNS server

---

## 5.7 Routing and Switching

Learn:

- Router
- Switch
- VLAN
- Routing table
- Static routing
- Dynamic routing

---

## 5.8 NAT

**NAT = Network Address Translation**

Allows private IP addresses to communicate with public networks.

---

## 5.9 VPN

VPN provides encrypted communication across untrusted networks.

Learn:

- Remote-access VPN
- Site-to-site VPN
- IPsec
- SSL VPN

---

## 5.10 Firewalls

A firewall controls network traffic.

Typical rule:

```text
Source
Destination
Port
Protocol
Action
```

Example:

```text
Internet → Web Server → TCP 443 → Allow
Internet → Database → TCP 3306 → Deny
```

---

## 5.11 Proxies and Load Balancers

Learn:

- Forward proxy
- Reverse proxy
- Load balancer
- WAF

---

# 6. Web and Internet Fundamentals

Web security requires understanding how web applications work.

## 6.1 HTTP and HTTPS

HTTP request example:

```http
GET /profile HTTP/1.1
Host: example.com
```

HTTPS adds TLS encryption.

Learn:

- Methods
- Status codes
- Headers
- Request body
- Response body

Methods:

```text
GET
POST
PUT
PATCH
DELETE
```

---

## 6.2 Headers, Cookies, and Sessions

Learn:

```text
Cookies
Session IDs
Authorization Headers
Content-Type
CORS
CSRF Tokens
```

---

## 6.3 REST APIs

APIs expose functionality over HTTP.

Example:

```text
GET /users
POST /users
GET /users/10
DELETE /users/10
```

Security concerns include:

- Authentication
- Authorization
- Input validation
- Rate limiting
- Broken object-level authorization

---

## 6.4 Authentication and Authorization

Remember:

```text
Authentication → Who are you?
Authorization  → What can you do?
```

---

## 6.5 Frontend Basics

Learn basic:

```text
HTML
CSS
JavaScript
DOM
Forms
Browser Storage
```

You do not need to become a frontend expert, but you need to understand browser behavior.

---

# 7. Databases

## 7.1 Relational Databases

Examples:

```text
PostgreSQL
MySQL
SQL Server
Oracle
```

Learn:

- Tables
- Rows
- Columns
- Primary keys
- Foreign keys
- Relationships

---

## 7.2 SQL Fundamentals

Learn:

```sql
SELECT
WHERE
JOIN
GROUP BY
ORDER BY
INSERT
UPDATE
DELETE
```

---

## 7.3 Database Security

Learn:

- Database users
- Roles
- Permissions
- Encryption
- Backups
- Auditing
- Least privilege
- SQL injection prevention

---

# 8. Cryptography

Cryptography protects information mathematically.

Core goals include:

```text
Confidentiality
Integrity
Authenticity
Non-Repudiation
```

## 8.1 Encryption

Encryption converts:

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
```

Decryption reverses the process.

---

## 8.2 Symmetric Encryption

Same key is used for encryption and decryption.

Example algorithms:

```text
AES
ChaCha20
```

Advantages:

- Fast
- Good for large amounts of data

Main challenge:

- Secure key distribution

---

## 8.3 Asymmetric Encryption

Uses:

```text
Public Key
Private Key
```

Examples:

```text
RSA
ECC
```

Used in:

- Certificates
- Key exchange
- Digital signatures

---

## 8.4 Hashing

Hashing is one-way.

```text
Input
  ↓
Hash Function
  ↓
Fixed-Length Hash
```

Examples:

```text
SHA-256
SHA-3
```

Used for:

- Integrity checking
- Digital signatures
- Password systems

---

## 8.5 Salting

A salt is random data added before hashing passwords.

```text
Password + Salt
      ↓
Password Hash
```

This helps defend against precomputed hash attacks.

---

## 8.6 Digital Signatures

Used to support:

- Integrity
- Authenticity
- Non-repudiation

Simplified:

```text
Document
   ↓
Hash
   ↓
Sign with Private Key
```

Verification uses the public key.

---

## 8.7 PKI and Certificates

**PKI = Public Key Infrastructure**

Learn:

```text
Digital Certificates
Certificate Authority
Public Key
Private Key
Certificate Chain
Certificate Revocation
```

---

## 8.8 TLS

TLS protects network communication.

Used in HTTPS.

Simplified:

```text
Browser
   ↓
TLS Handshake
   ↓
Certificate Validation
   ↓
Encrypted Session
```

---

# 9. Identity and Access Management

IAM is a major cybersecurity domain.

## 9.1 Authentication

Verifies identity.

Examples:

- Password
- Passkey
- Certificate
- Biometrics

---

## 9.2 Authorization

Controls permissions.

Examples:

```text
Read
Write
Delete
Admin
```

---

## 9.3 MFA

Uses multiple authentication factors.

Example:

```text
Password
   +
Security Key
```

---

## 9.4 RBAC and ABAC

### RBAC

Permissions based on roles.

```text
User → Role → Permissions
```

### ABAC

Permissions based on attributes.

```text
Department
Location
Device
Time
Resource Type
```

---

## 9.5 SSO, OAuth, OIDC, and SAML

Learn:

- SSO
- OAuth 2.0
- OpenID Connect
- SAML
- Federation

These are important in enterprise and cloud security.

---

# 10. Virtualization and Containers

## 10.1 Virtual Machines

Learn:

```text
Hypervisor
VM
Host OS
Guest OS
Snapshot
Virtual Network
```

Popular tools:

- VMware
- Hyper-V
- VirtualBox

Virtual machines are widely used in cybersecurity labs.

---

## 10.2 Docker

Learn:

```text
Images
Containers
Dockerfile
Volumes
Networks
Registries
Secrets
```

Security topics:

- Non-root containers
- Image scanning
- Minimal images
- Container isolation

---

## 10.3 Kubernetes

Learn:

```text
Pods
Deployments
Services
Namespaces
Ingress
RBAC
Secrets
NetworkPolicy
Service Accounts
```

Security topics:

- Cluster hardening
- RBAC
- Admission controls
- Network policies
- Container security

---

# 11. Cloud Computing

Cloud security is now a major part of cybersecurity.

## 11.1 Cloud Service Models

```text
IaaS
PaaS
SaaS
```

### IaaS

Infrastructure as a Service.

Examples:

- Virtual machines
- Networks
- Storage

### PaaS

Platform as a Service.

Examples:

- Managed databases
- Application platforms

### SaaS

Software as a Service.

Examples:

- Microsoft 365
- Salesforce

---

## 11.2 Cloud Deployment Models

Learn:

```text
Public Cloud
Private Cloud
Hybrid Cloud
Multi-Cloud
```

---

## 11.3 AWS, Azure, and GCP Fundamentals

Learn one platform first.

Focus on:

```text
Compute
Storage
Networking
IAM
Databases
Logging
Monitoring
Encryption
Secrets
```

---

## 11.4 Cloud Security Basics

Learn:

- Shared responsibility model
- IAM
- Least privilege
- Cloud logging
- Security groups
- Network controls
- Encryption
- Key management
- Secrets management
- Cloud posture management

---

# 12. Software Development and DevOps Fundamentals

## 12.1 Git

Learn:

```text
git clone
git add
git commit
git branch
git merge
git pull
git push
```

Security engineers frequently work with development teams.

---

## 12.2 CI/CD

Understand:

```text
Code
 ↓
Build
 ↓
Test
 ↓
Security Scan
 ↓
Deploy
```

---

## 12.3 Infrastructure as Code

Tools:

```text
Terraform
CloudFormation
Bicep
```

Security topics:

- Misconfigurations
- Secrets
- Policy as code
- Secure state storage

---

## 12.4 DevSecOps

DevSecOps integrates security into development.

```text
Code
 ↓
SAST
 ↓
Dependency Scan
 ↓
Secrets Scan
 ↓
Container Scan
 ↓
IaC Scan
 ↓
Deployment
```

---

# 13. Security Fundamentals

## 13.1 CIA Triad

```text
Confidentiality
Integrity
Availability
```

---

## 13.2 Threat, Vulnerability, and Risk

```text
Threat
   ↓
Exploits
   ↓
Vulnerability
   ↓
Causes
   ↓
Impact
   ↓
Risk
```

---

## 13.3 Security Controls

Three implementation categories:

```text
Physical
Technical
Administrative
```

Functional categories:

```text
Preventive
Detective
Corrective
Recovery
Deterrent
Compensating
Directive
```

---

## 13.4 Least Privilege

Users should receive only the permissions required to perform their jobs.

```text
Required Access Only
        ↓
Reduced Attack Surface
```

---

## 13.5 Defense in Depth

Use multiple layers of security.

```text
Firewall
   ↓
WAF
   ↓
Authentication
   ↓
Authorization
   ↓
Encryption
   ↓
Monitoring
```

---

# 14. Security Operations Fundamentals

## 14.1 Logs

Security analysts need to understand logs from:

- Firewalls
- Servers
- Applications
- Endpoints
- Cloud
- Identity systems

---

## 14.2 SIEM

**SIEM = Security Information and Event Management**

Typical flow:

```text
Logs
  ↓
SIEM
  ↓
Correlation
  ↓
Alert
  ↓
SOC Analyst
```

---

## 14.3 IDS and IPS

### IDS

**Intrusion Detection System**

Detects suspicious traffic.

### IPS

**Intrusion Prevention System**

Can detect and block suspicious traffic.

---

## 14.4 EDR

**Endpoint Detection and Response**

Monitors endpoints for:

- Process activity
- Files
- Network connections
- Malware
- Suspicious behavior

---

## 14.5 Incident Response

Common phases:

```text
Preparation
   ↓
Detection
   ↓
Analysis
   ↓
Containment
   ↓
Eradication
   ↓
Recovery
   ↓
Lessons Learned
```

---

# 15. Application Security Foundations

## 15.1 OWASP Top 10

Learn common web security risks.

Examples:

- Broken Access Control
- Injection
- Security Misconfiguration
- Authentication Failures
- Cryptographic Failures

---

## 15.2 Common Web Vulnerabilities

Learn:

```text
SQL Injection
XSS
CSRF
SSRF
Command Injection
Path Traversal
Broken Authentication
Broken Authorization
```

---

## 15.3 API Security

Learn:

- Authentication
- Authorization
- JWT
- OAuth
- Rate limiting
- Input validation
- Object-level authorization

---

## 15.4 Secure Coding

Core principles:

```text
Validate Input
Escape Output
Least Privilege
Secure Secrets
Use Parameterized Queries
Handle Errors Safely
Patch Dependencies
```

---

# 16. Offensive Security Foundations

Only perform offensive security activities on systems you own or are explicitly authorized to test.

## 16.1 Reconnaissance

Collect information about the target environment.

---

## 16.2 Scanning and Enumeration

Learn concepts such as:

```text
Port Scanning
Service Enumeration
Host Discovery
```

---

## 16.3 Vulnerability Assessment

Identify weaknesses.

Typical workflow:

```text
Discover Assets
      ↓
Scan
      ↓
Identify Vulnerabilities
      ↓
Validate
      ↓
Prioritize
```

---

## 16.4 Penetration Testing

Authorized testing evaluates whether vulnerabilities can be exploited and what impact they may have.

Typical phases:

```text
Scope
 ↓
Reconnaissance
 ↓
Enumeration
 ↓
Vulnerability Analysis
 ↓
Controlled Exploitation
 ↓
Evidence
 ↓
Report
 ↓
Remediation
```

---

# 17. Defensive Security Foundations

Defensive security focuses on protecting systems.

Important areas:

```text
Hardening
Monitoring
Detection
Incident Response
Threat Hunting
Vulnerability Management
Patch Management
IAM
SIEM
EDR
Network Security
Cloud Security
```

---

# 18. Recommended Learning Order

A practical order is:

```text
1. Computer Fundamentals
        ↓
2. Networking
        ↓
3. Linux
        ↓
4. Windows
        ↓
5. System Administration
        ↓
6. Python
        ↓
7. Bash / PowerShell
        ↓
8. Web Fundamentals
        ↓
9. SQL / Databases
        ↓
10. Cryptography
        ↓
11. Authentication / IAM
        ↓
12. Security Fundamentals
        ↓
13. Logs / SIEM
        ↓
14. Cloud Fundamentals
        ↓
15. Docker / Kubernetes
        ↓
16. Application Security
        ↓
17. Choose Cybersecurity Specialization
```

---

# 19. Skills by Cybersecurity Career Path

## SOC / Blue Team

Focus on:

```text
Networking
Linux
Windows
System Administration
Logs
SIEM
EDR
Incident Response
Python
PowerShell
```

---

## Penetration Testing

Focus on:

```text
Networking
Linux
Python
Bash
Web
JavaScript
SQL
Operating Systems
Application Security
```

---

## Application Security

Focus on:

```text
Programming
Web Development
HTTP
APIs
Databases
Authentication
Authorization
OWASP
Secure Coding
Cloud
```

---

## Cloud Security

Focus on:

```text
Networking
Linux
Cloud
IAM
Python
Bash
Docker
Kubernetes
Terraform
Logging
SIEM
DevSecOps
```

---

## DevSecOps

Focus on:

```text
Software Development
Git
Linux
Cloud
Docker
Kubernetes
CI/CD
Terraform
SAST
DAST
SCA
Secrets Management
```

---

## Malware Analysis / Reverse Engineering

Focus on:

```text
C
C++
Assembly
Operating Systems
Memory
Debugging
Python
Windows Internals
```

---

## Security Engineering

Focus on:

```text
Python
Linux
Networking
Cloud
IAM
APIs
Automation
SIEM
Security Architecture
DevOps
```

---

# 20. Final Summary

The strongest cybersecurity engineers understand more than security tools.

They understand the systems they are protecting.

Core foundation:

```text
Programming
       +
System Administration
       +
Operating Systems
       +
Networking
       +
Web
       +
Databases
       +
Cryptography
       +
Identity
       +
Cloud
       +
Security Fundamentals
```

A simple roadmap is:

```text
Networking
   ↓
Linux + Windows
   ↓
System Administration
   ↓
Python + Bash / PowerShell
   ↓
Web + SQL
   ↓
Cryptography
   ↓
IAM
   ↓
Security Fundamentals
   ↓
Cloud / Containers
   ↓
Cybersecurity Specialization
```

If the target is **Cloud Security Engineering**, prioritize:

```text
Networking
Linux
Python
Bash
Cloud Fundamentals
IAM
Cloud Networking
Cryptography
Docker
Kubernetes
Terraform
CI/CD
SIEM
DevSecOps
```
