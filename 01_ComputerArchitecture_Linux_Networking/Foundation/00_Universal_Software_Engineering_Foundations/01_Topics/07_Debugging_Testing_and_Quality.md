# Debugging, testing, static analysis and quality

> **Priority:** Core · **Study window:** 3 and 5, then every week · **Approximate focused time:** 16–20 (overlaps with weekly plan)

## Why it is universal

Generating code is easy; independently proving requirements and diagnosing failures is a major engineering responsibility.

## Detailed table of contents / concepts to cover

- [ ] Bug reproduction, minimal failing examples and causal hypotheses
- [ ] Breakpoints, stack traces, logs, assertions and debugger state
- [ ] Unit, integration, end-to-end and regression testing: purpose and limitations
- [ ] Test design: normal, boundary, error, property-based thinking
- [ ] Test doubles, fixture setup and deterministic tests
- [ ] Formatters, linters, static type checks and dependency review
- [ ] Code review for logic, complexity, maintainability, security and tests

## How to learn it

1. Write at least one failing test before fixing an introduced defect.
2. Reduce a bug to the smallest reproducible input.
3. Use pytest for isolated units; keep an explicit manual test checklist for user workflows.
4. Review independently derived acceptance criteria rather than treating generated tests as authoritative.

## Required exercise

Seed five defects (boundary, exception, data loss, complexity, missing validation) into the CLI app; reproduce and fix them with regression tests.

## Independent exit criteria

- [ ] Can explain what a failing test demonstrates and what it cannot demonstrate.
- [ ] Can debug an unexpected result without asking AI for the fix first.
- [ ] Can perform a focused review of a small PR.

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

- [pytest](https://docs.pytest.org/en/stable/getting-started.html)
- [Google Code Review Guide](https://google.github.io/eng-practices/review/reviewer/)
- [MIT Missing Semester](https://missing.csail.mit.edu/2026/)

[← Back to the master roadmap](../README.md)
