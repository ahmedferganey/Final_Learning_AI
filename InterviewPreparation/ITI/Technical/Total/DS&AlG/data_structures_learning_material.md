# Data Structures: A Comprehensive Learning Guide
### From Beginner to Intermediate

> **How to use this guide:** Work through sections in order if you are new to data structures. Each section is self-contained for reference use. Every code block is Python 3.10+ compatible and runnable. Practice questions appear after each major topic.

---

## Table of Contents

1. [Introduction to Data Structures](#1-introduction-to-data-structures)
2. [Classification of Data Structures](#2-classification-of-data-structures)
3. [Core Data Structures](#3-core-data-structures)
   - [Array](#31-array)
   - [Linked List](#32-linked-list)
   - [Stack](#33-stack)
   - [Queue](#34-queue)
   - [Binary Tree & BST](#35-binary-tree--binary-search-tree)
   - [AVL Tree](#36-avl-tree)
   - [Heap](#37-heap)
   - [Trie](#38-trie-prefix-tree)
   - [Hash Table](#39-hash-table--hash-map)
   - [Graph](#310-graph)
4. [Time Complexity Analysis Guide](#4-time-complexity-analysis-guide)
5. [When to Use Which Data Structure](#5-when-to-use-which-data-structure)
6. [Further Reading & Resources](#6-further-reading--resources)

---

# 1. Introduction to Data Structures

## 1.1 Definition and Importance

A **data structure** is a way of organizing, storing, and managing data in a computer's memory so it can be accessed and modified efficiently. The choice of data structure directly impacts the performance, memory usage, and readability of your program.

```
Without the right data structure:
  Search 1,000,000 records → O(n)   = 1,000,000 operations
  With a Hash Table         → O(1)  = ~1 operation
  With a Balanced BST       → O(log n) = ~20 operations

The right choice can make a program millions of times faster.
```

**Why data structures matter in practice:**

| Domain | Problem | Best Data Structure |
|---|---|---|
| Web browsers | Back/forward history | Stack |
| Operating systems | CPU task scheduling | Priority Queue |
| Databases | Indexed lookups | B-Tree / Hash Map |
| Social networks | Friend connections | Graph |
| Autocomplete | Word prefix lookup | Trie |
| File systems | Directory hierarchy | Tree |
| Caches | Fast key-value store | Hash Map + Doubly Linked List |

## 1.2 Abstract Data Type (ADT) vs Data Structure

These two terms are often confused. The distinction is fundamental:

| | Abstract Data Type (ADT) | Data Structure |
|---|---|---|
| **What it is** | A mathematical *model* — defines WHAT operations are possible and their behavior | A concrete *implementation* — defines HOW data is stored and HOW operations work |
| **Specifies** | Interface (operations + semantics) | Internal representation + algorithms |
| **Example** | Stack ADT: push, pop, peek, is_empty — defines behavior, not storage | Stack using an array or linked list — a specific implementation choice |
| **Analogy** | A blueprint for a building | The actual building |

```
ADT (the contract):              Implementation (fulfilling the contract):
┌─────────────────────┐          ┌────────────────────────────────┐
│   Stack ADT         │  ──────► │  Array-based Stack             │
│  - push(item)       │          │  or                            │
│  - pop() → item     │          │  Linked-List-based Stack       │
│  - peek() → item    │          │  (same ADT, different          │
│  - is_empty() → bool│          │   performance characteristics) │
└─────────────────────┘          └────────────────────────────────┘
```

**Key insight:** The same ADT can have multiple data structure implementations, each with different trade-offs in time and space complexity.

## 1.3 Why We Need Different Data Structures

No single data structure is best for all situations. Each excels at specific operations:

```
Array:        Fast random access    O(1) read/write by index
              Slow insertion/delete O(n) shifting required

Linked List:  Fast insertion/delete O(1) at known position
              Slow random access    O(n) must traverse

Hash Map:     Fast search/insert    O(1) average
              No ordering           cannot do range queries

BST:          Fast ordered search   O(log n)
              Supports range queries, sorted traversal

Graph:        Models relationships  edges between any nodes
              Enables path-finding, connectivity queries
```

**The fundamental trade-off:** Almost every data structure optimizes for some operations at the cost of others. Choosing wisely means understanding your access patterns.

---

> **Practice Questions — Section 1**
> 1. What is the difference between an ADT and a data structure? Give two real-world analogies.
> 2. If you need to frequently search for students by their ID number, which data structure would you choose and why?
> 3. Can the same ADT (e.g., Queue) be implemented with both an array and a linked list? What would change?

---

# 2. Classification of Data Structures

## 2.1 Complete Classification Map

```
Data Structures
│
├── Primitive (built into language)
│   ├── Integer
│   ├── Float
│   ├── Character
│   └── Boolean
│
└── Non-Primitive
    │
    ├── Linear (elements arranged sequentially)
    │   ├── Static  → Array (fixed size)
    │   └── Dynamic → Linked List, Stack, Queue, Deque
    │
    └── Non-Linear (elements not in sequence)
        ├── Trees  → Binary Tree, BST, AVL, Heap, Trie, B-Tree
        ├── Graphs → Directed, Undirected, Weighted, DAG
        └── Hash-based → Hash Table, Hash Set, Hash Map
```

## 2.2 Linear vs Non-Linear

| Property | Linear | Non-Linear |
|---|---|---|
| **Element arrangement** | Sequential, one after another | Hierarchical or networked |
| **Traversal** | Single pass visits all elements | Multiple paths possible |
| **Memory** | Usually contiguous or chain | Scattered, pointer-heavy |
| **Relationship** | Each element has at most one predecessor and one successor | One element can relate to many others |
| **Examples** | Array, Linked List, Stack, Queue | Tree, Graph, Heap, Trie |

## 2.3 Static vs Dynamic

| Property | Static | Dynamic |
|---|---|---|
| **Size** | Fixed at creation | Grows/shrinks at runtime |
| **Memory** | Allocated at compile time (or initialization) | Allocated at runtime |
| **Waste risk** | May waste space (over-allocated) | No waste — allocates exactly what is needed |
| **Examples** | Array | Linked List, BST, Hash Table with dynamic resizing |

## 2.4 Primitive vs Non-Primitive

| | Primitive | Non-Primitive |
|---|---|---|
| **Definition** | Basic types defined by the language | Derived types built from primitives |
| **Operations** | Arithmetic, comparison | Depends on structure |
| **Memory** | Single memory location | Multiple memory locations |
| **Examples** | `int`, `float`, `bool`, `char` | Array, Linked List, Tree, Graph |

## 2.5 Key Complexity Overview

| Data Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Map | O(1) avg | O(1) avg | O(1) avg | O(1) avg | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(1) for min/max | O(n) | O(log n) | O(log n) | O(n) |
| Trie | — | O(m)** | O(m) | O(m) | O(n·m) |

*With a reference to the node. **m = length of the key string.

---

> **Practice Questions — Section 2**
> 1. Classify each: `[1,2,3,4]` (Python list), a family tree, a city road map, a dictionary.
> 2. Why is an array "static" even though Python lists can grow? (Hint: think about what happens internally.)
> 3. Name a situation where a non-linear data structure is unavoidable.

---

# 3. Core Data Structures

---

## 3.1 Array

### Definition and Real-World Applications

An **array** stores elements of the same type in **contiguous memory locations**, accessible via a numeric index. It is the most fundamental data structure.

```
Memory layout (array of integers [10, 20, 30, 40, 50]):

Index:   0     1     2     3     4
       ┌─────┬─────┬─────┬─────┬─────┐
Value: │ 10  │ 20  │ 30  │ 40  │ 50  │
       └─────┴─────┴─────┴─────┴─────┘
Addr:  1000  1004  1008  1012  1016   (4 bytes each for int)

element address = base_address + index × element_size
arr[3] = 1000 + 3 × 4 = 1012  → O(1) access
```

**Real-world applications:**
- Image pixels stored as a 2D array of RGB values
- Audio samples stored as a 1D array of floats
- Spreadsheet cells (2D array)
- Lookup tables (precomputed results by index)

### Operations and Complexities

| Operation | Time | Space | Notes |
|---|---|---|---|
| Access by index | O(1) | O(1) | Direct address calculation |
| Search (unsorted) | O(n) | O(1) | Must scan each element |
| Search (sorted) | O(log n) | O(1) | Binary search |
| Insert at end | O(1) amortized | O(1) | Occasional O(n) resize |
| Insert at index i | O(n) | O(1) | Must shift elements right |
| Delete at index i | O(n) | O(1) | Must shift elements left |
| Resize | O(n) | O(n) | Copy to new larger array |

### Python Implementation from Scratch

```python
class DynamicArray:
    """
    A dynamic array implementation similar to Python's built-in list.

    Internally uses a fixed-size array (via ctypes) that doubles in capacity
    when full, giving amortized O(1) append performance.
    """
    import ctypes

    def __init__(self) -> None:
        self._count    = 0      # Number of elements currently stored
        self._capacity = 1      # Current allocated capacity
        self._array    = self._make_array(self._capacity)

    def _make_array(self, capacity: int):
        """Allocate a raw C-style array of given capacity."""
        import ctypes
        return (capacity * ctypes.py_object)()

    def __len__(self) -> int:
        return self._count

    def __getitem__(self, index: int):
        """Access element at index. Supports negative indexing."""
        if index < 0:
            index += self._count
        if not (0 <= index < self._count):
            raise IndexError(f"Index {index} out of range")
        return self._array[index]

    def __setitem__(self, index: int, value) -> None:
        if not (0 <= index < self._count):
            raise IndexError(f"Index {index} out of range")
        self._array[index] = value

    def append(self, value) -> None:
        """Add element to end. Amortized O(1)."""
        if self._count == self._capacity:
            self._resize(2 * self._capacity)    # Double capacity when full
        self._array[self._count] = value
        self._count += 1

    def insert(self, index: int, value) -> None:
        """Insert value at index, shifting elements right. O(n)."""
        if not (0 <= index <= self._count):
            raise IndexError(f"Index {index} out of range")
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        # Shift elements right to make room
        for i in range(self._count, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._count += 1

    def delete(self, index: int) -> None:
        """Remove element at index, shifting elements left. O(n)."""
        if not (0 <= index < self._count):
            raise IndexError(f"Index {index} out of range")
        # Shift elements left to fill the gap
        for i in range(index, self._count - 1):
            self._array[i] = self._array[i + 1]
        self._count -= 1
        # Shrink array if only 1/4 full (prevents memory waste)
        if self._count == self._capacity // 4:
            self._resize(self._capacity // 2)

    def _resize(self, new_capacity: int) -> None:
        """Allocate new array of new_capacity and copy elements. O(n)."""
        new_array = self._make_array(new_capacity)
        for i in range(self._count):
            new_array[i] = self._array[i]
        self._array    = new_array
        self._capacity = new_capacity

    def __repr__(self) -> str:
        elements = [self._array[i] for i in range(self._count)]
        return f"DynamicArray({elements})"


# ── Example Usage ────────────────────────────────────────────────────────────
arr = DynamicArray()
for val in [10, 20, 30, 40]:
    arr.append(val)
print(arr)          # DynamicArray([10, 20, 30, 40])

arr.insert(2, 25)
print(arr)          # DynamicArray([10, 20, 25, 30, 40])

arr.delete(0)
print(arr)          # DynamicArray([20, 25, 30, 40])
print(arr[1])       # 25
```

### Built-in Python Equivalent

Python's `list` is a highly optimized dynamic array. Use it for all general-purpose sequential storage:

```python
# Python list — use this in practice
arr = [10, 20, 30, 40]
arr.append(50)          # O(1) amortized
arr.insert(2, 25)       # O(n)
arr.pop()               # O(1)  — remove last
arr.pop(0)              # O(n)  — remove first (shifts all)
arr[1]                  # O(1)  — access by index
25 in arr               # O(n)  — linear search

# For true fixed-size typed arrays (memory-efficient):
import array
typed_arr = array.array('i', [1, 2, 3, 4])   # 'i' = signed int

# For numerical arrays (use numpy in practice):
# import numpy as np
# np_arr = np.array([1, 2, 3, 4])
```

**Use the custom implementation when:** you need to understand the internals, or implement special behavior (e.g., a circular buffer, a bounded array).

### Advantages, Disadvantages, Use Cases

**Advantages:**
- O(1) random access — ideal when index-based lookup is frequent
- Cache-friendly — contiguous memory means good CPU cache utilization
- Simple and low overhead

**Disadvantages:**
- Insertion/deletion in the middle is O(n) due to shifting
- Static arrays waste space if over-allocated; resizing is expensive
- All elements must be the same size (in low-level languages)

**Best used when:** You have a fixed or slowly-changing dataset that you access frequently by index (image buffers, lookup tables, math vectors).

---

> **Practice Problems — Array**
> 1. Write a function `rotate_right(arr, k)` that rotates an array to the right by k positions in O(n) time and O(1) space.
> 2. Find the maximum sum of a contiguous subarray (Kadane's Algorithm).
> 3. Given a sorted array, remove duplicates in-place and return the new length.

---

## 3.2 Linked List

### Definition and Real-World Applications

A **linked list** is a linear data structure where elements (**nodes**) are stored at non-contiguous memory locations, each holding a value and a pointer to the next node. Unlike arrays, there is no index-based access — you must traverse from the head.

**Real-world applications:**
- Browser history (doubly linked list — back and forward)
- Music playlist navigation (circular linked list for loop mode)
- Memory allocators (OS free-block lists)
- Undo/Redo functionality in editors
- Implementing stacks and queues

### Visual Explanation

```
Singly Linked List:
head
 │
 ▼
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│  10  │  ●───┼───►│  20  │  ●───┼───►│  30  │ None │
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘
  Node 1               Node 2               Node 3

Doubly Linked List:
head                                              tail
 │                                                 │
 ▼                                                 ▼
┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐
│ None │  10  │  ●───┼───►│  ●   │  20  │  ●───┼───►│  ●   │  30  │ None │
└──────┴──────┴──────┘    └──────┴──────┴──────┘    └──────┴──────┴──────┘
 prev  data   next         prev   data   next         prev   data   next

Circular Singly Linked List:
head
 │
 ▼
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│  10  │  ●───┼───►│  20  │  ●───┼───►│  30  │  ●───┼──┐
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘  │
 ▲                                                       │
 └───────────────────────────────────────────────────────┘
```

### Operations and Complexities

| Operation | Singly | Doubly | Notes |
|---|---|---|---|
| Access by index | O(n) | O(n) | Must traverse from head |
| Search | O(n) | O(n) | Linear scan |
| Insert at head | O(1) | O(1) | Update head pointer |
| Insert at tail | O(1)* | O(1) | *If tail pointer maintained |
| Insert at middle | O(n) | O(n) | Find position, then O(1) link |
| Delete at head | O(1) | O(1) | Move head to next |
| Delete at tail | O(n) | O(1) | Singly needs to find prev |
| Delete given node | O(n) | O(1) | Doubly can use prev pointer |
| Space per node | O(1) + ptr | O(1) + 2 ptrs | Extra pointer overhead |

### Python Implementation — Singly Linked List

```python
from __future__ import annotations
from typing import Any, Iterator


class SLLNode:
    """A node in a singly linked list."""
    def __init__(self, data: Any) -> None:
        self.data: Any           = data
        self.next: SLLNode | None = None


class SinglyLinkedList:
    """
    Singly Linked List implementation.

    Maintains both head and tail pointers for O(1) append.
    Zero-indexed for intuitive use.
    """

    def __init__(self) -> None:
        self.head: SLLNode | None = None
        self.tail: SLLNode | None = None
        self._size: int           = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    # ── Insertion ─────────────────────────────────────────────────────────
    def prepend(self, data: Any) -> None:
        """Insert at the beginning. O(1)."""
        node      = SLLNode(data)
        node.next = self.head
        self.head = node
        if self.tail is None:       # First node is both head and tail
            self.tail = node
        self._size += 1

    def append(self, data: Any) -> None:
        """Insert at the end. O(1) — thanks to tail pointer."""
        node = SLLNode(data)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node        # Empty list: new node is also head
        self.tail  = node
        self._size += 1

    def insert_after(self, target_data: Any, new_data: Any) -> bool:
        """
        Insert new_data immediately after the first node containing target_data.
        Returns True if target was found, False otherwise. O(n).
        """
        current = self.head
        while current:
            if current.data == target_data:
                new_node       = SLLNode(new_data)
                new_node.next  = current.next
                current.next   = new_node
                if current == self.tail:
                    self.tail  = new_node   # Update tail if inserting after tail
                self._size += 1
                return True
            current = current.next
        return False

    # ── Deletion ──────────────────────────────────────────────────────────
    def delete_head(self) -> Any:
        """Remove and return the head element. O(1)."""
        if self.is_empty():
            raise IndexError("Delete from empty list")
        data      = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None        # List is now empty
        self._size -= 1
        return data

    def delete(self, target_data: Any) -> bool:
        """
        Remove the first node containing target_data.
        Returns True if found and deleted. O(n).
        """
        if self.is_empty():
            return False

        # Special case: deleting the head
        if self.head.data == target_data:
            self.delete_head()
            return True

        # Traverse to find the node just before the target
        prev    = self.head
        current = self.head.next
        while current:
            if current.data == target_data:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev    # Update tail if deleting last node
                self._size -= 1
                return True
            prev    = current
            current = current.next
        return False

    # ── Search & Access ───────────────────────────────────────────────────
    def search(self, target_data: Any) -> int:
        """Return index of first occurrence of target_data, or -1. O(n)."""
        current = self.head
        index   = 0
        while current:
            if current.data == target_data:
                return index
            current = current.next
            index  += 1
        return -1

    def __iter__(self) -> Iterator:
        current = self.head
        while current:
            yield current.data
            current = current.next

    # ── Utilities ─────────────────────────────────────────────────────────
    def reverse(self) -> None:
        """
        Reverse the list in-place. O(n) time, O(1) space.

        Technique: three-pointer walk — prev, current, next_node
        """
        prev    = None
        current = self.head
        self.tail = self.head           # Old head becomes new tail
        while current:
            next_node    = current.next # Save next
            current.next = prev         # Reverse the link
            prev         = current      # Advance prev
            current      = next_node    # Advance current
        self.head = prev                # prev is now the new head

    def __repr__(self) -> str:
        nodes = " → ".join(str(d) for d in self)
        return f"SLL: {nodes} → None"


# ── Example Usage ────────────────────────────────────────────────────────────
sll = SinglyLinkedList()
for val in [10, 20, 30, 40]:
    sll.append(val)

print(sll)              # SLL: 10 → 20 → 30 → 40 → None
sll.prepend(5)
print(sll)              # SLL: 5 → 10 → 20 → 30 → 40 → None
sll.insert_after(20, 25)
print(sll)              # SLL: 5 → 10 → 20 → 25 → 30 → 40 → None
sll.delete(25)
sll.reverse()
print(sll)              # SLL: 40 → 30 → 20 → 10 → 5 → None
```

### Python Implementation — Doubly Linked List

```python
from __future__ import annotations
from typing import Any


class DLLNode:
    """A node in a doubly linked list."""
    def __init__(self, data: Any) -> None:
        self.data: Any            = data
        self.prev: DLLNode | None = None
        self.next: DLLNode | None = None


class DoublyLinkedList:
    """
    Doubly Linked List — supports O(1) insert/delete at both ends
    and O(1) delete given a direct node reference.

    Uses sentinel (dummy) head and tail nodes to eliminate
    edge cases for empty lists and boundary operations.
    """

    def __init__(self) -> None:
        # Sentinel nodes — never hold real data
        self._head        = DLLNode(None)   # Dummy head
        self._tail        = DLLNode(None)   # Dummy tail
        self._head.next   = self._tail
        self._tail.prev   = self._head
        self._size: int   = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _insert_between(self, data: Any,
                         before: DLLNode, after: DLLNode) -> DLLNode:
        """
        Core helper: insert a new node between 'before' and 'after'. O(1).
        Both sentinels make this work uniformly for all positions.
        """
        node        = DLLNode(data)
        node.prev   = before
        node.next   = after
        before.next = node
        after.prev  = node
        self._size += 1
        return node

    def _delete_node(self, node: DLLNode) -> Any:
        """Remove a specific node. O(1) — given direct reference."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size    -= 1
        return node.data

    def append_left(self, data: Any) -> None:
        """Insert at the front. O(1)."""
        self._insert_between(data, self._head, self._head.next)

    def append_right(self, data: Any) -> None:
        """Insert at the back. O(1)."""
        self._insert_between(data, self._tail.prev, self._tail)

    def pop_left(self) -> Any:
        """Remove and return the front element. O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty list")
        return self._delete_node(self._head.next)

    def pop_right(self) -> Any:
        """Remove and return the back element. O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty list")
        return self._delete_node(self._tail.prev)

    def __iter__(self):
        current = self._head.next
        while current is not self._tail:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        nodes = " ⟺ ".join(str(d) for d in self)
        return f"DLL: ⊣ {nodes} ⊢"


# ── Example Usage ────────────────────────────────────────────────────────────
dll = DoublyLinkedList()
dll.append_right(10)
dll.append_right(20)
dll.append_right(30)
dll.append_left(5)
print(dll)              # DLL: ⊣ 5 ⟺ 10 ⟺ 20 ⟺ 30 ⊢
print(dll.pop_left())   # 5
print(dll.pop_right())  # 30
print(dll)              # DLL: ⊣ 10 ⟺ 20 ⊢
```

### Python Implementation — Circular Linked List

```python
class CircularLinkedList:
    """
    Circular Singly Linked List — the last node points back to head.
    Useful for round-robin scheduling, circular buffers, and game turns.
    """

    def __init__(self) -> None:
        self.head: SLLNode | None = None
        self._size: int           = 0

    def append(self, data: Any) -> None:
        """Insert at the end (before head). O(n) without tail pointer."""
        new_node = SLLNode(data)
        if not self.head:
            new_node.next = new_node    # Points to itself
            self.head     = new_node
        else:
            # Find the last node (the one pointing to head)
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next  = new_node
            new_node.next = self.head   # Close the circle
        self._size += 1

    def __iter__(self):
        """Iterate through all nodes exactly once."""
        if not self.head:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current is self.head:
                break

    def __repr__(self) -> str:
        nodes = " → ".join(str(d) for d in self)
        return f"CLL: {nodes} → (head)"


# ── Example: Round-Robin Scheduler ───────────────────────────────────────────
cll = CircularLinkedList()
for process in ["P1", "P2", "P3"]:
    cll.append(process)
print(cll)   # CLL: P1 → P2 → P3 → (head)
```

### Built-in Python Equivalent

```python
# Python's collections.deque is a doubly linked list optimized for
# O(1) operations at both ends — use it instead of a custom DLL.
from collections import deque

dll = deque()
dll.appendleft(10)      # O(1) — add to front
dll.append(20)          # O(1) — add to back
dll.popleft()           # O(1) — remove from front
dll.pop()               # O(1) — remove from back
dll[0]                  # O(1) — indexed access (unlike pure linked list!)

# Python's list is NOT a linked list — it's an array
# Use deque when you need frequent insertions/deletions at both ends
```

### Advantages, Disadvantages, Use Cases

**Advantages:**
- Dynamic size — no pre-allocation needed
- O(1) insertions and deletions at known positions
- Doubly linked list allows O(1) deletion of any node given its reference

**Disadvantages:**
- No O(1) random access — must traverse from head
- Extra memory for pointer(s) per node
- Poor cache performance — nodes may be scattered in memory
- No simple binary search without converting to array

**Best used when:** You frequently insert/delete at the front or middle, and random access is rare. Classic use case: LRU cache (doubly linked list + hash map).

---

> **Practice Problems — Linked List**
> 1. Detect if a linked list has a cycle (Floyd's Tortoise and Hare algorithm).
> 2. Find the middle element of a linked list in one pass (two-pointer technique).
> 3. Merge two sorted linked lists into one sorted linked list.
> 4. Reverse a linked list in groups of k.

---

## 3.3 Stack

### Definition and Real-World Applications

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle: the last element pushed is the first one popped. Think of a stack of plates — you add and remove from the top only.

```
LIFO Visualization:

  push(10) → push(20) → push(30)

  ┌──────┐        ┌──────┐        ┌──────┐
  │  10  │        │  20  │        │  30  │ ← TOP
  └──────┘        ├──────┤        ├──────┤
                  │  10  │        │  20  │
                  └──────┘        ├──────┤
                                  │  10  │
                                  └──────┘

  pop() returns 30, then 20, then 10
```

**Real-world applications:**
- Function call stack (how recursion works in every programming language)
- Undo/Redo operations (Ctrl+Z in editors)
- Browser back button
- Expression evaluation and syntax checking (balanced parentheses)
- Backtracking algorithms (DFS uses an implicit stack)
- Compiler: converting infix to postfix notation

### Operations and Complexities

| Operation | Time | Space | Description |
|---|---|---|---|
| push(item) | O(1) | O(1) | Add item to top |
| pop() | O(1) | O(1) | Remove and return top item |
| peek() | O(1) | O(1) | View top item without removing |
| is_empty() | O(1) | O(1) | Check if stack has no elements |
| size() | O(1) | O(1) | Number of elements |

### Python Implementation

```python
from typing import Any


class Stack:
    """
    Stack (LIFO) implemented using a Python list as the underlying array.

    The END of the list is treated as the top of the stack:
    - list.append() → push   → O(1) amortized
    - list.pop()    → pop    → O(1)
    This avoids the O(n) shifting cost of inserting/removing at index 0.
    """

    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Add item to the top of the stack. O(1) amortized."""
        self._data.append(item)

    def pop(self) -> Any:
        """Remove and return the top item. O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        """Return the top item without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        if not self._data:
            return "Stack: [empty]"
        items = " | ".join(str(x) for x in self._data)
        return f"Stack (bottom→top): [ {items} ]  ← TOP"


# ── Classic Application: Balanced Parentheses Checker ────────────────────────
def is_balanced(expression: str) -> bool:
    """
    Check if brackets in the expression are properly balanced.

    Time: O(n), Space: O(n)

    Examples:
      "{[()]}"   → True
      "{[(])}"   → False  (wrong closing order)
      "((("      → False  (unclosed brackets)
    """
    stack   = Stack()
    pairs   = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()   # Stack must be empty if all brackets closed


# ── Classic Application: Evaluate Postfix Expression ─────────────────────────
def evaluate_postfix(expr: str) -> float:
    """
    Evaluate a postfix (Reverse Polish Notation) expression.

    Postfix: "3 4 + 2 *" → (3 + 4) * 2 = 14
    No parentheses needed; operator precedence encoded in position.
    """
    stack = Stack()
    ops   = {'+', '-', '*', '/'}

    for token in expr.split():
        if token in ops:
            b = stack.pop()   # Second operand
            a = stack.pop()   # First operand
            if   token == '+': stack.push(a + b)
            elif token == '-': stack.push(a - b)
            elif token == '*': stack.push(a * b)
            elif token == '/': stack.push(a / b)
        else:
            stack.push(float(token))

    return stack.pop()


# ── Example Usage ────────────────────────────────────────────────────────────
s = Stack()
s.push(10); s.push(20); s.push(30)
print(s)                            # Stack (bottom→top): [ 10 | 20 | 30 ]  ← TOP
print(s.peek())                     # 30
print(s.pop())                      # 30
print(s)                            # Stack (bottom→top): [ 10 | 20 ]  ← TOP

print(is_balanced("{[()]}"))        # True
print(is_balanced("{[(])}"))        # False
print(evaluate_postfix("3 4 + 2 *")) # 14.0
```

### Built-in Python Equivalent

```python
# Python list works perfectly as a stack — no need for a custom class
stack = []
stack.append(10)    # push
stack.append(20)
top = stack[-1]     # peek
val = stack.pop()   # pop

# collections.deque is slightly faster for large stacks
from collections import deque
stack = deque()
stack.append(10)    # push
stack.pop()         # pop
```

### Advantages, Disadvantages, Use Cases

**Advantages:** All core operations O(1). Simple and predictable. Natural fit for LIFO problems.
**Disadvantages:** No random access. Can overflow if unbounded (call stack limit).
**Best used when:** LIFO ordering is needed: parsing, backtracking, expression evaluation, DFS traversal.

---

> **Practice Problems — Stack**
> 1. Implement `min_stack`: a stack that also supports `get_min()` in O(1) time.
> 2. Use a stack to sort another stack (no other data structures allowed).
> 3. Convert an infix expression (e.g., `a + b * c`) to postfix using a stack.

---

## 3.4 Queue

### Definition and Real-World Applications

A **queue** is a linear data structure following the **First In, First Out (FIFO)** principle: the first element enqueued is the first one dequeued. Think of a line at a ticket counter.

```
FIFO Visualization:

  enqueue(10) → enqueue(20) → enqueue(30)

  FRONT                          REAR
   │                              │
   ▼                              ▼
  ┌──────┬──────┬──────┐
  │  10  │  20  │  30  │
  └──────┴──────┴──────┘

  dequeue() → returns 10 (FRONT)
  FRONT                     REAR
   │                         │
   ▼                         ▼
  ┌──────┬──────┐
  │  20  │  30  │
  └──────┴──────┘
```

**Real-world applications:**
- Print spooling (print jobs served in order)
- CPU process scheduling (Round Robin)
- BFS graph traversal
- Message queues (Kafka, RabbitMQ)
- Network packet buffering

### 3.4.1 Simple Queue

```python
from collections import deque
from typing import Any


class Queue:
    """
    FIFO Queue backed by collections.deque for O(1) enqueue and dequeue.

    Why deque over list?
    list.pop(0) is O(n) — it shifts all remaining elements.
    deque.popleft() is O(1) — doubly linked list allows O(1) front removal.
    """

    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Add item to the rear of the queue. O(1)."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Remove and return the front item. O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def front(self) -> Any:
        """Return the front item without removing. O(1)."""
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._data[0]

    def rear(self) -> Any:
        """Return the rear item without removing. O(1)."""
        if self.is_empty():
            raise IndexError("rear of empty queue")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        items = " → ".join(str(x) for x in self._data)
        return f"Queue FRONT→REAR: [ {items} ]"
```

### 3.4.2 Circular Queue (Fixed-Size Ring Buffer)

```python
class CircularQueue:
    """
    Fixed-size Circular Queue using a ring buffer.

    Uses modular arithmetic to wrap around the array,
    avoiding the need to shift elements or waste space.

    Visual for capacity=5:
      Index:  0    1    2    3    4
             ┌────┬────┬────┬────┬────┐
             │ 30 │ 40 │    │ 10 │ 20 │
             └────┴────┴────┴────┴────┘
                        ▲         ▲
                       rear      front
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data     = [None] * capacity
        self._front    = 0
        self._rear     = -1
        self._size     = 0

    def enqueue(self, item: Any) -> None:
        """Add to rear. O(1)."""
        if self._size == self._capacity:
            raise OverflowError("Queue is full")
        self._rear          = (self._rear + 1) % self._capacity
        self._data[self._rear] = item
        self._size         += 1

    def dequeue(self) -> Any:
        """Remove from front. O(1)."""
        if self._size == 0:
            raise IndexError("Dequeue from empty queue")
        item           = self._data[self._front]
        self._front    = (self._front + 1) % self._capacity
        self._size    -= 1
        return item

    def is_full(self) -> bool:
        return self._size == self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size


# ── Example ───────────────────────────────────────────────────────────────────
cq = CircularQueue(4)
cq.enqueue(10); cq.enqueue(20); cq.enqueue(30)
print(cq.dequeue())   # 10  — front leaves
cq.enqueue(40)        # wraps around to index 0
cq.enqueue(50)        # now full
```

### 3.4.3 Priority Queue

```python
import heapq


class PriorityQueue:
    """
    Min-Priority Queue — always dequeues the item with the LOWEST priority value.
    For a max-priority queue, negate all priorities.

    Backed by Python's heapq (binary min-heap).
    enqueue: O(log n)
    dequeue: O(log n)
    peek:    O(1)
    """

    def __init__(self) -> None:
        self._heap: list[tuple[int, Any]] = []
        self._counter = 0   # Tiebreaker for equal priorities (FIFO order)

    def enqueue(self, item: Any, priority: int) -> None:
        """Add item with given priority. Lower number = higher priority."""
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def dequeue(self) -> Any:
        """Remove and return the highest-priority (lowest value) item."""
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Any:
        """Return highest-priority item without removing. O(1)."""
        if self.is_empty():
            raise IndexError("peek at empty priority queue")
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def __len__(self) -> int:
        return len(self._heap)


# ── Example: Task Scheduler ───────────────────────────────────────────────────
pq = PriorityQueue()
pq.enqueue("Low priority task",    priority=5)
pq.enqueue("Critical bug fix",     priority=1)
pq.enqueue("Medium priority task", priority=3)

while not pq.is_empty():
    print(pq.dequeue())
# Critical bug fix
# Medium priority task
# Low priority task
```

### 3.4.4 Deque (Double-Ended Queue)

```python
from collections import deque as PyDeque

# Python's collections.deque IS a deque — O(1) at both ends
dq = PyDeque()
dq.appendleft(10)   # Add to front
dq.append(20)       # Add to back
dq.popleft()        # Remove from front
dq.pop()            # Remove from back
dq.rotate(2)        # Rotate right by 2 positions (circular)

# Custom implementation for learning:
class Deque:
    """Double-ended queue using a doubly linked list (via Python deque)."""
    def __init__(self) -> None:
        self._data = PyDeque()

    def add_front(self, item: Any) -> None:
        self._data.appendleft(item)

    def add_rear(self, item: Any) -> None:
        self._data.append(item)

    def remove_front(self) -> Any:
        if not self._data:
            raise IndexError("remove from empty deque")
        return self._data.popleft()

    def remove_rear(self) -> Any:
        if not self._data:
            raise IndexError("remove from empty deque")
        return self._data.pop()

    def peek_front(self) -> Any:
        return self._data[0]

    def peek_rear(self) -> Any:
        return self._data[-1]
```

### Queue Types Comparison

| Type | Insertion | Deletion | Order | Use Case |
|---|---|---|---|---|
| Simple Queue | O(1) | O(1) | FIFO | BFS, print spooling |
| Circular Queue | O(1) | O(1) | FIFO (ring) | Audio/video buffering |
| Priority Queue | O(log n) | O(log n) | By priority | Dijkstra's, OS scheduling |
| Deque | O(1) | O(1) | Both ends | Sliding window, palindrome |

---

> **Practice Problems — Queue**
> 1. Implement a queue using two stacks.
> 2. Implement a stack using two queues.
> 3. Given a stream of integers, use a deque to find the maximum in every window of size k.
> 4. Simulate a printer queue: tasks arrive with a priority (1–9). Implement fair scheduling.

---

## 3.5 Binary Tree & Binary Search Tree

### Definition and Real-World Applications

A **tree** is a hierarchical non-linear data structure with a root node and subtrees of children nodes, with no cycles. A **Binary Tree** limits each node to at most two children (left and right).

A **Binary Search Tree (BST)** adds the ordering property:
- All nodes in the **left subtree** have values **less than** the parent
- All nodes in the **right subtree** have values **greater than** the parent

```
Binary Tree structure:

         10                ← root
        /  \
       5    20             ← level 1
      / \    \
     3   7   25            ← level 2
    /
   1                       ← level 3

Key Terms:
  Root:     10 (no parent)
  Leaf:     1, 7, 25 (no children)
  Height:   3 (longest path from root to leaf)
  Depth:    depth of node 7 = 2 (edges from root)
  Subtree:  the tree rooted at any node

BST Property Visualization:

         15
        /  \
       8    22
      / \   / \
     3  12 18  25
         \
          14

  In-order traversal (left→root→right): 3, 8, 12, 14, 15, 18, 22, 25
  → Always produces sorted output for a valid BST!
```

**Real-world applications:**
- Database indexing (B-Trees are extensions of BSTs)
- File system directories (each folder is a tree node)
- Expression trees in compilers
- DOM (Document Object Model) in web browsers
- Decision trees in machine learning

### Tree Terminology Quick Reference

```
       A           ← root, depth=0
      / \
     B   C         ← depth=1
    / \   \
   D   E   F       ← depth=2, D/E/F are leaves
        \
         G         ← depth=3, leaf

Height of tree = 3 (longest root-to-leaf path)
Height of node B = 2

Full Binary Tree:     Every node has 0 or 2 children
Complete Binary Tree: All levels full except last, last filled left to right
Perfect Binary Tree:  All internal nodes have 2 children, all leaves same depth
Balanced Binary Tree: Height difference between left and right subtrees ≤ 1
```

### Operations and Complexities (BST)

| Operation | Average (Balanced) | Worst (Skewed) | Notes |
|---|---|---|---|
| Search | O(log n) | O(n) | Skewed = linked list |
| Insert | O(log n) | O(n) | |
| Delete | O(log n) | O(n) | Three cases |
| Min/Max | O(log n) | O(n) | Leftmost / Rightmost |
| In-order traversal | O(n) | O(n) | Produces sorted output |
| Space | O(n) | O(n) | |

### Python Implementation — BST

```python
from __future__ import annotations
from typing import Any, Iterator


class BSTNode:
    """A node in a Binary Search Tree."""
    def __init__(self, key: int, value: Any = None) -> None:
        self.key:   int               = key
        self.value: Any               = value
        self.left:  BSTNode | None    = None
        self.right: BSTNode | None    = None


class BinarySearchTree:
    """
    Binary Search Tree implementation.

    Supports insert, search, delete, and all four traversals.
    No balancing — performance degrades to O(n) on sorted input.
    For balanced BST, see AVLTree (Section 3.6).
    """

    def __init__(self) -> None:
        self.root: BSTNode | None = None

    # ── Insertion ─────────────────────────────────────────────────────────
    def insert(self, key: int, value: Any = None) -> None:
        """Insert a key-value pair. Duplicate keys update the value. O(h)."""
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: BSTNode | None, key: int, value: Any) -> BSTNode:
        if node is None:
            return BSTNode(key, value)   # Found insertion point
        if key < node.key:
            node.left  = self._insert(node.left,  key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value           # Update existing key
        return node

    # ── Search ────────────────────────────────────────────────────────────
    def search(self, key: int) -> Any:
        """Return value for key, or None if not found. O(h)."""
        node = self._search(self.root, key)
        return node.value if node else None

    def _search(self, node: BSTNode | None, key: int) -> BSTNode | None:
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ── Deletion ──────────────────────────────────────────────────────────
    def delete(self, key: int) -> None:
        """
        Delete node with given key. O(h).

        Three cases:
        1. Node is a leaf → simply remove
        2. Node has one child → replace node with its child
        3. Node has two children → replace with in-order successor
           (smallest value in the right subtree), then delete successor
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node: BSTNode | None, key: int) -> BSTNode | None:
        if node is None:
            return None

        if key < node.key:
            node.left  = self._delete(node.left,  key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1 & 2: zero or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: two children — find in-order successor
            successor       = self._min_node(node.right)
            node.key        = successor.key
            node.value      = successor.value
            node.right      = self._delete(node.right, successor.key)

        return node

    def _min_node(self, node: BSTNode) -> BSTNode:
        """Find the leftmost (minimum) node in a subtree."""
        while node.left:
            node = node.left
        return node

    # ── Min / Max ─────────────────────────────────────────────────────────
    def minimum(self) -> int | None:
        if not self.root: return None
        return self._min_node(self.root).key

    def maximum(self) -> int | None:
        if not self.root: return None
        node = self.root
        while node.right:
            node = node.right
        return node.key

    # ── Traversals ────────────────────────────────────────────────────────
    def inorder(self) -> list[int]:
        """Left → Root → Right. Produces sorted output for BST. O(n)."""
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self) -> list[int]:
        """Root → Left → Right. Useful for copying/serializing trees. O(n)."""
        result = []
        def _preorder(node):
            if node:
                result.append(node.key)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self) -> list[int]:
        """Left → Right → Root. Used for deletion, expression trees. O(n)."""
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.key)
        _postorder(self.root)
        return result

    def level_order(self) -> list[list[int]]:
        """
        BFS traversal — level by level. O(n).
        Returns a list of lists, each inner list is one level.
        """
        from collections import deque
        if not self.root:
            return []
        result = []
        queue  = deque([self.root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.key)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result

    def height(self) -> int:
        """Return the height of the tree. O(n)."""
        def _height(node):
            if not node:
                return -1   # Height of empty tree is -1 (or 0 by some definitions)
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def __repr__(self) -> str:
        return f"BST: inorder={self.inorder()}, height={self.height()}"


# ── Example Usage ────────────────────────────────────────────────────────────
bst = BinarySearchTree()
for key in [15, 8, 22, 3, 12, 18, 25, 14]:
    bst.insert(key)

print(bst)
# BST: inorder=[3, 8, 12, 14, 15, 18, 22, 25], height=3

print(bst.level_order())
# [[15], [8, 22], [3, 12, 18, 25], [14]]

bst.delete(8)
print(bst.inorder())   # [3, 12, 14, 15, 18, 22, 25]
print(bst.minimum())   # 3
print(bst.maximum())   # 25
```

### Advantages, Disadvantages, Use Cases

**Advantages:**
- O(log n) search, insert, delete when balanced
- In-order traversal gives sorted output
- Naturally recursive structure makes algorithms elegant
- Supports floor, ceiling, rank, and range queries efficiently

**Disadvantages:**
- Degrades to O(n) on sorted or nearly-sorted input (becomes a linked list)
- No guaranteed balance without AVL/Red-Black tree overhead
- More memory than an array (pointers per node)

**Best used when:** You need dynamic sorted data with frequent search, insert, delete operations. Self-balancing variants (AVL, Red-Black) are preferred in production.

---

> **Practice Problems — BST**
> 1. Write a function `is_valid_bst(root)` that checks if a binary tree is a valid BST.
> 2. Find the k-th smallest element in a BST.
> 3. Find the Lowest Common Ancestor (LCA) of two nodes in a BST.
> 4. Convert a sorted array to a height-balanced BST.

---

## 3.6 AVL Tree

### Definition and Real-World Applications

An **AVL Tree** (Adelson-Velsky and Landis, 1962) is a **self-balancing Binary Search Tree** where the height difference (balance factor) between the left and right subtrees of any node is at most 1. This guarantee ensures O(log n) operations in all cases.

```
Balance Factor (BF) = height(left subtree) - height(right subtree)
Valid values: -1, 0, or +1. Anything outside this range triggers a rotation.

Unbalanced BST (inserting 1,2,3 into plain BST):     After AVL rebalancing:

  1                                                      2
   \                                                    / \
    2     ← BF of 1 is -2 (right-heavy)              1   3
     \
      3

Rotations:
  Left Rotation (LL case on right-heavy nodes)
  Right Rotation (RR case on left-heavy nodes)
  Left-Right Rotation (LR case)
  Right-Left Rotation (RL case)
```

### The Four Rotation Cases

```
Right Rotation (right-rotate at z):
      z                    y
     / \                  / \
    y   T4               x   z
   / \          →       /\   /\
  x   T3               T1 T2 T3 T4

Left Rotation (left-rotate at z):
    z                        y
   / \                      / \
  T1  y          →         z   x
     / \                  /\   /\
    T2  x                T1 T2 T3 T4

Left-Right: Left-rotate left child, then right-rotate root.
Right-Left: Right-rotate right child, then left-rotate root.
```

### Python Implementation

```python
from __future__ import annotations


class AVLNode:
    def __init__(self, key: int) -> None:
        self.key:    int              = key
        self.left:   AVLNode | None   = None
        self.right:  AVLNode | None   = None
        self.height: int              = 1    # Height of this node's subtree


class AVLTree:
    """
    AVL Tree — self-balancing BST.
    All operations guaranteed O(log n) because height ≤ 1.44·log₂(n).
    """

    def _height(self, node: AVLNode | None) -> int:
        return node.height if node else 0

    def _balance_factor(self, node: AVLNode | None) -> int:
        if not node: return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node: AVLNode) -> None:
        node.height = 1 + max(self._height(node.left),
                               self._height(node.right))

    # ── Rotations ─────────────────────────────────────────────────────────
    def _rotate_right(self, z: AVLNode) -> AVLNode:
        """Right rotation — fixes left-heavy imbalance."""
        y        = z.left
        T3       = y.right
        y.right  = z
        z.left   = T3
        self._update_height(z)
        self._update_height(y)
        return y   # y is the new subtree root

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        """Left rotation — fixes right-heavy imbalance."""
        y        = z.right
        T2       = y.left
        y.left   = z
        z.right  = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _rebalance(self, node: AVLNode) -> AVLNode:
        """
        Rebalance the node if its balance factor is outside [-1, 1].
        Determines which of the four rotation cases applies.
        """
        self._update_height(node)
        bf = self._balance_factor(node)

        # Case 1: Left-Left (right rotate)
        if bf > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)

        # Case 2: Left-Right (left rotate child, then right rotate root)
        if bf > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Case 3: Right-Right (left rotate)
        if bf < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)

        # Case 4: Right-Left (right rotate child, then left rotate root)
        if bf < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node   # Already balanced

    # ── Insert ────────────────────────────────────────────────────────────
    def insert(self, root: AVLNode | None, key: int) -> AVLNode:
        """Insert key and rebalance. Returns new root. O(log n)."""
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left  = self.insert(root.left,  key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root   # Duplicate key ignored

        return self._rebalance(root)

    # ── Delete ────────────────────────────────────────────────────────────
    def delete(self, root: AVLNode | None, key: int) -> AVLNode | None:
        """Delete key and rebalance. Returns new root. O(log n)."""
        if not root:
            return None
        if key < root.key:
            root.left  = self.delete(root.left,  key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:  return root.right
            if not root.right: return root.left
            # Replace with in-order successor
            successor  = root.right
            while successor.left:
                successor = successor.left
            root.key   = successor.key
            root.right = self.delete(root.right, successor.key)

        return self._rebalance(root)

    # ── Traversal ─────────────────────────────────────────────────────────
    def inorder(self, root: AVLNode | None, result: list | None = None) -> list[int]:
        if result is None: result = []
        if root:
            self.inorder(root.left,  result)
            result.append(root.key)
            self.inorder(root.right, result)
        return result


# ── Example Usage ────────────────────────────────────────────────────────────
avl  = AVLTree()
root = None
for key in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, key)

# Without balancing: inserting 10,20,30,40,50 gives a skewed tree of height 4
# With AVL: height is kept at floor(log2(6)) = 2 or 3
print(avl.inorder(root))          # [10, 20, 25, 30, 40, 50]
print(f"Root: {root.key}")        # Root: 30  (balanced, not 10!)
print(f"Height: {root.height}")   # Height: 3
```

### AVL vs Plain BST

| Property | Plain BST | AVL Tree |
|---|---|---|
| Height (balanced input) | O(log n) | O(log n) |
| Height (sorted input) | O(n) — degenerate | O(log n) — always |
| Search worst case | O(n) | O(log n) |
| Insert overhead | None | Rebalance: up to O(log n) rotations |
| Practical use | Simple/educational | When read-heavy, balanced critical |

---

> **Practice Problems — AVL Tree**
> 1. Verify: insert 1, 2, 3, 4, 5, 6, 7 into an AVL tree. Draw the tree after each rotation.
> 2. What is the maximum number of rotations needed after a single insertion into an AVL tree?
> 3. What is the minimum number of nodes in an AVL tree of height h? (Fibonacci relationship!)

---

## 3.7 Heap

### Definition and Real-World Applications

A **heap** is a complete binary tree stored as an array that satisfies the **heap property**:
- **Max-Heap:** Every parent node is ≥ its children. Root holds the maximum.
- **Min-Heap:** Every parent node is ≤ its children. Root holds the minimum.

```
Max-Heap as a tree and its array representation:

         100
        /    \
       80      60
      /  \    /  \
     40   30 20   10

Array: [100, 80, 60, 40, 30, 20, 10]
Index:   0    1   2   3   4   5   6

Parent-Child index relationships (0-indexed):
  Parent of index i   = (i - 1) // 2
  Left child of i     = 2*i + 1
  Right child of i    = 2*i + 2

So: parent(3) = (3-1)//2 = 1  → arr[1]=80  ✓ (80 ≥ 40)
    left(1)   = 2*1+1    = 3  → arr[3]=40  ✓
    right(1)  = 2*1+2    = 4  → arr[4]=30  ✓
```

**Real-world applications:**
- Priority queues (OS process scheduling, Dijkstra's algorithm)
- Heap Sort
- Top-K elements problems
- Median maintenance (two heaps)
- Graph algorithms (Prim's MST)

### Operations and Complexities

| Operation | Time | Notes |
|---|---|---|
| peek min/max | O(1) | Root is always min or max |
| insert | O(log n) | Sift up to restore heap property |
| extract min/max | O(log n) | Sift down after removing root |
| build heap | O(n) | Not O(n log n) — due to mathematical sum |
| heapify (single) | O(log n) | Sift up or down |
| search | O(n) | Heap gives no search ordering |

### Python Implementation — Min-Heap

```python
class MinHeap:
    """
    Min-Heap from scratch.

    The smallest element is always at index 0 (the root).
    Push: add to end, sift up.    O(log n)
    Pop:  swap root with last, remove last, sift down.  O(log n)
    """

    def __init__(self) -> None:
        self._data: list[int] = []

    def _parent(self, i: int) -> int:  return (i - 1) // 2
    def _left(self,   i: int) -> int:  return 2 * i + 1
    def _right(self,  i: int) -> int:  return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def push(self, value: int) -> None:
        """Insert value into the heap. O(log n)."""
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def _sift_up(self, i: int) -> None:
        """
        Bubble the element at index i upward until heap property is restored.
        Compare with parent; swap if smaller than parent.
        """
        while i > 0:
            p = self._parent(i)
            if self._data[i] < self._data[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def pop(self) -> int:
        """Remove and return the minimum element. O(log n)."""
        if not self._data:
            raise IndexError("pop from empty heap")

        # Swap root with last element
        self._swap(0, len(self._data) - 1)
        minimum = self._data.pop()   # Remove old root (now at end)
        if self._data:
            self._sift_down(0)       # Restore heap property from root
        return minimum

    def _sift_down(self, i: int) -> None:
        """
        Push the element at index i downward until heap property is restored.
        Swap with the smaller of the two children.
        """
        n = len(self._data)
        while True:
            smallest = i
            l, r     = self._left(i), self._right(i)

            if l < n and self._data[l] < self._data[smallest]:
                smallest = l
            if r < n and self._data[r] < self._data[smallest]:
                smallest = r

            if smallest == i:
                break           # Heap property satisfied
            self._swap(i, smallest)
            i = smallest

    def peek(self) -> int:
        """Return minimum without removing. O(1)."""
        if not self._data:
            raise IndexError("peek at empty heap")
        return self._data[0]

    @classmethod
    def from_list(cls, values: list[int]) -> 'MinHeap':
        """
        Build a heap from an existing list. O(n) — more efficient than
        n individual pushes which would be O(n log n).

        Floyd's algorithm: sift down from the last non-leaf upward.
        """
        h = cls()
        h._data = list(values)
        # Last non-leaf index = (n // 2) - 1
        for i in range(len(h._data) // 2 - 1, -1, -1):
            h._sift_down(i)
        return h

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"MinHeap({self._data})"


# ── Example Usage ────────────────────────────────────────────────────────────
heap = MinHeap()
for val in [5, 3, 8, 1, 9, 2]:
    heap.push(val)

print(heap)            # MinHeap([1, 3, 2, 5, 9, 8])
print(heap.peek())     # 1
print(heap.pop())      # 1
print(heap.pop())      # 2
print(heap.pop())      # 3

# Build heap in O(n)
heap2 = MinHeap.from_list([10, 4, 7, 1, 6, 3])
print(heap2)           # MinHeap([1, 4, 3, 10, 6, 7])
```

### Max-Heap using negation

```python
import heapq

# Python's heapq is a min-heap. For max-heap, negate values.
max_heap: list[int] = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -20)

max_val = -heapq.heappop(max_heap)   # 30 — negate back
print(max_val)

# For objects, use a custom key:
import heapq
tasks = [(5, "low priority"), (1, "urgent"), (3, "medium")]
heapq.heapify(tasks)
print(heapq.heappop(tasks))   # (1, 'urgent') — lowest number = highest priority
```

### Classic Application: Top-K Elements

```python
def top_k_largest(nums: list[int], k: int) -> list[int]:
    """
    Find the k largest elements using a min-heap of size k.

    Maintain a min-heap of the k largest seen so far.
    If new element > heap minimum, replace minimum.

    Time: O(n log k)  — much better than O(n log n) sort for small k
    Space: O(k)
    """
    import heapq
    min_heap: list[int] = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)   # Pop min, push num

    return sorted(min_heap, reverse=True)


print(top_k_largest([3, 1, 5, 12, 2, 11], k=3))   # [12, 11, 5]
```

---

> **Practice Problems — Heap**
> 1. Find the median of a data stream in O(log n) per element using two heaps.
> 2. Merge k sorted arrays into one sorted array using a min-heap.
> 3. Given an array, find if it represents a valid max-heap.

---

## 3.8 Trie (Prefix Tree)

### Definition and Real-World Applications

A **Trie** (from re**trie**val) is a tree-like data structure where each node represents a single character of a string. Strings are stored by sharing common prefixes, making prefix-based operations extremely fast.

```
Trie storing: "car", "card", "care", "cat", "dog", "dot"

root
├── c
│   └── a
│       ├── r ← "car" (end)
│       │   ├── d ← "card" (end)
│       │   └── e ← "care" (end)
│       └── t ← "cat" (end)
└── d
    └── o
        ├── g ← "dog" (end)
        └── t ← "dot" (end)

Searching "care": root→c→a→r→e → found ✓
Searching "ca":   root→c→a → NOT an end node → word not in trie
Prefix "ca":      root→c→a → exists → words: "car","card","care","cat"
```

**Real-world applications:**
- Autocomplete (Google Search, IDE code completion)
- Spell checkers
- IP routing tables (prefix matching)
- Word games (Boggle, Scrabble solvers)
- DNA sequence search

### Operations and Complexities

| Operation | Time | Space | Notes |
|---|---|---|---|
| Insert word | O(m) | O(m·alphabet) | m = word length |
| Search word | O(m) | O(1) | |
| Starts-with prefix | O(m) | O(1) | |
| Delete word | O(m) | O(1) | |
| All words with prefix | O(m + n) | O(n) | n = number of results |

### Python Implementation

```python
from __future__ import annotations


class TrieNode:
    """A single node in a Trie."""
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool          = False
        self.word_count: int               = 0    # How many words end here


class Trie:
    """
    Prefix Tree (Trie) implementation.

    Each path from root to an end-of-word node spells out a stored word.
    Uses a dictionary for children (vs fixed 26-char array) to handle
    arbitrary alphabets and save memory on sparse tries.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie. O(m) where m = len(word).

        Walk character by character, creating nodes as needed.
        Mark the final node as an end of word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word_count    += 1

    def search(self, word: str) -> bool:
        """Return True if word exists in the trie. O(m)."""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Return True if any inserted word starts with prefix. O(m)."""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode | None:
        """Navigate to the node at the end of prefix, or None if not found."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix: str) -> list[str]:
        """
        Return all words in the trie that start with prefix.
        O(m + n) where n = total characters in all matching words.
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        results: list[str] = []
        self._collect_words(node, prefix, results)
        return results

    def _collect_words(self, node: TrieNode, current: str,
                        results: list[str]) -> None:
        """DFS to collect all words from this node onward."""
        if node.is_end_of_word:
            results.append(current)
        for char, child in node.children.items():
            self._collect_words(child, current + char, results)

    def delete(self, word: str) -> bool:
        """
        Delete a word from the trie. O(m).
        Only removes nodes that are no longer needed by other words.
        """
        return self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        """Recursive deletion. Returns True if current node should be deleted."""
        if depth == len(word):
            if not node.is_end_of_word:
                return False    # Word not in trie
            node.is_end_of_word = False
            return len(node.children) == 0   # Delete if leaf

        char = word[depth]
        if char not in node.children:
            return False

        should_delete_child = self._delete(node.children[char], word, depth + 1)
        if should_delete_child:
            del node.children[char]
            return not node.is_end_of_word and len(node.children) == 0

        return False

    def count_words_with_prefix(self, prefix: str) -> int:
        """Return the count of words that start with prefix."""
        return len(self.autocomplete(prefix))

    def __repr__(self) -> str:
        all_words = self.autocomplete("")
        return f"Trie({all_words})"


# ── Example Usage ────────────────────────────────────────────────────────────
trie = Trie()
for word in ["car", "card", "care", "cat", "dog", "dot", "do"]:
    trie.insert(word)

print(trie.search("card"))           # True
print(trie.search("car"))            # True
print(trie.search("ca"))             # False  (not a complete word)
print(trie.starts_with("ca"))        # True   (prefix exists)
print(trie.autocomplete("ca"))       # ['car', 'card', 'care', 'cat']
print(trie.autocomplete("do"))       # ['do', 'dog', 'dot']

trie.delete("card")
print(trie.search("card"))           # False
print(trie.search("car"))            # True  (car still exists)
```

---

> **Practice Problems — Trie**
> 1. Implement a spell checker using a Trie. Given a dictionary and a query word, suggest corrections.
> 2. Find the longest common prefix among an array of strings using a Trie.
> 3. Given a list of words, implement word search in a 2D grid using a Trie.

---

## 3.9 Hash Table / Hash Map

### Definition and Real-World Applications

A **hash table** maps **keys** to **values** using a **hash function** that converts a key to an array index. This achieves O(1) average-case lookups, insertions, and deletions.

```
Hash Table — how it works:

Key → hash_function(key) → index → store value at that index

hash("apple") % 7 = 3    → arr[3] = "fruit"
hash("banana") % 7 = 5   → arr[5] = "fruit"
hash("grape") % 7 = 3    → COLLISION! index 3 already taken

     0: []
     1: []
     2: []
     3: [("apple","fruit"), ("grape","fruit")]  ← chaining handles collision
     4: []
     5: [("banana","fruit")]
     6: []
```

**Real-world applications:**
- Python dictionaries and sets
- Database index tables
- Caching (e.g., Memcached, Redis key-value store)
- Counting word frequencies
- Deduplication
- Cryptographic hashing (SHA-256, MD5 — different purpose)

### Collision Resolution Strategies

```
1. Separate Chaining:
   Each slot holds a linked list (or dynamic array) of all key-value pairs
   that hash to that index.
   → Simple; degrades to O(n) if all keys collide (bad hash function)

2. Open Addressing — Linear Probing:
   If slot i is taken, try i+1, i+2, ... (wrapping around)
   → Cache-friendly; clustering can degrade performance

3. Open Addressing — Quadratic Probing:
   Try i+1², i+2², i+3², ... to reduce primary clustering

4. Open Addressing — Double Hashing:
   Use a second hash function for the probe step
   → Best distribution among open addressing methods

5. Robin Hood Hashing:
   During insertion, steal slots from "rich" keys (those far from home)
   to give to "poor" keys — reduces maximum probe length
```

### Python Implementation — Hash Map with Separate Chaining

```python
from typing import Any


class HashMap:
    """
    Hash Map using Separate Chaining for collision resolution.

    Each bucket is a list of (key, value) pairs.
    Automatically resizes when load factor exceeds 0.75 to maintain O(1) avg.

    Load factor = number of entries / number of buckets
    """

    _INITIAL_CAPACITY = 8
    _LOAD_FACTOR_MAX  = 0.75

    def __init__(self) -> None:
        self._capacity: int                            = self._INITIAL_CAPACITY
        self._size:     int                            = 0
        self._buckets:  list[list[tuple[Any, Any]]]   = [[] for _ in range(self._capacity)]

    def _hash(self, key: Any) -> int:
        """Map key to a bucket index using Python's built-in hash."""
        return hash(key) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update key-value pair. O(1) average.

        If key exists, update its value.
        Otherwise, append a new (key, value) pair to the bucket.
        Resize if load factor exceeds threshold.
        """
        index  = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)    # Update existing key
                return

        bucket.append((key, value))         # New key
        self._size += 1

        # Resize if load factor exceeded
        if self._size / self._capacity > self._LOAD_FACTOR_MAX:
            self._resize()

    def get(self, key: Any, default: Any = None) -> Any:
        """
        Retrieve value for key. O(1) average.
        Returns default if key not found.
        """
        index  = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return default

    def delete(self, key: Any) -> bool:
        """Remove key-value pair. Returns True if key existed. O(1) average."""
        index  = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True

        return False

    def contains(self, key: Any) -> bool:
        """Return True if key exists in the map. O(1) average."""
        return self.get(key, _sentinel := object()) is not _sentinel

    def _resize(self) -> None:
        """
        Double capacity and rehash all existing entries. O(n).
        Called when load factor exceeds threshold to keep operations O(1) avg.
        """
        old_buckets    = self._buckets
        self._capacity = self._capacity * 2
        self._size     = 0
        self._buckets  = [[] for _ in range(self._capacity)]

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)   # Rehash into new buckets

    def keys(self) -> list[Any]:
        return [k for bucket in self._buckets for k, _ in bucket]

    def values(self) -> list[Any]:
        return [v for bucket in self._buckets for _, v in bucket]

    def items(self) -> list[tuple[Any, Any]]:
        return [(k, v) for bucket in self._buckets for k, v in bucket]

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"{{{items}}}"


# ── Example Usage ────────────────────────────────────────────────────────────
hm = HashMap()
hm.put("name", "Alice")
hm.put("age",  30)
hm.put("city", "Cairo")

print(hm.get("name"))        # Alice
print(hm.get("country"))     # None
print(len(hm))               # 3

hm.put("age", 31)            # Update
print(hm.get("age"))         # 31

hm.delete("city")
print(hm.keys())             # ['name', 'age']
```

### Hash Map with Open Addressing (Linear Probing)

```python
class HashMapOpenAddressing:
    """
    Hash Map using Linear Probing (Open Addressing).

    No linked lists — all entries stored directly in the array.
    Uses a "tombstone" sentinel for deleted slots to avoid
    breaking probe chains during search.

    Better cache performance than chaining due to contiguous memory.
    """
    _EMPTY   = object()   # Sentinel for empty slots
    _DELETED = object()   # Sentinel for deleted slots (tombstone)

    def __init__(self, capacity: int = 8) -> None:
        self._capacity = capacity
        self._size     = 0
        self._keys:   list = [self._EMPTY] * capacity
        self._values: list = [self._EMPTY] * capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        """Insert or update. O(1) average, O(n) worst case."""
        if self._size / self._capacity > 0.6:
            self._resize()

        index = self._hash(key)
        while self._keys[index] not in (self._EMPTY, self._DELETED):
            if self._keys[index] == key:
                self._values[index] = value   # Update
                return
            index = (index + 1) % self._capacity   # Linear probe

        self._keys[index]   = key
        self._values[index] = value
        self._size += 1

    def get(self, key: Any, default: Any = None) -> Any:
        """Retrieve value for key. O(1) average."""
        index = self._hash(key)
        while self._keys[index] is not self._EMPTY:
            if self._keys[index] == key:
                return self._values[index]
            index = (index + 1) % self._capacity
        return default

    def _resize(self) -> None:
        """Expand and rehash. O(n)."""
        old_keys, old_vals = self._keys, self._values
        self._capacity    *= 2
        self._size         = 0
        self._keys         = [self._EMPTY] * self._capacity
        self._values       = [self._EMPTY] * self._capacity
        for k, v in zip(old_keys, old_vals):
            if k not in (self._EMPTY, self._DELETED):
                self.put(k, v)
```

### Built-in Python Equivalent

```python
# Python's dict is a highly optimized hash map — use it in production
d = {}
d["key"] = "value"          # put
val = d.get("key", None)    # get with default
del d["key"]                # delete
"key" in d                  # O(1) membership test

# Python's set is a hash set (keys only)
s = {1, 2, 3}
s.add(4)
s.remove(2)
3 in s                      # O(1)

# Counter — specialized hash map for counting
from collections import Counter
counts = Counter("aabbccc")   # {'c':3, 'a':2, 'b':2}

# defaultdict — auto-initializes missing keys
from collections import defaultdict
graph = defaultdict(list)
graph["A"].append("B")       # No KeyError even if "A" didn't exist
```

### Hash Table Complexity Summary

| Operation | Average | Worst | Notes |
|---|---|---|---|
| put/insert | O(1) | O(n) | Worst if all keys collide |
| get/search | O(1) | O(n) | |
| delete | O(1) | O(n) | |
| Space | O(n) | O(n) | Load factor affects constant |

---

> **Practice Problems — Hash Table**
> 1. Given an array, find the first non-repeating character using a hash map.
> 2. Implement an LRU Cache using a hash map + doubly linked list.
> 3. Group anagrams together from a list of strings.
> 4. Two Sum: given an array and target, find two indices that sum to the target.

---

## 3.10 Graph

### Definition

A **graph** G = (V, E) consists of:
- **V** = a set of **vertices** (nodes)
- **E** = a set of **edges** connecting pairs of vertices

Graphs model any pairwise relationship: road networks, social connections, web links, dependencies, electrical circuits, and more.

---

### 3.10.1 Graph Classification

#### By Edge Direction

```
Undirected Graph                   Directed Graph (Digraph)
   A --- B                            A ──► B
   |     |                            │     │
   C --- D                            ▼     ▼
                                      C ──► D
  A-B same as B-A                  A→B ≠ B→A (may not even exist)
  Models: friendships, roads       Models: web links, dependencies, Twitter follows
```

#### By Edge Weights

```
Unweighted                         Weighted
  A - B                              A ──5── B
  |   |                              |       |
  C - D                              3       2
                                     |       |
  All edges "equal"                  C ──8── D
  Models: social networks         Models: road distances, network latency
```

#### By Cycles

```
Cyclic Graph                       Acyclic Graph (DAG — Directed Acyclic Graph)
  A → B                              A → B → D
  ↑   ↓                              ↓       ↑
  D ← C                              C ──────┘
  Cycle: A→B→C→D→A               No cycles: useful for task dependencies,
                                  compilation order, version control
```

#### By Density

| Type | Edge Count | Representation | Example |
|---|---|---|---|
| **Sparse** | E ≈ O(V) | Adjacency List | Road network, social graph |
| **Dense** | E ≈ O(V²) | Adjacency Matrix | Complete graph, dense pipeline |

#### Other Important Types

| Type | Description | Example |
|---|---|---|
| Simple graph | No self-loops, no multiple edges | Most common type |
| Multigraph | Multiple edges between same pair | Airline routes (different airlines) |
| Complete graph | Every pair of vertices connected | K_n: n vertices, n(n-1)/2 edges |
| Bipartite graph | Vertices split into 2 sets, edges only cross-set | Job-applicant matching |
| Tree | Acyclic connected graph | File system |
| Forest | Acyclic (possibly disconnected) graph | Multiple trees |

---

### 3.10.2 Graph Representations

#### Adjacency Matrix

```
Graph:          Adjacency Matrix (0-indexed, 4 vertices):
  0 ──► 1
  │     │         0  1  2  3
  ▼     ▼     0 [ 0, 1, 1, 0 ]
  2 ──► 3     1 [ 0, 0, 0, 1 ]
              2 [ 0, 0, 0, 1 ]
              3 [ 0, 0, 0, 0 ]

  matrix[i][j] = 1 means edge from i to j
  Space: O(V²) — fine for dense graphs, wasteful for sparse

Weighted version: matrix[i][j] = weight (0 or ∞ if no edge)
```

#### Adjacency List

```
Same graph as above:
  0: [1, 2]
  1: [3]
  2: [3]
  3: []

  Space: O(V + E) — much more efficient for sparse graphs
  Most algorithms use this representation
```

### Python Implementations

```python
from collections import defaultdict, deque
from typing import Iterator


class GraphMatrix:
    """
    Directed/Undirected weighted graph using an Adjacency Matrix.

    Best for: dense graphs (E ≈ V²), O(1) edge lookup.
    Space: O(V²)
    """

    def __init__(self, vertices: int, directed: bool = True) -> None:
        self.V        = vertices
        self.directed = directed
        # Initialize with 0 (no edge). Use float('inf') for weighted graphs.
        self.matrix: list[list[int]] = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Add edge u→v (and v→u if undirected)."""
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0

    def has_edge(self, u: int, v: int) -> bool:
        return self.matrix[u][v] != 0

    def neighbors(self, u: int) -> list[int]:
        return [v for v in range(self.V) if self.matrix[u][v] != 0]

    def __repr__(self) -> str:
        header = "   " + "  ".join(str(i) for i in range(self.V))
        rows   = [f"{i}: {self.matrix[i]}" for i in range(self.V)]
        return header + "\n" + "\n".join(rows)


class GraphList:
    """
    Directed/Undirected weighted graph using an Adjacency List.

    Best for: sparse graphs (most real-world graphs).
    Space: O(V + E)

    Adjacency list format:
      self.adj[u] = [(v1, w1), (v2, w2), ...]   for weighted
      self.adj[u] = [v1, v2, ...]                for unweighted
    """

    def __init__(self, directed: bool = True, weighted: bool = False) -> None:
        self.directed = directed
        self.weighted = weighted
        self.adj: dict[int, list] = defaultdict(list)
        self.vertices: set[int]   = set()

    def add_vertex(self, v: int) -> None:
        self.vertices.add(v)
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Add edge u→v. For undirected, also adds v→u."""
        self.vertices.update([u, v])
        edge = (v, weight) if self.weighted else v
        self.adj[u].append(edge)
        if not self.directed:
            rev_edge = (u, weight) if self.weighted else u
            self.adj[v].append(rev_edge)

    def neighbors(self, u: int) -> list:
        """Return neighbors of u (as vertex ids)."""
        if self.weighted:
            return [v for v, _ in self.adj[u]]
        return list(self.adj[u])

    def neighbor_weights(self, u: int) -> list[tuple[int, int]]:
        """For weighted graphs: return [(neighbor, weight), ...] list."""
        return list(self.adj[u]) if self.weighted else [(v, 1) for v in self.adj[u]]

    def __repr__(self) -> str:
        lines = [f"Graph(directed={self.directed}, weighted={self.weighted})"]
        for v in sorted(self.vertices):
            lines.append(f"  {v}: {self.adj[v]}")
        return "\n".join(lines)
```

---

### 3.10.3 Graph Traversal: BFS and DFS

```python
# ── BFS — Breadth-First Search ────────────────────────────────────────────────
def bfs(graph: GraphList, start: int) -> list[int]:
    """
    BFS from start node — explores level by level.
    Finds shortest path (fewest edges) in unweighted graphs.

    Time:  O(V + E)
    Space: O(V)   — visited set + queue
    """
    visited = {start}
    queue   = deque([start])
    order   = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_levels(graph: GraphList, start: int) -> list[list[int]]:
    """
    BFS returning nodes grouped by their level (distance from start).
    Level 0 = [start], Level 1 = direct neighbors, etc.
    """
    visited = {start}
    queue   = deque([[start]])
    levels  = []

    while queue:
        level = queue.popleft()
        levels.append(level)
        next_level = []
        for node in level:
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)
        if next_level:
            queue.append(next_level)

    return levels


# ── DFS — Depth-First Search ──────────────────────────────────────────────────
def dfs_recursive(graph: GraphList, start: int,
                  visited: set | None = None) -> list[int]:
    """
    DFS from start — explores as deep as possible before backtracking.

    Time:  O(V + E)
    Space: O(V)   — visited set + recursion call stack
    """
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))

    return order


def dfs_iterative(graph: GraphList, start: int) -> list[int]:
    """
    Iterative DFS using an explicit stack.
    Avoids Python's recursion limit for very deep graphs.
    """
    visited = set()
    stack   = [start]
    order   = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Push in reverse order for consistent left-to-right traversal
            for neighbor in reversed(graph.neighbors(node)):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


# ── Example Usage ────────────────────────────────────────────────────────────
g = GraphList(directed=False)
for u, v in [(0,1),(0,2),(1,3),(1,4),(2,5)]:
    g.add_edge(u, v)

print(bfs(g, 0))            # [0, 1, 2, 3, 4, 5]
print(dfs_recursive(g, 0))  # [0, 1, 3, 4, 2, 5]
print(bfs_levels(g, 0))     # [[0], [1, 2], [3, 4, 5]]
```

---

### 3.10.4 Cycle Detection

```python
# ── Cycle Detection in Undirected Graph (DFS) ─────────────────────────────────
def has_cycle_undirected(graph: GraphList) -> bool:
    """
    Detect a cycle in an undirected graph using DFS.

    Key idea: if we visit a neighbor that is already visited AND
    is not the parent of the current node, a cycle exists.

    Time: O(V + E), Space: O(V)
    """
    visited = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:        # Back edge found — cycle!
                return True
        return False

    # Handle disconnected graphs
    for v in graph.vertices:
        if v not in visited:
            if dfs(v, -1):
                return True
    return False


# ── Cycle Detection in Directed Graph (DFS with 3-color marking) ──────────────
def has_cycle_directed(graph: GraphList) -> bool:
    """
    Detect a cycle in a directed graph using DFS with three states:
      WHITE (0): not yet visited
      GRAY  (1): currently in the DFS stack (being processed)
      BLACK (2): fully processed

    A cycle exists if we encounter a GRAY node — it means we've found
    a back edge to an ancestor in the current DFS path.

    Time: O(V + E), Space: O(V)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph.vertices}

    def dfs(node: int) -> bool:
        color[node] = GRAY       # Mark as "in progress"
        for neighbor in graph.neighbors(node):
            if color[neighbor] == GRAY:   # Back edge → cycle!
                return True
            if color[neighbor] == WHITE:  # Not yet visited
                if dfs(neighbor):
                    return True
        color[node] = BLACK      # Fully processed
        return False

    return any(dfs(v) for v in graph.vertices if color[v] == WHITE)


# ── Examples ──────────────────────────────────────────────────────────────────
# Undirected with cycle: 0-1-2-0
g_cycle = GraphList(directed=False)
for u, v in [(0,1),(1,2),(2,0)]:
    g_cycle.add_edge(u, v)
print(has_cycle_undirected(g_cycle))    # True

# Directed DAG (no cycle)
dag = GraphList(directed=True)
for u, v in [(0,1),(1,2),(0,2)]:
    dag.add_edge(u, v)
print(has_cycle_directed(dag))          # False

# Directed with cycle: 0→1→2→0
g_dir_cycle = GraphList(directed=True)
for u, v in [(0,1),(1,2),(2,0)]:
    g_dir_cycle.add_edge(u, v)
print(has_cycle_directed(g_dir_cycle))  # True
```

---

### 3.10.5 Topological Sort (for DAGs)

```python
def topological_sort_dfs(graph: GraphList) -> list[int]:
    """
    Topological Sort using DFS + stack.

    Produces a linear ordering of vertices such that for every
    directed edge u→v, u appears before v in the ordering.

    Only valid for Directed Acyclic Graphs (DAGs).
    Use case: task scheduling, build systems (make, npm), course prerequisites.

    Time: O(V + E), Space: O(V)
    """
    visited = set()
    stack   = []    # We push nodes AFTER all their neighbors are processed

    def dfs(node: int) -> None:
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)   # Push after fully exploring all descendants

    for v in graph.vertices:
        if v not in visited:
            dfs(v)

    return stack[::-1]   # Reverse: first pushed = last in topological order


def topological_sort_kahn(graph: GraphList) -> list[int] | None:
    """
    Topological Sort using Kahn's Algorithm (BFS-based).

    Uses in-degree counts:
    1. Start with all nodes that have in-degree 0 (no prerequisites).
    2. Process each, decrementing the in-degree of their neighbors.
    3. When a neighbor's in-degree reaches 0, add it to the queue.

    Returns None if graph has a cycle (result won't contain all vertices).

    Time: O(V + E), Space: O(V)
    """
    # Calculate in-degree for each vertex
    in_degree = {v: 0 for v in graph.vertices}
    for u in graph.vertices:
        for v in graph.neighbors(u):
            in_degree[v] = in_degree.get(v, 0) + 1

    # Start with all vertices that have no incoming edges
    queue  = deque([v for v, deg in in_degree.items() if deg == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.neighbors(node):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result doesn't include all vertices, there's a cycle
    return result if len(result) == len(graph.vertices) else None


# ── Example: Course Prerequisites ─────────────────────────────────────────────
# To take course 3 you need 2, to take 2 you need 0 and 1, etc.
courses = GraphList(directed=True)
for prereq, course in [(0, 2), (1, 2), (2, 3), (1, 3)]:
    courses.add_edge(prereq, course)

order = topological_sort_kahn(courses)
print(f"Course order: {order}")   # e.g. [0, 1, 2, 3]
```

---

### 3.10.6 Dijkstra's Shortest Path Algorithm

```python
import heapq

def dijkstra(graph: GraphList, source: int
             ) -> tuple[dict[int, float], dict[int, int | None]]:
    """
    Dijkstra's Algorithm — Single-Source Shortest Paths.

    Finds shortest path from source to all other vertices
    in a WEIGHTED graph with NON-NEGATIVE edge weights.

    Algorithm:
    1. Initialize source distance = 0, all others = ∞
    2. Use a min-heap to always process the closest unvisited vertex
    3. For each vertex, relax (update) distances to its neighbors
    4. Mark vertex as "finalized" when popped from heap

    Time:  O((V + E) log V) with binary heap
    Space: O(V + E)

    ⚠️  Does NOT work with negative edge weights. Use Bellman-Ford instead.
    """
    dist: dict[int, float]       = {v: float('inf') for v in graph.vertices}
    prev: dict[int, int | None]  = {v: None for v in graph.vertices}
    dist[source] = 0

    # Min-heap: (distance, vertex)
    heap = [(0, source)]

    while heap:
        curr_dist, u = heapq.heappop(heap)

        # Skip if we already found a shorter path (stale entry)
        if curr_dist > dist[u]:
            continue

        for v, weight in graph.neighbor_weights(u):
            new_dist = dist[u] + weight

            if new_dist < dist[v]:       # Relaxation step
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))

    return dist, prev


def reconstruct_path(prev: dict, source: int, target: int) -> list[int]:
    """Reconstruct shortest path from source to target using prev dict."""
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev.get(node)
    path.reverse()
    return path if path[0] == source else []


# ── Example ───────────────────────────────────────────────────────────────────
wg = GraphList(directed=False, weighted=True)
for u, v, w in [(0,1,4),(0,2,1),(1,3,1),(2,1,2),(2,3,5),(3,4,3)]:
    wg.add_edge(u, v, w)

distances, predecessors = dijkstra(wg, source=0)
print(f"Distances from 0: {distances}")
# {0:0, 1:3, 2:1, 3:4, 4:7}
print(f"Path 0→4: {reconstruct_path(predecessors, 0, 4)}")
# [0, 2, 1, 3, 4]
```

---

### 3.10.7 Minimum Spanning Tree: Kruskal's Algorithm

```python
def kruskal(vertices: int, edges: list[tuple[int,int,int]]
            ) -> tuple[list[tuple], int]:
    """
    Kruskal's MST Algorithm.

    Greedy approach: sort edges by weight, add cheapest edge
    that doesn't create a cycle. Uses Union-Find for cycle detection.

    Best for: sparse graphs (E << V²)
    Time:  O(E log E) dominated by sorting
    Space: O(V)
    """
    # ── Union-Find with path compression + union by rank ──────────────────
    parent = list(range(vertices))
    rank   = [0] * vertices

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])   # Path compression
        return parent[x]

    def union(x: int, y: int) -> bool:
        rx, ry = find(x), find(y)
        if rx == ry:
            return False    # Already in same component — would create cycle
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True

    # ── Main Algorithm ────────────────────────────────────────────────────
    edges.sort(key=lambda e: e[2])   # Sort by weight ascending
    mst_edges    = []
    total_weight = 0

    for u, v, w in edges:
        if union(u, v):              # Add edge if it doesn't create a cycle
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == vertices - 1:   # MST complete (V-1 edges)
                break

    return mst_edges, total_weight


# ── Example ───────────────────────────────────────────────────────────────────
edges_list = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
mst, total = kruskal(4, edges_list)
print(f"MST edges: {mst}")     # [(2,3,4), (0,3,5), (0,1,10)]
print(f"Total weight: {total}") # 19
```

---

### 3.10.8 Minimum Spanning Tree: Prim's Algorithm

```python
def prim(graph: GraphList, start: int = 0) -> tuple[list[tuple], int]:
    """
    Prim's MST Algorithm.

    Greedy approach: grow a single tree by always adding the cheapest
    edge that connects a tree vertex to a non-tree vertex.

    Best for: dense graphs (E ≈ V²) — O(V²) with array, O(E log V) with heap
    Time (with min-heap): O((V + E) log V)
    Space: O(V + E)

    Key difference from Kruskal's:
    - Prim's builds ONE connected tree (good for dense graphs).
    - Kruskal's processes edges globally (good for sparse graphs).
    """
    visited      = {start}
    mst_edges    = []
    total_weight = 0

    # Min-heap: (weight, from_vertex, to_vertex)
    heap = [(w, start, v) for v, w in graph.neighbor_weights(start)]
    heapq.heapify(heap)

    while heap and len(visited) < len(graph.vertices):
        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue    # Skip: v already in the tree

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        # Add all edges from v to unvisited vertices
        for neighbor, w in graph.neighbor_weights(v):
            if neighbor not in visited:
                heapq.heappush(heap, (w, v, neighbor))

    return mst_edges, total_weight


# ── Example ───────────────────────────────────────────────────────────────────
pg = GraphList(directed=False, weighted=True)
for u, v, w in [(0,1,2),(0,3,6),(1,2,3),(1,3,8),(1,4,5),(2,4,7),(3,4,9)]:
    pg.add_edge(u, v, w)

mst_p, weight_p = prim(pg, start=0)
print(f"MST: {mst_p}")
print(f"Total MST weight: {weight_p}")   # 16
```

### Graph Algorithm Complexity Summary

| Algorithm | Time | Space | Works On | Notes |
|---|---|---|---|---|
| BFS | O(V+E) | O(V) | Unweighted | Shortest path (fewest edges) |
| DFS | O(V+E) | O(V) | Any | Cycle detection, topo sort |
| Cycle Detection (undirected) | O(V+E) | O(V) | Undirected | Parent-tracking DFS |
| Cycle Detection (directed) | O(V+E) | O(V) | Directed | 3-color DFS |
| Topological Sort (DFS) | O(V+E) | O(V) | DAG | DFS + reverse stack |
| Topological Sort (Kahn's) | O(V+E) | O(V) | DAG | In-degree BFS |
| Dijkstra's | O((V+E)log V) | O(V+E) | Weighted, non-neg | Shortest path |
| Kruskal's MST | O(E log E) | O(V) | Weighted undirected | Sparse graphs |
| Prim's MST | O((V+E)log V) | O(V+E) | Weighted undirected | Dense graphs |
| Bellman-Ford | O(VE) | O(V) | Weighted, neg OK | Detects neg cycles |

### Adjacency Matrix vs Adjacency List

| Operation | Matrix O | List O | Notes |
|---|---|---|---|
| Space | O(V²) | O(V+E) | List wins for sparse graphs |
| Check edge (u,v) | O(1) | O(degree(u)) | Matrix wins |
| List all edges | O(V²) | O(V+E) | List wins |
| All neighbors of u | O(V) | O(degree(u)) | List wins |
| Add vertex | O(V²) | O(1) | List wins |
| Add edge | O(1) | O(1) | Same |

**Rule of thumb:** Use Adjacency List for almost all graph problems. Use Adjacency Matrix only when the graph is dense or you need very frequent O(1) edge existence checks.

---

> **Practice Problems — Graph**
> 1. Find all connected components in an undirected graph.
> 2. Determine if a graph is bipartite (can be 2-colored) using BFS.
> 3. Find the shortest path in an unweighted graph using BFS.
> 4. Given a list of prerequisites `[[1,0],[2,0],[3,1],[3,2]]`, determine if all courses can be finished (cycle detection in directed graph).
> 5. Implement Floyd-Warshall Algorithm for all-pairs shortest paths.
> 6. Find all bridges (critical edges) in an undirected graph.

---

# 4. Time Complexity Analysis Guide

## 4.1 How to Analyze Data Structure Operations

When analyzing the time complexity of operations on a data structure, follow this systematic approach:

### Step 1 — Identify the Primitive Operations
Count the operations that take constant time: comparisons, assignments, arithmetic, pointer follows.

### Step 2 — Express in Terms of Input Size
Use `n` for the number of elements stored. For strings use `m` for length.

### Step 3 — Apply Big-O Rules
- Drop constants: `3n → O(n)`
- Drop lower-order terms: `n² + n → O(n²)`
- Nested loops multiply: O(n) × O(n) = O(n²)
- Sequential independent loops add: O(n) + O(m) = O(n + m)

### Step 4 — Consider Best / Average / Worst Cases

```
Hash Map get():
  Best case:   O(1) — key hashes to an empty slot or head of a short chain
  Average:     O(1) — with good hash function and load factor ≤ 0.75
  Worst case:  O(n) — all keys hash to the same bucket (terrible hash function)

BST search():
  Best case:   O(1) — target is the root
  Average:     O(log n) — balanced tree
  Worst case:  O(n) — degenerate (skewed) tree from sorted insertions
```

### Step 5 — Identify Amortized Complexity Where Applicable

```python
# Dynamic Array append():
# Most appends: O(1) — just place at next index
# Occasional append: O(n) — must resize (copy all elements)

# Amortized analysis:
# After n appends, total work = n + n/2 + n/4 + ... = 2n = O(n)
# So PER OPERATION amortized cost = O(n)/n = O(1)
```

## 4.2 Master Comparison Table

### Core Data Structures

| Data Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| **Array (fixed)** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Dynamic Array** | O(1) | O(n) | O(1) amort. | O(n) | O(n) |
| **Singly Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Doubly Linked List** | O(n) | O(n) | O(1) | O(1)** | O(n) |
| **Stack (array)** | O(n) | O(n) | O(1) amort. | O(1) | O(n) |
| **Queue (deque)** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Priority Queue (heap)** | O(1)*** | O(n) | O(log n) | O(log n) | O(n) |
| **Hash Map** | O(1) avg | O(1) avg | O(1) avg | O(1) avg | O(n) |
| **BST (unbalanced)** | O(n) wc | O(n) wc | O(n) wc | O(n) wc | O(n) |
| **BST (balanced/AVL)** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap (min/max)** | O(1)*** | O(n) | O(log n) | O(log n) | O(n) |
| **Trie** | O(m) | O(m) | O(m) | O(m) | O(n·m) |

*With reference to node or head/tail. **Given direct node reference. ***Only for min/max.

### Graph Algorithms

| Algorithm | Time | Space | Best For |
|---|---|---|---|
| BFS | O(V + E) | O(V) | Shortest path (unweighted) |
| DFS | O(V + E) | O(V) | Cycle detection, topo sort |
| Dijkstra's (binary heap) | O((V+E) log V) | O(V+E) | Shortest path (non-neg weights) |
| Bellman-Ford | O(V·E) | O(V) | Shortest path (negative weights) |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| Topological Sort | O(V + E) | O(V) | DAG ordering |
| Kruskal's MST | O(E log E) | O(V) | MST on sparse graphs |
| Prim's MST | O((V+E) log V) | O(V+E) | MST on dense graphs |

### Graph Representations

| | Adjacency Matrix | Adjacency List |
|---|---|---|
| Space | O(V²) | O(V + E) |
| Check edge u→v | O(1) | O(degree) |
| Enumerate neighbors of u | O(V) | O(degree(u)) |
| Add edge | O(1) | O(1) |
| Add vertex | O(V²) | O(1) |
| Best for | Dense graphs | Sparse graphs (most real cases) |

## 4.3 Common Patterns and Their Complexities

```
Pattern                              Complexity
─────────────────────────────────────────────────
Single loop over n elements           O(n)
Nested loops (n × n)                  O(n²)
Halving the search space each step    O(log n)
Recursion on halved input:
  T(n) = T(n/2) + O(1)               O(log n)
  T(n) = 2T(n/2) + O(n)             O(n log n)
  T(n) = T(n-1) + O(n)              O(n²)
Generating all subsets                O(2ⁿ)
Generating all permutations           O(n!)
BFS/DFS on graph                      O(V + E)
Heap operations                       O(log n)
Hash table operations (avg)           O(1)
```

## 4.4 Best Practices for Data Structure Selection

```
Ask these questions when choosing a data structure:

1. WHAT OPERATIONS are most frequent?
   → Search-heavy?  → Hash Map or balanced BST
   → Insert/Delete? → Linked List, Hash Map
   → Min/Max often? → Heap
   → Prefix search? → Trie

2. IS ORDER IMPORTANT?
   → Sorted order needed?  → BST, sorted array
   → FIFO order?           → Queue
   → LIFO order?           → Stack
   → Priority order?       → Heap

3. HOW BIG IS THE DATA?
   → Few elements (< 100)? → Any structure; simplicity wins
   → Millions of elements? → Space efficiency matters; avoid O(n²) space

4. IS RANDOM ACCESS NEEDED?
   → Yes: array/hash map
   → No: linked list is fine

5. ARE THERE RANGE QUERIES?
   → Find all keys between A and B? → Balanced BST (O(log n + k))
   → Not possible with hash map

6. IS MEMORY A CONSTRAINT?
   → Avoid pointers (linked structures have overhead per node)
   → Arrays are more memory-efficient per element
```

---

# 5. When to Use Which Data Structure

## 5.1 Decision Guide

```
Your data is...
│
├── A sequence of items accessed by position?
│   └── Use: list (Python) / dynamic array
│       Unless: frequent insert/delete at front → use deque
│
├── A key-value mapping?
│   └── Use: dict (Python) / hash map
│       Unless: need sorted keys → use sorted dict / BST
│
├── Unique items only?
│   └── Use: set (Python) / hash set
│
├── Ordered with frequent insertions/deletions at arbitrary positions?
│   └── Use: doubly linked list
│
├── LIFO ordering (last in, first out)?
│   └── Use: list.append/pop or deque
│
├── FIFO ordering (first in, first out)?
│   └── Use: collections.deque
│
├── Priority-based access (always get the min/max)?
│   └── Use: heapq / priority queue
│
├── Prefix-based string queries?
│   └── Use: Trie
│
├── Hierarchical relationships?
│   └── Use: Tree (BST, AVL, etc.)
│
└── Pairwise relationships?
    └── Use: Graph (adjacency list)
```

## 5.2 Master Summary Table

| Use Case | Recommended Structure | Python Built-in |
|---|---|---|
| Random access by index | Dynamic Array | `list` |
| Frequent front insertions | Doubly Linked List | `collections.deque` |
| LIFO (undo, parsing) | Stack | `list` with append/pop |
| FIFO (BFS, scheduling) | Queue | `collections.deque` |
| Priority processing | Heap/Priority Queue | `heapq` |
| Fast key lookup | Hash Map | `dict` |
| Fast membership test | Hash Set | `set` |
| Sorted dynamic data | Balanced BST | `sortedcontainers.SortedList` |
| Top-K elements | Min-Heap of size K | `heapq.nlargest` |
| Prefix/autocomplete | Trie | Custom implementation |
| Network/relationship modeling | Graph (adj list) | Custom / `networkx` |
| Shortest path (unweighted) | BFS on graph | Custom BFS |
| Shortest path (weighted) | Dijkstra's + heap | Custom / `networkx` |
| Task dependency ordering | DAG + Topo Sort | Custom |
| Spanning tree | Kruskal's / Prim's | Custom |
| LRU Cache | Hash Map + DLL | `functools.lru_cache` |
| Counting occurrences | Hash Map | `collections.Counter` |
| Range queries on sorted data | Balanced BST | `sortedcontainers` |

## 5.3 Interview Quick-Reference Cheat Sheet

```
"Find if element exists in large dataset"
  → Hash Set O(1) avg

"Find k-th largest/smallest"
  → Min-Heap of size k  O(n log k)

"Process items in order of arrival"
  → Queue (deque)

"Undo/redo / function call simulation"
  → Stack

"Autocomplete / word prefix"
  → Trie

"Shortest path on a map"
  → Dijkstra's Algorithm

"Minimum connections to connect all cities"
  → MST: Kruskal's or Prim's

"Task ordering with dependencies"
  → Topological Sort on DAG

"Find cycle in code dependency graph"
  → DFS cycle detection

"Real-time median from a stream"
  → Two Heaps (max-heap + min-heap)

"Frequently accessed recently used items"
  → LRU Cache (Hash Map + Doubly Linked List)

"Count frequency of each word"
  → Hash Map / Counter

"Sorted insert / floor / ceiling queries"
  → Balanced BST / SortedList
```

---

# 6. Further Reading & Resources

## Books

**Beginner–Intermediate:**
- *Data Structures and Algorithms in Python* — Goodrich, Tamassia, Goldwasser. The most comprehensive Python-focused textbook; rigorous and complete.
- *Grokking Algorithms* — Aditya Bhargava. Visual, intuitive, beginner-friendly. Best first book.
- *Problem Solving with Algorithms and Data Structures Using Python* — Bradley Miller & David Ranum (also free at `runestone.academy`).

**Intermediate–Advanced:**
- *Introduction to Algorithms (CLRS)* — Cormen, Leiserson, Rivest, Stein. The definitive reference. Dense but authoritative.
- *The Algorithm Design Manual* — Steven Skiena. Excellent for connecting theory to real-world problems.
- *Advanced Data Structures* — Peter Brass. Deep coverage of advanced trees, heaps, and more.

## Online Courses

- **MIT 6.006 Introduction to Algorithms** — Free on OpenCourseWare. Lecture videos + problem sets.
- **Coursera: Data Structures and Algorithms Specialization** — UC San Diego. Well-paced and hands-on.
- **Stanford: Algorithms on Graphs** — Coursera. Focused graph coverage.
- **CS50 on edX** — Harvard's intro course, excellent fundamentals.

## Practice Platforms

| Platform | Best For |
|---|---|
| [LeetCode](https://leetcode.com) | Interview prep; problems tagged by data structure |
| [HackerRank](https://hackerrank.com) | Structured learning paths per topic |
| [Codeforces](https://codeforces.com) | Competitive programming |
| [Visualgo](https://visualgo.net) | Animated visualizations of every structure here |
| [CS Academy](https://csacademy.com) | Interactive graph visualizations |

## Visualization Tools

- **VisuAlgo** (visualgo.net) — Live animations for arrays, linked lists, stacks, queues, sorting, BST, AVL, heap, trie, graph algorithms.
- **Algorithm Visualizer** (algorithm-visualizer.org) — Code + step-by-step animation.
- **Data Structure Visualizations** — University of San Francisco (cs.usfca.edu/~galles/visualization/)

## Python Libraries for Production

```python
# Sorted containers (BST-equivalent in pure Python)
# pip install sortedcontainers
from sortedcontainers import SortedList, SortedDict, SortedSet

# Graph algorithms
# pip install networkx
import networkx as nx
G = nx.DiGraph()
G.add_edge('A', 'B', weight=4)
nx.shortest_path(G, 'A', 'B', weight='weight')

# NumPy for efficient array operations
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Efficient counter
from collections import Counter, defaultdict, deque, OrderedDict

# Priority queue (heapq is built-in)
import heapq
```

## Recommended Learning Path

```
Week 1:   Arrays, Strings, Python list internals
Week 2:   Linked Lists (Singly, Doubly) — implement from scratch
Week 3:   Stack and Queue — implement + classic problems
Week 4:   Hash Table — implement + collision resolution
Week 5:   Binary Trees — traversals + recursive thinking
Week 6:   BST — insert, delete, search, all operations
Week 7:   Heap — build from scratch + heap sort + top-K
Week 8:   Graph basics — representations, BFS, DFS
Week 9:   Graph algorithms — Dijkstra's, cycle detection
Week 10:  Graph algorithms — MST, topological sort
Week 11:  Trie + advanced hashing
Week 12:  AVL Trees + balanced BST concepts
Week 13+: Advanced: Segment Trees, Fenwick Trees, Disjoint Sets,
          B-Trees, Skip Lists, Bloom Filters
```

## Key Python Standard Library Modules

```python
# Everything you need for data structures in Python:

from collections import (
    deque,          # Doubly-ended queue — O(1) both ends
    defaultdict,    # Dict with default factory
    Counter,        # Counting hash map
    OrderedDict,    # Dict remembering insertion order
    namedtuple,     # Lightweight immutable record
    ChainMap,       # Multiple dicts as one view
)

import heapq            # Min-heap operations on lists
import bisect           # Binary search + sorted insertion on lists
import array            # Typed arrays (more memory-efficient than list)
import functools        # lru_cache for memoization
import itertools        # Combinatorial iterators (combinations, permutations)
from typing import (    # Type hints for cleaner code
    Any, Optional, Iterator, Generator,
    TypeVar, Generic
)
```

---

## Common Interview Pattern → Data Structure Mapping

| Pattern | Structures Used | Time Complexity |
|---|---|---|
| Two Sum | Hash Set | O(n) |
| Sliding Window | Deque / Hash Map | O(n) |
| Top-K Frequent | Heap + Hash Map | O(n log k) |
| Word Prefix / Autocomplete | Trie | O(m) per query |
| LRU Cache | Hash Map + Doubly Linked List | O(1) per op |
| Balanced Parentheses | Stack | O(n) |
| Level-Order Tree Traversal | Queue (BFS) | O(n) |
| Detect Cycle in Graph | DFS + color / Union-Find | O(V+E) |
| Course Schedule | DAG + Topological Sort | O(V+E) |
| Network Delay (Dijkstra's) | Graph + Min-Heap | O((V+E) log V) |
| Serialize/Deserialize Tree | BFS / DFS + Queue | O(n) |
| Median from Data Stream | Two Heaps | O(log n) per insert |
| Range Sum Query | Fenwick Tree / Segment Tree | O(log n) |

---

*End of Data Structures Learning Material — Version 1.0*

*This document covers beginner-to-intermediate data structures. Advanced topics (Segment Trees, Fenwick Trees, Disjoint Set Union, Skip Lists, B-Trees, Bloom Filters, Red-Black Trees, Suffix Arrays) are natural next steps after mastering everything here.*
