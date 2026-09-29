# Software Architecture — Four-Week Lesson Checklist

**Goal:** Learn architecture fundamentals that are useful across software tracks, before specializing.

**Course A:** [Software Architecture and Clean Code Design in OOP — Andrii Piatakha](https://www.udemy.com/course/software-architecture-learnit/)  
**Course B:** [Software Architecture & Design of Modern Large Scale Systems — Michael Pogrebinsky](https://www.udemy.com/course/software-architecture-design-of-modern-large-scale-systems/)

**Curriculum checked:** 28 September 2026. These are selected lessons from the official public Udemy outlines, not a requirement to finish every lesson in both courses. Where a video covers many patterns, focus on the specifically named patterns for this foundation phase. Watch relevant quizzes for reinforcement, even when individual quizzes are not listed below.

## Week 1 — Clean Code and SOLID (Course A)

*Objective: understand maintainability and use design principles to refactor existing code.*

### Section: SOLID Principles
- [ ] **A** — SOLID principles overview & Single Responsibility Principle (7:28)
- [ ] **A** — Open / Closed Principle (7:28)
- [ ] **A** — Liskov Substitution Principle (5:08)
- [ ] **A** — Interface Segregation Principle (4:47)
- [ ] **A** — Dependency Inversion Principle (5:51)
- [ ] **A** — Quiz: SOLID Principles - Check yourself

### Section: PRACTICE — Coding exercises to practice SOLID principles
- [ ] **A** — Single Responsibility Principle: User Registration and Authentication Refactoring Exercise
- [ ] **A** — Open / Closed Principle: Shape Refactoring Challenge
- [ ] **A** — Liskov Substitution Principle: Square and Rectangle Refactoring Challenge
- [ ] **A** — Interface Segregation Principle: Worker Refactoring Challenge
- [ ] **A** — Dependency Inversion Principle: Car-Engine Refactoring Challenge

### Section: Object-oriented Architecture, Clean Code Design (Advanced)
- [ ] **A** — Clean Code Architecture, Coupling & Cohesion (22:10)
- [ ] **A** — Tell, Don’t Ask Pricniple & Data Structures (20:18)
- [ ] **A** — Law of Demeter (8:52)
- [ ] **A** — KISS Principle in OOP (26:21)
- [ ] **A** — YAGNI Principle in OOP (24:43)
- [ ] **A** — DRY Principle in OOP | Part 1 (18:32)
- [ ] **A** — DRY Principle in OOP | Part 2 - Practice (11:51)

### Week 1 deliverable
- [ ] Refactor a small application, separate responsibilities, and add dependency injection for one external dependency.
- [ ] Write one paragraph explaining how the refactor changes coupling and cohesion.

## Week 2 — Design Patterns and Application Architecture (Course A)

*Objective: recognize common design problems and implement maintainable application structure.*

### Section: Object-oriented Architecture, Clean Code Design (Advanced)
- [ ] **A** — Packaging Pricniples p.1: Cohesion Principles (21:29)
- [ ] **A** — Packaging Pricniples p.2: Coupling Principles and Others (24:55)

### Section: GRASP Principles in OOP — selected essentials
- [ ] **A** — Introduction to GRASP (17:46)
- [ ] **A** — Information Expert (20:11)
- [ ] **A** — Creator (24:43)
- [ ] **A** — Controller (27:12)
- [ ] **A** — Low Coupling (26:39)
- [ ] **A** — High Cohesion (27:29)
- [ ] **A** — Polymorphism (27:05)
- [ ] **A** — Protected Variations (25:32)

### Section: GoF Design Patterns of Software Architecture in OOP
- [ ] **A** — GoF Patterns: Overview (13:56)
- [ ] **A** — Creational Patterns (30:39) — focus on Factory Method and Builder
- [ ] **A** — Structural Patterns, p.1 (31:07) — focus on Adapter and Façade
- [ ] **A** — Behevioral Patterns, p.1 (33:58) — focus on Strategy
- [ ] **A** — Behevioral Patterns, p.2 (31:50) — focus on Observer

### Section: Web Application Design Patterns
- [ ] **A** — DAO (Data Access Object) Design Pattern (19:29)
- [ ] **A** — MVC Design Pattern (15:47)
- [ ] **A** — Layered Architecture (25:58)

### Section: TDD, BDD & ATTD
- [ ] **A** — Test-driven development: Theory (23:55)
- [ ] **A** — TDD, BDD & ATTD - Practice (13:51)

### Week 2 deliverable
- [ ] Implement a small application with presentation/API, business logic, and data access layers.
- [ ] Apply Factory Method or Builder, Adapter, and Strategy where justified, and write automated tests.
- [ ] Explain why each chosen pattern is needed, and which simpler alternative you considered.

## Week 3 — System Architecture and Scalability (Course B)

*Objective: move from code-level decisions to system-level requirements, interfaces, and infrastructure building blocks.*

### Section: Introduction
- [ ] **B** — Introduction to Software Architecture (10:30)
- [ ] **B** — Download the Course Workbook (1:56)

### Section: System Requirements & Architectural Drivers
- [ ] **B** — Introduction to System Design & Architectural Drivers (9:49)
- [ ] **B** — Feature Requirements - Step by Step Process (8:03)
- [ ] **B** — System Quality Attributes Requirements (9:14)
- [ ] **B** — System Constraints in Software Architecture (10:11)

### Section: Most Important Quality Attributes in Large Scale Systems
- [ ] **B** — Performance (12:44)
- [ ] **B** — Scalability (14:14)
- [ ] **B** — Availability - Introduction & Measurement (9:10)
- [ ] **B** — Fault Tolerance & High Availability (10:01)
- [ ] **B** — SLA, SLO, SLI (10:04)

### Section: API Design
- [ ] **B** — Introduction to API Design for Software Architects (12:12)
- [ ] **B** — RPC (10:59)
- [ ] **B** — REST API (16:17)

### Section: Large Scale Systems Architectural Building Blocks
- [ ] **B** — DNS, Load Balancing & GSLB (15:10)
- [ ] **B** — Message Brokers (10:21)
- [ ] **B** — API Gateway (13:18)
- [ ] **B** — Content Delivery Network - CDN (13:15)

### Week 3 deliverable
- [ ] Define actors, use cases, user flows, key functional requirements, and measurable quality attributes for your application.
- [ ] Sketch a high-level component diagram and define example REST endpoints.
- [ ] Document one scalability trade-off and one failure-recovery strategy.

## Week 4 — Data, Architectural Styles and System Design (Course B)

*Objective: connect storage and communication choices to complete system designs.*

### Section: Data Storage at Global Scale
- [ ] **B** — Relational Databases & ACID Transactions (14:37)
- [ ] **B** — Non-Relational Databases (10:09)
- [ ] **B** — Techniques to Improve Performance, Availability & Scalability Of Databases (11:57)
- [ ] **B** — Brewer’s (CAP) Theorem (11:59)
- [ ] **B** — Scalable Unstructured Data Storage (15:17)

### Section: Software Architecture Patterns and Styles
- [ ] **B** — Introduction to Software Architecture Patterns & Styles (5:07)
- [ ] **B** — Multi-Tier Architecture (12:50)
- [ ] **B** — Microservices Architecture (12:32)
- [ ] **B** — Event Driven Architecture (16:47)

### Section: Software Architecture & System Design Practice
- [ ] **B** — Design a Highly Scalable Discussion Forum 1 - Requirements & API (13:39)
- [ ] **B** — Design a Highly Scalable Discussion Forum 2 - Functional Architecture Diagram (10:39)
- [ ] **B** — Design a Highly Scalable Discussion Forum 3 - Final Software Architecture (12:35)
- [ ] **B** — Design an E-Commerce Marketplace Platform 1 - Requirements & Sequence Diagram (13:46)
- [ ] **B** — Design an E-Commerce Marketplace Platform 2 - Functional Diagram (15:26)
- [ ] **B** — Design an E-Commerce Marketplace Platform 3 - Final Software Architecture (8:53)

### Week 4 deliverable
- [ ] Independently design the forum or marketplace *before* watching the solution lessons.
- [ ] Produce a requirements document, sequence diagram, component architecture, API outline, and data-storage choices.
- [ ] Write a short architecture decision record (ADR) explaining at least three trade-offs.

## Optional follow-up after the four weeks

These are in the same two courses, but you need not study them to complete this foundation sprint.

### Course A — more application-design depth
- [ ] Pure Fabrication
- [ ] Indirection
- [ ] How GRASP Patterns Interact
- [ ] GRASP in Architecture Layers
- [ ] GRASP vs SOLID vs GoF
- [ ] Behevioral Patterns, p.3
- [ ] BDD & ATTD
- [ ] Database Modelling & Design: Conceptual, Logical and Physical Data Models
- [ ] Database Normalization & Denormalization
- [ ] Event Driven Architecture Fundamentals
- [ ] Delivery Guarantees and Failure Reality
- [ ] Consistency Models and Business Transactions
- [ ] The Outbox Pattern and Reliable Publishing

### Course B — more large-scale data depth
- [ ] Introduction to Event-Stream Processing and Tumbling Window Strategy
- [ ] Hopping Window Event-Stream Processing Strategy
- [ ] Sliding Window Event-Stream Processing Strategy
- [ ] Session Window Event-Stream Processing Strategy
- [ ] Time in Stream Processing and Handling Late Arrival of Events
- [ ] Introduction to Big Data
- [ ] Big Data Processing Strategies
- [ ] Lambda Architecture

## Final competency checklist
- [ ] I can explain what makes code maintainable and demonstrate SOLID with refactoring.
- [ ] I can distinguish coupling from cohesion and organize components around responsibilities.
- [ ] I can justify design-pattern choices rather than inserting them unnecessarily.
- [ ] I can separate application layers and write tests against interfaces.
- [ ] I can turn product requirements into measurable system quality attributes.
- [ ] I can compare RPC and REST and explain when asynchronous messaging is useful.
- [ ] I can reason about performance, availability, scalability and basic fault tolerance.
- [ ] I can explain basic database storage, replication, sharding, and consistency trade-offs.
- [ ] I can compare multi-tier, microservices, and event-driven architectures without assuming one is universally superior.
- [ ] I can document an architecture with diagrams and an ADR, and critically review AI-generated alternatives.

## Sources
- [Course A: Udemy public curriculum](https://www.udemy.com/course/software-architecture-learnit/)
- [Course B: Udemy public curriculum](https://www.udemy.com/course/software-architecture-design-of-modern-large-scale-systems/)
