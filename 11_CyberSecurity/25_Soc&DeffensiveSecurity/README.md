# Phase 25 — SOC & Defensive Security

Dependency:

```text
Security Fundamentals + Networking + OS Administration
                         ↓
                       SOC
                         ↓
              Security Monitoring
                         ↓
              Threat Intelligence
                         ↓
                 Threat Hunting
```

## Courses

| # | Course | Focus |
|---|---|---|
| 100 | Security Operations Center Fundamentals | SOC mission, roles, triage, cases, SIEM/EDR/NDR/SOAR, playbooks, metrics |
| 101 | Security Monitoring Fundamentals | Telemetry, log engineering, SIEM queries, detections, data health, coverage |
| 102 | Cyber Threat Intelligence | Intelligence cycle, requirements, ATT&CK, indicators, STIX/TAXII, confidence, dissemination |
| 103 | Cyber Threat Hunting | Hypothesis-driven hunting, pivots, entity timelines, data gaps, detection conversion |

## Recommended Order

```text
100 SOC Fundamentals
  ↓
101 Security Monitoring
  ↓
102 Cyber Threat Intelligence
  ↓
103 Cyber Threat Hunting
```

## Defensive Operations Mental Model

```text
Assets / Threat Model
       ↓
Telemetry
       ↓
Detection
       ↓
SOC Triage
       ↓
Investigation
       ↓
CTI Context
       ↓
Threat Hunt
       ↓
Incident / No Incident
       ↓
Detection + Control Improvement
```

## Recommended Lab

```text
Windows + Linux Endpoints
        ↓
Identity / AD
        ↓
Firewall / DNS / Proxy / Flow
        ↓
Cloud / Applications
        ↓
SIEM / Log Platform
        ↓
SOC Case Management + Hunt Notebook
```

## Phase Capstone

Design a SOC for a hybrid 300-person organization. Produce: operating model, RACI, telemetry inventory, monitoring architecture, severity model, triage workflow, playbooks, SIEM query pack, six detections, detection tests, CTI requirements, one CTI brief, five hunt hypotheses, hunt notebook, metrics dashboard, and executive summary.

## Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 100 — SOC Fundamentals | 91 | 55 | 91 | 5,537 |
| 101 — Security Monitoring | 82 | 55 | 82 | 5,200 |
| 102 — Cyber Threat Intelligence | 79 | 55 | 79 | 5,070 |
| 103 — Cyber Threat Hunting | 64 | 55 | 64 | 4,506 |
| **Total** | **316** | **220** | **316** | **20,313** |

## Completion Criteria

Before Phase 26 you should be able to: triage and document alerts; identify required telemetry before querying; validate data health; write basic KQL/SPL/Sigma-style logic; create confidence-rated CTI; build hunt hypotheses; correlate endpoint, identity, network, cloud, and app evidence; convert findings into detections or engineering tasks; and escalate a confirmed incident with a timeline.

## Next Phase

```text
Phase 26 — Incident Response & Forensics
104 Incident Handling Fundamentals
105 Incident Response
106 Computer Forensics
107 Network Forensics
```
