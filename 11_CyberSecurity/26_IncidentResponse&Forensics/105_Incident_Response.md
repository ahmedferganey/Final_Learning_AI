# 105. Incident Response

> Phase 26 — Incident Response & Forensics

## 1. Topic Title

**Incident Response**

## 2. Learning Objectives

- Execute preparation, analysis, containment, eradication, recovery, and improvement.
- Coordinate endpoint, identity, network, cloud, application, and business actions.
- Build reliable timelines and scope assessments.
- Preserve evidence while containing active threats.
- Design credential/token/key revocation and trusted recovery.
- Perform lessons learned and corrective action.

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

# Part 1 — Incident Response Purpose

### Core Explanation

Incident response coordinates technical and business actions to contain threats, remove root causes, restore trust, and reduce recurrence.

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

# Part 2 — Preparation

### Core Explanation

Preparation establishes plans, roles, contacts, telemetry, tools, access, backups, and exercises before incidents.

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

# Part 3 — IR Plan

### Core Explanation

An incident-response plan defines governance, roles, severity, communication, evidence, escalation, and lifecycle activities.

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

# Part 4 — IR Team

### Core Explanation

Response combines SOC, endpoint, network, identity, cloud, application, legal/privacy, communications, and business expertise.

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

# Part 5 — Incident Commander

### Core Explanation

A designated lead coordinates priorities, decisions, communications, and workstreams.

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

# Part 6 — Technical Workstream

### Core Explanation

Technical teams scope, contain, investigate, eradicate, and recover affected technology.

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

# Part 7 — Business Workstream

### Core Explanation

Business teams prioritize service restoration and operational impact.

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

# Part 8 — Communications Workstream

### Core Explanation

Communication specialists manage approved internal and external messaging.

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

# Part 9 — Legal / Privacy Workstream

### Core Explanation

Specialists assess contractual, regulatory, privacy, and evidence obligations.

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

# Part 10 — Detection and Analysis

### Core Explanation

Validate malicious activity, reconstruct timeline, determine scope, and identify root cause.

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

# Part 11 — Scope Expansion

### Core Explanation

Search related users, hosts, cloud accounts, network connections, and behaviors to find the true boundary.

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

# Part 12 — Patient Zero

### Core Explanation

The first detected host is not necessarily the first compromised system.

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

# Part 13 — Root Cause

### Core Explanation

Identify the weakness or access path that enabled the incident, not only the final malware or alert.

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

# Part 14 — Initial Access

### Core Explanation

Determine whether access began through credentials, exposed service, application flaw, phishing, supplier, or another path.

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

# Part 15 — Persistence Analysis

### Core Explanation

Identify mechanisms that could restore attacker access after containment.

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

# Part 16 — Privilege Analysis

### Core Explanation

Determine what privileges were obtained and where they were used.

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

# Part 17 — Lateral Movement Analysis

### Core Explanation

Trace movement between systems and identities.

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

# Part 18 — Data Access Analysis

### Core Explanation

Determine what sensitive data was viewed, modified, collected, or transferred.

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

# Part 19 — C2 Analysis

### Core Explanation

Identify external communication used for remote tasking or staging without contacting malicious infrastructure.

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

# Part 20 — Impact Analysis

### Core Explanation

Assess confidentiality, integrity, availability, financial, safety, and business consequences.

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

# Part 21 — Containment Strategy

### Core Explanation

Choose containment that reduces harm while preserving evidence and operational viability.

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

# Part 22 — Account Containment

### Core Explanation

Disable, reset, revoke, restrict, or monitor identities according to evidence.

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

# Part 23 — Endpoint Containment

### Core Explanation

Isolate endpoints while preserving evidence and responder access.

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

# Part 24 — Network Containment

### Core Explanation

Block, segment, sinkhole, or restrict malicious paths while documenting effects.

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

# Part 25 — Cloud Containment

### Core Explanation

Revoke keys/tokens, isolate workloads, change policies, or quarantine resources.

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

# Part 26 — Application Containment

### Core Explanation

Disable vulnerable features, rotate secrets, force logout, or deploy temporary controls.

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

# Part 27 — Email Containment

### Core Explanation

Remove malicious messages, block artifacts, disable forwarding rules, and protect accounts.

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

# Part 28 — Containment Sequencing

### Core Explanation

Coordinate actions so an adversary is not warned prematurely while broader containment is prepared.

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

# Part 29 — Evidence Preservation

### Core Explanation

Collect volatile and persistent evidence needed for scoping, root cause, and lessons before destructive changes.

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

# Part 30 — Eradication

### Core Explanation

Remove malicious artifacts, persistence, unauthorized accounts, exposed credentials, and vulnerable configuration.

### Diagram / Command / Evidence Example

```text
remove persistence → patch entry point → rotate credentials → remove unauthorized accounts → validate clean state
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

# Part 31 — Patch Entry Point

### Core Explanation

Fix the vulnerability or misconfiguration that enabled access.

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

# Part 32 — Credential Rotation

### Core Explanation

Rotate passwords, keys, tokens, certificates, API secrets, and service credentials according to exposure.

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

# Part 33 — Remove Persistence

### Core Explanation

Remove tasks, services, startup artifacts, cloud persistence, OAuth grants, and unauthorized mechanisms.

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

# Part 34 — Rebuild vs Clean

### Core Explanation

Rebuilding from trusted images may provide stronger assurance than attempting to clean deeply compromised systems.

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

# Part 35 — Golden Image

### Core Explanation

Trusted base images support consistent restoration after endpoint or server compromise.

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

# Part 36 — Recovery

### Core Explanation

Restore systems and services to a known trustworthy state and monitor closely.

### Diagram / Command / Evidence Example

```text
trusted restore → validate controls → heightened monitoring → staged return → business verification
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

# Part 37 — Recovery Validation

### Core Explanation

Validate security controls, configuration, integrity, dependencies, identity, and business function.

### Diagram / Command / Evidence Example

```text
trusted restore → validate controls → heightened monitoring → staged return → business verification
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

# Part 38 — Staged Recovery

### Core Explanation

Restore critical services in phases so recurrence is detected before broad reintroduction.

### Diagram / Command / Evidence Example

```text
trusted restore → validate controls → heightened monitoring → staged return → business verification
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

# Part 39 — Heightened Monitoring

### Core Explanation

Increase monitoring after recovery for re-entry, persistence, or failed cleanup.

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

# Part 40 — Business Acceptance

### Core Explanation

Business owners confirm critical workflows operate correctly after technical recovery.

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

# Part 41 — Backup Restore

### Core Explanation

Use tested clean backups and ensure the backup path was not compromised.

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

# Part 42 — Backup Integrity

### Core Explanation

Validate backup provenance, timestamps, and malicious persistence risk.

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

# Part 43 — RPO / RTO

### Core Explanation

Recovery point and recovery time objectives guide acceptable data loss and restoration timing.

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

# Part 44 — Ransomware Response Awareness

### Core Explanation

Contain affected systems, protect backups, preserve evidence, scope identity, and coordinate recovery.

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

# Part 45 — Cloud Account Compromise

### Core Explanation

Revoke sessions and keys, review IAM changes, preserve audit logs, rotate trust, and validate resources.

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

# Part 46 — Active Directory IR

### Core Explanation

Protect domain controllers, privileged identities, replication rights, GPOs, trusts, and credentials.

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

# Part 47 — Web Application IR

### Core Explanation

Preserve app/WAF/API logs, protect data, disable vulnerable functionality, rotate secrets, and deploy fixes.

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

# Part 48 — Supply Chain IR

### Core Explanation

Identify affected builds/components, stop promotion, preserve provenance, rotate credentials, and rebuild trusted artifacts.

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

# Part 49 — Insider IR Awareness

### Core Explanation

Coordinate evidence and response with HR/legal/privacy while minimizing unnecessary employee-data access.

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

# Part 50 — Incident Timeline

### Core Explanation

Build a normalized timeline across endpoint, identity, network, cloud, application, and communications.

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

# Part 51 — Evidence Matrix

### Core Explanation

Track which evidence source supports each important conclusion.

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

# Part 52 — Confidence Statement

### Core Explanation

Distinguish confirmed facts from likely or possible interpretations.

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

# Part 53 — IOC Sweep

### Core Explanation

Search for confirmed artifacts across current and historical telemetry while considering indicator lifetime.

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

# Part 54 — Behavior Sweep

### Core Explanation

Search for attacker behavior and relationships beyond exact indicators.

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

# Part 55 — Retro Hunt

### Core Explanation

Use new findings to search earlier data for pre-detection activity.

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

# Part 56 — Threat Intelligence Integration

### Core Explanation

Use CTI to understand related infrastructure, malware, techniques, and exploitation patterns.

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

# Part 57 — Forensics Integration

### Core Explanation

Use disk, memory, network, and cloud evidence when normal telemetry cannot answer key questions.

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

# Part 58 — Malware Analysis Integration

### Core Explanation

Analyze suspicious binaries to understand behavior, persistence, network, and detection opportunities.

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

# Part 59 — Stakeholder Communication

### Core Explanation

Communicate confirmed facts, risk, current actions, decisions needed, and next update time.

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

# Part 60 — Executive Briefing

### Core Explanation

Leadership needs impact, scope, business implications, uncertainty, containment status, and decisions.

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

# Part 61 — External Communication Awareness

### Core Explanation

Customer or partner messages should use approved legal and communications processes.

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

# Part 62 — Decision Log

### Core Explanation

Preserve major response decisions and rationale.

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

# Part 63 — Action Tracking

### Core Explanation

Every containment, eradication, and recovery action should have owner, time, and verification.

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

# Part 64 — Out-of-Band Communication

### Core Explanation

Maintain alternatives if corporate identity, email, or chat is compromised.

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

# Part 65 — Responder Access

### Core Explanation

Use protected response accounts with strong authentication and logging.

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

# Part 66 — IR Tooling

### Core Explanation

Maintain trusted collection, remote response, forensic, EDR, cloud, and communication tools.

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

# Part 67 — Playbook

### Core Explanation

Scenario playbooks accelerate repeatable actions while preserving decision points.

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

# Part 68 — Tabletop

### Core Explanation

Tabletops validate people, communication, and decisions.

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

# Part 69 — Technical Exercise

### Core Explanation

Controlled simulations validate telemetry, containment, access, and recovery tools.

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

# Part 70 — Lessons Learned

### Core Explanation

Post-incident review examines root cause, detection, response, recovery, communication, and systemic improvements.

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

# Part 71 — Corrective Action

### Core Explanation

Assign owners and deadlines so lessons learned become real change.

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

# Part 72 — Detection Improvement

### Core Explanation

Turn incident behaviors into better analytics and data coverage.

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

# Part 73 — Hardening Improvement

### Core Explanation

Reduce exposed services, privilege, attack surface, or insecure workflows.

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

# Part 74 — Architecture Improvement

### Core Explanation

Major incidents may justify redesign of identity, segmentation, backup, SaaS, or applications.

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

# Part 75 — Training Improvement

### Core Explanation

Update analyst, engineering, admin, and user training based on observed failure modes.

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

# Part 76 — Metric Review

### Core Explanation

Use metrics to improve preparation and process rather than reward superficial speed.

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

## Lab 1 — Incident Response Purpose

### Objective
Practice **Incident Response Purpose** using a synthetic incident or authorized evidence.

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

## Lab 2 — Preparation

### Objective
Practice **Preparation** using a synthetic incident or authorized evidence.

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

## Lab 3 — IR Plan

### Objective
Practice **IR Plan** using a synthetic incident or authorized evidence.

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

## Lab 4 — IR Team

### Objective
Practice **IR Team** using a synthetic incident or authorized evidence.

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

## Lab 5 — Incident Commander

### Objective
Practice **Incident Commander** using a synthetic incident or authorized evidence.

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

## Lab 6 — Technical Workstream

### Objective
Practice **Technical Workstream** using a synthetic incident or authorized evidence.

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

## Lab 7 — Business Workstream

### Objective
Practice **Business Workstream** using a synthetic incident or authorized evidence.

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

## Lab 8 — Communications Workstream

### Objective
Practice **Communications Workstream** using a synthetic incident or authorized evidence.

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

## Lab 9 — Legal / Privacy Workstream

### Objective
Practice **Legal / Privacy Workstream** using a synthetic incident or authorized evidence.

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

## Lab 10 — Detection and Analysis

### Objective
Practice **Detection and Analysis** using a synthetic incident or authorized evidence.

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

## Lab 11 — Scope Expansion

### Objective
Practice **Scope Expansion** using a synthetic incident or authorized evidence.

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

## Lab 12 — Patient Zero

### Objective
Practice **Patient Zero** using a synthetic incident or authorized evidence.

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

## Lab 13 — Root Cause

### Objective
Practice **Root Cause** using a synthetic incident or authorized evidence.

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

## Lab 14 — Initial Access

### Objective
Practice **Initial Access** using a synthetic incident or authorized evidence.

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

## Lab 15 — Persistence Analysis

### Objective
Practice **Persistence Analysis** using a synthetic incident or authorized evidence.

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

## Lab 16 — Privilege Analysis

### Objective
Practice **Privilege Analysis** using a synthetic incident or authorized evidence.

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

## Lab 17 — Lateral Movement Analysis

### Objective
Practice **Lateral Movement Analysis** using a synthetic incident or authorized evidence.

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

## Lab 18 — Data Access Analysis

### Objective
Practice **Data Access Analysis** using a synthetic incident or authorized evidence.

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

## Lab 19 — C2 Analysis

### Objective
Practice **C2 Analysis** using a synthetic incident or authorized evidence.

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

## Lab 20 — Impact Analysis

### Objective
Practice **Impact Analysis** using a synthetic incident or authorized evidence.

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

## Lab 21 — Containment Strategy

### Objective
Practice **Containment Strategy** using a synthetic incident or authorized evidence.

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

## Lab 22 — Account Containment

### Objective
Practice **Account Containment** using a synthetic incident or authorized evidence.

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

## Lab 23 — Endpoint Containment

### Objective
Practice **Endpoint Containment** using a synthetic incident or authorized evidence.

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

## Lab 24 — Network Containment

### Objective
Practice **Network Containment** using a synthetic incident or authorized evidence.

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

## Lab 25 — Cloud Containment

### Objective
Practice **Cloud Containment** using a synthetic incident or authorized evidence.

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

## Lab 26 — Application Containment

### Objective
Practice **Application Containment** using a synthetic incident or authorized evidence.

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

## Lab 27 — Email Containment

### Objective
Practice **Email Containment** using a synthetic incident or authorized evidence.

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

## Lab 28 — Containment Sequencing

### Objective
Practice **Containment Sequencing** using a synthetic incident or authorized evidence.

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

## Lab 29 — Evidence Preservation

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

## Lab 30 — Eradication

### Objective
Practice **Eradication** using a synthetic incident or authorized evidence.

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
remove persistence → patch entry point → rotate credentials → remove unauthorized accounts → validate clean state
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

## Lab 31 — Patch Entry Point

### Objective
Practice **Patch Entry Point** using a synthetic incident or authorized evidence.

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

## Lab 32 — Credential Rotation

### Objective
Practice **Credential Rotation** using a synthetic incident or authorized evidence.

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

## Lab 33 — Remove Persistence

### Objective
Practice **Remove Persistence** using a synthetic incident or authorized evidence.

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

## Lab 34 — Rebuild vs Clean

### Objective
Practice **Rebuild vs Clean** using a synthetic incident or authorized evidence.

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

## Lab 35 — Golden Image

### Objective
Practice **Golden Image** using a synthetic incident or authorized evidence.

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

## Lab 36 — Recovery

### Objective
Practice **Recovery** using a synthetic incident or authorized evidence.

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
trusted restore → validate controls → heightened monitoring → staged return → business verification
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

## Lab 37 — Recovery Validation

### Objective
Practice **Recovery Validation** using a synthetic incident or authorized evidence.

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
trusted restore → validate controls → heightened monitoring → staged return → business verification
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

## Lab 38 — Staged Recovery

### Objective
Practice **Staged Recovery** using a synthetic incident or authorized evidence.

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
trusted restore → validate controls → heightened monitoring → staged return → business verification
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

## Lab 39 — Heightened Monitoring

### Objective
Practice **Heightened Monitoring** using a synthetic incident or authorized evidence.

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

## Lab 40 — Business Acceptance

### Objective
Practice **Business Acceptance** using a synthetic incident or authorized evidence.

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

## Lab 41 — Backup Restore

### Objective
Practice **Backup Restore** using a synthetic incident or authorized evidence.

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

## Lab 42 — Backup Integrity

### Objective
Practice **Backup Integrity** using a synthetic incident or authorized evidence.

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

## Lab 43 — RPO / RTO

### Objective
Practice **RPO / RTO** using a synthetic incident or authorized evidence.

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

## Lab 44 — Ransomware Response Awareness

### Objective
Practice **Ransomware Response Awareness** using a synthetic incident or authorized evidence.

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

## Lab 45 — Cloud Account Compromise

### Objective
Practice **Cloud Account Compromise** using a synthetic incident or authorized evidence.

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

## Lab 46 — Active Directory IR

### Objective
Practice **Active Directory IR** using a synthetic incident or authorized evidence.

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

## Lab 47 — Web Application IR

### Objective
Practice **Web Application IR** using a synthetic incident or authorized evidence.

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

## Lab 48 — Supply Chain IR

### Objective
Practice **Supply Chain IR** using a synthetic incident or authorized evidence.

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

## Lab 49 — Insider IR Awareness

### Objective
Practice **Insider IR Awareness** using a synthetic incident or authorized evidence.

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

## Lab 50 — Incident Timeline

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

## Lab 51 — Evidence Matrix

### Objective
Practice **Evidence Matrix** using a synthetic incident or authorized evidence.

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

## Lab 52 — Confidence Statement

### Objective
Practice **Confidence Statement** using a synthetic incident or authorized evidence.

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

## Lab 53 — IOC Sweep

### Objective
Practice **IOC Sweep** using a synthetic incident or authorized evidence.

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

## Lab 54 — Behavior Sweep

### Objective
Practice **Behavior Sweep** using a synthetic incident or authorized evidence.

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

## Lab 55 — Retro Hunt

### Objective
Practice **Retro Hunt** using a synthetic incident or authorized evidence.

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

# Mini Project — End-to-End Incident Response Exercise

Run a synthetic incident involving a compromised cloud identity and one endpoint. Build timeline, scope, evidence matrix, containment plan, credential/token rotation, endpoint/network actions, eradication, staged recovery, heightened monitoring, stakeholder briefings, lessons learned, and corrective actions.

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
- MITRE ATT&CK — https://attack.mitre.org/

## 8. Certification Relevance

Relevant to incident responder, DFIR, SOC lead, cloud incident response, and blue-team leadership.

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

### Q1. What is the key lesson from **Incident Response Purpose**?

**Short answer:** Incident response coordinates technical and business actions to contain threats, remove root causes, restore trust, and reduce recurrence.

### Q2. What is the key lesson from **Preparation**?

**Short answer:** Preparation establishes plans, roles, contacts, telemetry, tools, access, backups, and exercises before incidents.

### Q3. What is the key lesson from **IR Plan**?

**Short answer:** An incident-response plan defines governance, roles, severity, communication, evidence, escalation, and lifecycle activities.

### Q4. What is the key lesson from **IR Team**?

**Short answer:** Response combines SOC, endpoint, network, identity, cloud, application, legal/privacy, communications, and business expertise.

### Q5. What is the key lesson from **Incident Commander**?

**Short answer:** A designated lead coordinates priorities, decisions, communications, and workstreams.

### Q6. What is the key lesson from **Technical Workstream**?

**Short answer:** Technical teams scope, contain, investigate, eradicate, and recover affected technology.

### Q7. What is the key lesson from **Business Workstream**?

**Short answer:** Business teams prioritize service restoration and operational impact.

### Q8. What is the key lesson from **Communications Workstream**?

**Short answer:** Communication specialists manage approved internal and external messaging.

### Q9. What is the key lesson from **Legal / Privacy Workstream**?

**Short answer:** Specialists assess contractual, regulatory, privacy, and evidence obligations.

### Q10. What is the key lesson from **Detection and Analysis**?

**Short answer:** Validate malicious activity, reconstruct timeline, determine scope, and identify root cause.

### Q11. What is the key lesson from **Scope Expansion**?

**Short answer:** Search related users, hosts, cloud accounts, network connections, and behaviors to find the true boundary.

### Q12. What is the key lesson from **Patient Zero**?

**Short answer:** The first detected host is not necessarily the first compromised system.

### Q13. What is the key lesson from **Root Cause**?

**Short answer:** Identify the weakness or access path that enabled the incident, not only the final malware or alert.

### Q14. What is the key lesson from **Initial Access**?

**Short answer:** Determine whether access began through credentials, exposed service, application flaw, phishing, supplier, or another path.

### Q15. What is the key lesson from **Persistence Analysis**?

**Short answer:** Identify mechanisms that could restore attacker access after containment.

### Q16. What is the key lesson from **Privilege Analysis**?

**Short answer:** Determine what privileges were obtained and where they were used.

### Q17. What is the key lesson from **Lateral Movement Analysis**?

**Short answer:** Trace movement between systems and identities.

### Q18. What is the key lesson from **Data Access Analysis**?

**Short answer:** Determine what sensitive data was viewed, modified, collected, or transferred.

### Q19. What is the key lesson from **C2 Analysis**?

**Short answer:** Identify external communication used for remote tasking or staging without contacting malicious infrastructure.

### Q20. What is the key lesson from **Impact Analysis**?

**Short answer:** Assess confidentiality, integrity, availability, financial, safety, and business consequences.

### Q21. What is the key lesson from **Containment Strategy**?

**Short answer:** Choose containment that reduces harm while preserving evidence and operational viability.

### Q22. What is the key lesson from **Account Containment**?

**Short answer:** Disable, reset, revoke, restrict, or monitor identities according to evidence.

### Q23. What is the key lesson from **Endpoint Containment**?

**Short answer:** Isolate endpoints while preserving evidence and responder access.

### Q24. What is the key lesson from **Network Containment**?

**Short answer:** Block, segment, sinkhole, or restrict malicious paths while documenting effects.

### Q25. What is the key lesson from **Cloud Containment**?

**Short answer:** Revoke keys/tokens, isolate workloads, change policies, or quarantine resources.

### Q26. What is the key lesson from **Application Containment**?

**Short answer:** Disable vulnerable features, rotate secrets, force logout, or deploy temporary controls.

### Q27. What is the key lesson from **Email Containment**?

**Short answer:** Remove malicious messages, block artifacts, disable forwarding rules, and protect accounts.

### Q28. What is the key lesson from **Containment Sequencing**?

**Short answer:** Coordinate actions so an adversary is not warned prematurely while broader containment is prepared.

### Q29. What is the key lesson from **Evidence Preservation**?

**Short answer:** Collect volatile and persistent evidence needed for scoping, root cause, and lessons before destructive changes.

### Q30. What is the key lesson from **Eradication**?

**Short answer:** Remove malicious artifacts, persistence, unauthorized accounts, exposed credentials, and vulnerable configuration.

### Q31. What is the key lesson from **Patch Entry Point**?

**Short answer:** Fix the vulnerability or misconfiguration that enabled access.

### Q32. What is the key lesson from **Credential Rotation**?

**Short answer:** Rotate passwords, keys, tokens, certificates, API secrets, and service credentials according to exposure.

### Q33. What is the key lesson from **Remove Persistence**?

**Short answer:** Remove tasks, services, startup artifacts, cloud persistence, OAuth grants, and unauthorized mechanisms.

### Q34. What is the key lesson from **Rebuild vs Clean**?

**Short answer:** Rebuilding from trusted images may provide stronger assurance than attempting to clean deeply compromised systems.

### Q35. What is the key lesson from **Golden Image**?

**Short answer:** Trusted base images support consistent restoration after endpoint or server compromise.

### Q36. What is the key lesson from **Recovery**?

**Short answer:** Restore systems and services to a known trustworthy state and monitor closely.

### Q37. What is the key lesson from **Recovery Validation**?

**Short answer:** Validate security controls, configuration, integrity, dependencies, identity, and business function.

### Q38. What is the key lesson from **Staged Recovery**?

**Short answer:** Restore critical services in phases so recurrence is detected before broad reintroduction.

### Q39. What is the key lesson from **Heightened Monitoring**?

**Short answer:** Increase monitoring after recovery for re-entry, persistence, or failed cleanup.

### Q40. What is the key lesson from **Business Acceptance**?

**Short answer:** Business owners confirm critical workflows operate correctly after technical recovery.

### Q41. What is the key lesson from **Backup Restore**?

**Short answer:** Use tested clean backups and ensure the backup path was not compromised.

### Q42. What is the key lesson from **Backup Integrity**?

**Short answer:** Validate backup provenance, timestamps, and malicious persistence risk.

### Q43. What is the key lesson from **RPO / RTO**?

**Short answer:** Recovery point and recovery time objectives guide acceptable data loss and restoration timing.

### Q44. What is the key lesson from **Ransomware Response Awareness**?

**Short answer:** Contain affected systems, protect backups, preserve evidence, scope identity, and coordinate recovery.

### Q45. What is the key lesson from **Cloud Account Compromise**?

**Short answer:** Revoke sessions and keys, review IAM changes, preserve audit logs, rotate trust, and validate resources.

### Q46. What is the key lesson from **Active Directory IR**?

**Short answer:** Protect domain controllers, privileged identities, replication rights, GPOs, trusts, and credentials.

### Q47. What is the key lesson from **Web Application IR**?

**Short answer:** Preserve app/WAF/API logs, protect data, disable vulnerable functionality, rotate secrets, and deploy fixes.

### Q48. What is the key lesson from **Supply Chain IR**?

**Short answer:** Identify affected builds/components, stop promotion, preserve provenance, rotate credentials, and rebuild trusted artifacts.

### Q49. What is the key lesson from **Insider IR Awareness**?

**Short answer:** Coordinate evidence and response with HR/legal/privacy while minimizing unnecessary employee-data access.

### Q50. What is the key lesson from **Incident Timeline**?

**Short answer:** Build a normalized timeline across endpoint, identity, network, cloud, application, and communications.

### Q51. What is the key lesson from **Evidence Matrix**?

**Short answer:** Track which evidence source supports each important conclusion.

### Q52. What is the key lesson from **Confidence Statement**?

**Short answer:** Distinguish confirmed facts from likely or possible interpretations.

### Q53. What is the key lesson from **IOC Sweep**?

**Short answer:** Search for confirmed artifacts across current and historical telemetry while considering indicator lifetime.

### Q54. What is the key lesson from **Behavior Sweep**?

**Short answer:** Search for attacker behavior and relationships beyond exact indicators.

### Q55. What is the key lesson from **Retro Hunt**?

**Short answer:** Use new findings to search earlier data for pre-detection activity.

### Q56. What is the key lesson from **Threat Intelligence Integration**?

**Short answer:** Use CTI to understand related infrastructure, malware, techniques, and exploitation patterns.

### Q57. What is the key lesson from **Forensics Integration**?

**Short answer:** Use disk, memory, network, and cloud evidence when normal telemetry cannot answer key questions.

### Q58. What is the key lesson from **Malware Analysis Integration**?

**Short answer:** Analyze suspicious binaries to understand behavior, persistence, network, and detection opportunities.

### Q59. What is the key lesson from **Stakeholder Communication**?

**Short answer:** Communicate confirmed facts, risk, current actions, decisions needed, and next update time.

### Q60. What is the key lesson from **Executive Briefing**?

**Short answer:** Leadership needs impact, scope, business implications, uncertainty, containment status, and decisions.

### Q61. What is the key lesson from **External Communication Awareness**?

**Short answer:** Customer or partner messages should use approved legal and communications processes.

### Q62. What is the key lesson from **Decision Log**?

**Short answer:** Preserve major response decisions and rationale.

### Q63. What is the key lesson from **Action Tracking**?

**Short answer:** Every containment, eradication, and recovery action should have owner, time, and verification.

### Q64. What is the key lesson from **Out-of-Band Communication**?

**Short answer:** Maintain alternatives if corporate identity, email, or chat is compromised.

### Q65. What is the key lesson from **Responder Access**?

**Short answer:** Use protected response accounts with strong authentication and logging.

### Q66. What is the key lesson from **IR Tooling**?

**Short answer:** Maintain trusted collection, remote response, forensic, EDR, cloud, and communication tools.

### Q67. What is the key lesson from **Playbook**?

**Short answer:** Scenario playbooks accelerate repeatable actions while preserving decision points.

### Q68. What is the key lesson from **Tabletop**?

**Short answer:** Tabletops validate people, communication, and decisions.

### Q69. What is the key lesson from **Technical Exercise**?

**Short answer:** Controlled simulations validate telemetry, containment, access, and recovery tools.

### Q70. What is the key lesson from **Lessons Learned**?

**Short answer:** Post-incident review examines root cause, detection, response, recovery, communication, and systemic improvements.

### Q71. What is the key lesson from **Corrective Action**?

**Short answer:** Assign owners and deadlines so lessons learned become real change.

### Q72. What is the key lesson from **Detection Improvement**?

**Short answer:** Turn incident behaviors into better analytics and data coverage.

### Q73. What is the key lesson from **Hardening Improvement**?

**Short answer:** Reduce exposed services, privilege, attack surface, or insecure workflows.

### Q74. What is the key lesson from **Architecture Improvement**?

**Short answer:** Major incidents may justify redesign of identity, segmentation, backup, SaaS, or applications.

### Q75. What is the key lesson from **Training Improvement**?

**Short answer:** Update analyst, engineering, admin, and user training based on observed failure modes.

### Q76. What is the key lesson from **Metric Review**?

**Short answer:** Use metrics to improve preparation and process rather than reward superficial speed.

## Completion Checklist
- [ ] I completed at least 30 labs.
- [ ] I completed the mini project.
- [ ] I can preserve and document evidence.
- [ ] I can build a cross-source timeline.
- [ ] I can distinguish containment, eradication, and recovery.
- [ ] I can state confidence and limitations.
