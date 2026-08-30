# Phase 24 — Malware & Reverse Engineering

Phase 24 introduces **defensive binary and malware analysis**. It is intentionally ordered so that operational malware analysis comes before deeper reverse engineering.

```text
98 Malware Analysis
        ↓
99 Reverse Engineering
```

Malware analysis asks:

> **What does this sample do, what is the impact, and how do defenders detect and remove it?**

Reverse engineering asks:

> **How is that behavior implemented at the binary/code level?**

---

# Phase Goal

```text
Preserve Sample
      ↓
Static Triage
      ↓
Behavior Hypothesis
      ↓
Controlled Dynamic Analysis
      ↓
Reverse Engineering as Needed
      ↓
Behavior + IOCs
      ↓
Detection Engineering
      ↓
Containment / Eradication / Recovery
```

---

# Mandatory Safety Rules

Unknown samples must never be executed on:

```text
normal workstation
personal laptop
production server
corporate user endpoint
unrestricted Internet-connected VM
```

Use:

```text
disposable analysis VM
snapshots
controlled / simulated networking
synthetic credentials and documents
disabled shared folders/clipboard where practical
separate evidence storage
```

For reverse engineering, use:

```text
training / CTF binaries
binaries you compiled
open-source software
binaries you are explicitly authorized to analyze
```

Do not use reverse engineering to bypass licensing/DRM or modify third-party software outside authorization.

---

# Course 98 — Malware Analysis

## Core Workflow

```text
SHA-256 / Sample Identity
       ↓
File Type
       ↓
Metadata
       ↓
Strings
       ↓
Sections / Imports / Resources
       ↓
Static Hypothesis
       ↓
Controlled Execution
       ↓
Process / File / Registry / Network Timeline
       ↓
Persistence / Collection / Impact
       ↓
IOCs + Behavioral Detections
```

## Static Analysis Questions

```text
What file format is it?
Which architecture?
Signed?
Packed?
Which sections are unusual?
Which APIs/libraries are imported?
Which strings/configuration clues exist?
Which embedded resources exist?
```

Remember:

```text
Capability != Confirmed Behavior
```

A networking import does not prove that the sample connects to the Internet. Dynamic evidence or code-path confirmation is required.

## Dynamic Analysis Questions

Observe:

```text
process tree
command line
created / modified files
registry changes
services
tasks / autostarts
DNS
HTTP / TLS destinations
named pipes / mutexes
system discovery
data access
security-tool interaction
```

Do not allow the sample to contact real command-and-control infrastructure.

---

# Indicators and Detection

## IOC Model

```text
Indicator
  ↓
Confidence
  ↓
Context
  ↓
Lifetime
  ↓
Detection / Block / Hunt Use
```

Possible indicators:

```text
hashes
domains
IP addresses
filenames
paths
registry keys
mutexes
certificates
user agents
service names
scheduled tasks
```

Prefer behavior-based detections when possible because infrastructure and hashes can change rapidly.

## YARA Role

YARA should identify stable characteristics of a sample/family, not simply one common word.

```text
stable byte/string pattern
  +
structural context
  +
low false-positive rate
  ↓
useful triage rule
```

---

# Course 99 — Reverse Engineering

Reverse engineering should be hypothesis-driven.

```text
Binary
  ↓
File Format / Architecture
  ↓
Strings / Imports / Symbols
  ↓
Functions / Xrefs
  ↓
Assembly / Decompiler
  ↓
Control Flow
  ↓
Data Flow
  ↓
Debugger Validation
  ↓
Documented Behavior
```

## Assembly Mental Model

Do not memorize instructions as isolated vocabulary.

Read each instruction as:

```text
old register / memory state
       ↓ instruction
new register / memory / flag state
```

Then group instructions into:

```text
conditions
loops
function calls
string handling
buffer handling
structure access
protocol parsing
state transitions
```

## Important x86/x64 Concepts

```text
registers
instruction pointer
stack pointer
flags
mov / lea
push / pop
call / ret
cmp / test
conditional jumps
memory addressing
stack frames
calling conventions
return values
```

---

# Ghidra Workflow

```text
Import Binary
    ↓
Auto Analysis
    ↓
Check Format / Architecture
    ↓
Strings / Imports
    ↓
Cross References
    ↓
Functions
    ↓
Decompiler
    ↓
Rename / Retype / Annotate
    ↓
Function Graph / Call Graph
    ↓
Debugger Validation
```

Decompiler output is **not source code**. It is a reconstruction hypothesis.

Always validate important behavior with:

```text
assembly
xrefs
data flow
runtime evidence
```

---

# Static + Dynamic Analysis Relationship

```text
Static clue
   ↓
Hypothesis
   ↓
Breakpoint / runtime observation
   ↓
Confirmed or rejected
   ↓
Update annotations
```

This feedback loop is the central reverse-engineering skill.

---

# Recommended Lab Structure

```text
Phase_24_Lab/
├── samples/
│   ├── originals/
│   └── hashes.csv
├── static/
│   ├── metadata/
│   ├── strings/
│   ├── pe_elf/
│   └── yara/
├── dynamic/
│   ├── process/
│   ├── filesystem/
│   ├── registry/
│   └── network/
├── reverse/
│   ├── ghidra/
│   ├── debugger/
│   ├── call_graphs/
│   └── notes/
├── detections/
└── reports/
```

---

# Recommended Tools

## Analysis Environment

```text
REMnux
FLARE-VM
isolated Windows/Linux VMs
snapshots
```

## Static

```text
file
sha256sum
strings
PE / ELF inspection tools
Ghidra
YARA
hex viewer
```

## Dynamic

```text
process monitoring
filesystem/registry monitoring
Wireshark / tcpdump
controlled DNS/HTTP simulation
debugger appropriate to platform
```

Use tools because they answer a question, not because they are installed.

---

# Combined Phase 24 Capstone

Use a benign training sample or explicitly authorized sample containing several observable behaviors.

Deliver:

1. Sample source/provenance
2. SHA-256
3. File type / architecture
4. Static metadata
5. Strings analysis
6. Imports / sections / resources
7. Static behavior hypotheses
8. Dynamic execution timeline
9. Process tree
10. File / registry / persistence artifacts
11. Network behavior
12. IOC table with confidence
13. YARA training rule
14. Detection ideas
15. Ghidra function map
16. Key functions renamed/annotated
17. Control-flow or state diagram
18. Debugger validation
19. Containment recommendations
20. Eradication recommendations
21. Recovery recommendations
22. Limitations and confidence

---

# Knowledge Check

Before leaving Phase 24, explain:

```text
SHA-256
static analysis
dynamic analysis
PE / ELF
entry point
sections
imports
strings
entropy
packing
obfuscation
persistence
C2 / beaconing
IOC
behavioral detection
YARA
assembly
register
stack
calling convention
basic block
CFG
xrefs
decompiler
debugger
breakpoint
data flow
```

---

# Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 98 — Malware Analysis | 120 | 70 | 120 | 7,415 |
| 99 — Reverse Engineering | 134 | 70 | 134 | 8,000 |
| **Total** | **254** | **140** | **254** | **15,415** |

---

# Completion Criteria

Phase 24 is complete when you can:

- handle suspicious files safely;
- calculate and track exact sample hashes;
- identify common executable/script formats;
- perform static triage;
- observe controlled runtime behavior;
- distinguish capability from behavior;
- identify persistence and network behaviors;
- create useful IOCs and YARA/detection ideas;
- read fundamental x86/x64 assembly;
- navigate functions/xrefs in Ghidra;
- validate important hypotheses using a debugger;
- document confidence and limitations;
- explain when reverse engineering adds value beyond malware triage.

---

# Next Phase

**Phase 25 — SOC & Defensive Security**

```text
100 Security Operations Center Fundamentals
101 Security Monitoring Fundamentals
102 Cyber Threat Intelligence
103 Cyber Threat Hunting
```

Phase 24 provides technical depth for Phase 25 because SOC and threat-hunting teams often need to understand **what suspicious code actually did**, not merely that an alert fired.
