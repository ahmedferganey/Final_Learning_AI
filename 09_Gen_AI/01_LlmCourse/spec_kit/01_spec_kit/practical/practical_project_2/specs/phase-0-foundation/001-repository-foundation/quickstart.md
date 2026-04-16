# Quickstart: Repository Foundation

**Date**: 2026-04-09
**Plan**: [plan.md](plan.md)

## Prerequisites

- Git installed locally
- GitHub account with write access to the GymOS repository
- `detect-secrets` installed (local verification only): `pip install detect-secrets`

---

## Implementation Order

Complete these steps in sequence. Each step maps to one or more functional requirements.

| Step | Action | FR |
|---|---|---|
| 1 | Initialize `.gitignore` with Python + Node + Flutter/Dart entries | FR-008 |
| 2 | Create `backend/`, `web/`, `mobile/`, `infra/`, `docs/decisions/`, `specs/` with `.gitkeep` | FR-001 |
| 3 | Write `README.md` (purpose, surfaces, stack, layout) | FR-002 |
| 4 | Write `CONTRIBUTING.md` (branches, commits, PR process, ADR process, detect-secrets hook) | FR-003, FR-010 |
| 5 | Write `.github/pull_request_template.md` (what/why/how/spec-link) | FR-004 |
| 6 | Write `docs/decisions/adr-template.md` | FR-005 |
| 7 | Write `docs/decisions/001-modular-monolith.md` (status: proposed) | FR-006 |
| 8 | Write `docs/decisions/002-stack-selection.md` (status: proposed) | FR-007 |
| 9 | Initialize `.secrets.baseline` and commit it | FR-010, SC-005 |
| 10 | Open PRs for ADRs; obtain ≥ 1 approving review each; set status to `accepted` | SC-002 |
| 11 | Verify all acceptance criteria (SC-001 through SC-005) | — |

> **Note**: Steps 7–8 each require a GitHub PR with ≥ 1 approving review before the ADR
> status advances to `accepted`. Factor review time into scheduling.

---

## Verification (Acceptance Criteria)

### SC-001 — New engineer orientates from README alone

```bash
git clone <repo-url> gymos-verify
cd gymos-verify
# Read README.md only. Answer without other sources:
# Q1: What is GymOS?
# Q2: Where does backend auth code live?       → backend/
# Q3: Where do mobile workout screens go?      → mobile/
# Q4: Where do Phase 1 specs live?             → specs/phase-1-auth-users/
```

**Pass**: All four questions answerable from `README.md` and `CONTRIBUTING.md` alone.

---

### SC-002 — ADR approval

```bash
grep "^status:" docs/decisions/001-modular-monolith.md
grep "^status:" docs/decisions/002-stack-selection.md
# Expected: "status: accepted" for both files
```

Plus: verify each ADR was merged via a GitHub PR with ≥ 1 approving review (check PR history).

---

### SC-003 — Directory structure present after clone

```bash
git clone <repo-url> gymos-clean
ls gymos-clean/
# Expected directories: backend  web  mobile  infra  docs  specs
# Expected files: README.md  CONTRIBUTING.md  .gitignore  .secrets.baseline
```

---

### SC-004 — PR template auto-populates

Open a new PR against `main` in the GitHub web UI. The PR description MUST auto-populate
with the template prompting: what changed / why / how to test / spec link.

---

### SC-005 — Zero secrets (CI gate + local verification)

```bash
# Local verification:
pip install detect-secrets
detect-secrets scan --baseline .secrets.baseline
# Expected: exits 0, no unacknowledged findings

# CI gate: GitHub Actions runs the same scan on every PR automatically (Spec 0.5)
```

---

## detect-secrets Baseline Initialization (one-time)

```bash
pip install detect-secrets
# Run from repo root on a clean state (no real secrets present):
detect-secrets scan > .secrets.baseline
git add .secrets.baseline
git commit -m "chore: initialize detect-secrets baseline"
```

If a false positive is reported later, acknowledge it:
```bash
detect-secrets audit .secrets.baseline
# Mark false positives interactively, then commit the updated baseline
```
