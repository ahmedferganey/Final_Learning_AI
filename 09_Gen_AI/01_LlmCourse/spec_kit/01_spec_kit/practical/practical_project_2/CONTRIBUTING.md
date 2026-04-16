## Branch Naming

Format: `feature/<spec-id>-<short-name>`

Examples:
- `feature/001-repository-foundation`
- `feature/002-backend-scaffold`
- `fix/short-description`
- `release/1.0.0`

Branches are created per spec. One spec = one branch = one PR.

## Commit Convention

All commits MUST follow [Conventional Commits](https://www.conventionalcommits.org/):

Format: `<type>(<scope>): <description>`

Permitted types: feat, fix, docs, refactor, test, chore, perf

Permitted scopes: auth, training, coaching, analytics, nutrition,
notifications, sync, web, mobile, infra

Valid examples:
- `feat(auth): add JWT login endpoint`
- `docs(specs): add spec 0.2 backend scaffold`
- `chore(infra): update Docker base image to python 3.11`

Invalid examples (DO NOT USE):
- `updated stuff` — missing type, scope, and description format
- `fixed bug` — missing type and scope

## PR Process

- PRs MUST reference a spec ID in the title or description.
- Keep PRs small and reviewable (< 500 lines of diff, excluding generated code and migrations).
- CI must pass before a PR can be merged.
- At least 1 approving review is required. Self-merge is prohibited.
- Use the PR template — fill all four sections (what changed, why, how to test, spec link).

## Creating an Architecture Decision Record (ADR)

1. Copy `docs/decisions/adr-template.md` to `docs/decisions/NNN-short-name.md`
   where NNN is the next available zero-padded number (e.g., `003-...`).
2. Fill in all sections of the template.
3. Set `status: proposed`.
4. Open a PR with the new ADR file.
5. Obtain at least 1 approving review from a team member other than the author.
6. On merge, update `status: accepted`.
7. ADRs are immutable once accepted. Only `status` may change post-acceptance
   (to `superseded` if a replacement ADR is ratified).

Numbering collision: if two engineers create an ADR simultaneously, the second
must be renumbered before merging.

## Secret Scanning

`detect-secrets` is mandatory. Install it: `pip install detect-secrets`

Before committing: `detect-secrets scan --baseline .secrets.baseline`

The CI pipeline runs this scan automatically on every PR and will block merge
if unacknowledged secrets are found.

To acknowledge a false positive:
`detect-secrets audit .secrets.baseline`
Then commit the updated `.secrets.baseline`.

## Spec-Driven Development

Every feature begins as a spec in `specs/`. Implementation MUST NOT begin
before the spec is reviewed and acceptance criteria are agreed upon.
See `Plan.md` at the repository root for the full phase and spec breakdown.
