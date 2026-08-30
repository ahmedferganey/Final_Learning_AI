# 107. Network Forensics

> Phase 26 — Incident Response & Forensics

## 1. Topic Title

**Network Forensics**

## 2. Learning Objectives

- Preserve and analyze PCAP, flow, DNS, firewall, proxy, VPN, and sensor evidence.
- Use tcpdump, Wireshark, and Zeek concepts to reconstruct activity.
- Analyze DNS, HTTP, TLS metadata, sessions, flows, and beacon-like behavior.
- Correlate network evidence with endpoint and identity timelines.
- Document limitations caused by encryption, packet loss, NAT, and missing sensors.

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

# Part 1 — Network Forensics Purpose

### Core Explanation

Network forensics preserves and analyzes packet, flow, DNS, firewall, proxy, VPN, and sensor telemetry to reconstruct network activity.

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

# Part 2 — Network Evidence Sources

### Core Explanation

Common sources include PCAP, NetFlow/IPFIX, Zeek, firewall, DNS, DHCP, proxy, VPN, IDS/IPS, NDR, and cloud flow logs.

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

# Part 3 — Packet Capture

### Core Explanation

PCAP records individual packets and may contain detailed payload and protocol evidence.

### Diagram / Command / Evidence Example

```bash
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

# Part 4 — Full Packet Capture

### Core Explanation

Full capture offers rich evidence but creates storage, privacy, and access-control challenges.

### Diagram / Command / Evidence Example

```bash
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

# Part 5 — Capture Point

### Core Explanation

Sensor placement determines which traffic direction, NAT state, and segments are visible.

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

# Part 6 — SPAN Port

### Core Explanation

Switch mirroring can copy traffic to sensors but may drop packets under load.

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

# Part 7 — Network TAP

### Core Explanation

A TAP can provide dedicated traffic copies depending on design.

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

# Part 8 — Packet Loss

### Core Explanation

Dropped capture packets create uncertainty and can break session reconstruction.

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

# Part 9 — Capture Filter

### Core Explanation

Capture filters reduce what is stored at collection time.

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

# Part 10 — Display Filter

### Core Explanation

Display filters select what is shown from an existing capture.

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

# Part 11 — tcpdump

### Core Explanation

tcpdump captures and filters authorized network traffic.

### Diagram / Command / Evidence Example

```bash
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

# Part 12 — Wireshark

### Core Explanation

Wireshark decodes protocols and supports filtering and stream reconstruction.

### Diagram / Command / Evidence Example

```text
Wireshark filters: dns | http | tls | tcp.flags.syn == 1 | ip.addr == 192.0.2.10
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

# Part 13 — TShark Awareness

### Core Explanation

TShark provides command-line Wireshark analysis for automation.

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

# Part 14 — Ethernet Evidence

### Core Explanation

Layer-2 frames reveal MAC, VLAN, and local-segment context.

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

# Part 15 — ARP Evidence

### Core Explanation

ARP can help map IPv4-to-MAC relationships on local networks.

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

# Part 16 — IPv4 Evidence

### Core Explanation

IPv4 headers provide source, destination, fragmentation, TTL, and protocol context.

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

# Part 17 — IPv6 Evidence

### Core Explanation

IPv6 analysis includes addresses, extension headers, and neighbor behavior.

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

# Part 18 — TCP Evidence

### Core Explanation

TCP sequence, flags, ports, retransmissions, and state help reconstruct sessions.

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

# Part 19 — UDP Evidence

### Core Explanation

UDP lacks connection state and requires protocol context.

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

# Part 20 — ICMP Evidence

### Core Explanation

ICMP reveals reachability, errors, scanning, and path behavior.

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

# Part 21 — TCP Handshake

### Core Explanation

SYN, SYN/ACK, ACK establish a normal TCP connection and identify attempts.

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

# Part 22 — TCP Reset

### Core Explanation

RST packets can indicate closed services, application resets, firewall behavior, or disruption.

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

# Part 23 — Retransmission

### Core Explanation

Retransmissions may indicate loss, congestion, or asymmetric capture rather than attacks.

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

# Part 24 — 5-Tuple

### Core Explanation

Source IP, destination IP, source port, destination port, and protocol identify a flow.

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

# Part 25 — Flow Record

### Core Explanation

Flow telemetry summarizes connection metadata without full payload.

### Diagram / Command / Evidence Example

```text
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

# Part 26 — NetFlow

### Core Explanation

NetFlow-style records support large-scale relationship and volume analysis.

### Diagram / Command / Evidence Example

```text
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

# Part 27 — IPFIX

### Core Explanation

IPFIX is a standardized extensible flow-export format.

### Diagram / Command / Evidence Example

```text
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

# Part 28 — Flow Direction

### Core Explanation

Exporter location and direction determine how source and destination should be interpreted.

### Diagram / Command / Evidence Example

```text
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

# Part 29 — NAT Awareness

### Core Explanation

NAT changes visible addresses and ports and requires mapping logs for attribution.

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

# Part 30 — DHCP Correlation

### Core Explanation

DHCP data maps changing IP addresses to devices over time.

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

# Part 31 — VPN Correlation

### Core Explanation

VPN logs map remote users to assigned internal addresses and sessions.

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

# Part 32 — DNS Evidence

### Core Explanation

DNS queries and answers reveal domains, resolution paths, failures, and timing.

### Diagram / Command / Evidence Example

```text
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

# Part 33 — DNS Query Types

### Core Explanation

A, AAAA, MX, TXT, SRV, and other types provide protocol context.

### Diagram / Command / Evidence Example

```text
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

# Part 34 — NXDOMAIN

### Core Explanation

Repeated failed queries can indicate malware, misconfiguration, or algorithmic domain generation.

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

# Part 35 — DNS Tunneling Awareness

### Core Explanation

Unusual encoded or high-volume queries can suggest tunneling but require validation.

### Diagram / Command / Evidence Example

```text
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

# Part 36 — HTTP Evidence

### Core Explanation

HTTP requests reveal methods, hosts, paths, headers, status, types, and user agents when visible.

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

# Part 37 — HTTP User-Agent

### Core Explanation

User agents can support client identification but are easy to spoof.

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

# Part 38 — HTTP Upload Awareness

### Core Explanation

Large POST/PUT bodies or unusual endpoints can support exfiltration investigations.

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

# Part 39 — Proxy Logs

### Core Explanation

Proxy telemetry provides user, URL, category, method, action, bytes, and policy context.

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

# Part 40 — TLS Evidence

### Core Explanation

Encryption hides payload but endpoints, certificates, SNI, timing, and flow remain useful.

### Diagram / Command / Evidence Example

```text
TLS metadata: endpoints | SNI | certificate | version | timing | bytes
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

# Part 41 — SNI

### Core Explanation

Server Name Indication can reveal the intended hostname when present and visible.

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

# Part 42 — TLS Certificate

### Core Explanation

Certificate subject, issuer, validity, fingerprints, and SANs support infrastructure analysis.

### Diagram / Command / Evidence Example

```text
TLS metadata: endpoints | SNI | certificate | version | timing | bytes
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

# Part 43 — JA3 / JA4 Awareness

### Core Explanation

TLS/client fingerprints can support clustering but are not unique identities.

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

# Part 44 — QUIC / HTTP3 Awareness

### Core Explanation

QUIC encrypts more transport metadata and requires updated tooling and assumptions.

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

# Part 45 — SMB Evidence

### Core Explanation

SMB traffic/logs can reveal file access, authentication, and lateral administration.

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

# Part 46 — RDP Evidence

### Core Explanation

RDP can be correlated through network, gateway, Windows, and identity logs.

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

# Part 47 — SSH Evidence

### Core Explanation

SSH payload is encrypted but connection timing and server logs remain useful.

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

# Part 48 — SMTP Evidence

### Core Explanation

Mail transport metadata supports phishing and message-path investigations.

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

# Part 49 — Zeek

### Core Explanation

Zeek converts network activity into structured protocol logs.

### Diagram / Command / Evidence Example

```text
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

# Part 50 — Zeek conn.log

### Core Explanation

Connection logs summarize sessions and state.

### Diagram / Command / Evidence Example

```text
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

# Part 51 — Zeek dns.log

### Core Explanation

DNS logs provide query, answer, type, and response context.

### Diagram / Command / Evidence Example

```text
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

# Part 52 — Zeek http.log

### Core Explanation

HTTP logs provide request and response metadata when visible.

### Diagram / Command / Evidence Example

```text
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

# Part 53 — Zeek ssl.log

### Core Explanation

TLS logs provide certificates, versions, SNI, and session metadata.

### Diagram / Command / Evidence Example

```text
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

# Part 54 — Zeek files.log

### Core Explanation

File metadata can connect transferred files to sessions where configured.

### Diagram / Command / Evidence Example

```text
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

# Part 55 — IDS Alerts

### Core Explanation

IDS/IPS alerts should be correlated with underlying traffic and endpoint context.

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

# Part 56 — NDR Evidence

### Core Explanation

NDR findings provide behavioral relationships but require validation.

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

# Part 57 — Firewall Evidence

### Core Explanation

Firewall logs provide policy decisions, NAT, zones, rule IDs, sessions, and application classification.

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

# Part 58 — Cloud Flow Logs

### Core Explanation

Cloud flow logs show virtual-network traffic and policy outcomes.

### Diagram / Command / Evidence Example

```text
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

# Part 59 — Load Balancer Logs

### Core Explanation

Load-balancer logs reveal client requests, TLS, target response, and backend routing.

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

# Part 60 — WAF Logs

### Core Explanation

WAF telemetry provides rule matches and HTTP request context.

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

# Part 61 — API Gateway Logs

### Core Explanation

API gateways provide route, client, token, response, latency, and quota evidence.

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

# Part 62 — Beaconing

### Core Explanation

Repeated low-volume connections at regular intervals can suggest command-and-control-like behavior.

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

# Part 63 — Beacon Interval

### Core Explanation

Measure timing variation instead of assuming perfectly regular intervals.

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

# Part 64 — Rare Destination

### Core Explanation

New or low-prevalence destinations are useful pivots with process and asset context.

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

# Part 65 — Fan-Out

### Core Explanation

One host connecting to many destinations may indicate discovery, admin activity, or scanning.

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

# Part 66 — Fan-In

### Core Explanation

Many sources connecting to one destination may reflect normal service use or attack traffic.

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

# Part 67 — Lateral Movement

### Core Explanation

Correlate remote-service connections with authentication and endpoint events.

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

# Part 68 — Exfiltration

### Core Explanation

Look for unusual outbound volume, destinations, archives, cloud uploads, or protocol use.

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

# Part 69 — Data Volume Baseline

### Core Explanation

Volume anomalies require comparison with expected user and service behavior.

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

# Part 70 — Session Reconstruction

### Core Explanation

Reconstruct ordered conversations using connection state and payload when available and authorized.

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

# Part 71 — TCP Stream

### Core Explanation

Wireshark can reconstruct streams when capture completeness permits.

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

# Part 72 — File Carving Awareness

### Core Explanation

Files may be recovered from unencrypted traffic in authorized investigations.

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

# Part 73 — Encrypted Traffic Limitation

### Core Explanation

Encryption limits payload analysis and increases dependence on endpoint/proxy/app context.

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

# Part 74 — Asymmetric Capture

### Core Explanation

Seeing only one direction can make sessions appear incomplete.

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

# Part 75 — Packet Timestamp

### Core Explanation

Sensor clock accuracy affects event ordering.

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

# Part 76 — PCAP Integrity

### Core Explanation

Hash and protect captures used as formal evidence.

### Diagram / Command / Evidence Example

```bash
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

# Part 77 — Evidence Minimization

### Core Explanation

Captures can contain unrelated sensitive traffic and should be scoped carefully.

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

# Part 78 — Timeline

### Core Explanation

Normalize packet, flow, DNS, firewall, proxy, VPN, endpoint, and identity evidence.

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

# Part 79 — Host Pivot

### Core Explanation

Start from a host and enumerate destinations, protocols, users, and time windows.

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

# Part 80 — Domain Pivot

### Core Explanation

Start from a domain and identify clients, answers, IPs, processes, and sightings.

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

# Part 81 — IP Pivot

### Core Explanation

Investigate hosts and users that communicated with an address and map NAT/VPN identity.

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

# Part 82 — Session Pivot

### Core Explanation

Use one connection to locate related process, user, DNS, proxy, or endpoint evidence.

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

# Part 83 — Network IOC

### Core Explanation

Domains, IPs, URLs, certificates, and protocol artifacts can support scoping with context.

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

# Part 84 — Behavioral Network Indicator

### Core Explanation

Connection pattern, timing, protocol misuse, or relationships can outlast infrastructure indicators.

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

# Part 85 — Network Forensics Report

### Core Explanation

Report sources, sensor gaps, timeline, sessions, indicators, confidence, and limitations.

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

## Lab 1 — Network Forensics Purpose

### Objective
Practice **Network Forensics Purpose** using a synthetic incident or authorized evidence.

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

## Lab 2 — Network Evidence Sources

### Objective
Practice **Network Evidence Sources** using a synthetic incident or authorized evidence.

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

## Lab 3 — Packet Capture

### Objective
Practice **Packet Capture** using a synthetic incident or authorized evidence.

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
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

## Lab 4 — Full Packet Capture

### Objective
Practice **Full Packet Capture** using a synthetic incident or authorized evidence.

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
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

## Lab 5 — Capture Point

### Objective
Practice **Capture Point** using a synthetic incident or authorized evidence.

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

## Lab 6 — SPAN Port

### Objective
Practice **SPAN Port** using a synthetic incident or authorized evidence.

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

## Lab 7 — Network TAP

### Objective
Practice **Network TAP** using a synthetic incident or authorized evidence.

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

## Lab 8 — Packet Loss

### Objective
Practice **Packet Loss** using a synthetic incident or authorized evidence.

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

## Lab 9 — Capture Filter

### Objective
Practice **Capture Filter** using a synthetic incident or authorized evidence.

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

## Lab 10 — Display Filter

### Objective
Practice **Display Filter** using a synthetic incident or authorized evidence.

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

## Lab 11 — tcpdump

### Objective
Practice **tcpdump** using a synthetic incident or authorized evidence.

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
sudo tcpdump -i lo -nn -c 50 -w /tmp/lab.pcap
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

## Lab 12 — Wireshark

### Objective
Practice **Wireshark** using a synthetic incident or authorized evidence.

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
Wireshark filters: dns | http | tls | tcp.flags.syn == 1 | ip.addr == 192.0.2.10
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

## Lab 13 — TShark Awareness

### Objective
Practice **TShark Awareness** using a synthetic incident or authorized evidence.

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

## Lab 14 — Ethernet Evidence

### Objective
Practice **Ethernet Evidence** using a synthetic incident or authorized evidence.

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

## Lab 15 — ARP Evidence

### Objective
Practice **ARP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 16 — IPv4 Evidence

### Objective
Practice **IPv4 Evidence** using a synthetic incident or authorized evidence.

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

## Lab 17 — IPv6 Evidence

### Objective
Practice **IPv6 Evidence** using a synthetic incident or authorized evidence.

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

## Lab 18 — TCP Evidence

### Objective
Practice **TCP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 19 — UDP Evidence

### Objective
Practice **UDP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 20 — ICMP Evidence

### Objective
Practice **ICMP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 21 — TCP Handshake

### Objective
Practice **TCP Handshake** using a synthetic incident or authorized evidence.

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

## Lab 22 — TCP Reset

### Objective
Practice **TCP Reset** using a synthetic incident or authorized evidence.

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

## Lab 23 — Retransmission

### Objective
Practice **Retransmission** using a synthetic incident or authorized evidence.

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

## Lab 24 — 5-Tuple

### Objective
Practice **5-Tuple** using a synthetic incident or authorized evidence.

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

## Lab 25 — Flow Record

### Objective
Practice **Flow Record** using a synthetic incident or authorized evidence.

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
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

## Lab 26 — NetFlow

### Objective
Practice **NetFlow** using a synthetic incident or authorized evidence.

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
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

## Lab 27 — IPFIX

### Objective
Practice **IPFIX** using a synthetic incident or authorized evidence.

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
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

## Lab 28 — Flow Direction

### Objective
Practice **Flow Direction** using a synthetic incident or authorized evidence.

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
src_ip dst_ip src_port dst_port proto bytes packets start end action
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

## Lab 29 — NAT Awareness

### Objective
Practice **NAT Awareness** using a synthetic incident or authorized evidence.

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

## Lab 30 — DHCP Correlation

### Objective
Practice **DHCP Correlation** using a synthetic incident or authorized evidence.

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

## Lab 31 — VPN Correlation

### Objective
Practice **VPN Correlation** using a synthetic incident or authorized evidence.

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

## Lab 32 — DNS Evidence

### Objective
Practice **DNS Evidence** using a synthetic incident or authorized evidence.

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
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

## Lab 33 — DNS Query Types

### Objective
Practice **DNS Query Types** using a synthetic incident or authorized evidence.

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
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

## Lab 34 — NXDOMAIN

### Objective
Practice **NXDOMAIN** using a synthetic incident or authorized evidence.

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

## Lab 35 — DNS Tunneling Awareness

### Objective
Practice **DNS Tunneling Awareness** using a synthetic incident or authorized evidence.

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
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

## Lab 36 — HTTP Evidence

### Objective
Practice **HTTP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 37 — HTTP User-Agent

### Objective
Practice **HTTP User-Agent** using a synthetic incident or authorized evidence.

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

## Lab 38 — HTTP Upload Awareness

### Objective
Practice **HTTP Upload Awareness** using a synthetic incident or authorized evidence.

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

## Lab 39 — Proxy Logs

### Objective
Practice **Proxy Logs** using a synthetic incident or authorized evidence.

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

## Lab 40 — TLS Evidence

### Objective
Practice **TLS Evidence** using a synthetic incident or authorized evidence.

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
TLS metadata: endpoints | SNI | certificate | version | timing | bytes
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

## Lab 41 — SNI

### Objective
Practice **SNI** using a synthetic incident or authorized evidence.

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

## Lab 42 — TLS Certificate

### Objective
Practice **TLS Certificate** using a synthetic incident or authorized evidence.

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
TLS metadata: endpoints | SNI | certificate | version | timing | bytes
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

## Lab 43 — JA3 / JA4 Awareness

### Objective
Practice **JA3 / JA4 Awareness** using a synthetic incident or authorized evidence.

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

## Lab 44 — QUIC / HTTP3 Awareness

### Objective
Practice **QUIC / HTTP3 Awareness** using a synthetic incident or authorized evidence.

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

## Lab 45 — SMB Evidence

### Objective
Practice **SMB Evidence** using a synthetic incident or authorized evidence.

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

## Lab 46 — RDP Evidence

### Objective
Practice **RDP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 47 — SSH Evidence

### Objective
Practice **SSH Evidence** using a synthetic incident or authorized evidence.

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

## Lab 48 — SMTP Evidence

### Objective
Practice **SMTP Evidence** using a synthetic incident or authorized evidence.

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

## Lab 49 — Zeek

### Objective
Practice **Zeek** using a synthetic incident or authorized evidence.

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
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

## Lab 50 — Zeek conn.log

### Objective
Practice **Zeek conn.log** using a synthetic incident or authorized evidence.

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
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

## Lab 51 — Zeek dns.log

### Objective
Practice **Zeek dns.log** using a synthetic incident or authorized evidence.

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
client | query | answer | rcode | resolver | timestamp → correlate with host/process/user
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

## Lab 52 — Zeek http.log

### Objective
Practice **Zeek http.log** using a synthetic incident or authorized evidence.

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
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

## Lab 53 — Zeek ssl.log

### Objective
Practice **Zeek ssl.log** using a synthetic incident or authorized evidence.

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
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

## Lab 54 — Zeek files.log

### Objective
Practice **Zeek files.log** using a synthetic incident or authorized evidence.

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
PCAP → Zeek → conn.log | dns.log | http.log | ssl.log | files.log → timeline/pivots
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

## Lab 55 — IDS Alerts

### Objective
Practice **IDS Alerts** using a synthetic incident or authorized evidence.

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

# Mini Project — Network Forensics Investigation

Use a lab PCAP plus synthetic firewall, DNS, DHCP/VPN, and endpoint logs. Hash the PCAP, identify sessions, build host/domain pivots, analyze DNS/HTTP/TLS/flow evidence, use Zeek-style logs, correlate with identity/endpoint data, reconstruct a timeline, and document encryption, packet-loss, and NAT limitations.

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

- Wireshark Documentation — https://www.wireshark.org/docs/
- Zeek — https://zeek.org/
- tcpdump — https://www.tcpdump.org/
- NIST SP 800-86 — https://csrc.nist.gov/pubs/sp/800/86/final

## 8. Certification Relevance

Relevant to network forensics, DFIR, incident response, SOC, NDR, threat hunting, and network-security analysis.

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

### Q1. What is the key lesson from **Network Forensics Purpose**?

**Short answer:** Network forensics preserves and analyzes packet, flow, DNS, firewall, proxy, VPN, and sensor telemetry to reconstruct network activity.

### Q2. What is the key lesson from **Network Evidence Sources**?

**Short answer:** Common sources include PCAP, NetFlow/IPFIX, Zeek, firewall, DNS, DHCP, proxy, VPN, IDS/IPS, NDR, and cloud flow logs.

### Q3. What is the key lesson from **Packet Capture**?

**Short answer:** PCAP records individual packets and may contain detailed payload and protocol evidence.

### Q4. What is the key lesson from **Full Packet Capture**?

**Short answer:** Full capture offers rich evidence but creates storage, privacy, and access-control challenges.

### Q5. What is the key lesson from **Capture Point**?

**Short answer:** Sensor placement determines which traffic direction, NAT state, and segments are visible.

### Q6. What is the key lesson from **SPAN Port**?

**Short answer:** Switch mirroring can copy traffic to sensors but may drop packets under load.

### Q7. What is the key lesson from **Network TAP**?

**Short answer:** A TAP can provide dedicated traffic copies depending on design.

### Q8. What is the key lesson from **Packet Loss**?

**Short answer:** Dropped capture packets create uncertainty and can break session reconstruction.

### Q9. What is the key lesson from **Capture Filter**?

**Short answer:** Capture filters reduce what is stored at collection time.

### Q10. What is the key lesson from **Display Filter**?

**Short answer:** Display filters select what is shown from an existing capture.

### Q11. What is the key lesson from **tcpdump**?

**Short answer:** tcpdump captures and filters authorized network traffic.

### Q12. What is the key lesson from **Wireshark**?

**Short answer:** Wireshark decodes protocols and supports filtering and stream reconstruction.

### Q13. What is the key lesson from **TShark Awareness**?

**Short answer:** TShark provides command-line Wireshark analysis for automation.

### Q14. What is the key lesson from **Ethernet Evidence**?

**Short answer:** Layer-2 frames reveal MAC, VLAN, and local-segment context.

### Q15. What is the key lesson from **ARP Evidence**?

**Short answer:** ARP can help map IPv4-to-MAC relationships on local networks.

### Q16. What is the key lesson from **IPv4 Evidence**?

**Short answer:** IPv4 headers provide source, destination, fragmentation, TTL, and protocol context.

### Q17. What is the key lesson from **IPv6 Evidence**?

**Short answer:** IPv6 analysis includes addresses, extension headers, and neighbor behavior.

### Q18. What is the key lesson from **TCP Evidence**?

**Short answer:** TCP sequence, flags, ports, retransmissions, and state help reconstruct sessions.

### Q19. What is the key lesson from **UDP Evidence**?

**Short answer:** UDP lacks connection state and requires protocol context.

### Q20. What is the key lesson from **ICMP Evidence**?

**Short answer:** ICMP reveals reachability, errors, scanning, and path behavior.

### Q21. What is the key lesson from **TCP Handshake**?

**Short answer:** SYN, SYN/ACK, ACK establish a normal TCP connection and identify attempts.

### Q22. What is the key lesson from **TCP Reset**?

**Short answer:** RST packets can indicate closed services, application resets, firewall behavior, or disruption.

### Q23. What is the key lesson from **Retransmission**?

**Short answer:** Retransmissions may indicate loss, congestion, or asymmetric capture rather than attacks.

### Q24. What is the key lesson from **5-Tuple**?

**Short answer:** Source IP, destination IP, source port, destination port, and protocol identify a flow.

### Q25. What is the key lesson from **Flow Record**?

**Short answer:** Flow telemetry summarizes connection metadata without full payload.

### Q26. What is the key lesson from **NetFlow**?

**Short answer:** NetFlow-style records support large-scale relationship and volume analysis.

### Q27. What is the key lesson from **IPFIX**?

**Short answer:** IPFIX is a standardized extensible flow-export format.

### Q28. What is the key lesson from **Flow Direction**?

**Short answer:** Exporter location and direction determine how source and destination should be interpreted.

### Q29. What is the key lesson from **NAT Awareness**?

**Short answer:** NAT changes visible addresses and ports and requires mapping logs for attribution.

### Q30. What is the key lesson from **DHCP Correlation**?

**Short answer:** DHCP data maps changing IP addresses to devices over time.

### Q31. What is the key lesson from **VPN Correlation**?

**Short answer:** VPN logs map remote users to assigned internal addresses and sessions.

### Q32. What is the key lesson from **DNS Evidence**?

**Short answer:** DNS queries and answers reveal domains, resolution paths, failures, and timing.

### Q33. What is the key lesson from **DNS Query Types**?

**Short answer:** A, AAAA, MX, TXT, SRV, and other types provide protocol context.

### Q34. What is the key lesson from **NXDOMAIN**?

**Short answer:** Repeated failed queries can indicate malware, misconfiguration, or algorithmic domain generation.

### Q35. What is the key lesson from **DNS Tunneling Awareness**?

**Short answer:** Unusual encoded or high-volume queries can suggest tunneling but require validation.

### Q36. What is the key lesson from **HTTP Evidence**?

**Short answer:** HTTP requests reveal methods, hosts, paths, headers, status, types, and user agents when visible.

### Q37. What is the key lesson from **HTTP User-Agent**?

**Short answer:** User agents can support client identification but are easy to spoof.

### Q38. What is the key lesson from **HTTP Upload Awareness**?

**Short answer:** Large POST/PUT bodies or unusual endpoints can support exfiltration investigations.

### Q39. What is the key lesson from **Proxy Logs**?

**Short answer:** Proxy telemetry provides user, URL, category, method, action, bytes, and policy context.

### Q40. What is the key lesson from **TLS Evidence**?

**Short answer:** Encryption hides payload but endpoints, certificates, SNI, timing, and flow remain useful.

### Q41. What is the key lesson from **SNI**?

**Short answer:** Server Name Indication can reveal the intended hostname when present and visible.

### Q42. What is the key lesson from **TLS Certificate**?

**Short answer:** Certificate subject, issuer, validity, fingerprints, and SANs support infrastructure analysis.

### Q43. What is the key lesson from **JA3 / JA4 Awareness**?

**Short answer:** TLS/client fingerprints can support clustering but are not unique identities.

### Q44. What is the key lesson from **QUIC / HTTP3 Awareness**?

**Short answer:** QUIC encrypts more transport metadata and requires updated tooling and assumptions.

### Q45. What is the key lesson from **SMB Evidence**?

**Short answer:** SMB traffic/logs can reveal file access, authentication, and lateral administration.

### Q46. What is the key lesson from **RDP Evidence**?

**Short answer:** RDP can be correlated through network, gateway, Windows, and identity logs.

### Q47. What is the key lesson from **SSH Evidence**?

**Short answer:** SSH payload is encrypted but connection timing and server logs remain useful.

### Q48. What is the key lesson from **SMTP Evidence**?

**Short answer:** Mail transport metadata supports phishing and message-path investigations.

### Q49. What is the key lesson from **Zeek**?

**Short answer:** Zeek converts network activity into structured protocol logs.

### Q50. What is the key lesson from **Zeek conn.log**?

**Short answer:** Connection logs summarize sessions and state.

### Q51. What is the key lesson from **Zeek dns.log**?

**Short answer:** DNS logs provide query, answer, type, and response context.

### Q52. What is the key lesson from **Zeek http.log**?

**Short answer:** HTTP logs provide request and response metadata when visible.

### Q53. What is the key lesson from **Zeek ssl.log**?

**Short answer:** TLS logs provide certificates, versions, SNI, and session metadata.

### Q54. What is the key lesson from **Zeek files.log**?

**Short answer:** File metadata can connect transferred files to sessions where configured.

### Q55. What is the key lesson from **IDS Alerts**?

**Short answer:** IDS/IPS alerts should be correlated with underlying traffic and endpoint context.

### Q56. What is the key lesson from **NDR Evidence**?

**Short answer:** NDR findings provide behavioral relationships but require validation.

### Q57. What is the key lesson from **Firewall Evidence**?

**Short answer:** Firewall logs provide policy decisions, NAT, zones, rule IDs, sessions, and application classification.

### Q58. What is the key lesson from **Cloud Flow Logs**?

**Short answer:** Cloud flow logs show virtual-network traffic and policy outcomes.

### Q59. What is the key lesson from **Load Balancer Logs**?

**Short answer:** Load-balancer logs reveal client requests, TLS, target response, and backend routing.

### Q60. What is the key lesson from **WAF Logs**?

**Short answer:** WAF telemetry provides rule matches and HTTP request context.

### Q61. What is the key lesson from **API Gateway Logs**?

**Short answer:** API gateways provide route, client, token, response, latency, and quota evidence.

### Q62. What is the key lesson from **Beaconing**?

**Short answer:** Repeated low-volume connections at regular intervals can suggest command-and-control-like behavior.

### Q63. What is the key lesson from **Beacon Interval**?

**Short answer:** Measure timing variation instead of assuming perfectly regular intervals.

### Q64. What is the key lesson from **Rare Destination**?

**Short answer:** New or low-prevalence destinations are useful pivots with process and asset context.

### Q65. What is the key lesson from **Fan-Out**?

**Short answer:** One host connecting to many destinations may indicate discovery, admin activity, or scanning.

### Q66. What is the key lesson from **Fan-In**?

**Short answer:** Many sources connecting to one destination may reflect normal service use or attack traffic.

### Q67. What is the key lesson from **Lateral Movement**?

**Short answer:** Correlate remote-service connections with authentication and endpoint events.

### Q68. What is the key lesson from **Exfiltration**?

**Short answer:** Look for unusual outbound volume, destinations, archives, cloud uploads, or protocol use.

### Q69. What is the key lesson from **Data Volume Baseline**?

**Short answer:** Volume anomalies require comparison with expected user and service behavior.

### Q70. What is the key lesson from **Session Reconstruction**?

**Short answer:** Reconstruct ordered conversations using connection state and payload when available and authorized.

### Q71. What is the key lesson from **TCP Stream**?

**Short answer:** Wireshark can reconstruct streams when capture completeness permits.

### Q72. What is the key lesson from **File Carving Awareness**?

**Short answer:** Files may be recovered from unencrypted traffic in authorized investigations.

### Q73. What is the key lesson from **Encrypted Traffic Limitation**?

**Short answer:** Encryption limits payload analysis and increases dependence on endpoint/proxy/app context.

### Q74. What is the key lesson from **Asymmetric Capture**?

**Short answer:** Seeing only one direction can make sessions appear incomplete.

### Q75. What is the key lesson from **Packet Timestamp**?

**Short answer:** Sensor clock accuracy affects event ordering.

### Q76. What is the key lesson from **PCAP Integrity**?

**Short answer:** Hash and protect captures used as formal evidence.

### Q77. What is the key lesson from **Evidence Minimization**?

**Short answer:** Captures can contain unrelated sensitive traffic and should be scoped carefully.

### Q78. What is the key lesson from **Timeline**?

**Short answer:** Normalize packet, flow, DNS, firewall, proxy, VPN, endpoint, and identity evidence.

### Q79. What is the key lesson from **Host Pivot**?

**Short answer:** Start from a host and enumerate destinations, protocols, users, and time windows.

### Q80. What is the key lesson from **Domain Pivot**?

**Short answer:** Start from a domain and identify clients, answers, IPs, processes, and sightings.

### Q81. What is the key lesson from **IP Pivot**?

**Short answer:** Investigate hosts and users that communicated with an address and map NAT/VPN identity.

### Q82. What is the key lesson from **Session Pivot**?

**Short answer:** Use one connection to locate related process, user, DNS, proxy, or endpoint evidence.

### Q83. What is the key lesson from **Network IOC**?

**Short answer:** Domains, IPs, URLs, certificates, and protocol artifacts can support scoping with context.

### Q84. What is the key lesson from **Behavioral Network Indicator**?

**Short answer:** Connection pattern, timing, protocol misuse, or relationships can outlast infrastructure indicators.

### Q85. What is the key lesson from **Network Forensics Report**?

**Short answer:** Report sources, sensor gaps, timeline, sessions, indicators, confidence, and limitations.

## Completion Checklist
- [ ] I completed at least 30 labs.
- [ ] I completed the mini project.
- [ ] I can preserve and document evidence.
- [ ] I can build a cross-source timeline.
- [ ] I can distinguish containment, eradication, and recovery.
- [ ] I can state confidence and limitations.
