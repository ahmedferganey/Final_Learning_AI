# Operating systems, processes and concurrency

> **Priority:** Core overview · **Study window:** 6 · **Approximate focused time:** 8–10 (overlaps with weekly plan)

## Why it is universal

Threads, processes, memory and resource limits affect backend, AI, embedded, desktop and infrastructure work.

## Detailed table of contents / concepts to cover

- [ ] Program vs. process vs. thread
- [ ] CPU, memory, stack and heap conceptual models
- [ ] Filesystem operations, permissions and failure cases
- [ ] I/O-bound vs. CPU-bound tasks and scheduling intuition
- [ ] Race conditions, shared state, locks and deadlocks: introductions
- [ ] Synchronous vs. asynchronous operations and when each is useful

## How to learn it

1. Draw a program execution diagram and track mutable state.
2. Compare a sequential and a concurrent toy example; verify correctness first.
3. Use process monitoring and logs to investigate one slow or stuck script.

## Required exercise

Process several local files sequentially; introduce parallel work only after stating what shared state exists and what ordering guarantees are required.

## Independent exit criteria

- [ ] Can describe when a process, thread or async task is appropriate at a high level.
- [ ] Can identify a possible data race in shared mutable state.
- [ ] Can explain why extra concurrency does not always improve performance.

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

[← Back to the master roadmap](../README.md)
