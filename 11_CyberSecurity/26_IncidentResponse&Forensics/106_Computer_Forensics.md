# 106. Computer Forensics

> Phase 26 — Incident Response & Forensics

## 1. Topic Title

**Computer Forensics**

## 2. Learning Objectives

- Explain evidence integrity, chain of custody, acquisition, and working copies.
- Understand disk, filesystem, memory, registry, browser, logs, persistence, and user artifacts.
- Build forensic timelines from multiple sources.
- Use hashes and acquisition concepts correctly.
- Separate fact, interpretation, confidence, and limitations in forensic reports.

## 3. Prerequisites

```text
Phase 25 SOC & Defensive Security
Cybersecurity Fundamentals
Linux / Windows administration
Networking
Cloud fundamentals
Active Directory / identity basics
```

For formal forensic work, use only authorized evidence and follow organizational/legal evidence procedures.

## 4. Core Concepts Explanation

# Part 1 — Computer Forensics Purpose

### Core Explanation

Computer forensics preserves, acquires, examines, analyzes, and reports digital evidence while maintaining integrity and context.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 2 — Forensic Readiness

### Core Explanation

Prepare logging, time, ownership, retention, tools, access, and procedures before incidents.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 3 — Evidence Integrity

### Core Explanation

Forensic conclusions depend on preserving evidence and documenting transformations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 4 — Chain of Custody

### Core Explanation

Chain of custody records collection, possession, transfer, storage, access, and integrity.

### Diagram / Command / Evidence Example

```text
Evidence ID → collected by/time → hash/integrity → storage → transfers/access → analysis copy
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 5 — Evidence ID

### Core Explanation

Every evidence item should have a unique identifier tied to notes and storage.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 6 — Acquisition

### Core Explanation

Acquisition creates a reliable copy of source evidence for analysis.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 7 — Original Evidence

### Core Explanation

Original media should be preserved and accessed as little as possible after acquisition.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 8 — Working Copy

### Core Explanation

Analysis should normally occur on verified copies rather than originals.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 9 — Forensic Image

### Core Explanation

A forensic image captures storage data for later analysis and verification.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 10 — Logical Acquisition

### Core Explanation

Logical acquisition collects selected files, folders, or application data through OS or APIs.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 11 — Physical Acquisition Awareness

### Core Explanation

Physical acquisition attempts to capture lower-level storage content and may include deleted/unallocated areas.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 12 — Live Acquisition

### Core Explanation

Live acquisition collects volatile or accessible evidence from a running system.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 13 — Dead-Box Acquisition

### Core Explanation

Dead-box acquisition examines powered-off media to reduce OS changes.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 14 — Order of Volatility

### Core Explanation

Collect evidence that disappears quickly before more persistent artifacts when appropriate.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 15 — Write Blocker Awareness

### Core Explanation

Write blockers reduce accidental modification of source storage.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 16 — Hash Verification

### Core Explanation

Cryptographic hashes verify that evidence copies remain unchanged.

### Diagram / Command / Evidence Example

```bash
sha256sum evidence.img
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 17 — SHA-256 Evidence Hash

### Core Explanation

SHA-256 is commonly used to document evidence integrity.

### Diagram / Command / Evidence Example

```bash
sha256sum evidence.img
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 18 — Evidence Storage

### Core Explanation

Evidence needs controlled access, integrity protection, backups, and retention rules.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 19 — Evidence Encryption

### Core Explanation

Sensitive evidence may require encryption at rest and in transit.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 20 — Forensic Notes

### Core Explanation

Record commands, versions, timestamps, observations, and interpretations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 21 — Tool Validation

### Core Explanation

Understand tool capabilities, versions, failure modes, and result generation.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 22 — Time Zone Handling

### Core Explanation

Normalize time while preserving original timezone and clock context.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 23 — Clock Drift

### Core Explanation

System clock drift can create misleading timelines and should be documented.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 24 — Filesystem Basics

### Core Explanation

Filesystems organize metadata, directories, allocation, timestamps, permissions, and content.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 25 — NTFS Awareness

### Core Explanation

NTFS provides MFT, attributes, timestamps, journals, and metadata useful in investigations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 26 — MFT

### Core Explanation

The Master File Table records metadata for NTFS files and directories.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 27 — USN Journal Awareness

### Core Explanation

The NTFS change journal records filesystem changes and supports timelines.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 28 — Windows Prefetch Awareness

### Core Explanation

Prefetch artifacts can provide evidence about program execution on supported systems.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 29 — Windows Event Logs

### Core Explanation

Event logs provide authentication, service, policy, system, and application evidence.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 30 — Windows Registry

### Core Explanation

Registry hives contain configuration, persistence, user, device, network, and app artifacts.

### Diagram / Command / Evidence Example

```text
Registry pivots: Run keys | services | user profiles | USB | recent files | network config
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 31 — Registry Run Keys

### Core Explanation

Run/RunOnce keys can indicate legitimate or malicious autostart activity.

### Diagram / Command / Evidence Example

```text
Registry pivots: Run keys | services | user profiles | USB | recent files | network config
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 32 — Services Registry

### Core Explanation

Service configuration can reveal persistence or system modification.

### Diagram / Command / Evidence Example

```text
Registry pivots: Run keys | services | user profiles | USB | recent files | network config
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 33 — User Profile Artifacts

### Core Explanation

Profiles contain documents, browser data, app state, recent files, and per-user registry hives.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 34 — Recent File Artifacts

### Core Explanation

Recent-items metadata can support user-activity timelines.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 35 — LNK Awareness

### Core Explanation

Shortcut files can preserve paths, volumes, and access-related metadata.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 36 — Jump Lists Awareness

### Core Explanation

Jump Lists can preserve recently used files and application activity.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 37 — USB Artifacts

### Core Explanation

System artifacts can reveal connected USB devices and timing.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 38 — Recycle Bin Awareness

### Core Explanation

Deleted files may remain in recycle-bin structures with metadata.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 39 — Deleted File Recovery

### Core Explanation

Deleted content may remain recoverable until blocks are reused or trimmed.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 40 — Unallocated Space

### Core Explanation

Unallocated storage can contain remnants of deleted content.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 41 — File Slack Awareness

### Core Explanation

Slack space can contain residual bytes depending on filesystem behavior.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 42 — Linux Filesystems

### Core Explanation

Linux filesystems provide inodes, timestamps, journals, permissions, and allocation metadata.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 43 — Linux Logs

### Core Explanation

Journal, syslog, auth, and application logs support user and service activity analysis.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 44 — Shell History

### Core Explanation

Shell histories can reveal commands but may be incomplete, disabled, or modified.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 45 — Cron

### Core Explanation

Cron jobs can indicate normal automation or persistence.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 46 — systemd Units

### Core Explanation

Units and timers can reveal service execution or persistence.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 47 — SSH Artifacts

### Core Explanation

Authorized keys, known hosts, configs, auth logs, and histories support remote-access analysis.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 48 — macOS Artifacts

### Core Explanation

Unified logs, property lists, LaunchAgents/Daemons, browser data, and user artifacts support macOS investigations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 49 — Browser History

### Core Explanation

History databases reveal visited URLs and timestamps.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 50 — Browser Downloads

### Core Explanation

Download records link files to source URLs and user activity.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 51 — Browser Cache

### Core Explanation

Cache can preserve response content and metadata.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 52 — Browser Cookies

### Core Explanation

Cookies can contain sensitive session and context data.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 53 — Browser Extensions

### Core Explanation

Extensions may explain suspicious behavior or persistence.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 54 — Email Artifacts

### Core Explanation

Messages, headers, attachments, and local caches support phishing and account investigations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 55 — Document Metadata

### Core Explanation

Documents may contain author, timestamps, software, paths, and embedded content.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 56 — Archive Artifacts

### Core Explanation

Archives can reveal collection or staging activity.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 57 — File Hashing

### Core Explanation

Hash files for deduplication, malware correlation, and integrity.

### Diagram / Command / Evidence Example

```bash
sha256sum evidence.img
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 58 — File Signature

### Core Explanation

Magic bytes help identify true file type even when extensions are misleading.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 59 — Memory Forensics

### Core Explanation

Memory can reveal processes, network connections, loaded modules, injected regions, runtime strings, and volatile credentials.

### Diagram / Command / Evidence Example

```text
Memory → processes | sockets | modules | runtime strings | volatile configuration | injected regions
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 60 — Memory Acquisition

### Core Explanation

Acquire volatile memory with trusted tools when the incident question justifies it.

### Diagram / Command / Evidence Example

```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 61 — Process List

### Core Explanation

Compare processes, parent relationships, users, paths, and signatures.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 62 — Process Tree

### Core Explanation

Parent-child chains help reconstruct execution.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 63 — Loaded Modules

### Core Explanation

Unexpected modules or executable memory can indicate injection or runtime manipulation.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 64 — Network Connections in Memory

### Core Explanation

Memory may reveal active sockets and owning processes.

### Diagram / Command / Evidence Example

```text
Memory → processes | sockets | modules | runtime strings | volatile configuration | injected regions
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 65 — Command Lines in Memory

### Core Explanation

Process command lines can reveal execution parameters not preserved elsewhere.

### Diagram / Command / Evidence Example

```text
Memory → processes | sockets | modules | runtime strings | volatile configuration | injected regions
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 66 — Credential Material Sensitivity

### Core Explanation

Memory can contain authentication secrets and requires strict handling.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 67 — Timeline Analysis

### Core Explanation

Combine timestamped artifacts into one chronological narrative.

### Diagram / Command / Evidence Example

```text
filesystem + event logs + registry + browser + EDR + network → normalized timeline
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 68 — MACB Times Awareness

### Core Explanation

Filesystem modified, accessed, changed, and birth times have different semantics.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 69 — Super Timeline Awareness

### Core Explanation

A super timeline combines multiple artifact sources for correlation.

### Diagram / Command / Evidence Example

```text
filesystem + event logs + registry + browser + EDR + network → normalized timeline
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 70 — Event Correlation

### Core Explanation

Relate file, process, registry, browser, login, and network events by time and identity.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 71 — Persistence Analysis

### Core Explanation

Review services, tasks, autostarts, scripts, startup folders, and user persistence locations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 72 — Malware Artifact Analysis

### Core Explanation

Hash and preserve suspicious files before handing them to malware analysis.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 73 — User Attribution Awareness

### Core Explanation

Users, sessions, artifacts, and devices support attribution with appropriate confidence.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 74 — Anti-Forensics Awareness

### Core Explanation

Attackers may delete logs, alter timestamps, encrypt data, or use volatile execution.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 75 — Timestomping Awareness

### Core Explanation

Modified timestamps can be manipulated and require cross-validation.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 76 — Log Clearing Awareness

### Core Explanation

Cleared logs may create their own evidence or suspicious gaps.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 77 — Encryption Awareness

### Core Explanation

Encrypted volumes/files may limit access and require authorized keys or alternate evidence.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 78 — Virtual Machine Artifacts

### Core Explanation

VM disks, snapshots, logs, and metadata can support forensic analysis.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 79 — Cloud Disk Snapshots

### Core Explanation

Cloud snapshots can preserve server disks while reducing impact.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 80 — Container Forensics Awareness

### Core Explanation

Image, writable layer, runtime metadata, logs, orchestrator events, and host evidence should be correlated.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 81 — Mobile Forensics Boundary

### Core Explanation

Mobile forensics requires specialized tools and explicit organizational/legal authorization.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 82 — Forensic Search

### Core Explanation

Search should be hypothesis-driven and avoid unnecessary exposure of unrelated personal data.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 83 — Keyword Search

### Core Explanation

Keywords can locate artifacts but need context and false-positive review.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 84 — Known File Filtering

### Core Explanation

Known-good or known-bad hash sets can reduce analysis volume.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 85 — Metadata Analysis

### Core Explanation

Ownership, timestamps, paths, size, and attributes can be as important as content.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 86 — Forensic Report

### Core Explanation

Reports should explain acquisition, integrity, methods, findings, timeline, confidence, and limitations.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 87 — Fact vs Interpretation

### Core Explanation

Separate observed artifact facts from analyst interpretation.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

# Part 88 — Reproducibility

### Core Explanation

Another qualified analyst should be able to reproduce the method from notes.

### Diagram / Command / Evidence Example

```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

### Why It Matters

Reliable incident response and forensics depend on preserving context while reducing harm. The responder must distinguish confirmed evidence from hypotheses and avoid destroying the artifacts needed to understand scope and root cause.

### Practical Use

Apply the concept to a tabletop, synthetic incident, your own lab systems, authorized forensic images, or PCAP/log datasets you are permitted to analyze.

### Common Problems

- Reimaging or deleting artifacts before evidence preservation.
- Assuming the first detected host is the first compromised system.
- Resetting one password while leaving tokens, keys, sessions, or service credentials valid.
- Mixing analyst interpretation with observed facts.
- Ignoring clock drift or missing evidence sources.
- Restoring service without fixing the entry point or persistence.

### Best Practice

Preserve volatile evidence when justified, keep an action log, correlate multiple sources, contain proportionately, remove root causes, restore trusted state, and convert lessons into prevention and detection improvements.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Computer Forensics Purpose

### Objective
Practice **Computer Forensics Purpose** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 2 — Forensic Readiness

### Objective
Practice **Forensic Readiness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 3 — Evidence Integrity

### Objective
Practice **Evidence Integrity** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 4 — Chain of Custody

### Objective
Practice **Chain of Custody** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Evidence ID → collected by/time → hash/integrity → storage → transfers/access → analysis copy
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 5 — Evidence ID

### Objective
Practice **Evidence ID** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 6 — Acquisition

### Objective
Practice **Acquisition** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 7 — Original Evidence

### Objective
Practice **Original Evidence** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 8 — Working Copy

### Objective
Practice **Working Copy** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 9 — Forensic Image

### Objective
Practice **Forensic Image** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 10 — Logical Acquisition

### Objective
Practice **Logical Acquisition** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 11 — Physical Acquisition Awareness

### Objective
Practice **Physical Acquisition Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 12 — Live Acquisition

### Objective
Practice **Live Acquisition** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 13 — Dead-Box Acquisition

### Objective
Practice **Dead-Box Acquisition** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Source media → write-protected acquisition → image → SHA-256 → working copy → analysis
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 14 — Order of Volatility

### Objective
Practice **Order of Volatility** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 15 — Write Blocker Awareness

### Objective
Practice **Write Blocker Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 16 — Hash Verification

### Objective
Practice **Hash Verification** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```bash
sha256sum evidence.img
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 17 — SHA-256 Evidence Hash

### Objective
Practice **SHA-256 Evidence Hash** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```bash
sha256sum evidence.img
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 18 — Evidence Storage

### Objective
Practice **Evidence Storage** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 19 — Evidence Encryption

### Objective
Practice **Evidence Encryption** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 20 — Forensic Notes

### Objective
Practice **Forensic Notes** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 21 — Tool Validation

### Objective
Practice **Tool Validation** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 22 — Time Zone Handling

### Objective
Practice **Time Zone Handling** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 23 — Clock Drift

### Objective
Practice **Clock Drift** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 24 — Filesystem Basics

### Objective
Practice **Filesystem Basics** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 25 — NTFS Awareness

### Objective
Practice **NTFS Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 26 — MFT

### Objective
Practice **MFT** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 27 — USN Journal Awareness

### Objective
Practice **USN Journal Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 28 — Windows Prefetch Awareness

### Objective
Practice **Windows Prefetch Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 29 — Windows Event Logs

### Objective
Practice **Windows Event Logs** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 30 — Windows Registry

### Objective
Practice **Windows Registry** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Registry pivots: Run keys | services | user profiles | USB | recent files | network config
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 31 — Registry Run Keys

### Objective
Practice **Registry Run Keys** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Registry pivots: Run keys | services | user profiles | USB | recent files | network config
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 32 — Services Registry

### Objective
Practice **Services Registry** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Registry pivots: Run keys | services | user profiles | USB | recent files | network config
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 33 — User Profile Artifacts

### Objective
Practice **User Profile Artifacts** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 34 — Recent File Artifacts

### Objective
Practice **Recent File Artifacts** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 35 — LNK Awareness

### Objective
Practice **LNK Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 36 — Jump Lists Awareness

### Objective
Practice **Jump Lists Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 37 — USB Artifacts

### Objective
Practice **USB Artifacts** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 38 — Recycle Bin Awareness

### Objective
Practice **Recycle Bin Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 39 — Deleted File Recovery

### Objective
Practice **Deleted File Recovery** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 40 — Unallocated Space

### Objective
Practice **Unallocated Space** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 41 — File Slack Awareness

### Objective
Practice **File Slack Awareness** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 42 — Linux Filesystems

### Objective
Practice **Linux Filesystems** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 43 — Linux Logs

### Objective
Practice **Linux Logs** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 44 — Shell History

### Objective
Practice **Shell History** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 45 — Cron

### Objective
Practice **Cron** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 46 — systemd Units

### Objective
Practice **systemd Units** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 47 — SSH Artifacts

### Objective
Practice **SSH Artifacts** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 48 — macOS Artifacts

### Objective
Practice **macOS Artifacts** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 49 — Browser History

### Objective
Practice **Browser History** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 50 — Browser Downloads

### Objective
Practice **Browser Downloads** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 51 — Browser Cache

### Objective
Practice **Browser Cache** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 52 — Browser Cookies

### Objective
Practice **Browser Cookies** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 53 — Browser Extensions

### Objective
Practice **Browser Extensions** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 54 — Email Artifacts

### Objective
Practice **Email Artifacts** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## Lab 55 — Document Metadata

### Objective
Practice **Document Metadata** using a synthetic incident or authorized evidence.

### Procedure
1. Record incident question and scope.
2. Preserve relevant evidence before invasive actions.
3. Record time, collector, source, and integrity information.
4. Analyze only a working copy when applicable.
5. Correlate at least two data sources.
6. Build or update the timeline.
7. Record facts, inference, confidence, and limitations separately.
8. Decide containment/remediation or next forensic step.
9. Verify the action.
10. Record lessons/detection improvements.

### Starter Example
```text
Preserve → Collect → Correlate → Scope → Decide → Act → Verify → Improve
```

```text
Incident / case:
Evidence ID:
Time range:
Method:
Facts:
Inference:
Confidence:
Action:
Verification:
Limitations:
```

---

## 6. Mini Project

# Mini Project — Host Forensics Case

Use a benign forensic image or your own lab VM snapshot. Record evidence ID and hash, analyze filesystem/user artifacts, Windows/Linux logs as applicable, browser history, persistence, suspicious files, and one memory/volatile dataset. Build a timeline and write a forensic report separating facts from interpretation.

### Required Deliverables
1. Scope / incident scenario
2. Timeline
3. Evidence inventory
4. Collection / analysis methods
5. Findings and confidence
6. Containment / remediation decisions
7. Recovery or forensic conclusions
8. Detection / control improvements
9. Limitations
10. Final report

## 7. Recommended Resources

- NIST SP 800-86 — https://csrc.nist.gov/pubs/sp/800/86/final
- The Sleuth Kit — https://www.sleuthkit.org/
- Volatility Foundation — https://volatilityfoundation.org/
- Eric Zimmerman tools — https://ericzimmerman.github.io/

## 8. Certification Relevance

Relevant to DFIR, computer forensics, incident response, malware analysis, and security operations.

## 9. Common Mistakes & Best Practices

### Common Mistakes
- Destroying evidence during containment.
- Failing to record response actions.
- Treating IOC absence as proof of safety.
- Restoring from backups without validating trust.
- Ignoring tokens, keys, and service credentials during credential rotation.
- Reporting forensic interpretation as unquestionable fact.

### Best Practices
- Keep a timeline and decision log.
- Preserve evidence before invasive changes when feasible.
- Hash formal evidence and analyze copies.
- Separate fact, inference, and confidence.
- Coordinate technical actions with business recovery.
- Retest and heighten monitoring after recovery.

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the key lesson from **Computer Forensics Purpose**?

**Short answer:** Computer forensics preserves, acquires, examines, analyzes, and reports digital evidence while maintaining integrity and context.

### Q2. What is the key lesson from **Forensic Readiness**?

**Short answer:** Prepare logging, time, ownership, retention, tools, access, and procedures before incidents.

### Q3. What is the key lesson from **Evidence Integrity**?

**Short answer:** Forensic conclusions depend on preserving evidence and documenting transformations.

### Q4. What is the key lesson from **Chain of Custody**?

**Short answer:** Chain of custody records collection, possession, transfer, storage, access, and integrity.

### Q5. What is the key lesson from **Evidence ID**?

**Short answer:** Every evidence item should have a unique identifier tied to notes and storage.

### Q6. What is the key lesson from **Acquisition**?

**Short answer:** Acquisition creates a reliable copy of source evidence for analysis.

### Q7. What is the key lesson from **Original Evidence**?

**Short answer:** Original media should be preserved and accessed as little as possible after acquisition.

### Q8. What is the key lesson from **Working Copy**?

**Short answer:** Analysis should normally occur on verified copies rather than originals.

### Q9. What is the key lesson from **Forensic Image**?

**Short answer:** A forensic image captures storage data for later analysis and verification.

### Q10. What is the key lesson from **Logical Acquisition**?

**Short answer:** Logical acquisition collects selected files, folders, or application data through OS or APIs.

### Q11. What is the key lesson from **Physical Acquisition Awareness**?

**Short answer:** Physical acquisition attempts to capture lower-level storage content and may include deleted/unallocated areas.

### Q12. What is the key lesson from **Live Acquisition**?

**Short answer:** Live acquisition collects volatile or accessible evidence from a running system.

### Q13. What is the key lesson from **Dead-Box Acquisition**?

**Short answer:** Dead-box acquisition examines powered-off media to reduce OS changes.

### Q14. What is the key lesson from **Order of Volatility**?

**Short answer:** Collect evidence that disappears quickly before more persistent artifacts when appropriate.

### Q15. What is the key lesson from **Write Blocker Awareness**?

**Short answer:** Write blockers reduce accidental modification of source storage.

### Q16. What is the key lesson from **Hash Verification**?

**Short answer:** Cryptographic hashes verify that evidence copies remain unchanged.

### Q17. What is the key lesson from **SHA-256 Evidence Hash**?

**Short answer:** SHA-256 is commonly used to document evidence integrity.

### Q18. What is the key lesson from **Evidence Storage**?

**Short answer:** Evidence needs controlled access, integrity protection, backups, and retention rules.

### Q19. What is the key lesson from **Evidence Encryption**?

**Short answer:** Sensitive evidence may require encryption at rest and in transit.

### Q20. What is the key lesson from **Forensic Notes**?

**Short answer:** Record commands, versions, timestamps, observations, and interpretations.

### Q21. What is the key lesson from **Tool Validation**?

**Short answer:** Understand tool capabilities, versions, failure modes, and result generation.

### Q22. What is the key lesson from **Time Zone Handling**?

**Short answer:** Normalize time while preserving original timezone and clock context.

### Q23. What is the key lesson from **Clock Drift**?

**Short answer:** System clock drift can create misleading timelines and should be documented.

### Q24. What is the key lesson from **Filesystem Basics**?

**Short answer:** Filesystems organize metadata, directories, allocation, timestamps, permissions, and content.

### Q25. What is the key lesson from **NTFS Awareness**?

**Short answer:** NTFS provides MFT, attributes, timestamps, journals, and metadata useful in investigations.

### Q26. What is the key lesson from **MFT**?

**Short answer:** The Master File Table records metadata for NTFS files and directories.

### Q27. What is the key lesson from **USN Journal Awareness**?

**Short answer:** The NTFS change journal records filesystem changes and supports timelines.

### Q28. What is the key lesson from **Windows Prefetch Awareness**?

**Short answer:** Prefetch artifacts can provide evidence about program execution on supported systems.

### Q29. What is the key lesson from **Windows Event Logs**?

**Short answer:** Event logs provide authentication, service, policy, system, and application evidence.

### Q30. What is the key lesson from **Windows Registry**?

**Short answer:** Registry hives contain configuration, persistence, user, device, network, and app artifacts.

### Q31. What is the key lesson from **Registry Run Keys**?

**Short answer:** Run/RunOnce keys can indicate legitimate or malicious autostart activity.

### Q32. What is the key lesson from **Services Registry**?

**Short answer:** Service configuration can reveal persistence or system modification.

### Q33. What is the key lesson from **User Profile Artifacts**?

**Short answer:** Profiles contain documents, browser data, app state, recent files, and per-user registry hives.

### Q34. What is the key lesson from **Recent File Artifacts**?

**Short answer:** Recent-items metadata can support user-activity timelines.

### Q35. What is the key lesson from **LNK Awareness**?

**Short answer:** Shortcut files can preserve paths, volumes, and access-related metadata.

### Q36. What is the key lesson from **Jump Lists Awareness**?

**Short answer:** Jump Lists can preserve recently used files and application activity.

### Q37. What is the key lesson from **USB Artifacts**?

**Short answer:** System artifacts can reveal connected USB devices and timing.

### Q38. What is the key lesson from **Recycle Bin Awareness**?

**Short answer:** Deleted files may remain in recycle-bin structures with metadata.

### Q39. What is the key lesson from **Deleted File Recovery**?

**Short answer:** Deleted content may remain recoverable until blocks are reused or trimmed.

### Q40. What is the key lesson from **Unallocated Space**?

**Short answer:** Unallocated storage can contain remnants of deleted content.

### Q41. What is the key lesson from **File Slack Awareness**?

**Short answer:** Slack space can contain residual bytes depending on filesystem behavior.

### Q42. What is the key lesson from **Linux Filesystems**?

**Short answer:** Linux filesystems provide inodes, timestamps, journals, permissions, and allocation metadata.

### Q43. What is the key lesson from **Linux Logs**?

**Short answer:** Journal, syslog, auth, and application logs support user and service activity analysis.

### Q44. What is the key lesson from **Shell History**?

**Short answer:** Shell histories can reveal commands but may be incomplete, disabled, or modified.

### Q45. What is the key lesson from **Cron**?

**Short answer:** Cron jobs can indicate normal automation or persistence.

### Q46. What is the key lesson from **systemd Units**?

**Short answer:** Units and timers can reveal service execution or persistence.

### Q47. What is the key lesson from **SSH Artifacts**?

**Short answer:** Authorized keys, known hosts, configs, auth logs, and histories support remote-access analysis.

### Q48. What is the key lesson from **macOS Artifacts**?

**Short answer:** Unified logs, property lists, LaunchAgents/Daemons, browser data, and user artifacts support macOS investigations.

### Q49. What is the key lesson from **Browser History**?

**Short answer:** History databases reveal visited URLs and timestamps.

### Q50. What is the key lesson from **Browser Downloads**?

**Short answer:** Download records link files to source URLs and user activity.

### Q51. What is the key lesson from **Browser Cache**?

**Short answer:** Cache can preserve response content and metadata.

### Q52. What is the key lesson from **Browser Cookies**?

**Short answer:** Cookies can contain sensitive session and context data.

### Q53. What is the key lesson from **Browser Extensions**?

**Short answer:** Extensions may explain suspicious behavior or persistence.

### Q54. What is the key lesson from **Email Artifacts**?

**Short answer:** Messages, headers, attachments, and local caches support phishing and account investigations.

### Q55. What is the key lesson from **Document Metadata**?

**Short answer:** Documents may contain author, timestamps, software, paths, and embedded content.

### Q56. What is the key lesson from **Archive Artifacts**?

**Short answer:** Archives can reveal collection or staging activity.

### Q57. What is the key lesson from **File Hashing**?

**Short answer:** Hash files for deduplication, malware correlation, and integrity.

### Q58. What is the key lesson from **File Signature**?

**Short answer:** Magic bytes help identify true file type even when extensions are misleading.

### Q59. What is the key lesson from **Memory Forensics**?

**Short answer:** Memory can reveal processes, network connections, loaded modules, injected regions, runtime strings, and volatile credentials.

### Q60. What is the key lesson from **Memory Acquisition**?

**Short answer:** Acquire volatile memory with trusted tools when the incident question justifies it.

### Q61. What is the key lesson from **Process List**?

**Short answer:** Compare processes, parent relationships, users, paths, and signatures.

### Q62. What is the key lesson from **Process Tree**?

**Short answer:** Parent-child chains help reconstruct execution.

### Q63. What is the key lesson from **Loaded Modules**?

**Short answer:** Unexpected modules or executable memory can indicate injection or runtime manipulation.

### Q64. What is the key lesson from **Network Connections in Memory**?

**Short answer:** Memory may reveal active sockets and owning processes.

### Q65. What is the key lesson from **Command Lines in Memory**?

**Short answer:** Process command lines can reveal execution parameters not preserved elsewhere.

### Q66. What is the key lesson from **Credential Material Sensitivity**?

**Short answer:** Memory can contain authentication secrets and requires strict handling.

### Q67. What is the key lesson from **Timeline Analysis**?

**Short answer:** Combine timestamped artifacts into one chronological narrative.

### Q68. What is the key lesson from **MACB Times Awareness**?

**Short answer:** Filesystem modified, accessed, changed, and birth times have different semantics.

### Q69. What is the key lesson from **Super Timeline Awareness**?

**Short answer:** A super timeline combines multiple artifact sources for correlation.

### Q70. What is the key lesson from **Event Correlation**?

**Short answer:** Relate file, process, registry, browser, login, and network events by time and identity.

### Q71. What is the key lesson from **Persistence Analysis**?

**Short answer:** Review services, tasks, autostarts, scripts, startup folders, and user persistence locations.

### Q72. What is the key lesson from **Malware Artifact Analysis**?

**Short answer:** Hash and preserve suspicious files before handing them to malware analysis.

### Q73. What is the key lesson from **User Attribution Awareness**?

**Short answer:** Users, sessions, artifacts, and devices support attribution with appropriate confidence.

### Q74. What is the key lesson from **Anti-Forensics Awareness**?

**Short answer:** Attackers may delete logs, alter timestamps, encrypt data, or use volatile execution.

### Q75. What is the key lesson from **Timestomping Awareness**?

**Short answer:** Modified timestamps can be manipulated and require cross-validation.

### Q76. What is the key lesson from **Log Clearing Awareness**?

**Short answer:** Cleared logs may create their own evidence or suspicious gaps.

### Q77. What is the key lesson from **Encryption Awareness**?

**Short answer:** Encrypted volumes/files may limit access and require authorized keys or alternate evidence.

### Q78. What is the key lesson from **Virtual Machine Artifacts**?

**Short answer:** VM disks, snapshots, logs, and metadata can support forensic analysis.

### Q79. What is the key lesson from **Cloud Disk Snapshots**?

**Short answer:** Cloud snapshots can preserve server disks while reducing impact.

### Q80. What is the key lesson from **Container Forensics Awareness**?

**Short answer:** Image, writable layer, runtime metadata, logs, orchestrator events, and host evidence should be correlated.

### Q81. What is the key lesson from **Mobile Forensics Boundary**?

**Short answer:** Mobile forensics requires specialized tools and explicit organizational/legal authorization.

### Q82. What is the key lesson from **Forensic Search**?

**Short answer:** Search should be hypothesis-driven and avoid unnecessary exposure of unrelated personal data.

### Q83. What is the key lesson from **Keyword Search**?

**Short answer:** Keywords can locate artifacts but need context and false-positive review.

### Q84. What is the key lesson from **Known File Filtering**?

**Short answer:** Known-good or known-bad hash sets can reduce analysis volume.

### Q85. What is the key lesson from **Metadata Analysis**?

**Short answer:** Ownership, timestamps, paths, size, and attributes can be as important as content.

### Q86. What is the key lesson from **Forensic Report**?

**Short answer:** Reports should explain acquisition, integrity, methods, findings, timeline, confidence, and limitations.

### Q87. What is the key lesson from **Fact vs Interpretation**?

**Short answer:** Separate observed artifact facts from analyst interpretation.

### Q88. What is the key lesson from **Reproducibility**?

**Short answer:** Another qualified analyst should be able to reproduce the method from notes.

## Completion Checklist
- [ ] I completed at least 30 labs.
- [ ] I completed the mini project.
- [ ] I can preserve and document evidence.
- [ ] I can build a cross-source timeline.
- [ ] I can distinguish containment, eradication, and recovery.
- [ ] I can state confidence and limitations.
