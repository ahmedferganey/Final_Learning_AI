# Data Model: Repository Foundation

**Date**: 2026-04-09
**Plan**: [plan.md](plan.md)

This spec contains no database entities. The artefacts tracked here are documentation
files versioned in Git, not rows in a database.

---

## Document Entity: ADR (Architecture Decision Record)

Stored as a Markdown file under `docs/decisions/NNN-short-kebab-name.md`.

| Field | Type | Required | Constraints |
|---|---|---|---|
| title | string | Yes | Sentence case; describes the decision, not the outcome |
| status | enum | Yes | `proposed` \| `accepted` \| `superseded` |
| date | ISO 8601 date | Yes | Set at file creation; immutable thereafter |
| context | text | Yes | Forces, constraints, and background driving the decision |
| decision | text | Yes | The chosen approach, stated decisively |
| consequences | text | Yes | Positive and negative impacts of the decision |
| alternatives_considered | text | Yes | At least one rejected alternative with brief rationale |
| superseded_by | string (filename) | Conditional | Required only when `status = superseded`; links to replacement ADR |

**Naming convention**: `docs/decisions/NNN-short-kebab-name.md`
- `NNN`: zero-padded sequential integer starting at `001`
- Assigned at file creation; immutable
- Collision risk (two engineers create simultaneously): second ADR must be renumbered;
  documented in `CONTRIBUTING.md`

**Lifecycle state machine**:

```
proposed ──► accepted ──► superseded
```

- `proposed`: ADR written; PR opened for review
- `accepted`: PR received ≥ 1 GitHub approving review from a team member other than the author; merged to `main`
- `superseded`: A replacement ADR was accepted; `superseded_by` field added; file is retained (never deleted)

**Immutability rules**:
- `decision` and `consequences` sections are immutable once status is `accepted`
- Only `status` and `superseded_by` fields may change post-acceptance
- If two ADRs reach contradictory conclusions, both revert to `proposed` and are re-reviewed

---

## Directory Structure Contract

The committed top-level layout is a structural contract binding all future specs.

| Directory | Purpose | Managed by Spec |
|---|---|---|
| `backend/` | FastAPI application code | 0.2 Backend Scaffold |
| `web/` | Next.js application code | 0.3 Web Scaffold |
| `mobile/` | Flutter application code | 0.4 Mobile Scaffold |
| `infra/` | Docker, CI, infrastructure config | 0.5 Local Dev & CI Foundation |
| `docs/decisions/` | Architecture Decision Records | **0.1 (this spec)** |
| `specs/` | Spec Kit feature specifications | Spec Kit tooling |

**Initial content rule**: Each top-level directory MUST contain at least a `.gitkeep` file
at the time of the first commit so the structure survives a fresh `git clone` (FR-001).

---

## No External Interfaces

This spec exposes no APIs, CLIs, events, or inter-process protocols. The `contracts/`
directory is not created for this spec.
