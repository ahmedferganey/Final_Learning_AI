# Research: Repository Foundation

**Date**: 2026-04-09
**Plan**: [plan.md](plan.md)

All NEEDS CLARIFICATION items from Technical Context are resolved here.

---

## 1. .gitignore Coverage — Python, Node.js, Flutter/Dart

**Decision**: Combine the GitHub-maintained community gitignore templates for Python, Node, and
Dart into a single root `.gitignore`.

**Rationale**: The `github/gitignore` community templates are the standard reference and cover all
common build artefacts. A single root `.gitignore` is simpler than per-directory files and Git
respects it across all subdirectories of the monorepo.

**Key entries required:**

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
env/
venv/
.venv/
*.egg-info/
dist/
build/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/

# Node.js / Next.js
node_modules/
.next/
out/
*.tsbuildinfo
.npm
.eslintcache

# Flutter / Dart
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
build/

# Secrets
.env
.env.local
.env.*.local
.secrets.baseline.bak
```

**Alternatives considered**: Per-directory `.gitignore` files per stack — rejected because
the root `.gitignore` achieves the same result with less fragmentation.

---

## 2. detect-secrets CI Job Structure

**Decision**: GitHub Actions workflow step using `detect-secrets` baseline scan with a committed
`.secrets.baseline` file.

**Rationale**: GitHub Actions is the CI platform (confirmed: GitHub is canonical hosting
platform, clarified 2026-04-09). The baseline approach allows developers to acknowledge
intentional false positives without permanently blocking CI. Any unacknowledged secret causes
the CI job to exit non-zero and block the PR merge.

**Recommended CI step** (to be wired up in Spec 0.5 — GitHub Actions):

```yaml
- name: Scan for secrets
  run: |
    pip install detect-secrets
    detect-secrets scan --baseline .secrets.baseline
    detect-secrets audit .secrets.baseline
```

**Baseline initialization** (one-time, committed to repo in this spec):

```bash
pip install detect-secrets
detect-secrets scan > .secrets.baseline
git add .secrets.baseline
```

**Alternatives considered**:
- `truffleHog` — more comprehensive but heavier; better suited for Phase 9 hardening audit
- `git-secrets` — AWS credential patterns only; too narrow for a general-purpose monorepo
- GitGuardian — third-party SaaS with data residency concerns; deferred to Phase 9 if needed

---

## 3. ADR Template Format

**Decision**: MADR (Markdown Any Decision Record) structure with required GymOS fields.

**Rationale**: MADR is lightweight, widely adopted, git-diffable, and maps cleanly to the
required sections in FR-005. No external tooling or services are required.

**Required sections** (per FR-005):
- `title` — decision name in sentence case
- `status` — `proposed` | `accepted` | `superseded`
- `date` — ISO 8601 (set at creation, immutable)
- `context` — forces and constraints driving the decision
- `decision` — the chosen approach
- `consequences` — positive and negative impacts
- `alternatives considered` — at least one rejected option with brief rationale

**Alternatives considered**: RFC format — more verbose and suited for external communication;
rejected for internal ADRs as overhead is not justified at current team size.

---

## Resolution Summary

| Item | Status | Outcome |
|---|---|---|
| `.gitignore` artefact coverage | Resolved | Combined Python + Node + Flutter/Dart entries in root `.gitignore` |
| `detect-secrets` CI structure | Resolved | GitHub Actions step with `.secrets.baseline`; CI gate blocks unacknowledged secrets |
| ADR template format | Resolved | MADR structure with 7 required fields |
