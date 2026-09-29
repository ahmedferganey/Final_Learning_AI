# Learning strategy and AI-assisted engineering

> **Priority:** Continuous from Week 1 · **Study window:** 1–12 · **Approximate focused time:** Integrated (overlaps with weekly plan)

## Why it is universal

Learn without outsourcing understanding; use AI for explanation, alternatives and carefully bounded implementation.

## Detailed table of contents / concepts to cover

- [ ] How software is built: requirements → design → implementation → verification → operation
- [ ] The independent / pair-programming / delegated-task learning modes
- [ ] AI context: repository map, conventions, acceptance criteria, constraints and examples
- [ ] The limits of autocomplete and agents: plausible mistakes, stale context and insecure suggestions
- [ ] Prompt injection, confidential-data handling, approval before risky tool operations
- [ ] Diff inspection, reproducibility, evidence from tests, and explicit stop conditions
- [ ] Keep a learning journal that records what you can explain without AI

## How to learn it

1. Before an exercise, state inputs, outputs and edge cases in your own words.
2. Attempt the core task manually; ask AI for hints and comparisons after an honest attempt.
3. For delegated changes, provide a scoped task and tests; inspect the full diff and run the tests yourself.
4. Explain one piece of generated code from memory and alter it without asking AI.

## Required exercise

Give an AI assistant an intentionally ambiguous feature request. Write a clearer requirement and test plan first, compare two proposed implementations, and reject at least one unsupported assumption.

## Independent exit criteria

- [ ] Can explain a generated function line by line.
- [ ] Can identify and reproduce one mistake from an AI answer.
- [ ] Never commits secrets or approves commands that are not understood.

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

- [MIT Missing Semester](https://missing.csail.mit.edu/2026/)
- [Google Code Review Guide](https://google.github.io/eng-practices/review/reviewer/)
- [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)

[← Back to the master roadmap](../README.md)
