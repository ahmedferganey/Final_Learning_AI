# 1. Topic Title

## Introduction to Programming

Programming is the skill of converting a problem into precise, executable steps. In this learning path it will later support automation, infrastructure tooling, APIs, security scripts, data processing, cloud operations, backend development, and AI.

The central mental model is:

```text
Problem
  ↓
Requirements
  ↓
Input
  ↓
Validation
  ↓
Processing / Decisions
  ↓
Output
  ↓
Testing
  ↓
Debugging / Improvement
```

This module uses Python because its syntax is readable and it is widely used in infrastructure, cloud, DevOps, cybersecurity, backend engineering, and data/AI work.

The goal is not to memorize syntax. The goal is to learn how programs represent data, make decisions, repeat work, organize logic, handle failure, and communicate results.

# 2. Learning Objectives

By the end of this topic, you should be able to:

1. Translate a small problem into input, processing, output, and edge cases.
2. Write pseudocode before implementation.
3. Use variables and fundamental Python data types.
4. Convert and validate user/file input.
5. Use arithmetic, comparison, and boolean operators.
6. Use conditions correctly and reason about branch ordering.
7. Use `for` and `while` loops safely.
8. Use `break`, `continue`, `range`, and `enumerate`.
9. Write reusable functions with parameters and return values.
10. Explain local scope and global-state concerns.
11. Use lists, tuples, sets, and dictionaries.
12. Work with strings using indexing, slicing, normalization, split, and join.
13. Explain mutability and shared references at a foundational level.
14. Handle specific exceptions.
15. Read tracebacks.
16. Read and write text files.
17. Process CSV safely with the standard library.
18. Parse and serialize JSON at a foundational level.
19. Organize code into modules.
20. Use standard-library modules and `pathlib`.
21. Understand command-line arguments conceptually.
22. Apply testing to normal, boundary, and invalid cases.
23. Debug by comparing expected and observed state.
24. Avoid hardcoded secrets and unsafe evaluation of input.
25. Build a complete infrastructure health reporting program.

# 3. Prerequisites

Recommended:

```text
00. Computer Architecture
01. Operating Systems Fundamentals
```

You should be able to:

```text
Create files/folders
Navigate paths
Open a terminal
Run commands
Recognize stdout/stderr
```

No previous programming language is required.

# 4. Core Concepts Explanation

# Part 1 — Programming as Problem Solving

### Core Explanation

Programming is the process of transforming a problem into explicit steps that a computer can execute.

A vague requirement such as "check server health" is not yet a program. You must define what health means, what data is available, what thresholds matter, what should happen when data is missing, and what output is required.

### Code / Visualization

```text
Problem:
"Warn when disk usage is high."

Decomposition:
Input: used_gb, total_gb
Processing: used_gb / total_gb * 100
Decision:
  < 75       -> normal
  75-89.99   -> warning
  >= 90      -> critical
Output: percentage + state
Edge cases:
  total_gb <= 0
  negative values
  non-numeric input
```

### Why It Works / Matters

Correct syntax cannot compensate for incorrect problem definition.

### Practical Use

Use this reasoning pattern before writing automation, API, security, or cloud scripts.

# Part 2 — Input → Processing → Output

### Core Explanation

A beginner-friendly model for almost every small program is Input → Processing → Output. Inputs are values the program receives, processing transforms or evaluates those values, and output communicates the result.

### Code / Visualization

```text
Input:
cpu = 91

Processing:
compare cpu with thresholds

Output:
"critical"
```

### Why It Works / Matters

It separates data acquisition from decision logic and presentation.

### Practical Use

Useful for reports, calculators, log processors, CLI tools, and health checks.

# Part 3 — Edge Cases

### Core Explanation

Edge cases are unusual, boundary, empty, or invalid inputs that expose weaknesses in logic.

### Code / Visualization

```text
Normal:
cpu = 40

Boundary:
cpu = 75
cpu = 90

Invalid:
cpu = -1
cpu = 101
cpu = "high"
```

### Why It Works / Matters

Production failures often happen at boundaries rather than the normal case.

### Practical Use

List edge cases before implementation.

# Part 4 — Algorithm

### Core Explanation

An algorithm is an ordered finite procedure for solving a problem. The algorithm exists independently of Python syntax.

### Code / Visualization

```text
Algorithm:
1. Read CPU usage.
2. Reject values outside 0-100.
3. If CPU >= 90, return critical.
4. Else if CPU >= 75, return warning.
5. Else return normal.
```

### Why It Works / Matters

Separating algorithm design from syntax makes the reasoning transferable to Python, C, JavaScript, or another language.

### Practical Use

Write the algorithm first for unfamiliar tasks.

# Part 5 — Pseudocode

### Core Explanation

Pseudocode expresses an algorithm in structured human-readable steps without requiring exact programming-language syntax.

### Code / Visualization

```text
READ cpu
IF cpu < 0 OR cpu > 100
    ERROR "invalid"
ELSE IF cpu >= 90
    PRINT "critical"
ELSE IF cpu >= 75
    PRINT "warning"
ELSE
    PRINT "normal"
```

### Why It Works / Matters

It keeps attention on logic rather than punctuation.

### Practical Use

Useful before coding a function or troubleshooting incorrect logic.

# Part 6 — Source Code

### Core Explanation

Source code is the human-readable text of a program. Python source files normally use the .py extension.

### Code / Visualization

```text
# hello.py
print("Hello")
```

### Expected Behavior / Output

```text
Hello
```

### Why It Works / Matters

The source is an artifact you can version, review, test, and execute.

### Practical Use

Store source in Git later in the learning path.

# Part 7 — Python Interpreter

### Core Explanation

The Python runtime reads Python source, transforms it into an internal executable representation, and executes the program. At this level, the key point is that the interpreter/runtime is the program that executes your Python code.

### Code / Visualization

```text
python hello.py
```

### Expected Behavior / Output

```text
Hello
```

### Why It Works / Matters

This explains why Python must be installed and why different interpreter environments can behave differently.

### Practical Use

Check the runtime with `python --version` or `python3 --version`.

# Part 8 — Syntax vs Logic

### Core Explanation

Syntax determines whether Python can parse the program. Logic determines whether the program solves the intended problem correctly. A script may be syntactically valid and still be wrong.

### Code / Visualization

```text
used = 80
total = 100

# Syntactically valid but logically wrong:
usage = total / used * 100
print(usage)
```

### Expected Behavior / Output

```text
125.0
```

### Why It Works / Matters

Successful execution is not proof of correctness.

### Practical Use

Tests must check expected values.

# Part 9 — Comments

### Core Explanation

Comments explain intent, constraints, or non-obvious reasoning. They begin with `#` in Python.

### Code / Visualization

```text
# Threshold agreed with operations team.
critical_threshold = 90
```

### Why It Works / Matters

Good comments preserve why a decision exists, while obvious comments add noise.

### Practical Use

Prefer explaining intent rather than restating code.

# Part 10 — Readable Formatting

### Core Explanation

Python code should be formatted consistently. Indentation is part of Python syntax, and readable spacing/naming reduces mistakes.

### Code / Visualization

```text
if cpu >= 90:
    status = "critical"
else:
    status = "normal"
```

### Why It Works / Matters

Readable code is easier to review, test, and secure.

### Practical Use

Use four spaces per indentation level.

# Part 11 — Variables

### Core Explanation

A variable is a name bound to a value.

### Code / Visualization

```text
hostname = "server-01"
cpu = 73
```

### Why It Works / Matters

Names let code refer to data meaningfully.

### Practical Use

Use descriptive names such as `disk_percent`.

# Part 12 — Assignment

### Core Explanation

The `=` operator assigns or reassigns a name.

### Code / Visualization

```text
cpu = 50
cpu = 80
print(cpu)
```

### Expected Behavior / Output

```text
80
```

### Why It Works / Matters

The second assignment changes what `cpu` refers to.

### Practical Use

Do not confuse `=` with equality `==`.

# Part 13 — String (`str`)

### Core Explanation

Strings represent text.

### Code / Visualization

```text
hostname = "web-01"
ip = "10.0.0.10"
```

### Why It Works / Matters

Strings support formatting, parsing, comparison, indexing, and methods.

### Practical Use

Hostnames, paths, and many raw inputs begin as strings.

# Part 14 — Integer (`int`)

### Core Explanation

Integers represent whole numbers.

### Code / Visualization

```text
cpu_count = 8
port = 443
```

### Why It Works / Matters

Use integers when fractional values are not meaningful.

### Practical Use

Counts, indexes, many IDs, and ports.

# Part 15 — Float (`float`)

### Core Explanation

Floats represent floating-point numeric values.

### Code / Visualization

```text
cpu = 72.5
memory_gb = 31.75
```

### Why It Works / Matters

Useful for measurements, but binary floating-point is approximate.

### Practical Use

Percentages, timing, measurements.

# Part 16 — Boolean (`bool`)

### Core Explanation

Booleans represent `True` or `False`.

### Code / Visualization

```text
is_online = True
has_error = False
```

### Why It Works / Matters

Booleans make decision state explicit.

### Practical Use

Names such as `is_valid`, `has_access`, `is_online`.

# Part 17 — `None`

### Core Explanation

`None` represents absence of a value.

### Code / Visualization

```text
result = None
```

### Why It Works / Matters

It is different from zero, False, or an empty string.

### Practical Use

Use when no value exists yet.

# Part 18 — `type()`

### Core Explanation

`type()` shows the runtime type of a value.

### Code / Visualization

```text
cpu = 73
print(type(cpu))
```

### Expected Behavior / Output

```text
<class 'int'>
```

### Why It Works / Matters

Useful when learning and debugging unexpected data.

### Practical Use

Inspect data arriving from files or input.

# Part 19 — Dynamic Typing

### Core Explanation

Python names can refer to values of different types over time.

### Code / Visualization

```text
value = 10
value = "ten"
```

### Why It Works / Matters

Flexible, but changing conceptual meaning can create bugs.

### Practical Use

Keep variable purpose consistent even when Python allows reassignment.

# Part 20 — Type Conversion

### Core Explanation

Use built-ins such as `int()`, `float()`, and `str()` to convert compatible values.

### Code / Visualization

```text
raw = "75.5"
cpu = float(raw)
print(cpu)
```

### Expected Behavior / Output

```text
75.5
```

### Why It Works / Matters

External input is often text.

### Practical Use

Validate conversion errors.

# Part 21 — User Input Is Text

### Core Explanation

The built-in `input()` returns a string even when the user types digits.

### Code / Visualization

```text
raw = input("CPU: ")
print(type(raw))
```

### Expected Behavior / Output

```text
<class 'str'>
```

### Why It Works / Matters

Numeric processing requires explicit conversion.

### Practical Use

Convert with `float()` or `int()` and catch `ValueError`.

# Part 22 — Mutability

### Core Explanation

Mutable objects can be changed in place. Common mutable types include list, dict, and set. Common immutable types include int, float, str, bool, and tuple.

### Code / Visualization

```text
ports = [22, 80]
ports.append(443)

hostname = "WEB-01"
hostname = hostname.lower()
```

### Why It Works / Matters

Mutability affects sharing, function behavior, and bugs.

### Practical Use

Be especially careful when multiple names reference one list or dictionary.

# Part 23 — Shared References

### Core Explanation

Assignment of a mutable object usually creates another reference to the same object rather than an independent copy.

### Code / Visualization

```text
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)
```

### Expected Behavior / Output

```text
[1, 2, 3]
[1, 2, 3]
```

### Why It Works / Matters

This surprises many beginners.

### Practical Use

Use `.copy()` when an independent shallow copy is required.

# Part 24 — Shallow Copy

### Core Explanation

A shallow copy creates a new outer collection while nested mutable values may still be shared.

### Code / Visualization

```text
a = [1, 2]
b = a.copy()
b.append(3)

print(a)
print(b)
```

### Expected Behavior / Output

```text
[1, 2]
[1, 2, 3]
```

### Why It Works / Matters

It avoids accidental outer-list sharing.

### Practical Use

Nested copying is a later topic.

# Part 25 — Arithmetic Operators

### Core Explanation

`+ - * / // % **` perform arithmetic.

### Code / Visualization

```text
a = 10
b = 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)
```

### Why It Works / Matters

Operators encode calculations.

### Practical Use

Disk usage, counters, averages, retry calculations.

# Part 26 — Comparison Operators

### Core Explanation

`== != < <= > >=` compare values and return booleans.

### Code / Visualization

```text
cpu = 80
print(cpu >= 75)
print(cpu == 90)
```

### Expected Behavior / Output

```text
True
False
```

### Why It Works / Matters

Conditions depend on comparison results.

### Practical Use

Threshold logic.

# Part 27 — Equality `==`

### Core Explanation

`==` compares values.

### Code / Visualization

```text
status = "warning"
print(status == "warning")
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

It is different from assignment `=`.

### Practical Use

Compare expected states.

# Part 28 — Identity `is`

### Core Explanation

`is` checks object identity. A common correct use is checking `None`.

### Code / Visualization

```text
value = None
print(value is None)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Value equality and object identity are different ideas.

### Practical Use

Use `is None`; use `==` for ordinary value equality.

# Part 29 — Boolean `and`

### Core Explanation

`and` requires both operands/conditions to be truthy.

### Code / Visualization

```text
cpu = 80
mem = 60
print(cpu >= 75 and mem < 90)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Combines requirements.

### Practical Use

Validation and policy conditions.

# Part 30 — Boolean `or`

### Core Explanation

`or` is truthy when at least one operand is truthy.

### Code / Visualization

```text
cpu = 95
mem = 50
print(cpu >= 90 or mem >= 90)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Useful when any metric can trigger a state.

### Practical Use

Worst-condition logic.

# Part 31 — Boolean `not`

### Core Explanation

`not` reverses truthiness.

### Code / Visualization

```text
is_online = False
print(not is_online)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Expresses negative conditions.

### Practical Use

Use with positive variable names.

# Part 32 — Operator Precedence

### Core Explanation

Operators are evaluated according to precedence; parentheses make intended order explicit.

### Code / Visualization

```text
print(2 + 3 * 4)
print((2 + 3) * 4)
```

### Expected Behavior / Output

```text
14
20
```

### Why It Works / Matters

Incorrect assumptions create logical bugs.

### Practical Use

Use parentheses when readability improves.

# Part 33 — Truthy and Falsy

### Core Explanation

Python interprets values such as `False`, `None`, `0`, empty strings, and empty collections as falsy.

### Code / Visualization

```text
items = []
if not items:
    print("empty")
```

### Expected Behavior / Output

```text
empty
```

### Why It Works / Matters

Python uses truthiness frequently.

### Practical Use

Use explicit checks when zero and missing have different meanings.

# Part 34 — `if` Statement

### Core Explanation

`if` executes an indented block when its condition is truthy.

### Code / Visualization

```text
cpu = 95

if cpu >= 90:
    print("critical")
```

### Expected Behavior / Output

```text
critical
```

### Why It Works / Matters

This is the foundation of decision-making.

### Practical Use

Use conditions to classify data and validate state.

# Part 35 — `elif` and `else`

### Core Explanation

`elif` adds additional mutually exclusive branches; `else` handles the remaining case.

### Code / Visualization

```text
if cpu >= 90:
    status = "critical"
elif cpu >= 75:
    status = "warning"
else:
    status = "normal"
```

### Why It Works / Matters

The first matching branch runs.

### Practical Use

Order thresholds from most specific/highest severity to broader cases.

# Part 36 — Condition Ordering

### Core Explanation

Branch order matters. A broad condition placed before a narrower condition can make later branches unreachable.

### Code / Visualization

```text
# Wrong:
if cpu >= 75:
    status = "warning"
elif cpu >= 90:
    status = "critical"
```

### Why It Works / Matters

`95 >= 75` is already true, so the critical branch never executes.

### Practical Use

Test exact threshold values.

# Part 37 — Nested Conditions

### Core Explanation

Conditions can be nested, but deep nesting makes code difficult to follow.

### Code / Visualization

```text
if is_online:
    if cpu >= 90:
        print("online but critical")
```

### Why It Works / Matters

Nested conditions are sometimes appropriate but can often be simplified with helper functions or guard clauses.

### Practical Use

Prefer readable flow over excessive nesting.

# Part 38 — Guard Clauses

### Core Explanation

A guard clause handles invalid or special cases early and exits before normal logic.

### Code / Visualization

```text
def calculate_usage(used, total):
    if total <= 0:
        raise ValueError("total must be positive")

    return used / total * 100
```

### Why It Works / Matters

Early validation reduces nesting and protects assumptions.

### Practical Use

Use at function boundaries.

# Part 39 — Range Validation

### Core Explanation

Python supports chained comparisons.

### Code / Visualization

```text
if not 0 <= cpu <= 100:
    raise ValueError("cpu must be between 0 and 100")
```

### Why It Works / Matters

This is clearer than separate comparisons for many numeric ranges.

### Practical Use

Percentages, ports, retry counts, thresholds.

# Part 40 — `for` Loop

### Core Explanation

A `for` loop iterates over each item in an iterable.

### Code / Visualization

```text
servers = ["web-01", "db-01"]
for server in servers:
    print(server)
```

### Expected Behavior / Output

```text
web-01
db-01
```

### Why It Works / Matters

Natural for collections.

### Practical Use

Inventories and records.

# Part 41 — Loop Variable

### Core Explanation

The loop variable receives one item at a time.

### Code / Visualization

```text
for port in [22, 80, 443]:
    print(port)
```

### Expected Behavior / Output

```text
22
80
443
```

### Why It Works / Matters

Meaningful names make loops readable.

### Practical Use

Use `port`, `server`, `row`, not `x`.

# Part 42 — `range()`

### Core Explanation

`range()` produces a sequence of integers.

### Code / Visualization

```text
for i in range(3):
    print(i)
```

### Expected Behavior / Output

```text
0
1
2
```

### Why It Works / Matters

Useful for fixed-count repetition.

### Practical Use

Avoid index loops when direct iteration is clearer.

# Part 43 — `enumerate()`

### Core Explanation

`enumerate()` provides an index/count together with each item.

### Code / Visualization

```text
for n, host in enumerate(["web", "db"], start=1):
    print(n, host)
```

### Expected Behavior / Output

```text
1 web
2 db
```

### Why It Works / Matters

Cleaner than manually maintaining a counter.

### Practical Use

Numbered reports.

# Part 44 — `while` Loop

### Core Explanation

A `while` loop continues while its condition remains truthy.

### Code / Visualization

```text
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

### Why It Works / Matters

Useful when iteration count depends on changing state.

### Practical Use

Retries and polling.

# Part 45 — Infinite Loop Risk

### Core Explanation

A while loop may never terminate if its controlling state never changes.

### Code / Visualization

```text
count = 0
# while count < 5:
#     print(count)
#     # count never changes
```

### Why It Works / Matters

Infinite loops consume resources.

### Practical Use

Identify the variable/event that guarantees termination.

# Part 46 — `break`

### Core Explanation

`break` exits the nearest loop.

### Code / Visualization

```text
for port in [22, 80, 443]:
    if port == 80:
        break
    print(port)
```

### Expected Behavior / Output

```text
22
```

### Why It Works / Matters

Stops when a goal or failure condition is reached.

### Practical Use

Search loops.

# Part 47 — `continue`

### Core Explanation

`continue` skips the rest of the current iteration.

### Code / Visualization

```text
for value in [10, -1, 20]:
    if value < 0:
        continue
    print(value)
```

### Expected Behavior / Output

```text
10
20
```

### Why It Works / Matters

Useful for skipping invalid rows.

### Practical Use

Batch processing.

# Part 48 — Accumulator

### Core Explanation

An accumulator keeps a running result.

### Code / Visualization

```text
total = 0
for value in [10, 20, 30]:
    total += value
print(total)
```

### Expected Behavior / Output

```text
60
```

### Why It Works / Matters

Common programming pattern.

### Practical Use

Summaries and totals.

# Part 49 — Counter

### Core Explanation

A counter tracks how many times a condition occurs.

### Code / Visualization

```text
critical = 0
for cpu in [50,95,91]:
    if cpu >= 90:
        critical += 1
print(critical)
```

### Expected Behavior / Output

```text
2
```

### Why It Works / Matters

Useful in reports.

### Practical Use

Count normal/warning/critical systems.

# Part 50 — Nested Loops

### Core Explanation

A loop may run inside another loop, producing combinations.

### Code / Visualization

```text
for host in ["web","db"]:
    for port in [80,443]:
        print(host, port)
```

### Why It Works / Matters

Work grows multiplicatively.

### Practical Use

Use when combinations are truly required.

# Part 51 — Function

### Core Explanation

A function is a named reusable unit of behavior.

### Code / Visualization

```text
def greet():
    print("hello")

greet()
```

### Expected Behavior / Output

```text
hello
```

### Why It Works / Matters

Functions reduce repetition.

### Practical Use

Separate validation, calculation, I/O, and reporting.

# Part 52 — Parameter

### Core Explanation

A parameter is a name in a function definition that receives input.

### Code / Visualization

```text
def greet(name):
    print(f"Hello {name}")
```

### Why It Works / Matters

Parameters make functions reusable.

### Practical Use

Pass hostnames, thresholds, paths.

# Part 53 — Argument

### Core Explanation

An argument is the value supplied to a function call.

### Code / Visualization

```text
greet("web-01")
```

### Expected Behavior / Output

```text
Hello web-01
```

### Why It Works / Matters

Parameter and argument are different terms.

### Practical Use

Read documentation more accurately.

# Part 54 — Return Value

### Core Explanation

`return` sends a result to the caller.

### Code / Visualization

```text
def add(a,b):
    return a+b

result = add(5,7)
print(result)
```

### Expected Behavior / Output

```text
12
```

### Why It Works / Matters

Returned values can be reused and tested.

### Practical Use

Prefer calculation functions that return rather than print.

# Part 55 — Implicit `None` Return

### Core Explanation

A function without an explicit return value returns `None`.

### Code / Visualization

```text
def log(msg):
    print(msg)

result = log("x")
print(result)
```

### Expected Behavior / Output

```text
x
None
```

### Why It Works / Matters

Explains unexpected `None` values.

### Practical Use

Use return behavior intentionally.

# Part 56 — Single Responsibility

### Core Explanation

A good beginner function usually performs one coherent task.

### Code / Visualization

```text
validate_percentage()
classify_usage()
load_servers()
print_report()
```

### Why It Works / Matters

Small functions are easier to test and reason about.

### Practical Use

Do not place all project logic in one function.

# Part 57 — Default Parameter

### Core Explanation

A parameter can have a default value.

### Code / Visualization

```text
def classify(value, warning=75, critical=90):
    ...
```

### Why It Works / Matters

Allows common behavior while supporting configuration.

### Practical Use

Avoid mutable default values until you understand the pitfall.

# Part 58 — Keyword Argument

### Core Explanation

Arguments can be passed by parameter name.

### Code / Visualization

```text
classify(80, warning=70, critical=95)
```

### Why It Works / Matters

Improves readability of configurable calls.

### Practical Use

Threshold configuration.

# Part 59 — Local Scope

### Core Explanation

Names assigned inside a function are normally local to that function.

### Code / Visualization

```text
def demo():
    x = 5
    print(x)
```

### Expected Behavior / Output

```text
5
```

### Why It Works / Matters

Local scope reduces accidental interference.

### Practical Use

Prefer local state.

# Part 60 — Global State Awareness

### Core Explanation

Module-level values are globally accessible within the module, but mutable global state makes behavior harder to test.

### Code / Visualization

```text
threshold = 90

def classify(cpu):
    return cpu >= threshold
```

### Why It Works / Matters

Hidden dependencies reduce clarity.

### Practical Use

Pass configuration as parameters when practical.

# Part 61 — Pure-Style Function

### Core Explanation

A pure-style function calculates output from input without hidden I/O or state changes.

### Code / Visualization

```text
def usage(used,total):
    return used/total*100
```

### Why It Works / Matters

Easy to test.

### Practical Use

Keep calculations separate from file and console operations.

# Part 62 — Docstring

### Core Explanation

A docstring documents a module/function/class.

### Code / Visualization

```text
def classify(value):
    """Return normal, warning, or critical for a percentage."""
    ...
```

### Why It Works / Matters

Communicates contract and intent.

### Practical Use

Document public reusable functions.

# Part 63 — Type Hint Awareness

### Core Explanation

Type hints document expected types and improve editor/static-analysis support.

### Code / Visualization

```text
def classify(value: float) -> str:
    ...
```

### Why It Works / Matters

Useful documentation but not automatic runtime validation.

### Practical Use

Phase 2 will deepen typing.

# Part 64 — List

### Core Explanation

A list is an ordered mutable collection.

### Code / Visualization

```text
ports = [22, 80, 443]
ports.append(8080)
```

### Why It Works / Matters

Useful when order matters and items may change.

### Practical Use

Inventories, rows, results.

# Part 65 — List Indexing

### Core Explanation

List indexes start at zero; negative indexes count from the end.

### Code / Visualization

```text
ports = [22,80,443]
print(ports[0])
print(ports[-1])
```

### Expected Behavior / Output

```text
22
443
```

### Why It Works / Matters

Indexing accesses specific positions.

### Practical Use

Invalid indexes raise `IndexError`.

# Part 66 — List Slicing

### Core Explanation

A slice extracts a range and excludes the stop index.

### Code / Visualization

```text
ports = [22,80,443,8080]
print(ports[1:3])
```

### Expected Behavior / Output

```text
[80, 443]
```

### Why It Works / Matters

Useful for subsets.

### Practical Use

Learn start:stop:step semantics gradually.

# Part 67 — `append()`

### Core Explanation

Adds one item to the end of a list.

### Code / Visualization

```text
alerts = []
alerts.append("db-01")
print(alerts)
```

### Expected Behavior / Output

```text
['db-01']
```

### Why It Works / Matters

Mutates the list.

### Practical Use

Collect results.

# Part 68 — `extend()`

### Core Explanation

Adds each item from another iterable.

### Code / Visualization

```text
ports = [22]
ports.extend([80,443])
print(ports)
```

### Expected Behavior / Output

```text
[22, 80, 443]
```

### Why It Works / Matters

Different from appending the whole list as one nested element.

### Practical Use

Combine lists.

# Part 69 — Tuple

### Core Explanation

A tuple is an ordered immutable collection.

### Code / Visualization

```text
server_key = ("web-01", 443)
```

### Why It Works / Matters

Useful for fixed grouped values.

### Practical Use

Return multiple values or immutable keys.

# Part 70 — Set

### Core Explanation

A set stores unique values and is useful for membership tests.

### Code / Visualization

```text
ports = {22,80,443,443}
print(443 in ports)
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Duplicates collapse.

### Practical Use

Unique IPs, ports, IDs.

# Part 71 — Dictionary

### Core Explanation

A dictionary maps keys to values.

### Code / Visualization

```text
server = {"hostname":"web-01","cpu":75}
```

### Why It Works / Matters

Matches configuration and record-like data.

### Practical Use

CSV/JSON processing.

# Part 72 — Dictionary Access

### Core Explanation

Bracket access retrieves required keys and raises `KeyError` if missing.

### Code / Visualization

```text
print(server["hostname"])
```

### Expected Behavior / Output

```text
web-01
```

### Why It Works / Matters

Good when the key is mandatory.

### Practical Use

Validate schemas.

# Part 73 — `dict.get()`

### Core Explanation

`.get()` retrieves an optional key with an optional default.

### Code / Visualization

```text
role = server.get("role", "unknown")
print(role)
```

### Expected Behavior / Output

```text
unknown
```

### Why It Works / Matters

Avoids exceptions for genuinely optional data.

### Practical Use

Do not hide required-data bugs.

# Part 74 — List of Dictionaries

### Core Explanation

A list of dictionaries is a simple table-like structure.

### Code / Visualization

```text
servers = [{"hostname":"web","cpu":45},{"hostname":"db","cpu":91}]
```

### Why It Works / Matters

Natural representation for CSV/JSON rows.

### Practical Use

Infrastructure inventory.

# Part 75 — String Indexing

### Core Explanation

Strings are sequences and support indexing.

### Code / Visualization

```text
name = "WEB-01"
print(name[0])
```

### Expected Behavior / Output

```text
W
```

### Why It Works / Matters

Useful for character-level operations.

### Practical Use

Prefer higher-level parsing when possible.

# Part 76 — String Slicing

### Core Explanation

Strings support slicing.

### Code / Visualization

```text
name = "server-01"
print(name[:6])
```

### Expected Behavior / Output

```text
server
```

### Why It Works / Matters

Useful for fixed-format extraction.

### Practical Use

Delimiter-based formats are usually better parsed with split or a dedicated parser.

# Part 77 — `lower()` / `upper()`

### Core Explanation

Case-conversion methods return new strings.

### Code / Visualization

```text
print("WEB-01".lower())
```

### Expected Behavior / Output

```text
web-01
```

### Why It Works / Matters

Useful for intentional case-insensitive comparison.

### Practical Use

Do not normalize data where case is meaningful.

# Part 78 — `strip()`

### Core Explanation

Removes leading and trailing whitespace.

### Code / Visualization

```text
line = "  web-01\n"
print(line.strip())
```

### Expected Behavior / Output

```text
web-01
```

### Why It Works / Matters

Essential when reading lines from files.

### Practical Use

Does not remove internal whitespace.

# Part 79 — `split()`

### Core Explanation

Splits a string using a delimiter.

### Code / Visualization

```text
print("web,db,cache".split(","))
```

### Expected Behavior / Output

```text
['web', 'db', 'cache']
```

### Why It Works / Matters

Useful for simple text formats.

### Practical Use

Use `csv` for CSV rather than manual splitting.

# Part 80 — `join()`

### Core Explanation

Joins strings with a separator.

### Code / Visualization

```text
print(",".join(["22","80","443"]))
```

### Expected Behavior / Output

```text
22,80,443
```

### Why It Works / Matters

Clearer than repeated concatenation.

### Practical Use

All items must be strings.

# Part 81 — f-Strings

### Core Explanation

f-strings interpolate values into readable text.

### Code / Visualization

```text
host="db-01"
cpu=91
print(f"{host}: {cpu}%")
```

### Expected Behavior / Output

```text
db-01: 91%
```

### Why It Works / Matters

Readable formatting is important in reports.

### Practical Use

Never include secrets in output.

# Part 82 — String Membership

### Core Explanation

`in` tests whether a substring occurs.

### Code / Visualization

```text
message="Disk ERROR"
print("error" in message.lower())
```

### Expected Behavior / Output

```text
True
```

### Why It Works / Matters

Useful for basic text classification.

### Practical Use

Naive substring checks are not sufficient for complex security detection.

# Part 83 — List Comprehension Awareness

### Core Explanation

A list comprehension creates a list from iteration and optional filtering.

### Code / Visualization

```text
values = [20, 80, 95, 50, 92]
critical = [v for v in values if v >= 90]
print(critical)
```

### Expected Behavior / Output

```text
[95, 92]
```

### Why It Works / Matters

Comprehensions are concise for simple transformations.

### Practical Use

Use a normal loop if the expression becomes difficult to read.

# Part 84 — Input Validation

### Core Explanation

Validation checks type, format, range, and required fields before data reaches normal logic.

### Code / Visualization

```text
if not 0 <= cpu <= 100:
    raise ValueError("cpu must be between 0 and 100")
```

### Why It Works / Matters

External data cannot be assumed correct.

### Practical Use

CLI input, files, APIs, logs.

# Part 85 — Exception

### Core Explanation

An exception represents an abnormal runtime condition.

### Code / Visualization

```text
int("abc")
```

### Expected Behavior / Output

```text
ValueError
```

### Why It Works / Matters

Exceptions communicate failure through the call stack.

### Practical Use

Handle only conditions you understand.

# Part 86 — `try` / `except`

### Core Explanation

Use `try` for code that may fail and `except` for specific errors you can handle.

### Code / Visualization

```text
try:
    cpu = float(raw)
except ValueError:
    print("CPU must be numeric")
```

### Why It Works / Matters

Allows graceful handling of expected invalid input.

### Practical Use

Catch specific exceptions.

# Part 87 — `else` in Exception Handling

### Core Explanation

`else` executes if the try block succeeds.

### Code / Visualization

```text
try:
    cpu=float(raw)
except ValueError:
    print("invalid")
else:
    print(cpu)
```

### Why It Works / Matters

Separates success logic from exception handling.

### Practical Use

Use when it improves clarity.

# Part 88 — `finally` Awareness

### Core Explanation

`finally` runs whether or not an exception occurred.

### Code / Visualization

```text
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

### Why It Works / Matters

Useful for cleanup, though context managers are often preferable for resources.

### Practical Use

Files, locks, connections.

# Part 89 — ValueError

### Core Explanation

Raised when content is inappropriate for an operation.

### Code / Visualization

```text
float("high")
```

### Expected Behavior / Output

```text
ValueError
```

### Why It Works / Matters

Common during input parsing.

### Practical Use

Catch around conversions.

# Part 90 — TypeError

### Core Explanation

Raised when an operation receives incompatible object types.

### Code / Visualization

```text
1 + "2"
```

### Expected Behavior / Output

```text
TypeError
```

### Why It Works / Matters

Often indicates incorrect assumptions about data.

### Practical Use

Inspect source and types.

# Part 91 — NameError

### Core Explanation

Raised when a referenced name does not exist in scope.

### Code / Visualization

```text
print(not_defined)
```

### Expected Behavior / Output

```text
NameError
```

### Why It Works / Matters

Usually typo, order, or scope.

### Practical Use

Read the exact missing name.

# Part 92 — KeyError

### Core Explanation

Raised when a required dictionary key is missing.

### Code / Visualization

```text
server={"hostname":"web"}
print(server["cpu"])
```

### Expected Behavior / Output

```text
KeyError
```

### Why It Works / Matters

May indicate malformed input.

### Practical Use

Validate required columns/keys.

# Part 93 — IndexError

### Core Explanation

Raised when a sequence index is outside its valid range.

### Code / Visualization

```text
ports=[22]
print(ports[4])
```

### Expected Behavior / Output

```text
IndexError
```

### Why It Works / Matters

Often caused by assumptions about collection length.

### Practical Use

Prefer direct iteration.

# Part 94 — ZeroDivisionError

### Core Explanation

Raised when division by zero occurs.

### Code / Visualization

```text
print(50/0)
```

### Expected Behavior / Output

```text
ZeroDivisionError
```

### Why It Works / Matters

Validate denominators before calculations.

### Practical Use

Disk/memory percentage calculations.

# Part 95 — FileNotFoundError

### Core Explanation

Raised when a requested file path does not exist.

### Code / Visualization

```text
open("missing.csv")
```

### Expected Behavior / Output

```text
FileNotFoundError
```

### Why It Works / Matters

Common CLI failure.

### Practical Use

Report the attempted path.

# Part 96 — PermissionError

### Core Explanation

Raised when the operating system denies file access.

### Code / Visualization

```text
open("/protected/path/file","w")
```

### Expected Behavior / Output

```text
PermissionError
```

### Why It Works / Matters

Programming and OS permissions interact.

### Practical Use

Do not solve by running everything as root/admin.

# Part 97 — Broad `except` Risk

### Core Explanation

Catching everything can hide bugs and make failures invisible.

### Code / Visualization

```text
try:
    risky()
except Exception:
    pass
```

### Why It Works / Matters

Silent failure is difficult to debug and unsafe operationally.

### Practical Use

Catch specific exceptions and preserve context.

# Part 98 — Traceback

### Core Explanation

A traceback shows the call stack and the exception type/message.

### Code / Visualization

```text
Traceback ...\nValueError: CPU must be numeric
```

### Why It Works / Matters

It is evidence, not noise.

### Practical Use

Read the final exception first, then follow calls in your code.

# Part 99 — File Paths

### Core Explanation

A file path identifies a filesystem location; relative paths depend on the current working directory.

### Code / Visualization

```text
servers.csv
./data/servers.csv
```

### Why It Works / Matters

Many scripts fail because they assume the wrong working directory.

### Practical Use

Use `pathlib` for portable path operations.

# Part 100 — `open()`

### Core Explanation

`open()` creates a file object.

### Code / Visualization

```text
f = open("servers.txt","r",encoding="utf-8")
f.close()
```

### Why It Works / Matters

Files are operating-system resources.

### Practical Use

Prefer a context manager.

# Part 101 — `with open(...)`

### Core Explanation

A `with` block closes the file automatically when the block exits.

### Code / Visualization

```text
with open("servers.txt",encoding="utf-8") as f:
    data=f.read()
```

### Why It Works / Matters

Safer resource management.

### Practical Use

Standard pattern for file I/O.

# Part 102 — Read Entire File

### Core Explanation

`.read()` loads the remaining file content into memory.

### Code / Visualization

```text
with open("small.txt",encoding="utf-8") as f:
    text=f.read()
```

### Why It Works / Matters

Simple for small files.

### Practical Use

Stream large logs instead.

# Part 103 — Read Line by Line

### Core Explanation

Iterating a file processes one line at a time.

### Code / Visualization

```text
with open("servers.txt",encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Why It Works / Matters

Memory-efficient.

### Practical Use

Logs and inventories.

# Part 104 — Write File

### Core Explanation

Opening with mode `w` creates or overwrites the file.

### Code / Visualization

```text
with open("report.txt","w",encoding="utf-8") as f:
    f.write("status=ok\n")
```

### Why It Works / Matters

`w` is destructive to previous contents.

### Practical Use

Reports.

# Part 105 — Append File

### Core Explanation

Mode `a` appends to the end.

### Code / Visualization

```text
with open("events.txt","a",encoding="utf-8") as f:
    f.write("new event\n")
```

### Why It Works / Matters

Preserves prior text.

### Practical Use

Simple logs, not tamper-proof audit.

# Part 106 — CSV

### Core Explanation

CSV is a tabular text format, but quoting and delimiters make a dedicated parser safer than manual split.

### Code / Visualization

```text
hostname,role,cpu\nweb-01,web,45
```

### Why It Works / Matters

Common exchange format.

### Practical Use

Infrastructure inventory.

# Part 107 — `csv.DictReader`

### Core Explanation

Reads CSV rows as dictionaries keyed by column names.

### Code / Visualization

```text
import csv
with open("servers.csv",newline="",encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["hostname"])
```

### Why It Works / Matters

Column names are clearer than numeric positions.

### Practical Use

Validate required columns.

# Part 108 — JSON Awareness

### Core Explanation

JSON represents objects, arrays, strings, numbers, booleans, and null in a portable text format.

### Code / Visualization

```text
{"hostname":"web-01","cpu":75}
```

### Why It Works / Matters

Common for APIs and cloud tooling.

### Practical Use

Use the `json` module.

# Part 109 — `json.loads()`

### Core Explanation

Parses JSON text into Python objects.

### Code / Visualization

```text
import json
data=json.loads('{"cpu":75}')
print(data["cpu"])
```

### Expected Behavior / Output

```text
75
```

### Why It Works / Matters

Converts serialized data into usable structures.

### Practical Use

Handle malformed JSON.

# Part 110 — `json.dumps()`

### Core Explanation

Serializes Python-compatible objects to JSON text.

### Code / Visualization

```text
import json
print(json.dumps({"status":"ok"}))
```

### Expected Behavior / Output

```text
{"status": "ok"}
```

### Why It Works / Matters

Useful for API/report output.

### Practical Use

Not every Python object is JSON-serializable.

# Part 111 — Module

### Core Explanation

A module is usually a `.py` file containing reusable definitions.

### Code / Visualization

```text
health.py -> classify_usage()
```

### Why It Works / Matters

Organizes programs.

### Practical Use

Separate reusable logic from CLI entrypoint.

# Part 112 — `import`

### Core Explanation

Imports a module so its functionality can be reused.

### Code / Visualization

```text
import math
print(math.sqrt(16))
```

### Expected Behavior / Output

```text
4.0
```

### Why It Works / Matters

Avoid rewriting functionality that already exists.

### Practical Use

Use the standard library first.

# Part 113 — Standard Library

### Core Explanation

Python ships with modules such as `csv`, `json`, `pathlib`, `argparse`, `logging`, `datetime`, `statistics`, and `ipaddress`.

### Code / Visualization

```text
import csv
import json
from pathlib import Path
```

### Why It Works / Matters

Reduces unnecessary dependencies.

### Practical Use

Automation and reporting.

# Part 114 — `pathlib` Awareness

### Core Explanation

`Path` provides readable path composition and inspection.

### Code / Visualization

```text
from pathlib import Path
path=Path("data")/"servers.csv"
print(path)
```

### Expected Behavior / Output

```text
data/servers.csv
```

### Why It Works / Matters

More portable than hand-building path strings.

### Practical Use

CLI tools.

# Part 115 — `__name__` Guard

### Core Explanation

The `if __name__ == '__main__'` pattern separates importable definitions from direct script execution.

### Code / Visualization

```text
def main():
    print("run")

if __name__ == "__main__":
    main()
```

### Expected Behavior / Output

```text
run
```

### Why It Works / Matters

Makes modules reusable.

### Practical Use

Standard CLI structure.

# Part 116 — Command-Line Arguments Awareness

### Core Explanation

Programs can receive values from the command line rather than interactive input.

### Code / Visualization

```text
python report.py --input servers.csv
```

### Why It Works / Matters

Better for automation and CI.

### Practical Use

Use `argparse` later.

# Part 117 — Testing Mindset

### Core Explanation

For every function, identify normal, boundary, invalid, and empty cases.

### Code / Visualization

```text
0 -> normal
74.9 -> normal
75 -> warning
90 -> critical
101 -> error
```

### Why It Works / Matters

A program that only works for the happy path is incomplete.

### Practical Use

Write expected cases before coding.

# Part 118 — Assertion

### Core Explanation

`assert` checks an assumption and is useful for simple learning/tests.

### Code / Visualization

```text
assert classify_usage(90) == "critical"
```

### Why It Works / Matters

Turns expected behavior into executable evidence.

### Practical Use

Do not use assertions as the only validation of untrusted runtime data.

# Part 119 — Boundary Testing

### Core Explanation

Test exactly at and around thresholds.

### Code / Visualization

```text
74.9, 75, 89.99, 90
```

### Why It Works / Matters

Catches off-by-one and comparison mistakes.

### Practical Use

Threshold functions.

# Part 120 — Invalid-Input Testing

### Core Explanation

Tests should include wrong formats, ranges, and missing data.

### Code / Visualization

```text
-1, 101, "abc", ""
```

### Why It Works / Matters

Real input is imperfect.

### Practical Use

Batch processing must define row-level behavior.

# Part 121 — Regression Test Awareness

### Core Explanation

When a bug is fixed, add a test that would fail if the bug returns.

### Code / Visualization

```text
assert classify_usage(90) == "critical"
```

### Why It Works / Matters

Prevents repeated regressions.

### Practical Use

Build a test suite over time.

# Part 122 — Debugging with Print

### Core Explanation

Temporary print statements reveal actual variable values and execution flow.

### Code / Visualization

```text
print("DEBUG cpu=", cpu)
```

### Why It Works / Matters

Simple and useful for beginners.

### Practical Use

Remove or replace with logging later.

# Part 123 — Debugger Mindset

### Core Explanation

Debugging is evidence collection: compare expected state with observed state at the first point they diverge.

### Code / Visualization

```text
Expected cpu: 90\nObserved cpu: "90"
```

### Why It Works / Matters

Guessing leads to random changes.

### Practical Use

Inspect values, types, and branch paths.

# Part 124 — Logging Awareness

### Core Explanation

Operational scripts benefit from consistent logs rather than unstructured prints.

### Code / Visualization

```text
import logging
logging.info("processed server")
```

### Why It Works / Matters

Logs support troubleshooting and automation.

### Practical Use

Do not log credentials or sensitive values.

# Part 125 — Hardcoded Secret Risk

### Core Explanation

Credentials in source may leak through Git history, packages, screenshots, or logs.

### Code / Visualization

```text
api_key = "DO_NOT_PUT_REAL_SECRET_HERE"
```

### Why It Works / Matters

Deleting a secret later may not remove it from history.

### Practical Use

Use environment variables or secret managers later.

# Part 126 — External Input as Trust Boundary

### Core Explanation

User input, files, API responses, and command-line arguments are external data and require validation.

### Code / Visualization

```text
CSV/API/user input -> validate -> internal logic
```

### Why It Works / Matters

Reliability and security both depend on validation.

### Practical Use

Never execute external text as code.

# Part 127 — `eval()` Risk Awareness

### Core Explanation

`eval()` executes Python expressions and must not be used on untrusted input.

### Code / Visualization

```text
eval(user_input)  # unsafe for untrusted data
```

### Why It Works / Matters

Untrusted code execution can become a security vulnerability.

### Practical Use

Use dedicated parsers such as `json.loads()` instead.

# Part 128 — Readable Code over Clever Code

### Core Explanation

Shorter code is not automatically better. Readability, correctness, testability, and maintainability matter.

### Code / Visualization

```text
clear function names + simple branches
```

### Why It Works / Matters

Code is read more often than written.

### Practical Use

Optimize only after measuring a real need.

# 5. Hands-on Lab / Practical Exercises

## Lab 1 — Environment Check

Run:

```bash
python --version
```

or:

```bash
python3 --version
```

Create `hello.py`:

```python
print("Phase 1 programming lab")
```

Expected:

```text
Phase 1 programming lab
```

Explain the relationship:

```text
source file → Python interpreter → process → stdout
```

---

## Lab 2 — Design Before Coding

Problem:

```text
Calculate disk usage percentage.
```

Before writing Python, write:

```text
Inputs
Processing
Outputs
Invalid inputs
Boundary cases
```

Then implement it.

---

## Lab 3 — Variables and Types

```python
hostname = "web-01"
cpu_count = 8
memory_gb = 32.0
is_online = True

for value in [hostname, cpu_count, memory_gb, is_online]:
    print(value, type(value))
```

Explain each type.

---

## Lab 4 — Type Conversion

```python
raw = "75.5"
cpu = float(raw)

print(cpu)
print(type(cpu))
```

Then test:

```python
raw = "high"
```

Read the traceback.

---

## Lab 5 — Arithmetic

```python
used_gb = 76
total_gb = 100

usage_percent = used_gb / total_gb * 100

print(f"{usage_percent:.1f}%")
```

Expected:

```text
76.0%
```

Add validation for `total_gb <= 0`.

---

## Lab 6 — Resource Classification

```python
def classify_usage(value):
    if not 0 <= value <= 100:
        raise ValueError("usage must be between 0 and 100")

    if value >= 90:
        return "critical"
    elif value >= 75:
        return "warning"
    else:
        return "normal"
```

Test:

```text
0
20
74.9
75
89.99
90
100
-1
101
```

---

## Lab 7 — Find a Logic Bug

Test this incorrect logic:

```python
if cpu >= 75:
    status = "warning"
elif cpu >= 90:
    status = "critical"
```

Use:

```text
cpu = 95
```

Explain why it is wrong and fix it.

---

## Lab 8 — Boolean Logic

Given:

```python
cpu = 85
memory = 92
```

Create:

```text
critical if either >= 90
warning if either >= 75
otherwise normal
```

Test different combinations.

---

## Lab 9 — for Loop

```python
servers = ["web-01", "db-01", "cache-01"]

for server in servers:
    print(server)
```

Then number the output using `enumerate`.

---

## Lab 10 — while Loop

```python
attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
```

Explain exactly why it stops.

---

## Lab 11 — break and continue

```python
values = [50, -1, 80, 95]
```

Requirements:

```text
skip negative values
stop when first critical value is found
```

Use `continue` and `break`.

---

## Lab 12 — Functions

```python
def calculate_usage(used, total):
    if total <= 0:
        raise ValueError("total must be positive")

    return used / total * 100
```

Test:

```text
0/100
50/100
100/100
50/0
```

---

## Lab 13 — Return vs Print

Write two versions:

```text
Version A:
function prints result

Version B:
function returns result
caller prints result
```

Explain why Version B is usually more reusable.

---

## Lab 14 — Default Parameters

Modify:

```python
def classify_usage(value, warning=75, critical=90):
    ...
```

Test with:

```text
default thresholds
warning=70
critical=95
```

---

## Lab 15 — Lists

```python
ports = [22, 80, 443]

ports.append(8080)

print(ports)
print(ports[0])
print(ports[-1])
print(ports[1:3])
```

Predict output before running.

---

## Lab 16 — Shared Reference Bug

```python
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)
```

Explain why both contain `3`.

Then fix using:

```python
b = a.copy()
```

---

## Lab 17 — Sets

```python
ports = {22, 80, 443, 443}

print(ports)
print(443 in ports)
```

Explain uniqueness and membership.

---

## Lab 18 — Dictionaries

```python
server = {
    "hostname": "db-01",
    "ip": "10.0.0.20",
    "cpu": 91,
}

server["status"] = classify_usage(server["cpu"])

for key, value in server.items():
    print(key, value)
```

---

## Lab 19 — List of Dictionaries

```python
servers = [
    {"hostname": "web-01", "cpu": 45},
    {"hostname": "db-01", "cpu": 91},
    {"hostname": "app-01", "cpu": 79},
]
```

Print:

```text
web-01: normal
db-01: critical
app-01: warning
```

---

## Lab 20 — String Normalization

```python
host = "  WEB-01\n"

normalized = host.strip().lower()

print(normalized)
```

Expected:

```text
web-01
```

Explain both methods.

---

## Lab 21 — split and join

```python
line = "web-01,10.0.0.10,443"

parts = line.split(",")

print(parts)
print(" | ".join(parts))
```

Explain why real CSV should use `csv`.

---

## Lab 22 — Interactive Input Validation

```python
raw = input("CPU usage: ")

try:
    cpu = float(raw)
except ValueError:
    print("CPU usage must be numeric")
else:
    if not 0 <= cpu <= 100:
        print("CPU must be between 0 and 100")
    else:
        print(classify_usage(cpu))
```

Test:

```text
50
75
90
-1
101
abc
empty input
```

---

## Lab 23 — Exception Types

Create isolated examples for:

```text
ValueError
TypeError
NameError
KeyError
IndexError
ZeroDivisionError
FileNotFoundError
```

For each, record:

```text
exception type
line number
root cause
fix
```

---

## Lab 24 — Read a Text File

Create `servers.txt`:

```text
web-01
db-01
cache-01
```

Read:

```python
with open("servers.txt", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

---

## Lab 25 — Write a Report

```python
report = [
    "web-01: normal",
    "db-01: critical",
]

with open("report.txt", "w", encoding="utf-8") as file:
    for line in report:
        file.write(line + "\n")
```

Verify the file.

---

## Lab 26 — CSV Reader

Create:

```text
hostname,role,cpu
web-01,web,45
db-01,database,91
app-01,application,79
```

Read:

```python
import csv

with open("servers.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cpu = float(row["cpu"])
        print(row["hostname"], classify_usage(cpu))
```

---

## Lab 27 — Invalid CSV Row

Add:

```text
bad-01,test,not-a-number
```

The program must:

```text
report the invalid hostname
continue processing later rows
not crash the full batch
```

---

## Lab 28 — Missing CSV Field

Add a row with empty CPU.

Handle separately:

```text
missing value
non-numeric value
out-of-range value
```

Do not silently convert all failures into one generic message.

---

## Lab 29 — JSON Parsing

```python
import json

raw = '''
{
  "hostname": "web-01",
  "cpu": 70,
  "ports": [80, 443]
}
'''

server = json.loads(raw)

print(server["hostname"])
print(server["ports"])
```

---

## Lab 30 — JSON Output

```python
import json

result = {
    "hostname": "db-01",
    "status": "critical",
}

print(json.dumps(result, indent=2))
```

Explain serialization.

---

## Lab 31 — pathlib

```python
from pathlib import Path

path = Path("data") / "servers.csv"

print(path)
print(path.exists())
```

Create the directory and file, then rerun.

---

## Lab 32 — Create a Module

Create:

```text
health.py
main.py
```

`health.py`:

```python
def classify_usage(value):
    if not 0 <= value <= 100:
        raise ValueError("invalid usage")
    if value >= 90:
        return "critical"
    if value >= 75:
        return "warning"
    return "normal"
```

`main.py`:

```python
from health import classify_usage

print(classify_usage(90))
```

---

## Lab 33 — `__name__` Guard

```python
def main():
    print("program started")

if __name__ == "__main__":
    main()
```

Import the module from another script and observe the difference.

---

## Lab 34 — Assertions and Boundaries

```python
assert classify_usage(0) == "normal"
assert classify_usage(74.9) == "normal"
assert classify_usage(75) == "warning"
assert classify_usage(89.99) == "warning"
assert classify_usage(90) == "critical"
assert classify_usage(100) == "critical"
```

Add tests for invalid values.

---

## Lab 35 — Infrastructure Health Reporter

Create:

```text
hostname,ip,cpu_percent,memory_percent,disk_percent
web-01,10.0.0.10,45,50,60
db-01,10.0.0.20,91,70,82
bad-01,10.0.0.30,abc,20,30
```

Use separate functions:

```text
parse_percentage()
classify_usage()
worst_status()
load_servers()
build_summary()
print_report()
```

Do not place all logic inside one large function.

# 6. Mini Project

## Mini Project — Infrastructure Health Reporter

Build a command-line Python program that reads:

```text
hostname,ip,cpu_percent,memory_percent,disk_percent
```

from CSV.

### Processing Flow

```text
CSV
 ↓
Read Row
 ↓
Validate Required Fields
 ↓
Parse Percentages
 ↓
Classify CPU / Memory / Disk
 ↓
Determine Worst Overall State
 ↓
Store Result
 ↓
Continue to Next Row
 ↓
Sort / Summarize
 ↓
Print and Write Report
```

### Required Validation

Every percentage must be:

```text
present
numeric
>= 0
<= 100
```

### Classification

```text
< 75       normal
75-89.99   warning
>= 90      critical
```

### Overall State

The overall server state equals its worst metric.

Example:

```text
CPU      normal
Memory   warning
Disk     critical

Overall  critical
```

### Suggested Folder Structure

```text
infrastructure-health-reporter/
├── main.py
├── health.py
├── io_utils.py
├── data/
│   └── servers.csv
├── output/
│   └── report.txt
└── tests/
    └── test_health.py
```

### Required Functions

```python
def parse_percentage(raw_value):
    ...

def classify_usage(value):
    ...

def worst_status(*statuses):
    ...

def load_servers(path):
    ...

def build_summary(results):
    ...

def print_report(results, summary):
    ...
```

### Expected Output

```text
Infrastructure Health Report
============================

web-01 (10.0.0.10)
CPU:      45.0% normal
Memory:   50.0% normal
Disk:     60.0% normal
Overall:  normal

db-01 (10.0.0.20)
CPU:      91.0% critical
Memory:   70.0% normal
Disk:     82.0% warning
Overall:  critical

bad-01
ERROR: invalid CPU value 'abc'

Summary
-------
Normal:   1
Warning:  0
Critical: 1
Invalid:  1
```

### Reliability Requirements

The program must:

```text
continue after one invalid row
identify the affected hostname
identify the invalid field
catch only expected input errors
avoid silent failure
```

### Testing Requirements

Test:

```text
0
74.9
75
89.99
90
100
-1
101
non-numeric
empty
mixed metric states
```

### Stretch Goals

1. Write a text report.
2. Write JSON output.
3. Sort critical servers first.
4. Add timestamp.
5. Add command-line arguments with `argparse`.
6. Add configurable thresholds.
7. Add logging.
8. Add unit tests.
9. Add hostname/role filtering.
10. Return a non-zero process exit code when critical systems exist.

### Security Requirements

Do not:

```text
hardcode credentials
log secrets
execute CSV content
use eval() on external input
silently ignore malformed data
```

# 7. Recommended Resources

This Markdown is designed to be self-contained for Phase 1.

For deeper Python study, the preferred optional references are the official Python documentation:

```text
Python Tutorial
Built-in Functions
Standard Library
csv
json
pathlib
argparse
logging
```

Phase 2 — Python Programming Fundamentals will deepen syntax, data structures, functions, modules, object-oriented concepts, testing, tooling, and automation.

# 8. Certification Relevance

Programming fundamentals support nearly every later area.

## Cloud / DevOps

```text
Automation scripts
Cloud SDK usage
API clients
CI/CD utilities
Configuration validation
Infrastructure reporting
```

## System Administration

```text
Inventory
Health checks
File processing
User/report automation
Log processing
```

## Cybersecurity

```text
Log parsing
IOC processing
Security API automation
Evidence processing
Detection helpers
Defensive tooling
```

## Backend / AI

```text
Functions
Validation
Collections
JSON
Modules
Testing
Debugging
```

# 9. Common Mistakes & Best Practices

## Common Mistakes

- Writing code before understanding the problem.
- Copying examples without modifying and testing them.
- Confusing `=` and `==`.
- Ordering thresholds incorrectly.
- Assuming `input()` returns a number.
- Trusting external data.
- Using one huge function.
- Printing from every calculation function instead of returning values.
- Catching every exception broadly.
- Ignoring tracebacks.
- Using unclear variable names.
- Accidentally sharing mutable lists/dictionaries.
- Assuming assignment copies mutable values.
- Manually parsing real CSV with `split(",")`.
- Loading huge files entirely into memory.
- Hardcoding credentials.
- Logging sensitive values.
- Using `eval()` on untrusted input.
- Testing only normal values.
- Ignoring exact boundary values.
- Adding third-party dependencies before checking the standard library.
- Optimizing before correctness.

## Best Practices

- Decompose the problem first.
- Write pseudocode.
- List edge cases.
- Use descriptive names.
- Use small focused functions.
- Return reusable values.
- Validate external input.
- Catch specific exceptions.
- Preserve useful error context.
- Read tracebacks carefully.
- Use `with` for files.
- Use `csv` for CSV.
- Use `json` for JSON.
- Use `pathlib` for paths where practical.
- Keep secrets outside source code.
- Test normal, boundary, and invalid cases.
- Add a regression test after fixing a bug.
- Prefer readable code over clever code.
- Use the standard library before adding dependencies.

# 10. Self-Assessment Questions (with short answers)

1. **What is programming?**  
   Converting a problem into precise executable instructions.

2. **What are the three basic parts of a simple computational problem?**  
   Input, processing, and output.

3. **What is an edge case?**  
   Boundary, empty, unusual, or invalid input that may reveal a bug.

4. **What is an algorithm?**  
   Ordered finite steps for solving a problem.

5. **Why use pseudocode?**  
   To reason about logic before exact syntax.

6. **What is source code?**  
   Human-readable program text.

7. **What executes Python code?**  
   The Python interpreter/runtime.

8. **Syntax vs logic?**  
   Syntax is language grammar; logic is whether the solution behaves correctly.

9. **What is a variable?**  
   A name bound to a value/object.

10. **What does `=` do?**  
    Assignment.

11. **What does `==` do?**  
    Value equality comparison.

12. **What is a string?**  
    Text value of type `str`.

13. **What is an integer?**  
    Whole-number value of type `int`.

14. **What is a float?**  
    Floating-point numeric value.

15. **What is a boolean?**  
    `True` or `False`.

16. **What does `None` represent?**  
    Absence of a value.

17. **What does `type()` do?**  
    Shows the runtime type of an object.

18. **What type does `input()` return?**  
    `str`.

19. **Why is type conversion needed?**  
    External text often must become numeric data.

20. **What is mutability?**  
    Whether an object can be changed in place.

21. **Why can `b = a` be surprising for lists?**  
    Both names can reference the same mutable list.

22. **How can you create a shallow list copy?**  
    `a.copy()`.

23. **What does `/` do?**  
    Division producing a floating-point result.

24. **What does `//` do?**  
    Floor division.

25. **What does `%` do?**  
    Remainder/modulo.

26. **What does `and` mean?**  
    Both conditions must be truthy.

27. **What does `or` mean?**  
    At least one condition is truthy.

28. **What does `not` do?**  
    Inverts truthiness.

29. **Why does branch order matter?**  
    The first matching branch executes.

30. **What is a guard clause?**  
    Early handling of invalid/special cases.

31. **When do you use a `for` loop?**  
    To iterate through items.

32. **When do you use a `while` loop?**  
    To repeat while a condition remains true.

33. **What does `break` do?**  
    Exits the nearest loop.

34. **What does `continue` do?**  
    Skips to the next iteration.

35. **What does `enumerate()` provide?**  
    A count/index and the item.

36. **What is a function?**  
    Named reusable behavior.

37. **Parameter vs argument?**  
    Parameter is declared by function; argument is supplied at call time.

38. **What does `return` do?**  
    Sends a result to the caller.

39. **What does a function return without explicit return?**  
    `None`.

40. **Why prefer small functions?**  
    They are easier to understand, reuse, test, and debug.

41. **What is a list?**  
    Ordered mutable collection.

42. **What is a tuple?**  
    Ordered immutable collection.

43. **What is a set?**  
    Collection of unique values.

44. **What is a dictionary?**  
    Mapping from keys to values.

45. **What does `.get()` do?**  
    Reads a dictionary key with optional default.

46. **What does `.strip()` do?**  
    Removes leading/trailing whitespace.

47. **What does `.split()` do?**  
    Divides a string into pieces.

48. **What does `.join()` do?**  
    Combines strings using a separator.

49. **Why use f-strings?**  
    Clear interpolation/formatting.

50. **What is input validation?**  
    Checking external data against expected requirements.

51. **What is an exception?**  
    Runtime signal describing an abnormal condition.

52. **Why catch specific exceptions?**  
    Broad catches can hide real defects.

53. **What is a traceback?**  
    Information showing where an exception propagated.

54. **Why use `with open(...)`?**  
    It manages closing the file automatically.

55. **Why use `csv.DictReader`?**  
    It correctly parses CSV and exposes named columns.

56. **What is JSON?**  
    Portable structured text format used heavily by APIs and tools.

57. **What is a module?**  
    Python file containing reusable definitions.

58. **Why use the standard library first?**  
    It reduces unnecessary dependencies and often already solves common tasks.

59. **What is boundary testing?**  
    Testing exactly at and around thresholds.

60. **What is the most important beginner habit?**  
    Define the problem, assumptions, and edge cases before writing code.
