# Robotics Engineering — Stage 06: Choose and Complete One Specialization

**Companion to:** *Complete Robotics Engineering Roadmap* + Stages 01–05  
**Primary window:** **months 23–36** at **12–18 focused h/week**  
**Choice:** A — Industrial Robotics **OR** B — Rugged-Field/Defense-Adjacent (Non-Weaponized) **OR** C — IoT/IIoT Robotics Integration  
**Gate:** **P12** — chosen-track capstone; **P13** — required at W→P depth for IoT-primary learners, optional E/W extension otherwise  
**What “P” means:** focused proficiency on **one bounded, evidenced, reviewed system**, **not** production commissioning authority, a professional license, a safety certification, or domain-wide mastery.

> **Unchanged scope boundary:** The field/defense-adjacent branch is limited to **logistics, inspection, remote sensing, search-and-rescue support, and survey/hazard mapping**. It **excludes weapon integration, target selection, and autonomous engagement**. Study only public, non-controlled material; actual defense-sector requirements, controlled data, export controls, security/access permissions, qualification and deployment decisions require proper employer/program authorization and legal/security review. No self-study artifact substitutes for them.

> **Invariant across ALL tracks:** local independent safety-critical stop/control functions must **never depend on cloud/Internet connectivity, a dashboard, an LLM or an ordinary ROS 2 node**. A hobby test matrix, a simulated workcell, a mentor review or a home-built environmental test is **not certification or deployment authorization**.

## 0. Where Stage 06 sits in the seven-stage graph

```text
Stage 01  Math / software / frames / CAD            → P01–P03
Stage 02  Electronics / embedded / bounded PID      → P04–P05
Stage 03  ROS 2 / robot modeling / simulation        → P06–P07
Stage 04  Fusion / perception / ONE planner         → P08–P11
                                                     │
                                                     ▼
Stage 06  CHOOSE ONE primary specialization (23–36 months)
          ├─ A. Industrial robotic workcell          → P12
          ├─ B. Non-weaponized rugged-field system   → P12
          └─ C. IoT / IIoT robot-fleet integration   → P13 + P12

Stage 05  Optional mathematics ← pull only if a real blocked task needs it
Stage 07  Tests / documentation / reviews / budgets / safety ← always parallel
```

### Scope and time contract

| Intended outcome | Honest time horizon | Depth language |
|---|---:|---|
| One chosen track after P11 | **30–36 months total** | W→P in one bounded capstone; other tracks E |
| Two substantial tracks | **~40–48 months total** | P first; W→P second according to genuine evidence/access |
| All three | **~48–60+ months total** | Do not claim equal P in all three automatically |
| 24-month route | 24 months total | Core W + one track **orientation**, not specialization P |

**No double-counting:** a robot with one dashboard is not, by itself, both an industrial and IoT proficiency capstone. Reuse the robot/repo when sensible, but build distinct interface, failure, acceptance and review evidence for each claimed specialization.

## 1. Entry gate: do not start deep specialization just because the calendar says month 23

- [ ] P01–P03: correct units, motor sizing, frames, FK/IK/Jacobian and documented CAD.
- [ ] P04–P05: protected motor/axis or explicitly simulation-only substitute; controlled timing, saturation and stale-command behavior.
- [ ] P06–P07: reproducible ROS 2 workspace and robot simulation with `tf2`, URDF/Xacro and `ros2_control` where relevant.
- [ ] P08: compared localization/fusion result to a baseline with timestamp and uncertainty evidence.
- [ ] P09: **one** working Nav2 *or* MoveIt 2 scenario with bounded recovery; the other may remain E.
- [ ] P10: a bounded inspection/geometric perception pipeline with held-out or changed-condition evaluation.
- [ ] P11: integrated prototype; state-machine/fault handling; operator supervision; clear physical vs simulated evidence labels.
- [ ] Frozen stack and clean clone/reproduction instructions; no hidden datasets or credentials.
- [ ] Hardware/simulation hazards, separate safety boundary, public/non-controlled data scope defined.

**Entry failure:** spend 4–8+ recovery weeks on the blocking gate and shift Stage 06 accordingly. Stage 05 advanced math is *not* an automatic prerequisite.

## 2. Pick the track by work you want to demonstrate

| Decision question | A. Industrial robotics | B. Rugged field, non-weaponized | C. IoT/IIoT integration |
|---|---|---|---|
| Main system | One virtual production cell | One supervised benign logistics/inspection robot | One managed simulated/low-energy robot fleet |
| Main engineering uncertainty | PLC/robot process synchronization, quality, recovery | operating envelope, localization/links, endurance, field service | identity, schema, fleet updates, offline cloud boundary |
| Minimum useful setting | Virtual workcell / training cell | Indoor test route and simulation | 3+ simulated identities and local/cloud broker |
| Final portfolio evidence | cycle time, rejects, I/O and recovery trace | reliability/fault trial, localization and energy logs | fleet dashboard, identity/auth, OTA and WAN-loss proof |
| Physical facility dependence | Real commissioning requires qualified plant access | Environmental/field qualification requires controlled facilities | Production PKI, fleet and security operations require organizational access |
| Natural second-track extension | C for connected factories | C for fleet diagnostics | A or B for the robot domain, with more time |

**Choose by the problems, datasets, robots and reviewers you can actually access.** For a glass-manufacturing context, a simulated inspection/sorting cell can leverage domain knowledge; for AI/backend/cloud interests, fleet integration connects robotics with data and distributed systems. This is not a recommendation to pursue two tracks in 14 months.

## 3. The shared 14-month specialization operating plan

| Period | Shared work | Stage-specific result | Review / gate |
|---|---|---|---|
| Month 23 | Define user, environment, prohibited functions and success metric | One-page bounded requirement and operating envelope | Scope/hazard review |
| Month 24 | Interface map, baseline prototype, risk/FMEA or threat model | Track orientation demonstration | P11-to-P12/P13 review |
| Months 25–26 | Domain fundamentals, first integrated sequence and simulated faults | Track mini-project #1/#2 | Domain specialist reviews assumptions |
| Months 27–28 | Add one meaningful subsystem/interface, logging and acceptance metrics | Beta architecture, repeatable setup | External architecture critique |
| Months 29–30 | Improve one bottleneck, complete failures and maintenance/security analysis | Frozen capstone acceptance plan | Formal design review *method* (not certification) |
| Months 31–32 | Integrate P12 and, on C, the P13 fleet gate | End-to-end prototype + fault tests | Acceptance dry run |
| Months 33–34 | Repeated trials, corrective actions, adversarial but safe cases | Results, before/after measurements | Domain + systems/security reviewer |
| Months 35–36 | Stabilize, independently reproduce, publish only permitted artifacts | P12 portfolio; P13 for C | Final gate/rework buffer |

**Milestone estimates, not automatic promotions.** Months 31–36 are protected for integration, measurement, rework and review. Run Stage 05 only for a demonstrated blocker. Stage 07 habits run throughout.

### Weekly 15-hour allocation — shift emphasis with capstone phase

| Activity | 23–26 | 27–30 | 31–36 |
|---|---:|---:|---:|
| Domain knowledge / just-in-time mathematics | 3 h | 2 h | 1 h |
| Software, wiring/CAD or platform integration | 5 h | 5 h | 4 h |
| Capstone building and controlled experiments | 4 h | 5 h | 6 h |
| Docs, test automation, external review and safety | 3 h | 3 h | 4 h |

**Every 4 weeks:** runnable demo + a failed case + a chart + a reviewable commit. **Every ~12 weeks:** independent review request and a rework buffer. No “course completed” item substitutes for P12/P13 evidence.

---

# TRACK A — INDUSTRIAL ROBOTICS (manufacturing and automation)

## A0. Track mission and valid boundary

Build a **simulated manufacturing workcell** for benign inspection, pick/place, handling or sorting; understand industrial control and cell-engineering vocabulary; validate process/fault logic and measure throughput/quality. A real production cell needs vendor training, supervised access, qualified site safety engineering, applicable standards and commissioning authorization.

**Recommended bounded capstone example:** virtual glass-container inspection and sorting: part arrival → identity/traceability → inspection → PASS/FAIL → simulated robot pick/place → count/OEE-style metrics → fault/recovery. This is a *project option*, not a prerequisite.

## A1. Detailed learning path and evidence

### A1.1 Requirements, process flow and machine states (months 23–24)

- [ ] Select one workcell task with product, cycle, handling, reject and human-access boundaries.
- [ ] Draw product/process flow and identify all interfaces and permitted operating modes.
- [ ] Define production cycle-time target, quality metric and availability measure.
- [ ] Draft I/O list: sensor type, source, normal state, diagnostic state, signal owner.
- [ ] Draw machine states: Off, Ready, Start, Run, Hold, Fault, Recovery, Maintenance.
- [ ] Distinguish a normal process hold from an independently engineered protective stop.
- [ ] Specify restart prevention after faults/human access.
- [ ] Write a preliminary hazard log; mark each unverified safety assumption.
- [ ] Build a virtual line layout and check nominal work envelope and clearance.
- [ ] Review with a controls/integration mentor before adding physical automation.

### A1.2 PLC fundamentals and sequence logic (months 24–26)

- [ ] IEC 61131-3 vocabulary: program, function, function block and task cycle.
- [ ] Read/write simple ladder logic or structured text in **one** chosen simulator.
- [ ] Model normally open/closed inputs and why signal inversion is risky.
- [ ] Build edge detection, timers, counters, latches and explicit resets.
- [ ] Separate permissives, interlocks, operating modes and fault acknowledgment.
- [ ] Implement a debounced arrival sensor and product ID state.
- [ ] Write a finite-state sequence with bounded transitions and timeouts.
- [ ] Simulate stuck sensor, missing part, duplicate arrival and actuator nonresponse.
- [ ] Log state, timestamp, signal and reason for every abnormal transition.
- [ ] Demonstrate clean restart and prevention of unexpected automatic movement.

### A1.3 Robot controller and cell geometry (months 25–27)

- [ ] Select **one** robot/controller ecosystem for orientation; avoid learning four programming syntaxes in parallel.
- [ ] Explain base/tool/work-object frames and TCP calibration concept.
- [ ] Check the chosen virtual robot's reach, joint limits and tool clearance.
- [ ] Select a benign end-effector model and payload; document mass and COM.
- [ ] Design pick, transfer, place, retreat and home states in simulation.
- [ ] Handle unreachable pose and grasp failure without endless retries.
- [ ] Link robot program state to PLC `ready/busy/done/fault` handshake.
- [ ] Log frame IDs, part ID, status and cycle time for each motion sequence.
- [ ] Distinguish teaching/jog concepts from authorized physical robot operation.

### A1.4 Interfaces, plant data and vision (months 27–30)

- [ ] Explain 24 V I/O, network segregation and who owns each signal.
- [ ] Choose **one** lab/simulated integration method: explicit I/O handshake or OPC UA interface.
- [ ] Create a stable interface contract: names, values, units, timestamps and error codes.
- [ ] Define edge cases: lost message, stale status, repeated command and reconnect.
- [ ] Document fieldbus concepts (EtherCAT/PROFINET etc.) at E unless the actual platform demands one.
- [ ] Add camera/quality input from P10 or simulated inspection outcomes.
- [ ] Separate false reject, false accept and mechanical handling failure in reports.
- [ ] Link work order/part ID → result → robot cycle → timestamp → configuration version.
- [ ] Record a baseline cycle-time distribution before optimizing it.
- [ ] If cloud/IIoT is added, send **non-safety** monitoring data only; keep cell protection independent.

### A1.5 Standards and site-readiness literacy (all months; deeper by 30)

- [ ] Study risk-assessment method before proposing protective measures.
- [ ] Distinguish robot product and robot-application/cell responsibilities.
- [ ] Learn guarding, interlocking, lockout/tagout and safe maintenance *concepts*.
- [ ] Recognize ordinary PLC I/O vs safety-related control components.
- [ ] Recognize performance-level / SIL terms without making safety-rating claims.
- [ ] Read public catalog scopes for ISO 10218-1/-2, ISO 12100, ISO 13849-1, IEC 62061 and IEC 62443 as relevant.
- [ ] Check applicable scope and edition at **real** design time; obtain full licensed/current standards via the responsible organization.
- [ ] Record why excluded sectors cannot be assumed certified by industrial-robot standards.
- [ ] Require a competent, authorized safety/site reviewer for physical work.

**Standards are periodically revised.** A public preview, virtual simulation or homemade fault test cannot demonstrate a required PL/SIL or certify a cell.

## A2. Industrial project ladder and acceptance

| Project | Time | Deliverable | Mandatory failure case |
|---|---|---|---|
| **I1 — virtual cell** | 23–25 | workcell layout, product model, process states | unavailable part / unreachable pose |
| **I2 — PLC/robot handshake** | 25–28 | I/O contract + request/ready/busy/done/fault timing trace | missed/repeated command and timeout |
| **I3 — vision + traceability** | 27–30 | PASS/FAIL pipeline with product ID and quality metrics | false reject or stale inspection event |
| **P12-A — bounded industrial capstone** | 31–36 | integrated virtual cell, measured cycle time/quality/recovery dossier | chosen sensor/robot/handshake faults + restart |

### P12-A: industrial capstone checklist

- [ ] Requirements, process layout, I/O map and documented mode/state model.
- [ ] One simulated cell and **one** robot/control interface with reproducible launch.
- [ ] CAD or virtual cell layout, TCP/work-object frames and realistic payload assumptions.
- [ ] Robot/PLC sequence trace for normal production and failure/recovery.
- [ ] Predeclared cycle-time, false-reject and uptime/availability-style metrics.
- [ ] More than one repeated trial; record distribution, not a single best run.
- [ ] Stale signal, missing part, simulated power/connection fault and blocked restart tests.
- [ ] Risk-assessment **exercise** identifying unverified protective measures and physical gaps.
- [ ] Traceability from part/job → result → machine state → logs and version.
- [ ] Reviewer comments addressed; another person can run the virtual cell.
- [ ] Portfolio states **virtual or bench scope**; no production/safety certification claim.

**If behind at month 30:** keep one PLC language, one virtual robot, one handshake, fault states and measurable quality/cycle outcomes; defer second vendor, second fieldbus, fancy AI, cloud fleet and real commissioning.

---

# TRACK B — RUGGED-FIELD / DEFENSE-ADJACENT (NON-WEAPONIZED)

> **Keep this scope exact:** logistics, inspection, remote sensing, search-and-rescue support, and survey/hazard mapping. **No weapon integration, target selection or autonomous engagement.** The educational work below is not a military program, defense qualification, operational plan or authorization for outdoor/airborne testing.

## B0. Track mission and sample platform

Choose **one**: low-energy ground rover for benign indoor logistics/inspection; simulated civilian inspection aircraft (flight simulation only unless qualified/authorized); benign teleoperated cargo manipulator; or field environmental sensor node. **The default capstone is a small human-supervised indoor rover.** Do not treat simulation of degraded environments as permission to evade interference or operate outside permitted environments.

## B1. Detailed learning path and evidence

### B1.1 Environment, requirements and limits (months 23–24)

- [ ] Define payload as benign cargo/equipment, location as permitted route or simulation.
- [ ] Write speed, payload, endurance, incline, clearance and turning-radius assumptions.
- [ ] Draw system boundary: robot, operator, environment, comms, local stop and power.
- [ ] Create operating envelope and prohibited conditions; include human proximity.
- [ ] Create hazard log and FMEA: mechanical, battery, motor, sensor, comms, software, human error.
- [ ] Rank failures using a documented **project-specific** qualitative method; do not invent an official certification score.
- [ ] Write expected responses for faults: stop, hold, return on authorized request or operator takeover.
- [ ] Estimate energy and thermal duty cycle and mark untested assumptions.
- [ ] Identify permission, radio/flight/site/security/export issues for any *real* work.

### B1.2 Non-weaponized logistics and cargo workflow (months 24–26)

- [ ] Define task request → acceptance → load verification → supervised route → handoff → return/recovery.
- [ ] Calculate payload mass, COM shift and traction/braking assumptions.
- [ ] Model modest slopes, floor friction and wheel slip in simulation.
- [ ] Design simple load securing and low-energy docking/handoff concept.
- [ ] Implement destination and cargo state machine with clear operator supervision.
- [ ] Simulate a 2–4 vehicle logistics fleet **only as a benign logistics exercise** if time permits.
- [ ] For leader/convoy-following *concepts*, learn relative position, spacing and **loss-of-leader safe stop** in controlled simulation; do not create tactical/autonomous-combat guidance.
- [ ] Measure route time, load handling success, battery estimate and recovery time.

### B1.3 Localization and degraded sensing (months 26–29)

- [ ] Begin with P08 baseline; preserve known frame and timestamp conventions.
- [ ] Use encoder/IMU estimate and a known simulated reference route.
- [ ] Explain what GNSS is and why indoor or obstructed operation may lack it.
- [ ] Simulate GNSS unavailability; compare state uncertainty and position error.
- [ ] Introduce one permissible local aid: fiducials, map, vision or lidar localization.
- [ ] Reject impossible pose jumps and mark stale/conflicting sensors.
- [ ] Define an explicit localization-confidence threshold for reduced-speed/hold behavior in the simulation envelope.
- [ ] Plot drift, uncertainty and response to a degraded sensor against ground truth.
- [ ] Keep full factor-graph/particle-filter internals in Stage 05 unless the **measured** problem needs them.

### B1.4 Communications and safe degraded operation (months 27–30)

- [ ] Define operator link, telemetry link and any non-critical remote-service link separately.
- [ ] Model latency, disconnection and packet loss in a local lab/simulator.
- [ ] Detect stale commands and enter documented bounded safe behavior locally.
- [ ] Buffer non-critical telemetry and mark replayed data delayed.
- [ ] Show that a remote dashboard is not needed for local stop/override.
- [ ] Use only lawful/authorized wireless settings if using real radios; simulate all unavailable-link cases safely.
- [ ] Understand EMCON as **organization-controlled emissions policy awareness**, not self-directed operational RF design.
- [ ] Treat jamming/interference as a possible *loss-of-service condition*; do not build anti-jam or countermeasure-defeat techniques.
- [ ] Log loss-of-link detection and operator handover results.

### B1.5 Environmental and maintainability engineering (months 28–32)

- [ ] Define expected storage, transport, use and maintenance environments separately.
- [ ] List relevant temperature, rain/humidity, dust/sand, shock and vibration stresses.
- [ ] Study **MIL-STD-810H** categories and tailoring **conceptually**; recheck current issue/change status in DLA ASSIST for real program work.
- [ ] Understand what an ingress rating is; never infer actual ingress resistance from a CAD enclosure.
- [ ] Sketch connector, seal, strain-relief, cable routing and corrosion protection decisions.
- [ ] Derate power/actuation assumptions under temperature and duty-cycle changes.
- [ ] Document service access, consumables, spares, inspection and repair steps.
- [ ] Use synthetic disturbance inputs where lab capability is missing; label tests simulated.
- [ ] Record pre/post-test functionality for any approved benign bench trial.
- [ ] Do not perform unsupervised harsh-environment, hazardous battery or radio tests.

### B1.6 Interoperability, safety and legal/public-literacy (months 23–36)

- [ ] Know the name/purpose of **NATO NGVA / STANAG 4754 / AEP-4754** at the architectural level.
- [ ] Study modular vehicle interfaces and configuration control, not an invented compliance implementation.
- [ ] Study **MIL-STD-882E** as a system-safety process reference and reverify current change status.
- [ ] Read public DoD unmanned-system safety guidance at a conceptual level.
- [ ] Identify which documents are public, restricted or program-controlled; do not infer access rights.
- [ ] Know ITAR/EAR exist and that classification depends on item, data, end user, end use and transaction.
- [ ] Never post controlled/proprietary technical material to open source, public AI or forums without organizational authorization.
- [ ] State what real work would require: employer/program approval, relevant clearances/access, security/export/legal review, qualified testing, permits and formal acceptance.
- [ ] Reverify versions, distribution statement and contractual applicability before **actual** program work.

**Public-reference literacy is not conformance.** Home-made environmental/RF tests are not MIL-STD-810 qualification; safety reviews are not MIL-STD-882 acceptance; reading NGVA is not interoperability certification. Industrial ISO 10218 applicability must not be assumed for defense/other excluded systems.

## B2. Field project ladder and acceptance

| Project | Time | Deliverable | Mandatory failure case |
|---|---|---|---|
| **F1 — requirements + endurance** | 23–25 | hazard log, FMEA, power/thermal and safe envelope | overload/low-energy assumption |
| **F2 — benign logistics route** | 25–28 | indoor/simulated cargo cycle + operator role | blocked route or failed handoff |
| **F3 — degraded conditions** | 27–30 | sensor/link-loss recovery with logs and uncertainty | missing GNSS, stale command, lost link |
| **P12-B — bounded non-weaponized field capstone** | 31–36 | human-supervised inspection/logistics rover and maintenance evidence | repeatable critical faults and safe recovery |

### P12-B: field capstone checklist

- [ ] Explicit **non-weaponized** use case and authorized test environment.
- [ ] Defined payload, operating envelope, autonomy level and operator role.
- [ ] Simulation-first route with benign object delivery or equipment inspection.
- [ ] Energy, payload/COM, traction and stoppability assumptions documented.
- [ ] Baseline vs degraded localization results with frame/timestamp checks.
- [ ] Link-loss and stale-command tests demonstrating **local** bounded safe behavior.
- [ ] Repeat trials with time, task success, recovery and energy metrics.
- [ ] FMEA, maintenance/repair plan, versioned configuration and fault log.
- [ ] Environmental test plan distinguishes **simulated** stresses from qualified facility testing.
- [ ] Public standards map says **literacy only**, no compliance/qualification claim.
- [ ] Public/non-controlled portfolio contents and disclosure constraints reviewed.
- [ ] Reviewer challenge addressed; independent reproduction achieved.

**If behind at month 30:** use one small indoor rover, one route, one benign payload and one simulated loss-of-link/GNSS scenario. Preserve local stop, uncertainty, FMEA, serviceability and legal boundary. Defer multi-rover fleet, formal STANAG implementation, multiple radios, broad weather matrix and expensive sensors.

---

# TRACK C — IoT / INDUSTRIAL IoT ROBOTICS INTEGRATION

## C0. Track mission and architecture boundary

Turn an already functional simulated/low-energy robot into a **managed non-safety-critical fleet asset**. Select **one** IoT platform (local ThingsBoard/MQTT lab, AWS IoT Core, or Azure IoT Hub family) and model **at least three unique robot identities**. P13 is a **required primary-track W→P gate**; P12-C wraps its fleet result into a documented end-to-end capstone.

```text
Independent energy isolation / local safety controls
                   ↑ (never routed through IoT)
Motor controller + local watchdog + operator override
                   ↑
             ROS 2 robot
                   │ filtered NON-CRITICAL state only
                   ▼
          edge telemetry bridge
                   ▼
          MQTT / IoT platform ── dashboard / history / MES
                   │
                   └── NON-SAFETY configuration and staged update workflow
```

## C1. Detailed learning path and evidence

### C1.1 Messaging contract and network boundaries (months 23–25)

- [ ] Explain ROS 2/DDS as local robotics data exchange with QoS; it is not inherently safety-rated.
- [ ] Explain MQTT brokered pub/sub, topic namespace and QoS **without equating MQTT QoS to hard real time**.
- [ ] Explain CoAP constrained request/response/observe concept; use it only if relevant.
- [ ] Identify actual source node for robot health, battery, task and fault status.
- [ ] Define bridge allowlist; **never bridge the entire ROS graph automatically**.
- [ ] Document serialization/schema/version and field units.
- [ ] Include measurement/source timestamp, arrival timestamp, quality and stale indicator.
- [ ] Design robot/fleet/topic hierarchy without exposing secrets or personal data.
- [ ] Select telemetry rate/retention to avoid cost and overload.
- [ ] Simulate broker/WAN loss without affecting local control.

### C1.2 One platform and fleet inventory (months 25–27)

- [ ] Choose AWS IoT Core **or** Azure IoT Hub family **or** local ThingsBoard; others E.
- [ ] Create device registry/inventory for ≥3 simulated robot IDs.
- [ ] Define site, fleet, model, hardware revision and software/config version.
- [ ] Set up ingestion and one dashboard displaying per-robot health and faults.
- [ ] Distinguish command proposal from authorized local action.
- [ ] Simulate each device independently with its own status and clock.
- [ ] Document usage/retention budget; enable spend alerts if using managed cloud.
- [ ] Export simple telemetry for repeatable offline analysis.

### C1.3 Identity, authentication and fleet authorization (months 26–29)

- [ ] Give each robot a unique logical identity; avoid shared fleet-wide credentials.
- [ ] Learn X.509 or platform identity alternatives at a conceptual/practical lab level.
- [ ] Define device onboarding and least-privilege topic/API policy.
- [ ] Separate operator, cloud service and device permissions.
- [ ] Keep credentials out of git, screenshots, exported logs and images.
- [ ] Test denied cross-device topic read/write.
- [ ] Test expired/revoked credential; **no anonymous fallback**.
- [ ] Record key rotation/reprovisioning and decommissioning process.
- [ ] Document production gaps: secure element/TPM, PKI, HSM, audits and organizational IAM.

### C1.4 Telemetry, twins, offline state, enterprise mapping (months 28–31)

- [ ] Define digital twin as last-known/reported operational representation, **not safety ground truth**.
- [ ] Track software version, calibration version, reported health and desired non-critical config.
- [ ] Distinguish desired vs reported state and detect non-convergence.
- [ ] Buffer noncritical measurements with bounded storage and replay policy.
- [ ] Mark disconnected robots stale and show age of last contact.
- [ ] Build uptime, utilization, defect/inspection count or maintenance chart.
- [ ] Link robot/job ID and quality event to source timestamp and configuration.
- [ ] Explain OPC UA/ISA-95 style OT/MES boundaries conceptually; gateway only on approved network.
- [ ] Show dashboard/cloud loss does not prevent physical local stop or supervision.

### C1.5 Fleet-scale OTA/update strategy (months 30–34)

- [ ] Distinguish single MCU firmware flashing from fleet rollout orchestration.
- [ ] Version and authenticate update artifacts and compatibility metadata.
- [ ] Use a simulated container/robot software update if no safe device is available.
- [ ] Define canary one-device update → health check → next group.
- [ ] Define abort thresholds, maintenance window and update-rate limits.
- [ ] Simulate bad version, interrupted download and failed post-update health check.
- [ ] Demonstrate rollback **or explicitly documented known-good recovery**.
- [ ] Log who triggered update, target identities, old/new versions and outcome.
- [ ] Prove the robot's independent local stop still works with platform disconnected or update failed.
- [ ] Document production gaps: hardware root of trust, secure boot, bootloader design, emergency rollout governance.

### C1.6 Security, observability and cost (months 23–36)

- [ ] Draw trust boundaries from sensor/ROS graph to bridge/broker/cloud/MES.
- [ ] Define device/service/operator roles and least privilege.
- [ ] Monitor connection errors, schema errors, update failures and anomalous traffic.
- [ ] Store audit and test logs without leaking tokens or keys.
- [ ] Test reconnect/backoff and avoid unbounded message queues.
- [ ] Distinguish safety-critical local control from remotely proposed task coordination.
- [ ] Measure cloud/broker availability independently from robot safety status.
- [ ] Document message count, retention, storage and monthly cost assumptions.
- [ ] Request cloud/security review; request separate controls review for an industrial gateway.

## C2. IoT project ladder and acceptance

| Project | Time | Deliverable | Mandatory failure case |
|---|---|---|---|
| **C1 — local telemetry bridge** | 23–26 | versioned ROS-to-MQTT/IoT **allowlisted** contract | malformed/stale measurement |
| **C2 — managed 3-device fleet** | 26–30 | independent device identity, policy, inventory, dashboard | expired credential; cross-device access denial |
| **P13 — robot-to-IoT fleet integration** | 31–34 | OTA + auth + offline + auditing in a reproducible ≥3-device lab | broker/WAN loss, bad update, revoke credential |
| **P12-C — bounded IoT fleet capstone** | 34–36 | requirements-to-test handoff, enterprise mapping and independently reproduced fleet demonstration | repeat the combined fault suite |

### P13: required evidence checklist for IoT primary track

- [ ] Diagram separates independent local safety, ROS 2, edge bridge, broker/cloud and dashboard/MES.
- [ ] Versioned telemetry schema with units, quality indicators and timestamps.
- [ ] ≥3 unique identities, correctly scoped permissions and onboarding instructions.
- [ ] Fleet dashboard: health, uptime/energy, software/config version and fault state.
- [ ] Loss of Internet/broker does **not** prevent independent local stop or local safe behavior.
- [ ] Buffered/stale data displays distinguish delayed telemetry from live state.
- [ ] Per-device auth failure and revoked credential tested, without anonymous fallback.
- [ ] Canary/group update with artifact verification, audit and abort/rollback or known-good recovery.
- [ ] A reproducible simulated fleet with no hard-coded secrets.
- [ ] External IoT/security review + explicit production limitations.

### P12-C: final capstone acceptance

- [ ] One bounded fleet user story with business/maintenance outcome and acceptance criteria.
- [ ] P13 passed at W→P on documented synthetic or safe hardware scope.
- [ ] MES/SCADA/Industry 4.0 integration map clearly labels conceptual vs tested interfaces.
- [ ] 3+ device demonstration, repeat fault suite, versioned artifacts and setup guide.
- [ ] Updated threat model, cost estimate, maintenance/rollback runbook and reviewer actions.
- [ ] Zero claim that cloud, MQTT or ordinary ROS 2 is a certified safety path.

**If behind at month 30:** use one provider, one allowlisted telemetry schema and ≥3 virtual identities. Preserve local safety independence, least privilege, stale/offline behavior and P13 update recovery; defer second provider, complex digital twins, custom PKI/HSM, ML analytics and production-scale SRE.

---

## 4. Cross-track evidence matrix — the capstone must be testable

| Evidence area | Industrial A | Field B | IoT C |
|---|---|---|---|
| Requirements | part/cycle/quality envelope | benign cargo/inspection/terrain envelope | fleet/health/telemetry envelope |
| Architecture | robot + PLC + cell interfaces | robot + operator + local control + comms | robot + bridge + identities + broker |
| Baseline | cycle time / quality | route/endurance/recovery | ingestion/dashboard/identity |
| Fault injection | stuck I/O, missed ack, blocked restart | lost link/GNSS, stale sensor, low energy | WAN/broker loss, revoked ID, bad OTA |
| Repeated metrics | cycle/false reject/recovery | task success/drift/repair/endurance | latency/staleness/update/failures |
| Independent boundary | cell protective measures outside simulated PLC demo | local stop/operator and lawful permitted testing | local safety independent of Internet |
| Domain reviewer | automation/controls + qualified safety as needed | field/mechatronics + compliance as needed | cloud/security + controls for OT gateway |
| Claims prohibited | production safety PL/SIL or site certification | defense qualification, formal rugged certification | production PKI security or safety-rated cloud control |

### Shared P12 evidence checklist

- [ ] Requirements traceability: requirement → method → predeclared pass criterion → evidence.
- [ ] Architecture diagram and interfaces; versioned platform/toolchain.
- [ ] Explicit operator, safety, site/legal and public/non-controlled boundaries.
- [ ] Baseline and repeated experiments, not one edited highlight video.
- [ ] Normal state, fault state, restart/recovery state and regression results.
- [ ] Numerical metrics with units, uncertainty or sampling limitations as appropriate.
- [ ] Resource budget and operating/maintenance runbook.
- [ ] Reviewer findings, decisions and re-run evidence.
- [ ] Another person can reproduce the safe simulation without undocumented accounts.
- [ ] Portfolio statement accurately says **simulated**, **bench-tested** or **supervised physical**.

### Shared repository template

```text
stage-06-specialization/
├── README.md                       # one track, bounded use case, how to run
├── docs/
│   ├── requirements.md
│   ├── operating_envelope.md
│   ├── hazard_log.md
│   ├── architecture.md
│   ├── interfaces.md
│   ├── verification_matrix.md
│   ├── standards_scope.md         # literacy only, verify current/applicable issue
│   ├── budget_and_limits.md
│   └── test_report.md
├── cad/                            # if relevant
├── electronics/                    # if relevant; safe scope only
├── firmware/                       # if relevant
├── ros2_ws/src/
├── simulation/
├── plc_or_fleet/                    # selected track assets
├── configs/                        # versioned, no secrets
├── tests/
├── data/README.md                  # source, consent, controlled-data rules
├── review/                         # questions, reviewer actions and re-tests
└── .github/workflows/              # ordinary software CI ≠ safety certification
```

## 5. External review and mentorship calendar

| When | Who to seek | What to ask; evidence |
|---|---|---|
| Month 23–24 | selected-domain practitioner | Is the use case bounded? Which assumption is silently wrong? |
| Month 26 | industrial controls / field reliability / cloud security reviewer | Check interface, stop/failure and domain model before expansion |
| Month 29–30 | domain peer + someone outside project | Challenge verification criteria and failure cases before capstone lock |
| Month 33–34 | two reviewers if possible | One domain specialist and one mechatronics/software/security peer |
| Month 35–36 | independent reproducer | Clone, launch, provoke allowed fault and interpret logs without author help |

**Industrial physical safety** requires qualified reviewers and site procedures, not merely a helpful mentor. **Defense-adjacent documents** must remain public and non-controlled in any open review. No reviewer response is guaranteed; record review requests and perform independent test checks while waiting.

## 6. Costs, facilities and simulation-only substitutions

**Incremental September 2026 planning bands, USD, not vendor quotes:** exclude PC, tuition, labor, formal certification, site access, calibrated test facilities and commercial licenses. Include shipping/taxes/FX variations and roughly **15–25% purchase contingency**. Purchase only for the next passing gate.

| Track | Typical incremental budget | Optional purchases / access | Simulation-only substitute | What remains unproven |
|---|---:|---|---|---|
| A Industrial | **$100–700** | supervised PLC trainer, low-energy I/O fixture, vendor lab access | virtual PLC + cell simulation + OPC UA mock gateway | fieldbus electrical behavior, real commissioning, PL/SIL |
| B Rugged field | **$150–1,000** | benign enclosure/connectors, extra sensor, safe indoor rover, spare low-voltage supplies | Gazebo, synthetic GNSS/link/weather faults, energy model | environmental/RF qualification, representative long trials |
| C IoT/IIoT | **$0–350** typical lab spend, cloud variable | 1–3 SBC/MCU/gateway/secure-element dev boards | 3–10 virtual identities + local broker/dashboard + simulated OTA | production root of trust, fleet-scale PKI/SRE |

**Optional shared P11 hardware** belongs to Stages 02–04 and should not be counted twice. Cloud fees can grow with messages/storage; use billing alerts, quotas and cleanup. Do not substitute improvised hardware for necessary protections or claim formal qualification from an educational simulator.

## 7. Relevant named credentials — optional, not substitutes for gates

**Specific program names below are examples from the roadmap's certificate/career extension; verify provider, issuance type, eligibility, current exam/edition and local access before paying. A course-completion certificate is not necessarily a proctored professional credential.** No credential is a Stage 06 hard dependency.

| Track | Examples of *named* credentials/training | When to consider |
|---|---|---|
| A | Siemens **SITRAIN — TIA Portal Programming 1** (vendor training); **Ignition Core Certification**; chosen robot vendor programming course | After selecting actual PLC, SCADA and robot ecosystem |
| B | **INCOSE ASEP**; **ASQ Certified Reliability Engineer (CRE)** when eligible; **Esri ArcGIS Pro Associate** only for GIS-heavy chosen project | If requirements/reliability/GIS is part of target role; check experience prerequisites |
| C | **AWS Certified Cloud Practitioner**, **Microsoft Certified: Azure Fundamentals (AZ-900)**, **AWS Certified Developer – Associate** if AWS selected; **Ignition Core Certification** for IIoT/SCADA integration | Choose *one* cloud family first; P13 matters more than accumulating cloud basics |

## 8. Stage 05 optional-math triggers during Stage 06

| Observed block | Pull Stage 05 module | Do **not** do |
|---|---|---|
| Near-singular industrial arm IK | M02 pseudoinverse/SVD | full SLAM course |
| Unexplained industrial axis oscillation | M01 frequency-domain control | MPC by default |
| Field localization ambiguity beyond P08 baseline | M05 particles/factors; M03 for custom 3D poses only | rebuild entire SLAM stack unprompted |
| Dynamic payload invalidates simplified motor sizing | M08 rigid-body dynamics | learn all robotics dynamics proofs |
| IoT fleet telemetry not updating | **First debug schema, identity, QoS, timestamps, networking** | assume advanced robotics math will fix IoT |

## 9. If behind schedule: the month-30 decision

```text
P11 not stable? → Stop; repair the shared core.
P11 stable, specialization work late?
    ├─ A: one virtual cell + PLC handshake + recovery → finish P12-A.
    ├─ B: one benign indoor inspection/logistics route + local stop → finish P12-B.
    └─ C: one platform + ≥3 identities + offline safety + OTA → finish P13/P12-C.

Never compress away the test/review window to add another platform.
```

- [ ] Re-scope the use case to one measurable task and one primary interface.
- [ ] Freeze versions and log a short acceptance plan with nonnegotiable stop/fault checks.
- [ ] Defer second specialization, second planner and optional advanced math.
- [ ] If physical access is the blocker, finish the **simulation-only** capstone and label it accurately.
- [ ] Move the final date if the acceptance gate is not passed; do not relabel orientation as proficiency.

## 10. Official/public reference points (reverify before real work)

**Robotics and industrial:** [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/), [Gazebo](https://gazebosim.org/docs/harmonic/ros_installation/), [ros2_control](https://control.ros.org/), [ISO catalog](https://www.iso.org/), [Siemens SITRAIN](https://www.siemens.com/sitrain), [Inductive University](https://inductiveuniversity.com/).

**Rugged-field public literacy:** [DLA ASSIST / Quick Search](https://quicksearch.dla.mil/), [NATO STO public publications](https://publications.sto.nato.int/), [DoD system-safety resources](https://www.cto.mil/sea/sse/), [DDTC](https://www.pmddtc.state.gov/), [BIS EAR](https://www.bis.gov/regulations/ear). Public references do **not** authorize classified/controlled work or meet contracts.

**IoT/IIoT:** [MQTT 5.0 standard](https://www.oasis-open.org/standard/mqtt-v5-0-os/), [CoAP RFC 7252](https://www.rfc-editor.org/rfc/rfc7252), [OMG DDS](https://www.omg.org/omg-dds-portal/), [AWS IoT provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/iot-provision.html), [AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html), [Azure IoT DPS](https://learn.microsoft.com/azure/iot-dps/), [ThingsBoard](https://thingsboard.io/docs/).

**Final definition of done:** one safe, bounded specialization capstone with traceable requirements, repeated measurements, failed-case tests, outside critique, truthful limitations and independent reproduction. For track C, that includes P13 as a meaningful fleet-integration gate—not merely a dashboard screenshot.
