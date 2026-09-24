# Complete Robotics Engineering Roadmap

**From mechanics and mathematics to embedded electronics, software, AI, industrial automation, rugged field robotics, and IoT/IIoT integration**  
**Prepared:** September 2026  
**Format:** self-study curriculum, build plan, and portfolio checklist  
**Suggested horizon:** **30–36 months at 12–18 focused hours/week** for working full-stack competence plus proficiency in ONE chosen specialization: industrial robotics, rugged-field/defense-adjacent robotics, or IoT/IIoT robotics integration. Combining two tracks at genuine proficiency depth typically extends the plan to roughly **40–48 months**; all three can require **48–60+ months** depending on prior experience and access. **24 months** remains a scoped core-plus-orientation option, not equal depth. At 6–8 hours/week, plan approximately 48–72+ months depending on prior experience, facilities and project setbacks. These are planning estimates, not certification or employment guarantees.

> **Scope:** The defense-oriented branch covers non-weaponized field systems, logistics, inspection, search and rescue, demining *survey and hazard mapping only*, communications reliability, and operation in harsh environments. It does not cover weapon integration, target selection, or autonomous engagement. **This boundary is unchanged throughout the roadmap.** Public standards are discussed only for engineering literacy; hobby/self-study work cannot substitute for controlled-program requirements, organizational authorization, export-control/legal review, security clearances, qualified test organizations, or formal certification. Industrial safety standards described below must **not** be assumed to certify defense or other excluded applications.

## Revision summary — September 2026

| What changed | Why it matters |
|---|---|
| Kept the **30–36-month proficiency plan**, 24-month orientation option, and E/W/P depth labels; clarified that proficiency in **two** specializations normally means ~40–48 months rather than compression | Protects depth, testing and review time as the roadmap expands. |
| Preserved the **just-in-time core math gates** and optional/as-needed return triggers | Prevents new IoT/field material from front-loading unrelated advanced math. |
| Deepened the **rugged-field/defense-adjacent track** within the exact existing non-weaponized boundary: logistics/resupply robotics, cargo handling, convoy-following concepts, GPS-denied navigation concepts, degraded communications, EMCON awareness, interoperability literacy, environmental qualification, safety and export-control awareness | Makes the track relevant to real non-weaponized field engineering without drifting into weapon integration, target selection or autonomous engagement. |
| Added public-reference literacy for **NATO NGVA / STANAG 4754**, **MIL-STD-810H**, **MIL-STD-882E**, and DoD unmanned-system safety guidance, with explicit "verify current issue and contract applicability" warnings | Public standards can guide vocabulary and test thinking, but a self-study project is not a defense qualification or certification program. |
| Added a full **IoT / Industrial IoT robotics integration specialization**: MQTT, CoAP, DDS/ROS 2 comparison, cloud IoT platforms, fleet provisioning, device identity, digital twins, telemetry, OTA, edge/cloud partitioning, MES/SCADA integration and fleet operations | Treats robots as managed fleet assets while preserving real-time and safety boundaries. |
| Added **P13 — Robot-to-IoT fleet integration** with evidence checklist, external review checkpoint and E/W/P target | Converts IoT knowledge into a reproducible, reviewable engineering gate instead of a cloud demo. |
| Changed Part D from two choices to **three specialization tracks**, with explicit two-track timeline extensions | Prevents learners from mistaking breadth across industrial + field + IoT for proficiency in all three. |
| Extended the feedback/mentorship checkpoints to cover RF/comms assumptions, rugged qualification claims, cloud identity/OTA and fleet security | Catches silent architecture and security errors before they become deployment habits. |
| Split specialization budget staging into industrial, rugged-field and IoT/IIoT bands, each with simulation-only substitutions | Makes cost and facility requirements visible before committing to a track. |
| Updated the target-job map for **Field Robotics Engineer** and added **IoT/Robotics Integration Engineer** | Connects the curriculum to clearer job outcomes. |
| Preserved recovery/triage guidance and added IoT/field-specific deferrals | New breadth does not weaken load-bearing fundamentals. |

**Depth labels used throughout:** **E — Exposure** = can explain and reproduce a guided example; **W — Working competence** = independently implement and debug a bounded task with evidence; **P — Focused proficiency** = design, integrate, fault-test, review and maintain a repeatable project within a stated envelope. **P is not licensed practice, safety certification, or mastery of every robotics subdiscipline.**

---

## 0. Destination: what a full-stack roboticist can do

A capable robotics engineer can turn a **mission requirement** into a tested mechatronic system:

```text
Requirement and hazard analysis
         ↓
Mechanical design and dynamics ───── Electrical power and sensing
         ↓                                  ↓
Actuators, transmission, structure ← Embedded control and firmware
         ↓                                  ↓
        Robot model ←────────────── ROS 2 / software architecture
         ↓                                  ↓
State estimation → planning → controls → perception / AI
         ↓
Simulation → bench tests → guarded field tests → operation and maintenance
```

**Exit portfolio:** (1) closed-loop motor/axis, (2) modeled and controlled 2-link arm, (3) ROS 2 mobile robot in simulation, (4) a real small low-energy robot, (5) **one** industrial, rugged-field/defense-adjacent, or IoT/IIoT specialization capstone, and (6) reproducible engineering documentation for each. IoT-primary learners additionally complete P13 at W→P depth; learners in the other tracks may keep P13 at E/W unless they extend the timeline.

### A practical prioritization

For a learner with mechanical engineering and Python/AI exposure, **do not restart mechanics or Python from zero**. Test out of familiar topics, then fill the main robotics gaps: linear algebra and rigid transforms, feedback control, embedded electronics, real-time C/C++, ROS 2, state estimation, and integration/safety. Reuse CAD, manufacturing, machine-design, and ML experience as leverage.

## 1. Dependency map — study in this order, but overlap the tracks

| Sequence | Knowledge layer | Unlocks | Evidence of mastery |
|---|---|---|---|
| 1 | Units, vectors, calculus, Python/C++ fundamentals | Models and numerical work | Plot a physical simulation with units and tests |
| 2 | Linear algebra, 3D geometry, mechanics | Frames, forward/inverse kinematics | Calculate and draw a 2-link arm pose |
| 3 | Circuits, MCU programming, sensors, motors | Real-world actuation | Encoder-based velocity measurement and motor drive |
| 4 | Differential equations and feedback control | Stable motion | Simulated/physical PID with measured response |
| 5 | ROS 2 and simulation | Distributed robot software | Robot description, transforms, topics, tests |
| 6 | Probability, estimation, perception | Reliable localization | Fuse noisy odometry and IMU in simulation |
| 7 | Motion planning and autonomy | Useful tasks | Navigate or manipulate while respecting constraints |
| 8 | Safety, verification, integration | Responsible deployment | Hazard log, stop behavior, regression tests |
| 9 | Industrial, rugged-field/defense-adjacent, **or IoT/IIoT** specialization | Domain-specific capability | Completed capstone with real measured results |

**Avoid this trap:** learning object detection and an LLM framework before learning how a robot senses, moves, stops, and recovers from failure.

---

# PART A — MATHEMATICS AND PHYSICS

## 2. Mathematics: core gates first, depth only when it is needed

**Rule:** study just enough mathematics to unlock the *next* verified hardware/software gate; revisit harder theory when a measured failure or chosen specialization demands it. Never postpone P04/P05 until you have completed a graduate-level math sequence. A topic may be **core eventually** without being **core now**.

### 2.1 Strict core path — order, minimum depth, and unlocks

| When needed | Core math: minimum you must do | Concrete proof / next gate | Do **not** front-load |
|---|---|---|---|
| P01 (months 1–2) | SI units, dimensions, algebra, trigonometry, radians, vectors, dot/cross product, basic derivatives and integrals | Unit-checked torque/speed calculation; derive velocity from position | Eigenvalue proofs, tensor calculus |
| P02–P03 (months 2–4) | Matrix multiplication/inverse, 2D–3D rotations, homogeneous transforms, frame conventions, `atan2`, chain rule, basic Jacobian | Compose `T_world_base · T_base_tool`, invert and verify; derive 2-link FK/IK/Jacobian | Lie algebra formalism, sophisticated numerical IK |
| P04–P05 (months 4–7) | First/second-order ODEs, simple motor/load models, sampling, discrete integration, feedback error, PI/PID, stability intuition | Simulate then tune a bounded motor controller and show sample-rate and saturation effects | LQR, MPC, robust control proofs |
| P06–P07 (months 7–12) | Frame composition, quaternion *usage and normalization*, interpolation, time/timestamp arithmetic, basic numerical errors | Explain and test every `tf2` edge and robot description; replay logged trajectories | Quaternion differential geometry, symbolic SE(3) theory |
| P08 (months 13–18) | Mean/variance, Gaussian model, covariance, conditional probability/Bayes idea, linear least squares, simple Kalman update, Jacobian linearization for EKF if chosen | Odometry/IMU estimate with drift, uncertainty and timestamp checks | Particle-filter derivations, stochastic-process theory |
| P09–P10 (months 18–22) | Graphs, priority queues, A*/Dijkstra, gradients/least squares only when calibration requires them, trajectory speed/acceleration bounds | Explain planner failure, constraints, and held-out perception error | Nonlinear constrained optimization proofs, sampling-based planner theory |
| P11–P12 (months 21–36) | Reuse relevant core mathematics for your **selected platform**; add only missing actuator, power, kinematic, uncertainty or reliability calculations | Requirements-to-test traceability, measured margins and failure analysis | Universal advanced-math completion checklist |

**Core success criterion:** derive a small model, implement it, check units and frame conventions, compare with data, explain assumptions, and write a test. The table is a *minimum unlock*, not a ban on going deeper when your project requires it.

### 2.2 Optional/as-needed mathematics — explicit return triggers

| Optional topic | Circle back only when… | Earliest sensible window | Small proof of usefulness |
|---|---|---|---|
| Eigenanalysis, Laplace/Bode beyond basic intuition | PID tuning or oscillations cannot be explained from time responses | Months 5–8 | Explain a resonance or stability margin |
| Pseudoinverse, SVD and numerical conditioning | Arm IK becomes redundant, near-singular, or calibration is ill-conditioned | Months 9–16 | Demonstrate a singularity and regularized solution |
| Lie groups/algebras (`SO(3)`, `SE(3)`, `exp/log`) | Implementing custom 3D estimation, optimization, or advanced manipulator kinematics; using `tf2` **does not require** the full formalism | Months 16–26+ | Derive/test pose perturbations with correct frames |
| Observability and full state-space/LQR | Encoder/IMU signals leave states ambiguous, or classical feedback cannot meet a specified target | Months 16–26+ | Show unobservable case or compare controllers |
| Stochastic processes, particle filters and factor graphs | Sensor fusion/SLAM needs a model beyond a basic KF/EKF or a proven package | Months 19–30+ | Recover from a deliberately degraded measurement |
| Nonlinear optimization / full SLAM derivations | Implementing a solver, calibration algorithm or research extension rather than integrating an existing one | Months 22–36+ | Quantify solver accuracy, runtime and failure mode |
| MPC, robust/adaptive/impedance control | Chosen manipulation/control capstone has hard constraints or contact/uncertain dynamics **not met** by simpler control | Months 26–36+ | Compare against tuned baseline and safe failure case |
| Advanced rigid-body dynamics and inertia tensors | Designing high-speed/manipulator joints or a dynamics model where simplified sizing fails | Months 17–30+ | Check a coupled model against measurements |

**Return protocol:** (1) state the actual integration problem, (2) try a simpler validated model/tool, (3) learn the *smallest* missing math topic, (4) prove benefit on logged or simulated data, (5) document the difference. Advanced theory may remain **E** within 36 months if it is irrelevant to your chosen track.

### 2.3 Essential equations to derive, not merely memorize

```text
Translational kinematics:    v = dx/dt,  a = dv/dt
Angular kinematics:          ω = dθ/dt,  α = dω/dt
Force and torque:            F = ma,  τ = r × F
Rotational dynamics:         τ = Iα   [fixed axis, simplified]
Electrical power:            P = VI
Mechanical power:            P = τω
Gear reduction (ideal):      ω_out = ω_in / G; τ_out = G τ_in
Robot rigid transform:       T = [ R  p ]
                                [ 0  1 ]
Planar diff-drive motion:    v = r(ω_R + ω_L)/2
                             ω = r(ω_R - ω_L)/b
PID:                         u(t) = Kp e(t) + Ki∫e(t)dt + Kd de(t)/dt
Linear state-space:          x_dot = Ax + Bu; y = Cx + Du
Bayesian filtering idea:     belief ∝ likelihood × prior
```

`G` is a dimensionless speed-reduction ratio; `r` is wheel radius; `b` is wheel-center separation. State sign conventions and assumptions. State-space and Bayes are *introduced* here, not required for P01.

### 2.4 How to learn mathematics efficiently

1. Solve 5–10 representative problems by hand **for the current gate**.
2. Implement the model with Python, NumPy, SciPy, SymPy and Matplotlib.
3. Compare against analytical results or measured data, with units and frame definitions.
4. Explain where the model breaks: friction, saturation, backlash, delay or noise.
5. Save one notebook, plot, failed-case test and short engineering note; request review at the checkpoints in §17.3.

**Recommended texts:** *Modern Robotics* (Lynch & Park), *Underactuated Robotics* (Tedrake), *Feedback Systems* (Åström & Murray); follow the *relevant chapter*, not the entire book before building.

## 3. Physics to pair with mathematics

- **Statics:** free-body diagrams, force balance, bending, shear, torsion, center of mass.
- **Dynamics:** rigid-body kinetics, inertia tensors, angular momentum, coupled link dynamics.
- **Friction/contact:** static vs kinetic friction, Coulomb/viscous friction, traction, slip, rolling resistance.
- **Electricity/magnetism:** DC circuits, inductance, back EMF, PWM, motor magnetic basics.
- **Thermal physics:** motor/driver heating, cooling, derating, enclosure heat paths.
- **Signals and waves:** sampling, aliasing, frequency response, basic filtering, EMC fundamentals.
- **Optics and sensing:** lenses, depth, illumination, camera calibration, lidar measurement basics.
- **Energy:** batteries, power budgets, duty cycles, losses and efficiency.

**Gate:** model torque and current required for a low-speed wheel robot on flat ground and a modest slope; state all simplifying assumptions.

---

# PART B — MECHANICS, HARDWARE AND ELECTRONICS

## 4. Mechanical engineering for robotics

### 4.1 CAD and design fundamentals

- Parametric part, subassembly, assembly, constraints and reference geometry.
- Tolerance stack-ups, GD&T basics, fits, bearing seats, shafts, keys and fasteners.
- DFM/DFA: 3D printing, machining, laser-cut plates, sheet metal, standard components.
- Material selection: stiffness, strength, density, corrosion, fatigue, temperature.
- FEA as a verification aid: loads, restraints, mesh convergence; check calculations by hand.
- Technical drawings, BOM, part numbering, revisions, maintenance access.

### 4.2 Mechanisms and transmissions

- Four-bar linkages, sliders, gear trains, planetary gearboxes, belts, chains, screws and harmonic drives.
- Backlash, compliance, efficiency, reflected inertia, torque and speed trade-offs.
- Bearings, coupling alignment, lubrication, seals and vibration.
- Differential-drive, Ackermann, skid-steer, tracked and omnidirectional locomotion — focus on kinematics and environmental trade-offs rather than assuming one is universally best.
- Arm links, joints, work envelopes, singularities, counterweights and end-effectors.

### 4.3 Design calculations

For **each joint or drive**, estimate: payload/load, lever arm, peak and continuous torque, acceleration, reduction ratio, operating speed, brake need, duty cycle, efficiency, motor heating, and structural factor of safety. Include start/stop, stall and credible failure loads; never size only from a nominal steady-state calculation.

**Mechanical project:** design a guarded tabletop 2-DOF arm or a small low-energy rover. Deliver CAD, drawings, BOM, motor-sizing sheet, assembly procedure and test results.

## 5. Electrical and electronic engineering

### Study sequence

1. Ohm’s law, Kirchhoff’s laws, resistance/capacitance/inductance, grounding and protection.
2. Multimeter, bench supply, oscilloscope/logic analyzer; safe probing.
3. Digital logic, pull-ups, debouncing, logic levels, ADC/DAC, PWM, interrupts.
4. Sensors: switches, encoders, potentiometers, Hall sensors, current and temperature sensors.
5. IMUs, cameras, lidar/depth sensing, range sensors, proximity and limit switches.
6. Actuators: brushed DC, BLDC, stepper, servo, pneumatics and hydraulics — selection criteria.
7. Drivers and power electronics: H-bridges, ESCs, motor-driver current limits, protective devices.
8. Battery chemistry fundamentals, BMS, fuse selection, connectors, wire gauge and power isolation.
9. Schematics, PCB basics, EMI/EMC, ESD and harness routing.
10. Industrial power and interfacing: 24 VDC conventions, isolation, relays/contactors and safety-rated interfaces.

**Do not** connect motors directly to GPIO. Use current-limited supplies, matched drivers, protective devices, guarded low-energy tests, and qualified supervision for hazardous power or machinery.

### Buses and interfaces

| Level | Interfaces | What to learn |
|---|---|---|
| Board | GPIO, PWM, ADC, I²C, SPI, UART | Timing, electrical limits, protocols |
| Vehicle/machine | CAN / CANopen, RS-485 / Modbus | Framing, faults, node addressing |
| Networked robotics | Ethernet, DDS/ROS 2, time synchronization | Discovery, QoS, latency, clock drift |
| Industrial automation | EtherCAT, PROFINET, OPC UA | Determinism, device states, diagnostics, interoperability |

**Electrical project:** encoder + motor driver + current measurement + MCU + separate emergency stop for a small safe test rig. Measure command, actual speed, current and temperature; document wiring and fault behavior.

## 6. Embedded systems and real-time control

- C and C++: pointers/references, memory layout, RAII, compile/link, debugging, tests.
- MCU architecture: GPIO, timers, PWM, ADC, DMA, interrupts, watchdogs, bootloaders.
- Bare metal vs RTOS; tasks, queues, priorities, deadlines, race conditions.
- Sampling: fixed-rate control loops, timestamping, latency/jitter and aliasing.
- State machines; start-up, calibration, enable, fault, safe-stop and recovery states.
- Firmware update strategy, configuration integrity, bounded memory and diagnostic logs.
- `micro-ROS` **after** ordinary MCU and ROS 2 fundamentals, when actually needed.

**Embedded gate:** run a periodic velocity controller, log loop timing, reject invalid sensor readings, and enter a safe state on lost commands. A software stop alone is not a substitute for a properly engineered independent safety function.

---

# PART C — ROBOTICS THEORY AND SOFTWARE

## 7. Core robotics theory

### 7.1 Kinematics

- Degrees of freedom; coordinate frames, Euler angles vs quaternions.
- Homogeneous transformations and transform chains.
- Forward kinematics and inverse kinematics (analytical and numerical).
- Differential kinematics: Jacobian, end-effector velocity, singularities.
- Mobile robot kinematics: differential, Ackermann and holonomic constraints.
- Workspace, joint limits, collision geometry and trajectory limits.

### 7.2 Dynamics

- Center of mass and inertia, Lagrangian and Newton–Euler approaches.
- Manipulator form: `M(q)q_ddot + C(q,q_dot)q_dot + g(q) + friction = τ`.
- Wheel traction, motor electromechanics, contact and impacts.
- Identification of uncertain parameters from experiments.

**Gate:** write forward kinematics, inverse kinematics and a Jacobian for a planar 2-link arm; then simulate a trajectory with joint limits.

## 8. Feedback control (non-negotiable)

| Level | Content | Verification |
|---|---|---|
| Foundations | Open vs closed loop; steady-state error; overshoot; settling time | Plot and interpret a step response |
| Classical | P/PI/PID, anti-windup, derivative filtering, feedforward | Tune a DC-motor velocity loop |
| Frequency domain | Laplace, poles/zeros, Bode, margins | Explain a stability problem |
| Digital | Discrete time, sample period, quantization, delay | Compare sample rates |
| State space | Controllability, observability, LQR introduction | Simulate state feedback |
| Estimation/control interface | Sensor delay, actuator saturation, fault response | Stop safely on stale data |
| Advanced | Robust/adaptive control, MPC, impedance/admittance | Optional capstone extension |

**Control project:** model a motor and mechanical load, select sample time, implement PID with limits and anti-windup, then compare simulation and measured response **when safely accessible** (otherwise label as simulation-only). Report rise/settle times, overshoot, steady-state error, noise and current if measurable. Request a motor-control/electrical review at month 6.

## 9. Software engineering foundation

| Skill | Required scope |
|---|---|
| Linux | shell, processes, permissions, serial devices, service logs |
| Python | NumPy, SciPy, typing, testing, data logging, plots |
| C++ | modern fundamentals, CMake, memory, threads, ROS 2 nodes |
| Git | branching, pull requests, tagged releases, reproducibility |
| Build/test | colcon, ament, pytest, gtest, static analysis |
| Middleware | ROS 2 interfaces, DDS basics, QoS, lifecycle, executor model |
| Runtime | deterministic cleanup, timeouts, watchdogs, fault handling |
| Data | rosbag2, timestamps, calibration files, experiment metadata |
| DevOps | containers, CI, artifact/version management; hardware-in-loop when ready |
| Cybersecurity | authentication, least privilege, signed updates, secrets, logging, threat models |

**Architectural separation:** embedded motor control and independent safety functions at the low-level; ROS 2 for coordination/perception/planning; dashboards/cloud for non-safety-critical observation. Do not put a critical stop function behind an Internet API or LLM.

## 10. ROS 2 and simulation learning ladder

For an **Ubuntu 24.04** workstation, a sensible reproducible starting stack is **ROS 2 Jazzy + a compatible modern Gazebo release**; check package compatibility before mixing versions. Avoid beginning with obsolete Gazebo Classic tutorials. Validate one stack before upgrading components.

```text
Ubuntu + Git + Python/C++
  → ROS 2 command-line tools and turtlesim
  → nodes/topics/services/actions/parameters
  → workspaces, packages, launch, logging, rosbag2
  → tf2 and time, URDF/Xacro, robot_state_publisher
  → RViz and Gazebo (compatible versions)
  → ros2_control + simulated joints/wheels
  → actual sensors and actuators
  → MoveIt 2 (arm) OR Nav2 (mobile robot)
  → diagnostics, reproducible deployment, tests
```

**Must-build ROS 2 mini-projects:**

1. Python talker/listener with custom interface and tests.
2. C++ node + parameters + service/action + launch file.
3. Publish a correct `tf2` transform tree for a small robot.
4. Create URDF/Xacro and visualize in RViz.
5. Spawn robot in Gazebo and command joints/wheels via `ros2_control`.
6. Record/replay bag and reproduce a bug.
7. Add a startup/stop state machine and stale-data handling.

**Gate:** a new user can clone your repository, follow one README, run your simulation, issue a command and observe logs/plots without guessing your environment. Request external `tf2`/architecture review near month 12 (§17.3).

## 11. Estimation, localization and perception

### Estimation and maps

- Sensor models, precision vs accuracy, calibration, timestamps.
- Encoder odometry and IMU bias/drift; complementary filters.
- Bayes filters, Kalman filter, EKF/UKF concepts, particle filters.
- Coordinate frame correctness, covariance and uncertainty propagation.
- Occupancy grids, mapping, SLAM concepts, loop closure and failure cases.
- GNSS fundamentals and its limitations; visual/lidar odometry for appropriate lawful contexts.

### Computer vision and ML

- OpenCV, camera intrinsics/extrinsics, distortion and hand–eye calibration.
- Geometric vision: contours, corners, features, optical flow, stereo/depth.
- Object/defect detection, segmentation and tracking for **inspection**, not weapon targeting.
- Dataset versioning, annotation policy, leakage, train/val/test splits.
- Model latency, compute/power budgets, uncertainty and out-of-distribution failures.
- Edge inference, profiling, fallback paths and human review.

**Gate:** quantify pose or classification quality on held-out data under changed lighting, occlusion and motion; log latency and failure modes. Review baseline, noise model, covariance and sensor timestamps with a peer near month 18.

## 12. Planning, autonomy and human supervision

- Task-level finite-state machines and behavior trees.
- Graph search and spatial planning: A*, Dijkstra, sampling-based methods (conceptually).
- Path vs trajectory: geometry, velocities, acceleration and jerk constraints.
- Collision checking, joint limits, keep-out zones and recovery behavior.
- Navigation: localization, costmaps, route planning, local control, obstacle avoidance.
- Manipulation: grasp constraints, pick/place planning, force/torque feedback basics.
- Human–robot interaction: clear operating modes, operator override, logs and escalation.
- LLMs/agents, if used: limited to high-level assistance, documentation, or task proposals with deterministic validators and human authorization; never the sole safety controller.

**Gate:** in simulation, a robot completes a safe task, handles a blocked route or failed grasp, and returns to a known state without unbounded retries.

---

# PART D — SPECIALIZATIONS: INDUSTRIAL, RUGGED-FIELD, AND IoT/IIoT

**Choose ONE primary track for the 30–36-month plan.** Treat the other two as **E — Exposure** unless they directly support the chosen capstone. Combining two tracks at real W→P depth usually moves the finish line to roughly **40–48 months**; trying to make all three simultaneous proficiency tracks defeats the roadmap's depth discipline. Industrial + IoT/IIoT is a natural connected-factory combination; rugged-field + IoT is useful for fleet health/remote diagnostics; either combination still requires separate domain evidence and review.

## 13. Industrial robotics branch

### Typical environments

Automotive assembly, packaging, glass manufacturing, machine tending, inspection, material handling, warehouses, food/consumer goods and collaborative workcells.

### 13.1 Industrial automation skills

- PLC fundamentals; IEC 61131-3 languages, ladder logic, structured text and state machines.
- HMI/SCADA, I/O mapping, fieldbus diagnostics, OPC UA and MES integration.
- Robot controller concepts: teach pendant, jog modes, frames, tool center point (TCP), payload, program recovery.
- Vendor-specific training **after** platform-independent robotics: ABB RobotStudio/RAPID, FANUC ROBOGUIDE/TP or KAREL, KUKA.WorkVisual/KRL, Universal Robots/PolyScope/URScript, depending on local equipment and lawful access.
- Integration: conveyors, machine vision, grippers, pneumatic valves, interlocks, traceability and quality signals.
- Throughput and OEE: cycle-time breakdown, bottleneck analysis, downtime classification, part quality and maintainability.
- Robot cell simulation, reach studies, takt-time analysis, virtual commissioning.

### 13.2 Safety and compliance literacy

- Risk assessment and risk reduction from concept through decommissioning.
- Guarding, interlocked access, safety-rated monitoring, safe speed, protective stop, emergency stop and lockout/tagout.
- Distinguish ordinary control from safety-rated control; understand PL/SIL concepts without claiming certification from a hobby project.
- Relevant references include **ISO 10218-1:2025** (industrial robots), **ISO 10218-2:2025** (industrial applications/cells), **ISO 12100:2010** (risk assessment), **ISO 13849-1:2023 / IEC 62061** (safety-related controls), **ISO/TS 15066** (collaborative applications), **ISO 3691-4:2023** (driverless industrial trucks), and **IEC 62443** (industrial cybersecurity). These editions were checked against the ISO public catalog in September 2026; **reverify editions, application scope, full licensed text, national adoption and local law before any real deployment**.
- **Important scope caveat:** ISO 10218-2 explicitly excludes military/defense, airborne, underwater and several other applications; it is not a general license or certification for those sectors.

### 13.3 Industrial depth plan — ONE chosen platform, months 23–36

| Period | Focus / minimum evidence | Target depth |
|---|---|---|
| Months 23–26 | IEC 61131-3 ladder/structured text, I/O list, simulation, interlock/fault state machine, robot frames/TCP, risk-assessment exercise | **W** in virtual PLC/sequence; **E** in vendor programming and safety engineering |
| Months 27–30 | Integrate simulated PLC-to-robot handshakes, one selected fieldbus/OPC UA interface at conceptual or lab level, inspect timeout/state recovery, run workcell design review | **W** integration, **E/W** fieldbus depending on access |
| Months 31–36 | Build/test virtual workcell capstone; instrument throughput and quality; add traceability, repeated fault injection, maintenance/commissioning dossier | **P** in this *bounded virtual workcell*, not across all industrial platforms |

**True industrial-site proficiency additionally needs** supervised access to real robot controllers and PLCs, plant networks, integrator/vendor training, field commissioning under site procedures, review by qualified safety specialists, applicable full standards and local legal requirements. A hobby virtual workcell cannot demonstrate a safety PL/SIL claim, deliver real fieldbus interoperability, or authorize an industrial cell for production.

**Industrial feedback gate:** get a controls/automation professional to review the I/O list and fault states before I2; have a qualified safety professional review the *method* and scope of the hazard assessment before physical cell work. A mentor review is not certification.

### Industrial project progression

| Project | Goal | Required evidence |
|---|---|---|
| I1: virtual robot cell | Simulated safe pick/place or inspection sequence | Robot/workcell model, states, trace |
| I2: PLC/robot handshaking | Sensor → request → action → complete/fault | Sequence diagram, timeout/fault tests |
| I3: vision inspection | Inspect known parts; route PASS/FAIL | Accuracy, false rejects, latency, traceability |
| I4: capstone | Simulated packaging/glass-part handling cell | CAD/layout, PLC logic, ROS 2 or vendor simulation, risk register, cycle time and recovery report |

**Industrial capstone suggestion:** a *glass manufacturing inspection and sorting cell*, first fully simulated and later tested on a guarded low-energy bench **only after qualified review and authorization**. Integrate part tracking, safe conveyor state, vision quality check, virtual robot pick/place, production dashboard, traceability and a documented fault-recovery procedure.

## 14. Rugged field and defense-adjacent robotics branch (non-weaponized)

> **Scope boundary — keep this exact:** this branch is limited to **logistics, inspection, remote sensing, search-and-rescue support, and survey/hazard mapping**. It **excludes weapon integration, target selection, and autonomous engagement**. None of the material below changes that boundary.

### Appropriate use cases

Logistics transport and resupply support, facility inspection, perimeter *equipment monitoring*, remote sensing, search-and-rescue support, disaster mapping, infrastructure assessment, cargo movement and hazardous-area **survey by trained teams**. Physical testing must be authorized and comply with applicable safety, radio, aviation, site, cybersecurity, export-control and organizational requirements.

### 14.1 Engineering emphasis

- Requirements engineering for rain/dust/vibration/temperature, payload, endurance, maintainability, transportability and recovery.
- Ingress protection, connector choice, strain relief, EMI/EMC, grounding, sealing, corrosion, vibration isolation and environmental qualification concepts.
- Power budgeting, BMS and derating; fault detection, isolation and recovery; degraded-mode operation.
- Sensor calibration under lighting, dust, fog, vibration and temperature; test rather than assume robustness.
- Communications: link health, latency, packet loss, coverage gaps, safe timeout, operator takeover and logs.
- Field service: modular replacement, diagnostics, spare parts, configuration control, operator procedures and maintenance intervals.
- Reliability engineering: FMEA/FMECA concepts, hazard logs, fault trees, redundancy *where justified*, acceptance tests and repair-time measurements.
- Information security: authenticated commands, least privilege, signed software, audit trails, key handling and incident response.
- Human supervision: explicit operating modes, manual override, clear authority boundaries and recovery from automation faults.

### 14.2 Military-adjacent logistics and resupply robotics — non-weaponized concepts only

Study these as **mobility, logistics and systems-integration problems**, not tactical or combat-autonomy problems:

- **UGV transport:** payload/center-of-gravity limits, slope/traction, braking, battery/fuel endurance, thermal load, cargo restraint and route accessibility.
- **Resupply workflow:** task request → route assignment → load verification → supervised transit → delivery confirmation → return/recovery.
- **Cargo handling:** benign pallet/tote handling, lift/tilt constraints, docking/alignment, payload identification and safe human handoff.
- **Leader/convoy following concepts:** relative localization, route replay, spacing policy, loss-of-leader behavior, independent obstacle stopping and operator takeover. Keep experiments in simulation or controlled benign environments; do not treat convoy following as permission for unsupervised public-road or tactical use.
- **Fleet readiness:** state-of-charge, maintenance status, fault codes, payload status, mission log, spares and recovery plans.

**Gate idea:** simulate a 2–4 vehicle logistics fleet where each rover carries a benign virtual payload, follows an assigned route, stops independently for obstacles, safely handles leader/link loss, and returns or waits for operator instruction.

### 14.3 Interoperability and public standards literacy

The goal is to learn *architecture and assurance vocabulary*, not to claim conformance.

| Public reference | What to learn conceptually | Self-study boundary |
|---|---|---|
| **NATO STANAG 4754 / AEP-4754 — NATO Generic Vehicle Architecture (NGVA) for Land Systems** | Modular vehicle electronics, standardized interfaces/data concepts, service-oriented integration and interoperability thinking for land platforms | Public NATO technical publications reference NGVA/STANAG 4754; obtain the current authorized standard and program-specific profiles only through proper organizational channels. Do not claim NGVA compliance from a hobby implementation. |
| **MIL-STD-882E, including current change status in ASSIST** | System-safety process: hazard identification, risk assessment, mitigation, tracking and lifecycle integration | Use public material to learn system-safety discipline. Contract/program tailoring and risk acceptance belong to the responsible organization and authorities. |
| **DoD Unmanned System Safety Engineering Precepts Guide** | Safety precepts for unmanned-system acquisition, human interaction, command/control failure and autonomy-related hazards | Educational reading only; it does not authorize fielding, testing or procurement activity. |
| Allied/agency test and interoperability guidance applicable to the actual program | Interface verification, configuration control, test evidence and acceptance processes | Real requirements are program-, nation-, classification- and contract-specific; never infer them from an online roadmap. |

**Standards rule:** verify revision, distribution statement, program applicability, national implementation and contract wording at the time of real work. Public excerpts and homemade interoperability tests are **not certification, acceptance, or authorization**.

### 14.4 Contested/degraded-environment engineering — resilience without tactical optimization

Keep this at the level of **safe degraded operation and robust civil/field engineering**:

- **GNSS/GPS-denied navigation concepts:** wheel/visual/lidar odometry, IMU dead reckoning, map-relative localization, fiducials/beacons where authorized, covariance growth and explicit "localization confidence too low" states.
- **Navigation integrity:** cross-check sensors, detect impossible jumps, log source health, reduce speed or stop when localization confidence violates the operating envelope.
- **Communications resilience basics:** local autonomy sufficient to enter a safe state, buffered telemetry, retry/backoff, multiple lawful communication paths where permitted, link-quality monitoring and store-and-forward logs.
- **Jamming/degradation awareness:** recognize that RF loss/interference may occur and design safe fallback behavior. Do **not** treat a self-study project as an anti-jam communications program or develop techniques intended to defeat authorized countermeasures.
- **EMCON awareness:** understand that some organizations impose emissions-control policies governing when radios, Wi-Fi, cellular, GNSS transmitters/receivers or other emitters may operate. A hobby learner should model "communications unavailable" states; actual EMCON rules are operationally controlled and organization-specific.
- **No cloud dependency for motion safety:** loss of Internet, fleet server or remote dashboard must not remove the robot's ability to stop, remain within local limits or accept authorized local override.

### 14.5 Ruggedization and environmental qualification literacy

**MIL-STD-810H** is a U.S. DoD environmental-engineering/test-method reference. Study it to understand environmental tailoring and test categories, **not** to label a hobby robot "MIL-STD-810 certified." Reverify the current issue/change notice in DLA ASSIST before any real program use.

Conceptual categories to understand:

- high/low temperature and temperature shock;
- rain, humidity, dust/sand and ingress-related stresses;
- vibration and mechanical shock;
- altitude/low pressure where relevant;
- solar radiation, salt fog or icing **only when relevant to the actual life-cycle environment**;
- combined environmental profiles and pre/post-test functional checks.

**Educational test discipline:** write the life-cycle environment first, select only relevant stresses, define instrumentation and acceptance criteria, run low-risk/simulation substitutes where proper facilities are unavailable, and document why your test is *representative* rather than claiming formal qualification.

### 14.6 Export-control, controlled-program and authorization awareness

Defense-adjacent robotics can involve controlled hardware, software, technical data or services. At a high level:

- U.S. **ITAR** (22 CFR 120–130) governs defense articles/services and the U.S. Munitions List under the Department of State/DDTC; **EAR** (15 CFR 730–774) administered by BIS covers many dual-use and other controlled items, software and technology.
- Classification depends on the **specific item, technical data, destination, end user, end use and transaction**. Do not assume a civilian-origin robot is uncontrolled simply because it has a benign use case.
- Do not upload controlled technical data, proprietary program material, export-controlled source code, drawings or test data to public repositories, public AI systems or open forums without organizational authorization.
- A self-learner cannot independently satisfy classified/controlled-program requirements. Real defense-sector work requires the employer/program's export-control process, security organization, need-to-know/access controls, contractual rules, legal/compliance review, required licenses/authorizations and any necessary personnel/facility clearances.
- This roadmap is engineering education, **not legal advice, export classification, a compliance determination, or authorization to perform defense work**.

### 14.7 Choose one platform after the shared core

| Platform | First safe educational project | Specialized theory |
|---|---|---|
| Ground rover | Small indoor inspection/logistics rover with manual override | traction, suspension, wheel odometry, local navigation, payload/endurance |
| Aerial simulation | Camera-based inspection mission in **simulation first** | flight dynamics, state estimation, battery/failsafe, PX4/Gazebo |
| Manipulator | Remote sample/cargo handling with benign objects | force/position control, grasp planning, teleoperation |
| Field sensor node | Stationary remote health/environment monitor | low-power electronics, sensor calibration, comms reliability |

**PX4** is an optional simulation track for lawful civilian inspection and field research. Learn aircraft-specific regulations and safety from qualified instructors before any real flight. Avoid jumping from virtual quadrotor control to unsupervised outdoor testing.

### 14.8 Rugged-field depth plan — ONE selected platform, months 23–36

| Period | Focus / minimum evidence | Target depth |
|---|---|---|
| Months 23–26 | Environmental requirements/life-cycle profile, payload/endurance model, FMEA, comms timeout, manual override, operating envelope, export/control-awareness note | **W** requirements/FMEA and supervised simulation; **E** formal qualification/interoperability |
| Months 27–30 | GNSS-degraded simulation, repeated comms-loss, sensor-drift and degraded-light/dust tests; serviceability review; quantify availability, localization confidence and battery margins | **W** fault-tolerant field prototype; **E/W** degraded navigation depending on evidence |
| Months 31–36 | Non-weaponized inspection/logistics capstone, logs, service plan, regression tests, benign guarded trials where authorized, public-reference standards mapping | **P** in one bounded low-energy use case; **E/W** formal environmental/interoperability frameworks |

**True rugged-field/defense-sector proficiency additionally needs** supervised representative environmental/RF testing, calibrated facilities, long-duration reliability data, qualified EMC/RF/safety review, secure configuration control, program-specific interface standards, site permissions and the organization's security/export/legal processes. **Do not confuse a DIY rain/dust demo, simulated RF loss, public STANAG reading or homemade test matrix with formal qualification, interoperability acceptance, security accreditation, or defense-program authorization.**

**Field feedback gate:** before P12, ask a field engineer/robotics mentor to challenge safe timeout, localization-confidence behavior, actual energy isolation, repairability, failure detection and environmental-test claims. For defense-adjacent career preparation, separately ask an experienced compliance/security professional to review only your *public, non-controlled* understanding of export/security boundaries—not program data.

### Field capstone suggestion

A **small, human-supervised inspection/logistics rover**: maps a permitted mock facility in simulation, transports a benign payload between marked stations, reports environmental/equipment readings, demonstrates GNSS-unavailable localization in simulation, handles communication loss by entering a documented safe state, and returns on operator request. For physical testing, use a low-energy indoor platform, soft boundaries and a separate power-isolation mechanism.

## 14A. IoT / Industrial IoT robotics integration branch

### Appropriate use cases

Fleet telemetry, robot health monitoring, predictive-maintenance data collection, remote diagnostics, asset/configuration inventory, non-real-time task coordination, digital twins, MES/SCADA integration and secure fleet software deployment. **IoT is not the robot's safety controller.**

### 14A.1 Messaging: MQTT, CoAP and ROS 2 / DDS serve different layers

| Technology | Best fit | Communication model | Strengths | Robotics caution |
|---|---|---|---|---|
| **MQTT 5.0** | Fleet/cloud telemetry and event distribution | Brokered publish/subscribe | Lightweight, simple topic hierarchy, retained/session features, broad cloud support | Broker/cloud path is not a deterministic motor-control or safety channel |
| **CoAP (RFC 7252)** | Constrained device REST-like telemetry/configuration | Request/response over constrained networks, with observe patterns available | Compact, maps well to resource-oriented constrained devices | Treat Internet/WAN latency and loss as normal; do not put critical stop/control behind it |
| **DDS / ROS 2 topics** | On-robot and local distributed robotics data exchange | Data-centric pub/sub with rich QoS | Real-time/embedded-oriented QoS, discovery, local robot software integration | Still requires proper architecture; ROS 2 traffic itself is not automatically safety-rated |
| **OPC UA / MQTT + Sparkplug-style models (optional)** | Plant/IIoT semantic integration | Client/server, pub/sub or industrial telemetry models | Asset models, tag semantics, SCADA/MES interoperability | Use plant-approved gateways/segmentation; do not bridge safety I/O casually |

**Mental model:** ROS 2/DDS coordinates the robot locally; MQTT/CoAP/industrial gateways expose selected non-critical state to fleet or plant systems. Bridge only explicit, versioned interfaces—never mirror the entire ROS graph to the cloud by default.

### 14A.2 Treat the robot as a managed IoT/IIoT asset

Design a telemetry contract rather than publishing arbitrary debug data:

```text
robot/<fleet>/<robot_id>/telemetry/health
robot/<fleet>/<robot_id>/telemetry/energy
robot/<fleet>/<robot_id>/telemetry/mission
robot/<fleet>/<robot_id>/events/fault
robot/<fleet>/<robot_id>/config/reported
robot/<fleet>/<robot_id>/ota/status
```

For each field define: schema/version, units, timestamp source, quality/status, update rate, retention, privacy/security classification and owner. Add correlation IDs so cloud events can be traced back to local rosbag/log evidence.

**Digital twin concepts:** desired vs reported configuration, software version, calibration version, capability inventory, health state, last-known non-safety mission state and maintenance counters. A cloud twin is an **operations representation**, not ground truth for instantaneous safety decisions.

### 14A.3 IoT platforms — learn one deeply, recognize the others

| Platform family | Concepts to practice | Depth target |
|---|---|---|
| **AWS IoT Core / Device Management** | X.509 device identity, policies, fleet provisioning/JITP concepts, MQTT topics, device shadows, fleet indexing/groups, Jobs/OTA rollout, logging | **W** if selected track |
| **Azure IoT Hub + DPS + Device Update** | Per-device identity, X.509/TPM/symmetric options, zero-touch provisioning, device twins, routing, groups/deployments and OTA | **E/W** unless selected instead of AWS |
| **ThingsBoard or similar self-hosted platform** | Device provisioning, telemetry, attributes, dashboards, rule chains, OTA/fleet management concepts | **E/W** and useful for low-cost/local labs |

Choose **one** platform for P13. The skill is the architecture: identity, provisioning, authorization, telemetry schema, fleet operations, update safety and observability—not memorizing one vendor console.

### 14A.4 Fleet identity, authentication and authorization

Single-robot firmware flashing is not fleet management. Learn:

- one logical identity per robot/device; avoid shared long-lived credentials across a fleet;
- X.509 certificates or equivalent hardware-backed identities where appropriate;
- manufacturing/onboarding/provisioning flow, ownership transfer and decommissioning;
- least-privilege topic/API policies; separate operator, service and device identities;
- certificate/key rotation, revocation and lost-device response;
- inventory of hardware revision, software image, calibration and configuration version;
- audit logs for who changed device configuration or initiated an update.

### 14A.5 OTA at fleet scale

A credible OTA design includes:

1. signed/verifiable artifacts;
2. compatibility metadata and preconditions;
3. staged/canary rollout rather than "all robots now";
4. rollout rate limits/maintenance windows;
5. health check after update;
6. automatic abort criteria when failure rate rises;
7. rollback or known-good recovery image where platform supports it;
8. update status per robot and immutable audit evidence;
9. local rule: an interrupted cloud update must not defeat the robot's independent safe-stop behavior.

**P13 does not require writing a bootloader.** It requires proving a *fleet update workflow* with a simulator/container or safe lab device and documenting how production hardware would establish root of trust and rollback.

### 14A.6 Edge vs cloud — explicit safety boundary

| Keep on robot / local edge | Suitable for cloud / enterprise layer |
|---|---|
| hard real-time motor/servo loops | fleet dashboards and historical analytics |
| independent emergency/protective stop chain | maintenance trends and utilization/OEE summaries |
| collision avoidance needed to remain within the local safety envelope | non-real-time route/task proposals subject to local validation |
| watchdogs, stale-command handling and bounded degraded mode | long-horizon optimization, reports and model training |
| essential localization/control needed to stop or recover safely | aggregate digital twin, configuration inventory and fleet health |
| local operator override and energy isolation | OTA orchestration, deployment tracking and audit logs |

> **Critical constraint:** safety-critical stop/control functions must **never depend on cloud/Internet connectivity**. Loss of cloud, DNS, broker, VPN or WAN must not prevent a robot from stopping, remaining within its locally enforced operating envelope, or accepting its authorized local override. IoT integration is for telemetry, fleet operations, coordination and **non-safety-critical observation/control only** unless a separately engineered, certified safety architecture explicitly says otherwise.

### 14A.7 Industry 4.0 / MES / SCADA integration

- Map robot health, cycle count, mission state, quality outcome and maintenance counters into plant-approved tags/events.
- Understand **OPC UA** as a common industrial integration layer and **ISA-95-style** separation between control and enterprise/MES concerns conceptually.
- Use gateways/network segmentation instead of exposing robot control networks directly to enterprise/cloud networks.
- Distinguish historian/analytics latency from control-loop latency.
- Build traceability: `work_order → robot/job ID → software/config version → quality result → event/log evidence`.
- For industrial robots, keep safety PLC/robot safety functions independent of IoT dashboards and cloud brokers.

### 14A.8 IoT/IIoT depth plan — months 23–36 when chosen as the primary specialization

| Period | Focus / minimum evidence | Target depth |
|---|---|---|
| Months 23–26 | MQTT/CoAP concepts, ROS 2 bridge boundary, telemetry schema, local broker, device identity/threat model, one simple dashboard | **W** telemetry pipeline; **E/W** IoT security |
| Months 27–30 | One cloud/self-hosted platform, provisioning, per-device auth, digital twin/device shadow, offline buffering, fleet grouping, MES/SCADA conceptual mapping | **W** secure bounded fleet integration |
| Months 31–36 | **P13**: staged OTA simulation, fleet dashboard, fault injection (broker/WAN loss, expired credential, bad update), audit trail, independent reproduction and external review | **P** in one bounded robot-fleet integration; **E/W** in enterprise-scale operations |

**True production IoT/IIoT proficiency additionally needs** production PKI/HSM or secure-element practices, enterprise IAM, network/security operations, cloud cost/quotas, privacy/data governance, production monitoring/SRE, staged deployment at scale, incident response, and plant/enterprise change-control. A dashboard plus MQTT demo is not fleet-security proficiency.

### 14A.9 P13 — Robot-to-IoT fleet integration gate

**Deliverable:** connect a simulated or real low-energy robot's **non-critical telemetry** to one IoT platform, represent at least three robot identities (real or simulated), build a fleet dashboard, and demonstrate provisioning/authentication plus a safe OTA/update workflow.

**Evidence checklist:**

- [ ] Architecture diagram clearly separates `safety/local control`, `ROS 2`, `edge bridge`, `IoT broker/platform`, and `dashboard/MES`.
- [ ] Versioned telemetry schema with units, timestamps, quality/status fields and topic/resource naming.
- [ ] Unique identity/credential per simulated robot; least-privilege authorization demonstrated.
- [ ] Provisioning/onboarding flow documented and repeatable.
- [ ] Dashboard shows health, energy/uptime, software/config version and fault state for ≥3 identities.
- [ ] Internet/broker loss test proves local control and safe-stop behavior continue independently.
- [ ] Buffered/replayed telemetry behavior is explicit; stale cloud state is visibly marked stale.
- [ ] OTA/update rollout uses a canary/group, verifies artifact/version, reports status, and demonstrates abort/rollback or a documented safe recovery strategy.
- [ ] Credential revocation/expiry failure is tested without silently falling back to anonymous access.
- [ ] Audit evidence links update/config action → robot identity → version → result.
- [ ] README allows another person to reproduce the fleet demo from source without hidden credentials.
- [ ] Security review notes list what remains unproven: hardware root of trust, production PKI, SRE scale, formal industrial cybersecurity assessment, etc.

**External review checkpoint:** have a cloud/IoT/security practitioner review identity, authorization, OTA rollback/abort, secret handling and offline behavior. If integrating with an industrial cell, separately ask a controls engineer to confirm that the gateway cannot bypass the local safety/control architecture. Review is not certification.

---

# PART E — QUALITY, SYSTEMS ENGINEERING, TESTING AND DEPLOYMENT

## 15. Full robot development lifecycle

1. **Mission/use case:** stakeholders, operating context, prohibited actions, success criteria.
2. **Requirements:** measurable load, speed, accuracy, uptime, range, environment, budget.
3. **Hazards:** people, stored energy, pinch points, runaway motion, electrical/thermal faults.
4. **Architecture:** subsystems, interfaces, timing, power, computational and safety boundaries.
5. **Models:** CAD, kinematics, dynamics, sensor errors, power, thermal, simulation.
6. **Design reviews:** trade-offs, requirements traceability, failure analysis and test coverage.
7. **Implementation:** software tests, component bench tests, wiring inspection, versioned firmware.
8. **Verification:** simulation, unit, integration, hardware-in-loop, guarded system tests.
9. **Validation:** representative user task and environment; quantified acceptance criteria.
10. **Operation:** maintenance, backups, calibration, incident review, change control.

### Verification matrix template

| Requirement | Test method | Pass criterion | Evidence |
|---|---|---|---|
| Robot follows commanded low speed | bench test | measured tolerance defined before test | CSV + plot |
| Stale commands stop motion | fault injection | stop within documented system-specific limit | event log |
| Power budget supports duty cycle | measured runtime | meets target with margin | measurements |
| Sensor reports uncertainty | repeatability study | calibrated error band | report |
| Task success | repeated scenario trials | agreed success threshold | video + logs |
| Stop/restart behavior | controlled test | returns to known state | test log |

**Production readiness is not the same as a working demo.** Never claim a robot is safe or certified solely because it passes a homemade checklist.

## 16. Robotics cybersecurity and deployment

- System inventory, trust boundaries and threat modeling.
- Secure configuration, patch and dependency management, access control and authenticated interfaces.
- Network segmentation for machine networks, least-privilege remote access and event logging.
- ROS 2 security concepts and DDS transport/security configuration where relevant.
- OTA/firmware rollback design and incident-response procedures; for fleets, add staged rollout, per-device identity, revocation, audit and rollback/abort criteria (§14A).
- Containers/CI for development and non-real-time workloads; verify timing on the actual target.
- Datasets and experiment reproducibility; git tags, config snapshots, calibration versioning.

---

# PART F — THE ACTUAL STUDY PLAN

## 17. Realistic learning schedule — 30–36 months for focused proficiency

**Assumptions:** approximately 12–18 focused hours/week, ~50 effective weeks/year. That is roughly **1,500–2,700 total study/build hours across 30–36 months** (planning range, not guaranteed output); component supply delays, debugging, reviewer availability and access to machines may extend it. Existing mechanics/CAD and Python competence can be used to deepen weak areas, **not** to skip measurement or safety gates. At 6–8 hours/week, expect a substantially longer path (roughly 48–72+ months).

**Outcomes by depth:** build **W** competence across core modeling, embedded, control, ROS 2, estimation and one planning mode; develop **P** in *one bounded chosen specialization/capstone*; keep secondary planning mode, advanced control, SLAM internals and unchosen specialization(s) at **E**.

### 17.1 Main 30–36-month schedule

| Months | Main focus | Project/gate evidence | Expected depth at exit |
|---|---|---|---|
| 1–3 | Skills audit, just-in-time core math, Linux/Git, numeric Python/C++, units, frames and 2-link kinematics | P01–P03: calculations, tested transforms and CAD visualizer; first outside geometry review | **W** simple models; **E/W** C++ |
| 4–6 | Basic circuits, MCU, encoder, driver and power isolation; motor ODEs, PID and sampling | P04–P05: bench or simulated closed-loop axis, timing, saturation, safe fault state; electrical review | **W** bounded low-energy axis; **E/W** embedded internals |
| 7–10 | Embedded timing/C++, ROS 2 nodes/launch/tests; `tf2`, URDF/Xacro, RViz, Gazebo | P06 and partial P07: reproducible workspace and first correct robot model | **W** ROS 2 basics; **W** frame conventions |
| 11–14 | Complete P07, `ros2_control`, rosbag2, diagnostics, integration; one real or simulated interface | Robot launch, replay, timestamp and lost-command tests; month-12 external architecture review | **W** reproducible simulated robot |
| 15–18 | Sensor errors, calibration, covariance, odometry/IMU fusion, basic vision; fault-focused embedded reinforcement | P08, partial P10: logged drift/uncertainty/latency, baseline-vs-fusion test; month-18 review | **W** bounded estimation; **E** SLAM internals |
| 19–22 | **One** planning path: Nav2 mobile **OR** MoveIt 2 manipulation; complete P09/P10; integrate P11 | Failed-route/grasp recovery, held-out perception results and a low-energy robot **or full simulation** | **W** chosen planning mode; **E** other mode |
| 23–26 | **Choose ONE primary specialization: industrial, rugged-field/defense-adjacent, or IoT/IIoT**; learn domain architecture, constraints and orientation build | I1/I2, field reliability/logistics mini-project, or IoT local telemetry/provisioning mini-project; domain review | **W** domain fundamentals; **E** formal qualification/enterprise scale |
| 27–30 | Selected specialization in depth: domain integration, supervised benign tests where possible, measurement and capstone design | Reviewed architecture, risk/FMEA or threat model, versioned acceptance plan and integration tests | **W→P** in one bounded problem |
| 31–36 | Specialization capstone + fault injection + redesign + outside review. IoT-primary learners complete **P13** here; industrial/field learners may add P13 only at **E/W** if it does not displace P12 testing | Independent reproduction and predeclared acceptance evidence; final portfolio | **P** bounded chosen capstone; **not** professional certification |

**Specialization is not two months:** months **23–36** contain 14 months of domain learning, implementation, revision and capstone effort. Use **months 31–36** as a protected integration/testing window; do not substitute a second specialization or new optional theory for completing and reviewing the chosen capstone.

### 17.2 Choosing one, combining two, or touching all three

| Goal | Honest planning horizon | Depth claim |
|---|---:|---|
| One primary track | **30–36 months** | **P** in one bounded capstone; other tracks **E** |
| Two tracks with real project evidence | **~40–48 months** | **P** in first; **W→P** in second depending on facility/access/review |
| All three with substantial evidence | **~48–60+ months** | Do not promise equal **P**; depth depends on real access and repeated testing |
| 24-month route | **24 months** | Core **W** + one specialization **orientation**, not specialization proficiency |

**Good combinations:** industrial + IoT/IIoT for connected factories; rugged-field + IoT for fleet health/remote diagnostics; industrial + rugged-field only if your target role truly spans both. Reuse common artifacts (identity, logs, requirements, test framework) but do **not** count one integration demo as two independent proficiency capstones.

### 17.3 Honest 24-month alternative — core proficiency + specialization orientation

This is a distinct, narrower outcome, **not** the first two years of the 36-month claims compressed into 24. Prioritize P01–P08 plus P09 **in one mode**; complete P10/P11 only to a manageable bounded scope; make the final specialization work an **orientation prototype** with explicit follow-on work, not a proficiency claim.

| By month | Proficiency / working-competence targets | Exposure-only or deferred |
|---|---|---|
| 6 | Simple models, motor/sensor rig or simulated equivalent, PID, stopping/fault logic (**W**) | RTOS internals, BLDC tuning, MPC, advanced dynamics (**E/defer**) |
| 12 | ROS 2 packages, `tf2`, URDF/Gazebo and repeatable simulation (**W**) | MoveIt 2/Nav2 internals, deep C++ concurrency (**E/defer**) |
| 18 | Basic calibration, encoder/IMU fusion, noise and drift evidence (**W**); perception pipeline (**E/W**) | Full SLAM, particle filters, advanced stochastic processes (**E/defer**) |
| 21 | **One** planner in a simulation scenario, failure recovery, baseline integration (**W**) | Other planner, research-grade optimization (**E/defer**) |
| 22–24 | Industrial virtual handshake **OR** field-rover fault/recovery **OR** IoT telemetry/auth orientation; documented demo and backlog (**W** for bounded demo, **E** for wider track) | Real factory commissioning, formal rugged qualification, production PKI/fleet operations, advanced capstone (**defer**) |

**A 24-month portfolio should say:** “I built and measured a bounded robotic system and completed an industrial/field/IoT *orientation project*.” It should **not** say: “I am proficient in industrial safety integration, defense-sector qualification, fleet security, rugged qualification, all autonomy techniques and multiple robot platforms.” To reach focused domain proficiency afterward, reserve roughly **another 6–12+ months** (often more with limited equipment access) for the selected track, external reviews and repeated capstone testing.

### 17.4 Weekly cadence + real outside feedback

| Activity | Hours/week at ~15 h | What to produce |
|---|---:|---|
| Just-in-time math and theory | 2 | derivation/units notebook for current gate |
| Software and embedded | 4 | tested code, timing or runtime evidence |
| CAD/electronics/simulation | 3 | model, schematic, harness or experiment |
| Project integration and fault testing | 4 | demonstrable increment and failure reproduction |
| Docs and review/mentorship | 2 | design note, issue, review request, action log |

**Every 4 weeks:** one demo, technical explanation, measured result, failure analysis and reviewable commit. Every 12 weeks, budget a *review and rework week*. Real external review may take longer; build slack into milestones rather than treating comments as optional.

| Checkpoint | What to ask a second person to review | Where / what to provide | Acceptance evidence |
|---|---|---|---|
| Month 3: P02–P03 | Frame naming, transform multiplication order, units, IK edge cases | Robotics mentor, university lab, ROS Discourse/Robotics Stack Exchange; share diagram + notebook + tests | At least one issue discussed and regression-tested; don't equate silence with approval |
| Month 6: P04–P05 | Power wiring/protection by a qualified person; sampling, anti-windup, unsafe fault paths | Makerspace/electronics mentor; share schematic, low-energy rig photos and step/stop logs | Updated wiring/test plan; no unsupervised hazardous-power testing |
| Month 12: P06–P07 | ROS package structure, frame tree, timestamps, QoS, reproducibility | ROS community, local ROS meetup, a small relevant open-source PR, or maintainer feedback | Independent clean build + reviewer issue/action log |
| Month 18: P08 | Noise model, covariance consistency, ground truth, drift and sensor timing | Estimation/controls practitioner or reproducible technical forum question | Failed cases and corrected comparison plot |
| Month 24: P11 + track choice | Interface contract, hazard assumptions, FMEA/risk-register or IoT threat-model method, track scope | Industrial controls mentor, field-engineering mentor, or IoT/security mentor; qualified review when required | Written scope limits and revised verification matrix |
| Months 27–30 | **Industrial:** I/O/fault states. **Field:** degraded-navigation/comms assumptions, environmental claims. **IoT:** device identity, authorization, offline behavior and OTA rollout | Relevant domain practitioner; share only public/non-controlled information | Reviewed architecture + issue/action log + re-run tests |
| Months 33–36: capstone / P13 | Fault-injection evidence, maintenance/recovery, independent reproduction; for P13, secrets/PKI boundaries and update rollback/abort | Two reviewers if possible: one domain specialist and one software/mechatronics/security peer | Addressed comments, re-run tests, independent setup and design handoff |

**How to get a useful review:** post *one narrowly reproducible question* with expected vs actual behavior, frame diagram, software versions, minimal code, logs, measured units, risk boundary and exact question. Contribute docs/tests or an appropriately scoped fix to a robotics open-source project; do not ask maintainers to review an entire unreduced capstone. Try university labs, professional societies, local makerspaces, ROS community events/forums or a paid hourly mentor. For defense-adjacent preparation, share **only public, non-controlled** information and follow the relevant organization's disclosure/export/security rules. Communities vary in availability; a review request is not a guarantee of response.

```text
Review request template
Project/gate + Git commit:
Expected behavior and units/frames:
Actual measurements and failure case:
Architecture/schematic/transform tree:
One or two precise questions:
Safety boundary: simulation / de-energized bench / supervised low-energy test
Information boundary: public/non-controlled only
Proposed fix and follow-up test:
```

### 17.5 If you're behind schedule — triage before compressing gates

**Rule:** cut optional breadth and capstone complexity before cutting units/frames, safe power, closed-loop behavior, timestamps, regression tests or the independent stop strategy. A missed gate moves later gates to the right; it does not become a completed gate by the calendar.

| At checkpoint | Load-bearing: preserve / repair now | Safe cuts or deferrals | Recovery action |
|---|---|---|---|
| Month 6 | Units, FK/frames, motor sizing, wiring safety, encoder/timing, bounded PID and fault behavior | Advanced C++, RTOS, extra actuator families, LQR/MPC and formal Lie theory | Drop physical build **in favor of simulation** if equipment is the blocker; finish P04/P05 evidence and review |
| Month 12 | Runnable ROS 2 nodes, tests, `tf2`, URDF, one simulator, rosbag2 and safe stale-command behavior | Fancy visualization, extra middleware, micro-ROS, Nav2+MoveIt dual-track, GPU vision | Freeze stack, simplify robot to 2-wheel model, spend 4–8 weeks on one clean P07 repository |
| Month 18 | Timestamps, sensor calibration, covariance/noise intuition, baseline vs fused state, measured drift | Full SLAM, UKF/particle filters, Lie derivations, learned perception, PX4 | Use logged/synthetic data and one simple filter; produce P08 with failure cases before planning |
| Month 24 | One planner, recovery behavior, P11 integration, hazard log and project reproducibility | Second planner, unchosen specializations, real industrial hardware, rugged qualification claims, production cloud fleet | Deliver a **24-month orientation** project, defer specialization proficiency and extend 6–12+ months |
| Month 30 — industrial | Interface/state model, timeout/fault behavior, risk-assessment method and capstone criteria | Second fieldbus, second vendor, advanced vision/AI | Reduce to one virtual workcell and protect commissioning/fault-test time |
| Month 30 — rugged field | Safe lost-link behavior, localization integrity, power/endurance model, FMEA and environmental assumptions | Formal STANAG implementation, multiple radios, exotic sensors, broad environmental matrix | Reduce to one indoor logistics/inspection route and simulation-based degraded-environment tests |
| Month 30 — IoT/IIoT | Unique identity, least privilege, telemetry contract, offline behavior, local safety independence and update recovery | Second cloud provider, complex digital-twin platform, ML analytics, custom PKI/HSM lab | Use one platform + ≥3 simulated devices; finish P13 security/fault evidence before features |

**Never cut:** operator override where appropriate, safe de-energization and supervised boundaries, hazard identification, legally required approvals, protective measures, information/export/security boundaries, or the difference between educational checks and qualified certification. If these cannot be met, stay in simulation or a de-energized setup.

## 18. Thirteen project/gates, in escalating order

- [ ] **P01 — Units and motor sizing:** derive gear ratio, torque, speed, current and thermal assumptions.
- [ ] **P02 — Coordinate frames:** simulate transforms and validate forward/inverse transformations.
- [ ] **P03 — 2-link arm:** CAD + FK/IK/Jacobian + visualizer.
- [ ] **P04 — Motor test rig:** encoder, MCU, logging, driver and safe power isolation.
- [ ] **P05 — PID axis:** compare modeled vs observed response including saturation.
- [ ] **P06 — ROS 2 workspace:** Python/C++ packages, nodes, tests, launch, rosbag2.
- [ ] **P07 — Robot simulation:** URDF/Xacro + Gazebo + `ros2_control` + RViz.
- [ ] **P08 — Sensor fusion:** odometry + IMU with error and drift plots.
- [ ] **P09 — Navigation/manipulation:** Nav2 mobile scenario or MoveIt 2 pick/place.
- [ ] **P10 — Perception:** calibrated inspection model or geometry pipeline; report error and latency.
- [ ] **P11 — Small integrated prototype:** low-energy robot with operator override, safe-stop, tests.
- [ ] **P12 — Specialization capstone:** virtual industrial workcell, non-weaponized rugged-field inspection/logistics system, **or** IoT/IIoT robot-fleet integration system, with safety/quality/security documentation.
- [ ] **P13 — Robot-to-IoT fleet integration:** **required for the IoT/IIoT primary track; optional E/W extension for industrial or field tracks.** Connect non-critical telemetry to one platform, provision ≥3 identities, build a fleet dashboard, prove cloud-loss independence, and demonstrate a staged OTA/update flow with auth/audit evidence (§14A.9).

**Gate labels:** P01–P08 are core; P09 chooses **one** planning mode; P10/P11 should be bounded and may remain simulation-only if equipment access is constrained. P12 is a **24-month orientation project** OR a **30–36-month chosen-track capstone**, never both under the same proficiency claim. P13 is **W→P** only when IoT/IIoT is the chosen specialization; otherwise it should remain **E/W** unless the learner extends the timeline. Attach external review notes at P03, P05, P07, P08, P12 and P13 when attempted.

### Standard project repository structure

```text
robot-project/
├── README.md                  # setup, architecture, operation, safety note
├── docs/
│   ├── requirements.md
│   ├── hazard_log.md
│   ├── design_calculations.md
│   ├── verification_matrix.md
│   └── test_report.md
├── cad/                       # neutral exports + source links
├── electronics/               # schematics, wiring, BOM
├── firmware/
├── ros2_ws/src/
├── simulation/
├── configs/                   # versioned calibration and params
├── data/README.md             # dataset provenance; avoid bulky commits
├── tests/
└── .github/workflows/         # software CI, not a safety certificate
```

## 19. Learning pathway by target job

| Target role | Depth required first | Then add |
|---|---|---|
| Mechanical Robotics Engineer | CAD, mechanism sizing, structural design, dynamics | kinematics, sensors, motor selection, commissioning |
| Embedded Robotics Engineer | C/C++, MCU, buses, motor controls, instrumentation | RTOS, ROS 2 bridge, reliability and security |
| Robotics Software Engineer | Linux, C++, Python, ROS 2, testing, transforms | planning, estimation, hardware integration |
| Controls Engineer | calculus, ODEs, linear systems, system ID, PID | LQR/MPC, real-time, actuators and safety |
| Perception/Autonomy Engineer | probability, geometry, CV, estimation, ROS 2 | SLAM, navigation, learned perception, deployment |
| Industrial Robot Integrator | PLC, robot controllers, cell design, safety | vision, MES/OPC UA, IIoT gateways, optimization, maintenance |
| Field Robotics Engineer | full-stack robotics, reliability, power, communication, sensor fusion | ruggedization, GNSS-degraded navigation, environmental test planning, FMEA, supervised logistics/inspection workflows, interoperability/export-security literacy |
| **IoT/Robotics Integration Engineer** | ROS 2 boundaries, networking, MQTT/CoAP, Linux, device identity, telemetry schemas | IoT platform, fleet provisioning, digital twins, OTA, cloud/edge architecture, MES/SCADA integration, observability/SRE |
| Robotics Systems Engineer | interfaces, requirements, test, hazard analysis | broad mechanical/electrical/software literacy plus one domain track |

**Breadth vs depth:** understand every column well enough to integrate and troubleshoot; become professionally deep in one or two columns. “All aspects” does not mean equal specialization in every discipline.

## 20. Equipment and software acquisition — staged with budgets

**Planning costs in USD, September 2026 estimates, NOT live vendor quotes.** Ranges are intentionally broad; local availability, taxes, shipping, exchange rates, university access, quality, batteries, tools, sensors, cloud usage and replacement parts vary. They exclude an already-owned PC, tuition, labor, commercial licenses, real factory/defense-program access and formal certification. Buy only after the earlier gate passes; allow roughly **15–25% contingency** on purchases. A simulation-first learner can complete many gates for **$0 incremental hardware cost** with a suitable existing computer.

| Stage / gate | Software or access | Incremental purchase estimate (USD) | Physical items *only if needed* | Tight-budget substitution |
|---|---|---:|---|---|
| 0: P01–P03, math/CAD | Ubuntu, Python, Git, FreeCAD/available CAD, NumPy/SciPy | **$0–60** | No robot hardware; optional notebook/USB storage | Existing PC + open courses/public simulation |
| 1: P04–P05, basic electronics | KiCad, serial plotting, firmware tools | **$70–250** | Multimeter, suitable low-voltage supply, MCU, small encoder motor, protected driver, fuses/connector kit and stop/isolation parts | Makerspace bench; motor model + recorded/virtual encoder; **never** replace safety measures with improvised wiring |
| 2: P06–P11, integrated small robot | ROS 2, Gazebo, `ros2_control`, OpenCV, Nav2 **or** MoveIt 2 | **$150–500** | Modest indoor chassis/2-DOF arm, compute if missing, IMU/range sensor, mounts, guarded low-energy power | **$0 hardware** extension using Gazebo + rosbag2 datasets; defer physical P11 explicitly |
| 3A: industrial track, months 23–36 | Open PLC simulator/free vendor trial where available, OPC UA tools, robot simulation | **$100–700** | Optional PLC trainer/I/O, 24 V lab interfaces, low-energy fixture/sensors **only with proper supervision** | Virtual PLC/robot handshake + simulated OPC UA/MES; borrow training cell access |
| 3B: rugged-field track, months 23–36 | ROS/Gazebo, logging/network emulation tools, public standards references | **$150–1,000** | Optional rugged connectors/enclosure parts, spare batteries, benign payload fixture, extra IMU/range sensor, environmental logging; proper test facilities extra | Simulate GNSS loss, packet loss, temperature/power limits and vibration inputs; do not fake formal environmental qualification |
| 3C: IoT/IIoT track, months 23–36 / P13 | Local MQTT broker, ThingsBoard/community stack or one cloud IoT platform; dashboard/DB tooling | **$0–350** typical learning spend, cloud usage variable | Optional 1–3 SBC/MCU devices, secure-element/dev boards, local gateway; the ≥3-device fleet can be virtual | Run 3–10 containerized/simulated robot identities locally; use platform free tiers/trials carefully; emulate OTA with signed/versioned software packages |
| 4: optional after gate, supervised lab | Paid training, specialty instrumentation, licensed tools or lab rental | **$0–1,500+** | Oscilloscope, higher-grade sensors, rugged test/EMC access, industrial safety hardware **only if necessary and qualified** | University/community lab; remain in simulation and label missing physical validation |

**Indicative cumulative totals:** shared stages 0–2: **$220–810** before contingency. Adding one specialization often puts the learning build around **$320–1,810** before optional professional lab/training costs; the rugged-field upper end can rise quickly with sensors and facilities. IoT cloud bills can remain near zero for small labs or grow materially with message volume, storage, dashboards and managed services—set budgets/alerts and delete idle resources. These are planning bands, not product bundles or vendor quotes.

**Simulation-only substitutions are legitimate learning evidence when labeled honestly:** virtual PLCs can prove state logic but not real fieldbus electrical behavior; GNSS/RF/environment emulation can prove software recovery but not rugged qualification; virtual IoT fleets can prove identity/topic/update logic but not hardware root-of-trust or production PKI operations.

**Purchasing rule:** buy for the next testable objective, not an imagined final robot. Check documentation, electrical ratings, protection, replaceability, regional support, cloud/service lock-in, spares and data/security requirements. Prefer one repeatable robot to a pile of unrelated sensors; purchase industrial safety hardware or specialized environmental/RF test equipment only from appropriate sources and with qualified design/test support.

---

# PART G — STUDY RESOURCES AND REFERENCE MATERIAL

## 21. Primary official documentation and open courses

Access dates and compatibility change; inspect each project's **versioned** documentation before copying installation commands.

### Mathematics, mechanics, controls

- [Modern Robotics (Northwestern University)](https://modernrobotics.northwestern.edu/) — transformations, kinematics, dynamics, planning and control; textbook/courses.
- [MIT Underactuated Robotics](https://underactuated.mit.edu/) — modeling, nonlinear systems and advanced control.
- [Feedback Systems by Åström & Murray](https://fbsbook.org/) — open text on feedback/control.
- [MIT OpenCourseWare](https://ocw.mit.edu/) — linear algebra, calculus, mechanics and control courses.
- [SciPy](https://docs.scipy.org/doc/scipy/) and [NumPy](https://numpy.org/doc/) — numerical implementation.

### ROS 2, simulation and robot software

- [ROS 2 Jazzy documentation](https://docs.ros.org/en/jazzy/) — versioned docs, installation and tutorials; Jazzy targets Ubuntu 24.04. Check support before changing distro.
- [ROS 2 tutorials](https://docs.ros.org/en/jazzy/Tutorials.html) — work through in order.
- [Gazebo / ROS compatibility guidance](https://gazebosim.org/docs/harmonic/ros_installation/) — for Ubuntu 24.04 + ROS 2 Jazzy use the verified Jazzy/Harmonic pairing; recheck before installing newer releases.
- [MoveIt 2 documentation](https://moveit.picknik.ai/) — manipulation and planning.
- [Nav2 documentation](https://docs.nav2.org/) — mobile robotics.
- [ros2_control](https://control.ros.org/) — hardware interfaces, controllers, real/sim integration.
- [micro-ROS](https://micro.ros.org/) — optional MCU integration after embedded foundations.
- [OpenCV](https://docs.opencv.org/) — image processing and calibration.
- [PX4 user guide: ROS 2](https://docs.px4.io/main/en/ros2/user_guide) — **simulation-first lawful civilian flight research only**, check platform/version compatibility.

### Industrial automation and safety reference points

- [ISO 10218-1:2025 — industrial robots](https://www.iso.org/standard/73933.html).
- [ISO 10218-2:2025 — applications and cells](https://www.iso.org/standard/73934.html).
- [ISO 12100:2010 — machine risk assessment](https://www.iso.org/standard/51528.html); [ISO 13849-1:2023 — safety-related controls](https://www.iso.org/standard/73481.html).
- [ISO 3691-4:2023 — driverless industrial trucks](https://www.iso.org/standard/83545.html). As of September 2026, an edition-3 draft is under development; verify the status before an actual project.
- Vendor academies and documentation for the exact controller and machine installed at the relevant site.

### Rugged-field / defense-adjacent public reference points

- [NATO STO publications referencing STANAG 4754 / AEP-4754 NGVA](https://publications.sto.nato.int/) — use public documents for architecture literacy; obtain controlled/current program standards through authorized channels.
- [DLA ASSIST / Quick Search](https://quicksearch.dla.mil/) — authoritative U.S. defense-standard status lookup; recheck **MIL-STD-810H** and **MIL-STD-882E** issue/change status at time of use.
- [DoD System Safety Engineering resources](https://www.cto.mil/sea/sse/) — MIL-STD-882E and public unmanned-system safety-engineering guidance.
- [DDTC / ITAR information](https://www.pmddtc.state.gov/) and [BIS EAR](https://www.bis.gov/regulations/ear) — export-control awareness only; use organizational/legal compliance processes for any real classification or authorization.

### IoT / IIoT references

- [OASIS MQTT 5.0](https://www.oasis-open.org/standard/mqtt-v5-0-os/) — lightweight brokered publish/subscribe standard used widely in IoT.
- [IETF RFC 7252 — CoAP](https://www.rfc-editor.org/rfc/rfc7252) — constrained application protocol.
- [OMG DDS](https://www.omg.org/omg-dds-portal/) — data-centric real-time/embedded publish-subscribe middleware underlying common ROS 2 deployments.
- [AWS IoT Core device provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/iot-provision.html) and [AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) — fleet onboarding and remote-operation/update concepts.
- [Azure IoT Hub Device Provisioning Service](https://learn.microsoft.com/azure/iot-dps/) and [Device Update for IoT Hub](https://learn.microsoft.com/azure/iot-hub-device-update/) — fleet provisioning and OTA concepts.
- [ThingsBoard documentation](https://thingsboard.io/docs/) — self-hosted/open-source-friendly telemetry, dashboards, device management and OTA learning path.

**Standards reminder:** reverify all standard editions and scope at each real design/commissioning decision; a standard's title or online preview is not a substitute for a licensed full text, national implementation, local rules, a competent risk assessment or qualified commissioning. A homemade test suite or mentor review is **not** third-party certification or a legal approval.

---

# PART H — FIRST 30 DAYS: START HERE

## Week 1 — benchmark and setup

- [ ] Write a one-page goal: industrial cell, inspection/logistics rover, IoT-connected robot fleet, or general full-stack robotics.
- [ ] Assess calculus, vectors, mechanics, Python and C++; mark strong/weak topics.
- [ ] Establish Ubuntu development environment; pick **one compatible** ROS 2/Gazebo pair.
- [ ] Create Git repository and notebook template with SI units and plotted results.
- [ ] Make a simple units/motor-sizing notebook.

## Week 2 — coordinate geometry

- [ ] Revisit matrix multiplication, dot/cross products and trig.
- [ ] Derive rotation/translation transforms in 2D and 3D.
- [ ] Implement forward kinematics for a planar two-link arm.
- [ ] Visualize joint angles, link positions and reachable workspace.

## Week 3 — closed-loop thinking

- [ ] Study ODEs, mass–spring–damper and simple DC-motor models.
- [ ] Simulate P, PI and PID; compare tracking/error and saturation.
- [ ] Make plots with units and test variations in load and measurement noise.
- [ ] Write a short comparison of model assumptions and limitations.

## Week 4 — first ROS 2 integration

- [ ] Complete foundational ROS 2 CLI and Python node tutorials.
- [ ] Publish/subscribe command and measured-state messages.
- [ ] Add a timeout and basic node tests.
- [ ] Package Week 2–4 work as **Project 01: a simulated servo/robotics foundation**.

### First-month definition of done

You can explain `T_world_base`, derive motor torque from a simple load, simulate a feedback controller, and run **introductory** tested ROS 2 nodes. This is an *exposure-level preview* of ROS 2; P06/P07 working competence still belongs to months 7–14. Everything is versioned, plotted, documented and reproducible.

---

## 22. Quarterly self-assessment rubric

Score each dimension with **evidence**, not confidence: 0 = not attempted; 1 = explanation only; 2 = working model; 3 = tested integrated implementation. This is a personal learning tracker, **not** a safety or professional certification.

| Dimension | Evidence to attach |
|---|---|
| Mathematics and mechanics | derivation + simulation + units |
| Electronics and firmware | wiring, logs and fault test |
| Control systems | response plots and discussion |
| ROS 2/software | reproducible launch and automated tests |
| Perception/estimation | dataset, calibration and uncertainty |
| Integration and safety | requirements, hazard log and stop test |
| Specialization | real/simulated industrial, rugged-field, or IoT/IIoT test scenario with explicit depth label |
| Communication | drawings, video and concise report |

## 23. Final readiness checklist

- [ ] Can I explain all coordinate frames and units in my system?
- [ ] Can I independently estimate torque, current and thermal demands?
- [ ] Can I show measured behavior rather than just simulation claims?
- [ ] Can I debug a sensor, a wire, firmware, ROS 2 and a planner separately?
- [ ] Can I explain what happens when power, a sensor, local network, cloud/broker or communication link fails?
- [ ] Can another person reproduce my builds from source and instructions?
- [ ] Have I tested credible faults with an appropriate safe setup?
- [ ] Can I explain the limits of my robot and of applicable standards?
- [ ] Does my capstone solve a clear industrial, non-weaponized field/logistics, or IoT/IIoT robotics problem?
- [ ] If I used cloud/IoT, can the robot still stop and remain locally safe with the Internet completely disconnected?
- [ ] If I studied defense-adjacent systems, did I keep all work inside the non-weaponized boundary and avoid any claim that self-study replaces export/security/program authorization?

**North-star outcome:** not “I completed ROS 2,” but **“I can design, model, build, instrument, test, integrate, and communicate a robotic system that performs a well-defined task reliably within a defined safe operating envelope.”**
