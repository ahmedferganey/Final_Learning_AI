# 71. Node.js

> Phase 18 — Backend & Cloud Application Development

Node.js is a server-side JavaScript runtime built around an event-driven, non-blocking I/O model. It is especially strong for network services, APIs, real-time systems, automation, build tooling, and applications that spend significant time waiting on I/O.

A useful mental model is:

```text
JavaScript Source
      ↓
Node.js Runtime
      ↓
V8 JavaScript Engine
      ↓
Node APIs
├─ fs
├─ net
├─ http
├─ stream
├─ crypto
├─ timers
└─ process
      ↓
libuv / OS facilities
      ↓
Filesystem / Sockets / Timers / Thread Pool
```

The key idea is not that "Node.js is single-threaded."

A more accurate mental model is:

```text
JavaScript execution:
primarily one event-loop thread per process

I/O:
delegated to OS and runtime facilities

selected work:
uses background thread-pool or worker threads

parallelism:
can come from workers, processes, containers, or replicas
```

This course develops Node.js from runtime fundamentals through modules, async programming, streams, HTTP servers, process lifecycle, security, observability, testing, performance, and production backend architecture.

## 1. Topic Title

**Node.js**

## 2. Learning Objectives

- Explain Node.js runtime architecture and the role of V8 and libuv.
- Explain the event loop, call stack, task queues, microtasks, timers, and I/O callbacks.
- Explain non-blocking I/O and where Node.js can still block.
- Use CommonJS and ECMAScript modules correctly.
- Use package.json, package managers, lock files, semantic versioning, and dependency scopes.
- Write asynchronous code with callbacks, promises, and async/await.
- Handle promise rejections and asynchronous errors correctly.
- Use timers and cancellation patterns.
- Use Buffers and understand binary data.
- Use Streams for memory-efficient processing.
- Use filesystem APIs safely.
- Use path, URL, process, environment, and OS APIs.
- Build HTTP servers with Node's core HTTP APIs.
- Parse requests, headers, bodies, query strings, and URLs.
- Design middleware-like request pipelines.
- Explain TCP and socket fundamentals in Node.
- Explain EventEmitter and event-driven architecture.
- Use child processes and worker threads appropriately.
- Explain the thread pool and CPU-bound workload limits.
- Design graceful startup and shutdown.
- Manage configuration and secrets.
- Implement structured logging and correlation IDs.
- Use metrics and tracing concepts in Node applications.
- Explain memory, garbage collection, heap, event-loop delay, and common performance bottlenecks.
- Explain clustering/process replication at a conceptual level.
- Design stateless Node.js services for horizontal scaling.
- Explain Node.js security concerns including dependency risk, prototype pollution awareness, SSRF, injection, path traversal, and unsafe child-process execution.
- Implement tests using Node testing concepts and common test-runner patterns.
- Design a production Node.js backend structure.
- Troubleshoot common Node.js failures systematically.

## 3. Prerequisites

Required:

```text
70. Backend Development Fundamentals
JavaScript fundamentals
Git
Linux CLI
HTTP basics
```

Recommended:

```text
Promises and async/await awareness
Basic SQL
Docker
CI/CD
```

Course 71 revisits the JavaScript concepts required for server-side work so a separate standalone JavaScript course is not required.

## 4. Core Concepts Explanation

# Part 1 — What Node.js Is

### Core Explanation

Node.js is a JavaScript runtime for executing JavaScript outside the browser. It provides server-side APIs for files, networking, processes, streams, crypto, and more.

### Example / Visualization

```text
JavaScript + Node APIs → server application
```

### Why It Matters

It enables JavaScript to be used for backend and infrastructure tooling.

### Practical Use

Treat Node as a runtime, not a web framework.

# Part 2 — What Node.js Is Not

### Core Explanation

Node.js is not a programming language and not a web framework.

### Example / Visualization

```text
JavaScript = language
Node.js = runtime
Express/Fastify-like tools = frameworks
```

### Why It Matters

Separating language, runtime, and framework concepts avoids confusion.

### Practical Use

Learn core Node before depending on framework magic.

# Part 3 — V8

### Core Explanation

V8 is the JavaScript engine that parses, compiles, and executes JavaScript inside Node.

### Example / Visualization

```text
JS source → V8 → machine execution
```

### Why It Matters

Runtime performance and memory behavior depend heavily on the engine.

### Practical Use

Understand enough V8 behavior to reason about CPU and memory.

# Part 4 — libuv Awareness

### Core Explanation

libuv provides Node with an event loop and cross-platform abstractions for asynchronous I/O and selected thread-pool work.

### Example / Visualization

```text
Node APIs → libuv → OS/thread pool
```

### Why It Matters

This explains how one JS thread can coordinate many concurrent I/O operations.

### Practical Use

Do not assume every async operation consumes a dedicated JS thread.

# Part 5 — Event-Driven Runtime

### Core Explanation

Node applications often react to events such as incoming sockets, timers, filesystem completion, and stream data.

### Example / Visualization

```text
event occurs → callback runs
```

### Why It Matters

This model suits I/O-heavy workloads.

### Practical Use

Keep callbacks short and non-blocking.

# Part 6 — Call Stack

### Core Explanation

JavaScript function calls execute on a call stack.

### Example / Visualization

```text
main → handler → validate → return
```

### Why It Matters

Only one JS callback normally runs at a time on one event-loop thread.

### Practical Use

Long CPU work blocks progress for other callbacks.

# Part 7 — Event Loop

### Core Explanation

The event loop repeatedly processes ready work when the call stack is empty.

### Example / Visualization

```text
ready callback → execute → next ready callback
```

### Why It Matters

It is central to Node concurrency.

### Practical Use

Measure event-loop delay when diagnosing latency.

# Part 8 — Non-Blocking I/O

### Core Explanation

Non-blocking APIs start I/O and let the event loop continue until completion is ready.

### Example / Visualization

```text
read file → continue other work → callback later
```

### Why It Matters

This gives Node strong concurrency for I/O-heavy services.

### Practical Use

Prefer async APIs in request paths.

# Part 9 — Blocking I/O

### Core Explanation

Synchronous APIs block the JavaScript thread until completion.

### Example / Visualization

```text
fs.readFileSync during request
```

### Why It Matters

Blocking work delays every other request handled by that process.

### Practical Use

Avoid sync filesystem/crypto/CPU operations in hot request paths.

# Part 10 — Concurrency vs Parallelism

### Core Explanation

Concurrency means many operations make progress over time; parallelism means work executes simultaneously on multiple cores/threads/processes.

### Example / Visualization

```text
event loop = concurrent I/O
worker threads/processes = parallel CPU
```

### Why It Matters

Node can do both, but through different mechanisms.

### Practical Use

Match the mechanism to the workload.

# Part 11 — Single-Threaded Misconception

### Core Explanation

The main JS execution context is typically one thread, but Node uses OS async I/O, a thread pool for selected operations, and can use workers/processes.

### Example / Visualization

```text
JS thread + OS + thread pool + workers
```

### Why It Matters

Calling Node simply 'single-threaded' hides its architecture.

### Practical Use

Distinguish JS execution from runtime internals.

# Part 12 — CPU-Bound Work

### Core Explanation

Long-running CPU computation blocks the event loop if executed on the main JS thread.

### Example / Visualization

```text
large compression/calculation loop → latency spike
```

### Why It Matters

Node services can become unresponsive even with low I/O wait.

### Practical Use

Move CPU-heavy work to worker threads/processes/services.

# Part 13 — I/O-Bound Work

### Core Explanation

I/O-bound applications spend much of their time waiting for network, filesystem, or database responses.

### Example / Visualization

```text
API → DB/network waits
```

### Why It Matters

Node is well-suited to many such workloads.

### Practical Use

Still apply connection pools, timeouts, and backpressure.

# Part 14 — JavaScript Values Refresher

### Core Explanation

Node uses the standard JavaScript types: primitives and objects.

### Example / Visualization

```text
string, number, bigint, boolean, null, undefined, symbol, object
```

### Why It Matters

Backend correctness depends on type/serialization behavior.

### Practical Use

Be careful with numeric precision and null/undefined semantics.

# Part 15 — Objects

### Core Explanation

Objects store key-value properties and behavior.

### Example / Visualization

```text
const user = { id: 1, name: 'A' }
```

### Why It Matters

Most backend data structures are objects.

### Practical Use

Avoid mutating shared objects unexpectedly.

# Part 16 — Arrays

### Core Explanation

Arrays store ordered collections.

### Example / Visualization

```text
const ids = [1,2,3]
```

### Why It Matters

Common for records and transformations.

### Practical Use

Watch memory usage for very large arrays; streams may be better.

# Part 17 — Destructuring

### Core Explanation

Destructuring extracts values from objects/arrays.

### Example / Visualization

```text
const { id, name } = user
```

### Why It Matters

Useful for DTO processing and module imports.

### Practical Use

Avoid destructuring undefined values without validation.

# Part 18 — Spread Syntax

### Core Explanation

Spread copies/combines enumerable values.

### Example / Visualization

```text
const copy = { ...obj }
```

### Why It Matters

Useful for immutable-style updates.

### Practical Use

Shallow copy does not deeply clone nested objects.

# Part 19 — Rest Parameters

### Core Explanation

Rest gathers remaining arguments/properties.

### Example / Visualization

```text
function f(...args)
```

### Why It Matters

Useful in utilities and wrappers.

### Practical Use

Keep public function interfaces explicit.

# Part 20 — Optional Chaining

### Core Explanation

Optional chaining safely accesses nested values.

### Example / Visualization

```text
user.profile?.email
```

### Why It Matters

Prevents some null-reference errors.

### Practical Use

Do not use it to hide required-data validation.

# Part 21 — Nullish Coalescing

### Core Explanation

`??` provides fallback only for null/undefined.

### Example / Visualization

```text
value ?? defaultValue
```

### Why It Matters

Different from `||`, which also treats 0/false/empty string as false.

### Practical Use

Use when zero/false are valid values.

# Part 22 — Strict Equality

### Core Explanation

Use `===`/`!==` for predictable comparisons.

### Example / Visualization

```text
1 === '1' → false
```

### Why It Matters

Avoid implicit coercion surprises.

### Practical Use

Prefer explicit conversions.

# Part 23 — Functions

### Core Explanation

Functions are first-class values and can be passed as callbacks.

### Example / Visualization

```text
array.map(fn)
```

### Why It Matters

This underpins event-driven and functional patterns.

### Practical Use

Keep callback contracts clear.

# Part 24 — Arrow Functions

### Core Explanation

Arrow functions provide concise syntax and lexical `this`.

### Example / Visualization

```text
const add = (a,b) => a+b
```

### Why It Matters

Useful in callbacks.

### Practical Use

Do not use when dynamic `this` binding is required.

# Part 25 — Closures

### Core Explanation

A closure captures variables from surrounding scope.

### Example / Visualization

```text
handler captures config
```

### Why It Matters

Useful for factories and middleware.

### Practical Use

Captured objects can also keep memory alive unexpectedly.

# Part 26 — Classes

### Core Explanation

JavaScript classes provide prototype-based object syntax.

### Example / Visualization

```text
class OrderService { ... }
```

### Why It Matters

Useful for service objects but not mandatory.

### Practical Use

Prefer the simplest abstraction that communicates intent.

# Part 27 — Prototype Chain

### Core Explanation

Objects inherit through prototypes.

### Example / Visualization

```text
object → prototype → Object.prototype
```

### Why It Matters

Important for language behavior and some security concerns.

### Practical Use

Avoid unsafe merging of untrusted object keys.

# Part 28 — Error Object

### Core Explanation

JavaScript errors carry message, stack, and type information.

### Example / Visualization

```text
throw new Error('failed')
```

### Why It Matters

Backend error handling relies on consistent error objects.

### Practical Use

Create domain-specific error types when useful.

# Part 29 — try/catch

### Core Explanation

`try/catch` handles synchronous errors and awaited promise rejections.

### Example / Visualization

```text
try { await work() } catch (err) { ... }
```

### Why It Matters

Essential for async control flow.

### Practical Use

Do not catch errors only to ignore them.

# Part 30 — finally

### Core Explanation

`finally` executes cleanup regardless of success or error.

### Example / Visualization

```text
try → finally close resource
```

### Why It Matters

Important for resource cleanup.

### Practical Use

Use for locks/files/temp resources.

# Part 31 — Module

### Core Explanation

A module encapsulates code and exposes selected values.

### Example / Visualization

```text
module → exports/imports
```

### Why It Matters

Modules are the unit of code organization and dependency boundaries.

### Practical Use

Keep module responsibilities cohesive.

# Part 32 — CommonJS

### Core Explanation

CommonJS traditionally uses `require()` and `module.exports`.

### Example / Visualization

```text
const fs = require('node:fs')
```

### Why It Matters

Still encountered in Node ecosystems.

### Practical Use

Do not mix module systems without understanding interop.

# Part 33 — ECMAScript Modules

### Core Explanation

ESM uses `import` and `export`.

### Example / Visualization

```text
import fs from 'node:fs'
```

### Why It Matters

It is the standard JavaScript module syntax.

### Practical Use

Use explicit package/module configuration.

# Part 34 — package.json

### Core Explanation

`package.json` describes package identity, scripts, dependencies, module mode, and metadata.

### Example / Visualization

```text
name/version/scripts/dependencies
```

### Why It Matters

It is central to Node projects.

### Practical Use

Review it like source code.

# Part 35 — Package Scripts

### Core Explanation

Scripts provide canonical commands for build, test, lint, start, and tooling.

### Example / Visualization

```text
npm run test
```

### Why It Matters

CI and developers should use the same commands.

### Practical Use

Avoid hiding critical logic only in CI YAML.

# Part 36 — Dependencies

### Core Explanation

Runtime dependencies are packages needed by the application in production.

### Example / Visualization

```text
dependencies
```

### Why It Matters

They affect runtime security and artifact size.

### Practical Use

Keep dependency set minimal.

# Part 37 — Dev Dependencies

### Core Explanation

Development dependencies support tests, lint, build, and tooling.

### Example / Visualization

```text
devDependencies
```

### Why It Matters

Usually not needed in production runtime image.

### Practical Use

Separate build and runtime stages.

# Part 38 — Peer Dependencies

### Core Explanation

Peer dependencies express compatibility expectations with a host package.

### Example / Visualization

```text
peerDependencies
```

### Why It Matters

Common in libraries/plugins.

### Practical Use

Understand version ranges.

# Part 39 — Semantic Versioning

### Core Explanation

Semantic versioning communicates compatibility intent with MAJOR.MINOR.PATCH.

### Example / Visualization

```text
2.4.1
```

### Why It Matters

Package updates can change behavior.

### Practical Use

Review breaking changes rather than blindly updating.

# Part 40 — Version Range

### Core Explanation

Package manifests can allow version ranges.

### Example / Visualization

```text
^1.2.3 / ~1.2.3 concepts
```

### Why It Matters

Ranges influence future resolution.

### Practical Use

Lock files preserve an exact resolved graph.

# Part 41 — Lock File

### Core Explanation

A lock file records exact dependency resolution.

### Example / Visualization

```text
package-lock / pnpm-lock / yarn lock
```

### Why It Matters

It improves reproducible installs.

### Practical Use

Commit the lock file.

# Part 42 — Package Manager

### Core Explanation

Node projects commonly use npm-compatible package managers for dependency install and scripts.

### Example / Visualization

```text
install / update / audit / run
```

### Why It Matters

Package-manager behavior affects reproducibility and CI.

### Practical Use

Standardize one manager per repository.

# Part 43 — Clean Install

### Core Explanation

CI should install from the lock file without silently changing dependency versions.

### Example / Visualization

```text
frozen/clean install concept
```

### Why It Matters

Prevents CI from resolving a different graph.

### Practical Use

Fail if lock and manifest disagree.

# Part 44 — Transitive Dependency

### Core Explanation

A package can depend on packages that your application did not declare directly.

### Example / Visualization

```text
app → A → B → C
```

### Why It Matters

Supply-chain exposure extends beyond direct dependencies.

### Practical Use

Inspect and update the full dependency tree.

# Part 45 — Dependency Audit

### Core Explanation

Dependency scanning looks for known vulnerabilities and risk.

### Example / Visualization

```text
lock file → scanner
```

### Why It Matters

Node ecosystems can contain many transitive packages.

### Practical Use

Treat audit findings with severity/context, not panic.

# Part 46 — Package Provenance Awareness

### Core Explanation

Packages can carry metadata or attestations describing how they were built/published.

### Example / Visualization

```text
source → trusted build → package
```

### Why It Matters

Supply-chain assurance is increasingly important.

### Practical Use

Prefer trusted registries and controlled publishing.

# Part 47 — Private Registry

### Core Explanation

Organizations may proxy or host packages internally.

### Example / Visualization

```text
CI → internal registry → upstream
```

### Why It Matters

Improves governance, caching, and availability.

### Practical Use

Protect publish permissions.

# Part 48 — Scoped Package

### Core Explanation

Scoped package names group packages under an organization/namespace.

### Example / Visualization

```text
@org/package
```

### Why It Matters

Useful for internal libraries.

### Practical Use

Control registry scope configuration.

# Part 49 — Global Install Caution

### Core Explanation

Global packages create hidden machine state.

### Example / Visualization

```text
npm -g tool
```

### Why It Matters

They reduce reproducibility.

### Practical Use

Prefer project-local tooling or managed tool images.

# Part 50 — Node Built-In Module Prefix

### Core Explanation

Core modules can be imported with the `node:` prefix.

### Example / Visualization

```text
import fs from 'node:fs'
```

### Why It Matters

Makes built-in dependency explicit.

### Practical Use

Use consistently in modern codebases.

# Part 51 — Callback

### Core Explanation

A callback is a function invoked later when an operation or event completes.

### Example / Visualization

```text
readFile(path, callback)
```

### Why It Matters

Callbacks are a foundational async pattern.

### Practical Use

Prefer error-first conventions where applicable.

# Part 52 — Error-First Callback

### Core Explanation

Traditional Node callbacks often receive `(err, result)`.

### Example / Visualization

```text
(err, data) => {}
```

### Why It Matters

Makes error flow explicit.

### Practical Use

Return after handling errors to avoid double responses.

# Part 53 — Callback Hell

### Core Explanation

Deep nested callbacks reduce readability and error handling clarity.

### Example / Visualization

```text
a(()=>b(()=>c(...)))
```

### Why It Matters

Promises/async-await improve composition.

### Practical Use

Break work into named functions.

# Part 54 — Promise

### Core Explanation

A Promise represents a future fulfillment or rejection.

### Example / Visualization

```text
fetchData().then(...).catch(...)
```

### Why It Matters

Promises compose asynchronous operations.

### Practical Use

Always handle rejection.

# Part 55 — Promise States

### Core Explanation

A promise is pending, fulfilled, or rejected.

### Example / Visualization

```text
pending → fulfilled/rejected
```

### Why It Matters

State transition happens once.

### Practical Use

Do not expect to mutate a settled promise.

# Part 56 — then

### Core Explanation

`.then()` handles fulfillment and returns a new promise.

### Example / Visualization

```text
p.then(transform)
```

### Why It Matters

Allows chaining.

### Practical Use

Return nested promises so the chain waits.

# Part 57 — catch

### Core Explanation

`.catch()` handles rejection.

### Example / Visualization

```text
p.catch(handle)
```

### Why It Matters

Centralizes promise errors.

### Practical Use

Avoid swallowing errors unintentionally.

# Part 58 — finally on Promise

### Core Explanation

`.finally()` runs cleanup regardless of outcome.

### Example / Visualization

```text
p.finally(cleanup)
```

### Why It Matters

Useful for counters/resources.

### Practical Use

It does not receive the result directly.

# Part 59 — async Function

### Core Explanation

An `async` function always returns a promise.

### Example / Visualization

```text
async function f(){ return 1 }
```

### Why It Matters

Enables synchronous-looking async code.

### Practical Use

Callers still must await/handle its promise.

# Part 60 — await

### Core Explanation

`await` pauses the async function until a promise settles without blocking the entire event loop.

### Example / Visualization

```text
const data = await query()
```

### Why It Matters

Improves readability.

### Practical Use

Sequential awaits can be unnecessarily slow if work is independent.

# Part 61 — Sequential Await

### Core Explanation

Independent awaited operations run one after another if written sequentially.

### Example / Visualization

```text
await A(); await B();
```

### Why It Matters

Can increase latency.

### Practical Use

Use concurrency when operations are independent and safe.

# Part 62 — Promise.all

### Core Explanation

`Promise.all` waits for multiple promises and rejects if one rejects.

### Example / Visualization

```text
await Promise.all([A(),B()])
```

### Why It Matters

Runs independent async work concurrently.

### Practical Use

Bound concurrency for large collections.

# Part 63 — Promise.allSettled

### Core Explanation

Waits for every promise and returns each outcome.

### Example / Visualization

```text
allSettled([...])
```

### Why It Matters

Useful when partial failures should be reported.

### Practical Use

Do not use when one failure must stop the operation.

# Part 64 — Promise.race

### Core Explanation

Settles with the first settled input.

### Example / Visualization

```text
Promise.race([...])
```

### Why It Matters

Can support timeout-like patterns.

### Practical Use

Use cancellation where possible so losing work does not continue uselessly.

# Part 65 — Promise.any

### Core Explanation

Fulfills when the first promise fulfills, rejecting only if all reject.

### Example / Visualization

```text
Promise.any([...])
```

### Why It Matters

Useful for redundant sources.

### Practical Use

Understand aggregated failure behavior.

# Part 66 — Microtask Queue

### Core Explanation

Promise reactions and certain callbacks run as microtasks at defined points before the event loop advances to later phases.

### Example / Visualization

```text
promise.then → microtask
```

### Why It Matters

Microtasks have high scheduling priority.

### Practical Use

An endless microtask chain can starve other work.

# Part 67 — process.nextTick Awareness

### Core Explanation

`process.nextTick` schedules callbacks before the event loop continues and has special priority semantics.

### Example / Visualization

```text
nextTick queue
```

### Why It Matters

Overuse can starve I/O.

### Practical Use

Use only when its precise semantics are needed.

# Part 68 — Timer Queue Awareness

### Core Explanation

Timers become eligible after their delay threshold; exact execution time is not guaranteed.

### Example / Visualization

```text
setTimeout(fn,100)
```

### Why It Matters

Event-loop load can delay execution.

### Practical Use

Do not use timers as precise clocks.

# Part 69 — setTimeout

### Core Explanation

Schedules a callback after at least a delay.

### Example / Visualization

```text
setTimeout(fn, 1000)
```

### Why It Matters

Useful for deferred work and timeouts.

### Practical Use

Clear/cancel timers when no longer needed.

# Part 70 — setInterval

### Core Explanation

Schedules repeated callback attempts.

### Example / Visualization

```text
setInterval(fn, 1000)
```

### Why It Matters

Useful for simple periodic work.

### Practical Use

Long callback duration and overlap need consideration.

# Part 71 — setImmediate Awareness

### Core Explanation

Schedules work for a later event-loop phase.

### Example / Visualization

```text
setImmediate(fn)
```

### Why It Matters

Different scheduling from timers/nextTick.

### Practical Use

Use when you specifically need to yield to I/O/event loop.

# Part 72 — AbortController Awareness

### Core Explanation

Abort signals can propagate cancellation to supported APIs.

### Example / Visualization

```text
controller.abort()
```

### Why It Matters

Cancellation prevents wasted work.

### Practical Use

Propagate client disconnect/deadlines where supported.

# Part 73 — Async Error Boundary

### Core Explanation

Errors thrown inside an awaited async call can be caught with surrounding `try/catch`.

### Example / Visualization

```text
try { await query() } catch(e) {}
```

### Why It Matters

Creates structured error flow.

### Practical Use

Handle errors once at the appropriate boundary.

# Part 74 — Unhandled Rejection

### Core Explanation

A promise rejection without a handler can destabilize or terminate application behavior depending on runtime handling.

### Example / Visualization

```text
promise rejects, nobody awaits/catches
```

### Why It Matters

It indicates a programming defect.

### Practical Use

Treat as fatal or highly visible and fix root cause.

# Part 75 — Async Resource Cleanup

### Core Explanation

Asynchronous resources still need deterministic cleanup.

### Example / Visualization

```text
try { await use() } finally { await close() }
```

### Why It Matters

Leaks can exhaust pools/sockets/files.

### Practical Use

Use `finally` or structured resource APIs.

# Part 76 — Concurrency Limiting

### Core Explanation

Launching thousands of promises at once can overload DBs or APIs.

### Example / Visualization

```text
map 100k items → Promise.all ✗
```

### Why It Matters

Async does not mean infinite capacity.

### Practical Use

Use bounded worker pools/semaphores.

# Part 77 — Backpressure in Async Work

### Core Explanation

Producers must slow when consumers cannot process data fast enough.

### Example / Visualization

```text
producer > consumer
```

### Why It Matters

Prevents memory growth and dependency overload.

### Practical Use

Streams and queues provide structured backpressure.

# Part 78 — EventEmitter

### Core Explanation

`EventEmitter` implements publish/subscribe inside a Node process.

### Example / Visualization

```text
emitter.on('event', handler)
```

### Why It Matters

Many Node APIs are event-driven.

### Practical Use

Remove listeners when lifecycle ends.

# Part 79 — Event Listener

### Core Explanation

A listener executes when an event is emitted.

### Example / Visualization

```text
on('data', fn)
```

### Why It Matters

Useful for decoupled in-process events.

### Practical Use

Keep listener work short or async-safe.

# Part 80 — once Listener

### Core Explanation

A one-time listener removes itself after first event.

### Example / Visualization

```text
once('ready', fn)
```

### Why It Matters

Useful for initialization/one-shot events.

### Practical Use

Avoid duplicate initialization.

# Part 81 — Error Event

### Core Explanation

Some EventEmitter-based APIs use a special `error` event.

### Example / Visualization

```text
emitter.on('error', handler)
```

### Why It Matters

Missing error listeners can produce process-level failures in relevant APIs.

### Practical Use

Always understand the error contract of an emitter.

# Part 82 — Listener Leak

### Core Explanation

Repeatedly adding listeners without removal can consume memory and duplicate work.

### Example / Visualization

```text
per-request listener never removed
```

### Why It Matters

Often indicates lifecycle bugs.

### Practical Use

Track listener ownership.

# Part 83 — Buffer

### Core Explanation

A Buffer represents binary bytes.

### Example / Visualization

```text
Buffer.from('abc')
```

### Why It Matters

Needed for network, file, crypto, and protocol data.

### Practical Use

Know encoding when converting to/from strings.

# Part 84 — Encoding

### Core Explanation

Common string encodings include UTF-8 and base64 representations.

### Example / Visualization

```text
Buffer ↔ UTF-8/base64
```

### Why It Matters

Wrong encoding corrupts data.

### Practical Use

Never assume binary data is text.

# Part 85 — Binary vs Text

### Core Explanation

Not every request/file/socket payload is UTF-8 text.

### Example / Visualization

```text
image bytes ≠ string
```

### Why It Matters

Converting large binary data to strings wastes memory and can corrupt content.

### Practical Use

Keep binary data as Buffers/streams.

# Part 86 — Stream

### Core Explanation

A stream processes data incrementally rather than loading everything into memory.

### Example / Visualization

```text
large file → chunks
```

### Why It Matters

Essential for large payload efficiency.

### Practical Use

Prefer streams for large files/network pipelines.

# Part 87 — Readable Stream

### Core Explanation

Produces chunks of data.

### Example / Visualization

```text
file/network input
```

### Why It Matters

Consumers can read gradually.

### Practical Use

Respect backpressure.

# Part 88 — Writable Stream

### Core Explanation

Consumes chunks of data.

### Example / Visualization

```text
file/network output
```

### Why It Matters

Writes may return false when buffer is full.

### Practical Use

Wait for drain instead of continuing unbounded writes.

# Part 89 — Duplex Stream

### Core Explanation

Can read and write.

### Example / Visualization

```text
TCP socket
```

### Why It Matters

Useful for bidirectional protocols.

### Practical Use

Read and write sides have separate flow.

# Part 90 — Transform Stream

### Core Explanation

Transforms incoming chunks into outgoing chunks.

### Example / Visualization

```text
compression/encryption/parser
```

### Why It Matters

Supports streaming pipelines.

### Practical Use

Avoid buffering entire content in a transform unnecessarily.

# Part 91 — Backpressure in Streams

### Core Explanation

Backpressure prevents a fast producer from overwhelming a slower consumer.

### Example / Visualization

```text
read fast → write slow → pause/resume
```

### Why It Matters

Keeps memory bounded.

### Practical Use

Use pipeline utilities rather than manual piping where error handling matters.

# Part 92 — pipe

### Core Explanation

Connects readable output to writable input.

### Example / Visualization

```text
readable.pipe(writable)
```

### Why It Matters

Simple stream composition.

### Practical Use

Use more robust pipeline helpers for cleanup/error propagation.

# Part 93 — pipeline Concept

### Core Explanation

A pipeline composes streams and propagates completion/errors.

### Example / Visualization

```text
read → gzip → write
```

### Why It Matters

Safer than manually wiring every event.

### Practical Use

Ensure resources close on failure.

# Part 94 — HighWaterMark Awareness

### Core Explanation

Streams buffer data up to configured thresholds.

### Example / Visualization

```text
internal buffer threshold
```

### Why It Matters

It affects memory/throughput trade-offs.

### Practical Use

Tune only with measurement.

# Part 95 — Streaming HTTP Response

### Core Explanation

A server can send response data incrementally.

### Example / Visualization

```text
DB/file stream → response
```

### Why It Matters

Reduces time-to-first-byte and memory use.

### Practical Use

Handle client disconnect and backpressure.

# Part 96 — Streaming Upload

### Core Explanation

Incoming request bodies can be processed as streams.

### Example / Visualization

```text
request → parser/storage stream
```

### Why It Matters

Avoids buffering huge files in memory.

### Practical Use

Apply size limits and validation.

# Part 97 — Filesystem API

### Core Explanation

Node provides asynchronous and synchronous filesystem operations.

### Example / Visualization

```text
readFile / writeFile / streams
```

### Why It Matters

Filesystem is a common backend/tooling dependency.

### Practical Use

Prefer async or streams in request paths.

# Part 98 — fs.promises

### Core Explanation

Promise-based filesystem APIs integrate naturally with async/await.

### Example / Visualization

```text
await fs.promises.readFile(...)
```

### Why It Matters

Simplifies async file code.

### Practical Use

Still avoid reading huge files fully into memory.

# Part 99 — File Descriptor

### Core Explanation

Open files/sockets consume OS descriptors.

### Example / Visualization

```text
open → fd → close
```

### Why It Matters

Descriptor leaks can crash a service.

### Practical Use

Close resources deterministically.

# Part 100 — Path Module

### Core Explanation

Path utilities build and normalize filesystem paths.

### Example / Visualization

```text
path.join(base,name)
```

### Why It Matters

Safer than manual separators across OSes.

### Practical Use

Validation is still needed against traversal.

# Part 101 — Path Traversal

### Core Explanation

Untrusted path fragments can escape intended directories.

### Example / Visualization

```text
../../secret
```

### Why It Matters

Potential data exposure.

### Practical Use

Generate internal filenames or enforce safe roots.

# Part 102 — URL Class

### Core Explanation

The WHATWG URL class parses URLs safely.

### Example / Visualization

```text
new URL(request.url, base)
```

### Why It Matters

Useful for query/path parsing.

### Practical Use

Do not parse URLs with ad-hoc string splitting.

# Part 103 — process Object

### Core Explanation

`process` exposes runtime metadata, environment, signals, exit behavior, and streams.

### Example / Visualization

```text
process.env / process.pid
```

### Why It Matters

Central to service lifecycle.

### Practical Use

Avoid scattering environment reads throughout business code.

# Part 104 — process.env

### Core Explanation

Environment variables are exposed as strings.

### Example / Visualization

```text
process.env.PORT
```

### Why It Matters

Common configuration source.

### Practical Use

Parse and validate once.

# Part 105 — Exit Code

### Core Explanation

Processes communicate success/failure to supervisors through exit codes.

### Example / Visualization

```text
0 success / non-zero failure
```

### Why It Matters

Supervisors and CI rely on it.

### Practical Use

Use non-zero for fatal startup/runtime failures.

# Part 106 — Signals

### Core Explanation

Operating systems deliver signals such as termination requests.

### Example / Visualization

```text
SIGTERM
```

### Why It Matters

Containers/orchestrators use them for graceful shutdown.

### Practical Use

Register lifecycle handling.

# Part 107 — stdout/stderr

### Core Explanation

Standard streams are common destinations for application logs.

### Example / Visualization

```text
console/logging → stdout/stderr
```

### Why It Matters

Container platforms collect them naturally.

### Practical Use

Use structured logger rather than ad-hoc prints in production.

# Part 108 — Current Working Directory

### Core Explanation

`process.cwd()` is the directory from which the process was started.

### Example / Visualization

```text
cwd ≠ module directory
```

### Why It Matters

Relative path assumptions can break in production.

### Practical Use

Resolve configuration/assets deliberately.

# Part 109 — Environment Detection

### Core Explanation

Applications often behave differently in development/test/production.

### Example / Visualization

```text
NODE_ENV-like setting concept
```

### Why It Matters

Some behavior must vary, but artifact should remain the same.

### Practical Use

Avoid massive environment-specific code branches.

# Part 110 — OS Module Awareness

### Core Explanation

OS APIs expose CPU, memory, hostname, and platform information.

### Example / Visualization

```text
os.cpus()
```

### Why It Matters

Useful for diagnostics.

### Practical Use

Container limits may differ from host-level information.

# Part 111 — Core HTTP Server

### Core Explanation

Node's HTTP module can create an HTTP server without a framework.

### Example / Visualization

```text
createServer((req,res)=>{})
```

### Why It Matters

Understanding core behavior makes frameworks easier to reason about.

### Practical Use

Build one simple server manually.

# Part 112 — IncomingMessage

### Core Explanation

The request object represents method, headers, URL, socket, and a readable body stream.

### Example / Visualization

```text
req.method / req.url / req.headers
```

### Why It Matters

It is a stream-based interface.

### Practical Use

Do not assume body is already parsed.

# Part 113 — ServerResponse

### Core Explanation

The response object writes status, headers, and body.

### Example / Visualization

```text
res.statusCode / res.setHeader / res.end
```

### Why It Matters

You must end or stream a response correctly.

### Practical Use

Prevent double responses.

# Part 114 — Request Body Accumulation

### Core Explanation

Small JSON bodies can be collected from chunks before parsing.

### Example / Visualization

```text
chunks → Buffer.concat → JSON.parse
```

### Why It Matters

Demonstrates stream behavior.

### Practical Use

Always enforce size limits.

# Part 115 — JSON Parse Error

### Core Explanation

Malformed JSON should become a controlled 4xx error.

### Example / Visualization

```text
JSON.parse throws
```

### Why It Matters

Do not expose stack traces.

### Practical Use

Catch parsing separately from business errors.

# Part 116 — Route Matching

### Core Explanation

Without a framework, route matching is manual logic over method/path.

### Example / Visualization

```text
if GET /health
```

### Why It Matters

Shows what frameworks automate.

### Practical Use

Keep route tables explicit.

# Part 117 — HTTP Headers in Node

### Core Explanation

Headers are accessible through request/response APIs.

### Example / Visualization

```text
authorization / content-type
```

### Why It Matters

Header names and normalization matter.

### Practical Use

Validate content type and credentials.

# Part 118 — HTTP Keep-Alive

### Core Explanation

Node clients/servers can reuse connections.

### Example / Visualization

```text
many requests over fewer sockets
```

### Why It Matters

Connection reuse improves efficiency.

### Practical Use

Tune only after understanding defaults and load.

# Part 119 — HTTP Client Awareness

### Core Explanation

Node can make outbound HTTP(S) requests using built-in or higher-level APIs.

### Example / Visualization

```text
service → partner API
```

### Why It Matters

Outbound calls need timeouts and cancellation.

### Practical Use

Do not let dependencies hang indefinitely.

# Part 120 — TCP Socket

### Core Explanation

Node's networking APIs expose TCP sockets for lower-level protocols.

### Example / Visualization

```text
client ↔ socket ↔ server
```

### Why It Matters

HTTP ultimately relies on transport connections.

### Practical Use

Useful for understanding connection errors.

# Part 121 — TCP Server

### Core Explanation

A TCP server listens on an address/port and accepts sockets.

### Example / Visualization

```text
listen :9000
```

### Why It Matters

Foundation for custom protocols.

### Practical Use

Implement framing and limits carefully.

# Part 122 — Socket Backpressure

### Core Explanation

Socket writes can outpace the receiver.

### Example / Visualization

```text
write returns false → wait drain
```

### Why It Matters

Unbounded writes increase memory.

### Practical Use

Respect writable backpressure.

# Part 123 — Connection Error

### Core Explanation

Network clients can fail during DNS, TCP connect, TLS, or response phases.

### Example / Visualization

```text
ENOTFOUND / ECONNREFUSED / timeout
```

### Why It Matters

Error type helps locate the failure layer.

### Practical Use

Log operation and destination safely.

# Part 124 — DNS Awareness

### Core Explanation

Node resolves hostnames through OS/runtime facilities.

### Example / Visualization

```text
service.example → IP
```

### Why It Matters

DNS failures can look like app failures.

### Practical Use

Distinguish resolution from connection errors.

# Part 125 — TLS Awareness

### Core Explanation

HTTPS/TLS requires certificate trust, hostname validation, and secure configuration.

### Example / Visualization

```text
HTTPS → TLS → HTTP
```

### Why It Matters

Backend clients and servers depend on correct TLS.

### Practical Use

Do not disable certificate verification to 'fix' errors.

# Part 126 — WebSocket Awareness

### Core Explanation

WebSockets provide persistent bidirectional application messaging over an upgraded connection.

### Example / Visualization

```text
Client ⇄ Server
```

### Why It Matters

Useful for real-time applications.

### Practical Use

Long-lived connections change scaling/load-balancing considerations.

# Part 127 — Child Process

### Core Explanation

Node can launch external processes.

### Example / Visualization

```text
spawn(command,args)
```

### Why It Matters

Useful for trusted system tooling.

### Practical Use

Never concatenate untrusted input into shell commands.

# Part 128 — spawn vs exec Awareness

### Core Explanation

Spawn streams process I/O; exec-like APIs commonly buffer shell-command output.

### Example / Visualization

```text
spawn good for long output
```

### Why It Matters

Buffering and shell interpretation affect security/performance.

### Practical Use

Prefer direct executable + argument arrays.

# Part 129 — Shell Injection Risk

### Core Explanation

Passing untrusted data into a shell command can execute unintended commands.

### Example / Visualization

```text
`sh -c` + user input ✗
```

### Why It Matters

Potential remote code execution.

### Practical Use

Avoid shell mode for untrusted input.

# Part 130 — Worker Thread

### Core Explanation

Worker threads execute JavaScript in parallel threads within a process.

### Example / Visualization

```text
main thread → worker
```

### Why It Matters

Useful for CPU-bound JavaScript tasks.

### Practical Use

Do not use workers merely for ordinary async I/O.

# Part 131 — Worker Pool Pattern

### Core Explanation

A bounded set of workers handles CPU-heavy jobs.

### Example / Visualization

```text
requests → worker pool
```

### Why It Matters

Prevents creating one worker per request.

### Practical Use

Measure queue latency.

# Part 132 — Thread Pool Awareness

### Core Explanation

Selected Node APIs use an internal background thread pool.

### Example / Visualization

```text
crypto/fs/DNS-like selected work
```

### Why It Matters

Thread-pool saturation can cause latency even when JS CPU looks low.

### Practical Use

Measure and avoid unbounded heavy operations.

# Part 133 — Process Replication

### Core Explanation

Multiple Node processes can use multiple CPU cores and improve failure isolation.

### Example / Visualization

```text
LB → process1/process2/process3
```

### Why It Matters

One event-loop thread does not use all cores for JS by itself.

### Practical Use

Containers/orchestrators often handle replication.

# Part 134 — Stateless Process

### Core Explanation

Each Node process should avoid unique durable local state.

### Example / Visualization

```text
request can hit any replica
```

### Why It Matters

Supports horizontal scaling.

### Practical Use

Externalize sessions and durable data.

# Part 135 — Memory Heap

### Core Explanation

JavaScript objects primarily live in a managed heap.

### Example / Visualization

```text
objects → heap → GC
```

### Why It Matters

Heap growth affects latency and OOM behavior.

### Practical Use

Monitor heap used and process RSS.

# Part 136 — Garbage Collection Awareness

### Core Explanation

The JS engine reclaims unreachable memory automatically.

### Example / Visualization

```text
allocate → unreachable → GC
```

### Why It Matters

GC is automatic but not free.

### Practical Use

High allocation rates can increase pauses and CPU.

# Part 137 — Memory Leak

### Core Explanation

A leak occurs when objects remain reachable longer than intended.

### Example / Visualization

```text
global map/listener/cache grows forever
```

### Why It Matters

Eventually causes high memory/OOM.

### Practical Use

Profile heap snapshots and lifecycle ownership.

# Part 138 — Closure Retention

### Core Explanation

Closures can keep large objects alive.

### Example / Visualization

```text
listener captures request object
```

### Why It Matters

A subtle leak source.

### Practical Use

Capture only what is needed.

# Part 139 — Event Listener Leak

### Core Explanation

Listeners added repeatedly without removal retain references and duplicate behavior.

### Example / Visualization

```text
on per request
```

### Why It Matters

Common leak pattern.

### Practical Use

Own listener lifecycle.

# Part 140 — Unbounded Cache

### Core Explanation

An in-process Map used as cache can grow without limit.

### Example / Visualization

```text
Map size ↑ forever
```

### Why It Matters

Memory leak by design.

### Practical Use

Use size/TTL bounds.

# Part 141 — Large JSON Parsing

### Core Explanation

Parsing huge JSON blocks the event loop and consumes memory.

### Example / Visualization

```text
100MB JSON.parse
```

### Why It Matters

Can cause latency spikes or denial of service.

### Practical Use

Enforce body limits; stream where appropriate.

# Part 142 — Event-Loop Delay

### Core Explanation

Event-loop delay measures how long ready work waits because the JS thread is busy.

### Example / Visualization

```text
ready callback waits 200ms
```

### Why It Matters

Strong indicator of blocking work.

### Practical Use

Monitor under load.

# Part 143 — Throughput vs Latency

### Core Explanation

Optimizing requests/sec can worsen tail latency if queues become saturated.

### Example / Visualization

```text
higher throughput, p99 explodes
```

### Why It Matters

User experience depends on latency distribution.

### Practical Use

Measure p95/p99 and saturation.

# Part 144 — Profiling

### Core Explanation

CPU profiles and flame graphs can reveal expensive functions.

### Example / Visualization

```text
hot function consumes 60% CPU
```

### Why It Matters

Evidence beats guessing.

### Practical Use

Profile representative load.

# Part 145 — Heap Profiling

### Core Explanation

Heap snapshots help identify retained object graphs.

### Example / Visualization

```text
large Map retains users
```

### Why It Matters

Useful for memory leaks.

### Practical Use

Take snapshots carefully in production due to cost.

# Part 146 — Dependency Security

### Core Explanation

Node applications often depend on many packages.

### Example / Visualization

```text
app → hundreds of packages
```

### Why It Matters

Supply-chain risk is material.

### Practical Use

Pin lock files, scan dependencies, minimize packages.

# Part 147 — Prototype Pollution Awareness

### Core Explanation

Unsafe merging of untrusted keys into objects can alter object prototypes in vulnerable code patterns.

### Example / Visualization

```text
__proto__-like keys
```

### Why It Matters

Can corrupt application logic.

### Practical Use

Use safe merge libraries/patterns and validate object keys.

# Part 148 — SSRF in Node

### Core Explanation

URL-fetching features can be abused to access unintended destinations.

### Example / Visualization

```text
fetch(userUrl) → internal service
```

### Why It Matters

Node services often have internal network access.

### Practical Use

Use allowlists, egress controls, redirect and DNS/IP protections.

# Part 149 — Path Traversal in Node

### Core Explanation

User-controlled filenames can escape storage directories.

### Example / Visualization

```text
path.join(base,userInput) without policy
```

### Why It Matters

Can expose files.

### Practical Use

Generate internal names and enforce safe roots.

# Part 150 — Unsafe Regex Awareness

### Core Explanation

Catastrophic backtracking in some regular expressions can block the event loop.

### Example / Visualization

```text
evil input → regex CPU spike
```

### Why It Matters

A single request can cause latency for all users.

### Practical Use

Use safe regex patterns and input limits.

# Part 151 — Denial-of-Service by Blocking

### Core Explanation

Any expensive synchronous CPU or I/O path can block all requests in a process.

### Example / Visualization

```text
sync crypto / huge loop
```

### Why It Matters

Node's concurrency depends on a responsive event loop.

### Practical Use

Benchmark and offload heavy work.

# Part 152 — HTTP Body Limit

### Core Explanation

Bound incoming request size.

### Example / Visualization

```text
1MB JSON limit
```

### Why It Matters

Protects memory and parsing CPU.

### Practical Use

Use separate upload architecture for large files.

# Part 153 — Security Headers

### Core Explanation

Web frameworks/proxies can set browser-oriented security headers.

### Example / Visualization

```text
HSTS/CSP concepts
```

### Why It Matters

Useful for browser-facing services.

### Practical Use

Configure at appropriate layer.

# Part 154 — Configuration Validation

### Core Explanation

Parse and validate all environment/config at startup.

### Example / Visualization

```text
PORT integer / DB URL required
```

### Why It Matters

Prevents delayed failures.

### Practical Use

Freeze config object after startup where practical.

# Part 155 — Secret Handling

### Core Explanation

Secrets should come from secret managers or protected runtime injection.

### Example / Visualization

```text
process env contains reference/secret
```

### Why It Matters

Source and logs are not secret stores.

### Practical Use

Never log full tokens.

# Part 156 — Structured Logging

### Core Explanation

Use a logger that emits consistent JSON fields.

### Example / Visualization

```text
level/service/request_id/error
```

### Why It Matters

Makes logs searchable.

### Practical Use

Include error stack internally but redact sensitive values.

# Part 157 — Request Correlation

### Core Explanation

Propagate request/trace IDs through async work.

### Example / Visualization

```text
request_id across DB/client logs
```

### Why It Matters

Async systems otherwise produce interleaved logs.

### Practical Use

Use request-scoped context carefully.

# Part 158 — Metrics

### Core Explanation

Track request rate, errors, latency, event-loop delay, memory, GC, pool usage, and dependency latency.

### Example / Visualization

```text
RED + runtime metrics
```

### Why It Matters

Node runtime health matters in addition to business metrics.

### Practical Use

Avoid high-cardinality labels.

# Part 159 — Tracing

### Core Explanation

Instrument inbound HTTP, DB, and outbound calls as spans.

### Example / Visualization

```text
HTTP → DB → partner API
```

### Why It Matters

Shows end-to-end latency.

### Practical Use

Use OpenTelemetry-style concepts.

# Part 160 — Startup Sequence

### Core Explanation

Load config, initialize dependencies, then begin listening only when ready.

### Example / Visualization

```text
config → DB/connect → services → listen
```

### Why It Matters

Prevents accepting traffic too early.

### Practical Use

Fail startup on mandatory dependency/config errors.

# Part 161 — Graceful Shutdown

### Core Explanation

On SIGTERM, stop accepting traffic, drain requests, close clients/pools, flush telemetry, then exit.

### Example / Visualization

```text
SIGTERM → server.close → resources.close
```

### Why It Matters

Required for rolling deployments.

### Practical Use

Set a maximum shutdown deadline.

# Part 162 — Uncaught Exception

### Core Explanation

An uncaught exception indicates the process entered an unhandled failure state.

### Example / Visualization

```text
exception reaches process boundary
```

### Why It Matters

Continuing may be unsafe depending on failure.

### Practical Use

Log, fail safely, and rely on supervisor restart after cleanup where appropriate.

# Part 163 — Process Supervisor

### Core Explanation

Production Node processes should be supervised by a platform/process manager.

### Example / Visualization

```text
systemd/container orchestrator
```

### Why It Matters

Supervisors restart crashed processes and manage lifecycle.

### Practical Use

Do not implement your own endless restart loop inside app.

# Part 164 — Health Endpoint

### Core Explanation

Expose a cheap health endpoint.

### Example / Visualization

```text
GET /health
```

### Why It Matters

Supports monitoring.

### Practical Use

Avoid leaking internal details.

# Part 165 — Readiness Endpoint

### Core Explanation

Report whether mandatory startup/runtime dependencies allow serving traffic.

### Example / Visualization

```text
GET /ready
```

### Why It Matters

Orchestrators use it for routing.

### Practical Use

Do not include optional dependencies.

# Part 166 — Unit Testing

### Core Explanation

Test pure/domain/service logic without real network/DB.

### Example / Visualization

```text
node test runner / common JS test framework pattern
```

### Why It Matters

Fast feedback.

### Practical Use

Inject dependencies.

# Part 167 — Integration Testing

### Core Explanation

Use real disposable DB/cache/HTTP servers where needed.

### Example / Visualization

```text
Node app + test DB
```

### Why It Matters

Validates adapters.

### Practical Use

Keep test lifecycle isolated.

# Part 168 — HTTP Testing

### Core Explanation

Start the app on a test port or invoke handler through test harness and assert responses.

### Example / Visualization

```text
request → status/body
```

### Why It Matters

Validates routing and middleware.

### Practical Use

Use synthetic credentials/data.

# Part 169 — Mocking

### Core Explanation

Mock or fake true external boundaries.

### Example / Visualization

```text
fake payment client
```

### Why It Matters

Keeps unit tests deterministic.

### Practical Use

Avoid mocking every internal function.

# Part 170 — Node Test Runner Awareness

### Core Explanation

Node includes built-in testing capabilities in modern releases; ecosystems also use established third-party runners.

### Example / Visualization

```text
test files → assertions
```

### Why It Matters

The concepts remain the same regardless of runner.

### Practical Use

Standardize one approach per repo.

# Part 171 — Assertion

### Core Explanation

Assertions compare actual and expected behavior.

### Example / Visualization

```text
assert.equal(actual, expected)
```

### Why It Matters

Tests require meaningful checks.

### Practical Use

Prefer precise diffs.

# Part 172 — Test Coverage

### Core Explanation

Coverage reveals executed code but does not prove quality.

### Example / Visualization

```text
line/branch/function coverage
```

### Why It Matters

Useful for finding gaps.

### Practical Use

Do not chase 100% blindly.

# Part 173 — Mock Timers Awareness

### Core Explanation

Timer-dependent code should use fake/injected clocks where possible.

### Example / Visualization

```text
advance fake time
```

### Why It Matters

Avoid slow/flaky real waits.

### Practical Use

Design time as a dependency.

# Part 174 — Production Directory Structure

### Core Explanation

A production Node backend should separate application layers and infrastructure clearly.

### Example / Visualization

```text
src/controllers services domain adapters config observability
```

### Why It Matters

Structure communicates ownership.

### Practical Use

Organize by feature/module when scale grows.

# Part 175 — Configuration Module

### Core Explanation

Load and validate environment once.

### Example / Visualization

```text
config/index.js
```

### Why It Matters

Prevents scattered `process.env` access.

### Practical Use

Expose typed/validated config object.

# Part 176 — HTTP Layer

### Core Explanation

Keep route/controller code protocol-focused.

### Example / Visualization

```text
routes/controllers
```

### Why It Matters

Improves testability.

### Practical Use

Move business rules inward.

# Part 177 — Application Service Layer

### Core Explanation

Coordinate use cases and transactions.

### Example / Visualization

```text
services/use-cases
```

### Why It Matters

Keeps controller thin.

### Practical Use

Inject repositories/clients.

# Part 178 — Repository Layer

### Core Explanation

Encapsulate database access.

### Example / Visualization

```text
repositories
```

### Why It Matters

Centralizes persistence behavior.

### Practical Use

Inspect actual SQL.

# Part 179 — External Adapter Layer

### Core Explanation

Wrap payment/email/identity clients.

### Example / Visualization

```text
adapters
```

### Why It Matters

Contains timeouts/retries/auth.

### Practical Use

Expose domain-oriented interfaces.

# Part 180 — Observability Layer

### Core Explanation

Centralize logger, metrics, tracing, and request context.

### Example / Visualization

```text
observability/
```

### Why It Matters

Consistent instrumentation.

### Practical Use

Keep business logic independent of vendor SDK details.

# Part 181 — Production Build Artifact

### Core Explanation

For plain JS, artifact may be source + production dependencies; for TS/bundled apps, it may be compiled output.

### Example / Visualization

```text
Git → CI → artifact/image
```

### Why It Matters

Production should deploy a reproducible artifact.

### Practical Use

Use multi-stage containers where needed.

# Part 182 — Container Image

### Core Explanation

Node backends commonly run in containers with a minimal runtime image.

### Example / Visualization

```text
build → image → registry → deploy
```

### Why It Matters

Standardizes deployment.

### Practical Use

Do not run package manager dev tooling unnecessarily in runtime.

# Part 183 — Non-Root Runtime

### Core Explanation

Run application as non-root when practical.

### Example / Visualization

```text
USER node-like user
```

### Why It Matters

Reduces container privilege.

### Practical Use

Ensure file permissions are correct.

# Part 184 — Signal-Friendly PID1

### Core Explanation

Containerized Node should receive termination signals correctly.

### Example / Visualization

```text
orchestrator SIGTERM → Node
```

### Why It Matters

Needed for graceful shutdown.

### Practical Use

Use exec-form entrypoint and proper init handling where required.

# Part 185 — Horizontal Scaling

### Core Explanation

Run multiple Node replicas behind a load balancer.

### Example / Visualization

```text
LB → replicas
```

### Why It Matters

Improves capacity and availability.

### Practical Use

Externalize state and use shared stores.

# Part 186 — Node Backend Final Mental Model

### Core Explanation

A production Node service is an event-driven runtime process that must keep the event loop responsive, bound concurrency, manage async errors, protect dependencies, expose observability, and shut down gracefully.

### Example / Visualization

```text
HTTP → event loop → async dependencies → response
```

### Why It Matters

Node performance and reliability depend on runtime-aware design.

### Practical Use

Master the event loop and backpressure before framework abstractions.

# Part 187 — ESM Package Mode

### Core Explanation

A Node package can explicitly declare ESM semantics so `.js` files use ECMAScript modules.

### Example / Visualization

```text
package.json: type=module
```

### Why It Matters

Module mode affects import/export and file resolution.

### Practical Use

Choose one primary module system per project.

# Part 188 — CommonJS Module Cache

### Core Explanation

CommonJS modules are generally loaded once per resolved module identity and reused from cache.

### Example / Visualization

```text
require A twice → same loaded module instance
```

### Why It Matters

Module-level state can become process-global state.

### Practical Use

Avoid hidden mutable singletons.

# Part 189 — ESM Module Cache

### Core Explanation

Imported ESM modules are also evaluated according to module-loader semantics and reused for the process/module graph.

### Example / Visualization

```text
import config from module
```

### Why It Matters

Module initialization can have side effects.

### Practical Use

Keep imports predictable and initialization explicit.

# Part 190 — Dynamic Import

### Core Explanation

`import()` loads a module asynchronously at runtime.

### Example / Visualization

```text
await import('./plugin.js')
```

### Why It Matters

Useful for optional or lazy-loaded features.

### Practical Use

Avoid making core dependencies appear only through hidden dynamic paths.

# Part 191 — Top-Level Await Awareness

### Core Explanation

ES modules can perform awaited work during module evaluation.

### Example / Visualization

```text
await loadConfig() at module level
```

### Why It Matters

It can simplify initialization but also delay/couple module loading.

### Practical Use

Prefer explicit bootstrap for complex startup.

# Part 192 — Package Exports Awareness

### Core Explanation

A package can expose only selected public entry points through its package metadata.

### Example / Visualization

```text
package exports map
```

### Why It Matters

Protects internal files from becoming accidental public API.

### Practical Use

Treat exported paths as compatibility contracts.

# Part 193 — Package Imports Awareness

### Core Explanation

Packages can define internal import aliases in supported module configurations.

### Example / Visualization

```text
#config → internal module
```

### Why It Matters

Reduces long relative paths.

### Practical Use

Keep aliases understandable and tooling-compatible.

# Part 194 — Workspace Awareness

### Core Explanation

Package-manager workspaces can manage several Node packages in one repository.

### Example / Visualization

```text
repo/packages/api, shared, worker
```

### Why It Matters

Useful for monorepos and shared libraries.

### Practical Use

Define package boundaries and dependency direction.

# Part 195 — Monorepo Node Architecture

### Core Explanation

A Node monorepo can host multiple deployables and shared packages with one coordinated dependency graph.

### Example / Visualization

```text
apps/api + apps/worker + packages/domain
```

### Why It Matters

Improves cross-project refactoring but can create oversized CI.

### Practical Use

Use affected-project builds/tests.

# Part 196 — npm Lifecycle Script Security

### Core Explanation

Install/build lifecycle scripts execute code from packages and therefore belong to the software supply-chain trust boundary.

### Example / Visualization

```text
dependency install → lifecycle script executes
```

### Why It Matters

Installing a package can execute code.

### Practical Use

Review dependencies and use controlled CI/build environments.

# Part 197 — Dependency Confusion Awareness

### Core Explanation

Misconfigured private/public package scopes can cause an unintended public package to be resolved.

### Example / Visualization

```text
internal package name resolved externally
```

### Why It Matters

Supply-chain compromise can occur before application code runs.

### Practical Use

Use scoped packages and controlled registries.

# Part 198 — Lockfile Integrity

### Core Explanation

A lock file captures exact package graph and integrity metadata where supported.

### Example / Visualization

```text
manifest + lockfile → deterministic install
```

### Why It Matters

It limits unplanned dependency drift.

### Practical Use

Review lockfile changes in pull requests.

# Part 199 — Runtime vs Build Dependency

### Core Explanation

Transpilers, linters, and test tools need not exist in the production image.

### Example / Visualization

```text
build stage → runtime stage
```

### Why It Matters

Smaller runtime images reduce attack surface.

### Practical Use

Use multi-stage builds.

# Part 200 — URLSearchParams

### Core Explanation

`URLSearchParams` represents query parameters using a standard API.

### Example / Visualization

```text
new URL(req.url,...).searchParams
```

### Why It Matters

Safer than manual query splitting.

### Practical Use

Validate duplicated and multi-valued parameters.

# Part 201 — HTTP Header Multiplicity

### Core Explanation

Some HTTP headers may appear multiple times or have special joining semantics.

### Example / Visualization

```text
Set-Cookie multiple values
```

### Why It Matters

Incorrect handling can change security/protocol behavior.

### Practical Use

Use Node/framework header APIs rather than ad-hoc concatenation.

# Part 202 — HTTP Request Abort

### Core Explanation

Clients can disconnect before the server finishes work.

### Example / Visualization

```text
client closes socket → request aborted
```

### Why It Matters

Continuing expensive downstream work wastes capacity.

### Practical Use

Propagate cancellation where practical.

# Part 203 — Response Already Sent

### Core Explanation

Writing headers/body twice causes protocol/runtime errors.

### Example / Visualization

```text
res.end(); later res.write() ✗
```

### Why It Matters

Async code can accidentally respond from multiple branches.

### Practical Use

Return immediately after terminal responses.

# Part 204 — Slow Client

### Core Explanation

A client can read response data slowly, causing buffered output.

### Example / Visualization

```text
server produces > client consumes
```

### Why It Matters

Backpressure matters even for HTTP responses.

### Practical Use

Stream and respect writable signals.

# Part 205 — Slowloris Awareness

### Core Explanation

A malicious or broken client can hold connections open while sending data very slowly.

### Example / Visualization

```text
many incomplete HTTP requests
```

### Why It Matters

Consumes connection resources.

### Practical Use

Use server/proxy header/body/idle timeouts.

# Part 206 — HTTP Server Timeouts

### Core Explanation

Backend HTTP servers need appropriate request, header, keep-alive, and idle timeout policies.

### Example / Visualization

```text
connection lifecycle bounded
```

### Why It Matters

Timeouts are part of capacity/security engineering.

### Practical Use

Coordinate with reverse proxy/load balancer.

# Part 207 — HTTP/2 Awareness

### Core Explanation

HTTP/2 multiplexes multiple streams over a connection and changes some transport behavior.

### Example / Visualization

```text
one connection → multiple request streams
```

### Why It Matters

Useful behind gateways and service infrastructures.

### Practical Use

Application semantics still use request/response contracts.

# Part 208 — Compression Stream

### Core Explanation

Compression can be performed as a transform stream.

### Example / Visualization

```text
Readable → gzip → Response
```

### Why It Matters

Streaming avoids buffering the entire payload.

### Practical Use

Usually let edge proxies handle common response compression unless application-specific.

# Part 209 — Crypto Module Awareness

### Core Explanation

Node exposes cryptographic primitives, hashes, random bytes, and TLS-related functionality.

### Example / Visualization

```text
randomBytes / createHash concepts
```

### Why It Matters

Security-sensitive code should use mature primitives.

### Practical Use

Do not invent custom encryption protocols.

# Part 210 — Cryptographically Secure Randomness

### Core Explanation

Security tokens must use cryptographically secure randomness, not `Math.random`.

### Example / Visualization

```text
randomBytes → token
```

### Why It Matters

Predictable tokens can lead to account/session compromise.

### Practical Use

Use established token/session libraries where possible.

# Part 211 — Hash vs Password Hash

### Core Explanation

A fast general hash is not a password-hashing algorithm.

### Example / Visualization

```text
SHA-like hash ≠ adaptive password hash
```

### Why It Matters

Passwords need intentionally expensive adaptive hashing.

### Practical Use

Use dedicated password libraries.

# Part 212 — Random UUID Awareness

### Core Explanation

Node can generate UUID-style identifiers through cryptographic facilities.

### Example / Visualization

```text
random UUID → request/resource ID
```

### Why It Matters

Useful for opaque identifiers.

### Practical Use

Do not treat IDs as authorization.

# Part 213 — zlib Awareness

### Core Explanation

Node supports compression/decompression APIs using streaming and buffer forms.

### Example / Visualization

```text
gzip stream
```

### Why It Matters

Compression can be CPU-intensive.

### Practical Use

Avoid compressing already-compressed files.

# Part 214 — AsyncLocalStorage Awareness

### Core Explanation

Async-local context can carry request-scoped metadata across many asynchronous operations.

### Example / Visualization

```text
request_id available inside downstream callbacks
```

### Why It Matters

Useful for logging/tracing context.

### Practical Use

Do not use it as hidden business-state storage.

# Part 215 — Async Context

### Core Explanation

Asynchronous operations need a way to preserve request/trace identity despite interleaving.

### Example / Visualization

```text
request A/B callbacks interleave
```

### Why It Matters

Without context, logs become hard to correlate.

### Practical Use

Prefer explicit propagation or async-local context.

# Part 216 — performance Hooks Awareness

### Core Explanation

Runtime performance APIs can measure durations and event-loop behavior.

### Example / Visualization

```text
mark → measure
```

### Why It Matters

Useful for diagnosing internal latency.

### Practical Use

Profile representative workloads.

# Part 217 — Event Loop Utilization Awareness

### Core Explanation

Runtime metrics can estimate how busy the event loop is.

### Example / Visualization

```text
ELU high
```

### Why It Matters

Helps distinguish CPU/event-loop saturation from external wait.

### Practical Use

Interpret with CPU and request metrics.

# Part 218 — Heap Limit Awareness

### Core Explanation

The JavaScript heap is bounded; very large retained data can terminate the process.

### Example / Visualization

```text
heap approaches limit → GC pressure/OOM
```

### Why It Matters

Backend capacity includes memory limits.

### Practical Use

Stream/batch large work.

# Part 219 — RSS vs Heap

### Core Explanation

Resident Set Size includes more than JavaScript heap: native buffers, code, libraries, and other memory.

### Example / Visualization

```text
RSS > heapUsed
```

### Why It Matters

Looking only at heap can miss memory growth.

### Practical Use

Monitor both process and JS memory.

# Part 220 — Buffer Memory Pressure

### Core Explanation

Buffers may allocate significant memory outside the ordinary JS object heap accounting.

### Example / Visualization

```text
large Buffers → RSS growth
```

### Why It Matters

Streaming/binary workloads can exhaust memory even when heap looks moderate.

### Practical Use

Bound buffering.

# Part 221 — Worker Message Passing

### Core Explanation

Worker threads exchange messages or shared/transferable data.

### Example / Visualization

```text
main ⇄ worker messages
```

### Why It Matters

Serialization/copying can become a cost.

### Practical Use

Send compact data and benchmark.

# Part 222 — Transferable Data Awareness

### Core Explanation

Some binary memory can be transferred rather than copied between workers.

### Example / Visualization

```text
ArrayBuffer transfer
```

### Why It Matters

Reduces copying for large payloads.

### Practical Use

Ownership changes after transfer.

# Part 223 — Shared Memory Awareness

### Core Explanation

Workers can coordinate through shared memory primitives.

### Example / Visualization

```text
SharedArrayBuffer concept
```

### Why It Matters

Provides high performance but adds concurrency complexity.

### Practical Use

Prefer message passing unless shared memory is justified.

# Part 224 — Child Process IPC

### Core Explanation

Forked Node child processes can exchange messages through IPC.

### Example / Visualization

```text
parent ⇄ child
```

### Why It Matters

Useful for process isolation.

### Practical Use

Handle child crash/disconnect explicitly.

# Part 225 — Process Crash Isolation

### Core Explanation

A crash in one process does not necessarily terminate sibling replicas.

### Example / Visualization

```text
LB → process A/B/C
```

### Why It Matters

Process replication improves fault isolation.

### Practical Use

Do not rely on in-memory state across replicas.

# Part 226 — Hot Reloading vs Production

### Core Explanation

Development reloaders are productivity tools, not production supervisors.

### Example / Visualization

```text
file change → restart dev server
```

### Why It Matters

Production needs stable controlled lifecycle.

### Practical Use

Use orchestrator/process supervisor.

# Part 227 — Source Maps Awareness

### Core Explanation

Transpiled/bundled applications can use source maps to map stack traces back to source.

### Example / Visualization

```text
compiled stack → source line
```

### Why It Matters

Improves debugging.

### Practical Use

Protect source-map exposure in public deployments.

# Part 228 — TypeScript with Node Awareness

### Core Explanation

TypeScript adds static type checking and typically compiles/transforms to JavaScript executed by Node.

### Example / Visualization

```text
TS → type check/build → JS → Node
```

### Why It Matters

Types improve development feedback but do not replace runtime input validation.

### Practical Use

Validate network/database inputs at runtime.

# Part 229 — Runtime Schema Validation

### Core Explanation

Even TypeScript services need runtime validation for HTTP, environment, DB, and message inputs.

### Example / Visualization

```text
unknown JSON → validated DTO
```

### Why It Matters

Static types disappear at runtime.

### Practical Use

Use schema validation at external boundaries.

# Part 230 — OpenTelemetry Context Awareness

### Core Explanation

Tracing libraries need to propagate context through async operations.

### Example / Visualization

```text
trace/span context across awaits
```

### Why It Matters

Node's async model makes context propagation important.

### Practical Use

Use mature instrumentation rather than home-grown globals.

# Part 231 — Diagnostic Report Awareness

### Core Explanation

Node can produce diagnostic information about process/runtime state for severe failures.

### Example / Visualization

```text
runtime report concept
```

### Why It Matters

Useful during crashes, memory, or native failures.

### Practical Use

Store reports securely because they may contain sensitive metadata.

# Part 232 — Core Dump Awareness

### Core Explanation

Native/process crashes can sometimes be analyzed through OS-level crash artifacts.

### Example / Visualization

```text
process crash → dump
```

### Why It Matters

Deep production diagnostics may go below JavaScript.

### Practical Use

Use only under controlled security/operations procedures.

# Part 233 — Benchmarking Node

### Core Explanation

Benchmark throughput and tail latency using representative payloads and dependencies.

### Example / Visualization

```text
load → p95/p99 + CPU + ELU
```

### Why It Matters

Microbenchmarks can mislead.

### Practical Use

Benchmark the complete request path.

# Part 234 — Warm-Up Effects

### Core Explanation

JIT compilation, caches, and connection establishment can make early requests behave differently from steady state.

### Example / Visualization

```text
cold start → warm steady state
```

### Why It Matters

Load tests should include warm-up period.

### Practical Use

Measure cold and warm behavior separately when relevant.

# Part 235 — Dependency Timeout Composition

### Core Explanation

A request with several downstream calls needs a total deadline split among dependencies.

### Example / Visualization

```text
5s request budget → 1s DB + 2s partner + margin
```

### Why It Matters

Independent generous timeouts can exceed caller deadline.

### Practical Use

Budget end-to-end latency.

# Part 236 — Node.js Architecture Decision

### Core Explanation

Choose Node when its runtime model fits the workload and team, not because JavaScript is familiar.

### Example / Visualization

```text
I/O-heavy API ✓
large CPU scientific job may need worker/service
```

### Why It Matters

Technology choice affects performance and operations.

### Practical Use

Prototype critical workload characteristics before committing.

## 5. Hands-on Lab / Practical Exercises

### Lab 1 — Hello Node Runtime

Create a small script that prints process version, PID, cwd, and selected environment variables.

### Lab 2 — CommonJS Module

Create two modules using `require`/`module.exports`.

### Lab 3 — ES Module

Create two modules using `import`/`export`.

### Lab 4 — package.json

Create scripts for start, test, lint, and dev.

### Lab 5 — Lock File

Install one small dependency and inspect the resolved lock graph.

### Lab 6 — Async File Read

Compare async file read with sync file read and explain event-loop impact.

### Lab 7 — Callback to Promise

Convert an error-first callback flow into a Promise-based flow.

### Lab 8 — async/await

Rewrite a promise chain using async/await and try/catch.

### Lab 9 — Promise.all

Run two independent asynchronous operations concurrently.

### Lab 10 — Concurrency Limit

Process 100 simulated jobs with a maximum of five in flight.

### Lab 11 — Timers

Use setTimeout, clearTimeout, and one periodic timer with safe shutdown.

### Lab 12 — AbortController

Design cancellation for a slow outbound operation.

### Lab 13 — EventEmitter

Create an emitter with `on`, `once`, and error handling.

### Lab 14 — Listener Leak

Demonstrate accidental repeated listener registration and then fix lifecycle ownership.

### Lab 15 — Buffer

Convert UTF-8 text to Buffer, inspect bytes, and encode/decode base64.

### Lab 16 — Readable Stream

Read a large file as a stream rather than all at once.

### Lab 17 — Transform Stream

Create a transform that uppercases text chunks.

### Lab 18 — Backpressure

Write to a slow writable stream and handle the `drain` condition.

### Lab 19 — Filesystem

Create/read/update/delete files inside a temporary lab directory.

### Lab 20 — Path Safety

Design safe internal filenames and reject traversal-like user input.

### Lab 21 — URL Parsing

Parse path and query parameters using the URL class.

### Lab 22 — Core HTTP Server

Build an HTTP server with `/health` and `/echo`.

### Lab 23 — JSON Body Parser

Implement a bounded JSON-body collector for small requests.

### Lab 24 — Routing

Add GET `/users/:id`-like manual route logic.

### Lab 25 — Error Handling

Return safe 400/404/500 responses and log internal errors.

### Lab 26 — Request ID

Generate/propagate request IDs through logs and responses.

### Lab 27 — HTTP Client

Call a local dependency with timeout/cancellation.

### Lab 28 — TCP Server

Create a tiny authorized local TCP echo server.

### Lab 29 — Child Process

Use `spawn` with a trusted executable and argument list.

### Lab 30 — Worker Thread

Move a CPU-heavy calculation into a worker thread.

### Lab 31 — Event-Loop Blocking

Run a CPU-heavy loop and observe impact on a timer/HTTP response.

### Lab 32 — Memory Growth

Create then fix an intentionally unbounded in-memory cache.

### Lab 33 — Structured Logging

Create JSON log records with service, level, request_id, operation, and duration.

### Lab 34 — Metrics Design

Define request, event-loop, memory, GC, and dependency metrics.

### Lab 35 — Graceful Shutdown

Handle SIGTERM by closing the HTTP server and resources.

### Lab 36 — Readiness

Add `/ready` that changes only after mandatory initialization.

### Lab 37 — Unit Test

Write unit tests for one service function.

### Lab 38 — Async Test

Test an async success and rejection path.

### Lab 39 — Fake Dependency

Inject a fake repository into a service.

### Lab 40 — HTTP Integration Test

Start the service on a test port and verify status/body.

### Lab 41 — Security Review

Threat-model body size, SSRF, path traversal, dependency risk, and child-process use.

### Lab 42 — Configuration Validation

Fail startup when PORT/DB URL/timeouts are invalid.

### Lab 43 — Container Design

Write a conceptual production Dockerfile with non-root runtime.

### Lab 44 — Horizontal Scaling

Draw 3 Node replicas behind a load balancer with shared DB/cache.

### Lab 45 — Node Production Capstone Review

Review the mini project for event-loop safety, backpressure, errors, security, observability, testing, and shutdown.

### Lab 46 — AsyncLocalStorage Context

Design request-scoped logging context that preserves request ID across nested async calls.

### Lab 47 — HTTP Timeout Policy

Define header, request, keep-alive, outbound, and graceful-shutdown timeout hierarchy.

### Lab 48 — Worker Message Passing

Send a CPU task to a worker and return result without blocking the main HTTP event loop.

### Lab 49 — Runtime Memory Diagnostics

Design a dashboard for heapUsed, RSS, Buffers, GC, event-loop delay, and request latency.

### Lab 50 — Dependency Supply-Chain Review

Inspect a hypothetical package update: manifest, lockfile change, lifecycle scripts, transitive dependencies, and registry source.

## 6. Mini Project

# Mini Project — Production Node.js Order API

Build/design a Node.js backend service that implements:

```text
GET /health
GET /ready
POST /users
POST /sessions
POST /orders
GET /orders/:id
GET /orders
POST /reports
```

## Architecture

```text
Client
  ↓
Reverse Proxy / LB
  ↓
Node.js HTTP Service
  ├─ Router
  ├─ Middleware
  ├─ Controllers
  ├─ Services
  ├─ Domain
  ├─ Repositories
  ├─ External Clients
  └─ Observability
       ↓
Database
Cache
Object Storage
Job Queue
External API
```

## Runtime Requirements

```text
ES modules or clearly selected module mode
async/await
bounded concurrency
no synchronous I/O in request path
request size limits
stream large responses/files
timeouts
cancellation where supported
graceful shutdown
```

## Security Requirements

```text
validated configuration
no secrets in source
parameterized DB access
object-level authorization
safe path handling
SSRF controls
no shell construction from user input
dependency scanning
non-root container runtime
```

## Observability

```text
structured logs
request IDs
request metrics
event-loop delay
memory metrics
dependency latency
traces
```

## Testing

```text
unit
async
integration
HTTP
authorization
shutdown
```

## Required Documentation

```text
NODE_RUNTIME.md
EVENT_LOOP.md
ASYNC_DESIGN.md
STREAMING.md
SECURITY.md
OBSERVABILITY.md
TESTING.md
DEPLOYMENT.md
RUNBOOKS.md
```

## 7. Recommended Resources

This file is designed to be self-contained.

For implementation details, consult current official Node.js documentation for:

```text
modules
events
timers
streams
buffers
filesystem
HTTP
net
process
worker_threads
child_process
test runner
diagnostics / performance
```

Also use official package-manager documentation for the manager selected by your repository.

## 8. Certification Relevance

Relevant to:

```text
Backend Developer
Node.js Developer
Cloud Application Developer
DevOps Engineer
Platform Engineer
SRE
Full-Stack Developer
```

It directly prepares for Courses 72–76 and for practical Node.js backend work in containerized/cloud environments.

## 9. Common Mistakes & Best Practices

- **Mistake:** Calling Node.js a programming language.  
  **Best practice:** JavaScript is the language; Node.js is the runtime.
- **Mistake:** Assuming async code cannot block.  
  **Best practice:** CPU-heavy JS and synchronous APIs can block the event loop.
- **Mistake:** Using synchronous filesystem APIs in request paths.  
  **Best practice:** Use async APIs or streams.
- **Mistake:** Launching unlimited promises.  
  **Best practice:** Bound concurrency.
- **Mistake:** Ignoring promise rejections.  
  **Best practice:** Handle or propagate every promise.
- **Mistake:** Buffering huge files in memory.  
  **Best practice:** Use streams and backpressure.
- **Mistake:** Using shell commands with untrusted strings.  
  **Best practice:** Use direct executable + argument arrays or libraries.
- **Mistake:** Using global unbounded Maps as caches.  
  **Best practice:** Bound by size/TTL or use external cache.
- **Mistake:** Reading process.env throughout the code.  
  **Best practice:** Load and validate config once.
- **Mistake:** No outbound timeouts.  
  **Best practice:** Every dependency call needs a time budget.
- **Mistake:** Treating health and readiness as the same thing.  
  **Best practice:** Separate process health from ability to receive traffic.
- **Mistake:** Keeping sessions only in one process.  
  **Best practice:** Externalize shared state for horizontal scaling.
- **Mistake:** No graceful shutdown.  
  **Best practice:** Handle SIGTERM and drain resources.
- **Mistake:** Overusing worker threads for normal I/O.  
  **Best practice:** Use workers for CPU-bound work, not routine async I/O.
- **Mistake:** Ignoring dependency supply-chain risk.  
  **Best practice:** Lock, scan, minimize, and govern dependencies.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is Node.js?

**Answer:** A server-side JavaScript runtime with event-driven, non-blocking I/O APIs.

### Q2. What is V8?

**Answer:** The JavaScript engine executing JS code.

### Q3. What is libuv?

**Answer:** Runtime library providing event-loop and cross-platform async I/O abstractions.

### Q4. Is Node.js single-threaded?

**Answer:** Main JS execution is typically one event-loop thread per process, while runtime I/O/thread-pool/workers can use other threads.

### Q5. Why is blocking bad?

**Answer:** One long JS operation delays other callbacks/requests in the same process.

### Q6. I/O-bound workload?

**Answer:** Workload spending much time waiting for network/files/database.

### Q7. CPU-bound workload?

**Answer:** Workload dominated by computation.

### Q8. CommonJS syntax?

**Answer:** `require` and `module.exports`.

### Q9. ESM syntax?

**Answer:** `import` and `export`.

### Q10. Why commit a lock file?

**Answer:** Reproducible dependency resolution.

### Q11. Promise states?

**Answer:** Pending, fulfilled, rejected.

### Q12. What does async function return?

**Answer:** A Promise.

### Q13. Why Promise.all?

**Answer:** Run independent async work concurrently and await all.

### Q14. Why bound Promise concurrency?

**Answer:** Avoid overwhelming memory, DBs, or APIs.

### Q15. Microtask?

**Answer:** High-priority scheduled work such as promise reactions.

### Q16. Why avoid process.nextTick overuse?

**Answer:** It can starve I/O/event-loop progress.

### Q17. Buffer?

**Answer:** Binary byte container.

### Q18. Stream?

**Answer:** Incremental data-processing abstraction.

### Q19. Backpressure?

**Answer:** Mechanism for slowing producer when consumer cannot keep up.

### Q20. Readable stream?

**Answer:** Produces chunks.

### Q21. Writable stream?

**Answer:** Consumes chunks.

### Q22. Transform stream?

**Answer:** Consumes and produces transformed chunks.

### Q23. Why use pipeline abstraction?

**Answer:** Better error/cleanup propagation across streams.

### Q24. EventEmitter?

**Answer:** In-process event publication/subscription abstraction.

### Q25. Listener leak?

**Answer:** Listeners accumulate without removal and retain memory/duplicate work.

### Q26. Why use URL class?

**Answer:** Reliable URL/query parsing rather than string splitting.

### Q27. IncomingMessage?

**Answer:** Node core HTTP request object and readable body stream.

### Q28. ServerResponse?

**Answer:** Node core HTTP response object.

### Q29. Why body-size limits?

**Answer:** Protect memory and parsing CPU.

### Q30. Worker thread?

**Answer:** Parallel JS execution thread for CPU-heavy work.

### Q31. Child process?

**Answer:** Separate OS process launched by Node.

### Q32. Why avoid shell=true with user input?

**Answer:** Shell injection risk.

### Q33. Thread-pool saturation?

**Answer:** Background runtime tasks queue because worker pool is fully busy.

### Q34. Event-loop delay?

**Answer:** Ready work waits because the JS thread is busy.

### Q35. Common memory leak causes?

**Answer:** Unbounded caches, listeners, globals, closures, retained requests.

### Q36. Why structured logs?

**Answer:** Consistent machine-readable diagnosis.

### Q37. Why request IDs?

**Answer:** Correlate logs across async work and dependencies.

### Q38. Why graceful shutdown?

**Answer:** Avoid dropped requests/resources during deploy or scale-down.

### Q39. Readiness?

**Answer:** Whether instance can currently serve traffic.

### Q40. Liveness?

**Answer:** Whether process is alive/not stuck.

### Q41. Why externalize sessions?

**Answer:** Any replica can serve subsequent requests.

### Q42. Why OOM can happen despite GC?

**Answer:** Reachable objects remain and heap/process memory is finite.

### Q43. Why large JSON is dangerous?

**Answer:** Parsing is CPU/memory intensive and blocks event loop.

### Q44. Why dependency scanning?

**Answer:** Transitive packages can contain known vulnerabilities.

### Q45. Prototype pollution?

**Answer:** Unsafe manipulation of object prototype through untrusted keys.

### Q46. SSRF?

**Answer:** Backend is induced to request unintended network destinations.

### Q47. Why no sync I/O in hot path?

**Answer:** It blocks all other JS work in the process.

### Q48. What should production supervisor do?

**Answer:** Manage process/container lifecycle and restart failed instances.

### Q49. Best workload for Node?

**Answer:** Often I/O-heavy network applications with well-controlled CPU work.

### Q50. Final Node mental model?

**Answer:** Event-driven JS runtime: keep event loop responsive, bound concurrency, stream large data, manage lifecycle and dependencies explicitly.

## Completion Checklist

- [ ] I understand Node runtime architecture.
- [ ] I understand event loop and non-blocking I/O.
- [ ] I understand callbacks, promises, async/await, and microtasks.
- [ ] I can use modules and package metadata correctly.
- [ ] I understand Buffers and Streams.
- [ ] I can build a core HTTP server.
- [ ] I understand EventEmitter and socket concepts.
- [ ] I can use worker threads for CPU work.
- [ ] I can design safe child-process use.
- [ ] I understand memory and event-loop performance.
- [ ] I understand Node security risks.
- [ ] I can design structured logging and metrics.
- [ ] I can implement graceful shutdown.
- [ ] I can test Node services.
- [ ] I completed all labs.
- [ ] I completed the Node.js capstone.
