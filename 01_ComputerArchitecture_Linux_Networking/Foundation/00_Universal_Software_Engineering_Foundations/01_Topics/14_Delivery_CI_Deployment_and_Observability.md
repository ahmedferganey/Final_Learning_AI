# Delivery, CI, deployment and observability

> **Priority:** Core overview · **Study window:** 11 · **Approximate focused time:** 9–12 (overlaps with weekly plan)

## Why it is universal

Software is valuable when it runs predictably and can be inspected, maintained and recovered.

## Detailed table of contents / concepts to cover

- [ ] Reproducible environment and pinned/recorded dependencies
- [ ] Package/install/run instructions and build artifacts
- [ ] Continuous integration: run tests and static checks per change
- [ ] Development, test and production configurations
- [ ] Containers: image vs. container, Dockerfile and port mapping at introductory level
- [ ] Structured logs, health checks and basic metrics
- [ ] Safe deployment, backups and rollback awareness

## How to learn it

1. Set up local one-command test execution.
2. Configure a basic CI pipeline to run unit tests on each push or pull request.
3. Package the capstone for another machine; Docker is an optional extension if time permits.

## Required exercise

Create a GitHub Actions workflow for tests and document a clean install + test procedure; optionally containerize.

## Independent exit criteria

- [ ] Can explain why code passing locally can fail elsewhere.
- [ ] Can inspect a failed CI run and reproduce the failure.
- [ ] Can locate a failure using logs without printing credentials.

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

- [GitHub Actions](https://docs.github.com/en/actions/tutorials)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [MIT Missing Semester](https://missing.csail.mit.edu/2026/)

[← Back to the master roadmap](../README.md)
