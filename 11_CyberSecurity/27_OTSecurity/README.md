# Phase 27 — OT Security

Phase 27 introduces cybersecurity for systems that directly monitor or control the physical world.

Dependency:

```text
Networking
   +
Cybersecurity Fundamentals
   +
Network Security
   ↓
Operational Technology Security
```

## Course

**108 — Operational Technology (OT) Security**

## Why OT Security Is Different

```text
Enterprise IT priority examples:
Confidentiality
Integrity
Availability

OT must additionally prioritize:
Safety
Physical process integrity
Deterministic operation
Reliability
Availability
Equipment protection
Environmental impact
```

A security control that is reasonable in office IT can be unsafe in OT if it unexpectedly stops control, changes timing, overloads a controller, or prevents operators from seeing the process.

## OT Architecture Mental Model

```text
Enterprise IT
    ↓
Industrial DMZ
    ↓
Site Operations
    ↓
Supervisory Control
    ↓
Basic Control
    ↓
Physical Process
```

Key assets:

```text
PLC
RTU
SCADA
DCS
HMI
Historian
Engineering Workstation
SIS
Sensors / Actuators
Industrial switches/firewalls
Vendor remote-access systems
```

## Core OT Security Strategy

```text
Know assets and process
   ↓
Classify criticality / safety impact
   ↓
Segment zones and conduits
   ↓
Control remote / privileged access
   ↓
Harden stable endpoints
   ↓
Manage patches / changes carefully
   ↓
Passive monitoring
   ↓
Backup / restore
   ↓
OT-aware incident response
```

## Lab Safety

Use only:

```text
simulators
training PCAPs
vendor documentation
virtual PLC/SCADA labs
intentionally designed OT ranges
explicitly approved test systems
```

Do **not** actively scan, fuzz, exploit, reboot, patch, or modify production PLCs/controllers merely for training.

## Recommended Lab Structure

```text
Phase_27_OT_Lab/
├── architecture/
├── asset_inventory/
├── zones_conduits/
├── remote_access/
├── monitoring/
├── vulnerability_management/
├── backups/
├── incident_response/
└── tabletop/
```

## Phase Capstone

Design the cybersecurity architecture for a fictional manufacturing plant with:

```text
Enterprise IT
Industrial DMZ
SCADA
Historian
2 production cells
PLCs
HMIs
Engineering workstation
Vendor support
Safety system
```

Produce asset inventory, Purdue-style diagram, zone/conduit matrix, firewall-flow matrix, remote-access policy, monitoring architecture, patch/change workflow, vulnerability register, backup/restore plan, incident playbook, and tabletop.

## Phase Statistics

| Course | Core Topics | Labs | Q&A | Lines |
|---|---:|---:|---:|---:|
| 108 — OT Security | 121 | 70 | 121 | 10,259 |

## Completion Criteria

You should be able to:

- distinguish IT and OT risk priorities;
- explain PLC/RTU/SCADA/DCS/HMI/SIS roles;
- draw Purdue-style OT zones;
- design an Industrial DMZ;
- explain why passive visibility is often preferred;
- design remote vendor access;
- handle patch/change management safely;
- build an OT asset and vulnerability register;
- create backup/restore and incident-response plans;
- explain how cyber compromise can create physical impact.

## Next Phase

```text
Phase 28 — GRC
109 Governance, Risk and Compliance Fundamentals
110 Cybersecurity Risk Assessment
111 Security Compliance
```
