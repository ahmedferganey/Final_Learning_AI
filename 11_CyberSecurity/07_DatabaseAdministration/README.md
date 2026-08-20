# Phase 7 — Database

This phase develops a complete database foundation from **relational database design and SQL** through **Oracle development and administration**, then expands into **NoSQL and cloud database architecture**.

The phase is designed as one dependency chain:

```text
28. MySQL Database
        ↓
29. Oracle SQL and PL/SQL
        ↓
30. Oracle Database Administration I
        ↓
31. Oracle Database Administration II
        ↓
32. NoSQL Databases
        ↓
33. Cloud Database Fundamentals
```

The logic behind the sequence is:

```text
Relational Data + SQL
        ↓
Oracle SQL + Procedural Programming
        ↓
Oracle Core Administration
        ↓
Backup / Recovery / Performance / HA
        ↓
Non-Relational + Distributed Data Models
        ↓
Managed / Distributed Databases in Cloud
```

---

# Phase Goal

By the end of Phase 7, you should be able to move through the full database lifecycle:

```text
Business Requirement
        ↓
Data Modeling
        ↓
Schema Design
        ↓
SQL Development
        ↓
Transactions / Concurrency
        ↓
Indexing / Query Optimization
        ↓
Database Administration
        ↓
Backup / Recovery
        ↓
Performance / Troubleshooting
        ↓
High Availability / Disaster Recovery
        ↓
NoSQL / Distributed Data
        ↓
Cloud Database Architecture
        ↓
Migration / Security / Monitoring / Cost
```

This phase is therefore useful for learners targeting:

- Database Administration
- Cloud Engineering
- Backend Engineering
- DevOps / SRE
- Data Engineering
- Infrastructure Engineering
- Cybersecurity
- Cloud Security
- Solution Architecture

---

# Courses

## 28. MySQL Database

**File:** `28_MySQL_Database.md`

This course establishes the relational database foundation.

Main learning path:

```text
Relational Model
    ↓
Tables / Rows / Columns
    ↓
Primary / Foreign / Composite Keys
    ↓
Relationships
    ↓
DDL / DML / DCL / TCL
    ↓
SELECT / Filtering
    ↓
Functions
    ↓
GROUP BY / HAVING
    ↓
JOINs
    ↓
Subqueries / CTEs
    ↓
Views
    ↓
Normalization
    ↓
Indexes
    ↓
EXPLAIN
    ↓
Transactions / ACID
    ↓
Isolation Levels
    ↓
MVCC
    ↓
Locks / Deadlocks
    ↓
Stored Logic
    ↓
Users / Roles
    ↓
InnoDB Architecture
    ↓
Backup / PITR
    ↓
Replication / HA
    ↓
Monitoring / Security
```

You should finish this course able to:

- design a normalized relational schema;
- write practical SQL;
- reason about joins and query cardinality;
- understand indexes and execution plans;
- explain ACID, isolation, MVCC, locking, and deadlocks;
- perform logical backup and restore;
- explain replication and database availability concepts;
- troubleshoot common MySQL failures.

### Course Project

**Manufacturing Operations Database**

The project includes:

```text
Customer
Product
Orders
OrderItem
Machine
ProductionRun
QualityInspection
Inventory
```

and requires schema design, queries, indexes, transactions, security, backup, monitoring, and troubleshooting.

---

## 29. Oracle SQL and PL/SQL

**File:** `29_Oracle_SQL_and_PLSQL.md`

This course moves from general relational SQL into Oracle-specific SQL and PL/SQL.

Main learning path:

```text
Oracle SQL
    ↓
Oracle Data Types
    ↓
Functions / Conversion
    ↓
JOINs / Subqueries
    ↓
Set Operators
    ↓
ROLLUP / CUBE / GROUPING SETS
    ↓
Analytic Functions
    ↓
Hierarchical Queries
    ↓
PIVOT / UNPIVOT
    ↓
MERGE
    ↓
Sequences / Identity
    ↓
Views / Synonyms / Indexes
    ↓
Oracle Data Dictionary
    ↓
PL/SQL Blocks
    ↓
Variables / %TYPE / %ROWTYPE
    ↓
Conditions / Loops
    ↓
Cursors
    ↓
Exceptions
    ↓
Procedures / Functions
    ↓
Packages
    ↓
Triggers
    ↓
Collections
    ↓
Dynamic SQL
    ↓
BULK COLLECT / FORALL
    ↓
Security / Rights
    ↓
Debugging
```

Important Oracle concepts include:

- `VARCHAR2`, `NUMBER`, `DATE`, and `TIMESTAMP`;
- `NVL`, `COALESCE`, `CASE`, and Oracle conversion functions;
- analytic/window functions such as `ROW_NUMBER`, `RANK`, `LAG`, and `LEAD`;
- sequences and identity columns;
- `USER_*`, `ALL_*`, and `DBA_*` dictionary view families;
- PL/SQL block architecture;
- implicit and explicit cursors;
- `RAISE_APPLICATION_ERROR`;
- package specifications and package bodies;
- `:OLD` and `:NEW` in triggers;
- dynamic SQL and bind variables;
- `BULK COLLECT` and `FORALL`;
- definer-rights and invoker-rights security.

### Course Project

**Oracle Manufacturing Reporting and Order API**

The project builds both:

```text
Reporting SQL
+
Controlled PL/SQL Package API
```

with schema objects, analytic reports, packages, exception handling, triggers, bulk processing, security, and troubleshooting.

---

## 30. Oracle Database Administration I

**File:** `30_Oracle_Database_Administration_I.md`

This is the first true Oracle DBA course.

Main learning path:

```text
Oracle DBA Role
    ↓
Instance vs Database
    ↓
CDB / PDB
    ↓
SGA / PGA
    ↓
Background Processes
    ↓
Physical Database Files
    ↓
Logical Storage
    ↓
Oracle Software Layout
    ↓
Database Creation
    ↓
NOMOUNT / MOUNT / OPEN
    ↓
PFILE / SPFILE
    ↓
Initialization Parameters
    ↓
Oracle Net / Listener
    ↓
Services
    ↓
Users / Roles / Privileges
    ↓
Profiles / Quotas
    ↓
Tablespaces
    ↓
TEMP / UNDO
    ↓
Redo / Log Switches
    ↓
Control Files
    ↓
ARCHIVELOG
    ↓
Fast Recovery Area
    ↓
PDB Administration
    ↓
Dictionary / V$ Views
    ↓
Sessions / Blocking
    ↓
ADR / Alert Log
    ↓
Auditing / Security
```

Architecture to understand:

```text
Client
   |
Oracle Listener
   |
Database Service
   |
Oracle Instance
   |
   +-- SGA
   +-- Background Processes
   |
CDB
   |
   +-- CDB$ROOT
   +-- PDB$SEED
   +-- Application PDB
   |
Datafiles / Control Files / Redo
```

### Course Project

**MANUCDB / MANUPDB Administration**

You create and operate a multitenant Oracle environment with:

- storage;
- users and roles;
- listener/services;
- PDB administration;
- redo and ARCHIVELOG;
- FRA design;
- daily health checks;
- security baseline;
- failure simulations.

---

## 31. Oracle Database Administration II

**File:** `31_Oracle_Database_Administration_II.md`

This course extends core administration into production-grade recovery, performance, security, and availability.

Main learning path:

```text
Failure Types
    ↓
Instance Recovery
    ↓
Media Recovery
    ↓
RMAN
    ↓
Full / Incremental Backup
    ↓
Archived Redo
    ↓
Validation / CROSSCHECK
    ↓
Restore / Recover
    ↓
Control File / SPFILE Recovery
    ↓
PITR / RESETLOGS
    ↓
Flashback
    ↓
Data Pump
    ↓
Performance Methodology
    ↓
Wait Events
    ↓
Execution Plans
    ↓
Optimizer Statistics
    ↓
SQL Tuning
    ↓
AWR / ADDM / ASH Concepts
    ↓
PGA / TEMP / UNDO / Redo
    ↓
Blocking / Deadlocks
    ↓
Resource Manager
    ↓
Unified Auditing
    ↓
TDE
    ↓
Data Guard
    ↓
Switchover / Failover
    ↓
RAC / Clusterware / SCAN
    ↓
Patching / Upgrade
    ↓
Automation / Runbooks
```

A core recovery model from this course is:

```text
Backup File
    |
 RESTORE
    ↓
Restored Datafile
    |
 RECOVER
    ↓
Apply Redo
    |
    v
Recovered Database
```

And the HA/DR distinction:

```text
RAC
multiple instances
shared database

Data Guard
primary database
+
separate standby database
```

### Course Project

**Oracle Recovery, Performance, and DR Operations**

The project requires:

- RMAN backup policy;
- restore drills;
- PITR;
- Flashback;
- Data Pump;
- SQL performance investigation;
- auditing and encryption design;
- Data Guard design;
- RAC architecture;
- patch planning;
- disaster-recovery runbooks.

---

## 32. NoSQL Databases

**File:** `32_NoSQL_Databases.md`

This course expands from relational databases into distributed and non-relational data models.

The decision model is:

```text
Workload
    ↓
Access Pattern
    ↓
Data Model
    ↓
Consistency
    ↓
Scaling
    ↓
Database Type
```

Database models covered:

```text
Relational
Key-Value
Document
Wide-Column
Graph
Time-Series
Search-Oriented
```

The course includes:

```text
CAP
PACELC
Consistency Models
Partitioning
Sharding
Replication
Quorum

Redis
  strings
  hashes
  lists
  sets
  sorted sets
  TTL
  caching
  persistence
  replication
  Sentinel
  Cluster

MongoDB
  documents
  BSON
  CRUD
  embedding vs references
  indexes
  aggregation
  replica sets
  elections
  consistency
  sharding

Wide-Column
  partition keys
  clustering keys
  query-first design
  tunable consistency
  tombstones
  compaction

Graph
  nodes
  relationships
  Cypher
  traversals

Time-Series
Search
Polyglot Persistence
```

### Course Project

**Manufacturing Polyglot Database Platform**

Example design:

```text
Relational DB
    Orders / Master Data

Redis
    Cache / Sessions

MongoDB
    Machine Events

Wide-Column
    High-Volume Time-Partitioned Events

Graph DB
    Supplier / Product / Machine Dependencies
```

The project emphasizes **data ownership** so multiple databases do not accidentally become competing sources of truth.

---

## 33. Cloud Database Fundamentals

**File:** `33_Cloud_Database_Fundamentals.md`

This course moves database administration into cloud platforms.

Central question:

```text
Which responsibilities move to the provider,
and which remain with the customer?
```

Main learning path:

```text
On-Premises Database
    ↓
Database on IaaS
    ↓
Managed Database / DBaaS
    ↓
Serverless Database
    ↓
Shared Responsibility
    ↓
Regions / Zones
    ↓
High Availability
    ↓
Standby vs Read Replica
    ↓
Backups / PITR
    ↓
RPO / RTO
    ↓
Cross-Region DR
    ↓
Private Networking
    ↓
VPC / VNet / VCN
    ↓
Private Endpoints
    ↓
IAM / Managed Identity
    ↓
Database Roles
    ↓
Encryption / KMS
    ↓
Secrets
    ↓
Connection Pooling / Proxy
    ↓
Maintenance / Upgrades
    ↓
Scaling
    ↓
Managed NoSQL
    ↓
Monitoring
    ↓
FinOps / Cost
    ↓
Migration
    ↓
CDC
    ↓
Cutover / Rollback
    ↓
Infrastructure as Code
    ↓
Schema CI/CD
    ↓
Compliance / Governance
    ↓
Troubleshooting
```

Provider examples include:

```text
AWS
Azure
Google Cloud
Oracle Cloud
```

but the goal is to learn transferable cloud database architecture rather than memorize one provider console.

### Course Project

**Cloud Manufacturing Database Migration**

The project covers:

- business requirements;
- private network design;
- managed database HA;
- read replicas;
- managed cache;
- identity and secrets;
- encryption;
- backup/PITR;
- migration with CDC;
- Terraform;
- schema CI/CD;
- monitoring;
- cost;
- cross-region DR;
- incident runbooks.

---

# Recommended Study Sequence

Do not study the six courses independently.

Use this dependency flow:

```text
Step 1
28. MySQL Database

Understand:
relational database engineering
SQL
indexes
transactions
concurrency
backup/replication
        ↓

Step 2
29. Oracle SQL and PL/SQL

Add:
Oracle SQL
analytic SQL
PL/SQL programming
packages
triggers
bulk processing
        ↓

Step 3
30. Oracle DBA I

Move from developer to administrator:
instance
memory
processes
storage
network
security
PDBs
        ↓

Step 4
31. Oracle DBA II

Add production operations:
RMAN
recovery
performance
Data Guard
RAC
security
patching
        ↓

Step 5
32. NoSQL Databases

Expand beyond relational:
distributed systems
CAP/PACELC
Redis
MongoDB
wide-column
graph
        ↓

Step 6
33. Cloud Database Fundamentals

Apply everything to:
managed cloud databases
HA
DR
IAM
networking
migration
IaC
cost
```

---

# How to Study Each Course

For every major topic, use this process:

```text
1. Read the explanation
        ↓
2. Re-draw the visualization
        ↓
3. Type the SQL / command manually
        ↓
4. Predict the output before execution
        ↓
5. Run it
        ↓
6. Break one thing intentionally
        ↓
7. Troubleshoot it
        ↓
8. Document what happened
```

Do not only read commands.

For example:

```text
SELECT / SQL
```

should become:

```text
What rows enter?
What filters apply?
What index can be used?
What result cardinality do I expect?
```

And:

```text
database failover
```

should become:

```text
What failed?
What noticed the failure?
What became primary?
How did clients reconnect?
What happened to in-flight transactions?
What is the RPO/RTO?
```

---

# Practical Lab Strategy

Recommended directory:

```text
database-labs/
│
├── mysql/
│   ├── schema/
│   ├── queries/
│   ├── transactions/
│   ├── backup/
│   └── troubleshooting/
│
├── oracle-sql/
│   ├── sql/
│   ├── plsql/
│   ├── packages/
│   └── triggers/
│
├── oracle-dba/
│   ├── administration/
│   ├── rman/
│   ├── performance/
│   ├── dataguard/
│   └── runbooks/
│
├── nosql/
│   ├── redis/
│   ├── mongodb/
│   ├── wide-column/
│   └── graph/
│
└── cloud-database/
    ├── architecture/
    ├── terraform/
    ├── migrations/
    ├── monitoring/
    └── dr/
```

Keep commands/scripts in version control, but **never commit real credentials or production data**.

---

# Phase 7 Integrated Architecture

By the end of the phase, you should understand an architecture like:

```text
                           USERS
                             |
                         Application
                             |
              +--------------+---------------+
              |                              |
              v                              v
         Managed SQL                      Redis Cache
              |
        +-----+------+
        |            |
        v            v
   HA Standby     Read Replica
        |
        +----------------------------+
        |                            |
        v                            v
     Backups                    CDC / Events
        |                            |
        v                            +------> MongoDB
   PITR / DR                        |
                                     +------> Analytics
                                     |
                                     +------> Graph Projection
```

and be able to answer:

```text
Where is the source of truth?
How are transactions protected?
What happens during failure?
Where are backups?
How is access controlled?
How is data encrypted?
What can become stale?
What is the RPO?
What is the RTO?
How do we monitor it?
How much does it cost?
```

---

# Phase 7 Capstone Challenge

After completing all six courses, design one complete database platform for a manufacturing company.

Requirements:

```text
Transactional Database
    relational SQL

Reporting
    optimized read queries

Cache
    Redis-style

Flexible Event Data
    document DB

Backup
    full + incremental/log based

Recovery
    PITR

High Availability
    local/zone failure protection

Disaster Recovery
    cross-region/site design

Security
    least privilege
    TLS
    encryption
    secrets
    audit

Monitoring
    query latency
    connections
    storage
    replication
    backup
    cost

Infrastructure as Code
    cloud database/network/security definition

Migration
    source assessment
    CDC
    cutover
    rollback
```

Deliver:

```text
ARCHITECTURE.md
ERD.md
SQL_SCHEMA.sql
QUERY_PACK.sql
SECURITY.md
BACKUP_RECOVERY.md
NOSQL_DESIGN.md
CLOUD_DATABASE.md
MIGRATION.md
MONITORING.md
DR_RUNBOOK.md
TROUBLESHOOTING.md
```

---

# Phase 7 Completion Checklist

## Relational Database

- [ ] I can design entities and relationships.
- [ ] I can normalize data to an appropriate relational form.
- [ ] I can write complex SQL queries.
- [ ] I understand JOIN cardinality.
- [ ] I can design indexes.
- [ ] I can interpret query plans.
- [ ] I understand ACID.
- [ ] I understand isolation, MVCC, locks, and deadlocks.

## Oracle Development

- [ ] I can write Oracle SQL.
- [ ] I can use analytic/window functions.
- [ ] I can write PL/SQL blocks.
- [ ] I can use cursors and exceptions.
- [ ] I can create procedures/functions.
- [ ] I can design packages.
- [ ] I understand triggers and their risks.
- [ ] I understand bulk PL/SQL.

## Oracle Administration

- [ ] I understand instance vs database.
- [ ] I understand CDB/PDB architecture.
- [ ] I understand SGA/PGA and background processes.
- [ ] I can manage tablespaces/users/roles.
- [ ] I understand redo, undo, control files, and ARCHIVELOG.
- [ ] I can troubleshoot listener/services.
- [ ] I can inspect sessions and database state.

## Backup, Recovery, and Performance

- [ ] I understand RMAN.
- [ ] I understand restore vs recover.
- [ ] I understand PITR and Flashback.
- [ ] I understand backup validation.
- [ ] I can follow an evidence-based performance workflow.
- [ ] I understand Data Guard.
- [ ] I understand RAC at architecture level.
- [ ] I can write recovery runbooks.

## NoSQL

- [ ] I understand key-value databases.
- [ ] I understand document databases.
- [ ] I understand wide-column databases.
- [ ] I understand graph databases.
- [ ] I understand CAP and PACELC.
- [ ] I understand partitioning and replication.
- [ ] I can design Redis caching.
- [ ] I can model MongoDB documents.
- [ ] I can choose appropriate partition keys.
- [ ] I understand polyglot persistence.

## Cloud Database

- [ ] I understand managed database shared responsibility.
- [ ] I understand region/zone HA.
- [ ] I understand standby vs read replica.
- [ ] I understand backup/PITR/RPO/RTO.
- [ ] I can design private database networking.
- [ ] I understand IAM/managed identity integration.
- [ ] I understand encryption and secret management.
- [ ] I understand connection pooling/proxies.
- [ ] I can design database migration with CDC.
- [ ] I can describe cloud database infrastructure with IaC.
- [ ] I understand database cost drivers.
- [ ] I can create a cross-region DR runbook.

---

# Folder Structure

```text
Phase_7_Database/
│
├── README.md
├── 28_MySQL_Database.md
├── 29_Oracle_SQL_and_PLSQL.md
├── 30_Oracle_Database_Administration_I.md
├── 31_Oracle_Database_Administration_II.md
├── 32_NoSQL_Databases.md
└── 33_Cloud_Database_Fundamentals.md
```

---

# Next Phase

After completing Phase 7, continue with:

```text
Phase 8 — Storage & Data Center

34. Information Storage and Management
        ↓
35. Data Center Infrastructure Design
        ↓
36. Enterprise Backup and Recovery
        ↓
37. Veeam Backup and Replication
```

The dependency is logical:

```text
Databases
   ↓
understand how data is stored
   ↓
understand the data-center infrastructure hosting it
   ↓
understand enterprise-wide backup/recovery
   ↓
implement those concepts with Veeam
```

Do not move to Phase 8 until you are comfortable with at least the **Phase 7 Completion Checklist** above.
