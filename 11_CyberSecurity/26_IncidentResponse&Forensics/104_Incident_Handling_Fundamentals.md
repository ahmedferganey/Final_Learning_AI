# 104. Incident Handling Fundamentals

> Phase 26 — Incident Response & Forensics

## 1. Topic Title

**Incident Handling Fundamentals**

## 2. Learning Objectives

- Explain incident intake, classification, severity, ownership, and escalation.
- Perform initial validation and scoping while preserving evidence.
- Build timelines, action logs, handoffs, and stakeholder updates.
- Choose proportionate short- and long-term containment.
- Build handling runbooks and tabletop exercises.

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

# Part 1 — Incident Handling Purpose

### Core Explanation

Incident handling provides the first structured process for validating, classifying, escalating, coordinating, and stabilizing suspected security incidents.

### Diagram / Command / Evidence Example

```text
Prepare → Detect/Validate → Scope → Contain → Eradicate → Recover → Improve
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

# Part 2 — Incident Definition

### Core Explanation

An incident is an adverse security condition requiring coordinated analysis or response beyond routine alert handling.

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

# Part 3 — Event vs Alert vs Incident

### Core Explanation

Events are observations, alerts are detection signals, and incidents require coordinated response.

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

# Part 4 — Handling vs Response

### Core Explanation

Incident handling emphasizes intake, triage, communication, evidence, and escalation while full response includes eradication and recovery.

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

# Part 5 — Incident Intake

### Core Explanation

Intake records who reported what, when, affected assets, evidence, and immediate business impact.

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

# Part 6 — Reporting Channel

### Core Explanation

Organizations should provide clear channels for employees, customers, SOC analysts, and partners to report security concerns.

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

# Part 7 — Incident Ticket

### Core Explanation

A ticket should capture owner, severity, timeline, scope, evidence, decisions, actions, and communication.

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

# Part 8 — Incident Owner

### Core Explanation

Every incident requires an accountable lead or owner.

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

# Part 9 — Technical Lead

### Core Explanation

The technical lead coordinates investigation and technical actions.

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

# Part 10 — Business Owner

### Core Explanation

Business owners provide service criticality, constraints, and recovery priorities.

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

# Part 11 — Severity Model

### Core Explanation

Severity should reflect business impact, scope, privilege, data, availability, adversary activity, and recovery complexity.

### Diagram / Command / Evidence Example

```text
Severity = business impact + scope + privilege + data + availability + adversary activity + recovery complexity
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

# Part 12 — Priority

### Core Explanation

Priority may differ from technical severity when business timing or active exploitation changes urgency.

### Diagram / Command / Evidence Example

```text
Severity = business impact + scope + privilege + data + availability + adversary activity + recovery complexity
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

# Part 13 — Incident Category

### Core Explanation

Categories may include malware, account compromise, data exposure, denial of service, phishing, cloud compromise, insider, or web attack.

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

# Part 14 — Triage

### Core Explanation

Triage validates the report, gathers essential context, and determines escalation.

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

# Part 15 — Initial Scope

### Core Explanation

Identify affected users, endpoints, apps, cloud accounts, networks, data, and time range.

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

# Part 16 — Initial Hypothesis

### Core Explanation

Record the current explanation while distinguishing it from confirmed facts.

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

# Part 17 — Confidence

### Core Explanation

Express how strongly evidence supports the incident hypothesis.

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

# Part 18 — Evidence Preservation

### Core Explanation

Preserve volatile or easily changed evidence before invasive remediation when feasible.

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

# Part 19 — Volatile Evidence

### Core Explanation

Memory, processes, network connections, sessions, tokens, and temporary files can disappear quickly.

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

# Part 20 — Non-Volatile Evidence

### Core Explanation

Disk images, logs, cloud audit records, configuration, and backups persist longer but can still be overwritten.

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

# Part 21 — Chain of Custody

### Core Explanation

Formal investigations may require documented evidence collection, transfer, storage, and access.

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

# Part 22 — Time Synchronization

### Core Explanation

Accurate clocks enable reliable timelines across endpoint, network, identity, and cloud sources.

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

# Part 23 — Communication Plan

### Core Explanation

Define technical, business, leadership, legal/privacy, and external update paths.

### Diagram / Command / Evidence Example

```text
Incident lead → technical teams | business owner | legal/privacy | communications | leadership
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

# Part 24 — Need-to-Know

### Core Explanation

Share incident information only with people who require it for response or governance.

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

# Part 25 — War Room

### Core Explanation

Major incidents may use a dedicated coordination channel with clear ownership and notes.

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

# Part 26 — Out-of-Band Communication

### Core Explanation

If corporate email/chat may be compromised, responders need trusted alternatives.

### Diagram / Command / Evidence Example

```text
Incident lead → technical teams | business owner | legal/privacy | communications | leadership
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

# Part 27 — Escalation Criteria

### Core Explanation

Escalate based on privilege, persistence, lateral movement, sensitive data, service impact, active adversary, or uncertainty.

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

# Part 28 — Legal / Privacy Escalation

### Core Explanation

Potential regulated-data exposure should be escalated to appropriate internal specialists.

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

# Part 29 — Executive Escalation

### Core Explanation

Leadership should be notified according to severity and business impact.

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

# Part 30 — Third-Party Escalation

### Core Explanation

Cloud, SaaS, or vendors may need to provide logs, containment, or support.

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

# Part 31 — Containment Planning

### Core Explanation

Containment should reduce harm while preserving evidence and business continuity.

### Diagram / Command / Evidence Example

```text
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

# Part 32 — Short-Term Containment

### Core Explanation

Immediate controls may isolate a host, disable an account, revoke a token, or block a path.

### Diagram / Command / Evidence Example

```text
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

# Part 33 — Long-Term Containment

### Core Explanation

Longer-term containment stabilizes operations while permanent fixes are prepared.

### Diagram / Command / Evidence Example

```text
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

# Part 34 — Account Disablement

### Core Explanation

Disabling accounts can stop access but may disrupt services or evidence and should be targeted.

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

# Part 35 — Credential Reset

### Core Explanation

Reset or rotate exposed credentials after identifying affected identities and dependencies.

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

# Part 36 — Token Revocation

### Core Explanation

Cloud, session, and API tokens may remain usable after password changes unless explicitly revoked.

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

# Part 37 — Host Isolation

### Core Explanation

EDR or network isolation can stop communication while preserving state for investigation.

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

# Part 38 — Network Block

### Core Explanation

Firewall, proxy, DNS, or cloud blocks can limit malicious paths while preserving context.

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

# Part 39 — Service Disablement

### Core Explanation

Disabling a vulnerable service may be the safest containment when business impact permits.

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

# Part 40 — Evidence Before Reimage

### Core Explanation

Reimaging too early destroys artifacts needed for scoping and lessons learned.

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

# Part 41 — Containment Rollback

### Core Explanation

Containment actions need owners, rollback criteria, and documentation.

### Diagram / Command / Evidence Example

```text
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

# Part 42 — Incident Timeline

### Core Explanation

Maintain a chronological record of detection, evidence, actions, communication, and impact.

### Diagram / Command / Evidence Example

```text
10:14 EDR process start
10:16 DNS new domain
10:19 IAM token use
10:22 firewall outbound session
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

# Part 43 — Decision Log

### Core Explanation

Record major decisions, alternatives, owner, time, and rationale.

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

# Part 44 — Action Log

### Core Explanation

Record every containment or system change made during handling.

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

# Part 45 — Stakeholder Update

### Core Explanation

Updates should state confirmed facts, impact, actions, risks, and next checkpoint.

### Diagram / Command / Evidence Example

```text
Incident lead → technical teams | business owner | legal/privacy | communications | leadership
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

# Part 46 — Status Cadence

### Core Explanation

Define update frequency based on severity and uncertainty.

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

# Part 47 — Handoff

### Core Explanation

Handoffs should include scope, hypothesis, evidence, containment, and pending actions.

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

# Part 48 — Responder Safety

### Core Explanation

Major incidents create fatigue and error risk; role rotation and handoffs matter.

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

# Part 49 — Tabletop Exercise

### Core Explanation

Tabletops test roles, decisions, communications, and runbooks without technical impact.

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

# Part 50 — Incident Runbook

### Core Explanation

Runbooks define evidence, decisions, actions, escalation, and closure for common scenarios.

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

# Part 51 — Phishing Handling

### Core Explanation

Validate message/user impact, remove malicious content, protect accounts, and search for related messages.

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

# Part 52 — Malware Handling

### Core Explanation

Preserve sample and telemetry, isolate affected systems, and scope related hosts.

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

# Part 53 — Account Compromise Handling

### Core Explanation

Review sign-ins, MFA, tokens, privilege, SaaS changes, and connected hosts.

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

# Part 54 — Web Incident Handling

### Core Explanation

Preserve app/WAF/API logs, identify routes/accounts/data, and coordinate containment.

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

# Part 55 — Cloud Incident Handling

### Core Explanation

Review audit/IAM/network/object logs, revoke credentials, contain resources, and preserve evidence.

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

# Part 56 — Lost Device Handling

### Core Explanation

Revoke sessions, evaluate encryption/MDM, lock/wipe as appropriate, and assess data exposure.

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

# Part 57 — Data Exposure Handling

### Core Explanation

Identify data type, records, users, access path, duration, downloads, and governance implications.

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

# Part 58 — DoS Handling

### Core Explanation

Coordinate provider and edge controls, prioritize critical services, and collect traffic evidence.

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

# Part 59 — Insider Incident Awareness

### Core Explanation

Insider cases require careful HR/legal/privacy coordination and strict evidence handling.

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

# Part 60 — Incident Metrics

### Core Explanation

Measure time to validate, escalate, contain, communicate, and close while preserving quality.

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

# Part 61 — Post-Handling Review

### Core Explanation

Incidents should feed detection, hardening, and process improvements where useful.

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

## Lab 1 — Incident Handling Purpose

### Objective
Practice **Incident Handling Purpose** using a synthetic incident or authorized evidence.

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
Prepare → Detect/Validate → Scope → Contain → Eradicate → Recover → Improve
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

## Lab 2 — Incident Definition

### Objective
Practice **Incident Definition** using a synthetic incident or authorized evidence.

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

## Lab 3 — Event vs Alert vs Incident

### Objective
Practice **Event vs Alert vs Incident** using a synthetic incident or authorized evidence.

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

## Lab 4 — Handling vs Response

### Objective
Practice **Handling vs Response** using a synthetic incident or authorized evidence.

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

## Lab 5 — Incident Intake

### Objective
Practice **Incident Intake** using a synthetic incident or authorized evidence.

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

## Lab 6 — Reporting Channel

### Objective
Practice **Reporting Channel** using a synthetic incident or authorized evidence.

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

## Lab 7 — Incident Ticket

### Objective
Practice **Incident Ticket** using a synthetic incident or authorized evidence.

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

## Lab 8 — Incident Owner

### Objective
Practice **Incident Owner** using a synthetic incident or authorized evidence.

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

## Lab 9 — Technical Lead

### Objective
Practice **Technical Lead** using a synthetic incident or authorized evidence.

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

## Lab 10 — Business Owner

### Objective
Practice **Business Owner** using a synthetic incident or authorized evidence.

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

## Lab 11 — Severity Model

### Objective
Practice **Severity Model** using a synthetic incident or authorized evidence.

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
Severity = business impact + scope + privilege + data + availability + adversary activity + recovery complexity
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

## Lab 12 — Priority

### Objective
Practice **Priority** using a synthetic incident or authorized evidence.

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
Severity = business impact + scope + privilege + data + availability + adversary activity + recovery complexity
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

## Lab 13 — Incident Category

### Objective
Practice **Incident Category** using a synthetic incident or authorized evidence.

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

## Lab 14 — Triage

### Objective
Practice **Triage** using a synthetic incident or authorized evidence.

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

## Lab 15 — Initial Scope

### Objective
Practice **Initial Scope** using a synthetic incident or authorized evidence.

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

## Lab 16 — Initial Hypothesis

### Objective
Practice **Initial Hypothesis** using a synthetic incident or authorized evidence.

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

## Lab 17 — Confidence

### Objective
Practice **Confidence** using a synthetic incident or authorized evidence.

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

## Lab 18 — Evidence Preservation

### Objective
Practice **Evidence Preservation** using a synthetic incident or authorized evidence.

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

## Lab 19 — Volatile Evidence

### Objective
Practice **Volatile Evidence** using a synthetic incident or authorized evidence.

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

## Lab 20 — Non-Volatile Evidence

### Objective
Practice **Non-Volatile Evidence** using a synthetic incident or authorized evidence.

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

## Lab 21 — Chain of Custody

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

## Lab 22 — Time Synchronization

### Objective
Practice **Time Synchronization** using a synthetic incident or authorized evidence.

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

## Lab 23 — Communication Plan

### Objective
Practice **Communication Plan** using a synthetic incident or authorized evidence.

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
Incident lead → technical teams | business owner | legal/privacy | communications | leadership
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

## Lab 24 — Need-to-Know

### Objective
Practice **Need-to-Know** using a synthetic incident or authorized evidence.

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

## Lab 25 — War Room

### Objective
Practice **War Room** using a synthetic incident or authorized evidence.

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

## Lab 26 — Out-of-Band Communication

### Objective
Practice **Out-of-Band Communication** using a synthetic incident or authorized evidence.

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
Incident lead → technical teams | business owner | legal/privacy | communications | leadership
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

## Lab 27 — Escalation Criteria

### Objective
Practice **Escalation Criteria** using a synthetic incident or authorized evidence.

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

## Lab 28 — Legal / Privacy Escalation

### Objective
Practice **Legal / Privacy Escalation** using a synthetic incident or authorized evidence.

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

## Lab 29 — Executive Escalation

### Objective
Practice **Executive Escalation** using a synthetic incident or authorized evidence.

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

## Lab 30 — Third-Party Escalation

### Objective
Practice **Third-Party Escalation** using a synthetic incident or authorized evidence.

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

## Lab 31 — Containment Planning

### Objective
Practice **Containment Planning** using a synthetic incident or authorized evidence.

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
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

## Lab 32 — Short-Term Containment

### Objective
Practice **Short-Term Containment** using a synthetic incident or authorized evidence.

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
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

## Lab 33 — Long-Term Containment

### Objective
Practice **Long-Term Containment** using a synthetic incident or authorized evidence.

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
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

## Lab 34 — Account Disablement

### Objective
Practice **Account Disablement** using a synthetic incident or authorized evidence.

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

## Lab 35 — Credential Reset

### Objective
Practice **Credential Reset** using a synthetic incident or authorized evidence.

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

## Lab 36 — Token Revocation

### Objective
Practice **Token Revocation** using a synthetic incident or authorized evidence.

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

## Lab 37 — Host Isolation

### Objective
Practice **Host Isolation** using a synthetic incident or authorized evidence.

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

## Lab 38 — Network Block

### Objective
Practice **Network Block** using a synthetic incident or authorized evidence.

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

## Lab 39 — Service Disablement

### Objective
Practice **Service Disablement** using a synthetic incident or authorized evidence.

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

## Lab 40 — Evidence Before Reimage

### Objective
Practice **Evidence Before Reimage** using a synthetic incident or authorized evidence.

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

## Lab 41 — Containment Rollback

### Objective
Practice **Containment Rollback** using a synthetic incident or authorized evidence.

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
Containment: isolate host | disable/restrict account | revoke token | block path | disable vulnerable service | preserve evidence
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

## Lab 42 — Incident Timeline

### Objective
Practice **Incident Timeline** using a synthetic incident or authorized evidence.

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
10:14 EDR process start
10:16 DNS new domain
10:19 IAM token use
10:22 firewall outbound session
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

## Lab 43 — Decision Log

### Objective
Practice **Decision Log** using a synthetic incident or authorized evidence.

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

## Lab 44 — Action Log

### Objective
Practice **Action Log** using a synthetic incident or authorized evidence.

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

## Lab 45 — Stakeholder Update

### Objective
Practice **Stakeholder Update** using a synthetic incident or authorized evidence.

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
Incident lead → technical teams | business owner | legal/privacy | communications | leadership
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

## Lab 46 — Status Cadence

### Objective
Practice **Status Cadence** using a synthetic incident or authorized evidence.

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

## Lab 47 — Handoff

### Objective
Practice **Handoff** using a synthetic incident or authorized evidence.

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

## Lab 48 — Responder Safety

### Objective
Practice **Responder Safety** using a synthetic incident or authorized evidence.

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

## Lab 49 — Tabletop Exercise

### Objective
Practice **Tabletop Exercise** using a synthetic incident or authorized evidence.

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

## Lab 50 — Incident Runbook

### Objective
Practice **Incident Runbook** using a synthetic incident or authorized evidence.

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

## Lab 51 — Phishing Handling

### Objective
Practice **Phishing Handling** using a synthetic incident or authorized evidence.

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

## Lab 52 — Malware Handling

### Objective
Practice **Malware Handling** using a synthetic incident or authorized evidence.

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

## Lab 53 — Account Compromise Handling

### Objective
Practice **Account Compromise Handling** using a synthetic incident or authorized evidence.

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

## Lab 54 — Web Incident Handling

### Objective
Practice **Web Incident Handling** using a synthetic incident or authorized evidence.

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

## Lab 55 — Cloud Incident Handling

### Objective
Practice **Cloud Incident Handling** using a synthetic incident or authorized evidence.

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

# Mini Project — Incident Handling Program

Create an incident severity matrix, intake form, escalation tree, communications matrix, evidence checklist, containment decision matrix, handoff template, and five handling runbooks: phishing, malware, account compromise, web incident, and cloud incident. Conduct a tabletop and record gaps.

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

- NIST SP 800-61 Rev. 3 — https://csrc.nist.gov/pubs/sp/800/61/r3/final
- CISA Incident Response resources — https://www.cisa.gov/topics/cyber-threats-and-advisories
- NIST Cybersecurity Framework — https://www.nist.gov/cyberframework

## 8. Certification Relevance

Relevant to SOC, incident handler, security analyst, blue-team operations, and incident response.

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

### Q1. What is the key lesson from **Incident Handling Purpose**?

**Short answer:** Incident handling provides the first structured process for validating, classifying, escalating, coordinating, and stabilizing suspected security incidents.

### Q2. What is the key lesson from **Incident Definition**?

**Short answer:** An incident is an adverse security condition requiring coordinated analysis or response beyond routine alert handling.

### Q3. What is the key lesson from **Event vs Alert vs Incident**?

**Short answer:** Events are observations, alerts are detection signals, and incidents require coordinated response.

### Q4. What is the key lesson from **Handling vs Response**?

**Short answer:** Incident handling emphasizes intake, triage, communication, evidence, and escalation while full response includes eradication and recovery.

### Q5. What is the key lesson from **Incident Intake**?

**Short answer:** Intake records who reported what, when, affected assets, evidence, and immediate business impact.

### Q6. What is the key lesson from **Reporting Channel**?

**Short answer:** Organizations should provide clear channels for employees, customers, SOC analysts, and partners to report security concerns.

### Q7. What is the key lesson from **Incident Ticket**?

**Short answer:** A ticket should capture owner, severity, timeline, scope, evidence, decisions, actions, and communication.

### Q8. What is the key lesson from **Incident Owner**?

**Short answer:** Every incident requires an accountable lead or owner.

### Q9. What is the key lesson from **Technical Lead**?

**Short answer:** The technical lead coordinates investigation and technical actions.

### Q10. What is the key lesson from **Business Owner**?

**Short answer:** Business owners provide service criticality, constraints, and recovery priorities.

### Q11. What is the key lesson from **Severity Model**?

**Short answer:** Severity should reflect business impact, scope, privilege, data, availability, adversary activity, and recovery complexity.

### Q12. What is the key lesson from **Priority**?

**Short answer:** Priority may differ from technical severity when business timing or active exploitation changes urgency.

### Q13. What is the key lesson from **Incident Category**?

**Short answer:** Categories may include malware, account compromise, data exposure, denial of service, phishing, cloud compromise, insider, or web attack.

### Q14. What is the key lesson from **Triage**?

**Short answer:** Triage validates the report, gathers essential context, and determines escalation.

### Q15. What is the key lesson from **Initial Scope**?

**Short answer:** Identify affected users, endpoints, apps, cloud accounts, networks, data, and time range.

### Q16. What is the key lesson from **Initial Hypothesis**?

**Short answer:** Record the current explanation while distinguishing it from confirmed facts.

### Q17. What is the key lesson from **Confidence**?

**Short answer:** Express how strongly evidence supports the incident hypothesis.

### Q18. What is the key lesson from **Evidence Preservation**?

**Short answer:** Preserve volatile or easily changed evidence before invasive remediation when feasible.

### Q19. What is the key lesson from **Volatile Evidence**?

**Short answer:** Memory, processes, network connections, sessions, tokens, and temporary files can disappear quickly.

### Q20. What is the key lesson from **Non-Volatile Evidence**?

**Short answer:** Disk images, logs, cloud audit records, configuration, and backups persist longer but can still be overwritten.

### Q21. What is the key lesson from **Chain of Custody**?

**Short answer:** Formal investigations may require documented evidence collection, transfer, storage, and access.

### Q22. What is the key lesson from **Time Synchronization**?

**Short answer:** Accurate clocks enable reliable timelines across endpoint, network, identity, and cloud sources.

### Q23. What is the key lesson from **Communication Plan**?

**Short answer:** Define technical, business, leadership, legal/privacy, and external update paths.

### Q24. What is the key lesson from **Need-to-Know**?

**Short answer:** Share incident information only with people who require it for response or governance.

### Q25. What is the key lesson from **War Room**?

**Short answer:** Major incidents may use a dedicated coordination channel with clear ownership and notes.

### Q26. What is the key lesson from **Out-of-Band Communication**?

**Short answer:** If corporate email/chat may be compromised, responders need trusted alternatives.

### Q27. What is the key lesson from **Escalation Criteria**?

**Short answer:** Escalate based on privilege, persistence, lateral movement, sensitive data, service impact, active adversary, or uncertainty.

### Q28. What is the key lesson from **Legal / Privacy Escalation**?

**Short answer:** Potential regulated-data exposure should be escalated to appropriate internal specialists.

### Q29. What is the key lesson from **Executive Escalation**?

**Short answer:** Leadership should be notified according to severity and business impact.

### Q30. What is the key lesson from **Third-Party Escalation**?

**Short answer:** Cloud, SaaS, or vendors may need to provide logs, containment, or support.

### Q31. What is the key lesson from **Containment Planning**?

**Short answer:** Containment should reduce harm while preserving evidence and business continuity.

### Q32. What is the key lesson from **Short-Term Containment**?

**Short answer:** Immediate controls may isolate a host, disable an account, revoke a token, or block a path.

### Q33. What is the key lesson from **Long-Term Containment**?

**Short answer:** Longer-term containment stabilizes operations while permanent fixes are prepared.

### Q34. What is the key lesson from **Account Disablement**?

**Short answer:** Disabling accounts can stop access but may disrupt services or evidence and should be targeted.

### Q35. What is the key lesson from **Credential Reset**?

**Short answer:** Reset or rotate exposed credentials after identifying affected identities and dependencies.

### Q36. What is the key lesson from **Token Revocation**?

**Short answer:** Cloud, session, and API tokens may remain usable after password changes unless explicitly revoked.

### Q37. What is the key lesson from **Host Isolation**?

**Short answer:** EDR or network isolation can stop communication while preserving state for investigation.

### Q38. What is the key lesson from **Network Block**?

**Short answer:** Firewall, proxy, DNS, or cloud blocks can limit malicious paths while preserving context.

### Q39. What is the key lesson from **Service Disablement**?

**Short answer:** Disabling a vulnerable service may be the safest containment when business impact permits.

### Q40. What is the key lesson from **Evidence Before Reimage**?

**Short answer:** Reimaging too early destroys artifacts needed for scoping and lessons learned.

### Q41. What is the key lesson from **Containment Rollback**?

**Short answer:** Containment actions need owners, rollback criteria, and documentation.

### Q42. What is the key lesson from **Incident Timeline**?

**Short answer:** Maintain a chronological record of detection, evidence, actions, communication, and impact.

### Q43. What is the key lesson from **Decision Log**?

**Short answer:** Record major decisions, alternatives, owner, time, and rationale.

### Q44. What is the key lesson from **Action Log**?

**Short answer:** Record every containment or system change made during handling.

### Q45. What is the key lesson from **Stakeholder Update**?

**Short answer:** Updates should state confirmed facts, impact, actions, risks, and next checkpoint.

### Q46. What is the key lesson from **Status Cadence**?

**Short answer:** Define update frequency based on severity and uncertainty.

### Q47. What is the key lesson from **Handoff**?

**Short answer:** Handoffs should include scope, hypothesis, evidence, containment, and pending actions.

### Q48. What is the key lesson from **Responder Safety**?

**Short answer:** Major incidents create fatigue and error risk; role rotation and handoffs matter.

### Q49. What is the key lesson from **Tabletop Exercise**?

**Short answer:** Tabletops test roles, decisions, communications, and runbooks without technical impact.

### Q50. What is the key lesson from **Incident Runbook**?

**Short answer:** Runbooks define evidence, decisions, actions, escalation, and closure for common scenarios.

### Q51. What is the key lesson from **Phishing Handling**?

**Short answer:** Validate message/user impact, remove malicious content, protect accounts, and search for related messages.

### Q52. What is the key lesson from **Malware Handling**?

**Short answer:** Preserve sample and telemetry, isolate affected systems, and scope related hosts.

### Q53. What is the key lesson from **Account Compromise Handling**?

**Short answer:** Review sign-ins, MFA, tokens, privilege, SaaS changes, and connected hosts.

### Q54. What is the key lesson from **Web Incident Handling**?

**Short answer:** Preserve app/WAF/API logs, identify routes/accounts/data, and coordinate containment.

### Q55. What is the key lesson from **Cloud Incident Handling**?

**Short answer:** Review audit/IAM/network/object logs, revoke credentials, contain resources, and preserve evidence.

### Q56. What is the key lesson from **Lost Device Handling**?

**Short answer:** Revoke sessions, evaluate encryption/MDM, lock/wipe as appropriate, and assess data exposure.

### Q57. What is the key lesson from **Data Exposure Handling**?

**Short answer:** Identify data type, records, users, access path, duration, downloads, and governance implications.

### Q58. What is the key lesson from **DoS Handling**?

**Short answer:** Coordinate provider and edge controls, prioritize critical services, and collect traffic evidence.

### Q59. What is the key lesson from **Insider Incident Awareness**?

**Short answer:** Insider cases require careful HR/legal/privacy coordination and strict evidence handling.

### Q60. What is the key lesson from **Incident Metrics**?

**Short answer:** Measure time to validate, escalate, contain, communicate, and close while preserving quality.

### Q61. What is the key lesson from **Post-Handling Review**?

**Short answer:** Incidents should feed detection, hardening, and process improvements where useful.

## Completion Checklist
- [ ] I completed at least 30 labs.
- [ ] I completed the mini project.
- [ ] I can preserve and document evidence.
- [ ] I can build a cross-source timeline.
- [ ] I can distinguish containment, eradication, and recovery.
- [ ] I can state confidence and limitations.
