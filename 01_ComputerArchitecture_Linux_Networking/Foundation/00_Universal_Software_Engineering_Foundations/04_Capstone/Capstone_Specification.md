# Capstone — Track-neutral Task & Issue Tracker

A shared project to demonstrate foundational competence **before selecting a specialization**. Substitute a manufacturing, robotics or personal productivity domain only if you preserve the same engineering requirements.

## Product specification

Users can create a task, assign a title/category/priority, set due dates, update status, filter tasks and produce a summary. Data persists across restarts. Define invalid data and duplicate IDs. Record every assumption that affects behavior.

## Required functional scope

- Create, view, update, close and search tasks.
- Validate required fields, date formats, IDs and status transitions.
- Persist to SQLite with primary/foreign keys, constraints and parameterized queries.
- Support at least two related entities (e.g., Projects and Tasks); a third (e.g., Users) is useful but not required.
- Provide a CLI interface or small HTTP API. A browser frontend is *not* required.
- Separate interface, business logic and persistence into independently testable modules.
- Produce a clear error for invalid and nonexistent IDs. Avoid silent failure.

## Nonfunctional and engineering scope

- README: problem, install, run, tests, sample usage and limitations.
- Short architecture decision record: why these modules, storage and interface were chosen.
- Tests: happy path, boundary values, invalid input, persistence, and at least one regression test.
- Git history with small commits, a feature branch and reviewed change.
- CI runs tests on changes; provide a clean-environment installation test.
- Threat model: identify untrusted inputs and accidental or malicious data changes.
- Add structured, non-sensitive logs for important errors.
- Add reproducibility notes including dependency versions.

## Suggested layout (Python illustration, not a mandated framework)

```text
task-tracker/
├── README.md
├── pyproject.toml
├── src/task_tracker/
│   ├── domain.py
│   ├── service.py
│   ├── storage.py
│   └── cli.py
├── tests/
│   ├── test_domain.py
│   ├── test_service.py
│   └── test_storage.py
├── docs/
│   ├── requirements.md
│   ├── adr-001.md
│   └── threat-model.md
└── .github/workflows/tests.yml
```

## Optional enhancements (only after required scope)

- A small HTTP API for the same business logic.
- CSV import/export and error reporting.
- Simple performance benchmark or pagination.
- Docker packaging.
- Human approval before an AI agent can execute a destructive operation.

## Minimum definition of done

- [ ] Every requirement has an acceptance test or reproducible manual check.
- [ ] Tests run locally and in CI.
- [ ] Program survives invalid input without silent data corruption.
- [ ] Data persists and referential integrity is checked.
- [ ] Repository has no credentials, tokens or private customer data.
- [ ] A new developer can follow README to install and run it.
- [ ] I can explain each major module and important design tradeoffs without AI.
- [ ] I have reviewed all generated changes and can reproduce their test results.

## Evidence folder

Place screenshots or text outputs of passing tests, sample command sessions, schema, CI run, benchmark and your architecture diagram in this project or linked repository. Do not claim external review or real-world production readiness if it has not happened.
