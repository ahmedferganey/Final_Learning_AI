# Implementation Plan: Repository Foundation

**Branch**: `001-repository-foundation` | **Date**: 2026-04-09 | **Spec**: [spec.md](spec.md)
**Input**: `specs/phase-0-foundation/001-repository-foundation/spec.md`

## Summary

Establish the GymOS monorepo skeleton: top-level directory structure, README, CONTRIBUTING guide,
GitHub PR template, ADR template, and two founding ADRs (modular monolith, stack selection).
No application code, Docker configuration, or CI pipeline is delivered in this spec.
Secret scanning is enforced via a CI `detect-secrets` gate on every PR (clarified 2026-04-09).

## Technical Context

**Language/Version**: N/A — documentation and repository structure only
**Primary Dependencies**: N/A
**Storage**: N/A
**Testing**: Manual acceptance verification (README readability, `git clone` structure check,
`detect-secrets scan`, PR template inspection, ADR review)
**Target Platform**: GitHub-hosted Git repository
**Project Type**: Repository scaffold / documentation
**Performance Goals**: N/A
**Constraints**: MUST NOT contain application code, Docker config, or CI pipeline (delivered by
Specs 0.2–0.5). `.gitignore` MUST suppress artefacts for Python, Node.js, and Flutter/Dart.
**Scale/Scope**: Single monorepo, initial commit only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Applies | Status | Notes |
|---|---|---|---|
| I. Backend Intelligence Supremacy | No | N/A | No application code in this spec |
| II. Coaching Engine Versioning | No | N/A | No coaching code in this spec |
| III. Modular Monolith | Partial | PASS | FR-009 prohibits app code here; structure is correct |
| IV. Spec-First Delivery | Yes | PASS | Spec exists with 5 testable acceptance criteria |
| V. Test-First Discipline | Partial | PASS | Acceptance verification is manual; appropriate for a doc-only spec |
| VI. API-First Design | No | N/A | No API endpoints in this spec |
| VII. Row-Level Security | No | N/A | No data access in this spec |
| VIII. Offline Continuity | No | N/A | No mobile code in this spec |
| IX. Security by Default | Yes | PASS | FR-010 / SC-005: CI detect-secrets gate defined (clarified 2026-04-09) |
| X. Observability | No | N/A | No service code in this spec |

**Constitution result**: No violations. All applicable principles pass. Safe to proceed.

## Project Structure

### Documentation (this feature)

```text
specs/phase-0-foundation/001-repository-foundation/
├── plan.md          # This file
├── research.md      # Phase 0 output
├── data-model.md    # Phase 1 output
├── quickstart.md    # Phase 1 output
└── tasks.md         # Phase 2 output (created by /speckit-tasks)
```

### Deliverables (repository root)

```text
gymos/
├── .gitignore                           # FR-008: Python + Node.js + Flutter/Dart
├── .secrets.baseline                    # detect-secrets baseline (FR-010)
├── .github/
│   └── pull_request_template.md        # FR-004: what/why/how/spec-link
├── README.md                            # FR-002: purpose, surfaces, stack, layout
├── CONTRIBUTING.md                      # FR-003: branches, commits, PR process, ADR process
├── backend/
│   └── .gitkeep                         # FR-001: directory must exist after clone
├── web/
│   └── .gitkeep
├── mobile/
│   └── .gitkeep
├── infra/
│   └── .gitkeep
├── docs/
│   └── decisions/
│       ├── adr-template.md             # FR-005
│       ├── 001-modular-monolith.md     # FR-006
│       └── 002-stack-selection.md      # FR-007
└── specs/
    └── (phase-0-foundation already present)
```

**Structure Decision**: Documentation scaffold only — no `src/` application tree. All deliverables
are Markdown and config files. The `specs/` directory already contains this spec.

## Complexity Tracking

> No constitution violations. This section is not required.
