# 1. Topic Title

## Database Fundamentals

A database is not simply a file that stores rows. A database system is a controlled environment for representing business facts, preserving relationships, enforcing rules, answering questions efficiently, coordinating concurrent users, recovering from failure, and protecting data.

A useful mental model is:

```text
Applications / Analysts / Administrators
                ↓
             SQL / API
                ↓
            Database DBMS
     ┌──────────┼──────────┐
     ↓          ↓          ↓
   Parser    Optimizer   Transaction Manager
     ↓          ↓          ↓
   Executor  Indexes     Locks / MVCC
     └──────────┼──────────┘
                ↓
        Tables / Pages / Logs
                ↓
        Durable Storage
```

This module starts from the relational model and builds toward practical SQL, schema design, integrity, indexes, transactions, concurrency, backup/recovery, access control, and application safety.

The purpose is to make later MySQL, Oracle, NoSQL, cloud database, backend, and cybersecurity topics easier because you understand *why* database systems behave the way they do, not only the syntax of `SELECT`.

# 2. Learning Objectives

1. Distinguish data, database, DBMS, database engine, schema, and query language.
2. Explain the relational model using tables, rows, columns, domains, and keys.
3. Translate business requirements into entities, attributes, and relationships.
4. Design one-to-one, one-to-many, and many-to-many relationships.
5. Use primary keys, foreign keys, unique constraints, check constraints, and NOT NULL.
6. Explain candidate, natural, surrogate, composite, and alternate keys.
7. Apply 1NF, 2NF, and 3NF conceptually to remove harmful duplication.
8. Recognize insertion, update, and deletion anomalies.
9. Create tables using portable SQL.
10. Perform CRUD operations safely.
11. Use WHERE, ORDER BY, DISTINCT, aliases, expressions, and NULL-aware predicates.
12. Use INNER, LEFT, self, and multi-table joins.
13. Use GROUP BY, HAVING, COUNT, SUM, AVG, MIN, and MAX.
14. Explain subqueries and common table expression awareness.
15. Explain views and why they are useful.
16. Explain indexes, B-tree concepts, selectivity, composite indexes, and write trade-offs.
17. Read a basic query plan conceptually.
18. Explain transactions and ACID.
19. Use BEGIN, COMMIT, ROLLBACK, and savepoint awareness.
20. Explain lost updates, dirty reads, non-repeatable reads, and phantom reads conceptually.
21. Explain isolation levels and locking/MVCC at a foundational level.
22. Explain deadlocks and why they occur.
23. Explain database connection and session concepts.
24. Use parameterized queries from Python instead of SQL string concatenation.
25. Explain SQL injection at a defensive level.
26. Apply least privilege to database users and application accounts.
27. Explain backup, restore, dump, replication awareness, RPO, and RTO.
28. Explain transaction logs / write-ahead logging conceptually.
29. Explain durability versus availability.
30. Explain data types and why type selection matters.
31. Explain NULL semantics and three-valued logic awareness.
32. Explain schema migrations at a foundational level.
33. Build a normalized IT Asset and Incident database with practical queries.

# 3. Prerequisites

Recommended:

```text
03. Introduction to Programming
01. Operating Systems Fundamentals
```

Helpful concepts:

```text
Files
Processes
Permissions
Basic Python
Input validation
Basic networking
```

For hands-on work choose **one** engine and stay with it during the course:

```text
PostgreSQL
MySQL
or SQLite for the simplest local lab
```

Examples are written in broadly portable SQL. Engine-specific auto-increment, user-management, backup, and transaction behavior may differ.

# 4. Core Concepts Explanation

# Part 1 — Data, Information, and Persistence

### Core Explanation

Data is a representation of facts. Information is data interpreted in context. Persistence means the information survives beyond one process execution.

A Python variable disappears when the process ends. A database is designed to preserve application state durably and make it queryable.

### Diagram / Mental Model

```text
Process memory:
server_status = "critical"
        ↓ process exits
      value gone

Database:
server_status row
        ↓ restart application
      value still available
```

### Why It Matters

This distinction explains why backend applications need a persistence layer.

### Practical Use

Use databases for durable system state; use process memory for temporary computation.

# Part 2 — Database vs DBMS

### Core Explanation

A **database** is the organized data. A **DBMS** is the software that stores, retrieves, validates, protects, and coordinates access to that data.

### Diagram / Mental Model

```text
Users / Apps
     ↓
    DBMS
     ↓
 Database files / pages / logs
```

### Why It Matters

Saying 'PostgreSQL database' can refer to both the managed data and the DBMS ecosystem, but conceptually they are different.

### Practical Use

PostgreSQL, MySQL, Oracle Database, and SQLite are DBMS technologies.

# Part 3 — Database Engine

### Core Explanation

The database engine is the core subsystem that parses statements, chooses execution strategies, manages transactions, reads/writes storage, and enforces constraints.

### Diagram / Mental Model

```text
SQL
 ↓
Parser
 ↓
Planner / Optimizer
 ↓
Executor
 ↓
Buffer / Storage / Transaction subsystems
```

### Why It Matters

SQL is declarative: you specify what result you want; the engine decides how to obtain it.

### Practical Use

Query optimization later depends on understanding this separation.

# Part 4 — Relational Model

### Core Explanation

The relational model represents information as relations. In practical SQL systems, relations are exposed primarily as tables composed of rows and columns.

### Diagram / Mental Model

```text
servers
+----+----------+-------------+
| id | hostname | environment |
+----+----------+-------------+
| 1  | web-01   | production  |
| 2  | db-01    | production  |
+----+----------+-------------+
```

### Why It Matters

The model makes data structure explicit and supports mathematical relational operations such as selection, projection, and joins.

### Practical Use

Most enterprise transactional systems use relational databases for strongly structured data.

# Part 5 — Table, Row, and Column

### Core Explanation

A table models one type of entity or relationship. A row represents one record. A column represents one attribute with a defined data type/domain.

### Diagram / Mental Model

```text
Table: servers
Row: one server
Columns:
id
hostname
ip_address
environment
```

### Why It Matters

Clear table responsibility prevents mixing unrelated facts.

### Practical Use

Model `servers`, `teams`, and `incidents` as separate tables rather than one repeated spreadsheet.

# Part 6 — Schema

### Core Explanation

A schema is the structural definition of database objects: tables, columns, data types, constraints, indexes, views, and sometimes functions/procedures depending on DBMS terminology.

### Diagram / Mental Model

```text
Schema
├─ teams
├─ servers
├─ incidents
├─ indexes
└─ views
```

### Why It Matters

The schema is effectively a contract for stored data.

### Practical Use

Version schema changes alongside application releases.

# Part 7 — Data Type

### Core Explanation

A data type constrains the kind of values a column can store and affects validation, storage, comparison, indexing, and query semantics.

### Example / Code

```sql
CREATE TABLE metrics (
    id INTEGER PRIMARY KEY,
    cpu_percent DECIMAL(5,2) NOT NULL,
    sample_time TIMESTAMP NOT NULL
);
```

### Why It Matters

Storing numeric data as text weakens validation and makes sorting/calculation harder.

### Practical Use

Choose numeric types for numbers, dates/timestamps for time, and text for genuine text.

# Part 8 — VARCHAR and Text

### Core Explanation

Character types store text. `VARCHAR(n)` may express a maximum length, while unbounded text types differ by DBMS. Length should represent a real domain constraint rather than arbitrary habit.

### Example / Code

```sql
hostname VARCHAR(100) NOT NULL
```

### Why It Matters

Data types document expected values and can reject invalid data.

### Practical Use

Use realistic constraints for hostnames, status values, names, and identifiers.

# Part 9 — Integer Types

### Core Explanation

Integer types store whole-number values. DBMSs often provide small, normal, and large integer ranges.

### Example / Code

```sql
id INTEGER PRIMARY KEY
retry_count INTEGER NOT NULL
```

### Why It Matters

Use integer types for counts and numeric identifiers when appropriate.

### Practical Use

Do not store ports or counters as arbitrary strings unless there is a domain reason.

# Part 10 — Decimal vs Floating-Point Awareness

### Core Explanation

Exact decimal types are preferred when exact decimal arithmetic is required. Floating-point values are approximate binary representations.

### Example / Code

```sql
amount DECIMAL(12,2)
```

### Why It Matters

Financial and exact business values should not silently accumulate floating-point approximation.

### Practical Use

For CPU percentages either may be acceptable depending on requirements; money usually needs exact decimal semantics.

# Part 11 — Date and Time Awareness

### Core Explanation

Databases provide dedicated date/time types. Timestamps may have timezone-related semantics that vary by DBMS.

### Example / Code

```sql
created_at TIMESTAMP NOT NULL
```

### Why It Matters

Dates stored as arbitrary text are harder to validate, sort, filter, and calculate.

### Practical Use

Define a consistent timezone strategy for distributed systems.

# Part 12 — NULL

### Core Explanation

`NULL` represents missing, unknown, or not-applicable information. It is not the same as zero, an empty string, or False.

### Example / Code

```sql
SELECT *
FROM servers
WHERE team_id IS NULL;
```

### Why It Matters

SQL uses special NULL semantics. `team_id = NULL` is not the correct predicate.

### Practical Use

Use `IS NULL` and `IS NOT NULL`.

# Part 13 — Three-Valued Logic Awareness

### Core Explanation

Because NULL represents unknown, SQL predicates may evaluate to TRUE, FALSE, or UNKNOWN. Rows are returned by `WHERE` only when the predicate is TRUE.

### Diagram / Mental Model

```text
value = 5      → known comparison
value = NULL   → comparison may be UNKNOWN
```

### Why It Matters

NULL can change filtering and join behavior in ways that surprise beginners.

### Practical Use

Be explicit about whether columns may be NULL.

# Part 14 — Primary Key

### Core Explanation

A primary key uniquely identifies each row and must be unique and non-null.

### Example / Code

```sql
CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

### Why It Matters

Stable identity allows reliable references even when descriptive attributes change.

### Practical Use

Avoid using changeable names as the only identity when a stable key is better.

# Part 15 — Candidate Key

### Core Explanation

A candidate key is any minimal set of attributes that can uniquely identify a row. One candidate is chosen as primary key; others may be enforced with UNIQUE constraints.

### Diagram / Mental Model

```text
servers:
id           candidate
hostname     candidate if globally unique

Primary chosen:
id

Alternate:
hostname UNIQUE
```

### Why It Matters

Thinking in candidate keys improves integrity design.

# Part 16 — Natural Key

### Core Explanation

A natural key comes from the business domain, such as a globally unique asset tag or ISO code.

### Example / Code

```sql
asset_tag VARCHAR(50) UNIQUE NOT NULL
```

### Why It Matters

Natural keys can be meaningful but may change or have complicated formats.

### Practical Use

Use when the business identifier is truly stable and unique.

# Part 17 — Surrogate Key

### Core Explanation

A surrogate key is an artificial identifier such as an integer or UUID used primarily for row identity.

### Example / Code

```sql
id INTEGER PRIMARY KEY
```

### Why It Matters

It decouples row identity from changeable business attributes.

### Practical Use

Common in application schemas.

# Part 18 — Composite Key

### Core Explanation

A composite key uses multiple columns together for uniqueness.

### Example / Code

```sql
CREATE TABLE user_roles (
    user_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, role_id)
);
```

### Why It Matters

Association tables often naturally use composite keys.

### Practical Use

Prevents the same relationship being inserted twice.

# Part 19 — Foreign Key

### Core Explanation

A foreign key constrains a column to reference an existing key in another table.

### Example / Code

```sql
team_id INTEGER,
FOREIGN KEY (team_id) REFERENCES teams(id)
```

### Why It Matters

It prevents orphan references and preserves referential integrity.

### Practical Use

Use for relationships between entities.

# Part 20 — One-to-Many Relationship

### Core Explanation

One parent row can relate to many child rows.

### Diagram / Mental Model

```text
Team 1
  │
  ├── Server A
  ├── Server B
  └── Server C
```

### Example / Code

```sql
servers.team_id → teams.id
```

### Why It Matters

This is one of the most common relational patterns.

# Part 21 — One-to-One Relationship

### Core Explanation

One row corresponds to at most one row in another table. It is often enforced with a foreign key plus UNIQUE.

### Example / Code

```sql
CREATE TABLE server_secrets_metadata (
    server_id INTEGER UNIQUE NOT NULL,
    ...
);
```

### Why It Matters

One-to-one should be justified; sometimes the columns belong in the same table.

### Practical Use

Useful when separating optional/security-sensitive metadata.

# Part 22 — Many-to-Many Relationship

### Core Explanation

Many rows in A can relate to many rows in B. A junction table represents the relationships.

### Diagram / Mental Model

```text
Applications        Servers
 App A ─────────── Server 1
 App A ─────────── Server 2
 App B ─────────── Server 2
```

### Example / Code

```sql
CREATE TABLE application_servers (
    application_id INTEGER NOT NULL,
    server_id INTEGER NOT NULL,
    PRIMARY KEY (application_id, server_id)
);
```

### Why It Matters

Trying to store many IDs in one comma-separated column breaks relational querying and integrity.

# Part 23 — Referential Actions Awareness

### Core Explanation

Foreign keys can define behavior when referenced rows change or are deleted, such as RESTRICT/NO ACTION, CASCADE, or SET NULL depending on DBMS.

### Example / Code

```sql
FOREIGN KEY (team_id)
REFERENCES teams(id)
ON DELETE SET NULL
```

### Why It Matters

Delete behavior is a business rule, not merely a technical option.

### Practical Use

Avoid cascading deletes until you understand the full impact.

# Part 24 — NOT NULL

### Core Explanation

`NOT NULL` states that a value is required.

### Example / Code

```sql
hostname VARCHAR(100) NOT NULL
```

### Why It Matters

Application validation alone cannot protect against every writer to the database.

# Part 25 — UNIQUE

### Core Explanation

`UNIQUE` prevents duplicate values or combinations.

### Example / Code

```sql
hostname VARCHAR(100) NOT NULL UNIQUE
```

### Why It Matters

Useful for natural business uniqueness rules.

# Part 26 — CHECK Constraint

### Core Explanation

A CHECK constraint validates a predicate for each row.

### Example / Code

```sql
cpu_percent DECIMAL(5,2)
CHECK (cpu_percent >= 0 AND cpu_percent <= 100)
```

### Why It Matters

The database can reject invalid percentages even if application code contains a bug.

# Part 27 — Constraint as Data Integrity Layer

### Core Explanation

Constraints act as the final shared enforcement point for every application, script, migration, and administrator writing data.

### Diagram / Mental Model

```text
App A ─┐
App B ─┼→ Database Constraints → Valid State
Admin ─┘
```

### Why It Matters

Critical invariants should not exist only in one application.

# Part 28 — Data Redundancy

### Core Explanation

Redundancy means the same fact is repeated unnecessarily in many rows.

### Diagram / Mental Model

```text
incident rows repeatedly store:
server_hostname
server_ip
server_owner
```

### Why It Matters

Repeated facts can diverge and require many coordinated updates.

# Part 29 — Update Anomaly

### Core Explanation

An update anomaly occurs when one fact is stored in multiple places and only some copies are updated.

### Diagram / Mental Model

```text
web-01 IP changes:
row 1 → updated
row 2 → old IP
row 3 → old IP
```

### Why It Matters

The database now contains contradictory facts.

# Part 30 — Insertion Anomaly

### Core Explanation

An insertion anomaly occurs when you cannot store one fact without inventing unrelated data.

### Why It Matters

Poor table design couples independent entities.

# Part 31 — Deletion Anomaly

### Core Explanation

A deletion anomaly occurs when deleting one fact accidentally removes the only copy of another fact.

### Why It Matters

Separating entities prevents accidental information loss.

# Part 32 — First Normal Form — Conceptual

### Core Explanation

1NF requires table values to be atomic in the relational sense and avoids repeating groups in one row.

### Diagram / Mental Model

```text
Poor:
server | ports
web-01 | 80,443,8080

Better:
server_ports
web-01 | 80
web-01 | 443
web-01 | 8080
```

### Why It Matters

Multi-valued columns make joins, validation, and indexing difficult.

# Part 33 — Second Normal Form — Conceptual

### Core Explanation

2NF addresses partial dependency on part of a composite key. Non-key facts should depend on the complete key.

### Why It Matters

This matters most when tables use composite keys.

### Practical Use

At fundamentals level, focus on whether a fact belongs to the relationship as a whole.

# Part 34 — Third Normal Form — Conceptual

### Core Explanation

3NF aims to prevent non-key columns from depending on other non-key columns when those facts belong to separate entities.

### Diagram / Mental Model

```text
Poor:
servers(id, hostname, team_id, team_name)

Better:
servers(id, hostname, team_id)
teams(id, team_name)
```

### Why It Matters

Team name is a fact about the team, not about each server row.

# Part 35 — Denormalization Awareness

### Core Explanation

Denormalization intentionally duplicates or precomputes data to improve particular read patterns, at the cost of consistency complexity.

### Why It Matters

Normalization is not a religion; production systems make measured trade-offs.

### Practical Use

Normalize first. Denormalize only for a proven reason and define synchronization rules.

# Part 36 — SQL Is Declarative

### Core Explanation

SQL generally states *what* result is required, not the exact physical algorithm.

### Example / Code

```sql
SELECT hostname
FROM servers
WHERE environment = 'production';
```

### Why It Matters

The optimizer may choose an index scan, table scan, join order, or other plan.

# Part 37 — DDL

### Core Explanation

Data Definition Language statements define database objects.

### Example / Code

```sql
CREATE TABLE ...
ALTER TABLE ...
DROP TABLE ...
```

### Why It Matters

Schema changes can be destructive and should be versioned/reviewed.

# Part 38 — DML

### Core Explanation

Data Manipulation Language modifies data.

### Example / Code

```sql
INSERT
UPDATE
DELETE
```

### Why It Matters

These operations can affect business state and should often run within transactions.

# Part 39 — SELECT

### Core Explanation

`SELECT` retrieves rows and expressions.

### Example / Code

```sql
SELECT hostname, ip_address
FROM servers;
```

### Expected Result / Behavior

```text
hostname | ip_address
web-01   | 10.0.0.10
db-01    | 10.0.0.20
```

### Practical Use

Select only columns you need in application queries.

# Part 40 — WHERE

### Core Explanation

`WHERE` filters rows before projection/aggregation stages conceptually.

### Example / Code

```sql
SELECT *
FROM servers
WHERE environment = 'production';
```

### Why It Matters

Correct predicates are essential for both performance and safe data modification.

# Part 41 — ORDER BY

### Core Explanation

`ORDER BY` defines result ordering.

### Example / Code

```sql
SELECT hostname
FROM servers
ORDER BY hostname ASC;
```

### Why It Matters

Without ORDER BY, row order should not be assumed.

### Practical Use

Always specify ordering when business behavior depends on it.

# Part 42 — DISTINCT

### Core Explanation

`DISTINCT` removes duplicate result rows.

### Example / Code

```sql
SELECT DISTINCT environment
FROM servers;
```

### Why It Matters

Useful for query results, but should not be used to hide a flawed join that accidentally multiplies rows.

# Part 43 — Aliases

### Core Explanation

Aliases make queries readable and disambiguate repeated column names.

### Example / Code

```sql
SELECT s.hostname, t.name AS team_name
FROM servers AS s
JOIN teams AS t ON t.id = s.team_id;
```

# Part 44 — INSERT

### Core Explanation

`INSERT` creates rows.

### Example / Code

```sql
INSERT INTO servers
(id, hostname, ip_address, environment, team_id)
VALUES
(1, 'web-01', '10.0.0.10', 'production', 1);
```

### Why It Matters

Explicit column lists make inserts safer against schema changes.

# Part 45 — Multi-Row INSERT

### Core Explanation

Many DBMSs support multiple rows in one INSERT statement.

### Example / Code

```sql
INSERT INTO teams (id, name) VALUES
(1, 'Platform'),
(2, 'Data');
```

### Why It Matters

More efficient and readable for seed/sample data.

# Part 46 — UPDATE

### Core Explanation

`UPDATE` changes existing rows.

### Example / Code

```sql
UPDATE servers
SET environment = 'staging'
WHERE id = 1;
```

### Why It Matters

The WHERE clause controls scope.

### Troubleshooting / Common Failure

Before a destructive UPDATE, run a SELECT with the same WHERE predicate and confirm the exact rows.

# Part 47 — DELETE

### Core Explanation

`DELETE` removes rows.

### Example / Code

```sql
DELETE FROM incidents
WHERE id = 100;
```

### Why It Matters

Without the intended WHERE condition, many or all rows can be removed.

### Troubleshooting / Common Failure

Use a transaction and verify selected rows before committing destructive changes.

# Part 48 — CRUD Mapping

### Core Explanation

CRUD maps application operations to SQL concepts.

### Diagram / Mental Model

```text
Create → INSERT
Read   → SELECT
Update → UPDATE
Delete → DELETE
```

### Why It Matters

This provides a simple mental bridge from application behavior to data operations.

# Part 49 — INNER JOIN

### Core Explanation

An INNER JOIN returns rows where the join condition matches on both sides.

### Example / Code

```sql
SELECT s.hostname, i.severity
FROM servers AS s
JOIN incidents AS i
  ON i.server_id = s.id;
```

### Why It Matters

Use when only related records should appear.

# Part 50 — LEFT JOIN

### Core Explanation

A LEFT JOIN preserves every row from the left side and returns NULL columns for missing matches.

### Example / Code

```sql
SELECT s.hostname, i.id AS incident_id
FROM servers AS s
LEFT JOIN incidents AS i
  ON i.server_id = s.id;
```

### Why It Matters

Essential when asking 'which servers have no incidents?'

# Part 51 — Finding Missing Relationships

### Core Explanation

A common anti-join pattern uses LEFT JOIN plus `IS NULL`.

### Example / Code

```sql
SELECT s.hostname
FROM servers AS s
LEFT JOIN incidents AS i
  ON i.server_id = s.id
WHERE i.id IS NULL;
```

### Why It Matters

Useful for 'without' questions.

# Part 52 — Multi-Table Join

### Core Explanation

Joins can follow relationships across several tables.

### Example / Code

```sql
SELECT s.hostname, t.name AS team, i.severity
FROM incidents AS i
JOIN servers AS s ON s.id = i.server_id
JOIN teams AS t ON t.id = s.team_id;
```

### Why It Matters

Foreign keys define the logical paths between entities.

# Part 53 — Join Multiplication

### Core Explanation

A one-to-many join repeats the parent row for every matching child.

### Diagram / Mental Model

```text
server web-01
 incidents: 3
 join result:
 web-01 | incident1
 web-01 | incident2
 web-01 | incident3
```

### Why It Matters

This is correct relational behavior, but can inflate counts if you aggregate carelessly.

# Part 54 — Self Join Awareness

### Core Explanation

A table can be joined to itself when rows reference other rows of the same entity type.

### Example / Code

```sql
-- conceptual employee-manager pattern
SELECT e.name, m.name AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;
```

### Why It Matters

Useful for hierarchies.

# Part 55 — COUNT

### Core Explanation

`COUNT` counts rows or non-null values depending on expression.

### Example / Code

```sql
SELECT COUNT(*) AS server_count
FROM servers;
```

### Why It Matters

`COUNT(*)` counts rows; `COUNT(column)` ignores NULL values.

# Part 56 — GROUP BY

### Core Explanation

`GROUP BY` groups rows before aggregate calculation.

### Example / Code

```sql
SELECT severity, COUNT(*) AS incident_count
FROM incidents
GROUP BY severity;
```

### Why It Matters

Answers questions per category rather than for the entire table.

# Part 57 — HAVING

### Core Explanation

`HAVING` filters grouped results, while WHERE filters rows before grouping.

### Example / Code

```sql
SELECT server_id, COUNT(*) AS incident_count
FROM incidents
GROUP BY server_id
HAVING COUNT(*) >= 2;
```

### Why It Matters

Use HAVING for aggregate predicates.

# Part 58 — SUM and AVG

### Core Explanation

`SUM` totals numeric values; `AVG` calculates an average over non-null values.

### Example / Code

```sql
SELECT
    AVG(cpu_percent) AS avg_cpu,
    MAX(cpu_percent) AS peak_cpu
FROM server_metrics;
```

# Part 59 — MIN and MAX

### Core Explanation

`MIN` and `MAX` return smallest/largest values according to type semantics.

### Example / Code

```sql
SELECT MIN(created_at), MAX(created_at)
FROM incidents;
```

# Part 60 — Subquery Awareness

### Core Explanation

A subquery is a query nested inside another statement.

### Example / Code

```sql
SELECT hostname
FROM servers
WHERE id IN (
    SELECT server_id
    FROM incidents
    WHERE severity = 'critical'
);
```

### Why It Matters

Useful, although a join may sometimes be clearer or faster depending on the query and engine.

# Part 61 — Common Table Expression Awareness

### Core Explanation

A CTE names an intermediate query using `WITH`.

### Example / Code

```sql
WITH critical_incidents AS (
    SELECT server_id
    FROM incidents
    WHERE severity = 'critical'
)
SELECT s.hostname
FROM servers s
JOIN critical_incidents c ON c.server_id = s.id;
```

### Why It Matters

Improves readability for multi-step queries.

# Part 62 — View

### Core Explanation

A view stores a query definition and exposes it like a virtual table.

### Example / Code

```sql
CREATE VIEW production_servers AS
SELECT id, hostname, ip_address
FROM servers
WHERE environment = 'production';
```

### Why It Matters

Views can simplify repeated queries and provide controlled data exposure.

# Part 63 — Index

### Core Explanation

An index is an auxiliary structure that accelerates selected lookup and ordering patterns.

### Diagram / Mental Model

```text
Table rows
  ↓
B-tree-like index
  ├─ key A → row location
  ├─ key B → row location
  └─ key C → row location
```

### Example / Code

```sql
CREATE INDEX idx_incidents_server_id
ON incidents(server_id);
```

### Why It Matters

Indexes reduce search work for suitable predicates and joins.

# Part 64 — B-Tree Concept

### Core Explanation

Many relational indexes use balanced tree structures that keep keys ordered and support equality and range searches efficiently.

### Diagram / Mental Model

```text
[50]
    /    \
[10 20] [70 90]
   ↓       ↓
row refs  row refs
```

### Why It Matters

The tree avoids scanning every row for many lookup patterns.

# Part 65 — Index Trade-Off

### Core Explanation

Indexes improve selected reads but consume storage and must be maintained when rows change.

### Diagram / Mental Model

```text
More indexes
  + faster some reads
  - slower writes
  - more storage
  - more maintenance
```

### Why It Matters

Do not index every column automatically.

# Part 66 — Selectivity

### Core Explanation

Selectivity describes how narrowly a predicate identifies rows. Highly selective columns often benefit more from indexes than columns with very few distinct values.

### Diagram / Mental Model

```text
hostname:
millions of unique values → high selectivity

environment:
production/staging/dev → low selectivity
```

### Why It Matters

The optimizer considers statistics and expected row counts, not only whether an index exists.

# Part 67 — Composite Index

### Core Explanation

A composite index contains multiple columns in a defined order.

### Example / Code

```sql
CREATE INDEX idx_incident_server_severity
ON incidents(server_id, severity);
```

### Why It Matters

Column order matters because common B-tree access patterns use leading index columns.

# Part 68 — Query Plan Awareness

### Core Explanation

A query plan describes the strategy chosen by the optimizer: scans, joins, index use, estimated rows, and costs.

### Example / Code

```sql
EXPLAIN
SELECT *
FROM incidents
WHERE server_id = 10;
```

### Why It Matters

You optimize evidence from plans and measurements, not guesswork.

### Practical Use

Exact EXPLAIN syntax/output varies by DBMS.

# Part 69 — Full Table Scan

### Core Explanation

A full scan reads many or all table rows. It is not automatically bad: small tables and broad queries may be faster to scan than use an index.

### Why It Matters

The goal is efficient execution for the workload, not 'always use index'.

# Part 70 — Transaction

### Core Explanation

A transaction groups database operations into one logical unit.

### Example / Code

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Why It Matters

The transfer should not leave only one account updated.

# Part 71 — Atomicity

### Core Explanation

Atomicity means a transaction's intended changes take effect as a unit or are rolled back.

### Diagram / Mental Model

```text
Debit A
Credit B
   ↓
either both commit
or both roll back
```

# Part 72 — Consistency

### Core Explanation

Consistency means a committed transaction moves the database from one valid state to another according to enforced invariants and application rules.

### Why It Matters

ACID consistency is not the same concept as distributed CAP consistency.

# Part 73 — Isolation

### Core Explanation

Isolation controls how concurrent transactions observe and interfere with one another.

### Diagram / Mental Model

```text
Transaction A ─┐
               ├→ DB concurrency control
Transaction B ─┘
```

### Why It Matters

Without concurrency control, simultaneous users can corrupt logical state.

# Part 74 — Durability

### Core Explanation

Durability means committed changes survive expected failures according to the DBMS and storage configuration.

### Diagram / Mental Model

```text
COMMIT
  ↓
transaction/log/storage guarantees
  ↓
restart
  ↓
committed data remains
```

# Part 75 — COMMIT

### Core Explanation

`COMMIT` makes the transaction's changes durable/visible according to engine semantics.

### Example / Code

```sql
BEGIN;
UPDATE servers SET environment='staging' WHERE id=1;
COMMIT;
```

# Part 76 — ROLLBACK

### Core Explanation

`ROLLBACK` abandons uncommitted transaction changes.

### Example / Code

```sql
BEGIN;
DELETE FROM incidents;
ROLLBACK;
```

### Why It Matters

Extremely useful when validating destructive operations.

# Part 77 — Savepoint Awareness

### Core Explanation

A savepoint marks an intermediate point to which part of a transaction can be rolled back where supported.

### Example / Code

```sql
BEGIN;
SAVEPOINT before_optional_step;
-- work
ROLLBACK TO SAVEPOINT before_optional_step;
COMMIT;
```

### Why It Matters

Useful for complex transaction flows; exact syntax varies.

# Part 78 — Autocommit Awareness

### Core Explanation

Many clients automatically commit individual statements unless an explicit transaction is opened.

### Why It Matters

Beginners may think they can rollback a statement that was already autocommitted.

### Practical Use

Know your client/driver transaction mode.

# Part 79 — Concurrent Transactions

### Core Explanation

Multiple sessions may execute transactions at the same time.

### Diagram / Mental Model

```text
Session A: update server 1
Session B: read/update server 1
       ↓
locks / MVCC / isolation rules
```

### Why It Matters

Databases are multi-user systems.

# Part 80 — Lost Update

### Core Explanation

A lost update can occur when two transactions read the same value and one later overwrites the other's change without coordination.

### Diagram / Mental Model

```text
A reads 10
B reads 10
A writes 11
B writes 11
Expected maybe 12 → one update lost
```

### Why It Matters

Use proper locking, atomic update statements, or optimistic concurrency controls.

# Part 81 — Dirty Read Awareness

### Core Explanation

A dirty read means one transaction sees another transaction's uncommitted changes. Whether this is possible depends on the DBMS/isolation level.

### Why It Matters

Uncommitted data can later rollback, so observing it can produce inconsistent decisions.

# Part 82 — Non-Repeatable Read

### Core Explanation

The same row read twice in one transaction may appear changed because another transaction committed an update between reads, depending on isolation.

### Why It Matters

Important for consistent multi-step calculations.

# Part 83 — Phantom Read Awareness

### Core Explanation

A repeated query may return a different set of rows because another transaction inserted/deleted matching rows.

### Why It Matters

This matters for range and aggregate decisions.

# Part 84 — Isolation Levels

### Core Explanation

SQL databases expose isolation levels that trade concurrency against visibility anomalies. Typical names include Read Uncommitted, Read Committed, Repeatable Read, and Serializable, though exact guarantees vary by engine.

### Diagram / Mental Model

```text
Lower isolation
  ↑ more concurrency / possible anomalies

Higher isolation
  ↓ fewer anomalies / possible contention
```

### Why It Matters

Always read your DBMS documentation for exact semantics.

# Part 85 — Locks

### Core Explanation

Locks coordinate access to database objects/rows so conflicting operations do not proceed unsafely.

### Diagram / Mental Model

```text
Tx A owns write lock
Tx B waits
Tx A commits
Tx B continues
```

### Why It Matters

Lock waits are normal; excessive contention is a performance problem.

# Part 86 — MVCC Awareness

### Core Explanation

Multi-Version Concurrency Control keeps multiple row versions so readers and writers can often proceed with less blocking.

### Diagram / Mental Model

```text
Row version v1 ← reader snapshot
Row version v2 ← newer committed writer
```

### Why It Matters

PostgreSQL and other systems use MVCC-style techniques, though implementations differ.

# Part 87 — Deadlock

### Core Explanation

A deadlock occurs when transactions wait on each other in a cycle.

### Diagram / Mental Model

```text
Tx A locks Row 1
Tx B locks Row 2
Tx A waits Row 2
Tx B waits Row 1
      ↓
deadlock
```

### Why It Matters

The DBMS usually detects and aborts one transaction.

### Practical Use

Access shared resources in consistent order and keep transactions short.

# Part 88 — Short Transactions

### Core Explanation

Long transactions hold locks/versions/resources longer and increase contention and recovery complexity.

### Why It Matters

Do not perform slow user interaction or external API calls while holding a database transaction unless design requires it.

# Part 89 — Database Session / Connection

### Core Explanation

Applications communicate with a DBMS through network/local connections and sessions that hold transaction and authentication state.

### Diagram / Mental Model

```text
Application Process
  ↓ driver
DB Connection
  ↓
DB Session
  ↓
Transaction / Queries
```

### Why It Matters

Connections are limited resources.

# Part 90 — Connection Pool Awareness

### Core Explanation

A connection pool reuses a bounded number of database connections instead of creating one for every request.

### Diagram / Mental Model

```text
100 HTTP requests
      ↓
Connection Pool (10)
      ↓
Database
```

### Why It Matters

Connection creation is expensive and databases have connection limits.

# Part 91 — Parameterized Query

### Core Explanation

Parameterized queries send SQL structure separately from data values.

### Example / Code

```python
cursor.execute(
    "SELECT id, hostname FROM servers WHERE hostname = ?",
    (hostname,)
)
```

### Why It Matters

The driver safely binds the value rather than interpreting it as SQL syntax. Placeholder style differs by Python driver.

### Practical Use

Use parameter binding for every untrusted value.

# Part 92 — Unsafe SQL Concatenation

### Core Explanation

Building SQL by concatenating external input mixes data with program structure and can create SQL injection vulnerabilities.

### Example / Code

```python
# Unsafe pattern — do not use:
query = "SELECT * FROM users WHERE name = '" + user_input + "'"
```

### Why It Matters

Attackers can alter query meaning when input is interpreted as SQL.

### Practical Use

Use prepared/parameterized statements.

# Part 93 — SQL Injection — Defensive Mental Model

### Core Explanation

SQL injection occurs when untrusted input changes SQL syntax because the program constructs queries unsafely.

### Diagram / Mental Model

```text
Untrusted input
   ↓ concatenated into SQL
SQL parser cannot distinguish intended data from structure
   ↓
query meaning changes
```

### Why It Matters

This is why validation alone is not sufficient: parameterization is the primary structural defense.

# Part 94 — Authentication

### Core Explanation

Database authentication proves the identity of a user/application/service.

### Why It Matters

A database should not accept anonymous administrative access.

# Part 95 — Authorization

### Core Explanation

Authorization determines what an authenticated principal may do.

### Diagram / Mental Model

```text
App identity
   ↓
SELECT servers
INSERT incidents
NOT:
DROP DATABASE
```

### Why It Matters

Application accounts should not run with DBA privileges.

# Part 96 — Least Privilege

### Core Explanation

Grant only the minimum tables, operations, schemas, and administrative rights required.

### Why It Matters

If the application is compromised, least privilege reduces the blast radius.

# Part 97 — Database Roles Awareness

### Core Explanation

DBMSs commonly group privileges into users/roles, but exact commands differ.

### Why It Matters

Separate read-only analytics, application runtime, migration, and administration privileges.

# Part 98 — Encryption in Transit

### Core Explanation

TLS protects credentials and database traffic while traversing networks.

### Diagram / Mental Model

```text
Application
   ↓ TLS
Database Server
```

### Why It Matters

Internal networks should not automatically be treated as trusted.

# Part 99 — Encryption at Rest Awareness

### Core Explanation

Storage/database encryption protects persisted files/media according to platform capabilities and threat model.

### Why It Matters

It complements, not replaces, authorization and backups.

# Part 100 — Audit Logging

### Core Explanation

Database audit/activity logs can record authentication, administrative changes, and selected data access.

### Why It Matters

Useful for incident response, compliance, and troubleshooting.

### Practical Use

Avoid logging sensitive query values indiscriminately.

# Part 101 — Backup

### Core Explanation

A backup is an independent recoverable copy of data or database state.

### Diagram / Mental Model

```text
Primary Database
   ↓
Backup
   ↓
Separate recovery location
```

### Why It Matters

A live replica is not a complete substitute for backup because corruption/deletion may replicate.

# Part 102 — Logical Backup / Dump

### Core Explanation

A logical dump exports schema and/or data as SQL or structured records.

### Diagram / Mental Model

```text
DB objects/rows
   ↓ logical export
SQL/text dump
```

### Why It Matters

Portable and useful for small databases, migrations, and inspection.

### Practical Use

Exact tools include provider/engine-specific dump utilities.

# Part 103 — Physical Backup Awareness

### Core Explanation

Physical backups copy database storage pages/files in a DBMS-consistent manner.

### Why It Matters

Often faster for large systems but more engine/version-specific.

# Part 104 — Restore

### Core Explanation

A backup is useful only if it can be restored successfully.

### Diagram / Mental Model

```text
Backup
  ↓ restore
Test Database
  ↓ validation
Recovered service
```

### Why It Matters

Untested backups are assumptions, not recovery evidence.

# Part 105 — RPO

### Core Explanation

Recovery Point Objective is the maximum acceptable amount of data loss measured in time.

### Diagram / Mental Model

```text
Failure at 12:00
RPO 15 min
acceptable recovery point >= 11:45
```

### Why It Matters

RPO drives backup/replication frequency.

# Part 106 — RTO

### Core Explanation

Recovery Time Objective is the maximum acceptable time to restore service.

### Diagram / Mental Model

```text
Failure
  ↓
restore / failover
  ↓
service available
must fit RTO
```

### Why It Matters

RTO drives automation, standby architecture, and runbooks.

# Part 107 — Transaction Log / WAL Awareness

### Core Explanation

Relational systems commonly maintain a transaction/change log before or alongside durable data-file updates. Names and implementations differ.

### Diagram / Mental Model

```text
Transaction
  ↓
Change/Write-Ahead Log
  ↓
Data pages
  ↓
Recovery after crash
```

### Why It Matters

Logs support durability, crash recovery, replication, and point-in-time recovery in many DBMSs.

# Part 108 — Crash Recovery Awareness

### Core Explanation

After an unexpected restart, the DBMS uses persisted metadata/log information to recover committed state and discard incomplete work according to its design.

### Why It Matters

Do not treat database files like ordinary files that can always be copied live safely.

# Part 109 — Replication Awareness

### Core Explanation

Replication copies database changes to another instance for availability, read scaling, or disaster recovery.

### Diagram / Mental Model

```text
Primary
  ├→ Replica A
  └→ Replica B
```

### Why It Matters

Replication can copy mistakes as well as correct data; backups remain necessary.

# Part 110 — Schema Migration

### Core Explanation

A schema migration is a versioned change to database structure or data.

### Example / Code

```sql
ALTER TABLE incidents
ADD COLUMN status VARCHAR(20);
```

### Why It Matters

Schema changes must coordinate with application versions.

### Practical Use

Backup/recovery plan and backward compatibility matter for production.

# Part 111 — Migration Rollback Awareness

### Core Explanation

Not every schema change is easily reversible. Dropping or transforming data may make rollback impossible without backup.

### Why It Matters

Plan forward fixes and restore procedures before destructive migrations.

# Part 112 — Final Database Mental Model

### Core Explanation

A production database is a combination of **data model + constraints + query engine + transaction system + security + storage + recovery**.

### Diagram / Mental Model

```text
Business Rules
    ↓
Schema / Constraints
    ↓
SQL Queries
    ↓
Optimizer / Executor
    ↓
Transactions / Concurrency
    ↓
Pages / Indexes / Logs
    ↓
Durable Storage / Backup
```

### Why It Matters

This mental model connects development, DBA work, cloud databases, and database security.

# 5. Hands-on Lab / Practical Exercises

## Lab 1 — Choose and Verify a DBMS

Install or use one authorized local DBMS. Record:
```text
DBMS name
version
database file/server location
client tool
how to connect
```
Run a simple:
```sql
SELECT 1;
```

## Lab 2 — Create Teams Table

Create:
```sql
CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);
```
Explain every token and constraint.

## Lab 3 — Create Servers Table

Create a `servers` table containing:
```text
id
hostname
ip_address
environment
team_id
```
Add primary key, unique hostname, required fields, and foreign key.

## Lab 4 — Create Incidents Table

Create:
```text
incidents
id
server_id
severity
description
status
created_at
```
Add appropriate required fields and a severity CHECK if supported.

## Lab 5 — Insert Sample Data

Insert at least:
```text
3 teams
10 servers
15 incidents
```
Use explicit column lists.

## Lab 6 — Constraint Failure

Intentionally try:
```text
duplicate hostname
NULL required hostname
incident with missing server
invalid severity
```
Observe and document each database error.

## Lab 7 — Basic SELECT

Write queries for:
```text
all servers
hostname + IP only
production servers
servers ordered by hostname
unique environments
```

## Lab 8 — Safe UPDATE

Before:
```sql
UPDATE servers ...
```
first run:
```sql
SELECT ...
WHERE <same predicate>;
```
Then update one row and verify it.

## Lab 9 — Safe DELETE with Rollback

Start a transaction, delete selected lab rows, verify count, then ROLLBACK. Repeat and COMMIT only after confirming intended behavior.

## Lab 10 — INNER JOIN

Show every server with its owning team.
Explain:
```text
left table
right table
join key
result cardinality
```

## Lab 11 — LEFT JOIN

List all servers with incident counts, including servers with zero incidents.

## Lab 12 — Find Servers with No Incidents

Use:
```text
LEFT JOIN + IS NULL
```
and explain why an INNER JOIN cannot answer this directly.

## Lab 13 — Three-Table Join

Return:
```text
hostname
team name
incident severity
incident status
```
from teams + servers + incidents.

## Lab 14 — Aggregation

Count incidents by:
```text
severity
status
team
```
Use GROUP BY.

## Lab 15 — HAVING

Find servers with at least 2 incidents using GROUP BY + HAVING.

## Lab 16 — Normalization Exercise

Start with:
```text
incident_id
server_hostname
server_ip
team_name
team_email
severity
```
Normalize into separate tables. Draw before/after.

## Lab 17 — Many-to-Many Model

Add:
```text
applications
application_servers
```
so applications can run on many servers and servers can host many applications.

## Lab 18 — Composite Key

Make `(application_id, server_id)` the primary key of the junction table. Attempt a duplicate relationship and observe failure.

## Lab 19 — NULL Semantics

Insert optional `team_id = NULL` for a lab server. Compare:
```sql
WHERE team_id = NULL
WHERE team_id IS NULL
```
Document the result.

## Lab 20 — Index Creation

Create an index on `incidents(server_id)`. Explain why it may help joins/lookups.

## Lab 21 — Composite Index

Create an index on:
```text
(server_id, severity)
```
List queries that can potentially benefit and explain leading-column awareness.

## Lab 22 — EXPLAIN Awareness

Use your DBMS query-plan command for:
```sql
SELECT *
FROM incidents
WHERE server_id = 1;
```
Capture the plan before/after index if practical. Do not assume an index will always be used on a tiny table.

## Lab 23 — Transaction Commit

Create `service_capacity(server_id, capacity)`. Update two rows in one transaction and COMMIT. Verify both.

## Lab 24 — Transaction Rollback

Repeat the updates but ROLLBACK. Verify neither change remains.

## Lab 25 — Lost Update Simulation

With two DB sessions, conceptually or practically:
```text
A reads value
B reads value
A updates
B updates
```
Observe behavior under your engine/default isolation. Do not generalize semantics beyond the DBMS you tested.

## Lab 26 — Deadlock Demonstration Design

Draw a safe two-transaction deadlock sequence:
```text
A locks row1
B locks row2
A requests row2
B requests row1
```
If you reproduce it, use only a disposable lab database.

## Lab 27 — Parameterized Python Query

Using the appropriate Python driver for your DBMS, write a parameterized query. Do not use string concatenation. Document the driver's placeholder syntax.

## Lab 28 — SQL Injection Comparison

Create two code snippets:
```text
unsafe string concatenation
safe parameter binding
```
Do **not** attack any real system. Explain structurally why the safe version prevents input from changing SQL syntax.

## Lab 29 — Database Role Matrix

Design roles:
```text
app_runtime
report_reader
migration_role
dba
```
For each list required and prohibited privileges.

## Lab 30 — Backup / Export

Create a logical backup or SQLite file copy using the correct safe method for your chosen DBMS. Record the exact command/tool and resulting artifact.

## Lab 31 — Restore Test

Restore the backup into a separate lab database. Verify:
```text
table count
row counts
one critical query
constraints
```

## Lab 32 — RPO / RTO Exercise

For:
```text
development DB
internal business DB
critical production DB
```
define example RPO/RTO and explain how the requirements change backup architecture.

## Lab 33 — Schema Migration

Add an `incident_status` or `resolved_at` column. Create:
```text
migration up steps
application compatibility notes
rollback/forward-fix plan
```

## Lab 34 — Query Review

Review ten queries and identify:
```text
unnecessary SELECT *
missing WHERE
incorrect join
NULL bug
possible index opportunity
unsafe string SQL
```

## Lab 35 — Capstone Build

Implement the complete IT Asset and Incident Database project described below, including ERD, schema, data, queries, transaction example, index rationale, backup, and security notes.

# 6. Mini Project

## Mini Project — IT Asset, Application, Vulnerability, and Incident Database

Build a relational database that models:

```text
Teams
Users / Owners
Servers
Applications
Application ↔ Server deployment
Incidents
Incident status
Vulnerabilities
Server ↔ Vulnerability findings
```

### Architecture / ERD

A suggested relationship map:

```text
Teams
  │1
  ├────────< Servers
  │             │1
  │             ├────────< Incidents
  │             │
  │             └────────< Server_Vulnerabilities >──────── Vulnerabilities
  │
  └────────< Users

Applications
   │
   └────────< Application_Servers >──────── Servers
```

### Required Deliverables

```text
database-project/
├── README.md
├── erd.md
├── schema.sql
├── seed.sql
├── queries.sql
├── transactions.sql
├── indexes.md
├── security.md
├── backup-restore.md
└── migrations/
    └── 001_add_incident_status.sql
```

### Schema Requirements

Use:

```text
PRIMARY KEY
FOREIGN KEY
NOT NULL
UNIQUE
CHECK where portable/supported
at least one composite key
```

### Sample Data

At least:

```text
4 teams
8 users
20 servers
8 applications
30 application-server relationships
30 incidents
15 vulnerabilities
30 server-vulnerability findings
```

### Query Requirements

Create at least **20 useful queries**, including:

1. Production servers and owning teams.
2. Servers with no incidents.
3. Open incidents by severity.
4. Incident count per team.
5. Team with most open incidents.
6. Applications running on each server.
7. Servers hosting more than 2 applications.
8. Vulnerabilities per server.
9. Critical vulnerabilities not remediated.
10. Incident count by environment.
11. Left join showing zero-incident servers.
12. Multi-table join across incident → server → team.
13. Aggregate with HAVING.
14. Query using a subquery.
15. Query using a CTE if supported.
16. Update with verified WHERE.
17. Delete inside a rollback test.
18. Transaction updating two related records.
19. Query designed to use an index.
20. NULL-aware query.

### Index Plan

For each index document:

```text
query pattern
indexed columns
expected benefit
write/storage cost
why column order was chosen
```

### Security Plan

Define:

```text
app runtime role
report-only role
migration role
administrator role
parameterized query requirement
TLS requirement for remote DB traffic
backup access
audit/logging expectations
```

### Backup / Restore

Perform and document:

```text
backup
restore into separate lab DB
row-count validation
critical-query validation
```

### Failure Scenarios

Explain what happens if:

```text
application crashes before COMMIT
database restarts after COMMIT
two users update same logical record
backup exists but restore was never tested
application account is compromised
```

# 7. Recommended Resources

This Markdown is designed to provide the complete Phase 1 conceptual foundation.

Optional deeper references:

```text
PostgreSQL official tutorial/documentation
MySQL official manual/tutorial
SQLite official documentation
```

When implementing engine-specific behavior, verify the current official documentation for:

```text
auto-increment / identity columns
isolation semantics
foreign-key behavior
backup utilities
user/role syntax
EXPLAIN output
TLS configuration
```

Do not jump between database engines constantly while learning fundamentals. Choose one for the labs and learn its behavior well.

# 8. Certification Relevance

Database fundamentals support:

```text
Phase 7 — MySQL / Oracle / NoSQL / Cloud Databases
Backend engineering
Cloud architecture
DevOps
Power BI / analytics engineering
Cybersecurity
```

For cybersecurity they directly support:

```text
SQL injection prevention
database least privilege
data classification
audit analysis
backup/recovery
incident investigation
database exposure assessment
```

For cloud engineering they support managed database decisions involving:

```text
storage
connectivity
authentication
replication
backup
RPO/RTO
availability
```

# 9. Common Mistakes & Best Practices

- **Mistake:** Using a spreadsheet-like table containing every entity and repeated facts.  
  **Best practice:** Separate entities and relationships, then normalize.
- **Mistake:** Using changing names as the only identity.  
  **Best practice:** Use stable primary keys and enforce business uniqueness separately.
- **Mistake:** Allowing invalid state because 'the application validates it'.  
  **Best practice:** Use database constraints for critical invariants.
- **Mistake:** Using `= NULL`.  
  **Best practice:** Use `IS NULL` / `IS NOT NULL`.
- **Mistake:** Running UPDATE or DELETE before verifying the WHERE clause.  
  **Best practice:** Run a SELECT with the same predicate and use a transaction.
- **Mistake:** Using SELECT * everywhere.  
  **Best practice:** Select needed columns in application queries.
- **Mistake:** Using DISTINCT to hide duplicate rows from a bad join.  
  **Best practice:** Fix the relationship/join logic.
- **Mistake:** Indexing every column.  
  **Best practice:** Index measured query patterns and consider write/storage overhead.
- **Mistake:** Assuming an index must be used.  
  **Best practice:** Read the query plan; scans can be optimal.
- **Mistake:** Keeping transactions open while waiting on users/external APIs.  
  **Best practice:** Keep transactions short and focused.
- **Mistake:** Ignoring concurrency because a query works in one session.  
  **Best practice:** Test multi-user update scenarios.
- **Mistake:** Concatenating user input into SQL.  
  **Best practice:** Always use parameterized queries.
- **Mistake:** Giving application accounts DBA privileges.  
  **Best practice:** Use least privilege.
- **Mistake:** Treating a replica as a backup.  
  **Best practice:** Maintain independent recoverable backups.
- **Mistake:** Creating backups without testing restores.  
  **Best practice:** Perform restore drills.
- **Mistake:** Making destructive schema migrations without recovery planning.  
  **Best practice:** Use versioned migrations and backup/forward-fix strategy.
- **Mistake:** Storing comma-separated lists in a column for relational relationships.  
  **Best practice:** Use child/junction tables.
- **Mistake:** Treating NULL as an empty string or zero.  
  **Best practice:** Model missing/unknown state explicitly.
- **Mistake:** Assuming ACID means the application is automatically logically correct.  
  **Best practice:** Constraints and transaction design must encode the required invariants.
- **Mistake:** Learning only SQL syntax without understanding data modeling.  
  **Best practice:** Start from business facts, entities, relationships, and constraints.

# 10. Self-Assessment Questions (with short answers)

1. **Database vs DBMS?**  
   A database is organized data; a DBMS is software that manages it.

2. **What is a relational table?**  
   A structured relation exposed as rows and columns.

3. **What is a schema?**  
   Definition of database objects, columns, types, constraints, indexes, and related structures.

4. **What is a primary key?**  
   A unique non-null identifier for each row.

5. **What is a candidate key?**  
   Any minimal attribute set that could uniquely identify a row.

6. **Natural key?**  
   A business/domain identifier used as a key.

7. **Surrogate key?**  
   Artificial identifier created primarily for stable row identity.

8. **Composite key?**  
   A key made from multiple columns.

9. **Foreign key?**  
   Constraint referencing a key in another table.

10. **One-to-many?**  
   One parent can relate to many child rows.

11. **Many-to-many?**  
   Many A rows can relate to many B rows, usually through a junction table.

12. **Why use NOT NULL?**  
   Enforce that required data is present.

13. **Why use UNIQUE?**  
   Enforce business uniqueness.

14. **What does CHECK do?**  
   Reject values that do not satisfy a predicate.

15. **What is normalization?**  
   Organizing relations to reduce harmful redundancy and anomalies.

16. **Update anomaly?**  
   Repeated fact is updated inconsistently.

17. **Insertion anomaly?**  
   A fact cannot be stored without unrelated data.

18. **Deletion anomaly?**  
   Deleting one fact accidentally deletes another fact's only representation.

19. **1NF concept?**  
   Avoid repeating groups/multi-valued cells; represent values relationally.

20. **3NF concept?**  
   Non-key facts should depend on the key rather than other unrelated non-key facts.

21. **What is CRUD?**  
   Create, Read, Update, Delete.

22. **CRUD SQL mapping?**  
   INSERT, SELECT, UPDATE, DELETE.

23. **Why is WHERE dangerous to forget?**  
   UPDATE/DELETE may affect every row.

24. **INNER JOIN?**  
   Returns matching rows from both sides.

25. **LEFT JOIN?**  
   Preserves all rows from the left side even without a right-side match.

26. **How find rows with no child relationship?**  
   LEFT JOIN plus a right-side IS NULL check.

27. **What does GROUP BY do?**  
   Groups rows for aggregate calculation.

28. **WHERE vs HAVING?**  
   WHERE filters input rows; HAVING filters grouped results.

29. **COUNT(*) vs COUNT(column)?**  
   COUNT(*) counts rows; COUNT(column) ignores NULL values.

30. **What is an index?**  
   Auxiliary structure improving selected access paths at write/storage cost.

31. **Why not index every column?**  
   Indexes consume storage and slow writes/maintenance.

32. **What is selectivity?**  
   How narrowly a value/predicate identifies rows.

33. **Composite-index order matters why?**  
   B-tree access patterns commonly depend on leading columns.

34. **What is a query plan?**  
   The execution strategy chosen by the optimizer.

35. **Is a full scan always bad?**  
   No; it can be optimal for small tables or broad queries.

36. **What is a transaction?**  
   Logical group of database operations committed or rolled back together.

37. **Atomicity?**  
   All intended transaction changes happen as a unit or not at all.

38. **Consistency in ACID?**  
   Transaction preserves database/application invariants.

39. **Isolation?**  
   Controls interactions and visibility among concurrent transactions.

40. **Durability?**  
   Committed data survives expected failure according to system guarantees.

41. **COMMIT?**  
   Makes transaction changes permanent/visible according to DBMS semantics.

42. **ROLLBACK?**  
   Discards uncommitted changes.

43. **What is autocommit?**  
   Client/DB mode that commits statements automatically unless an explicit transaction is used.

44. **Lost update?**  
   One concurrent update overwrites another without preserving both logical changes.

45. **Dirty read?**  
   Reading another transaction's uncommitted data.

46. **Deadlock?**  
   Transactions wait on each other in a dependency cycle.

47. **Why keep transactions short?**  
   Reduce locks/version retention/contention and failure complexity.

48. **What is MVCC?**  
   Concurrency technique using multiple row versions so readers/writers interfere less.

49. **What is a DB connection?**  
   Application communication session to a DBMS.

50. **Why connection pool?**  
   Reuse a bounded number of expensive DB connections.

51. **Why parameterized queries?**  
   Keep data separate from SQL structure and prevent injection through values.

52. **What is SQL injection?**  
   Untrusted input changes SQL syntax/meaning when queries are constructed unsafely.

53. **Authentication vs authorization?**  
   Authentication proves identity; authorization controls permissions.

54. **Least privilege?**  
   Grant only required database rights.

55. **Backup vs replica?**  
   Backup is independent recoverable history; replica is a synchronized copy for availability/read scaling.

56. **RPO?**  
   Maximum acceptable data loss measured in time.

57. **RTO?**  
   Maximum acceptable recovery time.

58. **What is a transaction log/WAL concept?**  
   Durable change log used by many DBMSs for recovery/replication.

59. **What is a schema migration?**  
   Versioned change to database structure/data.

60. **Final database mental model?**  
   Data model + constraints + SQL/query engine + transactions/concurrency + security + storage/recovery.

