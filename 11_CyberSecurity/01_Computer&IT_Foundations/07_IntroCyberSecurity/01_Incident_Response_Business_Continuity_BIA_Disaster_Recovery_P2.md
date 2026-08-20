# Incident Response, Business Continuity, and Disaster Recovery

## Table of Contents

1. [Incident Response](#1-incident-response)
   - [1.1 Core Incident Response Concepts](#11-core-incident-response-concepts)
   - [1.2 Incident Response Lifecycle](#12-incident-response-lifecycle)
   - [1.3 Incident Response Plan — IRP](#13-incident-response-plan--irp)
   - [1.4 Incident Response Team](#14-incident-response-team)
   - [1.5 Detection and Investigation](#15-detection-and-investigation)
   - [1.6 Evidence Handling](#16-evidence-handling)
   - [1.7 Post-Incident Activities](#17-post-incident-activities)
2. [Business Continuity](#2-business-continuity)
   - [2.1 Business Continuity Fundamentals](#21-business-continuity-fundamentals)
   - [2.2 Business Continuity Plan — BCP](#22-business-continuity-plan--bcp)
   - [2.3 Business Impact Analysis — BIA](#23-business-impact-analysis--bia)
   - [2.4 Recovery Objectives from BIA](#24-recovery-objectives-from-bia)
   - [2.5 Business Dependencies](#25-business-dependencies)
   - [2.6 Continuity Strategies](#26-continuity-strategies)
   - [2.7 Business Continuity Testing](#27-business-continuity-testing)
3. [Disaster Recovery](#3-disaster-recovery)
   - [3.1 Disaster Recovery Fundamentals](#31-disaster-recovery-fundamentals)
   - [3.2 Types of Disaster](#32-types-of-disaster)
   - [3.3 Disaster Recovery Plan — DRP](#33-disaster-recovery-plan--drp)
   - [3.4 Recovery Objectives](#34-recovery-objectives)
   - [3.5 Backup and Recovery](#35-backup-and-recovery)
   - [3.6 Alternate Recovery Sites](#36-alternate-recovery-sites)
   - [3.7 Recovery Techniques](#37-recovery-techniques)
   - [3.8 Disaster Recovery Teams](#38-disaster-recovery-teams)
   - [3.9 Disaster Recovery Testing](#39-disaster-recovery-testing)
4. [Relationship Between the Three Areas](#4-relationship-between-the-three-areas)
5. [Final Review Sheet](#5-final-review-sheet)

---

# 1. Incident Response

**Incident Response** is the structured process used to prepare for, detect, investigate, contain, eradicate, and recover from cybersecurity incidents.

Main question:

> How do we handle a cybersecurity incident?

Main plan:

> **IRP — Incident Response Plan**

---

## 1.1 Core Incident Response Concepts

### Event

An **event** is any observable occurrence in a system, application, network, or security environment.

Examples:

- Successful login
- Failed login
- File creation
- Password change
- Firewall connection
- USB device connected

Not every event is malicious.

```text
User logs in
    ↓
Security Event
```

---

### Incident

A **security incident** is an event or group of events that threatens or violates:

```text
Confidentiality
Integrity
Availability
```

Examples:

- Malware infection
- Account compromise
- Ransomware
- Unauthorized access
- DDoS
- Data exfiltration

---

### Breach

A **breach** usually involves unauthorized access to, disclosure of, or acquisition of protected or sensitive information.

```text
Database Compromised
        ↓
Customer Data Stolen
        ↓
Data Breach
```

A breach is a type of incident, but not every incident is a breach.

---

### Intrusion

An **intrusion** is unauthorized entry into:

- A network
- A computer
- An application
- A cloud environment
- An account

Example:

```text
Stolen Credentials
       ↓
Unauthorized VPN Login
       ↓
Intrusion
```

---

### Threat

A **threat** is something capable of causing harm.

Examples:

```text
Cybercriminal
Malware
Ransomware
Insider
Fire
Flood
Hardware Failure
```

Memory:

> Threat = something that can cause harm.

---

### Vulnerability

A **vulnerability** is a weakness that could be exploited.

Examples:

```text
Weak Password
Missing Patch
SQL Injection
Public Cloud Storage
Incorrect Firewall Rule
Excessive Permissions
```

Memory:

> Vulnerability = weakness.

---

### Exploit

An **exploit** is a method, technique, or code that takes advantage of a vulnerability.

```text
Vulnerability
      ↓
Exploit
      ↓
Unauthorized Action
```

Example:

```text
Vulnerability:
SQL Injection

Exploit:
Crafted SQL Input

Result:
Unauthorized Database Access
```

---

### Zero-Day

A **zero-day vulnerability** is a newly discovered or previously unknown vulnerability for which defenders may not yet have an effective fix deployed.

A **zero-day exploit** takes advantage of that vulnerability.

```text
Unknown Vulnerability
        ↓
No Effective Patch Yet
        ↓
Attacker Exploits It
        ↓
Zero-Day Attack
```

---

### How the Concepts Connect

```text
Asset
  ↓
Vulnerability
  ↓
Threat
  ↓
Exploit
  ↓
Intrusion
  ↓
Incident
  ↓
Possible Breach
```

---

## 1.2 Incident Response Lifecycle

The classic incident-response lifecycle can be organized as:

```text
Preparation
    ↓
Detection and Analysis
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Post-Incident Activity
```

### Preparation

Preparation happens before the incident.

Activities include:

- Create an Incident Response Plan
- Define roles
- Train employees
- Deploy SIEM
- Deploy EDR
- Enable logging
- Maintain backups
- Prepare forensic tools
- Create playbooks
- Test communications

```text
People + Process + Technology
            ↓
       Preparation
```

---

### Detection and Analysis

Goal:

> Determine whether suspicious activity is a real security incident.

Sources:

```text
SIEM
EDR
IDS / IPS
Firewall Logs
Cloud Logs
User Reports
Threat Intelligence
Email Security
```

Typical process:

```text
Alert
 ↓
Validate
 ↓
Analyze
 ↓
Determine Scope
 ↓
Determine Severity
 ↓
Classify Incident
```

Important questions:

- What happened?
- When did it start?
- What systems are affected?
- Which users are affected?
- What data is involved?
- How did the attacker enter?
- Is the attacker still active?

---

### Containment

Containment limits damage and stops the spread.

Examples:

- Isolate infected devices
- Disable compromised accounts
- Block malicious IP addresses
- Revoke sessions/tokens
- Disconnect affected network segments

#### Short-Term Containment

Immediate action.

Example:

```text
Disconnect infected laptop
```

#### Long-Term Containment

Temporary secure operation while permanent remediation is prepared.

---

### Eradication

Eradication removes the attacker's presence and the root cause.

Examples:

```text
Remove Malware
Patch Vulnerability
Delete Persistence
Reset Credentials
Remove Malicious Accounts
Fix Misconfiguration
Reimage System
```

Correct approach:

```text
Malware Removed
      +
Root Cause Fixed
      +
Credentials Rotated
      +
Persistence Removed
```

---

### Recovery

Recovery returns systems safely to normal operations.

Activities:

- Restore clean backups
- Rebuild systems
- Patch systems
- Restore databases
- Validate security
- Reconnect systems
- Monitor for reinfection

```text
Clean System
    ↓
Restore
    ↓
Validate
    ↓
Return to Production
```

---

### Post-Incident Activity

After an incident:

```text
Review
  ↓
Root Cause Analysis
  ↓
Lessons Learned
  ↓
Improve Controls
  ↓
Update Plans
  ↓
Training
```

Questions:

- What happened?
- Why did it happen?
- What worked?
- What failed?
- Was detection fast enough?
- Were backups usable?
- What should be improved?

---

## 1.3 Incident Response Plan — IRP

An **Incident Response Plan — IRP** defines how an organization will handle cybersecurity incidents.

It should answer:

```text
Who responds?
What do they do?
When do they escalate?
Who must be contacted?
How is evidence handled?
How is recovery coordinated?
```

Core components:

- Purpose and scope
- Roles and responsibilities
- Incident classification
- Severity levels
- Escalation process
- Communication plan
- Response playbooks
- Evidence-handling rules
- Documentation requirements
- Legal/regulatory notification procedures

Example escalation:

```text
SOC Analyst
    ↓
Incident Response Lead
    ↓
Security Manager
    ↓
CISO
    ↓
Executives
```

---

## 1.4 Incident Response Team

Possible members:

```text
SOC Analysts
Incident Responders
Security Engineers
System Administrators
Network Engineers
Cloud Engineers
Digital Forensics
Legal
Compliance
Human Resources
Management
Public Relations
```

Different incidents require different combinations.

---

## 1.5 Detection and Investigation

Important tools and sources:

### SIEM

Collects and correlates logs.

```text
Logs
 ↓
SIEM
 ↓
Correlation
 ↓
Alert
```

### EDR

Monitors endpoint behavior.

Examples:

- Processes
- Files
- Network connections
- Registry changes
- Command execution

### IDS / IPS

Detects or blocks suspicious network traffic.

### Firewall Logs

Show permitted and denied network connections.

### Cloud Logs

Examples:

- AWS CloudTrail
- Azure Activity Logs
- GCP Audit Logs

### Threat Intelligence

Provides information about:

- Threat actors
- Malware
- Malicious IPs
- Domains
- Attack techniques

---

## 1.6 Evidence Handling

Possible evidence:

```text
Logs
Disk Images
Memory Captures
Emails
Malware Samples
Network Captures
Cloud Audit Logs
Screenshots
```

Documentation should record:

```text
Who
What
When
Where
How
Actions Taken
Evidence Collected
```

### Chain of Custody

A **chain of custody** documents:

- Who collected the evidence
- When it was collected
- Where it was stored
- Who accessed it
- Any transfers of custody

This is especially important when evidence may be used in legal or disciplinary proceedings.

---

## 1.7 Post-Incident Activities

Important activities include:

- Root cause analysis
- Lessons learned
- Improve security controls
- Update policies
- Update playbooks
- Improve monitoring
- Improve employee awareness
- Review incident-response performance

---

# 2. Business Continuity

**Business Continuity — BC** is the ability of an organization to continue delivering critical products and services during and after a disruption.

Main question:

> How do we keep critical business operations running?

Main plan:

> **BCP — Business Continuity Plan**

---

## 2.1 Business Continuity Fundamentals

Business continuity is broader than IT.

It includes:

```text
People
Processes
Technology
Facilities
Suppliers
Communication
```

Possible disruptions:

- Cyberattack
- Ransomware
- Power failure
- Fire
- Flood
- Cloud outage
- Network outage
- Pandemic
- Supplier failure

---

## 2.2 Business Continuity Plan — BCP

A **Business Continuity Plan — BCP** explains how critical business operations will continue during disruption.

Typical components:

- Critical business functions
- Responsible personnel
- Alternative work locations
- Remote-work arrangements
- Manual workarounds
- Communication procedures
- Supplier alternatives
- Emergency contacts
- Business dependencies
- Recovery priorities

Example:

```text
Primary Office Unavailable
        ↓
Remote Work Activated
        ↓
Alternate Systems Used
        ↓
Critical Business Continues
```

---

## 2.3 Business Impact Analysis — BIA

A **Business Impact Analysis — BIA** belongs primarily under **Business Continuity**.

It identifies:

```text
Critical Business Functions
Business Dependencies
Impact of Downtime
Recovery Priorities
Recovery Requirements
```

Main questions:

- Which business processes are critical?
- What systems support them?
- What happens if they stop?
- How long can they be unavailable?
- How much data loss can be tolerated?
- Which services must recover first?

---

### BIA Impact Categories

#### Financial Impact

Examples:

- Lost revenue
- Contract penalties
- Recovery costs

#### Operational Impact

Examples:

- Production stopped
- Orders delayed
- Employees unable to work

#### Legal Impact

Examples:

- Lawsuits
- Contract violations

#### Regulatory Impact

Examples:

- Compliance violations
- Regulatory penalties

#### Reputational Impact

Examples:

- Customer trust loss
- Brand damage

#### Safety Impact

Examples:

- Employee safety
- Public safety
- Industrial-process risks

---

### BIA Process

```text
1. Identify Business Processes
        ↓
2. Identify Critical Functions
        ↓
3. Identify Dependencies
        ↓
4. Evaluate Downtime Impact
        ↓
5. Determine Maximum Tolerable Downtime
        ↓
6. Define RTO
        ↓
7. Define RPO
        ↓
8. Prioritize Recovery
```

---

### BIA Example

| Business Function | Impact | RTO | RPO | Priority |
|---|---|---:|---:|---|
| Payment System | Critical | 30 min | 5 min | 1 |
| ERP | Critical | 4 hr | 30 min | 1 |
| Customer Support | High | 4 hr | 1 hr | 2 |
| Email | Medium | 8 hr | 4 hr | 2 |
| HR Portal | Medium | 24 hr | 24 hr | 3 |

---

## 2.4 Recovery Objectives from BIA

The BIA helps define recovery targets used by both Business Continuity and Disaster Recovery.

### RTO — Recovery Time Objective

**RTO** defines how quickly a service must be restored.

Main question:

> How long can this service remain unavailable?

Example:

```text
Failure:
10:00 AM

RTO:
2 Hours

Recovery Target:
12:00 PM
```

Memory:

```text
RTO
T = TIME to recover
```

---

### RPO — Recovery Point Objective

**RPO** defines how much recent data loss can be tolerated.

Main question:

> How far back in time can our recovered data be?

Example:

```text
Failure:
12:00 PM

RPO:
15 Minutes

Recovery Point:
11:45 AM or newer
```

Memory:

```text
RPO
P = POINT in time
```

---

### RTO vs RPO

| RTO | RPO |
|---|---|
| Recovery Time Objective | Recovery Point Objective |
| Focuses on downtime | Focuses on data loss |
| How quickly must we recover? | How much recent data can we lose? |
| Influences recovery architecture | Influences backup/replication |

Timeline:

```text
11:45 AM             12:00 PM              2:00 PM
   │                     │                    │
   │<------ RPO -------->│<------ RTO ------>│
   │                     │                    │
Recovery Point        Failure           Recovery Target
```

---

### MTD — Maximum Tolerable Downtime

**MTD** is the longest period a business function can be unavailable before the impact becomes unacceptable.

Example:

```text
RTO = 4 hours
MTD = 8 hours
```

Conceptually:

```text
RTO < MTD
```

The organization should recover before reaching the maximum tolerable outage.

---

### MTPD — Maximum Tolerable Period of Disruption

This is a closely related term to MTD.

It represents the longest tolerable disruption period before unacceptable consequences occur.

---

## 2.5 Business Dependencies

A BIA identifies dependencies such as:

### People

- Employees
- Managers
- Specialists
- Vendors

### Facilities

- Offices
- Factories
- Data centers
- Warehouses

### Technology

- Applications
- Databases
- Networks
- Cloud platforms
- Identity systems

### Suppliers

- Raw-material suppliers
- Cloud providers
- Software vendors
- Logistics partners

---

## 2.6 Continuity Strategies

Possible strategies include:

### Remote Work

Employees operate from home or alternate locations.

### Alternate Facilities

Use another office, factory, or work site.

### Manual Workarounds

Example:

```text
ERP Down
   ↓
Temporary Manual Order Processing
```

### Alternate Suppliers

Switch to backup suppliers if the primary supplier cannot deliver.

### Redundant Staff

Cross-train employees so critical tasks are not dependent on one person.

### Alternate Communication

Examples:

- Secondary phone system
- Emergency email service
- Messaging platform
- Satellite communications

---

## 2.7 Business Continuity Testing

Plans must be tested.

Common methods:

### Tabletop Exercise

Team discusses a simulated incident.

### Walkthrough

Teams review the plan step by step.

### Simulation

Organization simulates a realistic disruption.

### Parallel Test

Backup systems operate alongside primary systems.

### Full Interruption

Primary operations are intentionally stopped and recovery mechanisms are used.

This provides the strongest test but also carries the most operational risk.

---

# 3. Disaster Recovery

**Disaster Recovery — DR** focuses on restoring IT infrastructure, systems, applications, services, and data after a major disruption.

Main question:

> How do we restore the technology?

Main plan:

> **DRP — Disaster Recovery Plan**

---

## 3.1 Disaster Recovery Fundamentals

Disaster Recovery focuses mainly on:

```text
Servers
Networks
Databases
Cloud Services
Applications
Storage
Backups
Identity Systems
```

Main objectives:

- Restore critical IT services
- Restore business data
- Meet RTO requirements
- Meet RPO requirements
- Recover securely
- Return to normal operations

---

## 3.2 Types of Disaster

### Cyber Disasters

Examples:

```text
Ransomware
Destructive Malware
Cloud Compromise
Major Cyberattack
```

### Technical Disasters

Examples:

```text
Server Failure
Storage Failure
Network Failure
Database Corruption
```

### Environmental Disasters

Examples:

```text
Fire
Flood
Earthquake
Power Failure
```

### Human-Caused Disasters

Examples:

```text
Accidental Deletion
Misconfiguration
Sabotage
```

---

## 3.3 Disaster Recovery Plan — DRP

A **Disaster Recovery Plan — DRP** defines how the organization will restore technology after a disaster.

Core components:

### Executive Summary

High-level overview:

- Purpose
- Scope
- Objectives
- Management responsibilities

### Department-Specific Plans

Examples:

```text
IT
Finance
Production
Sales
HR
Customer Service
```

### Technical Recovery Guides

Examples:

```text
Database Restore Procedure
Server Rebuild Procedure
Network Recovery
Cloud Failover
Backup Restoration
```

### Recovery Roles

Define responsibilities for:

- Recovery team
- IT personnel
- Management
- Vendors
- Communications/PR

### Emergency Contacts

Maintain current contact information for:

- Internal teams
- Cloud providers
- Internet providers
- Hardware vendors
- Security vendors
- Emergency services

### Copies of the DRP

The plan must remain accessible even when primary systems are unavailable.

Examples:

- Offline copy
- Printed copy
- Secure external storage
- Protected cloud copy

---

## 3.4 Recovery Objectives

Disaster Recovery **uses the RTO and RPO defined from BIA/business continuity requirements**.

Example:

```text
BIA
 ↓
ERP is Critical
 ↓
RTO = 4 hours
RPO = 30 minutes
 ↓
DR Architecture Must Meet These Targets
```

### Recovery Priority

Systems are restored according to business importance.

Example:

```text
1. Identity Services
2. Network
3. Core Database
4. ERP
5. Customer Portal
6. Email
7. Internal Reporting
```

---

## 3.5 Backup and Recovery

### Full Backup

Copies all selected data.

Advantages:

- Easy restore

Disadvantages:

- More storage
- Longer backup time

---

### Incremental Backup

Copies changes since the last backup.

Example:

```text
Sunday → Full
Monday → Incremental
Tuesday → Incremental
Wednesday → Incremental
```

Advantages:

- Fast
- Less storage

---

### Differential Backup

Copies all changes since the last full backup.

Example:

```text
Sunday → Full
Monday → Changes since Sunday
Tuesday → Changes since Sunday
Wednesday → Changes since Sunday
```

Restore usually requires:

```text
Full Backup
+
Latest Differential
```

---

### Snapshots

Capture the state of a system, VM, volume, or database at a point in time.

Useful for:

- Fast restoration
- Testing
- Rollback

Snapshots are not always a complete replacement for independent backups.

---

### Replication

Copies data to another location or system.

Used when low RPO values are required.

Example:

```text
RPO = 5 minutes
```

A backup once every 24 hours would not satisfy that requirement.

---

### Offline / Immutable Backups

Important against ransomware.

```text
Production Data
      ↓
Backup
      ↓
Offline / Immutable Copy
```

The attacker should not be able to modify or delete all backup copies.

---

## 3.6 Alternate Recovery Sites

### Hot Site

A fully or nearly fully prepared recovery environment.

Characteristics:

```text
Infrastructure Ready
Data Replicated
Fast Activation
```

Advantages:

- Fastest recovery

Disadvantages:

- Highest cost

---

### Warm Site

Partially prepared recovery environment.

Characteristics:

```text
Infrastructure Available
Some Configuration Needed
Data Restore May Be Required
```

Advantages:

- Moderate cost
- Moderate recovery time

---

### Cold Site

Basic facility with power/connectivity but limited preinstalled technology.

Characteristics:

```text
Facility Available
Hardware / Software Must Be Installed
Data Must Be Restored
```

Advantages:

- Lowest cost

Disadvantages:

- Slowest recovery

---

## 3.7 Recovery Techniques

### Failover

Switch service to a secondary system.

```text
Primary
   ↓ Failure
Secondary
   ↓
Service Continues
```

### High Availability

Use redundant components to minimize downtime.

### Database Replication

Keep copies of data synchronized across systems.

### Cloud Recovery

Restore systems in a cloud environment.

### Server Rebuild

Recreate compromised/damaged servers from trusted images.

### Data Restoration

Restore from known-clean backups.

---

## 3.8 Disaster Recovery Teams

### Recovery Team

Coordinates overall recovery.

Responsibilities:

- Activate DRP
- Assign priorities
- Track progress
- Coordinate communication

### IT Personnel

Perform technical recovery:

```text
Check Backups
Start Alternate Site
Restore Identity
Restore Network
Restore Database
Restore Applications
Validate Security
```

### Management

Responsible for:

- Business decisions
- Resource allocation
- Escalation
- Risk acceptance

### Public Relations / Communication

Provide accurate information to:

- Employees
- Customers
- Regulators
- Media

---

## 3.9 Disaster Recovery Testing

A DRP must be tested.

### Backup Restore Test

Verify backups can actually be restored.

### Failover Test

Switch services to a secondary environment.

### Alternate-Site Test

Verify the alternate recovery site functions.

### Simulation

Simulate a disaster without stopping production.

### Full Interruption Test

Stop the primary environment and recover using the DR site.

This is highly realistic but also the most disruptive.

---

# 4. Relationship Between the Three Areas

The three domains are related but have different objectives.

```text
                     DISRUPTION
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ↓              ↓              ↓
     INCIDENT        BUSINESS       DISASTER
     RESPONSE       CONTINUITY      RECOVERY
          │              │              │
   Handle security   Keep critical   Restore IT
      incident        business        systems
                      running
          │              │              │
          ↓              ↓              ↓
         IRP            BCP            DRP
                         │
                         ↓
                        BIA
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
             RTO        RPO        MTD
                         │
                         ↓
               Recovery Requirements
                         │
                         ↓
                Disaster Recovery
```

## Main Difference

| Area | Main Question | Main Plan |
|---|---|---|
| Incident Response | How do we handle the incident? | IRP |
| Business Continuity | How do we keep the business running? | BCP |
| Disaster Recovery | How do we restore technology? | DRP |

---

## Important Relationship: BIA

**BIA belongs primarily under Business Continuity.**

It determines:

```text
Critical Business Functions
        ↓
Business Impact
        ↓
Recovery Priorities
        ↓
RTO
RPO
MTD
```

Those targets are then used by Disaster Recovery.

```text
Business Continuity / BIA
          ↓
Defines RTO + RPO
          ↓
Disaster Recovery
          ↓
Designs Technical Recovery
```

---

# 5. Final Review Sheet

## Incident Response

```text
Main Goal:
Handle a cybersecurity incident

Main Plan:
IRP

Core Lifecycle:
Preparation
↓
Detection and Analysis
↓
Containment
↓
Eradication
↓
Recovery
↓
Post-Incident
```

Core terms:

```text
Event
Threat
Vulnerability
Exploit
Intrusion
Incident
Breach
Zero-Day
```

---

## Business Continuity

```text
Main Goal:
Keep critical business operations running

Main Plan:
BCP

Important Analysis:
BIA
```

BIA determines:

```text
Critical Functions
Dependencies
Impact
Recovery Priority
RTO
RPO
MTD
```

---

## Disaster Recovery

```text
Main Goal:
Restore IT systems and data

Main Plan:
DRP
```

Important areas:

```text
Backups
Replication
Failover
Hot Site
Warm Site
Cold Site
System Restoration
Database Recovery
Cloud Recovery
```

---

## RTO

```text
Recovery Time Objective

Question:
How quickly must we recover?
```

---

## RPO

```text
Recovery Point Objective

Question:
How much recent data can we lose?
```

---

## MTD

```text
Maximum Tolerable Downtime

Question:
What is the maximum outage the business can tolerate?
```

---

## Complete Memory Model

```text
Incident Response
→ Handle the attack

Business Continuity
→ Keep the business running

BIA
→ Determine criticality and recovery requirements

Disaster Recovery
→ Restore the technology

RTO
→ Maximum target recovery time

RPO
→ Maximum acceptable data-loss window

MTD
→ Maximum tolerable business outage
```
