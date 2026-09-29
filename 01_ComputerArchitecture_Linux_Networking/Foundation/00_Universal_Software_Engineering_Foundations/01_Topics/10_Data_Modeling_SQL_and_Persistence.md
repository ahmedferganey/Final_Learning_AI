# Data modeling, SQL and persistence

> **Priority:** Core · **Study window:** 8 · **Approximate focused time:** 12–15 (overlaps with weekly plan)

## Why it is universal

Reliable storage and data modeling matter in analytics, AI, applications, robotics and infrastructure tooling.

## Detailed table of contents / concepts to cover

- [ ] Entities, attributes, primary/foreign keys and cardinality
- [ ] Normalization fundamentals and tradeoffs
- [ ] SELECT, WHERE, JOIN, GROUP BY, HAVING and ORDER BY
- [ ] INSERT, UPDATE, DELETE and transactions
- [ ] Constraints, uniqueness, NULL and basic indexes
- [ ] SQL injection and parameterized queries
- [ ] JSON files vs. SQLite vs. server databases; choose by requirement
- [ ] Data integrity, backups and migration awareness

## How to learn it

1. Draw a small entity-relationship diagram first.
2. Start with SQLite for low setup overhead; PostgreSQL SQL reference transfers well.
3. Write at least 10 hand-authored queries and explain their outputs.
4. Cause a uniqueness violation and a partial failure; use constraints and a transaction to protect data.

## Required exercise

Model projects, tasks and assignments in three tables, then query incomplete tasks by project and owner; add integrity constraints.

## Independent exit criteria

- [ ] Can design a simple relational schema from user requirements.
- [ ] Can write a JOIN without AI and explain cardinality.
- [ ] Can identify the need for a transaction and parameterized SQL.

## AI collaboration exercise

Ask an AI assistant for an alternative approach, at least three failure scenarios and a code/design review. Validate the suggestions independently, make one targeted improvement and describe what you accepted or rejected and why. Never treat the AI answer itself as evidence of correctness.

## Learning notes (fill in)

- **My explanation in five sentences:**
- **One concept diagram / small example:**
- **An error I reproduced and fixed:**
- **What I can now do without AI:**
- **Evidence link (code/tests/notes):**
- **Revisit date:**

## Official learning resources

- [PostgreSQL SQL Tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html)

[← Back to the master roadmap](../README.md)
