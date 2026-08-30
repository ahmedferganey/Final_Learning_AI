# 1. Topic Title

## Introduction to Software Engineering

Software engineering is the disciplined practice of turning an idea into software that can be understood, tested, deployed, operated, changed, and trusted over time.

Programming answers:

```text
How do I make this code work?
```

Software engineering asks a larger set of questions:

```text
What problem are we solving?
Who are the users and stakeholders?
What are the requirements?
What quality attributes matter?
How should the system be structured?
How do we test it?
How do multiple people change it safely?
How do we release it?
How do we observe it?
How do we recover when it fails?
How do we control risk and technical debt?
How do we change it without breaking users?
```

A useful lifecycle mental model is:

```text
Problem / Need
    ↓
Discovery
    ↓
Requirements
    ↓
Architecture / Design
    ↓
Implementation
    ↓
Verification
    ↓
Release
    ↓
Operation
    ↓
Feedback / Maintenance
    ↺
```

The process is not always a strict one-way waterfall. Modern teams iterate through these activities repeatedly.

This module uses a small **Server Health CLI** as the running example so every engineering concept maps to something concrete.

# 2. Learning Objectives

1. Distinguish programming, software development, and software engineering.
2. Explain stakeholders, users, business goals, constraints, assumptions, and scope.
3. Turn vague requests into testable functional requirements.
4. Write measurable non-functional requirements.
5. Define acceptance criteria using observable behavior.
6. Explain lifecycle models including waterfall, iterative, incremental, agile, and DevOps-oriented delivery.
7. Explain why feedback loops matter.
8. Write user stories without treating stories as complete specifications.
9. Break systems into components with clear responsibilities.
10. Explain separation of concerns, cohesion, coupling, interfaces, and dependencies.
11. Create context, component, data-flow, sequence, and deployment diagrams at a basic level.
12. Explain API/function contracts and preconditions/postconditions.
13. Explain architecture decisions and ADRs.
14. Explain trade-offs and quality attributes.
15. Explain unit, integration, system, end-to-end, acceptance, regression, performance, and security testing.
16. Apply boundary-value and negative testing.
17. Explain test pyramid awareness and why all tests should not be end-to-end.
18. Write reproducible defect reports.
19. Explain severity versus priority.
20. Explain debugging as evidence-driven problem isolation.
21. Explain version control and change traceability.
22. Explain branching awareness, commits, pull requests, and code review.
23. Apply code-review checklists.
24. Explain coding standards and static analysis awareness.
25. Explain refactoring and technical debt.
26. Explain semantic versioning awareness and backward compatibility.
27. Explain release readiness, deployment, rollback, and change control.
28. Explain CI/CD at a foundational level.
29. Explain configuration and secret separation.
30. Explain logs, metrics, tracing awareness, health checks, and operational runbooks.
31. Explain reliability, failure modes, graceful degradation, and recovery planning.
32. Explain security-by-design and threat awareness.
33. Explain risk registers and mitigation.
34. Explain documentation types and why documentation must evolve.
35. Explain maintenance, deprecation, and end-of-life.
36. Build a complete lightweight engineering package for a small software product.

# 3. Prerequisites

Recommended:

```text
03. Introduction to Programming
04. Database Fundamentals
```

Helpful:

```text
Operating Systems Fundamentals
Basic networking
Basic command-line usage
Git awareness
```

You do not need to be an advanced programmer. The focus is on **engineering reasoning around software**, not on writing a large codebase.

# 4. Core Concepts Explanation

# Part 1 — Programming vs Software Engineering

### Core Explanation

Programming focuses on implementing executable behavior. Software engineering includes the full lifecycle required to make software useful and sustainable under collaboration, change, operational failure, security requirements, and long-term maintenance.

### Diagram / Mental Model

```text
Programming:
requirement → code

Software Engineering:
problem
 ↓
requirements
 ↓
design
 ↓
code
 ↓
tests
 ↓
release
 ↓
operations
 ↓
maintenance
```

### Why It Matters

Code can be correct locally but still fail as a product because requirements, deployment, security, operations, or maintenance were ignored.

### Practical Use

When designing even a small script, think about how it is configured, tested, run, updated, and troubleshot.

# Part 2 — Stakeholder

### Core Explanation

A stakeholder is any person, team, organization, or system affected by or able to influence the software.

### Diagram / Mental Model

```text
Server Health CLI stakeholders:
Operations engineer
Security team
Platform team
Application owner
Management
CI/CD system
```

### Why It Matters

Different stakeholders often have conflicting goals.

### Practical Use

Capture stakeholder needs before deciding architecture.

# Part 3 — User vs Customer vs Operator

### Core Explanation

The person paying for software, the person using it, and the person operating it may be different.

### Diagram / Mental Model

```text
Customer: business manager
User: operations engineer
Operator: platform/SRE team
```

### Why It Matters

Designing for only one role can create operational or usability problems.

# Part 4 — Problem Statement

### Core Explanation

A problem statement defines the current problem, affected users, business impact, and desired outcome without prematurely prescribing a specific technical solution.

### Example / Code

```text
Poor:
"Build a Python microservice."

Better:
"Operations staff spend 30 minutes manually reviewing server-health CSV files. They need an automated report that highlights critical systems and continues when individual rows are invalid."
```

### Why It Matters

Technology-first statements can hide the actual need.

### Practical Use

Describe the pain before the implementation.

# Part 5 — Business Goal

### Core Explanation

A business goal explains the outcome the organization wants, such as reducing response time, preventing defects, improving visibility, or reducing cost.

### Diagram / Mental Model

```text
Problem:
manual health review

Goal:
reduce review time from 30 min to < 2 min
```

### Why It Matters

Goals help prioritize features and measure success.

# Part 6 — Scope

### Core Explanation

Scope defines what the project includes and excludes.

### Diagram / Mental Model

```text
In scope:
CSV input
classification
text report

Out of scope:
real-time monitoring
auto-remediation
distributed agent
```

### Why It Matters

Without boundaries, projects expand indefinitely.

# Part 7 — Assumption

### Core Explanation

An assumption is something believed to be true for planning but not yet guaranteed.

### Example / Code

```text
Assumption A-01:
Input files contain at most 100,000 rows.
```

### Why It Matters

Unverified assumptions become hidden risks.

### Practical Use

Record assumptions and validate important ones.

# Part 8 — Constraint

### Core Explanation

A constraint is a fixed limitation such as mandated technology, deadline, data residency, budget, legacy system, or supported operating system.

### Example / Code

```text
Constraint C-01:
The tool must run on Windows and Linux without administrator privileges.
```

### Why It Matters

Constraints eliminate design options and should be explicit.

# Part 9 — Functional Requirement

### Core Explanation

A functional requirement describes a behavior the system must provide.

### Example / Code

```text
FR-01:
The system shall read a CSV file containing:
hostname, ip, cpu_percent, memory_percent, disk_percent.

FR-02:
The system shall classify each metric as normal, warning, or critical.
```

### Why It Matters

Functional requirements define what the product does.

### Practical Use

Use stable IDs so requirements can link to tests.

# Part 10 — Non-Functional Requirement

### Core Explanation

A non-functional requirement defines a quality attribute or constraint such as performance, security, availability, usability, portability, maintainability, or recoverability.

### Example / Code

```text
NFR-01:
The tool shall process 100,000 valid rows in under 10 seconds on the reference machine.

NFR-02:
No secret values shall be written to logs.
```

### Why It Matters

Quality requirements often determine architecture more than functional behavior.

# Part 11 — Testable Requirement

### Core Explanation

A requirement should be precise enough to verify objectively.

### Example / Code

```text
Vague:
"The report should be fast."

Testable:
"On the reference machine, a 100,000-row valid input shall complete in <= 10 seconds."
```

### Why It Matters

If nobody can decide objectively whether the requirement passed, it is not useful for verification.

# Part 12 — Requirement Ambiguity

### Core Explanation

Ambiguous words include 'fast', 'secure', 'user-friendly', 'large', 'near real-time', and 'support many users' unless quantified or operationalized.

### Why It Matters

Different stakeholders interpret them differently.

### Practical Use

Replace ambiguous language with measurable conditions.

# Part 13 — Acceptance Criteria

### Core Explanation

Acceptance criteria define observable outcomes that make a requirement or story acceptable.

### Example / Code

```text
Given disk_percent = 92
When the record is classified
Then disk status is "critical"
```

### Why It Matters

Acceptance criteria connect business expectation to tests.

# Part 14 — Given-When-Then

### Core Explanation

Given-When-Then is a useful behavior-description structure.

### Diagram / Mental Model

```text
Given = initial context
When  = action/event
Then  = expected observable result
```

### Why It Matters

It keeps tests focused on behavior instead of implementation.

# Part 15 — Out of Scope

### Core Explanation

Out-of-scope items explicitly state what the current delivery will not solve.

### Why It Matters

This protects focus and prevents hidden expectations.

### Practical Use

Out of scope does not mean 'never'; it means 'not in this version/project'.

# Part 16 — Requirements Traceability

### Core Explanation

Traceability links goals → requirements → design → implementation → tests → release evidence.

### Diagram / Mental Model

```text
Goal G1
 ↓
FR-02
 ↓
classifier component
 ↓
test_classify_critical
 ↓
release test evidence
```

### Why It Matters

Useful for audits, regulated work, impact analysis, and defect investigation.

# Part 17 — Requirements Change

### Core Explanation

Requirements change because markets, users, regulations, architecture, and understanding change. Engineering must absorb change without losing control.

### Diagram / Mental Model

```text
Change request
 ↓
impact analysis
 ↓
requirements/design/tests update
 ↓
implementation
 ↓
verification
```

### Why It Matters

Change is normal; unmanaged change is the problem.

# Part 18 — Software Development Lifecycle

### Core Explanation

The SDLC is the set of activities used to discover, design, implement, verify, release, operate, and evolve software.

### Diagram / Mental Model

```text
Discover
 ↓
Requirements
 ↓
Design
 ↓
Build
 ↓
Test
 ↓
Release
 ↓
Operate
 ↓
Learn
 ↺
```

### Why It Matters

Every software product performs these activities even if a team uses different names.

# Part 19 — Waterfall Model Awareness

### Core Explanation

A waterfall-style process emphasizes sequential phases with substantial completion before the next phase.

### Diagram / Mental Model

```text
Requirements → Design → Build → Test → Release
```

### Why It Matters

Useful where change is expensive and formal approvals are required, but feedback may arrive late.

### Practical Use

Understand it as one lifecycle model, not as automatically 'bad'.

# Part 20 — Iterative Development

### Core Explanation

Iterative development repeatedly revisits a solution, improving it through feedback.

### Diagram / Mental Model

```text
Version 1 → feedback → Version 2 → feedback → Version 3
```

### Why It Matters

Early learning reduces the risk of building the wrong thing.

# Part 21 — Incremental Development

### Core Explanation

Incremental development delivers the system in usable slices.

### Diagram / Mental Model

```text
Increment 1: CSV read
Increment 2: classification
Increment 3: reports
Increment 4: JSON output
```

### Why It Matters

Value can be delivered before every feature is complete.

# Part 22 — Agile Thinking

### Core Explanation

Agile approaches emphasize frequent feedback, working increments, collaboration, adaptability, and continuous prioritization.

### Why It Matters

Agility is not 'no documentation' or 'no planning'.

### Practical Use

Plan enough to make good decisions, then update the plan from evidence.

# Part 23 — User Story

### Core Explanation

A user story expresses a user-centered need.

### Example / Code

```text
As an operations engineer,
I want critical systems highlighted,
so that I can prioritize investigation.
```

### Why It Matters

Stories help focus on value.

### Practical Use

A story should be supported by acceptance criteria, constraints, and technical detail where needed.

# Part 24 — Backlog

### Core Explanation

A backlog is an ordered set of work items such as features, defects, technical improvements, and research.

### Why It Matters

It makes work visible and prioritizable.

# Part 25 — Prioritization

### Core Explanation

Teams prioritize based on value, urgency, risk, dependencies, effort, and strategy rather than treating every request as equally important.

### Diagram / Mental Model

```text
High value / low effort → often early
High risk dependency → may need early discovery
Low value / high effort → often defer
```

# Part 26 — Definition of Done Awareness

### Core Explanation

A Definition of Done is a shared quality checklist that describes what must be true before work is considered complete.

### Example / Code

```text
Example:
code implemented
tests pass
review complete
docs updated
security checks pass
release notes updated
```

### Why It Matters

Prevents 'done' from meaning only 'coding finished'.

# Part 27 — Feedback Loop

### Core Explanation

A feedback loop measures results and uses them to improve the next iteration.

### Diagram / Mental Model

```text
Build → Measure → Learn → Adjust → Build
```

### Why It Matters

Software engineering is a learning system.

# Part 28 — Architecture

### Core Explanation

Software architecture describes major components, responsibilities, interfaces, dependencies, data flow, deployment boundaries, and significant design decisions.

### Diagram / Mental Model

```text
CSV Input
  ↓
Parser
  ↓
Validator
  ↓
Classifier
  ↓
Report Generator
  ↓
Console/File
```

### Why It Matters

Architecture allows engineers to reason about the system before reading every line of code.

# Part 29 — Design

### Core Explanation

Design is the detailed arrangement of components, data structures, functions/classes, interfaces, and algorithms used to realize the architecture.

### Why It Matters

Architecture and design overlap; the distinction is mainly level and significance.

# Part 30 — Separation of Concerns

### Core Explanation

Different responsibilities should be separated so one change does not unnecessarily affect unrelated behavior.

### Diagram / Mental Model

```text
Input parsing ≠ business classification ≠ output formatting
```

### Why It Matters

Improves testability and maintainability.

# Part 31 — Single Responsibility Awareness

### Core Explanation

A component should have one coherent reason to change.

### Example / Code

```text
Poor:
process_everything()

Better:
load_csv()
validate_row()
classify_metrics()
render_report()
```

### Why It Matters

Smaller responsibilities are easier to test and review.

# Part 32 — Cohesion

### Core Explanation

Cohesion describes how closely related responsibilities inside a module/component are. High cohesion means the component contains behaviors that belong together.

### Why It Matters

High cohesion makes components easier to understand.

# Part 33 — Coupling

### Core Explanation

Coupling describes dependencies between components. Excessive coupling means a change in one place causes widespread changes elsewhere.

### Diagram / Mental Model

```text
Tightly coupled:
Parser directly formats output and writes DB

Looser:
Parser → domain model → reporter
```

### Why It Matters

Low unnecessary coupling supports change.

# Part 34 — Interface

### Core Explanation

An interface defines how one component interacts with another.

### Example / Code

```text
def classify_usage(value: float) -> str:
    ...
```

### Why It Matters

Explicit interfaces allow independent implementation/testing.

# Part 35 — Contract

### Core Explanation

A contract documents valid inputs, outputs, errors, and guarantees.

### Example / Code

```text
classify_usage(value)
Precondition:
0 <= value <= 100

Returns:
"normal" | "warning" | "critical"

Raises:
ValueError for invalid percentage
```

### Why It Matters

A signature alone may not define complete behavior.

# Part 36 — Precondition

### Core Explanation

A precondition is something that must be true before an operation is valid.

### Example / Code

```text
0 <= cpu <= 100
```

### Why It Matters

Preconditions clarify responsibility between caller and callee.

# Part 37 — Postcondition

### Core Explanation

A postcondition describes what is guaranteed after successful completion.

### Example / Code

```text
If classify_usage returns successfully,
the result is one of:
normal, warning, critical
```

### Why It Matters

Useful for testing and reasoning.

# Part 38 — Dependency

### Core Explanation

A dependency is another component, library, service, database, or runtime needed by a component.

### Diagram / Mental Model

```text
Report CLI
├─ csv module
├─ filesystem
└─ classifier module
```

### Why It Matters

Dependencies can fail and must be managed.

# Part 39 — Dependency Direction

### Core Explanation

A useful design goal is to keep core business logic independent of infrastructure details where practical.

### Diagram / Mental Model

```text
CLI/File Adapter
      ↓
Application Logic
      ↓
Domain Rules

Core logic does not need to know terminal/file details
```

### Why It Matters

Makes testing easier and infrastructure replaceable.

# Part 40 — Context Diagram

### Core Explanation

A context diagram shows the system boundary and external actors/systems.

### Diagram / Mental Model

```text
Operations Engineer
       ↓
[ Server Health CLI ]
       ↓
Input File / Output File
```

### Why It Matters

Clarifies what is inside and outside the system.

# Part 41 — Component Diagram

### Core Explanation

A component diagram shows major internal parts and dependencies.

### Diagram / Mental Model

```text
CLI
 ↓
CSV Reader → Validator → Classifier → Reporter
```

### Why It Matters

Good for architecture communication.

# Part 42 — Data Flow Diagram

### Core Explanation

A data-flow diagram focuses on where data originates, transforms, crosses boundaries, and is stored.

### Diagram / Mental Model

```text
CSV
 ↓ raw row
Parser
 ↓ dict
Validator
 ↓ validated record
Classifier
 ↓ result
Reporter
```

### Why It Matters

Useful for security and troubleshooting.

# Part 43 — Sequence Diagram Awareness

### Core Explanation

A sequence diagram shows interactions over time.

### Diagram / Mental Model

```text
User      CLI      Reader    Classifier
 |         |          |          |
 | run     |          |          |
 |-------->| read     |          |
 |         |--------->|          |
 |         |<---------| rows     |
 |         | classify |--------->|
 |         |<--------------------| result
```

### Why It Matters

Helps reason about call order and failures.

# Part 44 — Deployment Diagram Awareness

### Core Explanation

A deployment view maps software components to runtime environments.

### Diagram / Mental Model

```text
Laptop / VM
└─ Python runtime
   └─ health CLI
      ├─ input CSV
      └─ report file
```

### Why It Matters

Runtime assumptions are part of engineering.

# Part 45 — Quality Attribute

### Core Explanation

A quality attribute is a measurable non-functional property such as reliability, performance, security, usability, scalability, or maintainability.

### Why It Matters

Architecture is largely the management of quality-attribute trade-offs.

# Part 46 — Trade-Off

### Core Explanation

Improving one quality may make another worse.

### Diagram / Mental Model

```text
More redundancy
+ availability
- cost
- complexity

More validation
+ correctness/security
- some processing overhead
```

### Why It Matters

There is rarely a universally optimal architecture.

# Part 47 — Architecture Decision Record

### Core Explanation

An ADR captures context, options, decision, and consequences for a significant architecture choice.

### Example / Code

```text
ADR-001: CSV input library
Context: need quoted CSV support
Options: manual split, stdlib csv
Decision: stdlib csv
Consequences: robust parsing, no external dependency
```

### Why It Matters

Preserves the reasoning behind decisions.

# Part 48 — YAGNI Awareness

### Core Explanation

You Aren't Gonna Need It encourages avoiding speculative features or abstractions that are not justified by current requirements.

### Why It Matters

Overengineering creates cost and complexity.

# Part 49 — KISS Awareness

### Core Explanation

Keep It Simple encourages the simplest design that satisfies requirements.

### Why It Matters

Simple systems are easier to test, secure, operate, and change.

# Part 50 — DRY Awareness

### Core Explanation

Don't Repeat Yourself means important knowledge/logic should have a single authoritative representation rather than copied implementations.

### Example / Code

```text
Poor:
same threshold logic in CLI and report module

Better:
one classify_usage() function
```

### Why It Matters

Duplicated business rules drift over time.

# Part 51 — Coding Standard

### Core Explanation

A coding standard defines naming, formatting, structure, error handling, documentation, and other team conventions.

### Why It Matters

Consistency reduces cognitive load.

# Part 52 — Readable Code

### Core Explanation

Readable code communicates intent through names, small units, direct logic, and appropriate comments.

### Example / Code

```text
def classify_usage(percent):
    ...
# clearer than:
def c(x):
    ...
```

### Why It Matters

Maintenance dominates the lifecycle of successful software.

# Part 53 — Code Smell Awareness

### Core Explanation

A code smell is a structural symptom that may indicate deeper design problems, such as very long functions, duplicated logic, excessive parameters, or hidden global state.

### Why It Matters

A smell is not automatically a bug; it is a prompt to investigate.

# Part 54 — Refactoring

### Core Explanation

Refactoring changes internal structure without intentionally changing externally visible behavior.

### Diagram / Mental Model

```text
Before:
one huge function

Refactor:
parse()
validate()
classify()
report()

Same expected behavior
```

### Why It Matters

Tests make refactoring safer.

# Part 55 — Technical Debt

### Core Explanation

Technical debt is the future cost created by shortcuts, obsolete design, missing tests, poor documentation, or accumulated complexity.

### Why It Matters

Some debt is deliberate and acceptable if visible and managed.

# Part 56 — Dependency Management Awareness

### Core Explanation

External libraries bring useful capabilities but also versioning, security, compatibility, and licensing responsibilities.

### Why It Matters

Every dependency adds a maintenance surface.

# Part 57 — Static Analysis Awareness

### Core Explanation

Static-analysis tools inspect source code without executing every path and can detect style, type, correctness, or security issues.

### Why It Matters

Automated analysis complements tests and review.

# Part 58 — Linting Awareness

### Core Explanation

Linters detect style and common code-quality issues.

### Why It Matters

Consistent automation reduces review noise.

# Part 59 — Formatting Automation Awareness

### Core Explanation

Formatters apply consistent style automatically.

### Why It Matters

Humans can focus review on behavior and design instead of whitespace.

# Part 60 — Verification vs Validation

### Core Explanation

Verification asks whether we built the system according to specification. Validation asks whether the system actually solves the intended user/business problem.

### Diagram / Mental Model

```text
Verification:
requirements → implementation correctness

Validation:
user need → useful outcome
```

### Why It Matters

Software can meet written requirements yet still fail the real need.

# Part 61 — Unit Test

### Core Explanation

A unit test verifies a small isolated unit such as a function.

### Example / Code

```python
def test_critical_boundary():
    assert classify_usage(90) == "critical"
```

### Why It Matters

Fast, focused feedback.

# Part 62 — Integration Test

### Core Explanation

An integration test verifies multiple components working together.

### Diagram / Mental Model

```text
CSV Reader + Validator + Classifier
```

### Why It Matters

Catches interface and data-format problems that unit tests may miss.

# Part 63 — System Test

### Core Explanation

A system test verifies the complete integrated product in a representative environment.

### Diagram / Mental Model

```text
input file → CLI process → output report
```

### Why It Matters

Tests end-to-end system behavior.

# Part 64 — End-to-End Test

### Core Explanation

An E2E test exercises a complete user-visible workflow across major components.

### Why It Matters

High confidence but slower and more fragile than focused tests.

# Part 65 — Acceptance Test

### Core Explanation

An acceptance test confirms agreed user/business behavior.

### Example / Code

```text
Given CPU=90
When report is generated
Then server is critical
```

### Why It Matters

Directly connects requirements to evidence.

# Part 66 — Regression Test

### Core Explanation

A regression test prevents a previously working or fixed behavior from breaking in the future.

### Why It Matters

Every significant defect should ideally produce a protective test.

# Part 67 — Boundary Testing

### Core Explanation

Boundary testing checks values at and immediately around decision boundaries.

### Diagram / Mental Model

```text
74.99 | 75 | 89.99 | 90
```

### Why It Matters

Many bugs occur at comparisons.

# Part 68 — Negative Testing

### Core Explanation

Negative tests intentionally provide invalid input or failure conditions.

### Diagram / Mental Model

```text
missing column
bad number
permission denied
corrupt file
```

### Why It Matters

Robust software must define failure behavior.

# Part 69 — Performance Test Awareness

### Core Explanation

Performance testing measures latency, throughput, memory, CPU, or scalability against requirements.

### Why It Matters

Performance should be measured under a defined workload.

# Part 70 — Security Testing Awareness

### Core Explanation

Security testing verifies authentication, authorization, input handling, secret management, dependency risk, and other security requirements.

### Why It Matters

Security must be tested, not assumed.

# Part 71 — Test Pyramid Awareness

### Core Explanation

A common model recommends many fast focused tests, fewer integration tests, and a smaller number of expensive E2E tests.

### Diagram / Mental Model

```text
E2E
     /---\
  Integration
 /-----------\
     Unit
/-------------\
```

### Why It Matters

All-E2E suites are slow and difficult to diagnose.

# Part 72 — Test Fixture

### Core Explanation

A fixture is controlled setup data/environment used by tests.

### Example / Code

```text
servers.csv test fixture
contains normal/warning/critical/invalid rows
```

### Why It Matters

Tests should be repeatable.

# Part 73 — Deterministic Test

### Core Explanation

A deterministic test produces the same result given the same controlled conditions.

### Why It Matters

Flaky tests reduce trust in CI.

# Part 74 — Test Coverage Awareness

### Core Explanation

Coverage measures which code was executed by tests, but high coverage does not prove good assertions or correct requirements.

### Why It Matters

Use coverage as one signal, not a quality score.

# Part 75 — Defect

### Core Explanation

A defect is a deviation between expected and actual software behavior or quality.

### Diagram / Mental Model

```text
Expected != Actual → defect candidate
```

# Part 76 — Defect Report

### Core Explanation

A useful bug report records title, environment, preconditions, steps, expected result, actual result, evidence, severity, and reproducibility.

### Example / Code

```text
Title: CPU=90 classified as warning
Environment: Python X, Windows/Linux
Steps:
1. Run classifier with 90
Expected: critical
Actual: warning
Evidence: test output
```

### Why It Matters

Reproducibility reduces investigation time.

# Part 77 — Severity vs Priority

### Core Explanation

Severity describes impact; priority describes how urgently the organization chooses to address the issue.

### Diagram / Mental Model

```text
High severity / lower priority possible
Low severity / high priority possible
```

### Why It Matters

They answer different questions.

# Part 78 — Reproduction

### Core Explanation

A reproducible failure can be triggered consistently from documented steps.

### Why It Matters

If you cannot reproduce it, gather environment and telemetry rather than declaring it impossible.

# Part 79 — Root Cause

### Core Explanation

Root cause is the underlying condition that produced the failure, not merely the visible symptom.

### Diagram / Mental Model

```text
Symptom:
report missing rows

Immediate cause:
CSV parser stopped

Root cause:
one invalid row throws unhandled ValueError
```

### Why It Matters

Fixing symptoms can leave the defect intact.

# Part 80 — Debugging Process

### Core Explanation

Debugging should be evidence-driven.

### Diagram / Mental Model

```text
Reproduce
 ↓
Narrow scope
 ↓
Inspect evidence
 ↓
Form hypothesis
 ↓
Test one change
 ↓
Verify
 ↓
Add regression test
```

### Why It Matters

Random changes destroy useful evidence.

# Part 81 — Five Whys Awareness

### Core Explanation

Repeatedly asking why can help trace symptoms to underlying process/design causes when used carefully.

### Why It Matters

It is a thinking aid, not a substitute for technical evidence.

# Part 82 — Version Control

### Core Explanation

Version control records source changes over time and supports history, comparison, collaboration, rollback, and traceability.

### Diagram / Mental Model

```text
Commit A → Commit B → Commit C
```

### Why It Matters

Software engineering requires knowing what changed and why.

# Part 83 — Commit

### Core Explanation

A commit records a coherent snapshot/change with author and message.

### Example / Code

```text
Example message:
Validate CPU percentage before classification
```

### Why It Matters

Small focused commits improve review and rollback.

# Part 84 — Branch Awareness

### Core Explanation

A branch provides an independent line of development.

### Diagram / Mental Model

```text
main ── A ── B ───────── D
             \ feature ─ C /
```

### Why It Matters

Supports parallel work and controlled integration.

# Part 85 — Pull Request / Merge Request Awareness

### Core Explanation

A change proposal provides a place for review, automated checks, discussion, and approval before integration.

### Why It Matters

Review is a risk-control mechanism.

# Part 86 — Code Review

### Core Explanation

Code review evaluates correctness, design, complexity, tests, security, maintainability, and consistency.

### Diagram / Mental Model

```text
Author change
   ↓
Automated checks
   ↓
Peer review
   ↓
Fix feedback
   ↓
Merge
```

### Why It Matters

Review distributes knowledge and catches defects before release.

# Part 87 — Review Scope

### Core Explanation

Small, focused changes are easier to understand accurately than huge mixed changes.

### Why It Matters

Cognitive load directly affects review quality.

# Part 88 — Review Checklist

### Core Explanation

A checklist makes recurring quality concerns explicit.

### Example / Code

```text
Correctness?
Tests?
Input validation?
Error handling?
Secrets?
Naming?
Complexity?
Docs?
Backward compatibility?
```

### Why It Matters

Checklists reduce omission.

# Part 89 — Change Control

### Core Explanation

Change control records the purpose, scope, risk, validation, rollout, rollback, and result of a change.

### Diagram / Mental Model

```text
Request
 ↓
Review risk
 ↓
Approve
 ↓
Deploy
 ↓
Verify
 ↓
Close / rollback
```

### Why It Matters

Especially important for production and regulated systems.

# Part 90 — Impact Analysis

### Core Explanation

Before changing a requirement/interface/schema, identify affected code, tests, consumers, documentation, operations, and data.

### Diagram / Mental Model

```text
Change API field
├─ backend
├─ frontend
├─ tests
├─ docs
└─ downstream clients
```

### Why It Matters

Prevents hidden breakage.

# Part 91 — Build

### Core Explanation

A build transforms source into a runnable/testable artifact or package.

### Diagram / Mental Model

```text
Source → dependencies → build → artifact
```

### Why It Matters

Builds should be reproducible.

# Part 92 — Artifact

### Core Explanation

An artifact is a versioned output such as a package, binary, container image, or deployable archive.

### Why It Matters

Deployment should use known artifacts, not untracked developer files.

# Part 93 — Continuous Integration Awareness

### Core Explanation

CI automatically builds and tests integrated changes frequently.

### Diagram / Mental Model

```text
Git push
 ↓
lint
 ↓
unit tests
 ↓
integration tests
 ↓
build artifact
```

### Why It Matters

Fast feedback catches integration defects early.

# Part 94 — Continuous Delivery Awareness

### Core Explanation

Continuous Delivery keeps software in a releasable state through automated verification and deployment processes, with production release potentially requiring approval.

### Why It Matters

Reduces risky manual release steps.

# Part 95 — Deployment

### Core Explanation

Deployment places a software version into a runtime environment.

### Diagram / Mental Model

```text
Artifact + Config → Runtime Environment
```

### Why It Matters

Deployment is not the same as release to users.

# Part 96 — Release

### Core Explanation

Release makes a capability available to users. Deployment and release can be separated using feature flags or staged rollout.

### Diagram / Mental Model

```text
Deploy code disabled
 ↓
verify
 ↓
enable feature
```

### Why It Matters

Separating them can reduce risk.

# Part 97 — Rollback

### Core Explanation

Rollback restores a previous known-good application/configuration state when a new release causes unacceptable failure.

### Diagram / Mental Model

```text
v2 bad → route/deploy v1
```

### Why It Matters

Recovery should be planned before the incident.

# Part 98 — Roll Forward

### Core Explanation

Sometimes fixing forward is safer than rollback, especially after irreversible data/schema changes.

### Why It Matters

Recovery strategy depends on compatibility and state.

# Part 99 — Release Checklist

### Core Explanation

A release checklist verifies readiness.

### Example / Code

```text
tests pass
security checks pass
config documented
backup/recovery ready
migration reviewed
rollback/forward plan
monitoring ready
owner available
```

### Why It Matters

A release is an operational event, not only a code merge.

# Part 100 — Semantic Versioning Awareness

### Core Explanation

Semantic versioning commonly expresses major.minor.patch with intended compatibility meaning.

### Diagram / Mental Model

```text
1.4.2
major.minor.patch
```

### Why It Matters

Versioning communicates change expectations, though not every project follows SemVer.

# Part 101 — Backward Compatibility

### Core Explanation

A backward-compatible change allows existing consumers/data to continue working.

### Example / Code

```text
Safer:
add optional field

Breaking:
rename/remove required field
```

### Why It Matters

Distributed systems often have multiple versions active during rollout.

# Part 102 — Configuration

### Core Explanation

Environment-specific settings should be separated from source code.

### Diagram / Mental Model

```text
Same artifact
+ dev config
+ stage config
+ prod config
```

### Why It Matters

Supports reproducible deployment and avoids hardcoded environment assumptions.

# Part 103 — Secret

### Core Explanation

Secrets such as passwords, tokens, and private keys require stronger handling than normal configuration.

### Why It Matters

Never commit secrets to source control.

# Part 104 — Environment Parity Awareness

### Core Explanation

Development, test, and production should be similar enough that important runtime assumptions are tested before release.

### Why It Matters

Large environment differences create 'works on my machine' failures.

# Part 105 — Operational Readiness

### Core Explanation

Software is operationally ready when teams know how to run, observe, recover, and support it.

### Diagram / Mental Model

```text
Release ready =
code + config + monitoring + runbook + recovery
```

### Why It Matters

Operations begins during design.

# Part 106 — Logging

### Core Explanation

Logs record discrete events with context such as timestamp, level, component, request/job ID, and message.

### Example / Code

```text
INFO processed_file rows=1000 invalid=2
```

### Why It Matters

Logs help reconstruct what happened.

### Practical Use

Do not log secrets or unnecessary personal data.

# Part 107 — Metrics

### Core Explanation

Metrics are numeric time-series signals such as request count, latency, errors, CPU, or business events.

### Diagram / Mental Model

```text
records_processed_total
invalid_rows_total
processing_seconds
```

### Why It Matters

Metrics help detect trends and automate alerts.

# Part 108 — Tracing Awareness

### Core Explanation

Tracing follows one request/job across multiple components using correlated spans/identifiers.

### Why It Matters

More relevant in distributed systems, but the concept begins with correlation.

# Part 109 — Health Check

### Core Explanation

A health check indicates whether a process/service is functioning enough for monitoring or routing.

### Why It Matters

Define what 'healthy' actually means.

# Part 110 — Monitoring

### Core Explanation

Monitoring continuously collects and evaluates operational signals.

### Diagram / Mental Model

```text
Software → logs/metrics/health → monitoring → alert/operator
```

### Why It Matters

You cannot operate what you cannot observe.

# Part 111 — Alert

### Core Explanation

An alert notifies a human/system when a signal crosses a meaningful condition.

### Why It Matters

Alert on actionable user-impacting conditions, not every fluctuation.

# Part 112 — Runbook

### Core Explanation

A runbook provides operational procedures for diagnosis, recovery, rollback, and escalation.

### Example / Code

```text
Incident: report generation fails
1. Check input path
2. Check permissions
3. Check logs
4. Reproduce with sample
5. Roll back if release-related
```

### Why It Matters

Incidents are a bad time to invent procedures.

# Part 113 — Failure Mode

### Core Explanation

A failure mode is a way a component can fail.

### Diagram / Mental Model

```text
Input reader:
file missing
permission denied
malformed CSV
disk failure
```

### Why It Matters

Enumerating failure modes improves design and tests.

# Part 114 — Graceful Failure

### Core Explanation

Graceful failure provides controlled behavior rather than uncontrolled crash or corrupt output.

### Example / Code

```text
One invalid CSV row
→ log row error
→ continue valid rows
→ summary invalid count
```

### Why It Matters

Failure policy is part of requirements.

# Part 115 — Graceful Degradation Awareness

### Core Explanation

A system may continue partial useful behavior when a non-critical dependency fails.

### Why It Matters

Availability does not always require every feature.

# Part 116 — Reliability

### Core Explanation

Reliability is the ability to perform required functions correctly over time under expected conditions and failures.

### Why It Matters

Reliability includes design, testing, operations, and recovery.

# Part 117 — Availability Awareness

### Core Explanation

Availability measures whether the service is usable when needed.

### Why It Matters

High availability requires redundancy, recovery, monitoring, and operational discipline.

# Part 118 — Security by Design

### Core Explanation

Security decisions should begin in requirements and architecture, not only after implementation.

### Diagram / Mental Model

```text
Requirements
 ↓
Threats
 ↓
Security controls
 ↓
Implementation
 ↓
Security tests
 ↓
Monitoring
```

### Why It Matters

Late security changes are more expensive.

# Part 119 — Threat Modeling Awareness

### Core Explanation

Threat modeling identifies assets, trust boundaries, potential attackers/misuse, and controls.

### Diagram / Mental Model

```text
Assets:
server inventory

Trust boundary:
external CSV input

Threat:
malformed or sensitive data

Controls:
validation, least privilege, logging policy
```

### Why It Matters

It makes security design explicit.

# Part 120 — Least Privilege

### Core Explanation

Software processes and deployment identities should have only required permissions.

### Why It Matters

Limits the impact of defects or compromise.

# Part 121 — Secure Defaults

### Core Explanation

The default configuration should prefer safer behavior.

### Example / Code

```text
Example:
report file private by default
no debug secrets
reject malformed input
```

### Why It Matters

Most users keep defaults.

# Part 122 — Dependency Security Awareness

### Core Explanation

Third-party libraries can contain vulnerabilities or malicious packages.

### Why It Matters

Track dependencies, trusted sources, and updates.

# Part 123 — Documentation as Product

### Core Explanation

Documentation should answer real engineering and operational questions and evolve with the code.

### Diagram / Mental Model

```text
README
requirements
architecture
API/contracts
test plan
runbooks
release notes
```

### Why It Matters

Outdated documentation can be worse than missing documentation.

# Part 124 — README

### Core Explanation

A README should explain purpose, setup, usage, examples, configuration, testing, and support/troubleshooting pointers.

### Why It Matters

It is the entry point for users and contributors.

# Part 125 — Architecture Documentation

### Core Explanation

Architecture docs explain components, responsibilities, interfaces, dependencies, data flow, important trade-offs, and deployment.

### Why It Matters

A diagram without explanation is incomplete.

# Part 126 — API / Contract Documentation

### Core Explanation

Contract docs describe inputs, outputs, errors, versioning, and examples.

### Why It Matters

Consumers need stable expectations.

# Part 127 — Test Plan

### Core Explanation

A test plan maps risks/requirements to test levels, environments, data, and acceptance criteria.

### Diagram / Mental Model

```text
Requirement → test case → evidence
```

### Why It Matters

Testing should be risk-driven.

# Part 128 — Risk

### Core Explanation

A risk is an uncertain event/condition that could negatively affect objectives.

### Example / Code

```text
Risk:
large CSV causes excessive memory use

Likelihood: medium
Impact: high
Mitigation:
stream rows instead of loading all
```

### Why It Matters

Engineering is partly risk management.

# Part 129 — Risk Register

### Core Explanation

A risk register records risk, likelihood, impact, owner, mitigation, contingency, and status.

### Why It Matters

Makes risk visible and actionable.

# Part 130 — Likelihood vs Impact

### Core Explanation

Likelihood estimates probability/frequency; impact estimates consequence.

### Diagram / Mental Model

```text
High likelihood + high impact → prioritize mitigation
```

### Why It Matters

Separating them helps rational prioritization.

# Part 131 — Mitigation

### Core Explanation

Mitigation reduces the likelihood or impact of a risk before it occurs.

### Why It Matters

Example: add input-size limits and streaming processing.

# Part 132 — Contingency

### Core Explanation

A contingency is what you do if the risk becomes real.

### Why It Matters

Example: rollback release, restore backup, switch provider.

# Part 133 — Maintenance

### Core Explanation

Maintenance includes defect fixes, dependency updates, performance improvements, platform changes, documentation, and feature evolution.

### Why It Matters

Most software cost occurs after initial implementation.

# Part 134 — Corrective Maintenance

### Core Explanation

Corrective maintenance fixes defects.

### Practical Use

Bug fix + regression test.

# Part 135 — Adaptive Maintenance

### Core Explanation

Adaptive maintenance updates software for changed environments, platforms, APIs, regulations, or dependencies.

### Practical Use

Support a new OS/runtime version.

# Part 136 — Perfective Maintenance

### Core Explanation

Perfective maintenance improves performance, maintainability, usability, or functionality.

### Practical Use

Refactor reporting pipeline or optimize large-file handling.

# Part 137 — Preventive Maintenance

### Core Explanation

Preventive maintenance reduces future risk before a failure occurs.

### Practical Use

Upgrade vulnerable dependency, add missing tests, simplify fragile code.

# Part 138 — Deprecation

### Core Explanation

Deprecation announces that a feature/interface remains temporarily available but is planned for removal.

### Why It Matters

Gives users time to migrate.

# Part 139 — End of Life Awareness

### Core Explanation

End of life means a version/product is no longer supported or maintained.

### Why It Matters

Unsupported software accumulates security and compatibility risk.

# Part 140 — Post-Incident Review Awareness

### Core Explanation

After a significant incident, teams should analyze what happened, impact, contributing factors, detection, response, and actions without reducing the process to blame.

### Diagram / Mental Model

```text
Incident
 ↓
Timeline
 ↓
Contributing factors
 ↓
Corrective actions
 ↓
Track completion
```

### Why It Matters

The goal is system learning.

# Part 141 — Final Software Engineering Mental Model

### Core Explanation

Software engineering connects user value, technical design, verification, delivery, operations, security, and long-term change.

### Diagram / Mental Model

```text
Need
 ↓
Requirements
 ↓
Architecture
 ↓
Implementation
 ↓
Tests
 ↓
Review
 ↓
Release
 ↓
Operate
 ↓
Observe
 ↓
Improve
 ↺
```

### Why It Matters

A successful engineer thinks beyond code execution to the complete system lifecycle.

# 5. Hands-on Lab / Practical Exercises

## Lab 1 — Turn a Vague Idea into Requirements

Start with:
```text
"Build a tool that checks server health."
```
Create:
```text
problem statement
stakeholders
business goal
8 functional requirements
8 non-functional requirements
5 out-of-scope items
5 assumptions
5 constraints
```
Every requirement must be testable.

## Lab 2 — Rewrite Ambiguous Requirements

Rewrite:
```text
The tool should be fast.
The tool should be secure.
The interface should be easy.
It should support large files.
```
into measurable requirements.

## Lab 3 — Acceptance Criteria

For at least 5 requirements, write Given-When-Then acceptance criteria.

## Lab 4 — Traceability Matrix

Create:
```text
Requirement ID
Design component
Test case
Release evidence
```
for at least 10 requirements.

## Lab 5 — Lifecycle Comparison

Compare:
```text
waterfall
iterative
incremental
agile
```
for the Server Health CLI. Explain benefits and risks of each.

## Lab 6 — Product Backlog

Create a prioritized backlog of:
```text
features
defects
technical debt
security tasks
documentation
```
Explain your top 5 priorities.

## Lab 7 — Architecture Decomposition

Draw:
```text
CLI
 ↓
Input Reader
 ↓
Validator
 ↓
Classifier
 ↓
Reporter
```
For each define responsibility, input, output, errors, dependencies.

## Lab 8 — Context Diagram

Draw the Server Health CLI boundary and show:
```text
operations user
input CSV
output file
CI job if applicable
```

## Lab 9 — Data Flow Diagram

Map raw CSV to validated record to classification result to report.
Mark the external-input trust boundary.

## Lab 10 — Sequence Diagram

Draw the interaction sequence for:
```text
user runs CLI
file opened
row parsed
row validated
classification calculated
report written
```

## Lab 11 — Function Contract

Write a full contract for:
```python
classify_usage(value)
```
including:
```text
preconditions
return values
errors
examples
```

## Lab 12 — ADR

Write ADR-001 comparing:
```text
manual CSV split
Python stdlib csv
third-party dataframe library
```
Choose one and document consequences.

## Lab 13 — Trade-Off Matrix

Compare:
```text
single-file script
multi-module CLI
microservice
```
against:
```text
complexity
testability
deployment
operations
security
scalability
```

## Lab 14 — Code Smell Review

Take one previous script and identify:
```text
long function
duplicate logic
unclear names
global state
mixed concerns
```
Refactor only where justified.

## Lab 15 — Unit Test Design

Create unit tests for classification:
```text
0
74.99
75
89.99
90
100
invalid low/high
```

## Lab 16 — Integration Test Design

Test:
```text
CSV Reader + Validator + Classifier
```
using controlled sample files.

## Lab 17 — End-to-End Test

Create a temporary input file, run the CLI, and verify the generated report contents and process exit behavior.

## Lab 18 — Negative Testing

Test:
```text
missing file
permission denied
missing column
empty row
bad number
oversized input awareness
```
Document expected behavior.

## Lab 19 — Performance Requirement Test Plan

Define how you would verify:
```text
100,000 rows processed in <= 10 seconds
```
including machine/environment, repeated runs, and measurements.

## Lab 20 — Defect Report

Introduce one intentional classification defect and write:
```text
title
environment
preconditions
steps
expected
actual
evidence
severity
priority recommendation
```

## Lab 21 — Root Cause Analysis

For the defect:
```text
program stops on one invalid row
```
separate:
```text
symptom
direct cause
root design cause
corrective action
preventive action
```

## Lab 22 — Version-Control Plan

Define a Git workflow:
```text
main branch
feature branch
small commits
pull request
automated checks
review
merge
```
No advanced Git implementation is required here.

## Lab 23 — Commit Quality

Take one large hypothetical change and split it into 4 coherent commits with good commit messages.

## Lab 24 — Code Review

Review a function using:
```text
correctness
requirements
tests
input validation
errors
security
naming
complexity
documentation
```

## Lab 25 — Change Impact Analysis

Requirement changes:
```text
warning threshold becomes configurable
```
List all affected:
```text
requirements
design
code
tests
docs
CLI
release notes
```

## Lab 26 — Release Checklist

Build a checklist containing:
```text
tests
security
config
docs
artifact
backup
migration
rollback
monitoring
support owner
```

## Lab 27 — Rollback Plan

Design a rollback plan for a CLI release that produces incorrect reports.
Include:
```text
detection
stop distribution
restore previous artifact
verify
communicate
```

## Lab 28 — CI Pipeline Design

Draw:
```text
commit
 ↓
format/lint
 ↓
unit tests
 ↓
integration tests
 ↓
security checks
 ↓
build artifact
```

## Lab 29 — Configuration Separation

Move thresholds and output path out of hardcoded business logic. Define how dev/test/prod configuration differs without changing source.

## Lab 30 — Secret Review

Search a sample project for patterns that should never be committed:
```text
passwords
tokens
private keys
database credentials
```
Write a remediation process including rotation.

## Lab 31 — Observability Design

Define:
```text
logs
metrics
error counts
processing duration
invalid-row count
version
```
for the CLI.

## Lab 32 — Runbook

Write a runbook for:
```text
CLI produces no report
```
with evidence-based troubleshooting steps.

## Lab 33 — Risk Register

Create at least 10 risks covering:
```text
requirements
data quality
performance
security
dependency
release
operations
maintenance
```
Assign likelihood, impact, mitigation, owner.

## Lab 34 — Documentation Review

Create a documentation map:
```text
README
requirements
architecture
test plan
runbook
release notes
ADR
risk register
```
For each state audience and purpose.

## Lab 35 — Capstone Engineering Package

Build the complete engineering package described below and perform a final review against requirements, architecture, tests, risks, release readiness, and operations.

# 6. Mini Project

## Mini Project — Engineering Package for a Production-Ready Server Health CLI

The main deliverable is **not lots of code**. It is the complete engineering system around a small product.

### Project Structure

```text
server-health-project/
├── README.md
├── requirements/
│   ├── problem-statement.md
│   ├── functional-requirements.md
│   ├── non-functional-requirements.md
│   └── traceability-matrix.md
├── architecture/
│   ├── context-diagram.md
│   ├── component-diagram.md
│   ├── data-flow.md
│   ├── sequence-diagram.md
│   └── adr/
│       ├── ADR-001-csv-library.md
│       └── ADR-002-project-structure.md
├── src/
│   ├── main.py
│   ├── health.py
│   ├── input_reader.py
│   └── reporter.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── test-plan.md
├── risk-register.md
├── release-checklist.md
├── rollback-plan.md
├── operations-runbook.md
└── CHANGELOG.md
```

### 1. Problem Statement

Explain:

```text
current manual process
affected users
business impact
desired outcome
success measures
```

### 2. Stakeholders

At minimum:

```text
Operations
Platform
Security
Application Owners
Management
```

### 3. Requirements

Create at least:

```text
12 functional requirements
10 non-functional requirements
8 acceptance-criteria scenarios
5 out-of-scope statements
5 assumptions
5 constraints
```

### 4. Traceability

Map:

```text
Requirement
 ↓
Architecture component
 ↓
Implementation
 ↓
Test
 ↓
Release evidence
```

### 5. Architecture

Required diagrams:

```text
Context
Component
Data flow
Sequence
Deployment
```

Suggested component architecture:

```text
CLI
 ↓
Input Reader
 ↓
Schema Validator
 ↓
Health Classifier
 ↓
Result Model
 ↓
Reporter
 ├→ Console
 └→ File
```

### 6. ADRs

At least two decisions with:

```text
Context
Decision
Alternatives
Consequences
```

### 7. Test Plan

Include:

```text
unit tests
integration tests
end-to-end tests
acceptance tests
boundary cases
negative cases
performance test
security-focused tests
```

### 8. Risk Register

At least 10 risks.

Example:

```text
Risk:
Malformed input causes full batch failure

Likelihood:
Medium

Impact:
High

Mitigation:
row-level validation and error isolation

Contingency:
preserve rejected rows and continue valid processing
```

### 9. Release Readiness

Checklist:

```text
requirements approved
tests passing
review complete
no secrets committed
configuration documented
artifact versioned
rollback available
runbook available
known risks accepted
release notes complete
```

### 10. Operations

Define:

```text
log format
metrics
error handling
support owner
known failure modes
troubleshooting steps
recovery
```

### 11. Change Scenario

After version 1 is complete, introduce:

```text
New requirement:
Thresholds must be configurable per environment.
```

Perform impact analysis and update:

```text
requirements
architecture
code design
tests
documentation
release plan
```

This exercise demonstrates that software engineering is primarily about **safe evolution**, not only initial implementation.

# 7. Recommended Resources

This Markdown is designed to be self-contained for Phase 1.

Optional deeper references:

```text
Google Engineering Practices
Google Code Review guidance
Pro Git
NASA Software Engineering Handbook
NASA software requirements guidance
official Python documentation for examples
```

Use external material to deepen process rigor, not to replace understanding of the lifecycle model in this file.

# 8. Certification Relevance

Software engineering fundamentals support virtually every later technical role.

## Backend / Cloud-Native

Directly relevant to:

```text
requirements
API contracts
architecture
testing
versioning
release compatibility
observability
maintenance
```

## DevOps / Platform Engineering

Directly relevant to:

```text
CI/CD
change control
artifact management
rollback
automation
runbooks
operational readiness
```

## Cybersecurity

Directly relevant to:

```text
security requirements
threat modeling
code review
dependency risk
secure defaults
change traceability
incident learning
```

## AI / Data Systems

Directly relevant to:

```text
requirements
data contracts
testing
reproducibility
deployment
monitoring
model/service lifecycle
```

# 9. Common Mistakes & Best Practices

- **Mistake:** Starting implementation before agreeing on the problem.  
  **Best practice:** Write a problem statement, stakeholders, scope, assumptions, and measurable outcomes first.
- **Mistake:** Writing vague requirements such as 'fast' or 'secure'.  
  **Best practice:** Make quality requirements measurable and verifiable.
- **Mistake:** Treating user stories as complete specifications.  
  **Best practice:** Add acceptance criteria, constraints, and non-functional requirements.
- **Mistake:** Designing architecture around favorite technologies.  
  **Best practice:** Start from requirements and quality attributes.
- **Mistake:** Creating diagrams with product logos but no responsibilities or flows.  
  **Best practice:** Show components, interfaces, data, trust boundaries, and failure paths.
- **Mistake:** Mixing parsing, business logic, and reporting in one function.  
  **Best practice:** Separate concerns and keep components cohesive.
- **Mistake:** Building abstractions for imagined future needs.  
  **Best practice:** Prefer simple designs until requirements justify complexity.
- **Mistake:** Treating testing as a final phase.  
  **Best practice:** Design tests alongside requirements and implementation.
- **Mistake:** Using only end-to-end tests.  
  **Best practice:** Balance fast unit tests with integration and selected E2E tests.
- **Mistake:** Measuring coverage instead of test quality.  
  **Best practice:** Focus on risks, boundaries, assertions, and requirements.
- **Mistake:** Writing bug reports that only say 'doesn't work'.  
  **Best practice:** Include reproducible steps, environment, expected/actual results, and evidence.
- **Mistake:** Fixing symptoms without root cause or regression test.  
  **Best practice:** Identify underlying cause and add a protective test.
- **Mistake:** Making giant mixed commits.  
  **Best practice:** Use small coherent changes.
- **Mistake:** Reviewing only syntax/style.  
  **Best practice:** Review correctness, design, tests, security, compatibility, and maintainability.
- **Mistake:** Committing secrets.  
  **Best practice:** Use secret-management mechanisms and rotate exposed credentials.
- **Mistake:** Deploying without rollback or forward-recovery planning.  
  **Best practice:** Define recovery before production change.
- **Mistake:** Changing schemas/interfaces without impact analysis.  
  **Best practice:** Identify consumers, tests, data, docs, and compatibility.
- **Mistake:** Operating without logs/metrics/runbooks.  
  **Best practice:** Design observability and support procedures before release.
- **Mistake:** Treating documentation as a one-time artifact.  
  **Best practice:** Update docs with the system.
- **Mistake:** Ignoring maintenance and deprecation.  
  **Best practice:** Plan lifecycle beyond the first release.

# 10. Self-Assessment Questions (with short answers)

1. **Programming vs software engineering?**  
   Programming implements code; software engineering covers the full lifecycle, quality, collaboration, operations, and evolution.

2. **What is a stakeholder?**  
   Anyone affected by or able to influence the system.

3. **What is a problem statement?**  
   Clear description of current problem, affected users, impact, and desired outcome.

4. **Functional requirement?**  
   Behavior the system must provide.

5. **Non-functional requirement?**  
   Quality attribute or constraint such as performance, security, or availability.

6. **Why must requirements be testable?**  
   So objective evidence can show whether they are satisfied.

7. **What is acceptance criteria?**  
   Observable conditions defining acceptable behavior.

8. **What does Given-When-Then represent?**  
   Context, action/event, and expected outcome.

9. **What is scope?**  
   Boundary of what the project includes.

10. **What is an assumption?**  
   Belief used for design/planning that may need validation.

11. **What is a constraint?**  
   Fixed limitation restricting solution choices.

12. **Requirements traceability?**  
   Linking requirements to design, implementation, tests, and release evidence.

13. **What is SDLC?**  
   Activities from discovery/requirements through design, build, test, release, operation, and maintenance.

14. **Waterfall?**  
   Primarily sequential lifecycle model.

15. **Iterative?**  
   Repeatedly refine the solution through feedback.

16. **Incremental?**  
   Deliver the product in usable slices.

17. **What does agile emphasize?**  
   Short feedback cycles, working increments, collaboration, prioritization, adaptation.

18. **What is a user story?**  
   Short user-centered statement of desired value.

19. **What is a backlog?**  
   Prioritized collection of work items.

20. **Definition of Done?**  
   Shared criteria that must be true before work is considered complete.

21. **What is software architecture?**  
   Major components, responsibilities, interfaces, dependencies, data flow, and significant decisions.

22. **Separation of concerns?**  
   Keep unrelated responsibilities in different components.

23. **Cohesion?**  
   How closely related responsibilities inside a component are.

24. **Coupling?**  
   Degree of dependency among components.

25. **Interface?**  
   Defined interaction surface between components.

26. **Contract?**  
   Inputs, outputs, errors, preconditions, and guarantees of an interaction.

27. **Precondition?**  
   Condition that must hold before an operation.

28. **Postcondition?**  
   Condition guaranteed after successful operation.

29. **What is an ADR?**  
   Record of an important architecture decision, alternatives, and consequences.

30. **What is a quality attribute?**  
   Measurable property such as reliability, security, performance, or maintainability.

31. **What is a trade-off?**  
   Improving one goal may increase cost/complexity or reduce another quality.

32. **YAGNI?**  
   Avoid speculative functionality not currently required.

33. **KISS?**  
   Prefer the simplest design satisfying requirements.

34. **DRY?**  
   Avoid duplicated authoritative knowledge/logic.

35. **What is refactoring?**  
   Changing internal structure without intentionally changing external behavior.

36. **Technical debt?**  
   Future cost caused by shortcuts or accumulated design/maintenance problems.

37. **Verification vs validation?**  
   Verification checks specification compliance; validation checks whether the right problem is solved.

38. **Unit test?**  
   Test of a small isolated unit.

39. **Integration test?**  
   Test of components working together.

40. **E2E test?**  
   Test of a complete user workflow.

41. **Acceptance test?**  
   Test demonstrating agreed user/business behavior.

42. **Regression test?**  
   Test preventing previously fixed behavior from breaking again.

43. **Boundary test?**  
   Test at and around decision boundaries.

44. **Negative test?**  
   Test invalid or failure conditions.

45. **Why not make every test E2E?**  
   E2E tests are slower, more fragile, and harder to diagnose.

46. **What makes a useful defect report?**  
   Repro steps, environment, expected/actual, evidence, impact.

47. **Severity vs priority?**  
   Severity is impact; priority is chosen urgency.

48. **What is root cause?**  
   Underlying condition that produced the failure.

49. **What is version control?**  
   System that records and manages source changes over time.

50. **What is a commit?**  
   Recorded coherent source change/snapshot.

51. **Why small commits?**  
   They are easier to review, understand, revert, and trace.

52. **What is code review for?**  
   Evaluate correctness, design, tests, security, complexity, and maintainability.

53. **What is change control?**  
   Managed process for assessing, approving, deploying, verifying, and recovering changes.

54. **What is impact analysis?**  
   Identify everything affected by a proposed change.

55. **What is CI?**  
   Automated frequent integration with build/test checks.

56. **Continuous Delivery?**  
   Keeping software releasable through automated verification/delivery processes.

57. **Deployment vs release?**  
   Deployment installs a version; release makes capability available to users.

58. **Rollback?**  
   Restore a previous known-good state.

59. **Why separate configuration from code?**  
   Same artifact can run safely in different environments.

60. **What is operational readiness?**  
   Ability to run, observe, support, recover, and troubleshoot software.

61. **What is a runbook?**  
   Documented operational procedure for diagnosis/recovery.

62. **What is a risk register?**  
   Tracked list of risks with likelihood, impact, mitigation, ownership, and status.

63. **Final engineering principle?**  
   Build software so it can be understood, verified, released, operated, recovered, and changed safely over time.

