# Phase 26 — Incident Response & Forensics

Recommended sequence:

```text
SOC Fundamentals
      ↓
104 Incident Handling Fundamentals
      ↓
105 Incident Response
      ↓
106 Computer Forensics
      ↓
107 Network Forensics
```

## Courses

| # | Course | Focus |
|---|---|---|
| 104 | Incident Handling Fundamentals | Intake, triage, severity, evidence preservation, escalation, communication, containment planning |
| 105 | Incident Response | Scope, containment, eradication, recovery, communications, lessons learned |
| 106 | Computer Forensics | Acquisition, integrity, filesystem, memory, registry, browser, timelines, reporting |
| 107 | Network Forensics | PCAP, flow, DNS, firewall/proxy/VPN, Wireshark/Zeek, session and timeline reconstruction |

## Incident Lifecycle

```text
Preparation → Detection/Validation → Scope → Containment → Eradication → Recovery → Lessons → Improvement
```

## Evidence Principle

```text
Preserve first → record actions → hash formal evidence → analyze copies → state fact/inference/confidence → verify conclusions
```

## Forensic Evidence Layers

```text
Computer: disk | filesystem | memory | registry | event logs | browser | persistence
Network: PCAP | flow | firewall | DNS/DHCP | proxy/VPN | Zeek | IDS/NDR | cloud flow
```

## Recommended Lab Structure

```text
Phase_26_IR_DFIR/
├── 104_Handling/
├── 105_Response/
│   ├── timeline/
│   ├── containment/
│   ├── eradication/
│   └── recovery/
├── 106_Computer_Forensics/
│   ├── evidence/
│   ├── hashes/
│   ├── filesystem/
│   ├── memory/
│   └── report/
└── 107_Network_Forensics/
    ├── pcaps/
    ├── zeek/
    ├── flow/
    ├── dns/
    └── report/
```

## Phase Capstone

Scenario: synthetic cloud-account compromise + one endpoint + suspicious web/API activity + unusual outbound traffic. Deliver incident intake, severity, timeline, scope, evidence matrix, containment, credential/token revocation, host forensic findings, network forensic findings, root cause, eradication, recovery, heightened monitoring, stakeholder updates, lessons learned, and detection improvements.

## Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 104 — Incident Handling | 61 | 55 | 61 | 4,508 |
| 105 — Incident Response | 76 | 55 | 76 | 5,094 |
| 106 — Computer Forensics | 88 | 55 | 88 | 5,556 |
| 107 — Network Forensics | 85 | 55 | 85 | 5,439 |
| **Total** | **310** | **220** | **310** | **20,597** |

## Completion Criteria

You should be able to classify and escalate incidents; preserve volatile evidence; build cross-source timelines; scope endpoints, identities, cloud, data, and network activity; choose containment; eradicate root causes; rotate credentials/tokens/keys; restore trusted state; hash and document forensic evidence; analyze basic filesystem/memory/browser/registry artifacts; analyze PCAP/flow/DNS/firewall evidence; and clearly separate fact from inference.

## Next Phase

```text
Phase 27 — OT Security
108 Operational Technology (OT) Security
```
