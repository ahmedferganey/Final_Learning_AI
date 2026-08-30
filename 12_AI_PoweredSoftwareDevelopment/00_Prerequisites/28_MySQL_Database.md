# 28. MySQL Database

> Phase 7 — Database

This course is the **relational-database foundation** for the rest of Phase 7. The examples use modern MySQL with **MySQL 8.4 LTS as the reference baseline**.

The goal is not to memorize SQL keywords. The goal is to understand the complete path:

```text
Business Requirement
        ↓
Data Model
        ↓
Tables + Keys + Constraints
        ↓
SQL
        ↓
Query Optimizer
        ↓
InnoDB
        ↓
Transactions / Locks / Indexes
        ↓
Memory + Logs + Storage
        ↓
Backup / Replication / Monitoring
```

Every major concept uses:

```text
Concept
  ↓
Visualization
  ↓
SQL / CLI
  ↓
Expected behavior
  ↓
Why it works
  ↓
Troubleshooting
```

---

## 1. Topic Title

**MySQL Database**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain why DBMS software exists and how relational databases organize business data.
- Design entities, attributes, relationships, keys, constraints, and normalized schemas.
- Install, connect to, inspect, and troubleshoot a MySQL server.
- Write SQL using DDL, DML, DCL, and TCL.
- Query with filtering, expressions, functions, aggregation, joins, subqueries, CTEs, views, and set operations.
- Explain InnoDB architecture and the difference between clustered and secondary indexes.
- Design indexes from real query patterns and interpret `EXPLAIN`.
- Explain ACID, transactions, isolation levels, MVCC, locks, lock waits, and deadlocks.
- Build procedures, functions, triggers, and scheduled events responsibly.
- Create users and roles and apply least privilege.
- Understand buffer pool, redo, undo, tablespaces, binary logs, and MySQL configuration.
- Create and restore backups and explain point-in-time recovery.
- Explain replication, GTID, replication lag, Group Replication, and InnoDB Cluster.
- Use Performance Schema, `sys`, slow-query information, and OS metrics for troubleshooting.
- Build a complete manufacturing database project.

---

## 3. Prerequisites

Recommended:

- Database Fundamentals
- basic programming
- Linux or Windows command-line familiarity
- networking fundamentals

Recommended lab:

```text
MySQL Server
------------
2 vCPU
4 GB RAM
30+ GB disk
MySQL 8.4 LTS-compatible environment

Tools
-----
mysql CLI
MySQL Shell
MySQL Workbench optional
VS Code / DBeaver optional
```

Main lab database:

```text
manufacturing
```

Core entities:

```text
Customer
Product
Department
Employee
Orders
OrderItem
Machine
ProductionRun
QualityInspection
Defect
Inventory
```

---

## 4. Core Concepts Explanation

# Part 1 — Why Databases Exist

## 1.1 File-based Data Problems

Suppose a company starts with:

```text
customers.xlsx
orders.xlsx
products.xlsx
inventory.xlsx
```

As the company grows:

```text
duplicate data
conflicting copies
two users editing simultaneously
no guaranteed relationships
poor access control
slow searches
weak recovery
```

A DBMS introduces coordinated access:

```text
Users / Applications
        |
       SQL
        |
        v
+----------------------+
| MySQL Server         |
|----------------------|
| Authentication       |
| SQL Parser           |
| Optimizer            |
| Transaction Manager  |
| InnoDB               |
+----------------------+
        |
        v
Persistent Storage
```

A DBMS is therefore much more than a file format.

## 1.2 Data vs Information

Raw data:

```text
quantity = 300
unit_price = 4.25
```

Derived information:

```text
line_total = 1275.00
```

SQL turns stored facts into useful information.

## 1.3 Database vs DBMS

```text
Database
    organized stored data

DBMS
    software managing data, access, concurrency,
    security, transactions, and recovery
```

MySQL is the DBMS.

---

# Part 2 — Relational Model

## 2.1 Table, Row, Column

```text
Product
+------------+---------------+-----------+
| product_id | product_name  | unit_price|
+------------+---------------+-----------+
| 1          | Bottle 330ml  | 0.2500    |
| 2          | Jar 500ml     | 0.4000    |
+------------+---------------+-----------+
```

- Table: a set of similar records.
- Row: one entity/fact.
- Column: one attribute.

## 2.2 Entity

Examples:

```text
Customer
Product
Machine
Employee
Order
```

An entity should have a clear identity.

## 2.3 Relationship

```text
Customer
   |
   | places
   v
Order
```

The relational model implements relationships using keys.

## 2.4 One-to-One

```text
Person 1 -------- 1 Passport
```

A unique foreign key can implement this relationship.

## 2.5 One-to-Many

```text
Department 1 -------- N Employee
```

Implementation:

```text
department.department_id  PK
employee.department_id    FK
```

The FK belongs on the many side.

## 2.6 Many-to-Many

Business relationship:

```text
Order N -------- N Product
```

Relational resolution:

```text
Orders
   |
   | 1:N
   v
OrderItem
   ^
   | N:1
   |
Product
```

`OrderItem` can store relationship attributes:

```text
quantity
unit_price
discount
```

---

# Part 3 — Keys

## 3.1 Primary Key

```sql
CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);
```

Primary key:

```text
unique
not null
row identity
```

## 3.2 Candidate and Alternate Keys

A table might have multiple candidate keys:

```text
employee_id
email
employee_number
```

One becomes primary; others may remain `UNIQUE`.

```sql
CREATE TABLE employee (
    employee_id BIGINT PRIMARY KEY,
    employee_number VARCHAR(30) NOT NULL UNIQUE,
    email VARCHAR(255) UNIQUE
);
```

## 3.3 Composite Key

```sql
CREATE TABLE order_item (
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,

    PRIMARY KEY (order_id, product_id)
);
```

Identity is the combination.

## 3.4 Foreign Key

```sql
CREATE TABLE employee (
    employee_id BIGINT PRIMARY KEY,
    employee_name VARCHAR(150) NOT NULL,
    department_id INT,

    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES department(department_id)
);
```

Now an employee cannot reference a missing department.

## 3.5 Natural vs Surrogate Keys

Natural key:

```text
business-provided identifier
```

Surrogate key:

```text
database-generated/internal identifier
```

Example:

```sql
customer_id BIGINT AUTO_INCREMENT PRIMARY KEY
```

Using a surrogate key does not remove the need for business uniqueness:

```sql
customer_code VARCHAR(50) NOT NULL UNIQUE
```

---

# Part 4 — MySQL Architecture

## 4.1 End-to-End Query Path

```text
Client
  |
  | TCP/3306 or local socket
  v
Connection Layer
  |
  v
Parser
  |
  v
Optimizer
  |
  v
Executor
  |
  v
InnoDB
  |
  +-- Buffer Pool
  +-- Redo
  +-- Undo
  +-- Tablespaces
  |
  v
Disk
```

## 4.2 Client/Server

Clients include:

```text
mysql
MySQL Shell
Workbench
backend application
BI/reporting tool
```

The server process is normally `mysqld`.

## 4.3 Connection Layer

Connection processing includes:

```text
network/session establishment
authentication
account resolution
privilege checks
session state
```

## 4.4 Parser and Optimizer

SQL:

```sql
SELECT product_name
FROM product
WHERE product_id = 10;
```

is parsed and optimized.

Possible plans:

```text
full table scan
primary-key lookup
secondary-index lookup
different join orders
```

The optimizer chooses a plan based on available access methods and statistics.

## 4.5 Storage Engines

```sql
SHOW ENGINES;
```

MySQL supports a storage-engine abstraction.

For transactional systems, **InnoDB** is the central engine to understand.

## 4.6 InnoDB

InnoDB provides:

```text
ACID transactions
row-level locking
MVCC
foreign keys
crash recovery
clustered indexes
redo/undo
```

Check engine:

```sql
SHOW TABLE STATUS
WHERE Name = 'product';
```

## 4.7 System Schemas

```text
mysql
    system/account/privilege information

information_schema
    metadata

performance_schema
    runtime instrumentation

sys
    convenient diagnostic views
```

Inspect:

```sql
SHOW DATABASES;
```

---

# Part 5 — Installation and Connectivity

## 5.1 Service Check

Linux:

```bash
systemctl status mysqld
```

Depending on packaging, service name can vary.

```bash
sudo systemctl start mysqld
sudo systemctl enable mysqld
```

## 5.2 Listener

Default classic MySQL protocol commonly uses:

```text
TCP/3306
```

Linux:

```bash
ss -tlnp | grep 3306
```

Windows:

```powershell
Get-NetTCPConnection -LocalPort 3306 -State Listen
```

## 5.3 Local Login

```bash
mysql -u root -p
```

Remote lab:

```bash
mysql \
  -h 10.60.0.20 \
  -P 3306 \
  -u appuser \
  -p
```

## 5.4 Connection Troubleshooting

```text
DNS
 ↓
IP route
 ↓
firewall
 ↓
mysqld listener/bind address
 ↓
user@host account
 ↓
authentication
 ↓
TLS policy
 ↓
database privileges
```

Inspect the session:

```sql
SELECT
    CONNECTION_ID(),
    USER(),
    CURRENT_USER(),
    DATABASE();
```

---

# Part 6 — SQL Categories

## 6.1 DDL

```text
CREATE
ALTER
DROP
TRUNCATE
```

## 6.2 DML

```text
SELECT
INSERT
UPDATE
DELETE
```

## 6.3 DCL

```text
GRANT
REVOKE
```

## 6.4 TCL

```text
START TRANSACTION
COMMIT
ROLLBACK
SAVEPOINT
```

---

# Part 7 — Database and Table Creation

## 7.1 Create Database

```sql
CREATE DATABASE manufacturing;
USE manufacturing;
SELECT DATABASE();
```

## 7.2 Create Table

```sql
CREATE TABLE customer (
    customer_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    customer_code VARCHAR(50) NOT NULL UNIQUE,
    customer_name VARCHAR(150) NOT NULL,
    email VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Inspect real definition:

```sql
SHOW CREATE TABLE customer\G
```

## 7.3 Character Set and Collation

Inspect:

```sql
SHOW VARIABLES LIKE 'character_set_server';
SHOW VARIABLES LIKE 'collation_server';
```

Character set controls representation.

Collation affects comparison/sorting behavior.

Choose intentionally for multilingual applications.

---

# Part 8 — Data Types

## 8.1 Integers

```text
TINYINT
SMALLINT
MEDIUMINT
INT
BIGINT
```

Choose based on valid domain/range.

## 8.2 DECIMAL

Exact numeric:

```sql
unit_price DECIMAL(12,4)
```

Good for financial quantities where exact decimal behavior matters.

## 8.3 FLOAT and DOUBLE

Approximate numeric values.

Do not automatically use floating point for money.

## 8.4 CHAR and VARCHAR

```text
CHAR
fixed-length semantics

VARCHAR
variable length
```

Example:

```sql
country_code CHAR(2),
product_name VARCHAR(150)
```

## 8.5 DATE/TIME

```text
DATE
TIME
DATETIME
TIMESTAMP
```

Think about:

```text
timezone
precision
business meaning
automatic timestamp behavior
```

## 8.6 JSON

```sql
CREATE TABLE machine_event (
    event_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    machine_id INT NOT NULL,
    event_time DATETIME NOT NULL,
    payload JSON NOT NULL
);
```

Use JSON when attributes are genuinely semi-structured—not as an excuse to avoid relational modeling.

---

# Part 9 — Constraints

## 9.1 NOT NULL

```sql
product_name VARCHAR(150) NOT NULL
```

## 9.2 UNIQUE

```sql
product_code VARCHAR(50) NOT NULL UNIQUE
```

## 9.3 PRIMARY KEY

```sql
product_id BIGINT PRIMARY KEY
```

## 9.4 FOREIGN KEY

```sql
CONSTRAINT fk_order_customer
    FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
```

## 9.5 CHECK

```sql
quantity INT NOT NULL
CHECK (quantity > 0)
```

## 9.6 DEFAULT

```sql
status VARCHAR(30)
NOT NULL
DEFAULT 'NEW'
```

Full example:

```sql
CREATE TABLE product (
    product_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(50) NOT NULL UNIQUE,
    product_name VARCHAR(150) NOT NULL,
    unit_price DECIMAL(12,4) NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT chk_product_price
        CHECK (unit_price >= 0)
);
```

Strong systems validate at:

```text
Application
    +
Database constraint
```

---

# Part 10 — INSERT

## 10.1 Single Row

```sql
INSERT INTO product (
    product_code,
    product_name,
    unit_price
)
VALUES (
    'BTL-330',
    'Bottle 330ml',
    0.2500
);
```

## 10.2 Multiple Rows

```sql
INSERT INTO product (
    product_code,
    product_name,
    unit_price
)
VALUES
    ('JAR-500', 'Jar 500ml', 0.4000),
    ('BTL-750', 'Bottle 750ml', 0.5500);
```

## 10.3 Auto Increment

```sql
SELECT LAST_INSERT_ID();
```

## 10.4 INSERT SELECT

```sql
INSERT INTO archived_product (
    product_id,
    product_code,
    product_name
)
SELECT
    product_id,
    product_code,
    product_name
FROM product
WHERE active = FALSE;
```

---

# Part 11 — SELECT Fundamentals

## 11.1 Projection

```sql
SELECT
    product_code,
    product_name
FROM product;
```

Prefer explicit columns in long-lived application/report queries.

## 11.2 Aliases

```sql
SELECT
    product_name AS name,
    unit_price AS price
FROM product;
```

## 11.3 DISTINCT

```sql
SELECT DISTINCT status
FROM orders;
```

`DISTINCT` is not a substitute for correct schema design.

## 11.4 Expressions

```sql
SELECT
    product_name,
    unit_price,
    unit_price * 1000 AS value_for_1000
FROM product;
```

## 11.5 ORDER BY

```sql
SELECT
    product_name,
    unit_price
FROM product
ORDER BY
    unit_price DESC,
    product_name;
```

Without `ORDER BY`, result order should not be assumed.

## 11.6 LIMIT

```sql
SELECT *
FROM product
ORDER BY product_id
LIMIT 10;
```

Pagination requires deterministic ordering.

---

# Part 12 — Filtering

## 12.1 WHERE

```sql
SELECT *
FROM product
WHERE active = TRUE;
```

## 12.2 AND / OR / NOT

```sql
SELECT *
FROM product
WHERE
    active = TRUE
    AND (
        product_code LIKE 'BTL-%'
        OR product_code LIKE 'JAR-%'
    );
```

Use parentheses to make intent explicit.

## 12.3 BETWEEN

```sql
WHERE unit_price BETWEEN 0.25 AND 0.50
```

Both boundaries are included.

## 12.4 IN

```sql
WHERE status IN ('NEW', 'APPROVED', 'SHIPPED')
```

## 12.5 LIKE

```sql
WHERE product_name LIKE 'Bottle%'
```

Patterns:

```text
% = zero or more characters
_ = one character
```

## 12.6 NULL

Wrong:

```sql
WHERE manager_id = NULL
```

Correct:

```sql
WHERE manager_id IS NULL
```

SQL logic includes:

```text
TRUE
FALSE
UNKNOWN
```

NULL is not the same as zero or an empty string.

---

# Part 13 — SQL Functions

## 13.1 String

```sql
SELECT
    UPPER(product_name),
    LOWER(product_name),
    LENGTH(product_name),
    TRIM(product_name),
    SUBSTRING(product_code, 1, 3)
FROM product;
```

Concatenate:

```sql
SELECT
    CONCAT(product_code, ' - ', product_name)
FROM product;
```

## 13.2 Numeric

```sql
SELECT
    ROUND(12.3456, 2),
    CEIL(12.1),
    FLOOR(12.9),
    ABS(-10);
```

## 13.3 Date

```sql
SELECT
    NOW(),
    CURDATE(),
    YEAR(NOW()),
    MONTH(NOW()),
    DATEDIFF('2026-08-17', '2026-08-01'),
    DATE_ADD(CURDATE(), INTERVAL 30 DAY);
```

---

# Part 14 — Aggregate Queries

## 14.1 Aggregates

```sql
SELECT
    COUNT(*) AS product_count,
    AVG(unit_price) AS avg_price,
    MIN(unit_price) AS min_price,
    MAX(unit_price) AS max_price
FROM product;
```

## 14.2 GROUP BY

```sql
SELECT
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status;
```

## 14.3 HAVING

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 5;
```

Difference:

```text
WHERE
filters rows

HAVING
filters groups
```

## 14.4 Logical Query Processing

Useful mental model:

```text
FROM / JOIN
    ↓
WHERE
    ↓
GROUP BY
    ↓
HAVING
    ↓
SELECT
    ↓
ORDER BY
    ↓
LIMIT
```

---

# Part 15 — JOINs

## 15.1 INNER JOIN

```sql
SELECT
    o.order_id,
    c.customer_name,
    o.order_date
FROM orders AS o
JOIN customer AS c
    ON c.customer_id = o.customer_id;
```

Visualization:

```text
Customers ∩ Orders
```

Only matches.

## 15.2 LEFT JOIN

```sql
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id
FROM customer AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id;
```

All customers remain.

Find customers with no orders:

```sql
SELECT
    c.customer_id,
    c.customer_name
FROM customer AS c
LEFT JOIN orders AS o
    ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;
```

## 15.3 RIGHT JOIN

Equivalent right-preserving operation exists, though teams often rewrite logic as LEFT JOIN for consistent readability.

## 15.4 CROSS JOIN

```sql
SELECT
    s.shift_name,
    m.machine_name
FROM shift AS s
CROSS JOIN machine AS m;
```

Every combination.

## 15.5 SELF JOIN

```sql
SELECT
    e.employee_name,
    m.employee_name AS manager_name
FROM employee AS e
LEFT JOIN employee AS m
    ON m.employee_id = e.manager_id;
```

## 15.6 Multi-table Join

```sql
SELECT
    o.order_id,
    c.customer_name,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price AS line_total
FROM orders AS o
JOIN customer AS c
    ON c.customer_id = o.customer_id
JOIN order_item AS oi
    ON oi.order_id = o.order_id
JOIN product AS p
    ON p.product_id = oi.product_id;
```

## 15.7 Cartesian Explosion

If a predicate is missing:

```text
1,000 orders
×
500 products
=
500,000 combinations
```

Symptoms:

```text
unexpectedly huge result
high CPU
wrong totals
slow query
```

Always reason about join cardinality before running large queries.

---

# Part 16 — Subqueries

## 16.1 Scalar

```sql
SELECT *
FROM product
WHERE unit_price > (
    SELECT AVG(unit_price)
    FROM product
);
```

## 16.2 IN

```sql
SELECT *
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE order_date >= '2026-01-01'
);
```

## 16.3 EXISTS

```sql
SELECT
    c.customer_id,
    c.customer_name
FROM customer AS c
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.customer_id = c.customer_id
);
```

## 16.4 Correlated

Concept:

```text
Outer Customer
      |
      +--> inner query references that customer
```

Do not assume a join is always faster. Use execution plans and measured behavior.

---

# Part 17 — Common Table Expressions

## 17.1 CTE

```sql
WITH customer_sales AS (
    SELECT
        o.customer_id,
        SUM(oi.quantity * oi.unit_price) AS sales
    FROM orders AS o
    JOIN order_item AS oi
        ON oi.order_id = o.order_id
    GROUP BY o.customer_id
)
SELECT
    c.customer_name,
    cs.sales
FROM customer_sales AS cs
JOIN customer AS c
    ON c.customer_id = cs.customer_id
ORDER BY cs.sales DESC;
```

A CTE names intermediate query logic.

## 17.2 Recursive CTE

```sql
WITH RECURSIVE org AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level
    FROM employee
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        org.level + 1
    FROM employee AS e
    JOIN org
        ON e.manager_id = org.employee_id
)
SELECT *
FROM org;
```

Visualization:

```text
CEO level 0
 |
 +-- Manager level 1
       |
       +-- Engineer level 2
```

---

# Part 18 — Set Operations

## 18.1 UNION

```sql
SELECT email FROM customer
UNION
SELECT email FROM supplier;
```

Removes duplicates.

## 18.2 UNION ALL

```sql
SELECT email FROM customer
UNION ALL
SELECT email FROM supplier;
```

Keeps duplicates.

If duplicate removal is unnecessary, `UNION ALL` communicates that directly and avoids duplicate-elimination semantics.

---

# Part 19 — Views

## 19.1 View Concept

```text
View definition
      ↓
Underlying tables
```

Create:

```sql
CREATE VIEW v_order_summary AS
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders AS o
JOIN customer AS c
    ON c.customer_id = o.customer_id
JOIN order_item AS oi
    ON oi.order_id = o.order_id
GROUP BY
    o.order_id,
    o.order_date,
    c.customer_name;
```

Use:

```sql
SELECT *
FROM v_order_summary
ORDER BY order_total DESC;
```

## 19.2 Why Views

```text
simplify complex query
standardize reporting
hide selected columns
provide abstraction
```

A normal view does not automatically materialize/store the result.

---

# Part 20 — Index Fundamentals

## 20.1 Why Indexes Exist

Without index:

```text
Row1
Row2
Row3
...
Row10,000,000
```

With B-tree concept:

```text
              [50]
            /      \
         [20]      [80]
        /   \      /   \
      ...   ...  ...   ...
```

The ordered structure can reduce rows examined.

## 20.2 InnoDB Clustered Index

InnoDB stores row data in the clustered index organization.

Normally:

```text
PRIMARY KEY
    ↓
clustered B-tree
    ↓
leaf pages contain row data
```

Primary-key design therefore affects table organization.

## 20.3 Secondary Index

Concept:

```text
Secondary index
email
  |
  +--> primary-key value
            |
            v
     clustered row
```

A very wide primary key increases secondary-index entry size.

## 20.4 Create Index

```sql
CREATE INDEX idx_orders_customer
ON orders(customer_id);
```

## 20.5 Composite Index

```sql
CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date);
```

Ordering:

```text
customer_id first
order_date second
```

## 20.6 Leftmost-prefix Principle

For:

```text
(customer_id, order_date, status)
```

leading patterns include:

```text
customer_id
customer_id + order_date
customer_id + order_date + status
```

Filtering only by `status` cannot use the index as though status were the leading key.

Verify with `EXPLAIN`.

## 20.7 Covering Index

If all required query columns exist in an index, MySQL may satisfy the query using that index without fetching full row data.

## 20.8 Selectivity

High selectivity:

```text
email = one row
```

Low selectivity:

```text
active = TRUE for 99% of rows
```

Not every filtered column needs an index.

## 20.9 Index Cost

Indexes cost:

```text
disk
memory
INSERT work
UPDATE work
DELETE work
backup size
```

Indexes are a tradeoff, not free acceleration.

---

# Part 21 — EXPLAIN and Query Plans

## 21.1 EXPLAIN

```sql
EXPLAIN
SELECT
    order_id,
    order_date
FROM orders
WHERE customer_id = 100;
```

Important concepts:

```text
table
access type
possible_keys
chosen key
estimated rows
filtered
Extra
```

## 21.2 Scan vs Indexed Access

A full scan is not always bad.

For:

```text
small table
low-selectivity predicate
most rows needed
```

a scan can be correct.

## 21.3 Composite-index Range

Query:

```sql
SELECT *
FROM orders
WHERE
    customer_id = 100
    AND order_date >= '2026-01-01';
```

Index:

```sql
CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date);
```

Concept:

```text
find customer 100
      ↓
walk date range for that customer
```

## 21.4 EXPLAIN ANALYZE

Where supported:

```sql
EXPLAIN ANALYZE
SELECT ...
```

This executes and reports observed plan behavior.

Use carefully with expensive queries.

## 21.5 Tuning Workflow

```text
Slow SQL
  ↓
capture exact query
  ↓
measure baseline
  ↓
EXPLAIN
  ↓
inspect rows/index/join order
  ↓
change one thing
  ↓
measure again
```

Never tune only from guesses.

---

# Part 22 — Normalization

## 22.1 Bad Spreadsheet Design

```text
OrderID
CustomerName
CustomerAddress
Product1
Product2
Product3
```

Problems:

```text
repeating fields
duplicated customer data
fixed product count
update anomalies
delete anomalies
insert anomalies
```

## 22.2 First Normal Form

Remove repeating groups.

Bad:

```text
product_ids = "10,15,22"
```

Better:

```text
one OrderItem row per product
```

## 22.3 Second Normal Form

With composite key:

```text
(order_id, product_id)
```

attribute:

```text
product_name
```

depends only on `product_id`, not the full key.

Move product name into Product.

## 22.4 Third Normal Form

Bad:

```text
employee_id
department_id
department_name
```

`department_name` depends on `department_id`.

Better:

```text
Employee
 department_id FK

Department
 department_id PK
 department_name
```

## 22.5 Denormalization

Can be justified for:

```text
reporting
precomputed aggregates
read-heavy workloads
distributed systems
```

Document:

```text
source of truth
refresh logic
consistency behavior
```

---

# Part 23 — Transactions and ACID

## 23.1 Transaction

```text
BEGIN
  ↓
create order
  ↓
create order items
  ↓
COMMIT
```

If one critical step fails:

```text
ROLLBACK
```

## 23.2 Atomicity

All or nothing.

```sql
START TRANSACTION;

INSERT INTO orders (...);

INSERT INTO order_item (...);
INSERT INTO order_item (...);

COMMIT;
```

If a line fails:

```sql
ROLLBACK;
```

## 23.3 Consistency

Correct transaction logic plus constraints should move data between valid states.

```text
before
valid inventory

transaction

after
valid inventory
```

The DBMS cannot invent missing business rules; schema/application design remains responsible.

## 23.4 Isolation

```text
Session A        Session B
    |                |
 update inventory    |
    |             read/update
```

Isolation controls what concurrent transactions may observe.

## 23.5 Durability

After a successful commit under configured durability guarantees, committed changes are designed to survive failures.

Redo logging is central to InnoDB crash recovery.

---

# Part 24 — Autocommit and Transaction Control

## 24.1 Autocommit

```sql
SELECT @@autocommit;
```

With autocommit enabled, eligible standalone statements commit automatically unless grouped inside an explicit transaction.

## 24.2 Explicit Transaction

```sql
START TRANSACTION;

UPDATE inventory
SET quantity = quantity - 10
WHERE product_id = 5;

UPDATE inventory
SET quantity = quantity + 10
WHERE product_id = 9;

COMMIT;
```

## 24.3 Rollback

```sql
START TRANSACTION;

UPDATE product
SET unit_price = unit_price * 10;

ROLLBACK;
```

## 24.4 Savepoint

```sql
START TRANSACTION;

UPDATE orders
SET status = 'PROCESSING'
WHERE order_id = 100;

SAVEPOINT after_status;

INSERT INTO audit_log (...);

ROLLBACK TO SAVEPOINT after_status;

COMMIT;
```

A savepoint lets you partially roll back within a larger transaction.


# Part 25 — Isolation Levels

InnoDB supports four standard transaction isolation levels:

```text
READ UNCOMMITTED
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
```

InnoDB commonly defaults to:

```text
REPEATABLE READ
```

Inspect current session:

```sql
SELECT @@transaction_isolation;
```

Set a session:

```sql
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

## 25.1 Dirty Read

Timeline:

```text
Session A
UPDATE salary = 10000
not committed

Session B
reads 10000

Session A
ROLLBACK
```

If B could see the uncommitted value, that is a dirty read.

## 25.2 Non-repeatable Read

```text
Session A:
SELECT price -> 10

Session B:
UPDATE price -> 12
COMMIT

Session A:
SELECT price again
```

If A sees 12 inside the same transaction, the same row was non-repeatable.

## 25.3 Phantom Read

```text
A:
SELECT orders WHERE total > 1000

B:
INSERT new qualifying order
COMMIT

A:
runs predicate again
```

The new matching row illustrates the phantom concept.

## 25.4 Choosing Isolation

Higher isolation may add coordination/locking/serialization cost.

Choose based on:

```text
business correctness
concurrency
read/write pattern
transaction length
```

Never lower isolation merely because "performance is slow" without understanding what anomalies become acceptable.

---

# Part 26 — MVCC

## 26.1 Multi-Version Concurrency Control

Concept:

```text
Row version 1
price = 10
   |
Transaction B updates
   v
Row version 2
price = 12
```

A transaction may continue reading an earlier consistent version while another transaction commits a newer version.

MVCC helps readers and writers coexist without every read requiring a blocking lock.

## 26.2 Read View

Conceptually, a transaction sees an allowed snapshot of committed row versions.

```text
Transaction A snapshot
       |
       +-- row v1 visible
       +-- row v2 too new / not visible yet
```

The exact visibility rules depend on isolation level and statement type.

## 26.3 Undo and Older Versions

Undo information helps reconstruct earlier row versions.

```text
current row
   |
   +--> undo record
          |
          +--> older version
```

Long-running transactions can retain old versions longer and increase purge/undo pressure.

Operational lesson:

```text
Long transaction
      ↓
old versions retained
      ↓
more undo history
      ↓
storage/performance consequences
```

---

# Part 27 — Locking

## 27.1 Row-level Locking

```sql
START TRANSACTION;

UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 100;
```

InnoDB locks the required index/row records until commit or rollback.

## 27.2 Locking Read

```sql
SELECT
    product_id,
    quantity
FROM inventory
WHERE product_id = 100
FOR UPDATE;
```

Use this when an application needs to read a value and then safely update based on that value inside one transaction.

Example:

```text
read inventory 20
   ↓
reserve 5
   ↓
write inventory 15
   ↓
commit
```

Without correct concurrency control, two transactions could both believe the same stock is available.

## 27.3 Shared and Exclusive Concepts

Simplified:

```text
Shared-style access
    compatible readers

Exclusive-style access
    writer prevents conflicting access
```

InnoDB has richer lock types, but this model helps start reasoning.

## 27.4 Index-based Locking

InnoDB locking operates on index records/ranges.

That means a poor query plan can increase locking impact.

Concept:

```text
Good selective index
      ↓
few records visited/locked

No useful index
      ↓
large scan
      ↓
larger lock footprint for modifying/locking statements
```

## 27.5 Gap and Next-key Locks

At some isolation levels and statement types, InnoDB locks gaps/ranges as well as existing index records.

Concept:

```text
Index values:

10      20      30
 |------|-------|

A transaction can protect
a record plus surrounding range
```

This is related to phantom prevention.

## 27.6 Lock Wait

Session A:

```sql
START TRANSACTION;

UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 1;
```

Keep it open.

Session B:

```sql
UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 1;
```

B waits.

The correct question is not just:

```text
"Why is query slow?"
```

It is:

```text
Who owns the lock?
What transaction is open?
Why has it not committed?
```

---

# Part 28 — Deadlocks

## 28.1 Deadlock Cycle

```text
Transaction A
locks Row 1
waits Row 2
       ^
       |
       |
Transaction B
locks Row 2
waits Row 1
```

Neither can continue.

InnoDB detects the cycle and rolls back one transaction so the other can proceed.

## 28.2 Controlled Lab

Session A:

```sql
START TRANSACTION;

UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 1;
```

Session B:

```sql
START TRANSACTION;

UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 2;
```

Then A:

```sql
UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 2;
```

Then B:

```sql
UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 1;
```

One should become the deadlock victim.

## 28.3 Diagnose

```sql
SHOW ENGINE INNODB STATUS\G
```

Look for the latest detected deadlock information.

Map:

```text
Transaction 1
holds X
waits Y

Transaction 2
holds Y
waits X
```

## 28.4 Reduce Deadlocks

Useful practices:

```text
acquire resources in consistent order
keep transactions short
use selective indexes
avoid human interaction while transaction is open
avoid unnecessarily large batch transactions
```

Applications should normally be prepared to retry a deadlock victim when the business operation is safe to retry.

---

# Part 29 — Stored Procedures

## 29.1 Procedure Concept

```text
Application
    |
    | CALL procedure
    v
Stored Procedure
    |
    +-- SQL
    +-- variables
    +-- conditions
    +-- transaction-aware logic
```

Example:

```sql
DELIMITER //

CREATE PROCEDURE GetOrdersByCustomer(
    IN p_customer_id BIGINT
)
BEGIN
    SELECT
        order_id,
        order_date,
        status
    FROM orders
    WHERE customer_id = p_customer_id
    ORDER BY order_date DESC;
END //

DELIMITER ;
```

Call:

```sql
CALL GetOrdersByCustomer(100);
```

## 29.2 Parameters

```text
IN
OUT
INOUT
```

## 29.3 Control Flow

```sql
IF p_quantity <= 0 THEN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Quantity must be positive';
END IF;
```

## 29.4 Set-based vs Row-by-row

Bad tendency:

```text
loop through 1,000,000 rows
update one row each iteration
```

Often better:

```sql
UPDATE product
SET active = FALSE
WHERE discontinued_date < '2025-01-01';
```

Use procedural logic when it adds value, but preserve SQL's set-based strengths.

---

# Part 30 — Stored Functions

Example:

```sql
DELIMITER //

CREATE FUNCTION OrderLineTotal(
    p_quantity INT,
    p_price DECIMAL(12,4)
)
RETURNS DECIMAL(16,4)
DETERMINISTIC
RETURN p_quantity * p_price //

DELIMITER ;
```

Use:

```sql
SELECT
    OrderLineTotal(10, 4.25);
```

Do not hide expensive multi-table queries behind a function that is then executed once per row without testing performance.

---

# Part 31 — Triggers

## 31.1 Trigger Flow

```text
INSERT / UPDATE / DELETE
          ↓
        Trigger
          ↓
automatic additional logic
```

Create audit table:

```sql
CREATE TABLE product_price_audit (
    audit_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    product_id BIGINT NOT NULL,
    old_price DECIMAL(12,4),
    new_price DECIMAL(12,4),
    changed_at TIMESTAMP
        NOT NULL
        DEFAULT CURRENT_TIMESTAMP
);
```

Trigger:

```sql
DELIMITER //

CREATE TRIGGER trg_product_price_update
AFTER UPDATE ON product
FOR EACH ROW
BEGIN
    IF OLD.unit_price <> NEW.unit_price THEN
        INSERT INTO product_price_audit (
            product_id,
            old_price,
            new_price
        )
        VALUES (
            NEW.product_id,
            OLD.unit_price,
            NEW.unit_price
        );
    END IF;
END //

DELIMITER ;
```

## 31.2 Why Triggers Can Become Dangerous

Triggers are implicit.

An application executes:

```sql
UPDATE product ...
```

but the real effect may be:

```text
UPDATE
  ↓
trigger
  ↓
audit insert
  ↓
another constraint
```

Document triggers clearly and avoid hiding large business workflows inside them.

---

# Part 32 — Event Scheduler

Inspect:

```sql
SHOW VARIABLES LIKE 'event_scheduler';
```

Example:

```sql
CREATE EVENT ev_clean_temp_logs
ON SCHEDULE EVERY 1 DAY
DO
    DELETE FROM temporary_event_log
    WHERE created_at < NOW() - INTERVAL 30 DAY;
```

Choose one owner for recurring work:

```text
MySQL Event Scheduler
OS scheduler
application scheduler
workflow platform
```

Do not schedule the same responsibility in multiple places.

---

# Part 33 — MySQL Accounts and Authentication

## 33.1 Account Identity Includes Host

MySQL accounts are identified as:

```text
'user'@'host'
```

Examples:

```text
'appuser'@'localhost'
'appuser'@'10.60.%'
```

These are distinct accounts.

This explains many "works locally but not remotely" incidents.

## 33.2 Create User

Lab:

```sql
CREATE USER
    'reportuser'@'10.60.%'
IDENTIFIED BY 'Lab-Only-Password-Change-Me';
```

In production:

```text
do not put reusable passwords in scripts
do not commit them to Git
prefer approved secret management
```

## 33.3 Inspect Accounts

```sql
SELECT
    user,
    host
FROM mysql.user
ORDER BY user, host;
```

The `mysql` system database contains security-sensitive information.

Ordinary application users should not receive direct access to privilege tables.

## 33.4 Authentication Plugins

MySQL supports pluggable authentication.

A client that cannot authenticate may be:

```text
old/incompatible client
unsupported auth method
wrong account selected
wrong TLS requirements
```

Do not downgrade authentication blindly just to satisfy old software.

---

# Part 34 — Privileges

## 34.1 Least Privilege

Application needs:

```text
SELECT
INSERT
UPDATE
DELETE on selected tables
```

It usually does not need:

```text
CREATE USER
DROP DATABASE
server administration
```

## 34.2 GRANT

```sql
GRANT
    SELECT,
    INSERT,
    UPDATE
ON manufacturing.orders
TO 'appuser'@'10.60.%';
```

## 34.3 REVOKE

```sql
REVOKE UPDATE
ON manufacturing.orders
FROM 'appuser'@'10.60.%';
```

## 34.4 Inspect

```sql
SHOW GRANTS
FOR 'appuser'@'10.60.%';
```

Security design:

```text
Identity
   ↓
Role / Privilege
   ↓
Object
   ↓
Allowed operation
```

---

# Part 35 — Roles

## 35.1 Create Role

```sql
CREATE ROLE 'report_reader';
```

Grant to role:

```sql
GRANT SELECT
ON manufacturing.*
TO 'report_reader';
```

Assign to user:

```sql
GRANT 'report_reader'
TO 'reportuser'@'10.60.%';
```

Set default:

```sql
SET DEFAULT ROLE 'report_reader'
TO 'reportuser'@'10.60.%';
```

Visualization:

```text
reportuser
    ↓
report_reader
    ↓
SELECT on manufacturing.*
```

Roles simplify privilege administration across many accounts.

---

# Part 36 — MySQL Configuration

## 36.1 Configuration Layers

Possible sources:

```text
my.cnf / my.ini
command-line options
server system variables
persisted system settings where supported
```

Paths depend on OS/package.

Inspect:

```sql
SHOW VARIABLES LIKE 'port';
SHOW VARIABLES LIKE 'datadir';
SHOW VARIABLES LIKE 'max_connections';
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
```

## 36.2 Dynamic vs Startup Variables

Some values can change online.

Some require restart or have special persistence behavior.

Never assume:

```sql
SET GLOBAL variable = value;
```

means:

```text
survives reboot
```

Always verify current documentation.

## 36.3 Bind Address

Network binding concept:

```text
127.0.0.1
local connections only

specific private IP
controlled network exposure

0.0.0.0
all local interfaces
```

Do not expose MySQL to untrusted networks simply because remote access is convenient.

## 36.4 max_connections

```text
Too low
    legitimate clients rejected

Too high
    resource exhaustion / overload
```

Before increasing it, inspect:

```text
connection leaks
application pool size
query duration
traffic
server capacity
```

---

# Part 37 — InnoDB Storage Architecture

## 37.1 Buffer Pool

The buffer pool caches table/index pages.

```text
Query
 ↓
Buffer Pool
  | hit
  +------> memory
  |
  | miss
  v
Disk read
  |
  v
Buffer Pool
```

Inspect:

```sql
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
```

## 37.2 Pages and Tablespaces

Concept:

```text
Tablespace
    ↓
Pages
    ↓
Rows / Index Records
```

Do not manipulate InnoDB data files directly with ordinary filesystem operations as an administration shortcut.

## 37.3 Dirty Page

```text
Disk page v1
    ↓ loaded
Buffer Pool page v1
    ↓ UPDATE
Buffer Pool page v2 [dirty]
    ↓ later flush
Disk page v2
```

## 37.4 Redo Log

Redo supports crash recovery.

```text
Transaction
    |
    +--> page change in memory
    |
    +--> redo record
              |
              v
           redo log
```

If MySQL crashes before all dirty pages reach data files, redo can replay required changes during recovery.

## 37.5 Undo

Undo supports:

```text
rollback
MVCC older versions
consistent reads
```

Visualization:

```text
Current row
    |
    +--> Undo record
           |
           +--> Earlier version
```

## 37.6 Redo vs Binary Log

Very important:

```text
InnoDB Redo
    crash recovery inside InnoDB

Binary Log
    server-level change/event stream used for
    replication and PITR workflows
```

They solve different problems.

---

# Part 38 — MySQL Logging

## 38.1 Error Log

Useful for:

```text
startup
shutdown
crash recovery
configuration errors
server failures
```

## 38.2 General Query Log

Can record broad statement activity.

Risks:

```text
very high volume
performance overhead
sensitive data exposure
```

Do not leave enabled casually.

## 38.3 Slow Query Log

Inspect:

```sql
SHOW VARIABLES LIKE 'slow_query_log';
SHOW VARIABLES LIKE 'long_query_time';
```

Use it to identify candidate slow statements.

## 38.4 Binary Log

Used for:

```text
replication
point-in-time recovery
```

Binary-log retention is part of recovery design.

---

# Part 39 — Backup Fundamentals

## 39.1 A Backup Strategy Is a Recovery Strategy

Questions:

```text
What data?
How often?
How consistent?
How long retained?
Encrypted?
Stored off-server?
Restore tested?
RPO?
RTO?
```

A file named `backup.sql` is not proof that recovery will work.

## 39.2 Logical Backup

Logical backup exports SQL/object/data representations.

Common tool:

```text
mysqldump
```

Advantages:

```text
portable
selective
human-readable-ish SQL
```

Tradeoffs:

```text
large dumps can be slow
restore can be slow
```

## 39.3 Physical Backup

Copies database storage using a consistency-aware supported method.

Often better suited to large datasets.

Never assume copying live `/var/lib/mysql` is a valid backup.

## 39.4 Hot vs Cold

```text
Cold:
database stopped / no writes

Hot:
database remains available
```

The backup method must preserve consistency.

---

# Part 40 — mysqldump

## 40.1 Full Database

```bash
mysqldump \
  -u backupuser \
  -p \
  manufacturing \
  > manufacturing.sql
```

Use a dedicated backup account with only required privileges.

## 40.2 Schema Only

```bash
mysqldump \
  -u backupuser \
  -p \
  --no-data \
  manufacturing \
  > manufacturing_schema.sql
```

## 40.3 Data Only

```bash
mysqldump \
  -u backupuser \
  -p \
  --no-create-info \
  manufacturing \
  > manufacturing_data.sql
```

## 40.4 Restore Test

Create disposable restore database:

```sql
CREATE DATABASE manufacturing_restore;
```

Then:

```bash
mysql \
  -u restoreuser \
  -p \
  manufacturing_restore \
  < manufacturing.sql
```

Verify:

```sql
SELECT COUNT(*) FROM product;
SELECT COUNT(*) FROM orders;
```

A backup should be judged by successful recovery, not only successful backup command exit.

---

# Part 41 — Point-in-Time Recovery

## 41.1 PITR Architecture

```text
Full Backup 01:00
      |
      +-- binlog events 01:00–06:00
      +-- binlog events 06:00–11:00
      +-- binlog events 11:00–11:20
      |
      X accidental DELETE at 11:20
```

Recovery concept:

```text
restore full backup
       +
replay binary logs
       +
stop before unwanted change
```

## 41.2 Why PITR Needs Planning

You need:

```text
valid base backup
binary logs
retention
time/position/GTID information
tested restore procedure
```

Never learn PITR for the first time during a production outage.

---

# Part 42 — Replication Fundamentals

## 42.1 Source and Replica

```text
Source
  |
  | binary-log changes
  v
Replica
```

Modern terminology uses **source** and **replica**.

## 42.2 Replication Pipeline

Simplified:

```text
Source Transaction
      ↓
Binary Log
      ↓
Replica Receiver
      ↓
Relay / Replication Pipeline
      ↓
Replica Applier
      ↓
Replica Data
```

## 42.3 Use Cases

```text
read scaling
reporting
HA building block
migration
geographic copy
```

## 42.4 Replication Is Not Backup

If the source executes:

```sql
DELETE FROM orders;
```

the replica may correctly reproduce the same destructive change.

Independent backups are still required.

## 42.5 GTID

Global Transaction Identifier:

```text
Transaction
   |
   +-- unique GTID
```

GTIDs help track which transactions have executed across replication topology.

They can support auto-positioning rather than manually managing only binary-log file/position.

## 42.6 Replication Lag

```text
Source latest:
12:00:10

Replica applied:
12:00:06
```

Lag = about 4 seconds conceptually.

Causes:

```text
network
large transaction
slow disk
CPU pressure
locks
under-sized replica
```

## 42.7 Read-after-write Problem

Application:

```text
WRITE -> source
READ  -> replica immediately
```

With asynchronous replication:

```text
new row may not yet exist on replica
```

Application architecture must understand consistency requirements.

---

# Part 43 — High Availability Foundations

## 43.1 Replication vs HA

```text
Replication
copies changes

High Availability
detects failure
protects correctness
selects healthy writer
redirects clients
```

Having a replica does not automatically create failover.

## 43.2 Group Replication

Concept:

```text
        Node1
       /     \
    Node2 --- Node3
```

Group members coordinate replicated transactions and membership.

Important concerns:

```text
quorum
network latency
failure domains
transaction compatibility
consistency
```

## 43.3 InnoDB Cluster

Concept:

```text
Application
     |
MySQL Router
     |
 +---+---+
 |   |   |
N1  N2  N3
Group Replication
```

Production HA still needs:

```text
backups
monitoring
network design
failure-domain design
application retry behavior
```

---

# Part 44 — Performance Schema

## 44.1 Purpose

Performance Schema provides instrumentation for:

```text
statements
waits
threads
transactions
locks
memory
connections
```

Explore:

```sql
SHOW TABLES
FROM performance_schema;
```

## 44.2 Query Pattern Analysis

Rather than analyze each literal statement:

```text
SELECT * FROM product WHERE product_id = 1
SELECT * FROM product WHERE product_id = 2
SELECT * FROM product WHERE product_id = 3
```

statement digest concepts let you think in terms of:

```text
SELECT ... WHERE product_id = ?
```

This makes workload analysis more useful.

---

# Part 45 — sys Schema

The `sys` schema exposes easier diagnostic views over lower-level metadata and Performance Schema.

Inspect:

```sql
SHOW FULL TABLES
FROM sys;
```

Use the views available in your installed version rather than memorizing an old list from a tutorial.

Typical diagnostic areas:

```text
statements
I/O
schema/index usage
sessions
memory
```

---

# Part 46 — Monitoring

## 46.1 Infrastructure Metrics

Start with:

```text
CPU
RAM
disk latency
disk capacity
network
```

Then MySQL:

```text
connections
queries
slow statements
buffer-pool behavior
locks
deadlocks
replication lag
```

## 46.2 Connections

```sql
SHOW STATUS LIKE 'Threads_connected';
SHOW VARIABLES LIKE 'max_connections';
```

## 46.3 Active Sessions

```sql
SHOW PROCESSLIST;
```

Or:

```sql
SELECT *
FROM performance_schema.processlist;
```

## 46.4 InnoDB Status

```sql
SHOW ENGINE INNODB STATUS\G
```

Useful areas include:

```text
transactions
deadlocks
semaphores
I/O
buffer pool
```

## 46.5 Monitoring Mental Model

```text
User reports slowness
       ↓
Is server resource constrained?
       ↓
Which SQL is slow?
       ↓
CPU or wait/lock/I/O?
       ↓
Execution plan?
       ↓
Data/index design?
```

---

# Part 47 — Troubleshooting Scenarios

## 47.1 Cannot Connect

Check:

```text
mysqld running?
 ↓
listener?
 ↓
route?
 ↓
firewall?
 ↓
bind address?
 ↓
user@host?
 ↓
password/auth?
 ↓
TLS?
```

Linux:

```bash
systemctl status mysqld
ss -tlnp | grep 3306
```

MySQL:

```sql
SELECT user, host
FROM mysql.user;
```

## 47.2 Access Denied

Possible:

```text
wrong password
wrong host-specific account
missing privilege
authentication mismatch
TLS requirement
```

Inspect:

```sql
SHOW GRANTS
FOR 'appuser'@'10.60.%';
```

## 47.3 Duplicate Key

Do not remove a UNIQUE constraint just to make the error disappear.

Ask:

```text
Is duplicate legitimate?
Is application retrying insert?
Is business identifier wrong?
```

## 47.4 Foreign-key Failure

Possible:

```text
missing parent
invalid delete
wrong referenced value
schema mismatch
```

Inspect:

```sql
SHOW CREATE TABLE order_item\G
```

## 47.5 Lock Wait

Questions:

```text
Which transaction owns the lock?
How long open?
What SQL?
Does query use useful index?
Why is commit delayed?
```

## 47.6 Deadlock

```sql
SHOW ENGINE INNODB STATUS\G
```

Then map the lock cycle.

## 47.7 Slow Query

Workflow:

```sql
EXPLAIN
SELECT ...;
```

Then inspect:

```text
rows
index
join predicates
sorting/grouping
data distribution
locks/waits
```

Do not tune by increasing hardware first.

## 47.8 Disk Full

OS:

```bash
df -h
```

Inspect MySQL data directory setting:

```sql
SHOW VARIABLES LIKE 'datadir';
```

Do **not** delete unknown files inside the MySQL data directory.

## 47.9 Too Many Connections

```sql
SHOW STATUS LIKE 'Threads_connected';
SHOW VARIABLES LIKE 'max_connections';
SHOW PROCESSLIST;
```

Possible root causes:

```text
connection leak
poor pooling
slow queries
traffic spike
database overloaded
```

Increasing the limit can make overload worse.

## 47.10 Replica Lag

Investigate:

```text
source transaction size
network
replica CPU
replica disk
locks
apply throughput
```

Connected replication does not guarantee fresh data.

---

# Part 48 — Security Hardening

## 48.1 Network Segmentation

Preferred:

```text
Internet
   X
   |
Application Tier
      |
private network
      |
MySQL
```

Avoid public database exposure.

## 48.2 Separate Accounts

```text
appuser
reportuser
backupuser
replication user
named DBA account
```

Different responsibilities need different privileges.

## 48.3 Avoid Remote Root

Use controlled, named administrative access rather than enabling unrestricted root login from arbitrary hosts.

## 48.4 TLS

Protect database traffic in transit.

Concept:

```text
Client
  |
TLS
  |
MySQL Server
```

Production clients should validate certificate identity/trust according to architecture.

## 48.5 Secret Management

Bad:

```python
password = "ProdPassword123"
```

Better:

```text
Application
   ↓
Secret Store
   ↓
credential
   ↓
MySQL
```

## 48.6 Patching

```text
review update
   ↓
compatibility test
   ↓
backup / rollback
   ↓
maintenance
   ↓
upgrade
   ↓
application + replication validation
```

## 48.7 Backup Security

Backups contain production data.

Protect:

```text
encryption
access control
off-host storage
retention
secure deletion
restore authorization
```

---

# Part 49 — Complete MySQL Troubleshooting Workflow

When any database incident occurs, use this hierarchy:

```text
1. Business symptom
       ↓
2. Client/application
       ↓
3. DNS/network
       ↓
4. MySQL connection/authentication
       ↓
5. SQL correctness
       ↓
6. Transaction/lock state
       ↓
7. Query plan/index
       ↓
8. InnoDB memory/storage
       ↓
9. OS resources
       ↓
10. Replication/HA
```

Example:

```text
Symptom:
Dashboard times out.

Check:
1. Can app connect?
2. Are connections exhausted?
3. Which query is slow?
4. Is it blocked?
5. EXPLAIN?
6. Disk latency?
7. Replica lag?
```

This prevents random changes.

---


# Enhanced Deep-Study Layer — MySQL Database Engineering

The original course is preserved below. This enhanced layer extends it into a deeper database-engineering guide covering relational design, SQL semantics, window functions, generated columns, JSON, indexing strategy, optimizer behavior, transaction internals, locking, metadata locks, online DDL, partitioning, security, backup/recovery, replication, high availability, observability, and production troubleshooting.

The central engineering model is:

```text
Business Rule
    ↓
Logical Data Model
    ↓
Physical Schema
    ↓
Constraints
    ↓
SQL Workload
    ↓
Optimizer
    ↓
Indexes / Access Paths
    ↓
InnoDB Transaction Engine
    ↓
Memory / Redo / Undo / Tablespaces
    ↓
Storage + Backup + Replication
    ↓
Monitoring + Recovery
```

The operational rule throughout this course is:

```text
Do not tune a database by guessing.
Measure → explain → change one thing → verify.
```

---

## Enhanced Deep Dive 1 — Logical vs Physical Database Design

Logical design answers:

```text
What entities exist?
What facts belong to each entity?
What relationships exist?
What business rules must always hold?
```

Physical design answers:

```text
Which MySQL types?
Which primary keys?
Which indexes?
Which partitioning strategy?
Which storage engine?
Which charset/collation?
```

Example:

```text
Logical:
Order has many OrderItems

Physical:
orders(order_id BIGINT PK)
order_item(order_id BIGINT FK, line_no INT, ...)
PRIMARY KEY(order_id, line_no)
```

Do not choose indexes before understanding the logical access patterns.

---

## Enhanced Deep Dive 2 — Strong Entity Identity

A good table should answer:

```text
What makes one row uniquely itself?
```

Bad:

```text
customer_name as primary key
```

because names can:

```text
change
repeat
have spelling variations
```

Better:

```sql
customer_id BIGINT AUTO_INCREMENT PRIMARY KEY,
customer_code VARCHAR(50) NOT NULL UNIQUE
```

This separates internal row identity from business identity.

---

## Enhanced Deep Dive 3 — Business Keys Still Matter

Surrogate keys do not remove business uniqueness requirements.

Example:

```sql
CREATE TABLE supplier (
    supplier_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    supplier_code VARCHAR(30) NOT NULL UNIQUE,
    supplier_name VARCHAR(150) NOT NULL
);
```

Without `UNIQUE(supplier_code)`, the database can still hold:

```text
SUP-001
SUP-001
SUP-001
```

which may violate the business model.

---

## Enhanced Deep Dive 4 — Relationship Optionality

A relationship is not only:

```text
1:N
```

It also has optionality.

Example:

```text
Employee may have zero or one manager
```

Implementation:

```sql
manager_id BIGINT NULL
```

with FK to `employee(employee_id)`.

Mandatory department:

```sql
department_id BIGINT NOT NULL
```

Optionality should be explicit in schema.

---

## Enhanced Deep Dive 5 — ON DELETE and ON UPDATE Rules

Foreign key actions include concepts such as:

```text
RESTRICT / NO ACTION
CASCADE
SET NULL
```

Example:

```sql
CONSTRAINT fk_employee_department
FOREIGN KEY (department_id)
REFERENCES department(department_id)
ON DELETE RESTRICT
```

Before choosing `CASCADE`, ask:

```text
Should deleting parent truly delete all children automatically?
```

Cascades can be correct, but they increase hidden impact.

---

## Enhanced Deep Dive 6 — Junction Table Design

A many-to-many relationship often becomes a business entity itself.

Example:

```text
Inspection N ↔ N Defect
```

Junction:

```sql
CREATE TABLE inspection_defect (
    inspection_id BIGINT NOT NULL,
    defect_id BIGINT NOT NULL,
    defect_qty INT NOT NULL CHECK (defect_qty > 0),
    PRIMARY KEY (inspection_id, defect_id)
);
```

The junction stores facts about the relationship.

---

## Enhanced Deep Dive 7 — Normal Forms Are About Dependencies

Normalization is not "split tables until small."

It is about dependency correctness.

Example:

```text
employee_id → department_id
department_id → department_name
```

Therefore:

```text
employee_id → department_name
```

is transitive.

Store `department_name` in `department`, not repeatedly in `employee`.

---

## Enhanced Deep Dive 8 — Update Anomaly

Bad table:

```text
Employee
employee_id
employee_name
department_id
department_name
```

If department changes name:

```text
update 2,000 employee rows
```

Miss one row:

```text
inconsistent department names
```

Normalization reduces this anomaly.

---

## Enhanced Deep Dive 9 — Insert Anomaly

Bad design:

```text
cannot add a department
unless an employee exists
```

because department data is stored only in employee rows.

Separate `department` table allows independent lifecycle.

---

## Enhanced Deep Dive 10 — Delete Anomaly

Bad design:

```text
last employee leaves Department 10
```

Deleting that row also deletes the only stored copy of:

```text
department name
department code
```

Separate entity tables prevent this accidental information loss.

---

## Enhanced Deep Dive 11 — Denormalization Must Have Ownership

If you store derived data:

```text
order_total
```

in addition to:

```text
SUM(order_item.quantity * order_item.unit_price)
```

then define:

```text
source of truth
update mechanism
reconciliation method
failure behavior
```

Without this, derived columns drift.

---

## Enhanced Deep Dive 12 — Character Set vs Collation

Character set:

```text
How characters are encoded
```

Collation:

```text
How strings compare and sort
```

Example questions:

```text
case-sensitive?
accent-sensitive?
language-specific ordering?
binary comparison?
```

Inspect:

```sql
SHOW VARIABLES LIKE 'character_set_server';
SHOW VARIABLES LIKE 'collation_server';
```

Schema defaults should be intentional.

---

## Enhanced Deep Dive 13 — UTF-8 and `utf8mb4`

Modern MySQL applications should understand `utf8mb4`.

Why?

Because full Unicode includes characters outside the older 3-byte UTF-8 subset historically called `utf8` in MySQL.

Concept:

```text
utf8mb4
→ full UTF-8 character range
```

Always verify application/connector compatibility and collation needs.

---

## Enhanced Deep Dive 14 — Collation Can Change Equality

Two strings can compare differently under different collations.

Example concepts:

```text
'A' vs 'a'
'é' vs 'e'
```

A case-insensitive collation may treat values equal.

This affects:

```text
UNIQUE constraints
JOINs
ORDER BY
search behavior
```

Data correctness depends on choosing the intended collation.

---

## Enhanced Deep Dive 15 — Integer Range and Signedness

Choosing:

```text
TINYINT
SMALLINT
INT
BIGINT
```

should follow domain range.

`UNSIGNED` changes range behavior.

Do not use `BIGINT` everywhere automatically.

Trade-offs include:

```text
index size
buffer-pool use
cache density
```

but correctness comes first.

---

## Enhanced Deep Dive 16 — DECIMAL Precision and Scale

```sql
DECIMAL(12,4)
```

means conceptually:

```text
12 total digits
4 after decimal point
```

Suitable for exact decimal values.

Avoid storing financial amounts in approximate floating point unless the domain accepts approximation.

---

## Enhanced Deep Dive 17 — TIMESTAMP vs DATETIME

Both represent date/time values but have different semantics and historical behaviors.

Design questions:

```text
Should value represent absolute instant?
Should application preserve entered wall-clock value?
What timezone conversions occur?
What date range is required?
```

Store timezone strategy in application architecture, not as an afterthought.

---

## Enhanced Deep Dive 18 — Time Zones

MySQL session time zone can influence temporal behavior.

Inspect:

```sql
SELECT @@session.time_zone, @@global.time_zone;
```

Production systems should define:

```text
database storage convention
application timezone
reporting timezone
conversion boundary
```

A timestamp without timezone policy creates ambiguous analytics.

---

## Enhanced Deep Dive 19 — TEXT and BLOB

Use:

```text
TEXT
→ character data

BLOB
→ binary data
```

Large values affect:

```text
row access
memory
network transfer
backup size
indexability
```

Do not store large binary assets in the database automatically without architectural justification.

---

## Enhanced Deep Dive 20 — ENUM and SET Trade-offs

`ENUM` can enforce a small set of values.

But changes to the allowed domain may require schema changes.

Alternative:

```text
lookup table
+
foreign key
```

is often more flexible.

Choose based on:

```text
stability
governance
reporting
schema-change frequency
```

---

## Enhanced Deep Dive 21 — Generated Columns

A generated column derives a value from other columns.

Concept:

```text
quantity
unit_price
   ↓
line_total
```

Example:

```sql
CREATE TABLE demo_line (
    quantity INT NOT NULL,
    unit_price DECIMAL(12,4) NOT NULL,
    line_total DECIMAL(16,4)
        GENERATED ALWAYS AS (quantity * unit_price) STORED
);
```

Generated columns can support:

```text
consistency
indexing derived expressions
query simplification
```

Use only for deterministic logic appropriate to the database.

---

## Enhanced Deep Dive 22 — Virtual vs Stored Generated Columns

Conceptually:

```text
VIRTUAL
→ calculated when needed

STORED
→ materialized in table storage
```

Trade-offs:

```text
read CPU
write CPU
disk
indexing requirements
```

Test real workload rather than assuming one is always better.

---

## Enhanced Deep Dive 23 — JSON Is Not a Replacement for Schema

Good JSON use:

```text
machine-specific telemetry payload
variable device attributes
external API response copy
```

Poor JSON use:

```text
all customer/order/product data hidden in one JSON column
```

Relational data should remain relational where relationships and constraints matter.

---

## Enhanced Deep Dive 24 — JSON Extraction

Example:

```sql
SELECT
    event_id,
    JSON_EXTRACT(payload, '$.temperature') AS temperature
FROM machine_event;
```

Short operator syntax may be available depending on context/version.

The key lesson:

```text
JSON path
→ extract structured value
```

Repeated JSON extraction in large scans can become expensive.

---

## Enhanced Deep Dive 25 — JSON_TABLE Awareness

Modern MySQL supports relational projection of JSON content using `JSON_TABLE` in supported versions.

Concept:

```text
JSON array
   ↓
JSON_TABLE
   ↓
relational rows/columns
```

Useful when semi-structured data must be queried relationally.

Still validate workload cost and schema governance.

---

## Enhanced Deep Dive 26 — Indexing JSON via Generated Columns

Pattern:

```text
JSON payload
  ↓ generated column
  ↓ index
```

Example concept:

```sql
ALTER TABLE machine_event
ADD COLUMN machine_state VARCHAR(30)
    GENERATED ALWAYS AS (
        JSON_UNQUOTE(JSON_EXTRACT(payload, '$.state'))
    ) STORED,
ADD INDEX idx_machine_state (machine_state);
```

This can turn repeated JSON scans into indexed access.

---

## Enhanced Deep Dive 27 — SQL Three-Valued Logic

SQL predicates can evaluate to:

```text
TRUE
FALSE
UNKNOWN
```

Example:

```sql
NULL = 5
```

is not true or false in ordinary SQL logic; it is unknown.

Therefore:

```sql
WHERE manager_id = NULL
```

matches nothing.

Use:

```sql
IS NULL
IS NOT NULL
```

---

## Enhanced Deep Dive 28 — NULL-Safe Equality

MySQL has a NULL-safe comparison operator.

Concept:

```text
normal equality
NULL = NULL → UNKNOWN

NULL-safe equality
NULL <=> NULL → TRUE
```

Use only when the business logic really wants NULL values treated as comparable.

---

## Enhanced Deep Dive 29 — CASE Expressions

Example:

```sql
SELECT
    order_id,
    CASE
        WHEN total_amount >= 10000 THEN 'LARGE'
        WHEN total_amount >= 1000 THEN 'MEDIUM'
        ELSE 'SMALL'
    END AS order_size
FROM orders;
```

CASE is set-based conditional logic.

Prefer it over row-by-row procedural loops for many classification tasks.

---

## Enhanced Deep Dive 30 — COALESCE

```sql
SELECT
    customer_name,
    COALESCE(email, 'NO_EMAIL') AS email_display
FROM customer;
```

`COALESCE` returns the first non-NULL expression.

Be careful not to hide meaningful missing-data problems by replacing every NULL automatically.

---

## Enhanced Deep Dive 31 — Window Functions

Window functions calculate across related rows without collapsing them like `GROUP BY`.

Example:

```sql
SELECT
    customer_id,
    order_id,
    order_date,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_date DESC
    ) AS rn
FROM orders;
```

This can identify the latest order per customer.

---

## Enhanced Deep Dive 32 — Aggregate vs Window Function

`GROUP BY`:

```text
many input rows
→ fewer grouped rows
```

Window function:

```text
many input rows
→ same number of output rows
+
analytics column
```

Example:

```sql
SELECT
    order_id,
    customer_id,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY customer_id
    ) AS customer_total
FROM orders;
```

---

## Enhanced Deep Dive 33 — RANK vs DENSE_RANK vs ROW_NUMBER

Given values:

```text
100
100
90
```

Conceptually:

```text
ROW_NUMBER
1 2 3

RANK
1 1 3

DENSE_RANK
1 1 2
```

Choose based on reporting semantics.

---

## Enhanced Deep Dive 34 — Running Total

Example:

```sql
SELECT
    order_date,
    total_amount,
    SUM(total_amount) OVER (
        ORDER BY order_date, order_id
        ROWS BETWEEN UNBOUNDED PRECEDING
                 AND CURRENT ROW
    ) AS running_sales
FROM orders;
```

Deterministic ordering matters when multiple rows share the same date.

---

## Enhanced Deep Dive 35 — LAG and LEAD

Example:

```sql
SELECT
    run_date,
    good_qty,
    LAG(good_qty) OVER (
        ORDER BY run_date
    ) AS previous_good_qty
FROM production_run;
```

Useful for:

```text
change detection
trend analysis
previous/next comparison
```

---

## Enhanced Deep Dive 36 — Window Frame Awareness

Window frame controls which rows contribute.

Examples:

```text
ROWS BETWEEN ...
RANGE BETWEEN ...
```

Do not assume default frame matches your running-total intent.

Always specify when correctness matters.

---

## Enhanced Deep Dive 37 — SARGability

A SARGable predicate can use an index efficiently.

Good:

```sql
WHERE order_date >= '2026-01-01'
```

Potentially worse:

```sql
WHERE YEAR(order_date) = 2026
```

because applying a function to the indexed column can prevent simple range access.

Rewrite:

```sql
WHERE order_date >= '2026-01-01'
  AND order_date <  '2027-01-01'
```

Then verify with `EXPLAIN`.

---

## Enhanced Deep Dive 38 — Prefix Indexes

Long string columns can sometimes use prefix indexing.

Concept:

```sql
CREATE INDEX idx_email_prefix
ON customer(email(20));
```

Trade-off:

```text
smaller index
but
less selectivity
```

Do not choose prefix length without measuring distinctness and query requirements.

---

## Enhanced Deep Dive 39 — Descending Indexes

Modern MySQL supports descending key parts in supported versions.

Concept:

```sql
CREATE INDEX idx_order_customer_date_desc
ON orders(customer_id, order_date DESC);
```

Can align with query ordering.

Always confirm plan behavior with `EXPLAIN`.

---

## Enhanced Deep Dive 40 — Invisible Indexes

Invisible indexes let you test impact of removing an index without immediately dropping it.

Concept:

```text
index remains maintained
optimizer ignores it by default
```

Use case:

```text
Can we remove this apparently unused index safely?
```

This is useful for controlled tuning.

---

## Enhanced Deep Dive 41 — Functional Indexing Awareness

When supported, expression-based indexing can improve queries that filter on computed expressions.

Alternative design:

```text
generated column
+
normal index
```

This is often easier to reason about explicitly.

Always verify version and deterministic-expression requirements.

---

## Enhanced Deep Dive 42 — Cardinality and Selectivity

Cardinality:

```text
number of distinct values
```

High cardinality:

```text
email
order_id
```

Low cardinality:

```text
active boolean
status with three values
```

Optimizer uses statistics to estimate row counts.

Wrong estimates can lead to poor plans.

---

## Enhanced Deep Dive 43 — Histograms Awareness

MySQL can maintain column histograms in supported versions to help estimate data distribution where an index may not exist or distribution is skewed.

Use when:

```text
optimizer estimates are badly wrong
distribution is nonuniform
```

Do not create histograms everywhere blindly.

---

## Enhanced Deep Dive 44 — Statistics Freshness

Optimizer decisions depend on statistics.

After major data distribution changes, estimates can differ from reality.

Useful mindset:

```text
query slow after huge data load?
→ inspect plan + estimates
→ consider statistics state
```

Do not immediately force indexes before understanding estimates.

---

## Enhanced Deep Dive 45 — `EXPLAIN FORMAT=JSON`

JSON-formatted explain can expose more detailed plan structure.

Example:

```sql
EXPLAIN FORMAT=JSON
SELECT ...
```

Useful for:

```text
join nesting
cost estimates
chosen access path
attached conditions
```

Human readability varies; learn the core plan concepts first.

---

## Enhanced Deep Dive 46 — Tree Explain Awareness

Recent MySQL versions support tree-oriented plan output in relevant contexts.

Concept:

```text
nested loop
 ├─ index lookup customer
 └─ index lookup orders
```

Tree representation can make operator relationships easier to visualize than tabular output.

---

## Enhanced Deep Dive 47 — EXPLAIN ANALYZE Caution

`EXPLAIN ANALYZE` executes the query.

Therefore:

```text
safe SELECT
→ okay in controlled environment

expensive query
→ can still consume real resources
```

Do not run it casually on production with unbounded expensive queries.

---

## Enhanced Deep Dive 48 — Covering Index Trade-off

Query:

```sql
SELECT customer_id, order_date, status
FROM orders
WHERE customer_id = ?
ORDER BY order_date DESC;
```

A covering index could include all required columns.

Benefit:

```text
fewer clustered-row lookups
```

Cost:

```text
larger index
more write work
more memory/disk
```

Cover intentionally, not reflexively.

---

## Enhanced Deep Dive 49 — Primary Key Width Matters

InnoDB secondary indexes store the primary-key value.

Therefore:

```text
very wide PK
  ↓
every secondary index wider
```

A compact stable PK can reduce total index size.

Correctness and business requirements still come first.

---

## Enhanced Deep Dive 50 — Random vs Sequential Primary Keys

Sequential integer keys:

```text
localized insert pattern
```

Random identifiers:

```text
insert spread across B-tree
potential page splits/cache effects
```

Distributed systems may need globally unique identifiers.

Choose based on architecture, not one-size-fits-all rules.

---

## Enhanced Deep Dive 51 — Composite Index Ordering

Given:

```text
WHERE customer_id = ?
AND order_date BETWEEN ? AND ?
ORDER BY order_date
```

Index:

```text
(customer_id, order_date)
```

matches:

```text
equality first
then range/order
```

A common heuristic:

```text
equality predicates
→ range
→ sort/group support
```

but always verify with the real query/data distribution.

---

## Enhanced Deep Dive 52 — Redundant Indexes

Indexes can overlap.

Example:

```text
INDEX(customer_id)
INDEX(customer_id, order_date)
```

The second may already support some `customer_id` queries.

But do not drop the first automatically.

Check:

```text
workload
covering behavior
index size
optimizer choices
```

---

## Enhanced Deep Dive 53 — Indexes and Writes

Every INSERT may update:

```text
clustered index
+
all relevant secondary indexes
```

Every UPDATE can require index maintenance.

Write-heavy tables can suffer from over-indexing.

Index review should include:

```text
read benefit
write cost
storage cost
backup cost
```

---

## Enhanced Deep Dive 54 — Temporary Tables

MySQL may use temporary tables for operations such as:

```text
GROUP BY
DISTINCT
sorting
complex intermediate results
```

Some remain in memory; some spill to disk depending on data and server settings.

Investigate when a query unexpectedly consumes I/O.

---

## Enhanced Deep Dive 55 — Filesort Meaning

`Using filesort` in an execution plan does not necessarily mean a literal OS file.

It means MySQL performs a sort operation not satisfied directly by index ordering.

Sorting can be perfectly acceptable.

The question is:

```text
How many rows?
How often?
Memory/disk?
Can index order help?
```

---

## Enhanced Deep Dive 56 — Join Order

For multiple tables, optimizer chooses a join order.

Concept:

```text
Start with selective table
  ↓
join small result
  ↓
join next table
```

A poor estimate can make it start with a huge intermediate result.

Use:

```text
EXPLAIN
row estimates
indexes
statistics
```

before forcing hints.

---

## Enhanced Deep Dive 57 — Join Buffer Awareness

When suitable indexes are absent, MySQL may use join buffering strategies.

That can increase memory/CPU and scanned rows.

The correct fix is often:

```text
correct join predicate
appropriate index
better data model
```

not simply raising join buffers.

---

## Enhanced Deep Dive 58 — Query Hints Are Last Resort

Hints can influence optimizer behavior.

But they can age poorly as:

```text
data volume changes
statistics change
MySQL version changes
indexes change
```

Use only after understanding why the optimizer chooses a poor plan and validating long-term need.

---

## Enhanced Deep Dive 59 — Prepared Statements

Prepared statements separate SQL structure from values.

Application concept:

```text
SQL template
SELECT ... WHERE customer_id = ?

value
100
```

Security benefit:

```text
reduces SQL injection risk
when parameters are truly bound
```

Do not build SQL by concatenating untrusted strings.

---

## Enhanced Deep Dive 60 — SQL Injection

Unsafe:

```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```

Safe pattern using DB driver parameters:

```python
cursor.execute(
    "SELECT * FROM users WHERE username = %s",
    (username,)
)
```

The exact placeholder syntax depends on connector.

The rule:

```text
data
must remain data
not executable SQL syntax
```

---

## Enhanced Deep Dive 61 — Dynamic SQL Risk

Stored routines/applications sometimes build dynamic SQL.

Risk:

```text
user input
  ↓ concatenation
  ↓ SQL text
  ↓ execution
```

If dynamic identifiers are required:

```text
whitelist allowed values
```

Parameters usually bind values, not arbitrary SQL identifiers.

---

## Enhanced Deep Dive 62 — Transaction Autocommit Boundary

With autocommit on:

```text
statement
→ transaction
→ commit
```

unless inside explicit transaction.

Application bugs often happen when developers assume several statements are atomic while they are actually separate committed units.

Always define transaction boundary explicitly for multi-step business operations.

---

## Enhanced Deep Dive 63 — Read View and Snapshot

In `REPEATABLE READ`, a consistent read can use a transaction read view.

Concept:

```text
Transaction begins
  ↓
first consistent read establishes visibility
  ↓
later consistent reads use snapshot rules
```

Locking reads and writes behave differently from plain consistent reads.

---

## Enhanced Deep Dive 64 — Consistent Read vs Locking Read

Plain:

```sql
SELECT ...
```

can use MVCC consistent read.

Locking:

```sql
SELECT ... FOR UPDATE
```

requests locks and current data appropriate to update workflow.

Use locking reads only when business logic needs to coordinate concurrent writers.

---

## Enhanced Deep Dive 65 — Lost Update Problem

Two sessions:

```text
A reads quantity 10
B reads quantity 10
A writes 9
B writes 9
```

One decrement is lost.

Safer:

```sql
UPDATE inventory
SET quantity = quantity - 1
WHERE product_id = 1
  AND quantity > 0;
```

Then check affected rows.

Set-based atomic updates can avoid unnecessary read-modify-write races.

---

## Enhanced Deep Dive 66 — Optimistic Concurrency

Add version column:

```sql
version INT NOT NULL
```

Update:

```sql
UPDATE product
SET price = ?, version = version + 1
WHERE product_id = ?
  AND version = ?;
```

If affected rows = 0:

```text
someone changed row first
```

Application can retry/reload.

This is useful when conflicts are relatively rare.

---

## Enhanced Deep Dive 67 — Pessimistic Concurrency

Use:

```sql
SELECT ... FOR UPDATE
```

inside short transaction.

Concept:

```text
lock first
then make decision
then update
then commit quickly
```

This reduces race conditions but increases blocking.

---

## Enhanced Deep Dive 68 — Lock Granularity Is Index-Driven

InnoDB locks index records/ranges.

A nonselective update:

```sql
UPDATE orders
SET status='ARCHIVED'
WHERE YEAR(order_date) < 2020;
```

may examine/lock many records.

Rewrite with SARGable range and proper index to reduce footprint.

---

## Enhanced Deep Dive 69 — Gap Locks and Phantom Protection

Under relevant isolation/locking operations, InnoDB can lock gaps.

Concept:

```text
existing values:
10      20

protected range:
(10,20)
```

This can block insertion of value 15.

Lock behavior depends on:

```text
isolation level
query type
index
predicate
```

---

## Enhanced Deep Dive 70 — Metadata Locks

DDL needs metadata coordination.

Example:

```text
Session A:
START TRANSACTION;
SELECT * FROM product;

Session B:
ALTER TABLE product ...
```

DDL can wait because Session A retains metadata lock.

Symptoms:

```text
ALTER TABLE appears "hung"
```

Investigate active transactions and metadata-lock waits before killing random sessions.

---

## Enhanced Deep Dive 71 — DDL Is Operationally Significant

Schema changes can impact:

```text
metadata locks
CPU
I/O
temporary space
replication
application compatibility
```

Production DDL needs:

```text
change window
backup/recovery
test
lock-impact review
rollback strategy
```

---

## Enhanced Deep Dive 72 — Atomic DDL Awareness

Modern MySQL provides stronger atomicity for many DDL operations.

Concept:

```text
DDL metadata + storage changes
→ coordinated commit/rollback behavior
```

But do not assume every schema operation is instantaneous or nonblocking.

Atomicity does not mean zero operational impact.

---

## Enhanced Deep Dive 73 — Online DDL Concepts

Algorithms/lock levels vary by operation and version.

Conceptual choices:

```text
INSTANT
INPLACE
COPY
```

and locking modes can differ.

Before production ALTER:

```text
verify exact operation support
table size
lock behavior
disk requirement
replication impact
```

---

## Enhanced Deep Dive 74 — Table Rebuild Cost

A table rebuild may require:

```text
read old table
write new copy
build indexes
temporary disk
metadata switch
```

For a 1 TB table, this is not a small change.

Always estimate:

```text
time
disk headroom
I/O
replica lag
```

---

## Enhanced Deep Dive 75 — Partitioning

Partitioning divides one logical table into physical partitions.

Common strategies:

```text
RANGE
LIST
HASH
KEY
```

Example use:

```text
large event table by date
```

Partitioning is not a substitute for indexing.

---

## Enhanced Deep Dive 76 — RANGE Partitioning

Concept:

```text
events_2024
events_2025
events_2026
```

Query:

```text
WHERE event_date >= 2026-01-01
```

can use partition pruning when predicates align.

This can reduce scanned partitions.

---

## Enhanced Deep Dive 77 — Partition Pruning

Pruning means optimizer skips partitions proven irrelevant.

Good partition key use:

```text
WHERE event_date BETWEEN ...
```

Poor:

```text
predicate cannot be mapped cleanly to partition expression
```

Always inspect plan/partition selection.

---

## Enhanced Deep Dive 78 — Partitioning Trade-offs

Benefits:

```text
manage large data ranges
drop/archive old ranges
pruning
maintenance patterns
```

Costs:

```text
design complexity
unique-key restrictions
operational complexity
not helpful for every query
```

Use only when workload/data lifecycle justifies it.

---

## Enhanced Deep Dive 79 — Views and Security Context

Views can execute under `DEFINER` or invoker-related security behavior depending on definition.

Security questions:

```text
Who owns the view?
Which privileges are evaluated?
Can view expose data user cannot access directly?
```

Review view definitions:

```sql
SHOW CREATE VIEW v_order_summary;
```

---

## Enhanced Deep Dive 80 — Stored Routine DEFINER

Stored procedures/functions/triggers/events can have a definer.

If that account is missing or overprivileged, deployment/security problems can occur.

Migration checklist:

```text
object definers
required privileges
environment-specific accounts
```

Do not restore dumps blindly with obsolete production definers.

---

## Enhanced Deep Dive 81 — Stored Procedure Transaction Design

A procedure can execute multiple SQL statements.

But transaction ownership must be clear.

Question:

```text
Does caller start transaction?
Does procedure start/commit?
Can nested business workflows combine it?
```

Poorly designed routines that commit internally can prevent higher-level rollback.

---

## Enhanced Deep Dive 82 — Trigger Side Effects

A trigger adds implicit work to every matching DML operation.

Consequences:

```text
extra writes
locks
replication volume
debugging complexity
failure propagation
```

Keep triggers small, deterministic, documented, and measurable.

---

## Enhanced Deep Dive 83 — Event Scheduler Ownership

Database event:

```text
runs inside MySQL
```

OS scheduler:

```text
cron/systemd timer/Task Scheduler
```

Application scheduler:

```text
business workflow
```

Choose one clear owner.

Duplicate scheduling causes duplicate execution.

---

## Enhanced Deep Dive 84 — MySQL Account Matching

Account identity:

```text
'user'@'host'
```

Connection may match a more specific host pattern.

Therefore:

```text
'appuser'@'localhost'
```

and:

```text
'appuser'@'%'
```

can behave differently.

Always inspect the exact account selected using:

```sql
SELECT USER(), CURRENT_USER();
```

---

## Enhanced Deep Dive 85 — `USER()` vs `CURRENT_USER()`

Conceptually:

```text
USER()
→ client-supplied/authenticated connection identity context

CURRENT_USER()
→ MySQL account used for privilege checking
```

This distinction is useful when host matching causes confusing privilege behavior.

---

## Enhanced Deep Dive 86 — Roles and Default Roles

Assigning a role does not always mean it is active automatically unless configured accordingly.

Inspect active/default role behavior in your installed version.

Use:

```sql
SHOW GRANTS;
```

and session role commands as appropriate.

---

## Enhanced Deep Dive 87 — Dynamic Privileges Awareness

Modern MySQL uses dynamic privileges for some administrative capabilities instead of old broad static privileges.

Security benefit:

```text
more granular admin delegation
```

Avoid giving legacy broad privileges when a narrower dynamic privilege exists.

Verify exact privilege names for installed version.

---

## Enhanced Deep Dive 88 — Account Locking and Password Expiration

Account lifecycle can include:

```text
lock/unlock
password expiration
password history/policy
failed-login controls depending on configuration
```

Use database-native controls together with enterprise secret management.

Service accounts should not unexpectedly expire if the application cannot rotate them safely.

---

## Enhanced Deep Dive 89 — TLS Requirement per Account

Accounts can require encrypted connections.

Concept:

```sql
CREATE USER 'reportuser'@'10.60.%'
IDENTIFIED BY '...'
REQUIRE SSL;
```

Production may require stronger certificate properties depending on architecture.

Client must validate server identity, not merely "use encryption."

---

## Enhanced Deep Dive 90 — Certificate Validation

TLS provides security only when trust is validated.

Bad:

```text
encrypt connection
but accept any server certificate
```

This can still allow man-in-the-middle scenarios.

Use:

```text
trusted CA
expected server identity
client certificate if required
```

according to deployment.

---

## Enhanced Deep Dive 91 — `local_infile` Security Awareness

Local file loading can be useful:

```text
bulk import
```

but increases data/file access risk if enabled broadly.

Treat it as a capability requiring:

```text
need
scope
client/server configuration
trusted input path
```

Do not enable it globally simply to solve one import without reviewing security implications.

---

## Enhanced Deep Dive 92 — `secure_file_priv`

MySQL can restrict server-side import/export file locations.

Inspect:

```sql
SHOW VARIABLES LIKE 'secure_file_priv';
```

This helps control:

```text
LOAD DATA INFILE
SELECT ... INTO OUTFILE
```

Server filesystem access is security-sensitive.

---

## Enhanced Deep Dive 93 — FILE Privilege Risk

The `FILE` privilege can permit server-side file read/write operations within applicable restrictions.

Application accounts usually do not need it.

Grant only to trusted administrative workflows.

---

## Enhanced Deep Dive 94 — Principle of Least Privilege for DBA Roles

Separate:

```text
application DML
reporting read
backup
replication
schema migration
full DBA
```

One credential should not automatically do all tasks.

This limits blast radius from credential compromise.

---

## Enhanced Deep Dive 95 — Connection Pooling

Backend applications usually use a pool.

Architecture:

```text
web requests
   ↓
connection pool
   ↓
limited reusable DB sessions
```

Without pooling:

```text
connect/disconnect per request
→ authentication + TLS + session overhead
```

Pool size must match database capacity and application concurrency.

---

## Enhanced Deep Dive 96 — Pool Size Is Not "More Is Faster"

If app has:

```text
500 worker threads
```

and each opens:

```text
100 DB connections
```

the database can be overwhelmed.

Pool sizing should consider:

```text
DB CPU
query latency
transaction duration
number of app instances
max_connections
```

---

## Enhanced Deep Dive 97 — Connection Leaks

Symptoms:

```text
Threads_connected increases continuously
application eventually gets connection errors
```

Possible cause:

```text
connections checked out but never returned
```

Fix application lifecycle before raising `max_connections`.

---

## Enhanced Deep Dive 98 — Long-Running Transactions

A long transaction can:

```text
hold locks
retain undo versions
delay purge
increase history length
block DDL
increase deadlock risk
```

Applications should not keep transactions open while:

```text
waiting for user input
calling slow external APIs
sleeping
```

---

## Enhanced Deep Dive 99 — InnoDB Buffer Pool

The buffer pool stores:

```text
data pages
index pages
dirty pages
```

High cache hit is useful, but "bigger is always better" is wrong if it starves:

```text
OS
other MySQL memory
other services
```

Size from workload and server role.

---

## Enhanced Deep Dive 100 — Buffer Pool Miss Path

```text
query needs page
  ↓
not in buffer pool
  ↓
read from storage
  ↓
place in memory
  ↓
query continues
```

Storage latency becomes visible when working set exceeds memory or cold pages are accessed.

---

## Enhanced Deep Dive 101 — Redo Log and Write-Ahead Logging

Core idea:

```text
record change in redo
before dirty page must reach final data file
```

This allows:

```text
commit durability
crash recovery
```

The exact flush/durability behavior depends on configuration.

Do not weaken durability parameters casually for benchmarks.

---

## Enhanced Deep Dive 102 — `innodb_flush_log_at_trx_commit` Awareness

This setting affects redo flush behavior and durability/performance trade-offs.

The principle:

```text
lower durability
→ potentially better throughput
→ more committed data at risk on crash
```

Do not change without explicit business acceptance of data-loss risk.

---

## Enhanced Deep Dive 103 — Binary Log Durability

Binary log durability interacts with:

```text
replication
PITR
crash recovery consistency
```

Production durability settings should be designed together with redo behavior and replication/recovery requirements.

---

## Enhanced Deep Dive 104 — Undo and Purge

Undo supports:

```text
rollback
older row versions
```

Purge removes no-longer-needed versions.

Long transactions can prevent cleanup.

Symptoms can include:

```text
growing history
storage pressure
performance degradation
```

---

## Enhanced Deep Dive 105 — Change Buffer Awareness

InnoDB can defer/optimize some secondary-index maintenance in certain conditions.

The key architectural point:

```text
InnoDB uses multiple internal structures to optimize random I/O
```

Do not tune advanced internals before identifying a real bottleneck.

---

## Enhanced Deep Dive 106 — Doublewrite Awareness

InnoDB includes mechanisms to protect against partial page writes.

This is part of storage-level resilience.

Do not disable protective features for benchmark numbers without understanding failure risk.

---

## Enhanced Deep Dive 107 — Tablespaces

Concepts include:

```text
system tablespace
file-per-table tablespaces
undo tablespaces
temporary tablespaces
```

Exact layout depends on configuration/version.

Administrators should know which files are managed by MySQL and never delete them manually to free disk space.

---

## Enhanced Deep Dive 108 — Disk Full Is a Database Emergency

If filesystem fills:

```text
writes fail
logs cannot grow
temporary operations fail
replication may stop
backup may fail
```

Safe response:

```text
identify filesystem
identify MySQL-managed files
free space using supported retention/archive policy
add capacity if needed
verify database state
```

Never delete unknown InnoDB files.

---

## Enhanced Deep Dive 109 — Error Log First

Startup failure:

```text
mysqld exits
```

Do not reinstall first.

Inspect:

```text
error log
service manager journal/Event Log
configuration syntax
port conflict
permissions
disk
```

The error log is usually the highest-value first evidence.

---

## Enhanced Deep Dive 110 — Slow Query Log as Candidate Generator

Slow query log tells you:

```text
which statements exceeded threshold
```

It does not automatically tell you:

```text
why
```

Next:

```text
query digest
EXPLAIN
locks/waits
data distribution
indexes
OS resources
```

---

## Enhanced Deep Dive 111 — General Log Risk

General log can capture nearly every statement.

That means:

```text
huge volume
performance overhead
possible passwords/tokens/PII in queries
```

Use briefly and intentionally when other tools cannot answer the question.

---

## Enhanced Deep Dive 112 — Performance Schema Consumers and Instruments

Performance Schema instrumentation can be enabled/disabled by category.

Concept:

```text
instrument
→ what to measure

consumer
→ where collected data is exposed/aggregated
```

Measure enough for observability without assuming every instrument must always be enabled at maximum detail.

---

## Enhanced Deep Dive 113 — Statement Digests

Digest groups normalized SQL patterns.

Example literals:

```text
product_id = 1
product_id = 2
product_id = 3
```

normalize to:

```text
product_id = ?
```

This identifies high-impact query families.

---

## Enhanced Deep Dive 114 — Wait Events

A slow query may spend time waiting on:

```text
lock
disk I/O
metadata lock
network
internal synchronization
```

CPU time is only one component.

Performance Schema helps distinguish execution vs waiting.

---

## Enhanced Deep Dive 115 — Data Lock Instrumentation

Modern Performance Schema exposes lock data in supported versions.

Conceptually investigate:

```text
who holds lock?
who waits?
which object/index?
which transaction?
```

This is better than guessing from "query has been running 30 seconds."

---

## Enhanced Deep Dive 116 — Metadata Lock Diagnostics

If DDL waits:

```text
ALTER TABLE
  ↓ waiting
```

inspect:

```text
active sessions
open transactions
metadata lock state
```

Often the blocker is an idle application transaction, not the ALTER itself.

---

## Enhanced Deep Dive 117 — Backup Types

Three broad categories:

```text
logical
physical
snapshot-based with DB consistency integration
```

Choice depends on:

```text
database size
RTO
RPO
portability
downtime tolerance
tooling
```

Large databases often need physical or snapshot-aware strategies for faster restore.

---

## Enhanced Deep Dive 118 — `mysqldump --single-transaction`

For transactional InnoDB data, consistent logical backups often use a transaction-based snapshot option.

Concept:

```text
start consistent read
  ↓
dump tables
  ↓
writers continue
```

But understand exceptions:

```text
DDL during dump
nontransactional tables
metadata changes
very long dump retaining versions
```

---

## Enhanced Deep Dive 119 — Backup Consistency Across Object Types

A backup may need:

```text
schema
data
routines
events
triggers
users/roles depending on scope
```

A database dump that omits routines/events may not recreate application behavior completely.

Document backup scope explicitly.

---

## Enhanced Deep Dive 120 — Restore Validation

Verify more than row counts.

Check:

```text
schema definitions
constraints
indexes
views
routines
triggers
application queries
permissions where in scope
```

A restore can complete syntactically while still be operationally incomplete.

---

## Enhanced Deep Dive 121 — RPO and RTO

RPO:

```text
How much data can we lose?
```

RTO:

```text
How long can service be unavailable?
```

Example:

```text
daily dump
→ worst-case RPO near 24 h
```

unless binary logs/replication improve recovery point.

Backup strategy must be derived from business targets.

---

## Enhanced Deep Dive 122 — PITR Requires Base + Logs

```text
base backup
+
binary logs
+
correct replay stop point
=
point-in-time recovery
```

Missing any one:

```text
PITR fails
```

Protect binary logs with the same seriousness as backup metadata.

---

## Enhanced Deep Dive 123 — PITR Time vs Position vs GTID

Recovery stop point can be identified by concepts such as:

```text
timestamp
binary log file/position
transaction identity/GTID context
```

The safest method depends on incident evidence.

Practice in lab before production need.

---

## Enhanced Deep Dive 124 — Replication Is Asynchronous by Default Conceptually

Source commits.

Replica receives/applies later.

Therefore:

```text
source has newest data
replica may be behind
```

Application read routing must understand:

```text
stale reads
read-after-write requirements
```

---

## Enhanced Deep Dive 125 — Replica I/O vs Apply Path

Simplified:

```text
source binlog
   ↓ receiver
relay log/pipeline
   ↓ applier
replica tables
```

Lag can occur at:

```text
network receive
apply throughput
locks
disk
CPU
large transaction
```

Diagnose the stage.

---

## Enhanced Deep Dive 126 — GTID Sets

GTID lets each transaction carry unique identity.

Replica can reason:

```text
executed transactions
missing transactions
```

This simplifies topology changes compared with manual file/position-only thinking.

---

## Enhanced Deep Dive 127 — Parallel Replication

Replica can apply independent transactions concurrently in supported configurations.

Benefit:

```text
higher apply throughput
lower lag
```

But parallelism is limited by workload dependency patterns and server capacity.

---

## Enhanced Deep Dive 128 — Replication Filters Risk

Filtering replication can create intentionally different datasets.

This increases complexity:

```text
backup expectations
failover safety
application routing
schema changes
```

Do not use filters casually in HA topologies.

---

## Enhanced Deep Dive 129 — Read Replica Consistency

If application writes:

```text
source
```

then reads from:

```text
replica
```

it may not see its own write immediately.

Solutions depend on architecture:

```text
read from source after write
session stickiness
consistency mechanisms
wait-for-position/GTID logic where appropriate
```

---

## Enhanced Deep Dive 130 — Group Replication Quorum

Group members coordinate membership and transactions.

Concept:

```text
majority/quorum
→ authoritative group progress
```

Network partition safety matters.

Three nodes are common because:

```text
one node failure
→ two remain
→ majority remains
```

but exact deployment requirements must follow current MySQL guidance.

---

## Enhanced Deep Dive 131 — Single-Primary vs Multi-Primary Concept

Group Replication can support modes conceptually:

```text
single-primary
→ one writer, others replicas

multi-primary
→ multiple writers
```

Multi-primary increases conflict/application complexity.

Use only when the application is designed for it.

---

## Enhanced Deep Dive 132 — MySQL Router

Architecture:

```text
Application
   ↓
MySQL Router
   ↓
InnoDB Cluster nodes
```

Router can abstract current primary/read topology.

It does not replace:

```text
application retry
timeouts
transaction correctness
monitoring
```

---

## Enhanced Deep Dive 133 — InnoDB Cluster

Combines tooling around:

```text
Group Replication
MySQL Shell administration
MySQL Router
```

A cluster is not a backup.

A replicated bad transaction can reach every member.

Independent backups remain mandatory.

---

## Enhanced Deep Dive 134 — Failure Domains

Three database nodes on one hypervisor:

```text
appear redundant
but
share one failure domain
```

Production HA should consider:

```text
host
rack
power
switch
availability zone
storage
```

Logical replication alone does not remove shared infrastructure risk.

---

## Enhanced Deep Dive 135 — Backup on Replica

Running backups on replica can reduce source load.

But verify:

```text
replica is caught up
backup consistency
replication filters
schema parity
backup tool interaction
```

A lagging replica backup may not meet expected RPO.

---

## Enhanced Deep Dive 136 — Schema Change and Replication

DDL can create:

```text
lag
locks
large apply work
compatibility problems
```

Test schema migration with replicas.

Monitor both source and replica before/after change.

---

## Enhanced Deep Dive 137 — Replication Lag and Large Transactions

One transaction modifying millions of rows may:

```text
commit once on source
then take long to apply on replica
```

Chunking can sometimes improve operational behavior.

But chunking changes transaction semantics.

Use only if business correctness allows it.

---

## Enhanced Deep Dive 138 — Connection Failure After Failover

Even with HA, clients can hold dead connections.

Applications must implement:

```text
timeouts
connection retry
transaction retry where safe
idempotency
```

HA is a system property spanning database and application.

---

## Enhanced Deep Dive 139 — Database Security Layers

Think:

```text
Network segmentation
    ↓
TLS
    ↓
MySQL authentication
    ↓
role/privilege
    ↓
schema/table/view/routine security
    ↓
application authorization
    ↓
audit/monitoring
```

One layer does not replace the others.

---

## Enhanced Deep Dive 140 — Database Exposure

Preferred:

```text
client/browser
  ↓
application/API
  ↓ private network
MySQL
```

Avoid:

```text
Internet
  ↓
TCP/3306
MySQL
```

unless architecture explicitly requires hardened controlled exposure.

---

## Enhanced Deep Dive 141 — SQL Security and Application Authorization

Database privilege:

```text
appuser can SELECT orders
```

does not mean:

```text
every end user should see every order
```

Application still enforces business authorization.

Database account often represents application service, not individual human users.

---

## Enhanced Deep Dive 142 — Backup Confidentiality

Backups may contain:

```text
credentials
PII
financial data
business secrets
```

Protect with:

```text
encryption
access control
retention
offsite policy
secure deletion
restore authorization
```

A stolen backup can be as damaging as a stolen live database.

---

## Enhanced Deep Dive 143 — Auditing Administrative Changes

Track changes such as:

```text
CREATE USER
GRANT
REVOKE
DROP/ALTER
schema migration
backup/restore
replication topology changes
```

Use:

```text
change management
database audit capability where available
central logs
```

Production DBA work should be attributable.

---

## Enhanced Deep Dive 144 — Slow Query vs Lock Wait

Both appear as "query slow."

But root cause differs.

```text
CPU/I/O/query plan
vs
blocked on another transaction
```

Before adding index:

```text
check whether query is actually executing or waiting
```

---

## Enhanced Deep Dive 145 — CPU-Bound Query

Characteristics:

```text
high CPU
many rows examined
complex expressions
sort/group/join cost
```

Investigate:

```text
EXPLAIN ANALYZE
statement digest
indexes
row estimates
```

---

## Enhanced Deep Dive 146 — I/O-Bound Query

Characteristics:

```text
storage latency
buffer-pool misses
large scan
temporary-table spill
```

Fix may involve:

```text
better index
less data scanned
more appropriate memory
faster storage
```

Do not assume memory is the answer if query scans unnecessary rows.

---

## Enhanced Deep Dive 147 — Lock-Bound Query

Characteristics:

```text
low CPU
session waiting
transaction blocker
```

Investigate:

```text
active transactions
data locks
blocker SQL
transaction age
```

Fix usually targets transaction design, not hardware.

---

## Enhanced Deep Dive 148 — Metadata-Lock-Bound DDL

Symptom:

```text
ALTER TABLE waits for minutes
```

Potential blocker:

```text
idle transaction that touched table
```

Operational lesson:

```text
application transaction hygiene
is part of schema-change reliability
```

---

## Enhanced Deep Dive 149 — Connection Storm

Incident:

```text
application restart
  ↓
hundreds of instances reconnect simultaneously
  ↓
database CPU/authentication saturation
```

Mitigations can include:

```text
connection pooling
backoff/jitter
controlled deployment
capacity planning
```

---

## Enhanced Deep Dive 150 — Final MySQL Troubleshooting Map

```text
Business symptom
   ↓
Application error
   ↓
DNS / route / firewall
   ↓
TCP listener
   ↓
'user'@'host'
   ↓
authentication / TLS
   ↓
privilege
   ↓
SQL correctness
   ↓
transaction / locks
   ↓
query plan / indexes
   ↓
InnoDB memory / redo / undo
   ↓
OS CPU / RAM / disk / network
   ↓
replication / HA
   ↓
backup / recovery
```

Always stop at the first failed layer.

---

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Logical vs Physical Design

Take the manufacturing model and produce:
`entities`, `relationships`, `keys`, `constraints`, then physical MySQL types.

## Enhanced Lab 2 — Optional vs Mandatory Relationships

Create examples using nullable and non-null foreign keys and test valid/invalid inserts.

## Enhanced Lab 3 — Foreign Key Actions

Test `RESTRICT`, `SET NULL`, and a safe lab `CASCADE`. Document business impact.

## Enhanced Lab 4 — Normalization Anomalies

Create one deliberately bad order table and demonstrate insert/update/delete anomalies.

## Enhanced Lab 5 — Collation

Create two tables with different collations and compare case/accent behavior.

## Enhanced Lab 6 — UTF8MB4

Store multilingual text and emoji; verify round-trip through client.

## Enhanced Lab 7 — Temporal Semantics

Compare `DATE`, `DATETIME`, `TIMESTAMP`, server/session time zone, and reporting conversion.

## Enhanced Lab 8 — Generated Column

Create stored/virtual generated columns and compare query behavior.

## Enhanced Lab 9 — JSON

Store machine telemetry JSON, query paths, validate missing/null behavior.

## Enhanced Lab 10 — JSON Index Pattern

Add generated column for JSON state and index it. Compare plan before/after.

## Enhanced Lab 11 — Three-Valued Logic

Create rows with NULL and test `=`, `IS NULL`, `COALESCE`, and NULL-safe equality.

## Enhanced Lab 12 — CASE

Build production-status classification using CASE rather than procedural row loops.

## Enhanced Lab 13 — Window ROW_NUMBER

Find latest order per customer.

## Enhanced Lab 14 — RANK and DENSE_RANK

Rank products by monthly sales with ties.

## Enhanced Lab 15 — Running Total

Create daily production running total.

## Enhanced Lab 16 — LAG

Compare each production run against previous run.

## Enhanced Lab 17 — Window Frame

Demonstrate difference between explicit ROWS frame and default behavior.

## Enhanced Lab 18 — SARGability

Compare `YEAR(order_date)=2026` with date range using `EXPLAIN`.

## Enhanced Lab 19 — Prefix Index

Create long email values and evaluate prefix selectivity.

## Enhanced Lab 20 — Invisible Index

Make a noncritical lab index invisible, inspect plan, then restore visibility.

## Enhanced Lab 21 — Composite Index Order

Compare `(customer_id, order_date)` and `(order_date, customer_id)` for two query patterns.

## Enhanced Lab 22 — Covering Index

Design a covering reporting index and record read/write trade-off.

## Enhanced Lab 23 — Redundant Index Review

Find overlapping indexes in synthetic schema and propose safe removals.

## Enhanced Lab 24 — EXPLAIN JSON

Run tabular and JSON EXPLAIN on same query and map operators.

## Enhanced Lab 25 — EXPLAIN ANALYZE

Use on bounded safe SELECT and compare estimated vs actual rows.

## Enhanced Lab 26 — Join Order

Create skewed data causing multiple join choices and inspect optimizer decision.

## Enhanced Lab 27 — Temporary Table

Build query requiring grouping/sorting and inspect plan/status indicators.

## Enhanced Lab 28 — Prepared Statement Security

Write a small Python client using parameters; compare with intentionally unsafe string concatenation in a harmless lab.

## Enhanced Lab 29 — Transaction Boundary

Show multi-statement business operation with and without explicit transaction.

## Enhanced Lab 30 — Lost Update

Reproduce lost-update pattern conceptually and fix using atomic UPDATE or locking.

## Enhanced Lab 31 — Optimistic Concurrency

Implement `version` column update and detect conflict.

## Enhanced Lab 32 — Pessimistic Concurrency

Use `FOR UPDATE` in two sessions and measure blocking.

## Enhanced Lab 33 — Gap Lock

In isolated lab, demonstrate range-lock insertion behavior under relevant isolation.

## Enhanced Lab 34 — Metadata Lock

Hold a transaction open and observe DDL waiting; identify blocker.

## Enhanced Lab 35 — Online DDL Review

For several ALTER operations, document expected algorithm/lock behavior using installed-version documentation/help.

## Enhanced Lab 36 — Partitioning

Create date-range partitioned synthetic events table and test pruning.

## Enhanced Lab 37 — Partition Lifecycle

Add future partition, drop old lab partition, document archival implications.

## Enhanced Lab 38 — View Security

Create reporting view, inspect definer/security context, test restricted user.

## Enhanced Lab 39 — Routine Definer

Create a procedure with lab definer and observe privilege behavior.

## Enhanced Lab 40 — Trigger Cost

Insert/update rows with and without audit trigger; document hidden write work.

## Enhanced Lab 41 — Roles

Create app/report/backup roles and map least privilege.

## Enhanced Lab 42 — USER vs CURRENT_USER

Connect using different host patterns and inspect account matching.

## Enhanced Lab 43 — Account Locking

Lock a lab account, test login, unlock, document operational use.

## Enhanced Lab 44 — TLS Requirement

Require SSL for a lab account and verify encrypted vs unencrypted client behavior.

## Enhanced Lab 45 — secure_file_priv

Inspect value and document allowed server-side import/export directory.

## Enhanced Lab 46 — Connection Pool Design

Calculate pool size across four application instances and compare against max_connections/capacity.

## Enhanced Lab 47 — Connection Leak Simulation

Open many connections in a safe script, observe Threads_connected, then correct lifecycle.

## Enhanced Lab 48 — Long Transaction

Hold a transaction open while updating data; observe lock/undo/DDL consequences.

## Enhanced Lab 49 — Buffer Pool Observation

Run cold/warm workload and compare reads at high level using status/Performance Schema.

## Enhanced Lab 50 — Error Log Startup Failure

Introduce a harmless invalid lab config, capture error evidence, revert.

## Enhanced Lab 51 — Slow Query Log

Enable briefly in lab, run known slow query, capture candidate, disable/revert.

## Enhanced Lab 52 — Statement Digests

Generate same query pattern with different literals and identify digest grouping.

## Enhanced Lab 53 — Data Lock Diagnostics

Create lock wait and inspect lock owner/waiter using available Performance Schema views.

## Enhanced Lab 54 — Logical Backup Consistency

Use a consistent InnoDB dump approach and document transaction/DDL assumptions.

## Enhanced Lab 55 — Full Restore Validation

Restore schema/data and verify views, routines, triggers, indexes, representative queries.

## Enhanced Lab 56 — RPO/RTO

Define manufacturing database RPO/RTO and derive backup/log strategy.

## Enhanced Lab 57 — PITR Tabletop

Create base backup + sequence of transactions + accidental DELETE; identify correct replay stop point.

## Enhanced Lab 58 — Source/Replica

If resources permit, configure two MySQL lab nodes and observe replication pipeline.

## Enhanced Lab 59 — GTID

Inspect GTID configuration/state in a lab and map executed transaction identity.

## Enhanced Lab 60 — Replica Lag

Create controlled write burst and observe lag; identify receive vs apply bottleneck conceptually.

## Enhanced Lab 61 — Read-After-Write

Write to source and immediately read replica; document consistency problem.

## Enhanced Lab 62 — Group Replication Design

Draw three-node quorum/failure-domain architecture even if not deployed.

## Enhanced Lab 63 — InnoDB Cluster Design

Map MySQL Shell, Router, Group Replication, app retries, and backup.

## Enhanced Lab 64 — Backup from Replica

Design safe criteria for taking backup from replica.

## Enhanced Lab 65 — Schema Change with Replica

Run safe ALTER in lab and monitor replica effects.

## Enhanced Lab 66 — Query Classification

For ten slow examples classify as CPU, I/O, lock, metadata lock, or network/connection.

## Enhanced Lab 67 — Connection Storm Tabletop

Design exponential backoff/jitter/pool safeguards for app restart.

## Enhanced Lab 68 — Security Review

Audit accounts, roles, host patterns, TLS requirements, FILE privilege, local_infile, network exposure.

## Enhanced Lab 69 — Database Health Script

Create `MYSQL_HEALTH.sql` covering:
connections, transactions, locks, InnoDB, replication, storage/log settings, and schema health.

## Enhanced Lab 70 — Integrated MySQL Incident Challenge

Inject at least 20 safe lab faults across:

```text
connection
authentication
privilege
SQL
constraint
index
transaction
lock
DDL
storage
backup
replication
```

For each record:

```text
symptom
architecture layer
evidence
root cause
minimal fix
verification
prevention
```



## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Install and Baseline MySQL

1. Install MySQL in a disposable lab.
2. Start the service.
3. Identify `mysqld`.
4. Verify listening socket.
5. Connect locally.
6. Run `SELECT VERSION();`.
7. List system schemas.
8. Record important variables.
9. Create `MYSQL_BASELINE.md`.

### Lab 2 — Build the Manufacturing Schema

Create:

```text
Customer
Product
Department
Employee
Orders
OrderItem
```

Requirements:

1. primary keys
2. unique business keys
3. foreign keys
4. `NOT NULL`
5. `CHECK`
6. defaults
7. intentional data types
8. `SHOW CREATE TABLE` verification

### Lab 3 — Insert Synthetic Data

1. Insert 20 products.
2. Insert 20 customers.
3. Insert departments.
4. Insert employees.
5. Insert at least 100 orders.
6. Insert multiple order lines.
7. attempt duplicate key.
8. attempt invalid FK.
9. explain each error.

### Lab 4 — SELECT and Filtering

Write examples using:

1. aliases
2. expressions
3. DISTINCT
4. WHERE
5. AND/OR
6. BETWEEN
7. IN
8. LIKE
9. NULL
10. ORDER BY
11. LIMIT

For every query explain:

```text
input rows
filter
output columns
expected row count
```

### Lab 5 — Functions and Aggregation

1. string functions
2. date functions
3. numeric functions
4. count orders by status
5. average product price
6. sales by customer
7. HAVING threshold
8. explain WHERE vs HAVING

### Lab 6 — JOINs

Write:

1. Customer → Orders
2. Orders → OrderItem → Product
3. customers with no orders
4. employee-manager self join
5. shift-machine CROSS JOIN
6. one intentional Cartesian-product error
7. fix and explain it

### Lab 7 — Subqueries and CTEs

Create:

1. products above average price
2. customers with EXISTS
3. correlated subquery
4. customer-sales CTE
5. recursive org hierarchy
6. compare readability with alternative joins

### Lab 8 — Normalization

Start:

```text
OrderID
CustomerName
CustomerAddress
Product1
Product2
Product3
SalesPerson
DepartmentName
```

1. identify repeating groups
2. identify dependencies
3. transform to 1NF
4. 2NF
5. 3NF
6. draw ASCII ERD
7. implement final schema

### Lab 9 — Transactions

1. start explicit transaction
2. create order header
3. create lines
4. commit
5. repeat with invalid line
6. rollback
7. verify no partial order
8. test savepoint

### Lab 10 — Isolation and Two Sessions

1. inspect default isolation.
2. open Session A and B.
3. compare `REPEATABLE READ`.
4. compare `READ COMMITTED`.
5. test `FOR UPDATE`.
6. record timeline.
7. explain visibility.

### Lab 11 — Lock Wait

1. Session A updates inventory row without commit.
2. Session B updates same row.
3. observe waiting behavior.
4. commit A.
5. observe B.
6. explain owner/waiter.

### Lab 12 — Deadlock

1. create two inventory rows.
2. lock them in opposite order across two sessions.
3. trigger deadlock.
4. inspect InnoDB status.
5. identify victim.
6. redesign consistent ordering.
7. retry transaction.

### Lab 13 — Index Design

1. generate thousands of orders.
2. query by customer/date.
3. `EXPLAIN`.
4. create `(customer_id, order_date)`.
5. `EXPLAIN` again.
6. compare rows/access.
7. query only by date.
8. explain leftmost-prefix effect.

### Lab 14 — Query Tuning

1. select a slow synthetic query.
2. capture baseline.
3. inspect plan.
4. identify join/index issue.
5. change one thing.
6. measure.
7. document why it improved or did not.

### Lab 15 — Views and Stored Logic

1. create order-summary view.
2. create reporting procedure.
3. create simple function.
4. create price-audit trigger.
5. verify trigger output.
6. document hidden side effects.

### Lab 16 — Users and Roles

Create:

```text
appuser
reportuser
backupuser
```

1. create `report_reader`.
2. grant SELECT to role.
3. assign role.
4. grant appuser limited DML.
5. inspect grants.
6. attempt unauthorized DROP.
7. verify denial.

### Lab 17 — Backup and Restore

1. create logical dump.
2. record size/time.
3. create restore database.
4. restore.
5. compare row counts.
6. compare table definitions.
7. run representative queries.
8. write restore report.

### Lab 18 — PITR Architecture

If binary logging is enabled:

1. inspect configuration.
2. create backup.
3. perform controlled transactions.
4. identify how log events could restore to a point.
5. document stop-before-error concept.

If binary logging is unavailable, build the same process as an architecture exercise.

### Lab 19 — Performance Schema and `sys`

1. list Performance Schema tables.
2. inspect current sessions.
3. inspect statement-related data.
4. list `sys` views.
5. run workload.
6. identify repeated SQL pattern.
7. connect result to `EXPLAIN`.

### Lab 20 — Troubleshooting Challenge

Inject one at a time:

1. mysqld stopped
2. TCP/3306 firewall block
3. wrong `user@host`
4. missing privilege
5. duplicate key
6. FK violation
7. lock wait
8. deadlock
9. missing useful index
10. small controlled connection exhaustion

Document:

```text
Symptom
Architecture path
Evidence
Failed layer
Root cause
Fix
Verification
Prevention
```

---

## 6. Mini Project

# Mini Project — Manufacturing Operations Database

Build a complete MySQL database for a manufacturing company.

## Architecture

```text
                  Backend / BI
                       |
                       v
                 MySQL Server
                       |
       +---------------+---------------+
       |               |               |
     Sales         Production        Quality
```

## Required Tables

```text
Customer
Product
Department
Employee
Orders
OrderItem
Machine
ProductionRun
QualityInspection
Defect
InspectionDefect
Inventory
InventoryMovement
```

## Relationship Model

```text
Customer 1 ----- N Orders

Orders 1 ----- N OrderItem
Product 1 ----- N OrderItem

Department 1 ----- N Employee

Machine 1 ----- N ProductionRun
Product 1 ----- N ProductionRun

ProductionRun 1 ----- N QualityInspection

QualityInspection N ----- N Defect
             via InspectionDefect

Product 1 ----- 1 Inventory
Product 1 ----- N InventoryMovement
```

## Required Business Rules

Examples:

```text
quantity > 0
unit price >= 0
good quantity >= 0
rejected quantity >= 0
unique product code
unique customer code
inventory movement quantity != 0
```

Implement appropriate rules using constraints.

## Query Requirements

At minimum:

```text
10 filtering queries
10 joins
5 aggregation reports
3 subqueries
3 CTEs
1 recursive hierarchy
2 views
```

Reports:

```text
sales by customer
monthly sales
top products
customers without orders
production by machine
reject rate by product
defect Pareto source query
inventory movement
inventory current balance
employee hierarchy
```

## Index Requirements

Design and justify at least:

```text
Orders(customer_id, order_date)
OrderItem(product_id)
ProductionRun(machine_id, run_date)
QualityInspection(production_run_id)
InventoryMovement(product_id, movement_time)
```

For each index record:

```text
Query pattern
Why this column order?
EXPLAIN before
EXPLAIN after
Rows/access change
Write/storage tradeoff
```

## Transaction Requirements

Implement:

```text
Create order transaction
    order header
    +
    order items
```

and:

```text
Inventory transfer transaction
    subtract source
    +
    add destination
```

Test rollback.

## Concurrency

Create:

```text
Session A
Session B
```

Demonstrate:

- lock wait
- transaction commit releasing lock
- controlled deadlock
- consistent-order fix

## Stored Logic

Create:

```text
1 view for order summary
1 procedure for customer order report
1 function with clear deterministic purpose
1 trigger for price audit
```

Explain why each belongs in the DB rather than application code.

## Security

Accounts:

```text
appuser
reportuser
backupuser
dbadmin_lab
```

Use least privilege and roles.

## Backup

Create and test:

```text
logical backup
restore into separate database
row-count verification
schema verification
```

Write PITR design using binary logs.

## Monitoring

Create:

```text
MYSQL_HEALTH.sql
```

Report selected:

```text
server version
connections
max connections
active sessions
database/table metadata
slow-query configuration
InnoDB diagnostic entry points
replication state if configured
```

## Project Files

```text
README.md
ERD.md
SCHEMA.sql
SEED.sql
QUERIES.sql
VIEWS.sql
ROUTINES.sql
INDEXES.md
TRANSACTIONS.md
SECURITY.sql
BACKUP_RECOVERY.md
MYSQL_HEALTH.sql
TROUBLESHOOTING.md
```

## Failure Tests

Document at least:

```text
cannot connect
access denied
duplicate key
FK failure
slow query
lock wait
deadlock
disk pressure
too many connections
replication lag scenario
```

For every incident:

```text
Symptom
Evidence
Root Cause
Correction
Verification
Prevention
```

---


# Expanded Capstone — Production-Style Manufacturing MySQL Platform

Build:

```text
                         Backend API
                             |
                        connection pool
                             |
                             v
                        MySQL Primary
                             |
                  +----------+----------+
                  |                     |
              Replica               Backup Store
                  |                     |
            BI / reporting      full backup + binlogs
```

Optional HA extension:

```text
Application
   ↓
MySQL Router
   ↓
3-node InnoDB Cluster
```

## Schema

Create:

```text
customer
product
department
employee
orders
order_item
machine
production_run
quality_inspection
defect
inspection_defect
inventory
inventory_movement
machine_event
```

## Required Design Rules

Implement and document:

```text
surrogate PKs
business UNIQUE keys
foreign keys
ON DELETE behavior
NOT NULL
CHECK
defaults
utf8mb4/collation
temporal strategy
JSON only where justified
```

## Advanced SQL

Deliver:

```text
10 joins
5 aggregates
5 window-function reports
3 subqueries
3 CTEs
1 recursive CTE
2 views
1 generated-column use case
1 JSON reporting use case
```

Reports must include:

```text
monthly sales
customer ranking
running production output
previous-run comparison with LAG
defect Pareto source data
latest order per customer
inventory movement balance
machine performance trend
```

## Index Engineering

For at least 10 query patterns document:

```text
query
expected cardinality
EXPLAIN before
index design
column order
EXPLAIN after
estimated/actual change
write cost
storage cost
```

Include:

```text
one covering index
one composite-index ordering comparison
one SARGability rewrite
one redundant-index review
```

## Transactions

Implement:

```text
create order
inventory movement
production close
```

Demonstrate:

```text
atomicity
rollback
savepoint
optimistic conflict
pessimistic lock
deadlock retry design
```

## DDL Operations

Document:

```text
schema migration
metadata lock risk
online DDL expectations
rollback strategy
disk headroom
replica impact
```

## Security

Create:

```text
app_role
report_role
backup_role
migration_role
```

Users:

```text
appuser
reportuser
backupuser
migrationuser
named DBA account
```

Requirements:

```text
least privilege
restricted host patterns
TLS for remote connections
no public 3306
no broad FILE privilege
secret-management plan
```

## Backup and Recovery

Implement/test:

```text
logical full backup
restore to isolated database
schema/object validation
representative query validation
```

Design:

```text
binary-log retention
PITR
RPO
RTO
off-host backup
encryption
restore authorization
```

## Replication

If resources permit:

```text
primary
replica
GTID
replication monitoring
```

Test:

```text
read lag
large transaction
replica restart
backup from replica criteria
```

## HA Design

Design a three-node topology:

```text
Node1
Node2
Node3
```

Across independent failure domains where possible.

Document:

```text
single-primary vs multi-primary choice
Router
quorum
application retries
backup independence
failover behavior
```

## Monitoring

Create:

```text
MYSQL_HEALTH.sql
```

and dashboard/report fields for:

```text
connections
active sessions
long transactions
lock waits
deadlocks
slow query candidates
buffer pool
disk usage
binary log retention
replication lag
server uptime
```

## Failure Matrix

At least 30:

```text
mysqld stopped
port blocked
bind address wrong
wrong user@host
password failure
TLS required
missing role/default role
missing table privilege
duplicate key
FK violation
CHECK violation
slow full scan
bad composite index order
non-SARGable predicate
lock wait
deadlock
long transaction
metadata lock
DDL disk pressure
connection leak
connection storm
disk nearly full
binary log retention issue
backup incomplete
restore missing routine
replica lag
replica SQL error
read-after-write stale read
source unavailable
Router/HA retry failure design
```

For every incident capture:

```text
Symptom
Expected layer
Evidence
Root cause
Fix
Verification
Rollback/Prevention
```

## Project Files

```text
README.md
ERD.md
SCHEMA.sql
SEED.sql
QUERIES_BASIC.sql
QUERIES_ADVANCED.sql
WINDOW_FUNCTIONS.sql
JSON.sql
INDEXES.md
EXPLAIN_REPORT.md
TRANSACTIONS.md
CONCURRENCY.md
DDL_OPERATIONS.md
ROUTINES.sql
SECURITY.sql
BACKUP_RECOVERY.md
REPLICATION.md
HA_DESIGN.md
MYSQL_HEALTH.sql
TROUBLESHOOTING.md
FAILURE_TESTS.md
```


## 7. Recommended Resources

Prioritize official MySQL documentation:

- MySQL Reference Manual
- InnoDB Storage Engine
- InnoDB and the ACID model
- transaction isolation levels
- InnoDB locking and deadlocks
- clustered and secondary indexes
- optimizer and `EXPLAIN`
- account management and roles
- MySQL security guidelines
- `mysqldump`
- binary logging
- replication and GTID
- Group Replication
- InnoDB Cluster
- Performance Schema
- `sys` schema

Local discovery:

```sql
HELP SELECT;
HELP CREATE TABLE;
HELP GRANT;
HELP START TRANSACTION;
```

CLI:

```bash
mysql --help
mysqldump --help
mysqlsh --help
```

---

## 8. Certification Relevance

This course is foundational for:

```text
MySQL DBA
Backend Engineer
Data Engineer
Cloud Engineer
DevOps Engineer
SRE
Cybersecurity Engineer
Database Security
```

It prepares for:

```text
29. Oracle SQL and PL/SQL
30. Oracle Database Administration I
31. Oracle Database Administration II
32. NoSQL Databases
33. Cloud Database Fundamentals
```

Transferable concepts:

```text
schema design
normalization
transactions
isolation
locking
indexes
query plans
security
backup
replication
monitoring
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** One giant table for all business data.  
  **Best practice:** Model entities and relationships intentionally.

- **Mistake:** Surrogate key but no business UNIQUE rule.  
  **Best practice:** Protect real business identifiers too.

- **Mistake:** `SELECT *` everywhere.  
  **Best practice:** Select required columns in stable application queries.

- **Mistake:** `column = NULL`.  
  **Best practice:** Use `IS NULL` / `IS NOT NULL`.

- **Mistake:** Join without predicting cardinality.  
  **Best practice:** Know expected row multiplication.

- **Mistake:** Create an index for every column.  
  **Best practice:** Design indexes from query patterns and `EXPLAIN`.

- **Mistake:** Ignore composite-index order.  
  **Best practice:** Design around leading predicates and sort/range requirements.

- **Mistake:** Keep transactions open during user interaction.  
  **Best practice:** Keep transactions short and deterministic.

- **Mistake:** Treat every deadlock as a MySQL bug.  
  **Best practice:** Use consistent ordering and application retries.

- **Mistake:** Give application accounts broad admin rights.  
  **Best practice:** Apply least privilege and roles.

- **Mistake:** Expose MySQL publicly for convenience.  
  **Best practice:** Use private/controlled network access and TLS.

- **Mistake:** Treat replication as backup.  
  **Best practice:** Keep independent backups and restore tests.

- **Mistake:** Delete database files manually when disk fills.  
  **Best practice:** Use supported retention/log/storage procedures.

- **Mistake:** Raise `max_connections` immediately.  
  **Best practice:** Investigate pooling, leaks, workload, and slow SQL.

- **Mistake:** Never test restore.  
  **Best practice:** Recovery tests are part of backup operations.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. Why use a DBMS?

**Short answer:** To coordinate structured data, concurrent access, integrity, security, transactions, querying, and recovery.

### Q2. What is a primary key?

**Short answer:** A chosen unique non-null row identifier.

### Q3. What is a foreign key?

**Short answer:** A constraint ensuring a child value references a valid parent key.

### Q4. How is a many-to-many relationship modeled?

**Short answer:** Through a junction table.

### Q5. What is InnoDB?

**Short answer:** MySQL's primary transactional storage engine.

### Q6. What is the common classic MySQL TCP port?

**Short answer:** 3306.

### Q7. DDL means?

**Short answer:** Data-definition statements such as CREATE and ALTER.

### Q8. DML means?

**Short answer:** Data query/change statements such as SELECT, INSERT, UPDATE, DELETE.

### Q9. Why is `= NULL` wrong?

**Short answer:** NULL is tested using `IS NULL` because SQL uses unknown/null semantics.

### Q10. WHERE vs HAVING?

**Short answer:** WHERE filters rows before grouping; HAVING filters grouped results.

### Q11. INNER JOIN?

**Short answer:** Returns rows matching the join condition on both sides.

### Q12. LEFT JOIN?

**Short answer:** Preserves every left-side row plus any right-side matches.

### Q13. What is a CTE?

**Short answer:** A named query expression defined using `WITH`.

### Q14. Why normalize?

**Short answer:** To reduce redundancy and modification anomalies by modeling dependencies correctly.

### Q15. What is InnoDB's clustered index?

**Short answer:** The index organization storing row data, normally based on the primary key.

### Q16. Why does composite-index order matter?

**Short answer:** B-tree ordering begins with the leading columns, affecting which predicates/ranges can use the index effectively.

### Q17. What does `EXPLAIN` show?

**Short answer:** MySQL's planned access/execution strategy.

### Q18. What are ACID properties?

**Short answer:** Atomicity, Consistency, Isolation, Durability.

### Q19. What is autocommit?

**Short answer:** Automatic commit behavior for eligible standalone statements outside explicit transaction grouping.

### Q20. What is the common InnoDB default isolation level?

**Short answer:** REPEATABLE READ.

### Q21. What is MVCC?

**Short answer:** Multi-Version Concurrency Control, allowing transactions to read appropriate row versions with reduced reader/writer blocking.

### Q22. What is `FOR UPDATE` for?

**Short answer:** A locking read when the transaction intends to update the selected rows.

### Q23. What is a deadlock?

**Short answer:** A cycle in which transactions wait for locks held by each other.

### Q24. How should applications handle deadlock victims?

**Short answer:** Retry safe operations while also minimizing deadlocks through transaction design.

### Q25. Why use roles?

**Short answer:** To group privileges and simplify least-privilege administration.

### Q26. What is the InnoDB buffer pool?

**Short answer:** Memory caching InnoDB data and index pages.

### Q27. Redo vs undo?

**Short answer:** Redo supports crash recovery; undo supports rollback and old-version/read-consistency behavior.

### Q28. Binary log vs redo log?

**Short answer:** Binary log supports server-level replication/PITR workflows; redo is InnoDB crash-recovery logging.

### Q29. What is `mysqldump`?

**Short answer:** A logical backup utility.

### Q30. What is PITR?

**Short answer:** Restore a backup then replay logged changes up to a chosen point.

### Q31. What is replication lag?

**Short answer:** Delay between a source commit and the replica applying/reflecting that change.

### Q32. Why isn't a replica a backup?

**Short answer:** Incorrect/destructive source changes can replicate too.

### Q33. What is GTID?

**Short answer:** A Global Transaction Identifier used to track replicated transactions.

### Q34. What is Performance Schema?

**Short answer:** MySQL runtime instrumentation for statements, waits, transactions, locks, threads, memory, and related activity.

### Q35. What is the correct connection troubleshooting order?

**Short answer:** Service → listener → network/firewall → `user@host` → authentication/TLS → privileges.

---


# Enhanced Self-Assessment Bank

### Q1. Logical vs physical design?
**Answer:** Logical models business entities/relationships; physical maps them to MySQL types, keys, indexes, and storage choices.

### Q2. Why keep business UNIQUE keys with surrogate PKs?
**Answer:** Surrogate identity does not enforce business uniqueness.

### Q3. Optional relationship?
**Answer:** Relationship where FK may be NULL.

### Q4. Why use ON DELETE RESTRICT?
**Answer:** Prevent parent deletion while dependent children exist.

### Q5. Cascade risk?
**Answer:** One parent delete can remove many dependent rows automatically.

### Q6. What is an update anomaly?
**Answer:** Duplicated fact must be changed in many rows and can become inconsistent.

### Q7. What does normalization optimize?
**Answer:** Functional dependency correctness and anomaly reduction.

### Q8. Character set vs collation?
**Answer:** Encoding vs comparison/sort rules.

### Q9. Why utf8mb4?
**Answer:** Full Unicode UTF-8 character range.

### Q10. Why can collation affect UNIQUE?
**Answer:** Equality rules determine whether two strings compare as same value.

### Q11. DECIMAL use?
**Answer:** Exact decimal arithmetic such as financial values.

### Q12. DATETIME vs TIMESTAMP design issue?
**Answer:** They differ in semantics/range/timezone behavior; choose according to business meaning.

### Q13. JSON should replace relational schema?
**Answer:** No.

### Q14. Generated column?
**Answer:** Column computed from expression over other columns.

### Q15. Window function?
**Answer:** Analytic calculation across related rows without collapsing result rows.

### Q16. GROUP BY vs window?
**Answer:** GROUP BY reduces rows; window keeps row granularity.

### Q17. ROW_NUMBER?
**Answer:** Sequential unique number inside window ordering.

### Q18. RANK vs DENSE_RANK?
**Answer:** RANK leaves gaps after ties; DENSE_RANK does not.

### Q19. LAG?
**Answer:** Access prior row value in a window order.

### Q20. SARGability?
**Answer:** Predicate form that allows efficient index search.

### Q21. Why YEAR(date)=2026 can be worse?
**Answer:** Function on indexed column may prevent direct date-range index access.

### Q22. Prefix index trade-off?
**Answer:** Smaller index but reduced selectivity.

### Q23. Invisible index?
**Answer:** Maintained index normally ignored by optimizer for safe removal testing.

### Q24. Covering index?
**Answer:** Index contains all data required by a query.

### Q25. Why PK width affects secondary indexes?
**Answer:** InnoDB secondary entries include primary-key value.

### Q26. Composite index order?
**Answer:** Determines searchable leading prefixes and range/sort usefulness.

### Q27. Redundant index?
**Answer:** Index whose useful access patterns substantially overlap another.

### Q28. What does `Using filesort` mean?
**Answer:** MySQL performs an explicit sort rather than reading final order directly from index.

### Q29. Why join order matters?
**Answer:** Early large intermediate results can multiply work.

### Q30. Prepared statements help security how?
**Answer:** Keep data parameters separate from SQL syntax.

### Q31. SQL injection?
**Answer:** Untrusted data becomes executable SQL syntax.

### Q32. Autocommit risk?
**Answer:** Multi-statement business process may commit each statement separately unless transaction is explicit.

### Q33. Consistent read?
**Answer:** MVCC snapshot-style read without locking current records for update.

### Q34. Locking read?
**Answer:** Read such as FOR UPDATE that acquires locks for coordinated update.

### Q35. Lost update?
**Answer:** Concurrent writers overwrite each other's changes.

### Q36. Optimistic concurrency?
**Answer:** Detect conflict with version/check at update time.

### Q37. Pessimistic concurrency?
**Answer:** Lock resource before modifying.

### Q38. Gap lock?
**Answer:** Lock on index range/gap used in relevant isolation/locking scenarios.

### Q39. Metadata lock?
**Answer:** Lock protecting schema/object metadata while statements/DDL interact.

### Q40. Why DDL can wait?
**Answer:** Existing transactions/statements may hold metadata locks.

### Q41. Atomic DDL means instant?
**Answer:** No; it improves failure consistency, not runtime cost.

### Q42. Online DDL?
**Answer:** Schema-change algorithms designed to reduce copying/locking depending on operation/version.

### Q43. Partitioning?
**Answer:** Splits one logical table into physical partitions by rule.

### Q44. Partition pruning?
**Answer:** Skip partitions that cannot contain matching rows.

### Q45. Partitioning replaces index?
**Answer:** No.

### Q46. View security context?
**Answer:** Privileges can depend on definer/invoker semantics.

### Q47. Trigger risk?
**Answer:** Hidden extra writes/locks/logic.

### Q48. What identifies MySQL account?
**Answer:** `'user'@'host'`.

### Q49. USER vs CURRENT_USER?
**Answer:** Connection identity context vs account used for privilege evaluation.

### Q50. Dynamic privilege?
**Answer:** Granular administrative privilege added independently of older static privilege set.

### Q51. Why require TLS?
**Answer:** Protect DB credentials/data in transit.

### Q52. Encryption without certificate validation enough?
**Answer:** No; identity/trust validation is required.

### Q53. secure_file_priv?
**Answer:** Restricts server-side import/export file paths.

### Q54. FILE privilege risk?
**Answer:** Enables sensitive server-side file operations.

### Q55. Why connection pool?
**Answer:** Reuse bounded DB sessions instead of reconnecting constantly.

### Q56. More pool connections always faster?
**Answer:** No; can overload DB.

### Q57. Connection leak?
**Answer:** Sessions checked out/opened and never released.

### Q58. Long transaction risk?
**Answer:** Locks, undo retention, purge delay, DDL blocking, deadlocks.

### Q59. Buffer pool?
**Answer:** InnoDB memory cache for data/index pages.

### Q60. Redo purpose?
**Answer:** Crash recovery/durability of InnoDB changes.

### Q61. Undo purpose?
**Answer:** Rollback and older-version/MVCC support.

### Q62. `innodb_flush_log_at_trx_commit` affects?
**Answer:** Redo flush/durability trade-off.

### Q63. Binary log purpose?
**Answer:** Replication and point-in-time recovery workflows.

### Q64. Why never delete unknown data-directory files?
**Answer:** They may be required InnoDB/system storage and deletion can corrupt DB.

### Q65. Slow query log tells what?
**Answer:** Candidate statements exceeding threshold, not root cause by itself.

### Q66. Performance Schema?
**Answer:** Runtime instrumentation for statements, waits, locks, memory, transactions, and sessions.

### Q67. Statement digest?
**Answer:** Normalized grouping of similar SQL patterns.

### Q68. Wait event?
**Answer:** Time spent waiting for a resource such as lock or I/O.

### Q69. Logical backup?
**Answer:** SQL/object/data representation export.

### Q70. Physical backup?
**Answer:** Consistency-aware copy of underlying database storage.

### Q71. `--single-transaction` concept?
**Answer:** Consistent transactional snapshot for InnoDB logical dump.

### Q72. Backup validation?
**Answer:** Restore and verify schema/data/objects/application queries.

### Q73. RPO?
**Answer:** Maximum acceptable data-loss window.

### Q74. RTO?
**Answer:** Maximum acceptable recovery duration.

### Q75. PITR requires?
**Answer:** Base backup plus binary logs plus known stop point.

### Q76. Replication usually guarantees immediate replica freshness?
**Answer:** No.

### Q77. GTID?
**Answer:** Unique global transaction identifier for replication tracking.

### Q78. Parallel replication?
**Answer:** Apply independent transactions concurrently to improve throughput.

### Q79. Read-after-write issue?
**Answer:** Replica may not yet contain source write.

### Q80. Group Replication quorum?
**Answer:** Majority-style membership authority protecting group progress.

### Q81. Single-primary?
**Answer:** One writable primary with other group members not acting as concurrent writers.

### Q82. Multi-primary risk?
**Answer:** More conflict/application complexity.

### Q83. MySQL Router?
**Answer:** Routing layer for InnoDB Cluster topology.

### Q84. InnoDB Cluster includes conceptually?
**Answer:** Group Replication + MySQL Shell administration + Router.

### Q85. Cluster replaces backup?
**Answer:** No.

### Q86. Failure domain?
**Answer:** Infrastructure components that can fail together.

### Q87. Backup from replica concern?
**Answer:** Replica lag/filtering/consistency must satisfy recovery target.

### Q88. Why large transaction causes lag?
**Answer:** Replica may need long apply time for one commit unit.

### Q89. HA requires app behavior?
**Answer:** Yes; retries/timeouts/idempotency matter after failover.

### Q90. Database security layers?
**Answer:** Network, TLS, authentication, privileges, object security, app authorization, audit.

### Q91. Public 3306 recommended?
**Answer:** Generally no; prefer controlled private access.

### Q92. DB privilege equals end-user authorization?
**Answer:** No.

### Q93. Why protect backups?
**Answer:** They contain production data/secrets.

### Q94. Slow query vs lock wait?
**Answer:** One may consume resources; the other may be blocked by another transaction.

### Q95. CPU-bound query signs?
**Answer:** High CPU, many rows, expensive join/sort/expression work.

### Q96. I/O-bound query signs?
**Answer:** Storage waits, large scans, buffer misses, temp spills.

### Q97. Lock-bound query signs?
**Answer:** Waiting session with blocker transaction and often low CPU.

### Q98. Metadata-lock-bound DDL?
**Answer:** Schema change waits on another statement/transaction's metadata lock.

### Q99. Connection storm?
**Answer:** Many clients reconnect simultaneously and overload DB.

### Q100. Best MySQL troubleshooting approach?
**Answer:** Walk the stack from client/network/auth through SQL/locks/optimizer/InnoDB/OS/replication and stop at first failed layer.


## Completion Checklist

- [ ] I can design relational entities and relationships.
- [ ] I can use primary, unique, composite, and foreign keys.
- [ ] I can write SELECT/filter/aggregate/join/subquery/CTE queries.
- [ ] I can normalize a dataset to 3NF.
- [ ] I understand InnoDB clustered and secondary indexes.
- [ ] I can design composite indexes.
- [ ] I can interpret basic `EXPLAIN`.
- [ ] I understand ACID and transaction control.
- [ ] I can compare isolation behavior using two sessions.
- [ ] I understand MVCC, lock waits, and deadlocks.
- [ ] I can create procedures, functions, triggers, and views responsibly.
- [ ] I can create users/roles with least privilege.
- [ ] I understand buffer pool, redo, undo, and binary logs.
- [ ] I can create and restore logical backups.
- [ ] I can explain PITR, replication, GTID, lag, Group Replication, and InnoDB Cluster.
- [ ] I can use Performance Schema and `sys` as diagnostic tools.
- [ ] I completed all 20 labs.
- [ ] I completed the Manufacturing Operations Database mini project.
