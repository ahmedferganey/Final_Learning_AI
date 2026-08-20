# 30. Oracle Database Administration I

> Phase 7 — Database

This course moves from **Oracle SQL and PL/SQL development** into **database administration**.

The reference baseline is **Oracle AI Database 26ai**. In Oracle Database 21c and later, the supported architecture is multitenant, so this material teaches Oracle administration through the **CDB/PDB model** rather than treating non-CDB architecture as the normal modern design.

The central mental model is:

```text
Clients
   |
Oracle Net
   |
Listener
   |
Database Service
   |
+-----------------------------------+
| Oracle Instance                   |
|-----------------------------------|
| SGA                               |
| Background Processes              |
| Server Processes                  |
+-----------------------------------+
                |
                v
+-----------------------------------+
| Multitenant Database              |
|-----------------------------------|
| CDB$ROOT                          |
| PDB$SEED                          |
| PDB1 / Application PDBs           |
+-----------------------------------+
                |
                v
Datafiles + Control Files + Redo Logs
```

The learning pattern throughout this file is:

```text
Architecture
   ↓
Command / SQL
   ↓
Expected state
   ↓
Why it works
   ↓
Operational use
   ↓
Failure case
   ↓
Troubleshooting
```

The objective is not to memorize Oracle commands. You should be able to reason about **instance state, memory, processes, storage, networking, users, privileges, PDBs, redo/undo, diagnostics, and daily operational health**.

---

## 1. Topic Title

**Oracle Database Administration I**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain the difference between an Oracle instance and an Oracle database.
- Explain the modern CDB/PDB multitenant architecture.
- Identify the SGA, PGA, foreground/server processes, and important background processes.
- Explain datafiles, control files, online redo logs, archived redo logs, tempfiles, parameter files, and password files.
- Explain logical storage using tablespaces, segments, extents, and blocks.
- Install or provision an Oracle database lab and understand Oracle Base, Oracle Home, inventory, and database creation concepts.
- Create and manage a CDB/PDB lab using DBCA or SQL.
- Start and stop the database using `NOMOUNT`, `MOUNT`, and `OPEN`.
- Explain PFILE vs SPFILE and safely manage initialization parameters.
- Configure and troubleshoot Oracle Net, listeners, service names, and client connect descriptors.
- Create and manage users, roles, system privileges, object privileges, quotas, profiles, and account state.
- Create/manage permanent, temporary, and undo tablespaces.
- Explain redo generation, log switches, checkpoints, and ARCHIVELOG mode.
- Inspect control files and understand multiplexing principles.
- Manage PDB open state and save PDB state.
- Use data dictionary and dynamic performance views.
- Diagnose sessions, blockers, basic waits, and invalid objects.
- Use the Automatic Diagnostic Repository and alert log for troubleshooting.
- Apply baseline database security and unified auditing concepts.
- Perform daily DBA health checks and create operational runbooks.
- Build a complete multitenant Oracle administration mini project.

---

## 3. Prerequisites

Required:

- 28. MySQL Database or equivalent relational database foundation
- 29. Oracle SQL and PL/SQL
- Linux fundamentals
- networking fundamentals
- basic storage concepts

Recommended lab:

```text
Oracle Linux / supported Linux VM
4 vCPU
8–12 GB RAM
80+ GB disk
Oracle AI Database 26ai Free or approved Oracle lab
```

Suggested layout:

```text
ORACLE_BASE
   |
   +-- product / Oracle Home
   +-- admin
   +-- diag
   +-- oradata
```

Suggested database:

```text
CDB: MANUCDB
PDB: MANUPDB
```

Safety:

Use disposable lab VMs or snapshots before:

- recreating control files
- changing redo-log structure
- changing ARCHIVELOG mode
- moving datafiles
- changing SPFILE parameters
- dropping PDBs
- changing listener configuration
- testing shutdown/startup failure conditions

---

## 4. Core Concepts Explanation

# Part 1 — The DBA Role

## 1.1 What a Database Administrator Manages

A DBA operates the database as a service.

```text
Application
    |
    v
Database Service
    |
    +-- availability
    +-- storage
    +-- security
    +-- performance
    +-- users
    +-- backup readiness
    +-- diagnostics
```

Typical daily responsibilities:

```text
Check database/PDB state
Check listener/services
Check tablespace usage
Check invalid objects
Check alert log
Check blocking sessions
Check backup status
Review audit/security events
Review capacity
```

## 1.2 DBA vs Developer

Developer focus:

```text
tables
queries
PL/SQL
application logic
```

DBA focus:

```text
instance
memory
processes
storage
security
availability
operations
recovery readiness
```

There is overlap, but the operational boundary matters.

---

# Part 2 — Instance vs Database

## 2.1 Oracle Instance

An instance consists primarily of:

```text
Memory
+
Processes
```

Visualization:

```text
Oracle Instance
   |
   +-- SGA
   |
   +-- background processes
   |
   +-- server processes
```

## 2.2 Oracle Database

The database consists of persistent files/structures.

```text
Database
   |
   +-- datafiles
   +-- control files
   +-- online redo logs
```

Supporting files include:

```text
archived redo
parameter file
password file
tempfiles
diagnostic files
```

## 2.3 Why the Difference Matters

Startup illustrates the difference:

```text
NOMOUNT
instance started
database not mounted

MOUNT
control file opened
database identified
datafiles not yet opened

OPEN
datafiles + redo opened
database available
```

This state model is central to backup/recovery and troubleshooting.

---

# Part 3 — Multitenant Architecture

## 3.1 Modern Architecture

Oracle Database 21c and later support the multitenant architecture as the normal supported model.

```text
CDB
 |
 +-- CDB$ROOT
 |
 +-- PDB$SEED
 |
 +-- MANUPDB
 |
 +-- TESTPDB
```

## 3.2 CDB$ROOT

Contains Oracle-supplied metadata and common infrastructure.

Think:

```text
CDB$ROOT
   |
   +-- common users
   +-- common metadata
   +-- system-wide structures
```

Application data should normally live in PDBs.

## 3.3 PDB$SEED

Template used to create new PDBs.

```text
PDB$SEED
   ↓ clone
NEW PDB
```

Do not treat the seed as a normal application PDB.

## 3.4 Pluggable Database

A PDB appears to applications as a logically separate database.

```text
CDB process/memory infrastructure
          |
          +-- PDB A application
          +-- PDB B application
```

Application connection should usually target a PDB service.

## 3.5 Current Container

Inspect:

```sql
SHOW CON_NAME;
```

Or:

```sql
SELECT SYS_CONTEXT(
    'USERENV',
    'CON_NAME'
) AS container_name
FROM dual;
```

## 3.6 Switch Container

As an appropriately privileged administrator:

```sql
ALTER SESSION
SET CONTAINER = MANUPDB;
```

Verify:

```sql
SHOW CON_NAME;
```

Operational rule:

```text
Before running administration SQL:
confirm container.
```

A command executed in root vs PDB can have very different scope.

---

# Part 4 — Oracle Memory Architecture

## 4.1 SGA

The System Global Area is shared instance memory.

```text
SGA
 |
 +-- Database Buffer Cache
 +-- Shared Pool
 +-- Redo Log Buffer
 +-- Large Pool
 +-- other components
```

## 4.2 PGA

Program Global Area is process/session-specific memory.

```text
Server Process
     |
     +-- sort/hash/work areas
     +-- session/process state
```

Think:

```text
SGA = shared
PGA = process/private
```

## 4.3 Memory Flow

```text
SQL
 ↓
Shared Pool
 ↓
execution
 ↓
Buffer Cache
 ↓
data blocks
```

Sort/hash operations may use PGA work areas.

---

# Part 5 — Database Buffer Cache

## 5.1 Purpose

The buffer cache stores copies of database blocks in memory.

```text
Query needs block
      |
      v
Buffer Cache
   |      |
 hit      miss
   |      |
memory    disk read
```

## 5.2 Dirty Buffers

An UPDATE modifies a block in memory:

```text
disk block v1
   ↓ read
buffer v1
   ↓ update
buffer v2 [dirty]
   ↓ later DBWn
disk block v2
```

The changed block does not need to be written immediately at commit because redo provides recovery protection.

---

# Part 6 — Shared Pool

## 6.1 Library Cache

Stores reusable parsed SQL/PLSQL representations and execution information.

```text
SQL text
  ↓
parse
  ↓
shared cursor
```

Repeated SQL with bind variables can improve cursor reuse.

## 6.2 Data Dictionary Cache

Caches metadata needed by Oracle.

Examples:

```text
object metadata
user metadata
privilege metadata
```

## 6.3 Hard Parse vs Reuse Concept

```text
New SQL shape
    ↓
parse/optimize
    ↓
cursor

Same reusable SQL
    ↓
reuse cursor where possible
```

This is one reason bind variables matter.

---

# Part 7 — Redo Log Buffer

Changes generate redo records in memory.

```text
DML
 |
 +--> buffer-cache change
 |
 +--> redo record
        |
        v
Redo Log Buffer
        |
       LGWR
        |
        v
Online Redo Log
```

Redo protects changes needed for crash recovery.

---

# Part 8 — Important Background Processes

## 8.1 DBWn

Database Writer writes dirty buffers from the buffer cache to datafiles.

```text
Dirty Buffer
   |
 DBWn
   |
Datafile
```

DBWn is not the process that "commits" a transaction.

## 8.2 LGWR

Log Writer writes redo from the redo log buffer to online redo logs.

Commit durability depends heavily on redo being safely written according to database configuration.

```text
COMMIT
  ↓
LGWR writes required redo
  ↓
commit acknowledged
```

## 8.3 CKPT

Checkpoint process coordinates checkpoint information and updates file headers/control-file metadata as appropriate.

Checkpoint does not write all dirty blocks itself.

## 8.4 SMON

System Monitor performs instance-level cleanup/recovery responsibilities.

## 8.5 PMON / Process Management

Oracle process-monitoring infrastructure handles cleanup/registration-related responsibilities.

Exact internal process names evolve across releases, so understand the function rather than memorizing only historical names.

## 8.6 ARCn

Archiver processes copy full online redo logs to archive destinations when ARCHIVELOG mode is enabled.

```text
Online Redo
   |
 log switch
   |
ARCn
   |
Archived Redo
```

## 8.7 MMON

Supports monitoring/statistics-related background work.

Advanced performance tooling appears in DBA II.

---

# Part 9 — Server and Client Processes

## 9.1 Dedicated Server Concept

```text
Client Session
     |
     v
Server Process
     |
     v
Oracle Instance
```

A server process executes SQL on behalf of the session.

## 9.2 Shared Server Concept

Oracle can support shared-server architectures for suitable workloads.

Foundation model:

```text
many clients
   ↓
dispatchers/shared server processes
```

Do not select shared server merely to reduce process count without workload analysis.

---

# Part 10 — Physical Database Files

## 10.1 Datafiles

Contain database data.

```text
Tablespace
   |
   +-- datafile 1
   +-- datafile 2
```

## 10.2 Control Files

Contain critical structural metadata about the database.

Conceptually includes information such as:

```text
database identity
datafile/redo metadata
checkpoint information
```

Loss of all control files is a serious recovery event.

## 10.3 Online Redo Logs

Circular groups used for redo.

```text
Group 1
  ↓ full
Group 2
  ↓ full
Group 3
  ↓
back to Group 1
```

## 10.4 Archived Redo Logs

Copies of completed redo logs in ARCHIVELOG mode.

These enable recovery beyond the last backup.

## 10.5 Tempfiles

Support temporary tablespaces for operations such as sorts/hash work when memory is insufficient.

Tempfiles are handled differently from permanent datafiles because temporary contents are not durable business data.

---

# Part 11 — Logical Storage

Hierarchy:

```text
Database / PDB
    ↓
Tablespace
    ↓
Segment
    ↓
Extent
    ↓
Oracle Block
```

## 11.1 Tablespace

Logical storage container.

Example:

```text
APP_DATA
APP_INDEX
USERS
TEMP
UNDO
```

## 11.2 Segment

Storage allocated to an object.

Examples:

```text
table segment
index segment
LOB segment
```

## 11.3 Extent

A group of contiguous Oracle blocks allocated to a segment.

## 11.4 Block

Smallest normal Oracle database I/O/storage unit.

The database block size may differ from OS filesystem block size.

---

# Part 12 — Core Tablespaces

## 12.1 SYSTEM

Critical data dictionary/system objects.

Do not use SYSTEM for normal application data.

## 12.2 SYSAUX

Auxiliary system components.

## 12.3 USERS

Common default user data tablespace in simple/lab systems.

Production applications usually receive purpose-specific tablespaces.

## 12.4 TEMP

Temporary operations.

## 12.5 UNDO

Stores undo records used for:

```text
rollback
read consistency
recovery support
flashback-related capabilities
```

---

# Part 13 — Oracle Software Layout

## 13.1 Oracle Base

Top-level administrative software/data directory concept.

## 13.2 Oracle Home

Contains one Oracle software installation.

```text
ORACLE_BASE
   |
   +-- product/.../dbhome
```

Environment:

```bash
echo $ORACLE_BASE
echo $ORACLE_HOME
```

## 13.3 Oracle Inventory

Tracks installed Oracle software components/homes.

DBA operations should not treat Oracle Home as an arbitrary folder that can be copied/deleted without Oracle tooling awareness.

---

# Part 14 — Database Creation Tools

## 14.1 DBCA

Database Configuration Assistant helps create/configure databases.

Typical decisions:

```text
database name
CDB/PDB
memory
storage
character set
listener
management
```

## 14.2 Manual Creation Concept

A DBA should understand manual stages even if DBCA is used:

```text
prepare environment
   ↓
create parameter file
   ↓
STARTUP NOMOUNT
   ↓
CREATE DATABASE
   ↓
create dictionary/components
   ↓
create PDB
```

Production creation should follow Oracle's current documented workflow.

---

# Part 15 — Startup States

## 15.1 NOMOUNT

```sql
STARTUP NOMOUNT;
```

State:

```text
parameter file read
SGA allocated
background processes started
control file not opened
```

Used for some creation/recovery operations.

## 15.2 MOUNT

```sql
STARTUP MOUNT;
```

State:

```text
instance started
control file opened
datafiles not opened
```

Used for recovery and certain structural operations.

## 15.3 OPEN

```sql
STARTUP;
```

or:

```sql
ALTER DATABASE OPEN;
```

State:

```text
control files
datafiles
online redo
available
```

## 15.4 Startup Visualization

```text
SHUTDOWN
   |
STARTUP NOMOUNT
   |
   +-- SGA/processes
   |
ALTER DATABASE MOUNT
   |
   +-- control file
   |
ALTER DATABASE OPEN
   |
   +-- datafiles/redo
```

---

# Part 16 — Shutdown Modes

Common modes:

```text
NORMAL
TRANSACTIONAL
IMMEDIATE
ABORT
```

## 16.1 SHUTDOWN IMMEDIATE

Common administrative shutdown:

```sql
SHUTDOWN IMMEDIATE;
```

Oracle ends active user work according to shutdown semantics and performs a clean shutdown.

## 16.2 SHUTDOWN ABORT

Emergency stop:

```sql
SHUTDOWN ABORT;
```

Does not perform normal clean shutdown.

Next startup requires instance recovery.

Use only when appropriate.

---

# Part 17 — PFILE and SPFILE

## 17.1 PFILE

Text initialization parameter file.

Concept:

```text
initSID.ora
```

Human-editable.

## 17.2 SPFILE

Server parameter file.

Binary Oracle-managed parameter repository.

Supports persistent database-managed parameter changes.

## 17.3 Startup Search

If no explicit PFILE is provided, startup uses default SPFILE if available, otherwise default initialization file behavior.

## 17.4 Create PFILE from SPFILE

```sql
CREATE PFILE='/tmp/initMANUCDB.ora'
FROM SPFILE;
```

Useful for backup/diagnosis.

## 17.5 Create SPFILE

```sql
CREATE SPFILE
FROM PFILE='/tmp/initMANUCDB.ora';
```

Only perform when you understand the active instance configuration.

---

# Part 18 — Initialization Parameters

Inspect:

```sql
SHOW PARAMETER memory
```

or:

```sql
SELECT
    name,
    value,
    issys_modifiable
FROM v$parameter
WHERE name LIKE '%memory%';
```

## 18.1 Dynamic vs Static

Some parameters can be modified online.

Others require restart.

## 18.2 SCOPE

Concept:

```text
SCOPE=MEMORY
current instance only

SCOPE=SPFILE
next startup

SCOPE=BOTH
current + persistent, when allowed
```

Example:

```sql
ALTER SYSTEM
SET some_parameter = value
SCOPE=BOTH;
```

Do not copy arbitrary memory/optimizer parameters from internet tuning posts.

---

# Part 19 — Memory Management

Oracle supports automated memory-management mechanisms.

The DBA should understand:

```text
SGA target
PGA target
component sizing
workload response
```

Inspect:

```sql
SHOW PARAMETER sga_target
SHOW PARAMETER pga_aggregate_target
```

Memory tuning should be evidence-based.

Advanced performance tuning belongs to DBA II.

---

# Part 20 — Oracle Net Architecture

Connection path:

```text
Client
  |
connect descriptor
  |
TCP/1521 commonly
  |
Listener
  |
Database Service
  |
Server Process
  |
PDB
```

Oracle Net is a distinct layer from database authentication.

---

# Part 21 — Listener

## 21.1 Listener Purpose

The listener accepts initial client connection requests and routes/redirects them to registered database services.

Check:

```bash
lsnrctl status
```

Start/stop lab listener:

```bash
lsnrctl start
lsnrctl stop
```

## 21.2 Default TCP Port

The standard default listener TCP port is commonly:

```text
1521
```

But do not assume every environment uses it.

## 21.3 Dynamic Service Registration

Modern services can dynamically register with the listener.

Concept:

```text
Database Instance
     |
register service
     |
Listener
```

Static listener configuration is not required for every normal database service.

---

# Part 22 — Service Names

Applications should connect to a service, especially PDB services.

Example concept:

```text
MANUPDB
   |
service: manupdb.example
```

Client does not need to reason directly about Oracle internal process structures.

Inspect services:

```sql
SELECT
    name,
    pdb
FROM v$services
ORDER BY name;
```

---

# Part 23 — Easy Connect and TNS Names

## 23.1 Easy Connect

Concept:

```text
host:port/service
```

Example:

```bash
sql appuser@//db01.example:1521/manupdb.example
```

## 23.2 tnsnames.ora

Alias concept:

```text
MANUPDB =
  host + port + service_name
```

Then client uses:

```text
MANUPDB
```

instead of full descriptor.

## 23.3 Connection Troubleshooting

```text
DNS resolves?
   ↓
TCP/1521 reachable?
   ↓
listener running?
   ↓
service registered?
   ↓
connect descriptor correct?
   ↓
database/PDB open?
   ↓
user authentication?
```

Useful:

```bash
lsnrctl status
```

and network tools such as:

```bash
ss -tln
```

---

# Part 24 — Users and Schemas

In Oracle:

```text
User
   |
owns
   |
Schema
```

Create a PDB-local lab user:

```sql
CREATE USER app_owner
IDENTIFIED BY "LabOnly_StrongPassword1!"
DEFAULT TABLESPACE app_data
TEMPORARY TABLESPACE temp
QUOTA 500M ON app_data;
```

Use secure secret-handling methods in real systems.

---

# Part 25 — System Privileges

Examples:

```text
CREATE SESSION
CREATE TABLE
CREATE VIEW
CREATE PROCEDURE
```

Grant:

```sql
GRANT
    CREATE SESSION,
    CREATE TABLE,
    CREATE VIEW,
    CREATE PROCEDURE
TO app_owner;
```

System privileges authorize database-level capabilities.

---

# Part 26 — Object Privileges

Examples:

```text
SELECT
INSERT
UPDATE
DELETE
EXECUTE
```

Grant:

```sql
GRANT SELECT
ON app_owner.v_order_summary
TO report_user;
```

Object privilege:

```text
specific action
on
specific object
```

---

# Part 27 — Roles

Create:

```sql
CREATE ROLE reporting_role;
```

Grant object access:

```sql
GRANT SELECT
ON app_owner.v_order_summary
TO reporting_role;
```

Assign:

```sql
GRANT reporting_role
TO report_user;
```

Model:

```text
User
 ↓
Role
 ↓
Privileges
```

Roles simplify privilege administration.

---

# Part 28 — Common vs Local Users

In multitenant architecture:

```text
Common User
    scope across CDB containers as designed

Local User
    exists in one PDB
```

Most application users should be local to their application PDB.

Common administrative accounts should be tightly controlled.

Always verify:

```sql
SHOW CON_NAME;
```

before user administration.

---

# Part 29 — User State

Inspect:

```sql
SELECT
    username,
    account_status,
    default_tablespace,
    temporary_tablespace
FROM dba_users
ORDER BY username;
```

Use `DBA_USERS` only with justified administrator access.

PDB-local administration can use appropriate container-scoped dictionary information.

Lock:

```sql
ALTER USER app_user
ACCOUNT LOCK;
```

Unlock:

```sql
ALTER USER app_user
ACCOUNT UNLOCK;
```

---

# Part 30 — Profiles

Profiles can control password/resource-related settings.

Concept:

```text
User
 ↓
Profile
 ↓
password/account policies
resource controls
```

Inspect:

```sql
SELECT *
FROM dba_profiles
WHERE profile = 'DEFAULT';
```

Do not weaken password settings to accommodate an outdated application without risk review.

---

# Part 31 — Quotas

A user may have table-creation privilege but still need storage quota.

```sql
ALTER USER app_owner
QUOTA 1G ON app_data;
```

Concept:

```text
CREATE TABLE privilege
      +
tablespace quota
      =
ability to allocate schema storage
```

Avoid granting unlimited tablespace casually.

---

# Part 32 — Create Permanent Tablespace

Example lab:

```sql
CREATE TABLESPACE app_data
DATAFILE '/u02/oradata/MANUCDB/MANUPDB/app_data01.dbf'
SIZE 1G
AUTOEXTEND ON
NEXT 100M
MAXSIZE 5G;
```

Path and syntax depend on storage architecture such as filesystem/ASM/OMF.

Use Oracle Managed Files where appropriate rather than hardcoding paths blindly.

---

# Part 33 — Datafile Management

Inspect:

```sql
SELECT
    tablespace_name,
    file_name,
    bytes / 1024 / 1024 AS mb,
    autoextensible
FROM dba_data_files
ORDER BY tablespace_name, file_name;
```

Potential actions include:

```text
add datafile
resize
enable/disable autoextend
move/rename using supported procedures
```

Never move an active datafile with ordinary `mv` and assume Oracle will discover it.

---

# Part 34 — Tablespace Usage

A useful starting query uses dictionary/dynamic views appropriate to your release.

Conceptual capacity report:

```text
Tablespace
   |
   +-- allocated
   +-- used
   +-- free
   +-- autoextend ceiling
```

Operational danger:

```text
95% allocated used
```

does not tell the whole story if autoextend/maxsize/storage capacity differ.

Capacity monitoring must include filesystem/ASM capacity too.

---

# Part 35 — Temporary Tablespace

Create concept:

```sql
CREATE TEMPORARY TABLESPACE app_temp
TEMPFILE ...
SIZE ...
AUTOEXTEND ON;
```

Temporary space is used for work such as:

```text
sort
hash
temporary result processing
```

If TEMP is exhausted:

```text
large query
   ↓
insufficient workarea memory
   ↓
temporary segment demand
   ↓
TEMP failure
```

Troubleshoot workload and capacity together.

---

# Part 36 — Undo Architecture

Undo records old change information.

Used for:

```text
ROLLBACK
read consistency
transaction recovery support
flashback-related features
```

Visualization:

```text
Row v1
  ↓ UPDATE
Row v2
  |
  +--> undo describes prior state
```

---

# Part 37 — Undo Tablespace

Inspect:

```sql
SHOW PARAMETER undo
```

Tablespace:

```sql
SELECT
    tablespace_name,
    status,
    contents
FROM dba_tablespaces
WHERE contents = 'UNDO';
```

Long-running queries plus heavy DML can create undo-retention pressure.

Symptoms may include snapshot-too-old style problems.

Advanced undo tuning is covered in DBA II.

---

# Part 38 — Redo Architecture

Every important database change generates redo.

```text
DML
 ↓
Redo Log Buffer
 ↓ LGWR
Online Redo Log
 ↓ log switch
Archived Redo
```

Redo is sequential recovery information, not a copy of data blocks.

---

# Part 39 — Online Redo Log Groups

Inspect:

```sql
SELECT
    group#,
    thread#,
    bytes / 1024 / 1024 AS mb,
    status,
    archived
FROM v$log
ORDER BY group#;
```

Members:

```sql
SELECT
    group#,
    member
FROM v$logfile
ORDER BY group#, member;
```

A group can have multiple members for multiplexing.

---

# Part 40 — Log Switch

Force in a lab:

```sql
ALTER SYSTEM SWITCH LOGFILE;
```

Concept:

```text
Current Group
   ↓ switch
Next Group becomes current
```

Too-frequent switching can indicate undersized logs or unusual workload.

Very infrequent switching may also affect recovery/archival operational goals.

Size from workload evidence.

---

# Part 41 — Checkpoints

Checkpoint concept:

```text
redo position advances
   ↓
checkpoint metadata
   ↓
dirty buffers eventually written
```

Checkpointing reduces instance-recovery work but creates I/O.

Do not manually force checkpoints as a generic "performance fix."

---

# Part 42 — Control Files

Inspect:

```sql
SELECT name
FROM v$controlfile;
```

Control files are critical.

Best-practice architecture commonly uses multiple copies on independent storage paths where appropriate.

Concept:

```text
Control File Copy A
Control File Copy B
```

Loss of every current control file is a recovery event covered in DBA II.

---

# Part 43 — ARCHIVELOG vs NOARCHIVELOG

## 43.1 NOARCHIVELOG

Completed redo is reused without archived copies.

Recovery options are limited.

## 43.2 ARCHIVELOG

Completed redo is archived.

```text
Online Redo
   ↓
Archive Destination
   ↓
Archived Redo Logs
```

Enables stronger recovery strategies and online backup capabilities.

## 43.3 Check Mode

```sql
SELECT
    log_mode
FROM v$database;
```

---

# Part 44 — Enable ARCHIVELOG in a Lab

Typical high-level sequence:

```text
clean shutdown
   ↓
startup mount
   ↓
ALTER DATABASE ARCHIVELOG
   ↓
open
```

Example:

```sql
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
ALTER DATABASE ARCHIVELOG;
ALTER DATABASE OPEN;
```

Then:

```sql
ARCHIVE LOG LIST;
```

Do this only in a disposable lab after archive-destination/FRA planning.

---

# Part 45 — Fast Recovery Area Concept

The Fast Recovery Area (FRA) is Oracle-managed storage for recovery-related files.

Possible contents:

```text
archived redo
RMAN backups
flashback logs
control-file autobackups
```

Inspect:

```sql
SHOW PARAMETER db_recovery_file_dest
SHOW PARAMETER db_recovery_file_dest_size
```

Do not place all database data and recovery copies on the same single failure domain if you expect media-failure protection.

---

# Part 46 — PDB Administration

List:

```sql
SHOW PDBS;
```

Open:

```sql
ALTER PLUGGABLE DATABASE MANUPDB OPEN;
```

Close:

```sql
ALTER PLUGGABLE DATABASE MANUPDB CLOSE IMMEDIATE;
```

## 46.1 Save State

```sql
ALTER PLUGGABLE DATABASE MANUPDB
SAVE STATE;
```

This allows Oracle to preserve desired PDB open state across CDB restart where applicable.

---

# Part 47 — Create a PDB

Example concept:

```sql
CREATE PLUGGABLE DATABASE MANUPDB
ADMIN USER pdbadmin
IDENTIFIED BY "LabOnly_StrongPassword2!";
```

Exact file-name clauses depend on OMF/storage environment.

Then:

```sql
ALTER PLUGGABLE DATABASE MANUPDB OPEN;
```

Use DBCA/OMF-aware methods where possible to avoid unsafe file-path assumptions.

---

# Part 48 — PDB Clone Concept

A PDB can be cloned under supported conditions.

```text
Source PDB
   ↓ clone
Test PDB
```

Use cases:

```text
development
testing
application lifecycle
migration
```

Cloning production data requires security/privacy controls.

---

# Part 49 — Data Dictionary Views

Core families:

```text
USER_*
ALL_*
DBA_*
CDB_*
```

In multitenant administration:

```text
CDB_*
```

can expose container-wide metadata when connected/privileged appropriately.

Examples:

```sql
SELECT username
FROM dba_users;
```

```sql
SELECT tablespace_name
FROM dba_tablespaces;
```

---

# Part 50 — Dynamic Performance Views

`V$` views expose live instance/database information.

Examples:

```text
V$INSTANCE
V$DATABASE
V$SESSION
V$PROCESS
V$SQL
V$LOG
V$DATAFILE
V$CONTROLFILE
V$SERVICES
```

Instance:

```sql
SELECT
    instance_name,
    status,
    database_status
FROM v$instance;
```

Database:

```sql
SELECT
    name,
    open_mode,
    log_mode
FROM v$database;
```

---

# Part 51 — Session Management

Inspect:

```sql
SELECT
    sid,
    serial#,
    username,
    status,
    machine,
    program,
    sql_id
FROM v$session
WHERE username IS NOT NULL;
```

A session is not the same as an OS process, though there can be process relationships.

---

# Part 52 — Blocking Sessions

Concept:

```text
Session A
 UPDATE row
 no commit
    |
  lock
    |
Session B waits
```

Useful views can expose blockers/waiters.

Before killing anything:

```text
Who owns session?
What transaction?
What application?
How long?
Can owner safely commit/rollback?
```

Killing sessions without business context can create larger incidents.

---

# Part 53 — Kill Session

Controlled lab:

```sql
ALTER SYSTEM
KILL SESSION 'sid,serial#'
IMMEDIATE;
```

This is a recovery/administrative action, not normal transaction management.

Use only after verifying exact SID and SERIAL#.

---

# Part 54 — Invalid Objects

Inspect:

```sql
SELECT
    owner,
    object_name,
    object_type,
    status
FROM dba_objects
WHERE status = 'INVALID'
ORDER BY owner, object_type, object_name;
```

Possible causes:

```text
dependency changed
failed deployment
missing privilege
compile error
```

Do not recompile blindly without checking the cause.

---

# Part 55 — Alert Log and ADR

Oracle diagnostic data is organized under the Automatic Diagnostic Repository.

Concept:

```text
Database / Listener
       ↓
ADR
       |
       +-- alert
       +-- trace
       +-- incident information
```

Find diagnostic destination:

```sql
SHOW PARAMETER diagnostic_dest
```

The alert log is one of the first places to inspect for:

```text
startup/shutdown
ORA errors
archive problems
file problems
background-process errors
```

---

# Part 56 — ADRCI

ADRCI is a command-line interface for ADR information.

Conceptual usage:

```bash
adrci
```

Then inspect homes and alert information using supported commands.

Do not delete diagnostic files randomly at OS level without understanding retention.

---

# Part 57 — Basic Performance Health

Start with system resources:

```text
CPU
memory
disk latency
storage capacity
network
```

Then database:

```text
sessions
SQL
waits
buffer activity
redo
TEMP
undo
```

Do not tune Oracle only by changing initialization parameters.

Advanced tuning belongs to DBA II.

---

# Part 58 — Basic Wait-State Thinking

A database session is broadly:

```text
on CPU
or
waiting
```

Wait examples:

```text
I/O
lock
network/client
commit/redo
```

Performance diagnosis asks:

```text
Where is time spent?
```

not:

```text
Which parameter can I increase?
```

---

# Part 59 — Unified Auditing Foundation

Oracle AI Database 26ai uses **unified auditing as the forward path**; traditional auditing is desupported for creating new traditional audit settings.

Concept:

```text
Audit Policy
    ↓
audited action/event
    ↓
Unified Audit Trail
```

Inspect unified audit policies/trail only with justified privileges.

Example concept:

```sql
CREATE AUDIT POLICY app_logon_policy
ACTIONS LOGON;
```

Then enable according to scope/security policy.

---

# Part 60 — Security Baseline

Minimum ideas:

```text
least privilege
separate application/admin identities
strong authentication
patching
private network exposure
TLS
auditing
encrypted backups/data where required
secure secrets
```

Do not let applications connect as `SYS`.

---

# Part 61 — SYS and SYSTEM

`SYS` owns core data dictionary objects and has special privileges.

`SYSTEM` is also highly privileged.

Operational rule:

```text
Normal application work
X
SYS/SYSTEM
```

Use named administrative accounts/roles and separation of duties where architecture supports it.

---

# Part 62 — Password File Concept

Administrative remote authentication can use an Oracle password file.

Inspect related configuration:

```sql
SHOW PARAMETER remote_login_passwordfile
```

Treat password-file storage/credentials as high-value secrets.

---

# Part 63 — Database Services and Application Isolation

Applications should connect via services.

Benefits:

```text
logical workload identity
routing
PDB targeting
HA integration
service management
```

Avoid hardcoding instance SID assumptions into modern application configuration.

---

# Part 64 — Basic Scheduler Administration

Oracle Scheduler jobs can automate database tasks.

Inspect:

```sql
SELECT
    owner,
    job_name,
    enabled,
    state
FROM dba_scheduler_jobs;
```

Use scheduling for database-owned tasks, but do not create overlapping schedules in Oracle, cron, and application code without clear ownership.

---

# Part 65 — Daily DBA Health Check

A daily report should answer:

```text
CDB open?
Required PDBs open?
Listener/services available?
Tablespaces healthy?
TEMP healthy?
Undo pressure?
Archive destination healthy?
Invalid objects?
Blocking sessions?
Critical alert-log events?
Backup jobs healthy?
Security/audit anomalies?
```

Automate evidence collection, not blind remediation.

---

# Part 66 — Troubleshooting Startup Failure

Workflow:

```text
STARTUP fails
   ↓
read exact ORA error
   ↓
which startup phase?
   ↓
NOMOUNT?
   parameter/SPFILE/memory

MOUNT?
   control file

OPEN?
   datafile/redo/recovery
```

This mapping is powerful.

---

# Part 67 — Troubleshooting Listener Failure

```text
Client ORA network error
   ↓
DNS/IP?
   ↓
TCP/1521?
   ↓
listener running?
   ↓
service registered?
   ↓
PDB open?
   ↓
connect string correct?
```

Use both network and Oracle evidence.

---

# Part 68 — Troubleshooting Tablespace Full

Do not immediately enable unlimited autoextend.

Ask:

```text
real growth?
runaway process?
retention problem?
temporary operation?
datafile max size?
filesystem/ASM free space?
```

Then choose:

```text
add capacity
resize
fix workload
purge according to policy
```

---

# Part 69 — Troubleshooting User Cannot Log In

Check:

```text
service/PDB?
account exists in correct container?
account locked?
password expired?
CREATE SESSION?
profile?
network/authentication?
```

Inspect account status.

Do not reset a password until you have identified the failure mode.

---

# Part 70 — Troubleshooting Invalid Objects

```text
invalid package
   ↓
USER_ERRORS / DBA_ERRORS
   ↓
dependency
   ↓
privilege/object change
   ↓
recompile after fix
```

Deployment pipelines should verify invalid-object counts.

---

# Enhanced Deep-Study Layer — Oracle Database Administration I Engineering

The original course is preserved below. This layer expands the DBA-I foundation into deeper instance, memory, process, multitenant, storage, Oracle Net, security, diagnostics, capacity, and operational troubleshooting material.

```text
Application
   ↓ service / listener
Oracle session
   ↓
Instance: SGA + processes
   ↓
CDB/PDB container
   ↓
tablespace / segment / extent / block
   ↓
datafiles + control files + redo
   ↓
archive/FRA + diagnostics
```

## Enhanced Deep Dive 1 — Oracle Instance Startup as a Dependency Chain

Startup is best understood as progressively adding dependencies. NOMOUNT requires parameter state and OS resources; MOUNT adds control files; OPEN adds datafiles and redo. This turns vague startup failures into a precise diagnostic tree.

```text
SHUTDOWN
  ↓ parameters + memory + processes
NOMOUNT
  ↓ control files
MOUNT
  ↓ datafiles + redo + recovery state
OPEN
```

```sql
SELECT
    status,
    database_status
FROM v$instance;

SELECT
    open_mode
FROM v$database;
```

**Expected behavior:** The views reveal which layers are currently available.

**Why it works:** Each startup phase proves that the previous dependency layer succeeded.

**Operational caution:** Do not jump directly to restoring files until you know which startup phase actually failed.

## Enhanced Deep Dive 2 — Restricted Session Mode

A database can be opened or placed into restricted access so only appropriately privileged sessions can connect. This is useful for controlled maintenance and some upgrade/deployment activities.

```text
normal OPEN
  ↓ enable restriction
maintenance users only
  ↓ disable restriction
normal service
```

```sql
ALTER SYSTEM ENABLE RESTRICTED SESSION;

SELECT logins
FROM v$instance;

ALTER SYSTEM DISABLE RESTRICTED SESSION;
```

**Expected behavior:** The instance login mode changes while the database can remain open.

**Why it works:** Restriction limits new ordinary sessions without requiring a full shutdown.

**Operational caution:** Existing sessions and service behavior must be considered; restriction is not a substitute for a maintenance communication plan.

## Enhanced Deep Dive 3 — Read-only Database or PDB Open Modes

Read-only opening is useful for selected reporting, clone, or recovery scenarios. It changes what DML/DDL operations are allowed while preserving query access.

```text
PDB
  ├→ READ WRITE
  └→ READ ONLY
```

```sql
SELECT
    name,
    open_mode
FROM v$pdbs;

-- Lab example:
ALTER PLUGGABLE DATABASE TESTPDB CLOSE IMMEDIATE;
ALTER PLUGGABLE DATABASE TESTPDB OPEN READ ONLY;
```

**Expected behavior:** The PDB reports READ ONLY and rejects normal application DML.

**Why it works:** Open mode is part of service state, not merely whether the PDB is 'up'.

**Operational caution:** Applications may still connect successfully but fail writes, so health checks should verify required open mode.

## Enhanced Deep Dive 4 — System Change Number (SCN) Mental Model

Oracle uses SCNs as logical database change-order markers. They underpin consistency, recovery, checkpoints, and replication-like technologies. You do not manually manage normal SCN progression, but understanding it makes recovery concepts much clearer.

```text
changes
SCN 100
SCN 101
SCN 102
   ↓
consistent point / recovery position
```

```sql
SELECT
    current_scn
FROM v$database;
```

**Expected behavior:** The current database SCN advances as database activity occurs.

**Why it works:** SCNs give Oracle a database-wide ordering framework for change and consistency.

**Operational caution:** Do not interpret SCN as a simple wall-clock timestamp; use supported conversion/recovery tooling when mapping time and SCN.

## Enhanced Deep Dive 5 — Checkpoint Position vs Commit

A transaction commit is primarily protected by redo durability; it does not wait for every changed data block to be written to its datafile. Checkpoints advance recovery metadata and coordinate dirty-buffer writing.

```text
UPDATE
 ├→ dirty buffer
 └→ redo
      ↓ LGWR
COMMIT acknowledged
      ↓ later
DBWn writes block
```

```sql
SELECT
    checkpoint_change#
FROM v$datafile_header
ORDER BY file#;
```

**Expected behavior:** File headers expose checkpoint-related positions.

**Why it works:** Redo allows committed changes to survive even when dirty data blocks are still only in memory at crash time.

**Operational caution:** Do not force frequent checkpoints as a generic performance improvement; they can increase write I/O.

## Enhanced Deep Dive 6 — Instance Recovery: Roll Forward then Roll Back

After an abnormal instance termination, Oracle can use online redo to roll datafiles forward, then use undo to remove uncommitted changes. This is different from restoring lost media.

```text
crash
 ↓
redo roll forward
 ↓
committed + uncommitted changes reconstructed
 ↓
undo uncommitted work
 ↓
consistent OPEN database
```

```sql
-- Lab:
SHUTDOWN ABORT;
STARTUP;

SELECT
    status
FROM v$instance;
```

**Expected behavior:** Startup performs required instance recovery automatically when the files are intact.

**Why it works:** Redo protects change history while undo preserves transaction semantics.

**Operational caution:** Do not practice ABORT on important systems; use a disposable lab.

## Enhanced Deep Dive 7 — SGA Granules and Component Sizing Awareness

Oracle allocates major SGA components in internal allocation units and can resize some components under automatic memory management. The DBA should think in terms of shared workload pressure rather than treating each cache as an isolated fixed bucket.

```text
SGA target
  ↓
buffer cache
shared pool
large pool
other components
  ↔ dynamic resizing where supported
```

```sql
SELECT
    component,
    current_size,
    min_size,
    max_size
FROM v$sga_dynamic_components
ORDER BY component;
```

**Expected behavior:** Dynamic component sizes reveal how memory is currently allocated.

**Why it works:** Automatic sizing can move memory to where workload needs it, within configured limits.

**Operational caution:** Do not conclude that a component is undersized from one snapshot; use workload evidence over time.

## Enhanced Deep Dive 8 — Buffer Cache Working Set

The buffer cache is valuable when active data/index blocks are reused. A large cache cannot rescue a query that unnecessarily scans vast data, and a smaller cache can still perform well when the working set is small.

```text
query working set
   ↓
buffer cache
   ├→ repeated blocks: hits
   └→ new blocks: physical reads
```

```sql
SELECT
    name,
    value
FROM v$sysstat
WHERE name IN (
    'physical reads',
    'session logical reads'
);
```

**Expected behavior:** The statistics expose physical I/O and logical buffer access at a high level.

**Why it works:** Cache effectiveness depends on workload locality, not only allocated bytes.

**Operational caution:** Do not use a simple cache-hit ratio as the only tuning decision; SQL access patterns matter more.

## Enhanced Deep Dive 9 — Shared Pool and Library Cache

The shared pool contains reusable SQL/PLSQL and metadata structures. High hard-parse rates, invalidations, or many unique literal SQL statements can create CPU and shared-pool pressure.

```text
SQL text
  ↓ parse
library cache cursor
  ↓ reuse by sessions
```

```sql
SELECT
    namespace,
    pins,
    reloads,
    invalidations
FROM v$librarycache
ORDER BY namespace;
```

**Expected behavior:** The view shows aggregate library-cache activity.

**Why it works:** Reusable cursors reduce repeated parsing and metadata work.

**Operational caution:** Do not flush the shared pool as a routine tuning action; it removes useful cached state and destroys evidence.

## Enhanced Deep Dive 10 — Large Pool

The large pool provides memory for selected large allocations such as shared-server, parallel-execution, RMAN, and other internal workloads depending on configuration. Keeping these allocations separate can reduce fragmentation pressure in the shared pool.

```text
SGA
 ├→ shared pool
 ├→ buffer cache
 └→ large pool
      ↓ selected large allocations
```

```sql
SHOW PARAMETER large_pool_size
```

**Expected behavior:** The parameter shows whether an explicit large-pool size is configured.

**Why it works:** Oracle can separate suitable large allocations from normal library-cache activity.

**Operational caution:** Do not size the large pool from a copied formula without identifying workloads that actually use it.

## Enhanced Deep Dive 11 — PGA Work Areas

Sorts, hashes, bitmap operations, and session processing use PGA work areas. If work cannot fit in memory, operations can spill to TEMP, increasing I/O.

```text
SQL operation
  ↓ work area
PGA memory
  ├→ fits → memory
  └→ spills → TEMP
```

```sql
SELECT
    name,
    value
FROM v$pgastat
WHERE name IN (
    'total PGA allocated',
    'total PGA inuse',
    'over allocation count'
);
```

**Expected behavior:** PGA statistics show current aggregate memory behavior.

**Why it works:** PGA and TEMP are connected parts of execution memory management.

**Operational caution:** A TEMP spike may be caused by SQL plan/data volume, not only by insufficient PGA configuration.

## Enhanced Deep Dive 12 — Dedicated vs Shared Server Operational Impact

Dedicated server gives a client session a dedicated server process. Shared server multiplexes many sessions over shared server processes through dispatchers. This changes process count and session memory placement.

```text
Dedicated:
client → server process

Shared:
clients → dispatcher → shared servers
```

```sql
SHOW PARAMETER shared_servers
SHOW PARAMETER dispatchers
```

**Expected behavior:** The parameters indicate whether shared-server infrastructure is configured.

**Why it works:** Connection architecture should match workload characteristics.

**Operational caution:** Do not enable shared server merely because the server has many sessions; test application compatibility and workload behavior.

## Enhanced Deep Dive 13 — Foreground Session, Server Process, and OS Process Mapping

A database session, Oracle server process, and operating-system process are related but not identical concepts. Mapping them is important during CPU or hung-process troubleshooting.

```text
V$SESSION
  ↓ PADDR
V$PROCESS
  ↓ SPID
OS process
```

```sql
SELECT
    s.sid,
    s.serial#,
    s.username,
    p.spid
FROM v$session s
JOIN v$process p
  ON p.addr = s.paddr
WHERE s.username IS NOT NULL;
```

**Expected behavior:** The query maps Oracle sessions to server-process OS identifiers.

**Why it works:** Oracle keeps separate session and process structures.

**Operational caution:** Never kill an OS PID because it 'looks busy' without proving which database session/process it represents and what recovery impact will occur.

## Enhanced Deep Dive 14 — Background Process Roles as a Data Flow

Instead of memorizing names, trace data movement: user changes blocks, redo is generated, LGWR persists redo, DBWn writes dirty blocks, CKPT advances checkpoint metadata, ARCn preserves completed redo when archiving is enabled.

```text
DML
 ├→ buffer cache → DBWn → datafile
 └→ redo buffer → LGWR → online redo → ARCn → archive
```

```sql
SELECT
    program
FROM v$process
WHERE program LIKE '%(LGWR)%'
   OR program LIKE '%(DBW%'
   OR program LIKE '%(ARC%';
```

**Expected behavior:** Relevant background processes can be identified where present.

**Why it works:** The process model explains commit, checkpoint, recovery, and archiving behavior.

**Operational caution:** Process names evolve across releases; learn responsibilities and verify current architecture.

## Enhanced Deep Dive 15 — Control File Contents and Why Multiplexing Matters

The control file contains structural metadata required to mount the database. Multiple current copies reduce the chance that one filesystem/device failure removes the only copy.

```text
control_files parameter
  ├→ copy A
  └→ copy B
      ↓
MOUNT depends on readable control metadata
```

```sql
SHOW PARAMETER control_files

SELECT name
FROM v$controlfile;
```

**Expected behavior:** The parameter/view lists current control-file copies.

**Why it works:** Oracle writes required control metadata to configured copies.

**Operational caution:** Copies on the same underlying disk failure domain provide much less protection than independent placement.

## Enhanced Deep Dive 16 — Online Redo Log Group vs Member

A redo group is one logical redo unit; a group can have multiple members containing the same redo stream for multiplexing. Oracle switches between groups, not between individual members.

```text
Group 1
 ├→ member A
 └→ member B
       ↓ switch
Group 2
 ├→ member A
 └→ member B
```

```sql
SELECT
    l.group#,
    l.status,
    f.member
FROM v$log l
JOIN v$logfile f
  ON f.group# = l.group#
ORDER BY l.group#, f.member;
```

**Expected behavior:** The query distinguishes logical group status from physical members.

**Why it works:** Multiplexed members protect against losing one redo member.

**Operational caution:** Do not place every member on the same fragile storage path and call it redundant.

## Enhanced Deep Dive 17 — Redo Log Sizing by Workload

Very small redo logs can cause frequent switches/checkpoints/archiving overhead; excessively large logs can influence recovery and archive-management behavior. Size from measured redo generation and operational goals.

```text
redo generation rate
   ↓
target switch interval / recovery design
   ↓
redo size
```

```sql
SELECT
    group#,
    bytes/1024/1024 AS mb,
    status
FROM v$log
ORDER BY group#;
```

**Expected behavior:** The view shows current log sizes and statuses.

**Why it works:** Redo sizing is a throughput and recovery design decision.

**Operational caution:** Do not resize based solely on a rule copied from another database; measure switch frequency and redo volume.

## Enhanced Deep Dive 18 — Redo Switch History

Log history allows a DBA to see how often switches occur and correlate them with workload spikes, batch jobs, or archiving pressure.

```text
workload
  ↓ redo generation
  ↓ log switches
  ↓ history timeline
```

```sql
SELECT
    first_time,
    thread#,
    sequence#
FROM v$log_history
ORDER BY first_time DESC
FETCH FIRST 30 ROWS ONLY;
```

**Expected behavior:** Recent switch times can be reviewed.

**Why it works:** Switch history is objective evidence for redo sizing and workload analysis.

**Operational caution:** One abnormal batch period should not automatically drive permanent sizing without considering normal workload.

## Enhanced Deep Dive 19 — Archived Redo Lifecycle

In ARCHIVELOG mode, completed redo must be archived, backed up according to policy, retained long enough for recovery objectives, and eventually removed using supported recovery-management procedures.

```text
online redo
  ↓ switch
archive
  ↓ backup
retention window
  ↓ approved deletion
```

```sql
ARCHIVE LOG LIST;

SELECT
    sequence#,
    first_time,
    next_time,
    archived,
    status
FROM v$archived_log
ORDER BY sequence# DESC
FETCH FIRST 20 ROWS ONLY;
```

**Expected behavior:** The database exposes archived-redo status/history.

**Why it works:** Recovery depends on a complete change chain after a backup.

**Operational caution:** Manual OS deletion can create repository/recovery gaps and is not normal archive management.

## Enhanced Deep Dive 20 — Fast Recovery Area Is Capacity-managed Recovery Storage

The FRA can hold multiple recovery file types. It is not 'free backup disk'; Oracle tracks usage against a configured quota, and pressure can eventually affect archiving and availability.

```text
FRA quota
 ├→ archived redo
 ├→ backups
 ├→ flashback logs
 └→ control/autobackup
      ↓
space pressure
```

```sql
SELECT
    name,
    space_limit,
    space_used,
    space_reclaimable
FROM v$recovery_file_dest;
```

**Expected behavior:** The view shows FRA capacity and reclaimable space.

**Why it works:** Centralized recovery storage allows Oracle-aware retention and space management.

**Operational caution:** Do not respond to FRA pressure with `rm`; identify retention, backup completion, restore points, flashback logs, and capacity first.

## Enhanced Deep Dive 21 — Datafile Header and Control-file Agreement

At OPEN, Oracle validates that control-file metadata and datafile headers are consistent enough for the requested open mode. Mismatched checkpoints or missing files can trigger recovery errors.

```text
control file expected state
        ↕
datafile headers
        ↓
OPEN decision
```

```sql
SELECT
    file#,
    name,
    checkpoint_change#
FROM v$datafile_header
ORDER BY file#;
```

**Expected behavior:** Headers expose each datafile's checkpoint state.

**Why it works:** Oracle must know every required datafile belongs to a consistent database timeline.

**Operational caution:** Do not edit or replace database files at OS level while Oracle is unaware of the change.

## Enhanced Deep Dive 22 — Smallfile vs Bigfile Tablespaces

Smallfile tablespaces use multiple normal datafiles; bigfile tablespaces are designed around one very large datafile. Bigfile can simplify file-count management but changes capacity/backup/storage operations.

```text
Smallfile:
TS → df1 + df2 + df3

Bigfile:
TS → one very large df
```

```sql
SELECT
    tablespace_name,
    bigfile
FROM dba_tablespaces
ORDER BY tablespace_name;
```

**Expected behavior:** The dictionary identifies tablespace type.

**Why it works:** Oracle supports different physical file-management strategies behind logical tablespaces.

**Operational caution:** Choose based on storage architecture, operational tooling, and scale rather than assuming bigfile is always newer/better.

## Enhanced Deep Dive 23 — Locally Managed Tablespaces

Modern Oracle tablespaces normally use locally managed extent allocation, where space-management metadata is maintained in the tablespace rather than old dictionary-managed mechanisms.

```text
tablespace
  ↓ local bitmap metadata
  ↓ extents allocated to segments
```

```sql
SELECT
    tablespace_name,
    extent_management,
    allocation_type
FROM dba_tablespaces
ORDER BY tablespace_name;
```

**Expected behavior:** The output shows local extent management and allocation type.

**Why it works:** Local management improves scalability and simplifies extent administration.

**Operational caution:** Do not follow legacy scripts that manually tune old extent parameters without confirming current tablespace type.

## Enhanced Deep Dive 24 — Automatic Segment Space Management

ASSM uses bitmap-based free-space tracking inside segments and is the normal modern foundation for many tablespaces. It reduces manual freelist-style management.

```text
segment blocks
  ↓ bitmap free-space classes
  ↓ concurrent block allocation
```

```sql
SELECT
    tablespace_name,
    segment_space_management
FROM dba_tablespaces
ORDER BY tablespace_name;
```

**Expected behavior:** Tablespaces report AUTO or MANUAL segment-space management.

**Why it works:** ASSM lets Oracle manage free block space more automatically.

**Operational caution:** Do not apply obsolete freelist tuning advice to ASSM-managed tablespaces.

## Enhanced Deep Dive 25 — Oracle Managed Files (OMF)

OMF lets Oracle generate and manage physical filenames under configured destinations. This reduces hardcoded path mistakes, especially with PDB creation and managed storage.

```text
DB_CREATE_FILE_DEST
   ↓
CREATE TABLESPACE/PDB
   ↓
Oracle-generated filename
```

```sql
SHOW PARAMETER db_create_file_dest
```

**Expected behavior:** If configured, Oracle can create files without manually supplied full paths for supported operations.

**Why it works:** File naming becomes a database-managed responsibility.

**Operational caution:** OMF does not eliminate storage design; capacity, redundancy, backup, and failure domains still matter.

## Enhanced Deep Dive 26 — ASM Foundation Awareness

Automatic Storage Management is Oracle's database-aware storage layer used in many enterprise systems. ASM groups disks into disk groups and provides striping/mirroring behavior according to configuration.

```text
Oracle DB
   ↓
ASM disk group
   ↓
disk 1 / disk 2 / disk 3 ...
```

```sql
-- If ASM is present, database file names can look like:
-- +DATA/MANUCDB/...
```

**Expected behavior:** ASM-managed files are addressed through disk-group style names rather than normal filesystem paths.

**Why it works:** ASM integrates database file management with storage allocation/redundancy.

**Operational caution:** Do not treat ASM files like ordinary filesystem files; administration uses Oracle/ASM tooling.

## Enhanced Deep Dive 27 — Tablespace Read-only State

A permanent tablespace can be made read only for archival or controlled migration scenarios. This can reduce accidental writes and influence backup strategy.

```text
READ WRITE
  ↓
READ ONLY
  ↓
queries allowed
writes blocked
```

```sql
ALTER TABLESPACE archive_data READ ONLY;

SELECT
    tablespace_name,
    status
FROM dba_tablespaces
WHERE tablespace_name = 'ARCHIVE_DATA';
```

**Expected behavior:** The tablespace reports READ ONLY.

**Why it works:** The state is enforced at the storage-container level.

**Operational caution:** Application dependencies must be checked before making a tablespace read only.

## Enhanced Deep Dive 28 — Tablespace Offline State

Taking a tablespace offline can isolate selected datafiles for maintenance/recovery while the rest of the database remains available, subject to object dependencies and tablespace type.

```text
database OPEN
  ├→ APP_DATA online
  └→ ARCHIVE_DATA offline
```

```sql
ALTER TABLESPACE app_data OFFLINE;

SELECT
    tablespace_name,
    status
FROM dba_tablespaces
WHERE tablespace_name='APP_DATA';
```

**Expected behavior:** Objects in the offline tablespace become unavailable while other areas can remain open.

**Why it works:** Oracle supports scoped storage administration.

**Operational caution:** Do this only in a lab or approved maintenance window because dependent applications can fail immediately.

## Enhanced Deep Dive 29 — Autoextend Is Not Infinite Storage

A datafile can autoextend only until MAXSIZE or underlying storage constraints are reached. Capacity monitoring must include allocated bytes, max potential growth, and filesystem/ASM free space.

```text
used
  ↓
allocated size
  ↓ autoextend
maxsize
  ↓
physical storage ceiling
```

```sql
SELECT
    file_name,
    bytes/1024/1024 AS current_mb,
    autoextensible,
    maxbytes/1024/1024 AS max_mb
FROM dba_data_files
ORDER BY file_name;
```

**Expected behavior:** The report separates current allocation from maximum configured growth.

**Why it works:** Autoextend delays manual file growth but does not create new storage.

**Operational caution:** Unlimited-looking MAXSIZE on a filesystem with 2 GB free is not operational capacity.

## Enhanced Deep Dive 30 — Temporary Tablespace Groups Awareness

Oracle can group multiple temporary tablespaces so sessions distribute temporary work across them. This is useful in larger environments but should be justified by workload/storage architecture.

```text
TEMP group
 ├→ temp01
 └→ temp02
      ↓
session temp work
```

```sql
SELECT
    group_name,
    tablespace_name
FROM dba_tablespace_groups
ORDER BY group_name, tablespace_name;
```

**Expected behavior:** Configured temporary groups and members are visible.

**Why it works:** Grouping can spread temporary I/O/space across managed temp areas.

**Operational caution:** Do not create multiple TEMP files/tablespaces without understanding the underlying storage bottleneck.

## Enhanced Deep Dive 31 — Undo Retention

Undo retention is a target for retaining old versions long enough to support read consistency and flashback-related needs. Actual ability to retain depends on undo space and workload unless stronger retention guarantees are configured.

```text
DML creates undo
   ↓
active transaction needs it
   ↓
consistent queries may need older versions
   ↓
retention / reuse
```

```sql
SHOW PARAMETER undo_retention

SELECT
    begin_time,
    tuned_undoretention
FROM v$undostat
ORDER BY begin_time DESC
FETCH FIRST 12 ROWS ONLY;
```

**Expected behavior:** The database exposes configured and workload-tuned retention information.

**Why it works:** Undo retention must match long-query and flashback requirements.

**Operational caution:** Increasing retention without enough undo space can simply shift pressure elsewhere.

## Enhanced Deep Dive 32 — Undo Retention Guarantee Awareness

An undo tablespace can be configured to guarantee retention in specialized cases, prioritizing preservation of unexpired undo over new DML space. This can protect long queries but can cause write failures if space is exhausted.

```text
undo space finite
  ↓
RETENTION GUARANTEE
  ↓
preserve old undo
  ↓
new DML may fail if no space
```

```sql
SELECT
    tablespace_name,
    retention
FROM dba_tablespaces
WHERE contents='UNDO';
```

**Expected behavior:** The RETENTION column shows guarantee policy.

**Why it works:** Guarantee changes the trade-off between query history and DML availability.

**Operational caution:** Use only when the business requirement explicitly prefers retained history over continued writes under space pressure.

## Enhanced Deep Dive 33 — ORA-01555 Mental Model

Snapshot-too-old conditions happen when a query needs an older block version but the required undo has already been reused. The root cause is a relationship among query duration, DML rate, undo capacity, and retention.

```text
long query at SCN X
  ↓ concurrent DML
undo generated/reused
  ↓ old version needed
  X no longer available
```

```sql
SELECT
    begin_time,
    ssolderrcnt,
    maxquerylen,
    tuned_undoretention
FROM v$undostat
ORDER BY begin_time DESC
FETCH FIRST 24 ROWS ONLY;
```

**Expected behavior:** The statistics help correlate long queries with snapshot-too-old counts and undo behavior.

**Why it works:** Read consistency depends on historical versions being available.

**Operational caution:** Do not 'fix' by committing more frequently inside the long query; that usually changes semantics and may worsen other behavior.

## Enhanced Deep Dive 34 — PDB Data Dictionary Container Awareness

Multitenant dictionary queries often expose `CON_ID`. A row may belong to root or a PDB, so container context must be understood before interpreting users, services, files, or parameters.

```text
CDB root query
   ↓
CDB_* / V$ views
   ↓
CON_ID
   ↓
map to container
```

```sql
SELECT
    con_id,
    name,
    open_mode
FROM v$containers
ORDER BY con_id;
```

**Expected behavior:** Every container has an identifier and state.

**Why it works:** Container ID lets shared instance views distinguish multitenant scope.

**Operational caution:** Never aggregate capacity/security findings across containers without knowing which rows are root vs application PDBs.

## Enhanced Deep Dive 35 — Common and Local Object Scope

Common users/roles can exist across containers, while local identities belong to a PDB. Administrative scripts must decide whether an action is container-local or common.

```text
CDB$ROOT
  ├→ common identity
  ├→ PDB1 local identity
  └→ PDB2 local identity
```

```sql
SELECT
    username,
    common,
    con_id
FROM cdb_users
ORDER BY username, con_id;
```

**Expected behavior:** The `COMMON` and `CON_ID` columns reveal scope.

**Why it works:** Multitenant architecture adds an administrative scope dimension to identity.

**Operational caution:** Avoid creating common application users just to avoid switching containers.

## Enhanced Deep Dive 36 — Common Roles vs Local Roles

Roles can also have common or local scope. Enterprise administration should keep application privileges local where possible and reserve common roles for cross-container administrative designs.

```text
common role
  ↓ multiple containers

local role
  ↓ one PDB
```

```sql
SELECT
    role,
    common
FROM dba_roles
ORDER BY role;
```

**Expected behavior:** Role scope is visible in dictionary metadata.

**Why it works:** Least privilege includes minimizing container scope.

**Operational caution:** A common role with powerful privileges can increase blast radius across PDBs.

## Enhanced Deep Dive 37 — PDB Save State After CDB Restart

Opening a PDB now does not necessarily mean it will automatically reopen after a CDB restart. Saving PDB state records the desired startup open mode.

```text
CDB restart
  ↓
PDB saved state?
  ├→ yes: restore desired open state
  └→ no: may remain mounted
```

```sql
ALTER PLUGGABLE DATABASE MANUPDB OPEN;
ALTER PLUGGABLE DATABASE MANUPDB SAVE STATE;

SELECT
    con_name,
    state
FROM dba_pdb_saved_states;
```

**Expected behavior:** The saved-state view records desired behavior.

**Why it works:** PDB lifecycle is separate from instance lifecycle.

**Operational caution:** A monitoring check should verify PDB open mode after every CDB restart, not only instance status.

## Enhanced Deep Dive 38 — PDB Unplug and Plug Concepts

A PDB can be unplugged into metadata and later plugged into another compatible CDB under supported conditions. This is a major migration/lifecycle capability.

```text
CDB A
  ↓ unplug metadata/files
PDB
  ↓ compatibility checks
CDB B plug
```

```sql
-- High-level lab concept only:
-- ALTER PLUGGABLE DATABASE ... UNPLUG INTO '...xml';
-- CREATE PLUGGABLE DATABASE ... USING '...xml';
```

**Expected behavior:** The operation moves logical database ownership without rebuilding every schema object manually.

**Why it works:** PDB portability is built into multitenant architecture.

**Operational caution:** Check version, options, character set, files, encryption keys, and compatibility before real migrations.

## Enhanced Deep Dive 39 — PDB Clone as a Data Governance Event

Cloning a production PDB into test is operationally convenient but can copy personal, financial, or confidential data. Database lifecycle operations are therefore also security/privacy operations.

```text
production PDB
   ↓ clone
test PDB
   ↓
same sensitive data unless masked
```

```sql
SELECT
    name,
    open_mode
FROM v$pdbs;
```

**Expected behavior:** The technical clone can be simple while the data-governance impact is large.

**Why it works:** Database cloning duplicates data, not merely schema definitions.

**Operational caution:** Mask/sanitize and restrict access to nonproduction copies according to policy.

## Enhanced Deep Dive 40 — PDB Services

A PDB can expose one or more services. Applications should connect to business services rather than relying on container names or instance SIDs.

```text
Application
   ↓ service
listener
   ↓
specific PDB / workload
```

```sql
SELECT
    name,
    pdb,
    con_id
FROM v$services
ORDER BY name;
```

**Expected behavior:** Services can be mapped to their PDB/container context.

**Why it works:** Services are the abstraction used for connectivity, workload identity, and later HA integration.

**Operational caution:** Do not hardcode a physical host or SID when a service should represent the application workload.

## Enhanced Deep Dive 41 — Listener Dynamic Registration

Database services normally register dynamically with the listener. If the listener is up but the required service is missing, troubleshoot database service registration rather than recreating listener files immediately.

```text
database instance
   ↓ service registration
listener
   ↓ client discovery
```

```bash
lsnrctl status

-- Database:
ALTER SYSTEM REGISTER;
```

**Expected behavior:** A manual registration request can be used after correcting configuration in a lab.

**Why it works:** Registration is initiated by database networking processes using configured listener information.

**Operational caution:** `ALTER SYSTEM REGISTER` is not a permanent fix for wrong LOCAL_LISTENER, DNS, service, or network settings.

## Enhanced Deep Dive 42 — LOCAL_LISTENER Awareness

`LOCAL_LISTENER` can tell an instance where its local listener is when the default assumptions are insufficient. This becomes important with non-default ports or listener addresses.

```text
instance
  ↓ LOCAL_LISTENER address/alias
listener
  ↓ service registration
```

```sql
SHOW PARAMETER local_listener
```

**Expected behavior:** The parameter displays the configured registration target.

**Why it works:** Dynamic registration requires the instance to know where to register.

**Operational caution:** Do not set a random TNS alias from another server; verify name resolution and listener address.

## Enhanced Deep Dive 43 — sqlnet.ora as Client/Server Network Policy

Oracle Net behavior can be influenced by `sqlnet.ora` settings such as naming methods, encryption/TLS-related configuration, authentication behavior, and timeouts depending on environment.

```text
client / server Oracle Net
   ↓
sqlnet policy
   ↓
connect behavior
```

```sql
# Conceptual file settings vary by release/environment.
# Always inspect the effective ORACLE_HOME/network/admin location.
```

**Expected behavior:** Network policy is separate from `listener.ora` and `tnsnames.ora` address definitions.

**Why it works:** Oracle Net uses multiple configuration layers.

**Operational caution:** Do not copy security settings from old examples; verify current supported parameters and cipher/certificate requirements.

## Enhanced Deep Dive 44 — TNS_ADMIN

`TNS_ADMIN` can redirect Oracle Net clients/tools to a specific network-configuration directory. This explains why editing one `tnsnames.ora` sometimes appears to have no effect.

```text
client
  ↓ TNS_ADMIN?
  ├→ custom network/admin
  └→ ORACLE_HOME/network/admin
```

```bash
echo $TNS_ADMIN
echo $ORACLE_HOME
```

**Expected behavior:** Environment variables reveal where clients may load network files.

**Why it works:** Multiple Oracle homes/config directories can coexist on one host.

**Operational caution:** Always prove which client binary and network directory are in use before editing configuration.

## Enhanced Deep Dive 45 — Listener vs Database Authentication

The listener accepts/routes the initial connection. Database authentication occurs after the connection reaches the database service. A listener being reachable does not mean the username/password is valid.

```text
TCP connect
  ↓ listener
service handoff
  ↓ database session authentication
  ↓ privilege checks
```

```bash
lsnrctl status

SELECT
    username,
    account_status
FROM dba_users
WHERE username='APP_USER';
```

**Expected behavior:** Network and identity state are checked independently.

**Why it works:** Layered troubleshooting avoids resetting passwords for a network problem.

**Operational caution:** Do not expose listener control or database credentials while troubleshooting connectivity.

## Enhanced Deep Dive 46 — SYSDBA Is an Administrative Authentication Mode

`SYSDBA` is not just a normal role granted for application convenience. It provides extraordinary administrative capability and changes how the session is authenticated/identified.

```text
administrator
  ↓ SYSDBA auth
  ↓ powerful database control
```

```sql
SELECT
    SYS_CONTEXT('USERENV','SESSION_USER') AS session_user,
    SYS_CONTEXT('USERENV','ISDBA') AS is_dba
FROM dual;
```

**Expected behavior:** An administrative session can report DBA status.

**Why it works:** Oracle separates powerful administration from ordinary object privilege models.

**Operational caution:** Do not give SYSDBA to application or routine support accounts.

## Enhanced Deep Dive 47 — Password File Administrative Authentication

Remote administrative connections can rely on an Oracle password file according to configuration. The password file is therefore high-value security material and part of recovery/HA planning.

```text
remote admin
  ↓ password file auth
listener/service
  ↓ SYSDBA-like session
```

```sql
SHOW PARAMETER remote_login_passwordfile
```

**Expected behavior:** The parameter shows the configured password-file mode.

**Why it works:** Administrative authentication may need to work before ordinary database objects/users are available.

**Operational caution:** Protect password file permissions, backups, synchronization, and credentials.

## Enhanced Deep Dive 48 — Roles vs Direct Privileges for Stored Code

Role-based privileges are ideal for human/session administration, but stored definer-rights PL/SQL often requires direct privileges on referenced objects. DBA privilege design must therefore consider both runtime users and schema owners.

```text
APPUSER → role → EXECUTE package
PACKAGE OWNER → direct grants → tables
```

```sql
SELECT
    grantee,
    owner,
    table_name,
    privilege
FROM dba_tab_privs
WHERE grantee='APP_OWNER';
```

**Expected behavior:** The DBA can verify exactly which direct object privileges the owner holds.

**Why it works:** Stored-code security and ordinary session role security have different dependency semantics.

**Operational caution:** Do not respond to compile errors by granting broad DBA roles to schema owners.

## Enhanced Deep Dive 49 — Default Roles

A user can have multiple granted roles but only selected roles enabled by default. This explains why a privilege appears granted yet a session does not have it active.

```text
user
  ↓ granted roles
default subset
  ↓ active session roles
```

```sql
SELECT
    granted_role,
    default_role
FROM dba_role_privs
WHERE grantee='APP_USER';
```

**Expected behavior:** The dictionary distinguishes granted from default-enabled roles.

**Why it works:** Role activation is session state.

**Operational caution:** Stored code and security-sensitive operations should not assume every granted role is enabled.

## Enhanced Deep Dive 50 — Profiles: Password Policy vs Resource Policy

Profiles can contain password/account controls and resource limits. Resource-limit enforcement also depends on database configuration and policy, so do not assume every profile field has active effect merely because it is populated.

```text
user
 ↓ profile
 ├→ password parameters
 └→ resource parameters
```

```sql
SELECT
    resource_name,
    resource_type,
    limit
FROM dba_profiles
WHERE profile='DEFAULT'
ORDER BY resource_type, resource_name;
```

**Expected behavior:** Profile contents can be reviewed by control category.

**Why it works:** Profiles centralize common account policy.

**Operational caution:** Test application/service-account compatibility before changing expiration or session resource limits.

## Enhanced Deep Dive 51 — Quota vs Tablespace Privilege

A schema needs both object-creation capability and permission to allocate space in the target tablespace. Quotas provide that storage boundary.

```text
CREATE TABLE privilege
    +
quota on APP_DATA
    ↓
segment allocation allowed
```

```sql
SELECT
    username,
    tablespace_name,
    bytes,
    max_bytes
FROM dba_ts_quotas
WHERE username='APP_OWNER';
```

**Expected behavior:** The report shows current usage and quota ceiling.

**Why it works:** Authorization to create an object is separate from authorization to consume storage.

**Operational caution:** Avoid UNLIMITED TABLESPACE for ordinary application schemas.

## Enhanced Deep Dive 52 — Object Ownership vs Tablespace Placement

Schema ownership and physical tablespace placement are independent. APP_OWNER can own a table whose segment is stored in APP_DATA and an index stored in APP_INDEX.

```text
schema owner APP_OWNER
  ├→ table → APP_DATA
  └→ index → APP_INDEX
```

```sql
SELECT
    owner,
    segment_name,
    segment_type,
    tablespace_name
FROM dba_segments
WHERE owner='APP_OWNER'
ORDER BY segment_type, segment_name;
```

**Expected behavior:** Objects can be inventoried by ownership and physical tablespace.

**Why it works:** Oracle separates logical security ownership from storage placement.

**Operational caution:** Do not assume moving a segment changes schema ownership or privileges.

## Enhanced Deep Dive 53 — Segment Growth Investigation

When a tablespace grows, identify which segments are responsible before adding storage. One large table/index/LOB can dominate usage.

```text
tablespace growth
  ↓
segments by bytes
  ↓
business owner / retention / index review
```

```sql
SELECT *
FROM (
    SELECT
        owner,
        segment_name,
        segment_type,
        bytes/1024/1024 AS mb
    FROM dba_segments
    WHERE tablespace_name='APP_DATA'
    ORDER BY bytes DESC
)
FETCH FIRST 20 ROWS ONLY;
```

**Expected behavior:** The largest space consumers become visible.

**Why it works:** Capacity management starts from object-level evidence.

**Operational caution:** Adding storage can hide a runaway retention or failed purge process.

## Enhanced Deep Dive 54 — LOB Segment Awareness

CLOB/BLOB columns often use separate LOB segments and indexes. A table can appear small while its LOB storage is huge.

```text
table row
  ↓ LOB locator
LOB segment
  ↓ large content
```

```sql
SELECT
    owner,
    table_name,
    column_name,
    segment_name,
    tablespace_name
FROM dba_lobs
WHERE owner='APP_OWNER';
```

**Expected behavior:** LOB storage is mapped separately from base table segments.

**Why it works:** Large objects have specialized physical storage.

**Operational caution:** Capacity and backup planning must include LOB segments, not only table segment sizes.

## Enhanced Deep Dive 55 — High-water Mark Awareness

Deleting rows does not necessarily return all table segment space to the tablespace or shrink the scan range. Segment high-water behavior affects full scans and space reclamation.

```text
segment allocated blocks
[used][used][free inside segment]
  ↑ high-water region may remain
```

```sql
SELECT
    segment_name,
    bytes/1024/1024 AS mb
FROM dba_segments
WHERE owner='APP_OWNER'
  AND segment_type='TABLE';
```

**Expected behavior:** Segment allocation can remain large after deletes.

**Why it works:** DELETE changes row contents; segment-space reclamation is a separate operation.

**Operational caution:** Do not shrink/move large production objects without analyzing locking, indexes, row movement, downtime, and recovery.

## Enhanced Deep Dive 56 — Datafile Resize Safety

A datafile can sometimes be resized smaller only when used extents do not occupy blocks beyond the target size. Capacity reduction is therefore not just a filesystem truncate.

```text
datafile
[used extents........][free tail]
                   ↓
resize possible only above used high blocks
```

```sql
ALTER DATABASE DATAFILE
'/path/app_data01.dbf'
RESIZE 1500M;
```

**Expected behavior:** A valid resize succeeds; an undersized target fails rather than discarding allocated extents.

**Why it works:** Oracle protects allocated database blocks from unsafe truncation.

**Operational caution:** Use real file names from dictionary/OMF-aware procedures, not copied paths.

## Enhanced Deep Dive 57 — PDB Storage and File Identification

In a CDB, files belong to containers. Capacity scripts should include `CON_ID` or use CDB views so the DBA knows which PDB owns each file.

```text
CDB files
  ↓ CON_ID
PDB1 files
PDB2 files
```

```sql
SELECT
    con_id,
    file#,
    name
FROM v$datafile
ORDER BY con_id, file#;
```

**Expected behavior:** Each datafile can be associated with container scope.

**Why it works:** Multitenant file administration requires both file identity and container identity.

**Operational caution:** Never move/drop a file based only on a basename when multiple PDBs can have similar logical structures.

## Enhanced Deep Dive 58 — Service Health Must Be End-to-End

A listener can be running while the PDB is closed, a service is unregistered, or the application user is locked. Health checks should validate the full connection path.

```text
DNS
 ↓
TCP listener
 ↓
service registered
 ↓
PDB READ WRITE
 ↓
user authenticated
 ↓
simple SQL succeeds
```

```sql
SELECT
    SYS_CONTEXT('USERENV','SERVICE_NAME') AS service_name,
    SYS_CONTEXT('USERENV','CON_NAME') AS con_name
FROM dual;
```

**Expected behavior:** A successful test session proves the service reached the expected container.

**Why it works:** Availability is an application-path property, not a process-exists property.

**Operational caution:** Do not declare the database healthy from `ps -ef | grep pmon` alone.

## Enhanced Deep Dive 59 — Dynamic Performance Views Are Current-State Evidence

`V$` and `GV$` views expose live or near-live instance state. Dictionary views such as `DBA_TABLES` describe metadata. The DBA must choose the evidence source that matches the question.

```text
Question:
'what exists?' → dictionary
'what is happening now?' → V$/GV$
```

```sql
SELECT
    sid,
    status,
    event,
    sql_id
FROM v$session
WHERE username IS NOT NULL;
```

**Expected behavior:** The view reports current session state.

**Why it works:** Oracle separates persistent metadata from dynamic runtime structures.

**Operational caution:** Do not use a static object inventory to answer a runtime wait/performance question.

## Enhanced Deep Dive 60 — GV$ Views and RAC Awareness

`GV$` views add instance identity to dynamic state and become essential in RAC. Even on single-instance systems, understanding the distinction prepares the DBA for clustered administration.

```text
V$SESSION
→ local instance

GV$SESSION
→ all instances + INST_ID
```

```sql
SELECT
    inst_id,
    sid,
    serial#,
    username
FROM gv$session
WHERE username IS NOT NULL;
```

**Expected behavior:** In RAC the rows can come from multiple instances.

**Why it works:** Global views aggregate per-instance fixed tables.

**Operational caution:** Do not assume SID is globally unique in RAC; pair it with instance context.

## Enhanced Deep Dive 61 — V$SESSION Status Is Not 'Good or Bad'

ACTIVE means the session is currently executing or waiting in an active call; INACTIVE often means it is connected but idle. Thousands of inactive pooled sessions can be normal or wasteful depending on architecture.

```text
session
  ├→ ACTIVE: in a call
  └→ INACTIVE: idle between calls
```

```sql
SELECT
    status,
    COUNT(*) AS sessions
FROM v$session
WHERE username IS NOT NULL
GROUP BY status;
```

**Expected behavior:** The distribution of active/inactive sessions is visible.

**Why it works:** Session state reflects current call activity, not business health by itself.

**Operational caution:** Do not kill every INACTIVE session; understand connection pooling and application expectations.

## Enhanced Deep Dive 62 — V$TRANSACTION and Long Transactions

A connected session may or may not have an active transaction. Mapping `V$SESSION` to `V$TRANSACTION` helps identify sessions retaining undo and locks.

```text
session
  ↓ TADDR
transaction
  ↓ undo / start time / locks
```

```sql
SELECT
    s.sid,
    s.serial#,
    s.username,
    t.start_time
FROM v$session s
JOIN v$transaction t
  ON t.addr = s.taddr;
```

**Expected behavior:** Only sessions with active transactions appear.

**Why it works:** Transaction state is separate from connection state.

**Operational caution:** An inactive session can still hold an open transaction and block work.

## Enhanced Deep Dive 63 — Blocking Chain Thinking

A large number of waiting sessions can be symptoms of one root blocker. Investigate the blocking tree rather than treating every waiter individually.

```text
root blocker A
  ├→ waiter B
  │    └→ waiter D
  └→ waiter C
```

```sql
SELECT
    sid,
    serial#,
    username,
    blocking_session,
    event
FROM v$session
WHERE blocking_session IS NOT NULL;
```

**Expected behavior:** Waiters can identify their blocker in common locking scenarios.

**Why it works:** Fixing the root transaction can release many downstream sessions at once.

**Operational caution:** Killing a waiter rarely solves the root cause.

## Enhanced Deep Dive 64 — Session Kill Lifecycle

`ALTER SYSTEM KILL SESSION` marks a session for termination; cleanup/rollback may take time. A killed session can remain visible while Oracle safely cleans transaction state.

```text
kill request
  ↓
session marked
  ↓
rollback/cleanup
  ↓
resources released
```

```sql
ALTER SYSTEM
KILL SESSION '123,4567'
IMMEDIATE;
```

**Expected behavior:** The exact target is identified by SID and SERIAL#.

**Why it works:** SERIAL# prevents accidentally targeting a new session that reused the same SID.

**Operational caution:** Use application owner/business impact analysis first; killing a large transaction can create a long rollback.

## Enhanced Deep Dive 65 — Scheduler Job State vs Last Run Result

A scheduler job being ENABLED only means it is eligible to run. Operational health requires checking run history and error status.

```text
job enabled
  ↓ schedule fires
run
  ├→ succeeded
  └→ failed → evidence
```

```sql
SELECT
    owner,
    job_name,
    status,
    actual_start_date,
    run_duration,
    additional_info
FROM dba_scheduler_job_run_details
ORDER BY actual_start_date DESC
FETCH FIRST 30 ROWS ONLY;
```

**Expected behavior:** Recent job outcomes are visible.

**Why it works:** Automation must be monitored by outcomes, not just configuration state.

**Operational caution:** Recurring failed jobs can create data, backup, or capacity incidents even though the job remains enabled.

## Enhanced Deep Dive 66 — Unified Audit Policy Design

Auditing should start from detection/compliance questions: which privileged actions, logons, schema changes, and sensitive-object accesses matter? Auditing everything without retention and review can create noise and storage pressure.

```text
security requirement
  ↓
audit policy
  ↓
unified audit trail
  ↓
central review / retention
```

```sql
SELECT
    policy_name,
    enabled_option,
    entity_name
FROM audit_unified_enabled_policies
ORDER BY policy_name;
```

**Expected behavior:** Enabled policy scope can be reviewed.

**Why it works:** Policy-driven auditing creates intentional evidence rather than uncontrolled logging.

**Operational caution:** Audit trail access and purge rights are themselves high-value privileges.

## Enhanced Deep Dive 67 — Audit Trail Storage and Retention

Audit data consumes storage and has legal/security retention requirements. Capacity planning must include audit growth and an approved archival/purge workflow.

```text
events
  ↓ unified audit trail
  ↓ retention
  ├→ central export/archive
  └→ approved purge
```

```sql
SELECT
    event_timestamp,
    dbusername,
    action_name,
    object_schema,
    object_name
FROM unified_audit_trail
ORDER BY event_timestamp DESC
FETCH FIRST 20 ROWS ONLY;
```

**Expected behavior:** Recent audited activity can be reviewed with appropriate privileges.

**Why it works:** Audit is useful only when evidence remains available and trustworthy.

**Operational caution:** Never purge audit records merely to fix a tablespace alert without security/compliance approval.

## Enhanced Deep Dive 68 — ADR Home and Diagnostic Scope

ADR stores diagnostic data for database instances and Oracle Net components in structured homes. Knowing the exact ADR home avoids searching random filesystem paths during incidents.

```text
diagnostic_dest
  ↓ diag/
      ├→ rdbms/... instance ADR home
      └→ tnslsnr/... listener ADR home
```

```sql
SHOW PARAMETER diagnostic_dest
```

**Expected behavior:** The base diagnostic destination is reported.

**Why it works:** ADR standardizes location and management of alert/trace/incident data.

**Operational caution:** Use ADRCI or supported retention tools rather than indiscriminately deleting diagnostic directories.

## Enhanced Deep Dive 69 — Alert Log as a Timeline

The alert log is not only an error list. It is a chronological database operational timeline containing startup, shutdown, parameter changes, log switches, archive issues, file errors, and significant ORA events.

```text
time
 ↓ startup
 ↓ parameter change
 ↓ error
 ↓ recovery
 ↓ shutdown
```

```sql
-- ADRCI example:
-- SHOW ALERT -TAIL 100
```

**Expected behavior:** The DBA can reconstruct the sequence of events around an incident.

**Why it works:** Timeline analysis is often more valuable than reading one isolated ORA code.

**Operational caution:** Preserve timestamps and correlate with OS, storage, network, and application logs.

## Enhanced Deep Dive 70 — Trace Files

Server/background processes can write detailed trace files. Trace is more granular than the alert log and can contain stack/error/context information for specific incidents.

```text
ORA event
  ↓ alert summary
  ↓ trace file path/detail
```

```sql
SELECT
    value
FROM v$diag_info
WHERE name IN (
    'Diag Trace',
    'Default Trace File'
);
```

**Expected behavior:** Oracle reports trace directories and current session trace file.

**Why it works:** Diagnostic files connect database-level errors to process-level evidence.

**Operational caution:** Trace files can contain SQL/text/data context; protect them as potentially sensitive diagnostics.

## Enhanced Deep Dive 71 — Parameter File Recovery Safety

Keeping a human-readable PFILE export of the active SPFILE provides a recovery and review artifact. It is not a replacement for proper backup, but it makes parameter diagnosis easier when startup fails.

```text
SPFILE
  ↓ CREATE PFILE
text snapshot
  ↓ version control / secure backup
```

```sql
CREATE PFILE='/tmp/initMANUCDB_backup.ora'
FROM SPFILE;
```

**Expected behavior:** A text parameter snapshot is created.

**Why it works:** SPFILE is binary/managed; PFILE is directly inspectable.

**Operational caution:** Protect the exported file because parameters can include sensitive paths or configuration information.

## Enhanced Deep Dive 72 — Parameter Change Validation

Every parameter change should record current value, desired value, dynamic/static behavior, scope, expected benefit, rollback, and verification. This is configuration management, not ad-hoc tuning.

```text
baseline
 ↓ change request
 ↓ ALTER SYSTEM
 ↓ verify memory/SPFILE
 ↓ observe workload
 ↓ rollback if needed
```

```sql
SELECT
    name,
    value,
    issys_modifiable,
    isdefault,
    ismodified
FROM v$parameter
WHERE name='open_cursors';
```

**Expected behavior:** The parameter metadata shows whether/how it can be changed.

**Why it works:** Oracle exposes changeability metadata so DBAs can avoid guesswork.

**Operational caution:** Never change hidden/underscore parameters without Oracle Support/vendor guidance for the specific issue.

## Enhanced Deep Dive 73 — Hidden Parameters Awareness

Underscore parameters are internal mechanisms and not normal tuning controls. Internet advice that begins with changing `_something` should be treated as a support-level action, not a learning shortcut.

```text
symptom
  ↓ supported diagnosis
  ↓ normal parameters / patch / code fix
  ↓
hidden parameter only under validated guidance
```

```sql
-- Do not change hidden parameters as a training exercise.
```

**Expected behavior:** The correct outcome is usually to avoid unsupported internal tuning.

**Why it works:** Internal parameters can change behavior in undocumented ways.

**Operational caution:** A workaround from another database/version can create corruption, instability, or supportability problems.

## Enhanced Deep Dive 74 — Character Set Is a Database Architecture Decision

Database character set influences storage and application compatibility. Changing it after data exists is not a casual parameter edit.

```text
application text
  ↓ database character set
storage / conversion / interoperability
```

```sql
SELECT
    parameter,
    value
FROM nls_database_parameters
WHERE parameter IN (
    'NLS_CHARACTERSET',
    'NLS_NCHAR_CHARACTERSET'
);
```

**Expected behavior:** The database-level character sets are reported.

**Why it works:** Text encoding is foundational persistent metadata.

**Operational caution:** Plan migrations/conversions using supported tools; do not manually update dictionary character-set values.

## Enhanced Deep Dive 75 — Database Time Zone vs Session Time Zone

Database timezone and session timezone can affect timezone-aware datatypes and application behavior. The DBA should document the organization's timezone strategy.

```text
database timezone
   ↕
session timezone
   ↓
TIMESTAMP WITH LOCAL TIME ZONE rendering
```

```sql
SELECT
    DBTIMEZONE,
    SESSIONTIMEZONE
FROM dual;
```

**Expected behavior:** The current database/session timezone values are visible.

**Why it works:** Temporal correctness spans database configuration and application session state.

**Operational caution:** Changing database timezone can have data-type/application implications; treat it as a planned change.

## Enhanced Deep Dive 76 — Database Default Temporary Tablespace

A default TEMP assignment prevents new users from falling back to inappropriate system storage for temporary operations.

```text
user
  ↓ default temp TS
sort/hash spill
  ↓ tempfile
```

```sql
SELECT
    property_name,
    property_value
FROM database_properties
WHERE property_name LIKE '%TEMP_TABLESPACE%';
```

**Expected behavior:** The configured default temporary tablespace is visible.

**Why it works:** Temporary work deserves a dedicated storage class.

**Operational caution:** Do not confuse TEMP capacity with permanent application data capacity.

## Enhanced Deep Dive 77 — Default Permanent Tablespace

A default permanent tablespace prevents ordinary user objects from accidentally landing in SYSTEM when a tablespace is not specified.

```text
new user/object
  ↓ default permanent TS
  ↓ user/application storage
```

```sql
SELECT
    property_name,
    property_value
FROM database_properties
WHERE property_name='DEFAULT_PERMANENT_TABLESPACE';
```

**Expected behavior:** The database default is visible.

**Why it works:** Defaults reduce dangerous omissions in user/schema creation.

**Operational caution:** Application owners should still receive explicit storage design and quotas.

## Enhanced Deep Dive 78 — Database Service Registration vs PDB Open State

A service can appear in listener output while the database/PDB is not usable in the way the application expects, depending on registration/state transitions. Verify both network registration and container open mode.

```text
listener service
  ↓
connect attempt
  ↓
PDB state
  ↓
application SQL
```

```sql
SELECT
    name,
    open_mode
FROM v$pdbs;

SELECT
    name,
    pdb
FROM v$services;
```

**Expected behavior:** The DBA can compare service and PDB state directly.

**Why it works:** Network identity and storage/container state are separate layers.

**Operational caution:** End-to-end probes should connect using the same service as the application.

## Enhanced Deep Dive 79 — Service-level Application Health SQL

A database health probe should be cheap, read-only, and prove the expected service/container is available.

```text
monitor
  ↓ application service
  ↓ authentication
  ↓ SELECT context
  ↓ healthy
```

```sql
SELECT
    SYS_CONTEXT('USERENV','DB_NAME') AS db_name,
    SYS_CONTEXT('USERENV','CON_NAME') AS con_name,
    SYS_CONTEXT('USERENV','SERVICE_NAME') AS service_name
FROM dual;
```

**Expected behavior:** The probe proves that a login reached the expected database, container, and service.

**Why it works:** This tests more of the real application path than a TCP port check.

**Operational caution:** Use a dedicated low-privilege monitoring identity, not SYS.

## Enhanced Deep Dive 80 — Startup FORCE

`STARTUP FORCE` combines an abort-like restart when needed. It is an operational recovery convenience, not a routine first choice.

```text
running instance → forced shutdown/restart → OPEN
```

```sql
STARTUP FORCE;
```

## Enhanced Deep Dive 81 — Shutdown Transactional

Transactional shutdown waits for active transactions to finish while preventing new transactional work according to mode semantics.

```text
new tx blocked → existing tx finish → shutdown
```

```sql
SHUTDOWN TRANSACTIONAL;
```

## Enhanced Deep Dive 82 — Parameter Modifiability

`ISSYS_MODIFIABLE` helps distinguish immediate/deferred/static parameter behavior.

```text
V$PARAMETER → changeability
```

```sql
SELECT name,issys_modifiable FROM v$parameter;
```

## Enhanced Deep Dive 83 — SPFILE Location Discovery

`SHOW PARAMETER spfile` proves whether an SPFILE is active and where it resides.

```text
startup source → SPFILE path
```

```sql
SHOW PARAMETER spfile
```

## Enhanced Deep Dive 84 — Password File Users

Administrative password-file identities can be inventoried through supported dictionary views.

```text
password file → privileged identities
```

```sql
SELECT * FROM v$pwfile_users;
```

## Enhanced Deep Dive 85 — Database Role and Open Mode

`V$DATABASE` exposes role/open mode, foundational for Data Guard and recovery later.

```text
database → role + open mode
```

```sql
SELECT database_role,open_mode FROM v$database;
```

## Enhanced Deep Dive 86 — Control File Record Sections

The control file contains multiple reusable record sections for backup/log/history metadata; record retention influences RMAN metadata history.

```text
control file → record sections
```

```sql
SELECT type,records_total,records_used FROM v$controlfile_record_section;
```

## Enhanced Deep Dive 87 — Control File Record Keep Time

`CONTROL_FILE_RECORD_KEEP_TIME` influences retention of reusable control-file records, especially relevant to backup metadata.

```text
RMAN metadata → reusable records → keep-time policy
```

```sql
SHOW PARAMETER control_file_record_keep_time
```

## Enhanced Deep Dive 88 — ARCHIVE Destination State

Archive destinations have status/error information that should be monitored before they block redo reuse.

```text
redo switch → destination → success/error
```

```sql
SELECT dest_id,status,error FROM v$archive_dest_status WHERE status<>'INACTIVE';
```

## Enhanced Deep Dive 89 — Force Archive Switch

`ALTER SYSTEM ARCHIVE LOG CURRENT` can force archival of current redo in controlled workflows.

```text
current redo → archive request
```

```sql
ALTER SYSTEM ARCHIVE LOG CURRENT;
```

## Enhanced Deep Dive 90 — Redo Member Loss Awareness

Losing one multiplexed member may leave the group usable but degraded; replace the failed member using supported procedures.

```text
group members A+B → A lost → group degraded
```

```sql
SELECT group#,member,status FROM v$logfile;
```

## Enhanced Deep Dive 91 — Database Block Size

`DB_BLOCK_SIZE` defines the standard database block size and is foundational to storage/I/O concepts.

```text
OS storage ↔ Oracle blocks
```

```sql
SHOW PARAMETER db_block_size
```

## Enhanced Deep Dive 92 — Tablespace Block Size

Nonstandard block-size tablespaces require corresponding buffer caches and specialized justification.

```text
tablespace → block size → cache
```

```sql
SELECT tablespace_name,block_size FROM dba_tablespaces;
```

## Enhanced Deep Dive 93 — Segment Extent Growth

Segments acquire extents as they grow; locally managed allocation makes this mostly automatic.

```text
segment → extent1+extent2+...
```

```sql
SELECT segment_name,extents FROM dba_segments WHERE owner='APP_OWNER';
```

## Enhanced Deep Dive 94 — Free Space Fragment View

Free extents can be inspected, but ASSM/LMT reduces the need for old-style manual fragmentation tuning.

```text
tablespace → free extents
```

```sql
SELECT tablespace_name,COUNT(*) extents,SUM(bytes) bytes FROM dba_free_space GROUP BY tablespace_name;
```

## Enhanced Deep Dive 95 — Tempfile Autoextend

TEMP files also have autoextend/maxsize constraints and underlying storage limits.

```text
sort spill → tempfile → max size
```

```sql
SELECT file_name,bytes,maxbytes,autoextensible FROM dba_temp_files;
```

## Enhanced Deep Dive 96 — Temp Usage by Session

Temporary-segment views can identify sessions consuming TEMP during large sorts/hashes.

```text
session → temp segments → TEMP
```

```sql
SELECT * FROM v$tempseg_usage;
```

## Enhanced Deep Dive 97 — Undo Tablespace Switching

Changing the active undo tablespace is an online administrative operation in supported conditions and requires capacity planning.

```text
UNDO_A active → ALTER SYSTEM → UNDO_B
```

```sql
ALTER SYSTEM SET undo_tablespace=UNDOTBS2;
```

## Enhanced Deep Dive 98 — PDB Default Tablespace

Each PDB/application schema should have explicit default storage design rather than inherited accidental defaults.

```text
PDB → default TS → schemas
```

```sql
SELECT property_name,property_value FROM database_properties WHERE property_name LIKE '%TABLESPACE%';
```

## Enhanced Deep Dive 99 — Create User in Correct Container

A local user must be created while connected to the intended PDB; the same command in root has different scope/rules.

```text
SHOW CON_NAME → CREATE USER
```

```sql
SHOW CON_NAME;
```

## Enhanced Deep Dive 100 — Common-user Naming Rules

Common-user naming is governed by multitenant conventions/prefix configuration; application users should normally remain local.

```text
root → common identity namespace
```

```sql
SHOW PARAMETER common_user_prefix
```

## Enhanced Deep Dive 101 — Container Data Views

`CDB_*` views allow appropriately privileged root sessions to see per-container metadata.

```text
root → CDB_* → CON_ID
```

```sql
SELECT con_id,username FROM cdb_users;
```

## Enhanced Deep Dive 102 — PDB Storage Quotas

Local schema quotas belong to the PDB's local tablespaces and must be checked in the correct container.

```text
local user → local TS quota
```

```sql
SELECT username,tablespace_name,max_bytes FROM dba_ts_quotas;
```

## Enhanced Deep Dive 103 — PDB Close Impact

Closing a PDB ends or disrupts application sessions depending on close mode; treat it as service downtime.

```text
PDB service → CLOSE → client impact
```

```sql
ALTER PLUGGABLE DATABASE MANUPDB CLOSE IMMEDIATE;
```

## Enhanced Deep Dive 104 — PDB Restricted Open

A PDB can be opened restricted for controlled maintenance with fewer users.

```text
PDB → restricted maintenance
```

```sql
ALTER PLUGGABLE DATABASE MANUPDB OPEN RESTRICTED;
```

## Enhanced Deep Dive 105 — PDB Clone Readiness

Before cloning, verify source open state, storage destination, encryption/key requirements, capacity, and data-governance controls.

```text
source PDB → readiness → clone
```

```sql
SHOW PDBS;
```

## Enhanced Deep Dive 106 — Service Naming Standard

Stable service naming separates application identity from host/instance names and simplifies later HA.

```text
app name → service → current instance/PDB
```

```sql
SELECT name,pdb FROM v$services;
```

## Enhanced Deep Dive 107 — Session Service Attribution

`SERVICE_NAME` in session context lets DBAs separate workloads sharing one database.

```text
connections → service → workload identity
```

```sql
SELECT service_name,COUNT(*) FROM v$session GROUP BY service_name;
```

## Enhanced Deep Dive 108 — Client Module/Action

Applications can set MODULE/ACTION so DBA views identify business operations.

```text
request → module/action → V$SESSION
```

```sql
SELECT module,action,COUNT(*) FROM v$session GROUP BY module,action;
```

## Enhanced Deep Dive 109 — Client Identifier

Connection pools can set CLIENT_IDENTIFIER for end-user/request attribution.

```text
pooled session → client identifier
```

```sql
SELECT client_identifier,COUNT(*) FROM v$session GROUP BY client_identifier;
```

## Enhanced Deep Dive 110 — Open Cursors

`OPEN_CURSORS` limits cursors a session can keep open; exhaustion often points to application cursor leaks.

```text
app opens cursors → limit
```

```sql
SHOW PARAMETER open_cursors
```

## Enhanced Deep Dive 111 — Cursor Leak Investigation

High opened-cursor counts should lead to application/cursor-lifecycle investigation rather than arbitrary parameter increases.

```text
session → open cursor count → leak?
```

```sql
SELECT sid,COUNT(*) FROM v$open_cursor GROUP BY sid ORDER BY COUNT(*) DESC FETCH FIRST 10 ROWS ONLY;
```

## Enhanced Deep Dive 112 — Processes and Sessions Limits

`PROCESSES` and `SESSIONS` capacity must align with workload and connection pools.

```text
connections → sessions/processes limits
```

```sql
SHOW PARAMETER processes
SHOW PARAMETER sessions
```

## Enhanced Deep Dive 113 — Connection Storm Risk

A restart of many app instances can create simultaneous authentication/process creation pressure.

```text
apps restart → connection burst → DB overload
```

```sql
-- Mitigate with pools, backoff, staged startup.
```

## Enhanced Deep Dive 114 — Listener Log Awareness

Listener diagnostic logs help distinguish network/service registration errors from database authentication failures.

```text
client → listener → log evidence
```

```sql
-- Inspect listener ADR home with ADRCI.
```

## Enhanced Deep Dive 115 — Network Reachability vs TNS

TCP connectivity only proves transport; TNS service resolution and DB authentication are later layers.

```text
TCP 1521 ✓ → service? → auth?
```

```bash
tnsping MANUPDB
```

## Enhanced Deep Dive 116 — TNSPING Limitations

`tnsping` validates naming/connectivity to the listener path but does not prove the database user can log in or execute SQL.

```text
tnsping ✓ ≠ DB login ✓
```

```bash
tnsping MANUPDB
```

## Enhanced Deep Dive 117 — SQLNET Timeouts Awareness

Connect/receive timeout policies can prevent sessions hanging indefinitely across broken networks; values must match application behavior.

```text
network failure → timeout → controlled error
```

```sql
-- Configure using current Oracle Net documentation.
```

## Enhanced Deep Dive 118 — OS Authentication

Local administrative OS authentication can avoid embedding SYS passwords in scripts when the host trust model permits it.

```text
trusted OS group → / as sysdba
```

```bash
sqlplus / as sysdba
```

## Enhanced Deep Dive 119 — Separation of Admin Identities

Named administrative accounts improve attribution compared with everyone using SYS for routine work.

```text
DBA person → named admin → audited actions
```

```sql
-- Use least-privilege admin design.
```

## Enhanced Deep Dive 120 — SYS-Owned Dictionary Protection

Core dictionary objects belong to SYS and are not application customization space.

```text
SYS schema → core metadata
```

```sql
SELECT owner,COUNT(*) FROM dba_objects WHERE owner='SYS' GROUP BY owner;
```

## Enhanced Deep Dive 121 — Recycle Bin Awareness

DROP TABLE can place eligible objects in the recycle bin, consuming space until purged or reused.

```text
DROP → recycle bin → flashback/purge
```

```sql
SHOW RECYCLEBIN
```

## Enhanced Deep Dive 122 — Deferred Segment Creation Awareness

Some objects may not allocate segments until data is inserted, so object existence and segment existence can differ.

```text
CREATE TABLE → metadata now → segment later
```

```sql
SELECT table_name,segment_created FROM user_tables;
```

## Enhanced Deep Dive 123 — Read-only User Design

Reporting users should receive SELECT on views or controlled objects instead of broad schema ownership privileges.

```text
REPORTUSER → role → views
```

```sql
GRANT SELECT ON app_owner.v_order_summary TO reporting_role;
```

## Enhanced Deep Dive 124 — Object Privilege WITH GRANT OPTION

Grant option lets a recipient regrant an object privilege, expanding delegation scope.

```text
owner → user WITH GRANT OPTION → third user
```

```sql
-- Grant only when delegation is explicitly required.
```

## Enhanced Deep Dive 125 — System Privilege WITH ADMIN OPTION

Admin option lets role/system privilege recipients grant it onward, creating powerful delegation paths.

```text
admin privilege → grantee → regrant
```

```sql
SELECT * FROM dba_sys_privs WHERE admin_option='YES';
```

## Enhanced Deep Dive 126 — Role Nesting

Roles can contain roles, simplifying administration but also obscuring effective privilege paths.

```text
user → role A → role B → privileges
```

```sql
SELECT * FROM role_role_privs;
```

## Enhanced Deep Dive 127 — Effective Privilege Review

Security review should trace direct system grants, object grants, roles, nested roles, and common/local scope.

```text
identity → effective privilege graph
```

```sql
-- Build a privilege inventory report.
```

## Enhanced Deep Dive 128 — Audit Privileged DDL

User/role changes and grants should be covered by intentional audit policy and change management.

```text
admin DDL → unified audit → review
```

```sql
-- Define policy according to security requirements.
```

## Enhanced Deep Dive 129 — Resource Limit Parameter Awareness

Profile resource controls depend on database enforcement settings such as RESOURCE_LIMIT where relevant.

```text
profile limits → RESOURCE_LIMIT → enforcement
```

```sql
SHOW PARAMETER resource_limit
```

## Enhanced Deep Dive 130 — Database Scheduler Ownership

Recurring database tasks should have one owner and monitored outcome, not duplicate schedules across cron/application/DB.

```text
task → one scheduler → monitored result
```

```sql
SELECT owner,job_name,state FROM dba_scheduler_jobs;
```

## Enhanced Deep Dive 131 — Statistics Job Awareness

Oracle maintenance windows can run automatic tasks such as optimizer statistics collection; DBA should know when they run before diagnosing night-time load.

```text
maintenance window → auto task → workload
```

```sql
SELECT client_name,status FROM dba_autotask_client;
```

## Enhanced Deep Dive 132 — Invalid Object Count as Deployment Metric

Track invalid counts by owner before/after releases so expected system objects are not mixed with new application failures.

```text
baseline invalids → deploy → compare
```

```sql
SELECT owner,COUNT(*) FROM dba_objects WHERE status='INVALID' GROUP BY owner;
```

## Enhanced Deep Dive 133 — Compile Schema Procedure

Oracle provides supported mechanisms to recompile invalid schema objects, but root cause should be fixed first.

```text
fix dependency → recompile → verify
```

```sql
BEGIN DBMS_UTILITY.COMPILE_SCHEMA(schema=>'APP_OWNER'); END; /
```

## Enhanced Deep Dive 134 — Alert Log Error Correlation

When an ORA error appears in application logs, correlate its timestamp with alert/trace only if it is a database-level event; many user SQL errors never belong in alert log.

```text
app error time ↔ DB diagnostics
```

```sql
-- Correlate timestamps and session/module.
```

## Enhanced Deep Dive 135 — Filesystem Capacity

Database datafile autoextend can fail because the OS filesystem is full; DB and OS monitoring must be correlated.

```text
datafile max → filesystem free
```

```bash
df -h
```

## Enhanced Deep Dive 136 — Inode/Filesystem Metadata Awareness

A filesystem can fail allocations due to inode/metadata issues even when byte capacity seems available, depending on filesystem.

```text
DB write → OS filesystem metadata
```

```bash
df -i
```

## Enhanced Deep Dive 137 — Mount Options and DB Storage

Filesystem mount reliability/performance options affect database storage and must follow Oracle/storage vendor support guidance.

```text
Oracle I/O → filesystem → storage
```

```bash
mount | grep oradata
```

## Enhanced Deep Dive 138 — NTP/Clock Discipline

Accurate host time supports logs, certificates, Kerberos-like integrations, cluster/DR operations, and incident correlation.

```text
time source → DB host → logs/audit
```

```sql
timedatectl status
```

## Enhanced Deep Dive 139 — Host Memory Pressure

OS swapping can severely hurt Oracle performance even if SGA/PGA settings look valid.

```text
Oracle memory + OS → swap pressure
```

```bash
free -h
```

## Enhanced Deep Dive 140 — HugePages Awareness

Large-page configuration can reduce page-table overhead for large SGA deployments on Linux, but exact setup depends on memory management mode and platform guidance.

```text
SGA → large pages → fewer page-table entries
```

```bash
grep -i Huge /proc/meminfo
```

## Enhanced Deep Dive 141 — NUMA Awareness

Large multi-socket systems introduce NUMA locality considerations. Treat NUMA tuning as platform/workload engineering rather than a beginner parameter tweak.

```text
CPU sockets ↔ local memory
```

```bash
lscpu
```

## Enhanced Deep Dive 142 — Database Process Baseline

A baseline of PMON-like/background processes, listener, memory, and file locations makes abnormal state easier to identify.

```text
healthy host snapshot → compare incident
```

```bash
ps -ef | grep ora_
```

## Enhanced Deep Dive 143 — Configuration Inventory

Record Oracle home, patch inventory, CDB/PDB names, services, listener, storage, SPFILE, FRA, and OS details in an operational inventory.

```text
host → Oracle inventory document
```

```bash
$ORACLE_HOME/OPatch/opatch lsinventory
```

## Enhanced Deep Dive 144 — Change Evidence

Before/after snapshots of parameters, services, files, and alerts turn maintenance into a verifiable process.

```text
baseline → change → validation
```

```sql
-- spool precheck/postcheck output.
```

## Enhanced Deep Dive 145 — Daily Health as Read-only Automation

Health automation should collect evidence and alert; destructive remediation should require separate logic/approval.

```text
health SQL → report → alert, not auto-delete/kill
```

```sql
-- DAILY_HEALTH.sql should be read-only.
```

## Enhanced Deep Dive 146 — PDB Health Per Service

For each required application PDB, monitor open mode, service, connection, basic query, and capacity.

```text
PDB → service → probe → business health
```

```sql
SELECT name,open_mode FROM v$pdbs;
```

## Enhanced Deep Dive 147 — Capacity Forecasting

Trend allocated/used/max storage over time rather than waiting for a 95% threshold.

```text
history → growth rate → forecast exhaustion date
```

```sql
-- Export daily tablespace/file metrics.
```

## Enhanced Deep Dive 148 — Runbook-driven Operations

Every high-impact operation should have prerequisites, exact target, commands, validation, rollback, and escalation.

```text
change → runbook → execute → validate
```

```sql
-- STARTUP, listener, tablespace, PDB, account, archive runbooks.
```

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Startup Dependency Matrix

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 2 — Restricted Session Maintenance

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 3 — Read-only PDB

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 4 — SCN Observation

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 5 — Abort and Instance Recovery

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 6 — SGA Dynamic Components

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 7 — Buffer Cache Evidence

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 8 — Shared Pool Cursor Baseline

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 9 — Large Pool Review

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 10 — PGA and TEMP Correlation

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 11 — Dedicated vs Shared Server Design

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 12 — Session-to-OS Process Mapping

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 13 — Background Process Data Flow

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 14 — Control File Multiplexing Review

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 15 — Redo Group/Member Map

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 16 — Redo Switch History

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 17 — Archive Lifecycle

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 18 — FRA Capacity

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 19 — Datafile Header State

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 20 — Smallfile vs Bigfile

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 21 — Locally Managed Tablespace

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 22 — ASSM

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 23 — OMF

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 24 — ASM Architecture Design

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 25 — Read-only Tablespace

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 26 — Offline Tablespace

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 27 — Autoextend Capacity

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 28 — Temporary Tablespace Group

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 29 — Undo Retention

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 30 — Snapshot-too-old Tabletop

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 31 — CON_ID Inventory

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 32 — Common vs Local User

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 33 — Common vs Local Role

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 34 — PDB Save State

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 35 — PDB Unplug/Plug Design

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 36 — Secure PDB Clone Design

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 37 — PDB Services

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 38 — Dynamic Listener Registration

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 39 — LOCAL_LISTENER Failure

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 40 — TNS_ADMIN Resolution

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 41 — Listener vs Authentication

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 42 — SYSDBA Review

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 43 — Password-file Users

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 44 — Default Roles

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 45 — Quota and Segment Placement

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 46 — Segment Growth

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 47 — LOB Storage

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 48 — High-water Mark Design Review

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 49 — Datafile Resize

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 50 — PDB File Ownership

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 51 — End-to-End Service Probe

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 52 — V$ vs DBA_* Evidence

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 53 — GV$ Awareness

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 54 — Inactive Session Analysis

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 55 — V$TRANSACTION

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 56 — Blocking Chain

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 57 — Safe Session Kill

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 58 — Scheduler Failure Investigation

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 59 — Unified Audit Baseline

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 60 — ADR and Alert Timeline

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 61 — Trace-file Evidence

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 62 — SPFILE/PFILE Recovery Artifact

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 63 — Parameter Change Runbook

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 64 — Character Set Inventory

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 65 — Time Zone Inventory

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 66 — Open Cursor Leak

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 67 — Process/Session Capacity

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 68 — Connection Storm Tabletop

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 69 — OS Capacity Correlation

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 70 — Daily Health Automation

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```

## Enhanced Lab 71 — Integrated DBA-I Failure Challenge

Perform this only in a disposable/authorized Oracle lab. Capture before-state, commands, expected state, actual state, Oracle/OS evidence, rollback, and what would change in production.

```text
Before state
Action
Expected state
Evidence
Root cause / architecture explanation
Security / availability impact
Rollback
```


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Build the Oracle DBA Lab

1. Deploy Oracle Linux or approved platform.
2. Install/provision Oracle AI Database 26ai Free or approved version.
3. identify `ORACLE_BASE`.
4. identify `ORACLE_HOME`.
5. identify database processes.
6. connect as administrative lab user.
7. create `DBA_BASELINE.md`.

### Lab 2 — Instance vs Database

1. Query `V$INSTANCE`.
2. Query `V$DATABASE`.
3. list datafiles.
4. list control files.
5. list redo groups.
6. draw the instance/database architecture.

### Lab 3 — SGA/PGA

1. inspect major memory parameters.
2. inspect SGA information.
3. inspect PGA-related configuration.
4. identify buffer cache/shared-pool/redo concepts.
5. explain shared vs private memory.

### Lab 4 — Background Processes

1. inspect Oracle OS processes.
2. identify LGWR/DBWn/CKPT/ARC-related processes where present.
3. generate a transaction.
4. explain redo vs datafile write path.

### Lab 5 — Startup States

1. `SHUTDOWN IMMEDIATE`.
2. `STARTUP NOMOUNT`.
3. inspect instance/database state.
4. mount.
5. inspect state.
6. open.
7. document what files become necessary at each stage.

### Lab 6 — PFILE/SPFILE

1. determine SPFILE use.
2. create PFILE backup.
3. inspect parameters.
4. change one harmless dynamic lab parameter.
5. verify memory vs persistent scope.
6. revert.

### Lab 7 — Oracle Net

1. run `lsnrctl status`.
2. identify listener port.
3. identify registered services.
4. connect using Easy Connect.
5. connect using a TNS alias.
6. break a lab alias and troubleshoot it.

### Lab 8 — PDB Administration

1. `SHOW PDBS`.
2. open/close MANUPDB.
3. save state.
4. switch container.
5. query container name before every action.
6. create a test PDB if resources permit.

### Lab 9 — Users and Roles

1. create app owner.
2. create reporting user.
3. create reporting role.
4. grant object privileges.
5. test least privilege.
6. lock/unlock account.
7. inspect profile and quota.

### Lab 10 — Permanent Tablespace

1. create `APP_DATA`.
2. create user with quota.
3. create table in it.
4. inspect datafile.
5. grow data safely.
6. inspect usage.

### Lab 11 — TEMP and UNDO

1. inspect TEMP.
2. inspect UNDO.
3. run controlled sort.
4. inspect temporary activity with supported views.
5. run a transaction and explain undo creation.

### Lab 12 — Redo

1. inspect redo groups/members.
2. generate DML.
3. force a log switch.
4. inspect status changes.
5. explain LGWR vs DBWn.

### Lab 13 — ARCHIVELOG

1. inspect log mode.
2. configure lab FRA/archive destination as required.
3. enable ARCHIVELOG using correct mount sequence.
4. generate switches.
5. verify archived logs.
6. document storage-growth risk.

### Lab 14 — Control Files

1. list control files.
2. inspect control-file parameter.
3. draw multiplexing design.
4. do not intentionally destroy all copies.
5. write recovery implications.

### Lab 15 — Dictionary and V$ Views

Build queries using:

```text
DBA_USERS
DBA_TABLESPACES
DBA_DATA_FILES
DBA_OBJECTS
V$INSTANCE
V$DATABASE
V$SESSION
V$LOG
V$SERVICES
```

Explain static metadata vs live performance/state views.

### Lab 16 — Session and Lock Investigation

1. open two sessions.
2. block one transaction with another.
3. identify blocker/waiter.
4. capture SID/SERIAL#.
5. commit blocker.
6. verify waiter continues.
7. discuss safe kill-session criteria.

### Lab 17 — Invalid Object

1. create a test package.
2. break dependency.
3. inspect invalid status.
4. inspect compile errors.
5. fix dependency.
6. recompile.
7. verify.

### Lab 18 — Alert Log / ADR

1. locate diagnostic destination.
2. locate alert log.
3. inspect recent startup/shutdown messages.
4. use ADRCI.
5. generate a harmless known error.
6. find related diagnostic evidence where recorded.

### Lab 19 — Unified Auditing Foundation

1. inspect existing unified audit policies.
2. create a lab audit policy if privileges/environment allow.
3. enable it for a test user.
4. perform test action.
5. inspect unified audit data.
6. disable/remove lab policy.
7. document privilege requirements.

### Lab 20 — Broken Database Challenge

Inject one at a time in a disposable VM:

1. PDB closed.
2. wrong service name.
3. listener stopped.
4. account locked.
5. quota exhausted.
6. temporary-space pressure.
7. invalid object.
8. archive/FRA space warning simulation.
9. long uncommitted transaction.
10. harmless bad initialization-parameter test with snapshot protection.

For every incident:

```text
Symptom
Database state
Evidence
Failed layer
Root cause
Fix
Verification
```

---

## 6. Mini Project

# Mini Project — Administer MANUCDB / MANUPDB

Build:

```text
Oracle Host
   |
   +-- Listener
   |
   +-- MANUCDB
          |
          +-- CDB$ROOT
          +-- PDB$SEED
          +-- MANUPDB
```

## Storage

Create/design:

```text
APP_DATA
APP_INDEX
TEMP
UNDO
FRA
```

Document physical datafile/tempfile locations or OMF/ASM strategy.

## Identity

Create:

```text
APP_OWNER
APP_USER
REPORT_USER
```

Roles:

```text
APP_RUNTIME_ROLE
REPORTING_ROLE
```

Use least privilege.

## Network

Document:

```text
listener
port
service name
Easy Connect
TNS alias
PDB target
```

## Redo/Recovery Readiness

Configure/document:

```text
redo groups
redo members
ARCHIVELOG
FRA
archive destination
control-file copies
```

## Operations

Create:

```text
DAILY_HEALTH.sql
```

It must report:

- instance status
- database open mode
- PDB open mode
- service names
- tablespace/datafile state
- invalid objects
- sessions
- blocking sessions
- log mode
- FRA parameters
- redo-log status
- archive state

## Security

Document:

```text
administrative identity model
application identity model
roles
quotas
profiles
unified auditing baseline
network exposure
```

## Failure Scenarios

Test:

```text
listener down
PDB closed
account locked
quota exhausted
invalid object
blocking session
archive-space pressure design
```

## Project Files

```text
README.md
ARCHITECTURE.md
MEMORY_PROCESSES.md
STORAGE.md
NETWORK.md
USERS_ROLES.sql
TABLESPACES.sql
ARCHIVELOG.md
PDB_ADMIN.sql
DAILY_HEALTH.sql
SECURITY_BASELINE.md
TROUBLESHOOTING.md
```

---


# Expanded Capstone — Production-Style MANUCDB / MANUPDB Administration

Build and document:

```text
                  Application / Monitoring
                           |
                      service name
                           |
                        Listener
                           |
                      Oracle Host
                           |
                 +---------+---------+
                 | Oracle Instance   |
                 | SGA + Processes   |
                 +---------+---------+
                           |
                       MANUCDB
                 +---------+---------+
                 |                   |
             CDB$ROOT             MANUPDB
                                     |
                   +-----------------+------------------+
                   |                 |                  |
                APP_DATA          APP_INDEX            TEMP
                   |
               application
                 objects
```

## Required Administration Deliverables

Create:

```text
ORACLE_INVENTORY.md
INSTANCE_ARCHITECTURE.md
MEMORY_BASELINE.sql
PROCESS_MAP.sql
STARTUP_SHUTDOWN_RUNBOOK.md
MULTITENANT.md
PDB_SERVICES.md
NETWORK.md
STORAGE.md
UNDO_TEMP.md
REDO_ARCHIVE.md
FRA.md
USERS_ROLES.md
AUDITING.md
DIAGNOSTICS.md
DAILY_HEALTH.sql
CAPACITY.md
FAILURE_TESTS.md
```

## Daily Health SQL Must Include

```text
instance/database status
database role/open mode
PDB open modes
services
listener/service probe design
control-file copies
redo groups/members/switch history
archive destination errors
FRA usage
datafile/tempfile size and max growth
tablespace allocation
largest segments
undo health
TEMP consumers
session counts
active transactions
blockers
invalid objects
scheduler failures
unified-audit review entry point
diagnostic destination
important parameter baseline
```

## Failure Tests

At least 30:

```text
listener stopped
wrong service
PDB mounted not open
PDB read only
account locked
missing CREATE SESSION
role not default
quota exhausted
tablespace read only
tablespace offline
datafile cannot autoextend
filesystem nearly full
TEMP pressure
long transaction
snapshot-too-old design
root blocker
session kill/rollback
invalid package
scheduler job failure
archive destination error
FRA pressure
one redo member missing design
control-file copy loss design
wrong LOCAL_LISTENER
wrong TNS_ADMIN
open cursor leak
process/session capacity
shared pool literal SQL pressure
OS swap pressure
post-restart PDB not open
```

For every scenario:

```text
Business symptom
Layer that failed
Oracle evidence
OS/network evidence
Root cause
Safe correction
Verification
Prevention
```

No production data should be used for destructive lab tests.


## 7. Recommended Resources

Use official Oracle documentation for the exact database release installed:

- Oracle AI Database Administrator's Guide
- Oracle AI Database Concepts / Technical Architecture
- Oracle Multitenant Administrator's Guide
- Oracle Net Services Administrator's Guide
- Oracle Database Reference
- Oracle Database Security Guide
- Oracle SQL Language Reference
- Oracle Utilities / SQL*Plus documentation
- Oracle AI Database Upgrade Guide for current deprecations/desupports

Important current-version notes:

- Multitenant CDB/PDB architecture is the supported architecture for Oracle Database 21c and later.
- Oracle AI Database 26ai uses unified auditing as the forward auditing model; traditional auditing is desupported for new traditional audit configuration.
- Version-specific upgrade and management procedures must be checked against current Oracle documentation.

---

## 8. Certification Relevance

This course develops practical skills for:

```text
Oracle DBA
Database Administrator
Database Operations Engineer
Linux/Database Engineer
Cloud Database Engineer
Application Support Engineer
```

It is the direct prerequisite for:

```text
31. Oracle Database Administration II
```

DBA II will assume you already understand:

```text
instance/database
CDB/PDB
memory/processes
storage
redo/undo
control files
ARCHIVELOG
networking
users/roles
dictionary views
diagnostics
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Treating instance and database as the same thing.  
  **Best practice:** Always separate memory/process state from persistent files.

- **Mistake:** Ignoring the current container.  
  **Best practice:** Check `SHOW CON_NAME` before multitenant administration.

- **Mistake:** Putting application objects in CDB$ROOT.  
  **Best practice:** Use application PDBs.

- **Mistake:** Memorizing background-process names without understanding data flow.  
  **Best practice:** Learn what LGWR, DBWn, CKPT, ARC and monitoring functions do.

- **Mistake:** Tuning memory from copied internet values.  
  **Best practice:** Measure workload and use documented sizing/tuning methods.

- **Mistake:** Hardcoding SID-style connections in modern PDB applications.  
  **Best practice:** Use database services.

- **Mistake:** Giving unlimited tablespace to every user.  
  **Best practice:** Use quotas.

- **Mistake:** Using SYS for application work.  
  **Best practice:** Separate administrative and application identities.

- **Mistake:** Treating autoextend as unlimited capacity.  
  **Best practice:** Monitor max size and physical storage.

- **Mistake:** Deleting datafiles/redo/archive files manually.  
  **Best practice:** Use supported Oracle administration procedures.

- **Mistake:** Enabling ARCHIVELOG without archive/FRA capacity planning.  
  **Best practice:** Monitor recovery-area growth and retention.

- **Mistake:** Killing blockers without business context.  
  **Best practice:** Identify transaction owner and impact first.

- **Mistake:** Treating audit logging as optional noise.  
  **Best practice:** Define useful unified audit policies and retention.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is an Oracle instance?

**Short answer:** SGA memory plus Oracle processes used to access/manage the database.

### Q2. What is the Oracle database?

**Short answer:** Persistent database files such as datafiles, control files, and online redo logs.

### Q3. What is a CDB?

**Short answer:** A multitenant container database hosting root, seed, and pluggable databases.

### Q4. What is a PDB?

**Short answer:** A pluggable application database inside a CDB that appears logically independent to applications.

### Q5. What is CDB$ROOT?

**Short answer:** The root container holding common/system metadata and infrastructure.

### Q6. What is PDB$SEED?

**Short answer:** The template PDB used for creating new PDBs.

### Q7. SGA vs PGA?

**Short answer:** SGA is shared instance memory; PGA is private process/session work memory.

### Q8. What is the buffer cache?

**Short answer:** SGA memory caching database blocks.

### Q9. What is the shared pool?

**Short answer:** SGA memory containing shared SQL/PLSQL and metadata structures.

### Q10. What does LGWR do?

**Short answer:** Writes redo from memory to online redo logs.

### Q11. What does DBWn do?

**Short answer:** Writes dirty database buffers to datafiles.

### Q12. What does ARCn do?

**Short answer:** Archives completed redo logs in ARCHIVELOG mode.

### Q13. What happens at NOMOUNT?

**Short answer:** The instance starts using initialization parameters, but the control file is not opened.

### Q14. What happens at MOUNT?

**Short answer:** The instance opens the control file but not normal datafiles for database access.

### Q15. What happens at OPEN?

**Short answer:** Datafiles/redo are opened and the database becomes available according to open mode.

### Q16. PFILE vs SPFILE?

**Short answer:** PFILE is a text initialization file; SPFILE is Oracle-managed server parameter storage.

### Q17. What does `SCOPE=BOTH` mean conceptually?

**Short answer:** Apply a supported parameter change now and persist it for future startup.

### Q18. What is the listener?

**Short answer:** Oracle Net process accepting initial client connection requests for registered services.

### Q19. What default TCP port is commonly used by Oracle listener?

**Short answer:** 1521.

### Q20. What should applications connect to in a PDB environment?

**Short answer:** An appropriate database service associated with the PDB.

### Q21. What is a tablespace?

**Short answer:** A logical storage container backed by database files.

### Q22. What is a segment?

**Short answer:** Storage allocated to a schema object such as a table or index.

### Q23. What is undo used for?

**Short answer:** Rollback, read consistency, and related recovery/flashback functionality.

### Q24. What is redo?

**Short answer:** Recovery information describing database changes.

### Q25. What is ARCHIVELOG mode?

**Short answer:** A mode where completed online redo is archived to support stronger recovery capabilities.

### Q26. What is the FRA?

**Short answer:** Oracle-managed recovery storage for files such as archived logs, backups, and flashback logs.

### Q27. What do `V$` views show?

**Short answer:** Dynamic live database/instance state and performance information.

### Q28. What is ADR?

**Short answer:** Automatic Diagnostic Repository containing alert, trace, incident, and diagnostic data.

### Q29. Why should you check the current container first?

**Short answer:** Administrative SQL may have different scope/effect in root vs a PDB.

### Q30. What auditing model is the forward path in Oracle AI Database 26ai?

**Short answer:** Unified auditing.

---

# Enhanced Self-Assessment Bank

### Q1. Instance vs database?
**Answer:** Instance is memory/process state; database is persistent files/structures.

### Q2. What proves NOMOUNT succeeded?
**Answer:** Parameters were read, SGA allocated, and background processes started.

### Q3. What additional dependency is needed for MOUNT?
**Answer:** The control file.

### Q4. What additional dependencies are needed for OPEN?
**Answer:** Required datafiles, redo, and valid recovery state.

### Q5. Why use restricted session?
**Answer:** To limit normal logins during controlled maintenance.

### Q6. What does READ ONLY PDB mean?
**Answer:** Queries can work while normal writes are blocked.

### Q7. What is an SCN?
**Answer:** Oracle's logical database change-order marker used for consistency/recovery.

### Q8. Commit vs checkpoint?
**Answer:** Commit relies on redo durability; checkpoint advances recovery metadata and dirty-buffer writing.

### Q9. What is instance recovery?
**Answer:** Automatic redo roll-forward and undo of uncommitted work after instance failure.

### Q10. SGA vs PGA?
**Answer:** SGA is shared instance memory; PGA is process/session-private work memory.

### Q11. What is the buffer cache?
**Answer:** Memory caching database blocks.

### Q12. What is the shared pool?
**Answer:** Shared SQL/PLSQL and metadata cache.

### Q13. What is the large pool?
**Answer:** Separate SGA area for selected large allocations/workloads.

### Q14. Why does TEMP relate to PGA?
**Answer:** Large work areas can spill from PGA to temporary storage.

### Q15. Dedicated vs shared server?
**Answer:** One server process per session vs multiplexed sessions through dispatchers/shared servers.

### Q16. How map session to OS PID?
**Answer:** Join V$SESSION to V$PROCESS through PADDR/ADDR.

### Q17. LGWR?
**Answer:** Writes redo to online redo logs.

### Q18. DBWn?
**Answer:** Writes dirty data blocks to datafiles.

### Q19. ARCn?
**Answer:** Archives completed redo in ARCHIVELOG mode.

### Q20. What does CKPT coordinate?
**Answer:** Checkpoint metadata/file-header/control-file progress.

### Q21. Why multiplex control files?
**Answer:** Reduce single-copy media-loss risk.

### Q22. Redo group vs member?
**Answer:** Group is logical log; members are multiplexed physical copies.

### Q23. Why review redo switch history?
**Answer:** To size/monitor redo from real workload.

### Q24. Why never manually rm archive logs?
**Answer:** It can break recovery/RMAN metadata and create gaps.

### Q25. What is FRA?
**Answer:** Oracle-managed recovery-file storage with a configured quota.

### Q26. Datafile header relevance?
**Answer:** Contains checkpoint/state information used for consistency/open/recovery.

### Q27. Smallfile vs bigfile?
**Answer:** Many normal datafiles vs one very large datafile per tablespace.

### Q28. Locally managed tablespace?
**Answer:** Extent allocation metadata is maintained locally in the tablespace.

### Q29. ASSM?
**Answer:** Automatic bitmap-based segment free-space management.

### Q30. OMF?
**Answer:** Oracle-managed file naming/creation under configured destinations.

### Q31. ASM?
**Answer:** Oracle database-aware storage management using disk groups.

### Q32. Why is autoextend not infinite?
**Answer:** MAXSIZE and physical storage still limit growth.

### Q33. What is a TEMP tablespace group?
**Answer:** Multiple temporary tablespaces grouped for temp workload distribution.

### Q34. Undo purpose?
**Answer:** Rollback, read consistency, transaction recovery support, and flashback-related history.

### Q35. Undo retention?
**Answer:** Target time to preserve old undo versions when space/workload permit.

### Q36. What can cause ORA-01555?
**Answer:** A query needs an old version whose undo has been reused.

### Q37. What is CON_ID?
**Answer:** Multitenant container identifier.

### Q38. Common vs local user?
**Answer:** Common spans configured CDB scope; local belongs to one PDB.

### Q39. Why save PDB state?
**Answer:** To preserve desired open state across CDB restarts.

### Q40. What is PDB unplug/plug?
**Answer:** Portable PDB lifecycle/migration mechanism.

### Q41. Why is a PDB clone a security event?
**Answer:** It can duplicate sensitive production data.

### Q42. Why connect through services?
**Answer:** Services abstract workload/PDB identity from physical instances/hosts.

### Q43. What is dynamic listener registration?
**Answer:** The database registers its services with the listener.

### Q44. LOCAL_LISTENER?
**Answer:** Parameter/alias telling the instance where to register locally when defaults are insufficient.

### Q45. What is TNS_ADMIN?
**Answer:** Environment/config location override for Oracle Net files.

### Q46. Does listener success prove DB authentication?
**Answer:** No.

### Q47. What is SYSDBA?
**Answer:** Powerful administrative authentication/privilege mode.

### Q48. Why protect password file?
**Answer:** It enables high-privilege administrative authentication.

### Q49. Role vs direct grant for definer code?
**Answer:** Stored code often needs direct privileges on referenced objects.

### Q50. Default role?
**Answer:** A granted role automatically enabled for ordinary session use.

### Q51. Quota?
**Answer:** Storage allocation limit for a user on a tablespace.

### Q52. Schema owner vs tablespace?
**Answer:** Ownership is security/logical; tablespace is physical storage placement.

### Q53. Why inspect largest segments?
**Answer:** To identify what actually drives space growth.

### Q54. Why inspect DBA_LOBS?
**Answer:** LOB data can consume separate large segments.

### Q55. Does DELETE always shrink segment allocation?
**Answer:** No.

### Q56. Why can a datafile shrink fail?
**Answer:** Allocated extents exist beyond the requested new size.

### Q57. Why include CON_ID in file reports?
**Answer:** To identify which PDB owns the file.

### Q58. What is end-to-end DB health?
**Answer:** Successful application-like service connection to the expected PDB/open mode plus SQL.

### Q59. DBA_* vs V$?
**Answer:** Persistent metadata vs current runtime state.

### Q60. GV$ vs V$?
**Answer:** Global/all-instance runtime view vs local-instance view.

### Q61. ACTIVE session means healthy?
**Answer:** No; it only indicates current call activity.

### Q62. Why inspect V$TRANSACTION?
**Answer:** To find sessions with open transactions, undo, and locks.

### Q63. Root blocker?
**Answer:** The session at the top of a waiting chain.

### Q64. Why use SID+SERIAL# when killing?
**Answer:** To identify the exact session incarnation.

### Q65. Enabled scheduler job means successful?
**Answer:** No; inspect run history.

### Q66. What is unified auditing?
**Answer:** Policy-based consolidated Oracle audit trail architecture.

### Q67. Why manage audit retention?
**Answer:** Audit data consumes storage and must satisfy security/compliance evidence needs.

### Q68. What is ADR?
**Answer:** Automatic Diagnostic Repository for Oracle diagnostics.

### Q69. Why is alert log important?
**Answer:** It provides a chronological operational/error timeline.

### Q70. What are trace files?
**Answer:** Detailed process/session diagnostic files.

### Q71. Why export a PFILE from SPFILE?
**Answer:** For human-readable review/recovery evidence.

### Q72. Why record parameter modifiability?
**Answer:** To know whether changes can apply now, later, or require restart.

### Q73. Why avoid underscore parameters?
**Answer:** They are internal and should not be changed casually.

### Q74. Why is character set architectural?
**Answer:** It affects persistent text storage and interoperability.

### Q75. DBTIMEZONE vs SESSIONTIMEZONE?
**Answer:** Database timezone setting vs current session timezone.

### Q76. Why have default TEMP/permanent tablespaces?
**Answer:** To avoid accidental use of inappropriate system storage.

### Q77. What can an open-cursor leak cause?
**Answer:** Sessions approach OPEN_CURSORS and consume cursor resources.

### Q78. Why not only raise PROCESSES after connection errors?
**Answer:** The root cause may be connection storms/leaks or capacity.

### Q79. What does tnsping prove?
**Answer:** Naming/listener path reachability, not user authentication or SQL success.

### Q80. Why use OS authentication locally?
**Answer:** It can avoid embedding highly privileged DB passwords when host trust permits.

### Q81. Why separate admin identities?
**Answer:** Better least privilege and attribution.

### Q82. What is recycle bin?
**Answer:** Retention area for eligible dropped objects that can support Flashback Drop.

### Q83. What is deferred segment creation?
**Answer:** Metadata object can exist before physical segment allocation.

### Q84. Why monitor OS filesystem too?
**Answer:** Database autoextend depends on underlying storage.

### Q85. Why monitor host time?
**Answer:** Accurate time supports logs, certificates, HA, and incident correlation.

### Q86. Why avoid swap pressure?
**Answer:** Paging Oracle memory can severely degrade response time.

### Q87. What is HugePages awareness for?
**Answer:** Reducing page-table overhead for large SGA deployments on supported Linux configurations.

### Q88. What belongs in Oracle inventory?
**Answer:** Homes/patches, DB/PDB, services, listener, parameters, files, FRA, and platform details.

### Q89. What should daily health automation do?
**Answer:** Collect evidence and alert, not perform blind destructive remediation.

### Q90. Why trend capacity?
**Answer:** Forecast exhaustion before an emergency threshold.

### Q91. What makes a good runbook?
**Answer:** Prerequisites, exact target, commands, evidence, validation, rollback, and escalation.


## Completion Checklist

- [ ] I can explain instance vs database.
- [ ] I can explain CDB/PDB architecture.
- [ ] I understand SGA and PGA.
- [ ] I understand LGWR, DBWn, CKPT, ARC, and monitoring processes.
- [ ] I can identify Oracle physical and logical storage structures.
- [ ] I can start/stop the database in appropriate modes.
- [ ] I can work with PFILE/SPFILE safely.
- [ ] I can inspect/change appropriate initialization parameters.
- [ ] I can troubleshoot listener/service connections.
- [ ] I can create users, roles, quotas, and profiles.
- [ ] I can create/manage basic tablespaces.
- [ ] I understand TEMP and UNDO.
- [ ] I understand redo groups, log switches, and checkpoints.
- [ ] I can explain ARCHIVELOG and FRA.
- [ ] I can manage PDB open state.
- [ ] I can use dictionary and V$ views.
- [ ] I can investigate sessions and blockers.
- [ ] I can use alert-log/ADR evidence.
- [ ] I understand unified auditing foundations.
- [ ] I completed all labs.
- [ ] I completed the MANUCDB/MANUPDB administration mini project.
