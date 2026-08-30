# Data Structures and Algorithms

> **Phase 2 — Programming Foundations**

This version is intentionally example-driven. Every major concept includes code, execution reasoning, and practical infrastructure/security-oriented examples. Do not only read the code: type it, change it, break it, and repair it.

## 1. Topic Title

**Data Structures and Algorithms**

## 2. Learning Objectives

- Reason about common time/space complexity classes.
- Choose lists, sets, dictionaries, stacks, queues, heaps, trees, and graphs by required operation.
- Implement binary search, BFS, DFS, recursion, and educational sorting.
- Benchmark design choices.
- Apply structures to cloud/security scenarios.

## 3. Prerequisites

- Python Programming Fundamentals.
- Basic functions, loops, collections, and OOP.

## 4. Core Concepts Explanation

### 1. Big-O Through Concrete Examples

Big-O describes how resource use grows with input size. Start with concrete code.

O(1):

```python
def first(items):
    return items[0]
```

Whether the list has 10 or 10 million elements, indexing one known position is constant-time in a dynamic array.

O(n):

```python
def contains(items, target):
    for item in items:
        if item == target:
            return True
    return False
```

Worst case examines every item.

O(n²):

```python
def all_pairs(items):
    pairs = []
    for a in items:
        for b in items:
            pairs.append((a, b))
    return pairs
```

Doubling `n` roughly quadruples pair count.

Big-O is a scaling model, not exact runtime. Constants, hardware, cache locality, interpreter overhead, and input distribution still matter.

### 2. Arrays / Python Lists

Python lists behave like dynamic arrays.

```python
hosts = ["web-01", "db-01", "cache-01"]
print(hosts[1])        # O(1) indexed access
hosts.append("mq-01") # amortized O(1)
```

Middle insertion shifts elements:

```python
hosts.insert(1, "api-01")  # O(n)
```

Unsorted lookup is linear:

```python
"db-01" in hosts  # O(n)
```

Use lists when ordered iteration and append/index operations dominate.

### 3. Sets and Hash Maps in Real Work

Suppose you process 500,000 log lines and repeatedly ask whether a source IP is blocked.

List approach:

```python
blocked = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
if source_ip in blocked:
    ...
```

Set approach:

```python
blocked = {"10.0.0.1", "10.0.0.2", "10.0.0.3"}
if source_ip in blocked:
    ...
```

Average set membership is typically treated as O(1), making it a much better conceptual choice for repeated membership checks.

Dictionary for indexed records:

```python
assets_by_id = {
    "srv-1001": {"hostname": "web-01", "criticality": "high"},
    "srv-1002": {"hostname": "db-01", "criticality": "critical"},
}
print(assets_by_id["srv-1002"])
```

### 4. Stack: LIFO

A stack is Last-In, First-Out.

```python
stack = []
stack.append("task-a")
stack.append("task-b")
print(stack.pop())  # task-b
```

Balanced brackets:

```python
def balanced(text: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

This is the same structural idea behind expression parsing and depth-first traversal.

### 5. Queue / Deque: FIFO

A queue is First-In, First-Out. Use `collections.deque` for efficient operations at both ends.

```python
from collections import deque

queue = deque(["job-1", "job-2"])
queue.append("job-3")
print(queue.popleft())  # job-1
```

Avoid repeatedly doing `list.pop(0)` on large lists because all remaining elements must shift.

Operational use case: a simple job dispatcher processes tasks in arrival order.

### 6. Linked Lists

A linked list stores nodes connected by references.

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

head = Node("web-01", Node("db-01", Node("cache-01")))

current = head
while current is not None:
    print(current.value)
    current = current.next
```

Random indexed access is O(n), because you walk node by node. In application Python, built-in lists/deques are usually preferable; implementing linked lists is mainly educational and helps with trees/graphs and pointer-style reasoning.

### 7. Binary Search

Binary search requires sorted data.

```python
def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

For 1,000,000 sorted items, binary search needs only about 20 halving steps in the worst case because `2^20 ≈ 1,048,576`.

But if you sort an unsorted list only to do one lookup, total work may exceed a simple linear scan. Always include preprocessing cost in reasoning.

### 8. Sorting and Why Built-ins Usually Win

Insertion sort for learning:

```python
def insertion_sort(items):
    values = items.copy()
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values
```

Typical worst-case complexity is O(n²).

Real Python:

```python
alerts = [
    {"id": 1, "severity": 3},
    {"id": 2, "severity": 5},
    {"id": 3, "severity": 1},
]
alerts.sort(key=lambda a: a["severity"], reverse=True)
```

Use trusted optimized built-in sorting in production unless you have a specialized algorithmic requirement.

### 9. Trees and Traversal

Tree node:

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Preorder traversal:

```python
def preorder(node):
    if node is None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)
```

Example tree:

```text
        prod
       /    \
     web     data
    /  \      \
 api   ui      db
```

Trees model hierarchical configuration, file structures, syntax, and organizational relationships.

### 10. Heaps and Priority Queues

Use `heapq` for a min-heap. To process highest severity first, negate the numeric priority.

```python
import heapq

queue = []
heapq.heappush(queue, (-5, "critical-db-alert"))
heapq.heappush(queue, (-2, "warning-web-alert"))
heapq.heappush(queue, (-4, "high-auth-alert"))

while queue:
    neg_priority, alert = heapq.heappop(queue)
    print(-neg_priority, alert)
```

Insertion/removal are O(log n), while reading the top is O(1). This structure maps naturally to schedulers and alert prioritization.

### 11. Graphs: Modeling Networks and Dependencies

An adjacency-list graph:

```python
graph = {
    "internet": ["firewall"],
    "firewall": ["web"],
    "web": ["api"],
    "api": ["db", "cache"],
    "db": [],
    "cache": [],
}
```

This graph can represent a service dependency path or network reachability relationship.

Graphs can be directed, undirected, weighted, or unweighted. Later cloud architecture and cybersecurity attack-path analysis rely heavily on graph thinking.

### 12. BFS and DFS with Worked Examples

BFS uses a queue:

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

DFS uses recursion or a stack:

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)
```

The `visited` set prevents cycles from causing infinite traversal.

### 13. Recursion and Stack Cost

Factorial is a classic recursive example:

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Trace `factorial(4)`:

```text
factorial(4)
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1
24
```

Each recursive call consumes call-stack space. Recursion can be elegant for trees, but very deep recursion may exceed language/runtime limits.

### 14. Worked Scenario: Security Alert Correlation

Given alerts:

```python
alerts = [
    {"id": "A1", "source": "10.0.0.9", "asset": "web", "severity": 5},
    {"id": "A2", "source": "10.0.0.9", "asset": "api", "severity": 4},
    {"id": "A3", "source": "10.0.0.8", "asset": "db", "severity": 3},
]
```

Choose structures intentionally:

```python
alerts_by_id = {a["id"]: a for a in alerts}      # exact lookup
sources = {a["source"] for a in alerts}           # uniqueness

from collections import Counter
source_counts = Counter(a["source"] for a in alerts)  # frequency
```

Graph relationships:

```python
from collections import defaultdict
attack_graph = defaultdict(set)
for a in alerts:
    attack_graph[a["source"]].add(a["asset"])
```

This one scenario uses a dictionary, set, counter, and graph because each supports a different operation efficiently and clearly.


# Enhanced Deep-Dive — Complete DSA Foundation

The original material already establishes the essential path from Big-O to Python containers, stacks, queues, heaps, trees, graphs, BFS/DFS, recursion, sorting, security-alert correlation, benchmarking, and dependency graphs. This expansion keeps that foundation and develops the missing algorithmic reasoning, implementation trade-offs, and advanced structures needed before backend, cloud, AI, embedded, and cybersecurity work.

Use this repeated reasoning loop:

```text
Problem
  ↓
Required operations
  ↓
Data size / shape
  ↓
Candidate structures
  ↓
Correctness invariant
  ↓
Time complexity
  ↓
Space complexity
  ↓
Implementation
  ↓
Boundary tests
  ↓
Benchmark realistic workloads
```

### Deep Dive — Data Structure, Algorithm, and Abstract Data Type

A data structure is a concrete organization of data. An algorithm is a procedure. An Abstract Data Type (ADT) defines operations and semantics independently from the concrete storage implementation.

For example, a stack ADT says `push`, `pop`, and `peek`; it does not require a linked list. In Python, a list is usually the best stack implementation.

#### Mental Model

```text
Stack ADT
├─ push(x)
├─ pop()
└─ peek()

Possible implementations:
├─ Python list
├─ linked nodes
└─ fixed array
```

#### Python Example

```python
stack = []
stack.append("scan-a")
stack.append("scan-b")
assert stack.pop() == "scan-b"
```

#### Practical Use

Separating ADT from implementation lets you reason about requirements before choosing a container.


### Deep Dive — Big-O, Big-Omega, and Big-Theta

Big-O describes an asymptotic upper bound, Big-Omega a lower bound, and Big-Theta a tight bound. In practical engineering, always name the operation and input variable before stating complexity.

A full scan that always visits every item is Θ(n). A linear search has O(n) worst case but can finish in Ω(1) best case if the first item matches.

#### Mental Model

```text
Growth language:

O(f(n))      upper growth bound
Ω(f(n))      lower growth bound
Θ(f(n))      tight growth bound
```

#### Complexity

Complexity notation describes scaling, not exact execution time.

#### Engineering Notes

Average-case claims require assumptions about input distribution.


### Deep Dive — Best, Average, Worst, and Amortized Cost

Worst-case cost protects you from pathological inputs. Average-case cost requires a model of typical inputs. Amortized analysis spreads occasional expensive operations over a sequence.

Dynamic-array append is the classic example: most appends are cheap, but occasionally the backing storage grows and existing references are copied.

#### Mental Model

```text
append append append append
                 ↓ capacity full
           allocate larger array
                 ↓
              copy n
                 ↓
       many cheap appends again
```

#### Complexity

Python list append is commonly reasoned about as amortized O(1).


### Deep Dive — Space Complexity and Time–Memory Trade-Offs

An algorithm can use additional memory to reduce repeated CPU work. A dictionary index converts repeated O(n) scans into average O(1) lookups after O(n) preprocessing, at the cost of O(n) extra memory.

#### Mental Model

```text
Without index:
q queries × n scan → O(qn)

With index:
build dict O(n)
q lookups O(q)
total average → O(n + q)
extra space → O(n)
```

#### Python Example

```python
by_id = {asset["id"]: asset for asset in assets}
for asset_id in queries:
    asset = by_id.get(asset_id)
```

#### Practical Use

Cloud inventory, CMDB enrichment, IOC indexing, database-like in-memory lookup.


### Deep Dive — Algorithm Correctness and Loop Invariants

Performance is irrelevant if the algorithm is wrong. A loop invariant is a condition preserved before and after every iteration.

Binary search uses the invariant: if the target exists, it remains inside the current search interval.

#### Mental Model

```text
Initial:
low ---------------- high
       target inside

Each comparison:
discard impossible half

Invariant remains:
target, if present, is still within low..high
```

#### Engineering Notes

Use invariants for binary search, partition algorithms, graph traversal, and dynamic programming.


### Deep Dive — Python List as Dynamic Array

A Python list provides O(1) indexed access because element references are stored in a dynamic array. Appending is amortized O(1). Inserting/removing near the front or middle shifts later references and is O(n).

#### Mental Model

```text
index  0    1    2    3
      ┌────┬────┬────┬────┐
      │ref │ref │ref │ref │
      └────┴────┴────┴────┘
```

#### Python Example

```python
hosts = ["web", "db", "cache"]
hosts.append("mq")       # amortized O(1)
hosts.insert(1, "api")   # O(n)
```

#### Practical Use

Ordered data, indexed access, append-heavy workloads.


### Deep Dive — Cache Locality Awareness

Two algorithms with the same Big-O can behave differently because of CPU caches and memory layout. Dynamic arrays usually have better locality than pointer-heavy linked structures because their references are contiguous.

#### Engineering Notes

Big-O is necessary but not sufficient for performance engineering.


### Deep Dive — Singly Linked Lists

A singly linked list stores a value and reference to the next node. It allows O(1) insertion at the head but O(n) indexed access because traversal is sequential.

#### Mental Model

```text
head
 ↓
[A | •] → [B | •] → [C | None]
```

#### Python Example

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def prepend(head, value):
    return Node(value, head)
```

#### Complexity

Head insert O(1); search/index O(n); delete-after-known-node O(1).

#### Engineering Notes

In normal Python code, built-in lists/deques are usually better. Linked lists remain important for pointer reasoning and tree/graph concepts.


### Deep Dive — Doubly and Circular Linked Lists

A doubly linked list stores both previous and next references. A circular list reconnects the tail to the head. These forms support efficient local removal and round-robin traversal when node locations are already known.

#### Mental Model

```text
Doubly:
None ← A ⇄ B ⇄ C → None

Circular:
A → B → C
↑       ↓
└───────┘
```

#### Engineering Notes

Circular structures require explicit termination rules to avoid infinite traversal.


### Deep Dive — Stack Algorithms

A stack is LIFO. The most recently pushed element is removed first. Stacks model nested structure naturally.

#### Mental Model

```text
push C
┌───┐
│ C │ ← top
├───┤
│ B │
├───┤
│ A │
└───┘
```

#### Python Example

```python
def balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack
```

#### Complexity

Balanced-bracket scan: O(n) time, O(n) worst-case stack space.


### Deep Dive — Queue, Deque, and FIFO Processing

A queue is FIFO. Python's `collections.deque` provides O(1) append and popleft operations, making it the correct general-purpose FIFO structure.

#### Mental Model

```text
enqueue → [A][B][C] → dequeue A
```

#### Python Example

```python
from collections import deque

jobs = deque(["backup", "scan"])
jobs.append("report")
next_job = jobs.popleft()
```

#### Complexity

append/popleft O(1).

#### Engineering Notes

Repeated `list.pop(0)` is O(n) because every later element shifts.


### Deep Dive — Ring Buffer / Circular Queue

A ring buffer stores a bounded queue inside a fixed array. Head and tail indexes wrap using modulo arithmetic. It is common in embedded systems, networking, logging, and telemetry where memory must remain bounded.

#### Mental Model

```text
capacity = 5

[0][1][2][3][4]
    ↑       ↑
  tail     head

next = (index + 1) % capacity
```

#### Practical Use

UART buffers, recent telemetry, packet queues, bounded event history.


### Deep Dive — Hash Tables

A hash table transforms a key into a hash value and then maps that hash to an internal location. Exact lookup avoids scanning every key under normal conditions.

#### Mental Model

```text
key
 ↓ hash()
hash value
 ↓ bucket/probe position
candidate entries
 ↓ equality check
matching value
```

#### Complexity

Average lookup/insert/delete commonly O(1); worst case can degrade toward O(n).


### Deep Dive — Hash Collisions, Load Factor, and Resizing

Different keys can map to the same internal region. Collision resolution may use chaining or probing. As the table becomes crowded, implementations resize to keep average operations efficient.

#### Mental Model

```text
hash("alice") ─┐
               ├→ bucket 7
hash("bob")   ─┘

collision ≠ equality
```

#### Engineering Notes

One resize can be O(n), but insertion remains amortized O(1) across long sequences.


### Deep Dive — Hashability and Equality

Hash-based collections require equality and hash semantics to agree. Immutable values such as strings, integers, and many tuples are suitable keys. Mutable lists and dictionaries are not.

#### Mental Model

```text
Rule:
a == b
→ hash(a) must equal hash(b)
```

#### Practical Use

Sets, dictionaries, memoization keys, caching.


### Deep Dive — Algorithmic Complexity as a Security Concern

A structure that behaves well on ordinary data can become an availability problem under adversarially large or pathological input.

Defensive engineering therefore includes:
- input-size limits
- bounded queues/windows
- timeouts
- avoiding obviously quadratic parsing
- understanding hash-collision risk

#### Mental Model

```text
untrusted input
    ↓
algorithmic worst case
    ↓
CPU / RAM exhaustion
    ↓
availability loss
```

#### Practical Use

Security parsers, API endpoints, log ingestion, SIEM pipelines.


### Deep Dive — Linear Search

Linear search works on any iterable order. It examines elements until it finds the target or exhausts the data.

#### Mental Model

```text
def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1
```

#### Complexity

Best O(1), worst O(n), O(1) auxiliary space.


### Deep Dive — Binary Search

Binary search requires sorted data. Compare the middle element and discard the half that cannot contain the target.

#### Mental Model

```text
[1 3 5 7 9 11 13]
       ↑ mid
target 11 > 7
discard left half
```

#### Python Example

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

#### Complexity

O(log n) time, O(1) auxiliary space.

#### Engineering Notes

Test empty, one-element, first, last, missing-low, and missing-high cases.


### Deep Dive — Binary Search for Boundaries with bisect

Binary search is also used to find insertion boundaries rather than exact equality. `bisect_left` returns the first legal insertion position; `bisect_right` returns the position after existing equal values.

#### Mental Model

```text
from bisect import bisect_left, bisect_right

values = [10, 20, 20, 20, 30]
left = bisect_left(values, 20)
right = bisect_right(values, 20)
assert (left, right) == (1, 4)
```

#### Practical Use

Time ranges, ordered indexes, duplicate intervals.


### Deep Dive — Sorting Properties: Stable, In-Place, Adaptive

A stable sort preserves original order among equal keys. An in-place sort uses little auxiliary memory. An adaptive sort exploits existing order.

These properties can matter as much as asymptotic complexity.

#### Practical Use

Multi-column reports, constrained systems, partially sorted logs.


### Deep Dive — Bubble Sort

Bubble sort repeatedly swaps adjacent out-of-order items. It is useful for learning invariants but rarely for production.

#### Mental Model

```text
def bubble_sort(values):
    a = values.copy()

    for end in range(len(a)-1, 0, -1):
        swapped = False
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped:
            break

    return a
```

#### Complexity

Worst O(n²); best O(n) with early-exit optimization.


### Deep Dive — Selection Sort

Selection sort repeatedly finds the smallest remaining item and places it into the next final position.

#### Mental Model

```text
def selection_sort(values):
    a = values.copy()

    for i in range(len(a)):
        smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]

    return a
```

#### Complexity

Θ(n²) comparisons; O(1) auxiliary space in the in-place form.


### Deep Dive — Insertion Sort

Insertion sort grows a sorted prefix. It is simple and performs well on small or nearly sorted data.

#### Mental Model

```text
def insertion_sort(values):
    a = values.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = key

    return a
```

#### Complexity

Worst O(n²); near O(n) on already/nearly sorted input.


### Deep Dive — Merge Sort

Merge sort divides the input into halves, recursively sorts each half, then merges the sorted results.

#### Mental Model

```text
[8,3,5,1]
   split
[8,3] [5,1]
 split   split
[8][3] [5][1]
 merge   merge
[3,8] [1,5]
   merge
[1,3,5,8]
```

#### Python Example

```python
def merge_sort(values):
    if len(values) <= 1:
        return values.copy()

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    out = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1

    out.extend(left[i:])
    out.extend(right[j:])
    return out
```

#### Complexity

O(n log n) time; O(n) auxiliary memory for this implementation.


### Deep Dive — Quick Sort

Quick sort partitions values around a pivot and recursively sorts the partitions. Good pivot behavior gives excellent practical performance, but poor partitioning can produce quadratic worst-case time.

#### Mental Model

```text
pivot
  ↓
[ smaller ][ equal ][ greater ]
        recurse both sides
```

#### Python Example

```python
def quick_sort(values):
    if len(values) <= 1:
        return values.copy()

    pivot = values[len(values)//2]
    left = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    right = [x for x in values if x > pivot]
    return quick_sort(left) + equal + quick_sort(right)
```

#### Complexity

Average O(n log n), worst O(n²). The example uses extra lists for clarity.


### Deep Dive — Counting and Radix Sort Awareness

Comparison sorting is not always necessary. If keys come from a small known integer range, counting sort can operate in O(n+k), where k is the key range. Radix sort processes digits/bytes using stable sub-sorts.

These algorithms beat the comparison-model lower bound by using stronger assumptions about keys.

#### Mental Model

```text
Severity values only 1..5:
count each value
↓
reconstruct ordered output
```

#### Practical Use

Small integer severity classes, byte-oriented keys, constrained domains.


### Deep Dive — Why Built-In Sorting Usually Wins

Python's built-in sort is stable, highly optimized, and adaptive. Custom sorts should normally be educational or required by a specialized constraint.

#### Mental Model

```text
alerts.sort(
    key=lambda a: (a["severity"], a["timestamp"]),
    reverse=True,
)
```

#### Engineering Notes

Optimization work should focus on data modeling, key extraction, query reduction, and avoiding unnecessary full sorts.


### Deep Dive — Recursion and the Call Stack

Recursion solves a problem using smaller instances of itself. Every recursive function needs a base case and progress toward it.

Each active call consumes a frame, so very deep recursion can exceed Python's recursion limit.

#### Mental Model

```text
factorial(4)
→ 4 * factorial(3)
→ 4 * 3 * factorial(2)
→ 4 * 3 * 2 * factorial(1)
→ 24
```

#### Engineering Notes

Python does not guarantee tail-call optimization; use iterative approaches for very deep/untrusted structures.


### Deep Dive — Divide and Conquer

Divide-and-conquer splits a problem, solves independent subproblems, then combines results.

#### Mental Model

```text
Problem n
 /      n/2    n/2
 |       |
solve   solve
 \       /
  combine
```

#### Practical Use

Merge sort, binary search, many geometric and numerical algorithms.


### Deep Dive — Backtracking

Backtracking explores a decision tree and undoes a choice when a branch cannot produce a valid result.

#### Mental Model

```text
choice A
├─ choice B
│  ├─ valid
│  └─ invalid → backtrack
└─ choice C
```

#### Python Example

```python
def subsets(values):
    out = []

    def visit(i, current):
        if i == len(values):
            out.append(current.copy())
            return

        visit(i + 1, current)
        current.append(values[i])
        visit(i + 1, current)
        current.pop()

    visit(0, [])
    return out
```

#### Complexity

Generating all subsets requires Θ(2^n) outputs.


### Deep Dive — Tree Terminology and Traversal

A tree is a connected acyclic hierarchy. Important terms include root, parent, child, sibling, leaf, depth, height, and subtree.

#### Mental Model

```text
prod
   /         web     data
/  \        api   ui     db
```

#### Practical Use

Filesystems, syntax trees, configuration hierarchies, organizational structures.


### Deep Dive — Preorder, Inorder, Postorder, and Level Order

Traversal order changes what you can compute naturally.

- preorder: node before children
- inorder: left, node, right
- postorder: children before node
- level-order: breadth-first by depth

#### Mental Model

```text
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

#### Engineering Notes

For a binary search tree, inorder traversal yields sorted keys.


### Deep Dive — Binary Search Trees

A BST maintains an ordering invariant. Search follows only one branch at each comparison.

Its efficiency depends on height.

#### Mental Model

```text
Balanced:
       4
      /      2   6

Degenerate:
1
   2
       3
```

#### Complexity

Operations O(h). Balanced h=O(log n); degenerate h=O(n).


### Deep Dive — AVL and Red-Black Trees Awareness

Self-balancing BSTs use rotations and invariants to keep height O(log n).

AVL trees are more strictly height-balanced. Red-black trees use coloring constraints and are widely used in systems libraries.

#### Practical Use

Ordered maps/sets when predictable logarithmic operations are required.


### Deep Dive — Trie / Prefix Tree

A trie shares prefixes between strings. Search cost depends on query length rather than number of stored strings.

#### Mental Model

```text
(root)
  |
  w
 / e   a
|   |
b   f
```

#### Python Example

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True
```

#### Practical Use

Autocomplete, command prefix matching, hostname/path-prefix matching.


### Deep Dive — Segment Tree and Fenwick Tree Awareness

When an array receives many range queries and updates, rescanning every range is expensive.

- Segment tree: flexible range queries/updates in O(log n)
- Fenwick tree: compact prefix-sum/point-update structure in O(log n)

#### Practical Use

Time-series aggregation, counters, online range totals.


### Deep Dive — Heap and Priority Queue

A min-heap guarantees that the smallest item is at the root. It does not globally sort all elements.

#### Mental Model

```text
1
      /        4     3
    /    8   5

array → [1,4,3,8,5]
```

#### Python Example

```python
import heapq

pq = []
heapq.heappush(pq, (2, "warning"))
heapq.heappush(pq, (1, "critical"))
priority, item = heapq.heappop(pq)
```

#### Complexity

peek O(1), push O(log n), pop O(log n), heapify O(n).


### Deep Dive — Top-K with a Heap

If you need only the largest k values, sorting every element may perform unnecessary work. A heap can maintain only k candidates.

#### Mental Model

```text
import heapq

top = heapq.nlargest(
    10,
    alerts,
    key=lambda a: a["severity"],
)
```

#### Complexity

Typical top-k approach O(n log k), instead of full sort O(n log n).


### Deep Dive — Graph Fundamentals

A graph contains vertices and edges. Unlike trees, graphs can contain arbitrary relationships, cycles, disconnected components, directions, and weights.

#### Mental Model

```text
internet → firewall → web → api → db
                         ↘ cache
```

#### Practical Use

Networks, dependencies, attack-path modeling, IAM trust, package graphs.


### Deep Dive — Adjacency List, Matrix, and Edge List

Choose graph representation by density and operations.

Adjacency list stores only actual neighbors. Matrix allocates V×V relationship slots. Edge list stores edges directly.

#### Mental Model

```text
Sparse:
A → [B,C]
B → [D]

Matrix:
    A B C
A [ 0 1 1 ]
B [ 0 0 0 ]
C [ 0 0 0 ]
```

#### Complexity

Adjacency list space O(V+E); matrix space O(V²).


### Deep Dive — Breadth-First Search

BFS explores nodes in nondecreasing number of edges from the start. It uses a FIFO queue.

#### Mental Model

```text
from collections import deque

def bfs(graph, start):
    seen = {start}
    q = deque([start])

    while q:
        node = q.popleft()
        yield node

        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
```

#### Complexity

O(V+E) with an adjacency list.

#### Engineering Notes

Mark visited when enqueuing to prevent duplicate queue entries.


### Deep Dive — Shortest Path in an Unweighted Graph

Because BFS explores hop distance layer by layer, the first time it reaches a node is through a shortest path by number of edges.

#### Mental Model

```text
distance 0: start
distance 1: neighbors
distance 2: neighbors-of-neighbors
...
```

#### Practical Use

Minimum-hop service dependency or reachability path.


### Deep Dive — Depth-First Search

DFS follows one path deeply before backtracking. It can use recursion or an explicit stack.

#### Mental Model

```text
def dfs_iterative(graph, start):
    seen = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in seen:
            continue

        seen.add(node)
        stack.extend(reversed(graph.get(node, [])))

    return seen
```

#### Complexity

O(V+E).

#### Engineering Notes

Use iterative DFS for very deep or externally supplied graphs.


### Deep Dive — Connected Components

In an undirected graph, start BFS/DFS from each unvisited node. Each traversal discovers one connected component.

#### Practical Use

Identify isolated network zones or disconnected service groups.


### Deep Dive — Cycle Detection in Directed Graphs

DFS can classify nodes as:
- WHITE: unseen
- GRAY: currently on recursion path
- BLACK: fully processed

An edge to a GRAY node is a back edge and proves a cycle.

#### Mental Model

```text
A → B → C
    ↑   ↓
    └───┘

C → B while B is GRAY
→ cycle
```

#### Practical Use

Dependency validation, build graphs, IaC plans.


### Deep Dive — Topological Sorting

A DAG can be ordered so every dependency appears before the dependent node.

Two standard approaches:
- DFS postorder with cycle detection
- Kahn's algorithm using indegrees

#### Mental Model

```text
database ─┐
          ├→ api → frontend
cache ────┘

valid:
database, cache, api, frontend
```

#### Complexity

O(V+E).

#### Practical Use

Deployment ordering, package managers, CI stages, build systems.


### Deep Dive — Dijkstra's Shortest Path

Dijkstra computes single-source shortest paths when all edge weights are non-negative. A priority queue always expands the currently cheapest known node.

#### Mental Model

```text
import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d != dist[node]:
            continue

        for nxt, weight in graph.get(node, []):
            nd = d + weight
            if nd < dist.get(nxt, float("inf")):
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist
```

#### Complexity

Common binary-heap analysis: O((V+E) log V).

#### Engineering Notes

Do not use Dijkstra with negative edge weights.


### Deep Dive — Bellman-Ford, Floyd-Warshall, and A* Awareness

Different shortest-path problems require different algorithms.

- Bellman-Ford handles negative edge weights and can detect reachable negative cycles.
- Floyd-Warshall computes all-pairs shortest paths.
- A* adds a heuristic to guide search toward a goal.

#### Mental Model

```text
Shortest-path choice

Unweighted graph
    ↓
   BFS

Weighted, non-negative
    ↓
 Dijkstra

Negative edges
    ↓
Bellman-Ford

All pairs / smaller dense graph
    ↓
Floyd-Warshall

Goal-directed + useful heuristic
    ↓
   A*
```

#### Complexity

Bellman-Ford O(VE); Floyd-Warshall O(V³); A* depends on graph, heuristic, and implementation.

#### Engineering Notes

Algorithm choice depends on graph assumptions and query pattern.


### Deep Dive — Union-Find / Disjoint Set

Union-Find maintains disjoint components.

Core operations:
- `find(x)` returns the representative of x's component.
- `union(a, b)` merges the two components.

Path compression and union-by-rank/size keep trees shallow.

#### Mental Model

```text
Before union:
A—B     C—D

union(B,C)

After:
A—B—C—D
one connected component
```

#### Python Example

```python
class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True
```

#### Complexity

With path compression + rank/size heuristics, operations are nearly constant amortized.

#### Practical Use

Connectivity, clustering, Kruskal MST, undirected-cycle detection.


### Deep Dive — Minimum Spanning Tree: Kruskal and Prim

For a connected weighted undirected graph, a minimum spanning tree connects all vertices with no cycles while minimizing total selected edge weight.

This objective differs from shortest path. An MST minimizes the **sum of chosen edges**, not distance from a particular source.

#### Mental Model

```text
Kruskal:
sort edges
  ↓
take cheapest
  ↓
does it join two components?
  ├─ yes → keep
  └─ no  → skip
  ↓
Union-Find

Prim:
start from one node
  ↓
keep cheapest edge crossing tree boundary
  ↓
grow tree
```

#### Complexity

Kruskal is commonly O(E log E), dominated by edge sorting. Prim with a heap is commonly O(E log V).

#### Practical Use

Minimum-cost cabling/network design and graph-connectivity planning.


### Deep Dive — Two-Pointer Technique

Two pointers can replace nested searching when the data has useful ordering or structure.

For a sorted array, one pointer starts at each end. Their sum tells you which pointer to move.

#### Mental Model

```text
target = 10

[1,2,4,6,8]
 ↑       ↑
 L       R

1+8 < 10
move L right
```

#### Python Example

```python
def pair_sum_sorted(values, target):
    left = 0
    right = len(values) - 1

    while left < right:
        total = values[left] + values[right]

        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1

    return None
```

#### Complexity

O(n) after data is sorted.

#### Engineering Notes

If sorting is required first, include its O(n log n) preprocessing cost.


### Deep Dive — Fixed and Variable Sliding Windows

A sliding window reuses state between neighboring contiguous ranges.

Fixed window:
- remove the item leaving the window
- add the item entering the window

Variable window:
- grow right edge
- shrink left edge while a constraint is violated

#### Mental Model

```text
[a b c] d e
   ↓ shift
 a [b c d] e

reuse:
old_sum - a + d
```

#### Python Example

```python
def max_window(values, k):
    if k <= 0 or k > len(values):
        raise ValueError("invalid k")

    current = sum(values[:k])
    best = current

    for i in range(k, len(values)):
        current += values[i] - values[i-k]
        best = max(best, current)

    return best
```

#### Complexity

Fixed sliding window is O(n) instead of O(nk).

#### Practical Use

Rate limits, event windows, rolling CPU/error metrics.


### Deep Dive — Prefix Sums and Difference Arrays

A prefix sum stores cumulative totals so range sums can be answered with subtraction.

A difference array performs the opposite style of optimization: many range increments are recorded at interval boundaries and materialized later with one prefix scan.

#### Mental Model

```text
values:  [3, 2, 5, 4]
prefix: [0, 3, 5,10,14]

sum values[1:3]
= prefix[3] - prefix[1]
= 10 - 3
= 7
```

#### Python Example

```python
def prefix_sums(values):
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    return prefix
```

#### Complexity

Prefix build O(n); range sum O(1); extra space O(n).

#### Practical Use

Time-series range totals, packet counters, production telemetry.


### Deep Dive — Monotonic Stack and Monotonic Queue

A monotonic stack keeps candidates in increasing or decreasing order.

For next-greater-element problems, each index is pushed once and popped at most once, so the total work is linear.

A monotonic deque extends the idea to rolling minima/maxima.

#### Mental Model

```text
values: 2 1 5 3

stack stores unresolved indices
2 waits
1 waits
5 resolves both
```

#### Python Example

```python
def next_greater(values):
    result = [-1] * len(values)
    stack = []

    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            j = stack.pop()
            result[j] = value
        stack.append(i)

    return result
```

#### Complexity

O(n), because each index enters and leaves the stack at most once.

#### Practical Use

Next-greater events, rolling maxima, span calculations.


### Deep Dive — Greedy Algorithms

A greedy algorithm makes the locally best choice at each step.

Greedy methods are attractive because they are often simple and fast, but they are correct only when the problem has a property proving that local choices can lead to a global optimum.

#### Mental Model

```text
current state
    ↓
choose locally best next action
    ↓
new state
    ↓
repeat
```

#### Practical Use

Scheduling, MSTs, interval selection, priority handling.

#### Engineering Notes

A heap may support a greedy choice efficiently, but the data structure does not prove the greedy algorithm is correct.


### Deep Dive — Dynamic Programming

Dynamic programming is useful when the same smaller subproblems appear repeatedly.

The important work is not drawing a table. It is defining:
- state
- transition
- base cases
- evaluation order

#### Mental Model

```text
Naive recursion:
same state solved repeatedly

          f(5)
       /             f(4)       f(3)
    /   \       /    f(3) f(2)   f(2) f(1)

DP:
state → solve once → cache/reuse
```

#### Practical Use

Optimization, sequence problems, scheduling, counting, path problems.


### Deep Dive — Memoization vs Tabulation

Memoization is top-down recursion plus caching. Tabulation is bottom-up computation.

Memoization naturally follows the recursive definition. Tabulation avoids recursive call overhead/depth and often exposes opportunities to keep only the last few states.

#### Python Example

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_tab(n):
    if n <= 1:
        return n

    prev, cur = 0, 1
    for _ in range(2, n + 1):
        prev, cur = cur, prev + cur

    return cur
```

#### Complexity

Both examples are O(n) time; iterative version uses O(1) state beyond integer size.

#### Engineering Notes

Do not use DP simply because recursion exists. Look for overlapping subproblems.


### Deep Dive — String Matching: Naive Search, KMP, and Rolling Hash

Naive substring search can recheck many characters after a mismatch.

KMP preprocesses the pattern to build prefix/fallback information, allowing O(n+m) matching.

Rabin-Karp style rolling hashes compare window hashes, but hash matches still require verification because collisions are possible.

#### Mental Model

```text
Naive:
restart comparison after mismatch

KMP:
reuse longest prefix/suffix knowledge
      ↓
skip comparisons already implied

Rolling hash:
window hash
   ↓ equals?
verify actual characters
```

#### Complexity

Naive worst case O(nm); KMP O(n+m).

#### Practical Use

Large text/log matching and parser foundations.


### Deep Dive — Bit Manipulation and Bit Sets

Bits can encode many boolean flags compactly.

A bit set is especially attractive when the universe is small and fixed.

#### Python Example

```python
READ = 1 << 0
WRITE = 1 << 1
EXEC = 1 << 2

permissions = READ | WRITE

can_read = bool(permissions & READ)
permissions |= EXEC
permissions &= ~WRITE
```

#### Practical Use

Permissions, protocol flags, embedded registers, compact state masks.


### Deep Dive — LRU Cache

Least Recently Used eviction removes the entry that has gone unused for the longest time when capacity is exceeded.

A practical implementation combines hash lookup with recency ordering.

#### Python Example

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return None

        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)

        self.data[key] = value

        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
```

#### Complexity

Average get/put O(1) with an ordered hash-map implementation.

#### Engineering Notes

Production caches also need TTL/freshness, invalidation, concurrency, and memory policies.


### Deep Dive — Streaming and Online Algorithms

Streaming algorithms process items as they arrive without retaining the whole dataset. Online algorithms make incremental decisions before seeing all future input.

This matters when telemetry never ends.

#### Mental Model

```text
event
  ↓
update bounded state
  ↓
emit/update result
  ↓
discard raw event
```

#### Python Example

```python
count = 0
total = 0.0
maximum = None

for sample in stream:
    count += 1
    total += sample
    maximum = sample if maximum is None else max(maximum, sample)
```

#### Practical Use

Monitoring, SIEM, telemetry, packet/event analytics.


### Deep Dive — Reservoir Sampling

Reservoir sampling keeps a fixed-size uniform sample from a stream whose total length may be unknown.

The key idea is that later elements probabilistically replace earlier selected elements so every item has equal final inclusion probability.

#### Practical Use

Sampling enormous logs with O(k) memory for a reservoir of size k.


### Deep Dive — Bloom Filter

A Bloom filter is a probabilistic membership structure built from a bit array and multiple hash positions.

Standard interpretation:
- any required bit is zero → definitely absent
- all required bits are one → possibly present

A positive must be verified against an exact source when false positives matter.

#### Mental Model

```text
key
 ├─ hash1 → bit 3
 ├─ hash2 → bit 8
 └─ hash3 → bit 12

query:
any zero?
→ definitely absent

all one?
→ possibly present
```

#### Practical Use

Large watchlist prefilters, deduplication prechecks, cache/database lookup reduction.

#### Engineering Notes

Bloom filters trade exactness for memory efficiency.


### Deep Dive — Benchmarking and Scaling

A benchmark should test realistic operations across several input sizes.

One data point tells you a duration; multiple sizes help reveal the growth trend.

#### Python Example

```python
from timeit import timeit

for n in [1_000, 10_000, 100_000]:
    items = list(range(n))
    lookup = set(items)
    target = n - 1

    list_t = timeit(lambda: target in items, number=100)
    set_t = timeit(lambda: target in lookup, number=100)

    print(n, list_t, set_t)
```

#### Engineering Notes

Control setup, repeat enough times, and avoid claiming the exact timings are universal.


### Deep Dive — Profiling Before Optimization

Profiling identifies where an actual program spends its CPU time or memory.

A 10× improvement to a function that consumes 1% of runtime barely changes the system. A better data structure in a hot O(n²) path can transform the workload.

#### Mental Model

```text
Correctness
   ↓
Measure
   ↓
Find hot path
   ↓
Improve algorithm / data structure
   ↓
Measure again
```

#### Practical Use

Production performance engineering.


### Deep Dive — Defensive Time-Window Correlation

For repeated-login-failure detection, retain only events still inside the active time window.

A deque is ideal because old events expire from the left while new events append on the right.

#### Python Example

```python
from collections import defaultdict, deque

windows = defaultdict(deque)

def record_failure(ip, now, window_seconds=60):
    q = windows[ip]
    cutoff = now - window_seconds

    while q and q[0] < cutoff:
        q.popleft()

    q.append(now)
    return len(q)
```

#### Complexity

Each timestamp is appended once and removed once, so expiry is amortized O(1) per event beyond dictionary access.

#### Practical Use

Synthetic defensive authentication-monitoring exercises.


### Deep Dive — Attack-Path and Blast-Radius Graph Thinking

A graph can model allowed network/service relationships. BFS or DFS answers what is reachable from an initial node.

This is an architectural reachability model. It does not prove exploitability, vulnerability, or authorization to interact with real systems.

#### Mental Model

```text
internet
   ↓
firewall
   ↓
web
   ↓
api
 ├─→ db
 └─→ cache
```

#### Practical Use

Architecture review, dependency blast radius, defensive attack-path modeling.


### Deep Dive — Strongly Connected Components

In a directed graph, a strongly connected component is a maximal group where every node can reach every other node.

Tarjan's and Kosaraju's algorithms can identify SCCs in O(V+E).

#### Mental Model

```text
A → B → C
↑   ↓   |
└── D ←─┘

some nodes may form one mutually reachable SCC
```

#### Practical Use

Circular service dependencies, mutually reachable trust/dependency regions.


### Deep Dive — Articulation Points and Bridges

In an undirected graph:
- an articulation point is a vertex whose removal disconnects the graph
- a bridge is an edge whose removal disconnects the graph

These structures identify fragile connectivity.

#### Practical Use

Single points of failure, network-resilience modeling.


### Deep Dive — Choosing a Data Structure by Dominant Operation

The best structure usually follows from the operation that dominates the workload.

Examples:
- exact lookup by key → dictionary
- repeated membership → set
- FIFO → deque
- LIFO → stack/list
- highest-priority next → heap
- hierarchy → tree
- arbitrary relationships → graph
- fixed recent history → bounded deque/ring buffer

#### Mental Model

```text
Requirement
   ↓
Dominant operation
   ↓
Candidate structure
   ↓
Time/space analysis
   ↓
Benchmark
```

#### Engineering Notes

This is the central engineering habit that matters more than memorizing definitions.


### Deep Dive — Final DSA Engineering Workflow

Data structures and algorithms become practical when they are tied to requirements, correctness, scale, and measurement.

#### Mental Model

```text
Business / technical requirement
           ↓
        operation
           ↓
        data shape
           ↓
     data structure
           ↓
        algorithm
           ↓
 correctness invariant
           ↓
 time + space cost
           ↓
 realistic benchmark
           ↓
 production trade-off
```

#### Practical Use

Use this workflow in backend, cloud, cybersecurity, AI, embedded, and interview problems.



## 5. Hands-on Lab / Practical Exercises

### Lab — Benchmark list vs set membership

1. Generate 100,000 identifiers.
2. Store them in both a list and set.
3. Use `timeit` for repeated existing/missing lookups.
4. Explain the measured result using expected complexity.

**Starter / reference code:**

```python
from timeit import timeit

items = [f"host-{i}" for i in range(100_000)]
item_set = set(items)

target = "host-99999"
print(timeit(lambda: target in items, number=1000))
print(timeit(lambda: target in item_set, number=1000))
```

**Expected result:** A measured demonstration that theory and real runtime should be considered together.

### Lab — BFS service dependency explorer

1. Represent services with an adjacency-list dictionary.
2. Implement BFS using deque.
3. Add a cycle and verify visited-set behavior.
4. Return reachable services rather than only printing.

**Starter / reference code:**

```python
from collections import deque

def reachable(graph, start):
    seen = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return seen
```

**Expected result:** A reusable reachability function.

### Lab — Priority alert queue

1. Create alerts with severity.
2. Push them onto a heap.
3. Process highest severity first.
4. Add a tie-breaker such as sequence number to avoid comparing incompatible payloads.

**Starter / reference code:**

```python
import heapq

pq = []
seq = 0
for severity, message in [(5,"db"),(2,"web"),(5,"auth")]:
    heapq.heappush(pq, (-severity, seq, message))
    seq += 1

while pq:
    severity, _, message = heapq.heappop(pq)
    print(-severity, message)
```

**Expected result:** A safe priority-queue pattern.


## Enhanced Hands-on Labs

### Enhanced Lab 1 — Formal Complexity

Choose ten algorithms from this course and state the input measure, best case, worst case, and tight bound where known.

### Enhanced Lab 2 — Amortized List Growth

Append thousands of items and inspect memory-size jumps. Explain why occasional resizing does not make every append O(n).

### Enhanced Lab 3 — Space Complexity

Compare storing every failed log record with storing only per-user counts.

### Enhanced Lab 4 — Algorithmic DoS Review

Find three places where unbounded input combined with an inefficient algorithm could exhaust CPU or memory.

### Enhanced Lab 5 — Ring Buffer

Implement a fixed-size circular queue with head, tail, size, and explicit full-buffer policy.

### Enhanced Lab 6 — Toy Hash Table

Build a separate-chaining hash table with a tiny bucket count to force collisions.

### Enhanced Lab 7 — Load Factor

Measure bucket occupancy as the toy hash table fills.

### Enhanced Lab 8 — Hashability

Create examples of valid and invalid dictionary keys and explain why.

### Enhanced Lab 9 — Binary Search Trace

Trace low/mid/high by hand across success and failure cases.

### Enhanced Lab 10 — Bisect Range

Use bisect_left/right to find all equal timestamps in a sorted array.

### Enhanced Lab 11 — Stable Sorting

Perform two-stage sorting and verify equal-key relative order.

### Enhanced Lab 12 — Merge Sort

Implement merge sort and derive its recurrence.

### Enhanced Lab 13 — Quick Sort

Compare pivot behavior on random, sorted, and duplicate-heavy input.

### Enhanced Lab 14 — Counting Sort

Sort synthetic severity values from 1..5 and compare with general comparison sorting.

### Enhanced Lab 15 — Backtracking

Generate subsets of n=4 and n=5 and connect output growth to 2^n.

### Enhanced Lab 16 — Tree Traversals

Implement preorder, inorder, postorder, and level-order on one tree.

### Enhanced Lab 17 — BST Shape

Insert sorted vs randomized keys and compare height.

### Enhanced Lab 18 — Trie

Implement insert, contains, and starts_with for hostnames.

### Enhanced Lab 19 — Heapify

Compare heapq.heapify with repeated heappush for growing data sizes.

### Enhanced Lab 20 — Priority Tie Breaker

Use (-severity, sequence, payload) and explain why the sequence is needed.

### Enhanced Lab 21 — Top-K

Compare full sorting with heapq.nlargest for small k.

### Enhanced Lab 22 — Graph Representations

Represent one graph as adjacency list, matrix, and edge list; compare storage.

### Enhanced Lab 23 — BFS Reachability

Return all reachable services from a gateway.

### Enhanced Lab 24 — BFS Shortest Path

Return a parent-based shortest hop path.

### Enhanced Lab 25 — Iterative DFS

Traverse a very deep chain without recursion.

### Enhanced Lab 26 — Connected Components

Find isolated groups in an undirected network model.

### Enhanced Lab 27 — Directed Cycle Detection

Use WHITE/GRAY/BLACK states and test a DAG plus one back edge.

### Enhanced Lab 28 — Kahn Topological Sort

Implement indegree-based ordering and detect a cycle.

### Enhanced Lab 29 — Dijkstra

Compute shortest non-negative latency paths and test unreachable nodes.

### Enhanced Lab 30 — Bellman-Ford Reasoning

Manually relax a tiny graph with a negative edge and explain why Dijkstra is unsuitable.

### Enhanced Lab 31 — Union-Find

Implement find/union with path compression and rank.

### Enhanced Lab 32 — Kruskal

Construct a minimum-cost fictional network using sorted edges and DSU.

### Enhanced Lab 33 — Two Pointers

Solve sorted pair-sum in O(n) and compare with brute force.

### Enhanced Lab 34 — Sliding Window

Find the busiest 60-second event window.

### Enhanced Lab 35 — Prefix Sum

Answer many range-count queries after one cumulative build.

### Enhanced Lab 36 — Monotonic Stack

Compute next-greater values and trace stack state.

### Enhanced Lab 37 — Greedy Counterexample

Find a coin set where largest-first does not produce minimum coins.

### Enhanced Lab 38 — Memoization

Compare naive and cached Fibonacci call counts.

### Enhanced Lab 39 — Tabulation

Rewrite one memoized recurrence as bottom-up iteration.

### Enhanced Lab 40 — KMP Table

Build an LPS/prefix table manually for a short pattern.

### Enhanced Lab 41 — Bit Flags

Represent eight permissions in one integer and implement set/clear/test.

### Enhanced Lab 42 — LRU Cache

Test recency refresh, update, and eviction.

### Enhanced Lab 43 — Streaming Aggregation

Compute count, mean, and maximum from one million generated values without retaining them.

### Enhanced Lab 44 — Reservoir Sampling

Keep a uniform sample of size 10 from a stream of unknown final length.

### Enhanced Lab 45 — Bloom Filter Model

Use a tiny educational bit-array model and explain false positives.

### Enhanced Lab 46 — Benchmark Scaling

Measure list/set membership at 1k, 10k, 100k and discuss growth.

### Enhanced Lab 47 — Profile Then Refactor

Profile repeated asset scans, replace them with a dictionary index, then re-profile.

### Enhanced Lab 48 — Failure Window

Implement per-source deques with expiry and cleanup of inactive keys.

### Enhanced Lab 49 — Dependency DAG

Topologically order a deployment graph, then inject a cycle and reject it.

### Enhanced Lab 50 — Defensive Reachability

Use BFS on a synthetic reachability graph and explicitly distinguish reachability from exploitability.

### Enhanced Lab 51 — SCC Identification

Manually identify strongly connected groups in a directed graph.

### Enhanced Lab 52 — Bridge/Articulation Review

Remove nodes/edges from a small undirected network and identify disconnecting elements.

### Enhanced Lab 53 — Structure Selection Drill

For 20 operational scenarios, write the dominant operation before naming the structure.

### Enhanced Lab 54 — Capstone

Complete the expanded Security Alert Prioritization and Correlation Engine.


## 6. Mini Project

### Mini Project — Security Alert Prioritization and Correlation Engine

**Required structures**

- Dictionary: alert ID → alert record.
- Set: unique source IPs.
- `Counter`: frequency by source/category.
- Heap: highest-severity processing queue.
- Graph adjacency list: source → targeted assets or service dependencies.
- BFS/DFS: reachable/connected resources.

**Required analysis document**

For every important operation, state expected complexity. Example:

```text
lookup alert by ID      dict      avg O(1)
check seen source       set       avg O(1)
pop next alert          heap      O(log n)
traverse attack graph   BFS       O(V + E)
```

Then benchmark at least one design choice with increasing synthetic data sizes.


### Expanded Capstone — Security Alert Prioritization and Correlation Engine

Expand the original mini-project into a complete local defensive analytics simulation.

```text
Synthetic / JSON Alerts
        ↓
Validation
        ↓
Indexes
├─ dict: alert ID → Alert
├─ set: unique sources
├─ Counter: frequencies
├─ deque: active time windows
├─ heap: severity priority
└─ LRU: bounded enrichment cache
        ↓
Graph Models
├─ service dependency
├─ architectural reachability
└─ weighted latency/cost
        ↓
Algorithms
├─ BFS / DFS
├─ shortest unweighted path
├─ connected components
├─ cycle detection
├─ topological sorting
├─ Dijkstra
├─ Union-Find optional
└─ top-k
        ↓
Reports
├─ prioritized alerts
├─ noisy sources
├─ threshold violations
├─ reachable assets
├─ shortest paths
└─ benchmark / complexity report
```

Suggested folder:

```text
alert_engine/
├── README.md
├── pyproject.toml
├── src/
│   └── alert_engine/
│       ├── models.py
│       ├── validation.py
│       ├── indexes.py
│       ├── windows.py
│       ├── priority.py
│       ├── cache.py
│       ├── graphs.py
│       ├── algorithms.py
│       ├── reports.py
│       └── main.py
├── tests/
│   ├── test_indexes.py
│   ├── test_windows.py
│   ├── test_priority.py
│   ├── test_graphs.py
│   └── test_algorithms.py
└── docs/
    ├── complexity.md
    ├── benchmarks.md
    ├── memory.md
    └── graph-model.md
```

Required model:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Alert:
    alert_id: str
    timestamp: int
    source_ip: str
    asset: str
    category: str
    severity: int
```

Required target complexity table:

```text
Operation                         Structure       Expected
-----------------------------------------------------------------
lookup alert by ID                dict            avg O(1)
check source membership           set             avg O(1)
frequency update                  Counter/dict    avg O(1)
priority push/pop                 heap            O(log n)
expire oldest window event        deque           O(1)
BFS / DFS                         adjacency list  O(V+E)
topological sort                  adjacency list  O(V+E)
Dijkstra                          heap + graph    O((V+E)logV)
top-k                             bounded heap    O(n log k)
range-sum query (stretch)         prefix sums     O(1) after build
```

Required benchmarks:

```text
1. list membership vs set membership
2. repeated scan vs dictionary index
3. full sort vs heap top-k
4. load-all events vs streaming aggregation
```

Use increasing synthetic sizes such as:

```text
1,000
10,000
100,000
```

Required correctness tests:

```text
duplicate alert ID
empty data
severity 1 and 5 boundaries
priority ties
time-window expiry
multiple independent source windows
graph cycle
disconnected graph
start == goal
unreachable goal
valid DAG ordering
Dijkstra with non-negative weights
negative-weight input rejected before Dijkstra
```

For every major structure, document:

```text
dominant operation
why this structure
expected time
expected space
failure mode
alternative considered
```

Security scope:

```text
The project is defensive and synthetic.
Graph reachability represents only relationships encoded in the model.
It does not prove exploitability and does not target external systems.
```


## 7. Recommended Resources

- Python docs for built-in containers, `collections`, `heapq`, and `bisect`.
- MIT OpenCourseWare algorithms material.
- Open Data Structures free textbook.
- CPython documentation/notes when you need implementation-specific details; distinguish those from language guarantees.

## 8. Certification Relevance

DSA is more important for programming interviews and engineering quality than for cloud-admin certification objectives. It improves your ability to write efficient automation, reason about large inventories/logs, and understand graphs used in networks and security attack paths.

## 9. Common Mistakes & Best Practices

- **Mistake:** Memorizing Big-O without connecting it to an operation.
  - **Best practice:** Always state the operation and data structure.
- **Mistake:** Using lists for repeated membership checks by habit.
  - **Best practice:** Consider sets when order/duplicates are irrelevant.
- **Mistake:** Forgetting a visited set in graph traversal.
  - **Best practice:** Track visited nodes whenever cycles are possible.
- **Mistake:** Writing custom sort in production unnecessarily.
  - **Best practice:** Use optimized built-ins unless a special requirement exists.
- **Mistake:** Ignoring preprocessing cost.
  - **Best practice:** Include sorting/index construction in total cost.
- **Mistake:** Optimizing without measuring.
  - **Best practice:** Start correct and clear, then benchmark the real bottleneck.


### Additional DSA Mistakes & Engineering Corrections

- **Mistake:** Saying "dict lookup is O(1)" without qualifying average/expected behavior.
  - **Best practice:** State average and worst-case assumptions.
- **Mistake:** Calling every nested loop O(n²).
  - **Best practice:** Count actual iterations and independent variables.
- **Mistake:** Ignoring output size.
  - **Best practice:** An algorithm cannot emit exponentially many outputs in polynomial total time.
- **Mistake:** Using Dijkstra with negative edges.
  - **Best practice:** Validate graph assumptions before selecting the algorithm.
- **Mistake:** Confusing MST with shortest path.
  - **Best practice:** State the optimization objective first.
- **Mistake:** Using recursive DFS on an untrusted million-node chain.
  - **Best practice:** Prefer explicit stacks for potentially deep inputs.
- **Mistake:** Marking BFS nodes visited only when dequeued.
  - **Best practice:** Mark when enqueued to prevent duplicate queue entries.
- **Mistake:** Letting per-source monitoring state grow forever.
  - **Best practice:** Define expiration and inactive-key cleanup.
- **Mistake:** Treating Bloom-filter positives as exact truth.
  - **Best practice:** Verify possible matches in authoritative storage.
- **Mistake:** Benchmarking one data size.
  - **Best practice:** Measure scaling over several values of n.


## 10. Self-Assessment Questions (with short answers)

### Q1. What is list indexed access complexity?

**Answer:** Typically O(1).

### Q2. What is unsorted list membership complexity?

**Answer:** O(n).

### Q3. What is average set/dict exact lookup commonly treated as?

**Answer:** O(1).

### Q4. What structure does BFS use?

**Answer:** Queue/deque.

### Q5. What structure does DFS use?

**Answer:** Stack or recursion.

### Q6. What is binary search complexity?

**Answer:** O(log n), assuming sorted data.

### Q7. What is heap push/pop complexity?

**Answer:** O(log n).

### Q8. What is graph traversal complexity with adjacency lists?

**Answer:** O(V + E).

### Q9. Why can recursion be risky for very deep structures?

**Answer:** Each call consumes stack space and runtime recursion depth may be limited.

### Q10. Why benchmark after Big-O reasoning?

**Answer:** Real constants, runtime overhead, memory locality, and workload patterns also matter.


## Extended Self-Assessment

### Extended Q1. What is an ADT?

**Answer:** A behavioral contract independent of a concrete implementation.

### Extended Q2. What does Θ(n) mean?

**Answer:** A tight asymptotic linear bound.

### Extended Q3. What is amortized complexity?

**Answer:** Average cost across a sequence allowing occasional expensive operations.

### Extended Q4. Why index once for many queries?

**Answer:** Trade O(n) build/space for average O(1) repeated exact lookups.

### Extended Q5. What is a loop invariant?

**Answer:** A property preserved across iterations and used to reason about correctness.

### Extended Q6. Why is list append amortized O(1)?

**Answer:** Occasional resize/copy is spread across many cheap appends.

### Extended Q7. What is a hash collision?

**Answer:** Different keys map to the same internal location/bucket region.

### Extended Q8. Why can hash-table worst case be O(n)?

**Answer:** Pathological collisions can force many comparisons.

### Extended Q9. What is binary-search's core precondition?

**Answer:** The input is sorted under the comparison order.

### Extended Q10. What does stable sort preserve?

**Answer:** Relative order of equal-key elements.

### Extended Q11. Merge-sort complexity?

**Answer:** O(n log n).

### Extended Q12. Quick-sort worst case?

**Answer:** O(n²).

### Extended Q13. Why can counting sort beat n log n?

**Answer:** It exploits a bounded key range rather than only comparisons.

### Extended Q14. Why can recursion fail on correct logic?

**Answer:** Call-stack/recursion-depth limits.

### Extended Q15. BST operation cost depends on what?

**Answer:** Tree height.

### Extended Q16. Why self-balance a BST?

**Answer:** Keep height logarithmic.

### Extended Q17. Trie search cost depends primarily on what?

**Answer:** Key/prefix length.

### Extended Q18. Heapify complexity?

**Answer:** O(n).

### Extended Q19. Why heap for top-k?

**Answer:** Avoid sorting all n items when k is small.

### Extended Q20. Adjacency-list space?

**Answer:** O(V+E).

### Extended Q21. Adjacency-matrix space?

**Answer:** O(V²).

### Extended Q22. Why BFS finds shortest unweighted path?

**Answer:** It explores by increasing hop distance.

### Extended Q23. What does a GRAY node mean in DFS cycle detection?

**Answer:** It is currently on the active recursion path.

### Extended Q24. When does topological ordering exist?

**Answer:** Only for a DAG.

### Extended Q25. Why can't Dijkstra safely use negative edges?

**Answer:** A later negative path can improve a distance already considered final.

### Extended Q26. What does Union-Find maintain?

**Answer:** Disjoint connectivity components.

### Extended Q27. MST vs shortest path?

**Answer:** MST minimizes total connecting edge cost; shortest path minimizes route cost.

### Extended Q28. Sliding-window advantage?

**Answer:** Reuses state between neighboring ranges.

### Extended Q29. Prefix-sum advantage?

**Answer:** O(1) range sums after O(n) build.

### Extended Q30. Why is monotonic-stack work O(n)?

**Answer:** Each index is pushed and popped at most once.

### Extended Q31. When is greedy valid?

**Answer:** When problem-specific properties prove local choices lead to an optimum.

### Extended Q32. What suggests dynamic programming?

**Answer:** Overlapping subproblems and reusable subproblem structure.

### Extended Q33. Memoization vs tabulation?

**Answer:** Top-down caching vs bottom-up computation.

### Extended Q34. KMP complexity?

**Answer:** O(n+m).

### Extended Q35. What is LRU?

**Answer:** Least Recently Used cache eviction.

### Extended Q36. What is a streaming algorithm?

**Answer:** Incremental processing without retaining the full input.

### Extended Q37. What does a Bloom-filter positive mean?

**Answer:** Possibly present; verify exactly.

### Extended Q38. What is reservoir sampling?

**Answer:** Uniform fixed-size sample from an unknown-length stream.

### Extended Q39. Why vary n in benchmarks?

**Answer:** To observe scaling behavior rather than one noisy duration.

### Extended Q40. Reachability vs exploitability?

**Answer:** Reachability only reflects modeled relationships; it does not prove a real exploit path.


## End-of-Module Practice Checklist

- [ ] I typed the examples myself instead of only reading them.
- [ ] I changed inputs and predicted results before running the code.
- [ ] I intentionally introduced at least three errors and debugged them.
- [ ] I completed the labs without copying the final solution first.
- [ ] I completed the mini project and wrote a short README.
- [ ] I can explain the important design choices aloud.

## Extended Worked Exercises

### Exercise 1 — Complexity derivation

```python
for i in range(n):
    for j in range(i):
        do_work()
```

The number of calls is `0 + 1 + ... + (n-1) = n(n-1)/2`, which grows as O(n²).

### Exercise 2 — Index once, query many times

Without index:

```python
for query in queries:
    for asset in assets:
        if asset["id"] == query:
            ...
```

With dictionary index:

```python
by_id = {asset["id"]: asset for asset in assets}
for query in queries:
    asset = by_id.get(query)
```

Analyze total complexity when there are `n` assets and `q` queries.

### Exercise 3 — BFS shortest hop count

Extend BFS by storing `(node, distance)` tuples. In an unweighted graph, the first time BFS reaches a node gives the minimum number of edges from the start.

### Exercise 4 — Top-k alerts

Use `heapq.nlargest(k, alerts, key=...)` and compare with sorting all alerts. Discuss when the difference matters.

### Exercise 5 — Memory tradeoff

A set uses additional memory but can reduce repeated membership lookup time. Explain why 'fastest' is not the only design criterion.

### Scenario Analysis

- Host inventory lookup by hostname → dictionary.
- Unique source IPs → set.
- Jobs in arrival order → queue/deque.
- Highest-severity alerts first → priority queue/heap.
- Nested configuration → tree-like structure.
- Service dependency/attack path → graph.
- Undo stack → stack.


## Practical Code Notebook — Data Structures & Algorithms

### Example A — Frequency counting

Manual dictionary:

```python
counts = {}
for ip in source_ips:
    counts[ip] = counts.get(ip, 0) + 1
```

Using `Counter`:

```python
from collections import Counter
counts = Counter(source_ips)
print(counts.most_common(5))
```

The algorithmic idea remains a hash map from item to count.

### Example B — Two-sum with different complexity

Brute force:

```python
def two_sum_slow(values, target):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                return i, j
    return None
```

Typical complexity O(n²).

Hash-map solution:

```python
def two_sum(values, target):
    seen = {}
    for i, value in enumerate(values):
        needed = target - value
        if needed in seen:
            return seen[needed], i
        seen[value] = i
    return None
```

Average O(n) time with O(n) extra space. This is a clear time-memory tradeoff.

### Example C — Sliding window idea

For maximum sum of `k` consecutive measurements:

```python
def max_window(values, k):
    if k <= 0 or k > len(values):
        raise ValueError("invalid k")

    current = sum(values[:k])
    best = current

    for i in range(k, len(values)):
        current += values[i] - values[i-k]
        best = max(best, current)
    return best
```

Instead of recomputing each window sum in O(k), update by adding one new value and removing one old value.

### Example D — Stack-based depth-first traversal

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        print(node)
        stack.extend(reversed(graph.get(node, [])))

    return visited
```

Using an explicit stack avoids recursion-depth limitations.

### Example E — BFS shortest hop path

```python
from collections import deque


def shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None
```

This returns a shortest path by edge count in an unweighted graph.

### Example F — Topological dependency idea

A deployment dependency graph such as:

```text
database → api → frontend
cache    → api
```

must deploy prerequisites before dependents. Topological sorting applies to directed acyclic graphs. You do not need to memorize the full algorithm yet, but recognize the problem shape: **ordering tasks subject to dependencies**.

### Example G — Binary search boundary test

Test all of these:

```python
assert binary_search([], 5) == -1
assert binary_search([5], 5) == 0
assert binary_search([5], 6) == -1
assert binary_search([1, 2, 3], 1) == 0
assert binary_search([1, 2, 3], 3) == 2
```

Algorithm bugs frequently live at empty, first, last, or one-element boundaries.

### Example H — Heap versus full sort

If you only need the top 10 alerts out of millions, a heap-based top-k approach can avoid sorting the entire dataset. In Python:

```python
import heapq

top = heapq.nlargest(10, alerts, key=lambda a: a["severity"])
```

The exact advantage depends on `k`, `n`, implementation, and memory constraints.

### Example I — Memoization

Recursive Fibonacci is intentionally inefficient:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Memoized:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Caching avoids recomputing overlapping subproblems. This introduces dynamic-programming thinking.

### Example J — Streaming versus loading everything

Bad for very large logs:

```python
lines = open("huge.log").readlines()
```

Streaming:

```python
with open("huge.log", encoding="utf-8") as fh:
    for line in fh:
        process(line)
```

Algorithm analysis includes space as well as time.

### Example K — Sparse graph representation

For 10,000 services where each depends on only 2–3 others, an adjacency matrix would allocate space for around 100 million possible relationships. An adjacency list stores only actual edges and is therefore much more appropriate for sparse graphs.

### Example L — Choosing structure by operation

```text
Requirement                         Structure
----------------------------------  --------------------
Keep insertion order               list
Fast exact lookup by unique ID     dict
Unique membership                  set
FIFO processing                    deque / queue
LIFO processing                    list / stack
Highest-priority next              heap / priority queue
Hierarchy                          tree
Arbitrary relationships            graph
```

Do not choose based on familiarity; choose based on operations and constraints.


## Guided Walkthroughs — Algorithms in Practice

### Walkthrough 1 — Complexity of repeated searches

Assume `n` assets and `q` queries.

Nested scan:

```python
for query in queries:          # q
    for asset in assets:       # up to n
        if asset.id == query:
            ...
```

Worst-case O(q × n).

Index first:

```python
by_id = {asset.id: asset for asset in assets}  # O(n)
for query in queries:                           # q lookups
    asset = by_id.get(query)                    # avg O(1)
```

Total average-style reasoning: O(n + q), with additional O(n) space. If you perform many queries, the index is often worth the memory.

### Walkthrough 2 — Queue simulation

```python
from collections import deque

jobs = deque()
jobs.append({"id": 1, "task": "backup"})
jobs.append({"id": 2, "task": "scan"})

while jobs:
    job = jobs.popleft()
    print("processing", job)
```

The structure matches FIFO semantics directly. Good data structures often make algorithms almost self-documenting.

### Walkthrough 3 — Deduplication while preserving first-seen order

A set alone loses the conceptual guarantee of list order. Combine structures:

```python
def unique_in_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

The set provides fast membership; list preserves result order.

### Walkthrough 4 — Detecting a cycle in a dependency graph

One DFS approach uses states:

```python
WHITE, GRAY, BLACK = 0, 1, 2


def has_cycle(graph):
    state = {node: WHITE for node in graph}

    def visit(node):
        state[node] = GRAY
        for nxt in graph.get(node, []):
            if state.get(nxt, WHITE) == GRAY:
                return True
            if state.get(nxt, WHITE) == WHITE and visit(nxt):
                return True
        state[node] = BLACK
        return False

    return any(state[node] == WHITE and visit(node) for node in graph)
```

A GRAY node is currently on the recursion path. Reaching another GRAY node means a back edge and therefore a cycle.

### Walkthrough 5 — Connected components idea

In an undirected network graph, start BFS/DFS from every unvisited node. Each traversal discovers one connected component. This can model isolated network segments or groups of mutually reachable assets.

### Walkthrough 6 — Binary-search invariant

During binary search, maintain:

```text
If target exists, it is within indices low..high.
```

Every comparison shrinks that interval while preserving the invariant. Thinking in invariants is a powerful way to prove algorithm correctness.

### Walkthrough 7 — Merge-sort idea

```text
[8, 3, 5, 1]
      split
[8, 3]   [5, 1]
 split     split
[8][3]   [5][1]
 merge     merge
[3,8]    [1,5]
     merge
[1,3,5,8]
```

Divide-and-conquer produces O(n log n) merge sort. Implement it once for learning, but use language built-ins for ordinary production sorting.

### Walkthrough 8 — Greedy example intuition

Suppose an incident responder always processes the currently highest-severity alert. That is a greedy policy: make the locally strongest choice now. A heap supports this policy efficiently. But greedy choice does not guarantee global optimality for every problem; the algorithm must match a property of the problem.

### Walkthrough 9 — Dynamic programming intuition

If many recursive branches repeatedly solve the same smaller subproblem, store previously computed answers.

```python
memo = {}

def ways(n):
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = ways(n-1) + ways(n-2)
    return memo[n]
```

The pattern is **overlapping subproblems + reusable answers**.

### Walkthrough 10 — Space complexity example

Two ways to count failed logins:

```python
# approach A: save every failed record
failed = [record for record in records if record.failed]

# approach B: keep only counts
counts = Counter(record.user for record in records if record.failed)
```

If only counts are needed, storing full failed records may waste memory. Requirements determine appropriate state.

### Walkthrough 11 — Stable sorting

```python
records = [
    ("web", 2),
    ("db", 1),
    ("api", 2),
]
```

If you sort by the second field with a stable sort, `web` remains before `api` because they have equal keys and that was their original relative order. Stability matters in multi-stage sorting.

### Walkthrough 12 — Benchmark carefully

Use `timeit` instead of one `time.time()` measurement for tiny functions:

```python
from timeit import timeit

setup = "items=list(range(10000)); target=9999"
print(timeit("target in items", setup=setup, number=1000))
```

Control what you are measuring and repeat enough times to reduce noise.

### Walkthrough 13 — Problem-to-structure drill

Choose a structure and justify it:

1. Map username → last-login timestamp.
2. Maintain next scheduled task by priority.
3. Track visited hosts during a network crawl.
4. Find dependencies reachable from a service.
5. Reverse the last five operator actions.
6. Process incoming messages in arrival order.
7. Store an ordered timeline of events.

Your justification is more important than naming the structure.


## Case Study — Dependency-Aware Deployment Order

Assume services have dependencies:

```python
graph = {
    "database": [],
    "cache": [],
    "api": ["database", "cache"],
    "frontend": ["api"],
}
```

You cannot safely deploy `frontend` before `api`, and `api` depends on `database` and `cache`. This is a directed dependency graph. One simple DFS-based ordering for an acyclic graph is:

```python
def dependency_order(graph):
    visited = set()
    visiting = set()
    result = []

    def visit(node):
        if node in visited:
            return
        if node in visiting:
            raise ValueError("cycle detected")

        visiting.add(node)
        for dependency in graph.get(node, []):
            visit(dependency)
        visiting.remove(node)

        visited.add(node)
        result.append(node)

    for node in graph:
        visit(node)

    return result

print(dependency_order(graph))
```

Possible output:

```text
['database', 'cache', 'api', 'frontend']
```

This is not just an academic graph problem. Package managers, CI pipelines, Infrastructure as Code engines, and build systems all reason about dependency graphs.

### Complexity reasoning

Each node is completed once and each dependency edge is examined, so the traversal is O(V + E), ignoring output/storage details.

## Case Study — Detecting Brute-Force Sources

Given login events, you want the first source reaching five failures.

```python
from collections import defaultdict

failed = defaultdict(int)

for event in events:
    if event["status"] != "FAILED":
        continue

    ip = event["source_ip"]
    failed[ip] += 1

    if failed[ip] == 5:
        print("threshold reached:", ip)
```

Why a dictionary? The central operation is **retrieve/update count by IP address**. A list of `(ip,count)` pairs would require repeated searching.

If events arrive forever, memory grows with the number of distinct IPs ever seen. A real monitoring system might use time windows, expiration, or a bounded cache. Algorithm design includes lifecycle and memory, not only CPU time.

## Practice Problems with Hints

1. **First non-repeated hostname** — use a frequency dictionary, then scan the original list once more.
2. **Merge two sorted timestamp lists** — use two indexes; avoid sorting the combined list again.
3. **Find duplicate alert IDs** — use a set of seen IDs and a second set of duplicates.
4. **Process tasks by earliest deadline** — priority queue keyed by deadline.
5. **Check whether all services are reachable from a gateway** — BFS/DFS and compare visited count with graph node count.
6. **Find maximum CPU in a stream** — keep only current maximum rather than storing all measurements.
7. **Recent N events** — deque with `maxlen=N`.
8. **Cache repeated DNS-like lookup results** — dictionary; discuss eviction if memory must be bounded.

For each problem, write the required operations first, then select the data structure.


## Enhanced Completion Checklist

- [ ] I can distinguish ADT, data structure, and algorithm.
- [ ] I can explain O, Ω, Θ, best/worst/average, and amortized cost.
- [ ] I can analyze time and auxiliary space.
- [ ] I can use invariants to reason about correctness.
- [ ] I can choose list/deque/set/dict/heap intentionally.
- [ ] I understand linked-list and ring-buffer trade-offs.
- [ ] I understand hashing, collisions, load factor, resizing, and hashability.
- [ ] I can implement linear and binary search.
- [ ] I can explain sorting stability and implement major educational sorts.
- [ ] I can reason about recursion, divide-and-conquer, and backtracking.
- [ ] I can traverse trees and explain balanced BST motivation.
- [ ] I understand tries, segment trees, and Fenwick-tree use cases.
- [ ] I can use heaps for priority queues and top-k.
- [ ] I can choose graph representations by density and operation.
- [ ] I can implement BFS, DFS, cycle detection, and topological sorting.
- [ ] I understand Dijkstra, Bellman-Ford, Floyd-Warshall, and A* selection criteria.
- [ ] I can implement Union-Find and explain MST algorithms.
- [ ] I can apply two pointers, sliding windows, prefix sums, and monotonic stacks.
- [ ] I understand greedy correctness requirements.
- [ ] I can implement memoized and tabulated DP.
- [ ] I understand KMP, tries, rolling hashes, bit masks, LRU, and Bloom filters.
- [ ] I can process streams with bounded state.
- [ ] I can benchmark scaling and profile before optimizing.
- [ ] I can apply DSA to defensive security and cloud dependency problems.
- [ ] I completed the expanded capstone.
