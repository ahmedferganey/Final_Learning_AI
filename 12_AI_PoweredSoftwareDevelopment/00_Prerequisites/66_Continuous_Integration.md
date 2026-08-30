# 66. Continuous Integration

> Phase 17 — DevOps Fundamentals

Continuous Integration (CI) is the engineering practice of integrating small code changes frequently into a shared mainline and validating them automatically.

A mature CI system answers one question repeatedly:

```text
Is this change safe enough to integrate?
```

The CI feedback loop is:

```text
Developer Change
      ↓
Git Push / Pull Request
      ↓
CI Trigger
      ↓
Checkout
      ↓
Restore Dependencies
      ↓
Format / Lint
      ↓
Build
      ↓
Unit Tests
      ↓
Static Analysis
      ↓
Security Checks
      ↓
Package
      ↓
Artifact
      ↓
Status Returned to Developer
```

CI is not merely "a pipeline that runs tests." It is a discipline that depends on:

```text
small changes
frequent integration
fast feedback
reliable automation
reproducible builds
trusted artifacts
branch protection
clear ownership
```

## 1. Topic Title

**Continuous Integration**

## 2. Learning Objectives
- Explain Continuous Integration as both a practice and an automation system.
- Explain why frequent integration reduces merge and release risk.
- Design a CI pipeline from source checkout to artifact publication.
- Explain pipeline triggers, stages, jobs, DAGs, runners, agents, and executors.
- Use pipeline-as-code patterns.
- Design fast-feedback pipelines.
- Explain build reproducibility and dependency locking.
- Explain caches, artifacts, reports, and test evidence.
- Explain branch protection and required status checks.
- Explain trunk-based development and short-lived branches in CI.
- Explain unit, integration, contract, smoke, security, and quality checks inside CI.
- Explain test sharding, matrix builds, retries, and flaky-test management.
- Explain CI secrets, OIDC, short-lived credentials, and least privilege.
- Explain hosted vs self-hosted runners and ephemeral runners.
- Explain containerized build environments.
- Explain artifact repositories and registries.
- Explain SBOM, provenance, signatures, and software supply-chain controls.
- Explain CI observability and metrics.
- Explain queue time, execution time, failure rate, and pipeline reliability.
- Explain monorepo and polyrepo CI strategies.
- Explain reusable workflows/templates.
- Explain GitHub Actions, GitLab CI, Jenkins, and Azure DevOps concepts.
- Design CI for Python, Node.js, Java, containers, Terraform, and Kubernetes repositories.
- Troubleshoot common CI failures systematically.
- Build a production-grade CI platform design.

## 3. Prerequisites

Required:

```text
65. DevOps Concepts and Toolchain
Git
Linux CLI
Basic programming
Basic testing concepts
Docker fundamentals
```

Recommended:

```text
Python or Node.js
Terraform
Kubernetes
YAML
JSON
```

## 4. Core Concepts Explanation

# Part 1 — What Continuous Integration Means

### Core Explanation

Continuous Integration means developers integrate small changes frequently into a shared mainline and automated checks validate the integration continuously. The practice matters more than the CI product.

### Example / Visualization

```text
Small change → PR → automated checks → merge → main stays healthy
```

### Why It Matters

CI reduces large integration events and shortens feedback loops.

# Part 2 — CI vs Build Automation

### Core Explanation

Build automation compiles/packages software. CI includes integration discipline plus automated validation around every change.

### Example / Visualization

```text
Build automation: source → binary
CI: source → build + test + scan + feedback
```

### Why It Matters

A build server alone does not guarantee frequent integration or a healthy main branch.

# Part 3 — CI vs Continuous Delivery

### Core Explanation

CI determines whether a change is safe to integrate and produces validated artifacts. Continuous Delivery moves those artifacts through environments toward production.

### Example / Visualization

```text
CI: code → artifact
CD: artifact → environments
```

### Why It Matters

Separating the responsibilities helps design clean pipelines.

# Part 4 — CI Feedback Loop

### Core Explanation

The value of CI comes from the speed and reliability of feedback. A failure should reach the developer while the change context is still fresh.

### Example / Visualization

```text
commit → CI → red/green result → developer action
```

### Why It Matters

Slow feedback increases context switching and batch size.

# Part 5 — Frequent Integration

### Core Explanation

Teams should integrate at least daily and preferably much more often. Long-lived isolation increases merge complexity and hidden incompatibilities.

### Example / Visualization

```text
main: A-B-C-D-E
feature after 5 days: A-X-Y-Z → conflict
```

### Why It Matters

Frequent integration turns merge risk into small continuous events.

# Part 6 — Small Change Sets

### Core Explanation

CI works best with small pull requests and small commits. Large changes increase review time, test complexity, and failure diagnosis cost.

### Example / Visualization

```text
PR A: 150 lines
PR B: 4,000 lines
```

### Why It Matters

Smaller changes improve both flow and safety.

# Part 7 — Healthy Mainline

### Core Explanation

The main branch should remain buildable and releasable. Required checks prevent known-broken changes from entering.

### Example / Visualization

```text
PR → required checks → merge to protected main
```

### Why It Matters

A broken main branch blocks the entire team.

# Part 8 — Trunk-Based Development

### Core Explanation

Short-lived branches merge back to a shared trunk frequently. Feature flags can keep incomplete functionality hidden while integration continues.

### Example / Visualization

```text
feature branch hours/day → main
feature flag controls exposure
```

### Why It Matters

This reduces branch divergence and supports high-frequency CI.

# Part 9 — Long-Lived Branch Anti-Pattern

### Core Explanation

Branches that live for weeks defer integration. The eventual merge becomes a large high-risk event.

### Example / Visualization

```text
week 1: small difference
week 4: hundreds of conflicts
```

### Why It Matters

CI cannot validate integration that has not happened.

# Part 10 — Pull Request as CI Boundary

### Core Explanation

A pull request is a natural place to run automated validation and collect human review evidence before merge.

### Example / Visualization

```text
PR
├─ lint
├─ tests
├─ security
└─ review
```

### Why It Matters

The PR becomes the integration decision point.

# Part 11 — Status Checks

### Core Explanation

CI systems publish pass/fail statuses back to the source-control platform. Branch protection can require specific checks before merge.

### Example / Visualization

```text
required:
build ✓
unit ✓
security ✓
review ✓
```

### Why It Matters

Automation becomes an enforceable guardrail instead of optional advice.

# Part 12 — Fast Feedback

### Core Explanation

CI should prioritize fast, high-signal checks early. Cheap checks should fail before expensive integration environments are started.

### Example / Visualization

```text
format 20s → unit 2m → integration 15m
```

### Why It Matters

Failing fast protects developer time and CI capacity.

# Part 13 — Pipeline as Code

### Core Explanation

Pipeline definitions should live in version control and be reviewed like application code.

### Example / Visualization

```text
.github/workflows/ci.yml
.gitlab-ci.yml
Jenkinsfile
azure-pipelines.yml
```

### Why It Matters

Versioned pipelines are auditable and reproducible.

# Part 14 — CI Trigger

### Core Explanation

Pipelines may trigger on pull request, push, tag, schedule, manual request, or external event. Each trigger should have a clear purpose.

### Example / Visualization

```text
PR → fast validation
main → full build
tag → release build
```

### Why It Matters

Trigger design controls cost and feedback timing.

# Part 15 — CI Event Filtering

### Core Explanation

Use path, branch, tag, or file-change filters to avoid unnecessary jobs while ensuring required validations still run.

### Example / Visualization

```text
docs-only change → skip container build
```

### Why It Matters

Good filtering reduces wasted compute without weakening quality.

# Part 16 — CI Stage

### Core Explanation

Stages organize pipeline work into logical phases such as validate, build, test, scan, and package.

### Example / Visualization

```text
Validate → Build → Test → Scan → Package
```

### Why It Matters

Stages make the delivery logic easier to understand.

# Part 17 — CI Job

### Core Explanation

A job is an execution unit that runs on one runner/agent environment. Jobs can run sequentially or in parallel.

### Example / Visualization

```text
Test stage
├─ unit-linux
├─ unit-windows
└─ lint
```

### Why It Matters

Job boundaries affect parallelism, isolation, and cache/artifact transfer.

# Part 18 — Pipeline DAG

### Core Explanation

Modern CI engines can express dependencies between jobs rather than forcing every job to wait for the previous stage.

### Example / Visualization

```text
build ─┬→ unit
        ├→ lint
        └→ scan
all → package
```

### Why It Matters

DAG execution reduces unnecessary waiting.

# Part 19 — Job Dependency

### Core Explanation

A job should depend only on outputs it truly needs. Overly broad dependencies serialize the pipeline.

### Example / Visualization

```text
package needs build artifact
lint does not need integration DB
```

### Why It Matters

Accurate dependencies improve speed and clarity.

# Part 20 — Runner / Agent

### Core Explanation

A runner or agent executes pipeline jobs. It needs CPU, memory, filesystem, network, tools, and credentials appropriate to the job.

### Example / Visualization

```text
CI controller → runner → job commands
```

### Why It Matters

Runners are part of the software supply chain and require security controls.

# Part 21 — Hosted Runner

### Core Explanation

Hosted runners are maintained by the CI provider and are usually ephemeral. They reduce infrastructure maintenance.

### Example / Visualization

```text
job → provider-managed VM/container → destroy
```

### Why It Matters

Convenient default for many workloads.

# Part 22 — Self-Hosted Runner

### Core Explanation

Self-hosted runners provide custom networks, hardware, tools, or data access but create patching, isolation, and persistence responsibilities.

### Example / Visualization

```text
CI → organization runner → private network
```

### Why It Matters

Persistent privileged runners can become a major attack surface.

# Part 23 — Ephemeral Runner

### Core Explanation

An ephemeral runner exists only for one job and is destroyed afterward.

### Example / Visualization

```text
create runner → run job → destroy runner
```

### Why It Matters

This reduces cross-job contamination and persistence of secrets.

# Part 24 — Runner Pools

### Core Explanation

Organizations often create pools by trust zone or workload: public builds, internal builds, production deployment, GPU builds.

### Example / Visualization

```text
public-runner
internal-runner
prod-runner
```

### Why It Matters

Workload separation reduces privilege bleed.

# Part 25 — Runner Labels

### Core Explanation

Labels/tags route jobs to runners with required capabilities.

### Example / Visualization

```text
runs-on: [self-hosted, linux, docker]
```

### Why It Matters

Labels should describe capability rather than granting unnecessary access.

# Part 26 — Build Environment

### Core Explanation

The build environment should pin OS, language runtime, compiler, package manager, and critical tools.

### Example / Visualization

```text
build-image:v7
Python 3.13
Node 24
scanner versions pinned
```

### Why It Matters

Controlled environments improve reproducibility.

# Part 27 — Containerized Build

### Core Explanation

Containers are useful for CI because they package build tools and dependencies into reproducible execution environments.

### Example / Visualization

```text
CI job → build container → artifact
```

### Why It Matters

They reduce 'works on my machine' differences.

# Part 28 — Workspace

### Core Explanation

A job workspace contains checked-out source and temporary job files. It should be treated as ephemeral.

### Example / Visualization

```text
checkout → build files → reports → cleanup
```

### Why It Matters

Do not rely on undeclared files left by previous jobs.

# Part 29 — Checkout Depth

### Core Explanation

Shallow clones reduce network/time but some versioning, diff, or security tools need full history.

### Example / Visualization

```text
depth=1 vs full history
```

### Why It Matters

Choose clone depth based on pipeline requirements.

# Part 30 — Submodules

### Core Explanation

Git submodules complicate checkout, authentication, and versioning. If used, pin exact commits and configure CI credentials intentionally.

### Example / Visualization

```text
repo → submodule commit abc123
```

### Why It Matters

Hidden moving submodule branches reduce reproducibility.

# Part 31 — Monorepo CI

### Core Explanation

A monorepo contains multiple components. CI should detect affected paths and run only relevant builds while preserving cross-component tests where needed.

### Example / Visualization

```text
repo/
├─ api/
├─ web/
└─ shared/
```

### Why It Matters

Naively rebuilding everything can make monorepo CI slow.

# Part 32 — Polyrepo CI

### Core Explanation

Polyrepo environments have separate repositories per service/component. CI is simpler per repo but cross-service integration and version coordination need explicit mechanisms.

### Example / Visualization

```text
service-a repo
service-b repo
shared-lib repo
```

### Why It Matters

Repository strategy changes CI dependency management.

# Part 33 — Change Detection

### Core Explanation

Path-aware change detection can decide which jobs/modules need rebuilding.

### Example / Visualization

```text
shared-lib changed → build dependent services
```

### Why It Matters

Smart change detection improves scalability in large repositories.

# Part 34 — CI Concurrency

### Core Explanation

CI systems can run multiple pipelines simultaneously, but jobs that modify shared test infrastructure or publish mutable resources need concurrency control.

### Example / Visualization

```text
PR pipelines parallel
shared integration env serialized
```

### Why It Matters

Concurrency improves speed only when shared-state conflicts are controlled.

# Part 35 — Pipeline Cancellation

### Core Explanation

If a newer commit supersedes an older PR run, CI can cancel the older run to free capacity.

### Example / Visualization

```text
commit A running
commit B pushed → cancel A
```

### Why It Matters

Avoids wasting resources on obsolete validation.

# Part 36 — Pipeline Timeout

### Core Explanation

Every job should have a sensible timeout so hung builds do not consume runners indefinitely.

### Example / Visualization

```text
unit test timeout 10m
integration timeout 45m
```

### Why It Matters

Timeouts are operational controls, not only test settings.

# Part 37 — Build Automation

### Core Explanation

A build transforms source into an executable/package/image using a repeatable command.

### Example / Visualization

```text
source → compiler/build tool → artifact
```

### Why It Matters

CI should run the same build command developers can reproduce locally.

# Part 38 — Build Script

### Core Explanation

Keep the canonical build logic in repository scripts or build tools, not hidden inside CI UI steps.

### Example / Visualization

```text
make build / ./gradlew build / npm run build
```

### Why It Matters

This makes CI portable and testable.

# Part 39 — Reproducible Build

### Core Explanation

A reproducible build uses controlled dependencies and tool versions so the same source produces equivalent output.

### Example / Visualization

```text
commit + lockfile + build image → artifact
```

### Why It Matters

Critical for rollback and provenance.

# Part 40 — Dependency Resolution

### Core Explanation

CI restores language dependencies before build/test. Resolution should use lock files or pinned manifests where available.

### Example / Visualization

```text
pnpm-lock.yaml / poetry.lock / pom.xml
```

### Why It Matters

Unpinned dependency resolution can make the same commit behave differently tomorrow.

# Part 41 — Dependency Cache

### Core Explanation

Caches speed repeated dependency restoration but must be keyed by relevant inputs.

### Example / Visualization

```text
key = OS + runtime + lockfile hash
```

### Why It Matters

A stale cache can create confusing failures.

# Part 42 — Cache Poisoning Risk

### Core Explanation

Caches can become a supply-chain attack vector if untrusted branches can write cache consumed by privileged workflows.

### Example / Visualization

```text
untrusted PR cache → prod workflow ✗
```

### Why It Matters

Separate trust domains and cache permissions.

# Part 43 — Cache vs Artifact

### Core Explanation

Caches are disposable optimization data. Artifacts are outputs/evidence that must be preserved or promoted.

### Example / Visualization

```text
cache: dependencies
artifact: app.jar
```

### Why It Matters

Do not rely on cache retention for release recovery.

# Part 44 — Build Matrix

### Core Explanation

Matrix builds test combinations of OS, runtime, architecture, or feature flags.

### Example / Visualization

```text
Python 3.12/3.13 × Linux/Windows
```

### Why It Matters

Matrix testing catches compatibility problems efficiently.

# Part 45 — Matrix Explosion

### Core Explanation

Too many combinations can make CI expensive and slow.

### Example / Visualization

```text
5 OS × 5 versions × 4 DBs = 100 jobs
```

### Why It Matters

Choose representative supported combinations.

# Part 46 — Cross-Platform Builds

### Core Explanation

Applications supporting multiple OS/architectures should compile/test each supported target.

### Example / Visualization

```text
linux-amd64 / linux-arm64
```

### Why It Matters

Production target differences should be validated in CI.

# Part 47 — Build Number

### Core Explanation

A CI build number identifies one run but should be linked to commit SHA and artifact digest.

### Example / Visualization

```text
build 891 → commit abc → digest xyz
```

### Why It Matters

Build number alone is not immutable source identity.

# Part 48 — Semantic Versioning

### Core Explanation

Version numbers communicate compatibility intent for libraries and releases.

### Example / Visualization

```text
2.4.1 = major.minor.patch
```

### Why It Matters

CI can derive release metadata from tags and manifests.

# Part 49 — Version from Git

### Core Explanation

CI may derive version from Git tags/commits while keeping source-of-truth rules explicit.

### Example / Visualization

```text
git describe / tag v2.4.1
```

### Why It Matters

Traceability links source and artifact.

# Part 50 — Generated Files

### Core Explanation

Generated code or artifacts should be reproducible from source and either committed intentionally or rebuilt deterministically.

### Example / Visualization

```text
OpenAPI client generation
```

### Why It Matters

Hidden manual generation steps undermine CI.

# Part 51 — Compiler Warnings

### Core Explanation

Treat selected compiler warnings as errors for critical codebases if the signal is reliable.

### Example / Visualization

```text
-Werror-like policy
```

### Why It Matters

Warnings should not accumulate into ignored noise.

# Part 52 — Linting

### Core Explanation

Linters enforce code-quality and correctness rules quickly.

### Example / Visualization

```text
ruff / eslint / golangci-lint
```

### Why It Matters

Fast linters belong early in CI.

# Part 53 — Formatting Check

### Core Explanation

Automated formatting checks remove style debates from review.

### Example / Visualization

```text
terraform fmt -check / prettier --check
```

### Why It Matters

Humans can focus on logic.

# Part 54 — Static Type Checking

### Core Explanation

Type checkers catch interface and data-flow errors without running the application.

### Example / Visualization

```text
mypy / tsc / compiler
```

### Why It Matters

Fast pre-runtime feedback lowers defect cost.

# Part 55 — Unit Tests

### Core Explanation

Unit tests validate focused logic quickly and should usually run on every PR.

### Example / Visualization

```text
function input → expected output
```

### Why It Matters

They form the fast base of CI.

# Part 56 — Test Isolation

### Core Explanation

Tests should not depend on order, global mutable state, or other tests unless explicitly designed.

### Example / Visualization

```text
each test creates/cleans its data
```

### Why It Matters

Isolation improves parallelism and reliability.

# Part 57 — Test Determinism

### Core Explanation

Same code/input should produce same test result.

### Example / Visualization

```text
same commit → same result
```

### Why It Matters

Nondeterminism destroys trust.

# Part 58 — Test Fixtures

### Core Explanation

Fixtures create controlled inputs and environment state for tests.

### Example / Visualization

```text
sample DB rows / temp files
```

### Why It Matters

Reusable fixtures reduce duplicated test setup.

# Part 59 — Mocks

### Core Explanation

Mocks replace dependencies with controllable behavior to test one component's logic.

### Example / Visualization

```text
payment client mock
```

### Why It Matters

Useful for fast tests but cannot prove real integration.

# Part 60 — Stubs and Fakes

### Core Explanation

Stubs return predetermined data; fakes provide lightweight functional implementations.

### Example / Visualization

```text
in-memory repository fake
```

### Why It Matters

Different test doubles serve different purposes.

# Part 61 — Integration Tests

### Core Explanation

Integration tests validate multiple real components together.

### Example / Visualization

```text
API ↔ PostgreSQL
```

### Why It Matters

Catch interface/configuration failures not visible in unit tests.

# Part 62 — Ephemeral Test Environment

### Core Explanation

CI can create temporary databases, containers, or namespaces per pipeline.

### Example / Visualization

```text
docker compose / namespace per PR
```

### Why It Matters

Isolation reduces cross-test interference.

# Part 63 — Service Containers

### Core Explanation

CI systems often start databases/queues alongside jobs for integration tests.

### Example / Visualization

```text
job + postgres + redis
```

### Why It Matters

Useful for realistic integration without shared environments.

# Part 64 — Contract Tests

### Core Explanation

Contract tests validate consumer/provider interface expectations.

### Example / Visualization

```text
consumer contract ↔ provider verification
```

### Why It Matters

Reduce dependence on one shared integration environment.

# Part 65 — API Tests

### Core Explanation

Automated API tests validate status codes, schemas, auth, and business behavior.

### Example / Visualization

```text
GET /health, POST /orders
```

### Why It Matters

They provide higher-level confidence.

# Part 66 — End-to-End Tests

### Core Explanation

E2E tests validate broad user journeys across a deployed system.

### Example / Visualization

```text
browser → API → DB
```

### Why It Matters

Keep them focused because they are slower and more fragile.

# Part 67 — Smoke Tests in CI

### Core Explanation

Smoke tests can verify packaged/deployed test builds before artifact publication.

### Example / Visualization

```text
start app → health check → basic operation
```

### Why It Matters

Catch packaging/runtime errors.

# Part 68 — Regression Suite

### Core Explanation

Regression tests preserve previously working behavior across changes.

### Example / Visualization

```text
old bugs become tests
```

### Why It Matters

They protect against reintroducing known defects.

# Part 69 — Coverage

### Core Explanation

Coverage measures which code paths tests execute, but high coverage does not guarantee meaningful assertions.

### Example / Visualization

```text
90% lines covered
```

### Why It Matters

Use coverage as a signal, not a quality score.

# Part 70 — Coverage Gate

### Core Explanation

A coverage threshold can prevent severe regression but should not drive meaningless tests.

### Example / Visualization

```text
coverage must not drop > X
```

### Why It Matters

Protect trend rather than chase vanity numbers.

# Part 71 — Mutation Testing

### Core Explanation

Mutation testing changes code intentionally and checks whether tests catch the mutation.

### Example / Visualization

```text
operator flipped / return changed
```

### Why It Matters

Measures test effectiveness more directly than raw coverage.

# Part 72 — Test Sharding

### Core Explanation

Split a large test suite into balanced partitions across runners.

### Example / Visualization

```text
10 shards × 5m instead of 50m
```

### Why It Matters

Improves feedback time.

# Part 73 — Test Parallelism

### Core Explanation

Tests can run concurrently when isolated.

### Example / Visualization

```text
pytest -n / parallel workers
```

### Why It Matters

Shared state must be controlled.

# Part 74 — Flaky Test

### Core Explanation

A flaky test changes result without relevant code change.

### Example / Visualization

```text
pass-fail-pass on same commit
```

### Why It Matters

Flakiness erodes CI trust.

# Part 75 — Flaky Test Quarantine

### Core Explanation

Temporary quarantine can protect mainline flow while retaining visibility, but every quarantined test needs an owner and deadline.

### Example / Visualization

```text
quarantine list + issue
```

### Why It Matters

Quarantine must not become permanent deletion of coverage.

# Part 76 — Retry Policy

### Core Explanation

Retries should be limited and used only for known transient infrastructure errors, not as a substitute for fixing flaky tests.

### Example / Visualization

```text
retry network provisioning once
```

### Why It Matters

Unlimited reruns hide real failures.

# Part 77 — Fail Fast Ordering

### Core Explanation

Put cheap, deterministic checks before expensive environments.

### Example / Visualization

```text
format → lint → unit → integration
```

### Why It Matters

Reduces wasted compute.

# Part 78 — Fail-Slow Aggregate Mode

### Core Explanation

Some stages intentionally collect multiple independent findings before failing, such as lint + security + unit results.

### Example / Visualization

```text
parallel checks → report all
```

### Why It Matters

Useful when developer benefits from seeing all issues at once.

# Part 79 — Test Reports

### Core Explanation

CI should publish structured test reports that show failures, timing, and trends.

### Example / Visualization

```text
JUnit XML / coverage report
```

### Why It Matters

Developers should not search raw logs for every failure.

# Part 80 — Test Duration Tracking

### Core Explanation

Track slowest tests and suite duration over time.

### Example / Visualization

```text
top 20 slow tests
```

### Why It Matters

Prevents gradual CI slowdown.

# Part 81 — Performance Baseline

### Core Explanation

Selected performance checks can compare against a baseline and alert on major regression.

### Example / Visualization

```text
p95 latency +20% → fail/warn
```

### Why It Matters

Performance is part of quality.

# Part 82 — Resource Limits for Tests

### Core Explanation

Bound CPU/memory/time to expose leaks and protect shared runners.

### Example / Visualization

```text
job memory limit / timeout
```

### Why It Matters

Unbounded tests can destabilize CI infrastructure.

# Part 83 — Secret Scanning

### Core Explanation

Scan commits and history for tokens, keys, and credentials before merge.

### Example / Visualization

```text
secret scanner on PR/push
```

### Why It Matters

A leaked credential should be rotated even if removed from Git.

# Part 84 — SAST

### Core Explanation

Static security analysis checks source for insecure patterns.

### Example / Visualization

```text
source → SAST → findings
```

### Why It Matters

Fast static security feedback belongs in CI.

# Part 85 — SCA

### Core Explanation

Software composition analysis evaluates third-party dependencies for vulnerabilities/licenses.

### Example / Visualization

```text
lockfile → dependency scanner
```

### Why It Matters

Supply-chain risk often enters through dependencies.

# Part 86 — Container Scanning

### Core Explanation

Scan container images for vulnerable packages and policy violations.

### Example / Visualization

```text
image → scanner → findings
```

### Why It Matters

Images can become vulnerable after publication; periodic rescanning also matters.

# Part 87 — IaC Scanning

### Core Explanation

Scan Terraform/Kubernetes/cloud configuration for insecure infrastructure patterns.

### Example / Visualization

```text
public DB / open SSH detected
```

### Why It Matters

Prevents misconfiguration before deployment.

# Part 88 — Policy as Code in CI

### Core Explanation

Evaluate machine-readable policies against code or plan output.

### Example / Visualization

```text
deny public bucket
```

### Why It Matters

Automates governance.

# Part 89 — Security Severity Policy

### Core Explanation

Define which finding severities block merge and which create follow-up work.

### Example / Visualization

```text
critical=block, low=warn
```

### Why It Matters

Without policy, scanners create inconsistent decisions.

# Part 90 — False Positive Handling

### Core Explanation

Security findings need triage, suppression justification, owner, and expiry.

### Example / Visualization

```text
suppression with reason+expiry
```

### Why It Matters

Permanent blanket ignores destroy scanner value.

# Part 91 — SBOM Generation

### Core Explanation

Generate a software bill of materials for release artifacts.

### Example / Visualization

```text
artifact + SBOM
```

### Why It Matters

Supports vulnerability response and provenance.

# Part 92 — Build Provenance

### Core Explanation

Record source commit, builder identity, build process, dependencies, and artifact digest.

### Example / Visualization

```text
commit → trusted builder → provenance
```

### Why It Matters

Consumers can verify origin.

# Part 93 — Artifact Signing

### Core Explanation

Sign artifacts or attestations using trusted identity/key mechanisms.

### Example / Visualization

```text
digest + signature
```

### Why It Matters

Strengthens integrity.

# Part 94 — Artifact Repository

### Core Explanation

Publish validated packages to a repository rather than copying files manually.

### Example / Visualization

```text
CI → artifact repo
```

### Why It Matters

Separates build and deployment lifecycles.

# Part 95 — Container Registry

### Core Explanation

Publish container images to a controlled registry with immutable identity.

### Example / Visualization

```text
image tag + digest
```

### Why It Matters

Registry is a critical supply-chain component.

# Part 96 — Artifact Immutability

### Core Explanation

Do not overwrite published release versions.

### Example / Visualization

```text
2.4.1 fixed forever
```

### Why It Matters

Makes rollback and audit reliable.

# Part 97 — Artifact Metadata

### Core Explanation

Store commit SHA, build ID, tests, SBOM, provenance, and signature with the artifact.

### Example / Visualization

```text
artifact metadata manifest
```

### Why It Matters

Connects production to CI evidence.

# Part 98 — Artifact Retention

### Core Explanation

Define retention by artifact type and environment.

### Example / Visualization

```text
snapshots 14d, prod releases longer
```

### Why It Matters

Preserve rollback and audit evidence.

# Part 99 — Artifact Promotion

### Core Explanation

Promote the same artifact instead of rebuilding per environment.

### Example / Visualization

```text
digest X → dev → stage → prod
```

### Why It Matters

Preserves test evidence.

# Part 100 — Release Candidate

### Core Explanation

A release candidate is a validated artifact considered for promotion, not a separately rebuilt product.

### Example / Visualization

```text
app 2.4.0-rc1
```

### Why It Matters

Supports controlled release decisions.

# Part 101 — CI Secrets

### Core Explanation

Secrets required by CI should be stored in protected secret stores, not repository YAML.

### Example / Visualization

```text
secret store → job env/file
```

### Why It Matters

Pipeline code is not a secret vault.

# Part 102 — Environment-Scoped Secrets

### Core Explanation

Production secrets should be exposed only to protected production workflows.

### Example / Visualization

```text
PR jobs cannot read prod secret
```

### Why It Matters

Reduces blast radius.

# Part 103 — OIDC Federation

### Core Explanation

CI can exchange its workload identity for short-lived cloud credentials.

### Example / Visualization

```text
CI OIDC → cloud STS → temporary role
```

### Why It Matters

Eliminates many static keys.

# Part 104 — Least Privilege CI Identity

### Core Explanation

Build jobs and deploy jobs should have separate permissions.

### Example / Visualization

```text
build: repo+registry
apply: environment only
```

### Why It Matters

A compromised build should not automatically control production.

# Part 105 — Fork PR Security

### Core Explanation

Untrusted fork pull requests should not automatically receive organization secrets or privileged runners.

### Example / Visualization

```text
fork PR → unprivileged validation
```

### Why It Matters

Prevents secret theft through malicious CI code.

# Part 106 — Untrusted Pipeline Code

### Core Explanation

A PR can modify pipeline definitions. Privileged workflows must not blindly execute untrusted changes with secrets.

### Example / Visualization

```text
workflow changes require review
```

### Why It Matters

Pipeline code is executable supply-chain code.

# Part 107 — Self-Hosted Runner Isolation

### Core Explanation

Never let untrusted PR code run on a persistent privileged runner without isolation.

### Example / Visualization

```text
ephemeral/isolated runners
```

### Why It Matters

A malicious build can persist on the host.

# Part 108 — CI Network Segmentation

### Core Explanation

Runners should have only the network access required for their role.

### Example / Visualization

```text
build runner no prod DB route
```

### Why It Matters

Network controls reinforce least privilege.

# Part 109 — Dependency Proxy

### Core Explanation

Proxy external packages through trusted internal registries where useful.

### Example / Visualization

```text
CI → internal proxy → upstream
```

### Why It Matters

Improves availability, caching, and policy.

# Part 110 — Pin CI Actions/Plugins

### Core Explanation

Third-party CI actions/plugins are executable dependencies and should be version-controlled or pinned appropriately.

### Example / Visualization

```text
action@immutable-version/commit
```

### Why It Matters

Reduces supply-chain drift.

# Part 111 — CI Plugin Governance

### Core Explanation

Jenkins plugins, GitHub actions, GitLab components, and extensions require inventory and upgrade governance.

### Example / Visualization

```text
approved plugin catalog
```

### Why It Matters

Extensions expand attack surface.

# Part 112 — Runner Image Governance

### Core Explanation

Maintain approved runner/build images with patch cadence and scanning.

### Example / Visualization

```text
ci-runner-image:v12
```

### Why It Matters

Build infrastructure also requires lifecycle management.

# Part 113 — CI Audit Logs

### Core Explanation

Retain who triggered, approved, reran, cancelled, and changed pipeline configuration.

### Example / Visualization

```text
CI audit events
```

### Why It Matters

Useful for incident and compliance investigation.

# Part 114 — Pipeline Evidence

### Core Explanation

Store test reports, security results, plan output, provenance, and approvals as governed artifacts.

### Example / Visualization

```text
run 481 evidence bundle
```

### Why It Matters

CI is a source of release evidence.

# Part 115 — Build Hermeticity

### Core Explanation

A hermetic build minimizes undeclared dependencies on external machine state/network.

### Example / Visualization

```text
all inputs declared
```

### Why It Matters

Improves reproducibility.

# Part 116 — Offline/Reproducible Build Strategy

### Core Explanation

Critical environments may mirror dependencies so builds do not depend directly on changing Internet sources.

### Example / Visualization

```text
internal registry/cache
```

### Why It Matters

Improves resilience and control.

# Part 117 — CI Supply Chain Threat Model

### Core Explanation

Threat-model source repo, runner, dependencies, CI platform, credentials, artifacts, and registry.

### Example / Visualization

```text
Git → CI → artifact → deploy
```

### Why It Matters

Compromise anywhere can affect production.

# Part 118 — Malicious Dependency

### Core Explanation

Dependency compromise can enter through package resolution.

### Example / Visualization

```text
trusted lock/proxy/scanning
```

### Why It Matters

Dependency governance matters.

# Part 119 — Typosquatting

### Core Explanation

Package names similar to legitimate dependencies can trick automated builds.

### Example / Visualization

```text
reqeusts vs requests
```

### Why It Matters

Review dependency additions.

# Part 120 — Secret Redaction

### Core Explanation

CI platforms should mask secrets in logs, but masking is not a guarantee if code transforms/encodes the value.

### Example / Visualization

```text
masked env ≠ impossible to exfiltrate
```

### Why It Matters

Do not expose unnecessary secrets to jobs.

# Part 121 — Debug Logging Risk

### Core Explanation

Verbose build/debug modes may print credentials or internal data.

### Example / Visualization

```text
set -x / provider debug logs
```

### Why It Matters

Use temporarily and protect logs.

# Part 122 — Artifact Download Permissions

### Core Explanation

Not every developer or external user should read all artifacts, especially proprietary or sensitive packages.

### Example / Visualization

```text
repo RBAC
```

### Why It Matters

Artifact access is an information-security boundary.

# Part 123 — SBOM Retention

### Core Explanation

Keep SBOMs for released artifacts as long as vulnerability response requires.

### Example / Visualization

```text
release → SBOM retained
```

### Why It Matters

Needed when a new CVE appears months later.

# Part 124 — Provenance Verification

### Core Explanation

Deployment systems can verify artifact provenance before promotion.

### Example / Visualization

```text
trusted builder required
```

### Why It Matters

Prevents untrusted artifacts from entering release flow.

# Part 125 — Policy Exceptions

### Core Explanation

Exceptions need reason, scope, owner, and expiration.

### Example / Visualization

```text
temporary waiver until date
```

### Why It Matters

Avoid permanent hidden bypasses.

# Part 126 — Security Feedback UX

### Core Explanation

Findings should link to file, line, severity, fix guidance, and policy context.

### Example / Visualization

```text
actionable finding
```

### Why It Matters

Poor UX drives bypass behavior.

# Part 127 — Security Scan Performance

### Core Explanation

Run very fast checks on PR; schedule expensive deep scans where appropriate.

### Example / Visualization

```text
secret scan seconds; full DAST later
```

### Why It Matters

Balance feedback and cost.

# Part 128 — GitHub Actions Concept

### Core Explanation

GitHub Actions defines workflows triggered by repository events, containing jobs and steps executed on runners.

### Example / Visualization

```text
workflow → job → steps
```

### Why It Matters

Useful example of pipeline-as-code.

# Part 129 — GitHub Actions Workflow

### Core Explanation

A workflow file lives under `.github/workflows/` and can trigger on pull_request, push, schedule, or manual dispatch.

### Example / Visualization

```text
on: pull_request
```

### Why It Matters

Keep workflow permissions explicit.

# Part 130 — GitHub Actions Job

### Core Explanation

Jobs run on selected runners and can depend on other jobs using needs.

### Example / Visualization

```text
needs: build
```

### Why It Matters

DAG relationships improve speed.

# Part 131 — GitHub Actions Matrix

### Core Explanation

Strategy matrices run jobs across multiple combinations.

### Example / Visualization

```text
python-version: [3.12,3.13]
```

### Why It Matters

Good for compatibility testing.

# Part 132 — GitHub Actions Permissions

### Core Explanation

Workflow token permissions should be explicitly minimized.

### Example / Visualization

```text
permissions: contents: read
```

### Why It Matters

Defaults may be broader than required.

# Part 133 — GitLab CI Concept

### Core Explanation

GitLab CI uses `.gitlab-ci.yml` with stages/jobs/rules and GitLab runners.

### Example / Visualization

```text
stages: [validate,test,build]
```

### Why It Matters

Strong integrated source+CI model.

# Part 134 — GitLab Rules

### Core Explanation

Rules control whether jobs run based on branch, file changes, variables, or pipeline source.

### Example / Visualization

```text
rules: changes:
```

### Why It Matters

Useful for monorepos and cost control.

# Part 135 — GitLab Artifacts

### Core Explanation

Jobs can publish artifacts/reports consumed by later jobs or displayed in merge requests.

### Example / Visualization

```text
artifacts: reports:
```

### Why It Matters

Evidence should be structured.

# Part 136 — Jenkins Concept

### Core Explanation

Jenkins is an extensible automation server often using Pipeline/Jenkinsfile plus agents and plugins.

### Example / Visualization

```text
controller → agents → stages
```

### Why It Matters

Powerful but operationally heavier.

# Part 137 — Jenkinsfile

### Core Explanation

Declarative or scripted pipelines can be stored in source control.

### Example / Visualization

```text
pipeline { stages { ... } }
```

### Why It Matters

Pipeline-as-code improves auditability.

# Part 138 — Jenkins Controller Security

### Core Explanation

The controller should not execute untrusted builds directly and requires careful plugin/credential governance.

### Example / Visualization

```text
controller != general build worker
```

### Why It Matters

Persistent control plane compromise is high impact.

# Part 139 — Jenkins Shared Libraries

### Core Explanation

Reusable pipeline logic can be centralized through shared libraries.

### Example / Visualization

```text
common ci functions
```

### Why It Matters

Version and test shared libraries because many repositories depend on them.

# Part 140 — Azure DevOps Pipelines Concept

### Core Explanation

Azure Pipelines uses YAML pipelines with stages/jobs/steps and Microsoft-hosted or self-hosted agents.

### Example / Visualization

```text
stages → jobs → steps
```

### Why It Matters

Another common enterprise CI model.

# Part 141 — Azure Service Connections

### Core Explanation

External cloud access should use scoped service connections/workload identity rather than shared admin credentials.

### Example / Visualization

```text
pipeline → service connection
```

### Why It Matters

Identity boundaries matter.

# Part 142 — Reusable CI Templates

### Core Explanation

Organizations should publish reusable templates for standard validation, build, scan, and artifact patterns.

### Example / Visualization

```text
include template ci/python.yml
```

### Why It Matters

Reduces duplicated pipeline code.

# Part 143 — Template Versioning

### Core Explanation

Reusable pipeline templates are shared software and should be versioned/tested.

### Example / Visualization

```text
template v3.2
```

### Why It Matters

Breaking changes can affect many teams.

# Part 144 — Pipeline Parameterization

### Core Explanation

Templates should accept clear parameters rather than copy-paste modifications.

### Example / Visualization

```text
language_version, test_command
```

### Why It Matters

Balances reuse and flexibility.

# Part 145 — Pipeline Composition

### Core Explanation

Compose smaller reusable workflows rather than one giant template with dozens of flags.

### Example / Visualization

```text
build template + scan template + publish template
```

### Why It Matters

Improves maintainability.

# Part 146 — Monorepo Pipeline Orchestration

### Core Explanation

Large monorepos may use dependency graphs to build affected projects and shared dependencies.

### Example / Visualization

```text
changed package → affected graph
```

### Why It Matters

Avoid full-repo rebuild when unnecessary.

# Part 147 — Polyrepo Integration CI

### Core Explanation

Cross-service contracts and versioned dependencies are important because services integrate after separate CI pipelines.

### Example / Visualization

```text
contract tests + versioned API
```

### Why It Matters

CI must still validate distributed compatibility.

# Part 148 — CI Queue Time

### Core Explanation

Measure how long jobs wait for runners.

### Example / Visualization

```text
queued 8m, run 3m
```

### Why It Matters

High queue time indicates insufficient capacity or poor scheduling.

# Part 149 — CI Execution Time

### Core Explanation

Measure actual pipeline/job duration separately from queue time.

### Example / Visualization

```text
queue 10m + run 5m
```

### Why It Matters

Different problems require different fixes.

# Part 150 — CI Success Rate

### Core Explanation

Track pipeline failures by category: code, test flake, infrastructure, dependency, runner, auth.

### Example / Visualization

```text
failure taxonomy
```

### Why It Matters

Helps prioritize platform improvements.

# Part 151 — CI Reliability SLO

### Core Explanation

Treat CI as an internal service with availability and latency expectations.

### Example / Visualization

```text
95% PR checks start within 2m
```

### Why It Matters

Broken CI blocks developer flow.

# Part 152 — Runner Utilization

### Core Explanation

Monitor runner CPU/memory utilization and concurrency.

### Example / Visualization

```text
runner saturation 90%
```

### Why It Matters

Capacity problems create queue delays.

# Part 153 — Autoscaling Runners

### Core Explanation

Self-hosted runner fleets can scale based on queue demand.

### Example / Visualization

```text
queue↑ → runners↑
```

### Why It Matters

Must preserve isolation and cleanup.

# Part 154 — Warm vs Cold Runners

### Core Explanation

Warm runners reduce startup time but retain state; cold ephemeral runners improve isolation.

### Example / Visualization

```text
warm=fast, cold=clean
```

### Why It Matters

Choose according to security/performance trade-off.

# Part 155 — CI Cost Management

### Core Explanation

CI cost depends on runner minutes, hardware size, parallelism, cache efficiency, and unnecessary jobs.

### Example / Visualization

```text
cost per pipeline
```

### Why It Matters

Optimize after protecting feedback quality.

# Part 156 — Critical Path

### Core Explanation

The pipeline critical path is the longest dependent chain determining total duration.

### Example / Visualization

```text
build 5m → integration 15m → package 2m = 22m
```

### Why It Matters

Parallelizing non-critical jobs may not improve total time.

# Part 157 — Pipeline Profiling

### Core Explanation

Measure duration per job/step to find bottlenecks.

### Example / Visualization

```text
dependency install 6m → cache candidate
```

### Why It Matters

Optimize based on evidence.

# Part 158 — Test Selection

### Core Explanation

Run a minimal safe test subset for changed components while retaining scheduled/full regression coverage.

### Example / Visualization

```text
PR affected tests; nightly full
```

### Why It Matters

Requires trustworthy dependency mapping.

# Part 159 — Nightly CI

### Core Explanation

Scheduled pipelines can run expensive regression, compatibility, performance, or security suites.

### Example / Visualization

```text
nightly full test
```

### Why It Matters

Do not use nightly runs as a substitute for essential PR checks.

# Part 160 — Pre-Merge vs Post-Merge CI

### Core Explanation

Pre-merge validates candidate changes; post-merge verifies actual integrated mainline state.

### Example / Visualization

```text
PR tests ≠ merged-main tests
```

### Why It Matters

Both matter in high-change repositories.

# Part 161 — Merge Queue

### Core Explanation

A merge queue tests changes against an up-to-date integration base before final merge.

### Example / Visualization

```text
PRs → queue → combined validation → main
```

### Why It Matters

Prevents individually green PRs from breaking main when combined.

# Part 162 — Rebase Before Merge

### Core Explanation

Keeping PR branches current with main can reduce integration surprises but may trigger repeated CI.

### Example / Visualization

```text
update branch → rerun checks
```

### Why It Matters

Balance freshness with compute cost.

# Part 163 — Broken Main Response

### Core Explanation

When main is broken, prioritize restoration: revert, fix-forward, or disable faulty change.

### Example / Visualization

```text
stop-the-line
```

### Why It Matters

Teams should not pile more changes onto broken main.

# Part 164 — Stop-the-Line Culture

### Core Explanation

A failing main branch or critical CI system becomes a team priority rather than someone else's issue.

### Example / Visualization

```text
main red → swarm to restore
```

### Why It Matters

Protects integration health.

# Part 165 — CI Runbook

### Core Explanation

Maintain runbooks for runner outage, registry outage, dependency outage, secret issue, cache corruption, and CI platform incident.

### Example / Visualization

```text
symptom → evidence → recovery
```

### Why It Matters

CI itself requires operations.

# Part 166 — Dependency Outage

### Core Explanation

If an external package registry fails, internal mirrors/caches can keep builds running.

### Example / Visualization

```text
upstream down → internal proxy
```

### Why It Matters

CI resilience depends on external services.

# Part 167 — Registry Outage

### Core Explanation

Builds may succeed but publication fail. Preserve artifacts/evidence and retry publication safely after recovery.

### Example / Visualization

```text
build artifact retained
```

### Why It Matters

Avoid rebuilding if the original artifact can be promoted later.

# Part 168 — CI Platform DR

### Core Explanation

Source and pipeline definitions should be recoverable, along with secrets integration, runners, and artifact metadata.

### Example / Visualization

```text
Git backup + IaC + runbooks
```

### Why It Matters

CI is part of the delivery control plane.

# Part 169 — CI Migration

### Core Explanation

Moving CI platforms requires mapping triggers, secrets, runners, artifacts, approvals, templates, and status checks.

### Example / Visualization

```text
old CI → dual-run → new CI
```

### Why It Matters

Do not migrate only YAML syntax.

# Part 170 — CI Anti-Pattern: One Giant Job

### Core Explanation

A 60-minute job hides failure boundaries and cannot parallelize.

### Example / Visualization

```text
one script does everything
```

### Why It Matters

Split by logical stages/jobs with artifact boundaries.

# Part 171 — CI Anti-Pattern: Hidden UI Configuration

### Core Explanation

Pipelines configured only in web UI are difficult to review/reproduce.

### Example / Visualization

```text
manual UI steps ✗
```

### Why It Matters

Prefer pipeline-as-code.

# Part 172 — CI Anti-Pattern: Permanent Shared Workspace

### Core Explanation

Persistent files from prior jobs create nondeterministic builds.

### Example / Visualization

```text
dirty runner workspace
```

### Why It Matters

Use clean/ephemeral workspaces.

# Part 173 — CI Anti-Pattern: Secrets Everywhere

### Core Explanation

Global secrets available to every job increase blast radius.

### Example / Visualization

```text
all jobs get prod key ✗
```

### Why It Matters

Scope by environment/job.

# Part 174 — CI Anti-Pattern: Rerun Until Green

### Core Explanation

Repeated reruns conceal flaky tests or infrastructure defects.

### Example / Visualization

```text
red → rerun → green
```

### Why It Matters

Fix the cause.

# Part 175 — CI Anti-Pattern: Slow PR Feedback

### Core Explanation

A two-hour PR pipeline encourages developers to batch changes and bypass checks.

### Example / Visualization

```text
feedback arrives after context switch
```

### Why It Matters

Optimize the critical path.

# Part 176 — CI Anti-Pattern: Build Different in Prod

### Core Explanation

If production rebuilds source, tested artifact identity is lost.

### Example / Visualization

```text
test artifact A, prod rebuild B
```

### Why It Matters

Build once, deploy many.

# Part 177 — CI Anti-Pattern: Mutable Dependencies

### Core Explanation

Using unpinned dependencies makes historical builds irreproducible.

### Example / Visualization

```text
latest dependency
```

### Why It Matters

Pin/lock and upgrade deliberately.

# Part 178 — CI Anti-Pattern: Over-Parallelization

### Core Explanation

Excessive parallelism can hit quotas, overload dependencies, or increase cost without reducing the critical path.

### Example / Visualization

```text
100 jobs, same bottleneck
```

### Why It Matters

Parallelize meaningful independent work.

# Part 179 — CI Troubleshooting Framework

### Core Explanation

Diagnose in layers: trigger → checkout → environment → dependency → build → test → security → artifact → publication.

### Example / Visualization

```text
layer-by-layer
```

### Why It Matters

Avoid random reruns.

# Part 180 — Trigger Failure

### Core Explanation

If pipeline never starts, check event filters, branch/path rules, repository permissions, webhook/event delivery, and CI configuration validity.

### Example / Visualization

```text
no run created
```

### Why It Matters

This is different from a failed job.

# Part 181 — Checkout Failure

### Core Explanation

Check repository access, submodules, Git LFS, network, commit existence, and token permissions.

### Example / Visualization

```text
fatal: repository not found
```

### Why It Matters

Do not debug application code first.

# Part 182 — Dependency Failure

### Core Explanation

Check registry availability, lockfile, proxy, certificates, credentials, and cache corruption.

### Example / Visualization

```text
package install 403/timeout
```

### Why It Matters

Dependency restoration is its own failure layer.

# Part 183 — Build Failure

### Core Explanation

Inspect compiler/build output, environment versions, generated files, and changed inputs.

### Example / Visualization

```text
compile error
```

### Why It Matters

Reproduce with the same build container/toolchain.

# Part 184 — Test Failure

### Core Explanation

Distinguish deterministic code defect, test defect, shared-state interference, timeout, and environment failure.

### Example / Visualization

```text
same commit repeated
```

### Why It Matters

Classify before deciding retry.

# Part 185 — Security Scan Failure

### Core Explanation

Review the exact finding, policy threshold, exploitability/context, suppression process, and remediation.

### Example / Visualization

```text
critical CVE blocks
```

### Why It Matters

Do not simply disable the scanner.

# Part 186 — Artifact Publication Failure

### Core Explanation

Check repository auth, quota, naming/version collision, network, and immutable-version policy.

### Example / Visualization

```text
409 version exists
```

### Why It Matters

Preserve the already-built artifact if possible.

# Part 187 — Runner Failure

### Core Explanation

Check runner registration, health, disk, memory, network, executor, certificates, and capacity.

### Example / Visualization

```text
job stuck queued
```

### Why It Matters

CI platform operations require infrastructure troubleshooting.

# Part 188 — CI Final Mental Model

### Core Explanation

CI is a rapid integration feedback system that turns small source changes into trusted evidence and immutable artifacts.

### Example / Visualization

```text
Change → Evidence → Artifact
```

### Why It Matters

The system must be fast, trustworthy, secure, and reproducible.


# Supplemental Deep-Study Layer — Continuous Integration

> **Source distinction:** The uploaded Course 66 remains preserved in full. The section below extends it with merge-queue correctness, runner trust zones, ephemeral execution, OIDC, cache poisoning controls, hermetic/reproducible builds, dependency supply-chain defenses, artifact lineage, SBOM/provenance/signing, advanced test engineering, Kubernetes runner security, policy governance, CI observability/SLOs, platform DR, and evidence-first troubleshooting.

Preferred learning flow:

```text
Integration risk
  ↓
Trigger / branch policy
  ↓
Runner + identity
  ↓
Reproducible build
  ↓
Tests / scans / policies
  ↓
Artifact + provenance
  ↓
Feedback
  ↓
Metrics / improvement
```


## Advanced Deep Dive 1 — Pre-Merge Test Merge Commit

### Concept

A PR can be green against its own branch but fail after merge because main changed. CI can test the effective merge result or use a merge queue so validation reflects the integration state.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
main A-B-C
PR branch A-X
CI tests merge(C,X), not only X alone
```

### Expected Evidence

The validated commit is close to the commit that will enter main.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Validate the integrated result before final merge.

---

## Advanced Deep Dive 2 — Merge Queue Serialization

### Concept

A merge queue orders candidate changes and validates each against an updated base, preventing multiple individually green PRs from combining into a broken mainline.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR1 green
PR2 green
queue:
test main+PR1
then main+PR1+PR2
```

### Expected Evidence

Main remains protected from stale-base races.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use merge queues in high-change repositories with strict mainline health.

---

## Advanced Deep Dive 3 — Branch Protection as Policy

### Concept

Protected branches convert process expectations into enforceable controls: required reviews, passing checks, restricted force pushes, and signed or verified changes.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
main:
require PR
require 2 reviews
require CI
block force push
```

### Expected Evidence

Direct unsafe integration paths are removed.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Treat branch protection as production policy.

---

## Advanced Deep Dive 4 — Status Check Design

### Concept

Too few required checks weakens safety; too many noisy checks makes developers bypass CI. Required checks should be fast, deterministic, and high-signal.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
required:
build
unit
security-critical
merge validation

informational:
deep scan
nightly performance
```

### Expected Evidence

Merge blocking reflects actual confidence.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Only make a check required when the team trusts its signal.

---

## Advanced Deep Dive 5 — PR Size Guardrail

### Concept

Very large PRs increase review latency and defect probability. Automated warnings can encourage smaller batches without blocking legitimate generated changes.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```python
changed_lines = 1800
if changed_lines > 800:
    print("Warning: consider splitting this PR")
```

### Expected Evidence

Large change sets are surfaced early.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Prefer guidance and ownership over arbitrary hard limits.

---

## Advanced Deep Dive 6 — Review Queue SLO

### Concept

Code review is part of CI flow. A repository can define an internal SLO such as first review within four working hours.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
SLI: PRs reviewed within 4h
SLO: >= 90%
```

### Expected Evidence

Review delay becomes measurable alongside pipeline delay.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Optimize human queues as seriously as runner queues.

---

## Advanced Deep Dive 7 — Pipeline Critical Path

### Concept

Total CI time is determined by the longest dependency chain, not the sum of every job. Optimizing work outside the critical path may not improve feedback time.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
build 5m → integration 18m → package 2m = 25m
lint 4m parallel
scan 7m parallel
critical path = 25m
```

### Expected Evidence

The true latency bottleneck is identified.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Profile the DAG before adding parallelism.

---

## Advanced Deep Dive 8 — Queue Time vs Run Time

### Concept

A five-minute test can still provide 20-minute feedback if it waits 15 minutes for a runner. Capacity planning must separate queue and execution time.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```python
queue=15
run=5
print("Feedback time:", queue+run, "minutes")
```

### Expected Evidence

Runner saturation becomes distinguishable from slow tests.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Track queue p50/p95 separately from job duration.

---

## Advanced Deep Dive 9 — Runner Capacity Headroom

### Concept

A CI fleet sized to average load develops long queues during synchronized PR bursts, releases, or outages.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
average demand: 20 jobs
burst: 60 jobs
runner capacity: 25
→ queue
```

### Expected Evidence

Burst behavior is included in capacity design.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Maintain autoscaling or reserved headroom for peak feedback demand.

---

## Advanced Deep Dive 10 — Runner Autoscaling Signal

### Concept

Autoscaling on CPU alone may miss queued work. Queue depth and queue age are direct demand signals for ephemeral runner fleets.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
queue depth ↑
oldest queued job age ↑
→ add runners
```

### Expected Evidence

Scaling responds to developer waiting time.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Scale from demand while enforcing upper cost limits.

---

## Advanced Deep Dive 11 — Ephemeral Runner Lifecycle

### Concept

A secure self-hosted runner can be created for one job, registered with short-lived credentials, execute, upload evidence, scrub, and be destroyed.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
request
→ provision runner
→ register
→ execute one job
→ upload results
→ destroy
```

### Expected Evidence

Cross-job persistence is eliminated.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Prefer ephemeral runners for privileged or untrusted workloads.

---

## Advanced Deep Dive 12 — Runner Trust Zones

### Concept

Different jobs need different network and credential access. Separate public PR, internal build, release signing, and production deployment runners.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
Zone A: fork PR, no secrets
Zone B: internal CI
Zone C: signing
Zone D: production deploy
```

### Expected Evidence

Compromise of a low-trust job cannot directly reach high-trust systems.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Route jobs by trust requirement, not convenience.

---

## Advanced Deep Dive 13 — Fork PR Isolation

### Concept

External contribution code is untrusted. Fork PRs should not receive organization secrets or execute on persistent privileged runners.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
fork PR
→ read-only checkout
→ no prod secrets
→ ephemeral hosted/isolated runner
```

### Expected Evidence

Malicious pipeline code has limited capability.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Treat repository code as executable input.

---

## Advanced Deep Dive 14 — pull_request vs Privileged Event Semantics

### Concept

CI platforms may expose different trust contexts for PR events. Privileged workflows that run base-repository code must never check out and execute untrusted PR code with secrets.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
trusted workflow logic
+ untrusted PR contents
+ secret
= high-risk combination
```

### Expected Evidence

Workflow event choice is treated as a security design decision.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Separate untrusted validation from privileged follow-up jobs.

---

## Advanced Deep Dive 15 — Workflow Token Minimization

### Concept

Default CI tokens can have more repository permissions than a job needs. Explicitly scope read/write permissions.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```yaml
permissions:
  contents: read
  packages: write
  id-token: write
```

### Expected Evidence

The workflow has a visible minimal permission set.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Grant write permissions only to jobs that truly publish/change something.

---

## Advanced Deep Dive 16 — OIDC Claim Restriction

### Concept

Federated cloud access should trust not just the CI issuer but also repository, branch/tag, environment, workflow, and audience claims.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
Allow role if:
repo=org/app
ref=refs/heads/main
environment=prod
aud=cloud-sts
```

### Expected Evidence

A token from another repository or branch cannot assume the role.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Constrain federation with contextual claims.

---

## Advanced Deep Dive 17 — Short-Lived Release Credentials

### Concept

Release jobs should exchange workload identity for credentials that expire automatically instead of using static cloud keys or kubeconfigs.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI OIDC
→ STS
→ 30-minute role credential
→ deploy
```

### Expected Evidence

Credential lifetime matches the job.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Prefer federated identity for CI/CD.

---

## Advanced Deep Dive 18 — Secret Fan-Out Analysis

### Concept

One secret injected into twenty jobs creates twenty exposure paths. Map which jobs genuinely need the value.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
prod token
currently → 18 jobs
required → 1 deploy job
```

### Expected Evidence

Credential exposure is reduced by design.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Scope secrets by job, environment, and trust zone.

---

## Advanced Deep Dive 19 — Secret Redaction Limits

### Concept

Log masking is not a security boundary. Malicious code can transform, encode, split, or transmit a secret.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
masked SECRET
→ base64/HTTP exfiltration still possible
```

### Expected Evidence

The design no longer relies on console masking for containment.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Do not expose secrets to untrusted code in the first place.

---

## Advanced Deep Dive 20 — Shell Trace Risk

### Concept

`set -x`, verbose package managers, and debug modes can print commands and expanded credentials into durable logs.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
set +x
# perform secret-bearing command
set -x
```

### Expected Evidence

Sensitive command output is excluded from logs.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Disable shell tracing around credentials and use stdin/file mechanisms.

---

## Advanced Deep Dive 21 — Pipeline Definition Review

### Concept

CI YAML, Jenkinsfiles, shared libraries, and reusable actions are executable production-supply-chain code and need the same review rigor as application code.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
pipeline change
→ code review
→ security checks
→ protected merge
```

### Expected Evidence

A pipeline privilege change cannot bypass peer review.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Protect CI configuration paths explicitly.

---

## Advanced Deep Dive 22 — Shared Workflow Version Pinning

### Concept

Reusable workflows and CI actions are dependencies. Pinning immutable commits or controlled versions reduces surprise behavior changes.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
uses: org/security-workflow@<approved-commit>
```

### Expected Evidence

A historical CI run can identify the exact workflow implementation.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Upgrade shared workflow versions deliberately.

---

## Advanced Deep Dive 23 — Jenkins Plugin Attack Surface

### Concept

Plugins execute inside or alongside the CI control plane and can introduce vulnerabilities, dependency conflicts, and upgrade risk.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
plugin inventory
→ approved list
→ patch cadence
→ remove unused
```

### Expected Evidence

Plugin footprint is measurable and governable.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Minimize plugins and maintain an ownership/upgrade process.

---

## Advanced Deep Dive 24 — Controller/Runner Separation

### Concept

A CI controller should orchestrate work, not execute arbitrary untrusted builds on the same persistent host.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
controller
  ↓ schedules
ephemeral agents
  ↓ execute jobs
```

### Expected Evidence

Build compromise is less likely to compromise the control plane.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep execution isolated from CI control-plane state.

---

## Advanced Deep Dive 25 — Runner Image Supply Chain

### Concept

Runner images contain compilers, CLIs, scanners, package managers, CAs, and credentials helpers. They need versioning, patching, scanning, and provenance.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
base OS
→ tool install
→ scan
→ sign
→ runner-image:v12
```

### Expected Evidence

Build infrastructure can be traced to an approved image version.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Treat runner images as production artifacts.

---

## Advanced Deep Dive 26 — Build Container Pinning

### Concept

Containerized jobs should pin build images by controlled version or digest so toolchain changes do not silently alter build results.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```yaml
container:
  image: registry.example/ci/python@sha256:...
```

### Expected Evidence

The CI toolchain is immutable for the run.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Promote build images like any other critical dependency.

---

## Advanced Deep Dive 27 — Hermetic Build Boundary

### Concept

A hermetic build declares its inputs and minimizes dependence on host files, time, locale, network, or mutable package repositories.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
declared source
+ lockfile
+ compiler image
+ vendored/mirrored deps
→ artifact
```

### Expected Evidence

The same inputs can reproduce equivalent output.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Remove undeclared environmental inputs incrementally.

---

## Advanced Deep Dive 28 — SOURCE_DATE_EPOCH Concept

### Concept

Timestamps embedded during builds can break byte-for-byte reproducibility. Reproducible-build techniques normalize time and metadata where supported.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
export SOURCE_DATE_EPOCH="$(git log -1 --pretty=%ct)"
```

### Expected Evidence

Timestamp-sensitive build steps can use a deterministic source time.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use ecosystem-specific reproducible-build guidance.

---

## Advanced Deep Dive 29 — Locale and Timezone Reproducibility

### Concept

Tests and builds can change behavior across locales/timezones. CI should set them explicitly when relevant.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
export TZ=UTC
export LC_ALL=C.UTF-8
```

### Expected Evidence

Date/string behavior becomes predictable across runners.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Control locale/timezone inputs instead of relying on host defaults.

---

## Advanced Deep Dive 30 — Dependency Lock Integrity

### Concept

Lock files are executable supply-chain inputs. CI should verify they match manifests and fail if generated dependency state is inconsistent.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
npm ci
# or equivalent frozen-lockfile mode
```

### Expected Evidence

CI installs exactly what the lock file describes.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use frozen/immutable dependency install modes.

---

## Advanced Deep Dive 31 — Dependency Confusion Defense

### Concept

Private package names can be hijacked from public registries if resolver precedence is misconfigured.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
@company/internal-lib
→ internal registry namespace
not public fallback
```

### Expected Evidence

Private package resolution cannot silently fall through to an attacker-controlled source.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Reserve namespaces and configure scoped registries.

---

## Advanced Deep Dive 32 — Typosquatting Review

### Concept

New dependency names should be reviewed because automated package installation can pull similarly named malicious projects.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
requests
vs
reqeusts
```

### Expected Evidence

Dependency additions receive explicit human/tool review.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Require approval for new external dependencies.

---

## Advanced Deep Dive 33 — Internal Dependency Proxy

### Concept

A controlled proxy improves cache performance, availability, policy, and visibility while reducing direct Internet dependency.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI
  ↓ internal package proxy
  ↓ approved upstream registries
```

### Expected Evidence

Builds continue during some upstream outages and package access is logged.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Harden the proxy as critical supply-chain infrastructure.

---

## Advanced Deep Dive 34 — Cache Trust Domains

### Concept

Caches generated by untrusted branches should not be consumed by privileged release workflows because cache contents can be attacker-controlled.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
fork cache namespace
≠ trusted-main cache namespace
```

### Expected Evidence

Cross-trust cache poisoning is prevented.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Partition cache keys and permissions by trust level.

---

## Advanced Deep Dive 35 — Cache Key Completeness

### Concept

A cache key should include every input that determines cached validity: OS, architecture, runtime, lockfile, build flags, and sometimes compiler/tool version.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
linux-amd64-python3.13-<lock-hash>
```

### Expected Evidence

Relevant input changes invalidate stale cache data.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Prefer under-caching to silently reusing incompatible output.

---

## Advanced Deep Dive 36 — Remote Build Cache

### Concept

Large monorepos can reuse compilation outputs across machines when cache keys are content-addressed and trust is controlled.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
source/action digest
→ remote cache
→ verified build output
```

### Expected Evidence

Repeated builds avoid recomputing unchanged actions.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Treat remote cache as supply-chain data, not only performance data.

---

## Advanced Deep Dive 37 — Cache Poisoning Detection

### Concept

A suspicious cache hit can be investigated by rebuilding with cache disabled and comparing outputs.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
cached build artifact A
clean rebuild artifact B
compare digests
```

### Expected Evidence

Mismatch proves the cache influenced output unexpectedly.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep a clean-build troubleshooting path.

---

## Advanced Deep Dive 38 — Artifact vs Cache Enforcement

### Concept

Release artifacts should be stored in durable immutable repositories with metadata; caches should be assumed disposable.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
cache retention: days
release artifact retention: policy-driven
```

### Expected Evidence

A cache purge cannot remove the only deployable release.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Never promote from a transient cache.

---

## Advanced Deep Dive 39 — Build Once Evidence

### Concept

CI should publish one immutable artifact and attach commit SHA, build ID, toolchain, tests, SBOM, and provenance.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```json
{"commit":"abc123","build":"5821","digest":"sha256:...","toolchain":"ci-image:v12"}
```

### Expected Evidence

Artifact lineage is queryable from one record.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Make artifact publication the terminal CI contract.

---

## Advanced Deep Dive 40 — Artifact Immutability Policy

### Concept

Repositories should reject overwriting existing release versions/tags where feasible.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
push app:2.4.1 once
second push same immutable release → reject
```

### Expected Evidence

Historical release identity remains trustworthy.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Publish a new version for every changed artifact.

---

## Advanced Deep Dive 41 — Container Digest Capture

### Concept

After pushing an image, CI should record the registry-resolved immutable digest for downstream promotion.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
# Example concept; command depends on registry tooling
echo "repo/app@sha256:..."
```

### Expected Evidence

CD can deploy an immutable reference rather than a mutable tag.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Pass the digest as pipeline output/evidence.

---

## Advanced Deep Dive 42 — SBOM Generation Placement

### Concept

Generate an SBOM from the built artifact or image so it describes what will actually be released, not only source manifests.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
source manifests
→ build artifact
→ artifact/image SBOM
```

### Expected Evidence

The SBOM corresponds to production bits.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Retain SBOM with artifact lineage.

---

## Advanced Deep Dive 43 — Provenance Attestation

### Concept

Provenance should identify source, build recipe, builder identity, and artifact digest so consumers can verify how the artifact was produced.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
subject: sha256:artifact
builder: ci-prod-builder
source: commit abc123
```

### Expected Evidence

Artifact origin can be evaluated programmatically.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Generate provenance inside the trusted build boundary.

---

## Advanced Deep Dive 44 — Artifact Signing Identity

### Concept

Signing proves that an expected identity approved or produced an artifact. Keyless identity-based signing can reduce long-lived key custody where supported.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI workload identity
→ signing service
→ signature bound to artifact digest
```

### Expected Evidence

The signature is tied to a trusted build identity.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Verify signer identity and digest before promotion.

---

## Advanced Deep Dive 45 — SLSA Build Threat Model

### Concept

Supply-chain maturity improves when builds are isolated, inputs are identified, provenance is generated, and artifact substitution is checked.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
source
→ isolated trusted builder
→ provenance
→ immutable artifact
→ verification
```

### Expected Evidence

The pipeline controls more than vulnerability scanning.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Adopt controls according to realistic threats.

---

## Advanced Deep Dive 46 — Test Pyramid Economics

### Concept

The base of CI should be fast deterministic tests, with fewer expensive system tests, because feedback speed and reliability matter as much as coverage.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
        E2E
    integration
unit/component/static
```

### Expected Evidence

Most failures are caught quickly.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep expensive end-to-end tests focused on critical journeys.

---

## Advanced Deep Dive 47 — Contract Test Placement

### Concept

Consumer/provider contracts can run in CI without requiring every service to deploy into one shared environment.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
consumer publishes expectation
provider CI verifies
```

### Expected Evidence

Interface breakage is detected before release.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Version contracts and assign ownership.

---

## Advanced Deep Dive 48 — Integration Test Containers

### Concept

Disposable databases/queues in CI reduce shared-environment coupling while providing realistic boundary testing.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
job
├─ app container
├─ postgres
└─ redis
```

### Expected Evidence

Each pipeline gets isolated dependency state.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Pin service versions and wait for readiness explicitly.

---

## Advanced Deep Dive 49 — Integration Environment Namespacing

### Concept

When CI uses Kubernetes/OpenShift, one namespace per PR or pipeline can isolate Services, Secrets, and test data.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
pr-481 namespace
→ deploy
→ test
→ TTL cleanup
```

### Expected Evidence

Concurrent pipelines do not overwrite each other.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Enforce quotas and automatic deletion.

---

## Advanced Deep Dive 50 — Test Data Factory

### Concept

Deterministic factories create synthetic data for tests instead of copying production datasets into CI.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```python
def order_fixture():
    return {"id":"test-1","amount":100,"currency":"USD"}
```

### Expected Evidence

Tests receive predictable non-sensitive data.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use synthetic or properly masked data.

---

## Advanced Deep Dive 51 — Database Migration CI

### Concept

Schema migrations should be tested against representative previous schemas and verify forward/rollback compatibility where applicable.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
DB schema N
→ apply migration N+1
→ app tests
→ rollback/fix-forward test
```

### Expected Evidence

Migration failures appear before CD.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Test migration duration and locking, not only correctness.

---

## Advanced Deep Dive 52 — Mutation Testing

### Concept

Mutation testing changes application logic deliberately and checks whether tests fail, revealing weak assertions hidden by high coverage.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
x > 10
mutated to
x >= 10
tests should detect
```

### Expected Evidence

Surviving mutants identify gaps in test quality.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use selectively because mutation testing can be expensive.

---

## Advanced Deep Dive 53 — Coverage Diff Policy

### Concept

Instead of demanding arbitrary total coverage, CI can focus on coverage of changed code and preventing meaningful regressions.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
total coverage: 82%
changed lines coverage: 96%
```

### Expected Evidence

New code quality is visible without gaming legacy areas.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use coverage as one signal among many.

---

## Advanced Deep Dive 54 — Flake Rate

### Concept

Measure how often tests change result on the same commit. Flake rate is a CI reliability metric.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```python
runs=1000
flakes=18
print("Flake rate:", flakes/runs)
```

### Expected Evidence

The team can prioritize the worst flaky suites.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Track by test owner and duration.

---

## Advanced Deep Dive 55 — Flake Quarantine SLA

### Concept

Quarantine preserves flow temporarily but needs an owner and deadline or it becomes permanent lost coverage.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
test_checkout_timeout
owner: team-checkout
quarantine until: +7 days
```

### Expected Evidence

Known flaky tests remain visible and accountable.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Expire quarantine automatically.

---

## Advanced Deep Dive 56 — Infrastructure Failure Classification

### Concept

A CI failure taxonomy should distinguish code/test failures from runner, network, registry, dependency, and CI-platform failures.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
failure_class:
code
test-flake
runner
network
dependency
registry
auth
```

### Expected Evidence

Reliability investment targets systemic CI failures.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Do not charge infrastructure failures against product quality.

---

## Advanced Deep Dive 57 — Retry Taxonomy

### Concept

Retries are appropriate for selected transient infrastructure failures but dangerous for deterministic build/test failures.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
registry 502 → retry with backoff
compile error → no retry
test assertion → no retry
```

### Expected Evidence

Retries reduce transient noise without hiding defects.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Retry by classified error, not blanket pipeline rerun.

---

## Advanced Deep Dive 58 — Exponential Backoff for External Services

### Concept

Dependency retries should spread load rather than hammer an already failing package registry or API.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```python
for i in range(5):
    print(min(30, 2**i), "seconds + jitter")
```

### Expected Evidence

Retry delay grows with repeated failure.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Add jitter and a total retry budget.

---

## Advanced Deep Dive 59 — Timeout Budget per Job

### Concept

Jobs need finite timeouts based on expected duration so deadlocks and external hangs release capacity.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
lint: 5m
unit: 10m
integration: 30m
image build: 20m
```

### Expected Evidence

Hung work stops predictably.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Alert on timeout trend rather than only increasing limits.

---

## Advanced Deep Dive 60 — Cancellation of Superseded Runs

### Concept

When a new commit replaces an older PR commit, continuing expensive old jobs wastes capacity and delays current feedback.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR commit A running
push commit B
→ cancel A
→ prioritize B
```

### Expected Evidence

Runner demand tracks current developer intent.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Enable concurrency groups/cancellation where safe.

---

## Advanced Deep Dive 61 — Test Impact Analysis

### Concept

Dependency graphs can run only tests affected by a change while scheduled full suites preserve safety.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
shared-auth changed
→ api-auth tests
→ web-login tests
→ contract tests
```

### Expected Evidence

PR feedback becomes faster without arbitrary omission.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep a regular full regression to validate impact mapping.

---

## Advanced Deep Dive 62 — Monorepo Dependency Graph

### Concept

A scalable monorepo CI system understands which libraries/services depend on changed code rather than using only raw path filters.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
shared-lib
├─ api
└─ worker
change shared-lib → build both
```

### Expected Evidence

Dependent projects rebuild correctly.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use graph-aware tooling for complex monorepos.

---

## Advanced Deep Dive 63 — Polyrepo Contract Registry

### Concept

Separate repositories benefit from versioned API contracts or schemas that CI can validate independently.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
service-a CI
→ publish contract/schema
service-b CI
→ compatibility check
```

### Expected Evidence

Distributed changes do not require a giant shared branch.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Make interface compatibility part of CI.

---

## Advanced Deep Dive 64 — Matrix Strategy Sampling

### Concept

Full cross-product matrices can explode cost. Use representative combinations on PR and wider matrices on main/nightly.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR: latest runtime × supported OS
Nightly: all supported runtimes × OS
```

### Expected Evidence

Compatibility coverage is balanced with feedback speed.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Design the matrix from support policy.

---

## Advanced Deep Dive 65 — Architecture Matrix

### Concept

Multi-architecture images or binaries should test build and runtime behavior on supported architectures, not only cross-compile.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
amd64 build+test
arm64 build+test
manifest list publish
```

### Expected Evidence

Architecture-specific defects are detected.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use real or emulated testing according to risk.

---

## Advanced Deep Dive 66 — BuildKit Cache Strategy

### Concept

Container builds can use layer/cache mounts and remote cache, but cache inputs and secrets must be separated so sensitive data is never committed to image layers.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
```

### Expected Evidence

Dependency downloads are reused without becoming release layers.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use BuildKit secret mounts instead of ARG/ENV for build secrets.

---

## Advanced Deep Dive 67 — Secret Mount in Container Build

### Concept

Build secrets should be mounted temporarily and excluded from layers/history.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

### Expected Evidence

The credential exists only during the build step.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Verify final image does not contain secret files.

---

## Advanced Deep Dive 68 — Rootless Build Workers

### Concept

Rootless or isolated container-build mechanisms reduce the privilege required by CI compared with mounting the host Docker socket.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI job
→ rootless builder
→ OCI image
not host docker.sock
```

### Expected Evidence

A compromised build has less host control.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Avoid exposing privileged runtime sockets to untrusted jobs.

---

## Advanced Deep Dive 69 — Docker Socket Risk

### Concept

Mounting `/var/run/docker.sock` gives container jobs powerful host/runtime control and often root-equivalent capability.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
job container
+ docker.sock
→ control host containers/filesystem mounts
```

### Expected Evidence

The risk is recognized as privilege escalation.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use isolated builders or dedicated ephemeral hosts.

---

## Advanced Deep Dive 70 — Kubernetes CI Runner Isolation

### Concept

Runner Pods need dedicated namespaces, ServiceAccounts, quotas, NetworkPolicies, and often node pools when executing untrusted builds.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
ci-untrusted namespace
+ default deny
+ no prod routes
+ restricted SA
+ ephemeral Pods
```

### Expected Evidence

Cluster-based runners do not inherit broad platform privileges.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Separate runner trust zones at namespace and node/network layers.

---

## Advanced Deep Dive 71 — CI Network Egress Policy

### Concept

Builds should reach only source control, dependency mirrors, artifact registries, scanners, and approved APIs for their job.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
runner egress:
Git ✓
package proxy ✓
registry ✓
prod DB ✗
metadata service ✗
```

### Expected Evidence

Network exposure matches pipeline purpose.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Combine network controls with identity controls.

---

## Advanced Deep Dive 72 — Cloud Metadata Blocking

### Concept

Self-hosted runners in cloud VMs should not let untrusted jobs access powerful instance metadata credentials.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
runner job
✕ node/instance admin metadata
✓ workload-specific identity
```

### Expected Evidence

A malicious job cannot inherit broad VM role credentials.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use workload identity and metadata hardening.

---

## Advanced Deep Dive 73 — Artifact Publication Permission Split

### Concept

Only release jobs should publish immutable release versions. PR jobs can build temporary artifacts in separate namespaces/repos.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR artifact → snapshots/pr-481
main release → releases/2.4.1
```

### Expected Evidence

Untrusted or unreviewed code cannot overwrite production releases.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Separate repositories and credentials by lifecycle.

---

## Advanced Deep Dive 74 — Release Tag Trust

### Concept

A tag-triggered release is only trustworthy if tag creation/mutation is protected and the tag points to an approved commit.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
protected tag v*
→ only release maintainers/bot
→ CI verifies commit on protected main
```

### Expected Evidence

Release tags cannot bypass normal review.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Protect tag creation and reject moving release tags.

---

## Advanced Deep Dive 75 — Signed Commit/Tag Context

### Concept

Signatures can strengthen identity evidence but do not replace code review, branch protection, or CI validation.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
signed tag
+ protected branch
+ CI evidence
→ stronger release identity
```

### Expected Evidence

The team treats signing as one control in a chain.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Verify signatures where they support a real trust requirement.

---

## Advanced Deep Dive 76 — Reproducible Release Build

### Concept

Release builds should use the same build logic as PR/main validation, with only release metadata/publishing differences.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR: make build/test
Release: make build/test + publish
```

### Expected Evidence

Production artifacts are not built by an unrelated hidden process.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep canonical build logic in the repository.

---

## Advanced Deep Dive 77 — CI Evidence Retention

### Concept

Test reports, scan results, provenance, approvals, and build logs need retention appropriate to release audit and incident needs.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR logs: 30d
release evidence: 1y+
SBOM/provenance: lifetime of release
```

### Expected Evidence

Historical production artifacts retain enough evidence for investigation.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Define retention by evidence value and compliance needs.

---

## Advanced Deep Dive 78 — CI Audit Events

### Concept

Trigger, approval, rerun, cancellation, secret/config change, runner registration, and workflow modification are security-relevant audit events.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
who
what
repository
workflow
timestamp
result
```

### Expected Evidence

Suspicious CI activity can be reconstructed.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Forward high-value audit events to centralized logging/SIEM.

---

## Advanced Deep Dive 79 — CI Deployment Marker Boundary

### Concept

CI should publish the artifact and metadata; CD should record deployment. Keeping these contracts separate improves traceability and least privilege.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI output:
artifact digest + evidence

CD input:
artifact digest + promotion decision
```

### Expected Evidence

Build and deploy responsibilities remain distinct.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Avoid giving build pipelines unnecessary production access.

---

## Advanced Deep Dive 80 — Quality Gate Exceptions

### Concept

A bypass should record who approved it, exact finding, reason, scope, risk, and expiration.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```yaml
exception:
  check: dependency-CVE
  artifact: 2.4.1
  owner: security
  expires: 2026-09-01
```

### Expected Evidence

Temporary risk acceptance is auditable.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Make bypasses narrow and expiring.

---

## Advanced Deep Dive 81 — Security Finding Baseline

### Concept

Legacy repositories may need a controlled baseline so new critical findings are blocked without requiring all historical debt to disappear in one day.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
existing findings = known baseline
new critical finding → block
baseline reduction → tracked backlog
```

### Expected Evidence

Security improves without permanently accepting new debt.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Do not let the baseline grow.

---

## Advanced Deep Dive 82 — Policy as Code Unit Tests

### Concept

CI policies themselves should have tests proving allowed and denied examples before deployment.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
policy test:
private bucket → pass
public bucket → deny
exception case → pass with waiver
```

### Expected Evidence

A policy update does not unexpectedly block or allow all pipelines.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Version and test policy code.

---

## Advanced Deep Dive 83 — Scanner Availability Strategy

### Concept

If a noncritical scanner is temporarily unavailable, the policy should define fail-open, fail-closed, or queue behavior based on risk.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
secret scanner outage → fail closed
optional style scanner outage → warn
```

### Expected Evidence

Tool outages have predictable delivery behavior.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Make failure policy explicit per control.

---

## Advanced Deep Dive 84 — Scanner False-Positive Workflow

### Concept

Findings need triage with evidence and ownership rather than broad ignore lists.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
finding
→ reproduce/context
→ fix or exception
→ owner + expiry
```

### Expected Evidence

Scanner trust remains high.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Review suppression files like production policy.

---

## Advanced Deep Dive 85 — Vulnerability DB Freshness

### Concept

Security scanners depend on vulnerability intelligence updates. A scanner that has not refreshed its database can produce misleading green builds.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
scan result
+ vulnerability DB timestamp
```

### Expected Evidence

Freshness becomes part of scan evidence.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Monitor scanner feed age.

---

## Advanced Deep Dive 86 — Post-Build Rescanning

### Concept

Images/packages can become vulnerable after CI has completed because new CVEs are disclosed. Registries/security platforms should rescan released artifacts.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
artifact clean on day 0
new CVE day 30
→ rescan inventory
→ patch pipeline
```

### Expected Evidence

Released exposure is continuously reassessed.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep artifact-to-owner mapping for rapid remediation.

---

## Advanced Deep Dive 87 — CI Platform SLO

### Concept

CI is an internal production service. Useful SLIs include trigger success, queue time, job infrastructure failure rate, artifact publication success, and API availability.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
SLO:
95% PR jobs start <2m
99.9% trigger availability
<1% infra-caused failures
```

### Expected Evidence

Developer experience becomes measurable.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Separate CI-platform failures from application failures.

---

## Advanced Deep Dive 88 — CI Error Budget

### Concept

An internal CI error budget gives platform teams a rational balance between new CI features and reliability work.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI SLO 99.9%
budget burns due runner outage
→ prioritize platform reliability
```

### Expected Evidence

Shared platform reliability drives roadmap decisions.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use error-budget policy for internal platforms too.

---

## Advanced Deep Dive 89 — Pipeline Duration Percentiles

### Concept

Median pipeline time hides slow-tail developer experience. p90/p95 reveal contention and unstable tests.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
p50 8m
p95 31m
```

### Expected Evidence

Slow outliers become visible.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Optimize percentile feedback time, not only averages.

---

## Advanced Deep Dive 90 — Top Failure Category Dashboard

### Concept

A dashboard of failure classes shows whether developer pain comes from product defects, flakes, dependencies, runners, or platform outages.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
last 30d:
code 52%
flake 18%
runner 12%
dependency 10%
other 8%
```

### Expected Evidence

CI improvement work targets the dominant cause.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Auto-classify where possible, sample manually to validate.

---

## Advanced Deep Dive 91 — Runner Disk Pressure

### Concept

Self-hosted runners accumulate images, caches, workspaces, and logs. Disk pressure can manifest as unrelated build failures.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
df -h
df -i
du -sh /var/lib/* 2>/dev/null | sort -h | tail
```

### Expected Evidence

Byte or inode exhaustion is identified.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use ephemeral runners or automated cleanup with quotas.

---

## Advanced Deep Dive 92 — Runner CPU/Memory Saturation

### Concept

Overcommitted runners make tests flaky and timing-sensitive. Resource telemetry should be correlated with CI failures.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
job timeout
+ runner CPU 100%
+ memory pressure
→ infrastructure cause
```

### Expected Evidence

The test is not blamed for host contention.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Set concurrency based on measured resource usage.

---

## Advanced Deep Dive 93 — Shared Test Environment Contention

### Concept

Multiple pipelines against one integration environment create nondeterminism and data collisions.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR A resets DB
PR B running tests
→ false failure
```

### Expected Evidence

The shared-state failure mechanism is explicit.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Prefer ephemeral isolated environments or strict tenancy.

---

## Advanced Deep Dive 94 — CI Dependency Outage Runbook

### Concept

When a package registry, Git provider, artifact store, or scanner is down, responders need a known fallback or fail policy.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
detect dependency outage
→ confirm scope
→ use internal mirror if allowed
→ preserve build evidence
→ communicate
```

### Expected Evidence

External failure does not trigger random pipeline edits.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Maintain dependency status/runbooks.

---

## Advanced Deep Dive 95 — Registry Publication Recovery

### Concept

If build and tests succeeded but registry publication failed, preserve the exact artifact and retry publication instead of rebuilding from source.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
artifact digest locally preserved
registry recovers
→ publish same artifact
```

### Expected Evidence

The eventual release remains identical to the validated build.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Separate build success from publication success.

---

## Advanced Deep Dive 96 — CI Disaster Recovery Order

### Concept

Recover identity/DNS, Git/repositories, CI configuration, secret integration, runners, artifact stores, and status-check integration in dependency order.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
Identity/DNS
→ Git
→ CI control plane
→ runners/secrets
→ artifact stores
→ branch checks
```

### Expected Evidence

The CI service can be restored predictably.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Practice rebuild from IaC/config-as-code.

---

## Advanced Deep Dive 97 — Runner Compromise Response

### Concept

A suspected runner compromise requires isolating the host, revoking credentials, preserving evidence, invalidating caches/artifacts if trust is uncertain, and rebuilding from known-good images.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
isolate runner
→ revoke tokens
→ capture evidence
→ quarantine outputs
→ destroy/rebuild
```

### Expected Evidence

Supply-chain trust is restored deliberately.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Assume credentials available to the runner may be exposed.

---

## Advanced Deep Dive 98 — Artifact Trust Revocation

### Concept

If a build environment was compromised, every artifact produced during the uncertain window may need to be identified and blocked.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
compromised runner ID
→ query build records
→ affected artifact digests
→ revoke/quarantine
```

### Expected Evidence

Potentially tainted releases can be scoped.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Record builder identity in provenance.

---

## Advanced Deep Dive 99 — CI Migration Dual Run

### Concept

Moving CI platforms safely can use a period where old and new systems run the same validation and results are compared.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR
├─ old CI
└─ new CI
compare results/duration
```

### Expected Evidence

Functional gaps are found before cutover.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Migrate capability and trust controls, not only YAML syntax.

---

## Advanced Deep Dive 100 — Reusable Workflow Contract

### Concept

Shared CI templates should expose a small stable interface: inputs, outputs, required permissions, supported versions, and failure semantics.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
inputs:
runtime_version
test_command
publish=false

outputs:
artifact_digest
test_report
```

### Expected Evidence

Teams can consume templates without reading internal implementation.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Treat shared workflows as platform APIs.

---

## Advanced Deep Dive 101 — Reusable Workflow Backward Compatibility

### Concept

A shared template update can break hundreds of repositories. Version and deprecate it like a library.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
ci-template/v2 supported
ci-template/v3 recommended
v2 EOL in 90d
```

### Expected Evidence

Consumers can migrate intentionally.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Avoid silently changing behavior behind mutable references.

---

## Advanced Deep Dive 102 — Pipeline Lint/Test

### Concept

Pipeline definitions can be syntax-validated and unit-tested with sample inputs before rollout.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
pipeline lint
template unit tests
dry-run/sample repo
```

### Expected Evidence

Shared CI changes fail before reaching every repository.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Test the delivery system itself.

---

## Advanced Deep Dive 103 — CI Change Canary

### Concept

Roll out a new runner image or shared workflow to a small repository set before fleet-wide adoption.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
canary repos 5%
→ observe
→ 25%
→ all
```

### Expected Evidence

Platform regressions have limited blast radius.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Use progressive rollout for CI infrastructure changes.

---

## Advanced Deep Dive 104 — Pipeline Feature Flag

### Concept

CI platform changes can be controlled with flags/versions so teams can opt into new behavior before a forced migration.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
scanner_v2=false
→ pilot teams enable
→ validate
→ default true
```

### Expected Evidence

Migration is staged and reversible.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Set an end date for compatibility flags.

---

## Advanced Deep Dive 105 — Developer Feedback UX

### Concept

A failed CI job should surface the exact file/test/finding, likely cause, remediation link, and owner rather than forcing developers to parse thousands of log lines.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
FAIL: tests/test_orders.py::test_total
Expected 100, got 99
See: runbook/test-failure
```

### Expected Evidence

The next action is obvious.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Design CI output for humans under time pressure.

---

## Advanced Deep Dive 106 — Annotation and PR Summary

### Concept

CI can summarize failures, coverage, security, artifacts, and plan output directly in the PR.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
CI Summary:
✓ lint
✓ unit
✗ SCA: 1 critical
artifact: not published
```

### Expected Evidence

Developers receive one coherent status surface.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep summaries concise and link to detailed evidence.

---

## Advanced Deep Dive 107 — Fast-Path vs Full-Path CI

### Concept

Repositories can use a fast PR path for high-signal checks and a full post-merge/nightly path for expensive coverage.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR <10m
main 20m
nightly 90m
```

### Expected Evidence

Fast feedback and deep assurance coexist.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Never defer essential merge-safety checks to nightly.

---

## Advanced Deep Dive 108 — Scheduled Dependency Refresh

### Concept

Periodic CI can test the current code against refreshed vulnerability feeds, base images, or supported dependency versions even when no source changes occur.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
weekly:
rebuild
rescan
compatibility matrix
```

### Expected Evidence

Latent ecosystem changes are detected proactively.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep scheduled results owned and actionable.

---

## Advanced Deep Dive 109 — Base Image Rebuild Trigger

### Concept

Applications should rebuild when their base image receives security updates, not only when application code changes.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
base digest changed
→ rebuild app image
→ tests/scans
→ new release candidate
```

### Expected Evidence

Patched runtime layers reach applications predictably.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Track base-image lineage.

---

## Advanced Deep Dive 110 — Generated Code Drift Check

### Concept

If generated clients/schema files are committed, CI can regenerate and fail when Git is not clean.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```bash
make generate
git diff --exit-code
```

### Expected Evidence

Generated files remain synchronized with source definitions.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Automate generation rather than relying on developer memory.

---

## Advanced Deep Dive 111 — License Policy Gate

### Concept

SCA can enforce allowed/denied license policy for new dependencies in addition to vulnerability checks.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
dependency added
→ license detected
→ allow / review / deny
```

### Expected Evidence

Legal/compliance risk is caught before release.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Keep policy exceptions reviewable and expiring.

---

## Advanced Deep Dive 112 — Binary Provenance for Compiled Artifacts

### Concept

Compiled binaries should be traceable to compiler/toolchain versions and source revision, not only a package name.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
binary hash
← compiler image digest
← commit
← build ID
```

### Expected Evidence

Runtime binary identity can be reconstructed.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Embed or attach build metadata.

---

## Advanced Deep Dive 113 — Test Result Provenance

### Concept

A green badge is weaker evidence than a structured record linking test results to the exact commit/artifact under test.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
test report subject:
commit abc123
artifact sha256:xyz
runner image sha256:runner
```

### Expected Evidence

Evidence cannot be confused across reruns.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Bind test reports to immutable subjects.

---

## Advanced Deep Dive 114 — Mainline Health SLO

### Concept

Mainline health can be measured as the percentage of time the protected branch is green/releasable.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
main green 99.4% of working hours
```

### Expected Evidence

Broken-main impact becomes visible.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Treat a red main branch as a high-priority team incident.

---

## Advanced Deep Dive 115 — Stop-the-Line Automation

### Concept

When main breaks, automation can block further merges and notify owners until the branch is restored.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
main CI red
→ merge queue paused
→ team notification
→ revert/fix
```

### Expected Evidence

Damage does not compound.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Restore main before normal feature work continues.

---

## Advanced Deep Dive 116 — Revertability Check

### Concept

Small atomic PRs and migration discipline make automatic or manual revert safer.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
PR has:
one coherent feature
no irreversible DB contract
feature flag default off
```

### Expected Evidence

A failed integration can be removed cleanly.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Design changes for reversible integration.

---

## Advanced Deep Dive 117 — CI Change Failure Review

### Concept

When CI itself causes widespread failures, run a lightweight post-incident review just like a production outage.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
runner image v12 rollout
→ 70% build failures
→ rollback v11
→ root cause + guardrail
```

### Expected Evidence

Platform learning improves future CI changes.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Operate CI as a production platform.

---

## Advanced Deep Dive 118 — Evidence-First CI Troubleshooting

### Concept

Reliable CI diagnosis starts with trigger, identity, runner, checkout, dependencies, build, tests, scans, artifact, and publication in that order.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
No run? trigger
Queued? runner/capacity
Checkout? auth/network
Install? dependency
Build? toolchain
Test? code/flake/env
Publish? registry
```

### Expected Evidence

The failure is placed at one layer before remediation.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Avoid random reruns; classify first.

---

## Advanced Deep Dive 119 — CI Operational Readiness

### Concept

A production CI platform needs branch protection, isolated runners, identity federation, artifact immutability, cache governance, scanner policy, observability, backups, DR, and runbooks.

### CI Mental Model

```text
Repository Event
      ↓
Policy / Trigger
      ↓
Runner Trust Zone
      ↓
Checkout + Dependencies
      ↓
Build + Tests + Security
      ↓
Evidence
      ↓
Immutable Artifact
      ↓
Publish / Hand Off to CD
```

### Code / Configuration / Calculation

```text
[ ] protected main
[ ] trust-zone runners
[ ] OIDC
[ ] artifact repo
[ ] SBOM/provenance
[ ] CI SLO
[ ] DR
[ ] incident runbooks
```

### Expected Evidence

The platform is operable and secure before broad adoption.

### Why It Works

CI is a software supply-chain control plane. Correctness depends on integration freshness, reproducible inputs, runner isolation, deterministic tests, trusted dependencies, explicit identities, immutable artifacts, and fast developer feedback. Security and reliability failures often originate outside application code, so a mature CI system separates product failures from platform and supply-chain failures.

### Production Example

Apply the topic to a real repository by identifying the trust boundary, trigger, runner, credentials, build inputs, expected evidence, artifact identity, and failure/recovery path.

### Troubleshooting Workflow

```text
Trigger created?
   ↓
Correct repo/ref/event?
   ↓
Runner assigned and healthy?
   ↓
Checkout/auth/network?
   ↓
Dependency resolution/cache?
   ↓
Build/toolchain?
   ↓
Tests/scans/policy?
   ↓
Artifact generated?
   ↓
Publication/metadata?
   ↓
Return actionable feedback
```

### Common Mistakes

- Rerunning until green without classifying the failure.
- Giving untrusted PRs secrets or privileged persistent runners.
- Treating caches as trusted artifacts.
- Rebuilding release output differently from validated CI.
- Using mutable dependencies or runner images.
- Making every scanner finding a blocking gate without policy.
- Ignoring queue time and CI platform reliability.

### Best Practice

Make CI readiness a platform launch gate.

---

# Supplemental Hands-on Lab Series — Continuous Integration

## Enhanced CI Lab 1 — Pre-Merge Test Merge Commit

### Objective

Practice **Pre-Merge Test Merge Commit** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
main A-B-C
PR branch A-X
CI tests merge(C,X), not only X alone
```

### Expected Result

The validated commit is close to the commit that will enter main.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Validate the integrated result before final merge.

---

## Enhanced CI Lab 2 — Merge Queue Serialization

### Objective

Practice **Merge Queue Serialization** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR1 green
PR2 green
queue:
test main+PR1
then main+PR1+PR2
```

### Expected Result

Main remains protected from stale-base races.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use merge queues in high-change repositories with strict mainline health.

---

## Enhanced CI Lab 3 — Branch Protection as Policy

### Objective

Practice **Branch Protection as Policy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
main:
require PR
require 2 reviews
require CI
block force push
```

### Expected Result

Direct unsafe integration paths are removed.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Treat branch protection as production policy.

---

## Enhanced CI Lab 4 — Status Check Design

### Objective

Practice **Status Check Design** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
required:
build
unit
security-critical
merge validation

informational:
deep scan
nightly performance
```

### Expected Result

Merge blocking reflects actual confidence.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Only make a check required when the team trusts its signal.

---

## Enhanced CI Lab 5 — PR Size Guardrail

### Objective

Practice **PR Size Guardrail** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```python
changed_lines = 1800
if changed_lines > 800:
    print("Warning: consider splitting this PR")
```

### Expected Result

Large change sets are surfaced early.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Prefer guidance and ownership over arbitrary hard limits.

---

## Enhanced CI Lab 6 — Review Queue SLO

### Objective

Practice **Review Queue SLO** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
SLI: PRs reviewed within 4h
SLO: >= 90%
```

### Expected Result

Review delay becomes measurable alongside pipeline delay.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Optimize human queues as seriously as runner queues.

---

## Enhanced CI Lab 7 — Pipeline Critical Path

### Objective

Practice **Pipeline Critical Path** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
build 5m → integration 18m → package 2m = 25m
lint 4m parallel
scan 7m parallel
critical path = 25m
```

### Expected Result

The true latency bottleneck is identified.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Profile the DAG before adding parallelism.

---

## Enhanced CI Lab 8 — Queue Time vs Run Time

### Objective

Practice **Queue Time vs Run Time** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```python
queue=15
run=5
print("Feedback time:", queue+run, "minutes")
```

### Expected Result

Runner saturation becomes distinguishable from slow tests.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Track queue p50/p95 separately from job duration.

---

## Enhanced CI Lab 9 — Runner Capacity Headroom

### Objective

Practice **Runner Capacity Headroom** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
average demand: 20 jobs
burst: 60 jobs
runner capacity: 25
→ queue
```

### Expected Result

Burst behavior is included in capacity design.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Maintain autoscaling or reserved headroom for peak feedback demand.

---

## Enhanced CI Lab 10 — Runner Autoscaling Signal

### Objective

Practice **Runner Autoscaling Signal** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
queue depth ↑
oldest queued job age ↑
→ add runners
```

### Expected Result

Scaling responds to developer waiting time.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Scale from demand while enforcing upper cost limits.

---

## Enhanced CI Lab 11 — Ephemeral Runner Lifecycle

### Objective

Practice **Ephemeral Runner Lifecycle** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
request
→ provision runner
→ register
→ execute one job
→ upload results
→ destroy
```

### Expected Result

Cross-job persistence is eliminated.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Prefer ephemeral runners for privileged or untrusted workloads.

---

## Enhanced CI Lab 12 — Runner Trust Zones

### Objective

Practice **Runner Trust Zones** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
Zone A: fork PR, no secrets
Zone B: internal CI
Zone C: signing
Zone D: production deploy
```

### Expected Result

Compromise of a low-trust job cannot directly reach high-trust systems.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Route jobs by trust requirement, not convenience.

---

## Enhanced CI Lab 13 — Fork PR Isolation

### Objective

Practice **Fork PR Isolation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
fork PR
→ read-only checkout
→ no prod secrets
→ ephemeral hosted/isolated runner
```

### Expected Result

Malicious pipeline code has limited capability.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Treat repository code as executable input.

---

## Enhanced CI Lab 14 — pull_request vs Privileged Event Semantics

### Objective

Practice **pull_request vs Privileged Event Semantics** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
trusted workflow logic
+ untrusted PR contents
+ secret
= high-risk combination
```

### Expected Result

Workflow event choice is treated as a security design decision.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Separate untrusted validation from privileged follow-up jobs.

---

## Enhanced CI Lab 15 — Workflow Token Minimization

### Objective

Practice **Workflow Token Minimization** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```yaml
permissions:
  contents: read
  packages: write
  id-token: write
```

### Expected Result

The workflow has a visible minimal permission set.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Grant write permissions only to jobs that truly publish/change something.

---

## Enhanced CI Lab 16 — OIDC Claim Restriction

### Objective

Practice **OIDC Claim Restriction** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
Allow role if:
repo=org/app
ref=refs/heads/main
environment=prod
aud=cloud-sts
```

### Expected Result

A token from another repository or branch cannot assume the role.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Constrain federation with contextual claims.

---

## Enhanced CI Lab 17 — Short-Lived Release Credentials

### Objective

Practice **Short-Lived Release Credentials** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI OIDC
→ STS
→ 30-minute role credential
→ deploy
```

### Expected Result

Credential lifetime matches the job.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Prefer federated identity for CI/CD.

---

## Enhanced CI Lab 18 — Secret Fan-Out Analysis

### Objective

Practice **Secret Fan-Out Analysis** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
prod token
currently → 18 jobs
required → 1 deploy job
```

### Expected Result

Credential exposure is reduced by design.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Scope secrets by job, environment, and trust zone.

---

## Enhanced CI Lab 19 — Secret Redaction Limits

### Objective

Practice **Secret Redaction Limits** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
masked SECRET
→ base64/HTTP exfiltration still possible
```

### Expected Result

The design no longer relies on console masking for containment.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Do not expose secrets to untrusted code in the first place.

---

## Enhanced CI Lab 20 — Shell Trace Risk

### Objective

Practice **Shell Trace Risk** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
set +x
# perform secret-bearing command
set -x
```

### Expected Result

Sensitive command output is excluded from logs.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Disable shell tracing around credentials and use stdin/file mechanisms.

---

## Enhanced CI Lab 21 — Pipeline Definition Review

### Objective

Practice **Pipeline Definition Review** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
pipeline change
→ code review
→ security checks
→ protected merge
```

### Expected Result

A pipeline privilege change cannot bypass peer review.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Protect CI configuration paths explicitly.

---

## Enhanced CI Lab 22 — Shared Workflow Version Pinning

### Objective

Practice **Shared Workflow Version Pinning** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
uses: org/security-workflow@<approved-commit>
```

### Expected Result

A historical CI run can identify the exact workflow implementation.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Upgrade shared workflow versions deliberately.

---

## Enhanced CI Lab 23 — Jenkins Plugin Attack Surface

### Objective

Practice **Jenkins Plugin Attack Surface** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
plugin inventory
→ approved list
→ patch cadence
→ remove unused
```

### Expected Result

Plugin footprint is measurable and governable.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Minimize plugins and maintain an ownership/upgrade process.

---

## Enhanced CI Lab 24 — Controller/Runner Separation

### Objective

Practice **Controller/Runner Separation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
controller
  ↓ schedules
ephemeral agents
  ↓ execute jobs
```

### Expected Result

Build compromise is less likely to compromise the control plane.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep execution isolated from CI control-plane state.

---

## Enhanced CI Lab 25 — Runner Image Supply Chain

### Objective

Practice **Runner Image Supply Chain** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
base OS
→ tool install
→ scan
→ sign
→ runner-image:v12
```

### Expected Result

Build infrastructure can be traced to an approved image version.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Treat runner images as production artifacts.

---

## Enhanced CI Lab 26 — Build Container Pinning

### Objective

Practice **Build Container Pinning** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```yaml
container:
  image: registry.example/ci/python@sha256:...
```

### Expected Result

The CI toolchain is immutable for the run.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Promote build images like any other critical dependency.

---

## Enhanced CI Lab 27 — Hermetic Build Boundary

### Objective

Practice **Hermetic Build Boundary** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
declared source
+ lockfile
+ compiler image
+ vendored/mirrored deps
→ artifact
```

### Expected Result

The same inputs can reproduce equivalent output.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Remove undeclared environmental inputs incrementally.

---

## Enhanced CI Lab 28 — SOURCE_DATE_EPOCH Concept

### Objective

Practice **SOURCE_DATE_EPOCH Concept** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
export SOURCE_DATE_EPOCH="$(git log -1 --pretty=%ct)"
```

### Expected Result

Timestamp-sensitive build steps can use a deterministic source time.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use ecosystem-specific reproducible-build guidance.

---

## Enhanced CI Lab 29 — Locale and Timezone Reproducibility

### Objective

Practice **Locale and Timezone Reproducibility** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
export TZ=UTC
export LC_ALL=C.UTF-8
```

### Expected Result

Date/string behavior becomes predictable across runners.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Control locale/timezone inputs instead of relying on host defaults.

---

## Enhanced CI Lab 30 — Dependency Lock Integrity

### Objective

Practice **Dependency Lock Integrity** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
npm ci
# or equivalent frozen-lockfile mode
```

### Expected Result

CI installs exactly what the lock file describes.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use frozen/immutable dependency install modes.

---

## Enhanced CI Lab 31 — Dependency Confusion Defense

### Objective

Practice **Dependency Confusion Defense** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
@company/internal-lib
→ internal registry namespace
not public fallback
```

### Expected Result

Private package resolution cannot silently fall through to an attacker-controlled source.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Reserve namespaces and configure scoped registries.

---

## Enhanced CI Lab 32 — Typosquatting Review

### Objective

Practice **Typosquatting Review** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
requests
vs
reqeusts
```

### Expected Result

Dependency additions receive explicit human/tool review.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Require approval for new external dependencies.

---

## Enhanced CI Lab 33 — Internal Dependency Proxy

### Objective

Practice **Internal Dependency Proxy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI
  ↓ internal package proxy
  ↓ approved upstream registries
```

### Expected Result

Builds continue during some upstream outages and package access is logged.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Harden the proxy as critical supply-chain infrastructure.

---

## Enhanced CI Lab 34 — Cache Trust Domains

### Objective

Practice **Cache Trust Domains** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
fork cache namespace
≠ trusted-main cache namespace
```

### Expected Result

Cross-trust cache poisoning is prevented.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Partition cache keys and permissions by trust level.

---

## Enhanced CI Lab 35 — Cache Key Completeness

### Objective

Practice **Cache Key Completeness** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
linux-amd64-python3.13-<lock-hash>
```

### Expected Result

Relevant input changes invalidate stale cache data.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Prefer under-caching to silently reusing incompatible output.

---

## Enhanced CI Lab 36 — Remote Build Cache

### Objective

Practice **Remote Build Cache** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
source/action digest
→ remote cache
→ verified build output
```

### Expected Result

Repeated builds avoid recomputing unchanged actions.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Treat remote cache as supply-chain data, not only performance data.

---

## Enhanced CI Lab 37 — Cache Poisoning Detection

### Objective

Practice **Cache Poisoning Detection** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
cached build artifact A
clean rebuild artifact B
compare digests
```

### Expected Result

Mismatch proves the cache influenced output unexpectedly.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep a clean-build troubleshooting path.

---

## Enhanced CI Lab 38 — Artifact vs Cache Enforcement

### Objective

Practice **Artifact vs Cache Enforcement** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
cache retention: days
release artifact retention: policy-driven
```

### Expected Result

A cache purge cannot remove the only deployable release.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Never promote from a transient cache.

---

## Enhanced CI Lab 39 — Build Once Evidence

### Objective

Practice **Build Once Evidence** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```json
{"commit":"abc123","build":"5821","digest":"sha256:...","toolchain":"ci-image:v12"}
```

### Expected Result

Artifact lineage is queryable from one record.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Make artifact publication the terminal CI contract.

---

## Enhanced CI Lab 40 — Artifact Immutability Policy

### Objective

Practice **Artifact Immutability Policy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
push app:2.4.1 once
second push same immutable release → reject
```

### Expected Result

Historical release identity remains trustworthy.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Publish a new version for every changed artifact.

---

## Enhanced CI Lab 41 — Container Digest Capture

### Objective

Practice **Container Digest Capture** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
# Example concept; command depends on registry tooling
echo "repo/app@sha256:..."
```

### Expected Result

CD can deploy an immutable reference rather than a mutable tag.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Pass the digest as pipeline output/evidence.

---

## Enhanced CI Lab 42 — SBOM Generation Placement

### Objective

Practice **SBOM Generation Placement** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
source manifests
→ build artifact
→ artifact/image SBOM
```

### Expected Result

The SBOM corresponds to production bits.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Retain SBOM with artifact lineage.

---

## Enhanced CI Lab 43 — Provenance Attestation

### Objective

Practice **Provenance Attestation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
subject: sha256:artifact
builder: ci-prod-builder
source: commit abc123
```

### Expected Result

Artifact origin can be evaluated programmatically.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Generate provenance inside the trusted build boundary.

---

## Enhanced CI Lab 44 — Artifact Signing Identity

### Objective

Practice **Artifact Signing Identity** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI workload identity
→ signing service
→ signature bound to artifact digest
```

### Expected Result

The signature is tied to a trusted build identity.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Verify signer identity and digest before promotion.

---

## Enhanced CI Lab 45 — SLSA Build Threat Model

### Objective

Practice **SLSA Build Threat Model** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
source
→ isolated trusted builder
→ provenance
→ immutable artifact
→ verification
```

### Expected Result

The pipeline controls more than vulnerability scanning.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Adopt controls according to realistic threats.

---

## Enhanced CI Lab 46 — Test Pyramid Economics

### Objective

Practice **Test Pyramid Economics** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
        E2E
    integration
unit/component/static
```

### Expected Result

Most failures are caught quickly.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep expensive end-to-end tests focused on critical journeys.

---

## Enhanced CI Lab 47 — Contract Test Placement

### Objective

Practice **Contract Test Placement** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
consumer publishes expectation
provider CI verifies
```

### Expected Result

Interface breakage is detected before release.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Version contracts and assign ownership.

---

## Enhanced CI Lab 48 — Integration Test Containers

### Objective

Practice **Integration Test Containers** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
job
├─ app container
├─ postgres
└─ redis
```

### Expected Result

Each pipeline gets isolated dependency state.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Pin service versions and wait for readiness explicitly.

---

## Enhanced CI Lab 49 — Integration Environment Namespacing

### Objective

Practice **Integration Environment Namespacing** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
pr-481 namespace
→ deploy
→ test
→ TTL cleanup
```

### Expected Result

Concurrent pipelines do not overwrite each other.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Enforce quotas and automatic deletion.

---

## Enhanced CI Lab 50 — Test Data Factory

### Objective

Practice **Test Data Factory** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```python
def order_fixture():
    return {"id":"test-1","amount":100,"currency":"USD"}
```

### Expected Result

Tests receive predictable non-sensitive data.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use synthetic or properly masked data.

---

## Enhanced CI Lab 51 — Database Migration CI

### Objective

Practice **Database Migration CI** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
DB schema N
→ apply migration N+1
→ app tests
→ rollback/fix-forward test
```

### Expected Result

Migration failures appear before CD.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Test migration duration and locking, not only correctness.

---

## Enhanced CI Lab 52 — Mutation Testing

### Objective

Practice **Mutation Testing** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
x > 10
mutated to
x >= 10
tests should detect
```

### Expected Result

Surviving mutants identify gaps in test quality.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use selectively because mutation testing can be expensive.

---

## Enhanced CI Lab 53 — Coverage Diff Policy

### Objective

Practice **Coverage Diff Policy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
total coverage: 82%
changed lines coverage: 96%
```

### Expected Result

New code quality is visible without gaming legacy areas.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use coverage as one signal among many.

---

## Enhanced CI Lab 54 — Flake Rate

### Objective

Practice **Flake Rate** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```python
runs=1000
flakes=18
print("Flake rate:", flakes/runs)
```

### Expected Result

The team can prioritize the worst flaky suites.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Track by test owner and duration.

---

## Enhanced CI Lab 55 — Flake Quarantine SLA

### Objective

Practice **Flake Quarantine SLA** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
test_checkout_timeout
owner: team-checkout
quarantine until: +7 days
```

### Expected Result

Known flaky tests remain visible and accountable.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Expire quarantine automatically.

---

## Enhanced CI Lab 56 — Infrastructure Failure Classification

### Objective

Practice **Infrastructure Failure Classification** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
failure_class:
code
test-flake
runner
network
dependency
registry
auth
```

### Expected Result

Reliability investment targets systemic CI failures.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Do not charge infrastructure failures against product quality.

---

## Enhanced CI Lab 57 — Retry Taxonomy

### Objective

Practice **Retry Taxonomy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
registry 502 → retry with backoff
compile error → no retry
test assertion → no retry
```

### Expected Result

Retries reduce transient noise without hiding defects.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Retry by classified error, not blanket pipeline rerun.

---

## Enhanced CI Lab 58 — Exponential Backoff for External Services

### Objective

Practice **Exponential Backoff for External Services** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```python
for i in range(5):
    print(min(30, 2**i), "seconds + jitter")
```

### Expected Result

Retry delay grows with repeated failure.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Add jitter and a total retry budget.

---

## Enhanced CI Lab 59 — Timeout Budget per Job

### Objective

Practice **Timeout Budget per Job** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
lint: 5m
unit: 10m
integration: 30m
image build: 20m
```

### Expected Result

Hung work stops predictably.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Alert on timeout trend rather than only increasing limits.

---

## Enhanced CI Lab 60 — Cancellation of Superseded Runs

### Objective

Practice **Cancellation of Superseded Runs** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR commit A running
push commit B
→ cancel A
→ prioritize B
```

### Expected Result

Runner demand tracks current developer intent.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Enable concurrency groups/cancellation where safe.

---

## Enhanced CI Lab 61 — Test Impact Analysis

### Objective

Practice **Test Impact Analysis** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
shared-auth changed
→ api-auth tests
→ web-login tests
→ contract tests
```

### Expected Result

PR feedback becomes faster without arbitrary omission.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep a regular full regression to validate impact mapping.

---

## Enhanced CI Lab 62 — Monorepo Dependency Graph

### Objective

Practice **Monorepo Dependency Graph** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
shared-lib
├─ api
└─ worker
change shared-lib → build both
```

### Expected Result

Dependent projects rebuild correctly.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use graph-aware tooling for complex monorepos.

---

## Enhanced CI Lab 63 — Polyrepo Contract Registry

### Objective

Practice **Polyrepo Contract Registry** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
service-a CI
→ publish contract/schema
service-b CI
→ compatibility check
```

### Expected Result

Distributed changes do not require a giant shared branch.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Make interface compatibility part of CI.

---

## Enhanced CI Lab 64 — Matrix Strategy Sampling

### Objective

Practice **Matrix Strategy Sampling** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR: latest runtime × supported OS
Nightly: all supported runtimes × OS
```

### Expected Result

Compatibility coverage is balanced with feedback speed.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Design the matrix from support policy.

---

## Enhanced CI Lab 65 — Architecture Matrix

### Objective

Practice **Architecture Matrix** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
amd64 build+test
arm64 build+test
manifest list publish
```

### Expected Result

Architecture-specific defects are detected.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use real or emulated testing according to risk.

---

## Enhanced CI Lab 66 — BuildKit Cache Strategy

### Objective

Practice **BuildKit Cache Strategy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
```

### Expected Result

Dependency downloads are reused without becoming release layers.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use BuildKit secret mounts instead of ARG/ENV for build secrets.

---

## Enhanced CI Lab 67 — Secret Mount in Container Build

### Objective

Practice **Secret Mount in Container Build** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

### Expected Result

The credential exists only during the build step.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Verify final image does not contain secret files.

---

## Enhanced CI Lab 68 — Rootless Build Workers

### Objective

Practice **Rootless Build Workers** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI job
→ rootless builder
→ OCI image
not host docker.sock
```

### Expected Result

A compromised build has less host control.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Avoid exposing privileged runtime sockets to untrusted jobs.

---

## Enhanced CI Lab 69 — Docker Socket Risk

### Objective

Practice **Docker Socket Risk** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
job container
+ docker.sock
→ control host containers/filesystem mounts
```

### Expected Result

The risk is recognized as privilege escalation.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use isolated builders or dedicated ephemeral hosts.

---

## Enhanced CI Lab 70 — Kubernetes CI Runner Isolation

### Objective

Practice **Kubernetes CI Runner Isolation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
ci-untrusted namespace
+ default deny
+ no prod routes
+ restricted SA
+ ephemeral Pods
```

### Expected Result

Cluster-based runners do not inherit broad platform privileges.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Separate runner trust zones at namespace and node/network layers.

---

## Enhanced CI Lab 71 — CI Network Egress Policy

### Objective

Practice **CI Network Egress Policy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
runner egress:
Git ✓
package proxy ✓
registry ✓
prod DB ✗
metadata service ✗
```

### Expected Result

Network exposure matches pipeline purpose.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Combine network controls with identity controls.

---

## Enhanced CI Lab 72 — Cloud Metadata Blocking

### Objective

Practice **Cloud Metadata Blocking** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
runner job
✕ node/instance admin metadata
✓ workload-specific identity
```

### Expected Result

A malicious job cannot inherit broad VM role credentials.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use workload identity and metadata hardening.

---

## Enhanced CI Lab 73 — Artifact Publication Permission Split

### Objective

Practice **Artifact Publication Permission Split** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR artifact → snapshots/pr-481
main release → releases/2.4.1
```

### Expected Result

Untrusted or unreviewed code cannot overwrite production releases.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Separate repositories and credentials by lifecycle.

---

## Enhanced CI Lab 74 — Release Tag Trust

### Objective

Practice **Release Tag Trust** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
protected tag v*
→ only release maintainers/bot
→ CI verifies commit on protected main
```

### Expected Result

Release tags cannot bypass normal review.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Protect tag creation and reject moving release tags.

---

## Enhanced CI Lab 75 — Signed Commit/Tag Context

### Objective

Practice **Signed Commit/Tag Context** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
signed tag
+ protected branch
+ CI evidence
→ stronger release identity
```

### Expected Result

The team treats signing as one control in a chain.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Verify signatures where they support a real trust requirement.

---

## Enhanced CI Lab 76 — Reproducible Release Build

### Objective

Practice **Reproducible Release Build** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR: make build/test
Release: make build/test + publish
```

### Expected Result

Production artifacts are not built by an unrelated hidden process.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep canonical build logic in the repository.

---

## Enhanced CI Lab 77 — CI Evidence Retention

### Objective

Practice **CI Evidence Retention** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR logs: 30d
release evidence: 1y+
SBOM/provenance: lifetime of release
```

### Expected Result

Historical production artifacts retain enough evidence for investigation.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Define retention by evidence value and compliance needs.

---

## Enhanced CI Lab 78 — CI Audit Events

### Objective

Practice **CI Audit Events** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
who
what
repository
workflow
timestamp
result
```

### Expected Result

Suspicious CI activity can be reconstructed.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Forward high-value audit events to centralized logging/SIEM.

---

## Enhanced CI Lab 79 — CI Deployment Marker Boundary

### Objective

Practice **CI Deployment Marker Boundary** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI output:
artifact digest + evidence

CD input:
artifact digest + promotion decision
```

### Expected Result

Build and deploy responsibilities remain distinct.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Avoid giving build pipelines unnecessary production access.

---

## Enhanced CI Lab 80 — Quality Gate Exceptions

### Objective

Practice **Quality Gate Exceptions** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```yaml
exception:
  check: dependency-CVE
  artifact: 2.4.1
  owner: security
  expires: 2026-09-01
```

### Expected Result

Temporary risk acceptance is auditable.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Make bypasses narrow and expiring.

---

## Enhanced CI Lab 81 — Security Finding Baseline

### Objective

Practice **Security Finding Baseline** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
existing findings = known baseline
new critical finding → block
baseline reduction → tracked backlog
```

### Expected Result

Security improves without permanently accepting new debt.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Do not let the baseline grow.

---

## Enhanced CI Lab 82 — Policy as Code Unit Tests

### Objective

Practice **Policy as Code Unit Tests** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
policy test:
private bucket → pass
public bucket → deny
exception case → pass with waiver
```

### Expected Result

A policy update does not unexpectedly block or allow all pipelines.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Version and test policy code.

---

## Enhanced CI Lab 83 — Scanner Availability Strategy

### Objective

Practice **Scanner Availability Strategy** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
secret scanner outage → fail closed
optional style scanner outage → warn
```

### Expected Result

Tool outages have predictable delivery behavior.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Make failure policy explicit per control.

---

## Enhanced CI Lab 84 — Scanner False-Positive Workflow

### Objective

Practice **Scanner False-Positive Workflow** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
finding
→ reproduce/context
→ fix or exception
→ owner + expiry
```

### Expected Result

Scanner trust remains high.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Review suppression files like production policy.

---

## Enhanced CI Lab 85 — Vulnerability DB Freshness

### Objective

Practice **Vulnerability DB Freshness** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
scan result
+ vulnerability DB timestamp
```

### Expected Result

Freshness becomes part of scan evidence.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Monitor scanner feed age.

---

## Enhanced CI Lab 86 — Post-Build Rescanning

### Objective

Practice **Post-Build Rescanning** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
artifact clean on day 0
new CVE day 30
→ rescan inventory
→ patch pipeline
```

### Expected Result

Released exposure is continuously reassessed.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep artifact-to-owner mapping for rapid remediation.

---

## Enhanced CI Lab 87 — CI Platform SLO

### Objective

Practice **CI Platform SLO** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
SLO:
95% PR jobs start <2m
99.9% trigger availability
<1% infra-caused failures
```

### Expected Result

Developer experience becomes measurable.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Separate CI-platform failures from application failures.

---

## Enhanced CI Lab 88 — CI Error Budget

### Objective

Practice **CI Error Budget** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI SLO 99.9%
budget burns due runner outage
→ prioritize platform reliability
```

### Expected Result

Shared platform reliability drives roadmap decisions.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use error-budget policy for internal platforms too.

---

## Enhanced CI Lab 89 — Pipeline Duration Percentiles

### Objective

Practice **Pipeline Duration Percentiles** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
p50 8m
p95 31m
```

### Expected Result

Slow outliers become visible.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Optimize percentile feedback time, not only averages.

---

## Enhanced CI Lab 90 — Top Failure Category Dashboard

### Objective

Practice **Top Failure Category Dashboard** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
last 30d:
code 52%
flake 18%
runner 12%
dependency 10%
other 8%
```

### Expected Result

CI improvement work targets the dominant cause.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Auto-classify where possible, sample manually to validate.

---

## Enhanced CI Lab 91 — Runner Disk Pressure

### Objective

Practice **Runner Disk Pressure** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
df -h
df -i
du -sh /var/lib/* 2>/dev/null | sort -h | tail
```

### Expected Result

Byte or inode exhaustion is identified.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use ephemeral runners or automated cleanup with quotas.

---

## Enhanced CI Lab 92 — Runner CPU/Memory Saturation

### Objective

Practice **Runner CPU/Memory Saturation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
job timeout
+ runner CPU 100%
+ memory pressure
→ infrastructure cause
```

### Expected Result

The test is not blamed for host contention.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Set concurrency based on measured resource usage.

---

## Enhanced CI Lab 93 — Shared Test Environment Contention

### Objective

Practice **Shared Test Environment Contention** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR A resets DB
PR B running tests
→ false failure
```

### Expected Result

The shared-state failure mechanism is explicit.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Prefer ephemeral isolated environments or strict tenancy.

---

## Enhanced CI Lab 94 — CI Dependency Outage Runbook

### Objective

Practice **CI Dependency Outage Runbook** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
detect dependency outage
→ confirm scope
→ use internal mirror if allowed
→ preserve build evidence
→ communicate
```

### Expected Result

External failure does not trigger random pipeline edits.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Maintain dependency status/runbooks.

---

## Enhanced CI Lab 95 — Registry Publication Recovery

### Objective

Practice **Registry Publication Recovery** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
artifact digest locally preserved
registry recovers
→ publish same artifact
```

### Expected Result

The eventual release remains identical to the validated build.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Separate build success from publication success.

---

## Enhanced CI Lab 96 — CI Disaster Recovery Order

### Objective

Practice **CI Disaster Recovery Order** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
Identity/DNS
→ Git
→ CI control plane
→ runners/secrets
→ artifact stores
→ branch checks
```

### Expected Result

The CI service can be restored predictably.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Practice rebuild from IaC/config-as-code.

---

## Enhanced CI Lab 97 — Runner Compromise Response

### Objective

Practice **Runner Compromise Response** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
isolate runner
→ revoke tokens
→ capture evidence
→ quarantine outputs
→ destroy/rebuild
```

### Expected Result

Supply-chain trust is restored deliberately.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Assume credentials available to the runner may be exposed.

---

## Enhanced CI Lab 98 — Artifact Trust Revocation

### Objective

Practice **Artifact Trust Revocation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
compromised runner ID
→ query build records
→ affected artifact digests
→ revoke/quarantine
```

### Expected Result

Potentially tainted releases can be scoped.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Record builder identity in provenance.

---

## Enhanced CI Lab 99 — CI Migration Dual Run

### Objective

Practice **CI Migration Dual Run** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR
├─ old CI
└─ new CI
compare results/duration
```

### Expected Result

Functional gaps are found before cutover.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Migrate capability and trust controls, not only YAML syntax.

---

## Enhanced CI Lab 100 — Reusable Workflow Contract

### Objective

Practice **Reusable Workflow Contract** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
inputs:
runtime_version
test_command
publish=false

outputs:
artifact_digest
test_report
```

### Expected Result

Teams can consume templates without reading internal implementation.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Treat shared workflows as platform APIs.

---

## Enhanced CI Lab 101 — Reusable Workflow Backward Compatibility

### Objective

Practice **Reusable Workflow Backward Compatibility** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
ci-template/v2 supported
ci-template/v3 recommended
v2 EOL in 90d
```

### Expected Result

Consumers can migrate intentionally.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Avoid silently changing behavior behind mutable references.

---

## Enhanced CI Lab 102 — Pipeline Lint/Test

### Objective

Practice **Pipeline Lint/Test** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
pipeline lint
template unit tests
dry-run/sample repo
```

### Expected Result

Shared CI changes fail before reaching every repository.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Test the delivery system itself.

---

## Enhanced CI Lab 103 — CI Change Canary

### Objective

Practice **CI Change Canary** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
canary repos 5%
→ observe
→ 25%
→ all
```

### Expected Result

Platform regressions have limited blast radius.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Use progressive rollout for CI infrastructure changes.

---

## Enhanced CI Lab 104 — Pipeline Feature Flag

### Objective

Practice **Pipeline Feature Flag** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
scanner_v2=false
→ pilot teams enable
→ validate
→ default true
```

### Expected Result

Migration is staged and reversible.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Set an end date for compatibility flags.

---

## Enhanced CI Lab 105 — Developer Feedback UX

### Objective

Practice **Developer Feedback UX** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
FAIL: tests/test_orders.py::test_total
Expected 100, got 99
See: runbook/test-failure
```

### Expected Result

The next action is obvious.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Design CI output for humans under time pressure.

---

## Enhanced CI Lab 106 — Annotation and PR Summary

### Objective

Practice **Annotation and PR Summary** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
CI Summary:
✓ lint
✓ unit
✗ SCA: 1 critical
artifact: not published
```

### Expected Result

Developers receive one coherent status surface.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep summaries concise and link to detailed evidence.

---

## Enhanced CI Lab 107 — Fast-Path vs Full-Path CI

### Objective

Practice **Fast-Path vs Full-Path CI** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR <10m
main 20m
nightly 90m
```

### Expected Result

Fast feedback and deep assurance coexist.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Never defer essential merge-safety checks to nightly.

---

## Enhanced CI Lab 108 — Scheduled Dependency Refresh

### Objective

Practice **Scheduled Dependency Refresh** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
weekly:
rebuild
rescan
compatibility matrix
```

### Expected Result

Latent ecosystem changes are detected proactively.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep scheduled results owned and actionable.

---

## Enhanced CI Lab 109 — Base Image Rebuild Trigger

### Objective

Practice **Base Image Rebuild Trigger** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
base digest changed
→ rebuild app image
→ tests/scans
→ new release candidate
```

### Expected Result

Patched runtime layers reach applications predictably.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Track base-image lineage.

---

## Enhanced CI Lab 110 — Generated Code Drift Check

### Objective

Practice **Generated Code Drift Check** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```bash
make generate
git diff --exit-code
```

### Expected Result

Generated files remain synchronized with source definitions.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Automate generation rather than relying on developer memory.

---

## Enhanced CI Lab 111 — License Policy Gate

### Objective

Practice **License Policy Gate** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
dependency added
→ license detected
→ allow / review / deny
```

### Expected Result

Legal/compliance risk is caught before release.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Keep policy exceptions reviewable and expiring.

---

## Enhanced CI Lab 112 — Binary Provenance for Compiled Artifacts

### Objective

Practice **Binary Provenance for Compiled Artifacts** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
binary hash
← compiler image digest
← commit
← build ID
```

### Expected Result

Runtime binary identity can be reconstructed.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Embed or attach build metadata.

---

## Enhanced CI Lab 113 — Test Result Provenance

### Objective

Practice **Test Result Provenance** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
test report subject:
commit abc123
artifact sha256:xyz
runner image sha256:runner
```

### Expected Result

Evidence cannot be confused across reruns.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Bind test reports to immutable subjects.

---

## Enhanced CI Lab 114 — Mainline Health SLO

### Objective

Practice **Mainline Health SLO** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
main green 99.4% of working hours
```

### Expected Result

Broken-main impact becomes visible.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Treat a red main branch as a high-priority team incident.

---

## Enhanced CI Lab 115 — Stop-the-Line Automation

### Objective

Practice **Stop-the-Line Automation** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
main CI red
→ merge queue paused
→ team notification
→ revert/fix
```

### Expected Result

Damage does not compound.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Restore main before normal feature work continues.

---

## Enhanced CI Lab 116 — Revertability Check

### Objective

Practice **Revertability Check** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
PR has:
one coherent feature
no irreversible DB contract
feature flag default off
```

### Expected Result

A failed integration can be removed cleanly.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Design changes for reversible integration.

---

## Enhanced CI Lab 117 — CI Change Failure Review

### Objective

Practice **CI Change Failure Review** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
runner image v12 rollout
→ 70% build failures
→ rollback v11
→ root cause + guardrail
```

### Expected Result

Platform learning improves future CI changes.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Operate CI as a production platform.

---

## Enhanced CI Lab 118 — Evidence-First CI Troubleshooting

### Objective

Practice **Evidence-First CI Troubleshooting** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
No run? trigger
Queued? runner/capacity
Checkout? auth/network
Install? dependency
Build? toolchain
Test? code/flake/env
Publish? registry
```

### Expected Result

The failure is placed at one layer before remediation.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Avoid random reruns; classify first.

---

## Enhanced CI Lab 119 — CI Operational Readiness

### Objective

Practice **CI Operational Readiness** as a measurable CI engineering and supply-chain problem.

### Safety Boundary

Use a personal/training repository and disposable runners/containers. Use fake credentials. Never expose real production secrets to fork PRs, debug logs, or untrusted build code.

### Procedure

1. Identify repository, event, branch policy, and trust level.
2. Draw the runner/credential/artifact path.
3. Capture baseline queue time and job duration.
4. Apply or model the configuration below.
5. Run one successful and one controlled failure case.
6. Classify the failure layer.
7. Capture structured evidence.
8. Verify artifact identity if the job publishes.
9. Measure the effect on speed, reliability, and security.
10. Convert the result into a reusable workflow or runbook.

### Code / Configuration

```text
[ ] protected main
[ ] trust-zone runners
[ ] OIDC
[ ] artifact repo
[ ] SBOM/provenance
[ ] CI SLO
[ ] DR
[ ] incident runbooks
```

### Expected Result

The platform is operable and secure before broad adoption.

### Evidence Record

```text
Repository/ref:
Trigger:
Runner:
Trust zone:
Credentials:
Cache:
Build inputs:
Test result:
Security result:
Artifact:
Queue time:
Run time:
Failure class:
Fix:
Prevention:
```

### Best Practice

Make CI readiness a platform launch gate.

---

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — First CI Pipeline

Create a simple repository and design a pipeline with checkout, format, lint, unit test, and package steps.

### Lab 2 — Pipeline-as-Code

Store the pipeline YAML/Jenkinsfile in Git and review it through a pull request.

### Lab 3 — Branch Protection

Configure or document protected main with required CI and review checks.

### Lab 4 — Fast-Fail Ordering

Measure the duration of format, lint, unit, and integration checks and reorder for faster failure.

### Lab 5 — Build Script

Move build logic from CI YAML into a reusable repository script such as `make build` or `scripts/build.sh`.

### Lab 6 — Dependency Locking

Commit a lock file and demonstrate how dependency resolution stays stable.

### Lab 7 — Cache Key

Design a cache key using OS, runtime version, and lock-file hash.

### Lab 8 — Cache Invalidation

Change the lock file and confirm the cache key changes.

### Lab 9 — Artifact Publication

Publish or locally archive a versioned build artifact with commit SHA metadata.

### Lab 10 — Build Once

Promote the same artifact through two simulated environments without rebuilding.

### Lab 11 — Matrix Build

Run or design a matrix across two runtime versions.

### Lab 12 — Test Parallelism

Split tests into multiple jobs and compare total pipeline time.

### Lab 13 — Flaky Test

Create or simulate a flaky test, record repeated outcomes, and write a remediation issue.

### Lab 14 — Integration Service

Run a temporary database/queue service alongside an integration test.

### Lab 15 — Contract Test

Create a simple consumer/provider API contract scenario.

### Lab 16 — Coverage Report

Generate a coverage report and define a sensible non-gaming policy.

### Lab 17 — Security Checks

Add secret scanning, dependency scanning, and SAST/IaC scanning conceptually or with available tools.

### Lab 18 — Container Build

Build a container image in CI and record tag plus digest.

### Lab 19 — Image Scan

Scan the image in an authorized/local workflow and classify findings.

### Lab 20 — SBOM

Generate or design an SBOM artifact tied to the image digest.

### Lab 21 — Provenance

Create a metadata file linking commit, build ID, builder, and artifact digest.

### Lab 22 — OIDC Identity Design

Draw CI → OIDC → cloud role and remove the need for a static key.

### Lab 23 — Least Privilege

Design separate build and deployment permissions.

### Lab 24 — Fork PR Threat Model

Document why forked PR code must not receive production secrets.

### Lab 25 — Hosted vs Self-Hosted

Compare security and operations for hosted, persistent self-hosted, and ephemeral self-hosted runners.

### Lab 26 — Ephemeral Runner

Design lifecycle: create → register → job → cleanup → destroy.

### Lab 27 — Monorepo Change Detection

Create path rules for api/, web/, and shared/ components.

### Lab 28 — Reusable Template

Extract common CI steps into a reusable workflow/template.

### Lab 29 — Merge Queue

Design a merge queue for three concurrent green pull requests.

### Lab 30 — Pipeline Metrics

Collect queue time, execution time, success rate, and top failure categories.

### Lab 31 — Critical Path

Draw the pipeline DAG and identify the critical path.

### Lab 32 — Optimize Slow CI

Choose one slow stage and reduce time using caching, sharding, or parallelism.

### Lab 33 — Nightly Pipeline

Design a nightly full regression/security pipeline distinct from PR CI.

### Lab 34 — Broken Main

Write a runbook for a main-branch-breaking commit.

### Lab 35 — Dependency Outage

Design how an internal package proxy/cache keeps CI running during upstream outage.

### Lab 36 — Registry Outage

Write recovery steps when artifact publication fails after a successful build.

### Lab 37 — Runner Disk Full

Create a troubleshooting checklist for a self-hosted runner with disk exhaustion.

### Lab 38 — Runner Queue

Design autoscaling or capacity response when queue time exceeds the internal SLO.

### Lab 39 — GitHub Actions Example

Write a small workflow with pull_request trigger, two jobs, and explicit minimal permissions.

### Lab 40 — GitLab CI Example

Write a minimal `.gitlab-ci.yml` with stages, artifacts, and rules.

### Lab 41 — Jenkins Example

Write a simple declarative Jenkinsfile with build/test/package stages.

### Lab 42 — Azure Pipelines Example

Write a minimal YAML pipeline with stage/job/step structure.

### Lab 43 — CI Security Review

Threat-model repository, runner, token, cache, artifact, and plugin supply-chain paths.

### Lab 44 — CI Incident Game Day

Simulate untrusted PR attempting to access a secret or privileged runner and define controls.

### Lab 45 — Capstone Validation

Review the mini project against speed, reliability, security, reproducibility, and artifact trust.


## 6. Mini Project

# Mini Project — Production Continuous Integration Platform

Design a CI platform for an organization with:

```text
Python APIs
Node.js frontends
Java services
Terraform repositories
Container images
Kubernetes/OpenShift workloads
```

Required architecture:

```text
Git Platform
    ↓
Pull Request
    ↓
CI Controller
    ↓
Ephemeral Runner Pool
    ├─ Format / Lint
    ├─ Unit Tests
    ├─ Integration Tests
    ├─ SAST / SCA / Secret Scan
    ├─ IaC Scan
    ├─ Container Build
    ├─ Image Scan
    ├─ SBOM
    └─ Provenance
    ↓
Artifact Repository / Registry
```

Required design decisions:

```text
branch protection
merge queue
runner trust zones
OIDC cloud identity
cache strategy
artifact retention
immutable versions
reusable CI templates
monorepo support
flaky-test policy
security severity policy
CI SLOs
CI disaster recovery
```

Required documentation:

```text
CI_ARCHITECTURE.md
RUNNER_SECURITY.md
BRANCH_POLICY.md
CACHE_STRATEGY.md
ARTIFACT_STANDARD.md
CI_SECURITY.md
CI_METRICS.md
CI_DR.md
```

## 7. Recommended Resources

Self-contained material is provided here. For implementation, use the current official documentation for your CI platform and language ecosystem:

```text
GitHub Actions
GitLab CI/CD
Jenkins
Azure Pipelines
Docker
language build/test tooling
artifact repository/registry documentation
```

Prefer official documentation for authentication, runner security, permissions, and artifact-handling details because these change over time.

## 8. Certification Relevance

Relevant to:

```text
DevOps Engineer
Platform Engineer
SRE
Cloud DevOps Engineer
DevSecOps Engineer
Build/Release Engineer
```

It also supports concepts commonly tested or used in cloud DevOps, Git-platform CI/CD, Kubernetes/OpenShift, and Terraform-oriented certification paths.

## 9. Common Mistakes & Best Practices

- **Mistake:** Treating CI as only a build server.  
  **Best practice:** Use CI as a frequent integration and automated feedback system.
- **Mistake:** Long-lived feature branches.  
  **Best practice:** Integrate small changes frequently.
- **Mistake:** Slow PR pipelines.  
  **Best practice:** Optimize the critical path and fail fast.
- **Mistake:** Rerun until green.  
  **Best practice:** Fix flaky tests and infrastructure instability.
- **Mistake:** Secrets available to every job.  
  **Best practice:** Scope secrets and prefer OIDC/short-lived identities.
- **Mistake:** Persistent privileged runners for untrusted PRs.  
  **Best practice:** Use isolated ephemeral runners/trust zones.
- **Mistake:** Rebuilding per environment.  
  **Best practice:** Build once and promote the same artifact.
- **Mistake:** Mutable release versions.  
  **Best practice:** Use immutable artifact versions/digests.
- **Mistake:** Ignoring the dependency lock file.  
  **Best practice:** Pin and deliberately upgrade dependencies.
- **Mistake:** One giant pipeline job.  
  **Best practice:** Split logical jobs and dependencies.
- **Mistake:** Pipeline configured only in UI.  
  **Best practice:** Use pipeline as code.
- **Mistake:** Using cache as artifact storage.  
  **Best practice:** Treat caches as disposable optimization only.
- **Mistake:** Blind scanner suppression.  
  **Best practice:** Use reviewed, expiring exceptions.
- **Mistake:** No CI observability.  
  **Best practice:** Measure queue time, duration, reliability, and failure taxonomy.
- **Mistake:** No CI runbooks.  
  **Best practice:** Operate CI as a critical internal platform.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is Continuous Integration?

**Answer:** Frequent integration of small changes into a shared mainline with automated validation.

### Q2. CI vs build automation?

**Answer:** Build automation creates artifacts; CI adds integration discipline and continuous feedback.

### Q3. Why small changes?

**Answer:** They are easier to review, test, diagnose, and merge.

### Q4. Why trunk-based development?

**Answer:** It reduces branch divergence and supports frequent integration.

### Q5. What is a CI trigger?

**Answer:** An event such as pull request, push, tag, schedule, or manual action that starts a pipeline.

### Q6. Stage vs job?

**Answer:** A stage groups pipeline phases; a job is one executable unit on a runner.

### Q7. Why DAG pipelines?

**Answer:** Independent jobs can run earlier/in parallel, reducing total duration.

### Q8. Runner?

**Answer:** The execution environment that runs CI jobs.

### Q9. Hosted vs self-hosted?

**Answer:** Hosted is provider-managed; self-hosted gives control but adds security/maintenance responsibility.

### Q10. Why ephemeral runners?

**Answer:** Reduce persistence and cross-job contamination.

### Q11. Cache vs artifact?

**Answer:** Cache is disposable performance data; artifact is preserved build output/evidence.

### Q12. Why lock dependencies?

**Answer:** To keep builds reproducible.

### Q13. Why build once?

**Answer:** So every environment runs the same tested artifact.

### Q14. What is a matrix build?

**Answer:** Running a job across multiple OS/runtime/configuration combinations.

### Q15. What is test sharding?

**Answer:** Splitting a test suite across parallel workers.

### Q16. What is a flaky test?

**Answer:** A test that changes result without a relevant code change.

### Q17. Should retries hide flakes?

**Answer:** No; retries should not replace root-cause fixes.

### Q18. What does SAST do?

**Answer:** Analyzes source/compiled code for security issues without running the app.

### Q19. What does SCA do?

**Answer:** Analyzes third-party dependencies for vulnerabilities/licenses.

### Q20. SBOM?

**Answer:** Software inventory associated with an artifact.

### Q21. Provenance?

**Answer:** Evidence describing source and build process for an artifact.

### Q22. Why artifact signing?

**Answer:** To verify integrity and trusted origin.

### Q23. Why OIDC in CI?

**Answer:** To obtain short-lived credentials instead of static keys.

### Q24. Why least privilege?

**Answer:** Reduce blast radius of compromised jobs.

### Q25. Why protect fork PRs?

**Answer:** Untrusted code could exfiltrate secrets or attack runners.

### Q26. Why pin CI actions/plugins?

**Answer:** They are executable dependencies and supply-chain risk.

### Q27. Why pipeline-as-code?

**Answer:** Versioning, review, auditability, and reproducibility.

### Q28. What is a merge queue?

**Answer:** A system that validates queued changes against current integration state before merge.

### Q29. Why status checks?

**Answer:** They enforce automated quality gates before merge.

### Q30. Why fail fast?

**Answer:** Return useful feedback quickly and save CI capacity.

### Q31. Why measure queue time?

**Answer:** It reveals runner-capacity/scheduling problems distinct from job duration.

### Q32. Critical path?

**Answer:** Longest dependent chain determining pipeline completion time.

### Q33. What is a service container?

**Answer:** Temporary dependency such as DB/queue started alongside a CI job.

### Q34. Why integration tests?

**Answer:** Validate real component interactions.

### Q35. Contract tests?

**Answer:** Validate interface expectations between independently deployed systems.

### Q36. Coverage enough for quality?

**Answer:** No; coverage is only a signal.

### Q37. Why structured reports?

**Answer:** Make failures understandable without parsing raw logs.

### Q38. Why internal dependency proxy?

**Answer:** Improve availability, caching, governance, and supply-chain visibility.

### Q39. What is artifact promotion?

**Answer:** Moving the same immutable artifact through lifecycle stages.

### Q40. Why immutable release versions?

**Answer:** Support reproducibility, provenance, and rollback.

### Q41. Why environment-scoped secrets?

**Answer:** Prevent non-production jobs from accessing production credentials.

### Q42. Why runner segmentation?

**Answer:** Different jobs have different trust/network/privilege requirements.

### Q43. Why cancel superseded runs?

**Answer:** Save capacity and shorten feedback for the latest commit.

### Q44. Why nightly CI?

**Answer:** Run expensive full regression/security suites without slowing every PR.

### Q45. What to do if main breaks?

**Answer:** Prioritize restoring it via revert or fix-forward.

### Q46. Why CI needs DR?

**Answer:** Git/CI/registry are critical delivery control-plane dependencies.

### Q47. Why self-hosted runner patching matters?

**Answer:** The runner executes potentially risky code and often has privileged network access.

### Q48. Why no permanent shared workspace?

**Answer:** Residue creates nondeterminism and security risk.

### Q49. What is the final CI output?

**Answer:** Trusted evidence plus a reproducible immutable artifact.

### Q50. Core CI goal?

**Answer:** Fast, reliable feedback that keeps the mainline healthy.



# Expanded Self-Assessment Bank — Continuous Integration

### Q1. What is the key CI engineering lesson from **Pre-Merge Test Merge Commit**?

**Answer:** Validate the integrated result before final merge.

### Q2. What is the key CI engineering lesson from **Merge Queue Serialization**?

**Answer:** Use merge queues in high-change repositories with strict mainline health.

### Q3. What is the key CI engineering lesson from **Branch Protection as Policy**?

**Answer:** Treat branch protection as production policy.

### Q4. What is the key CI engineering lesson from **Status Check Design**?

**Answer:** Only make a check required when the team trusts its signal.

### Q5. What is the key CI engineering lesson from **PR Size Guardrail**?

**Answer:** Prefer guidance and ownership over arbitrary hard limits.

### Q6. What is the key CI engineering lesson from **Review Queue SLO**?

**Answer:** Optimize human queues as seriously as runner queues.

### Q7. What is the key CI engineering lesson from **Pipeline Critical Path**?

**Answer:** Profile the DAG before adding parallelism.

### Q8. What is the key CI engineering lesson from **Queue Time vs Run Time**?

**Answer:** Track queue p50/p95 separately from job duration.

### Q9. What is the key CI engineering lesson from **Runner Capacity Headroom**?

**Answer:** Maintain autoscaling or reserved headroom for peak feedback demand.

### Q10. What is the key CI engineering lesson from **Runner Autoscaling Signal**?

**Answer:** Scale from demand while enforcing upper cost limits.

### Q11. What is the key CI engineering lesson from **Ephemeral Runner Lifecycle**?

**Answer:** Prefer ephemeral runners for privileged or untrusted workloads.

### Q12. What is the key CI engineering lesson from **Runner Trust Zones**?

**Answer:** Route jobs by trust requirement, not convenience.

### Q13. What is the key CI engineering lesson from **Fork PR Isolation**?

**Answer:** Treat repository code as executable input.

### Q14. What is the key CI engineering lesson from **pull_request vs Privileged Event Semantics**?

**Answer:** Separate untrusted validation from privileged follow-up jobs.

### Q15. What is the key CI engineering lesson from **Workflow Token Minimization**?

**Answer:** Grant write permissions only to jobs that truly publish/change something.

### Q16. What is the key CI engineering lesson from **OIDC Claim Restriction**?

**Answer:** Constrain federation with contextual claims.

### Q17. What is the key CI engineering lesson from **Short-Lived Release Credentials**?

**Answer:** Prefer federated identity for CI/CD.

### Q18. What is the key CI engineering lesson from **Secret Fan-Out Analysis**?

**Answer:** Scope secrets by job, environment, and trust zone.

### Q19. What is the key CI engineering lesson from **Secret Redaction Limits**?

**Answer:** Do not expose secrets to untrusted code in the first place.

### Q20. What is the key CI engineering lesson from **Shell Trace Risk**?

**Answer:** Disable shell tracing around credentials and use stdin/file mechanisms.

### Q21. What is the key CI engineering lesson from **Pipeline Definition Review**?

**Answer:** Protect CI configuration paths explicitly.

### Q22. What is the key CI engineering lesson from **Shared Workflow Version Pinning**?

**Answer:** Upgrade shared workflow versions deliberately.

### Q23. What is the key CI engineering lesson from **Jenkins Plugin Attack Surface**?

**Answer:** Minimize plugins and maintain an ownership/upgrade process.

### Q24. What is the key CI engineering lesson from **Controller/Runner Separation**?

**Answer:** Keep execution isolated from CI control-plane state.

### Q25. What is the key CI engineering lesson from **Runner Image Supply Chain**?

**Answer:** Treat runner images as production artifacts.

### Q26. What is the key CI engineering lesson from **Build Container Pinning**?

**Answer:** Promote build images like any other critical dependency.

### Q27. What is the key CI engineering lesson from **Hermetic Build Boundary**?

**Answer:** Remove undeclared environmental inputs incrementally.

### Q28. What is the key CI engineering lesson from **SOURCE_DATE_EPOCH Concept**?

**Answer:** Use ecosystem-specific reproducible-build guidance.

### Q29. What is the key CI engineering lesson from **Locale and Timezone Reproducibility**?

**Answer:** Control locale/timezone inputs instead of relying on host defaults.

### Q30. What is the key CI engineering lesson from **Dependency Lock Integrity**?

**Answer:** Use frozen/immutable dependency install modes.

### Q31. What is the key CI engineering lesson from **Dependency Confusion Defense**?

**Answer:** Reserve namespaces and configure scoped registries.

### Q32. What is the key CI engineering lesson from **Typosquatting Review**?

**Answer:** Require approval for new external dependencies.

### Q33. What is the key CI engineering lesson from **Internal Dependency Proxy**?

**Answer:** Harden the proxy as critical supply-chain infrastructure.

### Q34. What is the key CI engineering lesson from **Cache Trust Domains**?

**Answer:** Partition cache keys and permissions by trust level.

### Q35. What is the key CI engineering lesson from **Cache Key Completeness**?

**Answer:** Prefer under-caching to silently reusing incompatible output.

### Q36. What is the key CI engineering lesson from **Remote Build Cache**?

**Answer:** Treat remote cache as supply-chain data, not only performance data.

### Q37. What is the key CI engineering lesson from **Cache Poisoning Detection**?

**Answer:** Keep a clean-build troubleshooting path.

### Q38. What is the key CI engineering lesson from **Artifact vs Cache Enforcement**?

**Answer:** Never promote from a transient cache.

### Q39. What is the key CI engineering lesson from **Build Once Evidence**?

**Answer:** Make artifact publication the terminal CI contract.

### Q40. What is the key CI engineering lesson from **Artifact Immutability Policy**?

**Answer:** Publish a new version for every changed artifact.

### Q41. What is the key CI engineering lesson from **Container Digest Capture**?

**Answer:** Pass the digest as pipeline output/evidence.

### Q42. What is the key CI engineering lesson from **SBOM Generation Placement**?

**Answer:** Retain SBOM with artifact lineage.

### Q43. What is the key CI engineering lesson from **Provenance Attestation**?

**Answer:** Generate provenance inside the trusted build boundary.

### Q44. What is the key CI engineering lesson from **Artifact Signing Identity**?

**Answer:** Verify signer identity and digest before promotion.

### Q45. What is the key CI engineering lesson from **SLSA Build Threat Model**?

**Answer:** Adopt controls according to realistic threats.

### Q46. What is the key CI engineering lesson from **Test Pyramid Economics**?

**Answer:** Keep expensive end-to-end tests focused on critical journeys.

### Q47. What is the key CI engineering lesson from **Contract Test Placement**?

**Answer:** Version contracts and assign ownership.

### Q48. What is the key CI engineering lesson from **Integration Test Containers**?

**Answer:** Pin service versions and wait for readiness explicitly.

### Q49. What is the key CI engineering lesson from **Integration Environment Namespacing**?

**Answer:** Enforce quotas and automatic deletion.

### Q50. What is the key CI engineering lesson from **Test Data Factory**?

**Answer:** Use synthetic or properly masked data.

### Q51. What is the key CI engineering lesson from **Database Migration CI**?

**Answer:** Test migration duration and locking, not only correctness.

### Q52. What is the key CI engineering lesson from **Mutation Testing**?

**Answer:** Use selectively because mutation testing can be expensive.

### Q53. What is the key CI engineering lesson from **Coverage Diff Policy**?

**Answer:** Use coverage as one signal among many.

### Q54. What is the key CI engineering lesson from **Flake Rate**?

**Answer:** Track by test owner and duration.

### Q55. What is the key CI engineering lesson from **Flake Quarantine SLA**?

**Answer:** Expire quarantine automatically.

### Q56. What is the key CI engineering lesson from **Infrastructure Failure Classification**?

**Answer:** Do not charge infrastructure failures against product quality.

### Q57. What is the key CI engineering lesson from **Retry Taxonomy**?

**Answer:** Retry by classified error, not blanket pipeline rerun.

### Q58. What is the key CI engineering lesson from **Exponential Backoff for External Services**?

**Answer:** Add jitter and a total retry budget.

### Q59. What is the key CI engineering lesson from **Timeout Budget per Job**?

**Answer:** Alert on timeout trend rather than only increasing limits.

### Q60. What is the key CI engineering lesson from **Cancellation of Superseded Runs**?

**Answer:** Enable concurrency groups/cancellation where safe.

### Q61. What is the key CI engineering lesson from **Test Impact Analysis**?

**Answer:** Keep a regular full regression to validate impact mapping.

### Q62. What is the key CI engineering lesson from **Monorepo Dependency Graph**?

**Answer:** Use graph-aware tooling for complex monorepos.

### Q63. What is the key CI engineering lesson from **Polyrepo Contract Registry**?

**Answer:** Make interface compatibility part of CI.

### Q64. What is the key CI engineering lesson from **Matrix Strategy Sampling**?

**Answer:** Design the matrix from support policy.

### Q65. What is the key CI engineering lesson from **Architecture Matrix**?

**Answer:** Use real or emulated testing according to risk.

### Q66. What is the key CI engineering lesson from **BuildKit Cache Strategy**?

**Answer:** Use BuildKit secret mounts instead of ARG/ENV for build secrets.

### Q67. What is the key CI engineering lesson from **Secret Mount in Container Build**?

**Answer:** Verify final image does not contain secret files.

### Q68. What is the key CI engineering lesson from **Rootless Build Workers**?

**Answer:** Avoid exposing privileged runtime sockets to untrusted jobs.

### Q69. What is the key CI engineering lesson from **Docker Socket Risk**?

**Answer:** Use isolated builders or dedicated ephemeral hosts.

### Q70. What is the key CI engineering lesson from **Kubernetes CI Runner Isolation**?

**Answer:** Separate runner trust zones at namespace and node/network layers.

### Q71. What is the key CI engineering lesson from **CI Network Egress Policy**?

**Answer:** Combine network controls with identity controls.

### Q72. What is the key CI engineering lesson from **Cloud Metadata Blocking**?

**Answer:** Use workload identity and metadata hardening.

### Q73. What is the key CI engineering lesson from **Artifact Publication Permission Split**?

**Answer:** Separate repositories and credentials by lifecycle.

### Q74. What is the key CI engineering lesson from **Release Tag Trust**?

**Answer:** Protect tag creation and reject moving release tags.

### Q75. What is the key CI engineering lesson from **Signed Commit/Tag Context**?

**Answer:** Verify signatures where they support a real trust requirement.

### Q76. What is the key CI engineering lesson from **Reproducible Release Build**?

**Answer:** Keep canonical build logic in the repository.

### Q77. What is the key CI engineering lesson from **CI Evidence Retention**?

**Answer:** Define retention by evidence value and compliance needs.

### Q78. What is the key CI engineering lesson from **CI Audit Events**?

**Answer:** Forward high-value audit events to centralized logging/SIEM.

### Q79. What is the key CI engineering lesson from **CI Deployment Marker Boundary**?

**Answer:** Avoid giving build pipelines unnecessary production access.

### Q80. What is the key CI engineering lesson from **Quality Gate Exceptions**?

**Answer:** Make bypasses narrow and expiring.

### Q81. What is the key CI engineering lesson from **Security Finding Baseline**?

**Answer:** Do not let the baseline grow.

### Q82. What is the key CI engineering lesson from **Policy as Code Unit Tests**?

**Answer:** Version and test policy code.

### Q83. What is the key CI engineering lesson from **Scanner Availability Strategy**?

**Answer:** Make failure policy explicit per control.

### Q84. What is the key CI engineering lesson from **Scanner False-Positive Workflow**?

**Answer:** Review suppression files like production policy.

### Q85. What is the key CI engineering lesson from **Vulnerability DB Freshness**?

**Answer:** Monitor scanner feed age.

### Q86. What is the key CI engineering lesson from **Post-Build Rescanning**?

**Answer:** Keep artifact-to-owner mapping for rapid remediation.

### Q87. What is the key CI engineering lesson from **CI Platform SLO**?

**Answer:** Separate CI-platform failures from application failures.

### Q88. What is the key CI engineering lesson from **CI Error Budget**?

**Answer:** Use error-budget policy for internal platforms too.

### Q89. What is the key CI engineering lesson from **Pipeline Duration Percentiles**?

**Answer:** Optimize percentile feedback time, not only averages.

### Q90. What is the key CI engineering lesson from **Top Failure Category Dashboard**?

**Answer:** Auto-classify where possible, sample manually to validate.

### Q91. What is the key CI engineering lesson from **Runner Disk Pressure**?

**Answer:** Use ephemeral runners or automated cleanup with quotas.

### Q92. What is the key CI engineering lesson from **Runner CPU/Memory Saturation**?

**Answer:** Set concurrency based on measured resource usage.

### Q93. What is the key CI engineering lesson from **Shared Test Environment Contention**?

**Answer:** Prefer ephemeral isolated environments or strict tenancy.

### Q94. What is the key CI engineering lesson from **CI Dependency Outage Runbook**?

**Answer:** Maintain dependency status/runbooks.

### Q95. What is the key CI engineering lesson from **Registry Publication Recovery**?

**Answer:** Separate build success from publication success.

### Q96. What is the key CI engineering lesson from **CI Disaster Recovery Order**?

**Answer:** Practice rebuild from IaC/config-as-code.

### Q97. What is the key CI engineering lesson from **Runner Compromise Response**?

**Answer:** Assume credentials available to the runner may be exposed.

### Q98. What is the key CI engineering lesson from **Artifact Trust Revocation**?

**Answer:** Record builder identity in provenance.

### Q99. What is the key CI engineering lesson from **CI Migration Dual Run**?

**Answer:** Migrate capability and trust controls, not only YAML syntax.

### Q100. What is the key CI engineering lesson from **Reusable Workflow Contract**?

**Answer:** Treat shared workflows as platform APIs.

### Q101. What is the key CI engineering lesson from **Reusable Workflow Backward Compatibility**?

**Answer:** Avoid silently changing behavior behind mutable references.

### Q102. What is the key CI engineering lesson from **Pipeline Lint/Test**?

**Answer:** Test the delivery system itself.

### Q103. What is the key CI engineering lesson from **CI Change Canary**?

**Answer:** Use progressive rollout for CI infrastructure changes.

### Q104. What is the key CI engineering lesson from **Pipeline Feature Flag**?

**Answer:** Set an end date for compatibility flags.

### Q105. What is the key CI engineering lesson from **Developer Feedback UX**?

**Answer:** Design CI output for humans under time pressure.

### Q106. What is the key CI engineering lesson from **Annotation and PR Summary**?

**Answer:** Keep summaries concise and link to detailed evidence.

### Q107. What is the key CI engineering lesson from **Fast-Path vs Full-Path CI**?

**Answer:** Never defer essential merge-safety checks to nightly.

### Q108. What is the key CI engineering lesson from **Scheduled Dependency Refresh**?

**Answer:** Keep scheduled results owned and actionable.

### Q109. What is the key CI engineering lesson from **Base Image Rebuild Trigger**?

**Answer:** Track base-image lineage.

### Q110. What is the key CI engineering lesson from **Generated Code Drift Check**?

**Answer:** Automate generation rather than relying on developer memory.

### Q111. What is the key CI engineering lesson from **License Policy Gate**?

**Answer:** Keep policy exceptions reviewable and expiring.

### Q112. What is the key CI engineering lesson from **Binary Provenance for Compiled Artifacts**?

**Answer:** Embed or attach build metadata.

### Q113. What is the key CI engineering lesson from **Test Result Provenance**?

**Answer:** Bind test reports to immutable subjects.

### Q114. What is the key CI engineering lesson from **Mainline Health SLO**?

**Answer:** Treat a red main branch as a high-priority team incident.

### Q115. What is the key CI engineering lesson from **Stop-the-Line Automation**?

**Answer:** Restore main before normal feature work continues.

### Q116. What is the key CI engineering lesson from **Revertability Check**?

**Answer:** Design changes for reversible integration.

### Q117. What is the key CI engineering lesson from **CI Change Failure Review**?

**Answer:** Operate CI as a production platform.

### Q118. What is the key CI engineering lesson from **Evidence-First CI Troubleshooting**?

**Answer:** Avoid random reruns; classify first.

### Q119. What is the key CI engineering lesson from **CI Operational Readiness**?

**Answer:** Make CI readiness a platform launch gate.