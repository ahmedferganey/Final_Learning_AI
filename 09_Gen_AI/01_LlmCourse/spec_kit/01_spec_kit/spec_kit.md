# 🌱 GitHub Spec Kit — Complete Learning Roadmap
## Mastering Spec-Driven Development (SDD) with AI Coding Agents

> **Who this is for:** A Linux (Ubuntu/Debian) developer with Cursor IDE installed who knows basic git and terminal commands and wants to move from "vibe coding" to structured, AI-assisted development.

---

## 📋 Table of Contents

1. [Prerequisites & Foundational Knowledge](#1-prerequisites--foundational-knowledge)
2. [Core Concepts — Spec-Driven Development](#2-core-concepts--spec-driven-development)
3. [Installation & Setup](#3-installation--setup)
4. [The 5 Core Slash Commands (Deep Dive)](#4-the-5-core-slash-commands-deep-dive)
5. [Optional But Important Commands](#5-optional-but-important-commands)
6. [Project Artifacts & File Structure](#6-project-artifacts--file-structure)
7. [Advanced Topics](#7-advanced-topics)
8. [Practical Workflows](#8-practical-workflows)
9. [Troubleshooting & Debugging](#9-troubleshooting--debugging)
10. [Community & Ecosystem](#10-community--ecosystem)
11. [Hands-On Practice Project](#11-hands-on-practice-project)
12. [Learning Progress Tracker](#12-learning-progress-tracker)

---

## 1. Prerequisites & Foundational Knowledge

Before diving into Spec Kit, make sure you're comfortable with the following areas. These aren't blockers — you can learn them in parallel — but having them solid will make the SDD workflow feel natural.

### 1.1 Git Basics

Spec Kit is tightly integrated with Git. Every feature lives on its own branch, and the toolkit auto-detects your current branch name to determine the active feature context.

| Concept | Why You Need It |
|---------|----------------|
| Branching (`git checkout -b`) | Each Spec Kit feature gets its own branch |
| Commits | Spec artifacts are version-controlled |
| Pull Requests | SDD workflow ends with a PR |
| `git status` / `git log` | Inspecting artifact changes |
| Merging & rebasing | Keeping feature branches up to date |

**Minimum to know:**
```bash
# Create and switch to a feature branch
git checkout -b 001-user-auth

# Stage and commit spec artifacts
git add specs/
git commit -m "feat: add user auth spec and plan"

# Push and open a PR
git push origin 001-user-auth
```

### 1.2 Command Line Proficiency (Linux/Terminal)

Spec Kit's CLI (`specify`) is a terminal-first tool. You need to be comfortable with:

- Navigating directories (`cd`, `ls`, `pwd`)
- Setting environment variables (`export VAR=value`)
- Running scripts and CLIs
- Reading error output and using `--help` flags
- Pipe operators and output redirection

### 1.3 YAML & Markdown

Spec Kit stores all artifacts as **Markdown files**. You don't write YAML directly, but understanding Markdown formatting is essential because:

- All specs, plans, and tasks are `.md` files
- You read, edit, and reason about these files constantly
- The quality of your markdown input directly affects AI output quality

**Key Markdown elements:**
```markdown
# Heading 1
## Heading 2

- Bullet list
- [ ] Checkbox / task list

**Bold**, *italic*, `inline code`

```code block```

| Column 1 | Column 2 |
|----------|----------|
| Value    | Value    |
```

### 1.4 Familiarity with AI Coding Agents

Spec Kit works with many agents. For this roadmap, we focus on **Cursor IDE** with the `cursor-agent` flag. You should understand:

- How to open the chat/compose panel in Cursor
- How slash commands work in Cursor (type `/` to trigger)
- The concept of "agent mode" vs. "chat mode"
- How agents read files from your workspace
- Context windows and why they matter

**Supported agents (as of 2026):**

| Agent | Flag | Notes |
|-------|------|-------|
| Cursor | `cursor-agent` | Recommended for this roadmap |
| Claude Code | `claude` | Full slash command support |
| GitHub Copilot | `copilot` | Native VS Code integration |
| Gemini CLI | `gemini` | Google's CLI agent |
| OpenAI Codex | `codex` | Limited — no custom slash command args |
| Windsurf | `windsurf` | |
| Qwen Code | `qwen` | |

### 1.5 Python Package Management with `uv`

The `specify` CLI is a Python tool managed via `uv` — a fast, modern Python package manager.

```bash
# Install uv on Ubuntu/Debian
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify
uv --version

# One-time usage (no persistent install)
uvx --from git+https://github.com/github/spec-kit.git specify init my-project

# Persistent global install (recommended)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify specify is available
specify --version
```

> [!NOTE]
> `uvx` runs a tool once without installing it globally. `uv tool install` installs it persistently so you can call `specify` from anywhere. For regular use, the persistent install is strongly recommended.

---

## 2. Core Concepts — Spec-Driven Development

### 2.1 What Is SDD vs. Traditional Development?

Traditional development treats **code as the source of truth**. Specifications are written (if at all), used briefly, and then discarded. The code diverges from the docs almost immediately.

**Spec-Driven Development flips this model:**

| Aspect | Traditional | Spec-Driven |
|--------|-------------|-------------|
| Source of truth | The code | The specification |
| When spec is written | After (or never) | Before coding begins |
| Role of AI agent | "Write me some code" | "Execute this specification" |
| Prompt style | One-shot, vague | Multi-step, structured |
| Course correction | Refactor code | Update spec → regenerate |
| Documentation drift | Common | Prevented by design |

### 2.2 "Specifications as Executable" Philosophy

In SDD, a spec is not a static document. It is the **single source of truth** that:

- Drives the technical plan
- Generates the task breakdown
- Guides implementation
- Validates output (via checklists)

When requirements change, you update the spec — not the code directly — and then regenerate downstream artifacts. The spec *causes* the code to exist, not the other way around.

### 2.3 Intent-Driven Development

AI agents are excellent at pattern recognition and code generation but struggle with **intent**. When you say "build a user auth system," the agent makes dozens of implicit decisions: which library, which hash algorithm, session vs. JWT, etc.

SDD forces you to make intent explicit upfront:

```
❌ Vibe coding:  "Build a user auth system"

✅ Intent-driven: "Build a user auth system using bcrypt for
   password hashing, JWT with 24h expiry for sessions,
   email-based registration only (no OAuth), and rate-limiting
   on login attempts (5 tries, 15-minute lockout)"
```

The more specific your specification, the closer the output is to what you actually want.

### 2.4 Multi-Step Refinement vs. One-Shot Prompting

One-shot prompting produces generic results. SDD uses a **sequential refinement pipeline**:

```
Constitution → Specify → (Clarify) → Plan → Tasks → Implement
```

Each step builds on the previous. The agent's context grows richer at each stage, resulting in more accurate, intentional output. You review and refine at every checkpoint — you steer, the agent writes.

### 2.5 Greenfield vs. Brownfield Development

**Greenfield (Zero-to-One):** Starting a brand new project from scratch.
- Great for SDD because there are no pre-existing constraints
- Begin with `/speckit.constitution` to establish project principles

**Brownfield (Iterative Enhancement):** Adding features to an existing codebase.
- Spec Kit handles this well — it analyses existing code for context
- The `/speckit.analyze` command is especially valuable here
- No existing constitution required; the agent infers from the codebase

> [!NOTE]
> Brownfield SDD was demonstrated in a community walkthrough adding Docker Compose and a REST API to a ~307,000-line C# CMS codebase — showing the workflow scales to large, real-world projects.

---

## 3. Installation & Setup

### 3.1 System Requirements Check

```bash
# Check git
git --version  # Need 2.x+

# Check uv
uv --version   # Need 0.4+

# Check Python (uv manages this, but good to know)
python3 --version

# Check cursor is installed
which cursor || echo "Install Cursor IDE from https://cursor.sh"
```

### 3.2 Installing the `specify` CLI

**Option A — Persistent (Recommended):**
```bash
# Install a specific stable release (check https://github.com/github/spec-kit/releases)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z

# Or install the latest from main
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify
specify --version
specify check  # Checks system requirements
```

**Option B — One-Time Usage (No Install):**
```bash
uvx --from git+https://github.com/github/spec-kit.git specify init my-project --ai cursor-agent
```

> [!WARNING]
> Pin a specific release tag in production environments for stability. The `main` branch may include unreleased or breaking changes.

### 3.3 Initializing a Project

```bash
# Navigate to your workspace
cd ~/projects

# Initialize a new project for Cursor
specify init my-app --ai cursor-agent

# Initialize in the current directory
specify init . --ai cursor-agent
specify init --here --ai cursor-agent

# Skip git initialization (for non-git projects)
specify init my-app --ai cursor-agent --no-git

# Enable verbose debug output
specify init my-app --ai cursor-agent --debug
```

**What happens on `specify init`:**
1. Creates project directory (or uses current)
2. Runs `git init` and makes an initial commit (unless `--no-git`)
3. Creates the `.specify/` directory with templates
4. Creates the `.cursor/commands/` directory (agent-specific)
5. Installs slash commands as prompt files the agent can read

### 3.4 Understanding the `--ai` Flag

The `--ai` flag tells Spec Kit which agent to install slash commands for. This affects where command files are stored:

| Flag | Command Directory |
|------|------------------|
| `cursor-agent` | `.cursor/commands/` |
| `claude` | `.claude/commands/` |
| `copilot` | `.github/prompts/` or `.github/agents/` |
| `gemini` | `.gemini/commands/` |

> [!NOTE]
> You can reinitialize with a different `--ai` flag to add support for another agent. Spec Kit is cross-agent by design — the underlying templates work across all supported agents.

### 3.5 Generated Directory Structure

After `specify init`, your project looks like this:

```
my-app/
├── .specify/                  # Core Spec Kit templates (DO NOT edit)
│   ├── templates/             # Spec, plan, tasks templates
│   └── scripts/               # Agent-specific scripts
│
├── .cursor/                   # Cursor-specific (agent folder)
│   └── commands/              # Slash command prompt files
│       ├── speckit.constitution.md
│       ├── speckit.specify.md
│       ├── speckit.plan.md
│       ├── speckit.tasks.md
│       ├── speckit.implement.md
│       ├── speckit.clarify.md
│       ├── speckit.analyze.md
│       └── speckit.checklist.md
│
├── specs/                     # Your generated feature specs (git-tracked)
│   └── (empty at init)
│
└── constitution.md            # Project principles (created by /speckit.constitution)
```

> [!NOTE]
> The `specs/` directory is entirely yours. Spec Kit never modifies it during upgrades — your work is safe.

---

## 4. The 5 Core Slash Commands (Deep Dive)

The core Spec Kit workflow uses five commands in sequence. Think of them as a pipeline: the output of each becomes the input for the next.

```
/speckit.constitution  →  /speckit.specify  →  /speckit.plan  →  /speckit.tasks  →  /speckit.implement
        ↑                        ↑                    ↑                ↑
  Project Principles      Requirements          Technical Plan    Task Breakdown
```

---

### 4.1 `/speckit.constitution` — Project Principles & Governance

**Purpose:** Establishes a set of non-negotiable principles and conventions for the project. Think of it as the project's "constitution" — all subsequent commands reference it to stay aligned.

**When to use it:**
- At the very beginning of a greenfield project (run it first)
- When onboarding to an existing brownfield codebase
- Whenever you need to encode org-wide policies, tech stack constraints, or team conventions

**What to write (input):**
Write a description of your project's technical philosophy, team standards, and hard constraints. Be specific and opinionated:

```
/speckit.constitution

This is a FastAPI + PostgreSQL REST API for a B2B SaaS platform.
Conventions:
- Python 3.12+, type hints everywhere, no implicit Any
- SQLAlchemy 2.x with async sessions
- All endpoints require JWT authentication except /health and /auth/*
- Tests use pytest with 80% coverage minimum
- No third-party auth libraries (Authlib, python-jose only)
- Docker-first: all local dev runs in containers
- Conventional Commits enforced via pre-commit hooks
```

**Output artifacts:**
- `constitution.md` (in project root)

**Example constitution.md structure:**
```markdown
# Project Constitution

## Core Principles
1. Type safety is non-negotiable
2. Every endpoint is documented via OpenAPI

## Technology Stack
- Runtime: Python 3.12
- Framework: FastAPI
- Database: PostgreSQL 16 via SQLAlchemy 2.x (async)

## Testing Standards
- Minimum coverage: 80%
- All tests use pytest + pytest-asyncio

## Security Requirements
- JWT required on all protected routes
- Secrets via environment variables only (never hardcoded)
```

**Best practices:**
- Write the constitution *before* `/speckit.specify` — it anchors all future decisions
- Include "never do" items, not just "always do" — these are invaluable for the agent
- If brownfield, let the agent analyze your codebase first and generate a draft, then edit it

**Common mistakes:**
- Being too vague ("use good practices") — the agent will hallucinate what that means
- Skipping the constitution on brownfield projects — you lose governance coherence
- Writing it once and forgetting it exists — review it when major stack decisions change

---

### 4.2 `/speckit.specify` — Requirements & User Stories

**Purpose:** Generates a detailed `spec.md` for a specific feature based on your natural-language description. This is the heart of SDD — your intent is formalized here.

**When to use it:**
- When starting a new feature on any branch
- After creating/updating the constitution

**What to write (input):**
This is your most important prompt. Be detailed. Think about:
- What problem are you solving?
- Who are the users and what are their goals?
- What are the explicit acceptance criteria?
- What should it **not** do (exclusions)?

```
/speckit.specify

Build a photo album feature for our family sharing app.

Users can:
- Create named albums with optional cover photos
- Upload up to 50 photos per album (JPEG, PNG, WebP only, max 10MB each)
- Share albums via invite link (view-only or edit access)
- Soft-delete albums (recoverable within 30 days)

Users cannot:
- Share albums publicly (auth required to view)
- Upload videos (out of scope for v1)
- Nest albums inside other albums

Acceptance criteria:
- Upload completes in < 5 seconds for a 5MB image on a standard connection
- Album list loads in < 500ms
- Shared link works without login (view-only mode only)
```

**Output artifacts:**
- `specs/<branch-or-feature-name>/spec.md`

**Best practices:**
- Think through edge cases before running this command — corrections cost agent cycles
- Include explicit exclusions ("users cannot...") — they prevent scope creep in implementation
- Run `/speckit.clarify` after this if the spec feels ambiguous

**Common mistakes:**
- Writing vague, one-line descriptions ("add user profiles") — this produces generic specs
- Forgetting acceptance criteria — without them, "done" is undefined
- Running `/speckit.plan` immediately without reviewing `spec.md` — always read and edit first

---

### 4.3 `/speckit.plan` — Technical Implementation Plan

**Purpose:** Translates the `spec.md` into a concrete technical plan, including architecture decisions, component breakdown, data models, API contracts, and technology choices.

**When to use it:**
- After reviewing and approving `spec.md`
- Before breaking work into tasks

**What to write (input):**
Provide any technical constraints or preferences that should guide the plan:

```
/speckit.plan

Use S3-compatible storage (we have MinIO running locally).
Keep the upload logic in a dedicated PhotoService class.
Reuse the existing User model from auth module.
Prefer async/await patterns throughout.
```

You can also just run `/speckit.plan` with no additional input and let the agent derive the plan from the spec and constitution.

**Output artifacts:**
- `specs/<feature>/plan.md` — Main technical plan
- `specs/<feature>/research.md` — Technical decision log
- `specs/<feature>/data-model.md` — Database/model design
- `specs/<feature>/contracts/` — API endpoint specifications

**Example plan.md structure:**
```markdown
# Technical Plan: Photo Albums

## Architecture Overview
- PhotoService handles upload, resize, and storage
- AlbumController manages CRUD via REST API
- Background job handles post-upload thumbnail generation

## Components
1. AlbumModel (SQLAlchemy) — stores metadata
2. PhotoUploadHandler — validates, processes, stores
3. ShareLinkService — generates and validates invite tokens

## Data Flow
1. Client uploads to /api/albums/{id}/photos (multipart)
2. Handler validates MIME type and size
3. Photo stored in MinIO; record created in DB
4. Thumbnail job queued via Redis

## Dependencies
- Pillow 10.x (image processing)
- boto3 (MinIO/S3 client)
- python-ulid (ID generation)
```

**Best practices:**
- Review `plan.md` carefully before proceeding — changing architecture after tasks is costly
- Check `data-model.md` against your existing schema for conflicts
- Use `/speckit.analyze` after planning to catch cross-artifact inconsistencies

**Common mistakes:**
- Skipping `plan.md` review and going straight to tasks
- Not providing storage/infrastructure constraints — agent may suggest incompatible solutions
- Ignoring `research.md` — it documents *why* decisions were made, invaluable for future review

---

### 4.4 `/speckit.tasks` — Actionable Task Breakdown

**Purpose:** Converts the technical plan into an ordered, dependency-aware list of atomic tasks that the agent can execute one at a time.

**When to use it:**
- After approving `plan.md`
- Before beginning implementation

**What to write (input):**
You can run it with no input, or provide guidance on task granularity:

```
/speckit.tasks

Break tasks into small units — each should be completable in a single agent session.
Group by layer: data → service → API → tests.
Include a task for writing integration tests after each API endpoint.
```

**Output artifacts:**
- `specs/<feature>/tasks.md`

**Example tasks.md structure:**
```markdown
# Tasks: Photo Albums

## Phase 1: Data Layer
- [ ] 1.1 Create Album migration (id, name, owner_id, created_at, deleted_at)
- [ ] 1.2 Create Photo migration (id, album_id, url, thumbnail_url, size_bytes)
- [ ] 1.3 Implement AlbumModel SQLAlchemy class
- [ ] 1.4 Implement PhotoModel SQLAlchemy class

## Phase 2: Service Layer
- [ ] 2.1 Implement AlbumService (CRUD operations)
- [ ] 2.2 Implement PhotoUploadHandler (validation + MinIO upload)
- [ ] 2.3 Implement ShareLinkService (token generation + validation)

## Phase 3: API Layer
- [ ] 3.1 POST /api/albums — Create album
- [ ] 3.2 GET /api/albums — List user's albums
- [ ] 3.3 POST /api/albums/{id}/photos — Upload photo
- [ ] 3.4 GET /api/albums/share/{token} — View shared album

## Phase 4: Tests
- [ ] 4.1 Unit tests: AlbumService
- [ ] 4.2 Integration tests: Album API endpoints
- [ ] 4.3 Integration tests: Photo upload flow
```

**Best practices:**
- Tasks should be atomic — each independently verifiable
- Order by dependency (data model before service, service before API)
- Run `/speckit.analyze` *before* implementation to validate consistency across all artifacts

**Common mistakes:**
- Tasks that are too large ("implement the entire upload system") — agent loses focus
- Missing test tasks — they're easy to skip and hard to add later
- Skipping the dependency order — the agent may try to use a model that doesn't exist yet

---

### 4.5 `/speckit.implement` — Execute All Tasks

**Purpose:** Orchestrates the agent to implement all tasks in `tasks.md` sequentially, checking each off as it goes.

**When to use it:**
- After reviewing and approving `tasks.md`
- This is the "go" command — it triggers the actual code generation

**What to write (input):**
Usually no additional input needed. The agent reads all artifacts (constitution, spec, plan, tasks) as context:

```
/speckit.implement
```

You can optionally provide implementation notes:
```
/speckit.implement

Start with Phase 1 only. Pause after each phase for my review.
Run tests after each task and fix failures before continuing.
```

**Output artifacts:**
- Actual code files throughout your project
- Updated `tasks.md` with checked-off items

**Best practices:**
- Run in a clean git state (commit or stash any pending changes first)
- Watch the implementation in real-time — be ready to intervene if the agent drifts
- Commit after each phase, not just at the end
- If the agent stops midway, you can resume by referencing the unchecked tasks

**Common mistakes:**
- Running `/speckit.implement` without having reviewed all upstream artifacts
- Letting the agent run unsupervised for too long without a checkpoint
- Not committing frequently — makes it hard to roll back bad decisions

---

## 5. Optional But Important Commands

### 5.1 `/speckit.clarify` — Resolving Underspecified Areas

**Purpose:** Runs a two-phase define-and-apply workflow. The agent identifies ambiguities in your spec and proposes resolutions, which you approve before planning begins.

**When to use it:**
- After `/speckit.specify` when the spec feels incomplete or ambiguous
- When the feature domain is unfamiliar and you're unsure of edge cases

**Example:**
```
/speckit.clarify
```

The agent will surface questions like:
- "Should soft-deleted albums appear in shared link views?"
- "What happens to shared links when an album is deleted?"
- "Is there a maximum album count per user?"

You answer them, and the agent updates `spec.md` accordingly.

---

### 5.2 `/speckit.analyze` — Cross-Artifact Consistency Check

**Purpose:** Reviews all artifacts (constitution, spec, plan, tasks) for inconsistencies, gaps, and coverage issues. Think of it as a linter for your specifications.

**When to use it:**
- After `/speckit.tasks`, before `/speckit.implement`
- Any time you've made manual edits to multiple artifact files

**Example output:**
```
⚠ INCONSISTENCY: spec.md mentions "soft-delete with 30-day recovery"
  but tasks.md has no task for a purge/cleanup job.

⚠ GAP: constitution.md requires 80% test coverage, but tasks.md
  has no test tasks for ShareLinkService.

✓ data-model.md and plan.md are consistent.
✓ API contracts match spec.md user stories.
```

> [!NOTE]
> Run `/speckit.analyze` before every `/speckit.implement`. It catches expensive bugs at the planning stage, not during code review.

---

### 5.3 `/speckit.checklist` — Quality Validation Checklists

**Purpose:** Generates custom quality checklists that validate requirements completeness, clarity, and consistency — described as "unit tests for English."

**When to use it:**
- Before handing off a spec for team review
- As a pre-implementation gate to ensure spec quality

**Example:**
```
/speckit.checklist
```

Output is a checklist like:
```markdown
## Spec Quality Checklist

### Requirements
- [ ] All user stories have acceptance criteria
- [ ] Edge cases are explicitly handled
- [ ] Exclusions are clearly stated

### Technical
- [ ] Data model covers all entities mentioned in spec
- [ ] API contracts match all user-facing actions
- [ ] Performance requirements are quantified

### Governance
- [ ] All decisions align with constitution
- [ ] No tech stack violations
- [ ] Security requirements addressed
```

---

## 6. Project Artifacts & File Structure

After a full SDD cycle, a feature's artifacts live in `specs/<feature-name>/`:

```
specs/
└── 001-photo-albums/
    ├── spec.md          # What you're building (requirements + user stories)
    ├── plan.md          # How you're building it (architecture + component design)
    ├── tasks.md         # Ordered, checkable implementation tasks
    ├── research.md      # Technical decision log (why things were chosen)
    ├── data-model.md    # Database schema / ORM model designs
    └── contracts/
        ├── POST_albums.md
        ├── GET_albums.md
        └── POST_albums_{id}_photos.md

constitution.md           # Project-wide principles (root level)
```

### 6.1 `spec.md` — Feature Specification

The heart of the feature. Contains:
- Problem statement
- User stories ("As a [role], I want to [action] so that [benefit]")
- Acceptance criteria (testable, quantifiable)
- Explicit exclusions (out of scope)
- UX/flow descriptions

**Key rule:** If it's not in `spec.md`, it's not a requirement.

### 6.2 `plan.md` — Technical Plan

The architectural blueprint. Contains:
- High-level architecture diagram (text-based)
- Component list and responsibilities
- Data flow description
- External dependencies
- Performance targets
- Security considerations

### 6.3 `tasks.md` — Task List

Ordered, checkable implementation units. Contains:
- Phases (data, service, API, tests)
- Individual tasks with checkboxes (`- [ ]`)
- Dependencies between tasks (implied by ordering)

### 6.4 `research.md` — Technical Decision Log

Captures *why* decisions were made, not just *what* was decided. Critical for:
- Onboarding new team members
- Revisiting decisions in future iterations
- Avoiding "why did we do it this way?" confusion

### 6.5 `data-model.md` — Database / Model Design

Contains:
- Table or collection definitions
- Field names, types, constraints, indexes
- Relationships (foreign keys, references)
- Migration notes

### 6.6 `contracts/` — API Specifications

One file per endpoint. Contains:
- HTTP method and path
- Request body schema
- Response schema (success and error)
- Authentication requirements
- Rate limiting notes

### 6.7 `constitution.md` — Project Principles

The root-level governance document. Referenced by all other commands. Contains:
- Technology stack decisions
- Coding conventions
- Testing requirements
- Security policies
- "Never do" rules

---

## 7. Advanced Topics

### 7.1 Extensions System

Extensions add new capabilities to Spec Kit beyond the core commands. They integrate with external tools and services.

**Community extensions available:**
- **Jira Integration** — Creates Epics, Stories, and Issues from spec-kit specs and task breakdowns
- **Code Review Extension** — AI-driven code review workflows
- **Azure DevOps Integration** — Syncs User Stories and Task children as features progress
- **CI/CD Gate Extension** — Auto-detects GitHub Actions, CircleCI, GitLab CI, Bitbucket Pipelines; blocks QA handoff until pipeline is green
- **MAQA (Multi-Agent QA)** — Coordinator → feature → QA agent workflow with parallel worktree-based implementation

**Installing an extension:**
```bash
# Browse extensions at github.com/github/spec-kit/tree/main/extensions
specify extension install <extension-name>
```

### 7.2 Presets System

Presets customize the default templates and command behavior for your team or use case.

**Examples:**
- **Enterprise preset** — Adds compliance, security review, and audit trail templates
- **Pirate-speak preset** — Fun example showing how command responses can be rewritten in custom language (demonstrates the preset API)
- **Startup preset** — Lightweight, speed-optimized templates with fewer governance requirements

**Installing a preset:**
```bash
specify preset apply <preset-name>
```

**Community presets** are browseable at `github.com/github/spec-kit/tree/main/presets`

### 7.3 Template Resolution Order

When Spec Kit loads a template (e.g., for `/speckit.specify`), it follows this resolution order (first match wins):

```
1. Local overrides     (.specify/overrides/)
2. Applied presets     (.specify/presets/)
3. Installed extensions (.specify/extensions/)
4. Core templates      (.specify/templates/)
```

This means you can override any template at any level without modifying core files.

**Creating a local override:**
```bash
# Copy the core template you want to override
cp .specify/templates/specify.md .specify/overrides/specify.md

# Edit the override
# Your changes take precedence over core templates
```

### 7.4 Branch Numbering Strategies

Spec Kit auto-detects your branch name to determine the feature directory name. Two common strategies:

**Sequential numbering:**
```bash
git checkout -b 001-user-auth
git checkout -b 002-photo-albums
git checkout -b 003-notifications
```
Artifacts stored in `specs/001-user-auth/`, `specs/002-photo-albums/`, etc.

**Timestamp-based:**
```bash
git checkout -b 20260406-user-auth
git checkout -b 20260407-photo-albums
```
Useful when sequential numbers cause merge conflicts in large teams.

### 7.5 Environment Variables

**`SPECIFY_FEATURE`** — Override feature detection for non-Git repositories or when not using Git branches:

```bash
# Bash/Zsh
export SPECIFY_FEATURE="001-photo-albums"

# Fish shell
set -x SPECIFY_FEATURE "001-photo-albums"

# PowerShell (if applicable)
$env:SPECIFY_FEATURE = "001-photo-albums"
```

> [!WARNING]
> You **must** set `SPECIFY_FEATURE` before using `/speckit.plan` or follow-up commands when you initialized with `--no-git`. Without Git, Spec Kit cannot detect the active feature from your branch name.

---

## 8. Practical Workflows

### 8.1 Zero-to-One (Greenfield) Workflow

Building a brand new project from scratch.

```bash
# 1. Install specify
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 2. Initialize project
specify init my-saas-app --ai cursor-agent

# 3. Open in Cursor
cd my-saas-app
cursor .

# 4. Establish project principles
# In Cursor chat: /speckit.constitution
# → Describe your tech stack, conventions, constraints

# 5. Create feature branch for first feature
git checkout -b 001-core-user-management

# 6. Specify the feature
# In Cursor chat: /speckit.specify
# → Describe user management: registration, login, profile, roles

# 7. Clarify ambiguities (optional but recommended)
# /speckit.clarify

# 8. Generate technical plan
# /speckit.plan
# → Provide any technical constraints (DB choice, auth library, etc.)

# 9. Generate tasks
# /speckit.tasks

# 10. Validate consistency
# /speckit.analyze

# 11. Implement
# /speckit.implement

# 12. Review, test, commit, open PR
git add .
git commit -m "feat: implement core user management"
git push origin 001-core-user-management
```

### 8.2 Iterative Enhancement (Brownfield) Workflow

Adding a new feature to an existing codebase.

```bash
# 1. Open your existing project in Cursor
cd existing-project
cursor .

# 2. Install Spec Kit into the project
specify init --here --ai cursor-agent

# 3. Generate a constitution from your existing code
# In Cursor chat: /speckit.constitution
# The agent will analyze your codebase and generate a constitution
# representing your current conventions. Review and edit it carefully.

# 4. Create a feature branch
git checkout -b 004-export-to-csv

# 5. Specify the new feature
# /speckit.specify
# The agent reads constitution.md and existing code for context

# 6. Continue the pipeline as normal
# /speckit.plan → /speckit.tasks → /speckit.analyze → /speckit.implement
```

> [!NOTE]
> In brownfield SDD, `/speckit.constitution` is your most important step. It captures what your codebase *already does* so that new features stay consistent with existing patterns.

### 8.3 Creative Exploration (Parallel Implementations)

SDD enables exploring multiple implementations of the same spec:

```bash
# Create two branches from the same spec
git checkout main
git checkout -b explore/001-redis-sessions
git checkout main
git checkout -b explore/001-jwt-sessions

# Run the full SDD pipeline on each branch with different plan inputs:
# Branch 1: /speckit.plan "Use Redis for session storage"
# Branch 2: /speckit.plan "Use stateless JWT tokens"

# Compare implementations, pick the winner
# Merge the winning branch, delete the other
```

This is one of SDD's most powerful features — specs are stable while implementations are explorable.

### 8.4 Enterprise Constraints Workflow

Incorporating organizational policies and compliance requirements:

```bash
# 1. Create a company-wide preset
# This encodes your org's non-negotiables
specify preset create company-standards

# 2. Edit the preset templates to include:
# - Security review requirements
# - Compliance checklist (GDPR, SOC2, etc.)
# - Architecture review board approval gates
# - Required documentation standards

# 3. Apply to all projects
specify preset apply company-standards

# 4. The constitution for each project will now inherit these constraints
# while allowing project-specific additions
```

---

## 9. Troubleshooting & Debugging

### 9.1 Common CLI Errors

| Error | Likely Cause | Solution |
|-------|-------------|----------|
| `specify: command not found` | Not in PATH after install | Run `uv tool update-shell` or add `~/.local/bin` to PATH |
| `Failed to detect agent` | Wrong `--ai` flag | Check `specify check` for supported agents |
| `Feature directory not found` | Not on a feature branch | Create branch or set `SPECIFY_FEATURE` |
| `Constitution not found` | Skipped `/speckit.constitution` | Run it first, or create `constitution.md` manually |
| `Template not found` | Corrupt install | Reinstall with `uv tool install --force` |

### 9.2 Git Authentication Issues (Linux/GCM)

Git Credential Manager (GCM) can behave unexpectedly on Linux headless environments:

```bash
# Check current credential helper
git config --global credential.helper

# For headless/server environments, use store (simple) or cache
git config --global credential.helper store
# OR for temporary storage
git config --global credential.helper "cache --timeout=3600"

# For GUI environments, install GCM
sudo apt install git-credential-manager
git config --global credential.helper manager
```

### 9.3 Agent-Specific Quirks

**Cursor (`cursor-agent`):**
- Restart Cursor completely (not just reload window) after `specify init` to pick up new slash commands
- Check commands are installed: `ls -la .cursor/commands/`
- If commands don't appear, manually reload the workspace

**Claude Code (`claude`):**
- Commands live in `.claude/commands/`
- Use `claude --help` to verify slash command discovery

**GitHub Copilot (`copilot`):**
- Commands live in `.github/prompts/` or `.github/agents/`
- Copilot may use PowerShell commands unexpectedly on Linux — this is an IDE context issue, not Spec Kit
- Try: clear Copilot context window and restart VS Code

**OpenAI Codex (`codex`):**
- Does **not** support custom arguments for slash commands (platform restriction)
- In Codex skills mode, use `$speckit-constitution`, `$speckit-specify`, etc. instead of `/speckit.*`

### 9.4 Debug Flags

```bash
# Enable debug output during init
specify init my-project --ai cursor-agent --debug

# Ignore agent tool availability checks (for unsupported environments)
specify init my-project --ai cursor-agent --ignore-agent-tools

# Verify system requirements
specify check
```

### 9.5 Slash Commands Not Appearing in Cursor

```bash
# Verify files exist
ls -la .cursor/commands/

# If missing, re-run specify init (safe to run multiple times)
specify init --here --ai cursor-agent

# Then restart Cursor completely
```

### 9.6 Spec Kit Upgrade Process

```bash
# Upgrade the CLI tool
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git@vX.Y.Z

# Update project template files (safe — never touches specs/)
specify init --here --ai cursor-agent

# Verify upgrade
specify --version
```

> [!WARNING]
> The `specs/` directory is **never** modified during upgrades. However, `.specify/` templates are updated. If you have local overrides in `.specify/overrides/`, they are preserved.

---

## 10. Community & Ecosystem

### 10.1 Community Extensions

Browse and install community-contributed extensions at:
`https://github.com/github/spec-kit/tree/main/extensions`

Notable extensions:
- **jira-integration** — Create Jira Epics/Stories/Issues from spec artifacts
- **cdd-enforcement** — Canonical-Driven Development enforcement with automated checks
- **maqa** — Multi-agent QA workflow with parallel worktree implementation
- **azure-devops** — Azure DevOps Boards sync for user stories and tasks
- **ci-gate** — Blocks QA handoff until CI pipeline is green

### 10.2 Community Presets

Browse community presets at:
`https://github.com/github/spec-kit/tree/main/presets`

### 10.3 Community Walkthroughs

Official walkthroughs demonstrating real-world SDD in action:

| Walkthrough | Scenario | Tech Stack |
|-------------|----------|------------|
| Greenfield .NET CLI | Timezone Utility CLI | .NET single-binary, GitHub Copilot |
| Greenfield Spring Boot | LLM Performance Analytics | Spring Boot, React, PostgreSQL, Docker Compose |
| Brownfield ASP.NET | Extending 307k-line CMS | C#, Razor, Docker, REST API |

These walkthroughs are invaluable — study at least one greenfield and one brownfield before your first real project.

### 10.4 Related Tools & Ecosystem

| Tool | What It Is |
|------|-----------|
| **cc-spex** | Companion tool for spec management (community) |
| **Spec Kit Assistant (VS Code)** | VS Code extension bringing SDD directly into the editor UI |
| **IaC Spec Kit (IBM)** | Spec Kit adapted for Infrastructure-as-Code workflows |
| **OpenSpec** | Lighter alternative to Spec Kit with similar slash-command approach |
| **Amazon Kiro** | AWS's SDD tool (IDE-locked, Claude-only, but similar workflow) |

### 10.5 Community & Discussions

- GitHub Discussions: `https://github.com/github/spec-kit/discussions`
- GitHub Issues: `https://github.com/github/spec-kit/issues`
- The GitHub Blog: Watch for SDD articles and case studies

---

## 11. Hands-On Practice Project

### Project: Personal Expense Tracker CLI

Build a command-line expense tracker. This project is ideal because it's:
- Simple enough to complete in a weekend
- Complex enough to exercise all 5 core commands + optional commands
- Has a clear data model (expenses, categories, reports)
- Involves both a data layer and a user interface (CLI)

**Tech stack (suggested):**
- Python 3.12+
- SQLite (via SQLAlchemy, simple — no Docker needed)
- `rich` library for beautiful CLI output
- `typer` for CLI argument parsing

---

### Step-by-Step Instructions

#### Step 1 — Setup (30 minutes)

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install specify
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Initialize project
specify init expense-tracker --ai cursor-agent

cd expense-tracker
cursor .
```

#### Step 2 — Constitution (15 minutes)

In Cursor chat, type:
```
/speckit.constitution

This is a personal CLI expense tracker written in Python 3.12+.

Tech stack:
- Python 3.12+ with type hints everywhere
- SQLite via SQLAlchemy 2.x (sync sessions, no async needed)
- typer for CLI interface
- rich for terminal output formatting

Conventions:
- All money stored as integers (cents), displayed as decimals
- Dates stored as ISO 8601 strings in SQLite
- No external APIs or network calls
- Single-file commands for simplicity (not over-engineered)
- 70% test coverage minimum via pytest
```

Review `constitution.md`. Edit if needed.

#### Step 3 — Create Feature Branch & Specify (20 minutes)

```bash
git checkout -b 001-core-expense-management
```

In Cursor chat:
```
/speckit.specify

Build a core expense management system for a personal CLI tool.

Users can:
- Add an expense with: amount, category, description, date (optional, defaults to today)
- List all expenses (default: current month)
- Filter expenses by category and/or date range
- Delete an expense by ID
- Show a summary: total spent by category for a given period

Categories are free-form text (no predefined list).

Acceptance criteria:
- `expense add 42.50 food "Lunch at cafe"` adds an expense
- `expense list` shows current month's expenses in a table
- `expense summary` shows spending by category as a bar chart in the terminal
- All amounts displayed as currency formatted strings (e.g., $42.50)
- Deleting a non-existent ID shows a clear error message
```

Run `/speckit.clarify` to resolve any ambiguities the agent identifies.

#### Step 4 — Plan (20 minutes)

```
/speckit.plan

Keep it simple:
- Single SQLite file stored at ~/.expense-tracker/expenses.db
- No migrations framework — just CREATE TABLE IF NOT EXISTS at startup
- Single Python package, not split into microservices
```

Review `plan.md`, `data-model.md`, and `contracts/`.

#### Step 5 — Tasks (10 minutes)

```
/speckit.tasks

Group by: data layer → CLI commands → output formatting → tests.
Each task should be completable in one agent session (< 50 lines of code).
```

Review `tasks.md`. Reorder or edit if needed.

#### Step 6 — Analyze (5 minutes)

```
/speckit.analyze
```

Fix any inconsistencies the agent reports before proceeding.

#### Step 7 — Implement (60-90 minutes)

```
/speckit.implement

Implement one phase at a time. After each phase, run the tests and fix failures before continuing.
```

Watch the implementation. Intervene if the agent drifts. Commit after each phase:

```bash
git add .
git commit -m "feat: implement data layer"
# ... continue after each phase
```

#### Step 8 — Test & Validate

```bash
# Run tests
pytest

# Try the CLI
python -m expense_tracker add 15.00 coffee "Morning espresso"
python -m expense_tracker list
python -m expense_tracker summary
```

Run `/speckit.checklist` and validate each item.

#### Step 9 — Extend (Optional)

Once the core feature is working, practice a brownfield workflow by adding:
- `005-export-csv`: Export expenses to CSV (`/speckit.specify` → full pipeline)
- `006-budget-alerts`: Set monthly budget per category with alerts
- `007-recurring-expenses`: Mark expenses as recurring (weekly/monthly)

---

### Practice Checklist

- [ ] Installed `uv` and `specify` successfully
- [ ] Ran `specify init` and verified slash commands appear in Cursor
- [ ] Wrote a constitution with specific, opinionated constraints
- [ ] Ran `/speckit.specify` with detailed acceptance criteria
- [ ] Used `/speckit.clarify` at least once
- [ ] Reviewed `plan.md` and `data-model.md` before proceeding
- [ ] Ran `/speckit.analyze` and resolved all reported issues
- [ ] Committed after each implementation phase
- [ ] Ran `/speckit.checklist` and validated output quality
- [ ] Added a brownfield feature using the existing codebase

---

## 12. Learning Progress Tracker

Use this checklist to track your Spec Kit mastery:

### Foundation
- [ ] Comfortable with git branching and commits
- [ ] `uv` installed and working
- [ ] `specify` CLI installed and `specify check` passes
- [ ] Understand SDD vs traditional development philosophy
- [ ] Know the difference between greenfield and brownfield SDD

### Setup & Installation
- [ ] Successfully ran `specify init` with `--ai cursor-agent`
- [ ] Slash commands appear in Cursor
- [ ] Understand the generated directory structure
- [ ] Know how to upgrade Spec Kit without losing specs

### Core Commands
- [ ] Written a comprehensive `constitution.md`
- [ ] Written a `spec.md` with acceptance criteria and exclusions
- [ ] Used `/speckit.clarify` to resolve ambiguities
- [ ] Reviewed `plan.md`, `data-model.md`, and API contracts
- [ ] Validated with `/speckit.analyze` before implementing
- [ ] Used `/speckit.checklist` as a pre-implementation gate
- [ ] Completed at least one full greenfield pipeline (all 5 commands)
- [ ] Completed at least one brownfield pipeline

### Advanced Skills
- [ ] Understand the Template Resolution Order
- [ ] Created a local template override
- [ ] Set `SPECIFY_FEATURE` manually for a non-git scenario
- [ ] Explored at least one community extension
- [ ] Read at least one community walkthrough end-to-end

### Mastery
- [ ] Completed the Expense Tracker practice project
- [ ] Added a brownfield feature to the practice project
- [ ] Applied SDD to a real work project
- [ ] Can explain SDD philosophy to a colleague in 2 minutes
- [ ] Contributed to Spec Kit discussions or filed a meaningful issue

---

## 📚 Further Reading & Resources

| Resource | URL |
|----------|-----|
| GitHub Spec Kit Repository | `https://github.com/github/spec-kit` |
| Official Documentation | `https://github.com/github/spec-kit/tree/main/docs` |
| GitHub Blog — SDD Introduction | `https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/` |
| Community Walkthroughs | `https://github.com/github/spec-kit/discussions` |
| Spec Kit Website | `https://speckit.org` |
| Microsoft Developer Blog — SDD Deep Dive | `https://developer.microsoft.com/blog/spec-driven-development-spec-kit` |
| LogRocket Blog — Spec Kit Tutorial | `https://blog.logrocket.com/github-spec-kit/` |

---

*Last updated: April 2026 | Spec Kit is actively developed — always check the GitHub repo for the latest commands and features.*