# Universal Software Engineering Foundations — 12-Week Learning System

> **Purpose:** One reusable foundations folder for *any* future software specialization (frontend, backend, full-stack, mobile, data, AI/ML, DevOps, cybersecurity, robotics or embedded software). No track decision is required during these three months. Focus on concepts that transfer across languages, frameworks and tools while learning to collaborate with AI without losing independent engineering judgment.
>
> **Length:** 12 weeks (approximately 3 months). **Planning baseline:** ~15 focused hours/week (~180 hours). **Output:** a public-safe portfolio project, tested fundamentals, a documented learning record and an informed next-track shortlist. This is an introduction and applied proficiency target, **not mastery** of every subject.

## Table of contents

- [1. What this folder is for](#1-what-this-folder-is-for)
- [2. Recommended folder structure](#2-recommended-folder-structure)
- [3. Rules of the learning system](#3-rules-of-the-learning-system)
- [4. Foundation topics and depth](#4-foundation-topics-and-depth)
- [5. Twelve-week curriculum](#5-twelve-week-curriculum)
- [6. Exactly how to study each topic](#6-exactly-how-to-study-each-topic)
- [7. Practice projects and checkpoints](#7-practice-projects-and-checkpoints)
- [8. AI-assisted learning protocol](#8-ai-assisted-learning-protocol)
- [9. Skills you should *not* prioritize yet](#9-skills-you-should-not-prioritize-yet)
- [10. Week-12 readiness assessment](#10-week-12-readiness-assessment)
- [11. Choosing a track after the foundations](#11-choosing-a-track-after-the-foundations)
- [12. Curated official learning resources](#12-curated-official-learning-resources)
- [13. Time management and progress tracker](#13-time-management-and-progress-tracker)
- [14. Scope and limitations](#14-scope-and-limitations)

---

## 1. What this folder is for

Modern AI tools can draft code, suggest tests, interpret logs and sometimes operate development tools. These capabilities make **problem definition, computer science, independent verification, secure tool use and architectural reasoning** even more important. The aim is not to memorize API methods or outsource every exercise; it is to understand what a system must do, produce a working solution and know when the solution is wrong.

**Common across most software tracks:** problem decomposition, programming, data structures, Git, debugging and tests, command line, operating-system basics, network basics, SQL/data representation, modular design, security thinking, documentation and delivery. Depth varies by future track. This plan teaches a transferable overview and one integrated project rather than deep specialization.

**Teaching-language recommendation:** Python for examples because of readable syntax and broad applicability, **not** because every future developer must use Python. If you already know JavaScript/TypeScript, Java or C# well, reuse it. Learn **one** main language during the 12 weeks. SQL and shell are additional tools, not competing main languages.

**Prior experience:** If you can already demonstrate a skill by passing that topic's exit test, reduce its hours and invest the freed time in weaknesses. Do not skip understanding just because a tool can produce an answer.

## 2. Recommended folder structure

```text
00_Universal_Software_Engineering_Foundations/
├── README.md                          ← This master roadmap / table of contents
├── 01_Topics/                        ← Fifteen focused topic guides
│   ├── 01_Learning_Strategy_and_AI_Assisted_Engineering.md
│   ├── 02_Problem_Solving_and_Requirements.md
│   ├── 03_Programming_Fundamentals.md
│   ├── 04_Data_Structures_and_Algorithms.md
│   ├── 05_Git_and_Collaboration.md
│   ├── 06_Shell_Linux_and_Toolchain.md
│   ├── 07_Debugging_Testing_and_Quality.md
│   ├── 08_Operating_Systems_and_Concurrency.md
│   ├── 09_Networking_HTTP_and_Interoperability.md
│   ├── 10_Data_Modeling_SQL_and_Persistence.md
│   ├── 11_Software_Design_and_Architecture.md
│   ├── 12_Security_Privacy_and_Threat_Modeling.md
│   ├── 13_APIs_Integration_and_Contracts.md
│   ├── 14_Delivery_CI_Deployment_and_Observability.md
│   └── 15_Communication_Documentation_and_Product_Thinking.md
├── 02_Weekly_Plans/                  ← 12 weekly execution sheets
├── 03_Practice/                      ← Problem-solving, coding and debugging log
├── 04_Capstone/                      ← One reusable, track-neutral final project
└── 05_Tracking/                      ← Weekly reflection + readiness checklist
```

The individual topic files are intended to accumulate detailed notes, diagrams, exercises and corrections as you learn. Keep specialization-specific subjects **outside** this folder (e.g., advanced React, ROS 2 internals, CUDA optimization, Kubernetes administration).

## 3. Rules of the learning system

1. **One main language and one continuously improved project.** Build gradually rather than restarting in a different framework each week.
2. **Every major topic ends in evidence.** Notes alone are insufficient; produce a working exercise, reproducible experiment, test or design artifact.
3. **Manual first for core concepts.** After a genuine attempt, use AI to explain alternatives, identify edge cases or review your work.
4. **AI-generated code must be reviewed.** Inspect changed files and run tests; understand critical lines, dependencies and tool commands.
5. **Work from specifications.** Define inputs, outputs, edge cases, constraints and acceptance criteria before medium-sized tasks.
6. **Favor official docs and a single primary course.** Reference materials are not a requirement to finish several full courses concurrently.
7. **Track actual capability.** Progress means you can explain, modify, debug and test a concept on a fresh problem, not simply recognize a video.

**Weekly 15-hour template:** 3 hours concepts/documentation; 7 hours independent building and exercises; 2 hours testing/debugging; 2 hours AI-assisted comparison/review; 1 hour notes and self-assessment. Spread across 5–6 days and adjust as needed.

## 4. Foundation topics and depth

Priority definitions: **Core** = practice independently; **Core overview** = understand and apply in a small example, specialize later; **Continuous** = practice each week. Hours for overlapping and continuous topics are not additive to the overall 180-hour plan.

| # | Topic | Priority | Main study window | Evidence / exit target | Deep-dive guide |
|---|---|---|---|---|---|
| 01 | Learning strategy and AI-assisted engineering | Continuous from Week 1 | 1–12 | Can explain a generated function line by line. | [Open](01_Topics/01_Learning_Strategy_and_AI_Assisted_Engineering.md) |
| 02 | Problem solving, computational thinking and requirements | Core | 1–2, then every week | Can decompose an ambiguous feature into small tasks. | [Open](01_Topics/02_Problem_Solving_and_Requirements.md) |
| 03 | Programming fundamentals with one transferable language | Core | 2–3 | Can create functions and modules without autocomplete. | [Open](01_Topics/03_Programming_Fundamentals.md) |
| 04 | Data structures, algorithms and complexity | Core | 4 | Can choose a basic data structure for a requirement. | [Open](01_Topics/04_Data_Structures_and_Algorithms.md) |
| 05 | Git, collaboration and code review | Core | 1 and 5 | Can restore a file without losing unrelated edits. | [Open](01_Topics/05_Git_and_Collaboration.md) |
| 06 | Shell, operating environment and developer tools | Core | 1 and 6 | Can navigate a repository and search code from the terminal. | [Open](01_Topics/06_Shell_Linux_and_Toolchain.md) |
| 07 | Debugging, testing, static analysis and quality | Core | 3 and 5, then every week | Can explain what a failing test demonstrates and what it cannot demonstrate. | [Open](01_Topics/07_Debugging_Testing_and_Quality.md) |
| 08 | Operating systems, processes and concurrency | Core overview | 6 | Can describe when a process, thread or async task is appropriate at a high level. | [Open](01_Topics/08_Operating_Systems_and_Concurrency.md) |
| 09 | Networking, HTTP and interoperability | Core overview | 7 | Can interpret 200, 201, 400, 401, 403, 404, 429 and 500. | [Open](01_Topics/09_Networking_HTTP_and_Interoperability.md) |
| 10 | Data modeling, SQL and persistence | Core | 8 | Can design a simple relational schema from user requirements. | [Open](01_Topics/10_Data_Modeling_SQL_and_Persistence.md) |
| 11 | Software design, architecture and maintainability | Core overview | 9 | Can identify one unnecessary abstraction and remove it. | [Open](01_Topics/11_Software_Design_and_Architecture.md) |
| 12 | Security, privacy and threat modeling | Core awareness | 9 and 11 | Can distinguish authentication from authorization. | [Open](01_Topics/12_Security_Privacy_and_Threat_Modeling.md) |
| 13 | APIs, integration and interface contracts | Core overview | 7 and 10 | Can document an API another developer could consume. | [Open](01_Topics/13_APIs_Integration_and_Contracts.md) |
| 14 | Delivery, CI, deployment and observability | Core overview | 11 | Can explain why code passing locally can fail elsewhere. | [Open](01_Topics/14_Delivery_CI_Deployment_and_Observability.md) |
| 15 | Documentation, collaboration and product thinking | Core throughout | 1–12 | Can explain the project to a new developer in five minutes. | [Open](01_Topics/15_Communication_Documentation_and_Product_Thinking.md) |

**Ordering note:** Topics are not fifteen sequential courses. AI literacy, documentation and testing run throughout; programming and tools come early; systems, data and architecture follow; the capstone integrates all of them.

## 5. Twelve-week curriculum

**Three phases:** Month 1 = reasoning, programming and algorithms; Month 2 = software quality and system/data basics; Month 3 = architecture, security, integration and delivery.

| Week | Main focus | Topic files | Weekly deliverable | Independent checkpoint |
|---|---|---|---|---|
| 1 | Environment, Git and computational thinking | 01, 02, 05, 06, 15 | Initialized repository; 3 small pseudocode problems; 1 requirements document; first meaningful commits. | Without AI, navigate repo, stage/commit a change and turn a vague request into 5 acceptance criteria. |
| 2 | Programming I: values, decisions and functions | 02, 03, 01 | 10 small exercises and a mini calculator/validator with at least 6 tests. | Explain every line and solve one new control-flow task without generated code. |
| 3 | Programming II: modules, files and debugging | 03, 07, 01 | CLI project v1 with JSON persistence, validation, README and tests. | Reproduce and fix a seeded bug; explain exception handling and mutations. |
| 4 | Data structures, algorithms and complexity | 04, 02, 03 | 8 DSA exercises, 1 benchmark, short complexity explanations. | Choose data structures for 3 scenarios and justify runtime and memory tradeoffs. |
| 5 | Testing, quality, Git branches and reviews | 07, 05, 15 | CLI project v2; >=12 meaningful tests; reviewed pull request; issue log of 3 defects. | Discover a defect independently, demonstrate failing test and merged correction. |
| 6 | Linux, operating systems and concurrency overview | 06, 08 | Shell test runner; process/log investigation; short concurrency failure note. | Distinguish CPU vs. I/O bottlenecks and explain one race-condition scenario. |
| 7 | Networks, HTTP and contract basics | 09, 13 | HTTP client with timeout, JSON parsing, validation and error handling; API contract draft. | Interpret five HTTP failures and explain retry/idempotency risk. |
| 8 | Relational data, SQL and storage | 10, 03 | SQLite schema with 3 related tables; >=10 handwritten queries; transaction test. | Write and explain a JOIN, constraint failure and parameterized query without AI. |
| 9 | Architecture, requirements and secure design | 11, 12, 02, 15 | Capstone spec, component diagram, ADR, 4 documented threats and mitigations. | Explain why the architecture is adequate, not merely fashionable. |
| 10 | Build an integrated capstone | 03, 07, 10, 11, 13 | Capstone v1: usable workflow, validation, persistence, meaningful errors and test suite. | Complete one requested feature solo, review one delegated feature and compare behavior to specification. |
| 11 | Security, CI and packaging | 12, 14, 05, 07 | CI passing; clean-setup documentation; tests for invalid inputs; optional container. | Demonstrate fresh setup, CI failure diagnosis and no secrets in repository. |
| 12 | Integration, review and track exploration | 01–15, 04_Capstone | Capstone release, test report, design notes, 3 track-taste exercises and next-step decision worksheet. | Demo from a fresh environment and explain tradeoffs without reading AI-generated prose. |

**Detailed daily sequencing is in [`02_Weekly_Plans/`](02_Weekly_Plans/).** Do not attempt to achieve specialist-level depth in each weekly topic.

## 6. Exactly how to study each topic

Use this repeatable **six-step protocol** for any foundation topic:

1. **Define the learning goal (15–30 minutes).** Read the topic guide. Write the three most important things you must be able to *do*, and how you will prove them.
2. **Learn just enough theory.** Read the linked official resource or a relevant segment of CS50 / MIT Missing Semester. Make brief notes in your own words and one small diagram if useful. Stop passive consumption after ~20–30% of the allocated time.
3. **Reproduce a minimal example unaided.** Type, execute and modify it in your own development environment. Predict the output before running it.
4. **Complete a transfer exercise.** Apply the idea to a slightly different task. Use reference documentation; if you get stuck, ask AI for a hint or conceptual explanation before asking for full code.
5. **Break it and verify it.** Test valid, invalid and boundary inputs. Inspect errors, run the debugger, compare competing implementations, review the Git diff and record any AI errors.
6. **Pass the exit check and teach it back.** Explain the concept without looking at a generated explanation. Commit the working exercise and record your evidence link in the tracker.

**Topic note template:** `Goal` → `Concept map` → `Examples` → `Mistakes and misconceptions` → `Exercise` → `Tests / evidence` → `Unresolved questions` → `Next revisit date`.

**Spaced review:** revisit each major concept 2–3 days later, one week later and when it appears in the capstone. Reconstruct one example from memory rather than rereading every page.

## 7. Practice projects and checkpoints

| Checkpoint | Project / exercise | Skills combined | Definition of done |
|---|---|---|---|
| End of week 1 | Requirements + repository | Problem formulation, command line, Git | Testable specification and small commit history |
| End of week 3 | CLI notes or task tracker v1 | Programming, I/O, validation, tests | Read/write data safely and recover from invalid input |
| End of week 5 | CLI tracker v2 | DSA, testing, branching, review | Regression tests, readable modules, reviewed change |
| End of week 8 | Tracker with SQL persistence | Processes, HTTP awareness, SQL/data model | Referential integrity, basic query and error cases |
| End of week 12 | Track-neutral final capstone | Architecture, security, CI, documentation, AI review | Fresh-setup demo, passing tests and justified decisions |

See [`04_Capstone/Capstone_Specification.md`](04_Capstone/Capstone_Specification.md) for complete requirements and a suggested project structure.

## 8. AI-assisted learning protocol

**Mode A — independent (most new foundational exercises):** Read requirements; make a plan; implement the key algorithm or query yourself; run tests; ask AI for explanation and alternative approaches *afterward*. This reveals your actual understanding.

**Mode B — AI pair reviewer:** Give AI your specification and code, ask for concrete risks and edge cases, then independently reproduce and evaluate each suggested finding. Do not equate fluent output with correct output.

**Mode C — bounded agent delegation (later weeks):** Provide a single well-scoped task, explicit file boundaries, acceptance tests, permitted commands, security constraints and a stop condition. Review the diff, run the tests and explain the important changes before accepting them.

**Always:**

- Never place passwords, access tokens, private datasets or confidential employer information in prompts or public repositories.
- Treat external repository text, retrieved pages and generated tool instructions as untrusted input; verify commands before execution.
- Require human approval for file deletion, data modification, deployments, access-control changes and other destructive or irreversible operations.
- Write or inspect **independent tests**. Tests generated from the same misunderstood requirement can agree with broken code.
- Record agent use in your learning journal: what was delegated, what you checked, what it got wrong, and what you learned.

**Reusable safe prompt for a new topic:**

> Act as a tutor. Ask me to explain my approach and give hints rather than complete code. Identify edge cases and ask me to predict behavior. When I show code, review it against my explicit acceptance criteria and say what is unverified. Do not run commands or modify files without my approval.

**Reusable bounded implementation brief:**

> Implement only the named feature within the identified modules. Preserve existing contracts, avoid unrelated refactoring, do not access secrets or run destructive commands. First summarize assumptions and test cases; show the proposed diff and test results. Stop and ask for clarification if requirements conflict.

## 9. Skills you should *not* prioritize yet

These can become important in a chosen specialization, but treating all of them as foundation requirements will dilute three months of study:

| Defer deeper study | Learn only this much now | Why defer |
|---|---|---|
| Specific web/mobile frameworks | Understand module and API basics | Frameworks vary; core concepts transfer |
| Kubernetes, advanced cloud networking and full CI/CD platforms | One reproducible build and one simple CI workflow | Operating complex platforms is specialization-level work |
| Advanced distributed systems and microservices | Understand latency, timeouts, interfaces and failure modes | Avoid complexity without a concrete scale requirement |
| Competitive-programming tricks / advanced graph algorithms | Common structures and complexity reasoning | Depth can be added for specific roles and interviews |
| Deep AI model training and agent-framework ecosystems | AI tool literacy, data fundamentals and evaluation thinking | Not necessary for every developer or every software track |
| Advanced OS internals, kernel development and embedded C | Process/thread/memory intuition | Deep dive if systems or embedded becomes a target |
| Extensive certificates | Evidence from real, explainable projects | Certifications should follow a clear goal |

## 10. Week-12 readiness assessment

**Core exit tests — demonstrate without relying on generated implementation:**

- [ ] Convert an unclear request into scope, pseudocode, 5+ acceptance criteria and edge cases.
- [ ] Write and debug a small multi-module program in my chosen language.
- [ ] Choose an appropriate list/map/set and explain simple Big-O tradeoffs.
- [ ] Create, branch, merge, review and if needed recover changes using Git.
- [ ] Use shell tools to inspect files, processes, errors and environment configuration.
- [ ] Write unit and integration tests and reproduce one regression from a failing test.
- [ ] Explain process/thread basics, DNS → connection → HTTP flow and common error classes.
- [ ] Design a relational model, write JOIN queries and use parameterized SQL.
- [ ] Explain interface/core/storage boundaries and document one design tradeoff.
- [ ] Identify untrusted input, enforce validation and explain least privilege.
- [ ] Publish a clean-start project with CI, a README, test evidence and no secrets.
- [ ] Review an AI-generated patch, identify limitations and justify acceptance or rejection.

**Self-check rule:** If a category fails, allocate 1–2 extra weeks for targeted practice. Do **not** interpret the calendar alone as evidence of readiness.

## 11. Choosing a track after the foundations

After week 12, make three **small, comparable experiments**. The aim is to discover what you enjoy and where you want to invest, not to claim competence in all tracks:

| Track family | 3–6-hour taste-test task | Reused foundations |
|---|---|---|
| Web/backend | Expose a read-only endpoint for the capstone | APIs, SQL, tests, architecture |
| Frontend/mobile | Build a tiny interface consuming an existing sample API | State, HTTP, validation, usability |
| Data/AI | Analyze task records and build an evaluated baseline predictor or simple retrieval demo | Python, SQL, experiments, data integrity |
| DevOps/platform | Add CI, containerize and run a clean-environment diagnostic | Shell, Git, processes, security, observability |
| Cybersecurity | Threat-model and test an intentionally vulnerable *local* practice app | Networking, trust boundaries, input validation |
| Robotics/embedded | Simulate sensor readings, implement a state machine and log abnormal conditions | Control flow, concurrency, interfaces, testing |

Record for each experiment: interest, frustration, required math/domain depth, preferred work style, and whether you want to pursue deeper study. Choose a subsequent 3–6-month specialty plan **after** these experiments or whenever you have sufficient evidence.

## 12. Curated official learning resources

Use **CS50x as an optional primary broad course**, selectively rather than attempting every lecture plus every other resource in twelve weeks. Use MIT Missing Semester for developer tools, and official docs as topical references.

| Resource | Best use | Link |
|---|---|---|
| CS50x | Programming, abstraction and algorithms | [CS50x](https://cs50.harvard.edu/x/) |
| Python Tutorial | Reference for language fundamentals | [Python Tutorial](https://docs.python.org/3/tutorial/index.html) |
| MIT Missing Semester | Shell, Git, debugging and agentic coding | [MIT Missing Semester](https://missing.csail.mit.edu/2026/) |
| Pro Git | Version control | [Pro Git](https://git-scm.com/book/en/v2) |
| pytest | Python testing | [pytest](https://docs.pytest.org/en/stable/getting-started.html) |
| MDN How the Web Works | Browser/network model | [MDN How the Web Works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) |
| MDN HTTP | Protocol and API basics | [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) |
| PostgreSQL SQL Tutorial | Relational and SQL learning | [PostgreSQL SQL Tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html) |
| OWASP Top 10 (2025) | Application-security awareness | [OWASP Top 10 (2025)](https://top10.owasp.org/2025/) |
| OWASP Top 10 for LLM Applications (2025) | AI-specific risk awareness | [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) |
| Google Code Review Guide | Review process and code quality | [Google Code Review Guide](https://google.github.io/eng-practices/review/reviewer/) |
| GitHub Actions | CI workflows | [GitHub Actions](https://docs.github.com/en/actions/tutorials) |
| Docker Get Started | Optional basic packaging | [Docker Get Started](https://docs.docker.com/get-started/) |

## 13. Time management and progress tracker

**Baseline (15 h/week, 180 total):** ~20% learning concepts, 47% independent implementation, 13% debugging/testing, 13% AI-assisted comparison/review and 7% reflection. Treat the split as an adjustable guideline, not a strict measurement. At 8 hours/week, prioritize required topics and extend the schedule; at 20+ hours, add practice, tests and review rather than racing to extra frameworks.

- **Daily:** Work on a specific exit criterion; commit useful progress; record one mistake and its fix.
- **Weekly:** Demo something working, evaluate exit checks, write a short retrospective and adjust next week's practice.
- **Monthly:** Review one end-to-end project and one independent assessment. If core programming or debugging is weak, reinforce it before progressing.
- **Track evidence:** Keep links to code, tests, ADRs, screenshots of terminal output and a concise statement of independent vs. delegated work.

Open [`05_Tracking/Weekly_Progress_Template.md`](05_Tracking/Weekly_Progress_Template.md) and copy it once per week.

## 14. Scope and limitations

- These subjects are **widely transferable**, not equally important at equal depth in every job. For example, a robotics developer may need much more real-time systems knowledge, while a frontend developer may need more accessibility and browser fundamentals.
- Twelve weeks provide a broad foundation and one credible learning project; substantial job readiness usually requires further specialization and practice.
- Basic mathematical reasoning is used throughout. A math-heavy track (AI research, graphics, robotics, optimization) will later require a dedicated mathematics module: algebra, linear algebra, probability/statistics, calculus and/or control theory as appropriate.
- AI tools evolve quickly. Evaluate tools by your ability to verify outputs, maintain security and achieve project goals rather than by a single product's feature list.

**Maintaining this folder:** Revise your own examples and notes when tools change. Keep permanent concept explanations separate from version-specific installation commands and framework tutorials.
