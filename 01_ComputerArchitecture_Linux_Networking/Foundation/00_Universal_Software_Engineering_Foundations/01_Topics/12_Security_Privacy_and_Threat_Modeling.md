# Security, privacy and threat modeling

> **Priority:** Core awareness · **Study window:** 9 and 11 · **Approximate focused time:** 8–10 (overlaps with weekly plan)

## Why it is universal

Every developer creates trust boundaries; AI tools also introduce risky commands, data leakage and tool abuse.

## Detailed table of contents / concepts to cover

- [ ] Assets, threats, trust boundaries and attacker-controlled input
- [ ] Authentication, authorization and least privilege
- [ ] Validation, safe error handling and parameterized SQL
- [ ] Secrets, .env files, logging hygiene and dependency vulnerabilities
- [ ] TLS, hashing and encryption: correct-purpose overview
- [ ] OWASP web-application risk awareness
- [ ] AI-specific prompt injection, untrusted retrieved content and excessive tool permission

## How to learn it

1. Draw a data-flow diagram and label untrusted inputs.
2. Prove two failure cases: invalid input and unauthorized operation.
3. Run a secret scan or manually inspect repository history in a disposable practice repo.
4. Require human approval before destructive agent commands or deployments.

## Required exercise

Threat-model your task tracker: data theft, unauthorized deletion, injection and leaking a token. Implement two mitigations and test them.

## Independent exit criteria

- [ ] Can distinguish authentication from authorization.
- [ ] Can identify a secret-leaking or SQL-injection pattern.
- [ ] Can define a clear agent permission boundary.

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

- [OWASP Top 10 (2025)](https://top10.owasp.org/2025/)
- [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)

[← Back to the master roadmap](../README.md)
