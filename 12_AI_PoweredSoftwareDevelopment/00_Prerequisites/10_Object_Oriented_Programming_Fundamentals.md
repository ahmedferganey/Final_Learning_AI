# Object-Oriented Programming Fundamentals

> **Phase 2 — Programming Foundations**

This version is intentionally example-driven. Every major concept includes code, execution reasoning, and practical infrastructure/security-oriented examples. Do not only read the code: type it, change it, break it, and repair it.

## 1. Topic Title

**Object-Oriented Programming Fundamentals**

## 2. Learning Objectives

- Model coherent domain concepts with classes.
- Apply encapsulation, abstraction, inheritance, polymorphism, and composition.
- Use dataclasses and invariants appropriately.
- Apply dependency injection for testability.
- Use SOLID as design-review heuristics without overengineering.

## 3. Prerequisites

- Python Programming Fundamentals.
- Functions, modules, exceptions, and type hints.
- Phase 1 Introduction to Software Engineering.

## 4. Core Concepts Explanation

### 1. OOP as a Way to Model Responsibilities

OOP is not "put everything in a class." It is a way to create coherent units that combine state and behavior.

Procedural version:

```python
server = {"hostname": "web-01", "cpu": 82}

def status(server):
    return "warning" if server["cpu"] >= 75 else "normal"
```

Object-oriented version:

```python
class Server:
    def __init__(self, hostname: str, cpu: float) -> None:
        self.hostname = hostname
        self.cpu = cpu

    def status(self) -> str:
        return "warning" if self.cpu >= 75 else "normal"

server = Server("web-01", 82)
print(server.status())
```

Neither is automatically better. The class becomes useful when `Server` is a meaningful domain concept with multiple related behaviors and invariants.

### 2. Classes, Objects, Constructors, and Invariants

A constructor should establish valid state.

```python
class Endpoint:
    def __init__(self, host: str, port: int) -> None:
        if not host:
            raise ValueError("host is required")
        if not 1 <= port <= 65535:
            raise ValueError("invalid port")
        self.host = host
        self.port = port

    def url(self) -> str:
        return f"https://{self.host}:{self.port}"
```

The invariant is: every valid `Endpoint` has a non-empty host and a valid port. That simplifies later methods because they do not need to repeatedly check basic object validity.

### 3. Encapsulation with a Stable Public Interface

Suppose secrets may later move from environment variables to a secret manager.

Bad coupling:

```python
import os
api_key = os.environ["API_KEY"]
```

Repeated everywhere, storage details leak across the codebase.

Encapsulate access:

```python
class SecretStore:
    def get(self, name: str) -> str:
        raise NotImplementedError


class EnvironmentSecretStore(SecretStore):
    def get(self, name: str) -> str:
        import os
        value = os.getenv(name)
        if value is None:
            raise KeyError(name)
        return value
```

Callers depend on `get(name)`, not the storage mechanism. Later a cloud implementation can replace the environment implementation.

### 4. Abstraction and Interfaces

An abstraction should reflect what the application needs.

```python
from typing import Protocol

class Storage(Protocol):
    def upload(self, name: str, data: bytes) -> None: ...
    def download(self, name: str) -> bytes: ...
```

Local implementation:

```python
from pathlib import Path

class LocalStorage:
    def __init__(self, root: Path) -> None:
        self.root = root

    def upload(self, name: str, data: bytes) -> None:
        (self.root / name).write_bytes(data)

    def download(self, name: str) -> bytes:
        return (self.root / name).read_bytes()
```

A service can accept any object implementing the required behavior. This is a practical form of polymorphism.

### 5. Inheritance and Method Overriding

Inheritance models a specialization relationship.

```python
class Server:
    def restart(self) -> str:
        return "generic restart"

class LinuxServer(Server):
    def restart(self) -> str:
        return "systemctl reboot"

class WindowsServer(Server):
    def restart(self) -> str:
        return "Restart-Computer"
```

Polymorphic use:

```python
servers: list[Server] = [LinuxServer(), WindowsServer()]
for server in servers:
    print(server.restart())
```

But inheritance solely for code reuse can create bad hierarchies. Ask: **Can every subclass be safely used where the base type is expected?**

### 6. Composition over Inheritance

Composition means a class **has/uses** collaborators.

```python
class Logger:
    def info(self, message: str) -> None:
        print("INFO", message)

class DeploymentService:
    def __init__(self, provider, logger: Logger) -> None:
        self.provider = provider
        self.logger = logger

    def deploy(self, app: str) -> None:
        self.logger.info(f"deploying {app}")
        self.provider.deploy(app)
```

`DeploymentService` is not a subclass of `Logger` or cloud provider. It **uses** them. This produces lower coupling and easier testing.

### 7. Polymorphism Without Big if/elif Blocks

Provider-specific branching often grows badly:

```python
# less extensible
if provider == "aws":
    ...
elif provider == "azure":
    ...
elif provider == "gcp":
    ...
```

Replace with behavior:

```python
class AwsProvider:
    def deploy(self, app: str) -> None:
        print("AWS deploy", app)

class AzureProvider:
    def deploy(self, app: str) -> None:
        print("Azure deploy", app)


def run_deployment(provider, app: str) -> None:
    provider.deploy(app)
```

Adding GCP no longer requires editing `run_deployment`. This demonstrates the Open/Closed idea in a small, concrete way.

### 8. Dataclasses and Value Objects

For structured data, dataclasses reduce boilerplate.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkEndpoint:
    host: str
    port: int

    def __post_init__(self) -> None:
        if not 1 <= self.port <= 65535:
            raise ValueError("invalid port")
```

`frozen=True` discourages mutation after construction. A value object is compared by its values:

```python
a = NetworkEndpoint("db.internal", 5432)
b = NetworkEndpoint("db.internal", 5432)
print(a == b)  # True
```

This is ideal for stable configuration-like concepts.

### 9. Properties and Controlled Mutation

A property can enforce an invariant while preserving attribute-like use.

```python
class Health:
    def __init__(self, cpu: float) -> None:
        self.cpu = cpu

    @property
    def cpu(self) -> float:
        return self._cpu

    @cpu.setter
    def cpu(self, value: float) -> None:
        if not 0 <= value <= 100:
            raise ValueError("CPU must be 0..100")
        self._cpu = value
```

Do not hide expensive network calls behind properties. Callers expect `obj.attribute` to be cheap and predictable.

### 10. Dependency Injection for Testability

A tightly coupled service:

```python
class ReportService:
    def send(self, report: str) -> None:
        client = RealEmailClient()  # hard-coded dependency
        client.send(report)
```

Hard to test without email side effects.

Inject the dependency:

```python
class ReportService:
    def __init__(self, client) -> None:
        self.client = client

    def send(self, report: str) -> None:
        self.client.send(report)


class FakeEmailClient:
    def __init__(self) -> None:
        self.sent = []

    def send(self, report: str) -> None:
        self.sent.append(report)
```

Test:

```python
fake = FakeEmailClient()
service = ReportService(fake)
service.send("all healthy")
assert fake.sent == ["all healthy"]
```

No real external system is required.

### 11. SOLID with Infrastructure Examples

Use SOLID as review questions, not rigid laws.

**Single Responsibility**

Bad: one `CloudManager` class loads YAML, validates it, authenticates, deploys resources, sends Slack messages, and writes reports.

Better split:

```text
ConfigLoader
PlanValidator
CloudProvider
DeploymentService
Notifier
ReportWriter
```

**Open/Closed**: add a new provider implementation without modifying deployment orchestration.

**Liskov Substitution**: every provider used as `CloudProvider` must honor the same behavioral expectations.

**Interface Segregation**: a read-only monitoring component should not be forced to implement deployment/delete methods.

**Dependency Inversion**: orchestration depends on a provider interface, not directly on a vendor SDK.

### 12. Class Design Smells

Common smells:

```text
God Class               → too many unrelated responsibilities
Deep inheritance        → behavior becomes difficult to trace
Feature envy            → method mostly manipulates another object's data
Primitive obsession     → important domain concepts represented by loose strings/ints
Hidden I/O              → property/method unexpectedly performs network or disk side effects
```

Example of primitive obsession:

```python
# weak
connect("db.internal", 5432)

# stronger domain object
endpoint = NetworkEndpoint("db.internal", 5432)
connect(endpoint)
```

The second form can centralize validation and make interfaces clearer.

### 13. Worked Example: Provider-Agnostic Backup Service

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

class Storage(Protocol):
    def upload(self, name: str, data: bytes) -> None: ...

@dataclass(frozen=True)
class BackupRequest:
    source: Path
    remote_name: str

class LocalStorage:
    def __init__(self, root: Path) -> None:
        self.root = root

    def upload(self, name: str, data: bytes) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / name).write_bytes(data)

class BackupService:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def run(self, request: BackupRequest) -> None:
        if not request.source.is_file():
            raise FileNotFoundError(request.source)
        self.storage.upload(request.remote_name, request.source.read_bytes())
```

Usage:

```python
storage = LocalStorage(Path("./backup_target"))
service = BackupService(storage)
service.run(BackupRequest(Path("config.json"), "config-backup.json"))
```

Why this design is useful:

- `BackupService` owns orchestration.
- `Storage` abstracts destination behavior.
- `BackupRequest` is immutable structured input.
- A fake storage implementation can be injected in tests.
- A future cloud provider can be added without changing backup orchestration.

## 5. Hands-on Lab / Practical Exercises

### Lab — Infrastructure asset model

1. Create `Asset`, `Server`, `Database`, and `NetworkDevice`.
2. Define one stable public method such as `summary()`.
3. Store mixed objects in one list and call the method polymorphically.
4. Add invariants for names and ports.

**Starter / reference code:**

```python
class Asset:
    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError("name required")
        self.name = name

    def summary(self) -> str:
        return self.name

class Server(Asset):
    def __init__(self, name: str, os_name: str) -> None:
        super().__init__(name)
        self.os_name = os_name

    def summary(self) -> str:
        return f"Server {self.name} ({self.os_name})"
```

**Expected result:** A coherent object model with controlled specialization.

### Lab — Storage polymorphism

1. Define a `Storage` protocol.
2. Implement local and fake storage.
3. Inject storage into a backup service.
4. Write tests using fake storage.

**Starter / reference code:**

```python
class FakeStorage:
    def __init__(self):
        self.objects = {}

    def upload(self, name: str, data: bytes) -> None:
        self.objects[name] = data
```

**Expected result:** A testable provider-agnostic service.

### Lab — Refactor procedural automation

1. Take a Python script with config loading, validation, and reporting.
2. Identify responsibilities.
3. Create classes only where state+behavior benefit from a boundary.
4. Keep pure helpers as functions when a class adds no value.

**Starter / reference code:**

```python
# Rule: do not create EmptyManager/Utils classes simply to "use OOP".
```

**Expected result:** A deliberate comparison of procedural and object-oriented designs.

## 6. Mini Project

### Mini Project — Multi-Provider Deployment Planner (Simulation)

Build a simulation; do **not** create real cloud resources.

```text
planner/
├── domain.py
├── providers.py
├── policy.py
├── service.py
├── main.py
└── tests/
```

**Requirements**

- `DeploymentRequest` dataclass.
- Provider protocol/interface with `validate()` and `deploy()`.
- AWS, Azure, and Local mock providers.
- `PolicyValidator` for environment/resource rules.
- `DeploymentService` receives dependencies through its constructor.
- Custom `InvalidPlanError`.
- Tests use fake providers and verify calls/results.
- Add a fourth provider without modifying deployment orchestration; document how this demonstrates polymorphism/Open-Closed.

## 7. Recommended Resources

- Python Classes tutorial.
- Python `dataclasses`, `abc`, and `typing.Protocol` documentation.
- Refactoring.Guru for patterns only after mastering basic principles.
- Martin Fowler articles on refactoring and dependency injection as optional deeper reading.

## 8. Certification Relevance

OOP is important for backend engineering, cloud SDK wrappers, automation frameworks, microservices, testability, and software-design interviews. It is more of a professional engineering skill than a direct infrastructure certification objective.

## 9. Common Mistakes & Best Practices

- **Mistake:** Turning every noun into a class.
  - **Best practice:** Use classes when a coherent state+behavior boundary is useful.
- **Mistake:** Using inheritance only for code reuse.
  - **Best practice:** Prefer composition unless a true substitutable specialization exists.
- **Mistake:** God classes.
  - **Best practice:** Split by responsibility and reason to change.
- **Mistake:** Hard-coding SDK/network clients in business logic.
  - **Best practice:** Inject dependencies so tests can use fakes.
- **Mistake:** Applying design patterns mechanically.
  - **Best practice:** Start from the problem and add abstraction only when justified.
- **Mistake:** Leaking internal mutable state.
  - **Best practice:** Protect important invariants through stable interfaces.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is encapsulation?

**Answer:** Hiding implementation details behind a controlled public interface.

### Q2. What is abstraction?

**Answer:** Exposing essential behavior while hiding irrelevant detail.

### Q3. What is polymorphism?

**Answer:** Using different implementations through a common behavioral interface.

### Q4. When is inheritance appropriate?

**Answer:** When a true substitutable specialization relationship exists.

### Q5. Why prefer composition often?

**Answer:** It lowers coupling and improves replaceability/testability.

### Q6. What is dependency injection?

**Answer:** Supplying collaborators from outside rather than constructing them internally.

### Q7. What is an invariant?

**Answer:** A condition that should always hold for a valid object.

### Q8. What is a dataclass good for?

**Answer:** Concise structured data/value models.

### Q9. What does SRP ask?

**Answer:** Whether a component has one primary reason to change.

### Q10. Why can a fake client improve tests?

**Answer:** It removes real external side effects while preserving the behavioral contract.

## End-of-Module Practice Checklist

- [ ] I typed the examples myself instead of only reading them.
- [ ] I changed inputs and predicted results before running the code.
- [ ] I intentionally introduced at least three errors and debugged them.
- [ ] I completed the labs without copying the final solution first.
- [ ] I completed the mini project and wrote a short README.
- [ ] I can explain the important design choices aloud.

## Extended Worked Exercises

### Exercise 1 — Identify responsibility boundaries

Given a class that reads YAML, validates configuration, deploys cloud resources, formats HTML, and sends mail, propose a decomposition. Explain the reason-to-change for each resulting component.

### Exercise 2 — Composition vs inheritance

Compare:

```python
class DeploymentService(Logger, AwsClient):
    ...
```

with:

```python
class DeploymentService:
    def __init__(self, provider, logger):
        self.provider = provider
        self.logger = logger
```

Explain why the second usually models the relationships more accurately.

### Exercise 3 — Fake dependency

```python
class FakeProvider:
    def __init__(self):
        self.deployed = []

    def deploy(self, app):
        self.deployed.append(app)
```

Use it to test orchestration with no cloud access.

### Exercise 4 — Domain exception

```python
class InvalidDeploymentPlan(Exception):
    pass
```

Raise this only for domain validation errors; do not convert every unexpected programming defect into the same exception.

### Exercise 5 — Adding a provider

Implement `GcpProvider` after AWS/Azure. If you must edit ten existing files, the abstraction is probably too coupled. If only provider registration/configuration changes, the boundary is stronger.

### Design Review Questions

- Can I instantiate this class in a unit test without real credentials?
- Does this class know more than it should about another component?
- Are public methods expressing domain operations or exposing internal storage details?
- Is inheritance being used for substitutability or merely convenience?
- Is an abstraction solving an actual variation/testing problem?


## Practical Code Notebook — OOP

### Example A — Start procedural, introduce a class only when it helps

Procedural:

```python
def validate_server(server: dict) -> list[str]:
    errors = []
    if not server.get("hostname"):
        errors.append("hostname required")
    return errors
```

If the system later gains multiple server operations and invariants, a class may improve cohesion:

```python
class Server:
    def __init__(self, hostname: str, environment: str) -> None:
        if not hostname:
            raise ValueError("hostname required")
        if environment not in {"dev", "test", "prod"}:
            raise ValueError("invalid environment")
        self.hostname = hostname
        self.environment = environment

    def is_production(self) -> bool:
        return self.environment == "prod"
```

The lesson: OOP is a tool for managing a model, not a requirement for every function.

### Example B — Interface segregation

Too broad:

```python
class CloudPlatform(Protocol):
    def deploy(self): ...
    def delete(self): ...
    def read_metrics(self): ...
    def rotate_keys(self): ...
    def create_database(self): ...
```

A monitoring component only needs metrics. Prefer a focused interface:

```python
class MetricsReader(Protocol):
    def read_metrics(self) -> dict: ...
```

Clients should depend only on capabilities they actually use.

### Example C — Factory method from configuration

```python
from dataclasses import dataclass

@dataclass
class Endpoint:
    host: str
    port: int

    @classmethod
    def from_dict(cls, data: dict) -> "Endpoint":
        return cls(
            host=data["host"],
            port=int(data.get("port", 443)),
        )
```

A class method can provide an alternative construction path while keeping object invariants centralized.

### Example D — Strategy pattern without ceremony

```python
class RetryPolicy(Protocol):
    def should_retry(self, attempt: int, error: Exception) -> bool: ...

class NoRetry:
    def should_retry(self, attempt: int, error: Exception) -> bool:
        return False

class ThreeAttempts:
    def should_retry(self, attempt: int, error: Exception) -> bool:
        return attempt < 3
```

A service can receive a policy object. The algorithm varies independently from the service itself.

### Example E — Liskov-style substitution failure

Imagine a base abstraction says `delete(name)` removes an object or reports a normal not-found result. A subclass that instead deletes an entire bucket violates caller expectations even if the method name matches. Substitutability is about **behavioral contract**, not just method signatures.

### Example F — Domain service with injected repository

```python
class AssetRepository(Protocol):
    def get(self, asset_id: str): ...
    def save(self, asset) -> None: ...

class AssetService:
    def __init__(self, repository: AssetRepository) -> None:
        self.repository = repository

    def mark_critical(self, asset_id: str) -> None:
        asset = self.repository.get(asset_id)
        asset.critical = True
        self.repository.save(asset)
```

Test repository:

```python
class InMemoryRepository:
    def __init__(self, assets):
        self.assets = {a.id: a for a in assets}

    def get(self, asset_id):
        return self.assets[asset_id]

    def save(self, asset):
        self.assets[asset.id] = asset
```

The service can be tested without a real database.

### Example G — Custom exception hierarchy

```python
class DeploymentError(Exception):
    pass

class InvalidPlanError(DeploymentError):
    pass

class ProviderUnavailableError(DeploymentError):
    pass
```

Higher-level code can catch `DeploymentError` for domain failures while still distinguishing validation from provider availability when needed.

### Example H — Composition graph

```text
DeploymentService
 ├── Provider
 ├── PolicyValidator
 ├── AuditLogger
 └── Notifier
```

Each collaborator has a focused responsibility. The service orchestrates; it does not inherit from any of them.

### Example I — Immutable configuration

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class DeploymentConfig:
    environment: str
    region: str
    replicas: int

    def __post_init__(self):
        if self.environment not in {"dev", "test", "prod"}:
            raise ValueError("invalid environment")
        if self.replicas < 1:
            raise ValueError("replicas must be positive")
```

Immutability makes configuration easier to reason about: once validated, it does not change unexpectedly halfway through deployment.

### Example J — Tell, don't ask

Less object-oriented:

```python
if server.cpu > 90:
    server.alerts.append("high cpu")
```

More behavior-oriented:

```python
server.evaluate_health()
```

The object owns the rules that preserve its state. This is useful when health logic is genuinely part of the server domain model. Do not apply the rule mechanically; sometimes a separate monitoring service is the better owner.

### Example K — Unit test with fake provider

```python
class FakeProvider:
    def __init__(self):
        self.calls = []

    def deploy(self, request):
        self.calls.append(request)
        return {"status": "ok"}

fake = FakeProvider()
service = DeploymentService(fake, Logger())
service.deploy("portal")
assert fake.calls == ["portal"]
```

The important part is not the fake class itself. It is that the production design permits replacement of external dependencies.

### Example L — When a class is unnecessary

```python
class StringUtils:
    @staticmethod
    def normalize_hostname(value: str) -> str:
        return value.strip().lower()
```

This class adds no state or meaningful abstraction. A function is clearer:

```python
def normalize_hostname(value: str) -> str:
    return value.strip().lower()
```

Good OOP includes knowing when **not** to use OOP.


## Guided Walkthroughs — OOP Design

### Walkthrough 1 — From requirements to objects

Requirement: "The program reads a deployment plan, validates company policy, asks a selected cloud provider to deploy it, records an audit event, and notifies the operator."

Possible responsibilities:

```text
DeploymentPlan       structured domain data
PlanValidator        policy rules
CloudProvider        provider behavior contract
DeploymentService    orchestration
AuditSink            audit recording contract
Notifier             notification contract
```

Notice that file parsing is not automatically part of `DeploymentPlan`. Parsing is an input-boundary concern and can remain in a loader.

### Walkthrough 2 — Value object versus entity

A `NetworkEndpoint(host, port)` is naturally a value: two endpoints with equal host/port can be considered equal.

An `Asset` with ID `srv-1001` has identity. Even if hostname changes, it remains the same managed asset.

```python
@dataclass(frozen=True)
class NetworkEndpoint:
    host: str
    port: int

@dataclass
class Asset:
    id: str
    hostname: str
```

This distinction improves modeling decisions.

### Walkthrough 3 — Keep I/O at boundaries

```python
class JsonPlanLoader:
    def load(self, path: Path) -> DeploymentPlan:
        data = json.loads(path.read_text(encoding="utf-8"))
        return DeploymentPlan.from_dict(data)
```

The domain object does not need to know file paths. This keeps the core model reusable if plans later come from an API or database.

### Walkthrough 4 — Policy object

```python
class ProductionPolicy:
    def validate(self, plan: DeploymentPlan) -> list[str]:
        errors = []
        if plan.environment == "prod" and plan.replicas < 2:
            errors.append("production requires at least 2 replicas")
        if plan.environment == "prod" and not plan.backup_enabled:
            errors.append("production requires backups")
        return errors
```

Policies often change for business reasons and therefore deserve a separate responsibility from provider SDK calls.

### Walkthrough 5 — Provider adapter

```python
class AwsProvider:
    def __init__(self, sdk_client) -> None:
        self.client = sdk_client

    def deploy(self, plan: DeploymentPlan) -> DeploymentResult:
        # translate domain plan into SDK calls
        ...
```

The adapter translates between your application's domain interface and a vendor-specific API. High-level code should not need vendor-specific parameter names everywhere.

### Walkthrough 6 — Fake audit sink

```python
class FakeAuditSink:
    def __init__(self) -> None:
        self.events = []

    def record(self, event: dict) -> None:
        self.events.append(event)
```

Test:

```python
sink = FakeAuditSink()
service = DeploymentService(provider=fake_provider, validator=policy, audit=sink)
service.deploy(plan)
assert sink.events[-1]["action"] == "deploy"
```

The test observes behavior without a real logging platform.

### Walkthrough 7 — Avoid temporal coupling

Bad API:

```python
job = DeploymentJob()
job.set_provider(...)
job.set_plan(...)
job.validate()
job.execute()
```

If callers must invoke methods in exactly the correct hidden order, the object is easy to misuse.

Prefer construction that provides required dependencies/state:

```python
job = DeploymentJob(provider, validated_plan)
job.execute()
```

Make invalid states harder to represent.

### Walkthrough 8 — Method size and cohesion

If `deploy()` is 200 lines containing YAML parsing, network retries, report formatting, policy validation, and database writes, splitting it into private helper methods alone may not solve the design. The real issue may be multiple responsibilities. Move those responsibilities into focused collaborators.

### Walkthrough 9 — Equality behavior

Dataclasses provide value-based equality by default:

```python
@dataclass(frozen=True)
class Region:
    provider: str
    name: str

assert Region("aws", "eu-west-1") == Region("aws", "eu-west-1")
```

For entities, equality may instead be based on identity/ID. Decide intentionally.

### Walkthrough 10 — Dependency inversion in one picture

```text
          DeploymentService
                 |
          CloudProvider API
          /      |       \
       AWS     Azure     Fake
```

The arrow from high-level service points toward an abstraction that concrete implementations satisfy. Tests can use `Fake`; production uses AWS/Azure adapters.

### Walkthrough 11 — What not to abstract yet

If the program currently has exactly one simple formatter:

```python
def format_status(status: str) -> str:
    return status.upper()
```

Creating `IStatusFormatter`, `BaseStatusFormatter`, `DefaultStatusFormatter`, and a factory is probably unnecessary. Wait until variation or testing needs justify the abstraction.

### Walkthrough 12 — Review the mini-project with questions

For each class answer:

1. What state does it own?
2. What behavior does it own?
3. Why would it change?
4. Which dependencies does it need?
5. Can those dependencies be replaced in tests?
6. What invariants must always hold?
7. What public methods form its contract?
8. Is the class hiding implementation detail or leaking it?


---

# Comprehensive OOP Mastery Expansion

The original material above establishes the correct OOP direction: model responsibilities rather than mechanically creating classes, protect invariants, prefer composition when inheritance is not a real subtype relationship, inject external dependencies, and use SOLID as design heuristics.

This expansion turns that foundation into a complete Python-first OOP course. Python is the primary language. C++ is used when Python's dynamic object model hides an important mechanism such as explicit access control, virtual dispatch, object lifetime, or compile-time overload resolution. C# is used only where explicit interfaces, properties, or access modifiers make a concept clearer.

The recurring mental model is:

```text
Requirement
    ↓
Domain Concept
    ↓
Object Responsibility
    ├─ State
    ├─ Behavior
    ├─ Invariants
    └─ Public Contract
    ↓
Relationships
    ├─ Association
    ├─ Composition
    ├─ Dependency
    └─ Inheritance only when substitutable
    ↓
Dependency Boundaries
    ↓
Test Doubles / Contract Tests
    ↓
Evolvable Software
```

A strong OOP design should make these questions easy to answer:

```text
Who owns this state?
Who is allowed to change it?
What must always remain true?
Which behavior belongs to this object?
Which behavior belongs to a collaborator?
What can vary independently?
Which dependency should be hidden behind an abstraction?
Can a substitute implementation preserve the same contract?
Can I test this object without real infrastructure?
```


# Expanded Core Concepts — Full OOP Coverage

## OOP Expansion Part 1 — Class, Object, Instance, and Type

### Explanation

A class defines the behavior and initialization rules shared by a family of objects. An object is a runtime instance of a type. In Python, classes themselves are also objects, which is why they can be passed around, stored in variables, decorated, and inspected.

Do not confuse the *class definition* with the *state of one instance*. Two instances of the same class normally own independent instance attributes.

### Diagram / Mental Model

```text
class Server
   ├─ instance: web01
   │    └─ hostname = "web-01"
   └─ instance: db01
        └─ hostname = "db-01"
```

### Code Example

```python
class Server:
    def __init__(self, hostname: str) -> None:
        self.hostname = hostname

web = Server("web-01")
db = Server("db-01")

print(type(web) is Server)
print(web is db)
```

### Why It Matters

This is the minimum object model required before discussing encapsulation, inheritance, or polymorphism.

## OOP Expansion Part 2 — Object State

### Explanation

State is the information currently owned by an object. Good object state is cohesive: every field should belong to the same conceptual responsibility.

A class with unrelated state such as cloud credentials, HTML templates, invoice totals, and network socket state is signaling that multiple responsibilities were combined.

### Code Example

```python
class HealthSample:
    def __init__(self, cpu: float, memory: float) -> None:
        self.cpu = cpu
        self.memory = memory
```

### Why It Matters

State ownership is the first design boundary in OOP.

## OOP Expansion Part 3 — Object Behavior

### Explanation

Behavior is what an object can do while preserving its own rules. Methods should usually express meaningful operations rather than expose a sequence of internal field manipulations to callers.

### Code Example

```python
class HealthSample:
    def __init__(self, cpu: float) -> None:
        self.cpu = cpu

    def severity(self) -> str:
        if self.cpu >= 90:
            return "critical"
        if self.cpu >= 75:
            return "warning"
        return "normal"
```

### Why It Matters

Behavior placed with the data it owns can improve cohesion, but only if that behavior really belongs to the domain object.

## OOP Expansion Part 4 — Identity

### Explanation

Identity answers whether two objects represent the same conceptual entity over time. Entities normally have a stable identifier independent of mutable attributes.

A server asset may remain the same asset even after hostname or IP changes. A value object such as an Endpoint is usually identified only by its values.

### Code Example

```python
from dataclasses import dataclass

@dataclass
class Asset:
    id: str
    hostname: str

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Asset) and self.id == other.id
```

### Why It Matters

Identity affects equality, persistence, caching, event handling, and domain modeling.

## OOP Expansion Part 5 — Instance Attributes vs Class Attributes

### Explanation

Instance attributes belong to one object. Class attributes belong to the class and participate in attribute lookup for all instances. Class attributes are useful for constants or shared metadata but dangerous for mutable per-instance state.

### Code Example

```python
class Server:
    category = "compute"       # class attribute

    def __init__(self, hostname: str) -> None:
        self.hostname = hostname  # instance attribute
```

### Why It Matters

Confusing these two is a classic Python OOP bug.

## OOP Expansion Part 6 — Mutable Class Attribute Trap

### Explanation

A list or dictionary stored directly on the class is shared. Mutating it through one instance changes what every instance sees unless the attribute is shadowed.

### Code Example

```python
class BadInventory:
    items = []

one = BadInventory()
two = BadInventory()
one.items.append("web-01")
print(two.items)  # same shared list

class Inventory:
    def __init__(self) -> None:
        self.items = []
```

### Why It Matters

Per-instance mutable state belongs in instance initialization.

### Common Failure / Review Note

Do not repair the problem by copying the class list in random methods; make ownership explicit in __init__.

## OOP Expansion Part 7 — self and Bound Methods

### Explanation

`self` is the instance receiving an instance-method call. When `obj.method` is accessed, Python creates a bound method that remembers `obj`, so calling it supplies the instance automatically.

### Code Example

```python
class Server:
    def summary(self) -> str:
        return "server"

s = Server()
bound = s.summary
print(bound())
```

### Why It Matters

Understanding method binding makes decorators, descriptors, callbacks, and mocking easier later.

## OOP Expansion Part 8 — __init__ Is Initialization, Not Object Creation

### Explanation

`__init__` initializes an instance that already exists. `__new__` is responsible for actually creating/returning the instance. Normal application classes almost never need to override `__new__`, but knowing the distinction prevents conceptual confusion.

### Code Example

```python
class Endpoint:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, host: str) -> None:
        self.host = host
```

### Why It Matters

This distinction matters for immutable subclasses and advanced object construction.

## OOP Expansion Part 9 — Object Invariants

### Explanation

An invariant is a condition that must remain true for every valid object. Constructors and mutating operations should preserve it.

If every Endpoint guarantees a non-empty host and a valid port, later methods do not need to repeat the same checks.

### Code Example

```python
class Endpoint:
    def __init__(self, host: str, port: int) -> None:
        if not host:
            raise ValueError("host required")
        if not 1 <= port <= 65535:
            raise ValueError("port must be 1..65535")
        self.host = host
        self.port = port
```

### Why It Matters

Invariants make invalid states difficult to represent and reduce defensive duplication.

## OOP Expansion Part 10 — Make Invalid States Hard to Represent

### Explanation

Instead of passing raw primitives everywhere and repeatedly validating them, create a small type when the domain rule is important enough to deserve one authoritative representation.

### Code Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ReplicaCount:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1:
            raise ValueError("replicas must be >= 1")
```

### Why It Matters

A validated value object carries both data and domain meaning.

## OOP Expansion Part 11 — Encapsulation as Dependency Control

### Explanation

Encapsulation means callers use a stable public interface instead of depending on internal representation. Privacy syntax is only one mechanism. The deeper purpose is allowing implementation to evolve without forcing unrelated callers to change.

### Diagram / Mental Model

```text
Caller
  ↓ public operation
+---------------------+
| Object boundary     |
| private details     |
+---------------------+
```

### Code Example

```python
class SecretStore:
    def get(self, name: str) -> str:
        return self._backend_lookup(name)

    def _backend_lookup(self, name: str) -> str:
        ...
```

### Why It Matters

The storage mechanism can change while `get(name)` remains stable.

## OOP Expansion Part 12 — Python Public, Protected-Like, and Name-Mangled Conventions

### Explanation

Python does not use access modifiers the same way C++ or C#. `name` is public, `_name` signals non-public implementation detail by convention, and `__name` is name-mangled mainly to reduce accidental subclass collisions.

### Code Example

```python
class Example:
    def __init__(self) -> None:
        self.public = 1
        self._internal = 2
        self.__mangled = 3

obj = Example()
print(obj.__dict__)
```

### Why It Matters

The language emphasizes conventions and interfaces over strict field hiding.

### Common Failure / Review Note

Name mangling is not encryption, authorization, or real data secrecy.

## OOP Expansion Part 13 — C++ Access Modifiers Clarification

### Explanation

C++ makes encapsulation boundaries explicit with `public`, `protected`, and `private`. This helps clarify the difference between the *design principle* of encapsulation and one language's enforcement mechanism.

### Code Example

```cpp
class Endpoint {
private:
    std::string host_;
    int port_;

public:
    Endpoint(std::string host, int port)
        : host_(std::move(host)), port_(port) {}

    int port() const { return port_; }
};
```

### Why It Matters

Python can express the same conceptual boundary with conventions/properties without identical syntax.

## OOP Expansion Part 14 — Properties

### Explanation

A property can enforce rules while preserving attribute-like syntax. Use it when access is cheap and conceptually feels like an attribute.

### Code Example

```python
class Health:
    def __init__(self, cpu: float) -> None:
        self.cpu = cpu

    @property
    def cpu(self) -> float:
        return self._cpu

    @cpu.setter
    def cpu(self, value: float) -> None:
        if not 0 <= value <= 100:
            raise ValueError("CPU must be 0..100")
        self._cpu = value
```

### Why It Matters

The invariant is preserved even when the value changes after construction.

## OOP Expansion Part 15 — Read-Only Properties

### Explanation

A property with no setter exposes a value without permitting assignment through the normal interface. This is useful for derived state.

### Code Example

```python
class Endpoint:
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port

    @property
    def address(self) -> str:
        return f"{self._host}:{self._port}"
```

### Why It Matters

Derived values should usually be computed from authoritative state rather than independently mutated.

## OOP Expansion Part 16 — Do Not Hide Expensive Work Behind Properties

### Explanation

Callers expect attribute access to be cheap and predictable. A property that performs a network request, starts a deployment, writes a file, or sleeps violates that expectation.

### Code Example

```python
# Clear
metrics = client.fetch_remote_metrics()

# Misleading if it performs network I/O:
# metrics = client.metrics
```

### Why It Matters

API shape should communicate cost and side effects.

## OOP Expansion Part 17 — Class Methods as Alternative Constructors

### Explanation

A class method receives `cls` and is useful for named construction paths from another representation.

### Code Example

```python
class Endpoint:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Endpoint":
        return cls(str(data["host"]), int(data.get("port", 443)))
```

### Why It Matters

Construction logic remains centralized and subclass-friendly.

## OOP Expansion Part 18 — Static Methods

### Explanation

A static method receives neither instance nor class automatically. It is appropriate only when the operation is strongly associated with the type's conceptual API but needs no state.

### Code Example

```python
class Port:
    @staticmethod
    def is_valid(value: int) -> bool:
        return 1 <= value <= 65535
```

### Why It Matters

If the operation is generic rather than type-specific, a module function is usually simpler.

## OOP Expansion Part 19 — Instance vs Class vs Static Method Decision

### Explanation

Ask:
- Does the operation need one object's state? → instance method.
- Does it need the class or construct an instance? → class method.
- Does it belong to the type namespace but need no state? → maybe static method.
- Otherwise → module function.

### Diagram / Mental Model

```text
needs self? → instance method
needs cls?  → classmethod
needs neither but strongly type-related? → staticmethod
otherwise → function
```

### Why It Matters

This avoids utility-class habits imported from languages where module-level functions are less common.

## OOP Expansion Part 20 — Identity vs Equality

### Explanation

`is` asks whether two references point to the same object. `==` asks whether values are equal according to the type's equality contract.

### Code Example

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # same values
print(a is b)  # distinct objects
print(a is c)  # same object
```

### Why It Matters

Identity and equality must not be confused in caches, entities, tests, or value objects.

## OOP Expansion Part 21 — Custom Equality with __eq__

### Explanation

Implement `__eq__` when the type has a clear domain notion of equality. Return `NotImplemented` when the other operand is an unsupported type.

### Code Example

```python
class Endpoint:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Endpoint):
            return NotImplemented
        return (self.host, self.port) == (other.host, other.port)
```

### Why It Matters

Equality is part of the object's public semantic contract.

## OOP Expansion Part 22 — Hashing Contract

### Explanation

Objects used in sets or as dictionary keys need a stable hash consistent with equality. If two objects compare equal, their hashes must also be equal. Mutable equality-relevant state makes hash-based lookup unsafe.

### Code Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int

lookup = {Endpoint("db", 5432): "database"}
```

### Why It Matters

Frozen value objects are natural hash keys when all contained fields are hashable.

## OOP Expansion Part 23 — __repr__ and __str__

### Explanation

`__repr__` is developer-oriented and should help debugging. `__str__` is user-oriented. Both are part of object usability and observability.

### Code Example

```python
class Endpoint:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def __repr__(self) -> str:
        return f"Endpoint(host={self.host!r}, port={self.port!r})"

    def __str__(self) -> str:
        return f"{self.host}:{self.port}"
```

### Why It Matters

Never expose secrets, tokens, passwords, or sensitive keys in representations.

## OOP Expansion Part 24 — Dataclasses

### Explanation

A dataclass is useful when an object's main job is to hold structured fields with relatively little custom construction boilerplate. It can still contain methods and invariants.

### Code Example

```python
from dataclasses import dataclass

@dataclass
class Server:
    hostname: str
    environment: str
```

### Why It Matters

Dataclasses generate common methods such as initialization, repr, and equality.

## OOP Expansion Part 25 — __post_init__ Validation

### Explanation

Dataclass `__post_init__` executes after generated initialization and is a natural place to validate invariants.

### Code Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkEndpoint:
    host: str
    port: int

    def __post_init__(self) -> None:
        if not self.host:
            raise ValueError("host required")
        if not 1 <= self.port <= 65535:
            raise ValueError("invalid port")
```

### Why It Matters

A successful constructor means the object is valid.

## OOP Expansion Part 26 — Value Objects

### Explanation

A value object is defined by its values rather than independent identity. It is usually small, immutable, validated, and compared by value.

### Code Example

```python
@dataclass(frozen=True)
class Region:
    provider: str
    name: str
```

### Why It Matters

Examples include Endpoint, Region, Money, DateRange, ResourceLimit, and CIDR.

## OOP Expansion Part 27 — Entities

### Explanation

An entity has stable identity over time even while its attributes change.

### Code Example

```python
@dataclass
class Asset:
    id: str
    hostname: str
    status: str
```

### Why It Matters

Entities are natural persistence targets because identity survives attribute mutation.

## OOP Expansion Part 28 — Entity vs Value Object Decision

### Explanation

Ask whether two instances with the same fields should be interchangeable. If yes, the concept is likely a value. If the history/identity of one specific instance matters, it is likely an entity.

### Diagram / Mental Model

```text
Endpoint("db", 5432) == Endpoint("db", 5432)
→ same value

Asset(id="A-1", hostname="old")
Asset(id="A-1", hostname="new")
→ same entity over time
```

### Why It Matters

This distinction shapes equality, mutation, persistence, and event modeling.

## OOP Expansion Part 29 — Frozen Dataclasses and Shallow Immutability

### Explanation

`frozen=True` prevents normal field reassignment, but nested mutable members can still mutate. Deep immutability requires immutable nested values as well.

### Code Example

```python
@dataclass(frozen=True)
class Config:
    tags: tuple[str, ...]
```

### Why It Matters

Immutable configuration is easier to reason about and share safely.

## OOP Expansion Part 30 — Primitive Obsession

### Explanation

Primitive obsession means important concepts remain loose strings/integers throughout the code. A value object can centralize validation and clarify method signatures.

### Code Example

```python
# Weak
schedule("prod", "eu-west-1", 3)

# Stronger when rules are important
schedule(Environment("prod"), Region("aws", "eu-west-1"), ReplicaCount(3))
```

### Why It Matters

Do not create a class for every primitive; introduce types where the concept has meaningful rules or behavior.

## OOP Expansion Part 31 — Abstraction

### Explanation

Abstraction presents the essential operations a client needs while hiding irrelevant implementation detail. The best interface is designed from the consumer's needs rather than copying every method on a concrete class.

### Diagram / Mental Model

```text
BackupService
   ↓ needs upload(name,data)
Storage abstraction
   ├─ LocalStorage
   ├─ CloudStorage
   └─ FakeStorage
```

### Why It Matters

Abstraction controls coupling and creates substitution points.

## OOP Expansion Part 32 — Duck Typing

### Explanation

Python frequently uses behavior-based compatibility. An object need not inherit from a named base if it provides the operations the caller requires.

### Code Example

```python
class ConsoleLogger:
    def info(self, message: str) -> None:
        print(message)

class MemoryLogger:
    def __init__(self) -> None:
        self.messages = []

    def info(self, message: str) -> None:
        self.messages.append(message)

def run(logger) -> None:
    logger.info("running")
```

### Why It Matters

This is polymorphism through behavior rather than explicit inheritance.

## OOP Expansion Part 33 — typing.Protocol

### Explanation

A Protocol documents a structural interface for type checkers while preserving duck typing. Implementations satisfy it by having compatible members; explicit inheritance is not required.

### Code Example

```python
from typing import Protocol

class Storage(Protocol):
    def upload(self, name: str, data: bytes) -> None: ...
    def download(self, name: str) -> bytes: ...
```

### Why It Matters

Protocols are excellent boundaries for Python services and test doubles.

## OOP Expansion Part 34 — Abstract Base Classes

### Explanation

`ABC` and `@abstractmethod` create an explicit nominal base. Use them when explicit family membership, shared implementation, or runtime abstract-method enforcement adds value.

### Code Example

```python
from abc import ABC, abstractmethod

class Provider(ABC):
    @abstractmethod
    def deploy(self, app: str) -> None:
        ...
```

### Why It Matters

ABCs and Protocols are alternatives with different trade-offs, not a hierarchy of sophistication.

## OOP Expansion Part 35 — Protocol vs ABC

### Explanation

Use Protocol when the client cares only about capabilities and unrelated implementations should conform structurally. Use ABC when explicit inheritance/shared implementation is a meaningful part of the model.

### Diagram / Mental Model

```text
Protocol → "can do these operations"
ABC      → "is explicitly part of this family"
```

### Why It Matters

Choosing the simpler compatible mechanism reduces unnecessary coupling.

## OOP Expansion Part 36 — C# Interface Clarification

### Explanation

C# makes interfaces syntactically explicit. This comparison can make interface segregation and dependency inversion visually clearer.

### Code Example

```csharp
public interface IStorage
{
    void Upload(string name, byte[] data);
    byte[] Download(string name);
}
```

### Why It Matters

Python Protocol provides a similar architectural role without requiring explicit declaration by implementations.

## OOP Expansion Part 37 — Inheritance

### Explanation

Inheritance models a subtype relationship. A subclass can reuse/extend behavior, but the important question is substitutability: can every subclass safely be used wherever the base type is expected?

### Code Example

```python
class Server:
    def restart(self) -> str:
        return "generic restart"

class LinuxServer(Server):
    def restart(self) -> str:
        return "systemctl reboot"
```

### Why It Matters

Use inheritance for an is-a relationship, not merely to reuse helper code.

## OOP Expansion Part 38 — Method Overriding

### Explanation

A subclass overrides a method by supplying a new implementation while preserving the intended contract.

### Code Example

```python
class Provider:
    def deploy(self, app: str) -> str:
        raise NotImplementedError

class LocalProvider(Provider):
    def deploy(self, app: str) -> str:
        return f"local:{app}"
```

### Why It Matters

Same method name is insufficient if semantics differ.

## OOP Expansion Part 39 — super() and Cooperative Inheritance

### Explanation

`super()` calls the next implementation in Python's Method Resolution Order, not simply "my direct parent". This distinction becomes important with mixins and multiple inheritance.

### Code Example

```python
class Asset:
    def __init__(self, asset_id: str) -> None:
        self.asset_id = asset_id

class Server(Asset):
    def __init__(self, asset_id: str, hostname: str) -> None:
        super().__init__(asset_id)
        self.hostname = hostname
```

### Why It Matters

Cooperative `super()` lets compatible multiple-inheritance classes participate in one initialization chain.

## OOP Expansion Part 40 — Liskov Substitution Principle

### Explanation

A subtype should preserve the behavioral assumptions of the base contract. It should not demand stronger preconditions, provide weaker guarantees, or make an operation unexpectedly destructive.

### Diagram / Mental Model

```text
Storage.delete(name)
expected → remove one object

BadStorage.delete(name)
actual → delete entire bucket

same signature, incompatible behavior
```

### Why It Matters

LSP is about behavior, not syntax.

## OOP Expansion Part 41 — Deep Inheritance Smell

### Explanation

When behavior requires reading five ancestors, several overrides, and hidden base state, the hierarchy becomes fragile. Composition often creates clearer independent units.

### Diagram / Mental Model

```text
Base
 ↓
A
 ↓
B
 ↓
C
 ↓
D
```

### Why It Matters

Deep inheritance amplifies coupling to implementation details.

## OOP Expansion Part 42 — Multiple Inheritance

### Explanation

Python supports multiple base classes. It can be appropriate for small orthogonal mixins but makes method resolution and initialization more complicated.

### Code Example

```python
class JsonMixin:
    def to_json(self) -> str:
        return "{}"

class AuditMixin:
    def audit_name(self) -> str:
        return type(self).__name__

class Asset(JsonMixin, AuditMixin):
    pass
```

### Why It Matters

Use multiple inheritance deliberately rather than building large cross-cutting hierarchies.

## OOP Expansion Part 43 — Method Resolution Order

### Explanation

The MRO defines how Python searches classes for methods/attributes. Inspect it with `.mro()` when multiple inheritance is present.

### Code Example

```python
print(Asset.mro())
```

### Why It Matters

It explains which implementation `super()` will call next.

## OOP Expansion Part 44 — Diamond Inheritance

### Explanation

A diamond occurs when two parent paths share a common base. Python's C3 MRO and cooperative `super()` are designed so compatible methods can execute in a consistent order.

### Diagram / Mental Model

```text
Base
/       Left   Right
\    /
 Child
```

### Why It Matters

Directly naming parent classes instead of using cooperative super can call shared bases more than once or skip them.

## OOP Expansion Part 45 — Mixins

### Explanation

A mixin is a small behavior-focused class intended to be combined with another class. It should usually not represent a standalone domain entity.

### Code Example

```python
class TimestampMixin:
    def touch(self) -> None:
        from datetime import datetime, timezone
        self.updated_at = datetime.now(timezone.utc)
```

### Why It Matters

Mixins work best when the behavior is orthogonal and assumptions are minimal.

## OOP Expansion Part 46 — C++ Virtual Dispatch Clarification

### Explanation

Python instance methods use dynamic dispatch naturally. In C++, runtime polymorphism through a base pointer/reference requires `virtual`.

### Code Example

```cpp
class Server {
public:
    virtual ~Server() = default;
    virtual std::string restart() const {
        return "generic restart";
    }
};

class LinuxServer : public Server {
public:
    std::string restart() const override {
        return "systemctl reboot";
    }
};
```

### Why It Matters

The comparison clarifies that dynamic dispatch is an OOP mechanism whose syntax differs by language.

## OOP Expansion Part 47 — C++ Virtual Destructor Clarification

### Explanation

In C++, deleting a derived object through a polymorphic base pointer requires a suitable virtual destructor so the derived cleanup executes correctly.

### Code Example

```cpp
class Provider {
public:
    virtual ~Provider() = default;
    virtual void deploy() = 0;
};
```

### Why It Matters

Python's object lifetime differs; this example clarifies that OOP design also interacts with each language's resource model.

## OOP Expansion Part 48 — Polymorphism

### Explanation

Polymorphism lets different concrete implementations respond to the same operation. High-level code depends on the contract rather than knowing each type's internals.

### Code Example

```python
class AwsProvider:
    def deploy(self, app: str) -> None:
        print("AWS", app)

class AzureProvider:
    def deploy(self, app: str) -> None:
        print("Azure", app)

def run(provider, app: str) -> None:
    provider.deploy(app)
```

### Why It Matters

This removes provider-specific branches from orchestration.

## OOP Expansion Part 49 — Subtype Polymorphism

### Explanation

Subtype polymorphism is the familiar base/protocol/interface model in which many concrete types satisfy the same behavioral contract.

### Diagram / Mental Model

```text
DeploymentService
      ↓
Provider
 /   |   AWS Azure Fake
```

### Why It Matters

The caller can work with any conforming provider.

## OOP Expansion Part 50 — Parametric Polymorphism / Generics

### Explanation

Generic code works across parameterized types. In Python, `Generic` and `TypeVar` mainly improve static type checking and API clarity.

### Code Example

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Repository(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)
```

### Why It Matters

Generics avoid duplicating repository/container behavior while preserving type information.

## OOP Expansion Part 51 — Ad-Hoc Polymorphism / Operator Overloading

### Explanation

A type can define behavior for language operators through special methods. Operator overloading is useful only when the meaning is natural and unsurprising.

### Code Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Memory:
    mib: int

    def __add__(self, other: "Memory") -> "Memory":
        return Memory(self.mib + other.mib)
```

### Why It Matters

Avoid clever overloads that obscure domain meaning.

## OOP Expansion Part 52 — Polymorphism vs Simple Branching

### Explanation

A two-case fixed decision may be clearer as a simple `if`. Introduce polymorphism when variation is meaningful, repeated, independently evolving, externally integrated, or important for test substitution.

### Why It Matters

Patterns should reduce complexity, not increase it.

## OOP Expansion Part 53 — Association

### Explanation

Association means two objects know about or interact with each other. It does not by itself specify ownership.

### Diagram / Mental Model

```text
User ───── uses ───── Service
```

### Why It Matters

Association is the broadest object relationship.

## OOP Expansion Part 54 — Aggregation

### Explanation

Aggregation is a weaker whole-part relationship where parts can exist independently of the whole. Python has no special syntax; it is a modeling decision.

### Diagram / Mental Model

```text
Team  o──── Member
member survives team removal
```

### Why It Matters

Lifetime semantics distinguish aggregation from stronger composition in conceptual UML modeling.

## OOP Expansion Part 55 — Composition

### Explanation

Composition means an object is built from collaborators and delegates work to them. It is the preferred mechanism for combining independent behaviors.

### Code Example

```python
class DeploymentService:
    def __init__(self, provider, validator, audit) -> None:
        self.provider = provider
        self.validator = validator
        self.audit = audit
```

### Why It Matters

Composition supports replacement, testing, and independent evolution.

## OOP Expansion Part 56 — Dependency

### Explanation

A dependency is something an operation or object needs. Not every dependency must be stored permanently as an attribute; a method parameter can represent a short-lived dependency.

### Code Example

```python
def render(report, formatter) -> str:
    return formatter.format(report)
```

### Why It Matters

Dependency is broader than composition.

## OOP Expansion Part 57 — Composition over Inheritance

### Explanation

Use inheritance for *is-a*. Use composition for *has-a* or *uses-a*.

### Diagram / Mental Model

```text
Wrong model:
DeploymentService IS-A Logger

Better:
DeploymentService HAS-A Logger
```

### Why It Matters

Composition keeps behaviors independently replaceable and avoids fragile hierarchies.

## OOP Expansion Part 58 — Ownership and Lifetime of Collaborators

### Explanation

A class should know whether it owns a collaborator's lifetime or merely borrows it. This matters for files, DB sessions, sockets, thread pools, and clients.

### Why It Matters

Object composition should not hide resource ownership ambiguity.

## OOP Expansion Part 59 — Python Special Methods / Data Model

### Explanation

Python lets custom objects participate in built-in syntax through special methods such as `__len__`, `__iter__`, `__contains__`, `__call__`, and context-manager methods.

### Why It Matters

This creates natural object APIs instead of custom method names for standard language behaviors.

## OOP Expansion Part 60 — __len__

### Explanation

`__len__` integrates the object with `len()` and truthiness rules based on length.

### Code Example

```python
class Inventory:
    def __init__(self, items: list[str]) -> None:
        self._items = list(items)

    def __len__(self) -> int:
        return len(self._items)
```

### Why It Matters

Use only when the type naturally has a meaningful count.

## OOP Expansion Part 61 — __iter__

### Explanation

`__iter__` makes an object iterable and lets callers use standard `for` loops.

### Code Example

```python
class Inventory:
    def __iter__(self):
        return iter(self._items)
```

### Why It Matters

Prefer standard iteration protocols to custom `get_next_item()` style APIs.

## OOP Expansion Part 62 — __contains__

### Explanation

`__contains__` supports `item in object` when membership is part of the object's semantics.

### Code Example

```python
class Inventory:
    def __contains__(self, item: str) -> bool:
        return item in self._items
```

### Why It Matters

This can make domain code very readable.

## OOP Expansion Part 63 — Callable Objects with __call__

### Explanation

An object can act like a function while retaining configuration/state. This is useful for strategies, validators, and predicates.

### Code Example

```python
class Threshold:
    def __init__(self, limit: float) -> None:
        self.limit = limit

    def __call__(self, value: float) -> bool:
        return value >= self.limit

critical = Threshold(90)
print(critical(95))
```

### Why It Matters

It combines function-like use with object configuration.

## OOP Expansion Part 64 — Context Manager Objects

### Explanation

`__enter__` and `__exit__` define deterministic setup/cleanup around a `with` block.

### Code Example

```python
class ManagedSession:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("close")
        return False
```

### Why It Matters

Use this for resources with clear acquisition/release lifetime.

## OOP Expansion Part 65 — __del__ Is Not Deterministic Resource Management

### Explanation

`__del__` is a finalizer whose timing and execution context should not be relied upon for critical cleanup. Reference cycles and interpreter shutdown make finalization subtle.

### Why It Matters

Use context managers or explicit close methods for resources.

## OOP Expansion Part 66 — Descriptors

### Explanation

A descriptor implements attribute access methods such as `__get__`, `__set__`, or `__delete__`. Properties and bound methods are built on the descriptor protocol, and frameworks use descriptors for reusable validated fields.

### Code Example

```python
class Positive:
    def __set_name__(self, owner, name):
        self.storage = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(instance, self.storage, value)

class Job:
    retries = Positive()
```

### Why It Matters

Descriptors explain reusable attribute behavior in ORMs, validation libraries, and frameworks.

## OOP Expansion Part 67 — Object Lifetime in Python

### Explanation

Python objects remain alive while reachable according to runtime memory-management rules. CPython commonly combines reference counting and cyclic garbage collection, but application code should not depend on exact finalization timing.

### Why It Matters

Resource lifetime should be explicit even when object memory is garbage collected.

## OOP Expansion Part 68 — Shallow Copy

### Explanation

A shallow copy creates a new outer object but may preserve references to nested objects.

### Code Example

```python
from copy import copy

class Config:
    def __init__(self) -> None:
        self.tags = ["prod"]

a = Config()
b = copy(a)
b.tags.append("critical")
print(a.tags)
```

### Why It Matters

Shared nested state can surprise callers who expected independent copies.

## OOP Expansion Part 69 — Deep Copy

### Explanation

`deepcopy` recursively copies many nested objects, but resources such as sockets, locks, database sessions, and framework objects may not have meaningful copy semantics.

### Why It Matters

Prefer explicit clone/construction logic when domain identity or resource ownership matters.

## OOP Expansion Part 70 — Serialization Boundaries

### Explanation

External representations should be mapped deliberately rather than dumping private object fields. DTOs protect external contracts from internal refactoring.

### Diagram / Mental Model

```text
Domain Object
    ↓ mapper
DTO
    ↓ serializer
JSON / API / message
```

### Why It Matters

Do not make `__dict__` your public API.

## OOP Expansion Part 71 — Untrusted Pickle Warning

### Explanation

Pickle is Python-specific object serialization that can execute code while loading. Never deserialize pickle data from untrusted or unauthenticated sources.

### Why It Matters

Use safe interchange formats plus validation for untrusted boundaries.

## OOP Expansion Part 72 — Cohesion

### Explanation

Cohesion measures how closely the responsibilities inside a component belong together. High cohesion means fields and methods form one understandable concept.

### Diagram / Mental Model

```text
High cohesion:
PolicyValidator
├─ validate_environment
├─ validate_replicas
└─ validate_backup

Low cohesion:
CloudManager
├─ parse_yaml
├─ send_email
├─ calculate_invoice
└─ deploy_vm
```

### Why It Matters

High cohesion makes change more local and testing simpler.

## OOP Expansion Part 73 — Coupling

### Explanation

Coupling measures dependency between components. The goal is not zero coupling but reducing unnecessary dependence on unstable implementation details.

### Diagram / Mental Model

```text
Tight:
Service → AWS SDK calls everywhere

Looser:
Service → Provider Protocol → AWS Adapter
```

### Why It Matters

Stable abstractions reduce change propagation.

## OOP Expansion Part 74 — Tell, Don't Ask

### Explanation

A behavior-rich object often receives a meaningful operation rather than exposing fields for external manipulation. Apply this only when the behavior genuinely belongs to the object.

### Code Example

```python
# External manipulation
if server.cpu > 90:
    server.alerts.append("high cpu")

# Behavior-oriented
server.evaluate_health()
```

### Why It Matters

The object can preserve its own invariants, but a separate monitoring service may still be the correct owner in another domain.

## OOP Expansion Part 75 — Law of Demeter Awareness

### Explanation

Long navigation chains reveal that one component knows too much about another object's internal graph.

### Code Example

```python
# Suspicious
country = order.customer.profile.address.country.code
```

### Why It Matters

Prefer focused operations or query interfaces where deep traversal creates coupling.

## OOP Expansion Part 76 — Feature Envy

### Explanation

A method that repeatedly pulls data from another class and performs most of its logic around that other object's state may be misplaced.

### Why It Matters

Move behavior or create a domain service if responsibility belongs elsewhere.

## OOP Expansion Part 77 — God Class

### Explanation

A God Class centralizes many unrelated responsibilities and dependencies. It becomes difficult to test, understand, deploy, or change safely.

### Diagram / Mental Model

```text
CloudManager
├─ parse config
├─ auth
├─ deploy
├─ billing
├─ audit
├─ reports
└─ notifications
```

### Why It Matters

Split by reasons to change, not arbitrary method counts.

## OOP Expansion Part 78 — Temporal Coupling

### Explanation

Temporal coupling appears when callers must invoke methods in a hidden exact order before an object becomes usable.

### Code Example

```python
# Fragile
job = DeploymentJob()
job.set_provider(provider)
job.set_plan(plan)
job.validate()
job.execute()

# Stronger
job = DeploymentJob(provider, validated_plan)
job.execute()
```

### Why It Matters

Constructors/factories should establish required state where practical.

## OOP Expansion Part 79 — SOLID Overview

### Explanation

SOLID is a set of design-review heuristics rather than rules requiring maximal abstraction. Use them to reason about change, extension, substitutability, interface size, and dependency direction.

### Diagram / Mental Model

```text
S = Single Responsibility
O = Open/Closed
L = Liskov Substitution
I = Interface Segregation
D = Dependency Inversion
```

### Why It Matters

The value is in the questions the principles encourage, not in pattern-counting.

## OOP Expansion Part 80 — Single Responsibility Principle

### Explanation

A component should have one primary reason to change. Input-format rules, business policy, vendor SDK behavior, and notification formatting are different change drivers.

### Diagram / Mental Model

```text
JsonPlanLoader   → changes with JSON/input format
PolicyValidator  → changes with company policy
AwsAdapter       → changes with AWS SDK/API
Notifier         → changes with notification channel
```

### Why It Matters

SRP is about change ownership, not one method per class.

## OOP Expansion Part 81 — Open/Closed Principle

### Explanation

Where variation is expected, design stable extension points so new behavior can be added with minimal changes to existing orchestration.

### Diagram / Mental Model

```text
DeploymentService
       ↓
Provider Protocol
 /       |       AWS    Azure     GCP
```

### Why It Matters

Adding GCP should not require rewriting stable deployment orchestration.

## OOP Expansion Part 82 — LSP as Contract Preservation

### Explanation

A subtype must preserve client assumptions. It cannot strengthen required inputs, weaken promised results, or introduce incompatible side effects.

### Why It Matters

Shared interfaces are meaningful only when implementations behave consistently enough for substitution.

## OOP Expansion Part 83 — Interface Segregation Principle

### Explanation

Clients should depend only on the operations they use. A metrics dashboard should not be forced to depend on deploy/delete/rotate-key methods.

### Code Example

```python
class MetricsReader(Protocol):
    def read_metrics(self) -> dict[str, float]: ...

class Deployer(Protocol):
    def deploy(self, request) -> None: ...
```

### Why It Matters

Small capability-focused interfaces are easier to implement, fake, authorize, and evolve.

## OOP Expansion Part 84 — Dependency Inversion Principle

### Explanation

High-level policy should depend on abstractions based on its needs rather than concrete low-level vendor details. Low-level adapters implement those ports.

### Diagram / Mental Model

```text
DeploymentService
       |
  Provider Port
  /             AwsAdapter      FakeProvider
```

### Why It Matters

Business orchestration remains independent of vendor SDK changes.

## OOP Expansion Part 85 — DIP Does Not Mean Interface for Every Class

### Explanation

If a helper is stable, internal, deterministic, and has no substitution/testing problem, adding an interface can be needless ceremony.

### Why It Matters

Abstractions should solve actual variation or boundary problems.

## OOP Expansion Part 86 — Dependency Injection

### Explanation

Dependency injection means collaborators are supplied from outside instead of hard-coded inside the class.

### Code Example

```python
class ReportService:
    def __init__(self, mailer) -> None:
        self.mailer = mailer

    def send(self, report: str) -> None:
        self.mailer.send(report)
```

### Why It Matters

Tests can inject a fake mailer and production can inject a real adapter.

## OOP Expansion Part 87 — Constructor Injection

### Explanation

Constructor injection is the default choice for required dependencies because the object cannot be created without everything it needs.

### Code Example

```python
service = DeploymentService(
    provider=provider,
    validator=validator,
    repository=repository,
    audit=audit,
)
```

### Why It Matters

Dependencies become explicit in the type/object construction.

## OOP Expansion Part 88 — Method Injection

### Explanation

A collaborator used only for one operation can be passed as a method parameter instead of stored on the object.

### Code Example

```python
def export(self, report, writer) -> None:
    writer.write(report)
```

### Why It Matters

Do not promote every temporary dependency to permanent object state.

## OOP Expansion Part 89 — Setter Injection Caveat

### Explanation

Setting dependencies after construction creates incomplete intermediate states and temporal coupling if those dependencies are mandatory.

### Why It Matters

Prefer constructor injection for required collaborators.

## OOP Expansion Part 90 — Composition Root

### Explanation

A composition root is the application boundary where concrete implementations are selected and wired together.

### Diagram / Mental Model

```text
main.py
├─ AwsProvider()
├─ SqlRepository()
├─ AuditLogger()
└─ DeploymentService(...)
```

### Why It Matters

Business objects stay free of environment-specific construction logic.

## OOP Expansion Part 91 — Service Locator Anti-Pattern

### Explanation

A service locator hides dependencies behind global lookup. The class signature no longer tells readers/tests what the object requires.

### Code Example

```python
# Hidden dependency
mailer = services.get("mailer")
```

### Why It Matters

Constructor injection makes the dependency graph visible.

## OOP Expansion Part 92 — Testing Through Public Behavior

### Explanation

Prefer verifying observable contracts rather than asserting internal private method calls. This allows refactoring without rewriting tests unnecessarily.

### Why It Matters

Tests should protect behavior, not freeze implementation structure.

## OOP Expansion Part 93 — Fakes

### Explanation

A fake is a lightweight working implementation, such as an in-memory repository or storage adapter.

### Code Example

```python
class FakeStorage:
    def __init__(self) -> None:
        self.objects: dict[str, bytes] = {}

    def upload(self, name: str, data: bytes) -> None:
        self.objects[name] = data
```

### Why It Matters

Fakes provide realistic behavior without real infrastructure.

## OOP Expansion Part 94 — Stubs

### Explanation

A stub returns predetermined results to drive a code path.

### Code Example

```python
class StubHealthClient:
    def get_cpu(self, host: str) -> float:
        return 95.0
```

### Why It Matters

Use stubs when the test only needs controlled input from a collaborator.

## OOP Expansion Part 95 — Spies

### Explanation

A spy records interactions so tests can inspect them later.

### Code Example

```python
class SpyNotifier:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def send(self, message: str) -> None:
        self.messages.append(message)
```

### Why It Matters

Use when the interaction itself is required behavior.

## OOP Expansion Part 96 — Mocks

### Explanation

Mocks are configured around expected interactions. They can be useful at some boundaries but become brittle if every internal call sequence is mocked.

### Why It Matters

Prefer outcome/state tests and fakes when they express behavior more directly.

## OOP Expansion Part 97 — Contract Tests

### Explanation

When multiple implementations claim one interface, run the same behavioral test suite against all of them.

### Code Example

```python
def storage_contract(storage) -> None:
    storage.upload("a", b"x")
    assert storage.download("a") == b"x"
```

### Why It Matters

Contract tests provide practical evidence of substitutability.

## OOP Expansion Part 98 — Testability as Architecture Feedback

### Explanation

If a class cannot be instantiated without real credentials, filesystem state, network access, database sessions, and many globals, that difficulty is telling you something about coupling.

### Why It Matters

Hard-to-test code is often hard-to-change code.

## OOP Expansion Part 99 — Domain Service

### Explanation

A domain service contains domain behavior that does not naturally belong to one entity/value object.

### Code Example

```python
class PlacementPolicy:
    def choose_region(self, app, candidates):
        ...
```

### Why It Matters

Do not force every operation onto an entity merely to appear object-oriented.

## OOP Expansion Part 100 — Application Service

### Explanation

An application service orchestrates a use case. It coordinates domain objects and external ports without owning each collaborator's internal responsibilities.

### Diagram / Mental Model

```text
DeploymentService
  ↓ policy.validate
  ↓ provider.deploy
  ↓ repository.save
  ↓ audit.record
```

### Why It Matters

Orchestration is a distinct responsibility from persistence or SDK integration.

## OOP Expansion Part 101 — Repository Pattern

### Explanation

A repository provides domain-oriented persistence operations while hiding storage details such as SQL, ORM sessions, or remote APIs.

### Code Example

```python
class AssetRepository(Protocol):
    def get(self, asset_id: str) -> "Asset": ...
    def save(self, asset: "Asset") -> None: ...
```

### Why It Matters

Domain/application code depends on a collection-like contract rather than persistence technology.

## OOP Expansion Part 102 — DTOs

### Explanation

A Data Transfer Object carries data across process/layer boundaries. It can deliberately differ from the internal domain object.

### Code Example

```python
@dataclass
class AssetResponse:
    id: str
    hostname: str
    status: str
```

### Why It Matters

DTOs protect external contracts from internal refactoring.

## OOP Expansion Part 103 — Aggregates Awareness

### Explanation

In Domain-Driven Design, an aggregate is a consistency boundary around a root entity and related internal objects. External code should modify the group through the aggregate root.

### Why It Matters

This is useful for transactional invariants, but many applications do not need full DDD aggregate modeling.

## OOP Expansion Part 104 — Domain Events

### Explanation

A domain event represents a meaningful fact that has already happened, such as `DeploymentCompleted` or `AssetMarkedCritical`.

### Code Example

```python
@dataclass(frozen=True)
class DeploymentCompleted:
    deployment_id: str
    provider: str
```

### Why It Matters

Events can decouple follow-up reactions such as audit, metrics, and notifications.

## OOP Expansion Part 105 — UML Class Diagrams

### Explanation

A class diagram communicates classes, members, inheritance, associations, and multiplicity. Use it for important structural decisions rather than mirroring every line of code.

### Diagram / Mental Model

```text
+----------------------+
| DeploymentService    |
+----------------------+
| - provider           |
| - validator          |
+----------------------+
| + deploy(request)    |
+----------+-----------+
           |
           v
+----------------------+
| Provider <<Protocol>>|
+----------------------+
```

### Why It Matters

Diagrams improve architecture conversations before implementation detail overwhelms the discussion.

## OOP Expansion Part 106 — Multiplicity

### Explanation

Multiplicity describes relationship cardinality such as one-to-one, zero-or-one, one-to-many, or many-to-many.

### Diagram / Mental Model

```text
Team 1 -------- * Asset
User 1 -------- 0..1 Profile
```

### Why It Matters

Multiplicity captures domain constraints that code must ultimately preserve.

## OOP Expansion Part 107 — Object Diagrams

### Explanation

An object diagram shows concrete runtime instances and their links at a point in time.

### Diagram / Mental Model

```text
service:DeploymentService
   ├─> aws:AwsProvider
   ├─> policy:ProductionPolicy
   └─> repo:InMemoryRepository
```

### Why It Matters

It is useful for visualizing dependency injection and composition roots.

## OOP Expansion Part 108 — Sequence Diagrams

### Explanation

A sequence diagram shows object interaction over time and is especially useful for application services and external adapters.

### Diagram / Mental Model

```text
CLI       Service       Policy      Provider
 | deploy    |             |            |
 |---------->| validate    |            |
 |           |------------>|            |
 |           |<------------| OK         |
 |           | deploy                   |
 |           |------------------------->|
 |           |<-------------------------|
```

### Why It Matters

It exposes orchestration responsibilities and error-return points.

## OOP Expansion Part 109 — Design Patterns Are Vocabulary, Not Requirements

### Explanation

A design pattern names a recurring solution shape. The correct workflow is: identify a real design pressure, choose the simplest solution, and recognize a pattern if it helps communicate/refine the design.

### Why It Matters

Pattern-driven development can produce unnecessary classes and indirection.

## OOP Expansion Part 110 — Factory Method

### Explanation

Factory Method provides a named construction path and centralizes creation rules.

### Code Example

```python
class Endpoint:
    @classmethod
    def from_config(cls, data: dict[str, object]) -> "Endpoint":
        return cls(str(data["host"]), int(data.get("port", 443)))
```

### Why It Matters

Useful when construction from external representation requires parsing/validation.

## OOP Expansion Part 111 — Simple Factory

### Explanation

A simple factory selects a concrete implementation at the composition boundary.

### Code Example

```python
def build_provider(name: str):
    if name == "aws":
        return AwsProvider()
    if name == "azure":
        return AzureProvider()
    raise ValueError(name)
```

### Why It Matters

The branch is centralized in creation logic instead of scattered throughout use cases.

## OOP Expansion Part 112 — Abstract Factory Awareness

### Explanation

Abstract Factory creates related families of objects that must vary together, such as a cloud provider's storage, queue, and compute adapters.

### Diagram / Mental Model

```text
CloudFactory
├─ create_storage()
├─ create_queue()
└─ create_compute()

AwsFactory / AzureFactory
```

### Why It Matters

Use only when families really vary together.

## OOP Expansion Part 113 — Builder Pattern Awareness

### Explanation

Builder separates stepwise construction from the final object. In Python, keyword arguments/dataclasses already solve many cases, so Builder should be reserved for genuinely complex construction.

### Code Example

```python
class RequestBuilder:
    def __init__(self) -> None:
        self._tags = []

    def add_tag(self, tag: str) -> "RequestBuilder":
        self._tags.append(tag)
        return self
```

### Why It Matters

Do not import Java-style builder ceremony when Python construction is already clear.

## OOP Expansion Part 114 — Singleton Pattern Critique

### Explanation

Singleton enforces one global instance. It often creates hidden global state, test-order coupling, lifecycle problems, and implicit dependencies.

### Why It Matters

Prefer explicit composition unless process-wide uniqueness is truly part of the requirement.

## OOP Expansion Part 115 — Adapter Pattern

### Explanation

An adapter translates your application's interface into a vendor/library-specific interface.

### Code Example

```python
class AwsAdapter:
    def __init__(self, sdk_client) -> None:
        self.client = sdk_client

    def deploy(self, request):
        sdk_args = {
            "Name": request.application,
            "Count": request.replicas.value,
        }
        return self.client.create_simulated_resource(**sdk_args)
```

### Why It Matters

Vendor-specific terms stay at the edge.

## OOP Expansion Part 116 — Facade Pattern

### Explanation

Facade presents a simpler operation over several subsystem calls.

### Code Example

```python
class BackupFacade:
    def backup_application(self, app_id: str) -> None:
        self._snapshot_database(app_id)
        self._archive_files(app_id)
        self._write_manifest(app_id)
```

### Why It Matters

Callers do not need to understand subsystem orchestration details.

## OOP Expansion Part 117 — Decorator Pattern

### Explanation

The object Decorator pattern wraps another implementation of the same interface to add behavior through composition.

### Code Example

```python
class LoggingStorage:
    def __init__(self, inner) -> None:
        self.inner = inner

    def upload(self, name: str, data: bytes) -> None:
        print("upload", name)
        self.inner.upload(name, data)
```

### Why It Matters

This avoids subclass combinations such as LoggedEncryptedCachedCloudStorage.

## OOP Expansion Part 118 — Proxy Pattern

### Explanation

A proxy stands in for another object to control access, caching, lazy loading, authorization, or remote communication.

### Diagram / Mental Model

```text
Client → Proxy → Real Service
```

### Why It Matters

ORM lazy-loaded objects and remote-service stubs commonly use proxy-like behavior.

## OOP Expansion Part 119 — Composite Pattern

### Explanation

Composite models tree structures where both leaves and groups satisfy the same interface.

### Code Example

```python
class Node(Protocol):
    def size(self) -> int: ...

class FileNode:
    def __init__(self, size: int) -> None:
        self._size = size
    def size(self) -> int:
        return self._size

class Directory:
    def __init__(self, children: list[Node]) -> None:
        self.children = children
    def size(self) -> int:
        return sum(child.size() for child in self.children)
```

### Why It Matters

Clients can treat individual and grouped nodes uniformly.

## OOP Expansion Part 120 — Strategy Pattern

### Explanation

Strategy encapsulates a replaceable algorithm or policy behind a common interface.

### Code Example

```python
class RetryPolicy(Protocol):
    def should_retry(self, attempt: int, error: Exception) -> bool: ...

class NoRetry:
    def should_retry(self, attempt: int, error: Exception) -> bool:
        return False

class FixedAttempts:
    def __init__(self, max_attempts: int) -> None:
        self.max_attempts = max_attempts
    def should_retry(self, attempt: int, error: Exception) -> bool:
        return attempt < self.max_attempts
```

### Why It Matters

Workflow and variable policy evolve independently.

## OOP Expansion Part 121 — Observer Pattern

### Explanation

Observer lets multiple subscribers react to events without the publisher depending on each concrete reaction.

### Code Example

```python
class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list] = {}

    def subscribe(self, event: str, handler) -> None:
        self._handlers.setdefault(event, []).append(handler)

    def publish(self, event: str, payload) -> None:
        for handler in self._handlers.get(event, []):
            handler(payload)
```

### Why It Matters

Useful for audit/metrics/notifications, but event flows can become hard to trace if overused.

## OOP Expansion Part 122 — Command Pattern

### Explanation

Command represents an action/request as an object, enabling queues, logging, deferred execution, retries, or undo-oriented designs.

### Code Example

```python
@dataclass
class RestartServer:
    server_id: str

    def execute(self, service) -> None:
        service.restart(self.server_id)
```

### Why It Matters

Behavior can be scheduled or stored as data-like objects.

## OOP Expansion Part 123 — State Pattern

### Explanation

State places state-specific behavior in separate state objects. For a small state machine, an enum plus direct branch is usually simpler.

### Diagram / Mental Model

```text
Context
  ↓ current state
IdleState / RunningState / FailedState
```

### Why It Matters

Use when each state's behavior is large and evolves independently.

## OOP Expansion Part 124 — Template Method

### Explanation

Template Method uses inheritance to define an algorithm skeleton with overridable steps.

### Code Example

```python
from abc import ABC, abstractmethod

class ImportJob(ABC):
    def run(self) -> None:
        data = self.load()
        data = self.validate(data)
        self.save(data)

    @abstractmethod
    def load(self): ...

    def validate(self, data):
        return data

    @abstractmethod
    def save(self, data): ...
```

### Why It Matters

Strategy through composition is often more flexible, but Template Method is useful for stable inheritance-based workflows.

## OOP Expansion Part 125 — Chain of Responsibility

### Explanation

A request passes through ordered handlers that may validate, transform, reject, or continue it.

### Diagram / Mental Model

```text
Request
 ↓
Authentication
 ↓
Authorization
 ↓
Rate Limit
 ↓
Validation
 ↓
Handler
```

### Why It Matters

HTTP middleware pipelines commonly use this pattern.

## OOP Expansion Part 126 — Mutable State and Concurrency

### Explanation

An object's methods can each be correct in single-threaded use while becoming unsafe when two execution contexts mutate the same state concurrently.

### Why It Matters

Thread/task safety is part of the object's contract.

## OOP Expansion Part 127 — Immutability as a Concurrency Tool

### Explanation

Immutable value objects can often be safely shared because readers cannot race with mutation of those values.

### Why It Matters

This reduces synchronization requirements and temporal reasoning.

## OOP Expansion Part 128 — Lock-Protected State

### Explanation

When mutable state must be shared across threads, protect compound operations with an appropriate synchronization primitive.

### Code Example

```python
from threading import Lock

class Counter:
    def __init__(self) -> None:
        self._value = 0
        self._lock = Lock()

    def increment(self) -> None:
        with self._lock:
            self._value += 1
```

### Why It Matters

Do not add locks mechanically; define the concurrency model first.

## OOP Expansion Part 129 — Thread-Safety Contract

### Explanation

Document whether a class is thread-safe, immutable, single-thread confined, async-task confined, or requires external synchronization.

### Why It Matters

Callers cannot safely compose concurrent systems without this knowledge.

## OOP Expansion Part 130 — Exception Hierarchies as OOP

### Explanation

Exceptions are classes and polymorphic objects. A domain hierarchy lets higher layers catch a broad family while still distinguishing specific failure categories.

### Code Example

```python
class DeploymentError(Exception):
    pass

class InvalidPlanError(DeploymentError):
    pass

class ProviderUnavailableError(DeploymentError):
    pass
```

### Why It Matters

Exception inheritance is a real, practical example of subtype polymorphism.

## OOP Expansion Part 131 — Catch at the Correct Abstraction Level

### Explanation

Catch exceptions where enough context exists to recover, translate, retry, or present a meaningful error. Do not convert unrelated programming defects into one generic domain exception.

### Why It Matters

Error abstraction should preserve causality and useful distinctions.

## OOP Expansion Part 132 — Data Class / Anemic Model Smell

### Explanation

A domain class containing only mutable fields while all business rules live elsewhere may be an anemic model. But DTOs are intentionally data-centric, so the smell depends on role.

### Why It Matters

Ask where the behavior and invariants logically belong instead of applying one universal rule.

## OOP Expansion Part 133 — Message Chains

### Explanation

Long chains reveal internal structure across boundaries and increase coupling.

### Code Example

```python
# suspicious
transport = deployment.provider.client.session.transport
```

### Why It Matters

Expose focused operations rather than object-graph navigation when appropriate.

## OOP Expansion Part 134 — Inappropriate Intimacy

### Explanation

Two classes that constantly manipulate each other's non-public state have poorly separated responsibilities.

### Why It Matters

Clarify ownership and define public collaboration methods.

## OOP Expansion Part 135 — Middle Man

### Explanation

An object that only forwards every call without translating, coordinating, enforcing policy, caching, securing, or simplifying anything may be unnecessary.

### Why It Matters

Every abstraction should justify its maintenance cost.

## OOP Expansion Part 136 — Speculative Generality

### Explanation

Base classes, factories, plugin systems, hooks, and abstract interfaces built for hypothetical future needs can make today's system harder to understand.

### Why It Matters

Refactor toward abstraction when real variation appears or requirements make it clearly imminent.

## OOP Expansion Part 137 — Inheritance for Reuse Smell

### Explanation

If a child exists only to reuse helpers and cannot honestly satisfy an is-a relationship, move the helper behavior into a collaborator or function.

### Why It Matters

Inheritance establishes a strong semantic contract, not merely code sharing.

## OOP Expansion Part 138 — Boolean Parameter Smell

### Explanation

Many boolean flags can hide multiple modes and make calls unreadable.

### Code Example

```python
# hard to understand
service.deploy(plan, True, False, True)

# clearer
service.deploy(plan, DeploymentOptions(dry_run=True, notify=True))
```

### Why It Matters

Use option/value objects or separate operations when modes become complex.

## OOP Expansion Part 139 — Long Parameter List

### Explanation

A long list of primitives can signal that several values form one cohesive request/configuration concept.

### Code Example

```python
# before
deploy(app, env, region, replicas, cpu, memory, backup)

# after
deploy(DeploymentRequest(...))
```

### Why It Matters

Grouping should follow domain cohesion, not arbitrary parameter count.

## OOP Expansion Part 140 — Object Overhead Awareness

### Explanation

Objects add metadata and indirection compared with primitives/tuples. In ordinary application code, maintainability usually matters more than micro-optimizing object memory.

### Why It Matters

Measure before changing the model for performance.

## OOP Expansion Part 141 — __slots__ Awareness

### Explanation

`__slots__` can restrict instance attributes and reduce per-instance memory in some high-object-count situations.

### Code Example

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
```

### Why It Matters

Use only after profiling or when strict attribute layout is valuable.

## OOP Expansion Part 142 — Ports and Adapters Architecture

### Explanation

The application core defines the interfaces it needs (ports). Infrastructure components implement adapters around databases, cloud SDKs, message brokers, files, or external APIs.

### Diagram / Mental Model

```text
Application Core
    DeploymentService
    /      |              Provider  Repo     Audit
   ^       ^        ^
   |       |        |
  AWS     SQL     Logger
Adapter  Adapter   Adapter
```

### Why It Matters

This is Dependency Inversion applied at architectural scale.

## OOP Expansion Part 143 — Keep I/O at Boundaries

### Explanation

Domain/application objects should not automatically know JSON files, HTTP framework request objects, ORM sessions, or vendor SDK parameter names. Boundary adapters translate those representations.

### Code Example

```python
class JsonPlanLoader:
    def load(self, path: Path) -> DeploymentRequest:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return DeploymentRequest.from_dict(raw)
```

### Why It Matters

Core logic becomes reusable from CLI, API, tests, or message consumers.

## OOP Expansion Part 144 — Orchestration vs Domain Logic

### Explanation

An application service coordinates the use case, while domain objects/policies own domain rules and adapters own external integration details.

### Diagram / Mental Model

```text
DeploymentService
  ↓ PolicyValidator.validate
  ↓ Provider.deploy
  ↓ Repository.save
  ↓ Audit.record
```

### Why It Matters

Clear layers avoid giant service classes.

## OOP Expansion Part 145 — Final OOP Design Mental Model

### Explanation

The goal of OOP is not maximum class count. The goal is understandable responsibility, protected state, explicit dependencies, safe substitution, and changeable architecture.

### Diagram / Mental Model

```text
Requirements
   ↓
Domain concepts
   ↓
Entities / Value Objects
   ↓
Services / Policies
   ↓
Ports
   ↓
Adapters
   ↓
Composition Root
   ↓
Tests / Contract Tests
```

### Why It Matters

This mental model connects basic classes to production architecture.



# Expanded Hands-on Labs — Comprehensive OOP Practice

## Extended Lab 1 — Procedural vs OOP comparison

Implement one server-health feature both as functions+dict and as a class. Compare cohesion, amount of state, tests, and whether the class actually improves the design.

## Extended Lab 2 — Constructor invariants

Build Endpoint(host, port) and reject empty host, port 0, 65536, and non-integer conversion at the boundary.

## Extended Lab 3 — Mutable class attribute bug

Demonstrate one shared class list across two instances, then repair it with per-instance initialization.

## Extended Lab 4 — Class method factory

Implement Endpoint.from_dict() and Endpoint.from_string(). Keep invariant enforcement in one place.

## Extended Lab 5 — Property-controlled mutation

Implement CPU percentage property with 0..100 validation. Verify invalid assignment cannot create invalid object state.

## Extended Lab 6 — C++ access-control comparison

Translate one Python class to C++ public/private members and explain the enforcement difference.

## Extended Lab 7 — Identity vs equality

Model Endpoint as a value and Asset as an entity. Write tests showing the difference.

## Extended Lab 8 — Hashable value object

Use frozen Endpoint objects as dictionary keys and set members.

## Extended Lab 9 — Safe repr

Implement __repr__ for a CredentialMetadata class without ever showing the actual secret.

## Extended Lab 10 — Frozen dataclass depth

Show why frozen dataclass containing a list is not deeply immutable; replace list with tuple.

## Extended Lab 11 — Duck typing

Create two unrelated loggers exposing info(); use both with one service.

## Extended Lab 12 — Protocol-based storage

Implement Storage Protocol with LocalStorage and MemoryStorage.

## Extended Lab 13 — ABC comparison

Implement the same provider contract with ABC and compare with Protocol.

## Extended Lab 14 — Interface segregation

Split one broad CloudPlatform interface into MetricsReader, Deployer, and ObjectStorage.

## Extended Lab 15 — C# interface comparison

Write a tiny C# IStorage and implementation, then explain structural vs nominal typing.

## Extended Lab 16 — Inheritance and override

Create Asset→Server/NetworkDevice and polymorphic summary().

## Extended Lab 17 — LSP failure

Create a subclass violating delete() semantics, write a contract test that catches it, and redesign.

## Extended Lab 18 — super and MRO

Build a base + mixins hierarchy and inspect .mro().

## Extended Lab 19 — Diamond inheritance

Build Base/Left/Right/Child cooperative super chain and record call order.

## Extended Lab 20 — C++ virtual dispatch

Build C++ base Provider with pure virtual deploy() and two derived providers.

## Extended Lab 21 — Composition refactor

Replace a DeploymentService(Logger, AwsClient) inheritance design with constructor-composed collaborators.

## Extended Lab 22 — Association/aggregation/composition diagram

Draw three relationships and describe object lifetime/ownership for each.

## Extended Lab 23 — Custom iterable

Implement Inventory with __len__, __iter__, __contains__, and __repr__.

## Extended Lab 24 — Callable strategy object

Implement Threshold(limit).__call__ and inject it into a health evaluator.

## Extended Lab 25 — Context manager

Create a managed fake transaction; verify cleanup on success and exception.

## Extended Lab 26 — Descriptor

Create Positive descriptor for replicas/retries; compare with property-based validation.

## Extended Lab 27 — Object copy graph

Compare assignment, copy.copy, and copy.deepcopy on a nested object; draw references.

## Extended Lab 28 — Cohesion decomposition

Split a God CloudManager by independent reasons to change.

## Extended Lab 29 — Law of Demeter refactor

Replace a deep object chain with a focused public operation.

## Extended Lab 30 — Temporal coupling

Redesign a four-step set/validate/execute API so required state exists at construction.

## Extended Lab 31 — SRP review

For PlanLoader, PolicyValidator, AwsAdapter, DeploymentService, identify exactly what kind of requirement changes each one.

## Extended Lab 32 — OCP exercise

Add GCP behind Provider without modifying deployment orchestration.

## Extended Lab 33 — LSP contract suite

Write one provider contract and execute it against AWS/Azure/Local fake adapters.

## Extended Lab 34 — ISP exercise

Ensure read-only monitoring code depends only on MetricsReader.

## Extended Lab 35 — DIP diagram

Draw high-level service → owned protocol ← low-level adapter dependency direction.

## Extended Lab 36 — Constructor injection

Refactor hard-coded RealEmailClient() into an injected mailer and test with fake.

## Extended Lab 37 — Composition root

Create main.py wiring concrete provider/repository/audit/notifier.

## Extended Lab 38 — Service locator refactor

Identify hidden dependencies in services.get() usage and replace them with explicit constructor parameters.

## Extended Lab 39 — Fake/stub/spy

Implement all three in one report workflow and explain the testing question each answers.

## Extended Lab 40 — Contract test

Run one Storage behavior suite against memory and temporary-directory local implementations.

## Extended Lab 41 — Entity/value object model

Create Asset entity and NetworkEndpoint value object; define equality rules.

## Extended Lab 42 — Repository pattern

Create AssetRepository Protocol plus InMemoryRepository; keep AssetService persistence-agnostic.

## Extended Lab 43 — DTO mapping

Map Asset → AssetResponse → JSON; do not expose __dict__.

## Extended Lab 44 — Domain event

Publish DeploymentCompleted and attach audit/notification handlers.

## Extended Lab 45 — UML class diagram

Draw capstone classes, interfaces, composition, inheritance, and multiplicity.

## Extended Lab 46 — Sequence diagram

Draw CLI→Service→Policy→Provider→Repository→Audit successful flow.

## Extended Lab 47 — Simple factory

Centralize provider selection at composition boundary.

## Extended Lab 48 — Adapter

Wrap a fake vendor SDK and translate DeploymentRequest into vendor parameters.

## Extended Lab 49 — Facade

Create BackupFacade over DB snapshot/file archive/manifest subsystems.

## Extended Lab 50 — Decorator

Wrap Storage with LoggingStorage and ChecksumStorage while preserving Storage contract.

## Extended Lab 51 — Strategy

Inject NoRetry and FixedAttempts policies into one simulated operation.

## Extended Lab 52 — Observer

Publish a deployment event to audit + metrics + notification subscribers.

## Extended Lab 53 — Command

Create queued RestartServer commands and execute them later.

## Extended Lab 54 — State comparison

Implement a tiny workflow both with enum+branch and State objects; choose the simpler one.

## Extended Lab 55 — Template Method vs Strategy

Implement one import workflow both ways and compare coupling.

## Extended Lab 56 — Chain of Responsibility

Create auth→policy→validation handler pipeline for simulated requests.

## Extended Lab 57 — Concurrency contract

Protect a shared Counter with Lock and document thread-safety assumptions.

## Extended Lab 58 — Exception hierarchy

Create DeploymentError base with validation/provider subtypes and catch at two abstraction levels.

## Extended Lab 59 — Anti-pattern audit

Find God Class, utility class, deep hierarchy, service locator, boolean flags, long parameter list, speculative interface in a sample design.

## Extended Lab 60 — Capstone

Build the full Multi-Provider Deployment Planner described below and add a fourth provider without changing orchestration.




# Expanded Mini Project — Multi-Provider Deployment Planner

Build a **simulation only**. Do not create real cloud resources.

The project must demonstrate the full OOP model:

```text
JSON / CLI
   ↓
PlanLoader
   ↓
DeploymentRequest (immutable value object)
   ↓
PolicyValidator
   ↓
DeploymentService
   ├─ Provider Port
   │    ├─ AwsProvider
   │    ├─ AzureProvider
   │    ├─ GcpProvider
   │    └─ LocalProvider
   ├─ DeploymentRepository
   ├─ AuditSink
   ├─ EventPublisher
   └─ RetryPolicy
```

## Suggested Structure

```text
deployment_planner/
├── pyproject.toml
├── README.md
├── src/
│   └── planner/
│       ├── domain/
│       │   ├── values.py
│       │   ├── request.py
│       │   ├── result.py
│       │   └── events.py
│       ├── application/
│       │   ├── service.py
│       │   └── policy.py
│       ├── ports/
│       │   ├── provider.py
│       │   ├── repository.py
│       │   ├── audit.py
│       │   └── events.py
│       ├── adapters/
│       │   ├── aws.py
│       │   ├── azure.py
│       │   ├── gcp.py
│       │   ├── local.py
│       │   └── memory_repository.py
│       ├── factories.py
│       ├── errors.py
│       └── cli.py
└── tests/
    ├── fakes.py
    ├── test_values.py
    ├── test_policy.py
    ├── test_service.py
    └── test_provider_contract.py
```

## Required Value Objects

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Environment:
    value: str

    def __post_init__(self) -> None:
        if self.value not in {"dev", "test", "prod"}:
            raise ValueError("invalid environment")

@dataclass(frozen=True)
class ReplicaCount:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1:
            raise ValueError("replicas must be >= 1")

@dataclass(frozen=True)
class Region:
    provider: str
    name: str
```

## Deployment Request

```python
@dataclass(frozen=True)
class DeploymentRequest:
    application: str
    environment: Environment
    region: Region
    replicas: ReplicaCount
    backup_enabled: bool
```

## Provider Port

```python
from typing import Protocol

class Provider(Protocol):
    def validate(self, request: DeploymentRequest) -> list[str]: ...
    def deploy(self, request: DeploymentRequest) -> "DeploymentResult": ...
```

High-level orchestration must not contain:

```python
if provider_name == "aws":
    ...
elif provider_name == "azure":
    ...
```

Provider selection belongs in a factory/composition root.

## Policy Validator

```python
class PolicyValidator:
    def validate(self, request: DeploymentRequest) -> list[str]:
        errors = []

        if request.environment.value == "prod":
            if request.replicas.value < 2:
                errors.append("production requires >= 2 replicas")
            if not request.backup_enabled:
                errors.append("production requires backup")

        return errors
```

## Repository Port

```python
class DeploymentRepository(Protocol):
    def save(self, result: "DeploymentResult") -> None: ...
    def get(self, deployment_id: str) -> "DeploymentResult": ...
```

## Retry Strategy

```python
class RetryPolicy(Protocol):
    def should_retry(self, attempt: int, error: Exception) -> bool: ...
```

Implement:

```text
NoRetry
FixedAttempts
```

No real network operation is required.

## Deployment Service

The service should orchestrate only:

```text
validate business policy
validate provider compatibility
call provider
save result
record audit
publish event
```

It should not:

```text
parse JSON
know CLI syntax
know SQL
know cloud SDK parameter names
format HTML
instantiate real dependencies internally
```

## Contract Tests

Run the same provider contract against:

```text
AWS
Azure
GCP
Local
```

A valid provider must:

```text
return list[str] from validate
return DeploymentResult from deploy
not mutate the immutable request
identify its own provider correctly
preserve common result semantics
```

## Open/Closed Exercise

Build AWS/Azure/Local first. Then add GCP.

Allowed existing changes:

```text
provider registration/factory configuration
new provider tests
```

Not allowed:

```text
editing DeploymentService provider branches
```

## UML Class Diagram

```text
+----------------------+
| DeploymentService    |
+----------------------+
| provider             |
| policy               |
| repository           |
| audit                |
| retry_policy         |
+----------+-----------+
           |
           v
+----------------------+
| Provider <<Protocol>>|
+----------------------+
| validate(request)    |
| deploy(request)      |
+----+----+----+-------+
     ^    ^    ^
     |    |    |
    AWS Azure GCP ...
```

## Sequence Diagram

```text
CLI        Service       Policy       Provider       Repository       Audit
 | deploy     |             |             |               |             |
 |----------->| validate    |             |               |             |
 |            |------------>|             |               |             |
 |            |<------------| OK          |               |             |
 |            | validate                  |               |             |
 |            |-------------------------->|               |             |
 |            |<--------------------------| OK            |             |
 |            | deploy                    |               |             |
 |            |-------------------------->|               |             |
 |            |<--------------------------| result        |             |
 |            | save                                      |             |
 |            |------------------------------------------>|             |
 |            | audit                                                   |
 |            |-------------------------------------------------------->|
 |<-----------| result                                                  |
```

## Testing Requirements

At minimum:

```text
Value objects:
- invalid environment
- replicas 0/1/2
- immutability
- value equality

Policy:
- dev one replica valid
- prod one replica invalid
- prod no backup invalid
- prod >=2 + backup valid

Service:
- provider called once
- invalid policy prevents deploy
- provider validation failure prevents save
- repository receives result
- audit event recorded
- fake provider can be used with no credentials

Contract:
- same suite for all providers
```

## Pattern Review

Document where the project uses:

```text
Value Object
Repository
Adapter
Factory
Strategy
Observer/Event Publisher
Dependency Injection
Composition Root
```

Then list at least three patterns you **did not** use because the problem did not justify them.

## SOLID Review

Write a concrete project-specific explanation for every principle. Do not write definitions only.

## Anti-Pattern Review

Confirm the project does not contain:

```text
God CloudManager
provider-specific branching inside service
hidden service locator
deep inheritance
mutable global configuration
one huge CloudPlatform interface
utility classes containing only static helpers
```

## Optional C++ Comparison

Implement only the provider abstraction and one adapter:

```cpp
class Provider {
public:
    virtual ~Provider() = default;
    virtual DeploymentResult deploy(const DeploymentRequest&) = 0;
};
```

Explain how this maps to Python Protocol/duck typing.

## Optional C# Comparison

Implement:

```csharp
public interface IProvider
{
    DeploymentResult Deploy(DeploymentRequest request);
}
```

Explain how explicit interface implementation differs from Python structural typing.



# Extended Self-Assessment — OOP Mastery

### Extended Q1. Class vs object?

**Answer:** A class defines a type/behavior; an object is a runtime instance.

### Extended Q2. What is state?

**Answer:** Data currently owned by an object.

### Extended Q3. What is behavior?

**Answer:** Operations an object performs.

### Extended Q4. What is identity?

**Answer:** What makes an entity the same conceptual object over time.

### Extended Q5. What is an invariant?

**Answer:** A condition that must always hold for a valid object.

### Extended Q6. Why can a class attribute list be dangerous?

**Answer:** It is shared across instances.

### Extended Q7. What does self mean?

**Answer:** The instance receiving an instance method.

### Extended Q8. Does __init__ create the object?

**Answer:** No; it initializes an object returned by __new__.

### Extended Q9. What is encapsulation?

**Answer:** Protecting implementation/invariants behind a stable public interface.

### Extended Q10. Does _name make data private?

**Answer:** No; it is a convention.

### Extended Q11. What is name mangling for?

**Answer:** Reducing accidental subclass attribute collisions.

### Extended Q12. When use a property?

**Answer:** For cheap attribute-like access needing validation/derived computation.

### Extended Q13. Why not network I/O in a property?

**Answer:** It hides expensive side effects behind attribute syntax.

### Extended Q14. What is a classmethod?

**Answer:** A method receiving cls, often an alternative constructor.

### Extended Q15. What is a staticmethod?

**Answer:** A type-namespaced function receiving neither self nor cls.

### Extended Q16. Identity vs equality?

**Answer:** Identity is same object; equality is same value/domain equivalence.

### Extended Q17. What is a value object?

**Answer:** Object defined by its values, usually immutable.

### Extended Q18. What is an entity?

**Answer:** Object defined by stable identity.

### Extended Q19. What is primitive obsession?

**Answer:** Using raw primitives for domain concepts with important rules.

### Extended Q20. What is abstraction?

**Answer:** Exposing needed capabilities while hiding irrelevant details.

### Extended Q21. What is duck typing?

**Answer:** Compatibility based on supported behavior.

### Extended Q22. What is Protocol?

**Answer:** A structural typing contract in Python.

### Extended Q23. What is ABC?

**Answer:** An explicit abstract inheritance base.

### Extended Q24. When prefer Protocol?

**Answer:** When behavior matters more than explicit family inheritance.

### Extended Q25. What is interface segregation?

**Answer:** Clients depend only on operations they use.

### Extended Q26. What is inheritance?

**Answer:** Subtype/specialization relationship.

### Extended Q27. What is overriding?

**Answer:** Subclass supplies a replacement implementation while preserving contract.

### Extended Q28. What does super follow?

**Answer:** Python MRO.

### Extended Q29. What is LSP?

**Answer:** Subtypes preserve base behavioral expectations.

### Extended Q30. What is MRO?

**Answer:** Method Resolution Order.

### Extended Q31. What is a mixin?

**Answer:** Small reusable behavior class intended for combination.

### Extended Q32. Why use C++ virtual examples?

**Answer:** To make dynamic dispatch explicit where Python hides the mechanism.

### Extended Q33. What is polymorphism?

**Answer:** Different implementations used through one behavioral contract.

### Extended Q34. What is generic polymorphism?

**Answer:** Code parameterized by types.

### Extended Q35. What is operator overloading?

**Answer:** Custom behavior for language operators.

### Extended Q36. Should every branch become polymorphism?

**Answer:** No.

### Extended Q37. What is association?

**Answer:** General relationship between objects.

### Extended Q38. What is aggregation?

**Answer:** Weak whole-part relationship with independent lifetimes.

### Extended Q39. What is composition?

**Answer:** Building an object from collaborators/parts.

### Extended Q40. Why composition over inheritance often?

**Answer:** Lower coupling and correct has-a/uses-a modeling.

### Extended Q41. What is __iter__ for?

**Answer:** Making an object iterable.

### Extended Q42. What is __call__ for?

**Answer:** Making an object callable like a function.

### Extended Q43. What is a context manager object?

**Answer:** Object controlling setup/cleanup through with.

### Extended Q44. Why avoid __del__ for cleanup?

**Answer:** Finalization timing is not deterministic enough for resources.

### Extended Q45. What is a descriptor?

**Answer:** Object controlling attribute access through descriptor protocol.

### Extended Q46. What is shallow copy?

**Answer:** New outer object with nested references potentially shared.

### Extended Q47. Why map to DTO?

**Answer:** Protect external contracts from internal object representation.

### Extended Q48. What is cohesion?

**Answer:** How closely related responsibilities inside a component are.

### Extended Q49. What is coupling?

**Answer:** Degree of dependency between components.

### Extended Q50. What is Tell, Don't Ask?

**Answer:** Ask objects to perform meaningful behavior rather than manipulate internals externally.

### Extended Q51. What is Law of Demeter awareness?

**Answer:** Avoid unnecessary knowledge of deep collaborator internals.

### Extended Q52. What is God Class?

**Answer:** Class with many unrelated responsibilities.

### Extended Q53. What is temporal coupling?

**Answer:** Correct use depends on hidden method-call order.

### Extended Q54. What is SRP?

**Answer:** One primary reason/change driver per component.

### Extended Q55. What is OCP?

**Answer:** Stable extension points for expected variation.

### Extended Q56. What is ISP?

**Answer:** Small client-specific interfaces.

### Extended Q57. What is DIP?

**Answer:** High-level policy depends on abstractions rather than concrete low-level details.

### Extended Q58. Does DIP require an interface for every class?

**Answer:** No.

### Extended Q59. What is dependency injection?

**Answer:** Supplying collaborators from outside.

### Extended Q60. Why constructor injection?

**Answer:** Required dependencies are explicit at construction.

### Extended Q61. What is composition root?

**Answer:** Boundary where concrete object graph is assembled.

### Extended Q62. Why service locator is problematic?

**Answer:** It hides dependencies behind global lookup.

### Extended Q63. What is a fake?

**Answer:** Lightweight working test implementation.

### Extended Q64. What is a stub?

**Answer:** Controlled test response provider.

### Extended Q65. What is a spy?

**Answer:** Test double recording interactions.

### Extended Q66. What is a mock?

**Answer:** Test double with expected interaction behavior.

### Extended Q67. What is a contract test?

**Answer:** Shared behavioral suite applied to multiple implementations.

### Extended Q68. What is domain service?

**Answer:** Domain behavior that does not belong naturally to one entity/value.

### Extended Q69. What is application service?

**Answer:** Use-case orchestration.

### Extended Q70. What is repository?

**Answer:** Persistence abstraction with domain-oriented operations.

### Extended Q71. What is DTO?

**Answer:** Data carrier across a boundary.

### Extended Q72. What is aggregate?

**Answer:** DDD consistency boundary around an aggregate root.

### Extended Q73. What is domain event?

**Answer:** Fact representing meaningful domain occurrence.

### Extended Q74. What does a class diagram show?

**Answer:** Types and structural relationships.

### Extended Q75. What does a sequence diagram show?

**Answer:** Interactions ordered over time.

### Extended Q76. What is Factory Method?

**Answer:** Named construction path.

### Extended Q77. What is Adapter?

**Answer:** Translates one interface into another.

### Extended Q78. What is Facade?

**Answer:** Simplifies a complex subsystem.

### Extended Q79. What is Decorator pattern?

**Answer:** Adds behavior by wrapping same-interface objects.

### Extended Q80. What is Proxy?

**Answer:** Stand-in controlling/lazily forwarding access.

### Extended Q81. What is Composite?

**Answer:** Tree pattern treating leaves/groups uniformly.

### Extended Q82. What is Strategy?

**Answer:** Replaceable algorithm/policy object.

### Extended Q83. What is Observer?

**Answer:** Subscribers react to published events.

### Extended Q84. What is Command?

**Answer:** Action represented as an object.

### Extended Q85. What is State pattern?

**Answer:** State-specific behavior represented by state objects.

### Extended Q86. What is Template Method?

**Answer:** Base class defines algorithm skeleton with overridable steps.

### Extended Q87. What is Chain of Responsibility?

**Answer:** Request passes through ordered handlers.

### Extended Q88. Why is Singleton often avoided?

**Answer:** Hidden global state and lifecycle/testing coupling.

### Extended Q89. Why does immutability help concurrency?

**Answer:** It prevents shared-state mutation races for that data.

### Extended Q90. What is thread-safety contract?

**Answer:** Rules defining whether/how concurrent callers may use an object.

### Extended Q91. Why create exception hierarchy?

**Answer:** Catch broad domain family while preserving specific failures.

### Extended Q92. What is anemic model smell?

**Answer:** Domain object has only data while all domain behavior lives elsewhere.

### Extended Q93. What is Middle Man smell?

**Answer:** Class adds no meaningful abstraction beyond forwarding calls.

### Extended Q94. What is speculative generality?

**Answer:** Abstraction created for hypothetical future needs.

### Extended Q95. What is long-parameter-list smell?

**Answer:** May indicate missing cohesive request/value object.

### Extended Q96. What is ports-and-adapters architecture?

**Answer:** Core defines ports; infrastructure implements adapters.

### Extended Q97. Final OOP design goal?

**Answer:** Clear responsibility, valid state, explicit dependencies, substitutable behavior, testability, and evolvability.




# Comprehensive OOP Mastery Checklist

- [ ] I can explain when not to use a class.
- [ ] I can explain state, behavior, identity, and invariants.
- [ ] I understand instance/class/static/classmethod behavior.
- [ ] I can explain Python encapsulation conventions and C++ access-control differences.
- [ ] I can use properties without hiding expensive side effects.
- [ ] I can model entity vs value object deliberately.
- [ ] I understand equality and hashing contracts.
- [ ] I can choose Protocol vs ABC.
- [ ] I understand inheritance, overriding, super, MRO, mixins, and diamond inheritance.
- [ ] I can explain LSP with behavioral examples.
- [ ] I understand Python dynamic dispatch and C++ virtual dispatch.
- [ ] I can distinguish association, aggregation, composition, and dependency.
- [ ] I prefer composition when the relation is has-a/uses-a.
- [ ] I understand Python special-method protocols and descriptors.
- [ ] I understand shallow/deep copy and serialization boundaries.
- [ ] I can identify cohesion and coupling problems.
- [ ] I can apply all five SOLID principles to real code rather than definitions.
- [ ] I can use constructor dependency injection and a composition root.
- [ ] I know why service locator hides dependencies.
- [ ] I can choose fakes, stubs, spies, mocks, and contract tests appropriately.
- [ ] I can model entity, value object, repository, DTO, domain service, and application service.
- [ ] I can draw class/object/sequence diagrams.
- [ ] I understand major creational, structural, and behavioral patterns.
- [ ] I know when a pattern would be overengineering.
- [ ] I understand thread-safety and immutability implications.
- [ ] I can recognize major OOP smells and anti-patterns.
- [ ] I can explain ports-and-adapters architecture.
- [ ] I completed the extended labs.
- [ ] I completed the Multi-Provider Deployment Planner.
