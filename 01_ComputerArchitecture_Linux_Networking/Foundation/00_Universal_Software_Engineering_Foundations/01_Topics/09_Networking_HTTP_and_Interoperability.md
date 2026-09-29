# Networking, HTTP and interoperability

> **Priority:** Core overview · **Study window:** 7 · **Approximate focused time:** 10–12 (overlaps with weekly plan)

## Why it is universal

Even non-web systems depend on networked services, protocols, security boundaries and communication failures.

## Detailed table of contents / concepts to cover

- [ ] IP, DNS, ports, TCP vs. UDP and TLS intuition
- [ ] Client-server interactions, request/response, statelessness
- [ ] URL, HTTP methods, headers and common status codes
- [ ] JSON, serialization and schema/version compatibility
- [ ] Timeout, retry, backoff and idempotency concepts
- [ ] Authentication vs. authorization: introduction
- [ ] Consuming APIs safely and interpreting errors

## How to learn it

1. Explain the path from typing a URL to receiving a response.
2. Call a public test endpoint and inspect status, headers and JSON.
3. Induce timeout, invalid request and unavailable-service conditions.

## Required exercise

Write a small client for a sample HTTP service with input validation, explicit timeout and appropriate error handling.

## Independent exit criteria

- [ ] Can interpret 200, 201, 400, 401, 403, 404, 429 and 500.
- [ ] Can distinguish DNS, connection, TLS and application failures conceptually.
- [ ] Can explain when a retry might cause duplicate effects.

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

- [MDN How the Web Works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)
- [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)

[← Back to the master roadmap](../README.md)
