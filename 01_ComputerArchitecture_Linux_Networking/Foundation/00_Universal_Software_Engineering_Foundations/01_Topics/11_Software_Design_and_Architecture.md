# Software design, architecture and maintainability

> **Priority:** Core overview · **Study window:** 9 · **Approximate focused time:** 9–12 (overlaps with weekly plan)

## Why it is universal

Design should be reviewable and evolve as requirements change, not copied from whichever framework AI chooses.

## Detailed table of contents / concepts to cover

- [ ] Separation of concerns and high cohesion / low coupling
- [ ] Modules, interfaces, dependency direction and composition
- [ ] Functional core / imperative shell as a useful pattern
- [ ] Basic SOLID ideas without dogmatic pattern memorization
- [ ] Architecture decisions and tradeoffs; monolith vs. service awareness
- [ ] Nonfunctional requirements and operational constraints
- [ ] Backward compatibility and documenting design decisions

## How to learn it

1. Sketch components and data flows before implementing a feature.
2. Create two designs for the same small requirement and identify tradeoffs.
3. Refactor a single oversized script into domain, storage and interface boundaries.

## Required exercise

Design the capstone as CLI/UI layer → application logic → repository/storage; write one short architecture decision record.

## Independent exit criteria

- [ ] Can identify one unnecessary abstraction and remove it.
- [ ] Can explain dependencies between modules.
- [ ] Can change storage implementation without rewriting core business rules.

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

- [Google Code Review Guide](https://google.github.io/eng-practices/review/reviewer/)

[← Back to the master roadmap](../README.md)
