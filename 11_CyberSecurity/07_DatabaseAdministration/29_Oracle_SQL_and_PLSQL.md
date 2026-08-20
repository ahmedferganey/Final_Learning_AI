# 29. Oracle SQL and PL/SQL

> Phase 7 — Database

This course builds on the relational and SQL foundations from **28. MySQL Database** and moves into Oracle-specific SQL plus Oracle's procedural language, **PL/SQL**.

The reference baseline is **Oracle AI Database 26ai**, Oracle's current long-term-support database generation. The core SQL and PL/SQL skills in this file are deliberately chosen to remain useful across common Oracle 19c, 23ai, and 26ai environments.

The central mental model is:

```text
Application / User
        |
        | SQL
        v
+------------------------+
| Oracle SQL Engine      |
|------------------------|
| Parse                  |
| Optimize               |
| Execute                |
+------------------------+
        |
        | SQL statements inside PL/SQL
        v
+------------------------+
| PL/SQL Engine          |
|------------------------|
| Variables              |
| Conditions             |
| Loops                  |
| Cursors                |
| Exceptions             |
| Procedures / Functions |
| Packages / Triggers    |
+------------------------+
        |
        v
Oracle Database Objects
```

The learning style is:

```text
Concept
   ↓
Visualization
   ↓
Oracle SQL / PL/SQL
   ↓
Expected behavior
   ↓
Why it works
   ↓
Real use case
   ↓
Failure / troubleshooting
```

The goal is **not** to memorize Oracle syntax. You should be able to design queries, predict results, write safe PL/SQL, interpret errors, and decide whether logic belongs in SQL, PL/SQL, or the application.

---

## 1. Topic Title

**Oracle SQL and PL/SQL**

---

## 2. Learning Objectives

By the end of this course, you should be able to:

- Explain the difference between SQL and PL/SQL and how Oracle uses both.
- Connect to an Oracle database using SQL Developer, SQLcl, or SQL*Plus-style tools.
- Work with Oracle schemas, users, database objects, and common Oracle data types.
- Write SELECT statements using filtering, sorting, expressions, functions, conversion functions, NULL handling, and conditional expressions.
- Build aggregate reports using `GROUP BY`, `HAVING`, `ROLLUP`, `CUBE`, and `GROUPING SETS`.
- Write inner, outer, full outer, cross, and self joins.
- Use scalar, multi-row, correlated, and `EXISTS` subqueries.
- Use set operators such as `UNION`, `UNION ALL`, `INTERSECT`, and `MINUS`.
- Use Oracle analytic/window functions such as `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, and aggregate `OVER`.
- Use hierarchical queries, row limiting, pivoting, and other important Oracle SQL patterns.
- Perform `INSERT`, `UPDATE`, `DELETE`, and `MERGE` operations safely.
- Explain Oracle transaction behavior using `COMMIT`, `ROLLBACK`, and `SAVEPOINT`.
- Create tables, constraints, sequences, identity columns, views, indexes, and synonyms.
- Query Oracle data dictionary views such as `USER_*`, `ALL_*`, and conceptually `DBA_*`.
- Write anonymous PL/SQL blocks with declarations, executable statements, and exception handlers.
- Use `%TYPE`, `%ROWTYPE`, records, collections, and bind-variable-friendly code.
- Write conditional logic and loops while preserving set-based SQL where appropriate.
- Use implicit and explicit cursors and cursor `FOR` loops.
- Handle predefined and user-defined exceptions.
- Create stored procedures, functions, packages, and triggers.
- Use dynamic SQL with `EXECUTE IMMEDIATE` safely.
- Use `BULK COLLECT` and `FORALL` to reduce SQL/PLSQL context switching.
- Understand definer-rights vs invoker-rights security.
- Debug compilation/runtime problems using `DBMS_OUTPUT`, compiler diagnostics, and dictionary views.
- Build a complete Oracle manufacturing reporting and transaction package.

---

## 3. Prerequisites

Required:

- 28. MySQL Database, or equivalent relational database foundation
- understanding of tables, rows, keys, foreign keys, normalization, transactions, and joins
- basic programming concepts

Recommended Oracle lab:

```text
Oracle AI Database 26ai Free
or
Oracle Database 19c/23ai/26ai lab

Client:
SQL Developer
SQLcl
SQL*Plus-compatible CLI
```

Suggested schema:

```text
MANUFACTURING
```

Main lab entities:

```text
CUSTOMER
PRODUCT
DEPARTMENT
EMPLOYEE
ORDERS
ORDER_ITEM
MACHINE
PRODUCTION_RUN
QUALITY_INSPECTION
DEFECT
```

Safety:

```text
DROP USER
DROP TABLE
TRUNCATE
DELETE without WHERE
dynamic SQL
privileged DBA views
```

should be practiced only in a disposable lab schema.

---

## 4. Core Concepts Explanation

# Part 1 — Oracle SQL vs PL/SQL

## 1.1 SQL Is Declarative

SQL describes **what result or data change you want**.

Example:

```sql
SELECT
    product_id,
    product_name,
    unit_price
FROM product
WHERE active_flag = 'Y'
ORDER BY unit_price DESC;
```

You do not normally specify:

```text
read row 1
then row 2
then row 3
```

The optimizer chooses an execution plan.

Mental model:

```text
You specify:
"Give me active products"

Oracle decides:
access path
join order
index use
execution operations
```

## 1.2 PL/SQL Adds Procedural Logic

PL/SQL extends SQL with:

```text
variables
IF
CASE
LOOP
WHILE
FOR
exceptions
procedures
functions
packages
triggers
collections
```

Example:

```sql
BEGIN
    DBMS_OUTPUT.PUT_LINE('Hello from PL/SQL');
END;
/
```

The final `/` is a client-side execution delimiter used by tools such as SQL*Plus/SQLcl for PL/SQL blocks.

## 1.3 SQL vs PL/SQL Decision

Use SQL when the task is naturally set-based:

```sql
UPDATE employee
SET salary = salary * 1.05
WHERE department_id = 10;
```

Avoid unnecessarily replacing that with:

```text
fetch employee
update
fetch employee
update
...
```

Use PL/SQL when you need procedural orchestration:

```text
validate parameters
    ↓
execute several SQL statements
    ↓
branch depending on result
    ↓
handle expected exceptions
    ↓
return result/status
```

---

# Part 2 — Oracle Development Tools and Connections

## 2.1 SQL Developer

Oracle SQL Developer is a graphical tool for:

```text
SQL worksheets
object browsing
PL/SQL editing
debugging support
reports
connections
```

Conceptual connection:

```text
SQL Developer
      |
      | username/password or supported auth
      v
Oracle Listener
      |
      v
Database Service
      |
      v
Schema Session
```

## 2.2 SQLcl

SQLcl provides a modern Oracle command-line experience.

Concept:

```text
Terminal
   |
 sql
   |
Oracle Database
```

A typical connection pattern depends on the configured Oracle service.

Example conceptually:

```bash
sql manufacturing@//dbhost.example:1521/FREEPDB1
```

Never put production passwords directly into shell command history.

## 2.3 SQL*Plus

SQL*Plus remains important because many Oracle administration and development examples use its command model.

Useful commands:

```text
DESC
SET
SPOOL
SHOW ERRORS
VARIABLE
PRINT
```

Example:

```sql
DESC product
```

## 2.4 Database Service vs Schema

A connection targets a database service.

After authentication, your session operates as a database user/schema identity.

Concept:

```text
Oracle Database
   |
   +-- Schema MANUFACTURING
   |     +-- PRODUCT
   |     +-- ORDERS
   |
   +-- Schema REPORTING
         +-- views
```

In Oracle, a user owns a schema of the same name.

That is a different mental model from MySQL's use of the word "database."

---

# Part 3 — Oracle Naming and Schemas

## 3.1 Schema-qualified Object Names

Within your own schema:

```sql
SELECT *
FROM product;
```

Cross-schema, if privilege exists:

```sql
SELECT *
FROM manufacturing.product;
```

Pattern:

```text
schema.object
```

## 3.2 Quoted vs Unquoted Identifiers

Unquoted:

```sql
CREATE TABLE product (...);
```

Oracle stores/compares normal unquoted identifiers in uppercase semantics.

Quoted:

```sql
CREATE TABLE "Product" (...);
```

requires exact quoted case later.

Avoid unnecessary quoted mixed-case object names because they create friction:

```sql
SELECT * FROM "Product";
```

## 3.3 Naming Conventions

A practical schema might use:

```text
PK_PRODUCT
FK_ORDER_CUSTOMER
UK_PRODUCT_CODE
IX_ORDERS_CUSTOMER_DATE
V_ORDER_SUMMARY
PKG_ORDER_API
TRG_PRODUCT_AUDIT
```

Names should reveal object purpose.

---

# Part 4 — Oracle Data Types

## 4.1 NUMBER

General numeric type:

```sql
salary NUMBER(12,2)
```

Meaning:

```text
precision = total significant digits
scale     = digits after decimal
```

Example:

```text
NUMBER(12,2)
up to roughly 10 integer digits + 2 decimal digits
```

Use exact numeric semantics for financial data.

## 4.2 VARCHAR2

Variable-length character data:

```sql
product_name VARCHAR2(150)
```

For Oracle application schemas, `VARCHAR2` is the normal variable-character type to learn.

## 4.3 CHAR

Fixed-length character semantics:

```sql
active_flag CHAR(1)
```

Example:

```text
Y
N
```

## 4.4 DATE

Oracle `DATE` stores:

```text
year
month
day
hour
minute
second
```

This surprises learners coming from systems where DATE contains only a calendar date.

Example:

```sql
SELECT SYSDATE
FROM dual;
```

## 4.5 TIMESTAMP

Provides fractional seconds and related timestamp variants.

```sql
created_at TIMESTAMP DEFAULT SYSTIMESTAMP
```

## 4.6 CLOB

Character Large Object.

Useful for larger textual content.

## 4.7 BLOB

Binary Large Object.

Useful for binary content when storing it in the database is justified.

## 4.8 RAW

Stores binary byte sequences with Oracle-specific semantics.

## 4.9 NULL

NULL means missing/unknown—not zero or empty business meaning.

Oracle also has important empty-string behavior in character SQL contexts, so application logic should avoid treating empty strings and NULL as safely distinct without understanding Oracle semantics.

---

# Part 5 — SELECT Fundamentals

## 5.1 Basic Query

```sql
SELECT
    product_id,
    product_name,
    unit_price
FROM product;
```

## 5.2 DUAL

Traditional Oracle examples evaluate expressions using:

```sql
SELECT
    2 + 3 AS result
FROM dual;
```

Expected:

```text
RESULT
------
5
```

`DUAL` is a special one-row table historically used for expression evaluation.

## 5.3 Aliases

```sql
SELECT
    product_name AS name,
    unit_price AS price
FROM product;
```

Quoted aliases can contain spaces:

```sql
SELECT
    unit_price AS "Unit Price"
FROM product;
```

Use friendly aliases in reporting, but avoid awkward quoting in reusable code.

## 5.4 Concatenation

Oracle concatenation operator:

```sql
SELECT
    product_code || ' - ' || product_name AS product_label
FROM product;
```

## 5.5 DISTINCT

```sql
SELECT DISTINCT status
FROM orders;
```

## 5.6 ORDER BY

```sql
SELECT
    product_name,
    unit_price
FROM product
ORDER BY
    unit_price DESC,
    product_name ASC;
```

Without `ORDER BY`, do not assume row order.

---

# Part 6 — Filtering

## 6.1 WHERE

```sql
SELECT *
FROM product
WHERE active_flag = 'Y';
```

## 6.2 AND / OR

```sql
SELECT *
FROM product
WHERE
    active_flag = 'Y'
    AND (
        product_code LIKE 'BTL%'
        OR product_code LIKE 'JAR%'
    );
```

Parentheses make precedence explicit.

## 6.3 BETWEEN

```sql
WHERE unit_price BETWEEN 10 AND 20
```

Both bounds are inclusive.

## 6.4 IN

```sql
WHERE status IN ('NEW', 'APPROVED', 'SHIPPED')
```

## 6.5 LIKE

```sql
WHERE product_name LIKE 'Bottle%'
```

Pattern characters:

```text
%  zero or more characters
_  one character
```

## 6.6 NULL Conditions

Wrong:

```sql
WHERE manager_id = NULL
```

Correct:

```sql
WHERE manager_id IS NULL
```

SQL uses three-valued logic:

```text
TRUE
FALSE
UNKNOWN
```

---

# Part 7 — Character Functions

Common functions:

```text
UPPER
LOWER
INITCAP
LENGTH
SUBSTR
INSTR
TRIM
REPLACE
LPAD
RPAD
```

Example:

```sql
SELECT
    product_name,
    UPPER(product_name) AS uppercase_name,
    LENGTH(product_name) AS name_length,
    SUBSTR(product_code, 1, 3) AS family_code
FROM product;
```

Find substring:

```sql
SELECT
    INSTR('ORACLE DATABASE', 'DATABASE') AS position
FROM dual;
```

---

# Part 8 — Numeric Functions

Examples:

```sql
SELECT
    ROUND(12.3456, 2) AS rounded_value,
    TRUNC(12.3456, 2) AS truncated_value,
    MOD(10, 3) AS remainder
FROM dual;
```

Difference:

```text
ROUND
uses rounding rules

TRUNC
removes extra precision without rounding
```

This distinction matters for financial/reporting logic.

---

# Part 9 — Oracle Date and Time Functions

## 9.1 SYSDATE

```sql
SELECT SYSDATE
FROM dual;
```

Database-server date/time semantics.

## 9.2 SYSTIMESTAMP

```sql
SELECT SYSTIMESTAMP
FROM dual;
```

Provides richer timestamp information.

## 9.3 ADD_MONTHS

```sql
SELECT
    ADD_MONTHS(SYSDATE, 3)
FROM dual;
```

## 9.4 MONTHS_BETWEEN

```sql
SELECT
    MONTHS_BETWEEN(
        DATE '2026-12-01',
        DATE '2026-08-01'
    ) AS months_difference
FROM dual;
```

## 9.5 LAST_DAY

```sql
SELECT LAST_DAY(SYSDATE)
FROM dual;
```

## 9.6 NEXT_DAY

```sql
SELECT
    NEXT_DAY(SYSDATE, 'MONDAY')
FROM dual;
```

Be aware that textual date/day interpretation can depend on NLS settings.

---

# Part 10 — Type Conversion

## 10.1 Explicit Conversion Is Safer

Core functions:

```text
TO_CHAR
TO_DATE
TO_NUMBER
```

Date conversion:

```sql
SELECT
    TO_DATE(
        '2026-08-17',
        'YYYY-MM-DD'
    ) AS parsed_date
FROM dual;
```

Formatting:

```sql
SELECT
    TO_CHAR(
        SYSDATE,
        'YYYY-MM-DD HH24:MI:SS'
    ) AS formatted_time
FROM dual;
```

## 10.2 Why Implicit Conversion Is Dangerous

Query:

```sql
WHERE order_date = '17-AUG-26'
```

can depend on session NLS settings.

Safer:

```sql
WHERE order_date = DATE '2026-08-17'
```

or explicit conversion:

```sql
WHERE order_date =
      TO_DATE('2026-08-17', 'YYYY-MM-DD')
```

Mental model:

```text
Text
  ↓ format model
DATE
```

Make conversions explicit when ambiguity matters.

---

# Part 11 — NULL Handling

## 11.1 NVL

```sql
SELECT
    employee_name,
    NVL(commission_pct, 0) AS commission_pct
FROM employee;
```

## 11.2 NVL2

```sql
SELECT
    employee_name,
    NVL2(
        commission_pct,
        'HAS COMMISSION',
        'NO COMMISSION'
    ) AS commission_status
FROM employee;
```

## 11.3 NULLIF

```sql
SELECT
    NULLIF(actual_qty, target_qty)
FROM production_run;
```

Returns NULL when expressions are equal.

## 11.4 COALESCE

```sql
SELECT
    COALESCE(
        mobile_phone,
        office_phone,
        'NO PHONE'
    ) AS contact_number
FROM employee;
```

Returns first non-NULL expression.

---

# Part 12 — Conditional Expressions

## 12.1 CASE

```sql
SELECT
    product_name,
    unit_price,
    CASE
        WHEN unit_price >= 100 THEN 'HIGH'
        WHEN unit_price >= 50  THEN 'MEDIUM'
        ELSE 'LOW'
    END AS price_band
FROM product;
```

Flow:

```text
condition 1?
  | yes -> HIGH
  | no
condition 2?
  | yes -> MEDIUM
  | no -> LOW
```

## 12.2 DECODE

Oracle-specific legacy-style conditional expression:

```sql
SELECT
    status,
    DECODE(
        status,
        'N', 'NEW',
        'A', 'APPROVED',
        'S', 'SHIPPED',
        'UNKNOWN'
    ) AS status_description
FROM orders;
```

For complex logic, `CASE` is generally clearer and more portable.

---

# Part 13 — Aggregate Functions

Common:

```text
COUNT
SUM
AVG
MIN
MAX
```

Example:

```sql
SELECT
    COUNT(*) AS product_count,
    AVG(unit_price) AS average_price,
    MIN(unit_price) AS minimum_price,
    MAX(unit_price) AS maximum_price
FROM product;
```

NULL behavior matters:

```sql
COUNT(*)
counts rows

COUNT(column)
counts non-NULL column values
```

---

# Part 14 — GROUP BY and HAVING

## 14.1 GROUP BY

```sql
SELECT
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status;
```

## 14.2 HAVING

```sql
SELECT
    customer_id,
    SUM(order_total) AS sales
FROM orders
GROUP BY customer_id
HAVING SUM(order_total) > 100000;
```

Difference:

```text
WHERE
filters input rows

GROUP BY
forms groups

HAVING
filters groups
```

Logical model:

```text
FROM
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
```

---

# Part 15 — ROLLUP, CUBE, and GROUPING SETS

## 15.1 ROLLUP

```sql
SELECT
    department_id,
    status,
    SUM(order_total) AS total
FROM orders
GROUP BY ROLLUP (
    department_id,
    status
);
```

Concept:

```text
department + status totals
department subtotals
grand total
```

## 15.2 CUBE

```sql
GROUP BY CUBE (
    department_id,
    status
)
```

Conceptually produces multiple subtotal combinations.

Use carefully because combinations grow rapidly.

## 15.3 GROUPING SETS

Explicitly request desired group levels:

```sql
SELECT
    department_id,
    status,
    SUM(order_total) AS total
FROM orders
GROUP BY GROUPING SETS (
    (department_id, status),
    (department_id),
    ()
);
```

This is often clearer than computing many reports separately.

---

# Part 16 — JOINs

## 16.1 INNER JOIN

```sql
SELECT
    o.order_id,
    c.customer_name,
    o.order_date
FROM orders o
JOIN customer c
    ON c.customer_id = o.customer_id;
```

## 16.2 LEFT OUTER JOIN

```sql
SELECT
    c.customer_name,
    o.order_id
FROM customer c
LEFT JOIN orders o
    ON o.customer_id = c.customer_id;
```

All customers survive.

## 16.3 RIGHT OUTER JOIN

```sql
SELECT
    c.customer_name,
    o.order_id
FROM customer c
RIGHT JOIN orders o
    ON o.customer_id = c.customer_id;
```

Often rewrite as LEFT JOIN if that improves readability.

## 16.4 FULL OUTER JOIN

```sql
SELECT
    a.business_key,
    a.amount AS system_a_amount,
    b.amount AS system_b_amount
FROM system_a_data a
FULL OUTER JOIN system_b_data b
    ON b.business_key = a.business_key;
```

Excellent for reconciliation:

```text
only A
matching A+B
only B
```

## 16.5 CROSS JOIN

```sql
SELECT
    s.shift_name,
    m.machine_name
FROM shift s
CROSS JOIN machine m;
```

Every combination.

## 16.6 SELF JOIN

```sql
SELECT
    e.employee_name,
    m.employee_name AS manager_name
FROM employee e
LEFT JOIN employee m
    ON m.employee_id = e.manager_id;
```

---

# Part 17 — Multi-table Joins and Join Errors

Example:

```sql
SELECT
    o.order_id,
    c.customer_name,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price AS line_total
FROM orders o
JOIN customer c
    ON c.customer_id = o.customer_id
JOIN order_item oi
    ON oi.order_id = o.order_id
JOIN product p
    ON p.product_id = oi.product_id;
```

Before running, predict cardinality:

```text
1 order
   |
   +-- 3 order items
       |
       +-- 3 output rows
```

If you accidentally omit:

```sql
ON p.product_id = oi.product_id
```

you can create a Cartesian multiplication.

Always ask:

```text
What table is one side?
What table is many side?
How many rows should this join produce?
```

---

# Part 18 — Subqueries

## 18.1 Scalar

```sql
SELECT *
FROM product
WHERE unit_price > (
    SELECT AVG(unit_price)
    FROM product
);
```

## 18.2 Multi-row IN

```sql
SELECT *
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE order_date >= DATE '2026-01-01'
);
```

## 18.3 EXISTS

```sql
SELECT
    c.customer_id,
    c.customer_name
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

## 18.4 Correlated Subquery

```sql
SELECT
    e.employee_id,
    e.employee_name,
    e.salary
FROM employee e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.department_id = e.department_id
);
```

Concept:

```text
Employee row
   ↓
compare against
department-specific average
```

## 18.5 `NOT IN` and NULL Trap

If a `NOT IN` subquery returns NULL, three-valued logic can produce surprising results.

For anti-join semantics, `NOT EXISTS` is often safer and clearer:

```sql
SELECT *
FROM customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

---

# Part 19 — Set Operators

## 19.1 UNION

```sql
SELECT email FROM customer
UNION
SELECT email FROM supplier;
```

Removes duplicates.

## 19.2 UNION ALL

Keeps duplicates.

```sql
SELECT email FROM customer
UNION ALL
SELECT email FROM supplier;
```

## 19.3 INTERSECT

Returns common rows:

```sql
SELECT email FROM customer
INTERSECT
SELECT email FROM supplier;
```

## 19.4 MINUS

Oracle's set difference operator:

```sql
SELECT product_code
FROM expected_products

MINUS

SELECT product_code
FROM actual_products;
```

Useful for reconciliation:

```text
expected
minus
actual
=
missing
```

---

# Part 20 — Analytic / Window Functions

Analytic functions are one of Oracle SQL's most powerful reporting features.

They calculate across a set of rows **without collapsing those rows into one GROUP BY row**.

## 20.1 GROUP BY vs Analytic

GROUP BY:

```text
10 employees
   ↓
1 row per department
```

Analytic:

```text
10 employees remain 10 rows
+
department aggregate attached to each row
```

Example:

```sql
SELECT
    employee_id,
    department_id,
    salary,
    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS department_avg
FROM employee;
```

## 20.2 ROW_NUMBER

```sql
SELECT
    employee_id,
    department_id,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS rn
FROM employee;
```

Top employee per department:

```sql
SELECT *
FROM (
    SELECT
        e.*,
        ROW_NUMBER() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS rn
    FROM employee e
)
WHERE rn = 1;
```

## 20.3 RANK vs DENSE_RANK

Values:

```text
100
100
90
```

`RANK`:

```text
1
1
3
```

`DENSE_RANK`:

```text
1
1
2
```

## 20.4 LAG

Compare to previous row:

```sql
SELECT
    run_date,
    good_qty,
    LAG(good_qty) OVER (
        ORDER BY run_date
    ) AS previous_good_qty
FROM production_run;
```

## 20.5 LEAD

Look forward:

```sql
LEAD(run_date) OVER (
    ORDER BY run_date
)
```

## 20.6 Running Total

```sql
SELECT
    order_date,
    order_total,
    SUM(order_total) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING
                 AND CURRENT ROW
    ) AS running_sales
FROM orders;
```

Visualization:

```text
row1 total = 100  running = 100
row2 total = 50   running = 150
row3 total = 75   running = 225
```

---

# Part 21 — Row Limiting and Top-N

Modern Oracle syntax:

```sql
SELECT
    product_id,
    product_name,
    unit_price
FROM product
ORDER BY unit_price DESC
FETCH FIRST 10 ROWS ONLY;
```

Pagination concept:

```sql
OFFSET 20 ROWS
FETCH NEXT 10 ROWS ONLY
```

Always use a deterministic `ORDER BY`.

Without deterministic ordering:

```text
"page 2"
```

has no stable business meaning.

---

# Part 22 — Hierarchical Queries

Oracle has long supported hierarchical querying with `CONNECT BY`.

Employee hierarchy:

```sql
SELECT
    LEVEL,
    employee_id,
    employee_name,
    manager_id
FROM employee
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
```

Visualization:

```text
CEO
 |
 +-- Operations Director
 |      |
 |      +-- Production Manager
 |
 +-- Finance Director
```

Useful pseudocolumn:

```text
LEVEL
```

Display indentation:

```sql
SELECT
    LPAD(' ', (LEVEL - 1) * 2) ||
    employee_name AS org_chart
FROM employee
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
```

---

# Part 23 — PIVOT and UNPIVOT

Suppose input:

```text
Month  Status     Amount
Jan    GOOD       100
Jan    REJECT      10
Feb    GOOD       120
Feb    REJECT       8
```

Pivot to columns:

```sql
SELECT *
FROM (
    SELECT
        production_month,
        status,
        quantity
    FROM monthly_quality
)
PIVOT (
    SUM(quantity)
    FOR status IN (
        'GOOD' AS good_qty,
        'REJECT' AS reject_qty
    )
);
```

Output concept:

```text
Month   GOOD_QTY   REJECT_QTY
Jan       100          10
Feb       120           8
```

`UNPIVOT` performs the opposite transformation conceptually.

---

# Part 24 — DML: INSERT, UPDATE, DELETE

## 24.1 INSERT

```sql
INSERT INTO product (
    product_id,
    product_code,
    product_name,
    unit_price
)
VALUES (
    product_seq.NEXTVAL,
    'BTL-330',
    'Bottle 330ml',
    0.25
);
```

## 24.2 INSERT from Query

```sql
INSERT INTO archived_product
SELECT *
FROM product
WHERE active_flag = 'N';
```

Always verify column compatibility.

## 24.3 UPDATE

Safe pattern:

```sql
SELECT *
FROM product
WHERE product_id = 100;
```

Then:

```sql
UPDATE product
SET unit_price = 0.30
WHERE product_id = 100;
```

Then verify before commit.

## 24.4 DELETE

Danger:

```sql
DELETE FROM orders;
```

removes all rows.

Safe workflow:

```text
write WHERE
   ↓
SELECT with same WHERE
   ↓
verify rows
   ↓
DELETE
   ↓
verify
   ↓
COMMIT
```

---

# Part 25 — MERGE

`MERGE` is extremely useful for synchronize/upsert-style operations.

Example staging table:

```text
PRODUCT_STAGE
```

Target:

```text
PRODUCT
```

SQL:

```sql
MERGE INTO product p
USING product_stage s
ON (
    p.product_code = s.product_code
)
WHEN MATCHED THEN
    UPDATE SET
        p.product_name = s.product_name,
        p.unit_price = s.unit_price
WHEN NOT MATCHED THEN
    INSERT (
        product_id,
        product_code,
        product_name,
        unit_price
    )
    VALUES (
        product_seq.NEXTVAL,
        s.product_code,
        s.product_name,
        s.unit_price
    );
```

Flow:

```text
Stage Row
   ↓
Match target?
   |
 yes ---> UPDATE
   |
 no ----> INSERT
```

Use `MERGE` only after understanding uniqueness and source cardinality. Multiple source rows unexpectedly matching the same target key can create errors or ambiguous business logic.

---

# Part 26 — Transactions

## 26.1 Oracle Transaction Boundary

A transaction begins implicitly with transactional work and ends with:

```text
COMMIT
ROLLBACK
certain DDL boundaries
session termination behavior
```

Explicit example:

```sql
UPDATE inventory
SET quantity = quantity - 10
WHERE product_id = 1;

UPDATE inventory
SET quantity = quantity + 10
WHERE product_id = 2;

COMMIT;
```

## 26.2 ROLLBACK

```sql
UPDATE product
SET unit_price = unit_price * 100;

ROLLBACK;
```

## 26.3 SAVEPOINT

```sql
UPDATE orders
SET status = 'PROCESSING'
WHERE order_id = 1001;

SAVEPOINT order_updated;

INSERT INTO order_audit (...);

ROLLBACK TO order_updated;

COMMIT;
```

## 26.4 DDL and Transaction Awareness

Oracle DDL has important transaction-boundary behavior.

Do not mix:

```text
large uncommitted business transaction
+
casual DDL
```

without understanding the commit implications.

---

# Part 27 — DDL

## 27.1 CREATE TABLE

```sql
CREATE TABLE department (
    department_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    department_name VARCHAR2(100) NOT NULL,

    CONSTRAINT pk_department
        PRIMARY KEY (department_id),

    CONSTRAINT uk_department_name
        UNIQUE (department_name)
);
```

## 27.2 ALTER TABLE

```sql
ALTER TABLE product
ADD (
    active_flag CHAR(1) DEFAULT 'Y' NOT NULL
);
```

## 27.3 DROP

```sql
DROP TABLE temp_test;
```

Destructive.

Use disposable lab objects.

## 27.4 TRUNCATE

```sql
TRUNCATE TABLE temp_stage;
```

Concept:

```text
DELETE
row-oriented DML / transaction semantics

TRUNCATE
DDL-style fast removal of all rows
```

Do not use TRUNCATE when you require row-level filtering or normal rollback expectations.

---

# Part 28 — Constraints

## 28.1 NOT NULL

```sql
product_name VARCHAR2(150) NOT NULL
```

## 28.2 PRIMARY KEY

```sql
CONSTRAINT pk_product
PRIMARY KEY (product_id)
```

## 28.3 UNIQUE

```sql
CONSTRAINT uk_product_code
UNIQUE (product_code)
```

## 28.4 FOREIGN KEY

```sql
CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customer(customer_id)
```

## 28.5 CHECK

```sql
CONSTRAINT chk_product_price
CHECK (unit_price >= 0)
```

## 28.6 Constraint State Concepts

Oracle supports rich constraint management such as enabling/disabling and validation states.

The important operational lesson:

```text
constraint exists
≠
constraint currently validates/enforces exactly as you assume
```

Inspect dictionary metadata before making migration assumptions.

---

# Part 29 — Sequences

## 29.1 Sequence Object

```sql
CREATE SEQUENCE product_seq
    START WITH 1
    INCREMENT BY 1
    CACHE 100;
```

Next value:

```sql
SELECT product_seq.NEXTVAL
FROM dual;
```

Current session's current value after NEXTVAL:

```sql
SELECT product_seq.CURRVAL
FROM dual;
```

## 29.2 Sequences Are Not Gapless Counters

Possible sequence values:

```text
100
101
103
104
```

A rollback or caching/crash behavior can leave gaps.

Do not use a normal sequence when a legal/business requirement demands gapless document numbering without designing that requirement explicitly.

---

# Part 30 — Identity Columns

Instead of manually referencing a sequence:

```sql
CREATE TABLE machine (
    machine_id NUMBER
        GENERATED BY DEFAULT AS IDENTITY,
    machine_name VARCHAR2(100) NOT NULL,

    CONSTRAINT pk_machine
        PRIMARY KEY (machine_id)
);
```

Identity columns simplify generated-key definitions.

Sequences remain important because they are explicit reusable schema objects and appear throughout existing Oracle systems.

---

# Part 31 — Views

## 31.1 Simple View

```sql
CREATE VIEW v_active_product AS
SELECT
    product_id,
    product_code,
    product_name,
    unit_price
FROM product
WHERE active_flag = 'Y';
```

## 31.2 WITH CHECK OPTION

```sql
CREATE VIEW v_active_product AS
SELECT
    product_id,
    product_code,
    product_name,
    active_flag
FROM product
WHERE active_flag = 'Y'
WITH CHECK OPTION;
```

This prevents modifications through the view that would make rows fall outside the view predicate.

## 31.3 READ ONLY

For reporting:

```sql
CREATE VIEW v_product_report AS
SELECT
    product_id,
    product_name,
    unit_price
FROM product
WITH READ ONLY;
```

Views can serve:

```text
abstraction
reporting
security boundary
simplified API
```

but are not automatically materialized results.

---

# Part 32 — Synonyms

A synonym provides an alternate object name.

Private synonym:

```sql
CREATE SYNONYM product_master
FOR manufacturing.product;
```

Then:

```sql
SELECT *
FROM product_master;
```

Concept:

```text
Synonym
   ↓
target object
```

A synonym does **not** itself grant access.

You still need privilege on the target object.

Public synonyms affect broader namespace behavior and should be managed cautiously.

---

# Part 33 — Indexes

## 33.1 B-tree Index

```sql
CREATE INDEX ix_orders_customer_date
ON orders (
    customer_id,
    order_date
);
```

Use query patterns to determine column order.

## 33.2 Unique Index vs Unique Constraint

A unique constraint may use an index internally, but the **business meaning** is different:

```text
Unique Constraint
data integrity rule

Index
access structure
```

Prefer constraints to express integrity.

## 33.3 Composite Index

```text
(customer_id, order_date)
```

works best for predicates beginning with the leading columns.

## 33.4 Function-based Index

Suppose query:

```sql
SELECT *
FROM employee
WHERE UPPER(email) = 'USER@EXAMPLE.COM';
```

A function-based index can support the expression:

```sql
CREATE INDEX ix_employee_upper_email
ON employee (
    UPPER(email)
);
```

The query expression should match the indexed expression semantics.

## 33.5 Too Many Indexes

Every additional index affects:

```text
INSERT
UPDATE
DELETE
storage
backup
maintenance
```

Use execution-plan evidence rather than indexing every filter column.

---

# Part 34 — Oracle Data Dictionary

Oracle stores metadata about database/schema objects in dictionary views.

Three important families:

```text
USER_*
objects owned by current user

ALL_*
objects accessible to current user

DBA_*
database-wide administrative views,
normally requiring elevated privilege
```

Examples:

```sql
SELECT table_name
FROM user_tables
ORDER BY table_name;
```

Columns:

```sql
SELECT
    table_name,
    column_name,
    data_type,
    data_length
FROM user_tab_columns
WHERE table_name = 'PRODUCT';
```

Constraints:

```sql
SELECT
    constraint_name,
    constraint_type,
    status
FROM user_constraints
WHERE table_name = 'PRODUCT';
```

Indexes:

```sql
SELECT
    index_name,
    uniqueness
FROM user_indexes
WHERE table_name = 'PRODUCT';
```

Never request broad DBA privileges just because a tutorial uses `DBA_*`.

---

# Part 35 — PL/SQL Block Architecture

Canonical structure:

```sql
DECLARE
    -- declarations
BEGIN
    -- executable statements
EXCEPTION
    -- handlers
END;
/
```

Only `BEGIN ... END` is required for a basic block.

Visualization:

```text
DECLARE
  variables/types
     ↓
BEGIN
  executable logic
     ↓
EXCEPTION
  error handling
     ↓
END
```

Example:

```sql
SET SERVEROUTPUT ON

DECLARE
    v_message VARCHAR2(100) := 'Hello PL/SQL';
BEGIN
    DBMS_OUTPUT.PUT_LINE(v_message);
END;
/
```

---

# Part 36 — PL/SQL Variables and Constants

## 36.1 Variable

```sql
DECLARE
    v_quantity NUMBER := 100;
BEGIN
    DBMS_OUTPUT.PUT_LINE(v_quantity);
END;
/
```

## 36.2 Constant

```sql
DECLARE
    c_tax_rate CONSTANT NUMBER := 0.14;
BEGIN
    DBMS_OUTPUT.PUT_LINE(c_tax_rate);
END;
/
```

## 36.3 Scope

Nested blocks can introduce local scope.

```text
Outer block variable
     |
     +-- visible inside nested block unless shadowed
```

Avoid reusing the same names in confusing ways.

---

# Part 37 — Anchored Types: `%TYPE` and `%ROWTYPE`

## 37.1 `%TYPE`

Instead of duplicating a datatype:

```sql
DECLARE
    v_product_name product.product_name%TYPE;
BEGIN
    ...
END;
/
```

If the column datatype changes, the PL/SQL declaration stays aligned at compile time.

## 37.2 `%ROWTYPE`

```sql
DECLARE
    v_product product%ROWTYPE;
BEGIN
    SELECT *
    INTO v_product
    FROM product
    WHERE product_id = 1;

    DBMS_OUTPUT.PUT_LINE(
        v_product.product_name
    );
END;
/
```

Mental model:

```text
PRODUCT row
   ↓
record with matching fields
```

---

# Part 38 — SELECT INTO

PL/SQL can retrieve query values into variables:

```sql
DECLARE
    v_name  product.product_name%TYPE;
    v_price product.unit_price%TYPE;
BEGIN
    SELECT
        product_name,
        unit_price
    INTO
        v_name,
        v_price
    FROM product
    WHERE product_id = 1;

    DBMS_OUTPUT.PUT_LINE(
        v_name || ': ' || v_price
    );
END;
/
```

Important behavior:

```text
0 rows
    NO_DATA_FOUND

>1 row for scalar SELECT INTO
    TOO_MANY_ROWS
```

This must be handled if either condition is valid business behavior.

---

# Part 39 — PL/SQL Conditional Logic

## 39.1 IF / ELSIF / ELSE

```sql
DECLARE
    v_reject_rate NUMBER := 3.2;
BEGIN
    IF v_reject_rate >= 5 THEN
        DBMS_OUTPUT.PUT_LINE('CRITICAL');
    ELSIF v_reject_rate >= 2 THEN
        DBMS_OUTPUT.PUT_LINE('WARNING');
    ELSE
        DBMS_OUTPUT.PUT_LINE('NORMAL');
    END IF;
END;
/
```

## 39.2 CASE Statement

```sql
CASE v_status
    WHEN 'N' THEN
        DBMS_OUTPUT.PUT_LINE('NEW');
    WHEN 'A' THEN
        DBMS_OUTPUT.PUT_LINE('APPROVED');
    ELSE
        DBMS_OUTPUT.PUT_LINE('OTHER');
END CASE;
```

Use the construct that best communicates business intent.

---

# Part 40 — PL/SQL Loops

## 40.1 Basic LOOP

```sql
DECLARE
    v_counter PLS_INTEGER := 1;
BEGIN
    LOOP
        DBMS_OUTPUT.PUT_LINE(v_counter);
        v_counter := v_counter + 1;

        EXIT WHEN v_counter > 5;
    END LOOP;
END;
/
```

## 40.2 WHILE

```sql
DECLARE
    v_counter PLS_INTEGER := 1;
BEGIN
    WHILE v_counter <= 5 LOOP
        DBMS_OUTPUT.PUT_LINE(v_counter);
        v_counter := v_counter + 1;
    END LOOP;
END;
/
```

## 40.3 Numeric FOR Loop

```sql
BEGIN
    FOR i IN 1..5 LOOP
        DBMS_OUTPUT.PUT_LINE(i);
    END LOOP;
END;
/
```

## 40.4 Avoid Unnecessary Loops

Bad:

```text
fetch 100,000 products
loop
update each row
```

Better when business rule is set-based:

```sql
UPDATE product
SET active_flag = 'N'
WHERE discontinued_date < DATE '2025-01-01';
```

SQL engine should do set operations whenever practical.


# Part 41 — Implicit Cursors

Every SQL statement executed by PL/SQL has cursor-related state.

For ordinary DML, PL/SQL exposes implicit cursor attributes:

```text
SQL%ROWCOUNT
SQL%FOUND
SQL%NOTFOUND
SQL%ISOPEN
```

Example:

```sql
BEGIN
    UPDATE product
    SET active_flag = 'N'
    WHERE discontinued_date < DATE '2025-01-01';

    DBMS_OUTPUT.PUT_LINE(
        'Rows updated: ' || SQL%ROWCOUNT
    );
END;
/
```

Mental model:

```text
UPDATE executes
    ↓
Oracle knows affected row count
    ↓
SQL%ROWCOUNT exposes it to PL/SQL
```

This is useful when procedure logic depends on whether rows were changed.

---

# Part 42 — Explicit Cursors

## 42.1 Why Explicit Cursors Exist

A query can return multiple rows.

```text
Query
  ↓
Result Set
  ↓
Cursor
  ↓
Fetch one row
  ↓
Process
  ↓
Fetch next row
```

Example:

```sql
DECLARE
    CURSOR c_product IS
        SELECT
            product_id,
            product_name,
            unit_price
        FROM product
        WHERE active_flag = 'Y'
        ORDER BY product_id;

    v_id    product.product_id%TYPE;
    v_name  product.product_name%TYPE;
    v_price product.unit_price%TYPE;
BEGIN
    OPEN c_product;

    LOOP
        FETCH c_product
        INTO
            v_id,
            v_name,
            v_price;

        EXIT WHEN c_product%NOTFOUND;

        DBMS_OUTPUT.PUT_LINE(
            v_id || ' - ' ||
            v_name || ' - ' ||
            v_price
        );
    END LOOP;

    CLOSE c_product;
END;
/
```

## 42.2 Cursor Lifecycle

```text
DECLARE
   ↓
OPEN
   ↓
FETCH
   ↓
FETCH
   ↓
...
   ↓
CLOSE
```

## 42.3 Cursor Attributes

```text
%FOUND
%NOTFOUND
%ROWCOUNT
%ISOPEN
```

Example:

```sql
c_product%ROWCOUNT
```

---

# Part 43 — Cursor FOR Loops

PL/SQL can simplify explicit cursor handling:

```sql
DECLARE
    CURSOR c_product IS
        SELECT
            product_id,
            product_name,
            unit_price
        FROM product
        WHERE active_flag = 'Y';
BEGIN
    FOR r_product IN c_product LOOP
        DBMS_OUTPUT.PUT_LINE(
            r_product.product_id ||
            ' - ' ||
            r_product.product_name
        );
    END LOOP;
END;
/
```

PL/SQL handles:

```text
open
fetch
close
```

automatically.

Even simpler:

```sql
BEGIN
    FOR r_order IN (
        SELECT
            order_id,
            customer_id,
            order_total
        FROM orders
        WHERE status = 'NEW'
    ) LOOP
        DBMS_OUTPUT.PUT_LINE(
            r_order.order_id
        );
    END LOOP;
END;
/
```

Use cursor loops when procedural row-by-row processing is genuinely required.

Do not replace a single set-based SQL statement with a cursor loop without reason.

---

# Part 44 — Parameterized Cursors

A cursor can receive parameters.

```sql
DECLARE
    CURSOR c_order (
        p_customer_id orders.customer_id%TYPE
    ) IS
        SELECT
            order_id,
            order_date,
            order_total
        FROM orders
        WHERE customer_id = p_customer_id
        ORDER BY order_date DESC;
BEGIN
    FOR r_order IN c_order(100) LOOP
        DBMS_OUTPUT.PUT_LINE(
            r_order.order_id ||
            ' = ' ||
            r_order.order_total
        );
    END LOOP;
END;
/
```

Concept:

```text
same cursor logic
      +
different parameter
      ↓
different result set
```

Parameterized cursors make reusable cursor definitions clearer.

---

# Part 45 — Exception Handling

## 45.1 Why Exceptions Matter

Without deliberate exception handling:

```text
error occurs
    ↓
block stops
    ↓
caller gets error
```

With handling:

```text
error occurs
    ↓
appropriate handler
    ↓
log / transform / recover / re-raise
```

Structure:

```sql
BEGIN
    ...
EXCEPTION
    WHEN exception_name THEN
        ...
END;
/
```

## 45.2 `NO_DATA_FOUND`

```sql
DECLARE
    v_name product.product_name%TYPE;
BEGIN
    SELECT product_name
    INTO v_name
    FROM product
    WHERE product_id = -1;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE(
            'Product not found'
        );
END;
/
```

## 45.3 `TOO_MANY_ROWS`

Occurs when scalar `SELECT INTO` returns more than one row.

```sql
EXCEPTION
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE(
            'Query returned multiple rows'
        );
```

Fix the business/query assumption rather than simply suppressing the error.

## 45.4 `DUP_VAL_ON_INDEX`

Useful when a unique/primary-key rule is violated.

```sql
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        DBMS_OUTPUT.PUT_LINE(
            'Duplicate business key'
        );
```

## 45.5 `ZERO_DIVIDE`

```sql
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        ...
```

---

# Part 46 — User-Defined Exceptions

Declare:

```sql
DECLARE
    e_invalid_quantity EXCEPTION;
    v_quantity NUMBER := -5;
BEGIN
    IF v_quantity <= 0 THEN
        RAISE e_invalid_quantity;
    END IF;

EXCEPTION
    WHEN e_invalid_quantity THEN
        DBMS_OUTPUT.PUT_LINE(
            'Quantity must be greater than zero'
        );
END;
/
```

Concept:

```text
business condition
      ↓
raise named exception
      ↓
handler communicates business failure
```

Use meaningful exception names.

---

# Part 47 — `RAISE_APPLICATION_ERROR`

PL/SQL can return an application-specific Oracle error:

```sql
BEGIN
    IF 10 <= 0 THEN
        RAISE_APPLICATION_ERROR(
            -20001,
            'Quantity must be positive'
        );
    END IF;
END;
/
```

Custom application error range typically uses negative numbers in Oracle's application-error range.

Procedure example:

```sql
CREATE OR REPLACE PROCEDURE validate_quantity (
    p_quantity IN NUMBER
)
IS
BEGIN
    IF p_quantity <= 0 THEN
        RAISE_APPLICATION_ERROR(
            -20001,
            'Quantity must be positive'
        );
    END IF;
END;
/
```

This is far better than silently changing an invalid value.

---

# Part 48 — `WHEN OTHERS` and Error Propagation

This is dangerous:

```sql
EXCEPTION
    WHEN OTHERS THEN
        NULL;
```

It means:

```text
Any unexpected error
       ↓
silently ignored
       ↓
caller believes operation may have succeeded
```

Better:

```sql
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(
            'Error: ' || SQLERRM
        );
        RAISE;
END;
/
```

Functions:

```text
SQLCODE
SQLERRM
```

Example:

```sql
DBMS_OUTPUT.PUT_LINE(
    SQLCODE || ': ' || SQLERRM
);
```

Rule:

```text
Handle an error
only if you know what correct handling means.

Otherwise:
log context if appropriate
then re-raise.
```

---

# Part 49 — Stored Procedures

## 49.1 Procedure Architecture

```text
Application
    |
 CALL procedure
    |
    v
Stored Procedure
    |
    +-- validate
    +-- query/update
    +-- transaction-aware logic
    +-- return OUT values
```

Example:

```sql
CREATE OR REPLACE PROCEDURE get_customer_sales (
    p_customer_id IN  customer.customer_id%TYPE,
    p_total_sales OUT NUMBER
)
IS
BEGIN
    SELECT
        NVL(SUM(order_total), 0)
    INTO
        p_total_sales
    FROM orders
    WHERE customer_id = p_customer_id;
END;
/
```

Call from SQL*Plus/SQLcl-style client:

```sql
VARIABLE v_sales NUMBER;

EXEC get_customer_sales(
    100,
    :v_sales
);

PRINT v_sales;
```

## 49.2 Parameter Modes

```text
IN
input

OUT
output

IN OUT
both
```

Prefer `IN` by default unless the API truly needs output mutation.

## 49.3 Defaults

```sql
CREATE OR REPLACE PROCEDURE print_orders (
    p_status IN VARCHAR2 DEFAULT 'NEW'
)
...
```

Named notation can improve readability:

```sql
BEGIN
    print_orders(
        p_status => 'APPROVED'
    );
END;
/
```

---

# Part 50 — Stored Functions

A function returns a value.

```sql
CREATE OR REPLACE FUNCTION line_total (
    p_quantity   IN NUMBER,
    p_unit_price IN NUMBER
)
RETURN NUMBER
IS
BEGIN
    RETURN p_quantity * p_unit_price;
END;
/
```

Use:

```sql
SELECT
    line_total(10, 4.25)
FROM dual;
```

## 50.1 Procedure vs Function

```text
Procedure
    performs an operation/API

Function
    computes/returns a value
```

Functions called from SQL should be designed carefully.

If a function performs expensive queries for every selected row:

```text
10,000 rows
   ×
function query
```

you can create severe performance problems.

---

# Part 51 — Packages

Packages are one of PL/SQL's most important design features.

Architecture:

```text
Package
  |
  +-- Specification
  |     public API
  |
  +-- Body
        implementation
        private helpers
```

## 51.1 Package Specification

```sql
CREATE OR REPLACE PACKAGE pkg_order_api AS

    PROCEDURE create_order (
        p_customer_id IN NUMBER,
        p_order_id    OUT NUMBER
    );

    FUNCTION get_order_total (
        p_order_id IN NUMBER
    ) RETURN NUMBER;

END pkg_order_api;
/
```

## 51.2 Package Body

```sql
CREATE OR REPLACE PACKAGE BODY pkg_order_api AS

    FUNCTION get_order_total (
        p_order_id IN NUMBER
    )
    RETURN NUMBER
    IS
        v_total NUMBER;
    BEGIN
        SELECT NVL(SUM(
                   quantity * unit_price
               ), 0)
        INTO v_total
        FROM order_item
        WHERE order_id = p_order_id;

        RETURN v_total;
    END get_order_total;


    PROCEDURE create_order (
        p_customer_id IN NUMBER,
        p_order_id    OUT NUMBER
    )
    IS
    BEGIN
        INSERT INTO orders (
            order_id,
            customer_id,
            order_date,
            status
        )
        VALUES (
            order_seq.NEXTVAL,
            p_customer_id,
            SYSDATE,
            'NEW'
        )
        RETURNING order_id
        INTO p_order_id;
    END create_order;

END pkg_order_api;
/
```

## 51.3 Why Packages Matter

Benefits:

```text
encapsulation
namespace
public/private separation
reusable API
dependency organization
session package state where intentionally used
```

Application architecture:

```text
Backend
   |
pkg_order_api.create_order
   |
Oracle tables
```

This can be cleaner than granting the application arbitrary direct DML on every table.

---

# Part 52 — Package State

Package-level variables can maintain state within a database session.

Concept:

```text
Session A
  |
Package variable = 10

Session B
  |
Separate package state
```

Stateful packages can be useful but also dangerous with connection pools because:

```text
application request
       ↓
borrow pooled DB session
       ↓
session may contain package state from previous work
```

Prefer stateless APIs unless state is explicitly required and understood.

---

# Part 53 — Procedures, Functions, and Transaction Boundaries

A reusable stored procedure should not casually commit unless the API contract says it owns the entire transaction.

Example:

```text
Application transaction:
    call procedure A
    call procedure B
    update table C
    COMMIT
```

If Procedure A contains hidden:

```sql
COMMIT;
```

the caller loses atomic control.

General design principle:

```text
transaction owner
must be clear
```

Do not sprinkle `COMMIT` inside every procedure.

---

# Part 54 — Triggers

## 54.1 Row-level Trigger

```sql
CREATE OR REPLACE TRIGGER trg_product_price_audit
AFTER UPDATE OF unit_price
ON product
FOR EACH ROW
BEGIN
    INSERT INTO product_price_audit (
        product_id,
        old_price,
        new_price,
        changed_at
    )
    VALUES (
        :NEW.product_id,
        :OLD.unit_price,
        :NEW.unit_price,
        SYSTIMESTAMP
    );
END;
/
```

`:OLD`:

```text
row value before operation
```

`:NEW`:

```text
row value after/new operation
```

## 54.2 Trigger Timing

```text
BEFORE
AFTER
INSTEAD OF
```

## 54.3 Statement-level Trigger

No `FOR EACH ROW`.

Runs once per triggering statement.

Concept:

```text
UPDATE 10,000 rows
      |
statement trigger = once

row trigger = potentially 10,000 times
```

This distinction has major performance/design implications.

---

# Part 55 — `INSTEAD OF` Triggers

Useful for some non-directly-updatable views.

Concept:

```text
Application
   |
UPDATE complex view
   |
INSTEAD OF trigger
   |
custom DML on base tables
```

Example structure:

```sql
CREATE OR REPLACE TRIGGER trg_view_update
INSTEAD OF UPDATE
ON v_complex_order
FOR EACH ROW
BEGIN
    -- controlled updates to base tables
    NULL;
END;
/
```

Use cautiously because behavior becomes less obvious to developers.

---

# Part 56 — Compound Triggers

Compound triggers let one trigger define multiple timing sections.

Concept:

```text
BEFORE STATEMENT
      |
BEFORE EACH ROW
      |
AFTER EACH ROW
      |
AFTER STATEMENT
```

Use cases can include:

- sharing state during one DML statement
- batching row-level audit information
- addressing certain trigger design problems

Do not use them merely because they are advanced syntax.

---

# Part 57 — Mutating-table Problem Concept

A row trigger can run while its table is currently being modified.

Attempting to query/change that same table in an unsafe way from the row trigger can cause a mutating-table error.

Mental model:

```text
UPDATE PRODUCT
   |
Oracle is changing PRODUCT rows
   |
row trigger fires
   |
trigger tries to query unstable PRODUCT state
   |
error
```

Solutions depend on business need and can involve redesign or compound-trigger patterns.

The best solution is often:

```text
do not hide complex cross-row business logic in row triggers
```

---

# Part 58 — Records

Custom record:

```sql
DECLARE
    TYPE t_product_summary IS RECORD (
        product_id   product.product_id%TYPE,
        product_name product.product_name%TYPE,
        total_sales  NUMBER
    );

    v_product t_product_summary;
BEGIN
    v_product.product_id := 1;
    v_product.product_name := 'Bottle 330ml';
    v_product.total_sales := 50000;

    DBMS_OUTPUT.PUT_LINE(
        v_product.product_name
    );
END;
/
```

Record:

```text
one variable
  |
  +-- field 1
  +-- field 2
  +-- field 3
```

Records help model structured in-memory PL/SQL data.

---

# Part 59 — Collections

PL/SQL collection families include:

```text
Associative Arrays
Nested Tables
VARRAYs
```

## 59.1 Associative Array

```sql
DECLARE
    TYPE t_name_map IS TABLE OF VARCHAR2(100)
        INDEX BY PLS_INTEGER;

    v_names t_name_map;
BEGIN
    v_names(1) := 'Ahmed';
    v_names(2) := 'Sara';

    DBMS_OUTPUT.PUT_LINE(v_names(1));
END;
/
```

Useful for in-memory PL/SQL structures.

## 59.2 Nested Table Concept

```text
collection of elements
can be used in PL/SQL
and in some SQL/object-relational scenarios
```

## 59.3 VARRAY

Has an explicit maximum size and ordered elements.

Choose a collection type based on real access needs rather than syntax preference.

---

# Part 60 — Dynamic SQL

## 60.1 `EXECUTE IMMEDIATE`

Example:

```sql
DECLARE
    v_table_name VARCHAR2(30) := 'PRODUCT';
    v_count      NUMBER;
BEGIN
    EXECUTE IMMEDIATE
        'SELECT COUNT(*) FROM ' ||
        v_table_name
    INTO v_count;

    DBMS_OUTPUT.PUT_LINE(v_count);
END;
/
```

Dynamic SQL constructs SQL at runtime.

Use it only when static SQL cannot solve the requirement.

## 60.2 Bind Variables

For data values:

```sql
DECLARE
    v_sql   VARCHAR2(1000);
    v_count NUMBER;
    v_flag  CHAR(1) := 'Y';
BEGIN
    v_sql :=
        'SELECT COUNT(*) ' ||
        'FROM product ' ||
        'WHERE active_flag = :x';

    EXECUTE IMMEDIATE v_sql
        INTO v_count
        USING v_flag;

    DBMS_OUTPUT.PUT_LINE(v_count);
END;
/
```

Bind:

```text
SQL structure stays fixed
value supplied separately
```

This improves safety and cursor reuse.

## 60.3 Dynamic Identifiers Are Different

Bind variables cannot normally replace an object identifier such as a table name.

For dynamic object names:

```text
validate against an allowlist
or
use safe identifier-validation functions/patterns
```

Never concatenate arbitrary user-controlled table or column names.

---

# Part 61 — SQL Injection

Dangerous:

```sql
v_sql :=
    'SELECT * FROM employee ' ||
    'WHERE employee_name = ''' ||
    p_name ||
    '''';
```

Attacker-controlled text can change SQL structure.

Safer:

```sql
v_sql :=
    'SELECT employee_id ' ||
    'FROM employee ' ||
    'WHERE employee_name = :name';

EXECUTE IMMEDIATE v_sql
    INTO v_id
    USING p_name;
```

Security model:

```text
Untrusted Data
     |
     X do not concatenate into SQL syntax
     |
Bind Variable
     ↓
SQL Engine
```

Dynamic SQL is one of the highest-risk areas of database programming when written carelessly.

---

# Part 62 — Bind Variables and Cursor Reuse

Two literal statements:

```sql
SELECT *
FROM product
WHERE product_id = 1;

SELECT *
FROM product
WHERE product_id = 2;
```

Application-side bind concept:

```sql
SELECT *
FROM product
WHERE product_id = :product_id;
```

Benefits can include:

```text
security
less repeated parsing
cursor sharing/reuse
cleaner APIs
```

Do not confuse bind variables with PL/SQL local variables; they exist at the client/SQL interface boundary.

---

# Part 63 — `BULK COLLECT`

Normal row-by-row processing can cause repeated transfers between PL/SQL and SQL processing.

Concept:

```text
PL/SQL
  ↓ one call
SQL
  ↓
PL/SQL
  ↓ one call
SQL
...
```

`BULK COLLECT` retrieves multiple rows into collections.

Example:

```sql
DECLARE
    TYPE t_product_ids IS TABLE OF product.product_id%TYPE;
    TYPE t_names       IS TABLE OF product.product_name%TYPE;

    v_ids   t_product_ids;
    v_names t_names;
BEGIN
    SELECT
        product_id,
        product_name
    BULK COLLECT INTO
        v_ids,
        v_names
    FROM product
    WHERE active_flag = 'Y';

    DBMS_OUTPUT.PUT_LINE(
        'Rows: ' || v_ids.COUNT
    );
END;
/
```

Be careful with huge result sets because bulk collection consumes PGA/session memory.

---

# Part 64 — `FORALL`

`FORALL` sends bulk DML using collection elements.

Example concept:

```sql
DECLARE
    TYPE t_ids IS TABLE OF NUMBER;
    v_ids t_ids := t_ids(1, 2, 3);
BEGIN
    FORALL i IN 1..v_ids.COUNT
        UPDATE product
        SET active_flag = 'N'
        WHERE product_id = v_ids(i);
END;
/
```

Visual:

```text
Row-by-row loop:
PL/SQL -> SQL
PL/SQL -> SQL
PL/SQL -> SQL

FORALL:
PL/SQL =====bulk=====> SQL
```

This can greatly reduce PL/SQL/SQL context-switch overhead.

---

# Part 65 — Bulk Processing with LIMIT

For very large datasets, collecting everything at once can consume too much memory.

A common pattern is:

```text
fetch batch
process batch
fetch next batch
```

Conceptual example:

```sql
DECLARE
    CURSOR c_product IS
        SELECT product_id
        FROM product;

    TYPE t_ids IS TABLE OF product.product_id%TYPE;
    v_ids t_ids;
BEGIN
    OPEN c_product;

    LOOP
        FETCH c_product
        BULK COLLECT INTO v_ids
        LIMIT 1000;

        EXIT WHEN v_ids.COUNT = 0;

        -- bulk processing here
    END LOOP;

    CLOSE c_product;
END;
/
```

Choose batch size by measurement.

---

# Part 66 — PL/SQL and SQL Context Switching

Concept:

```text
PL/SQL Engine
     |
     | call SQL
     v
SQL Engine
     |
     | return
     v
PL/SQL Engine
```

For one call, overhead is trivial.

For millions of loop iterations:

```text
millions of context switches
```

can matter.

Performance hierarchy:

```text
Best when possible:
one set-based SQL statement

Then:
bulk PL/SQL

Last resort:
row-by-row procedural processing
```

This is the principle behind the phrase:

```text
"slow-by-slow"
```

often used to criticize unnecessary row-at-a-time database processing.

---

# Part 67 — Definer Rights vs Invoker Rights

Stored program units execute under a privilege model.

## 67.1 Definer Rights

Default behavior for many stored program units.

Concept:

```text
Caller
  |
execute procedure
  |
procedure runs with owner's stored privilege context
```

This can create a controlled API:

```text
App user
    cannot directly UPDATE sensitive table
    |
    can EXECUTE approved package
    |
package validates business rules
```

## 67.2 Invoker Rights

Declared with:

```sql
AUTHID CURRENT_USER
```

Concept:

```text
procedure executes under caller's rights context
```

Use when reusable logic should respect invoking user's privileges.

## 67.3 Security Design

Ask:

```text
Who owns code?
Who can execute?
What objects can code access?
Should caller inherit owner's power?
```

Stored code is part of the authorization boundary.

---

# Part 68 — Procedure Grants and API Security

Instead of:

```text
APPUSER:
INSERT/UPDATE/DELETE on every order table
```

possible architecture:

```text
APPUSER
   |
EXECUTE pkg_order_api
   |
Package Owner
   |
controlled DML
   |
ORDERS / ORDER_ITEM
```

Grant example:

```sql
GRANT EXECUTE
ON pkg_order_api
TO appuser;
```

This can reduce direct object privileges.

However, package code must be secure, especially dynamic SQL and parameter validation.

---

# Part 69 — Autonomous Transactions

PL/SQL supports autonomous transactions for specialized cases.

Concept:

```text
Main transaction
    |
    +-- Autonomous transaction
          separate commit/rollback scope
```

Typical example might be independent logging.

This feature is powerful and easy to misuse.

Bad pattern:

```text
business transaction fails
but autonomous procedure commits business data anyway
```

Use autonomous transactions only where independent transactional semantics are explicitly required.

---

# Part 70 — Debugging with `DBMS_OUTPUT`

Enable output:

```sql
SET SERVEROUTPUT ON
```

Example:

```sql
BEGIN
    DBMS_OUTPUT.PUT_LINE(
        'Starting order process'
    );
END;
/
```

Useful for:

```text
learning
simple debugging
controlled diagnostic output
```

Not a production logging architecture by itself.

---

# Part 71 — Compilation Errors

Create invalid code and Oracle stores compiler errors.

Example:

```sql
CREATE OR REPLACE PROCEDURE bad_proc
IS
BEGIN
    nonexistent_statement;
END;
/
```

Then:

```sql
SHOW ERRORS
```

or query:

```sql
SELECT
    name,
    type,
    line,
    position,
    text
FROM user_errors
ORDER BY
    name,
    sequence;
```

Troubleshooting workflow:

```text
Compile
  ↓
SHOW ERRORS / USER_ERRORS
  ↓
fix first meaningful error
  ↓
recompile
```

One syntax error can create many secondary error messages.

---

# Part 72 — Invalid Objects

Inspect:

```sql
SELECT
    object_name,
    object_type,
    status
FROM user_objects
WHERE status = 'INVALID';
```

Invalid can result from:

```text
dependency changed
referenced object dropped
compile error
privilege dependency
```

Recompile only after investigating root cause.

---

# Part 73 — Dependencies

Stored PL/SQL depends on referenced objects.

Concept:

```text
PKG_ORDER_API
      |
      +--> ORDERS
      +--> ORDER_ITEM
      +--> CUSTOMER
```

If a dependent object's definition changes, PL/SQL may become invalid and require recompilation.

Inspect dependency information:

```sql
SELECT
    name,
    type,
    referenced_name,
    referenced_type
FROM user_dependencies
WHERE name = 'PKG_ORDER_API';
```

Dependency management matters during deployments.

---

# Part 74 — Exception Logging Pattern

A useful error log might capture:

```text
timestamp
module
operation
business key
error code
error message
```

But never log secrets/passwords unnecessarily.

Conceptual procedure:

```sql
CREATE TABLE application_error_log (
    error_id      NUMBER GENERATED BY DEFAULT AS IDENTITY,
    error_time    TIMESTAMP DEFAULT SYSTIMESTAMP,
    module_name   VARCHAR2(100),
    error_code    NUMBER,
    error_message VARCHAR2(4000)
);
```

Exception logic:

```text
catch expected error
    ↓
add business context
    ↓
log if appropriate
    ↓
re-raise unexpected failure
```

Avoid building a system that turns every error into "success with a log row."

---

# Part 75 — Oracle SQL and PL/SQL Troubleshooting

## 75.1 ORA Errors

Oracle errors use codes such as:

```text
ORA-00001
ORA-00942
ORA-01403
ORA-01422
ORA-06512
```

Do not memorize thousands of codes.

Use:

```text
error code
error message
SQL/PLSQL line
object name
current schema
privileges
data state
```

## 75.2 ORA-00942 — Table or View Does Not Exist

Possible:

```text
wrong schema
object actually absent
missing privilege
synonym points elsewhere
quoted-name mismatch
```

Check:

```sql
SELECT table_name
FROM user_tables;

SELECT owner, table_name
FROM all_tables
WHERE table_name = 'PRODUCT';
```

## 75.3 ORA-00001 — Unique Constraint Violation

Find constraint/index:

```sql
SELECT
    constraint_name,
    table_name
FROM user_constraints
WHERE constraint_type IN ('P', 'U');
```

Ask:

```text
duplicate input?
application retry?
bad natural key?
sequence misuse?
```

## 75.4 ORA-01403 — No Data Found

Common in:

```sql
SELECT ... INTO
```

Handle only if "not found" is expected business behavior.

## 75.5 ORA-01422 — Exact Fetch Returns More Than Requested Rows

Your scalar query returned multiple rows.

Fix:

```text
predicate
business uniqueness
query design
```

Do not hide it with arbitrary `ROWNUM = 1` unless any row truly is acceptable.

## 75.6 Compilation Error

Use:

```sql
SHOW ERRORS
```

and:

```sql
SELECT *
FROM user_errors;
```

## 75.7 Slow PL/SQL

Ask:

```text
Is the real cost SQL?
row-by-row loop?
many context switches?
unbounded BULK COLLECT?
function called per row?
dynamic SQL reparsing?
```

Measure before rewriting everything.

---

# Enhanced Deep-Study Layer — Oracle SQL and PL/SQL Engineering

The original course is preserved below. This enhanced layer adds deeper Oracle SQL semantics, analytic-query patterns, transaction and locking behavior, PL/SQL architecture, bulk processing, package design, dynamic SQL security, stored-code privilege boundaries, instrumentation, deployment discipline, and production troubleshooting.

Core mental model:

```text
Business requirement
      ↓
Set-based SQL first
      ↓
Oracle parser + optimizer
      ↓
Rows / locks / transactions
      ↓
PL/SQL only where orchestration is needed
      ↓
Package API + least privilege
      ↓
Tests + instrumentation + deployment validation
```

## Enhanced Deep Dive 1 — Oracle SQL Parsing and Execution Pipeline

A SQL statement is not executed directly from left to right. Oracle must resolve object names, check privileges, parse syntax, optimize access paths, and execute a cursor. This mental model helps separate syntax errors, privilege errors, parse pressure, and execution-time performance problems.

```text
Client SQL
   ↓
Parse / semantic checks
   ↓
Shared SQL area / cursor
   ↓
Optimizer
   ↓
Execution plan
   ↓
Row-source execution
   ↓
Blocks / indexes / tables
```

```sql
SELECT product_id, product_name
FROM product
WHERE product_id = :id;
```

**Expected behavior:** A reusable statement shape can be shared across executions when the environment and cursor-sharing conditions permit.

**Why it works:** Bind-aware SQL keeps data values separate from SQL structure and usually improves both security and cursor reuse.

**Operational caution:** Do not assume every repeated text reuses the same cursor; schema, optimizer environment, object state, and text differences can affect sharing.

## Enhanced Deep Dive 2 — Hard Parse, Soft Parse, and Cursor Reuse

A hard parse performs expensive work such as semantic analysis and optimization. A soft parse can reuse an existing shareable cursor. High parse rates can consume CPU and library-cache resources even when individual SQL statements are fast.

```text
Literal-heavy workload
SELECT ... id=1
SELECT ... id=2
SELECT ... id=3
      ↓
many statement variants

Bind workload
SELECT ... id=:id
      ↓
one reusable SQL shape
```

```sql
VARIABLE v_id NUMBER;
EXEC :v_id := 100;

SELECT product_name
FROM product
WHERE product_id = :v_id;
```

**Expected behavior:** The bind value changes while the SQL text remains stable.

**Why it works:** Oracle can reuse parsed SQL more effectively when statement text and execution environment are compatible.

**Operational caution:** Do not force cursor-sharing settings as a substitute for fixing an application that concatenates values into SQL.

## Enhanced Deep Dive 3 — Schema Resolution and CURRENT_SCHEMA

Unqualified object names are resolved in a schema context. Understanding this prevents ORA-00942 and accidental access to the wrong object when multiple schemas contain similarly named tables.

```text
Session user
   ↓
current schema
   ↓
object resolution
   ↓
synonym resolution if applicable
```

```sql
SELECT
    SYS_CONTEXT('USERENV','SESSION_USER') AS session_user,
    SYS_CONTEXT('USERENV','CURRENT_SCHEMA') AS current_schema
FROM dual;
```

**Expected behavior:** The two values can differ when current schema is changed for name resolution.

**Why it works:** Authentication identity and name-resolution schema are separate concepts.

**Operational caution:** Changing CURRENT_SCHEMA does not grant privileges.

## Enhanced Deep Dive 4 — NLS Session State Is Part of Query Semantics

Oracle sessions have NLS settings that can affect date parsing, numeric formatting, language, sorting, and comparisons. Production code should not depend on whichever NLS defaults happen to exist on a developer workstation.

```text
Client / pool
   ↓
session NLS settings
   ↓
implicit conversion / formatting
   ↓
query result
```

```sql
SELECT
    parameter,
    value
FROM nls_session_parameters
WHERE parameter IN (
    'NLS_DATE_FORMAT',
    'NLS_DATE_LANGUAGE',
    'NLS_NUMERIC_CHARACTERS'
);
```

**Expected behavior:** The query exposes session-specific formatting rules.

**Why it works:** Explicit literals and format models make behavior deterministic.

**Operational caution:** Avoid `WHERE order_date='01/02/26'`; its meaning can change between sessions.

## Enhanced Deep Dive 5 — ANSI Date, Timestamp, and Interval Literals

Oracle supports explicit literals that avoid many implicit-conversion problems. This is especially valuable in deployment scripts and automated tests.

```text
text literal with explicit type
      ↓
deterministic temporal value
```

```sql
SELECT
    DATE '2026-08-19' AS d,
    TIMESTAMP '2026-08-19 14:00:00' AS ts,
    INTERVAL '2' DAY AS two_days
FROM dual;
```

**Expected behavior:** Oracle returns typed temporal values without depending on NLS date formatting.

**Why it works:** The datatype is encoded in the SQL itself.

**Operational caution:** For timezone-sensitive systems, define whether a business value is a local wall-clock time or an absolute instant.

## Enhanced Deep Dive 6 — TIMESTAMP WITH TIME ZONE vs LOCAL TIME ZONE

Oracle provides different timestamp semantics. `TIMESTAMP WITH TIME ZONE` preserves timezone information, while `TIMESTAMP WITH LOCAL TIME ZONE` normalizes storage and presents values relative to session timezone. This distinction matters for globally distributed systems.

```text
event instant
  ↓
timezone-aware datatype
  ↓
session rendering
```

```sql
SELECT
    SYSTIMESTAMP,
    CURRENT_TIMESTAMP,
    SESSIONTIMEZONE,
    DBTIMEZONE
FROM dual;
```

**Expected behavior:** You can compare server timestamp, session timestamp, and timezone settings.

**Why it works:** Timestamp datatype selection is a business-model decision, not merely a formatting decision.

**Operational caution:** Do not store a worldwide event as plain text because timezone interpretation becomes application-specific and error-prone.

## Enhanced Deep Dive 7 — Oracle Empty String and NULL Semantics

Oracle SQL treats a zero-length character string as NULL in many SQL contexts. Code ported from databases that distinguish `''` from NULL must be reviewed carefully.

```text
'' in character SQL
      ↓
NULL-like behavior
      ↓
IS NULL semantics
```

```sql
SELECT
    CASE
        WHEN '' IS NULL THEN 'EMPTY BECOMES NULL'
        ELSE 'DISTINCT'
    END AS result
FROM dual;
```

**Expected behavior:** The result demonstrates Oracle's character empty-string behavior.

**Why it works:** Oracle historically normalizes zero-length character values to NULL in SQL.

**Operational caution:** Do not design business rules that require reliable distinction between empty string and NULL without an explicit representation.

## Enhanced Deep Dive 8 — NULL Logic and LNNVL Awareness

NULL introduces UNKNOWN into predicates. Oracle also provides specialized constructs such as `LNNVL` for cases where an expression being FALSE or UNKNOWN must be handled together, particularly in optimizer-generated or advanced filtering logic.

```text
predicate
 ├─ TRUE
 ├─ FALSE
 └─ UNKNOWN
```

```sql
SELECT product_id, unit_price
FROM product
WHERE unit_price IS NULL
   OR unit_price < 10;
```

**Expected behavior:** Rows with NULL price are handled explicitly instead of relying on normal comparison.

**Why it works:** A normal comparison with NULL does not evaluate TRUE.

**Operational caution:** Prefer clear `IS NULL` logic in application SQL; use specialized operators only when they make intent clearer.

## Enhanced Deep Dive 9 — CASE, COALESCE, NVL, and Datatype Conversion

Oracle conditional/null functions can have different datatype-resolution behavior. `CASE` and `COALESCE` are generally expressive and portable; `NVL` is common in Oracle code but may introduce implicit conversion depending on argument types.

```text
input expressions
   ↓ datatype resolution
conditional/null selection
   ↓ result type
```

```sql
SELECT
    product_id,
    COALESCE(product_name, 'UNKNOWN') AS product_name,
    CASE
        WHEN unit_price IS NULL THEN 'NO PRICE'
        WHEN unit_price >= 100 THEN 'HIGH'
        ELSE 'NORMAL'
    END AS price_state
FROM product;
```

**Expected behavior:** The output preserves rows while classifying missing and non-missing values.

**Why it works:** Conditional logic is performed set-wise inside SQL.

**Operational caution:** Be cautious with `NVL(number_col, 'N/A')`; implicit conversion can fail.

## Enhanced Deep Dive 10 — Scalar Subquery Expressions

A scalar subquery is expected to return one column and at most one row. It is useful for attaching one derived value to each outer row, but the cardinality assumption must be true.

```text
outer row
   ↓
scalar subquery
   ↓
0 rows → NULL
1 row  → value
>1     → error
```

```sql
SELECT
    p.product_id,
    p.product_name,
    (
        SELECT MAX(oi.unit_price)
        FROM order_item oi
        WHERE oi.product_id = p.product_id
    ) AS max_sold_price
FROM product p;
```

**Expected behavior:** Every product remains one row with a derived maximum sold price.

**Why it works:** The aggregate guarantees one scalar result per product.

**Operational caution:** Do not hide a non-unique business relationship behind `MAX` or `MIN` merely to suppress a too-many-rows problem.

## Enhanced Deep Dive 11 — EXISTS as a Semi-Join Mental Model

`EXISTS` asks whether at least one matching row exists. Oracle can transform this into semi-join strategies; the inner SELECT list itself is normally irrelevant to the existence test.

```text
Customer row
   ↓
Any matching order?
   ├─ yes → keep customer
   └─ no  → discard
```

```sql
SELECT c.customer_id, c.customer_name
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

**Expected behavior:** A customer appears once regardless of how many orders exist.

**Why it works:** EXISTS tests existence, not multiplication of rows.

**Operational caution:** Do not replace it with a normal join plus `DISTINCT` unless the join semantics are actually what you need.

## Enhanced Deep Dive 12 — NOT EXISTS as an Anti-Join Mental Model

`NOT EXISTS` is usually the clearest anti-join pattern because it avoids the NULL trap of `NOT IN`.

```text
Customer row
   ↓
matching order?
   ├─ yes → reject
   └─ no  → keep
```

```sql
SELECT c.customer_id, c.customer_name
FROM customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

**Expected behavior:** Only customers with no related order remain.

**Why it works:** The correlated existence predicate has explicit anti-match semantics.

**Operational caution:** If the inner predicate is wrong or too broad, anti-joins can silently exclude large portions of data; validate cardinality.

## Enhanced Deep Dive 13 — Subquery Factoring with WITH

The `WITH` clause gives complex query stages meaningful names. It improves readability and can help isolate business logic for testing. Oracle may inline or materialize query blocks depending on optimization decisions.

```text
raw tables
   ↓
WITH stage_1
   ↓
WITH stage_2
   ↓
final report
```

```sql
WITH customer_sales AS (
    SELECT
        o.customer_id,
        SUM(oi.quantity * oi.unit_price) AS sales
    FROM orders o
    JOIN order_item oi
      ON oi.order_id = o.order_id
    GROUP BY o.customer_id
)
SELECT *
FROM customer_sales
ORDER BY sales DESC;
```

**Expected behavior:** The query exposes one named intermediate result rather than repeating the aggregation.

**Why it works:** A CTE is primarily a query-organization construct; physical execution is still chosen by the optimizer.

**Operational caution:** Do not assume every CTE is automatically materialized.

## Enhanced Deep Dive 14 — Recursive Subquery Factoring

Oracle supports recursive subquery factoring for recursive data problems in addition to `CONNECT BY`. Recursive CTE-style logic can make graph/tree algorithms more portable and explicit.

```text
anchor rows
   ↓
recursive member
   ↓
new rows
   ↓
repeat until no new rows
```

```sql
WITH org (employee_id, employee_name, manager_id, lvl) AS (
    SELECT employee_id, employee_name, manager_id, 1
    FROM employee
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.employee_id, e.employee_name, e.manager_id, o.lvl + 1
    FROM employee e
    JOIN org o
      ON e.manager_id = o.employee_id
)
SELECT *
FROM org;
```

**Expected behavior:** The hierarchy expands from root employees to descendants.

**Why it works:** The anchor seeds recursion; the recursive member finds the next level.

**Operational caution:** Always design cycle protection for data that can contain loops.

## Enhanced Deep Dive 15 — CONNECT BY Cycle Protection

Hierarchical data can contain accidental cycles. `NOCYCLE` and related pseudocolumns help detect them instead of allowing traversal to fail unexpectedly.

```text
A → B → C
    ↑   ↓
    └───┘ cycle
```

```sql
SELECT
    employee_id,
    manager_id,
    LEVEL,
    CONNECT_BY_ISCYCLE AS is_cycle
FROM employee
START WITH manager_id IS NULL
CONNECT BY NOCYCLE PRIOR employee_id = manager_id;
```

**Expected behavior:** Rows involved in a detected cycle can be identified.

**Why it works:** Cycle-aware traversal is essential for user-maintained organizational data.

**Operational caution:** Do not simply suppress cycles without correcting the business data that created them.

## Enhanced Deep Dive 16 — CONNECT_BY_ROOT and Path Construction

Hierarchical queries can expose the root ancestor and full traversal path, which is useful for organization charts, BOMs, and category trees.

```text
root
 ↓
child
 ↓
grandchild
   ↘ path/root metadata
```

```sql
SELECT
    employee_id,
    CONNECT_BY_ROOT employee_name AS root_manager,
    SYS_CONNECT_BY_PATH(employee_name, ' / ') AS hierarchy_path
FROM employee
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
```

**Expected behavior:** Each row can show its top-level root and complete path.

**Why it works:** Oracle maintains hierarchy context during traversal.

**Operational caution:** Paths can become large; use them for reporting/diagnosis rather than as a substitute for normalized parent relationships.

## Enhanced Deep Dive 17 — Analytic PARTITION BY vs ORDER BY

Analytic functions define a window with two independent ideas: partitioning determines which rows belong together; ordering determines sequence inside each partition.

```text
All rows
  ↓ PARTITION BY department
Dept A | Dept B
  ↓ ORDER BY salary
ordered rows per department
```

```sql
SELECT
    employee_id,
    department_id,
    salary,
    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS dept_avg,
    ROW_NUMBER() OVER (
        PARTITION BY department_id
        ORDER BY salary DESC, employee_id
    ) AS rn
FROM employee;
```

**Expected behavior:** The average is repeated per row while rank is deterministic within department.

**Why it works:** Analytic functions preserve detail rows while adding set-aware calculations.

**Operational caution:** Always add a deterministic tie-breaker when row numbering must be stable.

## Enhanced Deep Dive 18 — ROWS vs RANGE Window Frames

`ROWS` counts physical rows in the ordered result; `RANGE` groups peers according to ordering values. Running totals can differ when multiple rows share the same ordering key.

```text
ORDER BY date
same date has 3 rows

ROWS  → advances row by row
RANGE → peers may share frame boundary
```

```sql
SELECT
    order_id,
    order_date,
    order_total,
    SUM(order_total) OVER (
        ORDER BY order_date, order_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders;
```

**Expected behavior:** The explicit ROWS frame produces deterministic row-by-row accumulation.

**Why it works:** Window-frame semantics are part of correctness, not just performance.

**Operational caution:** Do not rely on default frames for financial running totals without confirming peer behavior.

## Enhanced Deep Dive 19 — FIRST_VALUE and LAST_VALUE

These functions return values from the current analytic frame. `LAST_VALUE` often surprises learners because the default frame may end at the current row rather than the entire partition.

```text
partition
[first ........ current ........ last]
frame boundary determines FIRST/LAST
```

```sql
SELECT
    department_id,
    employee_id,
    salary,
    FIRST_VALUE(salary) OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS highest_salary,
    LAST_VALUE(salary) OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS lowest_salary
FROM employee;
```

**Expected behavior:** Every row in a department sees the same highest and lowest values.

**Why it works:** The full-partition frame makes the intended boundary explicit.

**Operational caution:** Never assume `LAST_VALUE` means last row in partition unless you define the frame accordingly.

## Enhanced Deep Dive 20 — NTILE and Percentile-style Reporting

`NTILE` divides ordered rows into approximate buckets, useful for quartiles/deciles and operational segmentation.

```text
ordered salaries
  ↓
bucket 1 | bucket 2 | bucket 3 | bucket 4
```

```sql
SELECT
    employee_id,
    salary,
    NTILE(4) OVER (
        ORDER BY salary DESC
    ) AS salary_quartile
FROM employee;
```

**Expected behavior:** Employees are assigned to four ordered groups.

**Why it works:** Analytic bucketing avoids procedural sorting loops.

**Operational caution:** NTILE groups by row count, not by equal numeric salary ranges.

## Enhanced Deep Dive 21 — LISTAGG and Overflow Awareness

`LISTAGG` turns multiple row values into one delimited string. It is useful for reporting but can create very large results and should not replace normalized relationships.

```text
rows
A
B
C
 ↓
'A, B, C'
```

```sql
SELECT
    department_id,
    LISTAGG(employee_name, ', ')
        WITHIN GROUP (ORDER BY employee_name) AS employees
FROM employee
GROUP BY department_id;
```

**Expected behavior:** One row per department contains a delimited employee list.

**Why it works:** Aggregation occurs in SQL rather than application loops.

**Operational caution:** For large groups, use the overflow controls supported by your Oracle release or return rows instead of forcing giant strings.

## Enhanced Deep Dive 22 — GROUPING and GROUPING_ID

ROLLUP/CUBE output can contain NULLs that mean either 'real NULL data' or 'subtotal level'. `GROUPING` and `GROUPING_ID` distinguish those cases.

```text
detail row NULL
vs
subtotal-generated NULL
      ↓
GROUPING metadata
```

```sql
SELECT
    department_id,
    status,
    SUM(order_total) AS total,
    GROUPING(department_id) AS g_dept,
    GROUPING(status) AS g_status
FROM orders
GROUP BY ROLLUP(department_id, status);
```

**Expected behavior:** Subtotal rows can be identified without guessing from NULL values.

**Why it works:** Oracle attaches grouping metadata to superaggregate rows.

**Operational caution:** Never label every NULL in a ROLLUP result as 'TOTAL' without checking grouping metadata.

## Enhanced Deep Dive 23 — PIVOT Is Schema-shaped Reporting

PIVOT converts row values into columns. The output column set is normally declared in SQL, which makes PIVOT useful for known reporting dimensions but less natural for highly dynamic categories.

```text
rows:
month,status,qty
   ↓ PIVOT
month | GOOD | REJECT
```

```sql
SELECT *
FROM (
    SELECT production_month, status, quantity
    FROM monthly_quality
)
PIVOT (
    SUM(quantity)
    FOR status IN ('GOOD' AS good, 'REJECT' AS reject)
);
```

**Expected behavior:** One row per month contains separate aggregate columns.

**Why it works:** PIVOT is syntactic support for conditional aggregation.

**Operational caution:** For truly dynamic categories, application/report-layer generation or controlled dynamic SQL may be clearer.

## Enhanced Deep Dive 24 — ROW LIMITING and Deterministic Pagination

Pagination is stable only when the ordering uniquely determines row order. Ordering by a non-unique timestamp alone can cause rows to move between pages.

```text
ORDER BY order_date only
ties → unstable page boundary

ORDER BY order_date, order_id
ties resolved
```

```sql
SELECT order_id, order_date, status
FROM orders
ORDER BY order_date DESC, order_id DESC
OFFSET 20 ROWS
FETCH NEXT 10 ROWS ONLY;
```

**Expected behavior:** A stable tie-breaker makes page boundaries deterministic.

**Why it works:** Pagination is a data-ordering problem, not merely a syntax problem.

**Operational caution:** Large OFFSET values can become inefficient; keyset/seek pagination may be preferable for high-volume APIs.

## Enhanced Deep Dive 25 — Keyset Pagination Pattern

Instead of skipping an ever-growing number of rows, keyset pagination starts after the last key seen by the client.

```text
page 1 last key = (date,id)
      ↓
page 2 WHERE key < last_key
```

```sql
SELECT order_id, order_date, status
FROM orders
WHERE (order_date < :last_date)
   OR (order_date = :last_date AND order_id < :last_id)
ORDER BY order_date DESC, order_id DESC
FETCH FIRST 10 ROWS ONLY;
```

**Expected behavior:** The next page starts from the previous page's final ordering key.

**Why it works:** The database can use a matching index to seek near the next page instead of discarding many prior rows.

**Operational caution:** The predicate must exactly match the sort direction and tie-breaker semantics.

## Enhanced Deep Dive 26 — DML RETURNING

Oracle can return generated or changed column values directly from DML into PL/SQL variables, avoiding a second SELECT.

```text
INSERT/UPDATE
   ↓
RETURNING
   ↓
PL/SQL variable
```

```sql
DECLARE
    v_order_id orders.order_id%TYPE;
BEGIN
    INSERT INTO orders (
        order_id, customer_id, order_date, status
    )
    VALUES (
        order_seq.NEXTVAL, 100, SYSDATE, 'NEW'
    )
    RETURNING order_id INTO v_order_id;

    DBMS_OUTPUT.PUT_LINE(v_order_id);
END;
/
```

**Expected behavior:** The inserted identifier is immediately available in the block.

**Why it works:** Oracle already knows the changed row values during DML.

**Operational caution:** For multi-row DML, use the forms appropriate to bulk operations rather than assuming scalar RETURNING semantics.

## Enhanced Deep Dive 27 — Multi-table INSERT

Oracle can route one source query into multiple target tables. This is useful for controlled ETL-like transformations.

```text
source rows
   ↓
conditional routing
   ├→ target A
   └→ target B
```

```sql
INSERT ALL
    WHEN reject_qty = 0 THEN
        INTO good_run_archive(run_id, good_qty)
        VALUES(run_id, good_qty)
    WHEN reject_qty > 0 THEN
        INTO rejected_run_archive(run_id, reject_qty)
        VALUES(run_id, reject_qty)
SELECT run_id, good_qty, reject_qty
FROM production_run_stage;
```

**Expected behavior:** Source rows can create target rows according to conditions.

**Why it works:** The routing logic is executed set-wise.

**Operational caution:** Treat it as ETL logic with clear validation and transaction boundaries; do not make hidden routing rules impossible to audit.

## Enhanced Deep Dive 28 — MERGE Source Cardinality Safety

`MERGE` assumes the source/target relationship can be matched according to the ON clause. If multiple source rows target the same row, Oracle can reject the operation or produce logic that does not match business expectations.

```text
stage rows
A(code=X)
B(code=X)
   ↓
target code=X
   ↓
ambiguous update source
```

```sql
SELECT product_code, COUNT(*)
FROM product_stage
GROUP BY product_code
HAVING COUNT(*) > 1;
```

**Expected behavior:** The precheck finds duplicate source business keys before MERGE.

**Why it works:** Uniqueness should be validated before applying synchronization logic.

**Operational caution:** Do not use MERGE as a substitute for a clean staging model.

## Enhanced Deep Dive 29 — Sequence Cache and Gaps

Caching improves sequence scalability by reserving values in memory. Unused cached values can be lost on instance failure, and rolled-back transactions do not return values. Therefore sequences provide uniqueness/order generation, not gapless numbering.

```text
sequence cache:
100..199 reserved
      ↓
instance stops after 120
      ↓
some values never used
```

```sql
CREATE SEQUENCE order_seq
    START WITH 1
    INCREMENT BY 1
    CACHE 100
    NO CYCLE;
```

**Expected behavior:** Values are generated efficiently with expected gaps.

**Why it works:** Sequence generation is intentionally decoupled from transaction rollback.

**Operational caution:** Legal invoice numbering often requires a separate controlled business process, not a normal cached sequence.

## Enhanced Deep Dive 30 — Identity Column Options

Identity columns wrap sequence-like key generation behind table metadata. `GENERATED ALWAYS` and `GENERATED BY DEFAULT` express different rules about whether callers may provide values.

```text
INSERT
  ↓
identity policy
  ├→ database-generated
  └→ caller value allowed depending on definition
```

```sql
CREATE TABLE machine (
    machine_id NUMBER
        GENERATED ALWAYS AS IDENTITY,
    machine_name VARCHAR2(100) NOT NULL,
    CONSTRAINT pk_machine PRIMARY KEY(machine_id)
);
```

**Expected behavior:** Normal inserts omit `machine_id` and Oracle generates it.

**Why it works:** Identity syntax makes ownership of key generation explicit in the table definition.

**Operational caution:** Choose policy deliberately for migration/import scenarios where preserving existing identifiers may matter.

## Enhanced Deep Dive 31 — Virtual Columns

A virtual column derives its value from other columns and can participate in indexes/constraints when supported by the expression.

```text
base columns
qty × price
   ↓
virtual column line_total
```

```sql
CREATE TABLE order_line_demo (
    quantity NUMBER NOT NULL,
    unit_price NUMBER(12,2) NOT NULL,
    line_total NUMBER(14,2)
        GENERATED ALWAYS AS (quantity * unit_price) VIRTUAL
);
```

**Expected behavior:** `line_total` is computed from source columns rather than independently stored by application code.

**Why it works:** The database owns the derivation, reducing drift.

**Operational caution:** Do not put volatile or business-process logic into virtual columns just because an expression can be written.

## Enhanced Deep Dive 32 — Function-based Indexes and Expression Matching

A function-based index stores an expression result. The query must use semantically compatible expression logic for the optimizer to benefit.

```text
email
 ↓ UPPER(email)
function-based index
 ↓
case-insensitive lookup
```

```sql
CREATE INDEX ix_employee_upper_email
ON employee(UPPER(email));

SELECT employee_id
FROM employee
WHERE UPPER(email) = UPPER(:p_email);
```

**Expected behavior:** The plan can use the expression index when statistics and selectivity make it beneficial.

**Why it works:** The indexed expression converts a repeated runtime computation/search into an indexed access path.

**Operational caution:** Ensure NLS-sensitive functions and expression semantics are stable for the intended use.

## Enhanced Deep Dive 33 — Materialized Views

A materialized view stores query results physically and refreshes them according to a defined strategy. It is useful for expensive summaries but introduces refresh and staleness semantics.

```text
base tables
   ↓ refresh
materialized view
   ↓
fast reporting
```

```sql
CREATE MATERIALIZED VIEW mv_monthly_sales
BUILD IMMEDIATE
REFRESH COMPLETE ON DEMAND
AS
SELECT
    TRUNC(order_date, 'MM') AS month_start,
    SUM(order_total) AS sales
FROM orders
GROUP BY TRUNC(order_date, 'MM');
```

**Expected behavior:** The summary is stored and can be refreshed on demand.

**Why it works:** Precomputation trades freshness and refresh cost for read performance.

**Operational caution:** Do not present stale materialized data as real-time without documenting refresh guarantees.

## Enhanced Deep Dive 34 — Constraint Deferrability

Some Oracle constraints can be defined as deferrable so validation occurs at transaction commit rather than after each statement. This is useful for tightly controlled multi-step transformations.

```text
statement 1 temporarily violates
statement 2 repairs
   ↓
COMMIT
   ↓
deferred constraint validated
```

```sql
CREATE TABLE demo_parent (
    id NUMBER,
    CONSTRAINT pk_demo_parent
        PRIMARY KEY(id)
        DEFERRABLE INITIALLY IMMEDIATE
);
```

**Expected behavior:** The constraint can be deferred in a transaction when allowed.

**Why it works:** Deferred enforcement changes when consistency is checked, not whether consistency matters.

**Operational caution:** Use only when the transaction genuinely needs temporary inconsistency; otherwise immediate validation is easier to reason about.

## Enhanced Deep Dive 35 — Constraint ENABLE, DISABLE, VALIDATE, and NOVALIDATE

Oracle constraint state can distinguish whether new DML is enforced and whether existing rows have been validated. Migration scripts must inspect actual state instead of assuming a named constraint is fully trusted.

```text
constraint metadata
  ├→ enabled?
  └→ validated?
      ↓
different enforcement guarantees
```

```sql
SELECT
    constraint_name,
    status,
    validated
FROM user_constraints
WHERE table_name = 'PRODUCT';
```

**Expected behavior:** The result shows both enforcement and validation state.

**Why it works:** Oracle supports operational loading/migration states more nuanced than simply 'constraint exists'.

**Operational caution:** Do not leave NOVALIDATE constraints undocumented after bulk loads.

## Enhanced Deep Dive 36 — Oracle Read Consistency

A normal query sees a transactionally consistent view of data. Oracle uses undo information to reconstruct older block versions when concurrent writers have changed them.

```text
Query starts at SCN X
   ↓
block now newer
   ↓
undo
   ↓
reconstruct version visible at X
```

```sql
-- Session A
UPDATE product
SET unit_price = unit_price + 1
WHERE product_id = 1;

-- Session B, before A commits
SELECT unit_price
FROM product
WHERE product_id = 1;
```

**Expected behavior:** Session B normally sees the previously committed value rather than the uncommitted change.

**Why it works:** Oracle's multiversion read consistency separates readers from uncommitted writers.

**Operational caution:** Long queries need sufficient undo history; otherwise old versions may no longer be reconstructable.

## Enhanced Deep Dive 37 — SELECT FOR UPDATE

`FOR UPDATE` intentionally converts a read into a locking workflow for rows that will be modified based on their current state.

```text
read row
  ↓ lock
validate business rule
  ↓
update
  ↓
commit / rollback
```

```sql
SELECT quantity
INTO :v_qty
FROM inventory
WHERE product_id = :p_id
FOR UPDATE;
```

**Expected behavior:** A conflicting writer waits or fails according to additional locking options.

**Why it works:** The transaction reserves the selected row for coordinated change.

**Operational caution:** Keep the transaction short; never hold row locks while waiting for user interaction.

## Enhanced Deep Dive 38 — NOWAIT and SKIP LOCKED

Oracle can avoid waiting indefinitely for locked rows. `NOWAIT` fails immediately; `SKIP LOCKED` can be useful for queue/worker patterns where multiple consumers safely process different rows.

```text
workers
  ↓
candidate jobs
  ↓
locked jobs skipped
  ↓
each worker gets different work
```

```sql
SELECT job_id
FROM job_queue
WHERE status = 'READY'
FOR UPDATE SKIP LOCKED;
```

**Expected behavior:** Each concurrent worker can claim currently unlocked work.

**Why it works:** The lock itself becomes a coordination mechanism.

**Operational caution:** `SKIP LOCKED` changes business semantics: skipped rows are not necessarily complete; they are merely locked elsewhere.

## Enhanced Deep Dive 39 — DDL Transaction Boundaries

Oracle DDL performs implicit commit behavior around successful DDL operations. Therefore DDL mixed with uncommitted business DML can destroy the caller's expectation of rollback.

```text
DML uncommitted
   ↓
DDL
   ↓
implicit transaction boundary
   ↓
earlier DML may be committed
```

```sql
-- Lab only
UPDATE product
SET active_flag = 'N'
WHERE product_id = 1;

CREATE TABLE ddl_test(id NUMBER);

-- ROLLBACK cannot be assumed to undo the earlier DML.
```

**Expected behavior:** The lab demonstrates why schema changes should be separated from business transactions.

**Why it works:** DDL participates in database metadata changes with its own transaction semantics.

**Operational caution:** Migration tools must coordinate schema DDL and data changes explicitly.

## Enhanced Deep Dive 40 — PL/SQL Compilation Model

Stored PL/SQL is compiled into database schema objects. Compilation checks syntax and many object references, but runtime errors can still occur because of data, privileges, dynamic SQL, or environment.

```text
source
  ↓ compile
VALID or INVALID object
  ↓ execute
runtime behavior
```

```sql
CREATE OR REPLACE PROCEDURE p_demo
IS
BEGIN
    DBMS_OUTPUT.PUT_LINE('compiled');
END;
/

SELECT object_name, status
FROM user_objects
WHERE object_name = 'P_DEMO';
```

**Expected behavior:** A successfully compiled object appears VALID.

**Why it works:** Stored code has lifecycle and dependency state inside the database.

**Operational caution:** A VALID object can still fail at runtime; compilation is necessary but not sufficient verification.

## Enhanced Deep Dive 41 — PL/SQL Native Types and PLS_INTEGER

PL/SQL provides types optimized for procedural work. `PLS_INTEGER` is commonly appropriate for integer loop counters and in-memory arithmetic where database column anchoring is not required.

```text
SQL column types
vs
PL/SQL procedural types
```

```sql
DECLARE
    v_counter PLS_INTEGER := 0;
BEGIN
    FOR i IN 1..100 LOOP
        v_counter := v_counter + 1;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE(v_counter);
END;
/
```

**Expected behavior:** The counter ends at 100.

**Why it works:** PL/SQL can use procedural datatypes without creating database columns.

**Operational caution:** Use `%TYPE` when a variable represents a database column so schema changes propagate to declarations.

## Enhanced Deep Dive 42 — Record Types and Strong In-memory Structure

Records group fields into one PL/SQL value. They are clearer than parallel scalar variables for structured business data.

```text
record
 ├─ id
 ├─ name
 └─ price
```

```sql
DECLARE
    TYPE t_product_rec IS RECORD (
        product_id   product.product_id%TYPE,
        product_name product.product_name%TYPE,
        unit_price   product.unit_price%TYPE
    );
    v_product t_product_rec;
BEGIN
    SELECT product_id, product_name, unit_price
    INTO v_product
    FROM product
    WHERE product_id = 1;

    DBMS_OUTPUT.PUT_LINE(v_product.product_name);
END;
/
```

**Expected behavior:** One strongly structured variable represents the selected product.

**Why it works:** The record mirrors a logical data object without requiring a database object type.

**Operational caution:** Prefer `%ROWTYPE` when the entire table/cursor row is appropriate; custom records are better when only selected fields belong to the API.

## Enhanced Deep Dive 43 — Associative Arrays

Associative arrays are PL/SQL in-memory key/value collections. They are excellent for procedural lookup tables, batch identifiers, and temporary structures.

```text
index/key
  ↓
value
1 → A
2 → B
```

```sql
DECLARE
    TYPE t_name_map IS TABLE OF VARCHAR2(100)
        INDEX BY PLS_INTEGER;
    v_names t_name_map;
BEGIN
    v_names(10) := 'Bottle';
    v_names(20) := 'Jar';

    DBMS_OUTPUT.PUT_LINE(v_names(20));
END;
/
```

**Expected behavior:** The value `Jar` is retrieved by associative index 20.

**Why it works:** Associative arrays do not require persistent tables.

**Operational caution:** They exist only in PL/SQL memory and are not a replacement for shared persistent relational data.

## Enhanced Deep Dive 44 — Collection Methods

PL/SQL collections expose methods such as `COUNT`, `FIRST`, `LAST`, `NEXT`, `PRIOR`, `EXISTS`, `DELETE`, `EXTEND`, and `TRIM` depending on collection type.

```text
collection
  ↓ metadata methods
COUNT / FIRST / LAST / EXISTS
```

```sql
DECLARE
    TYPE t_ids IS TABLE OF NUMBER;
    v_ids t_ids := t_ids(10,20,30);
BEGIN
    DBMS_OUTPUT.PUT_LINE('Count=' || v_ids.COUNT);
    DBMS_OUTPUT.PUT_LINE('First=' || v_ids(v_ids.FIRST));
END;
/
```

**Expected behavior:** The block reports collection size and first value.

**Why it works:** Collection methods make iteration safer than assuming dense indexes.

**Operational caution:** Associative arrays can be sparse; do not blindly loop `1..COUNT` unless indexes are guaranteed dense.

## Enhanced Deep Dive 45 — BULK COLLECT with LIMIT

Bulk fetching reduces SQL-to-PL/SQL context switches, while `LIMIT` prevents one fetch from consuming unbounded session memory.

```text
cursor
 ↓ fetch 500
collection
 ↓ process
fetch next 500
 ↓
repeat
```

```sql
DECLARE
    CURSOR c_orders IS
        SELECT order_id, status
        FROM orders;

    TYPE t_order_tab IS TABLE OF c_orders%ROWTYPE;
    v_orders t_order_tab;
BEGIN
    OPEN c_orders;
    LOOP
        FETCH c_orders
        BULK COLLECT INTO v_orders
        LIMIT 500;

        EXIT WHEN v_orders.COUNT = 0;

        DBMS_OUTPUT.PUT_LINE(
            'Batch size=' || v_orders.COUNT
        );
    END LOOP;
    CLOSE c_orders;
END;
/
```

**Expected behavior:** Rows are processed in bounded batches.

**Why it works:** Bulk operations reduce round-trips between PL/SQL and SQL engines while controlling PGA usage.

**Operational caution:** Do not use unlimited BULK COLLECT on millions of rows unless memory impact is explicitly acceptable.

## Enhanced Deep Dive 46 — FORALL SAVE EXCEPTIONS

`FORALL` can continue bulk DML after individual row errors when `SAVE EXCEPTIONS` is used, allowing the caller to inspect failed iterations afterward.

```text
collection
 ↓ bulk DML
success success error success
        ↓
bulk exception list
```

```sql
DECLARE
    TYPE t_ids IS TABLE OF NUMBER;
    v_ids t_ids := t_ids(1,2,3);
BEGIN
    FORALL i IN 1..v_ids.COUNT SAVE EXCEPTIONS
        UPDATE product
        SET active_flag = 'N'
        WHERE product_id = v_ids(i);
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(
            'Bulk errors=' || SQL%BULK_EXCEPTIONS.COUNT
        );
        RAISE;
END;
/
```

**Expected behavior:** Bulk exceptions can be counted and mapped back to iteration indexes.

**Why it works:** The bulk operation is not forced to stop at the first row-level error.

**Operational caution:** Design partial-success semantics carefully; continuing after errors is not automatically correct for an atomic business transaction.

## Enhanced Deep Dive 47 — SQL%BULK_EXCEPTIONS Diagnostics

Each saved bulk exception includes the iteration index and Oracle error code. This allows precise reconciliation of failed input records.

```text
input[i]
  ↓ FORALL
error
  ↓
SQL%BULK_EXCEPTIONS(j).ERROR_INDEX
SQL%BULK_EXCEPTIONS(j).ERROR_CODE
```

```sql
-- inside a bulk exception handler:
FOR j IN 1..SQL%BULK_EXCEPTIONS.COUNT LOOP
    DBMS_OUTPUT.PUT_LINE(
        'Index=' ||
        SQL%BULK_EXCEPTIONS(j).ERROR_INDEX ||
        ', Code=' ||
        SQL%BULK_EXCEPTIONS(j).ERROR_CODE
    );
END LOOP;
```

**Expected behavior:** The handler identifies which collection element failed.

**Why it works:** Bulk diagnostics preserve correspondence between batch input and errors.

**Operational caution:** Never log sensitive record contents merely because an iteration failed.

## Enhanced Deep Dive 48 — REF CURSORs

REF CURSORs let PL/SQL return query result sets to callers. Strongly typed variants constrain row shape; weak variants provide flexibility.

```text
procedure
  ↓ open cursor for query
REF CURSOR
  ↓
client fetches rows
```

```sql
CREATE OR REPLACE PACKAGE pkg_reports AS
    TYPE t_order_cur IS REF CURSOR;

    PROCEDURE open_orders (
        p_customer_id IN NUMBER,
        p_result OUT t_order_cur
    );
END pkg_reports;
/
```

**Expected behavior:** The package can expose a cursor handle rather than copying every row into PL/SQL scalars.

**Why it works:** REF CURSORs are a database API boundary for result sets.

**Operational caution:** Define ownership/lifetime clearly; clients must fetch/close result sets appropriately.

## Enhanced Deep Dive 49 — Strong vs Weak REF CURSOR

A strong REF CURSOR declares a RETURN row type; a weak REF CURSOR can point to different query shapes. Strong typing catches mismatches earlier, while weak typing is useful for generic reporting APIs.

```text
strong
→ fixed row contract

weak
→ flexible query shape
```

```sql
DECLARE
    TYPE t_product_cur IS REF CURSOR
        RETURN product%ROWTYPE;

    v_cur t_product_cur;
BEGIN
    OPEN v_cur FOR
        SELECT *
        FROM product
        WHERE active_flag = 'Y';
    CLOSE v_cur;
END;
/
```

**Expected behavior:** The cursor is constrained to the PRODUCT row structure.

**Why it works:** Strong typing shifts shape validation toward compile time.

**Operational caution:** Do not use weak cursors simply to avoid defining stable API contracts.

## Enhanced Deep Dive 50 — Package Initialization Section

A package body can include an initialization section that runs once when the package is first referenced in a database session.

```text
session
  ↓ first package use
package initialization
  ↓
package routines
```

```sql
CREATE OR REPLACE PACKAGE BODY pkg_demo AS
    g_loaded_at TIMESTAMP;

    PROCEDURE show_state IS
    BEGIN
        DBMS_OUTPUT.PUT_LINE(g_loaded_at);
    END;
BEGIN
    g_loaded_at := SYSTIMESTAMP;
END pkg_demo;
/
```

**Expected behavior:** The timestamp is set on first use for that session.

**Why it works:** Package initialization establishes session package state.

**Operational caution:** Connection pools can reuse sessions, so initialization is not the same as 'once per web request'.

## Enhanced Deep Dive 51 — Package State and Connection Pools

Package globals persist for the lifetime of a database session. In a pooled application, request B can inherit package state left by request A if the same DB session is reused.

```text
request A
  ↓ pooled session #7
package state = X

request B
  ↓ same session #7
sees X unless reset
```

```sql
-- Prefer passing request data as parameters:
BEGIN
    pkg_order_api.create_order(
        p_customer_id => :customer_id,
        p_order_id    => :order_id
    );
END;
/
```

**Expected behavior:** Stateless APIs avoid cross-request state leakage.

**Why it works:** Connection pooling changes the lifecycle assumptions of database sessions.

**Operational caution:** Avoid package globals for user/session business context unless initialization/reset rules are explicit and tested.

## Enhanced Deep Dive 52 — SERIALLY_REUSABLE Package Awareness

Oracle provides `SERIALLY_REUSABLE` packages for specialized cases where package state should be released between server calls. This can reduce UGA/state retention but changes semantics and is not a default best practice.

```text
call
 ↓ package state allocated
return
 ↓ state released/reusable
```

```sql
-- Conceptual declaration:
CREATE OR REPLACE PACKAGE pkg_temp
IS
    PRAGMA SERIALLY_REUSABLE;
    ...
END;
/
```

**Expected behavior:** State does not behave like ordinary session-persistent package state.

**Why it works:** The pragma changes package-state lifetime.

**Operational caution:** Use only when you understand server-call boundaries and package restrictions in your release.

## Enhanced Deep Dive 53 — Package Overloading

Packages can expose multiple procedures/functions with the same name when parameter signatures differ sufficiently. This can create a clean API, but excessive overloads make calls ambiguous.

```text
API name
  ├→ version(number)
  └→ version(varchar2)
```

```sql
CREATE OR REPLACE PACKAGE pkg_format AS
    FUNCTION display_value(p_value NUMBER)
        RETURN VARCHAR2;

    FUNCTION display_value(p_value DATE)
        RETURN VARCHAR2;
END pkg_format;
/
```

**Expected behavior:** Call resolution depends on the parameter datatype.

**Why it works:** Overloading groups conceptually identical operations under one API name.

**Operational caution:** Do not create overloads whose implicit-conversion rules make calls ambiguous.

## Enhanced Deep Dive 54 — Private Package Helpers

Only declarations in the package specification are public. Subprograms declared only in the body are private implementation details.

```text
Package Spec
  public API
      ↓
Package Body
  public implementations
  private helpers
```

```sql
CREATE OR REPLACE PACKAGE BODY pkg_order_api AS
    PROCEDURE validate_customer(
        p_customer_id IN NUMBER
    ) IS
    BEGIN
        ...
    END;

    -- public procedures follow
END pkg_order_api;
/
```

**Expected behavior:** Callers cannot directly invoke the private helper.

**Why it works:** Encapsulation allows internal implementation changes without changing the public contract.

**Operational caution:** Do not expose every helper in the specification merely for testing convenience.

## Enhanced Deep Dive 55 — Exception Propagation

An exception propagates outward until a matching handler is found. A local handler that cannot fully recover should usually re-raise so the caller knows the operation failed.

```text
inner block error
   ↓ no adequate recovery
RAISE
   ↓
outer block / application
```

```sql
BEGIN
    pkg_order_api.create_order(...);
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        -- add context if useful
        RAISE;
END;
/
```

**Expected behavior:** The original error remains visible to higher layers.

**Why it works:** Error propagation preserves failure semantics.

**Operational caution:** Do not convert every exception to a generic success code; this makes transactional failures invisible.

## Enhanced Deep Dive 56 — Error Stack, Backtrace, and Call Stack

For deeper diagnostics, Oracle exposes formatted error stack/backtrace/call-stack information. This is more useful than only printing `SQLERRM`, because it can preserve where an exception originated.

```text
deep procedure error
  ↓
call stack
  ↓
backtrace line
  ↓
top-level handler
```

```sql
BEGIN
    pkg_order_api.create_order(...);
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(
            DBMS_UTILITY.FORMAT_ERROR_STACK
        );
        DBMS_OUTPUT.PUT_LINE(
            DBMS_UTILITY.FORMAT_ERROR_BACKTRACE
        );
        RAISE;
END;
/
```

**Expected behavior:** Diagnostics include more context than a single error message.

**Why it works:** Backtrace data helps identify the original failing PL/SQL line.

**Operational caution:** Production logging should route diagnostics to a controlled logging/observability system rather than only DBMS_OUTPUT.

## Enhanced Deep Dive 57 — RAISE vs RAISE_APPLICATION_ERROR

`RAISE` rethrows a current or named exception. `RAISE_APPLICATION_ERROR` creates an application-specific Oracle error number/message for API consumers.

```text
internal exception
  ├→ RAISE preserve/propagate
business validation
  └→ RAISE_APPLICATION_ERROR custom contract
```

```sql
IF p_quantity <= 0 THEN
    RAISE_APPLICATION_ERROR(
        -20001,
        'Quantity must be greater than zero'
    );
END IF;
```

**Expected behavior:** The caller receives a specific application error.

**Why it works:** Business validation failures deserve explicit, stable API messages.

**Operational caution:** Do not expose secrets or raw internal SQL in application error messages.

## Enhanced Deep Dive 58 — Native Dynamic SQL with Bind Variables

`EXECUTE IMMEDIATE` should keep values bound separately from SQL text. This improves injection safety and cursor reuse.

```text
SQL structure
  ↓ fixed string
bind values
  ↓ USING
execution
```

```sql
DECLARE
    v_sql VARCHAR2(1000);
    v_count NUMBER;
BEGIN
    v_sql :=
        'SELECT COUNT(*) ' ||
        'FROM orders ' ||
        'WHERE customer_id = :x';

    EXECUTE IMMEDIATE v_sql
        INTO v_count
        USING :customer_id;
END;
/
```

**Expected behavior:** The value never becomes SQL syntax.

**Why it works:** Bind placeholders are parsed as data parameters.

**Operational caution:** Binding cannot replace arbitrary table/column names; identifiers need allowlisting/validation.

## Enhanced Deep Dive 59 — DBMS_ASSERT for Identifier Validation

When dynamic SQL genuinely needs identifiers, Oracle's `DBMS_ASSERT` package provides validation utilities that can reduce injection risk. It should complement, not replace, an application allowlist.

```text
untrusted identifier
  ↓ allowlist
  ↓ DBMS_ASSERT
  ↓ concatenate validated identifier
```

```sql
DECLARE
    v_table VARCHAR2(128);
    v_sql   VARCHAR2(1000);
BEGIN
    v_table := DBMS_ASSERT.SIMPLE_SQL_NAME(
        :requested_table
    );

    v_sql := 'SELECT COUNT(*) FROM ' || v_table;
END;
/
```

**Expected behavior:** Invalid identifier syntax is rejected rather than blindly inserted into SQL.

**Why it works:** Identifier validation narrows the attack surface of necessary dynamic SQL.

**Operational caution:** A syntactically valid table name may still be unauthorized; enforce a business allowlist too.

## Enhanced Deep Dive 60 — DBMS_SQL Awareness

`DBMS_SQL` provides lower-level dynamic SQL capabilities useful when column count/types are unknown until runtime. It is more complex than `EXECUTE IMMEDIATE` and should be reserved for truly dynamic metadata-driven cases.

```text
unknown query shape
   ↓ parse with DBMS_SQL
describe columns
   ↓ define/fetch dynamically
```

```sql
-- Conceptual flow:
-- DBMS_SQL.OPEN_CURSOR
-- DBMS_SQL.PARSE
-- DBMS_SQL.DESCRIBE_COLUMNS...
-- DBMS_SQL.DEFINE_COLUMN
-- DBMS_SQL.EXECUTE
-- DBMS_SQL.COLUMN_VALUE
-- DBMS_SQL.CLOSE_CURSOR
```

**Expected behavior:** The caller can handle a result set whose structure is discovered at runtime.

**Why it works:** The package exposes a procedural dynamic-cursor API.

**Operational caution:** Use `EXECUTE IMMEDIATE` for normal dynamic SQL because it is simpler and safer to maintain.

## Enhanced Deep Dive 61 — Definer Rights Need Direct Privileges

Definer-rights stored code generally relies on privileges granted directly to the owner rather than privileges available only through roles. This is a common reason a statement works interactively but fails to compile inside a stored procedure.

```text
interactive session
role → SELECT works

stored definer-rights code
direct grant required
      ↓
compile/runtime resolution
```

```sql
-- As object owner:
GRANT SELECT ON other_schema.product
TO api_owner;

-- Then compile api_owner procedure/package.
```

**Expected behavior:** Direct object privilege allows the stored object to resolve the reference.

**Why it works:** Stored-code security intentionally avoids blindly inheriting all enabled role privileges.

**Operational caution:** Do not grant broad privileges merely to make compilation succeed; grant the exact object/system privilege needed.

## Enhanced Deep Dive 62 — Invoker Rights with AUTHID CURRENT_USER

Invoker-rights code evaluates object access using the caller's rights context. It is useful for reusable utilities that should not elevate callers to the owner's object privileges.

```text
caller A privileges
   ↓
same invoker-rights code
   ↓
A access

caller B privileges
   ↓
same code
   ↓
B access
```

```sql
CREATE OR REPLACE PROCEDURE show_my_tables
AUTHID CURRENT_USER
IS
BEGIN
    FOR r IN (
        SELECT table_name
        FROM user_tables
    ) LOOP
        DBMS_OUTPUT.PUT_LINE(r.table_name);
    END LOOP;
END;
/
```

**Expected behavior:** Different callers see behavior aligned with their own schema/rights context.

**Why it works:** Invoker rights make the caller the effective privilege context for many operations.

**Operational caution:** Choose definer vs invoker rights as an API security design decision, not as a compilation workaround.

## Enhanced Deep Dive 63 — Synonyms Do Not Grant Privileges

A synonym resolves a name but does not authorize access. This distinction is critical when troubleshooting ORA-00942 or designing cross-schema APIs.

```text
synonym name
   ↓
target object

separate:
GRANT privilege
```

```sql
CREATE SYNONYM product_master
FOR manufacturing.product;

-- privilege is separate:
GRANT SELECT
ON manufacturing.product
TO report_user;
```

**Expected behavior:** The synonym becomes usable only when the session also has required access.

**Why it works:** Name resolution and authorization are separate database layers.

**Operational caution:** Public synonyms increase namespace coupling; use cautiously.

## Enhanced Deep Dive 64 — Row vs Statement Trigger Cost

A row trigger fires once for every affected row, while a statement trigger fires once for the DML statement. A bulk UPDATE affecting 100,000 rows can therefore invoke a row trigger 100,000 times.

```text
UPDATE 100000 rows
   ├→ statement trigger: 1
   └→ row trigger: 100000
```

```sql
CREATE OR REPLACE TRIGGER trg_orders_stmt
AFTER UPDATE ON orders
BEGIN
    DBMS_OUTPUT.PUT_LINE('Statement finished');
END;
/
```

**Expected behavior:** One trigger invocation occurs for the statement.

**Why it works:** Trigger granularity changes both semantics and performance.

**Operational caution:** Do not place expensive network calls or large queries in row triggers.

## Enhanced Deep Dive 65 — Compound Trigger State

Compound triggers combine statement- and row-level timing sections and can share state across one DML statement. They are useful for batching audit rows or avoiding certain mutating-table patterns.

```text
BEFORE STATEMENT
  ↓ initialize collection
BEFORE EACH ROW
  ↓ collect
AFTER EACH ROW
  ↓ collect
AFTER STATEMENT
  ↓ bulk process
```

```sql
CREATE OR REPLACE TRIGGER trg_product_ct
FOR UPDATE OF unit_price ON product
COMPOUND TRIGGER

    TYPE t_ids IS TABLE OF NUMBER;
    g_ids t_ids := t_ids();

    AFTER EACH ROW IS
    BEGIN
        g_ids.EXTEND;
        g_ids(g_ids.LAST) := :NEW.product_id;
    END AFTER EACH ROW;

    AFTER STATEMENT IS
    BEGIN
        DBMS_OUTPUT.PUT_LINE(
            'Changed rows=' || g_ids.COUNT
        );
    END AFTER STATEMENT;

END;
/
```

**Expected behavior:** Row IDs are accumulated and processed after the statement.

**Why it works:** Shared trigger state is scoped to one triggering statement.

**Operational caution:** Do not use compound triggers to hide an entire business workflow inside database side effects.

## Enhanced Deep Dive 66 — Mutating-table Error as a Data-consistency Signal

Oracle prevents unsafe row-trigger queries against the table currently being modified because the table is in a transitional state. The right fix is usually architectural: set-based SQL, statement-level processing, or a compound trigger.

```text
row DML
  ↓ row trigger
  ↓ queries same table
  X unstable statement state
```

```sql
-- Avoid this pattern in a row trigger:
-- SELECT COUNT(*)
-- FROM product
-- WHERE ...;
```

**Expected behavior:** Oracle can raise a mutating-table error rather than expose an inconsistent intermediate view.

**Why it works:** The restriction protects statement-level consistency.

**Operational caution:** Do not bypass the error with autonomous transactions or other hacks that create even less consistent behavior.

## Enhanced Deep Dive 67 — Pipelined Table Functions

A pipelined table function can produce rows incrementally to SQL. It is useful for specialized transformations that are difficult to express in ordinary SQL, but it adds procedural complexity.

```text
PL/SQL producer
  ↓ PIPE ROW
SQL consumer
  ↓ rows arrive incrementally
```

```sql
-- Conceptual:
-- CREATE TYPE ...
-- CREATE FUNCTION transform(...)
-- RETURN table_type PIPELINED
-- IS
-- BEGIN
--   PIPE ROW(...);
-- END;
```

**Expected behavior:** SQL can query the function as a row source when the required SQL types are defined.

**Why it works:** Pipelining can stream transformed rows without materializing the whole result in PL/SQL first.

**Operational caution:** Prefer normal SQL/views when they solve the problem; pipelined functions complicate deployment, typing, and optimization.

## Enhanced Deep Dive 68 — DETERMINISTIC Is a Promise

Marking a function `DETERMINISTIC` tells Oracle that the same inputs always produce the same output. Oracle does not magically verify your business logic. Mislabeling a function can lead to incorrect indexed/optimized behavior.

```text
same inputs
  ↓
must always produce
same output
```

```sql
CREATE OR REPLACE FUNCTION calc_total(
    p_qty NUMBER,
    p_price NUMBER
)
RETURN NUMBER
DETERMINISTIC
IS
BEGIN
    RETURN p_qty * p_price;
END;
/
```

**Expected behavior:** This pure arithmetic function is a good deterministic example.

**Why it works:** Determinism enables certain optimization/indexing use cases.

**Operational caution:** Do not mark functions deterministic if they read changing tables, current time, session state, or nondeterministic sources.

## Enhanced Deep Dive 69 — Function Result Cache Awareness

Oracle supports PL/SQL function result caching for suitable deterministic-like workloads. It can reduce repeated computation but introduces cache invalidation and memory behavior that must be understood.

```text
same function inputs
  ↓
result cache
  ├→ hit
  └→ compute + store
```

```sql
-- Conceptual syntax:
-- FUNCTION f(...) RETURN ... RESULT_CACHE
-- IS
-- BEGIN
--   ...
-- END;
```

**Expected behavior:** Repeated calls may reuse a cached result when cache rules permit.

**Why it works:** Caching exchanges memory and invalidation complexity for reduced repeated work.

**Operational caution:** Do not cache functions whose results depend on rapidly changing or session-specific state without understanding invalidation semantics.

## Enhanced Deep Dive 70 — DBMS_APPLICATION_INFO Instrumentation

Packages can identify module/action names so DBAs can correlate sessions and SQL with application operations. This is a strong bridge between PL/SQL development and DBA performance troubleshooting.

```text
web request
  ↓ set MODULE/ACTION
DB session
  ↓
V$SESSION / observability
  ↓
performance diagnosis
```

```sql
BEGIN
    DBMS_APPLICATION_INFO.SET_MODULE(
        module_name => 'ORDER_API',
        action_name => 'CREATE_ORDER'
    );
END;
/
```

**Expected behavior:** The session can expose application context to monitoring tools.

**Why it works:** Good instrumentation makes database activity attributable.

**Operational caution:** Clear/reset or update action names as operations change; stale module metadata can mislead troubleshooting.

## Enhanced Deep Dive 71 — DBMS_OUTPUT Is Not Production Logging

`DBMS_OUTPUT` is a client-buffered debugging aid. It depends on the client enabling output and is not a durable, centralized, queryable operational log.

```text
PL/SQL
  ↓ DBMS_OUTPUT buffer
client chooses to fetch/display
```

```sql
SET SERVEROUTPUT ON

BEGIN
    DBMS_OUTPUT.PUT_LINE('Debug message');
END;
/
```

**Expected behavior:** The message appears only in supporting clients with output enabled.

**Why it works:** DBMS_OUTPUT is excellent for learning and interactive diagnosis.

**Operational caution:** Production logging needs retention, severity, correlation IDs, security controls, and centralized observability.

## Enhanced Deep Dive 72 — Application Error Logging Without Breaking Transactions

Logging an error inside the same transaction is rolled back if the business transaction rolls back. An autonomous logger can preserve a log independently, but that choice must be deliberate because it creates a separate commit boundary.

```text
business tx
  ↓ fails
same-tx log → rollback too

autonomous logger
  ↓ independent commit
  ↓ survives
```

```sql
-- Design decision:
-- business error context can be returned to application
-- application/central logger may persist it outside DB transaction
```

**Expected behavior:** The architecture explicitly decides whether logs must survive transaction rollback.

**Why it works:** Error observability is a separate concern from business atomicity.

**Operational caution:** Do not add autonomous transactions everywhere; they can create hidden committed state and deadlocks if they touch business rows.

## Enhanced Deep Dive 73 — Source Code in USER_SOURCE

Oracle stores source text for PL/SQL objects in dictionary views such as `USER_SOURCE`. This is useful for inspection, but source-of-truth should still live in version control.

```text
Git migration files
  ↓ deploy
database USER_SOURCE
  ↓ runtime copy
```

```sql
SELECT
    name,
    type,
    line,
    text
FROM user_source
WHERE name = 'PKG_ORDER_API'
ORDER BY type, line;
```

**Expected behavior:** The deployed package text can be inspected line by line.

**Why it works:** The database retains compiled-source metadata for schema objects.

**Operational caution:** Do not treat the database as the only source repository; use version-controlled migrations and review.

## Enhanced Deep Dive 74 — Dependency Invalidation

Changing a referenced object can invalidate dependent PL/SQL. This is normal dependency management, not necessarily corruption.

```text
TABLE/VIEW change
   ↓
dependent package
   ↓ INVALID
recompile on use or explicit compile
```

```sql
SELECT
    name,
    type,
    referenced_name,
    referenced_type
FROM user_dependencies
WHERE name = 'PKG_ORDER_API';
```

**Expected behavior:** The query maps direct dependencies.

**Why it works:** Oracle tracks object dependencies so changes can trigger recompilation.

**Operational caution:** Deployment pipelines should check invalid objects after schema changes and verify compilation errors.

## Enhanced Deep Dive 75 — Edition-based Redefinition Awareness

Oracle provides edition-based mechanisms for advanced online application upgrades in supported environments. The important foundation is that schema object versioning and deployment can be designed to reduce application downtime.

```text
old app → old edition
new app → new edition
          ↓ controlled cutover
```

```sql
-- Conceptual only:
-- editions, editioning views, crossedition triggers
-- are advanced deployment tools.
```

**Expected behavior:** Multiple application object versions can coexist during controlled transitions in appropriate designs.

**Why it works:** The feature separates application upgrade timing from one instant schema replacement.

**Operational caution:** This is an advanced operational feature; learn exact eligibility, object types, and deployment procedure before production use.

## Enhanced Deep Dive 76 — Unit Testing PL/SQL

Stored code deserves automated tests just like application code. Tests should cover normal paths, boundary values, exceptions, rollback behavior, privileges, and concurrency-sensitive cases.

```text
test data setup
  ↓
call package API
  ↓
assert result
  ↓
ROLLBACK/cleanup
```

```sql
DECLARE
    v_total NUMBER;
BEGIN
    v_total := pkg_order_api.get_order_total(1001);

    IF v_total < 0 THEN
        RAISE_APPLICATION_ERROR(
            -20999,
            'Test failed: negative total'
        );
    END IF;
END;
/
```

**Expected behavior:** The test fails loudly when an invariant is violated.

**Why it works:** Database code is executable software and benefits from repeatable tests.

**Operational caution:** Do not let tests commit uncontrolled data into shared environments.

## Enhanced Deep Dive 77 — Transaction Ownership in Package APIs

A package should define whether it owns the transaction or participates in the caller's transaction. In most reusable business APIs, allowing the caller to commit several package calls atomically provides better composability.

```text
caller
  ↓ create_order
  ↓ add_lines
  ↓ reserve_inventory
  ↓ COMMIT once
```

```sql
BEGIN
    pkg_order_api.create_order(...);
    pkg_order_api.add_order_item(...);
    pkg_inventory.reserve(...);

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/
```

**Expected behavior:** All related operations commit or roll back together.

**Why it works:** A single transaction boundary preserves cross-package atomicity.

**Operational caution:** Hidden COMMITs inside helper procedures make rollback impossible for the caller.

## Enhanced Deep Dive 78 — Package API vs Direct Table Grants

A definer-rights package can provide a narrow business API while the application user has no direct DML privileges on underlying tables.

```text
APPUSER
  EXECUTE only
     ↓
PKG_ORDER_API
  validates rules
     ↓
ORDERS / ORDER_ITEM
```

```sql
GRANT EXECUTE
ON pkg_order_api
TO appuser;

-- Do not grant broad UPDATE/DELETE on base tables
-- unless the application truly needs them.
```

**Expected behavior:** The application performs only operations exposed by the package API.

**Why it works:** Stored code becomes an authorization and validation boundary.

**Operational caution:** Package code must be reviewed like security-sensitive application code; dynamic SQL and definer rights can amplify mistakes.

## Enhanced Deep Dive 79 — SQL Execution Plans for Developers

PL/SQL developers should understand basic plans because slow stored code is often slow SQL. The most important first skill is mapping query predicates/joins to access paths and row estimates.

```text
SQL in procedure
   ↓
optimizer
   ↓
plan
   ↓
table/index access
```

```sql
EXPLAIN PLAN FOR
SELECT *
FROM orders
WHERE customer_id = 100;

SELECT *
FROM TABLE(DBMS_XPLAN.DISPLAY);
```

**Expected behavior:** The plan shows how Oracle intends to access the data.

**Why it works:** The database spends most application time executing SQL, not PL/SQL control flow.

**Operational caution:** For real executed SQL, runtime cursor plans can be more representative than EXPLAIN PLAN; detailed tuning continues in DBA II.

## Enhanced Deep Dive 80 — Bind Peeking and Plan Sensitivity Awareness

The optimizer may consider bind values when initially selecting a plan, and different data distributions can make one plan poor for another value. Modern Oracle has adaptive cursor-sharing mechanisms, but developers should understand why 'same SQL, different parameter, different runtime' can occur.

```text
bind :status
ACTIVE = 99%
CLOSED = 1%
   ↓
selectivity differs
   ↓
ideal plans may differ
```

```sql
SELECT *
FROM orders
WHERE status = :status;
```

**Expected behavior:** Runtime can vary dramatically if values have very different selectivity.

**Why it works:** Data distribution is part of query performance.

**Operational caution:** Do not hardcode literals merely to force a plan; investigate statistics, indexes, and plan behavior with DBA tooling.

## Enhanced Deep Dive 81 — Bitmap Index Awareness

Bitmap indexes can be effective for low-cardinality analytical dimensions with low concurrent DML, but they can create severe locking/concurrency problems in OLTP workloads.

```text
low-cardinality column
status: A/B/C
   ↓
bitmap representation
   ↓
fast analytical combinations
```

```sql
CREATE BITMAP INDEX bix_quality_class
ON quality_inspection(classification);
```

**Expected behavior:** Analytical filters can benefit in an appropriate warehouse-like workload.

**Why it works:** Bitmap structures optimize different access patterns from normal B-tree indexes.

**Operational caution:** Do not use bitmap indexes on heavily updated OLTP tables without understanding their locking behavior.

## Enhanced Deep Dive 82 — Materialized View Refresh Semantics

Refresh can be complete or incremental/fast when prerequisites are satisfied. Refresh mode determines load, staleness, logging, and operational complexity.

```text
base DML
   ↓
refresh strategy
   ├→ COMPLETE recompute
   └→ FAST changes if eligible
      ↓
materialized summary
```

```sql
BEGIN
    DBMS_MVIEW.REFRESH(
        list   => 'MV_MONTHLY_SALES',
        method => 'C'
    );
END;
/
```

**Expected behavior:** The materialized view is recomputed using complete refresh.

**Why it works:** Refresh is a data pipeline with its own schedule and failure modes.

**Operational caution:** Monitor refresh success and freshness; a stale materialized view can produce confidently wrong reports.

## Enhanced Deep Dive 83 — SQL Plan Stability Is an Operational Concern

A query that is fast today can change plan after statistics, schema, or version changes. Developers should record critical query shapes and expected performance, while DBAs manage deeper plan-stability tools.

```text
same SQL
  + changed stats/index/version
  ↓
new plan
  ↓
new runtime
```

```sql
-- Capture SQL text and representative plan during release testing.
SELECT *
FROM TABLE(DBMS_XPLAN.DISPLAY);
```

**Expected behavior:** A release artifact can include expected access patterns for critical queries.

**Why it works:** Performance depends on data and optimizer state, not only SQL text.

**Operational caution:** Do not lock in a bad plan permanently; plan stability is not a substitute for correct design.

## Enhanced Deep Dive 84 — SQL and PL/SQL Secure Coding Checklist

Database code should validate business inputs, bind data values, restrict dynamic identifiers, minimize definer-rights power, avoid secret logging, and expose only required package APIs.

```text
Input
 ↓ validate
 ↓ bind
Package API
 ↓ least privilege
Tables
 ↓ audit/monitor
```

```sql
-- Parameter validation example:
IF p_order_id IS NULL THEN
    RAISE_APPLICATION_ERROR(
        -20010,
        'Order ID is required'
    );
END IF;
```

**Expected behavior:** Invalid inputs fail before dangerous or ambiguous database work begins.

**Why it works:** Security is built into code structure and privilege design.

**Operational caution:** Never concatenate passwords, tokens, user-provided predicates, or arbitrary object names into dynamic SQL.

## Enhanced Deep Dive 85 — Scalar vs Set-based Thinking

When a requirement can be expressed as one relational operation, prefer one SQL statement over procedural loops. Set-based SQL lets the optimizer choose efficient join, filter, aggregation, and parallel execution strategies.

```text
rows → relational operation → result
```

```sql
UPDATE product SET active_flag='N' WHERE discontinued_date < DATE '2025-01-01';
```

## Enhanced Deep Dive 86 — Implicit Cursor Attributes

`SQL%ROWCOUNT`, `SQL%FOUND`, and `SQL%NOTFOUND` expose the result of the most recent implicit SQL statement in PL/SQL. They are useful for asserting expected DML impact.

```text
DML → implicit cursor state → PL/SQL decision
```

```sql
UPDATE orders SET status='CLOSED' WHERE order_id=:id;
DBMS_OUTPUT.PUT_LINE(SQL%ROWCOUNT);
```

## Enhanced Deep Dive 87 — Explicit Cursor Parameter Contracts

Parameterized cursors make query dependencies explicit and reusable. The parameter should represent query criteria, not become a hidden global.

```text
cursor definition + parameter → result set
```

```sql
CURSOR c_orders(p_customer_id NUMBER) IS SELECT order_id FROM orders WHERE customer_id=p_customer_id;
```

## Enhanced Deep Dive 88 — Cursor FOR Loop Lifecycle

A cursor FOR loop automatically opens, fetches, and closes the cursor. It is safer than manual lifecycle code when row-by-row processing is genuinely needed.

```text
FOR record IN cursor → automatic open/fetch/close
```

```sql
FOR r IN (SELECT order_id FROM orders) LOOP DBMS_OUTPUT.PUT_LINE(r.order_id); END LOOP;
```

## Enhanced Deep Dive 89 — Exception Handler Ordering

Specific exception handlers should appear before `WHEN OTHERS`. The general handler is the final safety net, not the primary branch for expected business errors.

```text
specific exception → handle; otherwise → OTHERS → log/re-raise
```

```sql
EXCEPTION WHEN NO_DATA_FOUND THEN ... WHEN DUP_VAL_ON_INDEX THEN ... WHEN OTHERS THEN RAISE;
```

## Enhanced Deep Dive 90 — PRAGMA EXCEPTION_INIT

A named PL/SQL exception can be associated with a specific Oracle error number so code can handle a known database error without comparing message strings.

```text
ORA code → named exception → handler
```

```sql
PRAGMA EXCEPTION_INIT(e_busy, -54);
```

## Enhanced Deep Dive 91 — Autonomous Transaction Boundaries

An autonomous transaction commits or rolls back independently of the caller. It is appropriate only when independent persistence is a real requirement, commonly carefully designed logging.

```text
main tx || autonomous tx → separate commits
```

```sql
PRAGMA AUTONOMOUS_TRANSACTION;
```

## Enhanced Deep Dive 92 — FORALL Rowcount

`SQL%BULK_ROWCOUNT` reports DML impact per FORALL iteration and helps reconcile batch operations.

```text
FORALL iteration → rowcount[i]
```

```sql
DBMS_OUTPUT.PUT_LINE(SQL%BULK_ROWCOUNT(i));
```

## Enhanced Deep Dive 93 — Record Collections

Collections of records can represent batches of strongly structured rows in memory and pair naturally with bulk fetch patterns.

```text
cursor rows → collection of records
```

```sql
TYPE t_rows IS TABLE OF c_orders%ROWTYPE;
```

## Enhanced Deep Dive 94 — Nested Tables in SQL Awareness

Schema-level nested-table types can cross the SQL/PLSQL boundary, but they add object-relational complexity. Use them only where array-like SQL parameters truly improve the API.

```text
client/list → SQL collection type → TABLE()
```

```sql
SELECT * FROM TABLE(:collection_value);
```

## Enhanced Deep Dive 95 — VARRAY Semantics

A VARRAY has an explicit maximum size and preserves element order. It is useful for small bounded lists, not unbounded transactional relationships.

```text
bounded ordered array
```

```sql
TYPE t_codes IS VARRAY(10) OF VARCHAR2(30);
```

## Enhanced Deep Dive 96 — DBMS_OUTPUT Buffering

DBMS_OUTPUT stores output for the client to fetch later; it is not a streaming terminal write. Large debug output can therefore consume session/client buffers.

```text
PL/SQL → buffer → client fetch
```

```sql
SET SERVEROUTPUT ON SIZE UNLIMITED
```

## Enhanced Deep Dive 97 — DBMS_APPLICATION_INFO Client Identifier

Session instrumentation can include client identifiers so connection-pooled sessions remain attributable to end users or requests.

```text
request ID → CLIENT_IDENTIFIER → V$SESSION
```

```sql
DBMS_SESSION.SET_IDENTIFIER(:request_id);
```

## Enhanced Deep Dive 98 — Application Context Awareness

Oracle application contexts can hold trusted session attributes used by security or application logic. Values should be set only through controlled trusted code.

```text
trusted package → context namespace → SYS_CONTEXT
```

```sql
SELECT SYS_CONTEXT('APP_CTX','TENANT_ID') FROM dual;
```

## Enhanced Deep Dive 99 — Fine-grained Access Control Awareness

Oracle supports policy-driven row filtering technologies. The foundation concept is that database authorization can include row-level policy, not only object-level GRANTs.

```text
query → policy predicate → filtered rows
```

```sql
-- Advanced security topic; design with DBA/security team.
```

## Enhanced Deep Dive 100 — Synonym Resolution Troubleshooting

When an unqualified name fails, inspect current schema, private synonym, public synonym, target existence, and target privilege separately.

```text
name → private synonym → public synonym → target + grant
```

```sql
SELECT synonym_name, table_owner, table_name FROM user_synonyms;
```

## Enhanced Deep Dive 101 — Editioning View Awareness

Editioning views provide a stable logical table interface during advanced edition-based application upgrades. They separate application-facing columns from base-table evolution.

```text
application → editioning view → evolving base table
```

```sql
-- Advanced deployment pattern.
```

## Enhanced Deep Dive 102 — DBMS_METADATA Awareness

DBMS_METADATA can extract Oracle DDL for schema objects, useful for inspection and migration tooling.

```text
dictionary metadata → generated DDL
```

```sql
SELECT DBMS_METADATA.GET_DDL('TABLE','PRODUCT') FROM dual;
```

## Enhanced Deep Dive 103 — Source-control Migration Discipline

Database DDL and PL/SQL should be deployed from reviewed version-controlled migration scripts with deterministic ordering and rollback/forward-fix planning.

```text
Git → CI checks → migration → validation
```

```sql
-- Store CREATE OR REPLACE package/table migration scripts in source control.
```

## Enhanced Deep Dive 104 — Compile Warnings

PL/SQL compiler warnings can reveal unreachable code, performance issues, or questionable constructs. Teams should enable and review appropriate warning levels.

```text
source → compiler → errors + warnings
```

```sql
ALTER SESSION SET PLSQL_WARNINGS='ENABLE:ALL';
```

## Enhanced Deep Dive 105 — PLSQL_OPTIMIZE_LEVEL Awareness

PL/SQL optimization level affects compiler transformations. Do not change it casually to solve application logic errors; correctness must not depend on optimization quirks.

```text
source → compiler optimization → executable code
```

```sql
SHOW PARAMETER plsql_optimize_level
```

## Enhanced Deep Dive 106 — Native Compilation Awareness

Oracle can compile PL/SQL using native compilation mechanisms in supported configurations. Treat this as a measured performance option, not a default coding technique.

```text
PL/SQL source → compilation mode → executable
```

```sql
SHOW PARAMETER plsql_code_type
```

## Enhanced Deep Dive 107 — Deterministic Test Data

Database tests should create known rows, run the unit under test, assert results, then roll back or clean up. Repeatability matters more than manually inspecting one successful run.

```text
setup → execute → assert → rollback
```

```sql
SAVEPOINT test_start; ... ROLLBACK TO test_start;
```

## Enhanced Deep Dive 108 — API Versioning

Changing a package specification can invalidate callers. Stable public signatures and additive versioning reduce deployment coupling.

```text
package spec v1 → callers; breaking change → coordinated release
```

```sql
-- Prefer additive overload/new routine before removing old API.
```

## Enhanced Deep Dive 109 — PL/SQL Naming Conventions

Prefixing local variables and parameters consistently can reduce accidental column/variable ambiguity in SQL embedded inside PL/SQL.

```text
p_ parameter; v_ local; c_ constant; g_ package global
```

```sql
PROCEDURE p(p_order_id IN orders.order_id%TYPE)
```

## Enhanced Deep Dive 110 — SQL Identifier Ambiguity

Inside PL/SQL, a parameter can accidentally have the same name as a column. Explicit table aliases and naming conventions prevent subtle predicates such as `WHERE order_id = order_id`.

```text
parameter name ≈ column name → ambiguity
```

```sql
WHERE o.order_id = p_order_id
```

## Enhanced Deep Dive 111 — MERGE Delete Clause Awareness

Oracle MERGE can support additional matched-row logic in supported syntax, but every branch should be treated as a potentially destructive synchronization rule and tested with source duplicates.

```text
source match → update / conditional delete
```

```sql
-- Use only with explicit business rule and lab verification.
```

## Enhanced Deep Dive 112 — Data Type Anchoring Across Package APIs

Using table-column `%TYPE` in package parameters keeps API types aligned with schema columns, but a column change can still invalidate the package and downstream callers.

```text
column type → %TYPE → package compile dependency
```

```sql
p_customer_id IN customer.customer_id%TYPE
```

## Enhanced Deep Dive 113 — NOCOPY Hint Awareness

`NOCOPY` can reduce copying of large OUT/IN OUT parameters but is a hint with semantic caveats if exceptions occur. Use only after measurement.

```text
large parameter → possible by-reference semantics
```

```sql
p_data IN OUT NOCOPY t_large_collection
```

## Enhanced Deep Dive 114 — OUT Parameter Initialization

OUT parameters should be set on every successful code path. Otherwise callers can receive NULL or stale assumptions.

```text
procedure paths → assign output → return
```

```sql
p_order_id := NULL; -- initialize explicitly when contract benefits
```

## Enhanced Deep Dive 115 — BOOLEAN in PL/SQL APIs

PL/SQL BOOLEAN is convenient inside PL/SQL but interoperability with SQL/client APIs depends on Oracle release and client capabilities. Public database APIs should consider cross-language compatibility.

```text
PL/SQL boolean ↔ client compatibility boundary
```

```sql
v_valid BOOLEAN := TRUE;
```

## Enhanced Deep Dive 116 — Package Constants

Package constants centralize stable domain values such as status codes, but database tables or configuration are better for values business administrators must change without code deployment.

```text
compile-time constant vs configurable data
```

```sql
c_status_new CONSTANT VARCHAR2(10) := 'NEW';
```

## Enhanced Deep Dive 117 — Trigger Recursion Awareness

A trigger that causes DML which fires related triggers can create recursive side effects. Map the entire trigger chain before deployment.

```text
DML → trigger A → DML B → trigger B → ...
```

```sql
SELECT trigger_name, triggering_event FROM user_triggers;
```

## Enhanced Deep Dive 118 — Trigger Enable/Disable State

A trigger can exist but be disabled. Deployment checks should validate STATUS, not only object existence.

```text
trigger object → enabled? → runtime effect
```

```sql
SELECT trigger_name, status FROM user_triggers;
```

## Enhanced Deep Dive 119 — Invalid Object Deployment Gate

A deployment should fail if expected application objects remain INVALID after compilation. Otherwise errors surface later during user traffic.

```text
deploy → compile → invalid-object check → release gate
```

```sql
SELECT object_name, object_type FROM user_objects WHERE status='INVALID';
```

## Enhanced Deep Dive 120 — PL/SQL Dependency on Grants

Revoking a direct object privilege can invalidate or break stored code that depends on it. Security changes therefore require application dependency review.

```text
REVOKE → dependency impact → compile/runtime failure
```

```sql
SELECT * FROM user_dependencies WHERE referenced_owner='OTHER_SCHEMA';
```

## Enhanced Deep Dive 121 — Transaction Retry Semantics

Application retry after deadlock/serialization/conflict must be safe. Stored procedures should avoid irreversible external side effects before commit.

```text
attempt → transient failure → rollback → retry
```

```sql
-- Keep external email/file/API side effects outside retryable DB transaction when possible.
```

## Enhanced Deep Dive 122 — Idempotent Stored APIs

An idempotent API can safely be retried without creating duplicate business effects. This is valuable with network timeouts where the caller may not know whether the first attempt committed.

```text
request key → unique constraint → repeat request returns same outcome
```

```sql
CREATE UNIQUE INDEX uk_order_request ON orders(request_id);
```

## Enhanced Deep Dive 123 — Unique Request Keys

A caller-supplied request identifier plus a UNIQUE constraint can prevent duplicate order creation during retries.

```text
client request_id → INSERT → uniqueness guards duplicates
```

```sql
INSERT INTO orders(request_id,...) VALUES(:request_id,...);
```

## Enhanced Deep Dive 124 — Savepoints in Complex APIs

Savepoints can support partial rollback inside a larger transaction, but overuse makes transaction flow hard to reason about.

```text
transaction → savepoint → optional work → rollback-to → continue
```

```sql
SAVEPOINT optional_step; ... ROLLBACK TO optional_step;
```

## Enhanced Deep Dive 125 — Database API Error Contract

Applications should map known Oracle/application errors to stable business error codes/messages rather than parsing arbitrary SQLERRM text.

```text
ORA/custom code → API error mapping → user/service response
```

```sql
RAISE_APPLICATION_ERROR(-20020,'INVALID_STATUS_TRANSITION');
```

## Enhanced Deep Dive 126 — Schema Inventory Queries

Automated inventory of tables, views, packages, triggers, sequences, and invalid objects makes database deployments observable.

```text
USER_* views → inventory report
```

```sql
SELECT object_type, COUNT(*) FROM user_objects GROUP BY object_type;
```

## Enhanced Deep Dive 127 — DDL Extraction and Drift

Comparing source-controlled DDL with `DBMS_METADATA` output can reveal environment drift, though generated DDL may include storage/environment clauses that require normalization.

```text
desired DDL ↔ deployed DDL → drift report
```

```sql
SELECT DBMS_METADATA.GET_DDL('VIEW','V_ORDER_SUMMARY') FROM dual;
```

## Enhanced Deep Dive 128 — Production Safety for Dynamic DDL

Dynamic DDL changes metadata and often introduces implicit commit boundaries. Restrict it to administrative deployment tools rather than user-facing request paths.

```text
request path X dynamic DDL; migration pipeline ✓
```

```sql
EXECUTE IMMEDIATE 'CREATE TABLE ...'; -- admin tooling only
```

## Enhanced Deep Dive 129 — SQLcl Scripting Discipline

SQLcl/SQL*Plus scripts should set failure behavior so CI/CD stops on errors rather than continuing with a half-deployed schema.

```text
script error → fail pipeline
```

```sql
WHENEVER SQLERROR EXIT SQL.SQLCODE
```

## Enhanced Deep Dive 130 — Spooling Deployment Evidence

Spooling captures deployment output for audit/troubleshooting, including compiler errors and validation queries.

```text
deployment → spool log → retained evidence
```

```sql
SPOOL deploy.log
... SQL ...
SPOOL OFF
```

## Enhanced Deep Dive 131 — Substitution vs Bind Variables

SQL*Plus substitution variables are text replacement; bind variables are typed runtime values. Confusing them can create quoting or injection problems in scripts.

```text
&name → textual substitution; :name → bind
```

```sql
VARIABLE v_id NUMBER
EXEC :v_id := 10;
```

## Enhanced Deep Dive 132 — SQLcl Script Parameters

Script parameters can make deployment reusable, but validate environment names and never pass secrets in plain command history.

```text
script env parameter → validated schema/service target
```

```sql
-- Use approved secret handling and environment validation.
```

## Enhanced Deep Dive 133 — Explain Before Rewrite

When a query is slow, capture the exact SQL, plan, row estimates, and representative bind values before changing it. Rewriting syntax without evidence can make performance worse.

```text
slow SQL → evidence → hypothesis → one change → remeasure
```

```sql
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

## Enhanced Deep Dive 134 — Top-N per Group

Top-N per group is naturally expressed with analytic ranking, not procedural loops.

```text
partition by group → rank → filter rank
```

```sql
SELECT * FROM (SELECT p.*, ROW_NUMBER() OVER(PARTITION BY category_id ORDER BY sales DESC) rn FROM product_sales p) WHERE rn<=5;
```

## Enhanced Deep Dive 135 — Latest Row per Business Key

Use `ROW_NUMBER()` with deterministic ordering to select the latest record per entity.

```text
entity rows → order newest first → rn=1
```

```sql
ROW_NUMBER() OVER(PARTITION BY machine_id ORDER BY event_time DESC, event_id DESC)
```

## Enhanced Deep Dive 136 — Gaps and Islands Awareness

Analytic functions can identify consecutive ranges such as machine downtime streaks. This is a powerful reporting pattern worth learning before resorting to procedural loops.

```text
events → LAG difference → group marker → islands
```

```sql
-- Use LAG plus cumulative SUM to assign group identifiers.
```

## Enhanced Deep Dive 137 — Conditional Aggregation

CASE inside aggregates is often simpler and more portable than PIVOT for a small known set of measures.

```text
rows → SUM(CASE...) → multiple metrics
```

```sql
SUM(CASE WHEN status='GOOD' THEN quantity ELSE 0 END) AS good_qty
```

## Enhanced Deep Dive 138 — Anti-duplication with ROW_NUMBER

When staging data contains duplicate business keys, analytic row numbering can identify which rows are duplicates before MERGE. Do not silently delete them without a business rule.

```text
partition by business key → rn>1 duplicates
```

```sql
ROW_NUMBER() OVER(PARTITION BY product_code ORDER BY loaded_at DESC)
```

# Enhanced Hands-on Lab Sequence

## Enhanced Lab 1 — Session NLS Baseline

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 2 — ANSI Temporal Literals

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 3 — Empty String vs NULL

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 4 — EXISTS vs JOIN

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 5 — NOT EXISTS vs NOT IN

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 6 — WITH Clause Refactor

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 7 — Recursive CTE Organization Chart

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 8 — CONNECT BY Cycle Detection

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 9 — Analytic Frames

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 10 — FIRST_VALUE/LAST_VALUE

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 11 — NTILE Quartiles

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 12 — LISTAGG

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 13 — GROUPING Metadata

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 14 — Deterministic Pagination

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 15 — Keyset Pagination

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 16 — DML RETURNING

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 17 — Multi-table INSERT

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 18 — MERGE Duplicate-source Guard

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 19 — Sequence Gap Demonstration

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 20 — Identity Policy

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 21 — Virtual Column

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 22 — Function-based Index

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 23 — Materialized View Refresh

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 24 — Deferrable Constraint

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 25 — Constraint State Inspection

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 26 — Read Consistency Two Sessions

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 27 — FOR UPDATE

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 28 — SKIP LOCKED Worker Queue

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 29 — DDL Commit Boundary

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 30 — PL/SQL Compile Lifecycle

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 31 — Custom Record

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 32 — Sparse Associative Array

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 33 — Bulk Collect LIMIT

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 34 — FORALL SAVE EXCEPTIONS

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 35 — SQL%BULK_EXCEPTIONS

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 36 — Strong REF CURSOR

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 37 — Package Initialization

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 38 — Package State with Connection Pool Simulation

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 39 — Package Overloading

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 40 — Private Helpers

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 41 — Error Backtrace

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 42 — DBMS_ASSERT Dynamic Identifier

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 43 — Definer-rights Direct Grant

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 44 — Invoker-rights Utility

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 45 — Trigger Firing Count

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 46 — Compound Trigger Batch

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 47 — Mutating-table Redesign

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 48 — DBMS_APPLICATION_INFO

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 49 — Source and Dependencies

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 50 — Compile Warnings

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 51 — Package API Transaction Ownership

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 52 — Idempotent Request Key

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 53 — SQL Plan Review

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 54 — Bind-sensitive Data Distribution

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 55 — Bitmap Index Design Review

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 56 — Materialized-view Freshness

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 57 — SQLcl Fail-fast Deployment

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 58 — Schema Drift Inventory

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 59 — Top-N per Group

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 60 — Latest Event per Machine

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 61 — Gaps-and-Islands Downtime

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 62 — Secure Dynamic Reporting API

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```

## Enhanced Lab 63 — Integrated PL/SQL Package Test Suite

Build this in a disposable Oracle schema. Before running the final SQL/PLSQL, write the expected result and the failure mode you are testing.

Required evidence:

```text
1. SQL/PLSQL used
2. Expected result
3. Actual result
4. Dictionary/plan/error evidence
5. Why Oracle behaved that way
6. Security or transaction implication
7. Cleanup / rollback
```


## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Oracle Client Environment

1. Install or access Oracle AI Database Free / approved Oracle lab.
2. Connect using SQL Developer or SQLcl.
3. Display current user.
4. inspect current schema.
5. run `SELECT SYSDATE FROM dual`.
6. run `DESC` on a table.
7. create `ORACLE_SQL_BASELINE.md`.

### Lab 2 — Build Core Schema

Create:

```text
CUSTOMER
PRODUCT
DEPARTMENT
EMPLOYEE
ORDERS
ORDER_ITEM
```

Requirements:

1. Oracle data types.
2. named primary keys.
3. named unique constraints.
4. foreign keys.
5. CHECK constraints.
6. identity/sequence-generated IDs.
7. default timestamps.
8. inspect using `USER_*` dictionary views.

### Lab 3 — Oracle Functions

Write queries using:

```text
UPPER
LOWER
SUBSTR
INSTR
TRIM
ROUND
TRUNC
SYSDATE
SYSTIMESTAMP
ADD_MONTHS
MONTHS_BETWEEN
TO_CHAR
TO_DATE
```

Explain each result and its datatype.

### Lab 4 — NULL and Conditional Logic

Use:

```text
NVL
NVL2
COALESCE
NULLIF
CASE
DECODE
```

Create a quality-status report using `CASE`.

### Lab 5 — Aggregation

Build:

1. sales per customer.
2. order count by status.
3. average employee salary by department.
4. `HAVING` report.
5. `ROLLUP`.
6. `CUBE`.
7. `GROUPING SETS`.

Explain subtotal/grand-total rows.

### Lab 6 — JOINs

Write:

1. Customer → Orders.
2. Orders → OrderItem → Product.
3. customers without orders.
4. employee-manager self join.
5. full outer reconciliation query.
6. controlled CROSS JOIN.
7. one accidental Cartesian result and correction.

### Lab 7 — Subqueries and Sets

Write:

1. scalar subquery.
2. `IN`.
3. correlated department salary query.
4. `EXISTS`.
5. `NOT EXISTS`.
6. `UNION`.
7. `UNION ALL`.
8. `INTERSECT`.
9. `MINUS`.

Explain `NOT IN` + NULL risk.

### Lab 8 — Analytic Functions

Create:

1. `ROW_NUMBER` top employee per department.
2. `RANK`.
3. `DENSE_RANK`.
4. `LAG` previous production.
5. `LEAD` next production.
6. running sales total.
7. department average attached to every employee row.

Compare analytic results with `GROUP BY`.

### Lab 9 — Hierarchical and Pivot Queries

1. create employee hierarchy.
2. use `START WITH`.
3. use `CONNECT BY PRIOR`.
4. display `LEVEL`.
5. create production status dataset.
6. pivot GOOD/REJECT columns.
7. unpivot a small report.

### Lab 10 — DML and Transactions

1. insert an order.
2. update a product.
3. use `SAVEPOINT`.
4. intentionally make a wrong update.
5. `ROLLBACK TO` savepoint.
6. commit final correct transaction.
7. demonstrate why DDL should not be mixed casually with uncommitted business work.

### Lab 11 — MERGE

1. create `PRODUCT_STAGE`.
2. insert existing and new products.
3. `MERGE` into PRODUCT.
4. verify UPDATE path.
5. verify INSERT path.
6. create a bad duplicate source scenario.
7. explain why source uniqueness matters.

### Lab 12 — Sequences, Identity, Views, Synonyms

1. create explicit sequence.
2. use `NEXTVAL`.
3. inspect `CURRVAL`.
4. create identity table.
5. create reporting view.
6. create `WITH CHECK OPTION` view.
7. create private synonym.
8. prove synonym does not grant privilege itself.

### Lab 13 — PL/SQL Blocks

1. anonymous block.
2. variables.
3. constants.
4. `%TYPE`.
5. `%ROWTYPE`.
6. `SELECT INTO`.
7. IF/ELSIF.
8. CASE.
9. loops.
10. DBMS_OUTPUT.

### Lab 14 — Cursors

1. implicit cursor + `SQL%ROWCOUNT`.
2. explicit cursor.
3. open/fetch/close.
4. cursor attributes.
5. cursor FOR loop.
6. parameterized cursor.
7. rewrite one cursor task as set-based SQL and compare complexity.

### Lab 15 — Exceptions

1. trigger `NO_DATA_FOUND`.
2. trigger `TOO_MANY_ROWS`.
3. handle `DUP_VAL_ON_INDEX`.
4. create user-defined exception.
5. use `RAISE_APPLICATION_ERROR`.
6. test `SQLCODE`/`SQLERRM`.
7. demonstrate why `WHEN OTHERS THEN NULL` is dangerous.

### Lab 16 — Procedures and Functions

Create:

```text
get_customer_sales
validate_quantity
calculate_reject_rate
```

Use:

```text
IN
OUT
defaults
named notation
```

Test from SQLcl/SQL Developer.

### Lab 17 — Package API

Create:

```text
PKG_ORDER_API
```

Specification:

```text
create_order
add_order_item
get_order_total
change_order_status
```

Body:

- validate customer.
- validate product.
- use sequences/identity.
- raise business errors.
- do not hide transaction ownership with arbitrary commits.

### Lab 18 — Triggers

1. product-price audit trigger.
2. inspect `:OLD`/`:NEW`.
3. create statement-level audit test.
4. compare row vs statement firing count.
5. design an `INSTEAD OF` trigger concept.
6. reproduce or study mutating-table problem safely.
7. explain when trigger logic should be moved elsewhere.

### Lab 19 — Collections and Bulk Processing

1. associative array.
2. record.
3. `BULK COLLECT`.
4. inspect collection `.COUNT`.
5. `FORALL` update.
6. compare row loop and bulk pattern.
7. use `LIMIT` for batch fetching.
8. document memory tradeoff.

### Lab 20 — Dynamic SQL and Injection Defense

1. execute static dynamic query.
2. use bind variable with `EXECUTE IMMEDIATE`.
3. demonstrate unsafe concatenation only with harmless local input.
4. rewrite safely.
5. create an allowlist for a dynamic object identifier.
6. explain why values and object names require different handling.

### Lab 21 — Security and Rights

1. create lab application user.
2. create package owner/API schema concept.
3. grant only EXECUTE on selected package.
4. compare direct-table access vs package API.
5. create a small `AUTHID CURRENT_USER` example.
6. explain definer vs invoker rights.
7. verify using `USER_TAB_PRIVS`/accessible dictionary information.

### Lab 22 — Debugging Challenge

Inject:

1. missing object.
2. invalid identifier.
3. unique violation.
4. no-data-found.
5. too-many-rows.
6. invalid procedure.
7. broken dependency.
8. bad dynamic SQL.
9. unhandled exception.
10. inefficient row-by-row loop.

For each:

```text
Error
Expected behavior
Evidence
Root cause
Fix
Verification
```

---

## 6. Mini Project

# Mini Project — Oracle Manufacturing Reporting and Order API

Build an Oracle schema that supports both analytical reporting and controlled transactional PL/SQL APIs.

## Architecture

```text
                    Application
                        |
                 EXECUTE Package API
                        |
                        v
                +----------------+
                | PKG_ORDER_API  |
                +----------------+
                  |            |
                  v            v
               ORDERS      ORDER_ITEM
                  |
                  v
               CUSTOMER

Reporting User
      |
      v
Reporting Views
      |
      +--> Sales
      +--> Production
      +--> Quality
```

## Required Tables

```text
CUSTOMER
PRODUCT
DEPARTMENT
EMPLOYEE
ORDERS
ORDER_ITEM
MACHINE
PRODUCTION_RUN
QUALITY_INSPECTION
DEFECT
INSPECTION_DEFECT
PRODUCT_PRICE_AUDIT
```

## Schema Requirements

Use:

- named PK constraints.
- named FK constraints.
- named UNIQUE constraints.
- CHECK constraints.
- identity columns and/or sequences.
- Oracle `NUMBER`, `VARCHAR2`, `DATE`, `TIMESTAMP`.
- appropriate indexes.

## SQL Reporting Requirements

Create at least:

```text
10 joins
5 grouped reports
2 ROLLUP/CUBE/GROUPING SETS reports
5 subquery reports
3 set-operator reports
6 analytic-function reports
1 hierarchical query
1 PIVOT report
```

Required business reports:

```text
sales by customer
monthly sales
top 5 products per month
employee salary ranking by department
month-over-month production using LAG
running production output
quality reject rate
defect ranking
expected-vs-actual reconciliation using MINUS/FULL OUTER JOIN
employee hierarchy
```

## Views

Create:

```text
V_ORDER_SUMMARY
V_PRODUCT_PERFORMANCE
V_QUALITY_SUMMARY
```

At least one should be read-only.

Document when `WITH CHECK OPTION` is useful.

## Package API

Create:

```text
PKG_ORDER_API
```

Public API:

```text
CREATE_ORDER
ADD_ORDER_ITEM
GET_ORDER_TOTAL
CHANGE_ORDER_STATUS
CANCEL_ORDER
```

Design:

```text
Caller
  ↓
Package
  ↓
validation
  ↓
SQL
  ↓
exceptions
  ↓
return result
```

Do not allow arbitrary dynamic SQL through the package.

## Exception Requirements

Create custom business errors for:

```text
customer not found
product not found
quantity <= 0
invalid status transition
insufficient inventory
```

Use meaningful `RAISE_APPLICATION_ERROR` messages.

## Transaction Requirement

The application/caller should be able to treat:

```text
create order
+
add lines
+
reserve inventory
```

as one atomic unit.

Document who owns `COMMIT`.

## Trigger Requirement

Create a focused audit trigger for product price changes.

Do **not** put the entire order-processing workflow in triggers.

## Bulk Requirement

Build one procedure for processing a batch of production records using:

```text
BULK COLLECT
FORALL
```

Compare conceptually with row-by-row processing.

## Dynamic SQL Requirement

Create one controlled reporting procedure where dynamic behavior is genuinely needed.

Requirements:

```text
bind data values
allowlist identifiers
no direct user text concatenation into SQL structure
```

## Security

Design roles/users:

```text
MANUFACTURING_OWNER
APPUSER
REPORTUSER
```

Conceptual privilege model:

```text
APPUSER
   |
EXECUTE package
   |
no broad direct table DML

REPORTUSER
   |
SELECT on reporting views
```

## Dictionary/Metadata Report

Create:

```text
SCHEMA_INVENTORY.sql
```

Report:

- tables.
- columns.
- constraints.
- indexes.
- views.
- sequences.
- procedures.
- functions.
- packages.
- triggers.
- invalid objects.

## Project Files

```text
README.md
SCHEMA.sql
SEED.sql
QUERIES.sql
ANALYTICS.sql
VIEWS.sql
SEQUENCES.sql
PACKAGE_SPEC.sql
PACKAGE_BODY.sql
TRIGGERS.sql
BULK_PROCESSING.sql
SECURITY.sql
SCHEMA_INVENTORY.sql
TEST_CASES.sql
TROUBLESHOOTING.md
```

## Failure Tests

Test and document:

```text
duplicate product code
invalid customer FK
NO_DATA_FOUND
TOO_MANY_ROWS
invalid order status
package compile error
broken dependency
dynamic SQL validation failure
unauthorized direct table access
bulk-operation partial failure design
```

For each:

```text
Symptom
Oracle error
Business meaning
Root cause
Correction
Verification
```

---


# Expanded Capstone — Oracle Manufacturing SQL/PLSQL Service Layer

Build a production-style schema and stored-code API:

```text
Backend / Batch / BI
        |
        +-----------------------------+
        |                             |
     APPUSER                      REPORTUSER
        |                             |
   EXECUTE only                 SELECT views
        |                             |
        v                             v
+------------------+           +------------------+
| PKG_ORDER_API    |           | Reporting Views  |
| PKG_INVENTORY    |           | Analytics        |
| PKG_QUALITY      |           | Materialized MV  |
+------------------+           +------------------+
        |
        v
CUSTOMER / PRODUCT / ORDERS / ORDER_ITEM
MACHINE / PRODUCTION_RUN / QUALITY / INVENTORY
```

## Required SQL Engineering

Implement:

```text
normal joins
anti-joins with NOT EXISTS
subquery factoring
recursive hierarchy
CONNECT BY path report
ROLLUP/GROUPING
window functions
top-N per group
running totals
LAG/LEAD
PIVOT or conditional aggregation
deterministic pagination
keyset pagination
MERGE with source validation
DML RETURNING
```

For every complex query provide:

```text
business question
row/cardinality prediction
SQL
expected result
execution-plan screenshot/text or DBMS_XPLAN output
index assumptions
edge cases
NULL behavior
```

## Stored API

Create:

```text
PKG_ORDER_API
  CREATE_ORDER
  ADD_ORDER_ITEM
  CHANGE_STATUS
  CANCEL_ORDER
  GET_ORDER_TOTAL

PKG_INVENTORY
  RESERVE
  RELEASE
  MOVE_STOCK

PKG_QUALITY
  CLOSE_INSPECTION
  GET_REJECT_RATE
```

Rules:

```text
no hidden COMMIT in reusable helpers
caller owns multi-package transaction
business validation raises stable application errors
definer-rights owner has direct least-privilege grants
APPUSER has EXECUTE, not broad base-table DML
dynamic values use binds
dynamic identifiers use allowlist + DBMS_ASSERT
```

## Concurrency

Demonstrate:

```text
read consistency
SELECT FOR UPDATE
NOWAIT
SKIP LOCKED worker pattern
idempotent request key
transaction retry design
```

## Bulk Processing

Build a batch loader using:

```text
BULK COLLECT ... LIMIT
FORALL
SAVE EXCEPTIONS
SQL%BULK_EXCEPTIONS
SQL%BULK_ROWCOUNT
```

Document which failures allow partial success and which must roll back the whole business transaction.

## Trigger Policy

Only focused triggers are allowed:

```text
price audit
statement-level deployment/audit example
compound trigger batching example
```

Do not implement core order workflow inside triggers.

## Instrumentation

Set:

```text
MODULE
ACTION
CLIENT_IDENTIFIER
```

for major package operations.

Create an error model that captures:

```text
business error code
Oracle error
module/action
request ID
order ID where safe
error backtrace
```

Do not log passwords, secrets, payment data, or raw sensitive payloads.

## Deployment

Create:

```text
001_schema.sql
002_constraints.sql
003_indexes.sql
004_views.sql
005_package_specs.sql
006_package_bodies.sql
007_triggers.sql
008_grants.sql
009_tests.sql
010_validation.sql
```

Deployment script must use fail-fast behavior and produce a spool log.

Validation checks:

```text
invalid objects
expected object counts
constraint status/validated state
trigger status
package compilation
grants
representative SQL tests
```

## Project Files

```text
README.md
ERD.md
SCHEMA.sql
ANALYTICS.sql
CONCURRENCY.sql
PACKAGE_SPECS.sql
PACKAGE_BODIES.sql
BULK_PROCESSING.sql
TRIGGERS.sql
SECURITY.sql
DEPLOY.sql
VALIDATE.sql
TESTS.sql
SCHEMA_INVENTORY.sql
TROUBLESHOOTING.md
```


## 7. Recommended Resources

Prioritize official Oracle documentation for the version used in your lab:

- Oracle AI Database SQL Language Reference
- Oracle AI Database PL/SQL Language Reference
- SQL Language Quick Reference
- Oracle Database Development documentation
- Oracle Database Error Messages documentation
- Oracle Database Security Guide for stored-code privilege design
- Oracle Database Performance documentation when studying SQL execution/performance
- SQL Developer and SQLcl documentation

Useful local discovery:

```sql
DESC object_name
```

SQLcl / SQL*Plus:

```sql
SHOW ERRORS
```

Dictionary:

```sql
SELECT * FROM user_objects;
SELECT * FROM user_errors;
SELECT * FROM user_dependencies;
```

---

## 8. Certification Relevance

This course provides core skills for:

```text
Oracle SQL Developer
PL/SQL Developer
Oracle DBA
Backend Engineer
Database Engineer
Data Engineer
Enterprise Application Developer
```

It prepares directly for:

```text
30. Oracle Database Administration I
31. Oracle Database Administration II
```

The key transferable concepts are:

```text
Oracle SQL syntax
query design
analytic functions
transactions
schema objects
Oracle metadata
procedural database APIs
exception handling
packages
bulk processing
security boundaries
```

---

## 9. Common Mistakes & Best Practices

- **Mistake:** Treating Oracle exactly like MySQL.  
  **Best practice:** Learn Oracle schemas, data types, date semantics, sequences, dictionary views, and PL/SQL explicitly.

- **Mistake:** Relying on implicit date conversions.  
  **Best practice:** Use ANSI date literals or explicit `TO_DATE` format models.

- **Mistake:** Using quoted mixed-case object names unnecessarily.  
  **Best practice:** Prefer conventional unquoted Oracle identifiers.

- **Mistake:** Using `NOT IN` without considering NULLs.  
  **Best practice:** Prefer `NOT EXISTS` when anti-join semantics are intended.

- **Mistake:** Using GROUP BY when an analytic function should preserve detail rows.  
  **Best practice:** Decide whether rows should collapse or remain visible.

- **Mistake:** Treating sequence values as gapless legal numbering.  
  **Best practice:** Use sequences for uniqueness, not gapless guarantees.

- **Mistake:** Removing constraints because test data fails.  
  **Best practice:** Fix data/business logic if the constraint is valid.

- **Mistake:** Writing row-by-row PL/SQL for work one SQL statement can perform.  
  **Best practice:** Prefer set-based SQL.

- **Mistake:** `WHEN OTHERS THEN NULL`.  
  **Best practice:** Handle expected exceptions specifically and re-raise unexpected errors.

- **Mistake:** Committing inside every stored procedure.  
  **Best practice:** Define transaction ownership clearly.

- **Mistake:** Putting all application logic in triggers.  
  **Best practice:** Keep triggers small, explicit, and documented.

- **Mistake:** Concatenating user input into dynamic SQL.  
  **Best practice:** Use bind variables and identifier allowlists.

- **Mistake:** `BULK COLLECT` an unlimited huge dataset.  
  **Best practice:** Use batching/`LIMIT` when memory matters.

- **Mistake:** Giving users `DBA_*` access because a tutorial uses those views.  
  **Best practice:** Start with `USER_*`/`ALL_*` and least privilege.

- **Mistake:** Ignoring package state with connection pools.  
  **Best practice:** Prefer stateless package APIs unless state is intentional.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. SQL vs PL/SQL?

**Short answer:** SQL is a declarative language for data/object operations; PL/SQL adds procedural programming around SQL.

### Q2. What does `DUAL` traditionally provide?

**Short answer:** A one-row Oracle table commonly used for evaluating expressions/functions.

### Q3. What Oracle datatype is normally used for variable-length character data?

**Short answer:** `VARCHAR2`.

### Q4. Does Oracle `DATE` contain time components?

**Short answer:** Yes, down to seconds.

### Q5. Why use explicit `TO_DATE` or ANSI date literals?

**Short answer:** To avoid NLS-dependent implicit conversion ambiguity.

### Q6. What does `NVL` do?

**Short answer:** Replaces NULL with another expression/value.

### Q7. `WHERE` vs `HAVING`?

**Short answer:** WHERE filters rows before grouping; HAVING filters groups after aggregation.

### Q8. What does `ROLLUP` provide?

**Short answer:** Hierarchical subtotal levels plus a grand-total level for grouped dimensions.

### Q9. What is a FULL OUTER JOIN useful for?

**Short answer:** Reconciliation where unmatched rows from either side must remain visible.

### Q10. Why can `NOT IN` be dangerous with NULL?

**Short answer:** NULL can make comparisons UNKNOWN and produce surprising anti-join results.

### Q11. `UNION` vs `UNION ALL`?

**Short answer:** UNION removes duplicates; UNION ALL keeps them.

### Q12. What does `MINUS` do?

**Short answer:** Returns rows in the first query result that are absent from the second.

### Q13. Why are analytic functions different from GROUP BY?

**Short answer:** They calculate across row windows while preserving individual detail rows.

### Q14. `ROW_NUMBER` vs `RANK`?

**Short answer:** ROW_NUMBER always produces unique sequential numbers; RANK gives ties the same rank and leaves gaps afterward.

### Q15. What does `LAG` do?

**Short answer:** Returns a value from a preceding row in an analytic ordering.

### Q16. What does `CONNECT BY` support?

**Short answer:** Oracle hierarchical query traversal.

### Q17. What is `MERGE`?

**Short answer:** A statement that conditionally updates matched rows and inserts unmatched rows from a source.

### Q18. Why is `TRUNCATE` different from `DELETE`?

**Short answer:** TRUNCATE is DDL-style whole-table removal with different transaction/operational semantics; DELETE is row-oriented DML.

### Q19. What does `NEXTVAL` do?

**Short answer:** Advances a sequence and returns its next value.

### Q20. Are sequences gapless?

**Short answer:** No.

### Q21. What does a synonym do?

**Short answer:** Provides an alternate name for another object; it does not itself grant privilege.

### Q22. What is a function-based index?

**Short answer:** An index on an expression such as `UPPER(email)`.

### Q23. `USER_*` vs `ALL_*` vs `DBA_*`?

**Short answer:** USER views describe current user's objects, ALL views accessible objects, DBA views database-wide administrative metadata.

### Q24. What are the three main PL/SQL block sections?

**Short answer:** Declaration, executable section, and exception section.

### Q25. What does `%TYPE` do?

**Short answer:** Anchors a PL/SQL variable datatype to an existing column/variable datatype.

### Q26. What does `%ROWTYPE` do?

**Short answer:** Creates a record matching the row structure of a table/cursor.

### Q27. What happens when scalar `SELECT INTO` returns no rows?

**Short answer:** `NO_DATA_FOUND`.

### Q28. What happens when scalar `SELECT INTO` returns more than one row?

**Short answer:** `TOO_MANY_ROWS`.

### Q29. Why use cursor FOR loops?

**Short answer:** They automatically manage cursor open/fetch/close for procedural row processing.

### Q30. Why is `WHEN OTHERS THEN NULL` dangerous?

**Short answer:** It silently hides unexpected failures.

### Q31. What does `RAISE_APPLICATION_ERROR` do?

**Short answer:** Raises a custom application error to the caller.

### Q32. Procedure vs function?

**Short answer:** A procedure primarily performs an operation; a function returns a value.

### Q33. What is a package specification?

**Short answer:** The public interface of a PL/SQL package.

### Q34. What is `:OLD` in a row trigger?

**Short answer:** The column value before the triggering row change.

### Q35. What is `:NEW`?

**Short answer:** The new/current column value associated with the row operation.

### Q36. What is an `INSTEAD OF` trigger commonly used for?

**Short answer:** Defining DML behavior on certain complex views.

### Q37. What is a mutating-table problem?

**Short answer:** A row trigger attempts unsafe access to the table currently being modified.

### Q38. What is `EXECUTE IMMEDIATE`?

**Short answer:** PL/SQL native dynamic SQL execution.

### Q39. Why use bind variables in dynamic SQL?

**Short answer:** They separate data values from SQL structure, improving safety and cursor reuse.

### Q40. What does `BULK COLLECT` do?

**Short answer:** Fetches multiple rows into PL/SQL collections in a bulk operation.

### Q41. What does `FORALL` do?

**Short answer:** Executes bulk DML using collection elements with reduced SQL/PLSQL context switching.

### Q42. Definer rights vs invoker rights?

**Short answer:** Definer-rights code executes using the owner's stored privilege context; invoker-rights code uses the current caller's rights context.

### Q43. What does `SHOW ERRORS` help with?

**Short answer:** PL/SQL/schema-object compilation diagnostics in compatible Oracle client tools.

### Q44. Where can compilation errors be queried?

**Short answer:** `USER_ERRORS` for objects in the current schema.

### Q45. What should you try before converting a set-based SQL operation into a PL/SQL loop?

**Short answer:** Determine whether one SQL statement can perform the entire operation efficiently and clearly.

---

# Enhanced Self-Assessment Bank

### Q1. What is a hard parse?
**Answer:** A parse requiring semantic/optimization work instead of reusing a shareable existing cursor.

### Q2. Why use bind variables?
**Answer:** To keep data separate from SQL syntax, reduce injection risk, and improve cursor reuse.

### Q3. Does CURRENT_SCHEMA change privileges?
**Answer:** No; it changes unqualified name resolution, not authorization.

### Q4. Why avoid implicit date conversion?
**Answer:** Session NLS settings can change how text is interpreted.

### Q5. What is special about Oracle empty strings?
**Answer:** A zero-length character string is treated as NULL in normal SQL character semantics.

### Q6. What does EXISTS test?
**Answer:** Whether at least one matching row exists.

### Q7. Why is NOT EXISTS safer than NOT IN for anti-joins?
**Answer:** It avoids surprising UNKNOWN behavior when the inner result contains NULL.

### Q8. Does a WITH clause guarantee materialization?
**Answer:** No; it is primarily a query-factoring construct and the optimizer chooses execution.

### Q9. Why protect recursive queries from cycles?
**Answer:** Bad hierarchy data can loop or fail traversal.

### Q10. PARTITION BY vs ORDER BY in analytics?
**Answer:** Partition defines groups; order defines sequence inside each group.

### Q11. ROWS vs RANGE?
**Answer:** ROWS uses physical row positions; RANGE uses ordering-value peer semantics.

### Q12. Why can LAST_VALUE surprise you?
**Answer:** The default analytic frame may end at the current row.

### Q13. What does NTILE do?
**Answer:** Assigns ordered rows to a requested number of approximate buckets.

### Q14. What does LISTAGG do?
**Answer:** Aggregates multiple values into one ordered delimited string.

### Q15. Why use GROUPING?
**Answer:** To distinguish subtotal-generated NULLs from real data NULLs.

### Q16. Why deterministic ORDER BY for pagination?
**Answer:** Without a unique ordering, rows can move between pages.

### Q17. Keyset vs OFFSET pagination?
**Answer:** Keyset seeks from the last key; OFFSET skips earlier rows and can become expensive.

### Q18. What does DML RETURNING avoid?
**Answer:** A separate SELECT to fetch values Oracle already knows from the changed row.

### Q19. Why validate MERGE source uniqueness?
**Answer:** Multiple source rows for one target key can make synchronization invalid or ambiguous.

### Q20. Are sequence values gapless?
**Answer:** No.

### Q21. Why can identity columns help?
**Answer:** They make generated-key ownership explicit in the table definition.

### Q22. What is a virtual column?
**Answer:** A column whose value is derived from an expression over other data.

### Q23. What is a function-based index?
**Answer:** An index storing an expression result such as UPPER(email).

### Q24. What is a materialized view?
**Answer:** A physically stored query result refreshed according to a defined strategy.

### Q25. What is a deferrable constraint?
**Answer:** A constraint whose checking can be deferred to transaction commit when configured.

### Q26. Why inspect VALIDATED as well as STATUS?
**Answer:** A constraint can enforce new DML without proving all existing rows were validated.

### Q27. What is Oracle read consistency?
**Answer:** Queries can reconstruct an appropriate committed view using undo.

### Q28. What does SELECT FOR UPDATE do?
**Answer:** Locks selected rows for a transaction that intends to modify them.

### Q29. NOWAIT?
**Answer:** Return an error immediately instead of waiting for a lock.

### Q30. SKIP LOCKED?
**Answer:** Skip rows currently locked by other transactions.

### Q31. Why is DDL dangerous inside business transactions?
**Answer:** DDL introduces implicit transaction boundaries.

### Q32. What is PLS_INTEGER?
**Answer:** A PL/SQL integer type useful for procedural arithmetic/counters.

### Q33. Why use %TYPE?
**Answer:** To anchor a PL/SQL variable/parameter datatype to a database column or variable.

### Q34. Why use records?
**Answer:** To group related fields into one structured PL/SQL value.

### Q35. What is an associative array?
**Answer:** An in-memory PL/SQL key/value collection.

### Q36. Why BULK COLLECT LIMIT?
**Answer:** Reduce context switching while bounding PGA memory consumption.

### Q37. What does FORALL do?
**Answer:** Executes bulk DML from collection elements.

### Q38. What does SAVE EXCEPTIONS do?
**Answer:** Allows FORALL to continue after row-level errors and report them afterward.

### Q39. What is SQL%BULK_EXCEPTIONS?
**Answer:** Collection-like diagnostic information about failed FORALL iterations.

### Q40. What is a REF CURSOR?
**Answer:** A cursor variable that can return a query result set to a caller.

### Q41. Strong REF CURSOR?
**Answer:** A REF CURSOR constrained to a declared row type.

### Q42. When does package initialization run?
**Answer:** On first reference to the package in a database session.

### Q43. Why is package state risky with pools?
**Answer:** The same DB session can be reused by another application request.

### Q44. What is package overloading?
**Answer:** Multiple routines with the same name but distinguishable parameter signatures.

### Q45. Why use private package helpers?
**Answer:** To hide implementation details outside the public specification.

### Q46. What should an unexpected exception normally do?
**Answer:** Add safe context if useful and re-raise rather than silently succeed.

### Q47. Why use FORMAT_ERROR_BACKTRACE?
**Answer:** To identify the original PL/SQL line where an error arose.

### Q48. RAISE_APPLICATION_ERROR use?
**Answer:** Return a stable application-specific Oracle error to the caller.

### Q49. What is native dynamic SQL?
**Answer:** Runtime SQL executed with constructs such as EXECUTE IMMEDIATE.

### Q50. Why bind values in dynamic SQL?
**Answer:** To keep values out of SQL syntax and improve safety/reuse.

### Q51. Can bind variables replace table names?
**Answer:** Normally no.

### Q52. What does DBMS_ASSERT help with?
**Answer:** Validating dynamic SQL identifiers/strings, alongside an authorization allowlist.

### Q53. When use DBMS_SQL?
**Answer:** When SQL/result shape is truly dynamic and lower-level cursor control is required.

### Q54. Why direct grants for definer-rights code?
**Answer:** Role privileges generally do not satisfy stored-code object privilege dependencies.

### Q55. What does AUTHID CURRENT_USER do?
**Answer:** Makes stored code use invoker-rights semantics.

### Q56. Does a synonym grant access?
**Answer:** No.

### Q57. Row vs statement trigger?
**Answer:** Row trigger fires per affected row; statement trigger fires once per DML statement.

### Q58. Why compound triggers?
**Answer:** To combine timing sections and share state across one DML statement.

### Q59. What is a mutating-table problem?
**Answer:** Unsafe row-trigger access to the table currently being modified.

### Q60. What is a pipelined table function?
**Answer:** A function that produces rows incrementally to SQL.

### Q61. What does DETERMINISTIC promise?
**Answer:** Same inputs always produce the same output.

### Q62. Why instrument MODULE/ACTION?
**Answer:** To attribute sessions/SQL to application operations.

### Q63. Is DBMS_OUTPUT production logging?
**Answer:** No.

### Q64. What does USER_SOURCE contain?
**Answer:** Stored source text for objects in the current schema.

### Q65. What does USER_DEPENDENCIES show?
**Answer:** Dependencies between stored objects and referenced objects.

### Q66. Why check INVALID objects after deployment?
**Answer:** A deployment can succeed partially while stored code remains unusable.

### Q67. Why enable compiler warnings?
**Answer:** To surface suspicious or suboptimal PL/SQL constructs.

### Q68. Who should own a package transaction?
**Answer:** The API contract must be explicit; reusable helpers usually participate in caller-owned transactions.

### Q69. What is an idempotent API?
**Answer:** One that can be retried without duplicating business effects.

### Q70. Why use a unique request ID?
**Answer:** To prevent duplicate operations after retries/timeouts.

### Q71. What is a savepoint?
**Answer:** A named point for partial rollback inside a transaction.

### Q72. Why stable business error codes?
**Answer:** Applications should not parse arbitrary Oracle message text.

### Q73. What does DBMS_METADATA do?
**Answer:** Extracts metadata/DDL representations for Oracle objects.

### Q74. Why version-control database code?
**Answer:** To review, reproduce, test, and audit schema/program deployments.

### Q75. What does WHENEVER SQLERROR EXIT do?
**Answer:** Makes SQL*Plus/SQLcl deployment scripts fail instead of continuing after SQL errors.

### Q76. Bind vs substitution variable?
**Answer:** Bind is typed runtime data; substitution is client-side text replacement.

### Q77. What is top-N per group?
**Answer:** Rank rows inside each group and filter to the first N.

### Q78. How select latest row per entity?
**Answer:** ROW_NUMBER partitioned by entity with deterministic newest-first ordering, then rn=1.

### Q79. What are gaps and islands?
**Answer:** SQL patterns for identifying consecutive sequences/ranges.

### Q80. Why conditional aggregation?
**Answer:** It creates multiple measures from one grouped scan using CASE.

### Q81. Why can bitmap indexes be poor for OLTP?
**Answer:** Their locking/update characteristics can hurt concurrent DML.

### Q82. What is query plan sensitivity?
**Answer:** Different data/statistics/binds can make different plans appropriate.

### Q83. What does DBMS_XPLAN display?
**Answer:** Oracle SQL execution-plan information.

### Q84. Why not hardcode literals to fix a plan?
**Answer:** It sacrifices cursor reuse/security and does not solve the underlying selectivity/statistics issue.

### Q85. What is result-cache risk?
**Answer:** Cached results can be wrong for logic that is session-specific or improperly modeled.

### Q86. What is NOCOPY?
**Answer:** A PL/SQL hint that can reduce copying for large OUT/IN OUT values with semantic caveats.

### Q87. Why avoid parameter names matching columns?
**Answer:** It can create ambiguous or accidentally tautological SQL predicates.

### Q88. What is SQL%BULK_ROWCOUNT?
**Answer:** Per-iteration row counts from FORALL DML.

### Q89. Why can autonomous logging be dangerous?
**Answer:** It creates an independent commit boundary and can persist state even when business work rolls back.

### Q90. What is an editioning view?
**Answer:** An application-facing view used in advanced edition-based online upgrade designs.

### Q91. Why materialized-view freshness matters?
**Answer:** Stored summaries can be stale even when queries are fast.

### Q92. What is a database API security boundary?
**Answer:** A package/view/privilege design that exposes only approved operations and data.

### Q93. What is the safest first choice for business data processing?
**Answer:** One clear set-based SQL statement when it correctly expresses the requirement.


## Completion Checklist

- [ ] I can connect to Oracle using SQL Developer/SQLcl-style tools.
- [ ] I understand Oracle user/schema naming.
- [ ] I can use Oracle numeric, character, date, timestamp, and LOB data types.
- [ ] I can write filters, functions, conversions, and CASE expressions.
- [ ] I can write joins, subqueries, and set operations.
- [ ] I can use ROLLUP, CUBE, and GROUPING SETS.
- [ ] I can use analytic functions including ROW_NUMBER, RANK, LAG, LEAD, and running totals.
- [ ] I can build hierarchical and pivot queries.
- [ ] I can use INSERT, UPDATE, DELETE, and MERGE safely.
- [ ] I understand Oracle transaction boundaries, COMMIT, ROLLBACK, and SAVEPOINT.
- [ ] I can create constraints, sequences, identity columns, views, synonyms, and indexes.
- [ ] I can use USER/ALL dictionary views.
- [ ] I can write PL/SQL anonymous blocks.
- [ ] I can use `%TYPE`, `%ROWTYPE`, variables, conditions, and loops.
- [ ] I can work with implicit/explicit cursors.
- [ ] I can handle predefined and custom exceptions.
- [ ] I can create procedures and functions.
- [ ] I can design package specifications and bodies.
- [ ] I understand trigger timing, `:OLD`, `:NEW`, and mutating-table risk.
- [ ] I can use records and collections.
- [ ] I can write safe dynamic SQL using bind variables.
- [ ] I understand `BULK COLLECT` and `FORALL`.
- [ ] I understand SQL/PLSQL context-switching cost.
- [ ] I understand definer vs invoker rights.
- [ ] I can diagnose invalid/failed PL/SQL using `SHOW ERRORS`, `USER_ERRORS`, and dependencies.
- [ ] I completed all 22 labs.
- [ ] I completed the Oracle Manufacturing Reporting and Order API mini project.
