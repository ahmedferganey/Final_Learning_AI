# Feature Specification: Repository Foundation

**Feature Branch**: `001-repository-foundation`
**Created**: 2026-04-09
**Status**: Draft
**Phase**: 0 — Foundation
**Plan Reference**: Plan.md → Spec 0.1

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — New Engineer Onboards Without Help (Priority: P1)

A new engineer joins the GymOS project. They clone the repository and — by reading only the
README — understand the project purpose, the technology stack, the directory layout, and how to
set up their local environment. They can navigate to the correct directory for the code they need
to work on without asking anyone.

**Why this priority**: Every subsequent spec depends on engineers being able to work in a
consistent, documented structure. Without this, onboarding time increases and inconsistencies
compound across the codebase.

**Independent Test**: Can be fully tested by cloning the repository to a fresh machine, reading
only the README, and answering: "What is GymOS?", "Where does backend code live?", "Where do
specs go?", "What branch strategy do we use?" — all four questions must be answerable from
documentation alone.

**Acceptance Scenarios**:

1. **Given** a fresh `git clone` of the repository, **When** an engineer reads `README.md`,
   **Then** they can identify the project purpose, all three client surfaces (web, mobile, backend),
   the technology stack, and the top-level directory structure.

2. **Given** the repository is cloned, **When** an engineer looks for where to create a new
   feature branch, **Then** `CONTRIBUTING.md` tells them the exact branch naming convention
   (`feature/<spec-id>-<short-name>`) and links to the commit message standard.

3. **Given** the repository is cloned, **When** an engineer wants to submit a PR, **Then**
   the `.github/pull_request_template.md` prompts them for: what changed, why, how to test,
   and the spec link — without any training.

---

### User Story 2 — Architecture Decisions Are Traceable (Priority: P2)

A team member questions why GymOS uses a modular monolith instead of microservices. Rather
than needing to reconstruct the reasoning from memory or Slack history, they read the ADR
and understand the decision, the alternatives considered, and the conditions under which
the decision should be revisited.

**Why this priority**: Without ADRs, architectural decisions are re-litigated repeatedly.
The modular-monolith and stack-selection decisions are foundational — they constrain every
subsequent spec. They must be documented before Phase 1 begins.

**Independent Test**: Can be fully tested by reading `docs/decisions/001-modular-monolith.md`
and verifying it contains: the decision, the alternatives considered, the rationale, and the
conditions for revisiting.

**Acceptance Scenarios**:

1. **Given** the ADR file exists, **When** an engineer reads it, **Then** they understand
   why microservices were rejected for GymOS at this stage and what conditions would trigger
   revisiting the decision.

2. **Given** the ADR template exists at `docs/decisions/adr-template.md`, **When** a future
   engineer needs to document a new architecture decision, **Then** the template provides
   sections for: title, status, context, decision, consequences, and alternatives considered.

3. **Given** two ADRs exist (monolith, stack selection), **When** they are read in sequence,
   **Then** there is no contradiction between the decisions documented.

---

### User Story 3 — Commit History Is Consistent From Day One (Priority: P3)

Every commit in the GymOS repository follows the Conventional Commits standard. An engineer
can read the git log and immediately understand what type of change each commit represents
(`feat`, `fix`, `docs`, `refactor`, `test`, `chore`) and which scope it belongs to
(`auth`, `training`, `coaching`, `web`, `mobile`, etc.).

**Why this priority**: Consistent commit messages enable automated changelogs, clear code
review context, and disciplined scope tracking across all future phases. Establishing the
standard before any code exists means it never has to be retrofitted.

**Independent Test**: Can be fully tested by verifying the commit convention is documented
in `CONTRIBUTING.md` with examples and enforced by a `commitlint` configuration (or equivalent
documentation of the standard).

**Acceptance Scenarios**:

1. **Given** the `CONTRIBUTING.md` exists, **When** an engineer reads the commit section,
   **Then** they find the exact format, permitted types, permitted scopes, and at least two
   examples of valid commit messages.

2. **Given** the convention is documented, **When** an engineer writes `feat(auth): add JWT
   login endpoint`, **Then** this is a valid commit message under the documented standard.

3. **Given** the convention is documented, **When** an engineer writes `updated stuff`,
   **Then** this is identifiably invalid against the documented standard.

---

### Edge Cases

- **Monorepo tooling (Turborepo, Nx):** MUST NOT be added at this stage. The constitution
  prohibits adding complexity without evidence of need. The repo is a standard Git monorepo
  with a `Makefile` — no workspace tooling.
- **`.gitignore` coverage:** The root `.gitignore` MUST cover all three stacks (Python
  `__pycache__`, `*.pyc`; Node `node_modules`, `.next`; Flutter `.dart_tool`, `build/`).
  Missing ignores from any stack cause noise in `git status`.
- **Conflicting ADR decisions:** If any two ADRs reach contradictory conclusions, both must
  be revisited before proceeding. ADRs are reviewed as a pair before this spec is marked done.
- **Empty directories in Git:** Git does not track empty directories. Each top-level directory
  (`backend/`, `web/`, `mobile/`, `infra/`, `docs/`, `specs/`) MUST contain at least a
  `.gitkeep` or an initial file so the structure is present after cloning.
- **ADR numbering collision:** ADR files use zero-padded sequential numbers (`001-`, `002-`).
  If two people create an ADR simultaneously, the second must be renumbered. This risk is
  documented in `CONTRIBUTING.md`.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The repository MUST contain the following top-level directories, each committed:
  `backend/`, `web/`, `mobile/`, `infra/`, `docs/`, `specs/`.
- **FR-002**: `README.md` MUST describe: project purpose, all three client surfaces, the full
  technology stack, and the directory layout — sufficient for a new engineer to orient
  themselves without assistance.
- **FR-003**: `CONTRIBUTING.md` MUST document: the branch naming strategy, the Conventional
  Commits standard with examples, the PR review process, and the ADR creation process.
- **FR-004**: `.github/pull_request_template.md` MUST prompt for: what changed, why it changed,
  how to test it, and the linked spec ID.
- **FR-005**: `docs/decisions/adr-template.md` MUST exist with sections: title, status, date,
  context, decision, consequences, alternatives considered.
- **FR-006**: `docs/decisions/001-modular-monolith.md` MUST be written and follow the ADR
  template, documenting the decision to use a modular monolith over microservices.
- **FR-007**: `docs/decisions/002-stack-selection.md` MUST be written and follow the ADR
  template, documenting the rationale for FastAPI, Next.js, Flutter, PostgreSQL, and Redis.
- **FR-008**: The root `.gitignore` MUST suppress artefacts from all three stacks: Python,
  Node.js, and Flutter/Dart.
- **FR-009**: The repository MUST NOT contain any application code, Docker configuration,
  or CI pipeline in this spec — those are delivered by Specs 0.2–0.5.
- **FR-010**: The repository MUST NOT have any secrets, API keys, or credentials committed.
  Enforcement: a CI pipeline job runs `detect-secrets scan` on every PR and fails the check if
  any findings exist. `CONTRIBUTING.md` additionally documents the pre-commit hook for local
  fast-feedback.

### Key Entities

- **ADR (Architecture Decision Record)**: A Markdown document capturing an architecture decision.
  Attributes: title, status (`proposed` / `accepted` / `superseded`), date, context, decision,
  consequences, alternatives considered. ADRs are immutable once accepted; superseded ADRs are
  updated to `status: superseded` and linked to the replacement.
- **Directory structure**: The canonical layout agreed upon in Plan.md, committed as the first
  meaningful commit to the repository. Serves as the contract for where all future code lives.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A developer with no prior GymOS knowledge can correctly identify the directory
  where backend authentication code will live, the directory where mobile workout screens will
  live, and the directory where Phase 1 specs will be stored — by reading only `README.md` and
  `CONTRIBUTING.md`. Target: 100% success rate across any reviewer who tests this.
- **SC-002**: Both ADRs (`001-modular-monolith`, `002-stack-selection`) are reviewed and
  accepted (status: `accepted`) before Phase 1 begins. Acceptance is defined as: the PR
  introducing each ADR file receives at least 1 GitHub PR approving review from a team member
  other than the author.
- **SC-003**: `git clone` of the repository produces the full directory structure with no
  missing top-level directories. Verified by: `ls` output matching the expected layout.
- **SC-004**: A PR created against this repository automatically displays the PR template,
  prompting all four required fields. Verified by opening a test PR.
- **SC-005**: Zero secrets or credentials are present in the repository at merge time.
  Verified by: `detect-secrets scan` returning no findings in the CI pipeline job that runs
  on every PR (automated gate, not manual verification).

---

## Assumptions

- The repository already exists as a Git repository (confirmed: `git status` shows existing
  repo on `main` branch).
- **GitHub is the canonical hosting platform.** The `.github/` directory structure, PR templates,
  and branch protection rules are GitHub-specific. Migration to another platform would require
  revisiting FR-003 and FR-004.
- No CI infrastructure exists yet — this spec produces only the repo structure and documentation.
  Docker Compose and GitHub Actions are delivered by Spec 0.5.
- The Conventional Commits standard is adopted as-is without project-specific modifications.
- ADRs will be stored as Markdown files under `docs/decisions/`, not in an external tool
  (Confluence, Notion, etc.).
- Monorepo tooling (Turborepo, Nx, Bazel) will NOT be adopted until a specific performance
  or team-isolation problem justifies it, as per the constitution's YAGNI principle.
- `detect-secrets` runs as a CI pipeline gate on every PR (auto-enforced). It is additionally
  documented as a pre-commit hook in `CONTRIBUTING.md` for local fast-feedback; hook installation
  remains a developer responsibility.

---

## Clarifications

### Session 2026-04-09

- Q: How should SC-005 (zero secrets at merge time) be enforced and verified? → A: CI pipeline runs `detect-secrets scan` on every PR and fails the check if findings exist (automated gate).
- Q: What constitutes a valid ADR approval for SC-002? → A: 1 GitHub PR approving review from a team member other than the author, on the PR introducing the ADR file.
- Q: What is the canonical Git hosting platform? → A: GitHub (`.github/` paths, PR templates, and branch protection are GitHub-specific).
