# Algorithms: A Comprehensive Learning Guide
### From Beginner to Intermediate

> **How to use this guide:** This guide follows a deliberate **6-phase learning roadmap** rather than a topic-by-topic list. Each phase builds directly on the skills from the one before it, so working through the sections in order will give you the smoothest learning curve. If you already know the basics, jump to any section using the Table of Contents — each section is still self-contained with runnable code.

---

## The 6-Phase Learning Roadmap

```
Phase 1 → Graph Traversal Core        (BFS, DFS)
Phase 2 → Core Algorithmic Techniques (Binary Search, Two Pointers, Sliding Window)
Phase 3 → Graph Algorithms            (Topological Sort, Dijkstra's, Bellman-Ford, Kruskal's, Prim's)
Phase 4 → Greedy Algorithms           (Activity Selection, Fractional Knapsack)
Phase 5 → Dynamic Programming         (Fibonacci, 0/1 Knapsack, LCS)
Phase 6 → Backtracking                (N-Queens, Subsets)
```

**Why this order?** BFS and DFS are primitives used everywhere else in this guide — graph algorithms, tree problems, backtracking, and cycle detection all assume you're comfortable with them, so they come first. Binary Search, Two Pointers, and Sliding Window come next because they reward pattern recognition over heavy theory, building problem-solving speed early. With traversal and pattern recognition in place, the full graph algorithms (Phase 3) extend BFS/DFS into complete systems: topological ordering, shortest paths, and minimum spanning trees. Greedy algorithms (Phase 4) become intuitive once you've seen graph optimization and ordering problems firsthand. Dynamic Programming (Phase 5) is deliberately placed later because it demands solid recursion skills and comfort with problem decomposition — both of which the earlier phases build. Backtracking closes the guide because it leans on DFS and recursion while being conceptually simple but computationally heavy, making it a natural capstone.

---

## Table of Contents

1. [Introduction to Algorithms](#1-introduction-to-algorithms)
2. [Types and Classification of Algorithms](#2-types-and-classification-of-algorithms)
3. [How to Analyze Time Complexity](#3-how-to-analyze-time-complexity)
4. [Sorting Algorithms](#4-sorting-algorithms)
   - Bubble Sort, Selection Sort, Insertion Sort
   - Merge Sort, Quick Sort, Heap Sort
   - Counting Sort, Radix Sort
5. [Searching Algorithms](#5-searching-algorithms)
   - Linear Search *(Binary Search has moved to Section 7 — see Phase 2)*
6. [Graph Traversal Core](#6-graph-traversal-core) — *Phase 1*
   - BFS, DFS
7. [Core Algorithmic Techniques](#7-core-algorithmic-techniques) — *Phase 2*
   - Binary Search, Binary Search on the Answer, Two Pointers, Sliding Window
8. [Graph Algorithms](#8-graph-algorithms) — *Phase 3*
   - Topological Sort, Dijkstra's, Bellman-Ford, Kruskal's, Prim's
9. [Greedy Algorithms](#9-greedy-algorithms) — *Phase 4*
   - Activity Selection, Fractional Knapsack
10. [Dynamic Programming](#10-dynamic-programming) — *Phase 5*
    - Fibonacci, 0/1 Knapsack, LCS
11. [Backtracking](#11-backtracking) — *Phase 6*
    - N-Queens, Subsets Generation
12. [Further Reading & Resources](#12-further-reading--resources)

---

# 1. Introduction to Algorithms

## 1.1 Definition and Importance

An **algorithm** is a finite, well-defined sequence of instructions that takes an input, processes it through a series of steps, and produces a correct output. Think of it as a recipe: given ingredients (input), follow the steps (instructions), and get a dish (output).

**Why do algorithms matter?**

- **Efficiency:** The difference between a poor and a great algorithm can mean the difference between a program that runs in milliseconds versus one that runs for days — on the same data.
- **Scalability:** An algorithm that works on 100 items may completely collapse on 1,000,000 items if poorly designed.
- **Universality:** Algorithms underpin everything from search engines and social media feeds to GPS navigation and medical imaging.
- **Problem Solving:** Learning algorithms trains you to break complex problems into manageable steps — a skill that transfers to all areas of engineering and science.

```
Real-world examples:
  Google Search    → Ranking algorithms (PageRank)
  GPS Navigation   → Shortest path algorithms (Dijkstra's)
  Netflix          → Recommendation algorithms
  Compression      → Huffman coding
  Fraud Detection  → Classification algorithms
```

## 1.2 Characteristics of a Good Algorithm

A well-designed algorithm should have these properties:

| Property | Description | Example |
|---|---|---|
| **Correctness** | Produces the right output for all valid inputs | Sorting [3,1,2] always gives [1,2,3] |
| **Finiteness** | Terminates in a finite number of steps | No infinite loops |
| **Definiteness** | Each step is precisely and unambiguously defined | No vague instructions |
| **Input** | Has zero or more well-defined inputs | Can accept an empty list |
| **Output** | Produces at least one output | Returns a sorted array |
| **Efficiency** | Uses minimal time and memory resources | Prefers O(n log n) over O(n²) |
| **Generality** | Solves a class of problems, not just one instance | Sorts any list, not just [3,1,2] |

---

> **Practice Questions — Section 1**
> 1. Can you think of an everyday task (making tea, finding a book) and write it as a step-by-step algorithm? Check that it has all 7 properties above.
> 2. Why might two algorithms that are both "correct" still differ in value?
> 3. If an algorithm runs forever on some input, which property does it violate?

---

# 2. Types and Classification of Algorithms

Algorithms can be classified in multiple overlapping ways. Understanding these categories helps you choose the right tool for a problem.

## 2.1 By Implementation Approach

### Recursive vs. Iterative

**Recursive** algorithms solve a problem by having the function call itself on smaller sub-problems.
**Iterative** algorithms solve a problem using loops.

```python
# Recursive factorial
def factorial_recursive(n: int) -> int:
    if n == 0:          # base case
        return 1
    return n * factorial_recursive(n - 1)   # recursive case

# Iterative factorial
def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

| Aspect | Recursive | Iterative |
|---|---|---|
| Readability | Often cleaner for tree/graph problems | Cleaner for simple loops |
| Memory | Uses call stack (risk of stack overflow) | Usually O(1) extra space |
| Speed | Slight overhead per call | Slightly faster in practice |
| Debugging | Can be harder to trace | Usually easier |

### Brute Force

Tries every possible solution. Simple to implement, but often very slow.

```
Example: Finding a password by trying all combinations.
         Checking every pair of numbers in an array.
```

### Divide and Conquer

Split the problem into independent sub-problems, solve each recursively, then combine.

```
Divide:   Split array [8,3,1,5,2] into [8,3] and [1,5,2]
Conquer:  Sort each half recursively
Combine:  Merge the sorted halves → [1,2,3,5,8]
```
*Examples: Merge Sort, Quick Sort, Binary Search*

### Dynamic Programming (DP)

Break the problem into overlapping sub-problems and store results to avoid recomputation.

```
Key insight: If you already computed fib(5), store it!
Don't compute it again when you need it for fib(6).
```
*Examples: Fibonacci, Knapsack, Longest Common Subsequence*

### Greedy

Make the locally optimal choice at each step, hoping it leads to a globally optimal solution.

```
Example: Making change with fewest coins.
         At each step, pick the largest coin that fits.
         Coins: [25, 10, 5, 1], Amount: 36
         → Pick 25 (remain: 11) → Pick 10 (remain: 1) → Pick 1 → Total: 3 coins
```
*Examples: Dijkstra's (with non-negative weights), Huffman Coding, Activity Selection*

### Backtracking

Try a solution step by step; if a step leads to a dead end, "backtrack" and try a different option.

```
Example: Solving a maze.
         Go forward → Hit wall → Go back → Try different direction
```
*Examples: N-Queens, Sudoku Solver, Subset Generation*

## 2.2 By Design Paradigm

```
Algorithm Paradigms
│
├── Brute Force           (try everything)
├── Divide and Conquer    (split → solve → combine)
├── Dynamic Programming   (memoize overlapping subproblems)
├── Greedy                (local best → global best)
├── Backtracking          (build + undo)
├── Branch and Bound      (backtracking + pruning with bounds)
├── Randomized            (use randomness: QuickSort pivot, Skip Lists)
└── Transform and Conquer (restate the problem first, then solve)
```

## 2.3 By Complexity

Algorithms are characterized by how their runtime or memory usage grows with input size `n`:

| Complexity | Name | Example | n=10 | n=100 | n=1000 |
|---|---|---|---|---|---|
| O(1) | Constant | Array index lookup | 1 | 1 | 1 |
| O(log n) | Logarithmic | Binary Search | ~3 | ~7 | ~10 |
| O(n) | Linear | Linear Search | 10 | 100 | 1,000 |
| O(n log n) | Linearithmic | Merge Sort | ~33 | ~664 | ~9,966 |
| O(n²) | Quadratic | Bubble Sort | 100 | 10,000 | 1,000,000 |
| O(2ⁿ) | Exponential | Brute-force TSP | 1,024 | ~10³⁰ | astronomical |
| O(n!) | Factorial | Permutations | 3.6M | ~10¹⁵⁷ | impossible |

> **Rule of thumb:** Aim for O(n log n) or better for competitive solutions. O(n²) is usually acceptable only for small inputs (n ≤ 10,000).

## 2.4 By Problem Domain

| Category | Examples | Key Algorithms |
|---|---|---|
| **Sorting** | Order a list | Merge Sort, Quick Sort, Heap Sort |
| **Searching** | Find an element | Binary Search, BFS, DFS |
| **Graph** | Networks, maps, social graphs | Dijkstra's, Kruskal's, BFS, DFS |
| **String** | Text processing | KMP, Rabin-Karp, Trie |
| **Mathematical** | Number theory | Sieve of Eratosthenes, GCD |
| **Geometric** | Coordinates, shapes | Convex Hull, Line Intersection |
| **Optimization** | Maximize/minimize | DP, Greedy, Linear Programming |

---

> **Practice Questions — Section 2**
> 1. Classify each: (a) Binary Search, (b) N-Queens, (c) Merge Sort, (d) Activity Selection — by implementation approach AND design paradigm.
> 2. An algorithm has runtime `T(n) = 3n² + 100n + 500`. What is its Big-O complexity? Why do we drop lower-order terms?
> 3. When would you prefer a greedy algorithm over dynamic programming?

---

# 3. How to Analyze Time Complexity

## 3.1 Big-O Notation Fundamentals

**Big-O** describes the upper bound of an algorithm's growth rate — how the worst-case runtime scales with input size `n`.

**Formal definition:** `f(n) = O(g(n))` if there exist constants `c > 0` and `n₀ ≥ 1` such that `f(n) ≤ c·g(n)` for all `n ≥ n₀`.

In plain English: *ignore constants and lower-order terms; keep the dominant term.*

```
T(n) = 5n² + 3n + 12
     → O(n²)   ← dominant term wins

T(n) = 100       (constant work regardless of n)
     → O(1)

T(n) = 2n·log(n) + 50n
     → O(n log n)
```

**The three cases:**
- **Best case (Ω):** The minimum time. Example: Binary search on a list where target is the middle element → O(1).
- **Average case (Θ):** Expected time over all inputs.
- **Worst case (O):** Maximum time. This is what we usually care about.

## 3.2 Rules for Deriving Complexity

### Rule 1 — Consecutive statements: ADD
```python
x = 5           # O(1)
for i in range(n):   # O(n)
    print(i)
# Total: O(1) + O(n) = O(n)
```

### Rule 2 — Nested loops: MULTIPLY
```python
for i in range(n):       # O(n)
    for j in range(n):   # O(n)
        print(i, j)      # O(1)
# Total: O(n) × O(n) × O(1) = O(n²)
```

### Rule 3 — If/else: take the MAX branch
```python
if condition:
    for i in range(n):   # O(n)
        pass
else:
    for i in range(n):       # O(n²)
        for j in range(n):
            pass
# Total: O(max(n, n²)) = O(n²)
```

### Rule 4 — Logarithmic loops: halving/doubling
```python
i = 1
while i < n:     # How many times does i double before reaching n?
    i *= 2       # i = 1, 2, 4, 8, ..., n → log₂(n) iterations
# Total: O(log n)
```

### Rule 5 — Drop constants
```python
for i in range(3 * n):   # 3n iterations
    pass
# Total: O(3n) = O(n)   ← drop the 3
```

## 3.3 The Master Theorem

Many recursive algorithms have recurrences of the form:

```
T(n) = a·T(n/b) + f(n)

where:
  a = number of subproblems
  b = factor by which input shrinks
  f(n) = cost of work done outside recursive calls
```

Let `k = log_b(a)`. Then:

| Condition | Result | Example |
|---|---|---|
| f(n) = O(nᵏ⁻ᵉ) for some ε > 0 | T(n) = **Θ(nᵏ)** | T(n) = 2T(n/2) + 1 → Θ(n) |
| f(n) = Θ(nᵏ) | T(n) = **Θ(nᵏ log n)** | T(n) = 2T(n/2) + n → Θ(n log n) |
| f(n) = Ω(nᵏ⁺ᵉ) for some ε > 0 | T(n) = **Θ(f(n))** | T(n) = 2T(n/2) + n² → Θ(n²) |

**Worked Example — Merge Sort:**
```
T(n) = 2·T(n/2) + O(n)
  a = 2, b = 2, f(n) = n
  k = log₂(2) = 1
  f(n) = n = Θ(n¹) = Θ(nᵏ)   → Case 2
  ∴ T(n) = Θ(n log n)         ✓
```

**Worked Example — Binary Search:**
```
T(n) = 1·T(n/2) + O(1)
  a = 1, b = 2, f(n) = 1
  k = log₂(1) = 0
  f(n) = O(1) = O(n⁰) = O(nᵏ)  → Case 2
  ∴ T(n) = Θ(log n)              ✓
```

## 3.4 Space Complexity

Space complexity counts the **extra memory** an algorithm uses beyond its input.

```python
# O(1) space — only a few variables
def sum_array(arr: list[int]) -> int:
    total = 0
    for x in arr:
        total += x
    return total

# O(n) space — creates a new array
def double_array(arr: list[int]) -> list[int]:
    return [x * 2 for x in arr]   # new array of size n

# O(n) space — recursive call stack depth n
def factorial(n: int) -> int:
    if n == 0: return 1
    return n * factorial(n - 1)   # n frames on call stack
```

## 3.5 Step-by-Step Example: Deriving Complexity from Code

```python
def find_duplicates(arr: list[int]) -> list[int]:
    result = []                         # O(1)
    seen = set()                        # O(1)

    for x in arr:                       # n iterations → O(n) outer
        if x in seen:                   #   O(1) average for set lookup
            result.append(x)            #   O(1) amortized
        else:
            seen.add(x)                 #   O(1)

    return result                       # O(1)
```

**Analysis:**
- Outer loop: runs `n` times
- Each inner operation: O(1) average (hash set)
- Total time: O(n) × O(1) = **O(n)**
- Space: O(n) for the `seen` set in the worst case (all unique)

---

> **Practice Questions — Section 3**
> 1. What is the time complexity of three nested loops each running `n` times?
> 2. Solve T(n) = 4T(n/2) + n using the Master Theorem.
> 3. Write a function that checks if a list has duplicates in O(n) time and O(n) space. Can you do it in O(n log n) time and O(1) space?

---

# 4. Sorting Algorithms

Sorting is among the most fundamental operations in computer science. A sorted collection enables binary search, simplifies merging, and speeds up many downstream algorithms.

---

## 4.1 Bubble Sort

### Problem Statement
Repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order. The largest unsorted element "bubbles up" to its correct position each pass.

### Real-World Use
Rarely used in production. Useful for teaching swaps and loop invariants, or for nearly-sorted data with an early-exit optimization.

### Visual Walkthrough

```
Input: [5, 3, 8, 1, 2]

Pass 1:
[5,3,8,1,2] → swap(5,3) → [3,5,8,1,2]
[3,5,8,1,2] → no swap    → [3,5,8,1,2]
[3,5,8,1,2] → swap(8,1) → [3,5,1,8,2]
[3,5,1,8,2] → swap(8,2) → [3,5,1,2,8]   ← 8 is in place

Pass 2:
[3,5,1,2,8] → no swap  → [3,5,1,2,8]
[3,5,1,2,8] → swap(5,1)→ [3,1,5,2,8]
[3,1,5,2,8] → swap(5,2)→ [3,1,2,5,8]   ← 5 is in place

... and so on until fully sorted: [1,2,3,5,8]
```

### Python Implementation

```python
def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sort a list in ascending order using Bubble Sort.

    The outer loop runs n-1 passes. After each pass i,
    the i largest elements are in their final positions.
    The 'swapped' flag enables early exit for sorted inputs.

    Args:
        arr: List of integers to sort (modified in-place and returned)

    Returns:
        The sorted list (same object as input)
    """
    n = len(arr)

    for i in range(n - 1):          # n-1 passes needed at most
        swapped = False

        # Last i elements are already in place — no need to check them
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # swap
                swapped = True

        if not swapped:             # Array is already sorted — early exit
            break

    return arr

# Example
data = [5, 3, 8, 1, 2]
print(bubble_sort(data))   # [1, 2, 3, 5, 8]
```

### Complexity Analysis

| Case | Time | Space |
|---|---|---|
| Best (already sorted) | O(n) — one pass, no swaps | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) — n(n-1)/2 comparisons | O(1) |

**Derivation:** The inner loop runs `n-1`, then `n-2`, ..., then `1` times.
Total comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = **O(n²)**.

---

## 4.2 Selection Sort

### Problem Statement
Find the minimum element in the unsorted portion and place it at the beginning. Repeat for each position.

### Visual Walkthrough

```
Input: [5, 3, 8, 1, 2]

Pass 1: Find min of [5,3,8,1,2] → 1 at index 3 → swap with index 0
        [1, 3, 8, 5, 2]   ← 1 is in place

Pass 2: Find min of [3,8,5,2] → 2 at index 4 → swap with index 1
        [1, 2, 8, 5, 3]   ← 2 is in place

Pass 3: Find min of [8,5,3] → 3 at index 4 → swap with index 2
        [1, 2, 3, 5, 8]   ← 3 is in place

Pass 4: Find min of [5,8] → 5 already in place
        [1, 2, 3, 5, 8]   ✓ sorted
```

### Python Implementation

```python
def selection_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using Selection Sort.

    For each position i, find the smallest element in arr[i:]
    and swap it into position i.

    Key property: makes at most n-1 swaps (useful when write
    operations are expensive).
    """
    n = len(arr)

    for i in range(n - 1):
        # Find the index of the minimum element in arr[i:]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Place minimum at position i (only swap if necessary)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example
data = [64, 25, 12, 22, 11]
print(selection_sort(data))   # [11, 12, 22, 25, 64]
```

### Complexity Analysis

| Case | Time | Space |
|---|---|---|
| All cases | O(n²) | O(1) |

Selection sort always makes exactly n(n-1)/2 comparisons regardless of input order. It has at most **n-1 swaps**, which can be an advantage when swaps are expensive.

---

## 4.3 Insertion Sort

### Problem Statement
Build a sorted subarray one element at a time. For each new element, insert it into its correct position in the already-sorted portion.

### Visual Walkthrough

```
Input: [5, 3, 8, 1, 2]

          sorted | unsorted
Start:    [5]   | [3,8,1,2]

Take 3:   Insert 3 before 5   → [3,5] | [8,1,2]
Take 8:   Insert 8 after 5    → [3,5,8] | [1,2]
Take 1:   Insert 1 before 3   → [1,3,5,8] | [2]
Take 2:   Insert 2 after 1    → [1,2,3,5,8]  ✓
```

### Python Implementation

```python
def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using Insertion Sort.

    Particularly efficient for:
    - Nearly sorted data (approaches O(n))
    - Small arrays (low overhead)
    - Online sorting (sort as elements arrive)

    Works like sorting playing cards in your hand.
    """
    for i in range(1, len(arr)):
        key = arr[i]    # The element to be positioned

        # Shift elements of arr[0..i-1] that are greater than key
        # one position to the right
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key   # Place key in its correct position

    return arr

# Example
data = [5, 3, 8, 1, 2]
print(insertion_sort(data))   # [1, 2, 3, 5, 8]
```

### Complexity Analysis

| Case | Time | Space | Notes |
|---|---|---|---|
| Best (sorted) | O(n) | O(1) | Inner while loop never runs |
| Average | O(n²) | O(1) | |
| Worst (reverse sorted) | O(n²) | O(1) | Max shifts every time |

---

## 4.4 Merge Sort

### Problem Statement
Divide the array into two halves, recursively sort each half, then merge the two sorted halves into a single sorted array.

### Visual Walkthrough

```
Input: [38, 27, 43, 3, 9, 82, 10]

                [38, 27, 43, 3, 9, 82, 10]
               /                           \
       [38, 27, 43, 3]              [9, 82, 10]
        /            \               /         \
   [38, 27]      [43, 3]         [9, 82]       [10]
    /    \        /    \          /    \
  [38]  [27]   [43]   [3]      [9]   [82]

                ↑ Split Phase Complete ↑

  [27,38]     [3,43]          [9,82]     [10]
       \      /                     \    /
     [3,27,38,43]               [9,10,82]
              \                   /
            [3, 9, 10, 27, 38, 43, 82]   ✓
```

### Python Implementation

```python
def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using Merge Sort (divide and conquer).

    Creates new arrays during merge — not in-place.
    Stable sort: equal elements maintain their relative order.
    Preferred for linked lists and external sorting.

    Time:  O(n log n) — always
    Space: O(n) — for the temporary merge arrays
    """
    if len(arr) <= 1:
        return arr              # Base case: already sorted

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])    # Sort left half
    right = merge_sort(arr[mid:])    # Sort right half

    return _merge(left, right)       # Merge sorted halves

def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    # Compare elements from both halves and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:    # <= ensures stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (one of these will be empty)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example
data = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(data))   # [3, 9, 10, 27, 38, 43, 82]
```

### Complexity Analysis

```
Recurrence: T(n) = 2·T(n/2) + O(n)

Using Master Theorem:
  a=2, b=2, f(n)=n
  k = log₂(2) = 1
  f(n) = n = Θ(n¹) → Case 2
  T(n) = Θ(n log n)
```

| Case | Time | Space |
|---|---|---|
| All cases | O(n log n) | O(n) auxiliary |

---

## 4.5 Quick Sort

### Problem Statement
Choose a "pivot" element, partition the array so elements smaller than the pivot are to its left and larger ones to its right, then recursively sort each side.

### Visual Walkthrough

```
Input: [10, 80, 30, 90, 40, 50, 70]   pivot = 70 (last element)

Partition step:
  Pointer i starts at -1.
  Walk j from 0 to 5:
    j=0: arr[0]=10 < 70 → i++, swap arr[i] with arr[j] → [10,80,30,90,40,50,70]
    j=1: arr[1]=80 ≥ 70 → skip
    j=2: arr[2]=30 < 70 → i++, swap         → [10,30,80,90,40,50,70]
    j=3: arr[3]=90 ≥ 70 → skip
    j=4: arr[4]=40 < 70 → i++, swap         → [10,30,40,90,80,50,70]
    j=5: arr[5]=50 < 70 → i++, swap         → [10,30,40,50,80,90,70]
  Place pivot at i+1:    swap arr[i+1] with arr[6] → [10,30,40,50,70,90,80]
                                                              ^
                                                           pivot in place

Now recursively sort [10,30,40,50] and [90,80].
```

### Python Implementation

```python
def quick_sort(arr: list[int], low: int = 0, high: int | None = None) -> list[int]:
    """
    Sort a list using Quick Sort (in-place, Lomuto partition scheme).

    Average case O(n log n), but degrades to O(n²) on sorted/reverse-sorted
    input with naive pivot selection. Randomized pivot mitigates this.

    Note: Not a stable sort.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)    # Sort left of pivot
        quick_sort(arr, pivot_idx + 1, high)   # Sort right of pivot

    return arr

def _partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition arr[low..high] around the last element as pivot.
    Returns the final index of the pivot.
    """
    pivot = arr[high]
    i = low - 1   # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # Move smaller element left

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

import random

def quick_sort_randomized(arr: list[int], low: int = 0, high: int | None = None) -> list[int]:
    """Quick Sort with random pivot — avoids O(n²) on sorted inputs."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Randomly pick a pivot and swap to end before partitioning
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        pivot_idx = _partition(arr, low, high)
        quick_sort_randomized(arr, low, pivot_idx - 1)
        quick_sort_randomized(arr, pivot_idx + 1, high)

    return arr

# Example
data = [10, 80, 30, 90, 40, 50, 70]
print(quick_sort(data))   # [10, 30, 40, 50, 70, 80, 90]
```

### Complexity Analysis

| Case | Time | Space (call stack) |
|---|---|---|
| Best / Average | O(n log n) | O(log n) |
| Worst (sorted input, naive pivot) | O(n²) | O(n) |

**Why worst case O(n²)?** When the pivot is always the smallest or largest element, one partition has n-1 elements and the other has 0. This gives: T(n) = T(n-1) + O(n) → O(n²).

**Optimization tip:** Use median-of-three pivot (take the median of first, middle, last element) or randomize the pivot to make O(n²) astronomically unlikely.

---

## 4.6 Heap Sort

### Problem Statement
Build a max-heap from the array, then repeatedly extract the maximum element and place it at the end.

### Key Concept: Max-Heap

```
A max-heap is a complete binary tree where each node is
greater than or equal to its children.

Array: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

         16
       /    \
     14      10
    /  \    /  \
   8    7  9    3
  / \  /
 2   4 1
```

### Python Implementation

```python
def heap_sort(arr: list[int]) -> list[int]:
    """
    Sort using Heap Sort.

    Phase 1: Build a max-heap from the unsorted array (O(n)).
    Phase 2: Repeatedly extract the max and rebuild the heap (O(n log n)).

    In-place sort, but NOT stable.
    Time: O(n log n) always.
    Space: O(1) — purely in-place (ignoring call stack for heapify).
    """
    n = len(arr)

    # Phase 1: Build max-heap
    # Start from the last non-leaf node and heapify each node upward
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Phase 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (maximum) to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap (size = i)
        _heapify(arr, i, 0)

    return arr

def _heapify(arr: list[int], heap_size: int, root: int) -> None:
    """
    Ensure the subtree rooted at 'root' satisfies the max-heap property.
    Assumes left and right subtrees are already valid max-heaps.
    """
    largest = root
    left    = 2 * root + 1   # Left child index
    right   = 2 * root + 2   # Right child index

    # Check if left child is larger than root
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than current largest
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, heap_size, largest)   # Recursively fix the affected subtree

# Example
data = [12, 11, 13, 5, 6, 7]
print(heap_sort(data))   # [5, 6, 7, 11, 12, 13]
```

### Complexity Analysis

| Case | Time | Space |
|---|---|---|
| All cases | O(n log n) | O(1) — in-place |

Building the heap is O(n) (not O(n log n) as you might expect — due to the mathematical sum of levels). Each of the n extractions costs O(log n). Total: O(n log n).

## 4.7 Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable? | Notes |
|---|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✓ | Only for teaching |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ✗ | Min writes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✓ | Great for small/nearly-sorted |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✓ | Best for linked lists |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ | Best practical average |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ✗ | Guaranteed O(n log n) in-place |

> **Python's built-in `sorted()` and `.sort()`** use **Timsort** — a hybrid of Merge Sort and Insertion Sort — which is O(n log n) worst case and O(n) best case. For almost all practical work, just use these.

---

> **Practice Questions — Section 4**
> 1. Trace Bubble Sort on `[1, 2, 3, 4, 5]`. How many comparisons are made? How many swaps?
> 2. When would you choose Insertion Sort over Merge Sort?
> 3. Why is Quick Sort generally faster than Merge Sort in practice, despite both being O(n log n)?
> 4. Implement a function that uses the appropriate sorting algorithm based on the array size (use Insertion Sort for n ≤ 10, Merge Sort otherwise).

---

## 4.6 Counting Sort

### Problem Statement
Sort integers by counting the number of occurrences of each value. Works when the input range is limited.

### Key Idea
Instead of comparing elements, count frequencies and reconstruct the sorted output.

### Python Implementation

```python
def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size

    # Step 1: Count frequencies
    for num in arr:
        count[num - min_val] += 1

    # Step 2: Prefix sums (for stability)
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Step 3: Build output (stable)
    output = [0] * len(arr)
    for num in reversed(arr):
        idx = num - min_val
        count[idx] -= 1
        output[count[idx]] = num

    return output
```

### Complexity Analysis

| Time | Space |
|---|---|
| O(n + k) | O(k) |

where k = range of input values.

---

## 4.7 Radix Sort

### Problem Statement
Sort numbers digit by digit starting from least significant digit using a stable sort (typically Counting Sort).

### Key Idea
Sort by each digit place while preserving previous ordering.

### Python Implementation

```python
def radix_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        _counting_sort(arr, exp)
        exp *= 10

    return arr

def _counting_sort(arr: list[int], exp: int) -> None:
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    arr[:] = output
```

### Complexity Analysis

| Time | Space |
|---|---|
| O(d * (n + k)) | O(n + k) |

where:
- d = number of digits
- k = base (10 for decimal)

# 5. Searching Algorithms

## 5.1 Linear Search

### Problem Statement
Find a target element in a list by checking each element one by one from the beginning.

### Python Implementation

```python
def linear_search(arr: list, target) -> int:
    """
    Search for target in arr by checking each element sequentially.

    Works on:
    - Unsorted arrays
    - Any iterable
    - Any comparable data type

    Returns the index of the first occurrence, or -1 if not found.
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(arr, 12))    # 3
print(linear_search(arr, 100))   # -1
```

### Complexity Analysis

| Case | Time | Space |
|---|---|---|
| Best (target is first) | O(1) | O(1) |
| Average | O(n/2) = O(n) | O(1) |
| Worst (not found / last) | O(n) | O(1) |

---

> **Note:** Binary Search has moved to **Section 7 (Core Algorithmic Techniques)**. In the learning roadmap for this guide, Binary Search is grouped with Two Pointers and Sliding Window as part of Phase 2 — techniques that reward pattern recognition and build problem-solving speed before you move into full graph algorithms and dynamic programming.

---

> **Practice Questions — Section 5**
> 1. When would Linear Search be preferable to Binary Search even though it is O(n)?
> 2. Modify Linear Search to return *all* indices where the target occurs, not just the first.
> 3. What is the best-case input for Linear Search, and why does that case not generalize?

---

# 6. Graph Traversal Core

A **graph** G = (V, E) consists of a set of **vertices** (nodes) V and a set of **edges** E connecting pairs of vertices. Graphs model networks, social connections, maps, dependencies, and more.

```python
# Graph representation — Adjacency List (most common)
from collections import defaultdict

graph = defaultdict(list)
graph[0] = [1, 2]     # Node 0 connects to 1 and 2
graph[1] = [0, 3, 4]  # Node 1 connects to 0, 3, 4
graph[2] = [0, 5]
graph[3] = [1]
graph[4] = [1]
graph[5] = [2]

# Visual:
#     0
#    / \
#   1   2
#  / \   \
# 3   4   5
```

> **Phase 1 of 6 — Foundations of Traversal.** BFS and DFS are the fundamental primitives that nearly everything later in this guide depends on: graph algorithms (Section 8), backtracking (Section 11), cycle detection, and shortest-path reasoning all build directly on these two traversal patterns. Master them before moving on.

## 6.1 Breadth-First Search (BFS)

### Problem Statement
Explore a graph level by level: visit all neighbors of the starting node first, then their neighbors, and so on. Uses a **queue** (FIFO).

### Visual Walkthrough

```
Graph:
    0
   / \
  1   2
 / \   \
3   4   5

BFS from node 0:
Queue: [0]        Visited: {0}
  Dequeue 0 → visit 0, enqueue neighbors 1, 2
Queue: [1, 2]     Visited: {0,1,2}
  Dequeue 1 → visit 1, enqueue neighbors 3, 4
Queue: [2, 3, 4]  Visited: {0,1,2,3,4}
  Dequeue 2 → visit 2, enqueue neighbor 5
Queue: [3, 4, 5]  Visited: {0,1,2,3,4,5}
  Dequeue 3, 4, 5 → no new neighbors

BFS order: 0 → 1 → 2 → 3 → 4 → 5
```

### Python Implementation

```python
from collections import deque

def bfs(graph: dict, start: int) -> list[int]:
    """
    Breadth-First Search from 'start' node.

    Applications:
    - Shortest path in unweighted graphs
    - Level-order traversal of trees
    - Finding all nodes reachable from a source
    - Bipartite graph detection

    Returns: List of nodes in BFS visit order.
    """
    visited = set([start])
    queue   = deque([start])
    order   = []

    while queue:
        node = queue.popleft()    # O(1) dequeue from front
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

def bfs_shortest_path(graph: dict, start: int, end: int) -> list[int] | None:
    """
    Find the shortest path (fewest edges) between start and end using BFS.
    Returns the path as a list of nodes, or None if no path exists.
    """
    if start == end:
        return [start]

    visited  = {start}
    queue    = deque([[start]])   # Queue of paths (not just nodes)

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]    # Found the target!
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None    # No path exists

# Example
graph = defaultdict(list, {
    0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]
})
print(bfs(graph, 0))                      # [0, 1, 2, 3, 4, 5]
print(bfs_shortest_path(graph, 3, 5))     # [3, 1, 0, 2, 5]
```

### Complexity Analysis

| | Time | Space |
|---|---|---|
| BFS | O(V + E) | O(V) |

V = vertices, E = edges. We visit every vertex once and traverse every edge once.

---

## 6.2 Depth-First Search (DFS)

### Problem Statement
Explore as far as possible along each branch before backtracking. Uses a **stack** (implicit via recursion, or explicit).

### Visual Walkthrough

```
Graph (same as above):
    0
   / \
  1   2
 / \   \
3   4   5

DFS from node 0 (exploring left neighbors first):
Visit 0 → explore 1
  Visit 1 → explore 3
    Visit 3 → no unvisited neighbors → backtrack to 1
  Explore 4
    Visit 4 → no unvisited neighbors → backtrack to 1
  → backtrack to 0
Explore 2
  Visit 2 → explore 5
    Visit 5 → no unvisited neighbors → backtrack

DFS order: 0 → 1 → 3 → 4 → 2 → 5
```

### Python Implementation

```python
def dfs_recursive(graph: dict, start: int,
                  visited: set | None = None) -> list[int]:
    """
    Depth-First Search (recursive).

    Applications:
    - Cycle detection
    - Topological sorting
    - Connected components
    - Maze solving
    - Finding paths

    Returns: List of nodes in DFS visit order.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))

    return order

def dfs_iterative(graph: dict, start: int) -> list[int]:
    """DFS using an explicit stack (avoids Python's recursion limit)."""
    visited = set()
    stack   = [start]
    order   = []

    while stack:
        node = stack.pop()    # O(1) pop from top

        if node not in visited:
            visited.add(node)
            order.append(node)

            # Push neighbors in reverse order so leftmost is processed first
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order

# Example
print(dfs_recursive(graph, 0))   # [0, 1, 3, 4, 2, 5]
print(dfs_iterative(graph, 0))   # [0, 1, 3, 4, 2, 5]
```

### BFS vs DFS Comparison

| | BFS | DFS |
|---|---|---|
| Data Structure | Queue | Stack (or recursion) |
| Shortest Path (unweighted) | ✓ Guaranteed | ✗ Not guaranteed |
| Memory | O(max width of graph) | O(max depth of graph) |
| Use Cases | Shortest paths, levels, networking | Cycles, topological sort, backtracking |
| Complete? | Yes (always finds if exists) | Yes (if graph is finite) |

---

> **Practice Questions — Section 6**
> 1. Draw the BFS and DFS traversal trees for a graph of your choice.
> 2. Modify BFS to detect if a graph is bipartite (can be 2-colored).
> 3. Given an unweighted graph, use BFS to find the shortest path between two nodes.
> 4. When would you choose DFS over BFS, and vice versa?

---

# 7. Core Algorithmic Techniques

> **Phase 2 of 6 — High-ROI Patterns.** Binary Search, Two Pointers, and Sliding Window are extremely common in technical interviews and real-world code. Unlike graph algorithms or DP, they require pattern recognition more than heavy theory — mastering them here builds problem-solving speed that pays off in every later phase.

## 7.1 Binary Search

### Problem Statement
Search for a target in a **sorted** array. At each step, compare the target with the middle element and eliminate half of the remaining search space.

### Visual Walkthrough

```
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

Step 1: low=0, high=9, mid=4
        arr[4] = 9 > 7 → search left half
        high = mid - 1 = 3

Step 2: low=0, high=3, mid=1
        arr[1] = 3 < 7 → search right half
        low = mid + 1 = 2

Step 3: low=2, high=3, mid=2
        arr[2] = 5 < 7 → search right half
        low = mid + 1 = 3

Step 4: low=3, high=3, mid=3
        arr[3] = 7 == 7 → FOUND at index 3 ✓

Checked only 4 of 10 elements!
```

### Python Implementation

```python
def binary_search_iterative(arr: list[int], target: int) -> int:
    """
    Search for target in a sorted array using Binary Search.

    Precondition: arr must be sorted in ascending order.
    Returns the index of target, or -1 if not found.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2   # Avoids integer overflow (vs (low+high)//2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1    # Target is in the right half
        else:
            high = mid - 1   # Target is in the left half

    return -1   # Target not found

def binary_search_recursive(arr: list[int], target: int,
                             low: int = 0, high: int | None = None) -> int:
    """Recursive version of Binary Search."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1    # Base case: search space is empty

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search_iterative(arr, 7))    # 3
print(binary_search_iterative(arr, 6))    # -1
print(binary_search_recursive(arr, 15))  # 7
```

### Finding First/Last Occurrence (Binary Search Variant)

```python
def find_first_occurrence(arr: list[int], target: int) -> int:
    """Find the index of the FIRST occurrence of target in a sorted array."""
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid        # Record this position
            high = mid - 1      # Keep searching LEFT for earlier occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Example: [1, 2, 2, 2, 3, 4] target=2 → returns index 1 (first 2)
arr = [1, 2, 2, 2, 3, 4]
print(find_first_occurrence(arr, 2))   # 1
```

### Complexity Analysis

```
Each iteration cuts the search space in half.
After k iterations: n / 2^k elements remain.
Search ends when 2^k = n → k = log₂(n).
```

| Case | Time | Space (iterative / recursive) |
|---|---|---|
| Best | O(1) | O(1) / O(1) |
| Average & Worst | O(log n) | O(1) / O(log n) |

## 7.2 Binary Search on the Answer

### Concept
Instead of searching for a value in an array, you search for the **answer** in a range of possible values. This works when:
1. The possible answers have a monotonic property (if X works, then X-1 also works, or vice versa).
2. You can efficiently check "is X a valid answer?"

### Template

```python
def binary_search_on_answer(lo: int, hi: int, condition) -> int:
    """
    Generic binary search on the answer.

    Find the smallest value in [lo, hi] satisfying 'condition'.
    'condition(mid)' returns True if mid is a valid answer.
    All values >= the answer satisfy condition; all < do not.
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition(mid):
            hi = mid      # mid could be the answer, search left
        else:
            lo = mid + 1  # mid is too small, search right
    return lo
```

### Example: Minimum Days to Make Bouquets

```python
def min_days_bouquets(bloom_day: list[int], m: int, k: int) -> int:
    """
    Find the minimum number of days to make m bouquets, each with k adjacent flowers.

    bloom_day[i] = day when flower i blooms.
    Key insight: if we can make m bouquets in D days, we can also in D+1 days.
    So the answer is monotone → binary search on D.

    Time: O(n log(max_day))
    """
    n = len(bloom_day)
    if m * k > n:
        return -1   # Impossible

    def can_make(day: int) -> bool:
        """Check if we can make m bouquets by 'day'."""
        bouquets = 0
        consecutive = 0
        for bd in bloom_day:
            if bd <= day:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0
        return bouquets >= m

    lo, hi = min(bloom_day), max(bloom_day)
    return binary_search_on_answer(lo, hi, can_make)

# Example
bloom_day = [1, 10, 3, 10, 2]
print(min_days_bouquets(bloom_day, m=3, k=1))   # 3
```

### Example: Allocate Minimum Pages

```python
def allocate_pages(pages: list[int], students: int) -> int:
    """
    Allocate books to students so the maximum pages any student reads
    is minimized. Each student gets contiguous books.

    Binary search on the answer (max pages).
    Lower bound: max single book (a student must read at least one book).
    Upper bound: sum of all pages (one student reads everything).

    Time: O(n log(sum(pages)))
    """
    def is_feasible(max_pages: int) -> bool:
        """Can we allocate books with no student reading > max_pages?"""
        count, current = 1, 0
        for p in pages:
            if p > max_pages:
                return False       # Single book exceeds limit
            if current + p > max_pages:
                count += 1         # Give to next student
                current = p
                if count > students:
                    return False
            else:
                current += p
        return True

    lo, hi = max(pages), sum(pages)
    return binary_search_on_answer(lo, hi, is_feasible)

# Example
books = [12, 34, 67, 90]
print(allocate_pages(books, students=2))   # 113
```

---

## 7.3 Two Pointers Technique

### Concept
Use two pointers (indices) that move through the data structure in a coordinated way. Reduces O(n²) brute-force solutions to O(n).

### Pattern 1 — Opposite Ends (for sorted arrays)

```
Find a pair summing to target in sorted array [1, 2, 3, 4, 6], target = 6:

left=0 [1], right=4 [6]  → sum=7 > 6  → right--
left=0 [1], right=3 [4]  → sum=5 < 6  → left++
left=1 [2], right=3 [4]  → sum=6 == 6 → FOUND (2, 4) ✓
```

```python
def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int] | None:
    """
    Find two numbers in a SORTED array that sum to target.
    Returns their indices, or None if not found.

    Time: O(n)  Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1    # Need a larger sum
        else:
            right -= 1   # Need a smaller sum

    return None

# Example
arr = [1, 2, 3, 4, 6]
print(two_sum_sorted(arr, 6))   # (1, 3) → values 2 and 4
```

### Pattern 2 — Same Direction (fast/slow pointers)

```python
def remove_duplicates_sorted(arr: list[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    Returns the length of the deduplicated array.

    slow: tracks position for next unique element
    fast: scans ahead looking for new unique elements

    Time: O(n)  Space: O(1)
    """
    if not arr:
        return 0

    slow = 0

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:   # Found a new unique element
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1   # Length of unique portion

# Example
arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n = remove_duplicates_sorted(arr)
print(arr[:n])   # [0, 1, 2, 3, 4]
```

### 3-Sum Problem (Two Pointers Extension)

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in nums that sum to 0.
    Time: O(n²)  Space: O(1) excluding output
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue    # Skip duplicates for the first element

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1     # Skip duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1    # Skip duplicates
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

# Example
print(three_sum([-1, 0, 1, 2, -1, -4]))
# [[-1, -1, 2], [-1, 0, 1]]
```

---

## 7.4 Sliding Window Technique

### Concept
Maintain a "window" (subarray/substring) and slide it across the data structure, adding new elements at one end and removing from the other. Efficient for problems about subarrays of fixed or variable size.

### Fixed-Size Window

```python
def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Find the maximum sum of any subarray of size k.

    Naive approach: O(n*k) — recompute sum for every window.
    Sliding window: O(n) — just add one element and remove one.
    """
    if len(arr) < k:
        return 0

    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum    = window_sum

    # Slide the window: add right element, remove left element
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # +new right, -old left
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example
arr = [2, 1, 5, 1, 3, 2]
print(max_sum_subarray(arr, 3))   # 9 (subarray [5,1,3])
```

### Variable-Size Window

```python
def min_subarray_length(arr: list[int], target: int) -> int:
    """
    Find the minimum length subarray with sum >= target.
    Uses a variable-size sliding window.

    Time: O(n)  Space: O(1)
    """
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]   # Expand window to the right

        # Shrink window from left while sum still >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Example
arr = [2, 3, 1, 2, 4, 3]
print(min_subarray_length(arr, 7))   # 2 (subarray [4,3])
```

### Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Classic sliding window with a set to track current window characters.
    Time: O(n)  Space: O(min(n, charset_size))
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink window until s[right] can be added without duplication
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Example
print(length_of_longest_substring("abcabcbb"))   # 3 ("abc")
print(length_of_longest_substring("pwwkew"))     # 3 ("wke")
```

---

> **Practice Questions — Section 7**
> 1. *(Binary Search)* How many steps does binary search take on an array of 1,000,000 elements? (Hint: log₂(10⁶) ≈ ?)
> 2. *(Binary Search)* Modify binary search to find the number of times a target appears in a sorted array.
> 3. *(Binary Search on the Answer)* Given a sorted array, find the square root of x without using `math.sqrt`, rounded down.
> 4. *(Two Pointers)* Use Two Pointers to check if a string is a palindrome, ignoring non-alphanumeric characters.
> 5. *(Sliding Window)* Modify the sliding window pattern to solve "Longest Substring with at most K distinct characters."

---

# 8. Graph Algorithms

A **graph** G = (V, E) consists of a set of **vertices** (nodes) V and a set of **edges** E connecting pairs of vertices. Graphs model networks, social connections, maps, dependencies, and more. This section assumes you're comfortable with the BFS and DFS traversal patterns from Section 6 — every algorithm below extends one of those two primitives into a complete system.

> **Phase 3 of 6 — From Traversal to Full Systems.** This phase expands BFS/DFS into complete graph algorithms, in a deliberate order: **Topological Sort** introduces DAG reasoning and builds directly on DFS. **Dijkstra's** builds on greedy choice plus a priority queue. **Bellman-Ford** generalizes Dijkstra's to handle negative edges. **MST (Kruskal's/Prim's)** introduces global optimization over a graph.

## 8.1 Topological Sort

### Problem Statement
Given a Directed Acyclic Graph (DAG), produce a linear ordering of vertices such that for every directed edge u → v, u comes before v.

### Key Idea
Use DFS or Kahn’s Algorithm (BFS with in-degree tracking).

### Python Implementation (Kahn’s Algorithm)

```python
from collections import deque

def topological_sort(V, edges):
    adj = [[] for _ in range(V)]
    indegree = [0] * V

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(V) if indegree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != V:
        raise ValueError("Graph has a cycle")

    return topo_order
```

### Complexity Analysis

| Time | Space |
|---|---|
| O(V + E) | O(V + E) |

## 8.2 Dijkstra's Algorithm

### Problem Statement
Find the shortest path from a source vertex to all other vertices in a **weighted graph with non-negative edge weights**.

### Visual Walkthrough

```
Graph:
  (A)--4--(B)--2--(C)
   |       |       |
   8       1       3
   |       |       |
  (D)--5--(E)--1--(F)

Source: A

Step 1: dist = {A:0, B:∞, C:∞, D:∞, E:∞, F:∞}
        Priority Queue: [(0,A)]

Step 2: Pop (0,A). Update neighbors:
        dist[B] = 0+4 = 4, dist[D] = 0+8 = 8
        PQ: [(4,B), (8,D)]

Step 3: Pop (4,B). Update neighbors:
        dist[C] = 4+2 = 6, dist[E] = 4+1 = 5
        PQ: [(5,E), (6,C), (8,D)]

Step 4: Pop (5,E). Update neighbors:
        dist[F] = 5+1 = 6, dist[D] = min(8, 5+5)=8
        PQ: [(6,C), (6,F), (8,D)]

... and so on

Final shortest distances from A:
  A:0, B:4, C:6, D:8, E:5, F:6
```

### Python Implementation

```python
import heapq
from collections import defaultdict

def dijkstra(graph: dict[int, list[tuple[int, int]]], source: int
             ) -> tuple[dict[int, int], dict[int, int | None]]:
    """
    Dijkstra's shortest-path algorithm.

    Args:
        graph: Adjacency list. graph[u] = [(v, weight), ...] for each neighbor.
        source: Starting node.

    Returns:
        dist: dict mapping each node to its shortest distance from source.
        prev: dict mapping each node to its predecessor on the shortest path.

    Limitations: Does NOT work with negative edge weights (use Bellman-Ford).
    """
    dist = defaultdict(lambda: float('inf'))
    prev = {}                     # For path reconstruction
    dist[source] = 0

    # Min-heap: (distance, node)
    pq = [(0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        # Skip if we already found a shorter path to u
        if curr_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dict(dist), prev

def reconstruct_path(prev: dict, source: int, target: int) -> list[int]:
    """Reconstruct the shortest path from source to target using 'prev' dict."""
    path = []
    node = target

    while node != source:
        if node not in prev:
            return []   # No path exists
        path.append(node)
        node = prev[node]

    path.append(source)
    return path[::-1]   # Reverse to get source → target order

# Example
graph = defaultdict(list)
edges = [(0,1,4), (0,2,1), (1,3,1), (2,1,2), (2,3,5), (3,4,3)]
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

distances, predecessors = dijkstra(graph, 0)
print(distances)                              # {0:0, 1:3, 2:1, 3:4, 4:7}
print(reconstruct_path(predecessors, 0, 4))  # [0, 2, 1, 3, 4]
```

### Complexity Analysis

With a binary heap (Python's `heapq`):

| | Complexity |
|---|---|
| Time | O((V + E) log V) |
| Space | O(V + E) |

With a Fibonacci heap: O(E + V log V) — rarely used in practice.

---

## 8.3 Bellman-Ford Algorithm

### Problem Statement
Find the shortest paths from a single source to all vertices in a graph, even when negative edge weights are present.

### Key Idea
Relax all edges repeatedly (V-1 times). Detect negative cycles by checking for further relaxation.

### Python Implementation

```python
def bellman_ford(edges, V, source):
    dist = [float('inf')] * V
    dist[source] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist
```

### Complexity Analysis

| Time | Space |
|---|---|
| O(V * E) | O(V) |

---

## 8.4 Minimum Spanning Tree: Kruskal's Algorithm

### Problem Statement
Find the subset of edges that connects all vertices in a weighted undirected graph with the **minimum total edge weight**, forming a tree.

**Key Idea:** Sort edges by weight. Add an edge if it doesn't form a cycle. Use a **Union-Find** data structure to detect cycles efficiently.

```
Example graph:
  4 --- 2   (weight 3)
  |     |
  1     3   edge weights on each connection
  |     |
  1 --- 3   (weight 2)
  (edge 1-2: weight 1)

Edges sorted by weight: (1,2,1), (1,3,2), (2,4,3), ...
Add (1,2,1) → no cycle → MST edge ✓
Add (1,3,2) → no cycle → MST edge ✓
Add (2,4,3) → no cycle → MST edge ✓
MST total weight: 1+2+3 = 6
```

### Python Implementation

```python
def kruskal_mst(vertices: int,
                edges: list[tuple[int, int, int]]
                ) -> tuple[list[tuple[int, int, int]], int]:
    """
    Kruskal's Minimum Spanning Tree Algorithm.

    Args:
        vertices: Number of vertices (labeled 0 to vertices-1).
        edges: List of (u, v, weight) tuples.

    Returns:
        mst_edges: List of edges in the MST.
        total_weight: Total weight of the MST.

    Uses Union-Find with path compression and union by rank
    for near-O(1) amortized operations.
    """
    # --- Union-Find Data Structure ---
    parent = list(range(vertices))
    rank   = [0] * vertices

    def find(x: int) -> int:
        """Find root with path compression."""
        if parent[x] != x:
            parent[x] = find(parent[x])   # Path compression
        return parent[x]

    def union(x: int, y: int) -> bool:
        """Union two sets. Returns False if already in same set (cycle)."""
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False   # Cycle detected!

        # Union by rank: attach smaller tree under larger tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        return True

    # --- Kruskal's Main Loop ---
    edges.sort(key=lambda e: e[2])   # Sort by weight
    mst_edges    = []
    total_weight = 0

    for u, v, weight in edges:
        if union(u, v):             # Add edge if it doesn't create a cycle
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == vertices - 1:  # MST has V-1 edges
                break

    return mst_edges, total_weight

# Example
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst, total = kruskal_mst(4, edges)
print(mst)     # [(2,3,4), (0,3,5), (0,1,10)]
print(total)   # 19
```

### Complexity Analysis

| | Complexity |
|---|---|
| Time | O(E log E) for sorting |
| Space | O(V + E) |

The Union-Find operations are nearly O(1) amortized (inverse Ackermann function).

---

## 8.5 Minimum Spanning Tree: Prim's Algorithm

### Problem Statement
Build the MST by growing a single tree. Start from any vertex, and repeatedly add the **cheapest edge** that connects a tree vertex to a non-tree vertex.

**Key difference from Kruskal's:** Prim's grows one connected tree (works better for dense graphs). Kruskal's works edge by edge (better for sparse graphs).

### Python Implementation

```python
def prim_mst(graph: dict[int, list[tuple[int, int]]], start: int = 0
             ) -> tuple[list[tuple[int, int, int]], int]:
    """
    Prim's Minimum Spanning Tree Algorithm.

    Uses a min-heap to efficiently find the cheapest edge to expand.

    Args:
        graph: graph[u] = [(v, weight), ...] adjacency list.
        start: Starting vertex.

    Returns:
        mst_edges: List of (u, v, weight) edges in the MST.
        total_weight: Sum of MST edge weights.
    """
    visited      = set([start])
    mst_edges    = []
    total_weight = 0

    # Min-heap of (weight, u, v) — edges crossing the cut
    heap = [(weight, start, v) for v, weight in graph[start]]
    heapq.heapify(heap)

    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue   # Skip if v is already in the tree

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        # Add all edges from v to non-visited vertices
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(heap, (edge_weight, v, neighbor))

    return mst_edges, total_weight

# Example
graph = defaultdict(list)
for u, v, w in [(0,1,2), (0,3,6), (1,2,3), (1,3,8), (1,4,5), (2,4,7), (3,4,9)]:
    graph[u].append((v, w))
    graph[v].append((u, w))

mst, total = prim_mst(graph, start=0)
print(total)   # 16
```

### Complexity Analysis

| Algorithm | Time (Binary Heap) | Best For |
|---|---|---|
| Kruskal's | O(E log E) | Sparse graphs |
| Prim's | O((V + E) log V) | Dense graphs |

---

> **Practice Questions — Section 8**
> 1. Why can't Dijkstra's algorithm handle negative edge weights? Construct an example where it gives the wrong answer.
> 2. A graph has 5 vertices and 7 edges. How many edges will its Minimum Spanning Tree have?
> 3. Given a list of course prerequisites, use Topological Sort to determine if all courses can be completed. What does it mean if no valid ordering exists?
> 4. When would you choose Bellman-Ford over Dijkstra's algorithm, given that it is slower?
> 5. When would you prefer Kruskal's algorithm over Prim's, and vice versa?

---

# 9. Greedy Algorithms

> **Phase 4 of 6 — Greedy Algorithms.** Having just worked through graph optimization and ordering problems in Phase 3, the greedy choice property should now feel intuitive rather than memorized. Focus on *why* the greedy choice works for each problem below — proof of correctness matters more here than for almost any other technique in this guide, because greedy is the easiest paradigm to apply incorrectly.

A **greedy algorithm** builds a solution step by step, always choosing the option that looks best **right now** — without reconsidering past choices or looking ahead. It works when the greedy choice leads to a globally optimal solution.

**Greedy works when:**
- The problem has **greedy choice property**: a global optimum can be reached by making a locally optimal (greedy) choice.
- The problem has **optimal substructure**: an optimal solution to the problem contains optimal solutions to its subproblems.

---

## 9.1 Activity Selection Problem

### Problem Statement
Given `n` activities with start and finish times, find the **maximum number of activities** that can be performed by a single person (activities cannot overlap).

### Greedy Insight
Always pick the activity that **finishes earliest** — this leaves the most time for remaining activities.

### Visual Walkthrough

```
Activities: (start, finish)
A1: (1, 4)
A2: (3, 5)
A3: (0, 6)
A4: (5, 7)
A5: (3, 8)
A6: (5, 9)
A7: (6, 10)
A8: (8, 11)
A9: (8, 12)
A10:(2, 13)
A11:(12,14)

Sort by finish time:
A1(1,4), A2(3,5), A3(0,6), A4(5,7), A5(3,8), A6(5,9), A7(6,10), A8(8,11), A9(8,12), A10(2,13), A11(12,14)

Select A1 (finishes at 4)  ✓
Skip A2 (starts at 3 < 4)
Skip A3 (starts at 0 < 4)
Select A4 (starts at 5 ≥ 4, finishes at 7)  ✓
Skip A5 (starts at 3 < 7)
Skip A6 (starts at 5 < 7)
Select A7 (starts at 6 < 7)? No. Skip.
Select A8 (starts at 8 ≥ 7, finishes at 11)  ✓
Skip A9 (starts at 8 < 11)
Skip A10 (starts at 2 < 11)
Select A11 (starts at 12 ≥ 11, finishes at 14)  ✓

Maximum activities: A1, A4, A8, A11 = 4 activities
```

### Python Implementation

```python
def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Select the maximum number of non-overlapping activities.

    Args:
        activities: List of (start, finish) tuples.

    Returns:
        List of selected (start, finish) tuples.

    Greedy strategy: always select the activity that finishes earliest.
    """
    # Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    selected = [sorted_activities[0]]         # Always pick the first activity
    last_finish = sorted_activities[0][1]

    for start, finish in sorted_activities[1:]:
        if start >= last_finish:              # No overlap with last selected
            selected.append((start, finish))
            last_finish = finish

    return selected

# Example
activities = [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9),
              (6,10), (8,11), (8,12), (2,13), (12,14)]
selected = activity_selection(activities)
print(selected)   # [(1,4), (5,7), (8,11), (12,14)]
print(f"Count: {len(selected)}")   # Count: 4
```

### Complexity Analysis

| | Time | Space |
|---|---|---|
| Sorting | O(n log n) | O(1) extra |
| Greedy scan | O(n) | O(1) |
| **Total** | **O(n log n)** | **O(1)** |

---

## 9.2 Fractional Knapsack

### Problem Statement
Like 0/1 Knapsack, but you can take **fractions** of items. This makes it solvable greedily (unlike 0/1 Knapsack which requires DP).

### Greedy Insight
Calculate value-per-unit-weight for each item. Take items in decreasing order of this ratio. If an item doesn't fully fit, take the fraction that does.

### Python Implementation

```python
def fractional_knapsack(weights: list[float], values: list[float],
                         capacity: float) -> tuple[float, list[tuple[int, float]]]:
    """
    Solve the Fractional Knapsack Problem greedily.

    Args:
        weights: Item weights.
        values: Item values.
        capacity: Knapsack capacity.

    Returns:
        max_value: Maximum achievable value.
        taken: List of (item_index, fraction_taken) pairs.
    """
    n = len(weights)

    # Calculate value-to-weight ratio and sort descending
    items = sorted(
        range(n),
        key=lambda i: values[i] / weights[i],
        reverse=True
    )

    total_value = 0.0
    taken = []
    remaining_capacity = capacity

    for i in items:
        if remaining_capacity <= 0:
            break

        if weights[i] <= remaining_capacity:
            # Take the whole item
            fraction = 1.0
            remaining_capacity -= weights[i]
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weights[i]
            remaining_capacity = 0

        total_value += fraction * values[i]
        taken.append((i, fraction))

    return total_value, taken

# Example
weights = [10, 20, 30]
values  = [60, 100, 120]
W = 50

max_val, taken = fractional_knapsack(weights, values, W)
print(f"Max value: {max_val:.2f}")   # Max value: 240.00
# Take all of item 0 (ratio=6), all of item 1 (ratio=5), 2/3 of item 2 (ratio=4)
```

### Comparing 0/1 vs Fractional Knapsack

| Property | 0/1 Knapsack | Fractional Knapsack |
|---|---|---|
| Items | Whole only | Fractions allowed |
| Approach | DP required | Greedy works |
| Time Complexity | O(n × W) | O(n log n) |
| Optimal? | DP is optimal | Greedy is optimal |

---

> **Practice Questions — Section 9**
> 1. Prove (informally) that Activity Selection's greedy choice is optimal. (Hint: show that replacing any selected activity with the earliest-finishing one doesn't decrease the total.)
> 2. Why does the Greedy approach fail for 0/1 Knapsack? Construct a counterexample.
> 3. Implement a solution to Huffman Coding (a greedy algorithm for lossless data compression). What greedy property does it use?

---

# 10. Dynamic Programming

> **Phase 5 of 6 — Dynamic Programming.** This is placed deliberately late: DP requires strong recursion fundamentals, pattern recognition, and experience decomposing problems — all of which Phases 1-4 have been building. For each problem below, focus on three things: **state definition** (what does `dp[i]` or `dp[i][j]` actually represent?), the **transition relation** (how do smaller states combine?), and the trade-off between **memoization** (top-down) and **tabulation** (bottom-up).

**Dynamic Programming (DP)** solves complex problems by breaking them into simpler overlapping subproblems, solving each just once, and storing the results.

**Two key properties for DP:**
1. **Optimal Substructure:** The optimal solution to the problem contains optimal solutions to subproblems.
2. **Overlapping Subproblems:** The same subproblems are solved multiple times in a naive recursive approach.

**Two approaches:**
- **Top-Down (Memoization):** Recursive + cache results.
- **Bottom-Up (Tabulation):** Build solution from smallest subproblems upward.

---

## 10.1 Fibonacci Sequence

### Problem Statement
Compute the nth Fibonacci number: F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2).

### Why DP? The Naive Recursion Problem

```
fib(5) calls fib(4) and fib(3)
fib(4) calls fib(3) and fib(2)    ← fib(3) computed TWICE
fib(3) calls fib(2) and fib(1)    ← fib(2) computed MULTIPLE TIMES

Call tree for fib(5):
                fib(5)
              /        \
          fib(4)       fib(3)
          /    \        /   \
       fib(3) fib(2) fib(2) fib(1)
       ...

Exponential time: O(2^n) without caching!
```

### Python Implementation

```python
from functools import lru_cache

# Approach 1: Naive Recursion — O(2^n) — DO NOT USE FOR LARGE n
def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Approach 2: Top-Down DP (Memoization) — O(n) time, O(n) space
def fib_memo(n: int, memo: dict | None = None) -> int:
    """
    Fibonacci with memoization.
    Each unique n is computed only once and cached.
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Approach 3: Using Python's built-in lru_cache decorator
@lru_cache(maxsize=None)
def fib_cached(n: int) -> int:
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

# Approach 4: Bottom-Up DP (Tabulation) — O(n) time, O(n) space
def fib_tabulation(n: int) -> int:
    """
    Build the solution table from fib(0) up to fib(n).
    Avoids recursion overhead entirely.
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Approach 5: Space-Optimized — O(n) time, O(1) space
def fib_optimized(n: int) -> int:
    """
    We only need the previous two values, not the entire table.
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2

    return prev1

# Examples
print(fib_tabulation(10))   # 55
print(fib_optimized(50))    # 12586269025
```

### Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Naive recursion | O(2ⁿ) | O(n) stack |
| Memoization | O(n) | O(n) |
| Tabulation | O(n) | O(n) |
| Space-optimized | O(n) | O(1) |

---

## 10.2 0/1 Knapsack Problem

### Problem Statement
Given `n` items, each with a weight `w[i]` and value `v[i]`, and a knapsack with capacity `W`, find the maximum value you can carry. Each item can be either taken (1) or not taken (0) — you cannot take fractions.

### Visual Walkthrough

```
Items: [(weight=1, value=1), (weight=3, value=4), (weight=4, value=5), (weight=5, value=7)]
Capacity W = 7

DP Table dp[i][w] = max value using first i items with capacity w:

        w: 0  1  2  3  4  5  6  7
item 0:    0  0  0  0  0  0  0  0   (no items)
item 1(1,1): 0  1  1  1  1  1  1  1
item 2(3,4): 0  1  1  4  5  5  5  5
item 3(4,5): 0  1  1  4  5  6  6  9
item 4(5,7): 0  1  1  4  5  7  8  9

Answer: dp[4][7] = 9
(Take item 2 (weight=3, value=4) + item 4 (weight=5, value=7) = weight 8? NO...
 Actually: item 3 (weight=4,value=5) + item 2 (weight=3,value=4) = 9, weight=7 ✓)
```

### Python Implementation

```python
def knapsack_01(weights: list[int], values: list[int],
                capacity: int) -> tuple[int, list[int]]:
    """
    Solve the 0/1 Knapsack Problem using bottom-up DP.

    Args:
        weights: List of item weights.
        values: List of item values (same length as weights).
        capacity: Maximum weight the knapsack can carry.

    Returns:
        max_value: Maximum achievable value.
        selected_items: Indices of items to include.

    Time:  O(n * W)
    Space: O(n * W) for the DP table
    """
    n  = len(weights)
    # dp[i][w] = max value using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Don't take item i-1
            dp[i][w] = dp[i - 1][w]

            # Option 2: Take item i-1 (if it fits)
            if weights[i - 1] <= w:
                take_value = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take_value)

    # Backtrack to find which items were selected
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:   # Item i-1 was taken
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]

# Space-optimized version — O(W) space
def knapsack_01_optimized(weights: list[int], values: list[int],
                           capacity: int) -> int:
    """
    Space-optimized 0/1 Knapsack.
    Uses a 1D DP array, iterating weights RIGHT TO LEFT to avoid
    using an item multiple times (which would give fractional knapsack).
    """
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # Iterate RIGHT to LEFT to prevent using item i more than once
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Example
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
W = 7

max_val, items = knapsack_01(weights, values, W)
print(f"Max value: {max_val}")    # Max value: 9
print(f"Items: {items}")          # Items: [1, 2] → weights [3,4], values [4,5]
```

### Complexity Analysis

| | Time | Space |
|---|---|---|
| Standard DP | O(n × W) | O(n × W) |
| Space-optimized | O(n × W) | O(W) |

> **Note:** O(n × W) is called "pseudo-polynomial" — it's polynomial in W, but W can be exponentially large if encoded in binary (e.g., W = 2³² requires a huge table). This is why 0/1 Knapsack is NP-complete.

---

## 10.3 Longest Common Subsequence (LCS)

### Problem Statement
Given two strings, find the length of their **longest common subsequence** (a subsequence is a sequence that appears in the same relative order but not necessarily contiguous).

```
Example:
  s1 = "ABCBDAB"
  s2 = "BDCABA"

LCS = "BCBA" or "BDAB" → length 4
```

### DP Table Approach

```
    ""  B  D  C  A  B  A
""   0  0  0  0  0  0  0
A    0  0  0  0  1  1  1
B    0  1  1  1  1  2  2
C    0  1  1  2  2  2  2
B    0  1  1  2  2  3  3
D    0  1  2  2  2  3  3
A    0  1  2  2  3  3  4
B    0  1  2  2  3  4  4

LCS length = 4
```

### Python Implementation

```python
def lcs(s1: str, s2: str) -> tuple[int, str]:
    """
    Compute the Longest Common Subsequence of s1 and s2.

    DP Recurrence:
      dp[i][j] = length of LCS of s1[0..i-1] and s2[0..j-1]

      If s1[i-1] == s2[j-1]:
          dp[i][j] = dp[i-1][j-1] + 1
      Else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Returns: (length of LCS, the LCS string itself)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_str))

# Example
s1 = "ABCBDAB"
s2 = "BDCABA"
length, sequence = lcs(s1, s2)
print(f"LCS Length: {length}")       # LCS Length: 4
print(f"LCS: {sequence}")            # LCS: BCBA (or BDAB depending on path)
```

### Complexity Analysis

| | Time | Space |
|---|---|---|
| Standard | O(m × n) | O(m × n) |
| Space-optimized | O(m × n) | O(min(m,n)) — only need two rows |

---

> **Practice Questions — Section 10**
> 1. Trace the DP table for knapsack with items [(2,3),(3,4),(4,5)] and capacity 5.
> 2. What is the LCS of "AGGTAB" and "GXTXAYB"?
> 3. How would you modify the Fibonacci bottom-up DP to also count the number of ways to reach step n if you can take 1 or 2 steps at a time? (This is the "Climbing Stairs" problem.)
> 4. Why is the 0/1 Knapsack space-optimized version iterated right-to-left?

---

# 11. Backtracking

> **Phase 6 of 6 — Backtracking.** This is the final phase because it builds directly on DFS and recursion — both of which you've now had extensive practice with. Backtracking problems are conceptually simple (try a choice, recurse, undo if it fails) but computationally heavy, which is why they're saved for last rather than tackled early.

## 11.1 Concept
Backtracking is a systematic way to build solutions incrementally, abandoning ("pruning") partial solutions that cannot lead to a valid complete solution.

```
Template:
  def backtrack(state):
      if state is a solution:
          record/return state
      for each choice:
          if choice is valid:
              make the choice
              backtrack(new state)
              undo the choice        ← KEY STEP (backtrack)
```

## 11.2 N-Queens Problem

**Problem:** Place N queens on an N×N chessboard so no two queens attack each other (same row, column, or diagonal).

```
Solution for N=4:
. Q . .       . . Q .
. . . Q       Q . . .
Q . . .       . . . Q
. . Q .       . Q . .
```

```python
def solve_n_queens(n: int) -> list[list[str]]:
    """
    Find all valid placements of N queens on an N×N chessboard.

    State: queen positions, one per row (queens[row] = col)
    Constraint: No two queens share a column or diagonal.

    Returns: List of solutions, each as a list of strings.
    """
    solutions = []
    queens    = []   # queens[i] = column of queen in row i

    # Track conflicts using sets for O(1) lookup
    cols         = set()
    diag_down    = set()   # row - col (same for "\" diagonals)
    diag_up      = set()   # row + col (same for "/" diagonals)

    def is_safe(row: int, col: int) -> bool:
        return (col not in cols and
                (row - col) not in diag_down and
                (row + col) not in diag_up)

    def backtrack(row: int) -> None:
        if row == n:
            # Build the board representation
            board = []
            for r in range(n):
                board.append('.' * queens[r] + 'Q' + '.' * (n - queens[r] - 1))
            solutions.append(board)
            return

        for col in range(n):
            if is_safe(row, col):
                # Place queen
                queens.append(col)
                cols.add(col)
                diag_down.add(row - col)
                diag_up.add(row + col)

                backtrack(row + 1)   # Recurse to next row

                # Remove queen (backtrack)
                queens.pop()
                cols.remove(col)
                diag_down.remove(row - col)
                diag_up.remove(row + col)

    backtrack(0)
    return solutions

# Example
solutions = solve_n_queens(4)
print(f"Number of solutions for N=4: {len(solutions)}")   # 2
for sol in solutions:
    print('\n'.join(sol))
    print()
```

## 11.3 Subsets Generation

```python
def generate_subsets(nums: list[int]) -> list[list[int]]:
    """
    Generate all subsets (power set) of nums.

    For nums = [1, 2, 3]:
    [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
    Total: 2^n subsets

    Time: O(2^n)  Space: O(n) recursive stack
    """
    result  = []
    current = []

    def backtrack(start: int) -> None:
        result.append(current[:])   # Record current subset

        for i in range(start, len(nums)):
            current.append(nums[i])     # Include nums[i]
            backtrack(i + 1)            # Recurse
            current.pop()               # Exclude nums[i] (backtrack)

    backtrack(0)
    return result

# Example
print(generate_subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

## 11.4 Complexity of Backtracking

Backtracking is inherently exponential in the worst case, but pruning can dramatically reduce the effective search space:
- Subsets: O(2ⁿ) states × O(n) to copy each = O(n · 2ⁿ)
- N-Queens: O(n!) in the worst case, much less with pruning
- Sudoku: O(9^(empty cells)) naive, far less with constraint propagation

---

> **Practice Questions — Section 11**
> 1. Use backtracking to generate all valid combinations of balanced parentheses for n pairs (e.g., n=3 → `"((()))"`, `"(()())"`, etc.).
> 2. Generate all permutations of a list using backtracking. How does the time complexity compare to generating all subsets?
> 3. Modify the Subsets algorithm to handle duplicate elements without producing duplicate subsets.
> 4. Solve Sudoku using backtracking with constraint propagation. Why does pruning matter so much here?

---

# 12. Further Reading & Resources

## Books

**Beginner to Intermediate:**
- *Introduction to Algorithms* (CLRS) — Cormen, Leiserson, Rivest, Stein. The definitive reference. Dense but comprehensive.
- *Grokking Algorithms* — Aditya Bhargava. Highly visual and beginner-friendly.
- *Algorithm Design Manual* — Steven Skiena. Great for problem-solving intuition and real-world applications.

**Advanced:**
- *The Art of Computer Programming* — Donald Knuth. The classic multi-volume reference.
- *Algorithms* — Sedgewick & Wayne. Excellent Java implementations with strong theory.

## Online Courses

- **MIT OpenCourseWare 6.006** — Introduction to Algorithms (free, with lecture videos and problem sets)
- **Stanford Algorithms Specialization** — Coursera (Tim Roughgarden). Rigorous and well-structured.
- **CS Dojo / NeetCode on YouTube** — Practical interview-focused algorithm walkthroughs.

## Practice Platforms

| Platform | Best For |
|---|---|
| [LeetCode](https://leetcode.com) | Interview prep, problem variety |
| [Codeforces](https://codeforces.com) | Competitive programming |
| [HackerRank](https://hackerrank.com) | Structured learning paths |
| [AlgoExpert](https://algoexpert.io) | Video explanations per problem |
| [Visualgo](https://visualgo.net) | Algorithm animations and visualizations |

## Visualization Tools

- **VisuAlgo** (visualgo.net) — Animated visualizations for almost every algorithm in this guide.
- **Algorithm Visualizer** (algorithm-visualizer.org) — Interactive code + animation.
- **Sorting.at** — Dedicated sorting algorithm visualizer.

## Cheat Sheets & References

- **Big-O Cheat Sheet** (bigocheatsheet.com) — Time/space complexity for common algorithms and data structures.
- **Python `heapq` docs** — For priority queues in graph algorithms.
- **Python `collections.deque`** — For O(1) BFS queues.

## Recommended Learning Path

```
Week 1-2:  Arrays, Strings, Two Pointers, Sliding Window
Week 3-4:  Sorting algorithms (understand all 6 covered here)
Week 5-6:  Recursion, Binary Search, Backtracking
Week 7-8:  Linked Lists, Stacks, Queues
Week 9-10: Trees, BFS, DFS
Week 11-12: Graphs (Dijkstra's, MST)
Week 13-16: Dynamic Programming (start with Fibonacci, then Knapsack, LCS)
Week 17+:  Advanced topics (Segment Trees, Tries, Network Flow)
```

---

## Quick Complexity Reference Card

```
O(1)        Constant     — Hash table lookup, array index
O(log n)    Logarithmic  — Binary search, balanced BST
O(n)        Linear       — Linear search, single-pass scan
O(n log n)  Linearithmic — Merge sort, heap sort, Dijkstra's
O(n²)       Quadratic    — Bubble/Selection/Insertion sort, nested loops
O(n³)       Cubic        — Naive matrix multiplication
O(2ⁿ)       Exponential  — Subsets, brute-force exponential
O(n!)       Factorial    — All permutations
```

---

*End of Algorithms Learning Material — Version 1.0*

*This document covers beginner-to-intermediate algorithms. For advanced topics (Segment Trees, Fenwick Trees, Network Flow, String Matching, Computational Geometry), continue with the resources listed above.*
