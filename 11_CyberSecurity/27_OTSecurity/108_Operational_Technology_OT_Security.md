# 108. Operational Technology (OT) Security

> Phase 27 — OT Security

This course is designed as a self-contained module using:

```text
Context
  ↓
Objective / Requirement
  ↓
Risk / Threat / Obligation
  ↓
Control
  ↓
Evidence
  ↓
Decision
  ↓
Remediation / Treatment
  ↓
Review
```

---

## 1. Topic Title

**Operational Technology (OT) Security**

---

## 2. Learning Objectives

- Explain OT, ICS, PLC, RTU, SCADA, DCS, HMI, historian, engineering workstation, and SIS roles.
- Compare OT priorities with enterprise IT, especially safety, availability, reliability, and integrity.
- Use Purdue-style zones and conduits to reason about industrial trust boundaries.
- Design IT/OT segmentation, industrial DMZ, jump-host, remote-access, and vendor-access controls.
- Understand industrial protocol security limitations and write/control-command risk.
- Build passive asset inventory and monitoring strategies without destabilizing production systems.
- Design OT hardening, patching, change, backup, restore, and vulnerability-management processes.
- Assess cyber-physical risk using process, safety, business, legacy, and vendor context.
- Design OT incident response and recovery that preserve safe operation.
- Apply NIST SP 800-82 Rev. 3, IEC 62443 awareness, and CISA CPG concepts.

---

## 3. Prerequisites

Required:

```text
Computer Networks
Cybersecurity Fundamentals
Network Security Fundamentals
Linux / Windows administration basics
```

Strongly recommended:

```text
Industrial process / manufacturing awareness
Network segmentation
Firewalls
Incident response basics
```

Production OT testing requires explicit authorization and operations/safety coordination.

---

## 4. Core Concepts Explanation

# Part 1 — Operational Technology Definition

### Core Explanation

Operational Technology includes programmable systems and devices that monitor or control physical processes, equipment, environments, and infrastructure.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 2 — OT vs IT

### Core Explanation

OT prioritizes safe, reliable physical operation and availability, while enterprise IT more often prioritizes information processing and confidentiality.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 3 — Cyber-Physical Risk

### Core Explanation

OT cyber events can create physical consequences such as unsafe states, damaged equipment, environmental impact, quality loss, or production downtime.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 4 — Safety First

### Core Explanation

Cybersecurity controls in OT must not undermine required safety functions or emergency procedures.

### Diagram / Example

```text
Basic Process Control System
      ↓
Physical Process
      ↑
Safety Instrumented System

Security design must not reduce required safety independence.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 5 — Reliability

### Core Explanation

OT systems may need continuous deterministic operation for years with limited maintenance windows.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 6 — Availability

### Core Explanation

Loss of availability can immediately stop production or critical infrastructure services.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 7 — Integrity

### Core Explanation

Unauthorized changes to control logic, setpoints, recipes, or sensor values can create dangerous physical outcomes.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 8 — Confidentiality in OT

### Core Explanation

Confidentiality still matters for engineering data, credentials, recipes, intellectual property, and safety/security configuration.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 9 — OT Asset Types

### Core Explanation

OT environments include PLCs, RTUs, DCS, SCADA, HMIs, engineering workstations, historians, sensors, actuators, safety systems, and industrial network devices.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 10 — PLC

### Core Explanation

Programmable Logic Controllers execute deterministic control logic close to the physical process.

### Diagram / Example

```text
Sensor
  ↓
PLC / Controller
  ↓ control logic
Actuator
  ↓
Physical process

Security question:
Can an unauthorized change alter physical behavior?
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 11 — RTU

### Core Explanation

Remote Terminal Units collect telemetry and perform control in geographically distributed systems.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 12 — SCADA

### Core Explanation

Supervisory Control and Data Acquisition systems provide remote monitoring and supervisory control across distributed assets.

### Diagram / Example

```text
Field devices
  ↓
PLC / RTU
  ↓
SCADA server
  ↓
HMI / operator console
  ↓
historian / engineering workstation
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 13 — DCS

### Core Explanation

Distributed Control Systems coordinate process control across plant or process areas.

### Diagram / Example

```text
Process Area A ─┐
Process Area B ─┼─ Controllers ─ DCS Servers ─ Operator Stations
Process Area C ─┘
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 14 — HMI

### Core Explanation

Human-Machine Interfaces show process state and allow authorized operators to issue commands.

### Diagram / Example

```text
Field devices
  ↓
PLC / RTU
  ↓
SCADA server
  ↓
HMI / operator console
  ↓
historian / engineering workstation
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 15 — Engineering Workstation

### Core Explanation

Engineering workstations configure controllers, logic, firmware, recipes, and industrial devices and are highly privileged OT assets.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 16 — Historian

### Core Explanation

Process historians collect operational measurements and events for analysis, reporting, and business integration.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 17 — SIS

### Core Explanation

Safety Instrumented Systems provide independent safety functions intended to drive a process to a safe state.

### Diagram / Example

```text
Basic Process Control System
      ↓
Physical Process
      ↑
Safety Instrumented System

Security design must not reduce required safety independence.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 18 — Sensors

### Core Explanation

Sensors measure physical properties such as temperature, pressure, level, speed, position, or flow.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 19 — Actuators

### Core Explanation

Actuators physically change valves, motors, relays, drives, and other equipment based on control commands.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 20 — Industrial Network Device

### Core Explanation

Industrial switches, routers, firewalls, gateways, and serial converters provide OT connectivity.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 21 — Building Automation

### Core Explanation

Building automation controls HVAC, elevators, lighting, access, and physical-environment systems.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 22 — Manufacturing OT

### Core Explanation

Manufacturing OT integrates machines, robots, production lines, quality equipment, and supervisory systems.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 23 — Energy OT

### Core Explanation

Energy OT includes generation, substations, distribution, pipelines, and related control systems.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 24 — Water OT

### Core Explanation

Water and wastewater OT controls pumps, treatment, chemical dosing, reservoirs, and distribution.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 25 — Transportation OT

### Core Explanation

Transportation OT includes signaling, fleet, traffic, rail, and other physical-control systems.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 26 — Purdue Model Awareness

### Core Explanation

The Purdue-style model provides a common mental model for separating enterprise, site operations, supervisory control, basic control, and physical process layers.

### Diagram / Example

```text
Enterprise IT
   │
Level 5/4 — Business / Enterprise
   │
Industrial DMZ
   │
Level 3 — Site Operations
   │
Level 2 — Supervisory Control
   │
Level 1 — Basic Control
   │
Level 0 — Physical Process
```

Security boundaries should respect operational dependencies and safety.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 27 — Level 0

### Core Explanation

Level 0 represents physical process sensors and actuators.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 28 — Level 1

### Core Explanation

Level 1 represents basic control devices such as PLCs and drives.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 29 — Level 2

### Core Explanation

Level 2 commonly contains HMIs and supervisory control.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 30 — Level 3

### Core Explanation

Level 3 commonly supports site manufacturing/operations services.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 31 — Industrial DMZ

### Core Explanation

An Industrial DMZ mediates communication between enterprise IT and OT operations without allowing uncontrolled direct trust.

### Diagram / Example

```text
Enterprise IT
    ↓
Firewall
    ↓
Industrial DMZ
 ├─ jump host
 ├─ patch relay
 ├─ historian replica
 └─ remote-access broker
    ↓
Firewall
    ↓
OT Operations Network
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 32 — Enterprise Zone

### Core Explanation

Enterprise IT contains business systems, identity, email, user workstations, and corporate services.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 33 — OT Zone

### Core Explanation

OT zones group systems by process, function, criticality, and communication need.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 34 — Cell / Area Zone

### Core Explanation

Cell or area segmentation limits faults or compromise to a smaller process region.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 35 — Conduit

### Core Explanation

A conduit is a controlled communication path between security zones.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 36 — Asset Inventory

### Core Explanation

A reliable OT inventory records device type, owner, vendor/model, firmware, location, zone, criticality, and dependencies.

### Diagram / Example

```text
Asset record:
owner
function
location
vendor/model
firmware
network zone
criticality
safety impact
support status
dependencies
backup/recovery owner
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 37 — Passive Asset Discovery

### Core Explanation

Passive observation is often safer than active scanning for fragile controllers or legacy devices.

### Diagram / Example

```text
SPAN/TAP
  ↓
Passive OT sensor
  ↓
asset discovery
protocol metadata
baseline
anomaly / signature detection
  ↓
SOC / OT engineering review
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 38 — Active Scanning Risk

### Core Explanation

Active probes can destabilize some OT devices and require explicit owner/vendor approval and testing.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 39 — Asset Criticality

### Core Explanation

Criticality should consider safety, environmental, production, quality, recovery, and cascading dependencies.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 40 — Process Dependency

### Core Explanation

Cybersecurity teams must understand what physical process depends on each asset.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 41 — Single Point of Failure

### Core Explanation

OT architectures should identify devices/services whose failure stops a process or defeats safety/recovery.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 42 — Legacy System

### Core Explanation

Legacy OT may run unsupported operating systems, proprietary protocols, or fixed firmware that cannot be patched easily.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 43 — Long Lifecycle

### Core Explanation

Industrial equipment can remain in service for decades, outlasting normal IT support cycles.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 44 — Vendor Dependency

### Core Explanation

OT maintenance often depends on vendors for firmware, engineering software, support, and remote access.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 45 — Proprietary Technology

### Core Explanation

Proprietary protocols and devices do not automatically provide security through obscurity.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 46 — Modbus Awareness

### Core Explanation

Modbus is widely used for industrial communication and historically provides limited native security in many deployments.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 47 — DNP3 Awareness

### Core Explanation

DNP3 is common in utilities and has legacy and secure authentication variants depending on implementation.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 48 — OPC Awareness

### Core Explanation

OPC technologies support industrial interoperability; modern OPC UA provides stronger security capabilities than older designs when configured correctly.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 49 — EtherNet/IP Awareness

### Core Explanation

EtherNet/IP carries Common Industrial Protocol traffic over standard Ethernet/IP networks and needs segmentation and monitoring.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 50 — PROFINET Awareness

### Core Explanation

PROFINET is an industrial Ethernet technology with timing and operational characteristics that must be considered during security changes.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 51 — BACnet Awareness

### Core Explanation

BACnet is common in building automation and requires careful segmentation and access control.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 52 — Serial Protocol Awareness

### Core Explanation

Many legacy OT communications use serial protocols bridged into Ethernet environments.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 53 — Protocol Authentication

### Core Explanation

Security teams should identify which industrial protocols authenticate commands and which rely mainly on network trust.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 54 — Protocol Encryption

### Core Explanation

Encryption may not be available in legacy OT protocols and may require compensating network/security controls.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 55 — Write Command Risk

### Core Explanation

Industrial write/control functions can directly change process behavior and need strict source and role restrictions.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 56 — Read-Only Monitoring

### Core Explanation

Monitoring architectures should prefer passive/read-only approaches when possible.

### Diagram / Example

```text
SPAN/TAP
  ↓
Passive OT sensor
  ↓
asset discovery
protocol metadata
baseline
anomaly / signature detection
  ↓
SOC / OT engineering review
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 57 — Network Segmentation

### Core Explanation

Separate enterprise IT, industrial DMZ, OT operations, process cells, safety, and vendor access according to communication need.

### Diagram / Example

```text
Enterprise IT
    ↓
Firewall
    ↓
Industrial DMZ
 ├─ jump host
 ├─ patch relay
 ├─ historian replica
 └─ remote-access broker
    ↓
Firewall
    ↓
OT Operations Network
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 58 — Default Deny in OT

### Core Explanation

Where technically feasible, only required flows should cross OT security boundaries.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 59 — Industrial Firewall

### Core Explanation

Industrial firewalls enforce zone-to-zone communication policy while respecting protocol and availability requirements.

### Diagram / Example

```text
Enterprise IT
    ↓
Firewall
    ↓
Industrial DMZ
 ├─ jump host
 ├─ patch relay
 ├─ historian replica
 └─ remote-access broker
    ↓
Firewall
    ↓
OT Operations Network
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 60 — Application / Protocol Allowlisting

### Core Explanation

Restrict expected industrial protocols and endpoints rather than allowing broad internal access.

### Diagram / Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 61 — Jump Host

### Core Explanation

Administrative access should pass through controlled jump hosts rather than direct enterprise-to-controller sessions.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 62 — Remote Access Gateway

### Core Explanation

Remote access should terminate in controlled infrastructure with MFA, approvals, logging, and session limitation.

### Diagram / Example

```text
Vendor
  ↓ MFA
Remote-access gateway
  ↓ approval / time-bound access
Jump host
  ↓ recorded session
Specific OT asset

No direct vendor-to-controller path.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 63 — Vendor Remote Access

### Core Explanation

Vendor access should be explicit, time-bound, monitored, and limited to named assets and purposes.

### Diagram / Example

```text
Vendor
  ↓ MFA
Remote-access gateway
  ↓ approval / time-bound access
Jump host
  ↓ recorded session
Specific OT asset

No direct vendor-to-controller path.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 64 — MFA for Remote Access

### Core Explanation

Remote and privileged OT access should use strong authentication when supported by architecture.

### Diagram / Example

```text
Vendor
  ↓ MFA
Remote-access gateway
  ↓ approval / time-bound access
Jump host
  ↓ recorded session
Specific OT asset

No direct vendor-to-controller path.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 65 — Shared Account Risk

### Core Explanation

Shared engineering or operator accounts reduce accountability and should be minimized where feasible.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 66 — Role-Based Access

### Core Explanation

Separate operator, engineer, maintenance, vendor, and security permissions.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 67 — Privileged Access Management

### Core Explanation

PAM can govern high-risk OT administrative credentials where compatible with operational constraints.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 68 — Password Management

### Core Explanation

Legacy devices may have weak credential capabilities, requiring vaulting, rotation planning, and network compensating controls.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 69 — Service Account

### Core Explanation

OT services and historians may use powerful accounts that require ownership and limited privileges.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 70 — Portable Media

### Core Explanation

USB and removable media can introduce malware into isolated OT networks and need controlled processes.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 71 — Media Scanning Station

### Core Explanation

Organizations may use dedicated scanning/kiosk processes before removable media enters sensitive OT zones.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 72 — Engineering Laptop

### Core Explanation

Portable engineering laptops can bridge corporate, vendor, and OT environments and require strict hardening.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 73 — OT Endpoint Hardening

### Core Explanation

Disable unnecessary services, apply allowlisting where appropriate, restrict admin rights, and protect engineering/HMI systems.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 74 — Application Allowlisting

### Core Explanation

Allowlisting can be effective on stable OT hosts because software changes are relatively infrequent.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 75 — Antivirus / EDR Compatibility

### Core Explanation

Endpoint security tooling must be tested for vendor support, performance impact, and deterministic operation.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 76 — Patch Management

### Core Explanation

OT patching must consider vendor approval, compatibility, maintenance windows, rollback, and process impact.

### Diagram / Example

```text
Vendor advisory
  ↓
lab / compatibility review
  ↓
maintenance window
  ↓
backup / rollback
  ↓
approved change
  ↓
validation with operations
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 77 — Compensating Control

### Core Explanation

When patches cannot be applied quickly, use segmentation, application allowlisting, source restriction, monitoring, or service disablement.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 78 — Firmware Management

### Core Explanation

Controller/device firmware needs inventory, vendor advisories, integrity verification, and controlled upgrades.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 79 — Secure Configuration Baseline

### Core Explanation

OT devices should have approved configurations covering accounts, services, protocols, logging, remote access, and network settings.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 80 — Configuration Backup

### Core Explanation

Controller logic, HMI projects, network configuration, and system settings should be backed up and versioned.

### Diagram / Example

```text
Back up:
PLC logic
HMI projects
SCADA config
historian config
network device config
licenses
recipes / parameters
      ↓
offline / protected copy
      ↓
restore test
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 81 — Offline Backup

### Core Explanation

Critical OT recovery copies should be protected from routine compromise paths.

### Diagram / Example

```text
Back up:
PLC logic
HMI projects
SCADA config
historian config
network device config
licenses
recipes / parameters
      ↓
offline / protected copy
      ↓
restore test
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 82 — Restore Testing

### Core Explanation

A backup is useful only if teams can restore controller logic, servers, applications, and configurations under operational pressure.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 83 — Golden Configuration

### Core Explanation

Known-good control logic and configuration provide a baseline for integrity comparison and recovery.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 84 — Change Management

### Core Explanation

OT changes require owner approval, safety/operations coordination, backup, rollback, and post-change validation.

### Diagram / Example

```text
Vendor advisory
  ↓
lab / compatibility review
  ↓
maintenance window
  ↓
backup / rollback
  ↓
approved change
  ↓
validation with operations
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 85 — Emergency Change

### Core Explanation

Emergency changes still need documentation, bounded scope, and retrospective review.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 86 — Maintenance Window

### Core Explanation

Production changes should align with approved process windows and operational risk.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 87 — OT Vulnerability Management

### Core Explanation

OT vulnerability management combines asset knowledge, vendor advisories, exposure, exploitability, safety, and compensating controls.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 88 — CVSS Limitation in OT

### Core Explanation

Generic technical severity may not reflect physical safety, process availability, or real network exposure.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 89 — OT Risk Scenario

### Core Explanation

Risk scenarios should connect cyber conditions to specific process and safety consequences.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 90 — Safety Impact Analysis

### Core Explanation

Assess whether a cyber event could defeat alarms, interlocks, limits, or safe operating states.

### Diagram / Example

```text
Basic Process Control System
      ↓
Physical Process
      ↑
Safety Instrumented System

Security design must not reduce required safety independence.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 91 — Business Impact

### Core Explanation

Downtime, scrap, quality loss, missed delivery, equipment damage, and regulatory impact can dominate OT risk.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 92 — Threat Sources

### Core Explanation

OT threats include cybercriminals, state actors, insiders, suppliers, commodity malware, accidents, and operational mistakes.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 93 — Ransomware in OT

### Core Explanation

Ransomware can stop OT operations indirectly by affecting Windows servers, identity, engineering systems, or business dependencies.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 94 — IT-to-OT Path

### Core Explanation

Compromise often crosses from enterprise identity/workstations into OT through shared services, remote access, or poorly segmented networks.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 95 — Supply Chain Risk

### Core Explanation

Industrial vendors, firmware, integrators, remote services, and engineering tools are part of the OT attack surface.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 96 — Physical Security

### Core Explanation

Cabinets, ports, field devices, control rooms, and engineering stations require physical access controls.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 97 — Passive OT Monitoring

### Core Explanation

Passive sensors can discover assets, protocols, baseline behavior, and anomalies without sending active probes.

### Diagram / Example

```text
SPAN/TAP
  ↓
Passive OT sensor
  ↓
asset discovery
protocol metadata
baseline
anomaly / signature detection
  ↓
SOC / OT engineering review
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 98 — OT IDS

### Core Explanation

OT-aware monitoring can identify unusual protocol commands, new devices, communication changes, or known malicious patterns.

### Diagram / Example

```text
SPAN/TAP
  ↓
Passive OT sensor
  ↓
asset discovery
protocol metadata
baseline
anomaly / signature detection
  ↓
SOC / OT engineering review
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 99 — Network Baseline

### Core Explanation

Document normal peers, protocols, command types, polling intervals, and engineering activity.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 100 — Anomaly Detection

### Core Explanation

Unexpected write commands, new devices, unusual engineering access, or changed communication patterns require investigation.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 101 — Log Collection

### Core Explanation

Collect firewall, Windows, authentication, engineering, remote-access, network, and application logs where supported.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 102 — Time Synchronization

### Core Explanation

Accurate OT timestamps improve process troubleshooting and incident investigation.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 103 — Historian as Evidence

### Core Explanation

Process historians can provide operational context for cyber investigations but are not substitutes for security logs.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 104 — OT SOC Integration

### Core Explanation

SOC processes should include OT-specific ownership, severity, escalation, and safety constraints.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 105 — OT Incident Response

### Core Explanation

Incident response must coordinate cyber teams with operators, engineers, safety, vendors, and business continuity.

### Diagram / Example

```text
Detection
  ↓
OT engineer + security validate
  ↓
safety / process impact
  ↓
contain with minimum operational risk
  ↓
preserve evidence
  ↓
restore trusted operation
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 106 — Containment in OT

### Core Explanation

Containment should avoid actions that unexpectedly stop safe control or destroy process visibility.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 107 — Controller Isolation Risk

### Core Explanation

Disconnecting a controller may be more dangerous than monitoring it; operations must lead process-safety decisions.

### Diagram / Example

```text
Sensor
  ↓
PLC / Controller
  ↓ control logic
Actuator
  ↓
Physical process

Security question:
Can an unauthorized change alter physical behavior?
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 108 — Manual Operations Awareness

### Core Explanation

Some facilities have manual fallback procedures that should be validated as part of resilience.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 109 — Safety Shutdown

### Core Explanation

Cyber response must understand when safety systems or controlled shutdown procedures are required.

### Diagram / Example

```text
Basic Process Control System
      ↓
Physical Process
      ↑
Safety Instrumented System

Security design must not reduce required safety independence.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 110 — Evidence Preservation

### Core Explanation

Preserve controller logic, engineering logs, network captures, system images, and change records where possible.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 111 — Recovery

### Core Explanation

Restore known-good logic/configuration, validate field/process state, reintroduce systems carefully, and monitor.

### Diagram / Example

```text
Back up:
PLC logic
HMI projects
SCADA config
historian config
network device config
licenses
recipes / parameters
      ↓
offline / protected copy
      ↓
restore test
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 112 — Cyber-Physical Tabletop

### Core Explanation

Tabletops should include security, control engineers, operators, safety, management, and vendors.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 113 — Business Continuity for OT

### Core Explanation

Continuity planning should address manual workarounds, spare parts, vendor support, alternate production, and recovery dependencies.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 114 — Spare Parts

### Core Explanation

Legacy systems may require stored replacement controllers, network devices, storage, licenses, or images.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 115 — Secure Decommissioning

### Core Explanation

Remove credentials, logic, sensitive configuration, and network access when industrial assets are retired.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 116 — OT Governance

### Core Explanation

Define accountable OT cybersecurity ownership spanning operations, engineering, IT, security, safety, and management.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 117 — OT Policy

### Core Explanation

Policies should reflect OT safety, change, remote access, removable media, asset, vulnerability, backup, and incident-response needs.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 118 — NIST SP 800-82 Rev. 3 Awareness

### Core Explanation

NIST SP 800-82 Rev. 3 provides guidance for securing OT while addressing performance, reliability, and safety requirements.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 119 — IEC 62443 Awareness

### Core Explanation

IEC 62443 provides a family of standards addressing industrial automation and control-system security across asset owners, integrators, and products.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 120 — CISA CPGs Awareness

### Core Explanation

CISA Cybersecurity Performance Goals provide prioritized practices relevant to both IT and OT critical-infrastructure environments.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

# Part 121 — OT Security Final Mental Model

### Core Explanation

OT security protects safe and reliable physical operation through asset knowledge, controlled trust boundaries, strong remote access, tested changes, passive visibility, recovery readiness, and engineering-security collaboration.

### Diagram / Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Why It Matters

This topic connects technical security to business, safety, operational, legal, or assurance outcomes.
OT work must prioritize **safety, reliability, availability, deterministic process behavior, and change control**. Active scanning or configuration changes should never be performed on production OT without owner/vendor approval and operational safeguards.

### Practical Use

Apply the concept using documented architectures, read-only evidence, synthetic scenarios, policy/control matrices, or explicitly authorized lab environments.

### Common Problems

- Treating compliance as equal to security.
- Treating a risk score as objective truth.
- Assigning controls without clear owners.
- Collecting evidence that does not actually prove the control works.
- Using generic IT changes in fragile OT environments.
- Ignoring business or safety consequences.
- Keeping exceptions open indefinitely.

### Best Practice

Define the objective, owner, evidence, decision criteria, residual risk, and review cycle. For OT, coordinate every meaningful change with operations and safety stakeholders.

---

## 5. Hands-on Lab / Practical Exercises

## Lab 1 — Operational Technology Definition

### Objective

Practice **Operational Technology Definition** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 2 — OT vs IT

### Objective

Practice **OT vs IT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 3 — Cyber-Physical Risk

### Objective

Practice **Cyber-Physical Risk** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 4 — Safety First

### Objective

Practice **Safety First** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Basic Process Control System
      ↓
Physical Process
      ↑
Safety Instrumented System

Security design must not reduce required safety independence.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 5 — Reliability

### Objective

Practice **Reliability** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 6 — Availability

### Objective

Practice **Availability** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 7 — Integrity

### Objective

Practice **Integrity** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 8 — Confidentiality in OT

### Objective

Practice **Confidentiality in OT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 9 — OT Asset Types

### Objective

Practice **OT Asset Types** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 10 — PLC

### Objective

Practice **PLC** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Sensor
  ↓
PLC / Controller
  ↓ control logic
Actuator
  ↓
Physical process

Security question:
Can an unauthorized change alter physical behavior?
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 11 — RTU

### Objective

Practice **RTU** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 12 — SCADA

### Objective

Practice **SCADA** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Field devices
  ↓
PLC / RTU
  ↓
SCADA server
  ↓
HMI / operator console
  ↓
historian / engineering workstation
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 13 — DCS

### Objective

Practice **DCS** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Process Area A ─┐
Process Area B ─┼─ Controllers ─ DCS Servers ─ Operator Stations
Process Area C ─┘
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 14 — HMI

### Objective

Practice **HMI** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Field devices
  ↓
PLC / RTU
  ↓
SCADA server
  ↓
HMI / operator console
  ↓
historian / engineering workstation
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 15 — Engineering Workstation

### Objective

Practice **Engineering Workstation** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 16 — Historian

### Objective

Practice **Historian** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 17 — SIS

### Objective

Practice **SIS** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Basic Process Control System
      ↓
Physical Process
      ↑
Safety Instrumented System

Security design must not reduce required safety independence.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 18 — Sensors

### Objective

Practice **Sensors** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 19 — Actuators

### Objective

Practice **Actuators** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 20 — Industrial Network Device

### Objective

Practice **Industrial Network Device** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 21 — Building Automation

### Objective

Practice **Building Automation** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 22 — Manufacturing OT

### Objective

Practice **Manufacturing OT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 23 — Energy OT

### Objective

Practice **Energy OT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 24 — Water OT

### Objective

Practice **Water OT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 25 — Transportation OT

### Objective

Practice **Transportation OT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 26 — Purdue Model Awareness

### Objective

Practice **Purdue Model Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Enterprise IT
   │
Level 5/4 — Business / Enterprise
   │
Industrial DMZ
   │
Level 3 — Site Operations
   │
Level 2 — Supervisory Control
   │
Level 1 — Basic Control
   │
Level 0 — Physical Process
```

Security boundaries should respect operational dependencies and safety.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 27 — Level 0

### Objective

Practice **Level 0** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 28 — Level 1

### Objective

Practice **Level 1** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 29 — Level 2

### Objective

Practice **Level 2** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 30 — Level 3

### Objective

Practice **Level 3** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 31 — Industrial DMZ

### Objective

Practice **Industrial DMZ** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Enterprise IT
    ↓
Firewall
    ↓
Industrial DMZ
 ├─ jump host
 ├─ patch relay
 ├─ historian replica
 └─ remote-access broker
    ↓
Firewall
    ↓
OT Operations Network
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 32 — Enterprise Zone

### Objective

Practice **Enterprise Zone** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 33 — OT Zone

### Objective

Practice **OT Zone** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 34 — Cell / Area Zone

### Objective

Practice **Cell / Area Zone** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 35 — Conduit

### Objective

Practice **Conduit** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 36 — Asset Inventory

### Objective

Practice **Asset Inventory** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Asset record:
owner
function
location
vendor/model
firmware
network zone
criticality
safety impact
support status
dependencies
backup/recovery owner
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 37 — Passive Asset Discovery

### Objective

Practice **Passive Asset Discovery** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
SPAN/TAP
  ↓
Passive OT sensor
  ↓
asset discovery
protocol metadata
baseline
anomaly / signature detection
  ↓
SOC / OT engineering review
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 38 — Active Scanning Risk

### Objective

Practice **Active Scanning Risk** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 39 — Asset Criticality

### Objective

Practice **Asset Criticality** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 40 — Process Dependency

### Objective

Practice **Process Dependency** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 41 — Single Point of Failure

### Objective

Practice **Single Point of Failure** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 42 — Legacy System

### Objective

Practice **Legacy System** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 43 — Long Lifecycle

### Objective

Practice **Long Lifecycle** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 44 — Vendor Dependency

### Objective

Practice **Vendor Dependency** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 45 — Proprietary Technology

### Objective

Practice **Proprietary Technology** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 46 — Modbus Awareness

### Objective

Practice **Modbus Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 47 — DNP3 Awareness

### Objective

Practice **DNP3 Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 48 — OPC Awareness

### Objective

Practice **OPC Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 49 — EtherNet/IP Awareness

### Objective

Practice **EtherNet/IP Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 50 — PROFINET Awareness

### Objective

Practice **PROFINET Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 51 — BACnet Awareness

### Objective

Practice **BACnet Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 52 — Serial Protocol Awareness

### Objective

Practice **Serial Protocol Awareness** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 53 — Protocol Authentication

### Objective

Practice **Protocol Authentication** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 54 — Protocol Encryption

### Objective

Practice **Protocol Encryption** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 55 — Write Command Risk

### Objective

Practice **Write Command Risk** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 56 — Read-Only Monitoring

### Objective

Practice **Read-Only Monitoring** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
SPAN/TAP
  ↓
Passive OT sensor
  ↓
asset discovery
protocol metadata
baseline
anomaly / signature detection
  ↓
SOC / OT engineering review
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 57 — Network Segmentation

### Objective

Practice **Network Segmentation** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Enterprise IT
    ↓
Firewall
    ↓
Industrial DMZ
 ├─ jump host
 ├─ patch relay
 ├─ historian replica
 └─ remote-access broker
    ↓
Firewall
    ↓
OT Operations Network
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 58 — Default Deny in OT

### Objective

Practice **Default Deny in OT** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 59 — Industrial Firewall

### Objective

Practice **Industrial Firewall** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Enterprise IT
    ↓
Firewall
    ↓
Industrial DMZ
 ├─ jump host
 ├─ patch relay
 ├─ historian replica
 └─ remote-access broker
    ↓
Firewall
    ↓
OT Operations Network
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 60 — Application / Protocol Allowlisting

### Objective

Practice **Application / Protocol Allowlisting** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
OT protocol review:
who initiates?
who responds?
is authentication present?
is encryption present?
is write/control possible?
what happens on malformed traffic?
```

Use passive review or vendor-approved lab testing for fragile systems.

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 61 — Jump Host

### Objective

Practice **Jump Host** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 62 — Remote Access Gateway

### Objective

Practice **Remote Access Gateway** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Vendor
  ↓ MFA
Remote-access gateway
  ↓ approval / time-bound access
Jump host
  ↓ recorded session
Specific OT asset

No direct vendor-to-controller path.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 63 — Vendor Remote Access

### Objective

Practice **Vendor Remote Access** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Vendor
  ↓ MFA
Remote-access gateway
  ↓ approval / time-bound access
Jump host
  ↓ recorded session
Specific OT asset

No direct vendor-to-controller path.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 64 — MFA for Remote Access

### Objective

Practice **MFA for Remote Access** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Vendor
  ↓ MFA
Remote-access gateway
  ↓ approval / time-bound access
Jump host
  ↓ recorded session
Specific OT asset

No direct vendor-to-controller path.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 65 — Shared Account Risk

### Objective

Practice **Shared Account Risk** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 66 — Role-Based Access

### Objective

Practice **Role-Based Access** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 67 — Privileged Access Management

### Objective

Practice **Privileged Access Management** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 68 — Password Management

### Objective

Practice **Password Management** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 69 — Service Account

### Objective

Practice **Service Account** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## Lab 70 — Portable Media

### Objective

Practice **Portable Media** using evidence and a documented decision process.

**OT safety boundary:** Use diagrams, packet captures from training labs, simulators, vendor documentation, or explicitly approved test environments. Do not actively scan, fuzz, exploit, or modify production controllers/PLCs.

### Procedure

1. Define scope and owner.
2. State the business/security/safety objective.
3. Identify applicable requirement, risk, or control.
4. Collect the minimum evidence needed.
5. Compare expected vs actual state.
6. Record assumptions and limitations.
7. Define remediation, acceptance, or next action.
8. Assign owner and due date.
9. Define retest/review evidence.
10. Record final status.

### Starter Example

```text
Physical Process
   ↑
Control / Supervision
   ↑
OT Network
   ↑
Industrial DMZ
   ↑
Enterprise IT

Protect safety, reliability, and process integrity first.
```

### Evidence Template

```text
Lab:
Scope:
Owner:
Objective:
Requirement / risk:
Expected:
Observed:
Evidence:
Gap / impact:
Decision:
Action:
Due date:
Retest / review:
```

---

## 6. Mini Project

# Mini Project — Secure a Manufacturing OT Environment

Design a fictional plant with:

```text
Enterprise IT
Industrial DMZ
OT operations network
two production cells
SCADA/HMI
PLCs
historian
engineering workstation
remote vendor support
safety system
```

Produce an OT asset inventory, Purdue-style diagram, zones/conduits matrix, remote-access design, passive-monitoring architecture, patch/change workflow, vulnerability register, backup/restore plan, removable-media process, vendor-access procedure, OT incident playbook, and recovery/tabletop scenario.

### Required Deliverables

1. Scope
2. Stakeholder / owner matrix
3. Architecture / governance diagram
4. Asset / process / obligation inventory
5. Risk or control register
6. Evidence repository
7. Gaps / findings
8. Treatment / remediation plan
9. Exceptions where applicable
10. Metrics
11. Review / retest criteria
12. Executive summary

---

## 7. Recommended Resources

- NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security — https://csrc.nist.gov/pubs/sp/800/82/r3/final
- CISA Cross-Sector Cybersecurity Performance Goals — https://www.cisa.gov/cybersecurity-performance-goals
- ISA/IEC 62443 overview — https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- MITRE ATT&CK for ICS — https://attack.mitre.org/matrices/ics/

---

## 8. Certification Relevance

Relevant to OT/ICS security engineer, industrial cybersecurity, critical infrastructure security, plant security, manufacturing security, OT SOC, and OT incident-response pathways.

---

## 9. Common Mistakes & Best Practices

### Common Mistakes

- Copying a framework without adapting it to business context.
- Treating risk matrices as mathematically precise.
- Confusing inherent and residual risk.
- Accepting risk without an accountable owner.
- Creating policies that cannot be evidenced or enforced.
- Collecting screenshots instead of reliable evidence.
- Letting control exceptions remain permanent.
- Treating OT like ordinary office IT.
- Making production OT changes without operations and safety approval.

### Best Practices

- Start from business/process objectives.
- Define ownership.
- Use repeatable risk scenarios.
- Map controls to explicit objectives.
- Keep evidence current.
- Separate design effectiveness from operating effectiveness.
- Track residual risk.
- Time-bound exceptions.
- Review continuously.
- In OT, preserve safety and availability first.

---

## 10. Self-Assessment Questions (with short answers)

### Q1. What is the key lesson from **Operational Technology Definition**?

**Short answer:** Operational Technology includes programmable systems and devices that monitor or control physical processes, equipment, environments, and infrastructure.

### Q2. What is the key lesson from **OT vs IT**?

**Short answer:** OT prioritizes safe, reliable physical operation and availability, while enterprise IT more often prioritizes information processing and confidentiality.

### Q3. What is the key lesson from **Cyber-Physical Risk**?

**Short answer:** OT cyber events can create physical consequences such as unsafe states, damaged equipment, environmental impact, quality loss, or production downtime.

### Q4. What is the key lesson from **Safety First**?

**Short answer:** Cybersecurity controls in OT must not undermine required safety functions or emergency procedures.

### Q5. What is the key lesson from **Reliability**?

**Short answer:** OT systems may need continuous deterministic operation for years with limited maintenance windows.

### Q6. What is the key lesson from **Availability**?

**Short answer:** Loss of availability can immediately stop production or critical infrastructure services.

### Q7. What is the key lesson from **Integrity**?

**Short answer:** Unauthorized changes to control logic, setpoints, recipes, or sensor values can create dangerous physical outcomes.

### Q8. What is the key lesson from **Confidentiality in OT**?

**Short answer:** Confidentiality still matters for engineering data, credentials, recipes, intellectual property, and safety/security configuration.

### Q9. What is the key lesson from **OT Asset Types**?

**Short answer:** OT environments include PLCs, RTUs, DCS, SCADA, HMIs, engineering workstations, historians, sensors, actuators, safety systems, and industrial network devices.

### Q10. What is the key lesson from **PLC**?

**Short answer:** Programmable Logic Controllers execute deterministic control logic close to the physical process.

### Q11. What is the key lesson from **RTU**?

**Short answer:** Remote Terminal Units collect telemetry and perform control in geographically distributed systems.

### Q12. What is the key lesson from **SCADA**?

**Short answer:** Supervisory Control and Data Acquisition systems provide remote monitoring and supervisory control across distributed assets.

### Q13. What is the key lesson from **DCS**?

**Short answer:** Distributed Control Systems coordinate process control across plant or process areas.

### Q14. What is the key lesson from **HMI**?

**Short answer:** Human-Machine Interfaces show process state and allow authorized operators to issue commands.

### Q15. What is the key lesson from **Engineering Workstation**?

**Short answer:** Engineering workstations configure controllers, logic, firmware, recipes, and industrial devices and are highly privileged OT assets.

### Q16. What is the key lesson from **Historian**?

**Short answer:** Process historians collect operational measurements and events for analysis, reporting, and business integration.

### Q17. What is the key lesson from **SIS**?

**Short answer:** Safety Instrumented Systems provide independent safety functions intended to drive a process to a safe state.

### Q18. What is the key lesson from **Sensors**?

**Short answer:** Sensors measure physical properties such as temperature, pressure, level, speed, position, or flow.

### Q19. What is the key lesson from **Actuators**?

**Short answer:** Actuators physically change valves, motors, relays, drives, and other equipment based on control commands.

### Q20. What is the key lesson from **Industrial Network Device**?

**Short answer:** Industrial switches, routers, firewalls, gateways, and serial converters provide OT connectivity.

### Q21. What is the key lesson from **Building Automation**?

**Short answer:** Building automation controls HVAC, elevators, lighting, access, and physical-environment systems.

### Q22. What is the key lesson from **Manufacturing OT**?

**Short answer:** Manufacturing OT integrates machines, robots, production lines, quality equipment, and supervisory systems.

### Q23. What is the key lesson from **Energy OT**?

**Short answer:** Energy OT includes generation, substations, distribution, pipelines, and related control systems.

### Q24. What is the key lesson from **Water OT**?

**Short answer:** Water and wastewater OT controls pumps, treatment, chemical dosing, reservoirs, and distribution.

### Q25. What is the key lesson from **Transportation OT**?

**Short answer:** Transportation OT includes signaling, fleet, traffic, rail, and other physical-control systems.

### Q26. What is the key lesson from **Purdue Model Awareness**?

**Short answer:** The Purdue-style model provides a common mental model for separating enterprise, site operations, supervisory control, basic control, and physical process layers.

### Q27. What is the key lesson from **Level 0**?

**Short answer:** Level 0 represents physical process sensors and actuators.

### Q28. What is the key lesson from **Level 1**?

**Short answer:** Level 1 represents basic control devices such as PLCs and drives.

### Q29. What is the key lesson from **Level 2**?

**Short answer:** Level 2 commonly contains HMIs and supervisory control.

### Q30. What is the key lesson from **Level 3**?

**Short answer:** Level 3 commonly supports site manufacturing/operations services.

### Q31. What is the key lesson from **Industrial DMZ**?

**Short answer:** An Industrial DMZ mediates communication between enterprise IT and OT operations without allowing uncontrolled direct trust.

### Q32. What is the key lesson from **Enterprise Zone**?

**Short answer:** Enterprise IT contains business systems, identity, email, user workstations, and corporate services.

### Q33. What is the key lesson from **OT Zone**?

**Short answer:** OT zones group systems by process, function, criticality, and communication need.

### Q34. What is the key lesson from **Cell / Area Zone**?

**Short answer:** Cell or area segmentation limits faults or compromise to a smaller process region.

### Q35. What is the key lesson from **Conduit**?

**Short answer:** A conduit is a controlled communication path between security zones.

### Q36. What is the key lesson from **Asset Inventory**?

**Short answer:** A reliable OT inventory records device type, owner, vendor/model, firmware, location, zone, criticality, and dependencies.

### Q37. What is the key lesson from **Passive Asset Discovery**?

**Short answer:** Passive observation is often safer than active scanning for fragile controllers or legacy devices.

### Q38. What is the key lesson from **Active Scanning Risk**?

**Short answer:** Active probes can destabilize some OT devices and require explicit owner/vendor approval and testing.

### Q39. What is the key lesson from **Asset Criticality**?

**Short answer:** Criticality should consider safety, environmental, production, quality, recovery, and cascading dependencies.

### Q40. What is the key lesson from **Process Dependency**?

**Short answer:** Cybersecurity teams must understand what physical process depends on each asset.

### Q41. What is the key lesson from **Single Point of Failure**?

**Short answer:** OT architectures should identify devices/services whose failure stops a process or defeats safety/recovery.

### Q42. What is the key lesson from **Legacy System**?

**Short answer:** Legacy OT may run unsupported operating systems, proprietary protocols, or fixed firmware that cannot be patched easily.

### Q43. What is the key lesson from **Long Lifecycle**?

**Short answer:** Industrial equipment can remain in service for decades, outlasting normal IT support cycles.

### Q44. What is the key lesson from **Vendor Dependency**?

**Short answer:** OT maintenance often depends on vendors for firmware, engineering software, support, and remote access.

### Q45. What is the key lesson from **Proprietary Technology**?

**Short answer:** Proprietary protocols and devices do not automatically provide security through obscurity.

### Q46. What is the key lesson from **Modbus Awareness**?

**Short answer:** Modbus is widely used for industrial communication and historically provides limited native security in many deployments.

### Q47. What is the key lesson from **DNP3 Awareness**?

**Short answer:** DNP3 is common in utilities and has legacy and secure authentication variants depending on implementation.

### Q48. What is the key lesson from **OPC Awareness**?

**Short answer:** OPC technologies support industrial interoperability; modern OPC UA provides stronger security capabilities than older designs when configured correctly.

### Q49. What is the key lesson from **EtherNet/IP Awareness**?

**Short answer:** EtherNet/IP carries Common Industrial Protocol traffic over standard Ethernet/IP networks and needs segmentation and monitoring.

### Q50. What is the key lesson from **PROFINET Awareness**?

**Short answer:** PROFINET is an industrial Ethernet technology with timing and operational characteristics that must be considered during security changes.

### Q51. What is the key lesson from **BACnet Awareness**?

**Short answer:** BACnet is common in building automation and requires careful segmentation and access control.

### Q52. What is the key lesson from **Serial Protocol Awareness**?

**Short answer:** Many legacy OT communications use serial protocols bridged into Ethernet environments.

### Q53. What is the key lesson from **Protocol Authentication**?

**Short answer:** Security teams should identify which industrial protocols authenticate commands and which rely mainly on network trust.

### Q54. What is the key lesson from **Protocol Encryption**?

**Short answer:** Encryption may not be available in legacy OT protocols and may require compensating network/security controls.

### Q55. What is the key lesson from **Write Command Risk**?

**Short answer:** Industrial write/control functions can directly change process behavior and need strict source and role restrictions.

### Q56. What is the key lesson from **Read-Only Monitoring**?

**Short answer:** Monitoring architectures should prefer passive/read-only approaches when possible.

### Q57. What is the key lesson from **Network Segmentation**?

**Short answer:** Separate enterprise IT, industrial DMZ, OT operations, process cells, safety, and vendor access according to communication need.

### Q58. What is the key lesson from **Default Deny in OT**?

**Short answer:** Where technically feasible, only required flows should cross OT security boundaries.

### Q59. What is the key lesson from **Industrial Firewall**?

**Short answer:** Industrial firewalls enforce zone-to-zone communication policy while respecting protocol and availability requirements.

### Q60. What is the key lesson from **Application / Protocol Allowlisting**?

**Short answer:** Restrict expected industrial protocols and endpoints rather than allowing broad internal access.

### Q61. What is the key lesson from **Jump Host**?

**Short answer:** Administrative access should pass through controlled jump hosts rather than direct enterprise-to-controller sessions.

### Q62. What is the key lesson from **Remote Access Gateway**?

**Short answer:** Remote access should terminate in controlled infrastructure with MFA, approvals, logging, and session limitation.

### Q63. What is the key lesson from **Vendor Remote Access**?

**Short answer:** Vendor access should be explicit, time-bound, monitored, and limited to named assets and purposes.

### Q64. What is the key lesson from **MFA for Remote Access**?

**Short answer:** Remote and privileged OT access should use strong authentication when supported by architecture.

### Q65. What is the key lesson from **Shared Account Risk**?

**Short answer:** Shared engineering or operator accounts reduce accountability and should be minimized where feasible.

### Q66. What is the key lesson from **Role-Based Access**?

**Short answer:** Separate operator, engineer, maintenance, vendor, and security permissions.

### Q67. What is the key lesson from **Privileged Access Management**?

**Short answer:** PAM can govern high-risk OT administrative credentials where compatible with operational constraints.

### Q68. What is the key lesson from **Password Management**?

**Short answer:** Legacy devices may have weak credential capabilities, requiring vaulting, rotation planning, and network compensating controls.

### Q69. What is the key lesson from **Service Account**?

**Short answer:** OT services and historians may use powerful accounts that require ownership and limited privileges.

### Q70. What is the key lesson from **Portable Media**?

**Short answer:** USB and removable media can introduce malware into isolated OT networks and need controlled processes.

### Q71. What is the key lesson from **Media Scanning Station**?

**Short answer:** Organizations may use dedicated scanning/kiosk processes before removable media enters sensitive OT zones.

### Q72. What is the key lesson from **Engineering Laptop**?

**Short answer:** Portable engineering laptops can bridge corporate, vendor, and OT environments and require strict hardening.

### Q73. What is the key lesson from **OT Endpoint Hardening**?

**Short answer:** Disable unnecessary services, apply allowlisting where appropriate, restrict admin rights, and protect engineering/HMI systems.

### Q74. What is the key lesson from **Application Allowlisting**?

**Short answer:** Allowlisting can be effective on stable OT hosts because software changes are relatively infrequent.

### Q75. What is the key lesson from **Antivirus / EDR Compatibility**?

**Short answer:** Endpoint security tooling must be tested for vendor support, performance impact, and deterministic operation.

### Q76. What is the key lesson from **Patch Management**?

**Short answer:** OT patching must consider vendor approval, compatibility, maintenance windows, rollback, and process impact.

### Q77. What is the key lesson from **Compensating Control**?

**Short answer:** When patches cannot be applied quickly, use segmentation, application allowlisting, source restriction, monitoring, or service disablement.

### Q78. What is the key lesson from **Firmware Management**?

**Short answer:** Controller/device firmware needs inventory, vendor advisories, integrity verification, and controlled upgrades.

### Q79. What is the key lesson from **Secure Configuration Baseline**?

**Short answer:** OT devices should have approved configurations covering accounts, services, protocols, logging, remote access, and network settings.

### Q80. What is the key lesson from **Configuration Backup**?

**Short answer:** Controller logic, HMI projects, network configuration, and system settings should be backed up and versioned.

### Q81. What is the key lesson from **Offline Backup**?

**Short answer:** Critical OT recovery copies should be protected from routine compromise paths.

### Q82. What is the key lesson from **Restore Testing**?

**Short answer:** A backup is useful only if teams can restore controller logic, servers, applications, and configurations under operational pressure.

### Q83. What is the key lesson from **Golden Configuration**?

**Short answer:** Known-good control logic and configuration provide a baseline for integrity comparison and recovery.

### Q84. What is the key lesson from **Change Management**?

**Short answer:** OT changes require owner approval, safety/operations coordination, backup, rollback, and post-change validation.

### Q85. What is the key lesson from **Emergency Change**?

**Short answer:** Emergency changes still need documentation, bounded scope, and retrospective review.

### Q86. What is the key lesson from **Maintenance Window**?

**Short answer:** Production changes should align with approved process windows and operational risk.

### Q87. What is the key lesson from **OT Vulnerability Management**?

**Short answer:** OT vulnerability management combines asset knowledge, vendor advisories, exposure, exploitability, safety, and compensating controls.

### Q88. What is the key lesson from **CVSS Limitation in OT**?

**Short answer:** Generic technical severity may not reflect physical safety, process availability, or real network exposure.

### Q89. What is the key lesson from **OT Risk Scenario**?

**Short answer:** Risk scenarios should connect cyber conditions to specific process and safety consequences.

### Q90. What is the key lesson from **Safety Impact Analysis**?

**Short answer:** Assess whether a cyber event could defeat alarms, interlocks, limits, or safe operating states.

### Q91. What is the key lesson from **Business Impact**?

**Short answer:** Downtime, scrap, quality loss, missed delivery, equipment damage, and regulatory impact can dominate OT risk.

### Q92. What is the key lesson from **Threat Sources**?

**Short answer:** OT threats include cybercriminals, state actors, insiders, suppliers, commodity malware, accidents, and operational mistakes.

### Q93. What is the key lesson from **Ransomware in OT**?

**Short answer:** Ransomware can stop OT operations indirectly by affecting Windows servers, identity, engineering systems, or business dependencies.

### Q94. What is the key lesson from **IT-to-OT Path**?

**Short answer:** Compromise often crosses from enterprise identity/workstations into OT through shared services, remote access, or poorly segmented networks.

### Q95. What is the key lesson from **Supply Chain Risk**?

**Short answer:** Industrial vendors, firmware, integrators, remote services, and engineering tools are part of the OT attack surface.

### Q96. What is the key lesson from **Physical Security**?

**Short answer:** Cabinets, ports, field devices, control rooms, and engineering stations require physical access controls.

### Q97. What is the key lesson from **Passive OT Monitoring**?

**Short answer:** Passive sensors can discover assets, protocols, baseline behavior, and anomalies without sending active probes.

### Q98. What is the key lesson from **OT IDS**?

**Short answer:** OT-aware monitoring can identify unusual protocol commands, new devices, communication changes, or known malicious patterns.

### Q99. What is the key lesson from **Network Baseline**?

**Short answer:** Document normal peers, protocols, command types, polling intervals, and engineering activity.

### Q100. What is the key lesson from **Anomaly Detection**?

**Short answer:** Unexpected write commands, new devices, unusual engineering access, or changed communication patterns require investigation.

### Q101. What is the key lesson from **Log Collection**?

**Short answer:** Collect firewall, Windows, authentication, engineering, remote-access, network, and application logs where supported.

### Q102. What is the key lesson from **Time Synchronization**?

**Short answer:** Accurate OT timestamps improve process troubleshooting and incident investigation.

### Q103. What is the key lesson from **Historian as Evidence**?

**Short answer:** Process historians can provide operational context for cyber investigations but are not substitutes for security logs.

### Q104. What is the key lesson from **OT SOC Integration**?

**Short answer:** SOC processes should include OT-specific ownership, severity, escalation, and safety constraints.

### Q105. What is the key lesson from **OT Incident Response**?

**Short answer:** Incident response must coordinate cyber teams with operators, engineers, safety, vendors, and business continuity.

### Q106. What is the key lesson from **Containment in OT**?

**Short answer:** Containment should avoid actions that unexpectedly stop safe control or destroy process visibility.

### Q107. What is the key lesson from **Controller Isolation Risk**?

**Short answer:** Disconnecting a controller may be more dangerous than monitoring it; operations must lead process-safety decisions.

### Q108. What is the key lesson from **Manual Operations Awareness**?

**Short answer:** Some facilities have manual fallback procedures that should be validated as part of resilience.

### Q109. What is the key lesson from **Safety Shutdown**?

**Short answer:** Cyber response must understand when safety systems or controlled shutdown procedures are required.

### Q110. What is the key lesson from **Evidence Preservation**?

**Short answer:** Preserve controller logic, engineering logs, network captures, system images, and change records where possible.

### Q111. What is the key lesson from **Recovery**?

**Short answer:** Restore known-good logic/configuration, validate field/process state, reintroduce systems carefully, and monitor.

### Q112. What is the key lesson from **Cyber-Physical Tabletop**?

**Short answer:** Tabletops should include security, control engineers, operators, safety, management, and vendors.

### Q113. What is the key lesson from **Business Continuity for OT**?

**Short answer:** Continuity planning should address manual workarounds, spare parts, vendor support, alternate production, and recovery dependencies.

### Q114. What is the key lesson from **Spare Parts**?

**Short answer:** Legacy systems may require stored replacement controllers, network devices, storage, licenses, or images.

### Q115. What is the key lesson from **Secure Decommissioning**?

**Short answer:** Remove credentials, logic, sensitive configuration, and network access when industrial assets are retired.

### Q116. What is the key lesson from **OT Governance**?

**Short answer:** Define accountable OT cybersecurity ownership spanning operations, engineering, IT, security, safety, and management.

### Q117. What is the key lesson from **OT Policy**?

**Short answer:** Policies should reflect OT safety, change, remote access, removable media, asset, vulnerability, backup, and incident-response needs.

### Q118. What is the key lesson from **NIST SP 800-82 Rev. 3 Awareness**?

**Short answer:** NIST SP 800-82 Rev.

### Q119. What is the key lesson from **IEC 62443 Awareness**?

**Short answer:** IEC 62443 provides a family of standards addressing industrial automation and control-system security across asset owners, integrators, and products.

### Q120. What is the key lesson from **CISA CPGs Awareness**?

**Short answer:** CISA Cybersecurity Performance Goals provide prioritized practices relevant to both IT and OT critical-infrastructure environments.

### Q121. What is the key lesson from **OT Security Final Mental Model**?

**Short answer:** OT security protects safe and reliable physical operation through asset knowledge, controlled trust boundaries, strong remote access, tested changes, passive visibility, recovery readiness, and engineering-security collaboration.

---

## Completion Checklist

- [ ] I completed the core topics.
- [ ] I completed at least 35 labs.
- [ ] I completed the mini project.
- [ ] I can identify owners, risks, controls, and evidence.
- [ ] I can explain residual risk.
- [ ] I can document gaps and remediation.
- [ ] I can define review/retest criteria.
