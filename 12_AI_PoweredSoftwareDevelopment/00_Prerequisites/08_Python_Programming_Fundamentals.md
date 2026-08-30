# Python Programming Fundamentals

> **Phase 2 — Programming Foundations**

This enhanced edition preserves the original course direction—example-driven Python for infrastructure, cloud, DevOps, and cybersecurity—and expands it into a deeper standalone learning resource.

The learning rule throughout this file is:

```text
Concept
  ↓
Mental Model / Diagram
  ↓
Python Syntax
  ↓
Expected Behavior
  ↓
Why It Works
  ↓
Real Engineering Use
  ↓
Failure / Security Considerations
  ↓
Hands-on Practice
```

Do not only read the examples. Before executing each one:

1. Predict the result.
2. Run it.
3. Change one variable.
4. Intentionally break it.
5. Read the error.
6. Repair it.
7. Explain why the repaired version works.

---

## 1. Topic Title

**Python Programming Fundamentals**

## 2. Learning Objectives

By the end of this course, you should be able to:

1. Explain Python's source → parse/compile → runtime execution model.
2. Distinguish syntax, runtime, and logic errors.
3. Explain names, objects, identity, equality, mutability, and references.
4. Use integers, floats, Decimal awareness, booleans, None, strings, and bytes/text concepts.
5. Normalize, parse, format, and validate strings safely.
6. Use arithmetic, comparison, boolean, and membership operators.
7. Write clear `if`/`elif`/`else` and guard-clause logic.
8. Use lists, tuples, sets, and dictionaries intentionally.
9. Use slicing, unpacking, comprehensions, sorting, and set operations.
10. Explain iterable, iterator, generator, and lazy-processing concepts.
11. Use `for`, `while`, `range`, `enumerate`, `zip`, `break`, and `continue`.
12. Write functions with clear contracts, parameters, return values, and type hints.
13. Explain scope, first-class functions, lambdas, decorators awareness, and context managers.
14. Avoid mutable-default-argument bugs.
15. Handle errors with specific exceptions, chaining, custom exceptions, and tracebacks.
16. Use `pathlib` and context managers for robust filesystem work.
17. Read/write text, CSV, and JSON using format-aware libraries.
18. Explain temporary files and atomic replacement awareness.
19. Organize code into modules and packages.
20. Use virtual environments and understand dependency isolation.
21. Recognize `pyproject.toml` as modern project metadata.
22. Use dataclasses and enums for structured domain data.
23. Use useful standard-library modules such as `collections`, `datetime`, `statistics`, `ipaddress`, `re`, `hashlib`, and `secrets`.
24. Parse environment configuration centrally.
25. Build CLIs with `argparse`, stdout/stderr discipline, and exit codes.
26. Use logging correctly without exposing secrets.
27. Execute subprocesses safely and understand shell-injection risk.
28. Apply bounded timeouts and retry-awareness.
29. Explain why `eval()` and untrusted `pickle` input are dangerous.
30. Recognize path traversal and oversized-input risks.
31. Write pure logic that is easy to test.
32. Apply normal, boundary, invalid, and regression testing.
33. Use `unittest` awareness, fakes, and dependency injection concepts.
34. Debug with tracebacks, `repr`, and debugger awareness.
35. Understand basic algorithmic-complexity implications of Python collection choices.
36. Separate I/O, validation, business logic, and reporting.
37. Design configuration precedence, idempotency, dry-run, and error taxonomy for automation.
38. Build a production-oriented Infrastructure Inventory and Health Reporter.

## 3. Prerequisites

Required:

```text
Phase 1 — Introduction to Programming
Operating Systems Fundamentals
Basic filesystem and terminal usage
```

Recommended:

```text
Computer Networks Fundamentals
Basic Git awareness
```

You should already understand:

```text
variables
if / loops
basic functions
lists / dictionaries
basic files
basic exceptions
```

This course revisits those areas much more deeply and connects them to real automation engineering.

## 4. Core Concepts Explanation

# Part 1 — How Python Executes a Program

### Core Explanation

A useful execution model is:

1. Python reads source code.
2. It parses the source according to Python grammar.
3. Valid source is compiled to an internal bytecode representation.
4. The Python runtime executes that representation.
5. Runtime operations create objects, call functions, perform I/O, and may raise exceptions.

You normally do not manually manage these stages, but separating them explains why a syntax error prevents execution while a runtime error happens only after execution reaches a particular operation.

### Diagram / Mental Model

```text
source.py
   ↓
Tokenizer / Parser
   ↓
Internal syntax representation
   ↓
Bytecode compilation
   ↓
Python Runtime / VM
   ↓
OS resources
├─ files
├─ network
├─ processes
└─ terminal
```

### Example / Code

```python
x = 10
y = 2
print(x / y)
```

### Expected Behavior / Output

```text
5.0
```

### Why It Works / Matters

The distinction between parse-time and runtime failure is one of the most useful debugging foundations.

### Practical Use

Use it whenever a script fails: first ask whether Python could parse the program, then ask which executed operation failed.

# Part 2 — Syntax Error vs Runtime Error

### Core Explanation

A syntax error means Python cannot interpret the program's grammatical structure. A runtime error means the program is syntactically valid but fails during execution.

A third category is a logic error: the program executes successfully but produces the wrong answer.

### Diagram / Mental Model

```text
Syntax error
→ program cannot start normally

Runtime error
→ execution starts
→ operation fails

Logic error
→ execution completes
→ result is wrong
```

### Example / Code

```python
# Runtime error:
value = "ten"
print(value / 2)
```

### Expected Behavior / Output

```text
TypeError: unsupported operand type(s) ...
```

### Why It Works / Matters

Different error categories require different troubleshooting strategies.

### Practical Use

Syntax: inspect grammar/indentation. Runtime: inspect types/state. Logic: compare expected and actual behavior using tests.

# Part 3 — REPL vs Script

### Core Explanation

The interactive interpreter (REPL) is useful for experimenting with expressions and small ideas. A script is a saved `.py` file intended for repeatable execution.

Use the REPL for exploration; use scripts/modules for reusable automation.

### Diagram / Mental Model

```text
REPL
input → immediate result

Script
source file → repeatable execution → Git / tests / automation
```

### Example / Code

```python
# REPL example concept:
>>> 2 ** 8
256
```

### Expected Behavior / Output

```text
256
```

### Why It Works / Matters

Understanding both workflows improves learning speed without turning experiments into unmaintainable production logic.

# Part 4 — The `__main__` Execution Model

### Core Explanation

When a Python file is executed directly, its special `__name__` variable is set to `"__main__"`. When the same file is imported, `__name__` is set to the module name.

The common guard prevents CLI behavior from executing just because another module imported reusable functions.

### Example / Code

```python
def main() -> int:
    print("application started")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

### Why It Works / Matters

This creates a clean boundary between reusable module behavior and process entry-point behavior.

### Practical Use

Use it in automation scripts, CLI tools, and small services.

# Part 5 — Process Exit Codes

### Core Explanation

A command-line program communicates success or failure to the shell through its process exit code.

Conventionally:
- `0` means success.
- non-zero means some category of failure.

The exact non-zero meanings are application-defined.

### Diagram / Mental Model

```text
Python CLI
   ↓ exits
OS / Shell receives integer
   ↓
CI / Bash / PowerShell can make decisions
```

### Example / Code

```python
def main() -> int:
    config_ok = False
    if not config_ok:
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

### Why It Works / Matters

Automation pipelines need machine-readable success/failure, not only printed text.

### Practical Use

Define exit code meanings in your README.

# Part 6 — Standard Input, Output, and Error

### Core Explanation

Python programs normally inherit three standard streams from the operating system:

- stdin: input
- stdout: normal output
- stderr: diagnostics/errors

Separating stdout and stderr allows scripts to pipe useful output while preserving diagnostics separately.

### Diagram / Mental Model

```text
stdin  → Python process
stdout ← normal result
stderr ← error / diagnostic messages
```

### Example / Code

```python
import sys

print("normal result")
print("configuration invalid", file=sys.stderr)
```

### Why It Works / Matters

This becomes important for shell pipelines, CI, logging, and automation composition.

# Part 7 — Names Bind to Objects

### Core Explanation

In Python, a variable is better understood as a **name bound to an object** rather than a typed memory box.

The type belongs to the object. The same name can later be rebound to another object of a different type.

### Diagram / Mental Model

```text
name "item"
   ↓
object 42 (int)

later:

name "item"
   ↓
object "server-01" (str)
```

### Example / Code

```python
item = 42
print(type(item))

item = "server-01"
print(type(item))
```

### Expected Behavior / Output

```text
<class 'int'>
<class 'str'>
```

### Why It Works / Matters

This explains dynamic typing, reference sharing, and many mutability behaviors.

# Part 8 — Identity vs Equality

### Core Explanation

Equality asks whether values compare equal. Identity asks whether two references point to the same object.

Use `==` for value equality. Use `is` primarily for singleton identity checks such as `is None`.

### Example / Code

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)
print(a is b)
print(a is c)
```

### Expected Behavior / Output

```text
True
False
True
```

### Why It Works / Matters

Confusing identity and equality can create subtle bugs.

### Practical Use

Use `value is None`, not `value == None`.

# Part 9 — `id()` Awareness

### Core Explanation

`id(obj)` returns an identity token that is unique for the object during its lifetime within that Python process. It is useful for learning/debugging reference behavior, but application logic should rarely depend on it.

### Example / Code

```python
a = []
b = a
print(id(a) == id(b))
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

It visually reinforces that two names can refer to one object.

# Part 10 — Mutability

### Core Explanation

Mutable objects can change in place. Lists, dictionaries, sets, and many user-defined objects are mutable. Strings, integers, floats, booleans, and tuples are immutable.

Mutability affects function behavior, copying, dictionary/set hashability, and concurrency.

### Diagram / Mental Model

```text
Mutable:
list → append changes same object

Immutable:
str → lower() creates new string object
```

### Example / Code

```python
ports = [22, 80]
ports.append(443)

hostname = "WEB-01"
hostname = hostname.lower()
```

### Why It Works / Matters

Cloud/configuration code frequently passes nested dictionaries between functions; shared mutation can alter state unexpectedly.

# Part 11 — Aliasing / Shared Mutable References

### Core Explanation

Assignment does not automatically copy a mutable object. If two names reference the same list or dictionary, mutation through either name is visible through the other.

### Example / Code

```python
servers = ["web-01", "db-01"]
alias = servers

alias.append("cache-01")

print(servers)
```

### Expected Behavior / Output

```text
['web-01', 'db-01', 'cache-01']
```

### Why It Works / Matters

This is a frequent source of accidental configuration changes.

# Part 12 — Shallow Copy

### Core Explanation

A shallow copy creates a new outer container but does not recursively duplicate nested mutable objects.

### Example / Code

```python
a = {"ports": [80, 443]}
b = a.copy()

b["ports"].append(8080)

print(a)
print(b)
```

### Expected Behavior / Output

```text
{'ports': [80, 443, 8080]}
{'ports': [80, 443, 8080]}
```

### Why It Works / Matters

The outer dictionaries differ, but both still reference the same nested list.

### Troubleshooting / Common Failure

When a shallow copy still changes nested data, inspect nested object identities.

# Part 13 — Deep Copy Awareness

### Core Explanation

`copy.deepcopy()` recursively copies many nested structures. It is useful when you truly need an independent object graph, but it is not automatically the right design.

Deep copying can be expensive and may be inappropriate for objects representing connections, file handles, locks, or external resources.

### Example / Code

```python
from copy import deepcopy

a = {"ports": [80, 443]}
b = deepcopy(a)

b["ports"].append(8080)

print(a)
print(b)
```

### Expected Behavior / Output

```text
{'ports': [80, 443]}
{'ports': [80, 443, 8080]}
```

### Why It Works / Matters

Understand the ownership model before copying everything.

# Part 14 — Hashability Awareness

### Core Explanation

Dictionary keys and set members must be hashable. Immutable values such as strings and many tuples are commonly hashable; mutable lists and dictionaries are not.

Hashability allows Python to place a value into hash-based collections while expecting its hash/equality behavior to remain stable.

### Example / Code

```python
allowed = {"prod", "test"}

mapping = {
    ("web-01", 443): "healthy",
}
```

### Why It Works / Matters

This explains why a list cannot normally be used as a dictionary key.

# Part 15 — Integers

### Core Explanation

Python integers represent whole numbers and are not limited to the fixed 32-bit/64-bit ranges common in lower-level languages; they grow as needed within available memory.

You still need domain validation. A technically valid Python integer such as `70000` is not a valid TCP port.

### Example / Code

```python
port = 443
retry_count = 3
large_value = 10**100
```

### Why It Works / Matters

Language range and business/domain range are different concepts.

# Part 16 — Floating-Point Numbers

### Core Explanation

Python `float` uses binary floating-point representation. Many decimal fractions cannot be represented exactly.

### Example / Code

```python
print(0.1 + 0.2)
```

### Expected Behavior / Output

```text
0.30000000000000004
```

### Why It Works / Matters

This is expected floating-point behavior, not Python being randomly incorrect.

### Practical Use

For money or exact decimal rules, use `decimal.Decimal`.

# Part 17 — `Decimal` Awareness

### Core Explanation

The `decimal` module supports decimal arithmetic with explicit precision and is useful when exact base-10 behavior matters.

### Example / Code

```python
from decimal import Decimal

total = Decimal("0.1") + Decimal("0.2")
print(total)
```

### Expected Behavior / Output

```text
0.3
```

### Why It Works / Matters

Construct Decimal from strings when exact decimal text matters.

# Part 18 — Booleans

### Core Explanation

`bool` has exactly two values: `True` and `False`. Conditions use truthiness, but explicit booleans make state easier to communicate.

### Example / Code

```python
is_online = True
has_alerts = False

if is_online and not has_alerts:
    print("healthy")
```

### Expected Behavior / Output

```text
healthy
```

# Part 19 — `None`

### Core Explanation

`None` represents absence of a value. It is distinct from `0`, `False`, empty text, and empty collections.

Use `is None` when testing for it.

### Example / Code

```python
region = None

if region is None:
    print("region not configured")
```

### Expected Behavior / Output

```text
region not configured
```

### Why It Works / Matters

Conflating missing values with empty/zero values often corrupts validation logic.

# Part 20 — Truthy and Falsy Values

### Core Explanation

Python converts many values to boolean context automatically.

Common falsy values include:
- `False`
- `None`
- `0`, `0.0`
- `""`
- `[]`, `{}`, `set()`

Everything else is generally truthy unless an object defines custom boolean behavior.

### Example / Code

```python
users = []

if not users:
    print("no users")
```

### Expected Behavior / Output

```text
no users
```

### Why It Works / Matters

Concise truthiness is idiomatic, but explicit comparisons are better when different falsy values mean different things.

# Part 21 — Strings Are Unicode Text

### Core Explanation

Python 3 strings represent Unicode text. Bytes are a different type used for raw binary data.

This distinction matters when reading files, network responses, cryptographic data, and subprocess output.

### Diagram / Mental Model

```text
Text:
str
  ↓ encode
bytes
  ↓ decode
str
```

### Example / Code

```python
text = "مرحبا"
raw = text.encode("utf-8")
restored = raw.decode("utf-8")

print(restored)
```

### Expected Behavior / Output

```text
مرحبا
```

### Why It Works / Matters

Encoding errors often come from mixing text and bytes or assuming the wrong encoding.

# Part 22 — String Immutability

### Core Explanation

Strings cannot be modified in place. Methods return new string objects.

### Example / Code

```python
name = "WEB-01"
lowered = name.lower()

print(name)
print(lowered)
```

### Expected Behavior / Output

```text
WEB-01
web-01
```

### Why It Works / Matters

This explains why string methods do not mutate the original variable unless you reassign.

# Part 23 — String Indexing and Slicing

### Core Explanation

Strings are sequences. Indexing retrieves one character; slicing creates a substring.

A slice uses `start:stop:step`, and the stop position is excluded.

### Example / Code

```python
name = "server-01"

print(name[0])
print(name[:6])
print(name[-2:])
```

### Expected Behavior / Output

```text
s
server
01
```

# Part 24 — String Normalization

### Core Explanation

External text often needs normalization such as stripping whitespace or normalizing case before comparison.

Normalization must be deliberate: do not lowercase or alter data where case is semantically important.

### Example / Code

```python
raw = "  PROD\n"
environment = raw.strip().lower()

print(environment)
```

### Expected Behavior / Output

```text
prod
```

### Practical Use

CLI args, environment variables, log fields, CSV values.

# Part 25 — Split and Join

### Core Explanation

`split()` breaks text into parts. `join()` combines strings with a separator.

Use format-aware parsers for CSV, JSON, URLs, IP addresses, and other structured formats instead of relying on manual splitting.

### Example / Code

```python
line = "web-01,10.0.0.10,prod"
parts = line.split(",")

print(parts)
print(" | ".join(parts))
```

### Expected Behavior / Output

```text
['web-01', '10.0.0.10', 'prod']
web-01 | 10.0.0.10 | prod
```

### Why It Works / Matters

Manual split fails on quoted CSV fields containing commas.

# Part 26 — f-Strings

### Core Explanation

f-strings provide readable interpolation and formatting.

### Example / Code

```python
host = "db-01"
cpu = 91.234

print(f"{host}: CPU={cpu:.1f}%")
```

### Expected Behavior / Output

```text
db-01: CPU=91.2%
```

### Why It Works / Matters

Readable output formatting is important for CLI and operational reports.

### Troubleshooting / Common Failure

Never interpolate secrets into logs or exception messages.

# Part 27 — Raw Strings Awareness

### Core Explanation

Raw string literals reduce interpretation of backslashes and are useful for regular expressions and Windows-style path fragments. A raw string still has syntax rules and cannot end with an unmatched backslash.

### Example / Code

```python
pattern = r"\d+\.\d+\.\d+\.\d+"
print(pattern)
```

### Expected Behavior / Output

```text
\d+\.\d+\.\d+\.\d+
```

### Why It Works / Matters

Useful when regexes contain many backslashes.

# Part 28 — Arithmetic Operators

### Core Explanation

Python supports addition, subtraction, multiplication, true division, floor division, modulo, and exponentiation.

Choose operators based on domain semantics rather than convenience.

### Example / Code

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### Expected Behavior / Output

```text
13
7
30
3.3333333333333335
3
1
1000
```

# Part 29 — Comparison Operators

### Core Explanation

Comparisons return booleans: `==`, `!=`, `<`, `<=`, `>`, `>=`.

### Example / Code

```python
cpu = 82

print(cpu >= 75)
print(cpu >= 90)
```

### Expected Behavior / Output

```text
True
False
```

### Why It Works / Matters

Boundary correctness depends on using the intended comparison operator.

# Part 30 — Chained Comparisons

### Core Explanation

Python can express range checks directly.

### Example / Code

```python
port = 443

if 1 <= port <= 65535:
    print("valid")
```

### Expected Behavior / Output

```text
valid
```

### Why It Works / Matters

This is clear and less error-prone than duplicated variable comparisons.

# Part 31 — Boolean Short-Circuiting

### Core Explanation

`and` and `or` stop evaluating once the result is already determined.

This can be useful but should not be abused for hidden side effects.

### Example / Code

```python
config = {}

if config and "region" in config:
    print(config["region"])
```

### Why It Works / Matters

The membership check does not run when the dictionary is empty.

### Practical Use

Prefer explicit validation functions for complex configuration rules.

# Part 32 — Operator Precedence

### Core Explanation

Operators have precedence rules. Parentheses should be used when they make intention easier to read.

### Example / Code

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

### Expected Behavior / Output

```text
14
20
```

# Part 33 — `if` / `elif` / `else`

### Core Explanation

Conditional branches should mirror the business rule clearly. The first matching branch executes.

### Example / Code

```python
cpu = 92

if cpu >= 90:
    severity = "critical"
elif cpu >= 75:
    severity = "warning"
else:
    severity = "normal"

print(severity)
```

### Expected Behavior / Output

```text
critical
```

### Why It Works / Matters

Branch ordering matters; place more specific or higher thresholds first.

# Part 34 — Guard Clauses

### Core Explanation

Guard clauses validate preconditions early and return/raise before normal logic.

### Example / Code

```python
def classify_cpu(value: float) -> str:
    if not 0 <= value <= 100:
        raise ValueError("CPU must be between 0 and 100")

    if value >= 90:
        return "critical"
    if value >= 75:
        return "warning"
    return "normal"
```

### Why It Works / Matters

This avoids deep nesting and protects core logic from invalid state.

# Part 35 — `match` Statement Awareness

### Core Explanation

Structural pattern matching can express some shape/value dispatch problems. It is useful when patterns are genuinely clearer than many `if` branches, but beginners should not replace every conditional with `match`.

### Example / Code

```python
def severity_message(level: str) -> str:
    match level:
        case "critical":
            return "immediate attention"
        case "warning":
            return "investigate"
        case "normal":
            return "healthy"
        case _:
            return "unknown"
```

### Why It Works / Matters

Know the feature, but prefer the clearest construct for the problem.

# Part 36 — Lists

### Core Explanation

A list is ordered, mutable, allows duplicates, and supports indexing/slicing.

Lists are a default choice for ordered sequences when you may add/remove/modify elements.

### Example / Code

```python
hosts = ["web-01", "db-01"]
hosts.append("cache-01")
print(hosts)
```

### Expected Behavior / Output

```text
['web-01', 'db-01', 'cache-01']
```

# Part 37 — List Methods

### Core Explanation

Common list operations include `append`, `extend`, `insert`, `remove`, `pop`, `sort`, and `reverse`.

Choose the operation whose semantics match your intention.

### Example / Code

```python
ports = [443, 22]
ports.append(80)
ports.sort()

print(ports)
```

### Expected Behavior / Output

```text
[22, 80, 443]
```

### Troubleshooting / Common Failure

`list.sort()` mutates the list and returns `None`; `sorted()` returns a new list.

# Part 38 — `sorted()` vs `.sort()`

### Core Explanation

`sorted(iterable)` returns a new sorted list. `list.sort()` mutates a list in place.

A `key` function lets you sort by derived properties.

### Example / Code

```python
servers = [
    {"name": "db", "cpu": 80},
    {"name": "web", "cpu": 95},
]

ordered = sorted(servers, key=lambda item: item["cpu"], reverse=True)
print(ordered[0]["name"])
```

### Expected Behavior / Output

```text
web
```

### Why It Works / Matters

Sorting structured records is common in reports.

# Part 39 — Tuples

### Core Explanation

A tuple is an ordered immutable sequence. Tuples are useful for fixed-size values, unpacking, and hashable composite keys when their contents are hashable.

### Example / Code

```python
endpoint = ("10.0.0.20", 443)
ip, port = endpoint

print(ip, port)
```

### Expected Behavior / Output

```text
10.0.0.20 443
```

# Part 40 — Sequence Unpacking

### Core Explanation

Python can assign multiple values from an iterable into multiple names.

### Example / Code

```python
host, ip, env = ("web-01", "10.0.0.10", "prod")
print(host)
```

### Expected Behavior / Output

```text
web-01
```

### Why It Works / Matters

Unpacking makes structured values easier to work with.

### Troubleshooting / Common Failure

The number of variables must match the number of items unless starred unpacking is used.

# Part 41 — Starred Unpacking Awareness

### Core Explanation

A starred target collects remaining items.

### Example / Code

```python
first, *middle, last = [1, 2, 3, 4, 5]

print(first)
print(middle)
print(last)
```

### Expected Behavior / Output

```text
1
[2, 3, 4]
5
```

# Part 42 — Sets

### Core Explanation

Sets store unique hashable values and are optimized for membership/set operations.

They do not provide sequence indexing and should not be used when stable order is the primary semantic requirement.

### Example / Code

```python
blocked_ips = {"10.0.0.9", "10.0.0.10"}
source = "10.0.0.9"

print(source in blocked_ips)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Membership checks and uniqueness are common in security and inventory tasks.

# Part 43 — Set Operations

### Core Explanation

Sets support union, intersection, difference, and symmetric difference.

### Example / Code

```python
expected = {"web-01", "db-01", "cache-01"}
observed = {"web-01", "db-01", "unknown-01"}

print("missing:", expected - observed)
print("unexpected:", observed - expected)
```

### Expected Behavior / Output

```text
missing: {'cache-01'}
unexpected: {'unknown-01'}
```

### Why It Works / Matters

Excellent for comparing inventories.

# Part 44 — Dictionaries

### Core Explanation

A dictionary maps unique hashable keys to values. It is ideal for lookup-oriented structured data.

Modern Python preserves insertion order as language behavior, but use dictionaries for mapping semantics rather than because you need list-like indexing.

### Example / Code

```python
server = {
    "hostname": "web-01",
    "ip": "10.0.0.10",
    "role": "frontend",
}

print(server["hostname"])
```

### Expected Behavior / Output

```text
web-01
```

# Part 45 — Required vs Optional Dictionary Keys

### Core Explanation

Use direct indexing when a key is required because failure should be explicit. Use `.get()` when absence is expected and meaningful.

### Example / Code

```python
server = {"hostname": "web-01"}

hostname = server["hostname"]      # required
role = server.get("role", "unknown")  # optional

print(hostname, role)
```

### Expected Behavior / Output

```text
web-01 unknown
```

### Why It Works / Matters

Using `.get()` everywhere can silently hide malformed required input.

# Part 46 — Dictionary Iteration

### Core Explanation

Dictionaries can be iterated by keys, values, or `(key, value)` pairs.

### Example / Code

```python
server = {"hostname": "web-01", "cpu": 4}

for key, value in server.items():
    print(key, value)
```

### Expected Behavior / Output

```text
hostname web-01
cpu 4
```

# Part 47 — Dictionary Merge Awareness

### Core Explanation

Python supports dictionary merging/unpacking patterns. These are useful for layered configuration but can accidentally overwrite keys.

### Example / Code

```python
base = {"region": "eu", "debug": False}
override = {"debug": True}

config = {**base, **override}
print(config)
```

### Expected Behavior / Output

```text
{'region': 'eu', 'debug': True}
```

### Why It Works / Matters

Later values win. Make precedence rules explicit.

# Part 48 — Nested Collections

### Core Explanation

Real configuration frequently nests dictionaries and lists. This is expressive but increases validation and copying complexity.

### Example / Code

```python
config = {
    "service": "api",
    "ports": [80, 443],
    "database": {
        "host": "db.internal",
        "port": 5432,
    },
}
```

### Why It Works / Matters

Define a schema/validation boundary rather than passing arbitrary nested dictionaries everywhere.

# Part 49 — Comprehensions

### Core Explanation

Comprehensions create collections through concise transformation/filter expressions.

They are excellent when the logic is simple. When multiple branches, logging, exceptions, or side effects are involved, an explicit loop is usually clearer.

### Example / Code

```python
ports = [22, 80, 443, 8080]
privileged = [port for port in ports if port < 1024]

print(privileged)
```

### Expected Behavior / Output

```text
[22, 80, 443]
```

# Part 50 — Dictionary Comprehension

### Core Explanation

Dictionary comprehensions are useful for building lookup tables.

### Example / Code

```python
hosts = ["web-01", "db-01"]
status = {host: "unknown" for host in hosts}

print(status)
```

### Expected Behavior / Output

```text
{'web-01': 'unknown', 'db-01': 'unknown'}
```

# Part 51 — Set Comprehension

### Core Explanation

Set comprehensions combine transformation and uniqueness.

### Example / Code

```python
records = ["WEB", "web", "DB"]
normalized = {item.lower() for item in records}

print(normalized)
```

### Expected Behavior / Output

```text
{'web', 'db'}
```

# Part 52 — `for` Loops

### Core Explanation

A `for` loop asks an iterable for successive values and processes each one.

### Example / Code

```python
for host in ["web-01", "db-01"]:
    print(host)
```

### Expected Behavior / Output

```text
web-01
db-01
```

# Part 53 — `range()`

### Core Explanation

`range()` represents an integer sequence without constructing a full list of every number.

### Example / Code

```python
for attempt in range(1, 4):
    print(attempt)
```

### Expected Behavior / Output

```text
1
2
3
```

### Why It Works / Matters

Useful for bounded retries and fixed repetition.

# Part 54 — `enumerate()`

### Core Explanation

`enumerate()` pairs each item with an index/counter.

### Example / Code

```python
hosts = ["web", "db"]

for number, host in enumerate(hosts, start=1):
    print(number, host)
```

### Expected Behavior / Output

```text
1 web
2 db
```

### Why It Works / Matters

Cleaner than manually incrementing a counter.

# Part 55 — `zip()`

### Core Explanation

`zip()` iterates over multiple iterables in parallel and stops when the shortest input is exhausted.

### Example / Code

```python
hosts = ["web", "db"]
ips = ["10.0.0.10", "10.0.0.20"]

for host, ip in zip(hosts, ips):
    print(host, ip)
```

### Expected Behavior / Output

```text
web 10.0.0.10
db 10.0.0.20
```

### Why It Works / Matters

Useful when sequences are intentionally aligned.

### Troubleshooting / Common Failure

If input lengths may differ, validate the lengths rather than silently losing values.

# Part 56 — `while` Loops

### Core Explanation

A `while` loop repeats while a condition remains true. Always identify the state/event that guarantees termination.

### Example / Code

```python
attempt = 1

while attempt <= 3:
    print(attempt)
    attempt += 1
```

### Expected Behavior / Output

```text
1
2
3
```

### Troubleshooting / Common Failure

If a loop hangs, inspect whether the controlling state can actually change.

# Part 57 — `break` and `continue`

### Core Explanation

`break` exits the nearest loop. `continue` skips the rest of the current iteration.

### Example / Code

```python
for value in [10, -1, 20, 99]:
    if value < 0:
        continue
    if value > 90:
        break
    print(value)
```

### Expected Behavior / Output

```text
10
20
```

# Part 58 — Iterable vs Iterator

### Core Explanation

An iterable can produce an iterator. An iterator tracks iteration state and returns the next item until it raises `StopIteration`.

You normally use this indirectly through `for`.

### Diagram / Mental Model

```text
Iterable
  ↓ iter()
Iterator
  ↓ next()
item
  ↓ next()
item
  ↓
StopIteration
```

### Example / Code

```python
values = [10, 20]
it = iter(values)

print(next(it))
print(next(it))
```

### Expected Behavior / Output

```text
10
20
```

### Why It Works / Matters

This is the foundation for generators and streaming data.

# Part 59 — Generator Function

### Core Explanation

A generator function uses `yield` to produce values lazily instead of constructing the entire result collection at once.

### Example / Code

```python
def failed_lines(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if "FAILED" in line:
                yield line.rstrip()
```

### Why It Works / Matters

Generators are excellent for large logs, files, API pages, and streams because memory use can remain bounded.

# Part 60 — Generator Expression

### Core Explanation

Generator expressions look similar to list comprehensions but produce values lazily.

### Example / Code

```python
squares = (x * x for x in range(5))

for value in squares:
    print(value)
```

### Expected Behavior / Output

```text
0
1
4
9
16
```

### Why It Works / Matters

Use when you only need to stream through the generated values once.

# Part 61 — `any()` and `all()`

### Core Explanation

`any()` is true if any element is truthy. `all()` is true if every element is truthy.

### Example / Code

```python
checks = [True, True, False]

print(all(checks))
print(any(checks))
```

### Expected Behavior / Output

```text
False
True
```

### Practical Use

Validation summaries and health checks.

# Part 62 — `min`, `max`, `sum`

### Core Explanation

Built-ins often express collection operations more clearly than manual accumulators.

### Example / Code

```python
samples = [70, 80, 95]

print(min(samples))
print(max(samples))
print(sum(samples) / len(samples))
```

### Expected Behavior / Output

```text
70
95
81.66666666666667
```

# Part 63 — Function as Reusable Behavior

### Core Explanation

Functions group coherent behavior behind a name and explicit interface.

### Example / Code

```python
def classify_cpu(usage: float) -> str:
    if usage >= 90:
        return "critical"
    if usage >= 75:
        return "warning"
    return "normal"
```

### Why It Works / Matters

Small pure functions are easy to test and reuse.

# Part 64 — Parameters vs Arguments

### Core Explanation

Parameters appear in the function definition. Arguments are the actual values supplied during a call.

### Example / Code

```python
def connect(host, port):
    print(host, port)

connect("api.internal", 443)
```

### Expected Behavior / Output

```text
api.internal 443
```

# Part 65 — Return Values

### Core Explanation

A function should usually return data when the caller may need to reuse or test the result.

Printing is a side effect; returning is an interface.

### Example / Code

```python
def free_percent(total: int, free: int) -> float:
    return free / total * 100

result = free_percent(100, 25)
print(result)
```

### Expected Behavior / Output

```text
25.0
```

# Part 66 — Implicit `None`

### Core Explanation

A function that reaches the end without an explicit return returns `None`.

### Example / Code

```python
def write_message():
    print("hello")

result = write_message()
print(result)
```

### Expected Behavior / Output

```text
hello
None
```

### Why It Works / Matters

Unexpected `None` values often come from forgetting to return.

# Part 67 — Default Parameters

### Core Explanation

Default parameters provide values when the caller omits an argument.

### Example / Code

```python
def connect(host: str, port: int = 443, timeout: int = 5) -> None:
    print(host, port, timeout)

connect("api.internal", timeout=10)
```

### Expected Behavior / Output

```text
api.internal 443 10
```

# Part 68 — Mutable Default Argument Trap

### Core Explanation

Default argument expressions are evaluated when the function is defined, not freshly for every call. A mutable default can therefore retain state between calls.

### Example / Code

```python
# Correct pattern:
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
```

### Why It Works / Matters

This is a classic Python bug and should be understood early.

# Part 69 — Keyword Arguments

### Core Explanation

Keyword arguments make calls self-documenting and let callers override selected defaults.

### Example / Code

```python
connect(
    host="api.internal",
    port=8443,
    timeout=10,
)
```

### Why It Works / Matters

Especially useful for configuration-heavy functions.

# Part 70 — Positional and Keyword-Only Awareness

### Core Explanation

Python supports restricting whether arguments can be supplied positionally or by keyword. This can make public APIs clearer.

The exact syntax is worth knowing but should be used when it improves readability rather than for novelty.

### Example / Code

```python
def connect(host: str, *, timeout: int = 5) -> None:
    print(host, timeout)

connect("api.internal", timeout=10)
```

### Why It Works / Matters

Keyword-only settings reduce mistakes when several parameters have similar types.

# Part 71 — Variable-Length Arguments Awareness

### Core Explanation

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.

They are powerful but can obscure a function contract if overused.

### Example / Code

```python
def log_event(event: str, **fields) -> None:
    print(event, fields)

log_event("login", user="alice", success=True)
```

### Expected Behavior / Output

```text
login {'user': 'alice', 'success': True}
```

### Why It Works / Matters

Use when an open-ended interface is genuinely needed.

# Part 72 — Scope and LEGB Awareness

### Core Explanation

Python resolves names through scopes often summarized as LEGB:

- Local
- Enclosing
- Global
- Built-in

Prefer explicit data flow rather than relying heavily on globals.

### Diagram / Mental Model

```text
function local
   ↓ if not found
enclosing function
   ↓
module global
   ↓
built-ins
```

### Why It Works / Matters

Understanding scope prevents NameError and accidental shadowing.

# Part 73 — Global State Risk

### Core Explanation

Mutable global state creates hidden dependencies between functions/tests and makes behavior depend on execution order.

### Example / Code

```python
# Avoid when possible:
threshold = 90

def is_critical(value):
    return value >= threshold
```

### Why It Works / Matters

Pass configuration explicitly or encapsulate it in an object/config structure.

# Part 74 — First-Class Functions

### Core Explanation

Functions are objects. They can be assigned to variables, passed to other functions, and returned.

This enables callbacks, dependency injection patterns, decorators, and higher-order functions.

### Example / Code

```python
def critical(value):
    return value >= 90

checker = critical
print(checker(95))
```

### Expected Behavior / Output

```text
True
```

# Part 75 — Lambda Awareness

### Core Explanation

A lambda creates a small anonymous function expression. It is useful for short key functions but should not replace readable named functions for complex behavior.

### Example / Code

```python
records = [
    {"host": "web", "cpu": 80},
    {"host": "db", "cpu": 95},
]

records.sort(key=lambda row: row["cpu"], reverse=True)
print(records[0]["host"])
```

### Expected Behavior / Output

```text
db
```

# Part 76 — Function Contracts

### Core Explanation

A robust function has an implicit or documented contract covering:
- valid inputs
- output meaning
- exceptions
- side effects
- important invariants

### Example / Code

```python
def read_port(text: str) -> int:
    """Parse a valid TCP/UDP port number from text."""
    ...
```

### Why It Works / Matters

Contracts make testing and reuse much easier.

# Part 77 — Docstrings

### Core Explanation

Docstrings document modules, functions, classes, and methods. Good docstrings explain the purpose, non-obvious constraints, important parameters/returns, and raised exceptions.

### Example / Code

```python
def read_port(text: str) -> int:
    """Return a validated port in the inclusive range 1..65535."""
```

### Why It Works / Matters

Avoid comments that simply restate obvious code.

# Part 78 — Exception Model

### Core Explanation

Exceptions represent abnormal conditions that propagate up the call stack until handled.

The right question is not 'How do I stop exceptions?' but 'Which failures can this layer handle meaningfully?'

### Diagram / Mental Model

```text
low-level operation fails
   ↓ raises exception
caller does not handle
   ↓
next caller
   ↓
boundary handles / logs / exits
```

### Why It Works / Matters

Exception propagation keeps error handling near the layer that has enough context to decide.

# Part 79 — Catching Specific Exceptions

### Core Explanation

Catch narrow exception types for failures you expect and know how to handle.

### Example / Code

```python
try:
    port = int("abc")
except ValueError as exc:
    print("invalid port:", exc)
```

### Why It Works / Matters

Broad catches can hide programming defects.

# Part 80 — Exception Chaining

### Core Explanation

When translating a low-level exception into a domain-specific one, use `raise ... from exc` to preserve the original cause.

### Example / Code

```python
class ConfigError(Exception):
    pass

try:
    value = int("not-a-number")
except ValueError as exc:
    raise ConfigError("invalid retry count") from exc
```

### Why It Works / Matters

Preserving the causal chain makes debugging much easier.

# Part 81 — Custom Exceptions

### Core Explanation

A custom exception can represent domain-level failure and prevent higher layers from depending on many low-level exception details.

### Example / Code

```python
class InventoryError(Exception):
    pass
```

### Practical Use

Use sparingly when a distinct failure category improves the interface.

# Part 82 — `else` in try/except

### Core Explanation

The `else` block runs only if the `try` block finishes without an exception.

### Example / Code

```python
try:
    port = int("443")
except ValueError:
    print("invalid")
else:
    print(port)
```

### Expected Behavior / Output

```text
443
```

### Why It Works / Matters

Keeps successful logic separate from the protected operation.

# Part 83 — `finally`

### Core Explanation

A `finally` block runs regardless of whether an exception occurred. It is useful for cleanup, although context managers are preferred for many resources.

### Example / Code

```python
try:
    print("work")
finally:
    print("cleanup")
```

### Expected Behavior / Output

```text
work
cleanup
```

# Part 84 — Do Not Swallow Exceptions

### Core Explanation

Patterns that catch and ignore every error create silent corruption and impossible debugging.

### Example / Code

```python
# Avoid:
# try:
#     important_operation()
# except Exception:
#     pass
```

### Why It Works / Matters

Unexpected failures should normally remain visible unless you can recover safely.

# Part 85 — Tracebacks

### Core Explanation

A traceback records the stack of calls through which an exception propagated. Read the final exception type/message first, then locate the relevant frames in your code.

### Diagram / Mental Model

```text
most recent failure:
ValueError: invalid port
   ↑ called by parse_config()
   ↑ called by main()
```

### Practical Use

Treat tracebacks as evidence.

# Part 86 — `pathlib.Path`

### Core Explanation

`Path` gives a portable object-oriented interface for filesystem paths.

### Example / Code

```python
from pathlib import Path

path = Path("reports") / "inventory.json"
print(path)
```

### Expected Behavior / Output

```text
reports/inventory.json
```

### Why It Works / Matters

Avoid manual slash/backslash concatenation.

# Part 87 — Current Working Directory

### Core Explanation

Relative paths are resolved from the process current working directory, not automatically from the script file's directory.

### Example / Code

```python
from pathlib import Path

print(Path.cwd())
```

### Why It Works / Matters

This explains many 'file exists but script cannot find it' problems in CI and services.

# Part 88 — Script Directory Awareness

### Core Explanation

If data is intentionally packaged relative to a module, derive its location from `__file__` rather than assuming the current working directory.

### Example / Code

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
config_path = BASE_DIR / "config.json"
```

### Why It Works / Matters

Use carefully: CLI input paths should usually remain user-controlled rather than silently forced relative to source.

# Part 89 — Context Managers for Files

### Core Explanation

`with` ensures the file is closed even when an exception occurs.

### Example / Code

```python
from pathlib import Path

path = Path("report.txt")

with path.open("w", encoding="utf-8") as fh:
    fh.write("status=healthy\n")
```

### Why It Works / Matters

Resource ownership and cleanup are explicit.

# Part 90 — Streaming Large Files

### Core Explanation

Iterating over a file reads progressively rather than loading everything into memory.

### Example / Code

```python
with open("auth.log", encoding="utf-8") as fh:
    for line_number, line in enumerate(fh, start=1):
        if "FAILED" in line:
            print(line_number, line.rstrip())
```

### Why It Works / Matters

This is critical for large logs.

# Part 91 — Text Encoding

### Core Explanation

Specify encodings explicitly when appropriate. UTF-8 is common and avoids dependence on platform default encodings.

### Example / Code

```python
text = Path("message.txt").read_text(encoding="utf-8")
```

### Why It Works / Matters

Cross-platform automation should not silently depend on local encoding defaults.

# Part 92 — JSON Parsing

### Core Explanation

`json.loads()` parses JSON text; `json.load()` parses from a file-like object.

### Example / Code

```python
import json

data = json.loads('{"host":"web-01","ports":[80,443]}')
print(data["ports"])
```

### Expected Behavior / Output

```text
[80, 443]
```

### Why It Works / Matters

Parsing does not automatically validate your business schema.

# Part 93 — JSON Serialization

### Core Explanation

`json.dumps()` converts supported Python values to JSON text.

### Example / Code

```python
import json

result = {"host": "web-01", "healthy": True}
print(json.dumps(result, indent=2))
```

### Expected Behavior / Output

```text
{
  "host": "web-01",
  "healthy": true
}
```

### Why It Works / Matters

JSON booleans/null use JSON syntax, not Python syntax.

# Part 94 — CSV Parsing

### Core Explanation

Use the `csv` module rather than manual splitting because CSV supports quoting and escaped delimiters.

### Example / Code

```python
import csv

with open("servers.csv", newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        print(row["hostname"], row["ip"])
```

### Why It Works / Matters

Format-aware parsers reduce data corruption.

# Part 95 — CSV Writing

### Core Explanation

`csv.DictWriter` writes dictionaries using a declared field order.

### Example / Code

```python
import csv

rows = [{"hostname": "web-01", "status": "healthy"}]

with open("report.csv", "w", newline="", encoding="utf-8") as fh:
    writer = csv.DictWriter(fh, fieldnames=["hostname", "status"])
    writer.writeheader()
    writer.writerows(rows)
```

### Why It Works / Matters

Stable schemas improve interoperability.

# Part 96 — Atomic File Replacement Awareness

### Core Explanation

When replacing important configuration/report files, a safer pattern can be:
1. write a temporary file
2. flush/close it
3. rename/replace it atomically where the filesystem semantics support that

This reduces the window where a crash leaves a partially written target.

### Diagram / Mental Model

```text
target.json
   ↑ replace
temp.json ← write fully first
```

### Why It Works / Matters

Useful for configuration generators and state files.

# Part 97 — Temporary Files Awareness

### Core Explanation

The `tempfile` module creates temporary files/directories safely without inventing predictable names manually.

### Example / Code

```python
from tempfile import TemporaryDirectory
from pathlib import Path

with TemporaryDirectory() as directory:
    path = Path(directory) / "result.txt"
    path.write_text("ok", encoding="utf-8")
    print(path.exists())
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Predictable temp filenames can cause collisions and security problems.

# Part 98 — Modules

### Core Explanation

A module is usually a `.py` file containing reusable code. Importing a module executes its top-level statements once per normal import lifecycle and exposes its definitions.

### Diagram / Mental Model

```text
main.py
  ↓ import
validators.py
  ├─ validate_port()
  └─ validate_env()
```

### Why It Works / Matters

Top-level side effects in imported modules should be minimized.

# Part 99 — Packages

### Core Explanation

A package groups related modules under a namespace and enables larger project organization.

The exact packaging metadata is a later topic; at fundamentals level, understand the namespace and responsibility model.

### Diagram / Mental Model

```text
infra_reporter/
├─ __init__.py (traditional package marker)
├─ collectors.py
├─ validators.py
└─ reporters.py
```

# Part 100 — Absolute vs Relative Imports Awareness

### Core Explanation

Imports can reference package names absolutely or use package-relative syntax. Prefer a consistent project structure that avoids fragile manipulation of `sys.path`.

### Why It Works / Matters

Import errors often come from launching code from unexpected directories or unclear project packaging.

# Part 101 — Import Side Effects

### Core Explanation

Code at module top level executes during import. Network calls, file writes, or long initialization at import time can make testing and startup unpredictable.

### Example / Code

```python
# Better:
def initialize():
    ...

# Avoid doing expensive/destructive work automatically at import.
```

### Why It Works / Matters

Keep imports cheap and unsurprising.

# Part 102 — Circular Import Awareness

### Core Explanation

A circular import happens when modules depend on each other during import initialization.

### Diagram / Mental Model

```text
a.py imports b.py
   ↑       ↓
   └───────┘
```

### Why It Works / Matters

It often signals tangled responsibilities or misplaced shared definitions.

### Troubleshooting / Common Failure

Refactor common abstractions into a third module or change dependency direction.

# Part 103 — Virtual Environments

### Core Explanation

A virtual environment isolates a project's Python interpreter environment and installed packages from other projects.

### Example / Code

```bash
python -m venv .venv
```

### Why It Works / Matters

Prevents one project's dependency versions from contaminating another.

# Part 104 — Activating a Virtual Environment

### Core Explanation

Activation adjusts shell environment variables such as PATH so `python` and package commands refer to the environment.

Activation is a convenience, not the mechanism that makes the environment exist.

### Example / Code

```text
Linux/macOS:
source .venv/bin/activate

Windows PowerShell:
.\.venv\Scripts\Activate.ps1
```

### Practical Use

Confirm the actual interpreter path when debugging dependency issues.

# Part 105 — Dependency Installation Awareness

### Core Explanation

Third-party packages should be installed from trusted sources and recorded in project dependency metadata.

Avoid installing random packages solely because a tutorial says so. Every dependency increases supply-chain and maintenance risk.

### Why It Works / Matters

Dependency management is part of reliability and security.

# Part 106 — `pyproject.toml` Awareness

### Core Explanation

Modern Python projects can use `pyproject.toml` to describe build-system and project metadata. You do not need to master packaging yet, but recognize it as a standard project configuration file.

### Example / Code

```toml
[project]
name = "infra-reporter"
version = "0.1.0"
```

### Why It Works / Matters

Later backend and automation projects will rely on structured project metadata.

# Part 107 — Type Hints

### Core Explanation

Type hints communicate expected interfaces to humans, IDEs, and static analysis tools. They do **not** automatically enforce runtime types.

### Example / Code

```python
def free_percent(total: int, free: int) -> float:
    if total <= 0:
        raise ValueError("total must be positive")
    return free / total * 100
```

### Why It Works / Matters

Type hints improve maintainability and catch many mistakes before execution.

# Part 108 — Collection Type Hints

### Core Explanation

Modern annotations can describe collection shapes.

### Example / Code

```python
def critical_hosts(records: list[dict[str, object]]) -> list[str]:
    ...
```

### Why It Works / Matters

For complex nested data, consider structured models instead of increasingly complicated dictionary annotations.

# Part 109 — Union / Optional Values

### Core Explanation

A value that may be absent can be annotated with a union including `None`.

### Example / Code

```python
def find_region(config: dict[str, str]) -> str | None:
    return config.get("region")
```

### Why It Works / Matters

This makes absence explicit in the interface.

# Part 110 — Dataclasses

### Core Explanation

A dataclass provides concise syntax for structured records with generated initialization/representation/equality behavior.

### Example / Code

```python
from dataclasses import dataclass

@dataclass
class Server:
    hostname: str
    ip: str
    environment: str = "dev"

server = Server("web-01", "10.0.0.10", "prod")
print(server)
```

### Expected Behavior / Output

```text
Server(hostname='web-01', ip='10.0.0.10', environment='prod')
```

### Why It Works / Matters

Use when the program benefits from a defined record shape.

# Part 111 — Frozen Dataclass Awareness

### Core Explanation

A frozen dataclass prevents normal field reassignment and can communicate that a record should be treated as immutable.

### Example / Code

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int
```

### Why It Works / Matters

Immutability can reduce accidental shared-state bugs.

# Part 112 — Enum Awareness

### Core Explanation

`Enum` gives a finite set of named values and can be clearer than repeated magic strings in some domains.

### Example / Code

```python
from enum import Enum

class Status(str, Enum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"
```

### Why It Works / Matters

Useful when values must come from a closed controlled set.

# Part 113 — `collections.Counter`

### Core Explanation

`Counter` counts hashable values.

### Example / Code

```python
from collections import Counter

statuses = ["FAILED", "OK", "FAILED", "FAILED"]
counts = Counter(statuses)

print(counts["FAILED"])
```

### Expected Behavior / Output

```text
3
```

### Practical Use

Authentication failures, HTTP statuses, event types.

# Part 114 — `defaultdict` Awareness

### Core Explanation

`defaultdict` automatically creates missing values using a factory.

### Example / Code

```python
from collections import defaultdict

by_user = defaultdict(list)
by_user["alice"].append("10.0.0.5")

print(by_user["alice"])
```

### Expected Behavior / Output

```text
['10.0.0.5']
```

### Why It Works / Matters

Useful for grouping, but normal dictionaries may be clearer when automatic creation is not desired.

# Part 115 — `deque` Awareness

### Core Explanation

`collections.deque` supports efficient append/pop operations at both ends.

### Example / Code

```python
from collections import deque

recent = deque(maxlen=3)
for item in [1, 2, 3, 4]:
    recent.append(item)

print(list(recent))
```

### Expected Behavior / Output

```text
[2, 3, 4]
```

### Practical Use

Bounded recent-event windows and queues.

# Part 116 — `statistics`

### Core Explanation

The standard library can calculate simple descriptive statistics.

### Example / Code

```python
from statistics import mean, median

samples = [10, 11, 12, 100]

print(mean(samples))
print(median(samples))
```

### Expected Behavior / Output

```text
33.25
11.5
```

### Why It Works / Matters

Median can communicate typical latency better when outliers are large.

# Part 117 — `datetime` and Timezone-Aware Timestamps

### Core Explanation

Operational software should treat time carefully. Prefer timezone-aware timestamps for distributed systems.

### Example / Code

```python
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
print(now.isoformat())
```

### Why It Works / Matters

Naive local timestamps become ambiguous across regions, daylight-saving changes, and systems.

# Part 118 — Parsing ISO Timestamps Awareness

### Core Explanation

When reading timestamps, use format-aware parsers rather than substring assumptions.

### Example / Code

```python
from datetime import datetime

value = datetime.fromisoformat("2026-08-19T08:00:00+03:00")
print(value.tzinfo)
```

### Why It Works / Matters

Timezones are data, not formatting decoration.

# Part 119 — `os.environ`

### Core Explanation

Environment variables are a common source of deployment configuration.

### Example / Code

```python
import os

environment = os.getenv("APP_ENV", "dev")
print(environment)
```

### Why It Works / Matters

Configuration from environment should still be converted and validated.

# Part 120 — Centralized Environment Parsing

### Core Explanation

Do not call `os.getenv()` throughout the codebase with ad-hoc conversion. Centralize parsing and validation.

### Example / Code

```python
import os

def read_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default

    value = raw.strip().lower()

    if value in {"1", "true", "yes", "on"}:
        return True
    if value in {"0", "false", "no", "off"}:
        return False

    raise ValueError(f"{name} must be boolean-like")
```

### Why It Works / Matters

Failing fast avoids surprising downstream configuration errors.

# Part 121 — `platform` and `socket`

### Core Explanation

The standard library can inspect basic platform and hostname information.

### Example / Code

```python
import platform
import socket

print(socket.gethostname())
print(platform.system())
print(platform.release())
```

### Practical Use

Local inventory and diagnostic tools.

# Part 122 — `shutil.disk_usage`

### Core Explanation

`shutil.disk_usage()` returns total, used, and free bytes for a filesystem path.

### Example / Code

```python
from pathlib import Path
import shutil

total, used, free = shutil.disk_usage(Path.cwd())

print(round(free / 1024**3, 2))
```

### Practical Use

Disk health and capacity reports.

# Part 123 — `ipaddress`

### Core Explanation

The `ipaddress` module validates and manipulates IPv4/IPv6 addresses and networks.

### Example / Code

```python
from ipaddress import ip_address, ip_network

address = ip_address("10.0.0.25")
network = ip_network("10.0.0.0/24")

print(address in network)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Use proven parsers instead of home-grown regex rules for IP semantics.

# Part 124 — `re` Regular Expressions

### Core Explanation

Regular expressions match text patterns. They are powerful for logs and text extraction, but not every parsing problem should become a regex.

Use domain-specific parsers for structured formats.

### Example / Code

```python
import re

line = "user=alice status=FAILED"
match = re.search(r"user=(\w+)\s+status=(\w+)", line)

if match:
    print(match.group(1), match.group(2))
```

### Expected Behavior / Output

```text
alice FAILED
```

### Why It Works / Matters

Regexes are useful for semi-structured text, but maintainability matters.

# Part 125 — Regex Anchors and Full Match

### Core Explanation

Use `fullmatch()` when the entire string must conform to a pattern rather than merely containing a matching substring.

### Example / Code

```python
import re

pattern = re.compile(r"[a-z0-9-]{1,20}")

print(bool(pattern.fullmatch("web-01")))
print(bool(pattern.fullmatch("web 01")))
```

### Expected Behavior / Output

```text
True
False
```

### Why It Works / Matters

Validation semantics differ from search semantics.

# Part 126 — ReDoS Awareness

### Core Explanation

Some poorly designed regular expressions can require excessive processing for crafted input. This is called catastrophic backtracking or regex denial-of-service behavior in affected engines/patterns.

Keep regexes simple for untrusted large inputs and enforce reasonable input-size limits.

### Why It Works / Matters

Security and performance are connected.

# Part 127 — `hashlib`

### Core Explanation

Cryptographic hash functions produce a fixed-size digest from data. A changed file normally produces a different digest.

A hash proves content equality/change against a trusted baseline; it does not tell you who changed the file or whether the change was malicious.

### Example / Code

```python
from hashlib import sha256
from pathlib import Path

digest = sha256(Path("config.txt").read_bytes()).hexdigest()
print(digest)
```

### Practical Use

Integrity baselines and artifact verification.

# Part 128 — `secrets` vs `random`

### Core Explanation

The `random` module is designed for simulation/general pseudo-random behavior, not for generating security secrets. Use `secrets` for tokens and security-sensitive random values.

### Example / Code

```python
import secrets

token = secrets.token_urlsafe(32)
print(len(token) > 20)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Security-sensitive randomness requires a cryptographically appropriate source.

# Part 129 — `argparse`

### Core Explanation

`argparse` creates command-line interfaces with typed arguments, help text, defaults, and validation support.

### Example / Code

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--threshold", type=int, default=3)

args = parser.parse_args()
print(args.input, args.threshold)
```

### Why It Works / Matters

CLI arguments are better than interactive input for repeatable automation.

# Part 130 — CLI Contract

### Core Explanation

A production CLI should define:
- command syntax
- required and optional arguments
- output format
- stdout/stderr behavior
- exit codes
- configuration precedence
- examples

### Diagram / Mental Model

```text
CLI input
  ↓ parse
  ↓ validate
  ↓ execute
  ↓ stdout/stderr
  ↓ exit code
```

### Why It Works / Matters

A CLI is an interface consumed by both people and scripts.

# Part 131 — Logging

### Core Explanation

`logging` provides severity, timestamps, formatting, handlers, and integration options missing from ad-hoc `print()`.

### Example / Code

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("inventory collection started")
```

### Why It Works / Matters

Operational code needs consistent diagnostic context.

# Part 132 — Logging Levels

### Core Explanation

Use levels according to operational meaning:

- DEBUG: detailed diagnostics
- INFO: normal lifecycle events
- WARNING: abnormal but recoverable condition
- ERROR: an operation failed
- CRITICAL: severe application-wide failure

Teams should define their own conventions consistently.

### Why It Works / Matters

Level inflation creates noisy logs and ineffective alerts.

# Part 133 — Exception Logging

### Core Explanation

Inside an exception handler, `logging.exception()` records the current traceback automatically.

### Example / Code

```python
import logging

try:
    raise RuntimeError("simulated")
except RuntimeError:
    logging.exception("collection failed")
```

### Why It Works / Matters

Preserves context without manually formatting tracebacks.

# Part 134 — Secret Redaction

### Core Explanation

Logs should not contain passwords, private keys, bearer tokens, session cookies, or full secret configuration.

Redact or omit sensitive values before logging.

### Example / Code

```python
def redact(value: str) -> str:
    if not value:
        return "<empty>"
    return value[:2] + "***"
```

### Why It Works / Matters

Logs are persistent and often accessible to many systems/users.

# Part 135 — `subprocess.run()`

### Core Explanation

`subprocess.run()` executes an external program and returns its exit code/output.

Prefer an argument list instead of constructing a shell string from untrusted data.

### Example / Code

```python
import subprocess

result = subprocess.run(
    ["python", "--version"],
    text=True,
    capture_output=True,
    check=False,
)

print("exit:", result.returncode)
print("stdout:", result.stdout.strip())
print("stderr:", result.stderr.strip())
```

### Why It Works / Matters

Argument lists avoid shell interpretation in the common case.

# Part 136 — Shell Injection Risk

### Core Explanation

If untrusted data is inserted into a shell command string, the shell may interpret the data as commands/operators rather than literal arguments.

Avoid `shell=True` unless you genuinely require shell syntax and fully control the command construction.

### Example / Code

```python
# Unsafe design pattern:
# subprocess.run(f"some-command {user_input}", shell=True)

# Safer design:
subprocess.run(["some-command", user_input], shell=False)
```

### Why It Works / Matters

Separating command and arguments is the same security principle as parameterized SQL.

# Part 137 — Checking Subprocess Results

### Core Explanation

A process returning output does not mean it succeeded. Check its exit code and decide whether failure is expected.

### Example / Code

```python
import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True,
)

if result.returncode != 0:
    raise RuntimeError(result.stderr.strip())
```

### Why It Works / Matters

Automation must reason about both data and execution status.

# Part 138 — Timeouts for External Commands

### Core Explanation

External commands can hang. Use bounded timeouts when your workflow requires a deadline.

### Example / Code

```python
import subprocess

try:
    result = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True,
        timeout=5,
    )
except subprocess.TimeoutExpired:
    print("command exceeded deadline")
```

### Why It Works / Matters

Every external dependency should have a failure/timeout model.

# Part 139 — Retry Awareness

### Core Explanation

Retries can recover from transient failures, but only retry operations that are safe to repeat and errors that are plausibly transient.

A retry loop should be bounded.

### Example / Code

```python
import time

def run_with_retry(operation, attempts: int = 3, delay: float = 1.0):
    if attempts < 1:
        raise ValueError("attempts must be >= 1")

    last_error = None

    for attempt in range(1, attempts + 1):
        try:
            return operation()
        except RuntimeError as exc:
            last_error = exc
            if attempt < attempts:
                time.sleep(delay)

    raise RuntimeError("operation failed after retries") from last_error
```

### Why It Works / Matters

Later distributed-systems courses add exponential backoff, jitter, retry budgets, and idempotency.

# Part 140 — Never `eval()` Untrusted Input

### Core Explanation

`eval()` executes Python expressions. Treating external text as executable code can become arbitrary code execution.

Use a parser for the expected data format instead.

### Example / Code

```python
# Dangerous for untrusted data:
# value = eval(user_supplied_text)

# Prefer:
import json
value = json.loads('{"enabled": true}')
```

### Why It Works / Matters

Data must remain data, not become code.

# Part 141 — `pickle` Security Awareness

### Core Explanation

Python pickle is a Python-specific object serialization mechanism that can execute code during deserialization. Never unpickle data from untrusted or unauthenticated sources.

### Diagram / Mental Model

```text
trusted application data
   ↓ maybe pickle

untrusted network/file input
   ✗ DO NOT unpickle
```

### Why It Works / Matters

Use safer interchange formats such as JSON for untrusted data, combined with validation.

# Part 142 — Path Traversal Awareness

### Core Explanation

If a user controls a filename/path, naive path concatenation may allow escape from an intended directory through `..` or absolute paths.

Path validation must be designed according to the application's trust boundary.

### Example / Code

```python
from pathlib import Path

BASE = Path("reports").resolve()

def safe_report_path(name: str) -> Path:
    candidate = (BASE / name).resolve()

    if BASE not in candidate.parents and candidate != BASE:
        raise ValueError("path escapes report directory")

    return candidate
```

### Why It Works / Matters

Filesystem paths are another form of untrusted input.

# Part 143 — Input Size Limits

### Core Explanation

Validation should consider not only content but size. A 'valid' 10 GB JSON or text input can exhaust memory or storage.

Define limits appropriate to the tool.

### Diagram / Mental Model

```text
External input
  ↓ size check
  ↓ format parse
  ↓ semantic validation
```

### Why It Works / Matters

Availability is part of secure programming.

# Part 144 — Secrets from Environment Variables

### Core Explanation

Environment variables are convenient but not magically secret. They may be visible to process inspection, crash dumps, CI systems, or misconfigured logs.

Use dedicated secret managers for production secrets where available and avoid printing environment dumps.

### Why It Works / Matters

Configuration mechanism and secret protection are separate concerns.

# Part 145 — Least Privilege for Automation

### Core Explanation

Run scripts with the minimum OS/cloud/database permissions required.

Do not solve permission errors by making the process Administrator/root unless the operation genuinely requires it.

### Why It Works / Matters

A compromised or buggy script can only damage what its identity can access.

# Part 146 — Pure Functions Are Easy to Test

### Core Explanation

Functions without external I/O or hidden state are straightforward to verify.

### Example / Code

```python
def free_percent(total: int, free: int) -> float:
    if total <= 0:
        raise ValueError("total must be positive")
    if not 0 <= free <= total:
        raise ValueError("free must be between 0 and total")
    return free / total * 100

assert free_percent(100, 25) == 25.0
```

### Why It Works / Matters

Separate I/O from calculations when practical.

# Part 147 — Assertions for Learning

### Core Explanation

`assert` is useful for tests and internal invariants, but should not be the sole validation mechanism for untrusted input because optimized execution can disable assertions.

### Example / Code

```python
assert classify_cpu(90) == "critical"
```

### Why It Works / Matters

Use explicit validation/raise for runtime input contracts.

# Part 148 — `unittest` Awareness

### Core Explanation

Python's standard library includes `unittest` for organized automated tests.

### Example / Code

```python
import unittest

class TestClassifier(unittest.TestCase):
    def test_critical_boundary(self):
        self.assertEqual(classify_cpu(90), "critical")

if __name__ == "__main__":
    unittest.main()
```

### Why It Works / Matters

You will encounter both standard-library and third-party test frameworks in professional projects.

# Part 149 — Test Normal, Boundary, and Invalid Cases

### Core Explanation

Every decision rule should be tested at normal values, exact boundaries, and invalid values.

### Diagram / Mental Model

```text
normal:
50

boundary:
74.99, 75, 89.99, 90

invalid:
-1, 101, "abc"
```

### Why It Works / Matters

Boundary bugs are common and often invisible in happy-path testing.

# Part 150 — Deterministic Tests

### Core Explanation

A deterministic test produces the same result under controlled inputs.

Time, randomness, network, filesystem state, and environment variables can make tests flaky unless isolated or injected.

### Why It Works / Matters

Flaky tests reduce trust in CI.

# Part 151 — Dependency Injection Awareness

### Core Explanation

Instead of having business logic construct every external dependency internally, pass the dependency in when practical.

This makes tests controllable.

### Example / Code

```python
class Clock:
    def now(self) -> str:
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()

def build_event(clock, message: str) -> dict:
    if not message:
        raise ValueError("message required")
    return {"timestamp": clock.now(), "message": message}
```

### Why It Works / Matters

A fake clock can make time-dependent tests deterministic.

# Part 152 — Fake Dependency Example

### Core Explanation

A fake object provides controlled behavior for testing.

### Example / Code

```python
class FakeClock:
    def now(self) -> str:
        return "2026-01-01T00:00:00+00:00"

event = build_event(FakeClock(), "started")
print(event["timestamp"])
```

### Expected Behavior / Output

```text
2026-01-01T00:00:00+00:00
```

# Part 153 — Debugging with `repr()`

### Core Explanation

`repr()` exposes escape sequences and exact string representation, which is useful when invisible whitespace causes problems.

### Example / Code

```python
value = "prod\n"

print(value)
print(repr(value))
```

### Expected Behavior / Output

```text
prod
'prod\n'
```

### Why It Works / Matters

Invisible whitespace is a common configuration/parser bug.

# Part 154 — Debugger Awareness (`pdb`)

### Core Explanation

Python includes a debugger (`pdb`) that can pause execution, inspect values, step through lines, and inspect the call stack.

Modern IDEs provide richer debugger interfaces, but the underlying debugging ideas are the same.

### Example / Code

```python
import pdb

# pdb.set_trace()
```

### Why It Works / Matters

Use a debugger when prints are insufficient to locate state divergence.

# Part 155 — Profiling Awareness

### Core Explanation

Do not optimize based on intuition alone. Measure where time or memory is spent before changing code for performance.

Python includes tools such as `cProfile` for CPU-time profiling.

### Example / Code

```bash
python -m cProfile your_script.py
```

### Why It Works / Matters

Performance engineering begins with evidence.

# Part 156 — Big-O Awareness in Python

### Core Explanation

Collection choice affects algorithmic cost.

Examples at a high level:
- list membership: generally linear
- set/dict membership by hash: generally near constant average
- sorting: commonly O(n log n)

Real performance also depends on constants, memory, hashing, and workload.

### Diagram / Mental Model

```text
Need fast membership?
list → scan many items
set  → hash lookup
```

### Why It Works / Matters

This links Phase 2 Python to the later Data Structures and Algorithms course.

# Part 157 — `map()` and `filter()` Awareness

### Core Explanation

`map()` transforms values and `filter()` selects values. Comprehensions are often more readable in Python, but you should recognize these built-ins.

### Example / Code

```python
values = [1, 2, 3]

squared = list(map(lambda x: x * x, values))
print(squared)
```

### Expected Behavior / Output

```text
[1, 4, 9]
```

### Why It Works / Matters

Know both styles; choose the clearer one.

# Part 158 — `functools.partial` Awareness

### Core Explanation

`partial()` pre-fills some function arguments, creating a new callable.

### Example / Code

```python
from functools import partial

def connect(host: str, port: int) -> str:
    return f"{host}:{port}"

https_endpoint = partial(connect, port=443)

print(https_endpoint("api.internal"))
```

### Expected Behavior / Output

```text
api.internal:443
```

### Why It Works / Matters

Useful for callbacks and configuration, but avoid cleverness when a named wrapper is clearer.

# Part 159 — Decorators Awareness

### Core Explanation

A decorator wraps or transforms a function/class. They are widely used by web frameworks, test frameworks, and libraries.

At fundamentals level, understand the wrapper idea; deep decorator design can wait.

### Diagram / Mental Model

```text
original function
      ↓ decorated by
wrapper function
      ↓
enhanced behavior
```

### Example / Code

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_call
def hello():
    print("hello")

hello()
```

### Expected Behavior / Output

```text
calling hello
hello
```

### Why It Works / Matters

Later FastAPI and pytest-style frameworks use decorators heavily.

# Part 160 — Context Manager Concept

### Core Explanation

A context manager defines setup/cleanup around a block. Files are the most common example, but locks, database transactions, and temporary resources use the same pattern.

### Diagram / Mental Model

```text
enter context
   ↓
use resource
   ↓
exit context / cleanup
```

### Why It Works / Matters

This pattern makes cleanup reliable even when exceptions occur.

# Part 161 — Separate I/O from Business Logic

### Core Explanation

A maintainable automation tool separates:
- reading external data
- validating data
- domain decisions
- reporting/output
- orchestration

### Diagram / Mental Model

```text
Input Adapter
    ↓
Validation
    ↓
Business Logic
    ↓
Result Model
    ↓
Output Adapter
```

### Why It Works / Matters

Each layer becomes easier to test and replace.

# Part 162 — Layered Small Project Structure

### Core Explanation

Even a small CLI can benefit from modules with clear responsibilities.

### Diagram / Mental Model

```text
infra_reporter/
├─ main.py          orchestration
├─ collectors.py    OS data acquisition
├─ validators.py    validation rules
├─ models.py        dataclasses/enums
├─ reporters.py     JSON/text output
└─ tests/
```

### Why It Works / Matters

Do not split a 20-line script into 20 files; structure should match complexity.

# Part 163 — Configuration Precedence

### Core Explanation

A tool may receive configuration from defaults, config files, environment variables, and CLI flags.

Define which source wins.

### Diagram / Mental Model

```text
lowest priority
defaults
  ↓
config file
  ↓
environment
  ↓
CLI arguments
highest priority
```

### Why It Works / Matters

Undocumented precedence causes operational surprises.

# Part 164 — Idempotency Awareness

### Core Explanation

An idempotent operation can be repeated without causing additional unintended state changes.

Automation frequently gets retried, so repeat-safety matters.

### Diagram / Mental Model

```text
Run once  → desired state
Run twice → same desired state
```

### Example / Code

```python
from pathlib import Path

path = Path("reports")
path.mkdir(parents=True, exist_ok=True)
```

### Why It Works / Matters

Later configuration management, APIs, and distributed systems depend heavily on idempotency.

# Part 165 — Dry-Run Awareness

### Core Explanation

A dry-run mode shows intended changes without applying them.

### Diagram / Mental Model

```text
Input
 ↓
Plan changes
 ↓
--dry-run? yes → display only
           no  → apply
```

### Why It Works / Matters

Useful for destructive or infrastructure automation.

# Part 166 — Structured Result Models

### Core Explanation

Instead of returning ad-hoc strings from deep logic, return structured data and let reporters choose the presentation.

### Example / Code

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class HealthResult:
    hostname: str
    status: str
    warnings: tuple[str, ...]
```

### Why It Works / Matters

Structured results support JSON, text, tests, and future APIs.

# Part 167 — Error Taxonomy

### Core Explanation

Define categories of failure rather than treating every error as identical.

For a CLI:
- configuration/input error
- operational dependency error
- unexpected internal defect
- health warning found

### Diagram / Mental Model

```text
Input error → exit 2
Health warning → exit 1
Success → exit 0
Unexpected defect → traceback/log + nonzero
```

### Why It Works / Matters

Error meaning improves automation and support.

# Part 168 — Observability for a CLI

### Core Explanation

Even a short-lived CLI benefits from:
- structured log context
- clear exit status
- timing
- processed/invalid counts
- version
- output path

### Why It Works / Matters

Operations should know what the tool did and whether it succeeded.

# Part 169 — Final Python Engineering Mental Model

### Core Explanation

A production-oriented Python program is more than syntax.

It combines:
- language semantics
- data modeling
- validation
- functions/modules
- resource management
- error handling
- safe external interaction
- configuration
- logging
- tests
- packaging/environment discipline

### Diagram / Mental Model

```text
External Input
    ↓
Parse
    ↓
Validate
    ↓
Typed / Structured Internal Data
    ↓
Business Logic
    ↓
External Operations
    ↓
Structured Result
    ↓
Logs + Output + Exit Code
```

### Why It Works / Matters

This is the bridge from 'Python syntax' to reliable automation engineering.

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Interpreter and Execution Model

Create:
```python
print("start")
x = 10
print(x / 2)
print("end")
```
Run it. Then create:
1. a syntax error
2. a TypeError
3. a logical calculation error

For each classify the failure and explain exactly when it occurs.

### Lab 2 — Names and Identity

Run:
```python
a = [1, 2]
b = a
c = [1, 2]

print(a == b, a is b)
print(a == c, a is c)
```
Draw the object-reference diagram.

### Lab 3 — Shallow vs Deep Copy

Use:
```python
a = {"ports": [80, 443]}
```
Compare:
```text
b = a
b = a.copy()
b = deepcopy(a)
```
Mutate the nested list and explain each result.

### Lab 4 — Numeric Types

Calculate:
```python
0.1 + 0.2
```
Then repeat with `Decimal("0.1") + Decimal("0.2")`.
Explain why the outputs differ.

### Lab 5 — Unicode Text and Bytes

Encode:
```text
English text
Arabic text
```
to UTF-8 bytes and decode them back.
Then intentionally decode bytes with the wrong encoding and inspect the failure.

### Lab 6 — String Parsing

Parse:
```text
"  WEB-01,10.0.0.10,PROD  "
```
into normalized host, IP, environment.
Then explain why you would not use manual split for arbitrary CSV.

### Lab 7 — Port Validator

Implement:
```python
def read_port(text: str) -> int:
    ...
```
Requirements:
```text
integer
1..65535
clear ValueError
```
Test boundaries and invalid strings.

### Lab 8 — Condition Boundaries

Implement CPU classification:
```text
<75 normal
75..<90 warning
>=90 critical
```
Test:
```text
0, 74.999, 75, 89.999, 90, 100
```

### Lab 9 — List Operations

Create a port list. Practice:
```text
append
extend
pop
sort
sorted
slice
membership
```
Explain which operations mutate.

### Lab 10 — Set Inventory Comparison

Given:
```python
expected = {"web-01", "db-01", "cache-01"}
observed = {"web-01", "db-01", "unknown-01"}
```
Report:
```text
missing
unexpected
present in both
```
using set operations.

### Lab 11 — Dictionary Required vs Optional Fields

Create server dictionaries where `hostname` is required and `role` optional.
Use direct indexing for required fields and `.get()` for optional fields.
Test missing required hostname and explain the resulting KeyError.

### Lab 12 — Nested Configuration Merge

Create:
```text
defaults
environment config
CLI overrides
```
Merge them in precedence order and explain exactly which values win.

### Lab 13 — Comprehensions

Rewrite a normal loop that extracts critical CPU samples using:
```text
list comprehension
set comprehension for environments
dictionary comprehension for initial host statuses
```
Keep each comprehension simple.

### Lab 14 — Iteration Tools

Practice:
```text
range
enumerate
zip
any
all
min
max
sum
```
using a server-health sample.

### Lab 15 — Generator for Large Logs

Write:
```python
def failed_lines(path):
    ...
```
using `yield`.
Compare conceptually with returning a list of every failure from a 10 GB log.

### Lab 16 — Function Contracts

Write a complete function contract for:
```python
parse_host(line: str) -> Host
```
including:
```text
valid input
returned data
possible errors
side effects
```
Then implement it.

### Lab 17 — Mutable Default Bug

Run an intentionally incorrect:
```python
def add_tag(tag, tags=[]):
    ...
```
multiple times.
Observe retained state, then repair with `None`.

### Lab 18 — Scope

Create examples of:
```text
local
global
enclosing
built-in
```
Name resolution.
Then refactor the example to minimize global state.

### Lab 19 — First-Class Function

Create two classifiers and pass one as an argument into:
```python
def evaluate(values, classifier):
    ...
```
Explain why functions can be treated as data.

### Lab 20 — Exception Translation

Implement:
```text
load JSON config
FileNotFoundError → ConfigError
JSONDecodeError → ConfigError
```
using exception chaining.
Print the final traceback once to inspect the cause.

### Lab 21 — Traceback Reading

Intentionally create a 3-function call chain where the lowest function raises ValueError.
Read the traceback from final exception upward and document:
```text
failure line
caller
entry point
```

### Lab 22 — Pathlib

Create:
```text
data/
reports/
```
using `Path`.
Write/read files without manual slash concatenation.
Test from a different working directory.

### Lab 23 — Large File Streaming

Create a synthetic text file with at least 100,000 lines.
Count matching lines by iteration without calling `.read()` on the full file.
Record memory observations if available.

### Lab 24 — JSON Validation

Create a JSON server inventory.
Validate:
```text
top-level list
hostname required
environment dev/test/prod
ports list of valid integers
```
Return all row errors.

### Lab 25 — CSV DictReader

Create a CSV containing a quoted field with a comma.
Show why `split(",")` breaks and `csv.DictReader` succeeds.

### Lab 26 — Atomic Report Write Design

Implement a simple:
```text
write temporary file
replace final report
```
workflow using a disposable directory.
Explain what failure window this reduces.

### Lab 27 — Temporary Directory

Use `TemporaryDirectory()` in a test to create isolated temporary input/output files.
Verify the directory is cleaned afterward.

### Lab 28 — Modules

Split one script into:
```text
main.py
validators.py
reporters.py
```
Make sure importing `validators` does not execute the CLI.

### Lab 29 — Circular Import Diagnosis

Create a small circular import in a disposable lab.
Observe the error/partial initialization behavior.
Refactor shared definitions into a third module.

### Lab 30 — Virtual Environment

Create `.venv`, activate it, and record:
```text
python path
python version
pip/package tool path if available
```
Deactivate and compare.

### Lab 31 — Type Hints

Add type hints to:
```text
parse_port
classify_cpu
load_servers
build_summary
```
Use an editor/static analyzer if available and intentionally introduce one mismatch.

### Lab 32 — Dataclass Inventory Record

Create:
```python
@dataclass(frozen=True)
class Host:
    name: str
    ip: str
    environment: str
```
Parse validated input into `Host` objects rather than dictionaries.

### Lab 33 — Enums

Create a Status enum for:
```text
normal
warning
critical
```
Compare enum values with raw strings in a small report.

### Lab 34 — Counter and defaultdict

Analyze synthetic authentication events:
```text
count failures per user
group source IPs by user
```
using `Counter` and `defaultdict`.

### Lab 35 — Deque

Keep only the last five alert events using:
```python
deque(maxlen=5)
```
Feed ten events and verify bounded memory behavior.

### Lab 36 — Timezone-Aware Events

Generate UTC-aware timestamps using:
```python
datetime.now(timezone.utc)
```
Serialize them with `isoformat()`.
Parse them back.

### Lab 37 — Environment Configuration

Create:
```text
APP_ENV
DEBUG
REGION
MAX_RETRIES
```
Load and validate them centrally.
Test invalid boolean and retry values.

### Lab 38 — IP Address Validation

Use `ipaddress` to validate:
```text
IPv4
IPv6
invalid addresses
membership in network
```
Do not use regex for semantic IP validation.

### Lab 39 — Regex Log Parsing

Parse synthetic log lines using a compiled regex.
Use `fullmatch()` for one validation case and `search()` for one extraction case.
Explain why they differ.

### Lab 40 — File Hashing

Create a configuration file.
Calculate SHA-256.
Modify one character.
Calculate again.
Explain what the hash proves and what it does not prove.

### Lab 41 — Secure Token Generation

Generate tokens with:
```python
secrets.token_urlsafe()
```
Compare the purpose of `secrets` and `random`.
Do not use real credentials.

### Lab 42 — Argparse CLI

Build:
```bash
python main.py --input servers.json --threshold 80 --verbose
```
with help text, required input, typed threshold, and boolean verbose option.

### Lab 43 — Logging

Configure logging.
Generate:
```text
INFO normal lifecycle
WARNING invalid row
ERROR failed file
```
Ensure no secrets are included.

### Lab 44 — Safe Subprocess

Run:
```text
python --version
```
using `subprocess.run([...])`.
Capture:
```text
return code
stdout
stderr
```
Add a timeout.

### Lab 45 — Shell Injection Review

Compare an unsafe shell-string pattern with an argument-list pattern.
Do not execute malicious input.
Explain structurally why shell interpretation creates risk.

### Lab 46 — Testing Pure Logic

Create `unittest` tests for:
```text
port validation
CPU classification
free disk percentage
environment validation
```
Include normal, boundaries, invalids.

### Lab 47 — Fake Clock

Create a `FakeClock` so timestamped event tests produce a deterministic timestamp.
Explain dependency injection.

### Lab 48 — Path Traversal Defense

In a temporary directory, create a helper that only permits report paths under `reports/`.
Test:
```text
valid.txt
nested/result.txt
../escape.txt
absolute outside path
```

### Lab 49 — Mini Performance Experiment

Compare membership checks conceptually/practically between:
```text
large list
large set
```
for repeated lookups.
Do not overinterpret one microbenchmark; explain Big-O and measurement noise.

### Lab 50 — Capstone Build

Build the complete Infrastructure Inventory and Health Reporter described in the Mini Project section below.
Complete all mandatory modules, tests, CLI behavior, logging, safety checks, and documentation.

## 6. Mini Project

# Mini Project — Infrastructure Inventory, Configuration, and Health Reporter

Build a production-oriented Python CLI that inventories a local machine, validates configuration, evaluates health, and produces structured reports.

The project intentionally integrates the entire course:

```text
Python runtime
  ↓
CLI
  ↓
Configuration
  ↓
Collectors
  ↓
Validation
  ↓
Structured models
  ↓
Health rules
  ↓
Reports
  ↓
Logs
  ↓
Exit codes
  ↓
Tests
```

## Required Folder Structure

```text
infra_reporter/
├── pyproject.toml
├── README.md
├── src/
│   └── infra_reporter/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── collectors.py
│       ├── validators.py
│       ├── models.py
│       ├── health.py
│       ├── reporters.py
│       └── errors.py
├── tests/
│   ├── test_validators.py
│   ├── test_health.py
│   ├── test_config.py
│   └── test_reporters.py
└── examples/
    └── config.json
```

A simpler flat layout is acceptable while learning, but you must understand the responsibility of each file.

## Architecture

```text
Shell / CI
    ↓
argparse CLI
    ↓
Configuration Loader
├─ defaults
├─ JSON config
├─ environment
└─ CLI overrides
    ↓
Validated Settings
    ↓
Collectors
├─ hostname
├─ OS
├─ Python version
├─ current user
├─ disk usage
└─ selected safe environment metadata
    ↓
Domain Models
    ↓
Health Evaluation
├─ disk free threshold
├─ configuration validity
└─ optional warning rules
    ↓
Result
    ↓
Reporter
├─ text
└─ JSON
    ↓
stdout / output file
    ↓
Exit Code
```

## Mandatory Data Model

Use dataclasses.

Example:

```python
from dataclasses import dataclass
from enum import Enum

class Status(str, Enum):
    HEALTHY = "healthy"
    WARNING = "warning"

@dataclass(frozen=True)
class DiskInfo:
    total_bytes: int
    free_bytes: int

@dataclass(frozen=True)
class HostInventory:
    hostname: str
    os_name: str
    os_release: str
    python_version: str
    disk: DiskInfo
```

## Mandatory CLI

Support:

```bash
python -m infra_reporter \
  --format json \
  --output reports/host.json \
  --disk-warning-percent 15 \
  --verbose
```

Required options:

```text
--format text|json
--output PATH
--disk-warning-percent N
--verbose
--config PATH
```

## Configuration Precedence

Document and implement:

```text
defaults
  ↓ overridden by
JSON config
  ↓ overridden by
environment variables
  ↓ overridden by
CLI options
```

Every value must be converted and validated centrally.

## Required Collectors

Collect only data that is safe and justified:

```text
hostname
operating-system name
OS release
Python version
current working directory
current user
disk total/free
```

Optional:

```text
selected non-secret environment variables
network-interface awareness
```

Do **not** dump all environment variables because credentials/tokens may exist there.

## Validation

At minimum:

```text
disk warning threshold:
1..99

output format:
text/json

output path:
must remain under an approved output directory when safe-path mode is enabled

config:
JSON object
known fields
correct value types
```

## Health Logic

Example:

```text
free disk percent < warning threshold
→ WARNING

otherwise
→ HEALTHY
```

Keep the calculation pure:

```python
def free_percent(total: int, free: int) -> float:
    ...
```

Then classify separately.

## Report Formats

### Text

```text
Infrastructure Health Report
============================

Hostname: web-01
OS: Linux
Python: 3.x
Disk Free: 18.4%
Status: HEALTHY
```

### JSON

```json
{
  "hostname": "web-01",
  "os": "Linux",
  "python_version": "3.x",
  "disk": {
    "free_percent": 18.4
  },
  "status": "healthy"
}
```

## Logging

Required:

```text
INFO:
startup
input/config selected
report written

WARNING:
health warning
invalid optional record

ERROR:
configuration failure
output failure
```

Never log:

```text
password
token
private key
authorization header
complete environment dump
```

## Exit Codes

Define:

```text
0 = healthy
1 = health warnings found
2 = configuration/input error
3 = operational failure
```

Document them.

## Error Taxonomy

Create custom exception categories if helpful:

```text
ConfigError
CollectionError
ReportError
```

Preserve low-level causes with exception chaining.

## File Safety

For report generation:

```text
approved output directory
        ↓
validate resolved path
        ↓
write temporary file
        ↓
replace final report
```

Use a safe temporary mechanism.

## Tests

At minimum test:

```text
free-percent calculation
total=0
invalid free bytes
threshold boundary
config precedence
invalid environment integer
output-format validation
status classification
JSON report structure
path traversal rejection
```

Use deterministic fixtures.

## Extended Security Requirements

- Do not use `eval`.
- Do not unpickle untrusted data.
- Do not construct shell commands from untrusted strings.
- Do not run as root/Administrator unless necessary.
- Use `secrets`, not `random`, if generating security tokens.
- Limit oversized configuration/input where practical.
- Do not expose credentials in errors or logs.

## Stretch Goals

1. Add CSV report output.
2. Compare two JSON inventory reports.
3. Display changed fields.
4. Hash the report and store the digest.
5. Add plug-in collector awareness without dynamic untrusted imports.
6. Add `--dry-run`.
7. Add `--version`.
8. Add Windows/Linux-specific collectors behind clear interfaces.
9. Add simple performance timing.
10. Add a synthetic authentication-log analyzer subcommand.

## Completion Architecture Review

Be able to explain:

```text
Why is configuration parsed in one place?
Why are collectors separate from validation?
Why is health logic pure?
Why are reporters separate?
Why are exit codes defined?
Why are logs separated from report output?
Why are subprocess arguments lists rather than shell strings?
Why is output path validated?
Why are tests deterministic?
```

If you can answer these questions from your own implementation, you have moved beyond Python syntax into Python engineering.

## 7. Recommended Resources

This Markdown is designed to be sufficient for the Phase 2 learning objectives.

Optional deeper references should come primarily from the official Python documentation:

```text
Python Tutorial
Built-in Functions
Data Model
Standard Library
pathlib
json
csv
argparse
logging
venv
typing
dataclasses
enum
collections
datetime
ipaddress
re
hashlib
secrets
subprocess
unittest
tempfile
```

Useful standards/guidance:

```text
PEP 8 — Python style
Python packaging documentation
```

When using a third-party package, always check its current official documentation, maintenance status, and security posture rather than copying an old tutorial command blindly.

## 8. Certification Relevance

Python is not usually the central exam objective in infrastructure certifications, but it is a major practical multiplier.

### Linux / System Administration

```text
inventory scripts
configuration validation
log processing
filesystem automation
process/subprocess orchestration
```

### Cloud Engineering

```text
cloud SDK automation
resource inventory
cost/security checks
API clients
deployment tooling
configuration generation
```

### DevOps / Platform Engineering

```text
CI helpers
release automation
validation tools
reporting
Git hooks
operational utilities
```

### Cybersecurity

```text
log analysis
IOC processing
hashing
IP/network parsing
security API automation
evidence processing
defensive scanners for owned systems
report generation
```

### Backend / AI Engineering

```text
functions/modules
structured data
type hints
JSON
testing
logging
packaging
configuration
```

This course is also the practical prerequisite for later:
```text
Bash + Python automation
backend development
cloud SDKs
Ansible-related scripting
security automation
AI engineering
```

## 9. Common Mistakes & Best Practices

- **Mistake:** Treating a Python variable as a fixed typed memory box.  
  **Best practice:** Think of names bound to objects; understand mutability and identity.
- **Mistake:** Using `is` for ordinary value comparison.  
  **Best practice:** Use `==`; reserve `is` mainly for identity checks such as `is None`.
- **Mistake:** Assuming assignment copies a list/dictionary.  
  **Best practice:** Understand aliasing; copy only when independent state is required.
- **Mistake:** Using shallow copy without considering nested objects.  
  **Best practice:** Inspect nested ownership; use deep copy only when truly appropriate.
- **Mistake:** Ignoring floating-point approximation.  
  **Best practice:** Use Decimal for exact decimal-domain requirements.
- **Mistake:** Mixing `str` and `bytes` without explicit encode/decode.  
  **Best practice:** Define text encoding boundaries, usually UTF-8 where appropriate.
- **Mistake:** Writing giant nested `if` statements.  
  **Best practice:** Use validation and guard clauses.
- **Mistake:** Using lists for repeated membership checks over large sets.  
  **Best practice:** Use a set/dict when hash lookup semantics match the problem.
- **Mistake:** Writing complicated one-line comprehensions.  
  **Best practice:** Prefer explicit loops for multi-step business logic.
- **Mistake:** Using while loops without a termination guarantee.  
  **Best practice:** Define bounded state or deadline.
- **Mistake:** Forgetting a function return statement.  
  **Best practice:** Write tests and use explicit contracts.
- **Mistake:** Using mutable default arguments.  
  **Best practice:** Use `None` and create a fresh object inside.
- **Mistake:** Relying on mutable global state.  
  **Best practice:** Pass configuration/dependencies explicitly.
- **Mistake:** Catching `Exception` everywhere.  
  **Best practice:** Catch specific expected failures and let unexpected defects remain visible.
- **Mistake:** Swallowing exceptions with `pass`.  
  **Best practice:** Log/recover meaningfully or propagate.
- **Mistake:** Ignoring exception causes.  
  **Best practice:** Use exception chaining when translating failures.
- **Mistake:** Using manual string splitting for CSV/JSON/IP semantics.  
  **Best practice:** Use format/domain-aware parsers.
- **Mistake:** Assuming relative paths are relative to the script.  
  **Best practice:** Understand current working directory; use pathlib intentionally.
- **Mistake:** Reading huge logs with `.read()`.  
  **Best practice:** Stream line by line or use generators.
- **Mistake:** Writing important files directly without considering partial writes.  
  **Best practice:** Use temporary + replace patterns where appropriate.
- **Mistake:** Doing expensive work at import time.  
  **Best practice:** Keep module imports cheap and side-effect-light.
- **Mistake:** Using `sys.path` hacks to repair project structure.  
  **Best practice:** Fix package/import layout.
- **Mistake:** Installing every package globally.  
  **Best practice:** Use virtual environments.
- **Mistake:** Adding dependencies without need.  
  **Best practice:** Prefer standard library and evaluate supply-chain cost.
- **Mistake:** Assuming type hints validate runtime data.  
  **Best practice:** Use explicit validation for external input.
- **Mistake:** Dumping all environment variables for debugging.  
  **Best practice:** Treat environment data as potentially secret.
- **Mistake:** Using regex to validate semantic IP addresses.  
  **Best practice:** Use `ipaddress`.
- **Mistake:** Using `random` for security tokens.  
  **Best practice:** Use `secrets`.
- **Mistake:** Using `eval()` on external data.  
  **Best practice:** Use dedicated parsers.
- **Mistake:** Unpickling untrusted input.  
  **Best practice:** Do not deserialize untrusted pickle data.
- **Mistake:** Building shell commands with user strings.  
  **Best practice:** Use subprocess argument lists and avoid unnecessary shell interpretation.
- **Mistake:** Ignoring subprocess return codes/timeouts.  
  **Best practice:** Check status and bound execution time.
- **Mistake:** Retrying every exception.  
  **Best practice:** Retry only safe, plausibly transient operations with bounded attempts.
- **Mistake:** Using print as the only operational telemetry.  
  **Best practice:** Use logging plus structured output/exit codes.
- **Mistake:** Logging credentials/tokens.  
  **Best practice:** Redact/omit sensitive values.
- **Mistake:** Using assertions as runtime security validation.  
  **Best practice:** Use explicit validation and exceptions.
- **Mistake:** Testing only happy paths.  
  **Best practice:** Test boundaries, invalids, error paths, and regressions.
- **Mistake:** Writing tests that depend on real time/network unnecessarily.  
  **Best practice:** Use fakes/injection and deterministic fixtures.
- **Mistake:** Optimizing code without profiling.  
  **Best practice:** Measure first.
- **Mistake:** Splitting tiny scripts into excessive modules.  
  **Best practice:** Match structure to complexity.
- **Mistake:** Mixing I/O, validation, business logic, and presentation.  
  **Best practice:** Separate responsibilities to improve testability.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the useful high-level execution model for Python?

**Answer:** Source → parse/compile → Python runtime execution.

### Q2. Syntax error vs runtime error?

**Answer:** Syntax error prevents parsing; runtime error occurs after execution reaches a failing operation.

### Q3. What is a logic error?

**Answer:** Program runs but produces behavior/result different from requirements.

### Q4. What does `__name__ == '__main__'` protect?

**Answer:** It separates direct process entry behavior from import behavior.

### Q5. Why are exit codes important?

**Answer:** Shells and CI systems need machine-readable success/failure.

### Q6. stdout vs stderr?

**Answer:** stdout is normal output; stderr is diagnostic/error output.

### Q7. What is a Python variable?

**Answer:** A name bound to an object.

### Q8. What does `==` compare?

**Answer:** Value equality.

### Q9. What does `is` compare?

**Answer:** Object identity.

### Q10. What is mutability?

**Answer:** Whether an object can be changed in place.

### Q11. Why can `alias = original_list` mutate the original?

**Answer:** Both names refer to the same list object.

### Q12. What is a shallow copy?

**Answer:** New outer container that may still share nested objects.

### Q13. When might deepcopy be inappropriate?

**Answer:** For external-resource objects, large graphs, or when shared ownership is intended.

### Q14. Why are lists not normal dictionary keys?

**Answer:** They are mutable and unhashable.

### Q15. Why can 0.1 + 0.2 look imprecise?

**Answer:** Binary floating-point cannot exactly represent many decimal fractions.

### Q16. When use Decimal?

**Answer:** When exact decimal arithmetic is required.

### Q17. What is `None`?

**Answer:** A singleton representing absence of a value.

### Q18. Why use `is None`?

**Answer:** It checks singleton identity explicitly.

### Q19. What is truthiness?

**Answer:** Automatic conversion of values to boolean context.

### Q20. What type is Python text?

**Answer:** `str`, representing Unicode text.

### Q21. How convert text to bytes?

**Answer:** Encode using a specified encoding such as UTF-8.

### Q22. How convert bytes to text?

**Answer:** Decode using the correct encoding.

### Q23. Are strings mutable?

**Answer:** No.

### Q24. What does slicing's stop index mean?

**Answer:** It is excluded.

### Q25. Why normalize external strings?

**Answer:** Remove accidental formatting differences before validation/comparison.

### Q26. Why not parse arbitrary CSV with split(',')?

**Answer:** CSV quoting/escaping can contain commas inside fields.

### Q27. Why use f-strings?

**Answer:** Readable value interpolation/formatting.

### Q28. What is a guard clause?

**Answer:** Early validation/return/raise before normal logic.

### Q29. Why does `elif` order matter?

**Answer:** The first matching branch executes.

### Q30. List vs tuple?

**Answer:** List is mutable; tuple is immutable.

### Q31. When use a set?

**Answer:** Uniqueness and fast membership/set operations.

### Q32. When use a dictionary?

**Answer:** Key-value lookup and structured mappings.

### Q33. Why use direct dictionary indexing for required keys?

**Answer:** Missing required data should fail explicitly.

### Q34. Why use `.get()`?

**Answer:** For genuinely optional keys/defaults.

### Q35. What is a comprehension?

**Answer:** Concise collection construction from iteration/filtering.

### Q36. When should a comprehension be avoided?

**Answer:** When logic becomes complex, side-effectful, or hard to read.

### Q37. What does `enumerate()` do?

**Answer:** Pairs items with a counter/index.

### Q38. What does `zip()` do?

**Answer:** Iterates multiple iterables in parallel.

### Q39. What is an iterable?

**Answer:** Object capable of producing an iterator.

### Q40. What is an iterator?

**Answer:** Stateful object producing successive values until StopIteration.

### Q41. What is a generator?

**Answer:** Lazy iterator typically produced with `yield` or generator expression.

### Q42. Why use generators for logs?

**Answer:** They can process large data with bounded memory.

### Q43. What does `any()` do?

**Answer:** True if at least one element is truthy.

### Q44. What does `all()` do?

**Answer:** True if every element is truthy.

### Q45. Parameter vs argument?

**Answer:** Parameter is declared in function definition; argument is supplied in a call.

### Q46. Why return values instead of always printing?

**Answer:** Returned values are reusable and testable.

### Q47. What does a function return without explicit return?

**Answer:** None.

### Q48. Why are mutable default arguments dangerous?

**Answer:** The same object is reused across calls.

### Q49. What is LEGB?

**Answer:** Local, Enclosing, Global, Built-in name lookup scopes.

### Q50. Why avoid mutable global state?

**Answer:** It creates hidden dependencies and test-order coupling.

### Q51. What does first-class function mean?

**Answer:** Functions can be passed/stored/returned like other objects.

### Q52. When are lambdas useful?

**Answer:** Small simple function expressions such as sort keys.

### Q53. What is a function contract?

**Answer:** Defined inputs, outputs, errors, side effects, and invariants.

### Q54. What is exception chaining?

**Answer:** Preserving a lower-level cause when raising a higher-level exception.

### Q55. Why catch specific exceptions?

**Answer:** Broad catches hide defects and mix unrelated failure categories.

### Q56. What is a traceback?

**Answer:** Call-stack history showing where an exception propagated.

### Q57. Why use pathlib?

**Answer:** Portable readable path manipulation.

### Q58. Why can a relative path fail in CI?

**Answer:** It is resolved from the process working directory, which may differ.

### Q59. Why use `with` for files?

**Answer:** Reliable cleanup/closing.

### Q60. Why stream large files?

**Answer:** Avoid loading all content into memory.

### Q61. What does JSON parsing not guarantee?

**Answer:** Business/schema validity.

### Q62. Why use temporary files for sensitive replacement workflows?

**Answer:** Reduce partial-write/collision risks when designed correctly.

### Q63. What is a Python module?

**Answer:** A Python source module providing definitions under a namespace.

### Q64. What is a package?

**Answer:** A namespace grouping related modules.

### Q65. Why avoid import-time side effects?

**Answer:** Imports should be predictable and testable.

### Q66. What causes circular import problems?

**Answer:** Modules depend on each other during initialization.

### Q67. What is a virtual environment?

**Answer:** Isolated Python project environment for interpreter/package dependencies.

### Q68. Do type hints enforce runtime types automatically?

**Answer:** No.

### Q69. Why use dataclasses?

**Answer:** Concise structured records with clear fields.

### Q70. Why use Enum?

**Answer:** Represent a closed set of named values.

### Q71. What does Counter do?

**Answer:** Counts hashable values.

### Q72. Why use deque(maxlen=N)?

**Answer:** Maintain a bounded recent-value queue.

### Q73. Why prefer timezone-aware timestamps?

**Answer:** Avoid ambiguity across systems/timezones.

### Q74. Why centralize environment parsing?

**Answer:** Consistent conversion, validation, defaults, and error messages.

### Q75. Why use ipaddress instead of regex for IP validation?

**Answer:** It understands actual IP semantics.

### Q76. Search vs fullmatch in regex?

**Answer:** Search finds a matching substring; fullmatch requires the whole text to match.

### Q77. What is ReDoS awareness?

**Answer:** Some regex patterns can consume excessive CPU on crafted input.

### Q78. What does SHA-256 file hashing tell you?

**Answer:** Whether content matches a trusted digest/baseline; not who or why it changed.

### Q79. Why use secrets instead of random for tokens?

**Answer:** secrets uses a source appropriate for security-sensitive randomness.

### Q80. What does argparse provide?

**Answer:** CLI parsing, types, defaults, help, and validation support.

### Q81. Why separate stdout/stderr and logs?

**Answer:** Different consumers need results vs diagnostics.

### Q82. Why use subprocess argument lists?

**Answer:** Avoid unnecessary shell parsing and improve argument safety.

### Q83. Why add subprocess timeout?

**Answer:** External commands can hang.

### Q84. Why are retries dangerous?

**Answer:** They can duplicate side effects or amplify failures if not bounded/safe.

### Q85. Why is eval dangerous on untrusted input?

**Answer:** It executes input as Python expressions/code.

### Q86. Why is untrusted pickle unsafe?

**Answer:** Deserialization can execute code.

### Q87. What is path traversal?

**Answer:** User-controlled paths escape an intended directory.

### Q88. Why impose input-size limits?

**Answer:** Valid-but-huge input can exhaust memory/storage/CPU.

### Q89. Why use least privilege for automation?

**Answer:** Limits damage from defects or compromise.

### Q90. Why are pure functions easy to test?

**Answer:** They depend only on explicit inputs and avoid hidden side effects.

### Q91. What cases should threshold tests include?

**Answer:** Normal, exact boundaries, values around boundaries, invalids.

### Q92. What makes a deterministic test?

**Answer:** Same controlled input/environment produces same result.

### Q93. Why inject a clock?

**Answer:** Tests can control time and avoid flakiness.

### Q94. What does `repr()` help reveal?

**Answer:** Exact string representation including invisible escape characters.

### Q95. Why profile before optimizing?

**Answer:** Identify actual bottlenecks instead of guessing.

### Q96. List vs set membership complexity at a high level?

**Answer:** List is typically linear scan; set is near constant average hash lookup.

### Q97. What is idempotency?

**Answer:** Repeating an operation does not cause additional unintended effects.

### Q98. What is dry-run?

**Answer:** Calculate/display intended changes without applying them.

### Q99. What is configuration precedence?

**Answer:** Defined order deciding which configuration source overrides another.

### Q100. Final Python engineering model?

**Answer:** Parse/validate external input → structured data → clear logic → safe external operations → structured output/logs/exit codes → tests.

## End-of-Module Practice Checklist

- [ ] I can distinguish syntax, runtime, and logic errors.
- [ ] I can explain Python names, identity, equality, and mutability.
- [ ] I understand shallow vs deep copying.
- [ ] I can work intentionally with strings and bytes.
- [ ] I can use each major collection type for the right semantics.
- [ ] I understand iterables, iterators, and generators.
- [ ] I can write functions with clear contracts and type hints.
- [ ] I understand the mutable-default-argument bug.
- [ ] I can read and chain exceptions.
- [ ] I can use pathlib and context managers.
- [ ] I can safely parse JSON and CSV.
- [ ] I can build modules without import-time surprises.
- [ ] I can create and verify a virtual environment.
- [ ] I can use dataclasses and enums appropriately.
- [ ] I can use Counter, deque, datetime, ipaddress, hashlib, and secrets.
- [ ] I can build a real argparse CLI.
- [ ] I can use logging without leaking secrets.
- [ ] I can run subprocesses without unsafe shell concatenation.
- [ ] I know why eval and untrusted pickle are dangerous.
- [ ] I can test boundaries and invalid data.
- [ ] I understand deterministic tests and fake dependencies.
- [ ] I can explain basic Python collection-complexity trade-offs.
- [ ] I can separate I/O, validation, logic, and reporting.
- [ ] I completed all labs.
- [ ] I completed the Infrastructure Inventory and Health Reporter.
